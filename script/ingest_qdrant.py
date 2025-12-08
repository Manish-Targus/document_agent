# scripts/ingest_qdrant.py
from __future__ import annotations
import os, re, json, argparse, hashlib
from pathlib import Path
from typing import Dict, List, Tuple
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct

from llama_parse import LlamaParse
import requests
import yaml


# ----------------------- Embeddings (NIM) -----------------------
def nim_embed(texts: List[str], model: str, base_url: str, api_key: str) -> List[List[float]]:
    url = f"{base_url}/embeddings"
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"input": texts, "model": model}
    r = requests.post(url, headers=headers, json=payload, timeout=300)
    r.raise_for_status()
    data = r.json()
    return [d["embedding"] for d in data["data"]]


# ----------------------- Parsing helpers -----------------------
def load_md(md_path: Path) -> Tuple[Dict, str]:
    txt = md_path.read_text(encoding="utf-8", errors="ignore")
    if txt.strip().startswith("---"):
        parts = txt.split("---", 2)
        if len(parts) >= 3:
            fm_raw = parts[1]
            body = parts[2]
            try:
                fm = yaml.safe_load(fm_raw) or {}
            except Exception:
                fm = {}
            return fm, body.strip()
    return {}, txt


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
    return out


def detect_scope(front: Dict, body: str) -> str:
    dts = (front.get("doc_types") or [])
    if "tech_deck" in dts: return "tech_deck"
    for t in ["NIT","RFP","SBD","GCC","ITB"]:
        if t in dts: return "tender"
    t = body.lower()
    if any(k in t for k in ["tender","nit","emd","epbg","gem","bid"]): return "tender"
    return "tech_deck"


def parse_with_llamaparse(api_key: str, pdf_path: Path) -> str:
    instruction = os.getenv(
        "LLAMAPARSE_INSTRUCTION",
        "Keep slide titles, bullet points, and code blocks. Ignore watermarks, lorem, and CSS debris."
    )
    parser = LlamaParse(api_key=api_key, result_type="markdown", parsing_instruction=instruction)
    docs = parser.load_data([str(pdf_path)])
    parts = [getattr(d, "text", None) for d in (docs or []) if getattr(d, "text", None)]
    return "\n\n".join(parts).strip()


# ----------------------- Qdrant helpers -----------------------
def create_or_get_collection(client: QdrantClient, name: str, dim: int, vectors_key: str = "text_vector"):
    try:
        client.get_collection(collection_name=name)
        return
    except Exception:
        pass
    client.recreate_collection(
        collection_name=name,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )


def make_id(*parts: str) -> str:
    return hashlib.md5(("||".join(parts)).encode("utf-8")).hexdigest()


def upsert_points(client: QdrantClient, collection: str, rows: List[Dict], vectors_key: str = "text_vector"):
    if not rows: return
    pts = [
        PointStruct(
            id=r["id"],
            vector={vectors_key: r["vector"]},
            payload=r["payload"]
        ) for r in rows
    ]
    client.upsert(collection_name=collection, points=pts)


# ----------------------- main -----------------------
def main():
    load_dotenv()
    ap = argparse.ArgumentParser(description="Ingest PDFs/MD into Qdrant with LlamaParse + NIM embeddings")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--pdf", nargs="+", help="One or more PDF files to parse and ingest")
    g.add_argument("--md", nargs="+", help="One or more Markdown files (already parsed) to ingest")
    ap.add_argument("--scope", default="", help="Override scope (tender|tech_deck|hr|finance|sales|management)")
    ap.add_argument("--collection", default="", help="Override collection name explicitly (bypass prefix+scope)")
    ap.add_argument("--store-text", action="store_true", help="Also save chunk text into payload (bigger payloads)")
    args = ap.parse_args()

    llama_key = os.getenv("LLAMAPARSE_API_KEY")
    if args.pdf and not llama_key:
        raise SystemExit("Missing LLAMAPARSE_API_KEY for --pdf mode")

    nim_key   = os.getenv("NVIDIA_API_KEY")
    nim_base  = os.getenv("NIM_BASE_URL", "https://integrate.api.nvidia.com/v1")
    nim_model = os.getenv("NIM_EMBED_MODEL", "NV-Embed-QA-4")
    if not nim_key:
        raise SystemExit("Missing NVIDIA_API_KEY for embeddings")

    q_url   = os.getenv("QDRANT_URL", "http://localhost:6333")
    q_key   = os.getenv("QDRANT_API_KEY", "")
    prefix  = os.getenv("QDRANT_COLLECTION_PREFIX", "kb_")
    dim_env = int(os.getenv("EMBED_DIM", "0"))

    client = QdrantClient(url=q_url, api_key=q_key)

    # Probe dim if needed
    if dim_env <= 0:
        dim = len(nim_embed(["probe dim"], nim_model, nim_base, nim_key)[0])
    else:
        dim = dim_env

    # Decide collection name builder
    def choose_collection(scope_: str) -> str:
        if args.collection.strip():
            return args.collection.strip()
        return f"{prefix}{scope_}"

    per_collection_rows: Dict[str, List[Dict]] = {}

    # ---------- gather ----------
    if args.pdf:
        for pdf in args.pdf:
            p = Path(pdf)
            if not p.exists():
                print(f"Skip missing: {p}"); continue
            md_text = parse_with_llamaparse(llama_key, p)
            front = {"title": p.stem, "source_files": [p.name], "doc_types": []}
            scope = args.scope or detect_scope(front, md_text)
            collection = choose_collection(scope)
            chunks = iter_chunks(md_text)

            recs, texts = [], []
            for i, ch in enumerate(chunks):
                section_title = ""
                m = re.search(r"(?m)^\s*#{1,6}\s+(.*)", ch)
                if m: section_title = m.group(1).strip()[:240]
                rid = make_id(str(p), str(i), str(hash(ch)))
                payload = {
                    "scope": scope,
                    "title": front.get("title") or "",
                    "source_file": p.name,
                    "section_title": section_title,
                    "path": str(p.resolve()),
                    "front_matter": front
                }
                if args.store_text:
                    payload["text"] = ch
                recs.append({"id": rid, "text": ch, "payload": payload})
                texts.append(ch)
            vecs = nim_embed(texts, nim_model, nim_base, nim_key)
            for r, v in zip(recs, vecs):
                r["vector"] = v
            per_collection_rows.setdefault(collection, []).extend(recs)

    if args.md:
        for md in args.md:
            mpath = Path(md)
            if not mpath.exists():
                print(f"Skip missing: {mpath}"); continue
            front, body = load_md(mpath)
            scope = args.scope or detect_scope(front, body)
            collection = choose_collection(scope)
            title = (front.get("title") or mpath.stem).strip()
            source_files = front.get("source_files") or [mpath.name]
            chunks = iter_chunks(body)

            recs, texts = [], []
            for i, ch in enumerate(chunks):
                section_title = ""
                m = re.search(r"(?m)^\s*#{1,6}\s+(.*)", ch)
                if m: section_title = m.group(1).strip()[:240]
                rid = make_id(str(mpath), str(i), str(hash(ch)))
                payload = {
                    "scope": scope,
                    "title": title,
                    "source_file": source_files[0] if source_files else mpath.name,
                    "section_title": section_title,
                    "path": str(mpath.resolve()),
                    "front_matter": front
                }
                if args.store_text:
                    payload["text"] = ch
                recs.append({"id": rid, "text": ch, "payload": payload})
                texts.append(ch)
            vecs = nim_embed(texts, nim_model, nim_base, nim_key)
            for r, v in zip(recs, vecs):
                r["vector"] = v
            per_collection_rows.setdefault(collection, []).extend(recs)

    # ---------- upsert ----------
    for collection, rows in per_collection_rows.items():
        create_or_get_collection(client, collection, dim)
        upsert_points(client, collection, rows)
        print(f"Indexed {len(rows)} chunks into Qdrant collection: {collection} (dim={dim})")


if __name__ == "__main__":
    main()