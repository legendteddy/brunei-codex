# BruneiVerse Operations

## Daily (15-30 min)

Generate daily topic recommendation:

```bash
python scripts/generate_daily_recommendation.py
```

Optional date override:

```bash
python scripts/generate_daily_recommendation.py --date 2026-02-14
```

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

Jekyll build (requires Ruby + Bundler installed):

```bash
bundle install
bundle exec jekyll build --trace
bundle exec jekyll serve
```
