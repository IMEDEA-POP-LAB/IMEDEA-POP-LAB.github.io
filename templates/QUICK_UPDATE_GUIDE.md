# 📝 Quick Update Guide

## Common Website Updates

### 📰 Adding News/Updates
**File:** `_pages/outreach.md`
**Location:** Find the "News" section
**Format:**
```markdown
| 2024-01-15 | Your news update here |
```

### 📚 Adding Publications
**File:** `_data/publications.yml`
**Format:**
```yaml
- title: "Your Publication Title"
  authors: "Last, First; Other, Author"
  journal: "Journal Name"
  year: 2024
  doi: "10.1000/example"
  abstract: "Brief description of the work..."
  featured: true  # Optional: shows on homepage
```

### 👥 Adding Team Members
**File:** `_pages/people.md`
**Steps:**
1. Copy template from `templates/person_template.md`
2. Add team photo to `assets/img/team/` (400x400px recommended)
3. Paste template in appropriate section
4. Replace placeholders with real information

### 🔬 Adding Projects
**File:** `_pages/projects.md`
**Steps:**
1. Copy template from `templates/project_template.md`
2. Add project image to `assets/img/projects/` (1200x600px recommended)
3. Paste template in projects section
4. Replace placeholders with project details

### 🖼️ Adding Gallery Images
**File:** `_pages/about.md`
**Location:** Find the "Gallery" section
**Format:**
```markdown
<div class="gallery-item">
  <img src="/assets/img/gallery/your-image.jpg" alt="Description">
  <div class="gallery-caption">Your caption here</div>
</div>
```

### ⚙️ Updating Site Configuration
**File:** `_config.yml`
**Common changes:**
- Site title, description
- Contact information
- Social media links

### 🧭 Updating Navigation
**File:** `_data/navigation.yml`
**Format:**
```yaml
- name: "Page Name"
  url: "/page-url/"
```

## 📁 File Locations Quick Reference

| Content Type | File Location | Image Location |
|--------------|---------------|----------------|
| News/Updates | `_pages/outreach.md` | `assets/img/` |
| Publications | `_data/publications.yml` | N/A |
| Team Members | `_pages/people.md` | `assets/img/team/` |
| Projects | `_pages/projects.md` | `assets/img/projects/` |
| Gallery | `_pages/about.md` | `assets/img/gallery/` |
| Site Config | `_config.yml` | N/A |
| Navigation | `_data/navigation.yml` | N/A |

## 🎨 Image Guidelines

- **Team photos**: 400x400px, square format
- **Project images**: 1200x600px, landscape format
- **Gallery images**: Any size, but optimize for web
- **File formats**: JPG for photos, PNG for graphics
- **Naming**: Use descriptive, lowercase names with hyphens

## 💡 Pro Tips

1. **Preview changes**: The site rebuilds automatically after commits
2. **Test on mobile**: Check how your changes look on different screen sizes
3. **Use consistent formatting**: Follow existing patterns in the files
4. **Keep it simple**: Less is often more for web content
5. **Alt text matters**: Always include descriptive alt text for images

## 🚨 Common Mistakes to Avoid

- Don't forget to upload images before linking to them
- Don't use spaces in file names (use hyphens instead)
- Don't forget to update both the image and the link
- Don't make overly long descriptions (keep it concise)
- Don't commit without testing the format first

---

*Need help? Check the full documentation in README.md or DEVELOPMENT.md*
