---
title: Events Guides in Brunei
permalink: /guides/events/
meta_description: Verified Brunei guides for events. Updated regularly with source-backed practical details.
---

# Events Guides in Brunei

Seasonal and public-calendar event planning resources.

{% assign items = site.guides | where: "category", "events" | sort: "title" %}
{% if items.size > 0 %}
<ul class="guide-list">
  {% for g in items %}
  <li>
    <a href="{{ g.url | relative_url }}">{{ g.title }}</a>
    {% if g.quick_answer %}<p>{{ g.quick_answer }}</p>{% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No guides published yet in this category.</p>
{% endif %}
