#!/bin/bash

# New content creation script for IMEDEA-AP-LAB website
# Usage: ./scripts/new-content.sh [type] [name]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}📝 IMEDEA-AP Lab Content Creator${NC}"
echo -e "${BLUE}================================${NC}"

# Function to create a new project
create_project() {
    local name="$1"
    local filename="_projects/${name}.md"
    local title=$(echo "$name" | tr '_-' ' ' | sed 's/\b\w/\U&/g')
    
    cat > "$filename" << EOF
---
layout: page
title: "$title"
description: "Brief description of the $title project"
img: /assets/img/projects/${name}.jpg
importance: 1
category: research
---

## Overview

Brief overview of the project.

## Objectives

- Objective 1
- Objective 2
- Objective 3

## Methodology

Description of the methodology used.

## Results

Key results and findings.

## Publications

List of related publications.

## Team

- Team member 1
- Team member 2

## Funding

Information about funding sources.

## Timeline

- Start date: 
- End date: 

EOF

    echo -e "${GREEN}✅ Created new project: $filename${NC}"
    echo -e "${YELLOW}💡 Don't forget to add a project image at: assets/img/projects/${name}.jpg${NC}"
}

# Function to create a new news item
create_news() {
    local title="$1"
    local date=$(date '+%Y-%m-%d')
    local filename="_news/${date}-${title}.md"
    
    cat > "$filename" << EOF
---
layout: post
date: $date
inline: true
related_posts: false
---

Your news content here. Keep it concise for inline news items.

EOF

    echo -e "${GREEN}✅ Created new news item: $filename${NC}"
}

# Function to add a new publication
add_publication() {
    local title="$1"
    local year=$(date '+%Y')
    
    echo -e "${YELLOW}📚 Adding publication to _data/publications.yml${NC}"
    echo -e "${BLUE}Please edit the file manually to add:${NC}"
    echo ""
    echo "  - title: \"$title\""
    echo "    authors: \"Author names\""
    echo "    journal: \"Journal name\""
    echo "    year: $year"
    echo "    doi: \"https://doi.org/...\""
    echo "    abstract: \"Abstract text\""
    echo "    bibtex: |"
    echo "      @article{key$year,"
    echo "        title={$title},"
    echo "        author={Author names},"
    echo "        journal={Journal name},"
    echo "        year={$year},"
    echo "        doi={...}"
    echo "      }"
    echo ""
}

# Main script logic
case "$1" in
    "project")
        if [ -z "$2" ]; then
            echo -e "${RED}❌ Project name required${NC}"
            echo "Usage: ./scripts/new-content.sh project project-name"
            exit 1
        fi
        create_project "$2"
        ;;
    "news")
        if [ -z "$2" ]; then
            echo -e "${RED}❌ News title required${NC}"
            echo "Usage: ./scripts/new-content.sh news news-title"
            exit 1
        fi
        create_news "$2"
        ;;
    "publication")
        if [ -z "$2" ]; then
            echo -e "${RED}❌ Publication title required${NC}"
            echo "Usage: ./scripts/new-content.sh publication \"Publication Title\""
            exit 1
        fi
        add_publication "$2"
        ;;
    *)
        echo -e "${YELLOW}📖 Available content types:${NC}"
        echo ""
        echo -e "${BLUE}Projects:${NC}"
        echo "  ./scripts/new-content.sh project project-name"
        echo ""
        echo -e "${BLUE}News:${NC}"
        echo "  ./scripts/new-content.sh news news-title"
        echo ""
        echo -e "${BLUE}Publications:${NC}"
        echo "  ./scripts/new-content.sh publication \"Publication Title\""
        echo ""
        exit 1
        ;;
esac

echo -e "${GREEN}✨ Content creation complete!${NC}"
