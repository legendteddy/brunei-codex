---
title: Working Guides in Brunei
permalink: /guides/working/
meta_description: Verified Brunei guides for working. Updated regularly with source-backed practical details.
---

# Working Guides in Brunei

Jobs, permits, salaries, and employment workflows.

{% assign items = site.guides | where: "category", "working" | sort: "title" %}
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
