---
title: Food Guides in Brunei
permalink: /guides/food/
meta_description: Verified Brunei guides for food. Updated regularly with source-backed practical details.
---

# Food Guides in Brunei

Dining choices, food logistics, and household meal planning.

{% assign items = site.guides | where: "category", "food" | sort: "title" %}
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
