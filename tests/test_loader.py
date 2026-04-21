"""Tests for the glossary loader."""

from __future__ import annotations

from pathlib import Path

import pytest

from privatemarkets import GlossaryTerm, glossary
from privatemarkets.loader import FrontmatterError, load_term, parse_frontmatter


def test_glossary_returns_dict():
    terms = glossary()
    assert isinstance(terms, dict)


def test_glossary_values_are_terms():
    for term in glossary().values():
        assert isinstance(term, GlossaryTerm)


def test_glossary_keys_are_kebab_case():
    for term_id in glossary():
        assert term_id.replace("-", "").isalnum()
        assert term_id.replace("-", "").islower()


def test_parse_frontmatter_rejects_file_without_frontmatter(tmp_path: Path):
    bad_file = tmp_path / "bad.md"
    bad_file.write_text("# Just a heading, no frontmatter\n")
    with pytest.raises(FrontmatterError):
        parse_frontmatter(bad_file)


def test_parse_frontmatter_extracts_data_and_body(tmp_path: Path):
    good_file = tmp_path / "good.md"
    good_file.write_text("---\nid: example-term\nname: Example Term\n---\nBody content here.\n")
    data, body = parse_frontmatter(good_file)
    assert data["id"] == "example-term"
    assert body == "Body content here."


def test_load_term_validates_frontmatter_and_sets_body(tmp_path: Path):
    term_file = tmp_path / "term.md"
    term_file.write_text(
        "---\n"
        "id: example-term\n"
        "name: Example Term\n"
        "category: examples\n"
        "status: draft\n"
        "version: 1.0.0\n"
        "---\n"
        "Prose here.\n"
    )
    term = load_term(term_file)
    assert term.id == "example-term"
    assert term.name == "Example Term"
    assert term.category == "examples"
    assert term.status == "draft"
    assert term.version == "1.0.0"
    assert term.body == "Prose here."
