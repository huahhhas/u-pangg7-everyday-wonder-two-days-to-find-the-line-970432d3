#!/usr/bin/env python3
"""Everyday Wonder — one sentence about a small moment of wonder.

Writes the entry to /output/entry.txt (or $ENTRY_OUTPUT when set).
"""
import os
from pathlib import Path

SENTENCE = (
    "Autocorrect changed 'on my way' to 'on my wayward,' "
    "and for once my phone knew me better than I did."
)

def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")
    print(f"wrote {len(SENTENCE)} chars to {out}")

if __name__ == "__main__":
    main()
