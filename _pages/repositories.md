---
layout: page
permalink: /repositories/
title: Repositories
description: Open source code, data, and tools from our research group
nav: true
nav_order: 5
---

<div class="repositories">

<!-- Repository Stats Overview -->
<div class="repository-stats-overview">
  <div class="stats-card">
    <span class="stats-number">{{ site.data.repositories.repositories | size }}</span>
    <span class="stats-label">Public Repositories</span>
  </div>
  <div class="stats-card">
    <span class="stats-number">{{ site.data.repositories.repositories | where: "featured", true | size }}</span>
    <span class="stats-label">Featured Projects</span>
  </div>
  <div class="stats-card">
    <span class="stats-number">{{ site.data.repositories.repositories | map: "language" | uniq | size }}</span>
    <span class="stats-label">Languages</span>
  </div>
  <div class="stats-card">
    <span class="stats-number">{{ site.data.repositories.repositories | where: "archived", false | size }}</span>
    <span class="stats-label">Active Projects</span>
  </div>
</div>

<!-- Featured Repository Section -->
{% assign featured_repos = site.data.repositories.repositories | where: "featured", true %}
{% if featured_repos.size > 0 %}
{% assign featured = featured_repos.first %}
<div class="featured-repository">
  <h2><i class="fas fa-star"></i> Featured Repository</h2>
  <h3>{{ featured.name }}</h3>
  <p>{{ featured.description }}</p>
  <a href="{{ featured.html_url }}" target="_blank" class="featured-repository-button">
    <i class="fab fa-github"></i>
    View on GitHub
  </a>
</div>
{% endif %}

<!-- Category Filters -->
{% assign categories = site.data.repositories.repositories | map: "category" | uniq | compact %}
{% if categories.size > 1 %}
<div class="repository-categories">
  <button class="category-filter active" data-category="all">All Repositories</button>
  {% for category in categories %}
  <button class="category-filter" data-category="{{ category | downcase | replace: ' ', '-' }}">{{ category }}</button>
  {% endfor %}
</div>
{% endif %}

<!-- Repository Grid -->
<div class="repositories-grid">
  {% for repo in site.data.repositories.repositories %}
  <div class="repository-card" data-category="{{ repo.category | default: 'general' | downcase | replace: ' ', '-' }}">
    <div class="repository-header">
      <div class="repository-icon">
        <i class="fab fa-github"></i>
      </div>
      <div class="repository-info">
        <h3 class="repository-name">
          <a href="{{ repo.html_url }}" target="_blank">{{ repo.name }}</a>
        </h3>
        {% if repo.language %}
        <div class="repository-meta">
          <div class="repository-meta-item">
            <i class="fas fa-code"></i>
            <span class="repository-language">{{ repo.language }}</span>
          </div>
          {% if repo.updated_at %}
          <div class="repository-meta-item">
            <i class="fas fa-clock"></i>
            <span>Updated {{ repo.updated_at | date: "%b %Y" }}</span>
          </div>
          {% endif %}
        </div>
        {% endif %}
      </div>
    </div>
    
    <p class="repository-description">{{ repo.description }}</p>
    
    <div class="repository-stats">
      {% if repo.stargazers_count %}
      <div class="repository-stat">
        <i class="fas fa-star"></i>
        <span>{{ repo.stargazers_count }}</span>
      </div>
      {% endif %}
      {% if repo.forks_count %}
      <div class="repository-stat">
        <i class="fas fa-code-branch"></i>
        <span>{{ repo.forks_count }}</span>
      </div>
      {% endif %}
      {% if repo.license.name %}
      <div class="repository-stat">
        <i class="fas fa-balance-scale"></i>
        <span>{{ repo.license.spdx_id | default: repo.license.name }}</span>
      </div>
      {% endif %}
    </div>
    
    {% if repo.topics.size > 0 %}
    <div class="repository-topics">
      {% for topic in repo.topics limit: 5 %}
      <span class="topic">{{ topic }}</span>
      {% endfor %}
    </div>
    {% endif %}
    
    <div class="repository-links">
      <a href="{{ repo.html_url }}" target="_blank" class="repository-link primary">
        <i class="fab fa-github"></i> View Code
      </a>
      {% if repo.homepage %}
      <a href="{{ repo.homepage }}" target="_blank" class="repository-link">
        {% if repo.doi %}
        <i class="fas fa-book"></i> DOI
        {% else %}
        <i class="fas fa-external-link-alt"></i> Website
        {% endif %}
      </a>
      {% endif %}
    </div>
  </div>
  {% endfor %}
</div>

<div class="repo-footer">
  <p><em>Last updated: {{ "now" | date: "%B %Y" }} | For current repositories, visit our <a href="https://github.com/IMEDEA-AP-LAB" target="_blank">GitHub organization</a> | Part of the <a href="https://imedea.uib-csic.es/en/research/marine-technologies-operational-and-coastal-oceanography/" target="_blank">TMOOC Research Group</a> at IMEDEA</em></p>
</div>

</div>

<script>
// Category filtering functionality
document.addEventListener('DOMContentLoaded', function() {
  const categoryButtons = document.querySelectorAll('.category-filter');
  const repositoryCards = document.querySelectorAll('.repository-card');
  
  categoryButtons.forEach(button => {
    button.addEventListener('click', function() {
      const category = this.getAttribute('data-category');
      
      // Update active button
      categoryButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
      
      // Filter repositories
      repositoryCards.forEach(card => {
        if (category === 'all' || card.getAttribute('data-category') === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
</script>
