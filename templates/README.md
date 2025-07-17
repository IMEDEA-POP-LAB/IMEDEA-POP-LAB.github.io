# 📝 Content Templates

This directory contains templates for creating new content on the IMEDEA-AP Lab website.

## 🚀 Quick Usage (GitHub Web Interface)

1. **Navigate to the appropriate directory** on GitHub
2. **Click "Add file" → "Create new file"**
3. **Copy the relevant template** from this directory
4. **Customize the content** for your needs
5. **Commit the changes** directly to the main branch

## 📋 Available Templates

### `project_template.md`
Template for adding new research projects to the projects page.

**Usage:**
- Copy the template content
- Replace placeholder text with your project details
- Add project images to `assets/img/projects/`
- The project will automatically appear on the projects page

### `person_template.md`  
Template for adding new team members to the people page.

**Usage:**
- Copy the template content
- Add to the appropriate section in `_pages/people.md`
- Add team photos to `assets/img/team/`
- Use 400x400px square images for best results

## 💡 Quick Editing Tips

### Adding Publications
Edit `_data/publications.yml` directly:
```yaml
- title: "Your Publication Title"
  authors: "Last, First; Other, Author"
  journal: "Journal Name"
  year: 2024
  doi: "10.1000/example"
  abstract: "Brief description..."
```

### Adding News/Updates
Edit `_pages/outreach.md` and add to the news section:
```markdown
| 2024-01-15 | Your news update here |
```

### Updating Team Information
Edit `_pages/people.md` and modify the existing team member cards or add new ones using the person template.

## 🎨 Image Guidelines

- **Team photos**: 400x400px, square crop, upload to `assets/img/team/`
- **Project images**: 1200x600px recommended, upload to `assets/img/projects/`
- **Gallery images**: Various sizes OK, upload to `assets/img/gallery/`

## 📝 Content Tips

- Use descriptive, URL-friendly names (lowercase, hyphens instead of spaces)
- Always include alt text for images for accessibility
- Keep descriptions concise but informative
- Test changes by viewing the live site after committing

---

*The website automatically rebuilds when you commit changes to GitHub. Changes typically appear within 1-5 minutes.*
