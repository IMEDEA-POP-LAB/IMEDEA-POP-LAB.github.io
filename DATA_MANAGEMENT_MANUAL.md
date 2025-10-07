# Data Management Manual

## Overview

This manual provides comprehensive instructions for managing the data files that power the IMEDEA Physical Ocean Processes Lab website. All data is stored in YAML format in the `_data/` directory and is automatically integrated into the website pages.

## Table of Contents

1. [Quick Reference](#quick-reference)
2. [People Management (`people.yml`)](#people-management-peopleyml)
3. [Project Management (`projects.yml`)](#project-management-projectsyml)
4. [Publications Management (`publications.yml`)](#publications-management-publicationsyml)
5. [Media Coverage (`media.yml`)](#media-coverage-mediayml)
6. [Outreach Content (`outreach.yml`)](#outreach-content-outreachyml)
7. [Repository Management (`repositories.yml`)](#repository-management-repositoriesyml)
8. [Navigation (`navigation.yml`)](#navigation-navigationyml)
9. [YAML Formatting Guidelines](#yaml-formatting-guidelines)
10. [Common Troubleshooting](#common-troubleshooting)

## Quick Reference

### Data Files Location
All data files are located in: `_data/`

### File Structure
```
_data/
├── people.yml         # Team members and their information
├── projects.yml       # Current research projects
├── publications.yml   # Academic publications
├── media.yml          # Press coverage and media mentions
├── outreach.yml       # Videos, documentaries, interviews
├── repositories.yml   # GitHub repositories (auto-updated)
└── navigation.yml     # Website navigation menu
```

### Images Location
- Team photos: `assets/img/team/`
- Project logos: `assets/img/projects/`
- Gallery images: `assets/img/gallery/`

---

## People Management (`people.yml`)

### Structure Overview
The people file is organized into four categories:
- `principal_investigators`
- `research_scientists`
- `postdocs`
- `students`

### Adding a New Team Member

1. **Choose the appropriate category** based on their position
2. **Add the new entry** following this template:

```yaml
- name: "Dr. [First] [Last]"
  title: "[Position Title]"
  period: "[Start Year] - [present/End Year]"
  image: "[filename.jpg]"
  email: "[email@domain.com]"
  orcid: "[ORCID URL]" # Optional
  scholar: "[Google Scholar URL]" # Optional
  website: "[Personal website URL]" # Optional
  imedea: "[IMEDEA profile URL]" # Optional - link to IMEDEA institutional profile
  bio: "[Brief biography paragraph]"
```

### Required Fields
- `name`: Full name with title (Dr., Prof., etc.)
- `title`: Academic/professional position
- `period`: Time at the institution
- `image`: Filename of photo in `assets/img/team/`
- `bio`: Short professional biography

### Optional Fields
- `email`: Contact email
- `orcid`: ORCID identifier URL
- `scholar`: Google Scholar profile URL
- `website`: Personal or academic website

### Example Entry
```yaml
postdocs:
  - name: "Dr. Maria Rodriguez"
    title: "Postdoctoral Researcher"
    period: "2024 - present"
    image: "maria_rodriguez.jpg"
    email: "maria.rodriguez@imedea.uib-csic.es"
    orcid: "https://orcid.org/0000-0000-0000-0000"
    scholar: "https://scholar.google.com/citations?user=XXXXXXX"
    bio: "Specializes in ocean modeling and data assimilation with focus on Mediterranean Sea dynamics."
```

### Image Guidelines
- **Format**: JPG or PNG
- **Size**: Recommended 400x400 pixels
- **Location**: Save in `assets/img/team/`
- **Naming**: Use format `firstname_lastname.jpg` (lowercase, underscore-separated)

---

## Project Management (`projects.yml`)

### Adding a New Project

Use this template for new projects:

```yaml
- title: "[Project Title]"
  period: "[Start Year]-[End Year]"
  logo: "[logo_filename.png]"
  url: "[project_website_url]" # Leave empty "" if no website
  description: "[Brief project description]"
  featured: true # or false
```

### Required Fields
- `title`: Full project name
- `period`: Project duration (e.g., "2024-2027")
- `logo`: Logo filename in `assets/img/projects/`
- `url`: Project website (use empty quotes "" if none)
- `description`: Brief description of the project
- `featured`: Boolean (true/false) - determines if shown prominently

### Example Entry
```yaml
- title: "Mediterranean Ocean Dynamics"
  period: "2024-2026"
  logo: "med_dynamics_logo.png"
  url: "https://example-project.com"
  description: "Investigating mesoscale processes in the Mediterranean Sea using satellite altimetry"
  featured: true
```

### Logo Guidelines
- **Format**: PNG preferred, SVG also supported
- **Size**: Recommended 200x100 pixels
- **Location**: Save in `assets/img/projects/`
- **Background**: Transparent preferred

---

## Publications Management (`publications.yml`)

### Structure Overview
The publications file has three sections:
- `recent`: Latest publications (displayed prominently)
- `preprints`: Accepted papers not yet published
- `all`: Complete publication list

### Adding a New Publication

#### For Recent Publications
Add to the `recent` section:

```yaml
recent:
  - title: "[Paper Title]"
    authors: "[Author1], [Author2], and [LastAuthor]"
    journal: "[Journal Name]"
    year: [YYYY]
    doi: "[DOI URL]"
```

#### For Preprints/Accepted Papers
Add to the `preprints` section:

```yaml
preprints:
  - title: "[Paper Title]"
    authors: "[Author List]"
    journal: "[Target Journal]"
    year: [YYYY]
    status: "accepted" # or "under review", "in press"
    doi: "[DOI URL if available]"
```

#### For Complete List
Add to the `all` section with same format as recent publications.

### Required Fields
- `title`: Full paper title
- `authors`: Complete author list
- `journal`: Journal or publication venue
- `year`: Publication year
- `doi`: DOI link (full URL)

### Author Formatting Guidelines
- Use full names as they appear in publication
- Separate multiple authors with commas
- Use "and" before the last author
- For many authors, consider truncating with "et al." after 3-5 names

### Example Entry
```yaml
- title: "Mesoscale Eddies in the Western Mediterranean: A Satellite Altimetry Study"
  authors: "Pascual, A., Barceló-Llull, B., Mourre, B., and Combes, V."
  journal: "Journal of Geophysical Research: Oceans"
  year: 2024
  doi: "https://doi.org/10.1029/2024JC020123"
```

---

## Media Coverage (`media.yml`)

### Adding Media Coverage

Use this template for new media mentions:

```yaml
- date: [YYYY-MM-DD]
  title: "[Article/Coverage Title]"
  outlet: "[Media Outlet Name]"
  url: "[Article URL]"
  excerpt: "[Brief excerpt or summary]"
  language: "[en/es/ca]"
  type: "[press/interview/feature]"
```

### Required Fields
- `date`: Publication date (YYYY-MM-DD format)
- `title`: Article or coverage title
- `outlet`: Name of media outlet
- `url`: Link to article
- `excerpt`: Brief description or key quote
- `language`: Language code (en, es, ca)
- `type`: Type of coverage (press, interview, feature)

### Example Entry
```yaml
- date: 2024-10-15
  title: "Scientists Track Ocean Currents with New Satellite Technology"
  outlet: "Science Daily"
  url: "https://www.sciencedaily.com/example-article"
  excerpt: "Researchers develop innovative methods for monitoring Mediterranean Sea dynamics"
  language: "en"
  type: "press"
```

### Ordering
- **Add new entries at the top** for reverse chronological order
- The website displays items with newest first

---

## Outreach Content (`outreach.yml`)

### Adding Outreach Content

Use this template for videos, documentaries, and interviews:

```yaml
- date: [YYYY-MM-DD]
  title: "[Content Title]"
  type: "[documentary/interview/presentation]"
  venue: "[Platform or Event Name]"
  youtube_id: "[YouTube Video ID]" # Extract from YouTube URL
  description: "[Brief description]"
  language: "[en/es/ca]"
  featured: true # or false
```

### Required Fields
- `date`: Content publication date
- `title`: Title of the content
- `type`: Type (documentary, interview, presentation, etc.)
- `venue`: Platform, channel, or event name
- `youtube_id`: YouTube video ID (from URL)
- `description`: Brief description of content
- `language`: Language code
- `featured`: Boolean for prominence on website

### YouTube ID Extraction
From URL: `https://www.youtube.com/watch?v=WQd9LeIdLSk`
Extract ID: `WQd9LeIdLSk`

### Example Entry
```yaml
- date: 2024-10-01
  title: "Ocean Research in the Mediterranean"
  type: "documentary"
  venue: "IMEDEA Productions"
  youtube_id: "abc123xyz789"
  description: "Documentary showcasing current oceanographic research methods"
  language: "en"
  featured: true
```

---

## Repository Management (`repositories.yml`)

### Important Note
⚠️ **This file is automatically updated by GitHub Actions**. Do not edit manually unless absolutely necessary.

### Manual Updates (if needed)
If you must manually add a repository:

```yaml
repositories:
  - name: "[Repository Name]"
    full_name: "[Organization]/[Repository Name]"
    description: "[Repository description]"
    html_url: "[GitHub repository URL]"
    homepage: "[Project website URL]" # Optional
    language: "[Primary programming language]"
    stargazers_count: [number]
    forks_count: [number]
    license:
      name: "[License name]"
      spdx_id: "[License ID]"
    topics: ["topic1", "topic2", "topic3"]
    created_at: "[ISO date]"
    updated_at: "[ISO date]"
    archived: false
    featured: true # or false
    category: "[Educational/Research/Tool]"
```

---

## Navigation (`navigation.yml`)

### Modifying Navigation Menu

The navigation file controls the main menu structure:

```yaml
- name: [Display Name]
  link: [URL path]
```

### Adding a New Page
1. Add entry to navigation.yml
2. Create corresponding page in `_pages/` directory

### Example
```yaml
- name: Resources
  link: /resources/
```

---

## YAML Formatting Guidelines

### Basic Rules
1. **Indentation**: Use 2 spaces (never tabs)
2. **Quotes**: Use double quotes for strings with special characters
3. **Lists**: Use `-` for list items
4. **Booleans**: Use `true` or `false` (lowercase)
5. **Empty values**: Use `""` for empty strings

### String Formatting
```yaml
# Good
title: "Ocean Dynamics in the Mediterranean"
description: "Multi-year study of mesoscale processes"

# Avoid special characters without quotes
title: Ocean Dynamics: A Study  # May cause errors
```

### Date Formatting
Always use ISO format: `YYYY-MM-DD`
```yaml
date: 2024-10-02  # Good
date: 10/02/2024  # Bad
```

### URL Formatting
Always include full URLs with protocol:
```yaml
url: "https://example.com"     # Good
url: "example.com"             # Bad
doi: "https://doi.org/10.1000/xyz"  # Good
```

---

## Common Troubleshooting

### Website Not Building
1. **Check YAML syntax**: Use a YAML validator
2. **Verify indentation**: Ensure consistent 2-space indentation
3. **Check for special characters**: Wrap in quotes if needed
4. **Validate required fields**: Ensure all required fields are present

### Images Not Displaying
1. **Check file path**: Verify image exists in correct directory
2. **Check filename**: Ensure exact match including case
3. **File format**: Use JPG, PNG, or SVG formats
4. **File size**: Keep under 1MB for optimal loading

### Content Not Appearing
1. **Check data structure**: Verify correct YAML structure
2. **Category placement**: Ensure item is in correct section
3. **Required fields**: Verify all required fields are present
4. **Boolean values**: Use `true`/`false`, not `yes`/`no`

### Character Encoding Issues
- Save all files in UTF-8 encoding
- Use YAML-safe characters or escape special characters
- For non-English text, always use quotes

### Testing Changes
1. **Local testing**: Use Jekyll locally to test changes
2. **GitHub Actions**: Check build status in repository
3. **Staging**: Use a separate branch for testing major changes

---

## Best Practices

### File Organization
- **Consistent naming**: Use clear, descriptive filenames
- **Regular updates**: Keep information current
- **Backup**: Commit changes regularly to version control

### Content Guidelines
- **Accuracy**: Verify all information before adding
- **Completeness**: Fill all required fields
- **Consistency**: Use consistent formatting across entries
- **Professional tone**: Maintain academic/professional language

### Maintenance Schedule
- **Monthly**: Review and update team information
- **Quarterly**: Update project statuses and publications
- **Annually**: Archive completed projects and update photos

---

## Getting Help

### Resources
- **YAML Validator**: [yamllint.com](https://yamllint.com)
- **Jekyll Documentation**: [jekyllrb.com](https://jekyllrb.com)
- **GitHub Markdown Guide**: [GitHub Guides](https://guides.github.com)

### Contact
For technical issues or questions about data management, contact [Cristina](mailto:cmarti@imedea.uib-csic.es) or [Joan](mailto:joanarmajach@imedea.uib-csic.es) or create an issue in the GitHub repository.

---

*Last updated: October 2025*
*Version: 1.0*