---
title: Education Guides
permalink: /guides/education/
category_key: education
meta_description: Education in Brunei guides for schools, admissions, curriculum choices, and student setup.
---

Education guides help families compare school pathways and administrative requirements.

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
