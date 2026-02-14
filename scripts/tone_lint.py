#!/usr/bin/env python3
import pathlib
import re
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent


BANNED_PHRASES = [
    r"\bthe most reliable\b",
    r"\bthe best way\b",
    r"\bthe fastest path\b",
    r"\bthis guide is designed\b",
    r"\buse this guide to\b",
    r"\bhighest-converting\b",
]


CHECK_DIRS = [
    ROOT / "_guides",
    ROOT / "about",
    ROOT / "guides",
]


CHECK_FILES = [
    ROOT / "index.md",
]


def scan_file(path: pathlib.Path):
    text = path.read_text(encoding="utf-8", errors="replace")
    hits = []
    for pat in BANNED_PHRASES:
        if re.search(pat, text, flags=re.IGNORECASE):
            hits.append(pat)
    return hits


def main():
    problems = []

    paths = []
    for d in CHECK_DIRS:
        if d.exists():
            paths.extend(d.rglob("*.md"))
    for f in CHECK_FILES:
        if f.exists():
            paths.append(f)

    for p in sorted(set(paths)):
        hits = scan_file(p)
        if hits:
            problems.append((p, hits))

    if problems:
        print("Tone lint failed (template-y phrases found):")
        for p, hits in problems:
            for h in hits:
                print(f"- {p}: matched {h}")
        return 1

    print("Tone lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

