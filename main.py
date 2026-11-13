"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke is fixed text (130 characters), so the program is fully
deterministic: every run writes the exact same bytes to /output/entry.txt.
No network, no randomness, no clock reads.

The joke is validated against the competition's limits (1-280 UTF-8
characters) before anything is written, and the output is written
atomically (temp file + rename) so a failed run never leaves a
half-written entry.txt behind.
"""

import os

JOKE = (
    "My AI coding agent shipped the feature in 30 seconds \u2014 "
    "then spent three hours confidently explaining why it was the wrong feature."
)

MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    if not MIN_CHARS <= len(JOKE.strip()) <= MAX_CHARS:
        raise ValueError(
            f"joke must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(JOKE.strip())}"
        )
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.replace(tmp_path, "/output/entry.txt")


if __name__ == "__main__":
    main()
