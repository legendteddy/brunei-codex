---
title: Food Guides
permalink: /guides/food/
category_key: food
meta_description: Food in Brunei guides: practical dining choices, budget bands, logistics, and date-checked details.
---

Food guides focus on “what this looks like” planning: where, price bands, timing, and how to verify opening hours.

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

