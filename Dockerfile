FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --frozen --no-install-project || uv sync --no-install-project

COPY . .
RUN uv sync --frozen || uv sync

EXPOSE 8000

CMD ["uv", "run", "mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]