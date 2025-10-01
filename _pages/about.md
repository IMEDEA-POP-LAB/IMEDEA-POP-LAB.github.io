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

<div class="lab-overview" style="text-align: justify;">
  <p>The Physical Ocean Processes lab at IMEDEA focuses on physical oceanography, investigating ocean dynamics at meso- and submesoscales to better understand the structure and variability of ocean circulation. By combining satellite altimetry, in situ observations, and numerical modeling, the team contributes to the validation and scientific exploitation of new altimetric products and the reconstruction of ocean state variables using advanced techniques, including artificial intelligence. Part of the research is conducted in the Mediterranean Sea, a region particularly vulnerable to climate change, where the effects of ocean warming and intensified extremes can be observed with increasing clarity. The approaches and scientific questions addressed are, however, relevant to ocean regions worldwide. Applications include improving ocean prediction systems and understanding potential impacts on marine ecosystems. Current investigations include the analysis of data from the SWOT satellite mission, the study of marine heatwaves and storm surges, the influence of small-scale dynamics on large-scale ocean circulation and climate, and the development of AI-based 3D reconstruction methods.</p>
</div>

## News

{% if site.data.news and site.data.news.size > 0 %}
{% assign featured_news = site.data.news | where: "featured", true %}
{% for item in featured_news limit: 3 %}
  <div class="news-item">
    <span class="news-date">{{ item.date | date: "%B %d, %Y" }}</span>
    <span class="news-content">{{ item.title }} - {{ item.description }}</span>
  </div>
{% endfor %}
{% endif %}

<div class="news-cta">
  <a href="/outreach/" class="cta-button">
    <span class="cta-text">View All News</span>
    <span class="cta-arrow">→</span>
  </a>
</div>

<div class="publications-cta">
  <a href="/publications/" class="cta-button">
    <span class="cta-text">View All Publications</span>
    <span class="cta-arrow">→</span>
  </a>
</div>
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

<div class="contact-footer">
  <p><strong>Principal Investigator:</strong> Dr. Ananda Pascual | <a href="mailto:ananda.pascual@imedea.uib-csic.es">ananda.pascual@imedea.uib-csic.es</a></p>
  <p><strong>Location:</strong> IMEDEA (CSIC-UIB), C/ Miquel Marquès 21, 07190 Esporles, Illes Balears, Spain</p>
</div>
