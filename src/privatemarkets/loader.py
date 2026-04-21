"""Load glossary terms from YAML front matter in markdown files."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from privatemarkets.models import GlossaryFrontmatter, GlossaryTerm

FRONTMATTER_DELIMITER = "---"


class FrontmatterError(ValueError):
    """Raised when a markdown file has missing or malformed YAML front matter."""


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """Split a markdown file into its YAML front matter and prose body."""
    text = path.read_text(encoding="utf-8")

    if not text.startswith(FRONTMATTER_DELIMITER):
        raise FrontmatterError(f"{path} has no YAML front matter")

    try:
        _, frontmatter_text, body = text.split(FRONTMATTER_DELIMITER, maxsplit=2)
    except ValueError as exc:
        raise FrontmatterError(f"{path} has malformed front matter") from exc

    data = yaml.safe_load(frontmatter_text) or {}
    return data, body.strip()


def load_term(path: Path) -> GlossaryTerm:
    """Load a single glossary term from a markdown file."""
    data, body = parse_frontmatter(path)
    frontmatter = GlossaryFrontmatter.model_validate(data)
    return GlossaryTerm(**frontmatter.model_dump(), body=body)


def load_glossary(glossary_dir: Path) -> dict[str, GlossaryTerm]:
    """Load every glossary term under a directory, keyed by id.

    Skips ``index.md`` files, which are category landing pages rather
    than terms.
    """
    terms: dict[str, GlossaryTerm] = {}
    for md_path in glossary_dir.rglob("*.md"):
        if md_path.name == "index.md":
            continue
        term = load_term(md_path)
        terms[term.id] = term
    return terms
