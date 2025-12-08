# scripts/search_qdrant.py
from __future__ import annotations
import os, json, argparse
from dotenv import load_dotenv
from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

import requests


def nim_embed(qs: List[str], model: str, base_url: str, api_key: str) -> List[List[float]]:
    url = f"{base_url}/embeddings"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"input": qs, "model": model}
    r = requests.post(url, headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    data = r.json()
    return [d["embedding"] for d in data["data"]]


def route_scope(q: str) -> str:
    ql = q.lower()
    if any(x in ql for x in ["bid","tender","emd","epbg","nit","gem"]): return "tender"
    elif any(x in ql for x in ["policy","holiday","recruit","salary","hr"]): return "hr"
    elif any(x in ql for x in ["invoice","po","ledger","finance"]): return "finance"
    elif any(x in ql for x in ["kpi","pipeline","lead","sales"]): return "sales"
    elif any(x in ql for x in ["board","okr","ceo","mgmt","management"]): return "management"
    return "tech_deck"


def main():
    load_dotenv()
    ap = argparse.ArgumentParser(description="Semantic search over Qdrant (NIM embeddings)")
    ap.add_argument("--q", required=True, help="user query")
    ap.add_argument("--scope", default="auto", help="tender|tech_deck|hr|finance|sales|management|auto")
    ap.add_argument("--collection", default="", help="Explicit collection name (overrides prefix+scope)")
    ap.add_argument("--k", type=int, default=8)
    args = ap.parse_args()

    base_url  = os.getenv("NIM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    api_key   = os.getenv("NVIDIA_API_KEY")
    em_model  = os.getenv("NIM_EMBED_MODEL", "NV-Embed-QA-4")
    q_url     = os.getenv("QDRANT_URL", "http://localhost:6333")
    q_key     = os.getenv("QDRANT_API_KEY", "")
    prefix    = os.getenv("QDRANT_COLLECTION_PREFIX", "kb_")

    if not api_key:
        raise SystemExit("Missing NVIDIA_API_KEY")
    client = QdrantClient(url=q_url, api_key=q_key)

    # Choose collection
    if args.collection.strip():
        collection = args.collection.strip()
        scope = None
    else:
        scope = args.scope if args.scope != "auto" else route_scope(args.q)
        collection = f"{prefix}{scope}"

    qv = nim_embed([args.q], em_model, base_url, api_key)[0]

    flt = None
    if scope:
        flt = Filter(must=[FieldCondition(key="scope", match=MatchValue(value=scope))])

    res = client.search(
        collection_name=collection,
        query_vector=("text_vector", qv),
        limit=max(20, args.k),
        with_payload=True,
        score_threshold=None,
        query_filter=flt
    )

    out = []
    for p in res[:args.k]:
        pl = p.payload or {}
        out.append({
            "score": float(p.score),
            "collection": collection,
            "scope": pl.get("scope"),
            "title": pl.get("title"),
            "source_file": pl.get("source_file"),
            "section_title": pl.get("section_title"),
            "path": pl.get("path"),
            "front_matter": pl.get("front_matter"),
            "has_text": bool(pl.get("text"))
        })

    print(json.dumps({
        "query": args.q,
        "collection": collection,
        "scope": scope or "",
        "topk": args.k,
        "results": out
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
