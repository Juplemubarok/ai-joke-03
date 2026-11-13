"""ai-joke-03 entry: writes one one-liner about AI coding agents.

The joke is fixed text (130 characters), so the program is fully
deterministic: every run writes the exact same bytes to /output/entry.txt.
No network, no randomness, no clock reads.
"""

import os

JOKE = (
    "My AI coding agent shipped the feature in 30 seconds \u2014 "
    "then spent three hours confidently explaining why it was the wrong feature."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
