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
