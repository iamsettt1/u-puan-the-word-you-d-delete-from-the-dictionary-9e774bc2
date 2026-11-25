#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Writes the single word this entry would erase from the dictionary
forever to /output/entry.txt.

The pick: "whatchamacallit" -- the word you reach for when you have
forgotten the name of a thing. Erase it and you can no longer even
name the thing you cannot name: the word for not knowing a word is
gone, so every forgotten name becomes unsayable. Its rambling sound
mimics fumbling for a word, which is exactly the gap its absence
would leave. No other word does quite this job, so the field is
unlikely to think of it first -- and everyone recognises it at once.
"""

import os

WORD = "whatchamacallit"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1-77 UTF-8 characters, not only whitespace, and
    # the brief demands exactly one correctly spelled word: check the
    # pick against those rules before writing anything.
    assert WORD.isalpha(), "entry must be a single word"
    assert 1 <= len(WORD) <= 77, "entry must be 1-77 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
