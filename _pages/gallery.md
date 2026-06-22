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
  <div class="section-header">
    <h1>Gallery</h1>
    <p>Highlights from our research work, field campaigns, outreach events, and team activities.</p>
  </div>

  <div class="photo-gallery">
    <div class="carousel-viewport">
      <div class="gallery-grid" id="gallery-carousel">
        {% for item in site.data.gallery %}
        <div class="gallery-item" tabindex="0">
          <img src="{{ '/assets/img/gallery/' | append: item.image | relative_url }}" alt="{{ item.title }}">
          <div class="gallery-caption">{{ item.title }}</div>
        </div>
        {% endfor %}
      </div>
    </div>

    <div class="gallery-controls" aria-hidden="false">
      <button id="gallery-prev" class="carousel-btn" aria-label="Previous gallery items">▴</button>
      <button id="gallery-next" class="carousel-btn" aria-label="Next gallery items">▾</button>
    </div>
  </div>
</div>
