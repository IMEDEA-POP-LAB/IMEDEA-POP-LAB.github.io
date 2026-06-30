---
layout: page
title: Gallery
permalink: /gallery/
description: Photo gallery showcasing lab activities, fieldwork, and events
nav: true
nav_order: 4
---

<div class="albums-grid">
  {% for album in site.data.gallery_albums.albums %}
  <a href="{{ '/gallery/album/' | append: album.slug | append: '/' | relative_url }}" class="album-card">
    <img src="{{ '/assets/img/gallery/' | append: album.cover_image | relative_url }}" alt="{{ album.title }}">
    <div class="album-card-caption">
      <strong>{{ album.title }}</strong>
    </div>
  </a>
  {% endfor %}
</div>
