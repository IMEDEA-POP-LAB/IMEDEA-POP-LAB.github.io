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

<!-- Principal Investigators -->
{% if site.data.team.principal_investigators %}
  {% for person in site.data.team.principal_investigators %}
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
{% endif %}

<!-- Research Scientists -->
{% if site.data.team.research_scientists %}
  {% for person in site.data.team.research_scientists %}
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
{% endif %}

<!-- Postdocs -->
{% if site.data.team.postdocs %}
  {% for person in site.data.team.postdocs %}
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
{% endif %}

<!-- PhD Students -->
{% if site.data.team.phd_students %}
  {% for person in site.data.team.phd_students %}
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
{% endif %}

<!-- Master's Students -->
{% if site.data.team.master_students %}
  {% for person in site.data.team.master_students %}
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
{% endif %}

<!-- Visiting Researchers -->
{% if site.data.team.visiting_researchers %}
  {% for person in site.data.team.visiting_researchers %}
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
{% endif %}

</div>

<!-- Alumni Section -->
{% if site.data.team.alumni %}
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