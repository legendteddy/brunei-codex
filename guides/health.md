---
title: Health Guides
permalink: /guides/health/
category_key: health
meta_description: Health in Brunei guides covering clinics, hospitals, insurance basics, and healthcare access.
---

Health guides explain how to access care quickly and prepare for routine and urgent visits.

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
