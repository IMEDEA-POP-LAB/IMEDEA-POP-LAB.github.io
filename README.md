# IMEDEA Physical Ocean Processes Lab

Website for Physical Ocean Processes Lab IMEDEA (CSIC-UIB).

🌐 **Live Site**: [https://imedea-pop-lab.github.io](https://imedea-pop-lab.github.io)

## How to Update Content

All website content is managed through simple YAML files in the `_data/` folder.

### Data Files
- `_data/people.yml` - Team members
- `_data/projects.yml` - Research projects  
- `_data/publications.yml` - Publications
- `_data/outreach.yml` - Videos and documentaries
- `_data/media.yml` - Press coverage

### Recent features
- Research gallery on the About page: vertical carousel with 4 visible tiles, hover/focus captions and keyboard navigation (`scripts/research-carousel.js`, styles in `_sass/components/_carousel.scss`).
- Outreach and media items: unified title styling and increased spacing (`_sass/pages/_outreach.scss`).
- Publications and projects: grid layouts and a minimalist "View All Publications" button (`_sass/pages/_publications.scss`, `_sass/utilities/_overrides.scss`).

### Editing the About research gallery
- Images: put image files in `assets/img/gallery/`.
- Markup: the gallery is currently defined directly in `_pages/about.md` — each tile uses a `div.gallery-item` with an `<img>` and a `<div class="gallery-caption">` for the visible caption. Captions are shown on hover and keyboard focus.
- JS/CSS: sizing and behavior are controlled by `scripts/research-carousel.js` and `_sass/components/_carousel.scss`.

### Instructions
📖 **See `DATA_MANAGEMENT_MANUAL.md` for complete instructions and examples**

### Repository Updates
```bash
./scripts/update_repositories.sh YOUR_GITHUB_TOKEN
```

## Development

To run locally:
```bash
bundle install
bundle exec jekyll serve
```

## License

MIT License - see [LICENSE](LICENSE) file.
