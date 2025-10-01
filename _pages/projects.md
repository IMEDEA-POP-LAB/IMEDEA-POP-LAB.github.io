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
{% assign featured_projects = site.data.projects | where: "featured", true %}
{% assign regular_projects = site.data.projects | where: "featured", false %}
{% assign sorted_projects = featured_projects | concat: regular_projects %}

{% for project in sorted_projects %}
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
    
    {% if project.keywords and project.keywords.size > 0 %}
    <div class="project-details">
      <div class="project-keywords">
        {% for keyword in project.keywords %}
          <span class="keyword-tag">{{ keyword }}</span>
        {% endfor %}
      </div>
    </div>
    {% endif %}
  </div>
{% endfor %}
</div>
</div>
{% endif %}