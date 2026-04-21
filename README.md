# Open Private Markets

**Shared, open infrastructure for the private markets industry.**

Open Private Markets (OPM) is a public initiative to build the commons that private markets firms and software vendors can build on rather than reinvent. This repository holds the first component: a shared reference vocabulary covering firm types, fund structures, strategies, asset classes, instruments, and roles. More components may follow.

The glossary is published two ways. As a documentation website at [openprivatemarkets.org](https://openprivatemarkets.org) for humans to read and cite. As the `privatemarkets` Python package on PyPI for software to consume programmatically.

## Why this exists

Private markets runs on language that nobody shares. Every firm defines the same concepts differently. Every software vendor hard-codes its own taxonomy. Every research report templates its data differently. The fragmentation makes benchmarking imprecise, regulatory reporting harder than it should be, and every new piece of software reinvent the same foundational work.

Other parts of finance have solved this with shared reference infrastructure. Banking has the [Financial Industry Business Ontology](https://spec.edmcouncil.org/fibo). The web has [schema.org](https://schema.org). APIs have [OpenAPI](https://www.openapis.org/). Private markets has nothing equivalent. OPM is the project to build one.

## Scope

OPM is a public umbrella for open, shared private markets infrastructure. The glossary is the first component because vocabulary is the foundation every other component depends on. Plausible future components include shared calculation libraries (IRR, MOIC, DPI, and so on), reference data schemas for common private markets data structures, validation tooling, and reference workflows. Each one is decided on when there is genuine demand, not on speculation.

## What is in this repository

- The glossary content under [`src/privatemarkets/glossary/`](./src/privatemarkets/glossary/), organised by category. Each term is a markdown file with YAML front matter holding the structured data and a prose body holding the definition.
- The Python package source under [`src/privatemarkets/`](./src/privatemarkets/), which loads the glossary into typed Pydantic models.
- The JSON Schema under [`schemas/`](./schemas/) that validates every term's front matter.
- The MkDocs configuration, Docker setup, and GitHub Actions workflows that render the site and publish the package.

The glossary lives inside the Python package folder (rather than at the repository root) so it ships with the package to PyPI consumers.

## Install

```bash
pip install privatemarkets
```

Use in Python:

```python
from privatemarkets import glossary

terms = glossary()  # dict keyed by term ID, e.g. "fund-manager"
fund_manager = terms["fund-manager"]
print(fund_manager.name)
print(fund_manager.sub_types)
```

Term IDs follow kebab-case throughout (`fund-manager`, not `fund_manager`). The dictionary key, the URL path, the filename, and the wikilink target are all the same string.

## Contribute

Contributions are welcome. The typical flow is to suggest an edit through the button on any page of the [documentation site](https://openprivatemarkets.org), which opens a pre-filled pull request. For direct contributions, see [CONTRIBUTING.md](./CONTRIBUTING.md).

The maintainer reviews every change personally. Expect careful discussion of definitions, because a shared vocabulary is only valuable if the definitions are precise.

## Develop locally

Prerequisites on your machine: [Docker Desktop](https://www.docker.com/products/docker-desktop), [UV](https://docs.astral.sh/uv/getting-started/installation/), [Just](https://just.systems), and Git.

```bash
git clone https://github.com/openprivatemarkets/privatemarkets.git
cd privatemarkets
just up
just url
```

`just url` prints the URL where the preview site is served (typically `http://localhost:8000`, or a different port if 8000 is busy on your machine). Open it in a browser. Changes to glossary files trigger automatic reloads.

Other useful commands:

```bash
just test          # run the test suite
just lint          # check code style
just typecheck     # type check with mypy
just build         # build the static site into ./site
just shell         # open a bash shell inside the dev container
just rebuild       # rebuild the image after dependency changes
just down          # stop the dev container
```

All day-to-day Python commands run inside a Docker container. UV is the only Python-related tool installed on the host, and only because it manages dependencies and scaffolds the project. Day-to-day commands do not touch your host.

To change Python dependencies (rare):

```bash
uv add <package>           # runtime dependency
uv add --dev <package>     # development dependency
just rebuild               # rebuild the container to pick up the change
```

## Relationship to adjacent standards

OPM aligns with [FIBO](https://spec.edmcouncil.org/fibo) where concepts overlap. Terms in this glossary record their FIBO equivalent through a URI field where one exists. FIBO's coverage of private markets is thin; OPM fills that gap.

The governance model is inspired by [schema.org](https://schema.org/docs/howwework.html). Lightweight collaboration through GitHub with a small steering group, not a formal standards body.

## License

OPM is dual-licensed.

**Content** (glossary definitions, prose bodies, documentation) is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Anyone can use, adapt, and redistribute, including commercially, with credit to OPM. See [LICENSE-CC-BY-4.0](./LICENSE-CC-BY-4.0).

**Code** (the Python package, build scripts, workflows, JSON Schema) is licensed under the [MIT License](https://opensource.org/licenses/MIT). See [LICENSE-MIT](./LICENSE-MIT).

The package metadata expresses this as the SPDX expression `MIT AND CC-BY-4.0` so tools that consume PyPI metadata can identify both licenses unambiguously.

Copyright © 2026 Sean Henney.

## Maintainer

OPM is currently maintained by Sean Henney. As the project grows, governance expands to a small committee and eventually a broader council. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the contribution process.

## Links

- Website: [openprivatemarkets.org](https://openprivatemarkets.org)
- Python package: [pypi.org/project/privatemarkets](https://pypi.org/project/privatemarkets)
- Source: [github.com/openprivatemarkets/privatemarkets](https://github.com/openprivatemarkets/privatemarkets)
- Issues: [github.com/openprivatemarkets/privatemarkets/issues](https://github.com/openprivatemarkets/privatemarkets/issues)