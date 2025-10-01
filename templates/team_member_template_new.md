# 👥 TEAM MEMBER TEMPLATE

> **NEW EASY METHOD**: Just edit the `_data/team.yml` file instead of HTML!

## 🚀 QUICK ADD (Recommended)

### Step 1: Upload Photo
- Save photo as `assets/img/team/lastname_firstname.jpg`
- Recommended size: 400x400px (square)
- Use professional headshot

### Step 2: Add to Data File
Open `_data/team.yml` and add to the appropriate section:

#### For Principal Investigators:
```yaml
principal_investigators:
  - name: "Dr. [Full Name]"
    title: "[Position Title]"
    period: "YYYY - present"
    image: "lastname_firstname.jpg"
    email: "email@imedea.uib-csic.es"
    orcid: "https://orcid.org/0000-0000-0000-0000"
    scholar: "https://scholar.google.com/citations?user=..."
    website: "https://personal-website.com"
    bio: "Brief 2-3 sentence biography describing background and research focus."
    research_interests:
      - "Research area 1"
      - "Research area 2"
      - "Research area 3"
```

#### For Postdocs:
```yaml
postdocs:
  - name: "Dr. [Full Name]"
    title: "Postdoctoral Researcher"
    period: "YYYY - present"
    image: "lastname_firstname.jpg"
    email: "email@imedea.uib-csic.es"
    orcid: "https://orcid.org/0000-0000-0000-0000"
    scholar: ""
    website: ""
    bio: "Brief description of research focus and background."
    research_interests:
      - "Specific research area"
      - "Another research focus"
```

#### For PhD Students:
```yaml
phd_students:
  - name: "[Full Name]"
    title: "PhD Student"
    period: "YYYY - present"
    image: "lastname_firstname.jpg"
    email: "email@imedea.uib-csic.es"
    orcid: ""
    scholar: ""
    website: ""
    bio: "Brief description of PhD research topic."
    research_interests:
      - "PhD research focus"
      - "Related interest"
```

#### For Visiting Researchers:
```yaml
visiting_researchers:
  - name: "Dr. [Full Name]"
    title: "Visiting Researcher"
    period: "YYYY - YYYY"
    image: "lastname_firstname.jpg"
    email: "email@home-institution.edu"
    orcid: ""
    scholar: ""
    website: ""
    bio: "Brief description and home institution."
    research_interests:
      - "Collaboration focus"
```

#### For Alumni:
```yaml
alumni:
  - name: "Dr. [Full Name]"
    title: "Former [Position]"
    period: "YYYY - YYYY"
    current_position: "Current Title at Current Institution"
    email: "current.email@institution.edu"
```

## 📝 FIELD EXPLANATIONS

- **name**: Full name with title (Dr., Prof., etc.)
- **title**: Current position/role in the lab
- **period**: Time period in the lab (use "present" for current)
- **image**: Filename of photo in `assets/img/team/`
- **email**: Contact email (preferably institutional)
- **orcid**: Full ORCID URL (leave empty if none)
- **scholar**: Google Scholar profile URL (leave empty if none)
- **website**: Personal/professional website (leave empty if none)
- **bio**: 2-3 sentence biography
- **research_interests**: List of 2-4 main research areas
- **current_position**: For alumni only - where they are now

## 📋 CHECKLIST

- [ ] Photo uploaded to correct folder
- [ ] Photo is 400x400px and professional
- [ ] All required fields filled
- [ ] Email is correct and active
- [ ] ORCID and Scholar URLs tested
- [ ] Bio is concise and informative
- [ ] Research interests are specific
- [ ] YAML syntax is correct (check indentation)

## 🎯 QUICK EXAMPLES

### Research Scientist
```yaml
research_scientists:
  - name: "Dr. Jane Smith"
    title: "Research Scientist"
    period: "2024 - present"
    image: "smith_jane.jpg"
    email: "jsmith@imedea.uib-csic.es"
    orcid: "https://orcid.org/0000-0000-0000-0000"
    scholar: "https://scholar.google.com/citations?user=abc123"
    website: "https://janesmith.com"
    bio: "Marine biologist specializing in plankton ecology. PhD from University of Barcelona, with expertise in microscopy and molecular techniques."
    research_interests:
      - "Plankton ecology"
      - "Marine biodiversity"
      - "Microscopy techniques"
```

### Master's Student
```yaml
master_students:
  - name: "Maria García"
    title: "Master's Student"
    period: "2024 - present"
    image: "garcia_maria.jpg"
    email: "mgarcia@imedea.uib-csic.es"
    orcid: ""
    scholar: ""
    website: ""
    bio: "Master's student in Marine Sciences working on microplastic impacts on marine organisms."
    research_interests:
      - "Marine pollution"
      - "Microplastics"
```

## 🚨 COMMON MISTAKES

- **Wrong image path**: Make sure filename matches exactly
- **Broken indentation**: YAML is sensitive to spaces
- **Missing quotes**: Always quote text values
- **Wrong section**: Put people in the right category
- **Outdated info**: Keep email and links current

## 💡 PRO TIPS

- Use consistent photo style across team
- Keep bios updated as research evolves
- Add new publications to individual Scholar profiles
- Update alumni section when people leave
- Consider adding Twitter/LinkedIn for social media presence