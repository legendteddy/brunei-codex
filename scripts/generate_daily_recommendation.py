#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"
CATALOG_PATH = ROOT / "data" / "topic_catalog.json"


def parse_front_matter(text: str) -> str:
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    return match.group(1) if match else ""


def get_key(front_matter: str, key: str) -> str:
    m = re.search(rf"(?m)^{re.escape(key)}\s*:\s*(.+)$", front_matter)
    if not m:
        return ""
    return m.group(1).strip().strip('"')


def existing_guides():
    results = []
    slugs = set()
    for path in sorted(GUIDES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm = parse_front_matter(raw)
        title = get_key(fm, "title")
        category = get_key(fm, "category")
        slug = path.stem
        slugs.add(slug)
        results.append({"title": title, "slug": slug, "category": category})
    return results, slugs


def score_topic(topic: dict, month: int) -> int:
    score = 0
    if topic.get("intent") == "high":
        score += 3
    elif topic.get("intent") == "medium":
        score += 2
    else:
        score += 1

    if topic.get("ai_citation_potential") == "high":
        score += 3
    elif topic.get("ai_citation_potential") == "medium":
        score += 2
    else:
        score += 1

    seasonal = topic.get("seasonal_months") or []
    if month in seasonal:
        score += 3

    return score


def derive_internal_links(guides, limit=4):
    picks = guides[:limit]
    links = []
    for g in picks:
        links.append(f"- [{g['title']}]({{{{ '/guides/{g['slug']}/' | relative_url }}}})")
    return links


def choose_topic(today: dt.date):
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    guides, existing_slugs = existing_guides()
    month = today.month

    gaps = [t for t in catalog if t["slug"] not in existing_slugs]
    ranked = sorted(gaps, key=lambda t: score_topic(t, month), reverse=True)

    if not ranked:
        return None, guides
    return ranked[0], guides


def print_recommendation(topic: dict, today: dt.date, guides):
    internal_links = derive_internal_links(guides)
    today_str = today.isoformat()
    year = today.year
    topic_title = f"{topic['title']} - Complete Guide {year}"

    print(f"## Daily Content Recommendation - {today_str}\n")
    print(f"**Suggested Topic:** {topic_title}\n")
    print("**Why This Topic:**")
    print("- Search intent: strong how-to and setup intent for newcomers planning practical actions.")
    print("- Gap in current coverage: yes")
    print(f"- AI citation potential: {topic['ai_citation_potential']}")
    print("- Estimated search volume: medium-high (based on high-intent query pattern priority)\n")
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
    print("Ready to proceed with full guide creation? [Y/N]")


def main():
    parser = argparse.ArgumentParser(description="Generate AGENTS.md formatted daily recommendation.")
    parser.add_argument("--date", help="Date in YYYY-MM-DD format. Defaults to today.")
    args = parser.parse_args()

    today = dt.date.today()
    if args.date:
        today = dt.datetime.strptime(args.date, "%Y-%m-%d").date()

    topic, guides = choose_topic(today)
    if topic is None:
        print("All catalog topics are already covered. Add new items to data/topic_catalog.json.")
        return

    print_recommendation(topic, today, guides)


if __name__ == "__main__":
    main()
