---
title: Living Guides
permalink: /guides/living/
category_key: living
meta_description: Living in Brunei guides: housing, cost of living, utilities, and practical setup advice.
---

Living guides focus on home setup, monthly budgeting, and day-to-day logistics.

## Guides in This Category

<div class="guide-list">
{% assign living_guides = site.guides | where: "category", page.category_key | sort: "date" | reverse %}
{% for guide in living_guides %}
  <article class="guide-item">
    <h3><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></h3>
    <p>{{ guide.meta_description }}</p>
  </article>
{% endfor %}
</div>
