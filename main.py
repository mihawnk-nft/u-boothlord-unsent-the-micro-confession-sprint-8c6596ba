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

# Gate the kit seals: /output/entry.txt must be UTF-8 text of 1 to 260
# characters, and the judge's brief caps the message line at 200.
MAX_ENTRY_CHARS = 260
MAX_MESSAGE_CHARS = 200


def main() -> None:
    to_line, message = ENTRY.split("\n", 1)
    assert to_line.startswith("To: "), "entry must open with a To: line"
    assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS, "entry outside the gate"
    assert len(message) <= MAX_MESSAGE_CHARS, "message over 200 chars"
    assert message.strip(), "message must not be only white space"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
