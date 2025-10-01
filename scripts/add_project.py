#!/usr/bin/env python3

"""
Project Addition Script

This script helps quickly add new projects to the website.
It generates the YAML entry for the projects data file.

Usage: python3 add_project.py
"""

import yaml

def get_project_input():
    """Collect project information from user input"""
    print("🔬 IMEDEA Lab Project Addition Tool")
    print("=" * 50)
    
    # Basic information
    title = input("Project title: ").strip()
    start_year = input("Start year (YYYY): ").strip()
    
    is_ongoing = input("Is this project ongoing? (y/n): ").strip().lower() == 'y'
    if is_ongoing:
        period = f"{start_year} - present"
        status = "current"
    else:
        end_year = input("End year (YYYY): ").strip()
        period = f"{start_year} - {end_year}"
        status = "completed"
    
    # Logo and URL
    print("\nLogo filename (will be in assets/img/projects/):")
    logo = input("Logo filename (e.g., project_logo.png): ").strip()
    
    url = input("Project website URL (optional): ").strip()
    
    # Description
    print("\nProject description (1-2 sentences):")
    description = input().strip()
    
    # Funding and team
    funding_agency = input("Funding agency: ").strip()
    pi = input("Principal Investigator: ").strip()
    
    print("Team members (separate by commas):")
    team_input = input().strip()
    team_members = [member.strip() for member in team_input.split(',') if member.strip()]
    
    print("Keywords (separate by commas):")
    keywords_input = input().strip()
    keywords = [keyword.strip() for keyword in keywords_input.split(',') if keyword.strip()]
    
    # Featured
    featured = input("Feature this project prominently? (y/n): ").strip().lower() == 'y'
    
    return {
        'title': title,
        'period': period,
        'status': status,
        'logo': logo,
        'url': url,
        'description': description,
        'funding_agency': funding_agency,
        'pi': pi,
        'team_members': team_members,
        'keywords': keywords,
        'featured': featured
    }

def generate_project_entry(project_data):
    """Generate YAML entry for the project"""
    entry = {
        'title': project_data['title'],
        'period': project_data['period'],
        'logo': project_data['logo'],
        'url': project_data['url'] if project_data['url'] else '',
        'description': project_data['description'],
        'funding_agency': project_data['funding_agency'],
        'pi': project_data['pi'],
        'team_members': project_data['team_members'],
        'keywords': project_data['keywords'],
        'featured': project_data['featured']
    }
    return entry

def main():
    # Get user input
    project_data = get_project_input()
    
    # Generate YAML entry
    yaml_entry = generate_project_entry(project_data)
    
    print("\n" + "=" * 50)
    print("📋 GENERATED YAML ENTRY")
    print("=" * 50)
    
    section = project_data['status']
    print(f"\n# Add this to the '{section}:' section in _data/projects.yml\n")
    
    # Format YAML output
    yaml_output = yaml.dump([yaml_entry], default_flow_style=False, allow_unicode=True)
    # Remove the leading list indicator and fix indentation
    yaml_lines = yaml_output.split('\n')[1:]  # Skip first line with '-'
    formatted_yaml = '  - ' + yaml_lines[0] + '\n'  # Add '  - ' to first line
    for line in yaml_lines[1:]:
        if line.strip():
            formatted_yaml += '    ' + line + '\n'  # Add 4-space indentation
    
    print(formatted_yaml)
    
    print("📝 INSTRUCTIONS:")
    print(f"1. Upload logo to: assets/img/projects/{project_data['logo']}")
    print(f"2. Open _data/projects.yml")
    print(f"3. Find the '{section}:' section")
    print(f"4. Add the YAML entry above")
    print(f"5. Commit your changes")
    
    print("\n✅ Done! The project will appear on the website after committing.")

if __name__ == '__main__':
    main()