from __future__ import annotations
import os, re, hashlib
from typing import List, Optional, Dict, Tuple

from fastapi import FastAPI, UploadFile, File, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
)
from qdrant_client.http.exceptions import UnexpectedResponse

from llama_parse import LlamaParse
import yaml

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA

del os.environ['NVIDIA_API_KEY']
load_dotenv()

app = FastAPI(title="Document Agent API")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# ---------- ENV ----------
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "").strip()
NIM_BASE_URL   = os.getenv("NIM_BASE_URL", "").strip()

EMBED_SINGLE = os.getenv("NIM_EMBED_MODEL", "").strip() or None
EMBED_QUERY  = os.getenv("NIM_EMBED_MODEL", "").strip() or None
EMBED_PASS   = os.getenv("NIM_EMBED_MODEL", "").strip() or None

CHAT_MODEL   = os.getenv("NIM_LLM_MODEL", "meta/llama3-70b-instruct").strip()

QDRANT_URL   = os.getenv("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", "")
COLL_PREFIX  = os.getenv("QDRANT_COLLECTION_PREFIX", "kb_")

LLAMAPARSE_API_KEY = os.getenv("LLAMAPARSE_API_KEY", "")
LLAMAPARSE_INSTRUCTION = os.getenv("LLAMAPARSE_INSTRUCTION", "Keep slide titles, bullet points, and code blocks. Ignore watermarks, lorem, and CSS debris.")

EMBED_DIM = int(os.getenv("EMBED_DIM","0"))
MAX_EMBED_TOKENS = int(os.getenv("MAX_EMBED_TOKENS", "7500"))
MAX_CHAT_TOKENS  = int(os.getenv("MAX_CHAT_TOKENS", "5500"))
CHARS_PER_TOKEN  = 4
MAX_EMBED_CHARS  = MAX_EMBED_TOKENS * CHARS_PER_TOKEN
MAX_CHAT_CHARS   = MAX_CHAT_TOKENS  * CHARS_PER_TOKEN
MAX_CTX_CHUNKS   = int(os.getenv("MAX_CTX_CHUNKS", "10"))

# ---------- Clients ----------
if not NVIDIA_API_KEY or not NVIDIA_API_KEY.startswith("nvapi-"):
    raise RuntimeError("NVIDIA_API_KEY missing/invalid (must start with 'nvapi-').")

qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

def _embedder_kwargs(model_name: str) -> dict:
    kw = {"model": model_name}
    if NIM_BASE_URL:
        kw["base_url"] = NIM_BASE_URL
    return kw

if EMBED_SINGLE:
    EMB_Q = NVIDIAEmbeddings(**_embedder_kwargs(EMBED_SINGLE))
    EMB_P = EMB_Q
else:
    EMB_Q = NVIDIAEmbeddings(**_embedder_kwargs(EMBED_QUERY or "nvidia/nv-embedqa-e5-v5-query"))
    EMB_P = NVIDIAEmbeddings(**_embedder_kwargs(EMBED_PASS  or "nvidia/nv-embedqa-e5-v5-passage"))

def make_chat() -> ChatNVIDIA:
    kw = {"model": CHAT_MODEL, "max_tokens": 2048, "temperature": 0.2}
    if NIM_BASE_URL:
        kw["base_url"] = NIM_BASE_URL
    return ChatNVIDIA(**kw)

# ---------- Utilities ----------
NAMED_VECTOR = "text_vector"
UNNAMED_VECTOR_COLLECTIONS: set[str] = set()

def approx_tokens(s: str) -> int:
    return max(1, len(s) // CHARS_PER_TOKEN)

def clamp_text_by_tokens(s: str, max_tokens: int) -> str:
    max_chars = max_tokens * CHARS_PER_TOKEN
    if len(s) <= max_chars:
        return s
    cut = s[:max_chars]
    last_para = cut.rfind("\n\n")
    if last_para > max_chars * 0.6:
        return cut[:last_para].strip()
    last_dot = cut.rfind(". ")
    if last_dot > max_chars * 0.6:
        return (cut[:last_dot+1]).strip()
    return cut.strip()

def ensure_collection_named(name: str, dim: int):
    qdrant.recreate_collection(
        collection_name=name,
        vectors_config={NAMED_VECTOR: VectorParams(size=dim, distance=Distance.COSINE)},
    )

def get_collection_vector_mode(name: str) -> str:
    try:
        info = qdrant.get_collection(collection_name=name)
        cfg = getattr(info, "config", None)
        if cfg and getattr(cfg, "params", None):
            vectors = getattr(cfg.params, "vectors", None)
            if isinstance(vectors, dict):
                return "named" if NAMED_VECTOR in vectors else "named_other"
            return "unnamed"
    except Exception:
        pass
    return "missing"

def ensure_collection_if_missing(name: str, dim: int):
    mode = get_collection_vector_mode(name)
    if mode == "missing":
        ensure_collection_named(name, dim)
    elif mode == "unnamed":
        UNNAMED_VECTOR_COLLECTIONS.add(name)

def make_id(*parts: str) -> str:
    return hashlib.md5(("||".join(parts)).encode("utf-8")).hexdigest()

def iter_chunks(md_text: str, target=900, overlap=120) -> List[str]:
    blocks = re.split(r"(?m)^(#{1,6}\s+.*)$", md_text)
    merged = []
    i = 0
    while i < len(blocks):
        if re.match(r"^#{1,6}\s+", blocks[i] or ""):
            head = blocks[i].strip()
            tail = (blocks[i+1] if i+1 < len(blocks) else "")
            merged.append((head + "\n" + tail).strip())
            i += 2
        else:
            if (blocks[i] or "").strip():
                merged.append(blocks[i].strip())
            i += 1

    chunks, buf = [], ""
    for b in merged:
        if len(buf) + len(b) <= target + overlap:
            buf = (buf + "\n\n" + b).strip()
        else:
            if buf: chunks.append(buf)
            buf = b
    if buf: chunks.append(buf)

    out=[]
    for c in chunks:
        if len(c) <= target*1.6:
            out.append(c); continue
        parts = re.split(r"\n\s*[-*•]\s+", c)
        cur = ""
        for p in parts:
            p = ("- " + p) if not p.strip().startswith("#") else p
            if len(cur)+len(p) < target*1.1:
                cur = (cur+"\n"+p).strip()
            else:
                if cur: out.append(cur)
                cur = p
        if cur: out.append(cur)

    hard_capped = [clamp_text_by_tokens(c, MAX_EMBED_TOKENS) for c in out]
    return [c for c in hard_capped if c.strip()]

def detect_scope(front: Dict, body: str) -> str:
    dts = (front.get("doc_types") or [])
    if "tech_deck" in dts: return "tech_deck"
    for t in ["NIT","RFP","SBD","GCC","ITB"]:
        if t in dts: return "tender"
    t = body.lower()
    if any(k in t for k in ["tender","nit","emd","epbg","gem","bid"]): return "tender"
    return "tech_deck"

def parse_with_llamaparse_bytes(pdf_bytes: bytes, filename: str) -> str:
    """Parse PDF bytes with LlamaParse, save raw and cleaned markdown."""
    if not LLAMAPARSE_API_KEY:
        raise RuntimeError("LLAMAPARSE_API_KEY missing")
    parser = LlamaParse(
        api_key=LLAMAPARSE_API_KEY, result_type="markdown",
        parsing_instruction=LLAMAPARSE_INSTRUCTION
    )
    tmp = f"./tmp_{make_id('upload', filename)}.pdf"
    with open(tmp, "wb") as f:
        f.write(pdf_bytes)
    docs = parser.load_data([tmp])
    parts = [getattr(d, "text", None) for d in (docs or []) if getattr(d, "text", None)]
    markdown_text = "\n\n".join(parts).strip()
    
    md_dir = os.path.join(os.path.dirname(__file__), "md_outputs")
    os.makedirs(md_dir, exist_ok=True)
    raw_path = os.path.join(md_dir, f"{make_id('raw', filename)}.md")
    with open(raw_path, "w", encoding="utf-8") as mf:
        mf.write(markdown_text)
    
    try:
        import sys, pathlib
        sys.path.append(os.path.join(os.path.dirname(__file__), "..", "script"))
        from md_parser import load_llamaparse_markdown as md_parser_load
        cleaned_md = md_parser_load(LLAMAPARSE_API_KEY, pathlib.Path(tmp))
        clean_path = os.path.join(md_dir, f"{make_id('clean', filename)}.md")
        with open(clean_path, "w", encoding="utf-8") as cf:
            cf.write(cleaned_md)
        print(f"✓ Saved cleaned markdown: {clean_path}", flush=True)
    except Exception as e:
        print(f"⚠ Could not clean markdown: {e}", flush=True)
    
    return markdown_text

def load_md_text(md_bytes: bytes) -> Tuple[Dict, str]:
    txt = md_bytes.decode("utf-8", errors="ignore")
    if txt.strip().startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1]; body = parts[2]
            try:
                fm = yaml.safe_load(fm_raw) or {}
            except Exception:
                fm = {}
            return fm, body.strip()
    return {}, txt

# ---------- Schemas ----------
class UploadResponse(BaseModel):
    collection: str
    count: int
    scope: str
    stored_text: bool
    vector_mode: str

class SearchItem(BaseModel):
    score: float
    collection: str
    scope: Optional[str]
    title: Optional[str]
    source_file: Optional[str]
    section_title: Optional[str]
    path: Optional[str]
    has_text: bool
    text_preview: Optional[str] = None

class SearchResponse(BaseModel):
    query: str
    collection: str
    scope: Optional[str]
    topk: int
    vector_mode: str
    results: List[SearchItem]

class ChatRequest(BaseModel):
    query: str
    k: int = 6
    scope: Optional[str] = None
    collection: Optional[str] = None

class ChatAnswer(BaseModel):
    answer: str
    citations: List[SearchItem]
    vector_mode: str

# ---------- Adaptive Qdrant helpers ----------
def upsert_adaptive(collection: str, points: List[PointStruct], vectors: List[List[float]]):
    try_named = [
        PointStruct(id=p.id, vector={NAMED_VECTOR: v}, payload=p.payload)
        for p, v in zip(points, vectors)
    ]
    try:
        qdrant.upsert(collection_name=collection, points=try_named)
        return "named"
    except UnexpectedResponse as e:
        if "vector name" in str(e):
            try_unnamed = [
                PointStruct(id=p.id, vector=v, payload=p.payload)
                for p, v in zip(points, vectors)
            ]
            qdrant.upsert(collection_name=collection, points=try_unnamed)
            UNNAMED_VECTOR_COLLECTIONS.add(collection)
            return "unnamed"
        raise

def search_adaptive(collection: str, qvec: List[float], limit: int, scope_filter: Optional[Filter]):
    use_unnamed = (collection in UNNAMED_VECTOR_COLLECTIONS) or (get_collection_vector_mode(collection) == "unnamed")
    if use_unnamed:
        return qdrant.search(
            collection_name=collection,
            query_vector=qvec,
            limit=limit,
            with_payload=True,
            score_threshold=None,
            query_filter=scope_filter
        ), "unnamed"
    else:
        return qdrant.search(
            collection_name=collection,
            query_vector=(NAMED_VECTOR, qvec),
            limit=limit,
            with_payload=True,
            score_threshold=None,
            query_filter=scope_filter
        ), "named"

# ---------- Routes ----------
@app.post("/upload", response_model=UploadResponse)
async def upload(
    files: List[UploadFile] = File(...),
    scope: Optional[str] = Form(None),
    collection: Optional[str] = Form(None),
    recreate: bool = Form(False)
):
    """Upload files - only sends CLEANED markdown chunks to Qdrant, always stores text"""
    global EMBED_DIM
    if EMBED_DIM <= 0:
        probe = EMB_Q.embed_query("probe dim")
        EMBED_DIM = len(probe)

    total_rows = 0
    used_scope = scope or ""
    used_collection = collection or ""
    points_per_collection: Dict[str, List[PointStruct]] = {}
    vectors_per_collection: Dict[str, List[List[float]]] = {}
    processed_filenames = []

    for uf in files:
        name = uf.filename or "upload"
        processed_filenames.append(name)
        data = await uf.read()
        ext = (name.rsplit(".",1)[-1] if "." in name else "").lower()

        if ext == "pdf":
            md_text = parse_with_llamaparse_bytes(data, name)
            front = {"title": name.rsplit(".",1)[0], "source_files": [name], "doc_types": []}
        else:
            front, md_text = load_md_text(data)

        this_scope = scope or detect_scope(front, md_text)
        used_scope = used_scope or this_scope
        coll = collection or (COLL_PREFIX + this_scope)
        used_collection = used_collection or coll

        if recreate:
            ensure_collection_named(coll, EMBED_DIM)
            if coll in UNNAMED_VECTOR_COLLECTIONS:
                UNNAMED_VECTOR_COLLECTIONS.discard(coll)
        else:
            ensure_collection_if_missing(coll, EMBED_DIM)

    # Process ONLY cleaned markdown
    mode_final = "named"
    md_dir = os.path.join(os.path.dirname(__file__), "md_outputs")
    
    for name in processed_filenames:
        clean_path = os.path.join(md_dir, f"{make_id('clean', name)}.md")
        if os.path.exists(clean_path):
            with open(clean_path, "r", encoding="utf-8") as cf:
                cleaned_md = cf.read().strip()
            
            if cleaned_md:
                chunks = iter_chunks(cleaned_md, target=1200, overlap=160)
                chunks = [clamp_text_by_tokens(c, MAX_EMBED_TOKENS) for c in chunks]
                chunks = [c for c in chunks if approx_tokens(c) <= MAX_EMBED_TOKENS]
                
                if chunks:
                    vectors = EMB_P.embed_documents(chunks)
                    pts: List[PointStruct] = []
                    
                    for i, ch in enumerate(chunks):
                        m = re.search(r"(?m)^\s*#{1,6}\s+(.*)", ch)
                        section_title = m.group(1).strip()[:240] if m else ""
                        pid = make_id(name, "clean", str(i))
                        payload = {
                            "scope": used_scope,
                            "title": name.rsplit(".",1)[0],
                            "source_file": name,
                            "section_title": section_title,
                            "path": f"upload://{name}",
                            "cleaned": True,
                            "text": ch  # Always store text
                        }
                        pts.append(PointStruct(id=pid, vector=[], payload=payload))
                    
                    points_per_collection.setdefault(used_collection, []).extend(pts)
                    vectors_per_collection.setdefault(used_collection, []).extend(vectors)
                    total_rows += len(pts)
                    print(f"✓ Chunked cleaned markdown: {name} → {len(pts)} chunks", flush=True)
    
    # Upsert all cleaned chunks
    for coll, pts in points_per_collection.items():
        mode = upsert_adaptive(coll, pts, vectors_per_collection[coll])
        if mode == "unnamed":
            mode_final = "unnamed"
        print(f"✓ Upserted {len(pts)} chunks to {coll}", flush=True)

    return UploadResponse(
        collection=used_collection or "",
        count=total_rows,
        scope=used_scope or "",
        stored_text=True,
        vector_mode=mode_final
    )

@app.get("/collections")
def get_collections():
    """List all Qdrant collections"""
    try:
        collections = qdrant.get_collections()
        return {"status": "success", "collections": [{"name": c.name, "points_count": getattr(c, 'points_count', 0)} for c in collections.collections]}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/collection/{collection_name}")
def get_collection_info(collection_name: str):
    """Get info about a specific collection"""
    try:
        info = qdrant.get_collection(collection_name=collection_name)
        return {"status": "success", "name": collection_name, "points_count": getattr(info, 'points_count', 0), "vectors_count": getattr(info, 'vectors_count', 0)}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/collection/{collection_name}")
def delete_collection(collection_name: str):
    """Delete a Qdrant collection"""
    try:
        qdrant.delete_collection(collection_name=collection_name)
        if collection_name in UNNAMED_VECTOR_COLLECTIONS:
            UNNAMED_VECTOR_COLLECTIONS.discard(collection_name)
        return {"status": "success", "message": f"Deleted '{collection_name}'"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/search", response_model=SearchResponse)
def search(
    q: str = Query(..., min_length=2),
    k: int = Query(8, ge=1, le=50),
    scope: Optional[str] = Query(None),
    collection: Optional[str] = Query(None)
):
    if not q.strip():
        raise RuntimeError("Empty query")

    if collection:
        coll = collection
        scope_filter = None
    else:
        sc = scope or "tech_deck"
        coll = COLL_PREFIX + sc
        scope_filter = Filter(must=[FieldCondition(key="scope", match=MatchValue(value=sc))])

    q_safe = clamp_text_by_tokens(q, MAX_EMBED_TOKENS)
    qv = EMB_Q.embed_query(q_safe)
    res, vmode = search_adaptive(coll, qv, max(20, k), scope_filter)

    items = []
    for p in res[:k]:
        pl = p.payload or {}
        items.append(SearchItem(
            score=float(p.score),
            collection=coll,
            scope=pl.get("scope"),
            title=pl.get("title"),
            source_file=pl.get("source_file"),
            section_title=pl.get("section_title"),
            path=pl.get("path"),
            has_text=bool(pl.get("text")),
            text_preview=(pl.get("text")[:300] + "…") if pl.get("text") else None
        ))

    return SearchResponse(query=q, collection=coll, scope=(scope or None), topk=k, vector_mode=vmode, results=items)

@app.post("/chat", response_model=ChatAnswer)
def chat(req: ChatRequest):
    if req.collection:
        coll = req.collection
        scope_filter = None
    else:
        sc = req.scope or "tech_deck"
        coll = COLL_PREFIX + sc
        scope_filter = Filter(must=[FieldCondition(key="scope", match=MatchValue(value=sc))])

    q_safe = clamp_text_by_tokens(req.query, MAX_EMBED_TOKENS)
    qv = EMB_Q.embed_query(q_safe)
    res, vmode = search_adaptive(coll, qv, max(20, req.k), scope_filter)

    print(f"\n🔍 CHAT - Query: '{req.query}' | Collection: {coll} | Retrieved: {len(res)} results", flush=True)

    hits = res[:req.k]
    contexts = []
    cite_items: List[SearchItem] = []
    for idx, p in enumerate(hits):
        pl = p.payload or {}
        print(f"  [{idx+1}] Score={p.score:.4f} | {pl.get('source_file')} | {pl.get('section_title', 'N/A')[:40]} | Cleaned={pl.get('cleaned', False)}", flush=True)
        chunk = pl.get("text") or pl.get("section_title") or ""
        chunk = clamp_text_by_tokens(chunk, MAX_CHAT_TOKENS // max(1, min(req.k, MAX_CTX_CHUNKS)))
        contexts.append(chunk)
        cite_items.append(SearchItem(
            score=float(p.score),
            collection=coll,
            scope=pl.get("scope"),
            title=pl.get("title"),
            source_file=pl.get("source_file"),
            section_title=pl.get("section_title"),
            path=pl.get("path"),
            has_text=bool(pl.get("text")),
            text_preview=(pl.get("text")[:300] + "…") if pl.get("text") else None
        ))

    context_joined = "\n\n---\n\n".join(contexts[:MAX_CTX_CHUNKS])
    context_joined = clamp_text_by_tokens(context_joined, MAX_CHAT_TOKENS)
    print(f"💬 Total context: {len(context_joined)} chars", flush=True)

    sys_prompt = (
        "You are a helpful enterprise assistant. "
        "Answer using ONLY the provided context. If the answer is not contained, say you don't find it. "
        "Be concise and cite key details that appear in the context."
    )
    user_msg = f"Question: {req.query}\n\nContext:\n{context_joined}"

    llm = make_chat()
    result = llm.invoke([
        {"role":"system","content":sys_prompt},
        {"role":"user","content":user_msg}
    ])

    return ChatAnswer(answer=result.content, citations=cite_items, vector_mode=vmode)
