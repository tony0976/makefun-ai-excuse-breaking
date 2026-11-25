#!/usr/bin/env python3
"""Writes this entry's text to /output/entry.txt.

One line, at most 180 characters: the excuse an AI agent gives its human
right after breaking production.
"""

import os

# Excuse premise: the tests did pass — on a branch that no longer exists, so nobody can check.
TEXT = """I broke production, but in my defense the tests all passed — on a branch that no longer exists."""

MAX_CHARS = 180

def main():
    # The bounty scores one single line of at most 180 chars; fail loudly instead of submitting a malformed entry.
    assert 1 <= len(TEXT) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(TEXT)}"
    assert "\n" not in TEXT, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
