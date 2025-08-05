# 🌊 Physical Ocean Processes - Ananda Pascual Lab

**Research group website for the Physical Ocean Processes Lab at IMEDEA (Mediterranean Institute for Advanced Studies)**

This website showcases our research on ocean dynamics, satellite oceanography, and marine processes in the Mediterranean Sea and beyond.

🌐 **Live Site**: [https://imedea-ap-lab.github.io](https://imedea-ap-lab.github.io)

## � How to Update the Website

### Easy Updates via GitHub 

1. **Go to the file you want to edit** on GitHub
2. **Click the pencil icon (✏️)** to edit
3. **Make your changes** using simple markdown
4. **Add a commit message** describing what you changed
5. **Click "Commit changes"**
6. **Wait 2-5 minutes** - your changes will appear on the website!

### Page Templates for Common Updates
#### 👥 Adding a New Team Member
Edit `_pages/people.md` and add:

```markdown
<div class="person-card">
  <div class="card-body">
    <img src="/assets/img/team/yourname.jpg" alt="Your Name" class="profile-image">
    <h5 class="card-title">Dr. Your Name</h5>
    <p class="card-subtitle">Your Position</p>
    <div class="social-links">
      <a href="mailto:your.email@example.com" class="social-link">
        <i class="fas fa-envelope"></i>
      </a>
    </div>
    <p class="card-text">Brief description of your research interests.</p>
  </div>
</div>
```

#### � Adding a New Publication
Edit `_pages/publications.md` and add to the **Recent Publications** section:

```markdown
<div class="publication-item featured">
  <div class="publication-header">
    <h4 class="publication-title">Your Paper Title</h4>
    <div class="publication-meta">
      <span class="journal">Journal Name</span>
      <span class="year">2025</span>
    </div>
  </div>
  <div class="publication-authors">Author 1, Author 2, Author 3</div>
  <div class="publication-links">
    <a href="https://doi.org/your-doi" class="link-doi">DOI</a>
  </div>
</div>
```

#### 🔬 Adding a New Project
Edit `_pages/projects.md` and add:

```markdown
<div class="project-card">
  <h4>Project Title</h4>
  <p class="project-description">Brief description of what this project is about and its main goals.</p>
  <div class="project-links">
    <a href="project-website-url" class="btn btn-primary">Learn More</a>
  </div>
</div>
```

#### 📰 Adding News/Updates
Edit `_pages/about.md` to add news items to the homepage.

## 📂 File Locations

- **Homepage**: `_pages/about.md`
- **Team page**: `_pages/people.md`
- **Publications**: `_pages/publications.md`
- **Projects**: `_pages/projects.md`
- **Team photos**: Upload to `assets/img/team/`

## 🆘 Need Help?

- **Can't find a file?** Use GitHub's search box at the top of the repository
- **Broke something?** Check the [commit history] and revert changes if needed
- **Images not showing?** Make sure you uploaded them to the correct folder in `assets/img/`

---

*For technical documentation and advanced development, see the full documentation in the `templates/` folder.*
