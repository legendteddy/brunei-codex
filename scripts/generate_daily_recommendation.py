#!/usr/bin/env python3
import argparse
import datetime as dt
from typing import Any

from generate_publish_queue import generate_queue
from lib.front_matter import parse_front_matter_yaml, split_front_matter

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"


def existing_guides() -> list[dict[str, str]]:
    results: list[dict[str, str]] = []
    for path in sorted(GUIDES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm_raw, _body, _full = split_front_matter(raw)
        fm = parse_front_matter_yaml(fm_raw or "")
        results.append(
            {
                "title": str(fm.get("title") or path.stem),
                "slug": path.stem,
                "category": str(fm.get("category") or ""),
            }
        )
    return results


def derive_internal_links(guides: list[dict[str, str]], limit: int = 4) -> list[str]:
    picks = guides[:limit]
    links: list[str] = []
    for g in picks:
        links.append(f"- [{g['title']}]({{{{ '/guides/{g['slug']}/' | relative_url }}}})")
    return links


def choose_topic(today: dt.date) -> dict[str, Any] | None:
    ranked = generate_queue(today=today, limit=1).get("queue") or []
    if not ranked:
        return None
    return ranked[0]


def print_recommendation(topic: dict[str, Any], today: dt.date, guides: list[dict[str, str]]) -> None:
    internal_links = derive_internal_links(guides)
    today_str = today.isoformat()
    year = today.year
    topic_title = f"{topic['title']} - Complete Guide {year}"

    print(f"## Daily Content Recommendation - {today_str}\n")
    print(f"**Suggested Topic:** {topic_title}\n")
    print("**Why This Topic:**")
    print("- Search intent: strong practical need with clear action steps for readers.")
    print("- Gap in current coverage: yes")
    print(f"- AI citation potential: {topic['ai_citation_potential']}")
    print(f"- Estimated search volume: weighted priority score {topic['scores']['total']}\n")
    print("**Outline:**")
    print("1. Quick Answer (2-3 sentences)")
    print("2. Main Sections:")
    print("   - Overview and who this guide is for")
    print("   - Step-by-step process with required documents/actions")
    print("   - Costs and timeline expectations")
    print("   - Common mistakes and risk reduction")
    print("3. Key Data Points to Include:")
    print("   - Comparison table of options/providers/process paths")
    print("   - Cost bands and timeline checkpoints")
    print("4. FAQ Questions (5-10)")
    print("5. Internal Links (to existing guides)")
    for link in internal_links:
        print(link)
    print("\n**Estimated Word Count:** 1200-1800 words  ")
    print("**Estimated Time:** 2 hours writing + 30 min editing\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AGENTS.md formatted daily recommendation.")
    parser.add_argument("--date", help="Date in YYYY-MM-DD format. Defaults to today.")
    args = parser.parse_args()

    today = dt.date.today()
    if args.date:
        today = dt.datetime.strptime(args.date, "%Y-%m-%d").date()

    topic = choose_topic(today)
    guides = existing_guides()

    if topic is None:
        print("All catalog topics are already covered. Add new items to data/topic_catalog.json.")
        return

    print_recommendation(topic, today, guides)


if __name__ == "__main__":
    main()
