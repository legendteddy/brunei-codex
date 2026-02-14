---
title: Business Guides
permalink: /guides/business/
category_key: business
meta_description: "Business in Brunei guides for registration, licensing, tax basics, and market setup."
---

Business guides provide factual, process-focused coverage for entrepreneurs and operators.

## Guides in This Category

<div class="guide-list">
{% assign guides_for_category = site.guides | where: "category", page.category_key | sort: "date" | reverse %}
{% for guide in guides_for_category %}
  <article class="guide-item">
    <h3><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></h3>
    <p>{{ guide.meta_description }}</p>
    <p><strong>Last updated:</strong> {{ guide.last_updated | date: "%Y-%m-%d" }} | <strong>State:</strong> {{ guide.content_state }}</p>
  </article>
{% endfor %}
</div>

