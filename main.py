#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line, exactly as it was typed, with nothing after it.

The confession is deterministic: the same text every run.
"""

import os

TO_LINE = "To: the girl from table six"

MESSAGE = (
    "I wrote your number on my hand and washed it off before "
    "I could decide if I was brave or just lonely."
)


def build_entry() -> str:
    """Compose the two-part confession as a single text."""
    return TO_LINE + "\n" + MESSAGE + "\n"


def validate_entry(text: str) -> None:
    """Check the entry against the competition gate before writing.

    Gate: UTF-8 text of 1 to 260 characters, not only white space,
    exactly two parts (a To: line and one message line of at most
    200 characters), with nothing after the message.
    """
    if not 1 <= len(text) <= 260:
        raise ValueError("entry must be 1-260 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    if not lines[0].startswith("To: "):
        raise ValueError("first line must be a To: line")
    if len(lines[1]) > 200:
        raise ValueError("message must be at most 200 characters")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = build_entry()
    validate_entry(text)
    data = text.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(data)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
