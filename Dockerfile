FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./
RUN uv sync --all-groups --frozen --no-install-project || uv sync --all-groups --no-install-project

COPY . .
RUN uv sync --all-groups --frozen || uv sync --all-groups

EXPOSE 8000

CMD ["uv", "run", "mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]