---
layout: page
title: outreach
permalink: /outreach/
description: Science communication and public engagement
nav: true
nav_order: 4
---

<!-- Lab News Section -->
{% if site.data.news and site.data.news.size > 0 %}
## Lab News

<div class="news-section">
{% for item in site.data.news limit: 10 %}
  <div class="news-item">
    <div class="news-date">{{ item.date | date: "%B %d, %Y" }}</div>
    <div class="news-content">
      <h4>{{ item.title }}</h4>
      <p>{{ item.description }}</p>
      {% if item.category %}
      <span class="news-category {{ item.category }}">{{ item.category | capitalize }}</span>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>
{% endif %}

<!-- Featured Outreach Content -->
{% if site.data.outreach and site.data.outreach.size > 0 %}
## Featured Content

<div class="featured-content">
{% for item in site.data.outreach %}
{% if item.featured %}
  <div class="featured-item">
    <div class="featured-date">{{ item.date | date: "%B %Y" }}</div>
    <div class="featured-details">
      <div class="featured-title">{{ item.title }}</div>
      <div class="featured-venue">{{ item.venue }}</div>
      {% if item.description %}
      <div class="featured-description">{{ item.description }}</div>
      {% endif %}
      {% if item.youtube_id %}
      <div class="featured-video">
        <iframe width="100%" height="200" src="https://www.youtube.com/embed/{{ item.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </div>
      {% endif %}
    </div>
  </div>
{% endif %}
{% endfor %}
</div>
{% endif %} 

## Recent Press Releases

<div class="press-releases">

  <div class="press-item">
    <div class="press-date">July 2025</div>
    <div class="press-title">
      <a href="https://www.ultimahora.es/noticias/local/2025/09/18/2471689/olas-calor-mar-balear-sistemas-medicion-podrian-estar-enganandosos.html#goog_rewarded" target="_blank">
       Olas de calor en el mar balear: Los sistemas de medición podrían estar engañándonos
      </a>
    </div>
    <div class="press-outlet">El Periódico</div>
    <div class="press-excerpt">Se ha calentado 0,036 ºC al año desde 1982, con anomalías récord en 2022 y 2023</div>
  </div>

  <div class="press-item">
    <div class="press-date">July 2025</div>
    <div class="press-title">
      <a href="https://www.elperiodico.com/es/medio-ambiente/20250707/disparado-temperatura-agua-mediterraneo-espanol-119356965" target="_blank">
       Así se ha disparado la temperatura del agua en el Mediterráneo español desde hace 40 años
      </a>
    </div>
    <div class="press-outlet">El Periódico</div>
    <div class="press-excerpt">El mar Mediterráneo, cuya temperatura media era de 22,6 °C en 1986, ha registrado picos hasta cinco grados por encima de lo normal para estas fechas, lo que lo convierte en un factor de riesgo para la formación de tormentas severas.</div>
  </div>

  <div class="press-item">
    <div class="press-date">July 2025</div>
    <div class="press-title">
      <a href="https://www.diariodemallorca.es/mallorca/2025/07/12/unica-mallorquina-expedicion-oceano-agencia-119603634.html" target="_blank">
       La única mallorquina en la expedición en el océano de la Agencia Espacial Europea: "Hay mucho por explorar"
      </a>
    </div>
    <div class="press-outlet">Diario de Mallorca</div>
    <div class="press-excerpt">La algaidina Elisabet Verger-Miralles, estudiante de doctorado de Oceanografía Física y Clima, ha sido la única mallorquina entre los seis españolas seleccionados como embajadores de la Década de las Naciones Unidas para las Ciencias Oceánicas.</div>
  </div>

  <div class="press-item">
    <div class="press-date">August 2024</div>
    <div class="press-title">
      <a href=" https://www.innovaspain.com/ananda-pascual-oceanos-libro-blanco-csic-imedea/" target="_blank">
       Ananda Pascual: "Los océanos son un espejo de lo que ocurre en el mundo"
      </a>
    </div>
    <div class="press-outlet">Innovaspain</div>
    <div class="press-excerpt">La oceanógrafa física coordina el Libro Blanco del CSIC sobre los océanos, que reúne los grandes retos de la investigación oceánica de la década.</div>
  </div>

</div>