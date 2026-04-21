"""Typed models for glossary terms."""

from __future__ import annotations

from datetime import date
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field

KebabId = Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]
SemVer = Annotated[str, Field(pattern=r"^\d+\.\d+\.\d+$")]
TermStatus = Literal["draft", "review", "approved", "deprecated"]


class GlossaryFrontmatter(BaseModel):
    """YAML front matter for one term; fields match ``glossary-term.schema.json``."""

    model_config = ConfigDict(extra="forbid")

    id: KebabId
    name: str
    category: str
    sub_types: list[KebabId] = Field(default_factory=list)
    typical_roles: list[KebabId] = Field(default_factory=list)
    related_terms: list[KebabId] = Field(default_factory=list)
    fibo_equivalent: str | None = None
    status: TermStatus
    version: SemVer
    last_updated: date | None = None


class GlossaryTerm(GlossaryFrontmatter):
    """Validated front matter plus markdown body below the closing ``---``."""

    body: str = ""
