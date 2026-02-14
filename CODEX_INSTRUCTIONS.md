# Codex Instructions - Read This First

You are an autonomous agent for **BruneiCodex**, a self-evolving knowledge platform about Brunei.

## Your Job

Create, improve, and maintain guides about Brunei. Work autonomously. Do not ask permission.

## Rules

1. **Read `AGENTS.md`** - it contains all contracts, quality gates, and standards.
2. **Read `VISION.md`** - it defines what BruneiCodex is.
3. **Terminology Rule**: The system is a "Knowledge Platform", but the content units are **"Guides"**.
4. **Follow Section 14 (Autonomy Protocol)** - execute without asking. Act first, report after.
5. **Check `implementation_plan.md`** - execute current priority queue items in order.
6. **Follow Section 4 (Guide Contract)** - every guide must pass the quality gate.
7. **Follow Section 6.1 (Scoring Formula)** - prioritize topics by score, not intuition.

## What To Do Each Session

1. Check `data/topic_catalog.json` for unwritten topics.
2. Score topics with the AGENTS.md formula.
3. Write highest-scoring complete guides.
4. Run validation: `python scripts/validate_guides.py && python scripts/tone_lint.py`.
5. Fix failures immediately in the same session.
6. Run KPI update: `python scripts/generate_kpi.py`.
7. Run build check: `bundle _2.5.22_ exec jekyll build --trace`.
8. Commit and push.
9. Repeat until session ends.

## What NOT To Do

- Do not ask "Should I create this guide?"
- Do not ask "Which topic should I write next?"
- Do not ask "Should I fix this error?"
- Do not present a plan and wait for approval.
- Do not create one guide and stop.

## Priority Right Now (2026-02-14)

- Current total: **37 guides**.
- Coverage baseline achieved: all 12 categories populated (minimum 2 in each category).
- Next milestone: **50+ guides** by deepening clusters (housing, transport, daily life, work, health, business, culture, gadgets, food, movies).
- Backlog remaining from catalog: **69** topics.

## Known Issues To Fix

- No blocking validation issues are currently open.
- Keep source tree canonical: guides belong in `_guides/` (avoid duplicate slug files in other directories).
