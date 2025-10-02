# Repository Page Automation Setup

The repository page has been automated to pull data directly from your GitHub organization. Here's what's been implemented:

## 🎯 What It Does

- **Automatically fetches** all public repositories from IMEDEA-AP-LAB organization
- **Categorizes repositories** based on content (Educational, Ocean Science, Tools, etc.)
- **Highlights featured repositories** based on activity and importance
- **Updates daily** via GitHub Actions
- **Provides manual update option** for immediate updates

## 📁 Files Created

### Data & Configuration
- `_data/repositories.yml` - Repository data (auto-updated)
- `_pages/repositories.md` - Updated page template with dynamic content

### Automation Scripts  
- `.github/workflows/update-repositories.yml` - Daily update workflow
- `.github/scripts/update_repositories.py` - Main automation script
- `scripts/update_repositories.sh` - Manual update script

### Styling
- `_sass/pages/_repositories.scss` - Updated with your color scheme

## 🚀 Features Added

### Visual Features
- **Statistics overview** - Shows total repos, featured count, languages
- **Featured repository section** - Highlights your most important project
- **Category filtering** - Filter by Educational, Ocean Science, Tools, etc.
- **GitHub-style cards** - Clean repository display with stats
- **Topic tags** - Shows repository topics as badges
- **Direct links** - Quick access to code and documentation

### Automatic Categorization
Repositories are automatically sorted into:
- **Educational** - Tutorials, courses, workshops
- **Ocean Science** - Oceanography, altimetry, modeling
- **Data & Analysis** - Jupyter notebooks, analysis tools  
- **Tools & Applications** - Web apps, utilities
- **Documentation** - Websites, documentation

### Featured Repository Logic
Repositories are marked as "featured" if they:
- Have 5+ stars
- Are educational content (tutorials, courses)
- Have recent significant activity (last 3 months)

## 🔄 How It Updates

### Automatic (Recommended)
- Runs **daily at 6:00 AM UTC**
- Updates `_data/repositories.yml` automatically
- Commits changes to your repository
- No manual work required!

### Manual Updates
For immediate updates or testing:

```bash
# Run the manual script
./scripts/update_repositories.sh YOUR_GITHUB_TOKEN
```

## 📊 Current Status

The system is now live with:
- ✅ 2 repositories detected and categorized
- ✅ 1 featured repository (MASS24_Altimetry_tutorial)
- ✅ Automatic daily updates scheduled
- ✅ Manual update capability
- ✅ Full integration with your color scheme

## 🛠 Customization

### Add Custom Repository Data
If you want to customize any repository's information, you can edit `_data/repositories.yml` manually. The automation script will preserve your custom fields.

### Modify Categories
Edit the `categorize_repo()` function in `.github/scripts/update_repositories.py` to adjust how repositories are categorized.

### Change Featured Logic
Modify the `is_featured_repo()` function to change which repositories are highlighted.

## 🔧 Configuration

The system uses these environment variables:
- `GITHUB_TOKEN` - For API access (required)
- `GITHUB_ORG` - Organization name (defaults to IMEDEA-AP-LAB)

## 📈 Benefits

1. **Always up-to-date** - No manual maintenance required
2. **Professional appearance** - GitHub-style repository cards
3. **Easy discovery** - Categories and featured sections help visitors find relevant code
4. **SEO friendly** - Proper metadata and descriptions
5. **Mobile responsive** - Works perfectly on all devices

The repository page is now a dynamic showcase of your research group's open-source contributions that maintains itself automatically!