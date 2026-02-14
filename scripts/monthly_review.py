#!/usr/bin/env python3
import collections
import datetime as dt
import json
import pathlib
import re

from lib.front_matter import parse_front_matter_yaml, split_front_matter


ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"
CATALOG_PATH = ROOT / "data" / "topic_catalog.json"
REPORT_DIR = ROOT / "reports"


def parse_tags(front_matter: dict):
    tags = front_matter.get("tags") or []
    if isinstance(tags, list):
        return [str(t).strip() for t in tags if str(t).strip()]
    if isinstance(tags, str):
        return [t.strip() for t in tags.split(",") if t.strip()]
    return []


def parse_date(value: str):
    try:
        return dt.datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        return None


def load_guides():
    guides = []
    for p in sorted(GUIDES_DIR.glob("*.md")):
        raw = p.read_text(encoding="utf-8")
        fm_raw, _body, _full = split_front_matter(raw)
        fm = parse_front_matter_yaml(fm_raw or "")
        guides.append(
            {
                "path": p,
                "slug": p.stem,
                "title": str(fm.get("title") or ""),
                "category": str(fm.get("category") or ""),
                "last_updated": parse_date(str(fm.get("last_updated") or "")),
                "tags": parse_tags(fm),
            }
        )
    return guides


def main():
    today = dt.date.today()
    guides = load_guides()
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    existing_slugs = {g["slug"] for g in guides}

    by_category = collections.Counter(g["category"] for g in guides if g["category"])
    by_tag = collections.Counter(t for g in guides for t in g["tags"])
    stale = []
    for g in guides:
        if g["last_updated"] is None:
            stale.append((g["title"], "invalid date"))
            continue
        age = (today - g["last_updated"]).days
        if age > 180:
            stale.append((g["title"], f"{age} days old"))

    backlog = [t for t in catalog if t["slug"] not in existing_slugs]
    high_intent_backlog = [t for t in backlog if t.get("intent") == "high"][:10]

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / f"monthly-review-{today.isoformat()}.md"

    lines = [
        f"# Monthly Review - {today.isoformat()}",
        "",
        "## Content Inventory",
        f"- Total guides: {len(guides)}",
        "",
        "## Coverage by Category",
    ]

    if by_category:
        for k, v in sorted(by_category.items()):
            lines.append(f"- {k}: {v}")
    else:
        lines.append("- No guides found.")

    lines.extend(["", "## Top Topic Signals (Tag Frequency)"])
    for tag, count in by_tag.most_common(10):
        lines.append(f"- {tag}: {count}")
    if not by_tag:
        lines.append("- No tags found.")

    lines.extend(["", "## Refresh Queue (180+ days old or invalid date)"])
    if stale:
        for title, reason in stale:
            lines.append(f"- {title}: {reason}")
    else:
        lines.append("- None")

    lines.extend(["", "## Suggested Next High-Intent Topics"])
    if high_intent_backlog:
        for t in high_intent_backlog:
            lines.append(f"- {t['title']} (`/guides/{t['slug']}/`)")
    else:
        lines.append("- Backlog clear for high-intent catalog entries.")

    lines.extend(
        [
            "",
            "## Notes",
            "- This review is a structural proxy because analytics/citation telemetry is not yet integrated.",
            "- Add Search Console and analytics exports to improve monthly prioritization quality.",
        ]
    )

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Monthly report written: {report_path}")


if __name__ == "__main__":
    main()
