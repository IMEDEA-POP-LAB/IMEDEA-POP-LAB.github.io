---
layout: page
permalink: /publications/
title: publications
nav: true
nav_order: 1
---

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
## Recent Publications

{% for pub in site.data.publications.recent %}
<div class="publication-item {% if pub.featured %}featured{% else %}published{% endif %}">
  <strong>{{ pub.title }}</strong><br>
  {{ pub.authors }}<br>
  <em class="journal">{{ pub.journal }}</em> (<span class="year">{{ pub.year }}</span>)
  {% if pub.volume or pub.pages %}
    {% if pub.volume %}{{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
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
    <pre><code>{{ pub.bibtex }}</code></pre>
  </details>
  {% endif %}
</div>
{% endfor %}
{% endif %}

<!-- Preprints -->
{% if site.data.publications.preprints %}
## Preprints & Accepted

{% for pub in site.data.publications.preprints %}
<div class="publication-item {% if pub.status == 'accepted' %}accepted{% else %}preprint{% endif %}">
  <strong>{{ pub.title }}</strong><br>
  {{ pub.authors }}<br>
  <em class="journal">{{ pub.journal }}</em> (<span class="year">{{ pub.year }}</span>)
  {% if pub.status %}
    <span class="status-badge {{ pub.status }}">{{ pub.status | capitalize }}</span>
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
</div>
{% endfor %}
{% endif %}

<!-- All Publications by Year -->
{% if site.data.publications.all %}
## All Publications

{% assign sorted_years = site.data.publications.all | map: 'first' | sort | reverse %}
{% for year in sorted_years %}
### {{ year }}

{% for pub in site.data.publications.all[year] %}
<div class="publication-item published">
  <strong>{{ pub.title }}</strong><br>
  {{ pub.authors }}<br>
  <em class="journal">{{ pub.journal }}</em> (<span class="year">{{ pub.year }}</span>)
  {% if pub.volume or pub.pages %}
    {% if pub.volume %}{{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
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
    <pre><code>{{ pub.bibtex }}</code></pre>
  </details>
  {% endif %}
</div>
{% endfor %}
{% endfor %}
{% endif %}