---
title: Living Guides in Brunei
permalink: /guides/living/
meta_description: Verified Brunei guides for living. Updated regularly with source-backed practical details.
---

# Living Guides in Brunei

Housing, daily setup, and household logistics in Brunei.

{% assign items = site.guides | where: "category", "living" | sort: "title" %}
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
