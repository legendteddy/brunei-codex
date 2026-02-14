---
title: Business Guides in Brunei
permalink: /guides/business/
meta_description: Verified Brunei guides for business. Updated regularly with source-backed practical details.
---

# Business Guides in Brunei

Registration, licensing, and business operations guidance.

{% assign items = site.guides | where: "category", "business" | sort: "title" %}
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
