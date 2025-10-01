---
layout: page
permalink: /people/
title: People
description: Meet our research team, past members, collaborators and visitors
nav: true
nav_order: 2
---

<!-- Principal Investigators -->
{% if site.data.team.principal_investigators and site.data.team.principal_investigators.size > 0 %}
## Principal Investigators

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Research Scientists -->
{% if site.data.team.research_scientists and site.data.team.research_scientists.size > 0 %}
## Research Scientists

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Postdoctoral Researchers -->
{% if site.data.team.postdocs and site.data.team.postdocs.size > 0 %}
## Postdoctoral Researchers

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- PhD Students -->
{% if site.data.team.phd_students and site.data.team.phd_students.size > 0 %}
## PhD Students

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Master's Students -->
{% if site.data.team.master_students and site.data.team.master_students.size > 0 %}
## Master's Students

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Visiting Researchers -->
{% if site.data.team.visiting_researchers and site.data.team.visiting_researchers.size > 0 %}
## Visiting Researchers

<div class="people-section">
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
      {% if person.research_interests and person.research_interests.size > 0 %}
      <div class="research-interests">
        <strong>Research Interests:</strong>
        <ul>
        {% for interest in person.research_interests %}
          <li>{{ interest }}</li>
        {% endfor %}
        </ul>
      </div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Alumni -->
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
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/CombesVincent.jpeg" alt="Dr. Vincent Combes" class="profile-image">
    <h5 class="card-title">Dr. Vincent Combes</h5>
    <h6 class="card-subtitle">Ramón y Cajal Fellow (2022 - present)</h6>
    <div class="social-links">
      <a href="mailto:vcombes@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="http://www.vincentcombes.com/" class="social-link website">
        <span>🌐</span>
        <span>Website</span>
      </a>
      <a href="https://orcid.org/0000-0002-0416-1827" class="social-link orcid">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
    </div>
    <p class="card-text">Has been a Senior Research Associate at Oregon State University, in the CEOAS department since 2010. He got his Phd from Georgia Tech (Atlanta) in 2010 and an engineering degree in Hydraulics from the ENSEEIHT (France) in 2005. He is specialized in modeling realistic ocean flows in regional and coastal seas including the Gulf of Alaska, California Current, Peru Chile Current system, Patagonian shelf and Southeast Atlantic. He is particularly interested in the low frequency ocean variability, coastal and shelfbreak upwellings, eddy dynamics, transport of nutrient rich shelf water to the deep ocean and remote sensing.</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Dr. Diego Cortés-Morales" class="profile-image">
    <h5 class="card-title">Dr. Diego Cortés-Morales</h5>
    <h6 class="card-subtitle">Postdoctoral Researcher (2024 - present)</h6>
    <div class="social-links">
      <a href="mailto:dcortes@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="https://orcid.org/0009-0004-7159-2645" class="social-link orcid">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
    </div>
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/PengJenPing.jpg" alt="Dr. Jen-Ping Peng" class="profile-image">
    <h5 class="card-title">Dr. Jen-Ping Peng</h5>
    <h6 class="card-subtitle">Postdoctoral Researcher (2025 - present)</h6>
    <div class="social-links">
      <a href="mailto:jppeng@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="https://orcid.org/0000-0003-1575-0165" class="social-link orcid">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
    </div>
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Elisabet Verger-Miralles" class="profile-image">
    <h5 class="card-title">Elisabet Verger-Miralles</h5>
    <h6 class="card-subtitle">Ph.D. Student (2023 - present)</h6>
    <div class="social-links">
      <a href="mailto:everger@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="https://orcid.org/0009-0008-4222-7242" class="social-link orcid">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dr. Baptiste Mourre</div>
    </div>
    -->
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Diego Vega-Giménez" class="profile-image">
    <h5 class="card-title">Diego Vega-Giménez</h5>
    <h6 class="card-subtitle">Ph.D. Student (2023 - present)</h6>
    <div class="social-links">
      <a href="mailto:dvega@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dr. Angel Amores</div>
    </div>
     -->
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Paul Hargous" class="profile-image">
    <h5 class="card-title">Paul Hargous</h5>
    <h6 class="card-subtitle">Ph.D. Student (2024 - present)</h6>
    <div class="social-links">
      <a href="mailto:hargous@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="https://www.linkedin.com/in/paul-hargous-964874195/" class="social-link linkedin">
        <span>💼</span>
        <span>LinkedIn</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dr. Vincent Combes</div>
    </div>
    -->
    <p class="card-text">His research focuses on mesoscale ocean variability in the Mediterranean Sea, particularly on eddy kinetic energy (EKE) and geostrophic currents derived from satellite altimetry as well as ocean transport using in-situ observations and remote sensing data.</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Cristina Martí-Solana" class="profile-image">
    <h5 class="card-title">Cristina Martí-Solana</h5>
    <h6 class="card-subtitle">Ph.D. Student (2024 - present)</h6>
    <div class="social-links">
      <a href="mailto:cmarti@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
      <a href="https://orcid.org/0009-0002-8276-7717" class="social-link orcid">
        <span>🔗</span>
        <span>ORCID</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisors</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dr. Simón Ruiz</div>
    </div>
    -->
    <p class="card-text">Her research focuses on the energy cascade between meso- and submesoscales, spectral analysis of oceanographic data, and the physical processes driving vertical transport in the upper ocean.</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Blanca Fernández-Álvarez" class="profile-image">
    <h5 class="card-title">Blanca Fernández-Álvarez</h5>
    <h6 class="card-subtitle">Ph.D. Student (2024 - present)</h6>
    <div class="social-links">
      <a href="mailto:bfernandez@imedea.uib-csic.es" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dra. Bàrbara Barceló-Llull</div>
    </div>
    -->
    <p class="card-text">Her research focuses on the definition, drivers, and impacts of surface and subsurface marine heatwaves in the Mediterranean Sea, as well as their links to mesoscale ocean processes.</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Joan Armajach-Riera" class="profile-image">
    <h5 class="card-title">Joan Armajach-Riera</h5>
    <h6 class="card-subtitle">Research Support Staff (2025 - present)</h6>
    <div class="social-links">
      <a href="mailto:joanarmajach12@gmail.com" class="social-link email">
        <span>📧</span>
        <span>Email</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">PhD Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual, Dr. Angel Amores</div>
    </div>
     -->
    <p class="card-text">Add Description</p>
  </div>
</div>

<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/placeholder.svg" alt="Paula Alós" class="profile-image">
    <h5 class="card-title">Paula Alós</h5>
    <h6 class="card-subtitle">Master Student</h6>
    <div class="social-links">
      <a href="#" class="social-link email">
        <span>📚</span>
        <span>Master's Thesis</span>
      </a>
    </div>
    <!--
    <div class="supervisor-info">
      <div class="supervisor-label">Supervisor</div>
      <div class="supervisor-name">Dra. Ananda Pascual</div>
    </div>
    -->
    <p class="card-text"></p>
  </div>
</div>

</div>

## Alumni

<div class="alumni-simple">
  <div class="alumni-list">

    <h3>Postdocs</h3>
    <div class="alumni-item">
      <strong>Bàrbara Barceló-Llull</strong> (2020-2023) • Now at <a href = 'https://imedea.uib-csic.es/en/the-institute/staff/?staff_id=2340'>IMEDEA Marine Ecology Group</a>
    </div>
    <div class="alumni-item">
      <strong>Laura Gómez-Navarro</strong> (2022-2025) • Now Postdoc with a Marie Skłodowska-Curie fellowship at ICM 
    </div>

    <h3>PhD Students</h3>
    <div class="alumni-item">
      <strong>Daniel R. Tarry</strong> (2018-2023) • Now Postdoc at <a href = 'https://apl.uw.edu/'>University of Washington</a> 
    </div>
    <div class="alumni-item">
      <strong>Eugenio Cutolo</strong> (2018-2023) • Now Postdoc at <a href = 'https://www.imt-atlantique.fr/en/about/departments/mathematical-electrical-engineering'>IMT Atlantique</a> 
    </div>
    <div class="alumni-item">
      <strong>Saïd Ouala</strong> (2017-2021) • Now Tenure-Track Associate Professor at <a href = 'https://www.imt-atlantique.fr/en/person/said-ouala'>IMT Atlantique</a>
    </div>
    <div class="alumni-item">
      <strong>Romain Escudier</strong> (2011-2015) • Now at Mercator Ocean International
    </div>
    <div class="alumni-item">
      <strong>Enrique Vidal Vijande</strong> (2007-2010) • Now Founding Partner at <a href = 'https://www.solworks.eu/'>SOLWORKS</a>
    </div>

    <h3>Master's Theses</h3>
    <div class="alumni-item">
      <strong>Helena Antich Homar</strong> (2022)
    </div>
    
  </div>
</div>

## Collaborators

<div class="section-highlight collaborators-section">
  <div class="collaborators-grid">

    <div class="collaborator-card featured">
      <div class="collaborator-header">
        <h5>Dr. Simón Ruiz</h5>
        <span class="collaboration-status ongoing">Ongoing</span>
      </div>
      <div class="collaborator-affiliation">IMEDEA (CSIC-UIB)</div>
      <div class="social-links">
        <a href="https://imedea.uib-csic.es/en/the-institute/staff/?staff_id=316" target="_blank" class="social-link imedea-link">
          <span>🏢</span>
          <span>IMEDEA</span>
        </a>
      </div> 
    </div>
    
     <div class="collaborator-card featured">
      <div class="collaborator-header">
        <h5>Dra. Bárbara Barceló-Llull</h5>
        <span class="collaboration-status ongoing">Ongoing</span>
      </div>
      <div class="collaborator-affiliation">IMEDEA (CSIC-UIB)</div>
      <div class="social-links">
        <a href="https://imedea.uib-csic.es/en/the-institute/staff/?staff_id=2340" target="_blank" class="social-link imedea-link">
          <span>🏢</span>
          <span>IMEDEA</span>
        </a>
      </div>
    </div>

    <div class="collaborator-card featured">
      <div class="collaborator-header">
        <h5>Collaborator #3</h5>
        <span class="collaboration-status ongoing">Ongoing</span>
      </div>
      <div class="collaborator-affiliation">IMEDEA (CSIC-UIB)</div>
    </div>

    <div class="collaborator-card featured">
      <div class="collaborator-header">
        <h5>Collaborator #4</h5>
        <span class="collaboration-status ongoing">Ongoing</span>
      </div>
      <div class="collaborator-affiliation">IMEDEA (CSIC-UIB)</div>
    </div>

  </div>
</div>

## Visitors

<div class="section-highlight visitors-section">
  <div class="visitors-grid">

    <div class="visitor-card featured">
      <div class="visitor-header">
        <h5>[Name]</h5>
        <span class="visit-status current">June - Aug 2024</span>
      </div>
      <div class="visitor-affiliation">Woods Hole Oceanographic Institution, USA</div>
    </div>

    <div class="visitor-card featured">
      <div class="visitor-header">
        <h5>[Name]</h5>
        <span class="visit-status current">June - Aug 2024</span>
      </div>
      <div class="visitor-affiliation">Woods Hole Oceanographic Institution, USA</div>
    </div>

    <div class="visitor-card featured">
      <div class="visitor-header">
        <h5>[Name]</h5>
        <span class="visit-status current">June - Aug 2024</span>
      </div>
      <div class="visitor-affiliation">Woods Hole Oceanographic Institution, USA</div>
    </div>

    <div class="visitor-card featured">
      <div class="visitor-header">
        <h5>[Name]</h5>
        <span class="visit-status current">June - Aug 2024</span>
      </div>
      <div class="visitor-affiliation">Woods Hole Oceanographic Institution, USA</div>
    </div>
    
  </div>
</div>
