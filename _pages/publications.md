---
layout: page
permalink: /publications/
title: publications
nav: true
nav_order: 1
---

<div class="publications-page">

<!-- External Profiles Links -->
<div class="external-profiles">
  <div class="profiles-header">
  </div>
  <div class="profiles-links">
    <a href="https://scholar.google.es/citations?user=JSX_hG8AAAAJ&hl=es" target="_blank" class="profile-link google-scholar">
      <span class="profile-icon">🎓</span>
      <span class="profile-text">Google Scholar</span>
    </a>
    <a href="https://orcid.org/0000-0001-9476-9272" target="_blank" class="profile-link orcid">
      <span class="profile-icon">🔗</span>
      <span class="profile-text">ORCID Profile</span>
    </a>
    <a href="https://www.researchgate.net/profile/Ananda-Pascual" target="_blank" class="profile-link researchgate">
      <span class="profile-icon">📊</span>
      <span class="profile-text">ResearchGate</span>
    </a>
  </div>
</div>

<!-- Recent Publications - Enhanced -->
{% if site.data.publications.recent %}
<div class="recent-publications-enhanced">
  <div class="section-header">
    <h2 class="section-title">Recent Publications</h2>
    <p class="section-subtitle">Our latest research contributions and findings</p>
  </div>

{% for pub in site.data.publications.recent %}
<div class="publication-item-enhanced {% if forloop.first %}featured{% endif %}">
  <div class="publication-main">
    <div class="publication-title">{{ pub.title }}</div>
    <div class="publication-authors">{{ pub.authors }}</div>
    
    <div class="publication-details">
      <span class="journal-name">{{ pub.journal }}</span>
      <span class="publication-year">{{ pub.year }}</span>
      {% if pub.volume or pub.pages %}
      <span class="volume-pages">
        {% if pub.volume %}Vol. {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
      </span>
      {% endif %}
    </div>
    
    {% if pub.doi or pub.url %}
    <div class="publication-actions">
      {% if pub.doi %}
      <a href="{{ pub.doi }}" class="action-link primary" target="_blank">
        <span class="link-icon">📄</span>
        View Article
      </a>
      {% endif %}
      {% if pub.url %}
      <a href="{{ pub.url }}" class="action-link secondary" target="_blank">
        <span class="link-icon">🔗</span>
        External Link
      </a>
      {% endif %}
    </div>
    {% endif %}
  </div>
  
  {% if forloop.first %}
  <div class="featured-badge">Latest</div>
  {% endif %}
</div>
{% endfor %}
</div>
{% endif %}

<!-- Preprints - Minimized -->
{% if site.data.publications.preprints and site.data.publications.preprints.size > 0 %}
<div class="preprints-minimized">
  <details class="preprints-toggle">
    <summary class="preprints-summary">
      <span class="toggle-text">Preprints & In Review ({{ site.data.publications.preprints.size }})</span>
    </summary>
    <div class="preprints-content">
      {% for pub in site.data.publications.preprints %}
      <div class="preprint-item-minimal">
        <div class="preprint-title">{{ pub.title }}</div>
        <div class="preprint-meta">
          <span class="preprint-authors">{{ pub.authors }}</span>
          <span class="preprint-status">{{ pub.status | default: "Preprint" | capitalize }}</span>
        </div>
        {% if pub.doi or pub.url %}
        <div class="preprint-link">
          {% if pub.doi %}
          <a href="{{ pub.doi }}" target="_blank">View Preprint</a>
          {% elsif pub.url %}
          <a href="{{ pub.url }}" target="_blank">View Preprint</a>
          {% endif %}
        </div>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </details>
</div>
{% endif %}

<!-- All Publications - No Year Headers -->
{% if site.data.publications.all %}
<div class="all-publications">
  <div class="section-header">
    <h2 class="section-title">All Publications</h2>
    <p class="section-subtitle">Complete list of research publications</p>
  </div>

{% assign sorted_pubs = site.data.publications.all | sort: 'year' | reverse %}
{% assign recent_titles = site.data.publications.recent | map: 'title' %}

{% for pub in sorted_pubs %}
{% assign is_recent = false %}
{% for recent_title in recent_titles %}
  {% if pub.title == recent_title %}
    {% assign is_recent = true %}
    {% break %}
  {% endif %}
{% endfor %}

{% unless is_recent %}
<div class="publication-item-standard">
  <div class="publication-content">
    <div class="publication-title">{{ pub.title }}</div>
    <div class="publication-authors">{{ pub.authors }}</div>
    
    <div class="publication-details">
      <span class="journal-name">{{ pub.journal }}</span>
      <span class="publication-year">{{ pub.year }}</span>
      {% if pub.volume or pub.pages %}
      <span class="volume-pages">
        {% if pub.volume %}Vol. {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
      </span>
      {% endif %}
    </div>
    
    {% if pub.doi or pub.url %}
    <div class="publication-links">
      {% if pub.doi %}
      <a href="{{ pub.doi }}" class="link-doi" target="_blank">DOI</a>
      {% endif %}
      {% if pub.url %}
      <a href="{{ pub.url }}" class="link-url" target="_blank">Link</a>
      {% endif %}
    </div>
    {% endif %}
  </div>
</div>
{% endunless %}
{% endfor %}
</div>
{% endif %}

</div>