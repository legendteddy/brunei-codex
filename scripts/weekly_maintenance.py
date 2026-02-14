#!/usr/bin/env python3
import argparse
import datetime as dt
import pathlib
import re
import sys

from lib.front_matter import parse_front_matter_yaml, split_front_matter


ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"
REPORT_DIR = ROOT / "reports"

REQUIRED_KEYS = [
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


def parse_date(raw: str):
    try:
        return dt.datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        return None


def collect_guides():
    guides = []
    for path in sorted(GUIDES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm_raw, body, _full = split_front_matter(raw)
        fm = parse_front_matter_yaml(fm_raw or "")
        guides.append(
            {
                "path": path,
                "front_matter": fm,
                "body": body,
                "slug": path.stem,
            }
        )
    return guides


def internal_link_targets(body: str):
    matches = re.findall(
        r"\]\(/guides/([^)\/]+)/\)|\]\(\{\{\s*['\"]/guides/([^'\"/]+)/['\"]\s*\|\s*relative_url\s*\}\}\)",
        body,
    )
    targets = []
    for old_style, liquid_style in matches:
        slug = old_style or liquid_style
        if slug:
            targets.append(slug)
    return targets


def run_audit():
    today = dt.date.today()
    guides = collect_guides()
    slugs = {g["slug"] for g in guides}

    missing_key_errors = []
    broken_internal_links = []
    stale_guides = []

    for g in guides:
        fm = g["front_matter"]
        for key in REQUIRED_KEYS:
            if key not in fm:
                missing_key_errors.append(f"{g['path']}: missing `{key}`")

        for target in internal_link_targets(g["body"]):
            if target not in slugs:
                broken_internal_links.append(f"{g['path']}: broken internal link `/guides/{target}/`")

        last_updated_raw = str(fm.get("last_updated") or "")
        last_updated = parse_date(last_updated_raw)
        if last_updated is None:
            stale_guides.append(f"{g['path']}: invalid `last_updated` date")
        else:
            age_days = (today - last_updated).days
            if age_days > 180:
                stale_guides.append(f"{g['path']}: stale ({age_days} days old)")

    return {
        "guide_count": len(guides),
        "missing_key_errors": missing_key_errors,
        "broken_internal_links": broken_internal_links,
        "stale_guides": stale_guides,
    }


def write_report(result: dict):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    report_path = REPORT_DIR / f"weekly-maintenance-{today}.md"

    lines = [
        f"# Weekly Maintenance Report - {today}",
        "",
        f"- Total guides: {result['guide_count']}",
        f"- Missing metadata issues: {len(result['missing_key_errors'])}",
        f"- Broken internal links: {len(result['broken_internal_links'])}",
        f"- Stale/invalid dates: {len(result['stale_guides'])}",
        "",
        "## Missing Metadata",
    ]
    if result["missing_key_errors"]:
        lines.extend([f"- {i}" for i in result["missing_key_errors"]])
    else:
        lines.append("- None")

    lines.extend(["", "## Broken Internal Links"])
    if result["broken_internal_links"]:
        lines.extend([f"- {i}" for i in result["broken_internal_links"]])
    else:
        lines.append("- None")

    lines.extend(["", "## Stale Guides (180+ days or invalid date)"])
    if result["stale_guides"]:
        lines.extend([f"- {i}" for i in result["stale_guides"]])
    else:
        lines.append("- None")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report_path


def main():
    parser = argparse.ArgumentParser(description="Run weekly BruneiVerse maintenance checks.")
    parser.add_argument("--write-report", action="store_true", help="Write markdown report to reports/")
    args = parser.parse_args()

    result = run_audit()

    print(f"Guides: {result['guide_count']}")
    print(f"Missing metadata issues: {len(result['missing_key_errors'])}")
    print(f"Broken internal links: {len(result['broken_internal_links'])}")
    print(f"Stale/invalid dates: {len(result['stale_guides'])}")

    if args.write_report:
        report = write_report(result)
        print(f"Report written: {report}")

    if result["missing_key_errors"] or result["broken_internal_links"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
