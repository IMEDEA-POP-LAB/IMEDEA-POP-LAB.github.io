# IMEDEA-AP Oceanography Lab Website

Welcome to the IMEDEA-AP Physical Oceanography Laboratory website! This site is built with Jekyll and hosted on GitHub Pages.

## 🌐 Live Site
Visit our website at: [https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Adding New Content](#adding-new-content)
- [Editing Existing Content](#editing-existing-content)
- [Site Structure](#site-structure)
- [Publishing Changes](#publishing-changes)
- [Troubleshooting](#troubleshooting)

## 🚀 Quick Start

### For Simple Edits (Recommended)
1. Navigate to any file on GitHub
2. Click the pencil icon (✏️) to edit
3. Make your changes
4. Scroll down and add a commit message
5. Click "Commit changes"
6. Changes will appear on the website in 1-5 minutes

### For Advanced Users
```bash
git clone https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io.git
cd IMEDEA-AP-LAB.github.io
# Make your changes
git add .
git commit -m "Your commit message"
git push origin main
```

## ➕ Adding New Content

### Adding a New Team Member

1. Go to `_pages/people.md`
2. Add a new person in this format:

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
