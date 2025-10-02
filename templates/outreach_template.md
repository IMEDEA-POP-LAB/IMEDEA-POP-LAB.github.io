# 📹 OUTREACH CONTENT TEMPLATE

> **EASY METHOD**: Just edit the `_data/outreach.yml` file!

## 🚀 QUICK ADD

### Open `_data/outreach.yml` and add entry:

```yaml
- date: 2024-MM-DD
  title: "Video/Documentary Title"
  type: "documentary"  # or "interview", "webinar", "presentation"
  venue: "Platform or Event Name"
  youtube_id: "VIDEO_ID_HERE"  # Just the ID, not full URL
  description: "Brief description of the content"
  language: "en"  # or "es" for Spanish
  featured: true  # Shows prominently if true
```

## 📋 FIELD EXPLANATIONS

- **date**: Date of publication/recording (YYYY-MM-DD format)
- **title**: Full title of the video/content
- **type**: Type of content (documentary, interview, webinar, presentation, talk)
- **venue**: Platform, conference, or organization name
- **youtube_id**: YouTube video ID (just the ID after `v=`)
- **description**: Brief description of the content and context
- **language**: Language code ("en", "es", etc.)
- **featured**: `true` to show prominently, `false` for regular display

## 🎯 EXAMPLES

### Documentary
```yaml
- date: 2024-03-15
  title: "Ocean Currents: A Mediterranean Perspective"
  type: "documentary"
  venue: "Science Channel"
  youtube_id: "abc123XYZ"
  description: "30-minute documentary about Mediterranean oceanography and climate research"
  language: "en"
  featured: true
```

### Conference Presentation
```yaml
- date: 2024-02-10
  title: "SWOT Satellite Data: New Insights into Ocean Dynamics"
  type: "presentation"
  venue: "Ocean Sciences Meeting 2024"
  youtube_id: "def456ABC"
  description: "Conference presentation on using SWOT satellite data for ocean current analysis"
  language: "en"
  featured: false
```

### Interview
```yaml
- date: 2024-01-20
  title: "Women in Ocean Science"
  type: "interview"
  venue: "STEM Talks"
  youtube_id: "ghi789DEF"
  description: "Discussion about career paths in oceanography and marine research"
  language: "en"
  featured: true
```

### Webinar/Workshop
```yaml
- date: 2023-11-15
  title: "Satellite Altimetry for Ocean Research"
  type: "webinar"
  venue: "European Space Agency"
  youtube_id: "jkl012GHI"
  description: "Technical webinar on using satellite altimetry data for oceanographic studies"
  language: "en"
  featured: false
```

## 🎬 CONTENT TYPES

- **documentary**: Formal documentaries or science films
- **interview**: Q&A format interviews
- **presentation**: Conference talks, academic presentations
- **webinar**: Educational webinars or workshops
- **talk**: Public lectures, outreach talks
- **panel**: Panel discussions or roundtables
- **tutorial**: Educational/instructional content

## 🎥 YouTube ID Guide

To get the YouTube ID from a URL:
- **Full URL**: `https://www.youtube.com/watch?v=abc123XYZ`
- **YouTube ID**: `abc123XYZ` (just the part after `v=`)

## 💡 PRO TIPS

1. **Test video IDs** - Make sure the YouTube ID works before adding
2. **Write clear descriptions** - Help visitors understand the content
3. **Use featured sparingly** - Only for the most important content
4. **Include context** - Mention the event, conference, or purpose
5. **Keep titles accurate** - Use the exact title from the video

## 📅 ORGANIZING CONTENT

- **Featured content** appears prominently on the outreach page
- **Regular content** appears in a standard list format
- Content is sorted by date (newest first)
- Use `featured: true` for your best/most important content

## 🚨 COMMON MISTAKES

- Using full YouTube URL instead of just the ID
- Wrong date format (use YYYY-MM-DD)
- Missing quotes around text values
- Too long descriptions
- Forgetting to set featured status

## 🔄 MANAGING VIDEOS

### Adding New Content
1. Upload to YouTube or get YouTube ID
2. Add entry to `_data/outreach.yml`
3. Set appropriate `featured` status
4. Commit changes

### Updating Existing Content
1. Find the entry in the YAML file
2. Update the relevant fields
3. Commit changes

### Removing Content
1. Delete the entry from the YAML file
2. Commit changes (video stays on YouTube)

---

**Remember**: Outreach content appears on the website immediately after committing to GitHub!