# 📰 NEWS TEMPLATE

> **NEW EASY METHOD**: Just edit the `_data/news.yml` file!

## 🚀 QUICK ADD (Recommended)

### Open `_data/news.yml` and add at the TOP:

```yaml
- date: 2024-MM-DD
  title: "Your news title here"
  description: "Brief description of the news (1-2 sentences)"
  category: "research"  # or team, funding, conference, award, publication, other
  featured: true  # Shows on homepage if true, false otherwise
```

## 📋 FIELD EXPLANATIONS

- **date**: Date in YYYY-MM-DD format
- **title**: Concise, descriptive title
- **description**: 1-2 sentence description
- **category**: One of: research, team, funding, conference, award, publication, other
- **featured**: `true` for important news (shows on homepage), `false` for regular news

## 🎯 EXAMPLES

### Research News
```yaml
- date: 2024-10-01
  title: "New study reveals Mediterranean warming trends"
  description: "Our latest research published in Nature Climate Change shows accelerating warming in the Mediterranean Sea over the past decade."
  category: "research"
  featured: true
```

### Team News
```yaml
- date: 2024-09-15
  title: "Dr. Smith joins the lab as postdoctoral researcher"
  description: "We welcome Dr. Jane Smith, who will be working on marine heatwave dynamics using satellite data."
  category: "team"
  featured: false
```

### Funding News
```yaml
- date: 2024-08-20
  title: "ERC Grant awarded for SWOT satellite research"
  description: "The lab has been awarded a 1.5M€ ERC Starting Grant to study fine-scale ocean processes using the new SWOT satellite."
  category: "funding"
  featured: true
```

### Conference News
```yaml
- date: 2024-07-10
  title: "Presenting at Ocean Sciences Meeting 2024"
  description: "Lab members will present 3 talks and 2 posters at the Ocean Sciences Meeting in New Orleans."
  category: "conference"
  featured: false
```

### Award News
```yaml
- date: 2024-06-05
  title: "Vincent wins best student presentation award"
  description: "PhD student Vincent Combes won the best presentation award at the European Geosciences Union General Assembly."
  category: "award"
  featured: true
```

### Publication News
```yaml
- date: 2024-05-12
  title: "New paper on submesoscale eddies published in JGR"
  description: "Our study on submesoscale eddy detection using machine learning has been published in Journal of Geophysical Research: Oceans."
  category: "publication"
  featured: false
```

## ⚡ QUICK TIPS

1. **Add at the top** - New items go at the beginning of the file
2. **Keep titles short** - Under 80 characters if possible
3. **Use active voice** - "We published..." not "A paper was published..."
4. **Be specific** - Include journal names, conference names, amounts
5. **Use featured sparingly** - Only for the most important news

## 📅 CATEGORIES GUIDE

- **research**: New findings, publications, research breakthroughs
- **team**: New hires, departures, promotions, achievements
- **funding**: Grants awarded, project starts/ends
- **conference**: Presentations, conference organization, workshops
- **award**: Individual or lab awards, recognitions
- **publication**: Papers published, special issues
- **other**: Everything else (collaborations, media coverage, etc.)

## 🚨 COMMON MISTAKES

- Wrong date format (use YYYY-MM-DD)
- Missing quotes around text
- Wrong category name
- Adding at bottom instead of top
- Too long descriptions
- Inconsistent formatting

## 💡 PRO TIPS

- **Batch updates**: Add multiple news items at once
- **Link to papers**: Include DOI or URL in description when relevant  
- **Use emojis sparingly**: Only in descriptions, not titles
- **Keep it current**: Archive old news periodically
- **Cross-reference**: Mention team members by name

---

**Remember**: News appears on the website immediately after committing to GitHub!