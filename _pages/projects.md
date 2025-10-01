---
layout: page
title: projects
permalink: /projects/
description: Our key research initiatives
nav: true
nav_order: 3
---

<!-- Current Research Projects -->
{% if site.data.projects.current and site.data.projects.current.size > 0 %}
## Current Research Projects

<div class="project-cards">
{% assign featured_current = site.data.projects.current | where: "featured", true %}
{% assign regular_current = site.data.projects.current | where: "featured", false %}
{% assign sorted_current = featured_current | concat: regular_current %}

{% for project in sorted_current %}
  <div class="project-card {% if project.featured %}featured-project{% endif %}">
    {% if project.logo and project.logo != "" %}
    <div class="project-logo-container">
      <img class="project-logo" src="{{ '/assets/img/projects/' | append: project.logo | relative_url }}" alt="{{ project.title }} Logo">
    </div>
    {% endif %}
    <div class="project-title">
      {% if project.url and project.url != "" %}
        <a href="{{ project.url }}" target="_blank">{{ project.title }}</a>
      {% else %}
        {{ project.title }}
      {% endif %}
    </div>
    <div class="project-meta">{{ project.period }}</div>
    <div class="project-desc">{{ project.description }}</div>
    
    {% if project.funding_agency or project.pi or project.team_members.size > 0 or project.keywords.size > 0 %}
    <div class="project-details">
      {% if project.funding_agency %}
      <div class="project-funding"><strong>Funding:</strong> {{ project.funding_agency }}</div>
      {% endif %}
      {% if project.pi %}
      <div class="project-pi"><strong>PI:</strong> {{ project.pi }}</div>
      {% endif %}
      {% if project.team_members and project.team_members.size > 0 %}
      <div class="project-team"><strong>Team:</strong> {{ project.team_members | join: ", " }}</div>
      {% endif %}
      {% if project.keywords and project.keywords.size > 0 %}
      <div class="project-keywords">
        {% for keyword in project.keywords %}
          <span class="keyword-tag">{{ keyword }}</span>
        {% endfor %}
      </div>
      {% endif %}
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Completed Research Projects -->
{% if site.data.projects.completed and site.data.projects.completed.size > 0 %}
## Completed Research Projects

<div class="project-cards completed-projects">
{% for project in site.data.projects.completed %}
  <div class="project-card completed">
    {% if project.logo and project.logo != "" %}
    <div class="project-logo-container">
      <img class="project-logo" src="{{ '/assets/img/projects/' | append: project.logo | relative_url }}" alt="{{ project.title }} Logo">
    </div>
    {% endif %}
    <div class="project-title">
      {% if project.url and project.url != "" %}
        <a href="{{ project.url }}" target="_blank">{{ project.title }}</a>
      {% else %}
        {{ project.title }}
      {% endif %}
    </div>
    <div class="project-meta">{{ project.period }}</div>
    <div class="project-desc">{{ project.description }}</div>
    
    {% if project.funding_agency or project.pi or project.team_members.size > 0 or project.keywords.size > 0 %}
    <div class="project-details">
      {% if project.funding_agency %}
      <div class="project-funding"><strong>Funding:</strong> {{ project.funding_agency }}</div>
      {% endif %}
      {% if project.pi %}
      <div class="project-pi"><strong>PI:</strong> {{ project.pi }}</div>
      {% endif %}
      {% if project.team_members and project.team_members.size > 0 %}
      <div class="project-team"><strong>Team:</strong> {{ project.team_members | join: ", " }}</div>
      {% endif %}
      {% if project.keywords and project.keywords.size > 0 %}
      <div class="project-keywords">
        {% for keyword in project.keywords %}
          <span class="keyword-tag">{{ keyword }}</span>
        {% endfor %}
      </div>
      {% endif %}
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
{% endif %}
      <img class="project-logo" src="{{ '/assets/img/projects/Cryo-TEMPO_logo.png' | relative_url }}" alt="Cryo-TEMPO Logo">
    </div>
    <div class="project-title">Cryo-TEMPO</div>
    <div class="project-meta">2020-2025</div>
    <div class="project-desc">Developing and providing advanced data products from the CryoSat mission, specifically for studying land ice, sea ice, and polar oceans</div>
  </div>
</div>

## Completed Projects

<div class="project-cards completed">
  <div class="project-card">
    <div class="project-logo-container">
      <img class="project-logo" src="{{ '/assets/img/projects/mesoscale_logo.svg' | relative_url }}" alt="Mesoscale Variability Project Logo">
    </div>
    <div class="project-title">Project #1</div>
    <!-- <div class="project-meta">XXXX-XXXX</div> -->
    <div class="project-desc">Add Description</div>
  </div>
  
  <div class="project-card">
    <div class="project-logo-container">
      <img class="project-logo" src="{{ '/assets/img/projects/interaction_logo.svg' | relative_url }}" alt="Ocean-Atmosphere Project Logo">
    </div>
    <div class="project-title">Project #2</div>
    <!-- <div class="project-meta">XXXX-XXXX</div> -->
    <div class="project-desc">Add Description</div>
  </div>
</div>

## Collaborative Networks
<!--
<ul class="collab-list">
  <li><strong>Global Ocean Observing System (GOOS)</strong></li>
  <li><strong>Mediterranean Ocean Observing System (MOOSE)</strong></li>
  <li><strong>International SWOT Science Team</strong></li>
  <li><strong>Copernicus Marine Service (CMEMS)</strong></li>
</ul>
-->
<ul class="collab-list">
  <li>Collaborative network 1</li>
  <li>Collaborative network 2</li>
  <li>Collaborative network 3</li>
  <li>Collaborative network 4</li>
</ul>
