# 🔬 PROJECT TEMPLATE

> **NEW EASY METHOD**: Just edit the `_data/projects.yml` file instead of creating separate pages!

## 🚀 QUICK ADD (Recommended)

### Step 1: Upload Logo/Image
- Save logo as `assets/img/projects/project_name_logo.png`
- Use PNG for logos, JPG for photos
- Any size is fine, but optimize for web

### Step 2: Add to Data File
Open `_data/projects.yml` and add to the appropriate section:

#### For Current Projects:
```yaml
current:
  - title: "Project Full Title"
    period: "YYYY-YYYY"
    logo: "project_name_logo.png"
    url: "https://project-website.com"  # Optional
    description: "Brief 1-2 sentence description of the project"
    funding_agency: "Funding Organization Name"
    pi: "Principal Investigator Name"
    team_members: ["Team Member 1", "Team Member 2"]
    keywords: ["keyword1", "keyword2", "keyword3"]
    featured: true  # Shows prominently if true
```

#### For Completed Projects:
```yaml
completed:
  - title: "Completed Project Title"
    period: "YYYY-YYYY"
    logo: "project_logo.png"
    url: ""
    description: "What the project achieved"
    funding_agency: "Funding Agency"
    pi: "PI Name"
    team_members: ["Former Team Member 1"]
    keywords: ["research area", "technique"]
    featured: false
```

## 📝 FIELD EXPLANATIONS

- **title**: Full project title (use official name)
- **period**: Project duration (YYYY-YYYY format)
- **logo**: Logo filename in `assets/img/projects/`
- **url**: Project website URL (leave empty "" if none)
- **description**: Brief description (1-2 sentences max)
- **funding_agency**: Organization providing funding
- **pi**: Principal Investigator name
- **team_members**: List of lab members involved
- **keywords**: 3-5 relevant keywords for categorization
- **featured**: `true` for important projects (shows prominently)

## 🎯 COMPLETE PROJECT EXAMPLES

### Large Research Project
```yaml
- title: "Mediterranean Marine Heatwave Dynamics"
  period: "2023-2026"
  logo: "marine_heatwave_logo.png"
  url: "https://marineheatwaves-med.org"
  description: "Investigating the increasing frequency and intensity of marine heatwaves in the Mediterranean Sea using satellite data and numerical models."
  funding_agency: "European Research Council"
  pi: "Ananda Pascual"
  team_members: ["Baptiste Mourre", "Vincent Combes", "Jen-Ping Peng"]
  keywords: ["marine heatwaves", "Mediterranean Sea", "satellite altimetry", "climate change"]
  featured: true
```

### Industry Collaboration
```yaml
- title: "COPERNICUS Sea Level Monitoring"
  period: "2024-2028"
  logo: "copernicus_logo.png"
  url: ""
  description: "Operational sea level monitoring and forecasting for the Copernicus Marine Environment Monitoring Service."
  funding_agency: "European Commission - Copernicus"
  pi: "Ananda Pascual"
  team_members: ["Baptiste Mourre"]
  keywords: ["sea level", "altimetry", "operational oceanography", "Copernicus"]
  featured: false
```

### Small/Pilot Project
```yaml
- title: "Glider Data Quality Assessment"
  period: "2024-2025"
  logo: "glider_qa_logo.png"
  url: ""
  description: "Developing automated quality control procedures for underwater glider observations."
  funding_agency: "IMEDEA Internal Funding"
  pi: "Baptiste Mourre"
  team_members: ["Vincent Combes"]
  keywords: ["gliders", "quality control", "data processing"]
  featured: false
```

## 📂 PROJECT CATEGORIES

### Current Projects
- Ongoing research projects
- Active funding
- Regular updates and progress

### Completed Projects
- Finished research
- Historical significance
- Results published or available

## 🎨 LOGO GUIDELINES

### Preferred Formats
- **PNG**: For logos with transparency
- **JPG**: For photos or complex images
- **SVG**: Vector logos (if supported)

### Size Recommendations
- **Width**: 200-400px ideal
- **Aspect ratio**: Square or landscape
- **File size**: < 500KB for fast loading

### Logo Sources
- Official project logos from funding agencies
- Custom logos created for the project
- Institutional logos (with permission)
- Simple text-based logos if no graphics available

## 📋 PROJECT CHECKLIST

- [ ] Logo uploaded to correct folder
- [ ] Project title is official/complete
- [ ] Period dates are accurate
- [ ] Description is concise but informative
- [ ] Funding agency name is correct
- [ ] All team members listed
- [ ] Keywords are relevant and searchable
- [ ] Featured status appropriate
- [ ] Website URL tested (if provided)

## 🔄 UPDATING PROJECTS

### Moving from Current to Completed
1. Cut entry from `current:` section
2. Paste into `completed:` section
3. Update description to past tense
4. Add final outcomes or results

### Adding New Phases
```yaml
- title: "Project Name - Phase 2"
  period: "2025-2027"
  # ... continue with same format
```

## 💡 PRO TIPS

### For Principal Investigators
- Keep project descriptions current
- Update team members as people join/leave
- Feature your most important projects
- Include project websites when available

### For Lab Managers
- Regular review of completed projects
- Consistent logo styling
- Archive old project materials
- Update funding information

### For Website Maintainers
- Monitor project status changes
- Ensure logos display correctly
- Check for broken links
- Balance featured vs. regular projects

## 🚨 COMMON ISSUES

- **Logo not showing**: Check filename and path
- **Formatting broken**: Verify YAML indentation
- **Projects not ordering correctly**: Check `featured` status
- **Long descriptions**: Keep to 1-2 sentences max
- **Outdated information**: Review quarterly