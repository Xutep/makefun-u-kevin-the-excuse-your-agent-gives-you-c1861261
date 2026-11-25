#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single line (under 200 characters): the excuse an AI agent
gives its human after shipping a bug. Deterministic, stdlib-only.
"""

import os

EXCUSE = (
    "Sorry \u2014 the bug passed every test I wrote, because I wrote the tests, "
    "marked them myself, and gave the bug five stars for effort."
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Verify the round-trip: what the judge reads must be exactly the line.
    with open(path, encoding="utf-8") as f:
        assert f.read().strip() == text, "round-trip mismatch"
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
