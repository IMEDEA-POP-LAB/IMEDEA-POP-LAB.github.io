#!/usr/bin/env python3

"""
Data Validation Script

This script validates the YAML data files for the IMEDEA Lab website.
It checks for syntax errors, required fields, and data consistency.

Usage: python3 validate_data.py
"""

import yaml
import os
from pathlib import Path

def validate_yaml_file(file_path):
    """Validate YAML syntax and structure"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        return True, data, None
    except yaml.YAMLError as e:
        return False, None, str(e)
    except Exception as e:
        return False, None, str(e)

def validate_team_data(data):
    """Validate team.yml structure and required fields"""
    issues = []
    
    if not isinstance(data, dict):
        issues.append("Team data should be a dictionary with categories")
        return issues
    
    required_categories = ['principal_investigators', 'research_scientists', 'postdocs', 
                          'phd_students', 'master_students', 'visiting_researchers', 'alumni']
    
    for category in required_categories:
        if category not in data:
            issues.append(f"Missing category: {category}")
        elif data[category] is None:
            continue  # Empty categories are OK
        elif not isinstance(data[category], list):
            issues.append(f"Category '{category}' should be a list")
        else:
            # Validate each team member
            for i, member in enumerate(data[category]):
                if not isinstance(member, dict):
                    issues.append(f"{category}[{i}]: Should be a dictionary")
                    continue
                
                required_fields = ['name', 'title', 'period', 'image', 'email']
                for field in required_fields:
                    if field not in member:
                        issues.append(f"{category}[{i}]: Missing required field '{field}'")
                
                # Check email format
                if 'email' in member and member['email']:
                    if '@' not in member['email']:
                        issues.append(f"{category}[{i}]: Invalid email format")
                
                # Check image file reference
                if 'image' in member and member['image']:
                    img_path = f"assets/img/team/{member['image']}"
                    if not os.path.exists(img_path):
                        issues.append(f"{category}[{i}]: Image file not found: {img_path}")
    
    return issues

def validate_projects_data(data):
    """Validate projects.yml structure and required fields"""
    issues = []
    
    if not isinstance(data, dict):
        issues.append("Projects data should be a dictionary with 'current' and 'completed' sections")
        return issues
    
    for section in ['current', 'completed']:
        if section not in data:
            issues.append(f"Missing section: {section}")
        elif data[section] is None:
            continue  # Empty sections are OK
        elif not isinstance(data[section], list):
            issues.append(f"Section '{section}' should be a list")
        else:
            # Validate each project
            for i, project in enumerate(data[section]):
                if not isinstance(project, dict):
                    issues.append(f"{section}[{i}]: Should be a dictionary")
                    continue
                
                required_fields = ['title', 'period', 'description', 'funding_agency', 'pi']
                for field in required_fields:
                    if field not in project:
                        issues.append(f"{section}[{i}]: Missing required field '{field}'")
                
                # Check logo file reference
                if 'logo' in project and project['logo']:
                    img_path = f"assets/img/projects/{project['logo']}"
                    if not os.path.exists(img_path):
                        issues.append(f"{section}[{i}]: Logo file not found: {img_path}")
                
                # Check team_members is a list
                if 'team_members' in project and project['team_members'] is not None:
                    if not isinstance(project['team_members'], list):
                        issues.append(f"{section}[{i}]: 'team_members' should be a list")
                
                # Check keywords is a list
                if 'keywords' in project and project['keywords'] is not None:
                    if not isinstance(project['keywords'], list):
                        issues.append(f"{section}[{i}]: 'keywords' should be a list")
    
    return issues

def validate_news_data(data):
    """Validate news.yml structure and required fields"""
    issues = []
    
    if not isinstance(data, list):
        issues.append("News data should be a list of news items")
        return issues
    
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            issues.append(f"News item {i}: Should be a dictionary")
            continue
        
        required_fields = ['date', 'title', 'description', 'category']
        for field in required_fields:
            if field not in item:
                issues.append(f"News item {i}: Missing required field '{field}'")
        
        # Validate date format
        if 'date' in item:
            try:
                from datetime import datetime
                datetime.strptime(item['date'], '%Y-%m-%d')
            except ValueError:
                issues.append(f"News item {i}: Invalid date format (should be YYYY-MM-DD)")
        
        # Validate category
        valid_categories = ['research', 'team', 'funding', 'conference', 'award', 'publication', 'other']
        if 'category' in item and item['category'] not in valid_categories:
            issues.append(f"News item {i}: Invalid category '{item['category']}' (valid: {', '.join(valid_categories)})")
    
    return issues

def validate_publications_data(data):
    """Validate publications.yml structure"""
    issues = []
    
    if not isinstance(data, dict):
        issues.append("Publications data should be a dictionary")
        return issues
    
    if 'recent' not in data:
        issues.append("Missing 'recent' section in publications")
        return issues
    
    if not isinstance(data['recent'], list):
        issues.append("'recent' section should be a list")
        return issues
    
    for i, pub in enumerate(data['recent']):
        if not isinstance(pub, dict):
            issues.append(f"Publication {i}: Should be a dictionary")
            continue
        
        required_fields = ['title', 'authors', 'journal', 'year']
        for field in required_fields:
            if field not in pub:
                issues.append(f"Publication {i}: Missing required field '{field}'")
        
        # Validate year
        if 'year' in pub:
            try:
                year = int(pub['year'])
                if year < 1900 or year > 2030:
                    issues.append(f"Publication {i}: Invalid year {year}")
            except (ValueError, TypeError):
                issues.append(f"Publication {i}: Year should be a number")
    
    return issues

def main():
    """Main validation function"""
    print("🔍 IMEDEA Lab Website Data Validation")
    print("=" * 50)
    
    data_dir = Path("_data")
    all_valid = True
    
    # Define validation functions for each file
    validators = {
        'team.yml': validate_team_data,
        'projects.yml': validate_projects_data,
        'news.yml': validate_news_data,
        'publications.yml': validate_publications_data
    }
    
    for filename, validator_func in validators.items():
        file_path = data_dir / filename
        
        print(f"\n📄 Validating {filename}...")
        
        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            all_valid = False
            continue
        
        # Check YAML syntax
        is_valid, data, error = validate_yaml_file(file_path)
        
        if not is_valid:
            print(f"❌ YAML syntax error: {error}")
            all_valid = False
            continue
        
        # Check structure and content
        issues = validator_func(data)
        
        if issues:
            print(f"❌ Found {len(issues)} issue(s):")
            for issue in issues:
                print(f"   • {issue}")
            all_valid = False
        else:
            print("✅ Valid!")
    
    # Check navigation.yml separately (simpler structure)
    nav_file = data_dir / 'navigation.yml'
    if nav_file.exists():
        print(f"\n📄 Validating navigation.yml...")
        is_valid, data, error = validate_yaml_file(nav_file)
        if is_valid:
            print("✅ Valid!")
        else:
            print(f"❌ YAML syntax error: {error}")
            all_valid = False
    
    print("\n" + "=" * 50)
    if all_valid:
        print("🎉 All data files are valid!")
    else:
        print("⚠️  Some issues found. Please fix them before deploying.")
    
    return all_valid

if __name__ == '__main__':
    exit(0 if main() else 1)