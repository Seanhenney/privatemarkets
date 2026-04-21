# Open Private Markets

**A shared reference vocabulary for private markets.**

Open Private Markets (OPM) is a public initiative to build shared, open infrastructure for the private markets industry. This repository holds the first component: a glossary of firm types, fund structures, strategies, asset classes, instruments, and roles.

The glossary is published two ways. As a documentation website at [openprivatemarkets.org](https://openprivatemarkets.org) for humans to read and cite. As a Python package called `privatemarkets` on PyPI for software to consume.

## Why this exists

Private markets runs on language that nobody shares. Every firm defines the same concepts differently. Every software vendor hard-codes its own taxonomy. Every research report templates its data differently. The fragmentation makes benchmarking imprecise, regulatory reporting harder than it should be, and every new piece of software reinvent the same foundational work.

Other parts of finance have solved this with shared reference infrastructure. Banking has the Financial Industry Business Ontology. The web has schema.org. APIs have OpenAPI. Private markets has nothing equivalent. OPM is the project to build one, starting with the vocabulary.

## What is in this repository

The glossary source files, organised by category under [`glossary/`](./glossary/). Each term is a markdown file with YAML front matter holding the structured data and a prose body holding the definition.

The Python package source under [`src/privatemarkets/`](./src/privatemarkets/) which exposes the glossary as typed Pydantic models for programmatic use.

The JSON Schema that validates every term under [`schemas/`](./schemas/).

The MkDocs configuration, Docker setup, and GitHub Actions workflows that render the site and publish the package.

## Install

```bash
pip install privatemarkets
```

Use in Python:

```python
from privatemarkets import glossary

terms = glossary()
fund_manager = terms["fund-manager"]
print(fund_manager.name)
print(fund_manager.sub_types)
```

## Contribute

Contributions are welcome. The typical flow is to suggest an edit through the button on any page of the [documentation site](https://openprivatemarkets.org), which opens a pre-filled pull request. For direct contributions, see [CONTRIBUTING.md](./CONTRIBUTING.md).

The maintainer reviews every change personally. Expect careful discussion of definitions, because a shared vocabulary is only valuable if the definitions are precise.

## Develop locally

Prerequisites: [Docker Desktop](https://www.docker.com/products/docker-desktop), [Just](https://just.systems), and Git.

```bash
git clone https://github.com/openprivatemarkets/privatemarkets.git
cd privatemarkets
just up
just serve
```

Open [http://localhost:8000](http://localhost:8000) to preview the site. Changes to glossary files trigger automatic reloads.

Other useful commands:

```bash
just test          # run the test suite
just lint          # check code style
just build         # build the static site
just shell         # open a shell inside the dev container
just down          # stop the dev container
```

All Python commands run inside a Docker container. Nothing is installed on the host machine beyond Docker, Just, and Git. This keeps the development environment reproducible across machines.

## Scope

OPM is a public umbrella for open, shared private markets infrastructure. The glossary is the first component. Future components may include shared calculation libraries, reference data schemas, validation tooling, and other infrastructure the industry benefits from having in common. Each component is decided on when there is genuine demand, not on speculation.

## Relationship to adjacent standards

OPM aligns with the [Financial Industry Business Ontology (FIBO)](https://spec.edmcouncil.org/fibo) where concepts overlap. Terms in this glossary record their FIBO equivalent through a URI field where one exists. FIBO coverage of private markets is thin; OPM fills that gap.

The governance model is inspired by [schema.org](https://schema.org). Lightweight collaboration through GitHub with a small steering group, not a formal standards body.

## License

Content in this repository (glossary definitions, documentation, and other prose) is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Anyone can use, adapt, and redistribute the content, including commercially, with credit to OPM.

Code in this repository (the Python package, build scripts, and workflows) is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Copyright © 2026 Sean Henney.

See [LICENSE](./LICENSE) for the full notice.

## Maintainer

OPM is currently maintained by Sean Henney. As the project grows, governance expands to a small committee and eventually a broader council. See [CONTRIBUTING.md](./CONTRIBUTING.md) for the contribution process.

## Links

- Website: [openprivatemarkets.org](https://openprivatemarkets.org)
- Python package: [pypi.org/project/privatemarkets](https://pypi.org/project/privatemarkets)
- Source: [github.com/openprivatemarkets/privatemarkets](https://github.com/openprivatemarkets/privatemarkets)
- Issues: [github.com/openprivatemarkets/privatemarkets/issues](https://github.com/openprivatemarkets/privatemarkets/issues)
