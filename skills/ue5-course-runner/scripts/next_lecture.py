#!/usr/bin/env python3
"""Print the first unchecked Markdown task item."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ITEM_RE = re.compile(r"^\s*-\s\[\s\]\s+(?P<title>.+)$")
LINK_RE = re.compile(r"\[[^\]]+\]\((?P<path>[^)]+)\)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("todo")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    todo_path = Path(args.todo)
    if not todo_path.is_file():
        raise SystemExit(f"Task list not found: {todo_path}")

    for line_no, line in enumerate(todo_path.read_text(encoding="utf-8").splitlines(), 1):
        match = ITEM_RE.match(line)
        if not match:
            continue
        title = match.group("title").strip()
        link = LINK_RE.search(title)
        payload = {
            "line": line_no,
            "title": title,
            "linked_path": str((todo_path.parent / link.group("path")).resolve()) if link else None,
        }
        print(json.dumps(payload, indent=2) if args.json else f"{line_no}: {title}")
        return 0

    print(json.dumps({"line": None, "title": None, "linked_path": None}, indent=2) if args.json else "No unchecked items found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
