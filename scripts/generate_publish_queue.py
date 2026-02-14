#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import pathlib
from collections import Counter, defaultdict
from typing import Any

from lib.front_matter import parse_front_matter_yaml, split_front_matter

ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"
CATALOG_PATH = ROOT / "data" / "topic_catalog.json"
REPORTS_DIR = ROOT / "reports"

ALL_CATEGORIES = [
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
]

PRIORITY_CATEGORY_RELEVANCE = {
    "living": 5,
    "working": 5,
    "business": 5,
    "health": 5,
    "home-services": 5,
    "gadgets": 5,
    "events": 5,
    "food": 5,
    "education": 4,
    "activities": 4,
    "culture": 4,
    "movies": 4,
}

INTENT_MAP = {"high": 5, "medium": 3, "low": 1}
CITATION_MAP = {"high": 5, "medium": 3, "low": 1}


def _load_guides() -> tuple[set[str], Counter]:
    slugs: set[str] = set()
    by_category: Counter = Counter()
    for path in sorted(GUIDES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm_raw, _body, _full = split_front_matter(raw)
        fm = parse_front_matter_yaml(fm_raw or "")
        slugs.add(path.stem)
        category = str(fm.get("category") or "").strip()
        if category:
            by_category[category] += 1
    return slugs, by_category


def _load_catalog() -> list[dict[str, Any]]:
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def _coverage_gap_score(category_count: int) -> int:
    if category_count <= 0:
        return 5
    if category_count == 1:
        return 4
    if category_count == 2:
        return 2
    return 1


def _freshness_risk_score(topic: dict[str, Any], today: dt.date) -> int:
    seasonal = topic.get("seasonal_months") or []
    if today.month in seasonal:
        return 5

    next_month = 1 if today.month == 12 else today.month + 1
    if next_month in seasonal:
        return 4

    category = str(topic.get("category") or "")
    if category in {"events", "food", "movies", "gadgets"}:
        return 4
    if category in {"working", "business", "health", "home-services"}:
        return 3
    return 2


def _audience_relevance_score(topic: dict[str, Any]) -> int:
    category = str(topic.get("category") or "")
    return PRIORITY_CATEGORY_RELEVANCE.get(category, 3)



def _score_topic(topic: dict[str, Any], by_category: Counter, today: dt.date) -> dict[str, Any]:
    intent = INTENT_MAP.get(str(topic.get("intent") or "").lower(), 2)
    coverage_gap = _coverage_gap_score(by_category.get(str(topic.get("category") or ""), 0))
    freshness = _freshness_risk_score(topic, today)
    citation = CITATION_MAP.get(str(topic.get("ai_citation_potential") or "").lower(), 2)
    relevance = _audience_relevance_score(topic)

    weighted = (
        (intent * 0.30)
        + (coverage_gap * 0.25)
        + (freshness * 0.20)
        + (citation * 0.15)
        + (relevance * 0.10)
    )

    boost = 0.0
    total = weighted + boost

    return {
        "slug": topic.get("slug"),
        "title": topic.get("title"),
        "category": topic.get("category"),
        "intent": topic.get("intent"),
        "ai_citation_potential": topic.get("ai_citation_potential"),
        "seasonal_months": topic.get("seasonal_months") or [],
        "scores": {
            "intent": intent,
            "coverage_gap": coverage_gap,
            "freshness_risk": freshness,
            "citation_potential": citation,
            "audience_relevance": relevance,
            "weighted": round(weighted, 4),
            "priority_boost": boost,
            "total": round(total, 4),
        },
    }


def _sort_scored(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(items, key=lambda x: (x["scores"]["total"], x["scores"]["freshness_risk"]), reverse=True)


def _build_foundation_queue(
    scored: list[dict[str, Any]],
    existing_by_category: Counter,
    min_per_category: int,
    limit: int,
) -> list[dict[str, Any]]:
    by_cat: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in scored:
        by_cat[str(item.get("category") or "")].append(item)

    selected: list[dict[str, Any]] = []
    selected_slugs: set[str] = set()

    for cat in ALL_CATEGORIES:
        deficit = max(0, min_per_category - int(existing_by_category.get(cat, 0)))
        if deficit <= 0:
            continue

        ranked = _sort_scored(by_cat.get(cat, []))
        for item in ranked[:deficit]:
            slug = str(item.get("slug") or "")
            if slug and slug not in selected_slugs:
                selected.append(item)
                selected_slugs.add(slug)

    selected = _sort_scored(selected)

    for item in _sort_scored(scored):
        if len(selected) >= limit:
            break
        slug = str(item.get("slug") or "")
        if slug and slug not in selected_slugs:
            selected.append(item)
            selected_slugs.add(slug)

    return selected[:limit]


def generate_queue(today: dt.date, limit: int, mode: str = "general", min_per_category: int = 2) -> dict[str, Any]:
    existing_slugs, by_category = _load_guides()
    catalog = _load_catalog()
    backlog = [t for t in catalog if t.get("slug") not in existing_slugs]

    scored = [_score_topic(t, by_category, today) for t in backlog]
    sorted_scored = _sort_scored(scored)

    if mode == "foundation":
        queue = _build_foundation_queue(
            scored=sorted_scored,
            existing_by_category=by_category,
            min_per_category=min_per_category,
            limit=limit,
        )
    else:
        queue = sorted_scored[:limit]

    return {
        "generated_on": today.isoformat(),
        "mode": mode,
        "min_per_category": min_per_category,
        "total_existing_guides": len(existing_slugs),
        "total_backlog_topics": len(backlog),
        "category_inventory": {cat: int(by_category.get(cat, 0)) for cat in ALL_CATEGORIES},
        "queue": queue,
    }


def write_outputs(data: dict[str, Any], out_json: pathlib.Path, week1_out: pathlib.Path, week_size: int) -> None:
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    top = data["queue"][:week_size]
    lines = [
        f"# Week 1 Publish Plan - {data['generated_on']}",
        "",
        f"Mode: `{data['mode']}` (min/category `{data['min_per_category']}`).",
        "Generated from AGENTS weighting: Intent 0.30, Coverage Gap 0.25, Freshness Risk 0.20, Citation Potential 0.15, Audience Relevance 0.10.",
        "",
        "## Priority Order",
    ]

    for idx, item in enumerate(top, start=1):
        score = item["scores"]
        lines.extend(
            [
                f"{idx}. **{item['title']}** (`{item['slug']}`)",
                f"   - Category: `{item['category']}`",
                f"   - Total score: `{score['total']}` (weighted `{score['weighted']}`, boost `{score['priority_boost']}`)",
                f"   - Components: intent `{score['intent']}`, coverage `{score['coverage_gap']}`, freshness `{score['freshness_risk']}`, citation `{score['citation_potential']}`, relevance `{score['audience_relevance']}`",
            ]
        )

    lines.extend(
        [
            "",
            "## Execution Notes",
            "- Seasonal urgency is handled by freshness-risk scoring and category coverage gaps.",
            "- Use live lookup before drafting each guide and update `last_updated` + `verified_on`.",
            "- Keep minimum 5 internal links per new guide when relevant.",
        ]
    )

    week1_out.parent.mkdir(parents=True, exist_ok=True)
    week1_out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate AGENTS-formula publish queue and Week 1 plan.")
    parser.add_argument("--date", help="Date in YYYY-MM-DD format. Defaults to today.")
    parser.add_argument("--mode", choices=["general", "foundation"], default="general", help="Ranking mode.")
    parser.add_argument("--min-per-category", type=int, default=2, help="Minimum target guides/category in foundation mode.")
    parser.add_argument("--limit", type=int, default=50, help="Number of ranked backlog topics to emit.")
    parser.add_argument("--week-size", type=int, default=5, help="Number of top topics for Week 1 markdown plan.")
    parser.add_argument("--out-json", default=str(REPORTS_DIR / "publish_queue.json"), help="Output JSON path.")
    parser.add_argument("--out-week1", default=None, help="Output markdown path for Week 1 plan.")
    args = parser.parse_args()

    today = dt.date.today()
    if args.date:
        today = dt.datetime.strptime(args.date, "%Y-%m-%d").date()

    out_json = pathlib.Path(args.out_json)
    if args.out_week1:
        out_week1 = pathlib.Path(args.out_week1)
    else:
        out_week1 = REPORTS_DIR / f"week1-publish-plan-{today.isoformat()}.md"

    data = generate_queue(
        today=today,
        limit=args.limit,
        mode=args.mode,
        min_per_category=args.min_per_category,
    )
    write_outputs(data=data, out_json=out_json, week1_out=out_week1, week_size=args.week_size)

    print(f"Queue written: {out_json}")
    print(f"Week 1 plan written: {out_week1}")
    print(f"Backlog topics scored: {data['total_backlog_topics']}")


if __name__ == "__main__":
    main()


