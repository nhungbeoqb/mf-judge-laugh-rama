#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes the entry line to /output/entry.txt.

The line (v2 — punchline tightened: the ghost gets a ticket number):
  I told the new hire the coffee machine is haunted and only brews if you
  apologize to it — she apologized, it brewed, and now the ghost has its
  own ticket number.

Gate self-check (mirrors the sealed scorer): /output/entry.txt must be
UTF-8 text of 1 to 200 characters, not only white space.
"""

import os
import sys

LINE = (
    "I told the new hire the coffee machine is haunted and only brews if "
    "you apologize to it \u2014 she apologized, it brewed, and now the "
    "ghost has its own ticket number."
)


def main() -> int:
    text = LINE
    # Gate self-check: 1-200 chars, not only white space.
    if not (1 <= len(text) <= 200):
        print(f"gate fail: length {len(text)} not in 1..200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is only white space", file=sys.stderr)
        return 1
    text.encode("utf-8")  # raises if not valid UTF-8 text
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
