---
title: Gadgets Guides
permalink: /guides/gadgets/
category_key: gadgets
meta_description: Gadgets in Brunei guides: buyer comparisons, price-check notes, warranty reality, and local availability.
---

Gadgets guides separate verified facts (specs, warranty, price checked) from editorial take.

## Guides in This Category

<div class="guide-list">
{% assign guides_for_category = site.guides | where: "category", page.category_key | sort: "date" | reverse %}
{% for guide in guides_for_category %}
  <article class="guide-item">
    <h3><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></h3>
    <p>{{ guide.meta_description }}</p>
  </article>
{% endfor %}
</div>

