---
title: Health Guides in Brunei
permalink: /guides/health/
meta_description: Verified Brunei guides for health. Updated regularly with source-backed practical details.
---

# Health Guides in Brunei

Healthcare access, emergency planning, and preventive care.

{% assign items = site.guides | where: "category", "health" | sort: "title" %}
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
