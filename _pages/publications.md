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

<!-- Recent Publications -->
{% if site.data.publications.recent %}
<div class="recent-publications">

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

{% assign grouped_pubs = site.data.publications.all | group_by: 'year' %}
{% assign sorted_groups = grouped_pubs | sort: 'name' | reverse %}
{% assign recent_titles = site.data.publications.recent | map: 'title' %}

{% for year_group in sorted_groups %}
<h3 class="publication-year-header">{{ year_group.name }}</h3>

{% for pub in year_group.items %}
{% assign is_recent = false %}
{% for recent_title in recent_titles %}
  {% if pub.title == recent_title %}
    {% assign is_recent = true %}
    {% break %}
  {% endif %}
{% endfor %}

<div class="publication-item {% if is_recent %}recent-highlight{% else %}published{% endif %}">
  <div class="publication-header">
    <div class="publication-title">{{ pub.title }}</div>
    <div class="publication-meta">
      <span class="journal">{{ pub.journal }}</span>
      <span class="year">{{ pub.year }}</span>
      {% if is_recent %}<span class="recent-badge">Recent</span>{% endif %}
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
{% endfor %}
</div>
{% endif %}

</div>