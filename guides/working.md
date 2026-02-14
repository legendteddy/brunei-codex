---
title: Working Guides
permalink: /guides/working/
category_key: working
meta_description: Working in Brunei guides covering jobs, permits, salaries, and remote work setup.
---

Working guides cover employment pathways, work permits, and career planning.

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
