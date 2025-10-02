# 📝 COMPREHENSIVE UPDATE GUIDE

> **NEW!** The website now uses data files for easier content management. No more editing HTML/Markdown manually!

## 🚀 EASY UPDATES (Data File Method)

### 📰 Adding News/Updates
**File:** `_data/news.yml`
**Instructions:**
1. Open `_data/news.yml`
2. Add new entry at the TOP of the file:
```yaml
- date: 2024-MM-DD
  title: "Your news title"
  description: "Brief description of the news"
  category: "research|team|funding|conference|award"
  featured: true  # Shows on homepage if true
```

### 👥 Adding Team Members
**File:** `_data/team.yml`
**Instructions:**
1. Upload photo to `assets/img/team/lastname_firstname.jpg` (400x400px)
2. Add entry to appropriate section in `_data/team.yml`:
```yaml
- name: "Dr. Full Name"
  title: "Position Title"
  period: "YYYY - present"
  image: "lastname_firstname.jpg"
  email: "email@imedea.uib-csic.es"
  orcid: "https://orcid.org/0000-0000-0000-0000"
  scholar: "https://scholar.google.com/..."
  website: "https://personal-website.com"
  bio: "Brief biography (2-3 sentences)"
  research_interests:
    - "Research area 1"
    - "Research area 2"
```

### 🔬 Adding Projects
**File:** `_data/projects.yml`
**Instructions:**
1. Upload logo to `assets/img/projects/project_logo.png`
2. Add to `current:` or `completed:` section:
```yaml
- title: "Project Title"
  period: "YYYY-YYYY"
  logo: "project_logo.png"
  url: "https://project-website.com"
  description: "Brief project description"
  funding_agency: "Funding Organization"
  pi: "Principal Investigator"
  team_members: ["Member 1", "Member 2"]
  keywords: ["keyword1", "keyword2"]
  featured: true  # Shows prominently if true
```

### 📚 Adding Publications
**File:** `_data/publications.yml`
**Instructions:**
Add to `recent:` section:
```yaml
- title: "Publication Title"
  authors: "Author1, A.; Author2, B."
  journal: "Journal Name"
  year: 2024
  doi: "https://doi.org/10.xxxx/xxxxx"
  abstract: "Brief abstract"
  bibtex: |
    @article{key2024,
      title={Publication Title},
      author={Author1, A. and Author2, B.},
      journal={Journal Name},
      year={2024}
    }
```

## 🎯 QUICK TASK REFERENCE

| Task | File | Time Required |
|------|------|---------------|
| Add news | `_data/news.yml` | 2 minutes |
| Add team member | `_data/team.yml` + photo | 5 minutes |
| Add project | `_data/projects.yml` + logo | 5 minutes |
| Add publication | `_data/publications.yml` | 3 minutes |
| Update contact info | `_config.yml` | 2 minutes |

## 📁 NEW FILE STRUCTURE

### Data Files (Easy Updates)
- `_data/news.yml` - News and updates
- `_data/team.yml` - Team members
- `_data/projects.yml` - Research projects
- `_data/publications.yml` - Publications
- `_data/navigation.yml` - Site navigation

### Page Files (Rarely Need Editing)
- `_pages/about.md` - About page content
- `_pages/people.md` - People page (now uses data)
- `_pages/projects.md` - Projects page (now uses data)
- `_pages/publications.md` - Publications page
- `_pages/outreach.md` - Outreach and news

### Assets
- `assets/img/team/` - Team member photos (400x400px)
- `assets/img/projects/` - Project logos (any size)
- `assets/img/gallery/` - Gallery images

## 🎨 IMAGE GUIDELINES

### Team Photos
- **Size**: 400x400px (square)
- **Format**: JPG preferred
- **Naming**: `lastname_firstname.jpg`
- **Style**: Professional headshot, good lighting

### Project Logos
- **Format**: PNG for logos with transparency, JPG for photos
- **Naming**: `projectname_logo.png`
- **Size**: Any size, but optimize for web

### Gallery Images
- **Format**: JPG for photos
- **Size**: Max 1920px wide
- **Naming**: Descriptive with hyphens

## 💡 PRO TIPS

### For Non-Technical Users
1. **Use GitHub web interface** - Edit files directly on GitHub.com
2. **Preview before committing** - Use the "Preview" tab
3. **Small changes first** - Start with news updates
4. **Copy existing entries** - Use as templates

### For Technical Users
1. **Clone locally** for bulk updates
2. **Use VS Code** with YAML extension
3. **Test locally** with Jekyll serve
4. **Batch image optimization** before uploading

### General Best Practices
1. **Consistent naming** - Use lowercase, hyphens for spaces
2. **Alt text always** - Describe images for accessibility
3. **Mobile-first** - Check on phone/tablet
4. **Keep it current** - Remove outdated content
5. **Backup important data** - Before major changes

## 🚨 TROUBLESHOOTING

### Common Issues
- **Site not building?** Check YAML syntax with online validator
- **Images not showing?** Verify file path and name match exactly
- **Formatting broken?** Check indentation in YAML files
- **Changes not visible?** Wait 2-3 minutes for GitHub Pages rebuild

### Getting Help
- Check `templates/` folder for examples
- Compare with existing entries in data files
- Use GitHub Issues for technical problems
- Contact lab admin for access issues

## 📋 MONTHLY MAINTENANCE CHECKLIST

- [ ] Add recent publications to `_data/publications.yml`
- [ ] Update team member status (graduations, departures)
- [ ] Add conference presentations to news
- [ ] Update project status (completed, new funding)
- [ ] Check all external links still work
- [ ] Review and archive old news items
- [ ] Update gallery with recent research images