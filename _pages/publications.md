---
layout: page
permalink: /publications/
title: publications
nav: true
nav_order: 1
---

<div class="publications-page-modern">

<!-- Navigation Tabs -->
<div class="publications-nav">
  <div class="nav-tabs">
    <button class="nav-tab active" data-section="recent">Recent Work</button>
    <button class="nav-tab" data-section="all">Complete List</button>
  </div>
</div>

<!-- Recent Publications Section -->
<div class="publications-section" id="recent-section">
  <div class="section-container">
    
    <!-- Recent Publications Grid -->
    {% if site.data.publications.recent %}
    <div class="recent-grid">
      {% for pub in site.data.publications.recent %}
      <article class="publication-card">
        <div class="card-header">
          <h3 class="card-title">{{ pub.title }}</h3>
          <div class="card-meta">
            <div class="card-journal">{{ pub.journal }}</div>
            <div class="card-year">{{ pub.year }}</div>
          </div>
        </div>
        
        <div class="card-content">
          <div class="card-authors">{{ pub.authors }}</div>
          
          {% if pub.volume or pub.pages %}
          <div class="card-details">
            {% if pub.volume %}Vol. {{ pub.volume }}{% endif %}{% if pub.pages %}, {{ pub.pages }}{% endif %}
          </div>
          {% endif %}
        </div>
        
        {% if pub.doi or pub.url %}
        <div class="card-actions">
          {% if pub.doi %}
          <a href="{{ pub.doi }}" target="_blank" class="card-link">View Paper</a>
          {% endif %}
        </div>
        {% endif %}
      </article>
      {% endfor %}
    </div>
    {% endif %}
    
    <!-- Recent Publications Box Section -->
    {% if site.data.publications.recent and site.data.publications.recent.size > 0 %}
    <div class="section-header">
      <h2 class="section-title">Recent Publications</h2>
      <p class="section-subtitle">Latest published work from our research group</p>
    </div>
    
    <div class="recent-publications-list">
      {% for pub in site.data.publications.recent limit:5 %}
      <div class="recent-publication-item">
        <div class="recent-publication-status-badge">Published</div>
        <h4 class="recent-publication-title">{{ pub.title }}</h4>
        <div class="recent-publication-authors">{{ pub.authors }}</div>
        <div class="recent-publication-journal">{{ pub.journal }} ({{ pub.year }})</div>
        {% if pub.doi or pub.url %}
        <a href="{{ pub.doi | default: pub.url }}" target="_blank" class="recent-publication-link">View Publication</a>
        {% endif %}
      </div>
      {% endfor %}
    </div>
    {% endif %}
    
    <!-- Preprints Section - Part of Recent Work -->
    {% if site.data.publications.preprints and site.data.publications.preprints.size > 0 %}
    <div class="section-header">
      <h2 class="section-title">Work in Progress</h2>
      <p class="section-subtitle">Preprints and manuscripts under review</p>
    </div>
    
    <div class="preprints-list">
      {% for pub in site.data.publications.preprints %}
      <div class="preprint-item">
        <div class="preprint-status-badge">{{ pub.status | default: "Preprint" | capitalize }}</div>
        <h4 class="preprint-title">{{ pub.title }}</h4>
        <div class="preprint-authors">{{ pub.authors }}</div>
        {% if pub.doi or pub.url %}
        <a href="{{ pub.doi | default: pub.url }}" target="_blank" class="preprint-link">View Preprint</a>
        {% endif %}
      </div>
      {% endfor %}
    </div>
    {% endif %}
  </div>
</div>



<!-- All Publications Section -->
{% if site.data.publications.all %}
<div class="publications-section hidden" id="all-section">
  <div class="section-container">
    
    <!-- Simple Filter -->
    <div class="publication-filter-simple">
      <input type="search" id="search-publications" class="simple-search" placeholder="🔍 Search publications by title or author...">
    </div>

    <!-- Publications List -->
    <div class="publications-list">
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
      <div class="publication-item" data-year="{{ pub.year }}">
        <div class="item-content">
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
      {% endunless %}
      {% endfor %}
    </div>
  </div>
</div>
{% endif %}



<!-- JavaScript for Tab Navigation -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabs = document.querySelectorAll('.nav-tab');
  const sections = document.querySelectorAll('.publications-section');
  
  tabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const targetSection = this.dataset.section;
      
      // Update active tab
      tabs.forEach(t => t.classList.remove('active'));
      this.classList.add('active');
      
      // Show/hide sections
      sections.forEach(section => {
        if (section.id === targetSection + '-section') {
          section.classList.remove('hidden');
        } else if (section.id && section.id.includes('-section')) {
          section.classList.add('hidden');
        }
      });
    });
  });
  
  // Simple search functionality
  const searchInput = document.getElementById('search-publications');
  const publicationItems = document.querySelectorAll('.publication-item');
  
  searchInput?.addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    
    publicationItems.forEach(item => {
      const title = item.querySelector('.item-title')?.textContent.toLowerCase() || '';
      const authors = item.querySelector('.item-authors')?.textContent.toLowerCase() || '';
      
      if (title.includes(searchTerm) || authors.includes(searchTerm)) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  });
});
</script>

</div>