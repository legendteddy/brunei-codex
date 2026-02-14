---
title: Movies Guides
permalink: /guides/movies/
category_key: movies
meta_description: "Movies and entertainment in Brunei guides: cinemas, formats, ticketing basics, and showtime sources."
---

Movies guides focus on where to watch, what formats exist, and where to check current showtimes.

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


