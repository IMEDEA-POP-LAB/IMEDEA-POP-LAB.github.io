# 🌊 Physical Ocean Processes - Ananda Pascual Lab

[![Jekyll](https://img.shields.io/badge/Jekyll-4.3.2-red.svg)](https://jekyllrb.com/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deployed-green.svg)](https://imedea-ap-lab.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Welcome to the Physical Ocean Processes research group website! This site showcases the work of the Ananda Pascual Lab at the Mediterranean Institute for Advanced Studies (IMEDEA).

## 🌐 Live Site
**[https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)**

## 📋 Table of Contents
- [Quick Start](#-quick-start)
- [Scripts & Automation](#-scripts--automation)
- [Site Structure](#-site-structure)
- [Content Management](#-content-management)
- [Development](#-development)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

### Direct GitHub Editing (Recommended)
1. Navigate to any file on GitHub
2. Click the pencil icon (✏️) to edit
3. Make your changes
4. Add a commit message and click "Commit changes"
5. Changes will appear on the website in 1-5 minutes

### Local Development (Optional)
```bash
git clone https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io.git
cd IMEDEA-AP-LAB.github.io
bundle install
bundle exec jekyll serve
```

## 🎨 Design System

### Modern Ocean Theme
- **Colors**: Blue gradient navigation, ocean-inspired palette
- **Typography**: Inter font family with clean, minimal headings
- **Layout**: Card-based design with consistent spacing
- **Responsive**: Mobile-first approach with flexible grids
./scripts/build.sh [--deploy]
```
- Builds the website for production
- Use `--deploy` flag to automatically commit and push changes

## 📁 Site Structure

```
IMEDEA-AP-LAB.github.io/
├── _config.yml              # Site configuration
├── _data/                   # Data files
│   ├── navigation.yml       # Navigation menu
│   └── publications.yml     # Publications database
├── _includes/               # Reusable components
│   └── recent-publications.html
├── _layouts/                # Page templates
├── _pages/                  # Main site pages
│   ├── about.md            # Homepage
│   ├── people.md           # Team page
│   ├── projects.md         # Projects page
│   ├── publications.md     # Publications page
│   ├── repositories.md     # Code repositories
│   └── outreach.md         # Outreach activities
├── assets/                 # Static assets
│   ├── css/
│   │   ├── main.scss       # Main stylesheet
│   │   └── scss/           # Organized SCSS partials
│   │       ├── base/       # Variables, mixins, reset
│   │       ├── components/ # Cards, buttons, navigation
│   │       ├── layout/     # Layout utilities
│   │       ├── pages/      # Page-specific styles
│   │       └── utilities/  # Overrides and utilities
│   └── img/                # Images
│       ├── team/           # Team photos
│       └── gallery/        # Research gallery
└── templates/              # Content templates
```

## 📝 Content Management

### Adding Team Members
Edit `_pages/people.md` and add:

```markdown
<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/name.jpg" alt="Name" class="profile-image">
    <h5 class="card-title">Dr. Full Name</h5>
    <p class="card-subtitle">Position Title</p>
    <div class="social-links">
      <a href="mailto:email@example.com" class="social-link">
        <i class="fas fa-envelope"></i> Email
      </a>
    </div>
    <p class="card-text">Brief bio and research interests.</p>
  </div>
</div>
```

### Adding Publications
Edit `_data/publications.yml` and add to the `recent:` section:

```yaml
- title: "Your Publication Title"
  authors: "Author Names"
  journal: "Journal Name"
  year: 2025
  doi: "https://doi.org/..."
  abstract: "Publication abstract"
  bibtex: |
    @article{key2025,
      title={Your Publication Title},
      author={Author Names},
      journal={Journal Name},
      year={2025}
    }
```

### Adding Projects
Use the script: `./scripts/new-content.sh project project-name`

Or manually create in `_projects/` with this template:

```yaml
---
layout: page
title: "Project Title"
description: "Brief description"
img: /assets/img/projects/project.jpg
importance: 1
category: research
---
```

## 💻 Development

### Prerequisites
- Ruby 2.7+
- Bundler
- Git

### Local Setup
```bash
# Clone repository
git clone https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io.git
cd IMEDEA-AP-LAB.github.io

# Install dependencies
bundle install

# Start development server
./scripts/serve.sh

# Or manually:
bundle exec jekyll serve --livereload
```

### Making Changes
1. Create a new branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Test locally: `./scripts/serve.sh`
4. Build for production: `./scripts/build.sh`
5. Commit and push: `git add . && git commit -m "Description" && git push`
6. Create a pull request

## 🚀 Deployment

### Automatic (Recommended)
Push to `main` branch and GitHub Pages will automatically build and deploy.

### Manual with Script
```bash
./scripts/build.sh --deploy
```

### Manual Commands
```bash
git add .
git commit -m "Update website"
git push origin main
```

## 🎨 Customization

### Colors & Styling
Edit `assets/css/main.scss` to modify:
- Color scheme (CSS variables at top)
- Typography
- Layout and spacing
- Component styles

### Navigation
Edit `_data/navigation.yml` to modify menu items:

```yaml
- name: "Home"
  link: "/"
- name: "People"
  link: "/people/"
```

### Site Configuration
Edit `_config.yml` for:
- Site title and description
- Social media links
- SEO settings
- Plugin configuration

## 🔧 Troubleshooting

### Common Issues

**Build fails:**
```bash
bundle update
./scripts/build.sh
```

**Images not loading:**
- Check file paths start with `/assets/img/`
- Verify files exist in repository
- Run `./scripts/optimize-images.sh`

**Local server won't start:**
```bash
# Kill any existing Jekyll processes
pkill -f jekyll

# Try different port
./scripts/serve.sh 4001
```

**Changes not appearing:**
- Wait 1-5 minutes for GitHub Pages to rebuild
- Check GitHub Actions tab for build status
- Clear browser cache

### Getting Help
1. Check [GitHub Issues](https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io/issues)
2. Review [Jekyll Documentation](https://jekyllrb.com/docs/)
3. Contact the lab's technical team

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Maintained by the IMEDEA-AP Physical Ocean Processes Lab**  
*Mediterranean Institute for Advanced Studies (IMEDEA)*

```markdown
### Dr. [Name]
**Position:** [Title/Role]  
**Email:** [email@example.com]  
**Research Interests:** [Brief description]

[Short bio paragraph describing their background and current research.]

---
```

### Adding a New Research Project

1. Create a new file in the `_projects/` folder
2. Name it descriptively: `your_project_name.md`
3. Use this template:

```markdown
---
layout: page
title: Your Project Title
description: Brief project description
img: /assets/img/your_project_image.jpg  # optional
importance: 1
category: current  # or "completed"
---

## Project Overview
[Detailed description of your project]

## Objectives
- Objective 1
- Objective 2
- Objective 3

## Methods
[Description of methods and approaches]

## Current Status
[What's happening now]

## Publications
- [List any related publications]

## Team Members
- [List team members involved]

## Funding
[Funding sources if applicable]
```

### Adding a New Publication

1. Go to `_pages/publications.md`
2. Add your publication in this format (most recent first):

```markdown
**[Year]** - [Authors]. "[Title]." *Journal Name*, Volume(Issue), pages. DOI: [doi link]
```

Example:
```markdown
**2025** - Pascual, A., Coauthor, F., & Second, C. "Interannual variability of Mediterranean Deep Water formation: A 20-year observational study." *Journal of Geophysical Research: Oceans*, 130(1), 123-145. DOI: [10.1029/2024JC021234](https://doi.org/10.1029/2024JC021234)
```

### Adding Images

1. Upload images to the `assets/img/` folder
2. Reference them in your content using:
   - `![Alt text](/assets/img/your-image.jpg)` for markdown files
   - `<img src="/assets/img/your-image.jpg" alt="Alt text">` for more control

## ✏️ Editing Existing Content

### Home Page
- Edit `index.html` or `_pages/about.md`
- Update lab description, mission, contact info

### Navigation Menu
- To add/remove pages from the menu, you need to create a `_data/navigation.yml` file
- Contact the site administrator for navigation changes

### Site Configuration
- Main settings are in `_config.yml`
- **Important:** Only edit basic info like title, description, email
- Do not modify plugins or advanced settings

### Styling and Colors
- Basic styling is in `assets/css/main.scss`
- The site uses CSS variables for easy color changes:
  - `--global-theme-color`: Main theme color (currently navy blue)
  - `--global-hover-color`: Link hover color
  - `--global-text-color`: Main text color

## 📁 Site Structure

```
├── _pages/           # Main site pages
│   ├── about.md      # About/Home page content
│   ├── people.md     # Team members page
│   ├── projects.md   # Projects overview
│   └── publications.md # Publications list
├── _projects/        # Individual project files
├── _layouts/         # Page templates (don't edit)
├── assets/
│   ├── css/         # Styling files
│   └── img/         # Images and media
├── _config.yml      # Site configuration
└── index.html       # Homepage
```

## 📤 Publishing Changes

### GitHub Web Interface (Easiest)
1. Make your changes directly on GitHub
2. Add a descriptive commit message
3. Click "Commit changes"
4. Wait 1-5 minutes for the site to update

### Using Git (Advanced)
```bash
git add .
git commit -m "Brief description of your changes"
git push origin main
```

## 🔧 Troubleshooting

### Site Not Updating?
1. Check the "Actions" tab on GitHub for build errors
2. Wait up to 10 minutes (GitHub Pages can be slow)
3. Clear your browser cache
4. Check that your file format is correct

### Common Issues

**Images not showing:**
- Ensure images are in `assets/img/`
- Use forward slashes in paths: `/assets/img/image.jpg`
- Check file extensions match exactly

**Markdown not rendering:**
- Check that front matter is correct (the `---` sections)
- Ensure proper markdown syntax
- Verify file has `.md` extension

**Page not appearing:**
- Ensure file is in the correct folder
- Check that front matter includes `layout: page`
- Verify no syntax errors

### Getting Help
- Check the GitHub Issues tab for common problems
- Contact the site administrator
- Review this README file

## 📝 Markdown Quick Reference

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*

- Bullet point
- Another bullet

1. Numbered list
2. Second item

[Link text](https://example.com)

![Image alt text](/assets/img/image.jpg)
```

## 🔒 Important Notes

- **Always preview your changes** before committing
- **Use descriptive commit messages** so others know what changed
- **Don't delete** files unless you're sure they're not needed
- **Ask before making major changes** to site structure or styling
- **Keep content professional** and scientifically accurate

## 👥 Site Administrators

For technical issues, major changes, or questions about site structure, contact:
- [Add primary contact here]
- [Add secondary contact here]

---

*This website is powered by Jekyll and hosted on GitHub Pages. Last updated: July 2025*
