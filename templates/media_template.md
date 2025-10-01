# 📰 MEDIA COVERAGE TEMPLATE

> **EASY METHOD**: Just edit the `_data/media.yml` file!

## 🚀 QUICK ADD

### Open `_data/media.yml` and add at the TOP:

```yaml
- date: 2024-MM-DD
  title: "Article or Interview Title"
  outlet: "Publication Name"
  url: "https://full-article-url.com"
  excerpt: "Brief excerpt or summary of the coverage"
  language: "en"  # or "es" for Spanish
  type: "press"   # or "interview", "feature", "podcast"
```

## 📋 FIELD EXPLANATIONS

- **date**: Date of publication (YYYY-MM-DD format)
- **title**: Full title of the article/interview
- **outlet**: Name of the publication/media outlet
- **url**: Complete URL to the article
- **excerpt**: Brief summary or key quote from the article
- **language**: Language code ("en" for English, "es" for Spanish, etc.)
- **type**: Type of coverage (press, interview, feature, podcast, radio, tv)

## 🎯 EXAMPLES

### Press Article
```yaml
- date: 2024-10-01
  title: "Mediterranean Sea Temperatures Reach Record Highs"
  outlet: "Science Daily"
  url: "https://sciencedaily.com/article/med-temperatures"
  excerpt: "New research shows unprecedented warming trends in the Mediterranean Sea, with implications for marine ecosystems."
  language: "en"
  type: "press"
```

### Interview
```yaml
- date: 2024-09-15
  title: "Ocean Scientist Discusses Climate Impact on Mediterranean"
  outlet: "BBC Science"
  url: "https://bbc.com/science/interview-ocean-climate"
  excerpt: "Dr. Pascual explains how satellite data reveals changing ocean patterns and their connection to climate change."
  language: "en"
  type: "interview"
```

### Spanish Media
```yaml
- date: 2024-08-20
  title: "Científica balear estudia las corrientes marinas del Mediterráneo"
  outlet: "Diario de Mallorca"
  url: "https://diariodemallorca.es/article"
  excerpt: "La investigación con satélites revela cambios preocupantes en la temperatura del mar Mediterráneo."
  language: "es"
  type: "press"
```

### Podcast/Radio
```yaml
- date: 2024-07-10
  title: "Ocean Currents and Climate Change"
  outlet: "Science Radio"
  url: "https://scienceradio.com/episode-123"
  excerpt: "45-minute discussion about oceanographic research and satellite technology."
  language: "en"
  type: "podcast"
```

## 📅 MEDIA TYPES

- **press**: News articles, press releases
- **interview**: Q&A format interviews  
- **feature**: Long-form feature articles
- **podcast**: Audio interviews/discussions
- **radio**: Radio show appearances
- **tv**: Television interviews
- **documentary**: Documentary appearances
- **blog**: Blog posts about the research

## 💡 PRO TIPS

1. **Add at the top** - New items go at the beginning of the file
2. **Use full URLs** - Include https:// for proper linking
3. **Keep excerpts short** - 1-2 sentences maximum
4. **Be accurate** - Double-check outlet names and titles
5. **Include quotes** - Use key quotes from the coverage when possible

## 🚨 COMMON MISTAKES

- Wrong date format (use YYYY-MM-DD)
- Missing quotes around text
- Broken or incomplete URLs
- Too long excerpts
- Misspelled outlet names

## 🔄 UPDATING EXISTING ENTRIES

To update an existing entry, just find it in the file and modify the relevant fields. The website will automatically update when you commit the changes.

---

**Remember**: Media coverage appears on the website immediately after committing to GitHub!