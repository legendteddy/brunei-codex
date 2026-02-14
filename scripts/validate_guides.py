#!/usr/bin/env python3
import pathlib
import re
import sys


REQUIRED_FRONT_MATTER_KEYS = [
    "title",
    "date",
    "last_updated",
    "category",
    "tags",
    "meta_description",
    "quick_answer",
    "sources",
]

MIN_WORDS = 1000
MAX_WORDS = 2200
MIN_FAQ = 5
MAX_FAQ = 10
MIN_INTERNAL_LINKS = 3


def split_front_matter(text: str):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.DOTALL)
    if not match:
        return None, text
    return match.group(1), match.group(2)


def count_words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def has_markdown_table(text: str) -> bool:
    lines = text.splitlines()
    for idx in range(len(lines) - 1):
        if "|" in lines[idx] and re.search(r"^\s*\|?\s*[-:]+(?:\s*\|\s*[-:]+)+\s*\|?\s*$", lines[idx + 1]):
            return True
    return False


def validate_guide(path: pathlib.Path):
    errors = []
    raw = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(raw)

    if front_matter is None:
        return [f"{path}: missing valid YAML front matter block."]

    for key in REQUIRED_FRONT_MATTER_KEYS:
        if not re.search(rf"(?m)^{re.escape(key)}\s*:", front_matter):
            errors.append(f"{path}: missing front matter key `{key}`.")

    if not re.search(r"(?mi)^\*\*Quick Answer:\*\*", body):
        errors.append(f"{path}: missing `**Quick Answer:**` section.")

    if not has_markdown_table(body):
        errors.append(f"{path}: missing markdown table.")

    faq_count = len(re.findall(r"(?mi)^\*\*Q:\s", body))
    if faq_count < MIN_FAQ or faq_count > MAX_FAQ:
        errors.append(
            f"{path}: FAQ count must be between {MIN_FAQ} and {MAX_FAQ}, found {faq_count}."
        )

    internal_link_count = len(
        re.findall(
            r"\]\((?:/guides/[^)]+|\{\{\s*['\"]/guides/[^'\"]+['\"]\s*\|\s*relative_url\s*\}\})\)",
            body,
        )
    )
    if internal_link_count < MIN_INTERNAL_LINKS:
        errors.append(
            f"{path}: must include at least {MIN_INTERNAL_LINKS} internal links, found {internal_link_count}."
        )

    word_count = count_words(body)
    if word_count < MIN_WORDS or word_count > MAX_WORDS:
        errors.append(
            f"{path}: word count must be between {MIN_WORDS}-{MAX_WORDS}, found {word_count}."
        )

    return errors


def main():
    guides_dir = pathlib.Path("_guides")
    if not guides_dir.exists():
        print("ERROR: `_guides` directory not found.")
        return 1

    guide_paths = sorted(guides_dir.glob("*.md"))
    if not guide_paths:
        print("ERROR: No guides found in `_guides`.")
        return 1

    all_errors = []
    for guide in guide_paths:
        all_errors.extend(validate_guide(guide))

    if all_errors:
        print("Guide validation failed:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    print(f"Guide validation passed for {len(guide_paths)} guide(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
