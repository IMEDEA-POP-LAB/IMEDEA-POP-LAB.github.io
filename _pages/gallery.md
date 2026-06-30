---
layout: page
title: Gallery
permalink: /gallery/
description: Photo gallery showcasing lab activities, fieldwork, and events
nav: true
nav_order: 4
gallery: true
---

<div class="gallery-page">
  <div class="photo-gallery">
    <div class="gallery-grid" >
      {% for album in site.data.gallery_albums.albums %}
      <a href="{{ '/gallery/album/' | append: album.slug | append: '/' | relative_url }}" class="gallery-item gallery-album-card" tabindex="0">
        <img src="{{ '/assets/img/gallery/' | append: album.cover_image | relative_url }}" alt="{{ album.title }}">
        <div class="gallery-caption">
          <strong>{{ album.title }}</strong>
          {% if album.description %}
          <span>{{ album.description }}</span>
          {% endif %}
        </div>
      </a>
      {% endfor %}
    </div>
  </div>
</div>
