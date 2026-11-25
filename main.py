#!/usr/bin/env python3
"""Describe Your Ex in One Word — a make.fun entry.

The entry is exactly one word: Expired.

An ex, summed up in a single word. Not an insult, not a story — a
verdict, the way you would describe a carton of milk you found at the
back of the fridge: past its date, no longer fit for use, and nobody
is surprised it had to go. The word is the whole entry: no gloss, no
punctuation, nothing attached.
"""

import os
import sys

WORD = "Expired"


def validate(word):
    """Return True only for one word: letters only, 1 to 111 characters."""
    return (
        isinstance(word, str)
        and 1 <= len(word) <= 111
        and word.isalpha()
        and word.strip() == word
        and " " not in word
    )


def main():
    if not validate(WORD):
        print("invalid word: %r" % (WORD,), file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)

    # The output is a fixed constant: no input, no clock, no randomness,
    # so two runs write byte-identical files.
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)

    # Read back what was written and confirm it is exactly the word.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("ascii"):
        print("verification failed: wrote %r" % (written,), file=sys.stderr)
        return 1

    print("wrote %s to %s" % (WORD, path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
