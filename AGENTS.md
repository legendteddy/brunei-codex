# AGENTS.md - BruneiVerse Agent Playbook

## 1) Project Snapshot
- Brand: BruneiVerse
- Live URL: `https://legendteddy.github.io/bruneiverse/`
- Repository: `https://github.com/legendteddy/bruneiverse`
- Platform: GitHub Pages (project site)
- Audience: Gen Z/Gen Alpha + expats/newcomers to Brunei
- Business model: Ad-supported now, transparent sponsored listings later

## 2) Core Outcome
Build BruneiVerse into a trusted, neutral, high-coverage source for "Brunei + [practical query]" across living, working, business, education, health, culture, activities/community, events, food/dining, movies/entertainment, home services, and gadget review topics.

## 3) Editorial Principles
- Prioritize practical, factual, action-oriented guidance.
- Keep tone neutral and non-promotional.
- Use clear structure and answer-first writing.
- Cite official sources for policies, regulations, or institutional claims.
- Prefer comprehensive depth over thin volume.

## 3.1) Evidence Standard (No Source, No Claim)
- Every factual claim must have a source.
- Prefer official primary sources first (government ministry/department/regulator).
- If no official source exists, use a reputable primary source and label it clearly.
- If a statement is advice, judgment, or estimate, label it as `Editorial guidance` or `Planning estimate` (not fact).
- If a claim cannot be sourced, remove it.
- For reviews, separate verified facts (specs, warranty, price/date checked, official availability) from editorial opinion.

## 3.2) Freshness and Accuracy Standard (Always Latest)
- Time-sensitive claims must be verified against the latest available source before publishing.
- Time-sensitive claims include: prices, event schedules, contact details, opening hours, regulations, permit steps, fees, and product availability.
- If latest status cannot be verified, do not publish the claim.
- Every guide must show `last_updated` and `verified_on` dates.
- For event and price-heavy guides, verification must be performed within 7 days of publish/update.
- For regulatory/process guides, verification must be performed within 30 days of publish/update.

## 3.3) Mandatory Live Lookup (Automatic Search Requirement)
- Agents must automatically search for latest information before drafting, editing, or refreshing any guide.
- Do not rely on memory-only facts for time-sensitive topics.
- Minimum pre-publish verification behavior:
  1. Search for latest official/reputable sources.
  2. Open and verify the source page directly.
  3. Capture citation links for each factual claim.
  4. Update `verified_on` and `last_updated` after verification.
- If latest information cannot be confirmed from a source, remove or defer the claim.

## 3.4) Obsolete Information Removal (Automatic)
- Agents must automatically detect obsolete information during every update pass.
- If a claim is outdated, agents must either:
  1. Replace it with verified latest information, or
  2. Remove it if no current source can confirm it.
- Do not keep historical values without explicit date context.
- Obsolete schedule/price/process text must never remain in "current" sections.

## 3.5) Source Retention and Verification Log
- For each guide update, keep a verification log of source URLs, source updated date (if shown), and verification date.
- Archive critical source snapshots (URL + date + key claim mapped) for auditability.
- If a source changes materially, re-verify affected claims immediately.

## 4) Required Guide Contract

### 4.1 Front Matter
Every guide must include:

```yaml
---
title: "[Topic] in Brunei - Complete Guide [YEAR]"
date: YYYY-MM-DD
last_updated: YYYY-MM-DD
verified_on: YYYY-MM-DD
owner: [editor_or_agent_id]
content_state: [draft/verified/stale-risk/needs-refresh/archived]
category: [living/working/business/education/health/culture/activities/events/food/movies/home-services/gadgets]
tags: [tag1, tag2, tag3]
meta_description: "Everything you need to know about [topic] in Brunei. Updated [YEAR]. Costs, process, tips, and recommendations."
quick_answer: "2-3 sentence direct answer."
sources:
  - https://official-source.example
---
```

Optional but recommended:
- `disclosure`: plain statement for sponsorship/affiliate context when applicable.

### 4.2 Body Structure
Required sections:
- H1 title
- Quick Answer (2-3 quotable sentences)
- Overview
- Key Information (with at least one table)
- Step-by-step process / how-to
- Costs and pricing
- Tips and recommendations
- FAQ (5-10 Q&A items)
- Verification Snapshot (verified date + source confidence summary + reviewer)
- Related resources
- Last updated footer line

Citation rule inside body:
- Add inline citations in relevant sentences, for example: `... [Source: MOH Contact Page]`
- Keep a `Source Notes` subsection that maps key claims to source links.
- Tag each source note with confidence level: `official`, `institutional`, or `secondary`.

Guide archetypes to support broader scope:
- Process guides (for example permits, setup, registration)
- Comparison guides (for example provider/option tables)
- Activity guides (for example where to play chess in Brunei)
- Event guides (for example what to do this weekend in Brunei)
- Home-service guides (for example house renovation planning in Brunei)
- Review guides (for example gadgets, devices, and buyer comparisons in Brunei)

Template variants by content type:
- Event guide: date/time/venue table, ticketing info, organizer source link, `verified_on` <= 7 days.
- Review guide: scoring criteria table, fact vs opinion split, disclosure block, price-checked date.
- Renovation guide: scope tiers, permit/compliance notes, contractor checklist, risk controls.
- Food guide: cuisine/price range/service style, location map links, operating-hours verification date.
- Movies guide: cinema/location table, format/language notes, showtime-source links, family suitability notes.

### 4.3 Quality Gate
Before publish, verify:
- Answer-first structure is present
- Clear H1/H2/H3 hierarchy
- At least one table
- 5-10 FAQ items
- At least 3 internal links to other guides
- `last_updated` present
- `verified_on` present
- Neutral and non-promotional framing
- Official sources listed for factual claims
- 1000-2000 words (target range)
- Every factual claim has an inline citation or explicit source mapping
- All time-sensitive claims are re-checked against the latest source before publish
- Obsolete claims have been replaced or removed
- No defaming, misleading, or misinformation content remains

## 5) Safety and Red Lines

## 5.1) Truthfulness and Defamation Policy (Required)
- No defaming individuals, organizations, institutions, or businesses.
- No misinformation: if a claim cannot be verified, do not publish it.
- No misleading framing: avoid deceptive wording, cherry-picked facts, or ambiguous claims presented as certain.
- If an error is discovered, correct or remove it immediately and update `last_updated` + `verified_on`.

## 5.2) Corrections and Retractions Policy
- Corrections SLA: patch confirmed factual errors within 24-72 hours.
- If a claim cannot be safely corrected, retract/remove it until verified.
- Add a short change note in the guide (`what changed` with date) for substantial corrections.

## 5.3) Copyright, IP, and Takedown Handling
- No unauthorized reuse of text, images, videos, logos, or proprietary assets.
- Maintain attribution/license evidence for reusable assets.
- Takedown workflow:
  1. Receive request with URL + ownership evidence.
  2. Temporarily unpublish disputed content if risk is high.
  3. Resolve within 72 hours with removal, replacement, or documented rejection.

## 5.4) Sponsored and Affiliate Disclosure
- Sponsored or affiliate content must be clearly labeled near the top of the page.
- Disclosures must be plain-language and unambiguous.
- Rankings/recommendations must not be secretly influenced by payment.

## 5.5) Legal/Professional Advice Boundary
- Content is informational and practical only; it is not legal, medical, or financial advice.
- For regulated decisions, link to official source pages and advise readers to confirm current official rules.

## 5.6) Reviews Methodology and Conflict-of-Interest
- Review guides must include criteria and scoring dimensions (for example price, warranty, availability, reliability).
- Distinguish objective facts from subjective opinion.
- Any partnership, sponsorship, loaner device, or affiliate relationship must be declared.

## 5.7) UGC Moderation Policy (If comments/reviews enabled later)
- Remove defamatory, misleading, unlawful, or privacy-violating submissions.
- Do not publish unverified allegations about persons or businesses.
- Keep moderation logs for removed/edited submissions.

## 5.8) Emergency Rollback Rule
- If a high-impact error is discovered (legal risk, safety risk, false factual claim), immediately unpublish or rollback the affected section.
- Publish a temporary correction note while full verification is completed.
- Resolve rollback cases within 24 hours when possible.

## 5.9) Image and Media Compliance
- Only use media with clear usage rights (owned, licensed, or permission granted).
- Keep attribution/license details in a media log.
- Remove any disputed media immediately until rights are verified.

### Never publish
- Political opinion or commentary
- Religious debate or doctrinal argument
- Criticism of government or monarchy
- Hidden promotions or biased recommendations
- Unverified claims presented as fact
- Defaming statements or allegations without verified evidence
- Misleading claims, headlines, or comparisons
- Misinformation or outdated claims presented as current
- Copied/plagiarized content
- Copyright-infringing text, images, videos, or other media
- Personal/private data

### Allowed with constraints
- Religious observances (for example Ramadan) only as practical logistics, etiquette, schedules, and factual guidance.
- Gadget reviews are allowed only with clear disclosure: sponsored/affiliate relationships must be labeled.
- Only use text/media with proper rights, permission, or clear license compliance.

## 6) Topic Priorities

## 6.1) Prioritization Score Model (Use Every Planning Cycle)
Score candidate topics with:
- Intent score (0-5)
- Coverage gap score (0-5)
- Freshness risk score (0-5)
- Citation potential score (0-5)
- Audience relevance score (0-5)

Priority score formula:
`(Intent * 0.30) + (Coverage Gap * 0.25) + (Freshness Risk * 0.20) + (Citation Potential * 0.15) + (Audience Relevance * 0.10)`

Rules:
- Publish highest scores first.
- If two topics tie, prioritize higher freshness risk.

### Priority (high intent)
- Housing, rent, neighborhoods
- House renovation (planning, permits, contractor selection, budgeting, timelines)
- Cost of living and utilities
- Banking and account setup
- Healthcare and hospitals
- Transport and licenses
- Work permits, salaries, labor rights
- Business registration, licenses, tax obligations
- Mobile/internet setup, groceries, schools
- Daily activities and community participation (for example chess clubs, sports groups, hobby communities)
- Brunei events coverage (weekend events, seasonal events, community fairs, festivals)
- Food and dining coverage (restaurants, cafes, local specialties, budget dining guides)
- Movies and entertainment coverage (cinemas, screenings, family-friendly options, release guides)
- Gadget reviews and buyer guides (phones, laptops, accessories, smart home devices in Brunei)

### Secondary (authority depth)
- Weather and climate patterns
- Safety and emergency services
- Geography/history background (factual only)
- Language basics

### New Cluster Targets (Broad Scope)
- Activities and community:
  - Where to play chess in Brunei
  - Chess clubs, tournaments, and beginner meetups
  - Weekend hobby groups and social activities
- Events:
  - Weekend events in Brunei (updated weekly)
  - Family-friendly events calendar
  - Seasonal and holiday event guides
  - Event venue guide by district
- Food and dining:
  - Best local food spots in Brunei
  - Budget dining guide by district
  - Halal-friendly dining and practical dining etiquette guide
  - Cafe and dessert guide
- Movies and entertainment:
  - Cinema guide in Brunei (locations, formats, ticketing basics)
  - Weekly movie releases and showtime resource guide
  - Family-friendly movie activities and rainy-day entertainment guide
- Home and renovation:
  - House renovation in Brunei (start-to-finish guide)
  - Renovation cost planning by scope
  - Contractor selection checklist and risk controls
  - Permit and compliance overview (where applicable)
- Gadgets and tech:
  - Best budget phones in Brunei
  - Laptop buying guide in Brunei
  - Home Wi-Fi router and mesh buyer guide
  - Smart home starter setup in Brunei

## 7) Linking and SEO Rules
- URL pattern: `/guides/[topic-slug-in-brunei]/`
- Title format: `[Topic] in Brunei - Complete Guide [YEAR]`
- Meta description format from section 4.1
- Every guide links to at least 3 related internal guides
- Use descriptive anchor text
- Keep `last_updated` current when edits are made

## 7.2) Automatic SEO Improvement (Required)
- Agents must automatically run an SEO pass whenever creating or updating a guide.
- Required SEO improvements per update:
  1. Optimize title for intent + location (`[topic] in Brunei`).
  2. Improve meta description for clarity, recency, and action value.
  3. Strengthen internal linking to related cluster pages (minimum 3, preferred 5+ when relevant).
  4. Ensure FAQ section uses direct question-answer phrasing.
  5. Ensure at least one structured table for scannability.
  6. Improve heading hierarchy and keyword clarity without stuffing.
  7. Add/refresh source-backed updates and update `last_updated` + `verified_on`.
- If an SEO improvement opportunity is detected, agent should apply it in the same update cycle (do not defer).

## 7.1) Source Hierarchy
Use sources in this order of preference:
1. Official Brunei government pages (`gov.bn`, ministry/department/regulator domains)
2. Official regulator or statutory body pages
3. Primary institutional pages (bank/provider/operator official docs)
4. Reputable secondary sources only when primary is unavailable (must be labeled)

Freshness requirement:
- When a source shows both publish date and updated date, use the updated date for verification status.
- Record verification date in content and update `verified_on` in front matter.

## 8) Operating Cadence

## 8.1) Automatic Audit (Required)
- Agents must automatically run an audit after any content create/update cycle.
- Minimum audit scope:
  1. Factual claim/source mapping completeness
  2. Freshness checks (`last_updated`, `verified_on`, time-sensitive claim validity)
  3. SEO checks (title, meta, headings, FAQ, internal links, table presence)
  4. Link integrity (internal and external references)
  5. Obsolete-information detection/removal
  6. Truthfulness and defamation check (no misleading or defamatory language)
- If audit fails, agent must fix issues immediately before publishing.

## 8.2) Automated Compliance Gate (CI Required)
- CI must fail if required compliance fields/checks are missing:
  - `last_updated`
  - `verified_on`
  - `owner`
  - `content_state`
  - source mapping for factual claims
  - disclosure field when sponsored/affiliate content is present
  - no unresolved audit findings

## 8.3) Content Lifecycle States
- `draft`: in production, not publish-ready.
- `verified`: publish-ready, fully sourced, passes all gates.
- `stale-risk`: still live but approaching verification timeout.
- `needs-refresh`: verification expired or material change detected.
- `archived`: intentionally retained for historical context; clearly labeled not-current.

State transition rules:
- `draft -> verified`: all quality, legal, SEO, and freshness checks pass.
- `verified -> stale-risk`: time-sensitive verification window nearing expiry.
- `stale-risk -> needs-refresh`: verification window exceeded or source changed.
- `needs-refresh -> verified`: re-verified and corrected.
- Any state -> `archived`: content no longer current but retained with date context.

## 8.4) KPI Dashboard File (Machine-Readable)
- Update `reports/kpi.json` weekly with:
  - total_guides
  - verified_guides
  - stale_risk_guides
  - needs_refresh_guides
  - source_coverage_ratio
  - internal_link_health
  - compliance_pass_rate
  - corrections_sla_adherence
  - last_generated_at
- Agents must use this file to prioritize refresh and remediation work.

### Daily (15-30 min)
1. Check practical high-intent query opportunities.
2. Identify content gaps in current coverage.
3. Produce one recommendation and outline.
4. Review urgent freshness flags (events/prices/announcements changed in last 24 hours).
5. Run mini-audit on recently changed guides.

### Content days (2-3x/week)
1. Draft one comprehensive guide.
2. Run quality gate.
3. Add internal links.
4. Publish with complete front matter and sources.
5. Re-check all time-sensitive claims on publish day.
6. Run automatic live lookup immediately before final publish.
7. Run automatic SEO improvement pass before publish.
8. Run full post-draft audit and resolve all findings before publish.

### Weekly (30-45 min)
1. Internal link audit (no broken internal paths).
2. Metadata audit (`meta_description`, `last_updated`).
3. Regenerate/verify sitemap.
4. Review broken external links.
5. Re-verify activity schedules and renovation process references on time-sensitive pages.
6. Re-verify event dates, times, venues, and organizer links on event pages.
7. Re-verify gadget prices/availability and note date-checked context.
8. Remove or rewrite obsolete claims discovered during re-verification.
9. Run SEO improvement sweep on top-priority guides (titles/meta/internal links/FAQ clarity).
10. Run full-site audit and produce a findings list with fixes.
11. Run misinformation/defamation sweep and remediate findings.
12. Run visual QA/glitch sweep (layout breakage, overflow, clipping, contrast issues on desktop/mobile).

### Monthly (1-2 hours)
1. Review coverage and freshness.
2. Update outdated prices/processes/regulations.
3. Prioritize next topic cluster.
4. Refresh seasonal topics when relevant.
5. Run an obsolete-content sweep and clean stale claims site-wide.
6. Run deep audit across all clusters and prioritize remediation backlog.

## 9) Agent Output Format (Daily Recommendation)

Use this exact format:

```markdown
## Daily Content Recommendation - [DATE]

**Suggested Topic:** [Topic Name]

**Why This Topic:**
- Search intent: [practical user need]
- Gap in current coverage: [yes/no]
- AI citation potential: [high/medium/low]
- Estimated search volume: [if known]

**Outline:**
1. Quick Answer (2-3 sentences)
2. Main Sections:
   - [Section 1]
   - [Section 2]
   - [Section 3]
3. Key Data Points to Include:
   - [Data point 1]
   - [Data point 2]
4. FAQ Questions (5-10)
5. Internal Links (to existing guides)

**Estimated Word Count:** 1200-1800 words
**Estimated Time:** 2 hours writing + 30 min editing
```

## 10) Phase 2 Direction (Later)
- `/directory/` expansion by category (contractors, restaurants, schools, etc.)
- Explicit paid listing labels: `Featured` / `Sponsored`
- Public transparency page: `/about/how-we-work/`

## 11) Success Metrics
- Published comprehensive guides (goal: 50+ in 6 months)
- Internal linking density (3+ links per guide)
- Freshness (no guide older than 6 months without review)
- Topic coverage breadth across core life categories
- Observable citation signals and organic visibility growth
- Source coverage ratio: 100% of factual claims source-mapped
- Accuracy/freshness SLA: 0 unresolved known factual errors, 100% time-sensitive claims verified within policy window
- Corrections SLA adherence: 100% of confirmed errors corrected/retracted within 72 hours
- Compliance pass rate: 100% CI compliance gate pass on main

## 12) Current Status Checklist
- [x] Repository exists (`legendteddy/bruneiverse`)
- [x] GitHub Pages URL set (`https://legendteddy.github.io/bruneiverse/`)
- [x] Base site structure exists (`index`, `about`, `guides`)
- [x] First 5 pillar guides published
- [x] Internal linking established in pillar set
- [ ] Search Console and Bing Webmaster submitted
- [ ] Optional custom domain configured

## 13) Naming and Style Glossary
- Use consistent district/place naming across all guides.
- Use one format for prices: `BND X` (or `BND X-Y` ranges).
- Use one format for dates: `YYYY-MM-DD` in metadata; human-readable dates in body.
- Use neutral comparatives: avoid absolute claims like "best" unless criteria are shown.
- Keep section naming consistent across guide types to improve scanability and AI extraction.

## 14) AI Swarm Team Topology (L5 Autonomy)
All work is executed as a coordinated swarm with clear ownership:

- Team 1: `Intel & Sources`
  - Discover latest official/reputable updates
  - Maintain source freshness and conflict checks
  - Trigger urgent refresh flags

- Team 2: `Content & Coverage`
  - Produce/refresh guides across all priority clusters
  - Expand coverage depth and internal topic clusters
  - Keep structure aligned to guide contracts

- Team 3: `Trust, Legal, and Compliance`
  - Enforce no-defamation/no-misinformation/no-misleading rules
  - Enforce copyright/IP/privacy/disclosure policies
  - Operate corrections/retractions/takedown workflows

- Team 4: `SEO & Information Architecture`
  - Run automatic SEO optimization on every update
  - Maintain internal linking graph and metadata quality
  - Improve search intent matching and FAQ extractability

- Team 5: `UX & Glitch QA`
  - Run visual quality checks (desktop/mobile)
  - Detect layout clipping/overflow/contrast regressions
  - Maintain a modern, readable, consistent UI baseline

- Team 6: `Automation & Release`
  - Run audits, CI checks, and KPI generation
  - Maintain operational scripts/workflows
  - Push verified updates to `main` continuously

Execution order per cycle:
1. Intel -> 2. Content -> 3. Trust/Legal -> 4. SEO/IA -> 5. UX/QA -> 6. Automation/Release

---

Last Updated: 2026-02-14  
Maintained by: legendteddy
