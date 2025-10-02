# Repository Automation

This directory contains automation scripts for keeping the repository page up-to-date with the latest information from GitHub.

## Overview

The repository page is automatically updated using:
- **GitHub Actions**: Runs daily to fetch latest repository data
- **Python Script**: Processes GitHub API data and updates Jekyll data files
- **Manual Script**: For local testing and manual updates

## Files

### GitHub Actions Workflow
- `.github/workflows/update-repositories.yml`: GitHub Actions workflow that runs daily
- Automatically commits updates to `_data/repositories.yml`
- Triggered daily at 6:00 AM UTC or manually via workflow dispatch

### Python Update Script
- `.github/scripts/update_repositories.py`: Main script that fetches and processes repository data
- Uses GitHub API to get organization repositories
- Categorizes repositories automatically
- Determines featured repositories based on activity and content
- Generates Jekyll-compatible YAML data

### Manual Update Script
- `scripts/update_repositories.sh`: Shell script for local updates
- Useful for testing changes before deployment
- Requires GitHub token as parameter or environment variable

## Usage

### Automatic Updates (Recommended)
The repositories page is automatically updated daily via GitHub Actions. No manual intervention required.

### Manual Updates
For testing or immediate updates:

```bash
# Method 1: Pass token as argument
./scripts/update_repositories.sh YOUR_GITHUB_TOKEN

# Method 2: Set environment variable
export GITHUB_TOKEN=your_github_token
./scripts/update_repositories.sh
```

## Repository Categorization

Repositories are automatically categorized based on:
- **Educational**: Tutorials, courses, workshops
- **Data & Analysis**: Jupyter notebooks, Python/R analysis tools
- **Ocean Science**: Oceanography, altimetry, modeling tools
- **Tools & Applications**: Web apps, dashboards, utilities
- **Documentation**: Documentation sites, GitHub pages
- **General**: Everything else

## Featured Repository Selection

Repositories are marked as "featured" if they meet any of these criteria:
- High star count (≥5 stars)
- Educational content (tutorials, courses)
- Recent significant activity (last 3 months with substantial content)

## Data Structure

The generated `_data/repositories.yml` includes:
- Repository metadata (name, description, URL)
- GitHub statistics (stars, forks, language)
- Topics and categories
- License information
- Feature status
- Timestamps

## Configuration

### Environment Variables
- `GITHUB_TOKEN`: Required for API access
- `GITHUB_ORG`: Organization name (default: IMEDEA-AP-LAB)

### Customization
To customize categorization or featured selection logic, edit:
- `categorize_repo()` function for custom categories
- `is_featured_repo()` function for featured selection criteria

## Troubleshooting

### Common Issues
1. **Rate Limiting**: GitHub API has rate limits. The workflow uses authenticated requests to increase limits.
2. **Token Permissions**: Ensure the GitHub token has `repo` and `read:org` permissions.
3. **Missing Dependencies**: The workflow automatically installs required Python packages.

### Debugging
- Check workflow logs in GitHub Actions tab
- Test locally using the manual script
- Verify `_data/repositories.yml` format after updates

## Security

- Never commit GitHub tokens to the repository
- Use GitHub Secrets for workflow configuration
- The workflow uses minimal required permissions
- Manual scripts accept tokens as parameters (not hardcoded)