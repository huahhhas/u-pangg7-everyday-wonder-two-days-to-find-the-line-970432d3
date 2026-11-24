#!/usr/bin/env python3
"""Everyday Wonder — one sentence about a small moment of wonder.

Writes the entry to /output/entry.txt (or $ENTRY_OUTPUT when set).
"""
import os
from pathlib import Path

SENTENCE = (
    "My reflection in the elevator mirror yawned a half-second before I did, "
    "and for a moment I wasn't sure which of us was the copy."
)

def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SENTENCE, encoding="utf-8")
    print(f"wrote {len(SENTENCE)} chars to {out}")

if __name__ == "__main__":
    main()
