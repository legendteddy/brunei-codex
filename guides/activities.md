---
title: Activities Guides
permalink: /guides/activities/
category_key: activities
meta_description: Activities in Brunei guides: hobbies, sports, community groups, and practical join-how.
---

Activities guides focus on logistics: where to go, how to join, what it costs, and what to bring.

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

