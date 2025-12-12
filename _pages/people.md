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
        {% endif %}
        {% if person.linkedin and person.linkedin != "" %}
        <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
          <span>💼</span>
          <span>LinkedIn</span>
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
        {% endif %}
        {% if person.linkedin and person.linkedin != "" %}
        <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
          <span>💼</span>
          <span>LinkedIn</span>
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
        {% if person.imedea and person.imedea != "" %}
        <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
          <span>🏛️</span>
          <span>IMEDEA</span>
        </a>
        {% endif %}
        {% if person.scholar and person.scholar != "" %}
        <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
          <span>🎓</span>
          <span>Google Scholar</span>
        </a>
        {% endif %}
        {% if person.linkedin and person.linkedin != "" %}
        <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
          <span>💼</span>
          <span>LinkedIn</span>
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
        {% if person.imedea and person.imedea != "" %}
        <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
          <span>🏛️</span>
          <span>IMEDEA</span>
        </a>
        {% endif %}
        {% if person.scholar and person.scholar != "" %}
        <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
          <span>🎓</span>
          <span>Google Scholar</span>
        </a>
        {% endif %}
        {% if person.linkedin and person.linkedin != "" %}
        <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
          <span>💼</span>
          <span>LinkedIn</span>
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
        {% if person.imedea and person.imedea != "" %}
        <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
          <span>🏛️</span>
          <span>IMEDEA</span>
        </a>
        {% endif %}
        {% if person.scholar and person.scholar != "" %}
        <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
          <span>🎓</span>
          <span>Google Scholar</span>
        </a>
        {% endif %}
        {% if person.linkedin and person.linkedin != "" %}
        <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
          <span>💼</span>
          <span>LinkedIn</span>
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

<!-- Visiting/Collaborating Researchers and Alumni in same row -->
<div class="visitors-alumni-container">
  <!-- Left column: Visiting & Collaborating Researchers -->
  <div class="visitors-column">
    <h2>Visiting & Collaborating Researchers</h2>
    <div class="compact-profile-grid">
      <!-- Collaborating and Visiting Researchers -->
      {% if site.data.people.collaborating_researchers %}
        {% for person in site.data.people.collaborating_researchers %}
          <div class="compact-profile-card">
            <img src="/assets/img/team/{{ person.image }}" alt="{{ person.name }}" class="profile-img">
            <div class="profile-content">
              <h4 class="profile-name">{{ person.name }}</h4>
              <p class="profile-title">{{ person.title }}</p>
            
              <div class="profile-links">
                {% if person.email and person.email != "" %}
                  <a href="mailto:{{ person.email }}" class="social-link email"> Email</a>
                {% endif %}
                {% if person.orcid and person.orcid != "" %}
                  <a href="{{ person.orcid }}" class="social-link orcid" target="_blank">🔗 ORCID</a>
                {% endif %}
                {% if person.imedea and person.imedea != "" %}
                <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
                  <span>🏛️</span>
                  <span>IMEDEA</span>
                </a>
                {% endif %}
                {% if person.scholar and person.scholar != "" %}
                <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
                  <span>🎓</span>
                  <span>Google Scholar</span>
                </a>
                {% endif %}
                {% if person.linkedin and person.linkedin != "" %}
                <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
                  <span>💼</span>
                  <span>LinkedIn</span>
                </a>
                {% endif %}
                {% if person.website and person.website != "" %}
                <a href="{{ person.website }}" class="social-link website" target="_blank">
                  <span>🌐</span>
                  <span>Website</span>
                </a>
                {% endif %}
              </div>
              <p class="profile-bio">{{ person.bio }}</p>
            </div>
          </div>
        {% endfor %}
      {% endif %}
      
      <!-- Visiting Researchers -->
      {% if site.data.people.visiting_researchers %}
        {% for person in site.data.people.visiting_researchers %}
        <div class="compact-profile-card">
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
              {% if person.imedea and person.imedea != "" %}
              <a href="{{ person.imedea }}" class="social-link imedea" target="_blank">
                <span>🏛️</span>
                <span>IMEDEA</span>
              </a>
              {% endif %}
              {% if person.scholar and person.scholar != "" %}
              <a href="{{ person.scholar }}" class="social-link google-scholar" target="_blank">
                <span>🎓</span>
                <span>Google Scholar</span>
              </a>
              {% endif %}
              {% if person.linkedin and person.linkedin != "" %}
              <a href="{{ person.linkedin }}" class="social-link linkedin" target="_blank">
                <span>💼</span>
                <span>LinkedIn</span>
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
  </div>

  <!-- Right columns: Alumni (split into 2 columns) -->
  <div class="alumni-column">
    {% if site.data.people.alumni %}
    <h2>Alumni</h2>
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
  </div>
</div>
