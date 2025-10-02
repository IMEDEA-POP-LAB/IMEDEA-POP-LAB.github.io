#!/usr/bin/env python3
"""
Script to automatically update repository data from GitHub API
"""

import requests
import yaml
import os
from datetime import datetime

def get_github_repos(org_name, token):
    """Fetch repositories from GitHub API"""
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    url = f'https://api.github.com/orgs/{org_name}/repos'
    params = {
        'type': 'public',
        'sort': 'updated',
        'per_page': 100
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        repos = response.json()
        
        # Filter out forks and archived repos, unless they're specifically marked as important
        filtered_repos = []
        for repo in repos:
            if not repo['fork'] and not repo['archived']:
                filtered_repos.append(repo)
        
        return filtered_repos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []

def categorize_repo(repo):
    """Categorize repository based on name, description, and topics"""
    name = repo['name'].lower()
    description = (repo['description'] or '').lower()
    topics = [topic.lower() for topic in repo.get('topics', [])]
    
    # Educational/Tutorial repositories
    if any(keyword in name + description for keyword in ['tutorial', 'course', 'lesson', 'education', 'teaching', 'workshop']):
        return 'Educational'
    
    # Data processing/Analysis tools
    if any(keyword in topics + [name] for keyword in ['data-processing', 'analysis', 'jupyter', 'python', 'r']):
        return 'Data & Analysis'
    
    # Ocean modeling and simulation
    if any(keyword in topics + [name, description] for keyword in ['ocean', 'model', 'simulation', 'altimetry', 'oceanography']):
        return 'Ocean Science'
    
    # Web applications and tools
    if any(keyword in topics + [name] for keyword in ['web', 'app', 'tool', 'dashboard', 'visualization']):
        return 'Tools & Applications'
    
    # Documentation and websites
    if any(keyword in name for keyword in ['docs', 'website', '.github.io', 'documentation']):
        return 'Documentation'
    
    return 'General'

def is_featured_repo(repo):
    """Determine if a repository should be featured"""
    # Feature repositories with high activity, recent updates, or specific topics
    topics = repo.get('topics', [])
    
    # High star count or recent activity
    if repo['stargazers_count'] >= 5:
        return True
    
    # Educational content is often featured
    if any(topic in topics for topic in ['tutorial', 'education', 'course']):
        return True
    
    # Recent significant updates (within last 3 months)
    from datetime import datetime, timedelta
    updated = datetime.strptime(repo['updated_at'], '%Y-%m-%dT%H:%M:%SZ')
    if datetime.now() - updated < timedelta(days=90) and repo['size'] > 100:  # Non-trivial size
        return True
    
    return False

def format_repo_data(repo):
    """Format repository data for Jekyll"""
    return {
        'name': repo['name'],
        'full_name': repo['full_name'],
        'description': repo['description'] or f"Repository: {repo['name']}",
        'html_url': repo['html_url'],
        'homepage': repo['homepage'] if repo['homepage'] else None,
        'language': repo['language'],
        'stargazers_count': repo['stargazers_count'],
        'forks_count': repo['forks_count'],
        'license': {
            'name': repo['license']['name'] if repo['license'] else None,
            'spdx_id': repo['license']['spdx_id'] if repo['license'] else None
        } if repo['license'] else None,
        'topics': repo.get('topics', []),
        'created_at': repo['created_at'],
        'updated_at': repo['updated_at'],
        'archived': repo['archived'],
        'featured': is_featured_repo(repo),
        'category': categorize_repo(repo)
    }

def main():
    """Main function to update repositories data"""
    token = os.environ.get('GITHUB_TOKEN')
    org_name = os.environ.get('GITHUB_ORG', 'IMEDEA-AP-LAB')
    
    if not token:
        print("GITHUB_TOKEN environment variable is required")
        return
    
    print(f"Fetching repositories for organization: {org_name}")
    repos = get_github_repos(org_name, token)
    
    if not repos:
        print("No repositories found or error occurred")
        return
    
    # Format data for Jekyll
    formatted_repos = [format_repo_data(repo) for repo in repos]
    
    # Sort repositories: featured first, then by stars, then by update date
    formatted_repos.sort(key=lambda x: (
        not x['featured'],  # Featured first (False sorts before True)
        -x['stargazers_count'],  # Then by stars (descending)
        x['updated_at']  # Then by update date (ascending - most recent last)
    ), reverse=True)
    
    # Create YAML structure
    data = {
        'repositories': formatted_repos,
        'last_updated': datetime.now().isoformat(),
        'total_count': len(formatted_repos)
    }
    
    # Write to file
    output_file = '_data/repositories.yml'
    
    # Add header comment
    yaml_content = f"""# GitHub repositories data
# Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
# Auto-generated by GitHub Actions - Do not edit manually
# Total repositories: {len(formatted_repos)}

"""
    
    with open(output_file, 'w') as f:
        f.write(yaml_content)
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    
    print(f"Updated {output_file} with {len(formatted_repos)} repositories")
    
    # Print summary
    categories = {}
    featured_count = 0
    for repo in formatted_repos:
        category = repo['category']
        categories[category] = categories.get(category, 0) + 1
        if repo['featured']:
            featured_count += 1
    
    print(f"Summary:")
    print(f"  Total repositories: {len(formatted_repos)}")
    print(f"  Featured repositories: {featured_count}")
    print(f"  Categories: {dict(categories)}")

if __name__ == '__main__':
    main()