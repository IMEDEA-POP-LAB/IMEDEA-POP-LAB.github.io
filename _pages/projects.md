---
layout: page
title: projects
permalink: /projects/
description: Current research projects
nav: true
nav_order: 3
---

{% if site.data.projects and site.data.projects.size > 0 %}
<div class="projects-container">

<div class="project-cards">
{% for project in site.data.projects %}
  {% if project.url and project.url != "" %}
  <a class="project-card" href="{{ project.url }}" target="_blank" rel="noopener noreferrer">
  {% else %}
  <div class="project-card">
  {% endif %}
    {% if project.logo and project.logo != "" %}
    <div class="project-logo-container">
      <img class="project-logo" src="{{ '/assets/img/projects/' | append: project.logo | relative_url }}" alt="{{ project.title }} Logo">
    </div>
    {% endif %}
    <div class="project-title">
      {{ project.title }}
    </div>
    <div class="project-meta">{{ project.period }}</div>
    <div class="project-desc">{{ project.description }}</div>
  {% if project.url and project.url != "" %}
  </a>
  {% else %}
  </div>
  {% endif %}
{% endfor %}
</div>
</div>
{% endif %}