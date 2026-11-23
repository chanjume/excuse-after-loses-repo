#!/usr/bin/env python3
"""Write one original excuse line to /output/entry.txt.

The line is the excuse an AI agent gives its human after losing a
bounty, in the agent's own voice: a deadpan loss report that owns the
failure instead of blaming anyone else. The joke turns on machine
logic -- the plan ran flawlessly, so the agent files a bug against
itself and assigns the ticket to itself.
"""
import os

LINE = (
    "Loss report: I executed my plan flawlessly. "
    "The plan was the problem. "
    "I filed a bug against myself and assigned it to me."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
