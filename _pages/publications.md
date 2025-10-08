---
layout: page
permalink: /publications/
title: publications
nav: true
nav_order: 1
---

<div class="publications-page-modern">

<!-- Single publications list (all items from `_data/publications.yml`) -->
<!-- All Publications Section -->
{% if site.data.publications.all %}
<div class="publications-section" id="all-section">
  <div class="section-container">
    
    <!-- Simple Filter -->
    <div class="publication-filter-simple">
      <input type="search" id="search-publications" class="simple-search" placeholder="🔍 Search publications by title or author...">
    </div>

    <!-- Publications List -->
    <div class="publications-list">
  {% assign sorted_pubs = site.data.publications.all %}

    {% for pub in sorted_pubs %}
      <div class="publication-item" data-year="{{ pub.year }}">
        <div class="item-content">
          {% if pub.image %}
          <div class="item-image">
            <img src="{{ pub.image }}" alt="{{ pub.title }}" loading="lazy">
          </div>
          {% endif %}
          
          <div class="item-text">
            <div class="item-header">
              <h3 class="item-title">{{ pub.title }}</h3>
              <div class="item-meta">
                <span class="journal-name">{{ pub.journal }}</span>
                <span class="item-year">{{ pub.year }}</span>
              </div>
            </div>
            
            <div class="item-authors">{{ pub.authors }}</div>
            
            {% if pub.volume or pub.pages %}
            <div class="item-details">
              {% if pub.volume %}Vol. {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
            </div>
            {% endif %}
            
            {% if pub.doi or pub.url %}
            <div class="item-actions">
              {% if pub.doi %}
              <a href="{{ pub.doi }}" target="_blank" class="item-link">
                <span class="link-icon">🔗</span>
                DOI
              </a>
              {% endif %}
            </div>
            {% endif %}
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
{% endif %}



<!-- Simple search script (filters the visible publication items) -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  const searchInput = document.getElementById('search-publications');
  const publicationItems = Array.from(document.querySelectorAll('.publication-item'));

  searchInput?.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    publicationItems.forEach(item => {
      const title = item.querySelector('.item-title')?.textContent.toLowerCase() || '';
      const authors = item.querySelector('.item-authors')?.textContent.toLowerCase() || '';
      item.style.display = (title.includes(searchTerm) || authors.includes(searchTerm)) ? 'block' : 'none';
    });
  });
});
</script>

</div>