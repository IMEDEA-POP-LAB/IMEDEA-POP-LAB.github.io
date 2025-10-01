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

<!-- Recent Publications -->
{% if site.data.publications.recent %}
<div class="recent-publications">
## Recent Publications

{% for pub in site.data.publications.recent %}
<div class="publication-item {% if pub.featured %}featured{% else %}published{% endif %}">
  <div class="publication-header">
    <div class="publication-title">{{ pub.title }}</div>
    <div class="publication-meta">
      <span class="journal">{{ pub.journal }}</span>
      <span class="year">{{ pub.year }}</span>
    </div>
  </div>
  
  <div class="publication-authors">{{ pub.authors }}</div>
  
  {% if pub.volume or pub.pages %}
  <div class="publication-volume">
    {% if pub.volume %}Volume {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
  </div>
  {% endif %}
  
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
  
  {% if pub.bibtex %}
  <details class="publication-bibtex">
    <summary>BibTeX</summary>
    <div class="bibtex-content">
      <pre><code>{{ pub.bibtex }}</code></pre>
    </div>
  </details>
  {% endif %}
</div>
{% endfor %}
</div>
{% endif %}

<!-- Preprints -->
{% if site.data.publications.preprints and site.data.publications.preprints.size > 0 %}
<div class="preprints-section">
## Preprints & Accepted

{% for pub in site.data.publications.preprints %}
<div class="publication-item {% if pub.status == 'accepted' %}accepted{% else %}preprint{% endif %}">
  <div class="publication-header">
    <div class="publication-title">{{ pub.title }}</div>
    <div class="publication-meta">
      <span class="journal {% if pub.status == 'preprint' %}preprint-server{% endif %}">{{ pub.journal }}</span>
      <span class="year">{{ pub.year }}</span>
      {% if pub.status %}
        <span class="preprint-badge">{{ pub.status | capitalize }}</span>
      {% endif %}
    </div>
  </div>
  
  <div class="publication-authors">{{ pub.authors }}</div>
  
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
{% endfor %}
</div>
{% endif %}

<!-- All Publications by Year -->
{% if site.data.publications.all %}
<div class="publication-list">
## All Publications

{% assign sorted_years = site.data.publications.all | map: 'first' | sort | reverse %}
{% for year in sorted_years %}
<h3 class="publication-year-header">{{ year }}</h3>

{% for pub in site.data.publications.all[year] %}
<div class="publication-item published">
  <div class="publication-citation">
    <strong>{{ pub.title }}</strong><br>
    {{ pub.authors }}<br>
    <em class="journal">{{ pub.journal }}</em> (<span class="year">{{ pub.year }}</span>)
    {% if pub.volume or pub.pages %}
      {% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
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
  
  {% if pub.bibtex %}
  <details class="publication-bibtex">
    <summary>BibTeX</summary>
    <div class="bibtex-content">
      <pre><code>{{ pub.bibtex }}</code></pre>
    </div>
  </details>
  {% endif %}
</div>
{% endfor %}
{% endfor %}
</div>
{% endif %}

</div>