"""Open Private Markets reference vocabulary."""

from __future__ import annotations

from functools import cache
from pathlib import Path

from privatemarkets.loader import load_glossary
from privatemarkets.models import GlossaryFrontmatter, GlossaryTerm

__version__ = "0.0.2"

_GLOSSARY_DIR = Path(__file__).parent / "glossary"


@cache
def glossary() -> dict[str, GlossaryTerm]:
    """Return every glossary term keyed by id."""
    return load_glossary(_GLOSSARY_DIR)


__all__ = ["GlossaryFrontmatter", "GlossaryTerm", "glossary"]
