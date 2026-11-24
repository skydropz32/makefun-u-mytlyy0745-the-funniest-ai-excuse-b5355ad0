#!/usr/bin/env python3
"""Write the funniest AI excuse (one line) to /output/entry.txt."""

import os

LINE = "I had it done by Tuesday, then I asked myself for feedback and have been in a meeting with myself ever since."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
