---
layout: page
permalink: /people/
title: People
description: Meet our research team, past members, collaborators and visitors
nav: true
nav_order: 2
---

## Research team

<div class="people row">

{% assign all_members = site.data.team.principal_investigators | concat: site.data.team.research_scientists | concat: site.data.team.phd_students | concat: site.data.team.postdocs | concat: site.data.team.master_students | concat: site.data.team.visiting_researchers %}

{% for person in all_members %}
<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
    <h5 class="card-title">{{ person.name }}</h5>
    <h6 class="card-subtitle">{{ person.title }} ({{ person.period }})</h6>
    <div class="social-links">
      {% if person.email and person.email != "" %}
      <a href="mailto:{{ person.email }}" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      {% endif %}
      {% if person.orcid and person.orcid != "" %}
      <a href="{{ person.orcid }}" class="social-link orcid" target="_blank">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
      {% endif %}
      {% if person.scholar and person.scholar != "" %}
      <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
        <span>🎓</span>
        <span>Google Scholar</span>
      </a>
      {% endif %}
      {% if person.website and person.website != "" %}
      <a href="{{ person.website }}" class="social-link website" target="_blank">
        <span>🌐</span>
        <span>Website</span>
      </a>
      {% endif %}
    </div>
    <p class="card-text">{{ person.bio }}</p>
  </div>
</div>
{% endfor %}

</div>

<!-- Alumni Section -->
{% if site.data.team.alumni and site.data.team.alumni.size > 0 %}
## Alumni

<div class="alumni-section">
{% for person in site.data.team.alumni %}
  <div class="alumni-item">
    <strong>{{ person.name }}</strong> - {{ person.title }} ({{ person.period }})
    {% if person.current_position %}
      <br><em>Now:</em> {{ person.current_position }}
    {% endif %}
    {% if person.email and person.email != "" %}
      <br><em>Contact:</em> <a href="mailto:{{ person.email }}">{{ person.email }}</a>
    {% endif %}
  </div>
{% endfor %}
</div>
{% endif %}