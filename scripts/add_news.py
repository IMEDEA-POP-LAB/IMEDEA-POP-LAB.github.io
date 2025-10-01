#!/usr/bin/env python3

"""
Quick News Addition Script

This script helps quickly add news updates to the website.
It generates the YAML entry for the news data file.

Usage: python3 add_news.py
"""

import yaml
from datetime import datetime, date

def get_news_input():
    """Collect news information from user input"""
    print("📰 IMEDEA Lab News Addition Tool")
    print("=" * 50)
    
    # Date
    use_today = input("Use today's date? (y/n): ").strip().lower() == 'y'
    if use_today:
        news_date = date.today().strftime('%Y-%m-%d')
    else:
        news_date = input("Date (YYYY-MM-DD): ").strip()
    
    # Title and description
    title = input("News title: ").strip()
    description = input("News description: ").strip()
    
    # Category
    print("\nSelect category:")
    print("1. Research")
    print("2. Team")
    print("3. Funding")
    print("4. Conference")
    print("5. Award")
    print("6. Publication")
    print("7. Other")
    
    category_map = {
        '1': 'research',
        '2': 'team',
        '3': 'funding',
        '4': 'conference',
        '5': 'award',
        '6': 'publication',
        '7': 'other'
    }
    
    while True:
        choice = input("Enter choice (1-7): ").strip()
        if choice in category_map:
            category = category_map[choice]
            break
        print("Invalid choice. Please enter 1-7.")
    
    # Featured
    featured = input("Feature on homepage? (y/n): ").strip().lower() == 'y'
    
    return {
        'date': news_date,
        'title': title,
        'description': description,
        'category': category,
        'featured': featured
    }

def generate_news_entry(news_data):
    """Generate YAML entry for the news item"""
    entry = {
        'date': news_data['date'],
        'title': news_data['title'],
        'description': news_data['description'],
        'category': news_data['category'],
        'featured': news_data['featured']
    }
    return entry

def main():
    # Get user input
    news_data = get_news_input()
    
    # Generate YAML entry
    yaml_entry = generate_news_entry(news_data)
    
    print("\n" + "=" * 50)
    print("📋 GENERATED YAML ENTRY")
    print("=" * 50)
    print("\n# Add this at the TOP of _data/news.yml\n")
    
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
    print("1. Open _data/news.yml")
    print("2. Add the YAML entry above at the TOP of the file")
    print("3. Commit your changes")
    
    print("\n✅ Done! The news will appear on the website after committing.")

if __name__ == '__main__':
    main()