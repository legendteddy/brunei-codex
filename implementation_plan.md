# BruneiCodex Development Plan - Autonomous Execution Blueprint

> **For AI agents**: Follow AGENTS.md Section 14 (Autonomy Protocol). Execute without permission requests in the Green Zone.

## Current State (2026-02-14)

| Metric | Value | Status |
|---|---|---|
| Total guides | **37** | ✅ Green |
| Compliance | 100% pass (37/37) | ✅ Green |
| Empty categories | **0** | ✅ Green |
| Catalog backlog | **69** topics remaining | ⚠️ Active |
| Phase 1 baseline | Complete | ✅ Green |

---

## Phase 1: Coverage Completion (Target: 24 guides)

**Status: COMPLETE**

All categories now have minimum viable coverage (2+ guides each).

---

## Phase 2: Cluster Deepening (Target: 50+ guides)

**Status: IN PROGRESS**

### Completed cluster items
- Housing: `renting-apartments-brunei`, `utilities-setup-brunei`
- Transport: `getting-drivers-license-brunei`, `public-transport-brunei`
- Daily Life: `grocery-shopping-brunei`, `mobile-internet-brunei`
- Work: `average-salaries-brunei`, `labor-laws-brunei`
- Health: `dental-care-brunei`, `pharmacy-otc-medicine-brunei`

### Next Priority Queue (continue in order)
1. `tax-obligations-rates-brunei`
2. `ecommerce-regulations-brunei`
3. `freelancing-remote-work-brunei`
4. `workplace-culture-guide-brunei`
5. `coworking-spaces-brunei`
6. `expat-community-social-groups-brunei`
7. `sports-fitness-facilities-brunei`
8. `climate-weather-patterns-brunei`
9. `laptop-buying-guide-brunei`
10. `smart-home-brunei-starter-guide`
11. `budget-dining-by-district-brunei`
12. `halal-dining-etiquette-brunei`
13. `cafe-guide-brunei`

Goal for this wave: publish the next 13 guides and move from 37 -> 50.

---

## Quality Gate (Every Session)

```bash
python scripts/validate_guides.py
python scripts/tone_lint.py
python scripts/generate_kpi.py
bundle _2.5.22_ exec jekyll build --trace
```

If any check fails: **fix in the same session**.

---

## Self-Evolution Cadence

| Cadence | Action |
|---|---|
| Every session | Write guides, fix issues, run validation, commit, push |
| Weekly | Run `weekly_maintenance.py`, refresh stale guides |
| Monthly | Run `monthly_review.py`, expand catalog, rebalance categories |
