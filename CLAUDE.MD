# Document Agent - RAG System for Tender/RFP Processing

## Project Overview

This is a **Document Intelligence & RAG (Retrieval-Augmented Generation)** system designed for processing and querying procurement documents, tenders, RFPs, and technical decks. The system uses NVIDIA NIM endpoints for embeddings and LLM capabilities, combined with Qdrant vector database for semantic search.

## Architecture

### Core Components

1. **FastAPI Server** (`server/fastapi_app.py`)
   - RESTful API for document upload, search, and chat
   - Multi-file PDF/Markdown processing
   - Excel report generation for RFP summaries

2. **Document Parsing** (`script/nim_extract.py`, `script/md_parser.py`)
   - LlamaParse integration for PDF to Markdown conversion
   - Metadata extraction using NVIDIA NIM LLM
   - Structured field extraction with reranking

3. **Vector Database** (Qdrant)
   - Stores document embeddings
   - Supports both named and unnamed vector collections
   - Semantic search with cosine similarity

4. **NVIDIA NIM Integration**
   - Embeddings: `nvidia/nv-embedqa-e5-v5`
   - Chat: `meta/llama3-70b-instruct`
   - Reranking: `nvidia/nv-rerankqa-mistral-4b-v3`

## Key Features

### 1. Document Upload & Ingestion
- PDF parsing with LlamaParse
- Markdown cleaning and noise removal
- Automatic chunking with overlap (1200 chars, 160 overlap)
- Metadata extraction (tender fields, tech deck fields)
- Multi-file consolidation support

### 2. Semantic Search
- Query embeddings with NVIDIA NIM
- Vector similarity search in Qdrant
- Scope-based filtering (tender, tech_deck, etc.)
- Adaptive vector mode (named/unnamed)

### 3. RAG Chat System
- Context-aware question answering
- Citation tracking
- Thinking/reasoning output support
- Specialized prompts for bid management

### 4. RFP Summary Generation
- Multi-sheet Excel report generation
- Targeted field extraction:
  - **Vitals**: Customer, Cost, Duration, EMD, PBG, Payment
  - **SOR**: Scope of Work, Deliverables
  - **Payment**: Terms, Milestones
  - **PQ**: Pre-Qualification Criteria
  - **Evaluation**: Criteria, Scoring
  - **SLA_Penalty**: Requirements, Clauses

## Configuration

### Environment Variables (.env)

```env
# NVIDIA API
NVIDIA_API_KEY=nvapi-...
NIM_BASE_URL=https://integrate.api.nvidia.com
NIM_EMBED_MODEL=nvidia/nv-embedqa-e5-v5-passage
NIM_LLM_MODEL=meta/llama3-70b-instruct

# Qdrant
QDRANT_URL=http://localhost:6333
QDRANT_API_KEY=
QDRANT_COLLECTION_PREFIX=kb_

# LlamaParse
LLAMAPARSE_API_KEY=llx_...
LLAMAPARSE_INSTRUCTION=Keep slide titles, bullet points, and code blocks. Ignore watermarks, lorem, and CSS debris.

# Limits
EMBED_DIM=1024
MAX_EMBED_TOKENS=7500
MAX_CHAT_TOKENS=4000
MAX_CTX_CHUNKS=10
```

### Field Configuration Files

- `configs/tender_fields.yaml` - Tender-specific extraction fields
- `configs/tech_deck_fields.yaml` - Technical deck fields
- `configs/hr_fields.yaml` - HR document fields
- `configs/finance_fields.yaml` - Finance document fields
- `configs/sales_fields.yaml` - Sales document fields
- `configs/management_fields.yaml` - Management report fields

## API Endpoints

### POST /upload
Upload PDF/Markdown files for processing and ingestion.

**Parameters:**
- `files`: List of files (multipart/form-data)
- `scope`: Optional scope (tender, tech_deck, consolidated)
- `collection`: Optional custom collection name
- `recreate`: Boolean to recreate collection

**Response:**
```json
{
  "collection": "kb_tender",
  "count": 42,
  "scope": "tender",
  "stored_text": true,
  "vector_mode": "named"
}
```

### GET /search
Semantic search across documents.

**Parameters:**
- `q`: Query string (required)
- `k`: Number of results (default: 8)
- `scope`: Filter by scope
- `collection`: Search specific collection

### POST /chat
RAG-based question answering.

**Request:**
```json
{
  "query": "What is the EMD amount?",
  "k": 6,
  "scope": "tender",
  "collection": null
}
```

**Response:**
```json
{
  "answer": "INR 50 Lakhs",
  "thinking": "Based on the tender document...",
  "citations": [...],
  "vector_mode": "named"
}
```

### POST /generate_rfp_summary
Generate comprehensive Excel summary from RFP documents.

**Returns:** Excel file with multiple sheets

### GET /collections
List all Qdrant collections.

### GET /collection/{collection_name}
Get collection metadata.

### DELETE /collection/{collection_name}
Delete a collection.

## Document Processing Pipeline

1. **Upload** → PDF/MD files received
2. **Parse** → LlamaParse converts PDF to Markdown
3. **Clean** → Noise removal using `md_parser.py`
4. **Extract** → Metadata extraction with NIM LLM + reranking
5. **Chunk** → Text chunking with overlap
6. **Embed** → Generate embeddings via NVIDIA NIM
7. **Store** → Insert into Qdrant with payload metadata

## Usage Examples

### Upload a Tender Document
```bash
curl -X POST "http://localhost:8000/upload" \
  -F "files=@tender.pdf" \
  -F "scope=tender"
```

### Search
```bash
curl "http://localhost:8000/search?q=EMD%20amount&k=5&scope=tender"
```

### Chat
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is the project duration?",
    "k": 6,
    "scope": "tender"
  }'
```

### Generate RFP Summary
```bash
curl -X POST "http://localhost:8000/generate_rfp_summary" \
  -H "Content-Type: application/json" \
  -d '{"query": "", "scope": "tender"}' \
  --output RFP_Summary.xlsx
```

## Directory Structure

```
document_agent/
├── server/
│   ├── fastapi_app.py          # Main FastAPI application
│   └── md_outputs/             # Parsed markdown outputs
├── script/
│   ├── nim_extract.py          # NVIDIA NIM extraction utilities
│   ├── md_parser.py            # Markdown parsing & cleaning
│   ├── ingest_qdrant.py        # Qdrant ingestion scripts
│   └── search_qdrant.py        # Search utilities
├── configs/
│   └── *_fields.yaml           # Field configurations per domain
├── data/                       # Sample documents
├── requirements.txt            # Python dependencies
└── .env                        # Environment configuration
```

## Key Technologies

- **FastAPI**: Web framework
- **Qdrant**: Vector database
- **NVIDIA NIM**: Embeddings, LLM, Reranking
- **LlamaParse**: PDF parsing
- **LangChain**: NVIDIA endpoint integration
- **Pandas/OpenPyXL**: Excel generation
- **PyYAML**: Configuration management

## Development Notes

### Token Limits
- Embedding max: 7500 tokens (~30,000 chars)
- Chat max: 4000 tokens (~16,000 chars)
- Context chunks: Max 10 per query

### Vector Modes
The system supports both:
- **Named vectors**: `{text_vector: [...]}`
- **Unnamed vectors**: `[...]`

Auto-detection and fallback ensure compatibility.

### Chunking Strategy
- Headers (# headings) preserved with content
- Bullet points kept together when possible
- Overlap prevents context loss at boundaries
- Hard cap at MAX_EMBED_TOKENS

## Testing Scripts

- `test_qdrant.py` - Test Qdrant connectivity
- `test_qdrant_dir.py` - Batch directory ingestion
- `test_chat.py` - Test chat endpoint
- `check_sig.py` - Check API signatures
- `check_error.py` - Error diagnostics
- `check_import.py` - Verify imports

## Running the Server

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys

# Run server
uvicorn server.fastapi_app:app --reload --port 8000
```

## Troubleshooting

### Empty LLM Responses
The system handles multiple response formats from NVIDIA NIM:
- `result.content`
- `result.additional_kwargs['reasoning_content']`
- `<think>` tags in content
- Fallback to string conversion

### Collection Vector Mode Mismatch
Auto-detection tries named vectors first, falls back to unnamed on error.

### PDF Parsing Failures
Check LlamaParse API key and quota. Raw markdown is saved even if cleaning fails.

## Future Enhancements

- [ ] Streaming chat responses
- [ ] Multi-language support
- [ ] Advanced chunk scoring
- [ ] Hybrid search (keyword + semantic)
- [ ] Document versioning
- [ ] User authentication
