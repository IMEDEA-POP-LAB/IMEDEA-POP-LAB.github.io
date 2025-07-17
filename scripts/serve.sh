#!/bin/bash

# Development server setup script for IMEDEA-AP-LAB website
# Usage: ./scripts/serve.sh [port]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default port
PORT=${1:-4000}

echo -e "${BLUE}🌊 IMEDEA-AP Lab Website Development Server${NC}"
echo -e "${BLUE}===========================================${NC}"

# Check if Jekyll is installed
if ! command -v jekyll &> /dev/null; then
    echo -e "${RED}❌ Jekyll is not installed${NC}"
    echo -e "${YELLOW}Installing Jekyll and dependencies...${NC}"
    
    # Check if bundle is available
    if ! command -v bundle &> /dev/null; then
        echo -e "${RED}❌ Bundler is not installed. Please install Ruby and Bundler first:${NC}"
        echo "  brew install ruby"
        echo "  gem install bundler"
        exit 1
    fi
    
    bundle install
fi

# Check if Gemfile exists and install dependencies
if [ -f "Gemfile" ]; then
    echo -e "${YELLOW}📦 Installing dependencies...${NC}"
    bundle install
fi

# Check if port is available
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null; then
    echo -e "${RED}❌ Port $PORT is already in use${NC}"
    echo -e "${YELLOW}💡 Try a different port: ./scripts/serve.sh 4001${NC}"
    exit 1
fi

echo -e "${GREEN}🚀 Starting Jekyll development server on port $PORT...${NC}"
echo -e "${BLUE}📱 Local site will be available at: http://localhost:$PORT${NC}"
echo -e "${YELLOW}⚡ Live reload is enabled - changes will auto-refresh${NC}"
echo ""
echo -e "${BLUE}Press Ctrl+C to stop the server${NC}"
echo ""

# Start Jekyll with live reload
bundle exec jekyll serve --port $PORT --livereload --drafts --incremental

echo -e "${GREEN}✅ Server stopped${NC}"
