---
layout: page
title: outreach
permalink: /outreach/
description: Science communication and public engagement
nav: true
nav_order: 4
---

<div class="outreach-page-modern">

<!-- Hero Section -->
<div class="outreach-hero">
  <div class="hero-content">
    <h1 class="hero-title">Science Communication</h1>
    <p class="hero-subtitle">Bridging the gap between cutting-edge oceanographic research and public understanding</p>
    
    <!-- Impact Stats -->
    <div class="outreach-stats">
      <div class="stat-item">
        <span class="stat-number">{{ site.data.outreach.size }}</span>
        <span class="stat-label">Featured Content</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">{{ site.data.media.size }}</span>
        <span class="stat-label">Media Coverage</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">3</span>
        <span class="stat-label">Languages</span>
      </div>
    </div>
  </div>
</div>

<!-- Featured Content Section -->
{% if site.data.outreach and site.data.outreach.size > 0 %}
<div class="outreach-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">Featured Content</h2>
      <p class="section-subtitle">Documentaries, interviews, and educational videos</p>
    </div>

    <div class="featured-grid">
      {% assign featured_items = site.data.outreach | where: "featured", true | sort: "date" | reverse %}
      {% for item in featured_items %}
      <div class="featured-card {% if forloop.first %}highlight{% endif %}">
        {% if item.youtube_id %}
        <div class="video-container">
          <iframe 
            src="https://www.youtube.com/embed/{{ item.youtube_id }}" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
          </iframe>
          <div class="video-overlay">
            <div class="play-button">▶</div>
          </div>
        </div>
        {% endif %}
        
        <div class="card-content">
          <div class="card-header">
            <div class="content-type">{{ item.type | capitalize }}</div>
            <div class="content-date">{{ item.date | date: "%B %Y" }}</div>
          </div>
          
          <h3 class="content-title">{{ item.title }}</h3>
          <div class="content-venue">{{ item.venue }}</div>
          
          {% if item.description %}
          <p class="content-description">{{ item.description }}</p>
          {% endif %}
          
          <div class="content-actions">
            {% if item.youtube_id %}
            <a href="https://www.youtube.com/watch?v={{ item.youtube_id }}" target="_blank" class="action-btn primary">
              <span class="btn-icon">🎥</span>
              Watch Video
            </a>
            {% endif %}
            {% if item.language %}
            <span class="language-tag">{{ item.language | upcase }}</span>
            {% endif %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
{% endif %}

<!-- Media Coverage Section -->
{% if site.data.media and site.data.media.size > 0 %}
<div class="outreach-section">
  <div class="section-container">
    <div class="section-header">
      <h2 class="section-title">Media Coverage</h2>
      <p class="section-subtitle">Press coverage and media appearances</p>
    </div>

    <!-- Latest Media Highlight -->
    {% assign latest_media = site.data.media | first %}
    <div class="media-highlight">
      <div class="highlight-badge">Latest Coverage</div>
      <div class="highlight-content">
        <h3 class="highlight-title">{{ latest_media.title }}</h3>
        <div class="highlight-meta">
          <span class="highlight-outlet">{{ latest_media.outlet }}</span>
          <span class="highlight-date">{{ latest_media.date | date: "%B %d, %Y" }}</span>
          <span class="highlight-type">{{ latest_media.type | capitalize }}</span>
        </div>
        {% if latest_media.excerpt %}
        <p class="highlight-excerpt">{{ latest_media.excerpt }}</p>
        {% endif %}
        <a href="{{ latest_media.url }}" target="_blank" class="highlight-cta">
          <span class="cta-icon">📰</span>
          Read Article
        </a>
      </div>
    </div>

    <!-- Media Grid -->
    <div class="media-grid">
      {% for item in site.data.media %}
      {% unless forloop.first %}
      <article class="media-card">
        <div class="media-header">
          <div class="media-type">{{ item.type | capitalize }}</div>
          <div class="media-date">{{ item.date | date: "%b %Y" }}</div>
        </div>
        
        <h3 class="media-title">
          <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
        </h3>
        
        <div class="media-outlet">{{ item.outlet }}</div>
        
        {% if item.excerpt %}
        <p class="media-excerpt">{{ item.excerpt }}</p>
        {% endif %}
        
        <div class="media-actions">
          <a href="{{ item.url }}" target="_blank" class="media-link">
            Read More
            <span class="link-arrow">→</span>
          </a>
        </div>
      </article>
      {% endunless %}
      {% endfor %}
    </div>
  </div>
</div>
{% endif %}

<!-- Science Communication Info -->
<div class="outreach-section">
  <div class="section-container">
    <div class="communication-cta">
      <div class="cta-content">
        <h3 class="cta-title">Interested in Science Communication?</h3>
        <p class="cta-description">
          We're always open to collaborating with media outlets, educational institutions, and science communicators 
          to share our oceanographic research and its implications for understanding our changing planet.
        </p>
        <div class="cta-actions">
          <a href="mailto:ananda.pascual@imedea.uib-csic.es" class="cta-btn primary">
            <span class="btn-icon">✉️</span>
            Contact for Media Inquiries
          </a>
          <a href="/about/" class="cta-btn secondary">
            <span class="btn-icon">👥</span>
            Learn About Our Research
          </a>
        </div>
      </div>
    </div>
  </div>
</div>

</div>