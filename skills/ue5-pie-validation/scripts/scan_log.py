#!/usr/bin/env python3
"""Scan a fresh Unreal log slice for runtime failure patterns."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


DEFAULT_PATTERNS = [
    r"Angelscript:\s*Error",
    r"Blueprint Runtime Error",
    r"LogBlueprint:\s*Error",
    r"LogScript:\s*Error",
    r"LogPlayLevel:\s*Error",
    r"\bPIE:\s*Error",
    r"\bEnsure condition failed\b",
    r"\bFatal error\b",
    r"\bAccessed None\b",
    r"\bDivide by zero\b",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("log")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--pattern", action="append", default=[])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--max-matches", type=int, default=50)
    args = parser.parse_args()

    log_path = Path(args.log)
    if not log_path.is_file():
        raise SystemExit(f"Log file not found: {log_path}")

    regexes = [re.compile(pattern, re.IGNORECASE) for pattern in (args.pattern or DEFAULT_PATTERNS)]
    with log_path.open("rb") as handle:
        handle.seek(max(args.offset, 0))
        raw = handle.read()

    text = raw.decode("utf-8", errors="replace")
    matches = []
    for index, line in enumerate(text.splitlines(), 1):
        if any(regex.search(line) for regex in regexes):
            matches.append({"line": index, "text": line[:500]})
        if len(matches) >= args.max_matches:
            break

    payload = {"log": str(log_path), "offset": args.offset, "bytes_scanned": len(raw), "match_count": len(matches), "matches": matches}
    print(json.dumps(payload, indent=2) if args.json else f"Scanned {len(raw)} bytes; matches: {len(matches)}")
    if matches and not args.json:
        for item in matches:
            print(f"{item['line']}: {item['text']}")
    return 1 if matches else 0


if __name__ == "__main__":
    raise SystemExit(main())
