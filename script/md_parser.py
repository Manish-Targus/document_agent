# md_parser.py (v5.6.0 — NoiseXL+, EndpointClean, FenceFix)
from __future__ import annotations
import argparse, json, os, re, yaml
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dotenv import load_dotenv

# Optional deps
try:
    from dateutil import parser as dtparse
    _HAS_DATEUTIL = True
except Exception:
    _HAS_DATEUTIL = False

try:
    import PyPDF2
    _HAS_PYPDF2 = True
except Exception:
    _HAS_PYPDF2 = False

try:
    from pptx import Presentation
    _HAS_PPTX = True
except Exception:
    _HAS_PPTX = False

# NIM optional (unchanged)
try:
    from nim_extract import (
        extract_fields_with_nims,
        extract_specific_fields_with_nims,
        NimClientError,
    )
    _HAS_NIM = True
except Exception:
    _HAS_NIM = False


# ---------------- Models ----------------
@dataclass
class DocMD:
    name: str
    path: Path
    md_text: str
    plain_text: str
    doc_type: Optional[str]
    meta: Dict[str, Optional[object]]
    notes: List[Dict[str, object]]
    tables: List[Dict[str, List[Dict[str, str]]]]


# ---------------- Config ----------------
def load_schema_config(schema: str) -> dict:
    cfg_path = Path(__file__).resolve().parent.parent / "configs" / f"{schema}_fields.yaml"
    if not cfg_path.exists():
        raise SystemExit(f"Config not found: {cfg_path}")
    with open(cfg_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------- Helpers ----------------
IST_TZOFFSET = timedelta(hours=5, minutes=30)

def _tz_ist(dt: datetime) -> datetime:
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone(IST_TZOFFSET))
    return dt.astimezone(timezone(IST_TZOFFSET))

def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()

def clean_title_for_yaml(t: Optional[str]) -> str:
    if not t:
        return ""
    return re.sub(r"^\s*#+\s*", "", t).strip()

def _only_digits(s: Optional[str]) -> Optional[str]:
    if not s:
        return None
    d = re.sub(r"[^\d]", "", s)
    return d or None

def _parse_amount_to_rupees(s: Optional[str]) -> Optional[str]:
    if not s: return None
    s0 = s.strip()
    m = re.search(r"(?i)\b(\d+(?:\.\d+)?)\s*(Crore|Lakh)\b", s0)
    if m:
        try: val = Decimal(m.group(1))
        except InvalidOperation: return _only_digits(s0)
        mult = Decimal("10000000") if m.group(2).lower()=="crore" else Decimal("100000")
        return str(int((val*mult).to_integral_value(rounding="ROUND_HALF_UP")))
    cleaned = re.sub(r"[₹,\s]", "", s0)
    try:
        return str(int(Decimal(cleaned).to_integral_value(rounding="ROUND_HALF_UP")))
    except Exception:
        return _only_digits(s0)


# ---------------- Markdown & Tables ----------------
def _fix_broken_json_fences(md: str) -> str:
    """
    Repairs common corrupt patterns like:
      Sample Payload ```json "customerId": "..." ...
    Ensures opening/closing fences and braces if missing.
    """
    out = []
    i, lines = 0, md.splitlines()
    while i < len(lines):
        ln = lines[i]
        if re.search(r"```json\s*\"", ln):
            # Start a new block, inject '{'
            prefix = re.sub(r'```json\s*"', '```json\n{ "', ln)
            out.append(prefix)
            i += 1
            # Copy until we hit closing fence or a blank header
            while i < len(lines) and not lines[i].strip().startswith("```"):
                out.append(lines[i])
                i += 1
            # Close brace if block content started with quote and didn't end with '}'
            if not any("}" in l for l in out[-20:]):
                out.append("}")
            if i < len(lines) and lines[i].strip().startswith("```"):
                out.append("```")
                i += 1
            else:
                out.append("```")
            continue
        out.append(ln)
        i += 1
    return "\n".join(out)

def noise_clean_markdown(md: str) -> str:
    if not md: return md
    # fence repairs first
    md = _fix_broken_json_fences(md)
    # Fix empty/unterminated fences
    md = re.sub(r"```(?:\w+)?\s*```", "", md)
    md = re.sub(r"```([^\n]*?)\Z", r"```\n\1\n```", md)
    md = re.sub(r"(^|\n)```json\s*\"","\\1```json\n\"", md)

    lines, out = md.splitlines(), []
    LOREM  = re.compile(r"(?i)\b(lorem|ipsum|placeholder|dummy text)\b")
    CSS    = re.compile(r"(?i)(\{|}|;|@media|^\.|</?\w+>|font[- ]|margin[- ]|width:|height:)")
    BASE64 = re.compile(r"data:image/[^;]+;base64,")
    HE_ECHO= re.compile(r"^\s*[—\-–]\s*#\s*")
    UPPER6 = re.compile(r"^[A-Z]{2,6}$")
    DROP_HEADINGS = re.compile(r"^\s*#+\s*(ALOO|C\s*argus|Cargus)\s*$", re.I)
    DROP_SINGLE   = re.compile(r"^(ALOO|C\s*argus|Cargus)\s*$", re.I)

    in_css_block = False
    for raw in lines:
        t = raw.rstrip("\n")

        # skip CSS fenced blocks
        if t.strip().startswith("```css"):
            in_css_block = True
            continue
        if in_css_block:
            if t.strip().startswith("```"):
                in_css_block = False
            continue

        s = t.strip()
        if not s:
            out.append(t); continue

        # Drop known garbage/headers
        if DROP_HEADINGS.match(s) or DROP_SINGLE.match(s):
            continue
        if LOREM.search(s) or BASE64.search(s):
            continue
        if CSS.search(s) and not s.startswith("```"):
            continue
        s = HE_ECHO.sub("", s)
        if UPPER6.match(s):
            continue

        out.append(s)

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned

def normalize_for_meta(s: str) -> str:
    out = []
    for ln in s.splitlines():
        t = ln.rstrip()
        if not t.strip(): continue
        if t.strip().startswith("|"):
            out.append(t); continue
        t = t.replace("|", " ")
        t = re.sub(r"\s{2,}", " ", t)
        out.append(t)
    return "\n".join(out)

def _is_rule_row(r: str) -> bool:
    s = r.strip()
    if not (s.startswith("|") and s.endswith("|")): return False
    core = s.strip("|").replace(" ","")
    return bool(core) and all(ch in "-:|" for ch in core) and "-" in core

def _cells(r: str) -> List[str]:
    return [c.strip() for c in r.strip().strip("|").split("|")]

def parse_markdown_tables(md: str) -> List[Dict[str, object]]:
    lines, i, tables = md.splitlines(), 0, []
    while i < len(lines):
        if lines[i].strip().startswith("|"):
            if i+1 < len(lines) and lines[i+1].strip().startswith("|") and _is_rule_row(lines[i+1]):
                headers = _cells(lines[i]); i += 2
                rows = []
                while i < len(lines) and lines[i].strip().startswith("|"):
                    cs = _cells(lines[i])
                    if len(cs) < len(headers): cs += [""]*(len(headers)-len(cs))
                    if len(cs) > len(headers): cs = cs[:len(headers)]
                    rows.append({h:c for h,c in zip(headers, cs)}); i += 1
                tables.append({"headers":headers, "rows":rows}); continue
        i += 1
    return tables


# ---------------- OCR & Titles ----------------
def _collapse_single_letter_spacing(s: str) -> str:
    return re.sub(r"\b(?:[A-Za-z]\s+){2,}[A-Za-z]\b", lambda m: m.group(0).replace(" ", ""), s)

def _fix_leading_single_to_word(s: str) -> str:
    return re.sub(r"\b([A-Za-z])\s+([A-Za-z]{2,})\b", r"\1\2", s)

def _ocr_common_fixes(s: str) -> str:
    s2 = s
    s2 = re.sub(r"\bZ\s*ero\b", "Zero", s2, flags=re.I)
    s2 = re.sub(r"\bT\s*ouch\b", "Touch", s2, flags=re.I)
    s2 = re.sub(r"\bZ\s*ero[-\s]?Touch\b", "Zero-Touch", s2, flags=re.I)
    s2 = s2.replace("C argus", "Cargus")
    s2 = _collapse_single_letter_spacing(s2)
    s2 = _fix_leading_single_to_word(s2)
    return s2

def _looks_like_email(s: str) -> bool:
    return bool(re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", s))

def _too_generic(s: str) -> bool:
    t = s.lower()
    return any(k in t for k in ["architecture","system","overview","apis","sequence","flow","slide","deck"])

def _score_title_candidate(s: str) -> float:
    s = s.strip()
    if not s: return -1.0
    s = _ocr_common_fixes(s)
    score = 0.0
    if 8 <= len(s) <= 64: score += 1.0
    if " " in s: score += 1.0
    if re.search(r"[a-z]", s) and re.search(r"[A-Z]", s): score += 0.6
    if _looks_like_email(s): score -= 2.0
    if _too_generic(s): score -= 0.8
    if re.search(r"(?i)\bZero[-\s]?Touch\b", s): score += 1.2
    if re.search(r"(?i)\bClaim System\b", s): score += 0.6
    if re.fullmatch(r"[A-Z\-]{2,}", s): score -= 0.6
    return score

def _candidate_stream(md_text: str, plain_text: str) -> List[str]:
    cands = []
    for ln in (md_text or "").splitlines()[:50]:
        if ln.strip().startswith("#"):
            cand = re.sub(r"^\s*#+\s*", "", ln).strip()
            if cand: cands.append(cand)
    md_nonempty = [ln.strip() for ln in (md_text or "").splitlines() if ln.strip()]
    cands.extend(md_nonempty[:30])
    pt_nonempty = [ln.strip() for ln in (plain_text or "").splitlines() if ln.strip()]
    cands.extend(pt_nonempty[:30])
    seen, uniq = set(), []
    for c in cands:
        n = _ocr_common_fixes(c)
        if n not in seen:
            seen.add(n); uniq.append(n)
    return uniq

def detect_deck_title(md_text: str, plain_text: str) -> Optional[str]:
    best, best_score = None, -999.0
    for cand in _candidate_stream(md_text, plain_text):
        if len(cand) < 3: continue
        if _looks_like_email(cand): continue
        cleaned = _ocr_common_fixes(cand)
        score = _score_title_candidate(cleaned)
        if score > best_score:
            best, best_score = cleaned, score
    return best if (best and best_score > -0.5) else None


# ---------------- Confidence helpers ----------------
def score_table() -> float: return 0.90
def score_kv_exact() -> float: return 0.92
def score_kv_synonym() -> float: return 0.84
def score_label_window() -> float: return 0.72
def score_global_regex() -> float: return 0.64
def score_canonical() -> float: return 1.00


# ---------------- Pattern sanitizers ----------------
_INLINE_FLAG_ONLY  = re.compile(r"\(\?[aiLmsux-]*\)")
_INLINE_FLAG_GROUP = re.compile(r"\(\?[aiLmsux-]*:")

def strip_inline_flags(p: str) -> str:
    p2 = _INLINE_FLAG_GROUP.sub("(", p)
    p2 = _INLINE_FLAG_ONLY.sub("", p2)
    return p2

def to_union(value_patterns: Optional[List[str]]) -> Optional[str]:
    if not value_patterns: return None
    cleaned = []
    for vp in value_patterns:
        if not isinstance(vp, str) or not vp.strip(): continue
        cleaned.append(f"(?:{strip_inline_flags(vp.strip())})")
    return "(?:"+"|".join(cleaned)+")" if cleaned else None


# ---------------- Table pickers (tender) ----------------
def table_pick_amount(tables, headers_like) -> Optional[str]:
    hdr_norm = [h.lower() for h in headers_like]
    for tbl in tables:
        headers = [h.strip() for h in tbl["headers"]]
        headers_l = [h.lower() for h in headers]
        idx = next((i for i,h in enumerate(headers_l) if any(k in h for k in hdr_norm)), None)
        if idx is None: continue
        for row in tbl["rows"]:
            vals = [row.get(h,"") for h in headers]
            cell = vals[idx].strip() if idx < len(vals) else ""
            if cell:
                m = re.search(r"(?i)(₹?\s*[\d,\.]+|[\d\.]+\s*(?:Crore|Lakh))", cell)
                return (m.group(1).strip() if m else cell)
    return None

def table_pick_text(tables, headers_like) -> Optional[str]:
    hdr_norm = [h.lower() for h in headers_like]
    for tbl in tables:
        headers = [h.strip() for h in tbl["headers"]]
        headers_l = [h.lower() for h in headers]
        idx = next((i for i,h in enumerate(headers_l) if any(k in h for k in hdr_norm)), None)
        if idx is None: continue
        for row in tbl["rows"]:
            vals = [row.get(h,"") for h in headers]
            cell = vals[idx].strip() if idx < len(vals) else ""
            if cell: return cell
    return None


# ---------------- Tender extract (selected) ----------------
_MONTHS = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)|Sep(?:t|tember)|Oct(?:ober)?|Nov(?:ember)|Dec(?:ember)?)"
_DAY    = r"(?:0?[1-9]|[12][0-9]|3[01])"
_YEAR   = r"(?:20\d{2}|\d{2})"
_DATE_SEP = r"(?:\/|-|\.|\s)"
_DATE_NUMERIC = rf"{_DAY}{_DATE_SEP}(?:0?[1-9]|1[0-2]){_DATE_SEP}{_YEAR}"
_DATE_MON     = rf"{_DAY}{_DATE_SEP}{_MONTHS}{_DATE_SEP}{_YEAR}"
_DATE_ANY     = rf"(?:{_DATE_NUMERIC}|{_DATE_MON}|\d{{4}}{_DATE_SEP}(?:0?[1-9]|1[0-2]){_DATE_SEP}{_DAY})"
_TIME12       = r"(?:0?[1-9]|1[0-2]):[0-5]\d(?:\s?[AP]M)"
_TIME24       = r"(?:[01]?\d|2[0-3]):[0-5]\d(?::[0-5]\d)?"
_TIME_ANY     = rf"(?:{_TIME24}|{_TIME12})"
_DT_PHRASE    = rf"{_DATE_ANY}(?:\D{{0,12}}{_TIME_ANY})?|{_TIME_ANY}(?:\D{{0,12}}{_DATE_ANY})?"

def extract_dates_from_phrase(s: str) -> Tuple[Optional[str], Optional[str]]:
    if not s: return (None,None)
    m = re.search(_DT_PHRASE, s, flags=re.I)
    if not m: return (None,None)
    frag = m.group(0)
    d = (re.search(_DATE_ANY, frag, flags=re.I) or re.search(_DATE_ANY, s, flags=re.I))
    t = (re.search(_TIME_ANY, frag, flags=re.I) or re.search(_TIME_ANY, s, flags=re.I))
    return (d.group(0) if d else None, t.group(0) if t else None)

def _normalize_datetime_ist(date_str: Optional[str], time_str: Optional[str]) -> Optional[str]:
    if not date_str and not time_str: return None
    s = " ".join([x for x in [date_str, time_str] if x]).strip()
    if not s: return None
    if _HAS_DATEUTIL:
        try:
            dt = dtparse.parse(s, dayfirst=True, fuzzy=True)
            return _tz_ist(dt).strftime("%Y-%m-%d %H:%M %z")
        except Exception:
            return s
    return s


# ---------------- Tech deck parsers ----------------
EMAIL_RX = re.compile(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b")
HTTP_METHOD_RX = r"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)"
PATH_RX        = r"(?:/[\w\-/\.{}\[\]_]+)"
ENDPOINT_LINE_RX = re.compile(rf"\b{HTTP_METHOD_RX}\s+{PATH_RX}\b")

def parse_env_vars(text: str, known_envs: List[str], stoplist: List[str]) -> List[str]:
    found = set()
    for line in text.splitlines():
        for m in re.finditer(r"\b([A-Z][A-Z0-9_]{2,})\s*=", line):
            tok = m.group(1)
            if "_" in tok and tok not in stoplist: found.add(tok)
        for tok in re.findall(r"\b[A-Z][A-Z0-9_]{2,}\b", line):
            if "_" in tok and tok not in stoplist: found.add(tok)
    for env in known_envs:
        if re.search(rf"\b{re.escape(env)}\b", text): found.add(env)
    return sorted(found)

def parse_api_endpoints(text: str) -> List[Dict[str, str]]:
    eps, seen = [], set()
    # lines
    for line in text.splitlines():
        m = ENDPOINT_LINE_RX.search(line)
        if not m: continue
        method = m.group(1)
        path = m.group(0).split()[1].lower()
        eps.append({"method": method, "path": path})
    # fenced code blocks
    for block in re.findall(r"```[a-zA-Z0-9]*\n(.*?)```", text, flags=re.S):
        for m in ENDPOINT_LINE_RX.finditer(block):
            method = m.group(1)
            path = m.group(0).split()[1].lower()
            eps.append({"method": method, "path": path})
    # unique
    uniq = []
    for ep in eps:
        key = (ep["method"], ep["path"])
        if key not in seen:
            seen.add(key); uniq.append(ep)
    return uniq

_FLOW_HEADINGS = [
    "claim api flow","unclaim api flow","admin flow","api flow",
    "sequence","capacity — status snapshot","capacity - status snapshot","capacity/status snapshot"
]

def _similar(a: List[str], b: List[str]) -> float:
    if not a or not b: return 0.0
    s1, s2 = set(a), set(b)
    return len(s1 & s2) / max(1, len(s1 | s2))

def parse_flows(text: str) -> List[Dict[str, object]]:
    flows = []
    for head in _FLOW_HEADINGS:
        m = re.search(rf"(?im)^\s*#{{1,3}}\s*{re.escape(head)}\s*$", text) or re.search(rf"(?i)\b{re.escape(head)}\b", text)
        if not m: continue
        start = m.end()
        tail = text[start:].splitlines()
        steps, subhead = [], False
        for ln in tail[:140]:
            if re.match(r"^\s*#{{1,3}}\s+\S", ln) and not re.search(rf"(?i){re.escape(head)}", ln): break
            if re.match(r"^\s*[-*•]\s+", ln) or re.match(r"^\s*\d+[\.\)]\s+", ln):
                subhead = False
                steps.append(re.sub(r"^\s*[-*•]\s+|\s*\d+[\.\)]\s+", "", ln).strip())
            elif re.match(r"^\s*###+\s+\S", ln):
                subhead = True
                steps.append(re.sub(r"^\s*#+\s*", "", ln).strip())
            elif subhead and ln.strip() and len(ln.strip()) < 160:
                steps[-1] = (steps[-1] + " " + ln.strip()).strip()
        steps = [s for s in steps if s]
        if steps: flows.append({"name": head.title(), "steps": steps})
    # de-dup
    kept = []
    for f in flows:
        if all(_similar(f["steps"], g["steps"]) < 0.7 for g in kept):
            kept.append(f)
    return kept

def parse_contacts(text: str) -> List[str]:
    mails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
    return sorted(set(mails))

def _infer_org_from_emails(text: str, domap: Dict[str,str]) -> Optional[str]:
    for m in re.finditer(r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b", text):
        d = m.group(1).lower()
        if d in domap: return domap[d]
    return None

# PPTX metadata
def _pptx_core_dates(pptx_path: Path) -> Tuple[Optional[datetime], Optional[datetime]]:
    if not _HAS_PPTX: return (None,None)
    try:
        prs = Presentation(str(pptx_path))
        cp = prs.core_properties
        return (cp.created if isinstance(cp.created, datetime) else None,
                cp.modified if isinstance(cp.modified, datetime) else None)
    except Exception:
        return (None,None)

def _pptx_core_title(pptx_path: Path) -> Optional[str]:
    if not _HAS_PPTX: return None
    try:
        prs = Presentation(str(pptx_path))
        t = (prs.core_properties.title or "").strip()
        return t or None
    except Exception:
        return None

# PDF meta
def _pdf_meta_dates(pdf_path: Path) -> List[datetime]:
    out=[]
    if not _HAS_PYPDF2: return out
    try:
        with open(pdf_path,"rb") as f:
            r = PyPDF2.PdfReader(f)
            info = getattr(r, "metadata", None) or getattr(r, "documentInfo", None)
            if info:
                for key in ("/CreationDate","/ModDate"):
                    val = info.get(key) if hasattr(info,"get") else None
                    if isinstance(val,str):
                        m = re.search(r"D:(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})?", val)
                        if m:
                            y,mo,d,hh,mm = map(int, [m.group(1),m.group(2),m.group(3),m.group(4),m.group(5) or "0"])
                            out.append(datetime(y,mo,d,hh,mm))
    except Exception:
        pass
    return out

def _fs_meta_dates(path: Path) -> List[datetime]:
    out=[]
    try:
        st = path.stat()
        out += [datetime.fromtimestamp(st.st_mtime), datetime.fromtimestamp(st.st_ctime)]
    except Exception:
        pass
    return out

def _to_ist_iso(dt: datetime) -> str:
    return _tz_ist(dt).strftime("%Y-%m-%d %H:%M %z")

def _prefer_recent(dts: List[datetime], min_year: int=2015) -> Optional[str]:
    if not dts: return None
    dts = [d for d in dts if d.year >= min_year]
    if not dts: return None
    return _to_ist_iso(max(dts))

def extract_presentation_date(md_text: str, plain_text: str, path: Path, cfg: dict, notes: List[Dict[str, object]]) -> Optional[str]:
    # Slide-level hints first
    for ln in (md_text or "").splitlines()[:150]:
        if re.search(r"(?i)\b(date|version|presented on|event)\b", ln):
            d,t = extract_dates_from_phrase(ln)
            norm = _normalize_datetime_ist(d,t)
            if norm:
                notes.append({"field":"presentation_date","source":"deck:title_hint","confidence":0.75})
                return norm
    # PPTX core (guarded)
    if path.suffix.lower()==".pptx":
        created, modified = _pptx_core_dates(path)
        cand = modified or created
        if cand and cand.year >= 2015:
            notes.append({"field":"presentation_date","source":"pptx:core","confidence":0.8})
            return _to_ist_iso(cand)
    # PDF metadata
    if path.suffix.lower()==".pdf":
        pdfd = _pdf_meta_dates(path)
        pref = _prefer_recent(pdfd, 2015)
        if pref:
            notes.append({"field":"presentation_date","source":"pdf:metadata","confidence":0.6})
            return pref
    # Regex fallback
    source = (md_text or "")+"\n"+(plain_text or "")
    m = re.search(_DATE_ANY, source, flags=re.I)
    if m and _HAS_DATEUTIL:
        try:
            dt = dtparse.parse(m.group(0), dayfirst=True, fuzzy=True)
            if dt.year >= 2015:
                notes.append({"field":"presentation_date","source":"deck:regex_hint","confidence":0.7})
                return _to_ist_iso(dt)
        except Exception:
            pass
    # FS timestamps
    fs = _prefer_recent(_fs_meta_dates(path), 2015)
    if fs:
        notes.append({"field":"presentation_date","source":"fs:timestamp","confidence":0.5})
        return fs
    return None

def summarize_tech_deck(md_text: str, plain_text: str, cfg: dict, path: Path, notes: List[Dict[str, object]]) -> Dict[str, object]:
    source = (md_text or "")+"\n"+(plain_text or "")
    title = detect_deck_title(md_text, plain_text) or None
    if path.suffix.lower()==".pptx":
        core_title = _pptx_core_title(path)
        if core_title and (not title or len(title)<6):
            title = core_title.strip()
    known_envs = cfg.get("env_vars_known", [])
    stop_envs  = cfg.get("env_vars_stoplist", [])
    env_vars   = parse_env_vars(source, known_envs, stop_envs)
    endpoints  = parse_api_endpoints(source)
    flows      = parse_flows(source)
    contacts   = parse_contacts(source)

    topics=[]
    for kw in cfg.get("topics_keywords", []):
        if re.search(rf"\b{re.escape(kw)}\b", source, flags=re.I): topics.append(kw)

    organisation=None
    inferred = _infer_org_from_emails(source, cfg.get("domain_org_map", {}))
    if inferred: organisation = inferred

    res = {
        "deck_title": clean_title_for_yaml(title) if title else None,
        "organisation": organisation,
        "topics": sorted(set(topics)),
        "env_vars": env_vars,
        "api_endpoints": endpoints,
        "flows": flows,
        "contacts": contacts,
    }
    pres = extract_presentation_date(md_text, plain_text, path, cfg or {}, notes)
    if pres: res["presentation_date"] = pres
    return res


# ---------------- Generic schema KV (HR/Finance/Sales/Mgmt) ----------------
def kv_like(text: str, lab: str, window: int, val_union: Optional[str]) -> Optional[str]:
    if not val_union: return None
    lab_regex = re.sub(r"\s+", r"\\s*", re.escape(lab))
    rp = re.compile(rf"{lab_regex}[^\n]{{0,{window}}}{val_union}", flags=re.I|re.S)
    m = rp.search(text)
    if not m: return None
    groups = [g for g in m.groups() if isinstance(g,str) and g.strip()]
    return groups[-1] if groups else m.group(0)

def table_pick_value_generic(tables, headers_like) -> Optional[str]:
    hdr_norm = [h.lower() for h in headers_like] if headers_like else []
    for tbl in tables:
        headers = [h.strip() for h in tbl["headers"]]
        headers_l = [h.lower() for h in headers]
        idx = next((i for i,h in enumerate(headers_l) if any(k in h for k in hdr_norm)), None)
        if idx is None: continue
        for row in tbl["rows"]:
            vals = [row.get(h,"") for h in headers]
            cell = vals[idx].strip() if idx < len(vals) else ""
            if cell: return cell
    return None

def extract_fields_by_schema(schema_cfg: dict, text_norm: str, full_text: str, tables) -> Dict[str, Optional[str]]:
    out = {}
    fields: dict = schema_cfg.get("fields", {})
    default_window = schema_cfg.get("default_window", 80)
    for fname, fcfg in fields.items():
        val=None
        t_heads = fcfg.get("table_headers")
        if t_heads:
            tval = table_pick_value_generic(tables, t_heads)
            if tval: val = tval
        if val is None:
            kv_labels = fcfg.get("kv_labels", [])
            val_union = to_union(fcfg.get("value_patterns"))
            window = fcfg.get("window", default_window)
            for lab in kv_labels:
                cand = kv_like(text_norm, lab, window, val_union)
                if cand: val = cand; break
        if val is None:
            for gr in fcfg.get("regex_fallbacks", []) or []:
                rg = re.compile(strip_inline_flags(gr), flags=re.I|re.S)
                m = rg.search(text_norm) or rg.search(full_text)
                if m:
                    groups = [g for g in m.groups() if isinstance(g,str) and g.strip()]
                    val = groups[-1] if groups else m.group(0); break
        norm = fcfg.get("normalize")
        if val and norm == "amount_inr":
            val = _parse_amount_to_rupees(val)
        elif val and norm == "integer":
            m = re.search(r"\b(\d{1,9})\b", val); val = m.group(1) if m else None
        elif val and norm == "percent":
            m = re.search(r"(\d+(?:\.\d+)?)", val); val = m.group(1) if m else None
        out[fname] = val
    return out


# ---------------- LlamaParse/pdfminer ----------------
def load_llamaparse_markdown(api_key: str, path: Path) -> str:
    from llama_parse import LlamaParse
    instruction = os.getenv(
        "LLAMAPARSE_INSTRUCTION",
        "Keep slide titles, bullet points, and code blocks. Ignore watermarks, lorem, CSS fragments, and stray CSS tokens. Normalize headings; omit duplicates."
    )
    parser = LlamaParse(api_key=api_key, result_type="markdown", parsing_instruction=instruction)
    docs = parser.load_data([str(path)])
    parts = [getattr(d,"text",None) for d in (docs or []) if getattr(d,"text",None)]
    raw = "\n\n".join(parts).strip()
    return noise_clean_markdown(raw)

def load_pdfminer_text(path: Path) -> str:
    try:
        from pdfminer_high_level import extract_text  # type: ignore
    except Exception:
        extract_text = None
    if extract_text and path.suffix.lower()==".pdf":
        try: return (extract_text(str(path)) or "").strip()
        except Exception: pass
    try:
        if path.suffix.lower()==".pdf":
            from pdfminer.high_level import extract_text as et_fallback
            return (et_fallback(str(path)) or "").strip()
    except Exception:
        pass
    return ""


# ---------------- Doc detection & tender helpers ----------------
def detect_doc_type_tenderish(text: str) -> Optional[str]:
    t = text.lower()
    if re.search(r"\brequest\s+for\s+proposal\b|\brfp\b", t): return "RFP"
    if re.search(r"\bnotice\s+inviting\s+tender\b|\bnit\b", t): return "NIT"
    if re.search(r"\bstandard\s+bid\s+document\b", t) and re.search(r"\b(gcc|itb)\b", t): return "SBD"
    if re.search(r"\bgeneral\s+conditions\s+of\s+contract\b", t): return "GCC"
    if re.search(r"\binstructions\s+to\s+bidders\b", t): return "ITB"
    return None

def looks_like_deck(text: str) -> bool:
    hits = sum(1 for kw in [
        "architecture","system overview","high-level","api flow","sequence",
        "environment variables","endpoints","data model","payload","admin flow","capacity"
    ] if kw in text.lower())
    return hits >= 2

def looks_like_from_keywords(text: str, keywords: List[str]) -> bool:
    t = text.lower()
    return sum(1 for kw in keywords if kw.lower() in t) >= 2

def looks_scanned(md_text: str, plain_text: str) -> bool:
    t = (md_text or "") + plain_text
    if len(t) < 400: return True
    letters = len(re.findall(r"[A-Za-zÀ-ÿऀ-\u097F]", t))
    return (letters / max(len(t),1)) < 0.15


# ---------------- Main doc parser ----------------
def parse_one_doc(api_key: str, pdf: Path,
                  tender_cfg, deck_cfg, hr_cfg, fin_cfg, sales_cfg, mgmt_cfg,
                  sum_quantity_if_missing: bool, schema_mode: str) -> DocMD:
    try:
        md_text = load_llamaparse_markdown(api_key, pdf)
    except Exception:
        md_text = ""
    plain_text = load_pdfminer_text(pdf)
    full_text  = (md_text + "\n" + plain_text)

    # Doc-type detection
    tenderish = detect_doc_type_tenderish(full_text)
    is_deck   = looks_like_deck(full_text)

    def _like(cfg): return looks_like_from_keywords(full_text, cfg.get("detect_keywords", []))
    looks_hr, looks_fin, looks_sales, looks_mgmt = _like(hr_cfg), _like(fin_cfg), _like(sales_cfg), _like(mgmt_cfg)

    if schema_mode != "auto":
        doc_type = schema_mode
    else:
        if is_deck and not tenderish: doc_type = "tech_deck"
        elif tenderish:               doc_type = tenderish
        elif looks_fin:               doc_type = "finance"
        elif looks_sales:             doc_type = "sales"
        elif looks_hr:                doc_type = "hr"
        elif looks_mgmt:              doc_type = "management"
        else:                         doc_type = "tech_deck"

    tables = parse_markdown_tables(md_text if md_text else plain_text)

    notes, meta = [], {}
    meta["tender_title"] = detect_deck_title(md_text, plain_text) if doc_type=="tech_deck" else detect_deck_title(md_text, plain_text) or detect_doc_type_tenderish(full_text)

    if doc_type == "tech_deck":
        meta.update(summarize_tech_deck(md_text, plain_text, deck_cfg or {}, pdf, notes))

    elif doc_type in ("NIT","RFP","SBD","GCC","ITB"):
        text_norm = normalize_for_meta(md_text if md_text else plain_text)
        core = ["tender_no","organisation","emd_amount_inr","closing_datetime","opening_datetime","validity_days","epbg_percentage","epbg_duration_months","total_quantity"]
        extra = [k for k in (tender_cfg.get("fields") or {}).keys() if k not in core and k not in ("tender_title","doc_type")]
        from_this_module = globals()
        meta_get = from_this_module.get("extract_field_tender")
        for field in core + extra:
            meta[field] = meta_get(field, text_norm, full_text, tender_cfg, notes, tables)

        if sum_quantity_if_missing and not meta.get("total_quantity"):
            summed = safe_sum_item_quantities(text_norm)
            if summed:
                meta["total_quantity"] = summed
                notes.append({"field":"total_quantity","source":"summed_items","confidence":0.55})

        if (md_text=="" and looks_scanned(md_text, plain_text)) or looks_scanned(md_text, plain_text):
            notes.append({"field":"ocr","source":"heuristic","confidence":0.5,"value":True})

        if _HAS_NIM and os.getenv("NVIDIA_API_KEY"):
            try:
                want = ["emd_amount_inr","closing_datetime","opening_datetime","validity_days","epbg_percentage","epbg_duration_months","total_quantity"]
                missing = [k for k in want if not (str(meta.get(k) or "").strip())]
                if missing:
                    queries = [
                        "Bid closing date and time (end date/time)",
                        "Bid opening date and time",
                        "Earnest Money Deposit EMD amount INR",
                        "Bid validity in days",
                        "ePBG percentage and duration in months",
                        "Total quantity of items"
                    ]
                    out = extract_specific_fields_with_nims(full_text, fields=missing, custom_queries=queries)
                    for k,v in (out or {}).items():
                        if isinstance(v, str) and v.strip():
                            if k in ("closing_datetime","opening_datetime"):
                                d,t = extract_dates_from_phrase(v)
                                v = _normalize_datetime_ist(d,t) or v.strip()
                            meta[k] = v.strip()
                    notes.append({"field":"__nim__","source":"rerank+llm:dates","confidence":0.82})
            except NimClientError as e:
                notes.append({"field":"__nim__","source":"error","value":str(e),"confidence":0.0})

    else:  # hr / finance / sales / management
        text_norm = normalize_for_meta(md_text if md_text else plain_text)
    pat_loose = re.compile(rf"({label_regex})\s+(.+)", flags=re.I)
    for line in text.splitlines():
        if ":" in line:
            m = pat_colon.search(line)
            if m: return m.group(2).strip()
        m2 = pat_paren.search(line)
        if m2: return m2.group(2).strip()
        m3 = pat_loose.search(line)
        if m3: return m3.group(2).strip()
    return None

def extract_field_tender(field_name, text_norm, full_text, cfg, notes, tables) -> Optional[str]:
    # Reuse your previously working implementation here (unchanged).
    # This placeholder ensures the file runs if accidentally left blank,
    # but you should paste your robust version.
    return None


# ---------------- Quantity fallback (tender) ----------------
def safe_sum_item_quantities(text_norm: str) -> Optional[str]:
    total = 0; hits = 0
    for line in text_norm.splitlines():
        if re.search(r"\bTotal\s*Quantity\b", line, flags=re.I): continue
        if re.search(r"\bQuantity\b", line, flags=re.I):
            m = re.search(r"\bQuantity\b[^0-9]{0,20}(\d{1,7})\b", line, flags=re.I)
            if m:
                try: total += int(m.group(1)); hits += 1
                except ValueError: pass
    return str(total) if hits>0 else None


# ---------------- Rendering ----------------
def render_kv_table(title: str, mapping: Dict[str, object], order: Optional[List[str]]=None, skip: Optional[List[str]]=None) -> str:
    skip=set(skip or [])
    lines=[f"### {title}","| Field | Value |","|---|---|"]
    keys = order or list(mapping.keys())
    for k in keys:
        if k in skip: continue
        v = mapping.get(k)
        v_show = ("```json\n"+json.dumps(v, ensure_ascii=False, indent=2)[:2000]+"\n```") if isinstance(v,(list,dict)) else (str(v) if v not in (None,"") else "—")
        lines.append(f"| {k} | {v_show} |")
    return "\n".join(lines)

def render_doc_summary_table_deck(doc: DocMD) -> str:
    m = doc.meta
    title = m.get("deck_title") or clean_title_for_yaml(m.get("tender_title") or "")
    env_vars = ", ".join(m.get("env_vars") or []) or "—"
    contacts = ", ".join(m.get("contacts") or []) or "—"
    topics = ", ".join(m.get("topics") or []) or "—"
    ep_count = len(m.get("api_endpoints") or [])
    flow_count = len(m.get("flows") or [])
    has_data_model = "Yes" if m.get("data_model") else "No"
    pres_date = m.get("presentation_date") or "—"
    lines = [
        "| Field | Value |","|---|---|",
        f"| File | {doc.name} |",
        f"| Deck Title | {title or '—'} |",
        f"| Organisation | {m.get('organisation') or '—'} |",
        f"| Presentation Date (IST) | {pres_date} |",
        f"| Doc Type | {doc.doc_type or 'tech_deck'} |",
        f"| Topics | {topics} |",
        f"| Environment Variables | {env_vars} |",
        f"| API Endpoints (count) | {ep_count} |",
        f"| Flows (count) | {flow_count} |",
        f"| Data Model Provided | {has_data_model} |",
        f"| Contacts | {contacts} |",
    ]
    if m.get("api_endpoints"):
        lines.append("\n**Endpoints:**")
        for ep in m["api_endpoints"][:60]:
            lines.append(f"- `{ep.get('method')} {ep.get('path')}`")
        if len(m["api_endpoints"])>60:
            lines.append(f"- … and {len(m['api_endpoints'])-60} more")
    if m.get("flows"):
        lines.append("\n**Flows:**")
        for fl in m["flows"]:
            lines.append(f"- **{fl.get('name')}**")
            for s in fl.get("steps", [])[:12]:
                lines.append(f"  - {s}")
    if m.get("data_model"):
        pretty = json.dumps(m["data_model"], indent=2, ensure_ascii=False)[:1600]
        lines += ["\n**Data Model (excerpt):**","```json",pretty,"```"]
    return "\n".join(lines)

def render_doc_summary_table_tender(doc: DocMD) -> str:
    m = doc.meta
    rows = [
        ("File", doc.name),
        ("EMD Amount (INR)", m.get("emd_amount_inr") or "—"),
        ("ePBG Percentage (%)", m.get("epbg_percentage") or "—"),
        ("ePBG Duration (Months)", m.get("epbg_duration_months") or "—"),
        ("Bid End Date / Time", m.get("closing_datetime") or "—"),
        ("Bid Opening Date / Time", m.get("opening_datetime") or "—"),
        ("Bid Offer Validity (days)", m.get("validity_days") or "—"),
        ("Total Quantity", m.get("total_quantity") or "—"),
        ("Doc Type", doc.doc_type or "—"),
    ]
    return "\n".join(["| Field | Value |","|---|---|"]+[f"| {k} | {v} |" for k,v in rows])

def render_bundle_markdown(docs: List[DocMD]) -> str:
    # Front-matter merged
    merged = {
        "title": None, "tender_no": None, "organisation": None, "emd_amount_inr": None,
        "closing_datetime": None, "opening_datetime": None, "validity_days": None,
        "epbg_percentage": None, "epbg_duration_months": None, "total_quantity": None, "presentation_date": None
    }
    def pick(k): 
        for d in docs:
            v = d.meta.get(k)
            if v: return v
        return None
    merged["title"] = clean_title_for_yaml(pick("tender_title"))
    for k in list(merged.keys())[1:]: merged[k] = pick(k)

    fm = {
        "title": merged["title"] or "Document Bundle",
        "tender_no": merged["tender_no"] or "",
        "organisation": merged["organisation"] or "",
        "emd_amount_inr": merged["emd_amount_inr"] or "",
        "closing_datetime": merged["closing_datetime"] or "",
        "opening_datetime": merged["opening_datetime"] or "",
        "validity_days": merged["validity_days"] or "",
        "epbg_percentage": merged["epbg_percentage"] or "",
        "epbg_duration_months": merged["epbg_duration_months"] or "",
        "total_quantity": merged["total_quantity"] or "",
        "presentation_date": merged["presentation_date"] or "",
        "doc_types": [d.doc_type for d in docs],
        "source_files": [d.name for d in docs],
        "parser": "llamaparse",
        "parser_version": "5.6.0-NoiseXL+-FenceFix",
        "generated_at": _now_iso(),
        "notes": sum([d.notes for d in docs], []),
    }
    front = "---\n"+yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()+"\n---\n\n"

    title = merged["title"] or "Document Bundle"
    out = [front, f"# {title}\n", "> This Markdown contains a per-document summary and the complete text of each input document.\n"]
    for i, d in enumerate(docs, 1):
        out += ["---\n", f"## Document {i}: {d.name}"]
        if d.doc_type == "tech_deck": out.append(render_doc_summary_table_deck(d))
        elif d.doc_type in ("NIT","RFP","SBD","GCC","ITB"): out.append(render_doc_summary_table_tender(d))
        else: out.append(render_kv_table(d.doc_type.title()+" Summary" if d.doc_type else "Summary", d.meta))
        out.append("\n### Full Text (Markdown)\n")
        if d.md_text.strip(): out.append(d.md_text.strip())
        elif d.plain_text.strip(): out.append("_No markdown captured; showing plain-text fallback._\n```\n"+d.plain_text.strip()+"\n```")
        else: out.append("_No text could be extracted from this document._")
    return "\n".join(out)


# ---------------- CLI ----------------
def main():
    load_dotenv()
    ap = argparse.ArgumentParser(description="Schema-routed Markdown bundle")
    ap.add_argument("--pdf", nargs="+", type=Path, required=True)
    ap.add_argument("-o","--out", type=Path, required=True)
    ap.add_argument("--schema", type=str, default="auto",
        choices=["auto","tender","tech_deck","hr","finance","sales","management"])
    ap.add_argument("--sum-quantity", action="store_true")
    args = ap.parse_args()

    api_key = os.getenv("LLAMAPARSE_API_KEY")
    if not api_key: raise SystemExit("Missing LLAMAPARSE_API_KEY in .env")

    tender_cfg = load_schema_config("tender")
    deck_cfg   = load_schema_config("tech_deck")
    hr_cfg     = load_schema_config("hr")
    fin_cfg    = load_schema_config("finance")
    sales_cfg  = load_schema_config("sales")
    mgmt_cfg   = load_schema_config("management")

    docs=[]
    for p in args.pdf:
        if not p.exists(): raise SystemExit(f"File not found: {p}")
        docs.append(parse_one_doc(api_key, p, tender_cfg, deck_cfg, hr_cfg, fin_cfg, sales_cfg, mgmt_cfg, args.sum_quantity, args.schema))

    bundle = render_bundle_markdown(docs)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(bundle, encoding="utf-8")
    print(f"✅ Wrote Markdown → {args.out.resolve()}")

if __name__ == "__main__":
    main()