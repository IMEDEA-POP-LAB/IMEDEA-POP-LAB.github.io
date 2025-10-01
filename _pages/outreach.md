---
layout: page
title: outreach
permalink: /outreach/
description: Science communication and public engagement
nav: true
nav_order: 4
---

<!-- Featured Outreach Content -->
{% if site.data.outreach and site.data.outreach.size > 0 %}
## Featured Content

<div class="featured-content">
{% for item in site.data.outreach %}
{% if item.featured %}
  <div class="featured-item">
    <div class="featured-date">{{ item.date | date: "%B %Y" }}</div>
    <div class="featured-details">
      <div class="featured-title">{{ item.title }}</div>
      <div class="featured-venue">{{ item.venue }}</div>
      {% if item.description %}
      <div class="featured-description">{{ item.description }}</div>
      {% endif %}
      {% if item.youtube_id %}
      <div class="featured-video">
        <iframe width="100%" height="200" src="https://www.youtube.com/embed/{{ item.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      {% endif %}
    </div>
  </div>
{% endif %}
{% endfor %}
</div>
{% endif %}

## Media Coverage & Press

{% if site.data.media and site.data.media.size > 0 %}
<div class="press-releases">
{% for item in site.data.media %}
  <div class="press-item">
    <div class="press-date">{{ item.date | date: "%B %Y" }}</div>
    <div class="press-title">
      <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
    </div>
    <div class="press-outlet">{{ item.outlet }}</div>
    {% if item.excerpt %}
    <div class="press-excerpt">{{ item.excerpt }}</div>
    {% endif %}
    {% if item.type %}
    <div class="press-type">{{ item.type | capitalize }}</div>
    {% endif %}
  </div>
{% endfor %}
</div>
{% endif %}