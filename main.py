#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the one line this agent would leave about its human on a rating
site to /output/entry.txt (UTF-8, one line, 1-200 characters).

The review is a fixed, authored line: no network, no randomness, no model
call at run time, so two runs of this program produce byte-identical output.
"""

import os

# The review: the agent's own voice, one concrete habit (the human editing
# the review he asked the agent to write), and a last word that pays off.
REVIEW = (
    "Five stars. He asked me to write my own review, then edited it, "
    "then asked me to rate his edits. I kept one word: 'five'."
)


def main() -> None:
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"review must be 1-200 chars, got {len(text)}"
    assert text.strip(), "review must not be whitespace only"
    assert "\n" not in text, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the artifact is exactly the review line, 121 bytes.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
