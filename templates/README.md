# 📝 Content Templates

This directory contains templates for creating new content on the IMEDEA-AP Lab website.

## 🚀 Quick Usage

Instead of manually copying these templates, use our automated scripts:

```bash
# Create a new project
./scripts/new-content.sh project project-name

# Create a news item  
./scripts/new-content.sh news news-title

# Add a publication
./scripts/new-content.sh publication "Publication Title"
```

## 📋 Available Templates

- `project_template.md` - Template for new research projects
- `person_template.md` - Template for adding team members

## 💡 Tips

- Use descriptive, URL-friendly names (lowercase, hyphens instead of spaces)
- Always add appropriate images to the `assets/img/` directory
- Update the `_data/navigation.yml` if adding new main pages
- Test locally with `./scripts/serve.sh` before deploying

## Available Templates

- `project_template.md` - Template for new research projects
- `person_template.md` - Template for adding new team members

---

*For more detailed instructions, see the main README.md file*
