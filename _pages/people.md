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
{% if site.data.people.principal_investigators %}
  {% for person in site.data.people.principal_investigators %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
      <div class="social-links">
        {% if person.email and person.email != "" %}
        <a href="mailto:{{ person.email }}" class="social-link email">
          <span>📧</span>
          <span>Email</span>
        </a>
        {% else %}
        <a class="social-link email disabled" aria-disabled="true" tabindex="-1">
          <span>📧</span>
          <span>Email</span>
        </a>
        {% endif %}
        {% if person.orcid and person.orcid != "" %}
        <a href="{{ person.orcid }}" class="social-link orcid" target="_blank">
          <span>🔗</span>
          <span>ORCID</span>
        </a>
        {% else %}
        <a class="social-link orcid disabled" aria-disabled="true" tabindex="-1">
          <span>🔗</span>
          <span>ORCID</span>
        </a>
        {% endif %}
        {% if person.imedea and person.imedea != "" %}
        <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
          <span>🏛️</span>
          <span>IMEDEA</span>
        </a>
        {% else %}
        <a class="social-link imedea disabled" aria-disabled="true" tabindex="-1">
          <span>🏛️</span>
          <span>IMEDEA</span>
        </a>
        {% endif %}
        {% if person.scholar and person.scholar != "" %}
        <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
          <span>🎓</span>
          <span>Google Scholar</span>
        </a>
        {% else %}
        <a class="social-link google-scholar disabled" aria-disabled="true" tabindex="-1">
          <span>🎓</span>
          <span>Google Scholar</span>
        </a>
        {% endif %}
        {% if person.website and person.website != "" %}
        <a href="{{ person.website }}" class="social-link website" target="_blank">
          <span>🌐</span>
          <span>Website</span>
        </a>
        {% else %}
        <a class="social-link website disabled" aria-disabled="true" tabindex="-1">
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
{% if site.data.people.research_scientists %}
  {% for person in site.data.people.research_scientists %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
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
{% if site.data.people.postdocs %}
  {% for person in site.data.people.postdocs %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
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
{% if site.data.people.phd_students %}
  {% for person in site.data.people.phd_students %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
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
{% if site.data.people.master_students %}
  {% for person in site.data.people.master_students %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
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
{% if site.data.people.visiting_researchers %}
  {% for person in site.data.people.visiting_researchers %}
  <div class="person-card">
    <div class="card-body">
      <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-image">
      <h5 class="card-title">{{ person.name }}</h5>
  <h6 class="card-subtitle">{{ person.title }}</h6>
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
{% if site.data.people.alumni %}
## Alumni

<div class="alumni-section">
{% for person in site.data.people.alumni %}
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