"""Funniest Lost Sock Status Update — entry for make.fun.

A single status update, written from the point of view of a lost sock
that ended up somewhere it does not belong.
"""

import os

ENTRY = "I left for one spin cycle and woke up inside a hotel minibar. Send help and fabric softener."


def validate(entry):
    """A valid entry is a single line of 1-120 characters."""
    return isinstance(entry, str) and 1 <= len(entry) <= 120 and "\n" not in entry


def main():
    if not validate(ENTRY):
        raise ValueError("ENTRY must be a single line of 1-120 characters")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
