---
title: Events Guides
permalink: /guides/events/
category_key: events
meta_description: Events in Brunei guides: what’s on, how to attend, tickets, venues, and verification notes.
---

Events guides prioritize date-checked logistics: when, where, tickets, and organizer links.

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

