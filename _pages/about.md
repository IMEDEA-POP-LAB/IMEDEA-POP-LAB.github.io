---
layout: page
permalink: /

social: true
---

<div class="intro-hero">
  <h1 class="lab-title">Physical Ocean Processes</h1>
  <p class="lab-subtitle"><a href='https://imedea.uib-csic.es/'>Mediterranean Institute for Advanced Studies (IMEDEA)</a></p>
</div>

<div class="about-grid">
  <div class="about-main">
    <div class="lab-overview" style="text-align: left;">
      <p>The Physical Ocean Processes lab at IMEDEA focuses on physical oceanography, investigating ocean dynamics at meso- and submesoscales to better understand the structure and variability of ocean circulation. By combining satellite altimetry, in situ observations, and numerical modeling, the team contributes to the validation and scientific exploitation of new altimetric products and the reconstruction of ocean state variables using advanced techniques, including artificial intelligence. Part of the research is conducted in the Mediterranean Sea, a region particularly vulnerable to climate change, where the effects of ocean warming and intensified extremes can be observed with increasing clarity. The approaches and scientific questions addressed are, however, relevant to ocean regions worldwide. Applications include improving ocean prediction systems and understanding potential impacts on marine ecosystems. Current investigations include the analysis of data from the SWOT satellite mission, the study of marine heatwaves and storm surges, the influence of small-scale dynamics on large-scale ocean circulation and climate, and the development of AI-based 3D reconstruction methods.</p>
    </div>

    <!-- Recent Publications (kept in the main column): show first 4 items from `all` -->
    {% if site.data.publications.all and site.data.publications.all.size > 0 %}
    <div class="recent-publications">
      <div class="section-header">
        <h3>Recent Publications</h3>
      </div>
      
      <div class="recent-publications-list">
        {% for publication in site.data.publications.all limit:4 %}
        <div class="recent-publication-item">
          {% if publication.image %}
          <div class="recent-publication-image">
            <img src="{{ publication.image }}" alt="{{ publication.title }}" loading="lazy">
          </div>
          {% endif %}
          
          <div class="recent-publication-content">
            <h4 class="recent-publication-title">{{ publication.title }}</h4>
            <div class="recent-publication-authors">{{ publication.authors }}</div>
            <div class="recent-publication-journal">{{ publication.journal }} ({{ publication.year }})</div>
            {% if publication.doi or publication.url %}
            <a href="{{ publication.doi | default: publication.url }}" target="_blank" class="recent-publication-link">View Publication</a>
            {% endif %}
          </div>
        </div>
        {% endfor %}
      </div>
      
      <div class="publication-cta">
        <a href="/publications/" class="view-all-btn">
          <span class="btn-icon">📚</span>
          View All Publications
        </a>
      </div>
    </div>
    {% endif %}
  </div>

  <aside class="about-side">
    <!-- Research Gallery -->
    <div class="photo-gallery">
      <div class="gallery-grid">
        <div class="gallery-item">
          <img src="/assets/img/gallery/experiments.jpg" alt="Experiments Stall">
          <div class="gallery-caption">Explaining thermohaline circulation</div>
        </div>
        <div class="gallery-item">
          <img src="/assets/img/gallery/ctd_fast_swot.jpg" alt="CTD deployment">
          <div class="gallery-caption">Deploying oceanographic instruments</div>
        </div>
        <div class="gallery-item">
          <img src="/assets/img/gallery/oral_diego.jpg" alt="Oral Presentation">
          <div class="gallery-caption">Diego V. at the Living Planet Symposium</div>
        </div>
        <div class="gallery-item">
          <img src="/assets/img/gallery/lab_lunch.jpg" alt="Lab Lunch">
          <div class="gallery-caption">Bye Bye Laura!</div>
        </div>
        <div class="gallery-item">
          <img src="/assets/img/gallery/ciencia_per_tothom_2025.jpg" alt="Ciència per Tothom 2025">
          <div class="gallery-caption">Lab Members at Ciència per Tothom</div>
        </div>
      </div>
    </div>
  </aside>
</div>