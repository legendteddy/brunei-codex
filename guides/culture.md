---
title: Culture Guides in Brunei
permalink: /guides/culture/
meta_description: Verified Brunei guides for culture. Updated regularly with source-backed practical details.
---

# Culture Guides in Brunei

Etiquette, customs, and practical social norms in Brunei.

{% assign items = site.guides | where: "category", "culture" | sort: "title" %}
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
