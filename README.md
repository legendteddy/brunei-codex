# BruneiVerse

BruneiVerse is a practical guide site for living, working, and navigating daily life in Brunei.

Repository: `https://github.com/legendteddy/bruneiverse`

## Stack

- Jekyll + Markdown
- GitHub Pages hosting
- CI checks for content quality, build stability, and internal links

## Local Development

```bash
bundle install
bundle exec jekyll serve
```

Site runs at `http://127.0.0.1:4000`.

## Content Model

- Guides are stored in `_guides/`
- Guide URLs are generated as `/guides/[slug]/`
- Required guide front matter:
  - `title`
  - `date`
  - `last_updated`
  - `category`
  - `tags`
  - `meta_description`
  - `quick_answer`
  - `sources`

## Content Quality Guardrails

CI runs `scripts/validate_guides.py` and checks each guide for:

- Quick Answer section
- H1 + H2/H3 structure (via markdown headings)
- At least one markdown table
- 5-10 FAQs
- At least 3 internal links to other guides
- Minimum content length for comprehensive coverage

## Deployment

Push to `main` and deploy through GitHub Pages workflow/repository settings.

## Operations

See `OPERATIONS.md` for daily/weekly/monthly commands:

- Daily topic recommendation generator
- Weekly maintenance audit with report output
- Monthly strategy review report generation
