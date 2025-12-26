from __future__ import annotations
import os, re, hashlib
from turtle import title
from typing import List, Optional, Dict, Tuple
from urllib import response
from datetime import datetime

from fastapi import FastAPI, UploadFile, File, Form, Query,Depends
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv 

from qdrant_client import QdrantClient
from qdrant_client.http.models import (
    Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
)
from qdrant_client.http.exceptions import UnexpectedResponse

from llama_parse import LlamaParse
from sqlalchemy import URL
import yaml
import pandas as pd
import tempfile
import time

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
import requests 
from server.bid_scrapper import capture_bids,get_direct_bids
import asyncio
from .database import init_db, get_session
from .models.user import User
from passlib.context import CryptContext

# del os.environ['NVIDIA_API_KEY']
load_dotenv(override=True)
app = FastAPI(title="Document Agent API")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

@app.on_event("startup")
async def on_startup():
    await init_db()
# @app.on_event("startup")
async def startup_event():
    # await so it completes before the app starts taking requests
    try:
        await capture_bids()
        print("✅ capture_bids() completed at startup", flush=True)
    except Exception as e:
        print(f"❌ capture_bids() failed at startup: {e}", flush=True)
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
MAX_CHAT_TOKENS  = int(os.getenv("MAX_CHAT_TOKENS", "4000"))
CHARS_PER_TOKEN  = 4
MAX_EMBED_CHARS  = MAX_EMBED_TOKENS * CHARS_PER_TOKEN
MAX_CHAT_CHARS   = MAX_CHAT_TOKENS  * CHARS_PER_TOKEN
MAX_CTX_CHUNKS   = int(os.getenv("MAX_CTX_CHUNKS", "10"))

# ---------- Clients ----------
if not NVIDIA_API_KEY or not NVIDIA_API_KEY.startswith("nvapi-"):
    raise RuntimeError("NVIDIA_API_KEY missing/invalid (must start with 'nvapi-').")

qdrant = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, timeout=60)

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
    kw = {"model": CHAT_MODEL, "max_tokens": 3000, "temperature": 0.2, "top_p": 0.95}
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
        from script.md_parser import load_llamaparse_markdown as md_parser_load
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

def clean_markdown(file_path: str) -> str:
    """Clean markdown file using md_parser's noise_clean_markdown."""
    try:
        import sys, pathlib
        # Ensure script dir is in path
        script_dir = os.path.join(os.path.dirname(__file__), "..", "script")
        if script_dir not in sys.path:
            sys.path.append(script_dir)
        
        from script.md_parser import noise_clean_markdown
        
        with open(file_path, "r", encoding="utf-8") as f:
            raw_md = f.read()
            
        cleaned = noise_clean_markdown(raw_md)
        
        md_dir = os.path.dirname(file_path)
        clean_filename = f"clean_{os.path.basename(file_path)}"
        clean_path = os.path.join(md_dir, clean_filename)
        
        with open(clean_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
            
        print(f"✓ Cleaned markdown saved to: {clean_path}", flush=True)
        return clean_path
    except Exception as e:
        print(f"⚠ Error cleaning markdown: {e}", flush=True)
        return file_path # Fallback to original if cleaning fails

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
    thinking: Optional[str] = None
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
@app.post("/register",response_model=User)
async def create_user(user_data: User, session: AsyncSession = Depends(get_session)):
    # 1. Check if user already exists
    statement = select(User).where(User.email == user_data.email)
    result = await session.exec(statement)
    if result.first():
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Hash the password before saving
    user_data.hashed_password = pwd_context.hash(user_data.hashed_password)
    
    # 3. Add to DB
    session.add(user_data)
    await session.commit()
    await session.refresh(user_data)
    return user_data
@app.post("/upload", response_model=UploadResponse)
async def upload(
    files: List[UploadFile] = File(...),
    scope: Optional[str] = Form(None),
    collection: Optional[str] = Form(None),
    recreate: bool = Form(False)
):
    """
    Upload files.
    - If 1 file: Process individually, extract metadata, ingest.
    - If >1 files: Consolidate into one MD, extract metadata from consolidated, ingest.
    """
    global EMBED_DIM
    if EMBED_DIM <= 0:
        probe = EMB_Q.embed_query("probe dim")
        EMBED_DIM = len(probe)

    total_rows = 0
    used_scope = scope or ("consolidated" if len(files) > 1 else "tech_deck")
    used_collection = collection or (COLL_PREFIX + used_scope)
    
    # Ensure collection exists
    if recreate:
        ensure_collection_named(used_collection, EMBED_DIM)
        if used_collection in UNNAMED_VECTOR_COLLECTIONS:
            UNNAMED_VECTOR_COLLECTIONS.discard(used_collection)
    else:
        ensure_collection_if_missing(used_collection, EMBED_DIM)

    # Helper to extract metadata
    def get_doc_md(name, md_text):
        try:
            import sys
            script_dir = os.path.join(os.path.dirname(__file__), "..", "script")
            if script_dir not in sys.path: sys.path.append(script_dir)
            from script.md_parser import analyze_text
            return analyze_text(name, md_text)
        except Exception as e:
            print(f"⚠ Metadata extraction failed: {e}", flush=True)
            return None

    # Logic branch: Process ALL files individually
    mode_final = "named"
    
    print(f"DEBUG: Processing {len(files)} files individually...", flush=True)

    for uf in files:
        name = uf.filename or "upload"
        data = await uf.read()
        ext = (name.rsplit(".",1)[-1] if "." in name else "").lower()
        
        print(f"DEBUG: Processing file {name}...", flush=True)
        
        if ext == "pdf":
            md_text = parse_with_llamaparse_bytes(data, name)
        else:
            _, md_text = load_md_text(data)
            
        # Save MD for reference
        md_dir = os.path.join(os.path.dirname(__file__), "md_outputs")
        os.makedirs(md_dir, exist_ok=True)
        raw_path = os.path.join(md_dir, f"{make_id('raw', name)}.md")
        with open(raw_path, "w", encoding="utf-8") as f: f.write(md_text)
        
        # Clean
        clean_path = clean_markdown(raw_path)
        final_md = md_text
        if os.path.exists(clean_path):
            with open(clean_path, "r", encoding="utf-8") as f: final_md = f.read()

        # Extract metadata from CLEANED text
        doc_md = get_doc_md(name, final_md)
        meta = doc_md.meta if doc_md else {}
        print(f"DEBUG: Extracted metadata for {name}: {list(meta.keys())}", flush=True)

        # Chunk & Upsert
        chunks = iter_chunks(final_md, target=1200, overlap=160)
        chunks = [clamp_text_by_tokens(c, MAX_EMBED_TOKENS) for c in chunks]
        chunks = [c for c in chunks if approx_tokens(c) <= MAX_EMBED_TOKENS]
        
        if chunks:
            vectors = EMB_P.embed_documents(chunks)
            pts = []
            for i, ch in enumerate(chunks):
                m_sec = re.search(r"(?m)^\s*#{1,6}\s+(.*)", ch)
                sec_title = m_sec.group(1).strip()[:240] if m_sec else ""
                pid = make_id(name, "clean", str(i))
                
                payload = {
                    "scope": used_scope,
                    "title": name.rsplit(".",1)[0],
                    "source_file": name,
                    "section_title": sec_title,
                    "path": f"upload://{name}",
                    "cleaned": True,
                    "text": ch
                }
                # Merge extracted metadata into payload
                payload.update({k: v for k, v in meta.items() if v is not None})
                
                pts.append(PointStruct(id=pid, vector=[], payload=payload))
            
            mode_final = upsert_adaptive(used_collection, pts, vectors)
            total_rows += len(pts)
        else:
            print(f"⚠ No chunks generated for {name}", flush=True)

    return UploadResponse(
        collection=used_collection,
        count=total_rows,
        scope=used_scope,
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
# @app.get("/bids")
# def get_bids():
#     """List all Qdrant collections"""
#     try:
#         URL = 'https://bidplus.gem.gov.in/all-bids'
#         response = requests.get(URL)
#         # 2. Parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # 3. Extract the title of the page
#         collections = qdrant.get_collections()
#         anchor_tag = soup.find('a')
#         file_name = "raw_scraped_data.html"

    
#         with open(file_name, 'w', encoding='utf-8') as f:
#             f.write(soup.prettify())
#         print(f"✅ Successfully saved raw HTML to '{file_name}'")
#     except Exception as e:
#         print(f"❌ An error occurred while saving the file: {e}")
#         # 2. Extract the 'href' attribute
#         if anchor_tag:
#             href_value = anchor_tag['href']
#             print(f"Extracted href: {soup}")
#         else:
#             print("Anchor tag not found.")
#         return {"status": "success", "collections": [{"name": c.name, "points_count": getattr(c, 'points_count', 0)} for c in collections.collections]}
#     except Exception as e:
#         return {"status": "error", "message": str(e)}

@app.get("/gem-bids")
async def get_gem_bids(  page: int = Query(1, ge=1, description="Page number"),
    rows: int = Query(10, ge=1, le=100, description="Records per page")):
    """Capture and return GEM bids"""
    try:
        print(f"🎯 Starting GEM bid capture via API...Pagre {page}", flush=True)
        
        # Call your async function
        result = await get_direct_bids(page)
        
        print(f"✅ Capture completed: {result}", flush=True)
        
        if result and result.get('code') == 200:
            data = result.get('response', []).get('response', []).get('docs', [])
            return {
                "status": "success",
                "message": f"Captured {len(data)} bid API calls",
                "count": len(data),
                "timestamp": datetime.now().isoformat(),
                "totalPages": result.get('response', []).get('response', []).get('numFound', 0) ,
                "data": data  # Return first 20 entries
            }
        else:
            return {
                "status": "error",
                "message": result.get('message', 'Capture failed'),
                "details": result
            }
            
    except Exception as e:
        print(f"❌ API endpoint error: {e}", flush=True)
        return {
            "status": "error",
            "message": f"Capture failed: {str(e)}",
            "timestamp": datetime.now().isoformat()
        }
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

from fastapi.responses import StreamingResponse
import json
import asyncio



@app.post("/chat", response_model=ChatAnswer)
def chat(req: ChatRequest):
    # Handle Swagger UI default values
    # User explicitly named collection "string", so we allow it.
    if req.scope == "string": req.scope = None

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
        "Answer as per document context. "
        # "You are a helpful assistant. Your primary task is to answer questions based on the provided context. "
        # "1. If the user's input is a greeting or general pleasantry (e.g., 'Hello', 'Hi', 'Who are you?'), respond politely and offer help with the documents. "
        # "2. For specific questions, answer based ONLY on the context provided below. "
        # "3. If the answer is not explicitly labeled, infer it from the document title, headers, or main subject matter. "
        # "4. Specifically for 'project name', if a labeled field is empty, use the full title of the tender or document (e.g. 'TENDER FOR...'). "
        # "5. If the information is truly not in the context, say 'I don't find it in the documents.' "
        # "You MUST provide your response in this format:\n"
        # "Thinking: <brief reasoning>\n"
        # "Final Answer: <the direct answer>"
    )
    user_msg = f"Context:\n{context_joined}\n\nQuestion: {req.query}\n\nAnswer:"

    llm = make_chat()
    result = llm.invoke([
        {"role":"system","content":sys_prompt},
        {"role":"user","content":user_msg}
    ])
    
    print(f"🤖 LLM Result Type: {type(result)}", flush=True)
    
    # Try different ways to extract the answer
    answer_text = ""
    thinking_text = None
    
    # Check additional_kwargs for reasoning_content (NVIDIA specific)
    if hasattr(result, 'additional_kwargs') and isinstance(result.additional_kwargs, dict):
        if 'reasoning_content' in result.additional_kwargs:
            thinking_text = str(result.additional_kwargs['reasoning_content'])
            print(f"✓ Got thinking from reasoning_content: {thinking_text[:100]}", flush=True)

    # Check content attribute (standard)
    if hasattr(result, 'content') and result.content:
        content = str(result.content)
        # Check for <think> tags if reasoning not found yet
        if not thinking_text and "<think>" in content and "</think>" in content:
            parts = content.split("</think>", 1)
            thinking_text = parts[0].replace("<think>", "").strip()
            answer_text = parts[1].strip()
            print(f"✓ Extracted thinking from <think> tags", flush=True)
        else:
            answer_text = content
        print(f"✓ Got answer from .content: {answer_text[:100]}", flush=True)
    
    # Fallback if answer is still empty but we have thinking
    if not answer_text and thinking_text:
         # Try to extract answer from thinking if it looks like it's there
         if "Final Answer:" in thinking_text:
             try:
                 answer_text = thinking_text.split("Final Answer:", 1)[1].strip()
                 print(f"✓ Extracted answer from thinking text", flush=True)
             except IndexError:
                 pass
    
    # If answer text contains "Final Answer:", clean it up
    if answer_text and "Final Answer:" in answer_text:
        answer_text = answer_text.split("Final Answer:", 1)[1].strip()
        print(f"✓ Cleaned 'Final Answer:' prefix from answer", flush=True)

    # Check response_metadata
    elif not answer_text and hasattr(result, 'response_metadata') and hasattr(result.response_metadata, 'text'):
        answer_text = str(result.response_metadata.text)
        print(f"✓ Got answer from response_metadata.text: {answer_text[:100]}", flush=True)
    # Fallback: convert to string
    elif not answer_text and not thinking_text:
        result_str = str(result)
        print(f"⚠ Fallback to string: {result_str[:200]}", flush=True)
        answer_text = result_str
    
    if not answer_text or answer_text.strip() == "":
        if thinking_text:
             answer_text = "(See thinking process)"
        else:
             answer_text = "I don't find it."
        print(f"⚠ Empty response, using default", flush=True)
    
    print(f"📝 Final Answer ({len(answer_text)} chars): {answer_text[:200]}...", flush=True)

    return ChatAnswer(answer=answer_text, thinking=thinking_text, citations=cite_items, vector_mode=vmode)


@app.post("/generate_rfp_summary")
def generate_rfp_summary(req: ChatRequest):
    """Generate a multi-sheet Excel summary by asking targeted questions for each field."""
    # Handle Swagger UI default values
    # User explicitly named collection "string", so we allow it.
    if req.scope == "string": req.scope = None
    print(f"DEBUG: Request scope after adjustment: {req}", flush=True)
    if req.collection:
        coll = req.collection
        scope_filter = None
    else:
        sc = req.scope or "tech_deck"
        coll = COLL_PREFIX + sc
        scope_filter = Filter(must=[FieldCondition(key="scope", match=MatchValue(value=sc))])

    # 1. Pre-fetch "Project Vitals" context
    # This table contains most of the key info, so we want to ensure it's available for all Vitals questions
    vitals_query = "Project Vitals table details end customer project name cost duration emd pbg penalty payment"
    q_safe = clamp_text_by_tokens(vitals_query, MAX_EMBED_TOKENS)
    qv = EMB_Q.embed_query(q_safe)
    res_vitals, _ = search_adaptive(coll, qv, limit=5, scope_filter=scope_filter)
    
    vitals_context_chunks = []
    for p in res_vitals:
        pl = p.payload or {}
        chunk = pl.get("text") or pl.get("section_title") or ""
        src = pl.get("source_file", "")
        vitals_context_chunks.append(f"[{src}] {chunk}")
    
    vitals_context_str = "\n\n---\n\n".join(vitals_context_chunks)
    print(f"DEBUG: Pre-fetched {len(vitals_context_chunks)} chunks for Project Vitals", flush=True)

    # Define the structure with specific queries
    # Removed "Project Vitals:" prefix to avoid retrieval drift
    field_queries = {
        "Vitals": {
            "End Customer": "Who is the End Customer, Consignee, Buyer, Client, or Authority? Look for 'CRIS' or 'Railways'.",
            "Project Name": "What is the Project Name, Tender Title, or Subject of the RFP?",
            "Bid Due Date": "What is the Bid Due Date, Submission Deadline, or Closing Date?",
            "Estimated Project Cost": "What is the Estimated Project Cost? If not explicitly stated, provide a SINGLE LINE ESTIMATE based on the EMD amount (e.g. 'Approx. INR X Cr based on EMD').",
            "Components": "What are the key Components, Bill of Material (BOM), or major items to be supplied?",
            "Duration": "What is the Duration, Period of Completion, Contract Period, or Timeline?",
            "EMD": "What is the EMD, Earnest Money Deposit, or Bid Security amount?",
            "PBG": "What is the PBG, Performance Bank Guarantee, or Security Deposit percentage?",
            "Penalty": "What are the Penalty clauses, Liquidated Damages (LD), or 'Capped to' limits?",
            "Payment": "What are the Payment Terms, Payment Schedule, 'Annual advance', or Milestones?",
            "Targus Scope": "What is the specific scope for the Bidder/System Integrator? Look for Resident Engineers or Support.",
            "Bid Evaluation Process": "What is the Bid Evaluation Process, Selection Criteria, or Evaluation Methodology?",
            "Implementation Ownership": "Who has Implementation Ownership or Responsibility?",
            "OEM Background": "What are the requirements regarding OEM Background or Incumbency?",
            "Partially Controlled Bid": "Analyze if the tender is 'Partially Controlled' or biased. Provide 1-2 short sentences.",
            "Competitive Scenario": "List likely competitors or OEMs in 3-4 short bullet points.",
            "Risks": "List top 3-4 Risks (Commercial/Technical) in short bullet points.",
            "Win Strategy": "List top 3-4 Key Selling Points or Win Strategy in short bullet points."
        },
        "SOR": {
            "Scope of Work Summary": "Summarize the Scope of Work and Technical Requirements.",
            "Key Deliverables": "List the Key Deliverables and Bill of Material."
        },
        "Payment": {
            "Payment Terms": "Provide the detailed Payment Terms and conditions.",
            "Milestones": "List the Payment Milestones."
        },
        "PQ": {
            "Pre-Qualification Criteria": "List the Pre-Qualification Criteria (PQ) and Eligibility."
        },
        "Evaluation": {
            "Evaluation Criteria": "Describe the Evaluation Criteria.",
            "Scoring Logic": "Explain the Scoring Logic."
        },
        "SLA_Penalty": {
            "SLA Requirements": "Summarize the SLA requirements.",
            "Penalty Clauses": "Detail the Penalty Clauses."
        }
    }

    # Data holder
    final_data = {}

    print(f"DEBUG: Starting field-wise processing...", flush=True)
    # Iterate through each section and each field
    for section, fields_dict in field_queries.items():
        section_data = {}
        print(f"DEBUG: Processing Section: {section}", flush=True)
        
        for field, query_text in fields_dict.items():
            # 2. Retrieve Context specifically for this field
            full_query = f"{field}: {query_text}"
            q_safe = clamp_text_by_tokens(full_query, MAX_EMBED_TOKENS)
            qv = EMB_Q.embed_query(q_safe)
            
            # Fetch context
            res, _ = search_adaptive(coll, qv, limit=15, scope_filter=scope_filter)
            
            contexts = []
            for p in res:
                pl = p.payload or {}
                chunk = pl.get("text") or pl.get("section_title") or ""
                src = pl.get("source_file", "")
                contexts.append(f"[{src}] {chunk}")
            
            # 3. Combine Contexts
            # If we are in Vitals section, prepend the pre-fetched Vitals context
            if section == "Vitals":
                combined_context_list = vitals_context_chunks + contexts
            else:
                combined_context_list = contexts
                
            # Deduplicate chunks (simple string match)
            unique_contexts = list(set(combined_context_list))
            
            context_text = "\n\n---\n\n".join(unique_contexts)
            context_text = clamp_text_by_tokens(context_text, 7000) 

            # 4. Ask LLM
            sys_prompt = (
                "You are an expert Bid Manager. Answer the specific question based on the context provided. "
                "1. Be EXTREMELY CONCISE and SPECIFIC. "
                "2. Do not use hedging language (e.g. 'It appears', 'likely', 'subject to'). State the best answer directly. "
                "3. If the answer is not explicitly found, provide a direct ESTIMATE or INFERENCE without explaining the reasoning. "
                "   - Example: 'Approx. 20 Cr based on EMD' instead of 'The cost is not stated but based on EMD...' "
                "4. Output ONLY the value or a short bulleted list. No intro/outro text. "
                "5. Only say 'Not Found' if absolutely no inference is possible."
            )
            
            user_msg = f"Context:\n{context_text}\n\nQuestion: {query_text}\n\nAnswer:"

            llm = make_chat()
            result = llm.invoke([
                {"role":"system","content":sys_prompt},
                {"role":"user","content":user_msg}
            ])
            
            answer = ""
            if hasattr(result, 'content'):
                answer = str(result.content)
            elif hasattr(result, 'additional_kwargs') and 'reasoning_content' in result.additional_kwargs:
                answer = str(result.additional_kwargs.get('reasoning_content', ''))
            
            # Clean answer
            answer = answer.replace("Final Answer:", "").strip()
            answer = answer.replace("**", "").replace("*", "").replace("`", "")
            
            if not answer: 
                answer = "Not Found"
            
            print(f"DEBUG: Field '{field}' -> {answer[:50]}...", flush=True)
            section_data[field] = answer
        
        final_data[section] = section_data

    # 5. Generate Excel
    # tmp_dir = tempfile.gettempdir()
    # tmp_path = os.path.join(tmp_dir, f"RFP_Summary_{make_id(coll)}.xlsx")
    
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx")
    tmp_path = tmp_file.name
    tmp_file.close()

    print(f"DEBUG: Writing to {tmp_path}", flush=True)
    with pd.ExcelWriter(tmp_path, engine='openpyxl') as writer:
        for section, data in final_data.items():
            df = pd.DataFrame(list(data.items()), columns=["Attribute", "Value"])
            safe_name = re.sub(r'[\\/*?:\[\]]', '', section)[:31]
            df.to_excel(writer, sheet_name=safe_name, index=False)
    
    print(f"DEBUG: Excel file created at {tmp_path}", flush=True)
    
    # Ensure the file exists and has content
    if os.path.exists(tmp_path):
        file_size = os.path.getsize(tmp_path)
        print(f"DEBUG: File size: {file_size} bytes", flush=True)
    else:
        print("ERROR: File was not created!", flush=True)
        raise HTTPException(status_code=500, detail="File generation failed ")
    
    return FileResponse(
        path=tmp_path, 
        filename="RFP_Summary_Generated.xlsx", 
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    ) 
#     with pd.ExcelWriter(tmp_path, engine='openpyxl') as writer:
#         for section, data in final_data.items():
#             # Convert dict to DataFrame
#             df = pd.DataFrame(list(data.items()), columns=["Attribute", "Value"])
#             safe_name = re.sub(r'[\\/*?:\[\]]', '', section)[:31]
#             df.to_excel(writer, sheet_name=safe_name, index=False)
#  # Write Excel

#     return FileResponse(
#         path=tmp_path, 
#         filename="RFP_Summary_Generated.xlsx", 
#         media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     )


