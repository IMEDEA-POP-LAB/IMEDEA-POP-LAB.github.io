# 🌊 Physical Ocean Processes - Ananda Pascual Lab

**Research group website for the Physical Ocean Processes Lab at IMEDEA (Mediterranean Institute for Advanced Studies)**

This website showcases our research on ocean dynamics, satellite oceanography, and marine processes in the Mediterranean Sea and beyond.

🌐 **Live Site**: [https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)

## 🚀 NEW! Super Easy Updates

The website now uses **data files** for content management - no more HTML editing required!

### ⚡ Quick Updates (2-5 minutes each)

| Content | File | Time Required |
|---------|------|---------------|
| 👥 Team members | `_data/team.yml` | 5 minutes |
| 🔬 Projects | `_data/projects.yml` | 5 minutes |
| 📚 Publications | `_data/publications.yml` | 3 minutes |
| 🎬 Outreach | `_data/outreach.yml` | 3 minutes |
| 📰 Media | `_data/media.yml` | 3 minutes |

### 🎯 How to Update Content

1. **🌐 GitHub Web Interface** - Edit YAML files directly on GitHub (easiest)
2. **📖 Data Management Manual** - Follow the comprehensive guide in `DATA_MANAGEMENT_MANUAL.md`
3. **🤖 Repository Updates** - Use `./scripts/update_repositories.sh` for GitHub repos

## 📋 Quick Examples

### Add Publication (3 minutes)
Edit `_data/publications.yml`, add to `recent` section:
```yaml
- title: "Paper Title"
  authors: "Author1, Author2, and Author3"
  journal: "Journal Name"
  year: 2024
  doi: "https://doi.org/10.1000/example"
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

## 🛠️ Repository Updates

To update the GitHub repositories data:
```bash
./scripts/update_repositories.sh YOUR_GITHUB_TOKEN
```

This script automatically fetches and updates repository information from your GitHub organization.

## 📂 Key Files & Folders

### Data Files (Easy Updates)
- `_data/team.yml` - All team members by category
- `_data/projects.yml` - Current and completed projects
- `_data/publications.yml` - Recent publications
- `_data/outreach.yml` - Videos, documentaries, interviews
- `_data/media.yml` - Press coverage and media mentions
- `_data/repositories.yml` - GitHub repositories (auto-updated)

### Documentation
- `DATA_MANAGEMENT_MANUAL.md` - Complete guide for managing all content

### Image Folders
- `assets/img/team/` - Team member photos (400x400px)
- `assets/img/projects/` - Project logos
- `assets/img/gallery/` - Research gallery images

## 🆘 Need Help?

- **📖 Complete Guide**: `DATA_MANAGEMENT_MANUAL.md` - Comprehensive manual for all data management
- **❓ Questions**: Create a GitHub issue
- **🚨 Broke something?**: Revert changes using GitHub history

## 🎯 Pro Tips

- Follow the examples in `DATA_MANAGEMENT_MANUAL.md`
- Use consistent file naming (lowercase, underscores)
- Always use proper YAML formatting (check indentation)
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