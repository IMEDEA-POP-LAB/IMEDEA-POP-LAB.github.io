# 🌊 Physical Ocean Processes - Ananda Pascual Lab

**Research group website for the Physical Ocean Processes Lab at IMEDEA (Mediterranean Institute for Advanced Studies)**

This website showcases our research on ocean dynamics, satellite oceanography, and marine processes in the Mediterranean Sea and beyond.

🌐 **Live Site**: [https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)

## 🚀 NEW! Super Easy Updates

The website now uses **data files** for content management - no more HTML editing required!

### ⚡ Quick Updates (2-5 minutes each)

| Content | File | Time Required |
|---------|------|---------------|
| 📰 News | `_data/news.yml` | 2 minutes |
| 👥 Team members | `_data/team.yml` | 5 minutes |
| 🔬 Projects | `_data/projects.yml` | 5 minutes |
| 📚 Publications | `_data/publications.yml` | 3 minutes |

### 🎯 Three Ways to Update

1. **🌐 GitHub Web Interface** - Edit YAML files directly on GitHub (easiest)
2. **🤖 Automation Scripts** - Use guided scripts in `scripts/` folder (fastest)
3. **📖 Templates & Guides** - Follow examples in `templates/` folder (most detailed)

## 📋 Quick Examples

### Add News (2 minutes)
Edit `_data/news.yml`, add at the top:
```yaml
- date: 2024-10-01
  title: "Your news title"
  description: "Brief description"
  category: "research"
  featured: true
```

### Add Team Member (5 minutes)
1. Upload photo to `assets/img/team/lastname_firstname.jpg`
2. Edit `_data/team.yml`, add to appropriate section:
```yaml
- name: "Dr. Full Name"
  title: "Position"
  period: "2024 - present"
  image: "lastname_firstname.jpg"
  email: "email@imedea.uib-csic.es"
  bio: "Brief description"
```

### Add Project (5 minutes)
1. Upload logo to `assets/img/projects/project_logo.png`
2. Edit `_data/projects.yml`:
```yaml
- title: "Project Name"
  period: "2024-2026"
  logo: "project_logo.png"
  description: "Brief description"
  featured: true
```

## 🛠️ Automation Tools

For technical users, run these scripts for guided updates:
```bash
python3 scripts/add_team_member.py    # Interactive team member addition
python3 scripts/add_news.py           # Quick news updates
python3 scripts/add_project.py        # Project management
python3 scripts/validate_data.py      # Check for errors
```

## 📂 Key Files & Folders

### Data Files (Easy Updates)
- `_data/news.yml` - Latest lab news and updates
- `_data/team.yml` - All team members by category
- `_data/projects.yml` - Current and completed projects
- `_data/publications.yml` - Recent publications

### Templates & Help
- `templates/COMPREHENSIVE_UPDATE_GUIDE.md` - Complete instructions
- `templates/team_member_template_new.md` - Team member examples
- `templates/project_template_new.md` - Project examples
- `scripts/README.md` - Automation guide

### Image Folders
- `assets/img/team/` - Team member photos (400x400px)
- `assets/img/projects/` - Project logos
- `assets/img/gallery/` - Research gallery images

## 🆘 Need Help?

- **📖 Complete Guide**: `templates/COMPREHENSIVE_UPDATE_GUIDE.md`
- **🔧 Technical Issues**: `scripts/README.md`
- **❓ Questions**: Create a GitHub issue
- **🚨 Broke something?**: Revert changes using GitHub history

## 🎯 Pro Tips

- Start with news updates (easiest)
- Copy existing entries as templates
- Use consistent file naming (lowercase, hyphens)
- Check syntax with `scripts/validate_data.py`
- Changes appear in 2-3 minutes after committing

## Contributing

To contribute to this website:

1. **Simple content updates**: Edit data files in `_data/` folder
2. **Complex changes**: Fork → branch → edit → test → pull request
3. **Need help?** Check `scripts/README.md` or create an issue

## Development

To run this site locally:

1. Clone this repository
2. Install Jekyll: `gem install bundler jekyll`
3. Install dependencies: `bundle install`
4. Run locally: `bundle exec jekyll serve`
5. Open browser to `http://localhost:4000`

## License

This website is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

🎉 **The website is now much easier to maintain!** No more HTML/CSS knowledge required.