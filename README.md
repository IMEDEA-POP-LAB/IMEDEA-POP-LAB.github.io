# 🌊 Physical Ocean Processes - Ananda Pascual Lab

[![Jekyll](https://img.shields.io/badge/Jekyll-4.3.2-red.svg)](https://jekyllrb.com/)
[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-deployed-green.svg)](https://imedea-ap-lab.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Welcome to the Physical Ocean Processes research group website! This site showcases the work of the Ananda Pascual Lab at the Mediterranean Institute for Advanced Studies (IMEDEA).

## 🌐 Live Site
**[https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)**

## 📋 Table of Contents
- [Quick Start](#-quick-start)
- [Site Architecture](#-site-architecture)
- [Content Management](#-content-management)
- [Development](#-development)
- [Deployment](#-deployment)
- [Troubleshooting](#-troubleshooting)

## 🚀 Quick Start

### Direct GitHub Editing (Recommended)
1. Navigate to any file on GitHub
2. Click the pencil icon (✏️) to edit
3. Make your changes using markdown
4. Add a descriptive commit message
5. Click "Commit changes"
6. Changes will appear on the website in 1-5 minutes

### Local Development (Optional)
```bash
git clone https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io.git
cd IMEDEA-AP-LAB.github.io
bundle install
bundle exec jekyll serve
```
## Design

### Modular SCSS Structure
The website uses a maintainable SCSS architecture:

```
_sass/
├── _index.scss              # Main SCSS index file
├── base/                    # Foundation styles
│   ├── _variables.scss      # CSS variables and colors
│   ├── _mixins.scss         # Reusable SCSS mixins
│   ├── _reset.scss          # CSS reset and normalize
│   └── _typography.scss     # Font and text styles
├── components/              # Reusable UI components
│   ├── _buttons.scss        # Button styles and DOI links
│   ├── _cards.scss          # Card components
│   └── _navigation.scss     # Navigation bar styling
├── layout/                  # Layout components
│   ├── _layout.scss         # General layout utilities
│   ├── _footer.scss         # Site footer styling
│   └── _utilities.scss      # Helper classes
├── pages/                   # Page-specific styles
│   ├── _about.scss          # Homepage and about styles
│   ├── _people.scss         # Team page styling
│   ├── _publications.scss   # Publications page layout
│   ├── _projects.scss       # Projects page styling
│   ├── _repositories.scss   # Code repositories styling
│   └── _outreach.scss       # Outreach activities styling
└── utilities/
    └── _overrides.scss      # Final overrides and tweaks
```

### Site Structure

```
IMEDEA-AP-LAB.github.io/
├── _config.yml              # Site configuration
├── _data/                   # Data files
│   └── navigation.yml       # Navigation menu structure
├── _includes/               # Reusable components (currently empty)
├── _layouts/                # Page templates
│   ├── default.html         # Base layout with header/footer
│   ├── page.html           # Standard page layout
│   └── about.html          # About page specific layout
├── _pages/                  # Main site pages
│   ├── about.md            # Homepage content
│   ├── people.md           # Team page
│   ├── projects.md         # Projects overview
│   ├── publications.md     # Publications with organized sections
│   ├── repositories.md     # Code repositories
│   └── outreach.md         # Outreach activities
├── _sass/                   # Modular SCSS files (see above)
├── assets/                  # Static assets
│   ├── css/
│   │   └── main.scss       # Main stylesheet entry point
│   └── img/                # Images organized by category
│       ├── team/           # Team member photos
│       ├── gallery/        # Research gallery images
│       └── about/          # About page images
├── templates/               # Content creation templates
└── documentation/           # Project documentation
    ├── CSS_ORGANIZATION.md  # SCSS structure guide
    └── DEVELOPMENT.md       # Development guidelines
```

## 📝 Content Management

### Publications Management

The publications page is organized into three main sections:

#### Recent Publications (Featured)
Featured publications with enhanced card-based layout:
```markdown
<div class="publication-item featured">
  <div class="publication-header">
    <h4 class="publication-title">Your Publication Title</h4>
    <div class="publication-meta">
      <span class="journal">Journal Name</span>
      <span class="year">2025</span>
    </div>
  </div>
  <div class="publication-authors">Author Names</div>
  <div class="publication-links">
    <a href="https://doi.org/..." class="link-doi">DOI</a>
  </div>
</div>
```

#### Accepted Papers
For papers accepted but not yet published:
```markdown
<div class="publication-item">
  <p class="publication-citation preprint">
    <strong>Paper Title</strong><br>
    Authors<br>
    <em class="preprint-server">Journal/Preprint Server</em> (<span class="year">2025</span>) 
    <a href="https://doi.org/..." class="link-doi">DOI</a>
  </p>
</div>
```

#### All Publications
Complete list with consistent DOI button styling:
```markdown
<div class="publication-item">
  <p class="publication-citation">
    <strong>Publication Title</strong><br>
    Authors<br>
    <em class="journal">Journal Name</em> (<span class="year">Year</span>)
  </p>
  <div class="publication-links">
    <a href="https://doi.org/..." class="link-doi">DOI</a>
  </div>
</div>
```

### Adding Team Members

Edit `_pages/people.md` with organized sections:

#### Principal Investigator
```markdown
<div class="supervisor-info">
  <div class="supervisor-content">
    <h3>Dr. Ananda Pascual</h3>
    <p class="supervisor-title">Principal Investigator</p>
    <p class="supervisor-bio">Research background and expertise...</p>
  </div>
</div>
```

#### Current Team Members
```markdown
<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/name.jpg" alt="Name" class="profile-image">
    <h5 class="card-title">Dr. Full Name</h5>
    <p class="card-subtitle">Position Title</p>
    <div class="social-links">
      <a href="mailto:email@example.com" class="social-link">
        <i class="fas fa-envelope"></i>
      </a>
      <a href="https://orcid.org/..." class="social-link">
        <i class="ai ai-orcid"></i>
      </a>
    </div>
    <p class="card-text">Research interests and brief bio.</p>
  </div>
</div>
```

#### Alumni
```markdown
<div class="alumni-grid">
  <div class="alumni-card">
    <h5>Dr. Alumni Name</h5>
    <p class="alumni-position">Former Position (Years)</p>
    <p class="alumni-current">Current Position at Institution</p>
  </div>
</div>
```

### Adding Projects

Create new files in `_projects/` or edit `_pages/projects.md`:

```markdown
<div class="project-card">
  <h4>Project Title</h4>
  <p class="project-description">Brief project description highlighting key objectives and methods.</p>
  <div class="project-links">
    <a href="/project-details/" class="btn btn-primary">Learn More</a>
  </div>
</div>
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
bundle exec jekyll serve --livereload

# View site at http://localhost:4000
```

### CSS Development

The site uses a modular SCSS architecture for maintainability:

#### Adding New Styles
1. **Page-specific styles**: Add to appropriate file in `_sass/pages/`
2. **Component styles**: Add to relevant file in `_sass/components/`
3. **Global variables**: Modify `_sass/base/_variables.scss`

#### CSS Variables
Key customizable variables in `_sass/base/_variables.scss`:
```scss
--ocean-blue: #2E86C1;
--ocean-deep: #1B4F72;
--gray-50: #F8F9FA;
--text-color: #2C3E50;
```

#### Button Styling
DOI and other link buttons use consistent styling:
```scss
.link-doi {
  padding: var(--space-1) var(--space-3);
  background: var(--ocean-blue);
  color: white;
  border-radius: var(--radius-md);
  // ... additional properties
}
```

### Making Changes
1. **Create feature branch**: `git checkout -b feature/your-feature`
2. **Make changes**: Edit relevant files
3. **Test locally**: `bundle exec jekyll serve`
4. **Build for production**: `bundle exec jekyll build`
5. **Commit and push**: 
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature
   ```
6. **Create pull request** on GitHub

### File Organization
- **SCSS files**: Follow the modular structure in `_sass/`
- **Page content**: Edit markdown files in `_pages/`
- **Images**: Organize by category in `assets/img/`
- **Templates**: Use files in `templates/` for new content

## 🚀 Deployment

### Automatic (Recommended)
Push to `main` branch and GitHub Pages will automatically build and deploy:
```bash
git add .
git commit -m "Update content"
git push origin main
```

Site updates typically appear within 1-5 minutes.

### Manual Commands
```bash
# Full deployment workflow
git add .
git commit -m "Descriptive commit message"
git push origin main

# Check build status
# Visit: https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io/actions
```

## 🎨 Customization

### Site Configuration
Edit `_config.yml` for basic site settings:
```yaml
title: Ananda Pascual Lab
description: Mediterranean Institute for Advanced Studies
email: ananda.pascual@imedea.uib-csic.es
url: https://imedea-ap-lab.github.io

# Social media links
github_username: IMEDEA-AP-LAB
orcid_id: 0000-0002-3832-9593
```

### Navigation Menu
Edit `_data/navigation.yml`:
```yaml
- name: "About"
  link: "/about/"
- name: "People"
  link: "/people/"
- name: "Publications"
  link: "/publications/"
```

### Footer Content
The comprehensive footer is automatically populated from `_config.yml`:
- Contact information
- Navigation links
- Social media profiles
- Copyright and attribution

## 🔧 Troubleshooting

### Common Issues

**DOI buttons not displaying:**
- Check that `<div class="publication-links">` wrapper is present
- Ensure `class="link-doi"` is applied to links
- Verify SCSS compilation (check browser console)

**Build fails:**
```bash
bundle update
bundle exec jekyll build
```

**Images not loading:**
- Check file paths start with `/assets/img/`
- Verify files exist in repository
- Ensure proper file extensions (.jpg, .png, .svg)

**Local server won't start:**
```bash
# Kill any existing Jekyll processes
pkill -f jekyll

# Try different port
bundle exec jekyll serve --port 4001
```

**Changes not appearing on live site:**
- Wait 1-5 minutes for GitHub Pages to rebuild
- Check GitHub Actions tab for build status
- Clear browser cache (Ctrl+Shift+R or Cmd+Shift+R)
- Verify changes are pushed to `main` branch

**SCSS compilation errors:**
- Check syntax in `_sass/` files
- Ensure all imports in `_sass/_index.scss` point to existing files
- Validate CSS variable usage

**Navigation not working:**
- Check `_data/navigation.yml` syntax
- Ensure page files exist in `_pages/`
- Verify front matter in page files

### Development Tips

**CSS Debugging:**
1. Use browser developer tools
2. Check compiled CSS in `_site/assets/css/main.css`
3. Validate SCSS syntax online

**Content Issues:**
1. Check markdown syntax
2. Verify front matter format
3. Ensure proper file encoding (UTF-8)

**Performance:**
1. Optimize images before uploading
2. Use appropriate image formats (WebP for modern browsers)
3. Minimize custom CSS

### Getting Help
1. Check [GitHub Issues](https://github.com/IMEDEA-AP-LAB/IMEDEA-AP-LAB.github.io/issues)
2. Review [Jekyll Documentation](https://jekyllrb.com/docs/)
3. Consult project documentation in `/documentation/`
4. Contact the site administrators

## 📚 Documentation

Additional documentation available in the repository:

- **CSS_ORGANIZATION.md**: Detailed SCSS structure and guidelines
- **DEVELOPMENT.md**: Advanced development practices
- **templates/**: Content creation templates

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes following the established patterns
4. Test thoroughly using local development server
5. Submit a pull request with detailed description

### Contribution Guidelines
- Follow the modular SCSS architecture
- Use consistent naming conventions
- Test on multiple screen sizes
- Document any new features
- Maintain accessibility standards

## 👥 Site Administrators

For technical issues, major changes, or questions about site structure:
- **Primary Contact**: [Add primary contact here]
- **Technical Support**: [Add technical contact here]
- **Content Management**: [Add content manager here]

---

**Maintained by the IMEDEA-AP Physical Ocean Processes Lab**  
*Mediterranean Institute for Advanced Studies (IMEDEA)*  
*University of the Balearic Islands (UIB) - Spanish National Research Council (CSIC)*

**Website**: https://imedea-ap-lab.github.io  
**Last Updated**: July 2025  
**Jekyll Version**: 4.3.2  
**Deployment**: GitHub Pages
