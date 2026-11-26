"""Funniest Lost Sock Status Update — entry for make.fun.

A single status update, written from the point of view of a lost sock
that ended up somewhere it does not belong.
"""

import os

def build_entry():
    """Assemble the status update from its two beats.

    The setup strands the sock somewhere it does not belong; the plea
    is the call for rescue. Joining the fragments keeps the exact
    winning line while making each beat editable on its own.
    """
    setup = "I left for one spin cycle and woke up inside a hotel minibar."
    plea = "Send help and fabric softener."
    return f"{setup} {plea}"


def validate_entry(entry):
    """Check the entry is a single line of 1-120 characters.

    Returns (ok, reason): ok is True when the entry is valid, otherwise
    reason names the exact rule that failed.
    """
    if not isinstance(entry, str):
        return False, "entry must be a string"
    if not 1 <= len(entry) <= 120:
        return False, f"entry must be 1-120 characters, got {len(entry)}"
    if "\n" in entry:
        return False, "entry must be a single line"
    return True, ""


def main():
    entry = build_entry()
    ok, reason = validate_entry(entry)
    if not ok:
        raise ValueError(f"invalid entry: {reason}")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
