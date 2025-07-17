# IMEDEA-AP Lab Website Makefile
# Simple commands for common tasks

.PHONY: help serve build deploy clean install new-project new-news optimize test

# Default target
help:
	@echo "🌊 IMEDEA-AP Lab Website Commands"
	@echo "================================="
	@echo ""
	@echo "Development:"
	@echo "  make serve       Start development server"
	@echo "  make build       Build the website"
	@echo "  make clean       Clean build files"
	@echo "  make install     Install dependencies"
	@echo ""
	@echo "Content:"
	@echo "  make new-project NAME=project-name"
	@echo "  make new-news TITLE=news-title"
	@echo ""
	@echo "Deployment:"
	@echo "  make deploy      Build and deploy to GitHub Pages"
	@echo ""
	@echo "Utilities:"
	@echo "  make optimize    Optimize images"
	@echo "  make test        Run tests"
	@echo ""

# Development commands
serve:
	@./scripts/serve.sh

build:
	@./scripts/build.sh

deploy:
	@./scripts/build.sh --deploy

clean:
	@bundle exec jekyll clean
	@echo "✅ Cleaned build files"

install:
	@bundle install
	@echo "✅ Dependencies installed"

# Content creation
new-project:
ifndef NAME
	$(error NAME is required. Usage: make new-project NAME=project-name)
endif
	@./scripts/new-content.sh project $(NAME)

new-news:
ifndef TITLE
	$(error TITLE is required. Usage: make new-news TITLE=news-title)
endif
	@./scripts/new-content.sh news $(TITLE)

# Utilities
optimize:
	@./scripts/optimize-images.sh

test:
	@echo "🧪 Running tests..."
	@bundle exec jekyll build --strict_front_matter
	@echo "✅ All tests passed"

# Quick development setup
setup: install
	@echo "🚀 Setup complete! Run 'make serve' to start development"
