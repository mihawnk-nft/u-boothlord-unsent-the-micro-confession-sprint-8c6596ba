"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a "To:" line naming who it was meant for, and the unsent message
itself, one line written exactly as it was typed.

Pure Python standard library; no network, no secrets, no input.
"""

import os

ENTRY = (
    "To: Dad\n"
    "I practiced saying sorry in the car for three years and by the time "
    "I could say it without crying you were already gone."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
