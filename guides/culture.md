---
title: Culture Guides
permalink: /guides/culture/
category_key: culture
meta_description: Culture and lifestyle guides for social norms, activities, and practical etiquette in Brunei.
---

Culture guides focus on practical etiquette and daily social context for smoother integration.

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
