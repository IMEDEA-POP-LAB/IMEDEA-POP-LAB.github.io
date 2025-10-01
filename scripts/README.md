# 🚀 WEBSITE UPDATE AUTOMATION

This directory contains scripts and tools to make updating the IMEDEA Lab website much easier.

## 📁 What's New

The website now uses **data files** for content management instead of editing HTML/Markdown directly. This makes updates much faster and less error-prone.

### Key Improvements:
- ⚡ **2-minute news updates** using `_data/news.yml`
- 👥 **5-minute team member additions** using `_data/team.yml`  
- 🔬 **5-minute project additions** using `_data/projects.yml`
- 📚 **3-minute publication updates** using `_data/publications.yml`
- 🎬 **2-minute media coverage** using `_data/media.yml`
- 📹 **Outreach content** using `_data/outreach.yml`
- 🤖 **Automation scripts** for guided content creation

## 🎯 Quick Start

### For Non-Technical Users
1. **Easy Updates**: Just edit the YAML files in `_data/` folder
2. **Follow Templates**: Use examples in each data file
3. **GitHub Web Interface**: Edit directly on GitHub.com

### For Technical Users  
1. **Use Scripts**: Run Python scripts in `scripts/` folder
2. **Local Development**: Clone repo and use Jekyll locally
3. **Bulk Updates**: Edit multiple files simultaneously

## 🛠️ Available Tools

### Automation Scripts (scripts/ folder)
- `add_team_member.py` - Interactive team member addition
- `add_news.py` - Quick news/update creation  
- `add_project.py` - Project entry generation
- `validate_data.py` - Check YAML syntax and structure

### Templates (templates/ folder)
- `COMPREHENSIVE_UPDATE_GUIDE.md` - Complete update instructions
- `team_member_template_new.md` - Team member examples
- `project_template_new.md` - Project entry examples
- `news_template.md` - News update formats

### Data Files (_data/ folder)
- `news.yml` - Latest lab news and updates
- `team.yml` - All team members by category  
- `projects.yml` - Current and completed projects
- `publications.yml` - Recent publications
- `navigation.yml` - Website navigation menu

## 🚀 How to Use Scripts

### Prerequisites
```bash
# Install Python 3 and PyYAML
pip install pyyaml
```

### Running Scripts
```bash
# Add a new team member
python3 scripts/add_team_member.py

# Add news update
python3 scripts/add_news.py

# Add new project  
python3 scripts/add_project.py

# Validate all data files
python3 scripts/validate_data.py
```

## ⚡ Super Quick Updates

### Add News (2 minutes)
1. Open `_data/news.yml`
2. Add at the top:
```yaml
- date: 2024-10-01
  title: "Your news title"
  description: "Brief description"
  category: "research"
  featured: true
```

### Add Team Member (5 minutes)  
1. Upload photo to `assets/img/team/lastname_firstname.jpg`
2. Add to appropriate section in `_data/team.yml`:
```yaml
- name: "Dr. Name"
  title: "Position"  
  period: "2024 - present"
  image: "lastname_firstname.jpg"
  email: "email@imedea.uib-csic.es"
  # ... (see template for full example)
```

### Add Project (5 minutes)
1. Upload logo to `assets/img/projects/project_logo.png`
2. Add to `current:` section in `_data/projects.yml`:
```yaml
- title: "Project Title"
  period: "2024-2026"
  logo: "project_logo.png"  
  description: "Brief description"
  # ... (see template for full example)
```

## 📋 Monthly Maintenance Tasks

### Content Review Checklist
- [ ] Update team member statuses
- [ ] Add recent publications  
- [ ] Add conference news
- [ ] Update project progress
- [ ] Check external links
- [ ] Archive old news

### Technical Maintenance  
- [ ] Run validation scripts
- [ ] Check image optimization
- [ ] Review site performance
- [ ] Update dependencies

## 🎨 Image Guidelines

### Team Photos
- **Size**: 400x400px (square)
- **Format**: JPG  
- **Naming**: `lastname_firstname.jpg`
- **Location**: `assets/img/team/`

### Project Logos
- **Format**: PNG (with transparency) or JPG
- **Naming**: `projectname_logo.png`
- **Location**: `assets/img/projects/`

### Gallery Images
- **Size**: Max 1920px wide
- **Format**: JPG
- **Location**: `assets/img/gallery/`

## 🚨 Troubleshooting

### Common Issues
- **Site not building**: Check YAML syntax
- **Images not showing**: Verify file paths match exactly
- **Formatting broken**: Check indentation in YAML files

### Getting Help
- Read the comprehensive guide: `templates/COMPREHENSIVE_UPDATE_GUIDE.md`
- Check existing examples in data files
- Use GitHub Issues for technical problems
- Contact lab admin for access issues

## 💡 Pro Tips

1. **Copy existing entries** as templates
2. **Use consistent naming** for files and data
3. **Preview changes** before committing
4. **Start small** - add news first, then team members
5. **Validate YAML** syntax with online tools
6. **Backup important data** before major changes

## 📞 Support

- **Technical Issues**: Create GitHub issue
- **Content Questions**: Contact lab PI or admin  
- **Access Problems**: Contact repository maintainer
- **Training**: Schedule session with tech-savvy lab member

---

🎉 **The website is now much easier to update! No more HTML editing required.**