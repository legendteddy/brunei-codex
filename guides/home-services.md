---
title: Home Services Guides
permalink: /guides/home-services/
category_key: home-services
meta_description: "Home services in Brunei guides: renovation planning, home maintenance, contractor checklists, and risk controls."
---

Home services guides focus on process, costs, and risk controls so you can compare like-for-like quotes.

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


