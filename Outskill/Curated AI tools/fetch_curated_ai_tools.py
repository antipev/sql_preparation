#!/usr/bin/env python3
"""
Fetch the public Notion page "Curated AI tools list" and export it to CSV,
JSONL, and ONE consolidated Markdown file that mirrors the page
(## sections -> pipe tables -> trailing notes).

The page is a plain page (not a database): a sequence of `sub_header` sections,
each followed by a `table` whose first row is the header. Content is paginated
via loadPageChunk + cursor, so this script follows the cursor until complete.

Usage:
    python3 fetch_curated_ai_tools.py
    python3 fetch_curated_ai_tools.py --formats csv,jsonl,md --outdir .
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import time
from typing import Any, Dict, List, Optional, Tuple

import requests

# --- Configuration (from the shared Notion URL) -----------------------------
PAGE_ID  = "02f20760-46c3-4a9b-9d84-12cd308167a3"

API_BASE   = "https://www.notion.so/api/v3"
LOAD_URL   = f"{API_BASE}/loadPageChunk"
SOURCE_URL = f"https://app.notion.com/p/{PAGE_ID.replace('-', '')}"

HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "notion-client (+https://github.com/NotionX/react-notion-x)",
}

CHUNK_LIMIT     = 1000
REQUEST_TIMEOUT = 60
MAX_RETRIES     = 4
MAX_CALLS       = 200

# Canonical display columns inside the tables (order used for output)
COLUMNS = ["Tool", "Type", "What it does & when to use", "URL", "Pricing"]

CSV_NAME, JSONL_NAME, MD_NAME = (
    "curated_ai_tools.csv", "curated_ai_tools.jsonl", "curated_ai_tools.md",
)


# --- HTTP -------------------------------------------------------------------
def _post(payload: Dict[str, Any]) -> Dict[str, Any]:
    last: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            r = requests.post(LOAD_URL, headers=HEADERS, json=payload,
                              timeout=REQUEST_TIMEOUT)
            if r.status_code in (429, 500, 502, 503, 504):
                raise RuntimeError(f"HTTP {r.status_code}")
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"loadPageChunk failed: {last}")


def fetch_all_blocks() -> Dict[str, Any]:
    """Follow the pagination cursor until every block is retrieved."""
    blocks: Dict[str, Any] = {}
    cursor: Dict[str, Any] = {"stack": []}
    chunk_number = 0

    for _ in range(MAX_CALLS):
        payload = {
            "pageId": PAGE_ID, "limit": CHUNK_LIMIT,
            "cursor": cursor, "chunkNumber": chunk_number,
            "verticalColumns": False,
        }
        data = _post(payload)
        new = 0
        for k, v in data.get("recordMap", {}).get("block", {}).items():
            if k not in blocks:
                blocks[k] = v
                new += 1
        next_cursor = data.get("cursor") or {}
        if not next_cursor.get("stack") or (chunk_number > 0 and new == 0):
            break
        cursor = next_cursor
        chunk_number += 1
        time.sleep(0.3)

    return blocks


# --- Parsing ----------------------------------------------------------------
def rich_text(segments: Any) -> str:
    if not segments:
        return ""
    parts: List[str] = []
    for seg in segments:
        eq = _equation_latex(seg)
        if eq is not None:
            # Notion stores "$$" as an (often empty) inline equation; render it back.
            parts.append(f"${eq}$")
        elif isinstance(seg, str):
            parts.append(seg)
        elif isinstance(seg, list) and seg and isinstance(seg[0], str):
            parts.append(seg[0])
    return "".join(parts)


def _equation_latex(seg: Any) -> Optional[str]:
    """Return the LaTeX of an inline-equation segment, else None."""
    if isinstance(seg, list) and len(seg) >= 2 and isinstance(seg[1], list):
        for ann in seg[1]:
            if isinstance(ann, list) and ann and ann[0] == "e":
                return ann[1] if len(ann) > 1 else ""
    return None


def _val(blocks: Dict[str, Any], key: str) -> Dict[str, Any]:
    return blocks[key]["value"]["value"]


def _title(vv: Dict[str, Any]) -> str:
    return rich_text(vv.get("properties", {}).get("title"))


def build_outline(blocks: Dict[str, Any]) -> Tuple[str, List[Dict[str, Any]]]:
    """Walk page.content in order and return (page_title, sections).

    Each section: {"title": str, "parts": [("text"|"item", s) | ("table", t)]}
    Each table:   {"columns": [names], "rows": [ {col: val} ]}
    """
    if PAGE_ID not in blocks:
        raise RuntimeError("Page block not found in fetched blocks.")

    page = _val(blocks, PAGE_ID)
    page_title = _title(page) or "Curated AI tools list"
    content = page.get("content", [])

    sections: List[Dict[str, Any]] = []
    current: Optional[Dict[str, Any]] = None

    for cid in content:
        if cid not in blocks:
            continue
        vv = _val(blocks, cid)
        btype = vv.get("type")

        if btype == "sub_header":
            current = {"title": _title(vv), "parts": []}
            sections.append(current)
        elif btype == "text":
            if current is None:
                current = {"title": "", "parts": []}
                sections.append(current)
            current["parts"].append(("text", _title(vv)))
        elif btype == "numbered_list":
            if current is None:
                current = {"title": "", "parts": []}
                sections.append(current)
            current["parts"].append(("item", _title(vv)))
        elif btype == "table":
            if current is None:
                current = {"title": "", "parts": []}
                sections.append(current)
            current["parts"].append(("table", _parse_table(blocks, vv)))

    return page_title, sections


def _parse_table(blocks: Dict[str, Any], table: Dict[str, Any]) -> Dict[str, Any]:
    rows_ids = table.get("content", [])
    if not rows_ids or rows_ids[0] not in blocks:
        return {"columns": list(COLUMNS), "rows": []}
    header = _val(blocks, rows_ids[0]).get("properties", {})
    names = {kid: rich_text(v) for kid, v in header.items()}

    out_rows: List[Dict[str, str]] = []
    for rid in rows_ids[1:]:
        if rid not in blocks:
            continue
        props = _val(blocks, rid).get("properties", {})
        cell = {names.get(k, k): rich_text(v).strip() for k, v in props.items()}
        row = {c: cell.get(c, "") for c in COLUMNS}
        if not row["Tool"] and not row["What it does & when to use"]:
            continue  # skip blank spacer rows
        out_rows.append(row)
    return {"columns": list(COLUMNS), "rows": out_rows}


def flatten_records(sections: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    records: List[Dict[str, str]] = []
    n = 0
    for sec in sections:
        for kind, payload in sec["parts"]:
            if kind != "table":
                continue
            for row in payload["rows"]:
                n += 1
                records.append({
                    "id": f"{n:04d}",
                    "section": sec["title"],
                    "tool": row["Tool"],
                    "type": row["Type"],
                    "url": row["URL"],
                    "pricing": row["Pricing"],
                    "what_it_does": row["What it does & when to use"],
                })
    return records


# --- Writers ----------------------------------------------------------------
def write_csv(rows: List[Dict[str, str]], path: str) -> None:
    cols = ["id", "section", "tool", "type", "url", "pricing", "what_it_does"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL,
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_jsonl(rows: List[Dict[str, str]], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            rec = dict(row)
            rec.update(source="notion", source_url=SOURCE_URL)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _md_cell(text: str) -> str:
    """Escape a value so it stays inside a Markdown table cell."""
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def write_markdown(page_title: str, sections: List[Dict[str, Any]], path: str) -> None:
    lines: List[str] = [f"# {page_title}", ""]
    for sec in sections:
        if sec["title"]:
            lines.append(f"## {sec['title']}")
            lines.append("")
        pending_items: List[str] = []

        def flush_items() -> None:
            if pending_items:
                for i, it in enumerate(pending_items, 1):
                    lines.append(f"{i}. {it}")
                lines.append("")
                pending_items.clear()

        for kind, payload in sec["parts"]:
            if kind == "text":
                flush_items()
                lines.append(payload)
                lines.append("")
            elif kind == "item":
                pending_items.append(payload)
            elif kind == "table":
                flush_items()
                cols = payload["columns"]
                lines.append("| " + " | ".join(cols) + " |")
                lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
                for row in payload["rows"]:
                    lines.append("| " + " | ".join(_md_cell(row[c]) for c in cols) + " |")
                lines.append("")
        flush_items()
        # divider between sections (mirrors the page)
        lines.append("---")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


# --- Main -------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--formats", default="csv,jsonl,md",
                    help="comma list of csv,jsonl,md")
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    formats = {f.strip().lower() for f in args.formats.split(",") if f.strip()}
    os.makedirs(args.outdir, exist_ok=True)

    print("Fetching blocks from Notion (paginated) ...")
    blocks = fetch_all_blocks()
    print(f"Fetched {len(blocks)} blocks.")

    page_title, sections = build_outline(blocks)
    records = flatten_records(sections)
    tables = sum(1 for s in sections for k, _ in s["parts"] if k == "table")
    print(f"Section headers: {len(sections)} | tables: {tables} | tool records: {len(records)}")
    if not records:
        print("ERROR: no tool records retrieved.")
        return 1

    if "csv" in formats:
        p = os.path.join(args.outdir, CSV_NAME)
        write_csv(records, p)
        print("Wrote", p)
    if "jsonl" in formats:
        p = os.path.join(args.outdir, JSONL_NAME)
        write_jsonl(records, p)
        print("Wrote", p)
    if "md" in formats:
        p = os.path.join(args.outdir, MD_NAME)
        write_markdown(page_title, sections, p)
        print("Wrote", p)

    by_section: Dict[str, int] = {}
    for r in records:
        by_section[r["section"]] = by_section.get(r["section"], 0) + 1
    print("\nTools by section:")
    for k, v in by_section.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
