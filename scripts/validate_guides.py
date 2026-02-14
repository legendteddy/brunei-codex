#!/usr/bin/env python3
import pathlib
import re
import sys

from lib.front_matter import parse_front_matter_yaml, split_front_matter


REQUIRED_FRONT_MATTER_KEYS = [
    "title",
    "date",
    "last_updated",
    "verified_on",
    "owner",
    "content_state",
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

ALLOWED_CONTENT_STATES = {"draft", "verified", "stale-risk", "needs-refresh", "archived"}
ALLOWED_CATEGORIES = {
    "living",
    "working",
    "business",
    "education",
    "health",
    "culture",
    "activities",
    "events",
    "food",
    "movies",
    "home-services",
    "gadgets",
}

def _has_source_mapping(body: str) -> bool:
    if not re.search(r"(?mi)^##\s+Source Notes\s*$", body):
        return False
    if not re.search(r"\[Source:\s*[^]]+\]", body):
        return False
    return True


def _requires_disclosure(front_matter: dict, body: str) -> bool:
    sources = front_matter.get("sources") or []
    source_text = ""
    if isinstance(sources, list):
        source_text = "\n".join(str(s) for s in sources if s)
    else:
        source_text = str(sources)

    combined = f"{source_text}\n{body}".lower()
    return "caramellabrunei.com" in combined or "affiliate" in combined or "sponsored" in combined


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
    front_matter_raw, body, _full = split_front_matter(raw)

    if front_matter_raw is None:
        return [f"{path}: missing valid YAML front matter block."]

    front_matter = parse_front_matter_yaml(front_matter_raw)

    for key in REQUIRED_FRONT_MATTER_KEYS:
        if key not in front_matter:
            errors.append(f"{path}: missing front matter key `{key}`.")

    content_state = str(front_matter.get("content_state") or "").strip()
    if content_state and content_state not in ALLOWED_CONTENT_STATES:
        errors.append(
            f"{path}: invalid `content_state` value `{content_state}` (allowed: {', '.join(sorted(ALLOWED_CONTENT_STATES))})."
        )

    category = str(front_matter.get("category") or "").strip()
    if category and category not in ALLOWED_CATEGORIES:
        errors.append(
            f"{path}: invalid `category` value `{category}` (allowed: {', '.join(sorted(ALLOWED_CATEGORIES))})."
        )

    if _requires_disclosure(front_matter, body) and "disclosure" not in front_matter:
        errors.append(f"{path}: missing `disclosure` front matter (sponsored/affiliate/vendor sources detected).")

    if not re.search(r"(?mi)^\*\*Quick Answer:\*\*", body):
        errors.append(f"{path}: missing `**Quick Answer:**` section.")

    if not has_markdown_table(body):
        errors.append(f"{path}: missing markdown table.")

    if not _has_source_mapping(body):
        errors.append(f"{path}: missing source mapping (`## Source Notes` and at least one inline `[Source: ...]`).")

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
