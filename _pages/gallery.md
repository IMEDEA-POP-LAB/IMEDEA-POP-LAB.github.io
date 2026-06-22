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
    <div class="carousel-viewport">
      <div class="gallery-grid" id="gallery-carousel">
        {% for item in site.data.gallery %}
        <div class="gallery-item" tabindex="0">
          {% if item.url %}
          <a href="{{ item.url }}" target="_blank" rel="noopener noreferrer" class="gallery-link">
            <img src="{{ '/assets/img/gallery/' | append: item.image | relative_url }}" alt="{{ item.title }}">
            <div class="gallery-caption">{{ item.title }}</div>
          </a>
          {% else %}
          <img src="{{ '/assets/img/gallery/' | append: item.image | relative_url }}" alt="{{ item.title }}">
          <div class="gallery-caption">{{ item.title }}</div>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </div>

  </div>
</div>
