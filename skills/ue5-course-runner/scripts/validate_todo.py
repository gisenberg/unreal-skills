#!/usr/bin/env python3
"""Fail if a Markdown task list still contains unchecked items."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


UNCHECKED_RE = re.compile(r"^\s*-\s\[\s\]\s+(?P<title>.+)$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("todo")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    todo_path = Path(args.todo)
    if not todo_path.is_file():
        raise SystemExit(f"Task list not found: {todo_path}")

    unchecked = [
        {"line": line_no, "title": match.group("title").strip()}
        for line_no, line in enumerate(todo_path.read_text(encoding="utf-8").splitlines(), 1)
        if (match := UNCHECKED_RE.match(line))
    ]
    payload = {"todo": str(todo_path), "unchecked_count": len(unchecked), "unchecked": unchecked}
    print(json.dumps(payload, indent=2) if args.json else f"Unchecked items: {len(unchecked)}")
    if unchecked and not args.json:
        for item in unchecked:
            print(f"{item['line']}: {item['title']}")
    return 1 if unchecked else 0


if __name__ == "__main__":
    raise SystemExit(main())
