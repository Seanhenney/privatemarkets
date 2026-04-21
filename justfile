# Show available recipes
default:
    @just --list

# Start the dev container in the background
up:
    docker compose up -d

# Stop the dev container
down:
    docker compose down

# Show the URL where the docs site is served
url:
    @printf "http://localhost:%s\n" "$(docker compose port docs 8000 | cut -d: -f2)"

# Run the MkDocs preview server
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

# Rebuild the container image (run after host-side dependency changes)
rebuild:
    docker compose down && docker compose up -d --build

# Clean up
clean:
    docker compose down -v
    rm -rf site/ dist/
