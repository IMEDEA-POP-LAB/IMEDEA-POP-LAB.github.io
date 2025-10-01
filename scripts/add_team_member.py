#!/usr/bin/env python3

"""
Automatic Team Member Addition Script

This script helps quickly add new team members to the website.
It generates the YAML entry and provides instructions for manual addition.

Usage: python3 add_team_member.py
"""

import yaml
from datetime import datetime
import os

def get_user_input():
    """Collect team member information from user input"""
    print("🎓 IMEDEA Lab Team Member Addition Tool")
    print("=" * 50)
    
    # Basic information
    name = input("Full name (e.g., Dr. Jane Smith): ").strip()
    title = input("Position/Title (e.g., Postdoctoral Researcher): ").strip()
    
    # Category selection
    print("\nSelect category:")
    print("1. Principal Investigators")
    print("2. Research Scientists")
    print("3. Postdocs")
    print("4. PhD Students")
    print("5. Master Students")
    print("6. Visiting Researchers")
    
    category_map = {
        '1': 'principal_investigators',
        '2': 'research_scientists',
        '3': 'postdocs',
        '4': 'phd_students',
        '5': 'master_students',
        '6': 'visiting_researchers'
    }
    
    while True:
        choice = input("Enter choice (1-6): ").strip()
        if choice in category_map:
            category = category_map[choice]
            break
        print("Invalid choice. Please enter 1-6.")
    
    # Time period
    start_year = input("Start year (YYYY): ").strip()
    is_current = input("Currently active? (y/n): ").strip().lower() == 'y'
    if is_current:
        period = f"{start_year} - present"
    else:
        end_year = input("End year (YYYY): ").strip()
        period = f"{start_year} - {end_year}"
    
    # Contact information
    email = input("Email: ").strip()
    orcid = input("ORCID URL (optional): ").strip()
    scholar = input("Google Scholar URL (optional): ").strip()
    website = input("Personal website (optional): ").strip()
    
    # Biography and research interests
    print("\nBiography (2-3 sentences):")
    bio = input().strip()
    
    print("\nResearch interests (separate by commas):")
    interests_input = input().strip()
    research_interests = [interest.strip() for interest in interests_input.split(',')]
    
    # Generate image filename suggestion
    name_parts = name.lower().replace('dr. ', '').replace('prof. ', '').split()
    if len(name_parts) >= 2:
        suggested_filename = f"{name_parts[-1]}_{name_parts[0]}.jpg"
    else:
        suggested_filename = f"{name_parts[0]}.jpg"
    
    print(f"\nSuggested photo filename: {suggested_filename}")
    image = input(f"Photo filename (or press Enter for '{suggested_filename}'): ").strip()
    if not image:
        image = suggested_filename
    
    return {
        'name': name,
        'title': title,
        'period': period,
        'image': image,
        'email': email,
        'orcid': orcid,
        'scholar': scholar,
        'website': website,
        'bio': bio,
        'research_interests': research_interests,
        'category': category
    }

def generate_yaml_entry(member_data):
    """Generate YAML entry for the team member"""
    entry = {
        'name': member_data['name'],
        'title': member_data['title'],
        'period': member_data['period'],
        'image': member_data['image'],
        'email': member_data['email'],
        'orcid': member_data['orcid'] if member_data['orcid'] else '',
        'scholar': member_data['scholar'] if member_data['scholar'] else '',
        'website': member_data['website'] if member_data['website'] else '',
        'bio': member_data['bio'],
        'research_interests': member_data['research_interests']
    }
    
    return entry

def main():
    # Get user input
    member_data = get_user_input()
    
    # Generate YAML entry
    yaml_entry = generate_yaml_entry(member_data)
    
    print("\n" + "=" * 50)
    print("📋 GENERATED YAML ENTRY")
    print("=" * 50)
    print(f"\n# Add this to the '{member_data['category']}:' section in _data/team.yml\n")
    
    # Format YAML output
    yaml_output = yaml.dump([yaml_entry], default_flow_style=False, allow_unicode=True)
    # Remove the leading list indicator and fix indentation
    yaml_lines = yaml_output.split('\n')[1:]  # Skip first line with '-'
    formatted_yaml = '- ' + yaml_lines[0] + '\n'  # Add '- ' to first line
    for line in yaml_lines[1:]:
        if line.strip():
            formatted_yaml += '  ' + line + '\n'  # Add 2-space indentation
    
    print(formatted_yaml)
    
    print("📝 INSTRUCTIONS:")
    print(f"1. Upload photo to: assets/img/team/{member_data['image']}")
    print(f"2. Open _data/team.yml")
    print(f"3. Find the '{member_data['category']}:' section")
    print(f"4. Add the YAML entry above")
    print(f"5. Commit your changes")
    
    print("\n✅ Done! The team member will appear on the website after committing.")

if __name__ == '__main__':
    main()