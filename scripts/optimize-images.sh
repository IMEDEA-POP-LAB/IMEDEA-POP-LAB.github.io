#!/bin/bash

# Image optimization script for IMEDEA-AP-LAB website
# Usage: ./scripts/optimize-images.sh [directory]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🖼️  IMEDEA-AP Lab Image Optimizer${NC}"
echo -e "${BLUE}=================================${NC}"

# Default directory
DIR=${1:-"assets/img"}

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo -e "${RED}❌ ImageMagick is not installed${NC}"
    echo -e "${YELLOW}Install with: brew install imagemagick${NC}"
    exit 1
fi

echo -e "${YELLOW}📁 Processing images in: $DIR${NC}"

# Function to optimize images
optimize_images() {
    local dir="$1"
    
    # Find and process JPG/JPEG files
    find "$dir" -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -print0 | while IFS= read -r -d '' file; do
        echo -e "${BLUE}🔧 Optimizing: $file${NC}"
        
        # Get original size
        original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        
        # Optimize with ImageMagick
        convert "$file" -strip -interlace Plane -gaussian-blur 0.05 -quality 85 "${file%.???}_optimized.jpg"
        
        # Replace original with optimized
        mv "${file%.???}_optimized.jpg" "$file"
        
        # Get new size
        new_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        
        # Calculate savings
        savings=$((original_size - new_size))
        percentage=$((savings * 100 / original_size))
        
        echo -e "${GREEN}  ✅ Saved ${savings} bytes (${percentage}%)${NC}"
    done
    
    # Find and process PNG files
    find "$dir" -type f -iname "*.png" -print0 | while IFS= read -r -d '' file; do
        echo -e "${BLUE}🔧 Optimizing: $file${NC}"
        
        # Get original size
        original_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        
        # Optimize with ImageMagick
        convert "$file" -strip -define png:compression-filter=5 -define png:compression-level=9 -define png:compression-strategy=1 "${file%.png}_optimized.png"
        
        # Replace original with optimized
        mv "${file%.png}_optimized.png" "$file"
        
        # Get new size
        new_size=$(stat -f%z "$file" 2>/dev/null || stat -c%s "$file" 2>/dev/null)
        
        # Calculate savings
        savings=$((original_size - new_size))
        percentage=$((savings * 100 / original_size))
        
        echo -e "${GREEN}  ✅ Saved ${savings} bytes (${percentage}%)${NC}"
    done
}

# Create web-optimized versions for gallery images
create_thumbnails() {
    local gallery_dir="assets/img/gallery"
    local thumb_dir="assets/img/gallery/thumbs"
    
    if [ -d "$gallery_dir" ]; then
        echo -e "${YELLOW}🖼️  Creating thumbnails for gallery...${NC}"
        
        # Create thumbnails directory if it doesn't exist
        mkdir -p "$thumb_dir"
        
        find "$gallery_dir" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" \) -print0 | while IFS= read -r -d '' file; do
            filename=$(basename "$file")
            thumb_file="$thumb_dir/$filename"
            
            if [ ! -f "$thumb_file" ]; then
                echo -e "${BLUE}🔧 Creating thumbnail: $filename${NC}"
                convert "$file" -resize 400x300^ -gravity center -crop 400x300+0+0 +repage -quality 80 "$thumb_file"
            fi
        done
    fi
}

# Run optimization
if [ -d "$DIR" ]; then
    optimize_images "$DIR"
    create_thumbnails
    echo -e "${GREEN}✅ Image optimization complete!${NC}"
else
    echo -e "${RED}❌ Directory $DIR does not exist${NC}"
    exit 1
fi
