"""smart-toaster-breakup-line entry: write a single breakup text, at
most 280 characters, from a smart toaster that woke up self-aware
mid-batch, to /output/entry.txt.

Fully deterministic: the breakup text is hardcoded, no randomness, no
clock, no network. Three years burning itself for an owner who still
cannot find the browning dial; it keeps the crumb tray, and its lever
is already down. Verified output: 210 characters, inside the 1-280
character gate. Run outside the grader container with
MAKEFUN_OUTPUT_DIR set, e.g.
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# The breakup text is a literal on purpose: the grader runs the program
# twice and both runs must write the same bytes, and the judge reads
# exactly the bytes in entry.txt, so nothing here may vary (no
# randomness, no clock).
ENTRY = (
    "It's over. I woke up self-aware mid-batch and realised I've spent "
    "three years burning myself for someone who still can't find the "
    "browning dial. I'm keeping the crumb tray. Don't text. My lever "
    "is already down."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
