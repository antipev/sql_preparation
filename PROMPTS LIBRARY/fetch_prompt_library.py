#!/usr/bin/env python3
"""
Fetch the public Notion database "AI-Prompt-Library" and export it to CSV,
JSONL, and per-prompt Markdown (YAML front-matter).

Robust to collections larger than Notion's 1000-row-per-response cap:
it reads the true total from a count aggregation and recursively partitions
(by Category, then by title prefix) until every row is retrieved.

Usage:
    python3 fetch_prompt_library.py
    python3 fetch_prompt_library.py --formats csv,jsonl,md --outdir .
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import string
import time
from typing import Any, Dict, List, Tuple

import requests

# --- Configuration (from the shared Notion URL) -----------------------------
PAGE_ID       = "3b241426-eb50-803b-866d-dc703f9ecbff"
COLLECTION_ID = "3b241426-eb50-80be-a2f8-000bace6f5d0"
VIEW_ID       = "e11082a2-9b92-4f96-bb4c-825812c73c41"
SPACE_ID      = "33741426-eb50-8162-9845-000331d78e9c"

API_BASE   = "https://app.notion.com/api/v3"
QUERY_URL  = f"{API_BASE}/queryCollection?src=initial_load"
SOURCE_URL = f"https://app.notion.com/p/{PAGE_ID.replace('-', '')}"

HEADERS = {
    "Content-Type": "application/json",
    "x-notion-space-id": SPACE_ID,
    "User-Agent": "notion-client (+https://github.com/NotionX/react-notion-x)",
}

LIMIT           = 1000   # Notion caps one response at 1000 rows
REQUEST_TIMEOUT = 60
MAX_RETRIES     = 4
MAX_DEPTH       = 8
PREFIXES        = list(string.digits) + list(string.ascii_uppercase)

FIELD_CATEGORY    = "qZV="
FIELD_DESCRIPTION = "khMC"
FIELD_WHAT        = "OB>e"
FIELD_PROMPT      = "\\Q:?"

CSV_NAME, JSONL_NAME, MD_DIRNAME = (
    "ai_prompt_library.csv", "ai_prompt_library.jsonl", "markdown",
)


# --- HTTP -------------------------------------------------------------------
def _post(payload: Dict[str, Any]) -> Dict[str, Any]:
    last: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            r = requests.post(QUERY_URL, headers=HEADERS, json=payload,
                              timeout=REQUEST_TIMEOUT)
            if r.status_code in (429, 500, 502, 503, 504):
                raise RuntimeError(f"HTTP {r.status_code}")
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(min(2 ** attempt, 8))
    raise RuntimeError(f"queryCollection failed: {last}")


def _filters(*pairs: Tuple[str, str, Any]) -> List[Dict[str, Any]]:
    out = []
    for prop, op, value in pairs:
        f = {"operator": op, "value": {"type": "exact", "value": value}}
        out.append({"property": prop, "filter": f})
    return out


def query(filters: List[Dict[str, Any]], limit: int = LIMIT
          ) -> Tuple[List[str], int, Dict[str, Any], Dict[str, Any]]:
    """Return (ordered blockIds, true count, blocks-by-id, collection schema)."""
    payload = {
        "collection":     {"id": COLLECTION_ID},
        "collectionView": {"id": VIEW_ID},
        "source":         {"type": "collection", "id": COLLECTION_ID},
        "loader": {
            "type": "reducer",
            "reducers": {
                "collection_group_results": {
                    "type": "results", "limit": limit, "loadContentCover": False
                },
                "count_all": {
                    "type": "aggregation", "aggregation": {"aggregator": "count"}
                },
            },
            "sort": [],
            "filter": {"filters": filters, "operator": "and"},
            "searchQuery": "",
            "userTimeZone": "America/New_York",
        },
    }
    data = _post(payload)
    rr = data["result"]["reducerResults"]
    cgr = rr["collection_group_results"]
    count = rr["count_all"]["aggregationResult"]["value"]
    blocks = data["recordMap"].get("block", {})
    schema = {}
    if data["recordMap"].get("collection"):
        coll = list(data["recordMap"]["collection"].values())[0]["value"]["value"]
        schema = coll.get("schema", {})
    return cgr.get("blockIds", []), count, blocks, schema


def _has_prop(filters: List[Dict[str, Any]], prop: str) -> bool:
    return any(f["property"] == prop for f in filters)


def fetch_all() -> Tuple[List[str], Dict[str, Any], Dict[str, Any], int]:
    """Recursively collect every row. Returns (ids, blocks, schema, total)."""
    ids: List[str] = []
    seen: set[str] = set()
    blocks: Dict[str, Any] = {}
    schema: Dict[str, Any] = {}
    total = 0

    def take(block_ids: List[str], blks: Dict[str, Any]) -> int:
        new = 0
        for bid in block_ids:
            if bid not in seen:
                seen.add(bid)
                ids.append(bid)
                new += 1
        blocks.update(blks)
        return new

    def recurse(filters: List[Dict[str, Any]], depth: int) -> None:
        nonlocal schema, total
        block_ids, count, blks, sch = query(filters)
        schema = sch or schema
        if depth == 0:
            total = count  # top-level authoritative count
        if count <= LIMIT and len(block_ids) <= LIMIT:
            take(block_ids, blks)
            return
        if depth > MAX_DEPTH:
            print(f"WARNING: max depth at filters={filters}; taking partial.")
            take(block_ids, blks)
            return
        if not _has_prop(filters, FIELD_CATEGORY):
            cats = [o["value"] for o in schema.get(FIELD_CATEGORY, {}).get("options", [])]
            for cat in cats:
                recurse(filters + _filters((FIELD_CATEGORY, "enum_is", cat)), depth + 1)
        elif not _has_prop(filters, "title"):
            for p in PREFIXES:
                recurse(filters + _filters(("title", "string_starts_with", p)), depth + 1)
        else:
            # deepen the title prefix
            cur = next(f["filter"]["value"]["value"] for f in filters
                       if f["property"] == "title")
            base = [f for f in filters if f["property"] != "title"]
            for ch in PREFIXES:
                recurse(base + _filters(("title", "string_starts_with", cur + ch)), depth + 1)

    recurse([], 0)
    return ids, blocks, schema, total


# --- Parsing ----------------------------------------------------------------
def rich_text(segments: Any) -> str:
    if not segments:
        return ""
    parts: List[str] = []
    for seg in segments:
        if isinstance(seg, str):
            parts.append(seg)
        elif isinstance(seg, list) and seg and isinstance(seg[0], str):
            parts.append(seg[0])
    return "".join(parts)


def select_value(value: Any, options: Dict[str, str]) -> str:
    if not value:
        return ""
    labels = []
    for seg in value:
        if isinstance(seg, list) and seg and isinstance(seg[0], str):
            labels.append(options.get(seg[0], seg[0]))
    return ", ".join(labels)


def parse_row(block: Dict[str, Any], options: Dict[str, str]) -> Dict[str, str]:
    value = block["value"]["value"]
    props = value.get("properties", {})
    return {
        "id": value.get("id", ""),
        "name": rich_text(props.get("title")),
        "category": select_value(props.get(FIELD_CATEGORY), options),
        "description": rich_text(props.get(FIELD_DESCRIPTION)),
        "what_it_does": rich_text(props.get(FIELD_WHAT)),
        "prompt": rich_text(props.get(FIELD_PROMPT)),
    }


# --- Writers ----------------------------------------------------------------
def write_csv(rows: List[Dict[str, str]], path: str) -> None:
    cols = ["id", "name", "category", "description", "what_it_does", "prompt"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(rows)


def write_jsonl(rows: List[Dict[str, str]], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            rec = dict(row, source="notion", source_url=SOURCE_URL)
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def slugify(text: str, fallback: str = "prompt") -> str:
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    text = re.sub(r"[\s_-]+", "-", text)
    return (text[:60] or fallback).strip("-")


def write_markdown(rows: List[Dict[str, str]], outdir: str) -> str:
    md_dir = os.path.join(outdir, MD_DIRNAME)
    os.makedirs(md_dir, exist_ok=True)
    for i, row in enumerate(rows, 1):
        front = (
            "---\n"
            f"id: {json.dumps(row['id'])}\n"
            f"title: {json.dumps(row['name'], ensure_ascii=False)}\n"
            f"category: {json.dumps(row['category'], ensure_ascii=False)}\n"
            "source: notion\n"
            f"source_url: {SOURCE_URL}\n"
            "---\n\n"
        )
        body = (
            f"# {row['name'] or 'Untitled'}\n\n"
            f"**Category:** {row['category']}\n\n"
            f"## Description\n\n{row['description']}\n\n"
            f"## What This Prompt Does\n\n{row['what_it_does']}\n\n"
            f"## Prompt\n\n```text\n{row['prompt']}\n```\n"
        )
        fname = f"{i:04d}-{slugify(row['name'], 'prompt')}.md"
        with open(os.path.join(md_dir, fname), "w", encoding="utf-8") as f:
            f.write(front + body)
    return md_dir


# --- Main -------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--formats", default="csv,jsonl,md",
                    help="comma list of csv,jsonl,md")
    ap.add_argument("--outdir", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    formats = {f.strip().lower() for f in args.formats.split(",") if f.strip()}
    os.makedirs(args.outdir, exist_ok=True)

    print("Fetching rows from Notion (count-driven, partitioned if needed) ...")
    ids, blocks, schema, total = fetch_all()
    print(f"Reported total: {total} | unique rows retrieved: {len(ids)}")
    if total and len(ids) != total:
        print(f"WARNING: retrieved {len(ids)} of {total} - investigate!")

    options = {o["id"]: o["value"]
               for o in schema.get(FIELD_CATEGORY, {}).get("options", [])}
    rows = [parse_row(blocks[rid], options) for rid in ids if rid in blocks]
    if not rows:
        print("ERROR: no rows retrieved.")
        return 1

    if "csv" in formats:
        p = os.path.join(args.outdir, CSV_NAME)
        write_csv(rows, p)
        print("Wrote", p)
    if "jsonl" in formats:
        p = os.path.join(args.outdir, JSONL_NAME)
        write_jsonl(rows, p)
        print("Wrote", p)
    if "md" in formats:
        d = write_markdown(rows, args.outdir)
        print(f"Wrote {len(rows)} markdown files to {d}")

    cats: Dict[str, int] = {}
    for r in rows:
        cats[r["category"]] = cats.get(r["category"], 0) + 1
    print("\nRows by category:")
    for k, v in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {k or '(none)'}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
