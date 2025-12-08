import os, json, re
import requests
from typing import List, Dict, Any, Optional, Tuple

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NIM_BASE_URL = os.getenv("NIM_BASE_URL", "https://integrate.api.nvidia.com")
EMBED_MODEL = os.getenv("NIM_EMBED_MODEL", "nvidia/nv-embedqa-mistral-7b-v2")
RERANK_MODEL = os.getenv("NIM_RERANK_MODEL", "nvidia/nv-rerankqa-mistral-4b-v3")
LLM_MODEL = os.getenv("NIM_LLM_MODEL", "meta/llama-3.3-70b-instruct")

HEADERS = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json",
}

class NimClientError(RuntimeError): ...
def _check():
    if not NVIDIA_API_KEY:
        raise NimClientError("NVIDIA_API_KEY not set")

# ------- Embeddings (not strictly required here, but kept for completeness) -------
def nim_embed(texts: List[str]) -> List[List[float]]:
    _check()
    url = f"{NIM_BASE_URL}/v1/embeddings"
    payload = {"model": EMBED_MODEL, "input": texts}
    r = requests.post(url, headers=HEADERS, json=payload, timeout=120)
    if r.status_code != 200:
        raise NimClientError(f"Embed error {r.status_code}: {r.text[:500]}")
    data = r.json()
    vecs = [d["embedding"] for d in data.get("data", [])]
    if len(vecs) != len(texts):
        raise NimClientError("Embedding count mismatch")
    return vecs

# ------- Reranker -------
def nim_rerank(query: str, passages: List[str], top_k: int = 8) -> List[Tuple[int, float]]:
    _check()
    url = f"{NIM_BASE_URL}/v1/rerank"
    payload = {
        "model": RERANK_MODEL,
        "query": query,
        "documents": [{"text": p} for p in passages],
        "top_n": min(top_k, len(passages))
    }
    r = requests.post(url, headers=HEADERS, json=payload, timeout=120)
    if r.status_code != 200:
        raise NimClientError(f"Rerank error {r.status_code}: {r.text[:500]}")
    data = r.json()
    results = data.get("results", [])
    out = []
    for item in results:
        idx = item.get("index")
        score = float(item.get("relevance_score", item.get("score", 0.0)))
        if idx is not None:
            out.append((idx, score))
    out.sort(key=lambda x: x[1], reverse=True)
    return out[:top_k]

# ------- LLM structured extraction -------
def _sys_prompt_for(fields: List[str]) -> str:
    schema = {
        "type": "object",
        "properties": {k: {"type": "string"} for k in fields},
        "required": [],
    }
    return (
        "You are a precise information extractor for procurement and tech documents.\n"
        "Return ONLY a single JSON object that matches the JSON Schema provided.\n"
        "Use empty string for unknown fields. Do not invent values. Preserve numeric strings as written.\n"
        f"JSON Schema:\n{json.dumps(schema)}"
    )

def _user_prompt(snippets: List[str], fields: List[str]) -> str:
    joined = "\n---\n".join(snippets[:16])
    want = ", ".join(fields)
    return (
        f"Extract the following fields: {want}.\n"
        "Be strict and concise.\n\n"
        f"TEXT SNIPPETS:\n{joined}"
    )

def nim_llm_extract(snippets: List[str], fields: List[str]) -> Dict[str, str]:
    _check()
    url = f"{NIM_BASE_URL}/v1/chat/completions"
    messages = [
        {"role": "system", "content": _sys_prompt_for(fields)},
        {"role": "user", "content": _user_prompt(snippets, fields)},
    ]
    payload = {
        "model": LLM_MODEL,
        "messages": messages,
        "temperature": 0.0,
        "response_format": {"type": "json_object"}
    }
    r = requests.post(url, headers=HEADERS, json=payload, timeout=180)
    if r.status_code != 200:
        raise NimClientError(f"LLM error {r.status_code}: {r.text[:500]}")
    data = r.json()
    content = data["choices"][0]["message"]["content"].strip()
    try:
        return json.loads(content)
    except Exception:
        m = re.search(r"\{[\s\S]*\}", content)
        if m:
            return json.loads(m.group(0))
        raise NimClientError("LLM returned non-JSON content")

# ------- Snippet selection -------
def _windows(md_text: str, window_chars: int = 800) -> List[str]:
    paras = [p.strip() for p in re.split(r"\n{2,}", md_text) if p.strip()]
    win = []
    for p in paras:
        if len(p) <= window_chars:
            win.append(p)
        else:
            for i in range(0, len(p), window_chars):
                win.append(p[i:i+window_chars])
    return win or [md_text]

def select_snippets_for(query: str, md_text: str, top_k: int = 12) -> List[str]:
    windows = _windows(md_text, window_chars=800)
    ranking = nim_rerank(query, windows, top_k=min(top_k, len(windows)))
    idxs = [i for i,_ in ranking]
    return [windows[i] for i in idxs]

# ------- Public helpers used by md_parser -------
def extract_fields_with_nims(md_text: str) -> Dict[str, str]:
    queries = [
        "Earnest Money Deposit EMD amount INR value",
        "ePBG percentage and duration in months",
        "Bid closing date and time",
        "Bid opening date and time",
        "Tender No and Organisation",
        "Total quantity",
        "Validity days of bid or offer"
    ]
    fields = [
        "tender_no","organisation","emd_amount_inr","closing_datetime",
        "opening_datetime","validity_days","epbg_percentage","epbg_duration_months","total_quantity"
    ]
    snippets = []
    for q in queries:
        snippets.extend(select_snippets_for(q, md_text))
    # dedupe
    seen = set()
    uniq = []
    for s in snippets:
        if s not in seen:
            uniq.append(s); seen.add(s)
    return nim_llm_extract(uniq, fields)

def extract_specific_fields_with_nims(md_text: str, fields: List[str], custom_queries: Optional[List[str]] = None) -> Dict[str, str]:
    if not fields:
        return {}
    queries = custom_queries or [f"extract field: {', '.join(fields)}"]
    snippets = []
    for q in queries:
        snippets.extend(select_snippets_for(q, md_text))
    seen = set()
    uniq = []
    for s in snippets:
        if s not in seen:
            uniq.append(s); seen.add(s)
    return nim_llm_extract(uniq, fields)