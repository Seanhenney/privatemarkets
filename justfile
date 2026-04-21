# Show available recipes
default:
    @just --list

# Start the dev container in the background
up:
    docker compose up -d

# Stop the dev container
down:
    docker compose down

# Run the MkDocs preview server at localhost:8000
serve:
    docker compose exec docs uv run mkdocs serve --dev-addr=0.0.0.0:8000

# Run pytest
test:
    docker compose exec docs uv run pytest

# Lint with Ruff
lint:
    docker compose exec docs uv run ruff check .

# Format with Ruff
format:
    docker compose exec docs uv run ruff format .

# Type check with mypy
typecheck:
    docker compose exec docs uv run mypy src/

# Build the docs site into ./site
build:
    docker compose exec docs uv run mkdocs build --strict

# Open a bash shell inside the container
shell:
    docker compose exec docs bash

# Add a Python dependency
add package:
    docker compose exec docs uv add {{package}}

# Rebuild the container image (after dependency changes)
rebuild:
    docker compose down && docker compose up -d --build

# Clean up
clean:
    docker compose down -v
    rm -rf site/ dist/ .venv/
