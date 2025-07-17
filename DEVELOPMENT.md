# 🛠️ Development Guide

This guide covers advanced development topics for the IMEDEA-AP Lab website.

## 🏗️ Architecture

The website is built with:
- **Jekyll**: Static site generator
- **GitHub Pages**: Hosting and automatic deployment
- **SCSS**: Styling with modern CSS features
- **Liquid**: Templating language

## 📂 Key Files

### Configuration
- `_config.yml` - Main site configuration
- `Gemfile` - Ruby dependencies
- `package.json` - Node.js scripts (optional)

### Data
- `_data/navigation.yml` - Site navigation structure
- `_data/publications.yml` - Publications database

### Styling
- `assets/css/main.scss` - Main stylesheet with CSS variables
- Modern design system with ocean-inspired palette

### Layouts
- `_layouts/default.html` - Base layout with header/footer
- `_layouts/page.html` - Standard page layout

## 🎨 Design System

### Colors
```scss
:root {
  --ocean-blue: #0284c7;
  --ocean-teal: #0891b2;
  --ocean-deep: #164e63;
  --ocean-light: #67e8f9;
}
```

### Typography
- **Primary Font**: Inter (modern sans-serif)
- **Monospace**: JetBrains Mono
- **Headings**: Minimal, lowercase h1 with underline
- **Responsive**: Uses clamp() for fluid typography

### Layout
- **Container**: Max-width 1280px, responsive padding
- **Cards**: Consistent shadow system and hover effects
- **Grid**: CSS Grid for responsive layouts

## 🔧 Development Workflow

### 1. Direct GitHub Editing
The recommended workflow for this site is direct editing on GitHub:

1. Navigate to the file you want to edit on GitHub
2. Click the pencil icon to edit
3. Make your changes
4. Commit directly to the `main` branch
5. GitHub Pages will automatically rebuild and deploy

### 2. Local Development (Optional)
If you prefer local development:

```bash
git clone [repository]
cd IMEDEA-AP-LAB.github.io
bundle install
bundle exec jekyll serve
```

### 3. CSS Organization
The CSS is now fully modularized in `assets/css/scss/`:
- `base/` - Variables, mixins, reset, typography
- `components/` - Reusable components (cards, buttons, navigation)
- `layout/` - Layout containers and utilities  
- `pages/` - Page-specific styles
- `utilities/` - Overrides and utility classes

Edit the appropriate SCSS partial for your changes.

## 📝 Content Guidelines

### Publications
- Always add to `_data/publications.yml` first
- Use consistent author format: "Last, First"
- Include DOI when available
- Write clear, concise abstracts

### Projects
- Use descriptive slugs (URL-friendly names)
- Add hero images (recommended: 1200x600px)
- Include team members and funding info
- Link to related publications

### Images
- **Team photos**: 400x400px, square crop
- **Gallery images**: Optimize with `make optimize`
- **Project images**: 1200x600px for hero images
- Always include alt text

### Writing Style
- Clear, concise language
- Use active voice
- Include relevant keywords for SEO
- Break up long text with headings and lists

## 🚀 Performance

### Image Optimization
```bash
make optimize  # Compress and create thumbnails
```

### CSS
- Critical CSS is inlined
- Fonts are preloaded
- Uses CSS custom properties for theming

### Jekyll Optimization
- Incremental builds enabled in development
- Asset compression in production
- Sitemap and feed generation

## 🔍 SEO & Analytics

### Built-in Features
- Semantic HTML structure
- Open Graph meta tags
- JSON-LD structured data
- XML sitemap generation
- RSS feed

### Google Analytics
Add to `_config.yml`:
```yaml
google_analytics: UA-XXXXXXXX-X
```

## 🎯 Advanced Features

### Dynamic Publications
The homepage automatically shows recent publications from the data file using:
```liquid
{% include recent-publications.html %}
```

### Responsive Navigation
Mobile-first design with flexbox navigation that works without JavaScript.

### Interactive Elements
- Hover effects on cards and links
- Smooth scrolling and transitions
- Focus states for accessibility

## 🧪 Testing

### Local Testing
```bash
make test  # Jekyll strict mode
make serve # Visual testing
```

### Browser Testing
- Test in multiple browsers
- Verify mobile responsiveness
- Check loading performance

### Content Validation
- Verify all links work
- Check image optimization
- Validate HTML/CSS

## 🚀 Deployment

### Automatic Deployment
- Push to `main` branch triggers GitHub Pages build
- Usually deploys within 1-5 minutes
- Check Actions tab for build status

### Manual Deployment
```bash
make deploy  # Builds and pushes changes
```

### Rollback
If issues occur:
```bash
git revert [commit-hash]
git push origin main
```

## 🔧 Troubleshooting

### Common Issues

**Build Failures:**
- Check `_config.yml` syntax
- Verify front matter formatting
- Look for liquid syntax errors

**Styling Issues:**
- Clear browser cache
- Check CSS variable definitions
- Verify SCSS compilation

**Content Issues:**
- Validate YAML front matter
- Check file paths and naming
- Ensure proper encoding (UTF-8)

### Debug Mode
```bash
JEKYLL_ENV=development bundle exec jekyll serve --verbose
```

## 📚 Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Guide](https://docs.github.com/en/pages)
- [Liquid Documentation](https://shopify.github.io/liquid/)
- [SCSS Documentation](https://sass-lang.com/documentation)
