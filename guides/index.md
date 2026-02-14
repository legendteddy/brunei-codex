---
title: All Guides
permalink: /guides/
meta_description: Browse complete BruneiVerse guides for living, working, and daily life in Brunei.
---

This is the full guide library. Start with pillar guides, then move into category-specific topics.

## Latest Guides

<div class="guide-list">
{% assign sorted_guides = site.guides | sort: "date" | reverse %}
{% for guide in sorted_guides %}
  <article class="guide-item">
    <h3><a href="{{ guide.url | relative_url }}">{{ guide.title }}</a></h3>
    <p>{{ guide.meta_description }}</p>
    <p><strong>Category:</strong> {{ guide.category | capitalize }}</p>
    <p><strong>Last updated:</strong> {{ guide.last_updated | date: "%B %-d, %Y" }}</p>
  </article>
{% endfor %}
</div>
