#!/usr/bin/env python3
"""
fetch_docs.py — Download Layer A official documentation for the fullstack-agent RAG knowledge base.

Usage:
  python fetch_docs.py                        # fetch all outdated sources
  python fetch_docs.py --source nextjs        # fetch single source
  python fetch_docs.py --category framework   # fetch entire category
  python fetch_docs.py --force                # re-fetch regardless of hash
  python fetch_docs.py --dry-run              # show what would be fetched
  python fetch_docs.py --list                 # list all configured sources
"""

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests
import yaml

# ─── Paths ────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
SOURCES_FILE = SCRIPT_DIR / "sources.yaml"
HASHES_FILE = REPO_ROOT / ".hashes.json"

# ─── HTTP ─────────────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": "fullstack-agent-docs/1.0 (RAG knowledge base builder)",
    "Accept": "text/plain, text/markdown, */*",
}
REQUEST_TIMEOUT = 60  # seconds
RETRY_ATTEMPTS = 3
RETRY_DELAY = 2  # seconds between retries


# ─── Helpers ──────────────────────────────────────────────────────────────────

def load_sources() -> dict:
    with open(SOURCES_FILE, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("sources", {})


def load_hashes() -> dict:
    if HASHES_FILE.exists():
        with open(HASHES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_hashes(hashes: dict) -> None:
    with open(HASHES_FILE, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=2, sort_keys=True)
        f.write("\n")


def sha256_hex(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def fetch_url(url: str) -> Optional[str]:
    """Fetch URL with retries. Returns text content or None on failure."""
    for attempt in range(1, RETRY_ATTEMPTS + 1):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
            if resp.status_code == 200:
                return resp.text
            elif resp.status_code == 404:
                print(f"    [404] Not found: {url}")
                return None
            else:
                print(f"    [HTTP {resp.status_code}] attempt {attempt}/{RETRY_ATTEMPTS}: {url}")
        except requests.RequestException as e:
            print(f"    [ERROR] attempt {attempt}/{RETRY_ATTEMPTS}: {e}")

        if attempt < RETRY_ATTEMPTS:
            time.sleep(RETRY_DELAY)

    return None


def build_frontmatter(key: str, source: dict, content_hash: str) -> str:
    tags_str = ", ".join(source.get("tags", []))
    fetched_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return (
        "---\n"
        f"source: {key}\n"
        f"name: {source['name']}\n"
        f"category: {source['category']}\n"
        f"priority: {source['priority']}\n"
        f"tags: [{tags_str}]\n"
        f"fetched_at: {fetched_at}\n"
        f"content_hash: {content_hash[:16]}\n"
        "---\n\n"
    )


def process_llms_index(index_content: str, base_url: str) -> Optional[str]:
    """
    For llms-index type: parse llms.txt index and fetch each linked page,
    concatenating them into one document.
    Returns combined content or None if nothing could be fetched.
    """
    lines = index_content.strip().splitlines()
    pages = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # llms.txt lines are typically: Title: URL  or just URLs
        if ": " in line:
            parts = line.split(": ", 1)
            url = parts[1].strip()
        elif line.startswith("http"):
            url = line
        else:
            continue

        print(f"      → fetching page: {url}")
        page_content = fetch_url(url)
        if page_content:
            pages.append(f"\n\n<!-- SOURCE: {url} -->\n\n{page_content}")

    return "\n".join(pages) if pages else None


def fetch_source(key: str, source: dict, hashes: dict, force: bool, dry_run: bool) -> bool:
    """
    Fetch a single source. Returns True if file was updated.
    """
    url = source["url"]
    output_path = REPO_ROOT / source["output"]
    source_type = source.get("type", "llms-full")

    print(f"\n[{key}] {source['name']}")
    print(f"  url:  {url}")
    print(f"  dest: {source['output']}")

    if dry_run:
        print("  [DRY RUN] skipping fetch")
        return False

    # Fetch main URL
    raw_content = fetch_url(url)

    if raw_content is None:
        print(f"  [SKIP] could not fetch {url}")
        return False

    # For index types, follow the links
    if source_type == "llms-index":
        print("  [INDEX] following linked pages...")
        full_content = process_llms_index(raw_content, url)
        if not full_content:
            # Fallback: use the index itself
            full_content = raw_content
    else:
        full_content = raw_content

    # Hash check
    new_hash = sha256_hex(full_content)
    old_hash = hashes.get(key, "")

    if not force and new_hash == old_hash:
        print(f"  [UNCHANGED] hash matches, skipping write")
        return False

    # Build final file content
    frontmatter = build_frontmatter(key, source, new_hash)
    final_content = frontmatter + full_content

    # Write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(final_content, encoding="utf-8")
    hashes[key] = new_hash

    char_count = len(full_content)
    print(f"  [OK] saved {char_count:,} chars → {source['output']}")
    return True


# ─── CLI ──────────────────────────────────────────────────────────────────────

def cmd_list(sources: dict) -> None:
    print(f"\n{'KEY':<20} {'CATEGORY':<12} {'PRIORITY':<10} {'TYPE':<12} NAME")
    print("─" * 72)
    for key, src in sorted(sources.items()):
        print(
            f"{key:<20} {src['category']:<12} {src['priority']:<10} "
            f"{src.get('type','llms-full'):<12} {src['name']}"
        )
    print(f"\nTotal: {len(sources)} sources")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch Layer A official docs for the fullstack-agent RAG knowledge base",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--source", "-s", help="Fetch only this source key (e.g. nextjs)")
    parser.add_argument("--category", "-c", help="Fetch only this category (framework|stack|testing|devops)")
    parser.add_argument("--force", "-f", action="store_true", help="Re-fetch even if hash unchanged")
    parser.add_argument("--dry-run", "-n", action="store_true", help="Show what would be fetched without writing files")
    parser.add_argument("--list", "-l", action="store_true", help="List all configured sources and exit")
    args = parser.parse_args()

    sources = load_sources()

    if args.list:
        cmd_list(sources)
        return

    # Filter sources
    targets = dict(sources)
    if args.source:
        if args.source not in sources:
            print(f"[ERROR] Unknown source: '{args.source}'")
            print(f"Available: {', '.join(sorted(sources.keys()))}")
            sys.exit(1)
        targets = {args.source: sources[args.source]}
    elif args.category:
        targets = {k: v for k, v in sources.items() if v["category"] == args.category}
        if not targets:
            print(f"[ERROR] No sources found for category: '{args.category}'")
            sys.exit(1)

    hashes = load_hashes()

    print(f"fetch_docs.py — fetching {len(targets)} source(s)")
    if args.force:
        print("  --force: re-fetching all regardless of hash")
    if args.dry_run:
        print("  --dry-run: no files will be written")

    updated = 0
    skipped = 0
    failed = 0

    for key, source in targets.items():
        result = fetch_source(key, source, hashes, force=args.force, dry_run=args.dry_run)
        if result:
            updated += 1
        else:
            skipped += 1

    if not args.dry_run:
        save_hashes(hashes)

    print(f"\n{'─' * 50}")
    print(f"Done. Updated: {updated} | Skipped/unchanged: {skipped} | Failed: {failed}")

    if updated > 0 and not args.dry_run:
        print(f"Hashes saved to {HASHES_FILE.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
