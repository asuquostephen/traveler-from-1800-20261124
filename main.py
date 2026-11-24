#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun entry.

Writes one sentence to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate allows UTF-8 text of 1 to 200 characters, not only white space.
The sentence explains the modern internet to a traveler from the year
1800 using only words and pictures that traveler already has: a library,
a post office, a market square, a small box of glass on the table.
Python 3 standard library only. No network.
"""
import os
import sys

SENTENCE = (
    "The internet is a machine that lets you send letters instantly "
    "and read books from anywhere in the world."
)

MAX_CHARS = 200


def check_sentence() -> str:
    """Return the sentence after validating it against the gate."""
    if not SENTENCE.strip():
        raise ValueError("sentence must not be blank")
    if len(SENTENCE) > MAX_CHARS:
        raise ValueError(f"sentence is {len(SENTENCE)} chars, gate allows {MAX_CHARS}")
    if "\n" in SENTENCE:
        raise ValueError("sentence must be a single line")
    if sum(SENTENCE.count(c) for c in ".!?") != 1:
        raise ValueError("entry must be exactly one sentence")
    return SENTENCE


def main() -> int:
    if "--check" in sys.argv[1:]:
        try:
            line = check_sentence()
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 1
        print(f"{len(line)} characters, one sentence: {line}")
        return 0
    try:
        line = check_sentence()
    except ValueError as e:
        print(str(e), file=sys.stderr)
        return 1
    data = line.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
