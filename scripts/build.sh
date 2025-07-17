#!/bin/bash

# Build and deploy script for IMEDEA-AP-LAB website
# Usage: ./scripts/build.sh [--deploy]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🏗️  IMEDEA-AP Lab Website Build Script${NC}"
echo -e "${BLUE}=====================================${NC}"

# Clean previous builds
echo -e "${YELLOW}🧹 Cleaning previous builds...${NC}"
bundle exec jekyll clean

# Build the site
echo -e "${YELLOW}🔨 Building the website...${NC}"
JEKYLL_ENV=production bundle exec jekyll build

# Check if build was successful
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Build completed successfully!${NC}"
    echo -e "${BLUE}📁 Built site is in the _site directory${NC}"
else
    echo -e "${RED}❌ Build failed${NC}"
    exit 1
fi

# If --deploy flag is passed, commit and push
if [ "$1" = "--deploy" ]; then
    echo -e "${YELLOW}🚀 Deploying to GitHub Pages...${NC}"
    
    # Check if there are any changes
    if [ -n "$(git status --porcelain)" ]; then
        echo -e "${YELLOW}📝 Committing changes...${NC}"
        git add .
        read -p "Enter commit message (or press Enter for default): " commit_msg
        if [ -z "$commit_msg" ]; then
            commit_msg="Update website content - $(date '+%Y-%m-%d %H:%M')"
        fi
        git commit -m "$commit_msg"
        
        echo -e "${YELLOW}⬆️  Pushing to GitHub...${NC}"
        git push origin main
        
        echo -e "${GREEN}🌐 Deployment complete! Changes will be live in 1-5 minutes.${NC}"
        echo -e "${BLUE}🔗 Visit: https://imedea-ap-lab.github.io${NC}"
    else
        echo -e "${YELLOW}📝 No changes to deploy${NC}"
    fi
fi

echo -e "${GREEN}✨ All done!${NC}"
