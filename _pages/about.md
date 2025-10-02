---
layout: page
permalink: /

news: false
latest_posts: false
selected_papers: false
social: true
---

<div class="intro-hero">
  <h1 class="lab-title">Physical Ocean Processes</h1>
  <p class="lab-subtitle"><a href='https://imedea.uib-csic.es/'>Mediterranean Institute for Advanced Studies (IMEDEA)</a></p>
</div>

<div class="lab-overview" style="text-align: left;">
  <p>The Physical Ocean Processes lab at IMEDEA focuses on physical oceanography, investigating ocean dynamics at meso- and submesoscales to better understand the structure and variability of ocean circulation. By combining satellite altimetry, in situ observations, and numerical modeling, the team contributes to the validation and scientific exploitation of new altimetric products and the reconstruction of ocean state variables using advanced techniques, including artificial intelligence. Part of the research is conducted in the Mediterranean Sea, a region particularly vulnerable to climate change, where the effects of ocean warming and intensified extremes can be observed with increasing clarity. The approaches and scientific questions addressed are, however, relevant to ocean regions worldwide. Applications include improving ocean prediction systems and understanding potential impacts on marine ecosystems. Current investigations include the analysis of data from the SWOT satellite mission, the study of marine heatwaves and storm surges, the influence of small-scale dynamics on large-scale ocean circulation and climate, and the development of AI-based 3D reconstruction methods.</p>
</div>

<!-- Latest Publication -->
{% if site.data.publications.recent and site.data.publications.recent.size > 0 %}
{% assign latest_pub = site.data.publications.recent | first %}
<div class="latest-publication">
  <div class="section-header">
    <h3>Latest Publication</h3>
  </div>
  
  <article class="publication-card">
    <div class="card-header">
      <h3 class="card-title">{{ latest_pub.title }}</h3>
      <div class="card-journal">{{ latest_pub.journal }}</div>
    </div>
    
    <div class="card-content">
      <div class="card-authors">{{ latest_pub.authors }}</div>
      <div class="card-year">{{ latest_pub.year }}</div>
      
      {% if latest_pub.volume or latest_pub.pages %}
      <div class="card-details">
        {% if latest_pub.volume %}Vol. {{ latest_pub.volume }}{% endif %}{% if latest_pub.pages %}, {{ latest_pub.pages }}{% endif %}
      </div>
      {% endif %}
    </div>
    
    {% if latest_pub.doi or latest_pub.url %}
    <div class="card-actions">
      {% if latest_pub.doi %}
      <a href="{{ latest_pub.doi }}" target="_blank" class="card-link">View Paper</a>
      {% endif %}
      <a href="/publications/" class="view-all-link">View All Publications</a>
    </div>
    {% endif %}
  </article>
</div>
{% endif %}

---

<!-- Research Gallery -->
<div class="photo-gallery">
  <div class="gallery-grid">
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-1.jpg" alt="Research expedition">
      <div class="gallery-caption">Research expedition in Mediterranean Sea</div>
    </div>
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-2.jpg" alt="Laboratory work">
      <div class="gallery-caption">Data analysis and modeling</div>
    </div>
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-3.jpg" alt="Field instruments">
      <div class="gallery-caption">Deploying oceanographic instruments</div>
    </div>
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-4.jpg" alt="Team collaboration">
      <div class="gallery-caption">International collaboration meeting</div>
    </div>
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-5.jpg" alt="Satellite data">
      <div class="gallery-caption">Satellite oceanography analysis</div>
    </div>
    <div class="gallery-item">
      <img src="/assets/img/gallery/research-6.jpg" alt="Conference presentation">
      <div class="gallery-caption">Presenting at international conference</div>
    </div>
  </div>
</div>