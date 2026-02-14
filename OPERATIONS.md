# BruneiCodex Operations

## Daily (15-30 min)

Generate daily topic recommendation:

```bash
python scripts/generate_daily_recommendation.py
```

Optional date override:

```bash
python scripts/generate_daily_recommendation.py --date 2026-02-14
```

Generate roadmap publish queue + Week 1 plan (Phase 1 foundation mode):

```bash
python scripts/generate_publish_queue.py --date 2026-02-14 --mode foundation --min-per-category 2 --limit 18 --week-size 5
```

Outputs:

- `reports/publish_queue.json`
- `reports/week1-publish-plan-YYYY-MM-DD.md`

## Weekly (30-45 min)

Run maintenance checks and write a report:

```bash
python scripts/weekly_maintenance.py --write-report
```

What it checks:

- Missing required guide metadata
- Broken internal guide links
- Stale guides (`last_updated` older than 180 days)

## Monthly (1-2 hours)

Generate strategic review report:

```bash
python scripts/monthly_review.py
```

What it includes:

- Coverage by category
- Top tag/topic signals
- Refresh queue
- High-intent backlog suggestions

## Quality and Build Checks

Guide contract validation:

```bash
python scripts/validate_guides.py
```

Tone lint (anti-template phrases):

```bash
python scripts/tone_lint.py
```

KPI snapshot (writes `reports/kpi.json`):

```bash
python scripts/generate_kpi.py
```

Note: scripts that parse guide front matter require PyYAML:

```bash
python -m pip install pyyaml
```

Jekyll build (requires Ruby + Bundler installed):

```bash
bundle install
bundle exec jekyll build --trace
bundle exec jekyll serve
```

