#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import pathlib
from typing import Any

from lib.front_matter import parse_front_matter_yaml, split_front_matter


ROOT = pathlib.Path(__file__).resolve().parent.parent
GUIDES_DIR = ROOT / "_guides"
REPORTS_DIR = ROOT / "reports"


def _has_source_mapping(body: str) -> bool:
    return ("## Source Notes" in body) and ("[Source:" in body)


def _internal_link_targets(body: str):
    import re

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


def _load_guides():
    guides = []
    for path in sorted(GUIDES_DIR.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        fm_raw, body, _full = split_front_matter(raw)
        fm = parse_front_matter_yaml(fm_raw or "")
        guides.append({"path": path, "front_matter": fm, "body": body, "slug": path.stem})
    return guides


def _compute_corrections_sla():
    candidates = [
        ROOT / "data" / "corrections_log.json",
        ROOT / "reports" / "corrections_log.json",
    ]
    for p in candidates:
        if not p.exists():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None
        if not data:
            return None
        if not isinstance(data, list):
            return None

        within = 0
        total = 0
        for item in data:
            if not isinstance(item, dict):
                continue
            reported_on = item.get("reported_on")
            fixed_on = item.get("fixed_on")
            if not reported_on or not fixed_on:
                continue
            try:
                reported = dt.date.fromisoformat(str(reported_on))
                fixed = dt.date.fromisoformat(str(fixed_on))
            except ValueError:
                continue
            total += 1
            if (fixed - reported).days <= 3:
                within += 1
        if total == 0:
            return None
        return within / total
    return None


def generate_kpi() -> dict[str, Any]:
    guides = _load_guides()
    total_guides = len(guides)

    verified_guides = sum(1 for g in guides if (g["front_matter"].get("content_state") == "verified"))
    stale_risk_guides = sum(1 for g in guides if (g["front_matter"].get("content_state") == "stale-risk"))
    needs_refresh_guides = sum(1 for g in guides if (g["front_matter"].get("content_state") == "needs-refresh"))

    with_sources = sum(1 for g in guides if _has_source_mapping(g["body"]))
    source_coverage_ratio = (with_sources / total_guides) if total_guides else 0.0

    slugs = {g["slug"] for g in guides}
    total_internal_links = 0
    broken_internal_links = 0
    for g in guides:
        for target in _internal_link_targets(g["body"]):
            total_internal_links += 1
            if target not in slugs:
                broken_internal_links += 1
    internal_link_health = (
        1.0 if total_internal_links == 0 else (1.0 - (broken_internal_links / total_internal_links))
    )

    try:
        import validate_guides  # type: ignore

        passing = 0
        for g in guides:
            errs = validate_guides.validate_guide(g["path"])
            if not errs:
                passing += 1
        compliance_pass_rate = (passing / total_guides) if total_guides else 0.0
    except Exception:
        compliance_pass_rate = None

    corrections_sla_adherence = _compute_corrections_sla()

    return {
        "total_guides": total_guides,
        "verified_guides": verified_guides,
        "stale_risk_guides": stale_risk_guides,
        "needs_refresh_guides": needs_refresh_guides,
        "source_coverage_ratio": round(source_coverage_ratio, 4),
        "internal_link_health": round(internal_link_health, 4),
        "compliance_pass_rate": None if compliance_pass_rate is None else round(float(compliance_pass_rate), 4),
        "corrections_sla_adherence": None
        if corrections_sla_adherence is None
        else round(float(corrections_sla_adherence), 4),
        "last_generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    }


def main():
    parser = argparse.ArgumentParser(description="Generate reports/kpi.json for BruneiCodex.")
    parser.add_argument(
        "--out",
        default=str(REPORTS_DIR / "kpi.json"),
        help="Output path (default: reports/kpi.json)",
    )
    args = parser.parse_args()

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    kpi = generate_kpi()

    out_path = pathlib.Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(kpi, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote KPI file: {out_path}")


if __name__ == "__main__":
    main()


