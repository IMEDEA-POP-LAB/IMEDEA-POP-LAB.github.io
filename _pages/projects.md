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
  <div class="project-card">
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
  </div>
{% endfor %}
</div>
</div>
{% endif %}