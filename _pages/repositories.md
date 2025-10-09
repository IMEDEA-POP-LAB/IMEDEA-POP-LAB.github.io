---
layout: page
permalink: /repositories/
title: Repositories
description: Open source code, data, and tools from our research group
nav: true
nav_order: 5
---

<div class="repositories">



<!-- Repository Grid -->
<div class="repositories-grid">
  {% for repo in site.data.repositories.repositories %}
  {% unless repo.name == ".github" %}
  <div class="repository-card">
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
  {% endunless %}
  {% endfor %}
</div>

<div class="repo-footer">
  <p><em>Last updated: {{ "now" | date: "%B %Y" }} | For current repositories, visit our <a href="https://github.com/IMEDEA-POP-LAB" target="_blank">GitHub organization</a> | Part of the <a href="https://imedea.uib-csic.es/en/research/marine-technologies-operational-and-coastal-oceanography/" target="_blank">Physical Oceanography and Climate Research Group</a> at IMEDEA</em></p>
</div>

</div>


