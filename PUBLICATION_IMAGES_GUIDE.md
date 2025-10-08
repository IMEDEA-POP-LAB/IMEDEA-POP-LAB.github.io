# Adding Images to Publications

This guide explains how to add images to your publications in the IMEDEA POP Lab website.

## Overview

Publications can now display thumbnail images alongside the text content. These images appear in the publications list and help make the page more visually engaging.

## Adding Images to Publications

Add an `image` field to your publication entry in `_data/publications.yml` using external URLs:

```yaml
- title: "Your Publication Title"
  authors: "Author list"
  journal: "Journal Name"
  year: 2025
  doi: "https://doi.org/..."
  image: "https://example.com/path/to/image.jpg"
```

**Note**: Only external image URLs are supported. Images must be publicly accessible on the internet.

## Best Practices for Images

### Image Sources
- **Journal figures**: Use key figures from your published articles
- **Journal covers**: Some journals provide cover images for articles
- **Publisher assets**: Many publishers provide downloadable figures
- **Graphical abstracts**: If available, these work well as thumbnails

### Image Specifications
- **Dimensions**: Images will be displayed at 120x80px (desktop) or 300x120px (mobile)
- **Format**: JPG, PNG, or WebP
- **Size**: Keep file sizes under 500KB for optimal loading
- **Aspect ratio**: 3:2 ratio works best (e.g., 300x200px)

### Finding Publication Images

#### From Journal Websites
1. Go to your published article's page
2. Look for downloadable figures or graphical abstracts
3. Right-click and copy image URL, or download and save locally

#### From Publisher APIs
Some publishers provide APIs or direct links to article images:
- **Nature/Springer**: Often have figure URLs in article metadata
- **Elsevier/ScienceDirect**: Provides downloadable figures
- **Wiley**: Article pages include figure thumbnails
- **AGU Publications**: Figures available in various formats

#### Example Image URLs
```yaml
# Nature/Scientific Reports
image: "https://media.springernature.com/.../MediaObjects/..._Fig1_HTML.png"

# Frontiers
image: "https://www.frontiersin.org/files/Articles/.../image_m/...-g001.jpg"

# AGU Publications  
image: "https://agupubs.onlinelibrary.wiley.com/cms/asset/.../...-fig-0001-m.jpg"

# Copernicus Publications
image: "https://sp.copernicus.org/articles/.../...-f01-web.png"
```

## Layout Behavior

- **With Image**: Publication displays with thumbnail on the left, text on the right
- **Without Image**: Publication displays as text-only with full width
- **Mobile**: Images stack above text content for better mobile experience
- **Loading**: Images use lazy loading for better performance

## Troubleshooting

### Image Not Displaying
- Check that the URL is accessible and doesn't require authentication
- Ensure the image format is supported (JPG, PNG, WebP, GIF)
- Verify there are no CORS restrictions on external images
- Make sure the URL points directly to an image file

### Layout Issues
- Images are automatically cropped to fit the 120x80px container
- Use images with landscape orientation for best results
- The layout automatically adapts when images are missing

### Performance
- External images are loaded lazily to improve page load speed
- Images are cached by browsers for subsequent visits
- No local storage means faster site builds and deployments

## Optional Enhancements

You can extend this system by:
- Adding alt text fields for better accessibility
- Including image captions or credits
- Supporting multiple images per publication
- Adding hover effects or lightbox functionality

## Support

For technical issues or questions about adding publication images, check the Jekyll documentation or contact the web team.