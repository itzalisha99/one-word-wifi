#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry program.

Writes a single word describing my Wi-Fi to /output/entry.txt.
The word: peekaboo. My Wi-Fi plays peekaboo — the signal is here,
then gone, then back again, always when I need it most.
"""

import os

WORD = "peekaboo"


def validate(word):
    """Mirror the bounty gate: 1-20 chars, not only whitespace, one word."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not (1 <= len(word) <= 20):
        raise ValueError("entry must be 1 to 20 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")
    return word


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
