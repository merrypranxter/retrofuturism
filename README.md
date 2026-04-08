# Retrofuturism Style Database

A local-first style archive for retrofuturism research, visual development, and AI-assisted prompt workflows.

This repository now combines:

- **Structured JSON entries** for machine use.
- **A Python/CLI interface** for loading and querying styles.
- **A doc set** for taxonomy, motif logic, composition systems, and application guidance.

## Repository layout

- `data/retrofuturism_entries.json` — canonical style entries.
- `data/schema.json` — JSON schema for validating entries.
- `docs/` — human-readable archive references:
  - taxonomy
  - visual trait matrix
  - motif vocabulary
  - composition logic
  - color/material/surface guide
  - historical & regional variants
  - application-domain guidance
  - prompting guide
  - glossary
- `src/retrofuturism_db/database.py` — data model + search API.
- `src/retrofuturism_db/cli.py` — CLI commands.
- `examples/prompt_templates.md` — reusable prompt templates.

## Data model summary

Each style entry includes base fields (`id`, `era`, `title`, `summary`) plus structured style facets:

- Visual cues and palette
- Materials, architecture, fashion
- Shape language and pattern systems
- Ornament and symbol logic
- Composition and lighting guidance
- Typography/graphics cues
- Historical context and regional variants
- Modern reinterpretation and adjacent styles
- Prompt tokens, negative tokens, and practical usage notes

## Example usage

### Python

```python
from retrofuturism_db import load_default_db

db = load_default_db()

# List all style IDs
print([entry.id for entry in db.list_entries()])

# Retrieve one entry
entry = db.get("cassette-futurism")
print(entry.composition_rules)

# Search by motif/context
for result in db.search("constructivist"):
    print(result.id, result.title)
```

### CLI

```bash
python -m retrofuturism_db.cli list
python -m retrofuturism_db.cli get y2k-retrofuture-pop
python -m retrofuturism_db.cli search "mission control"
```

## Curation rules for contributors

1. Keep entries historically anchored.
2. Separate adjacent substyles explicitly.
3. Add practical implementation detail (composition, materials, symbols).
4. Update `docs/INDEX.md` if new archive sections are created.
5. Avoid vague descriptors that could apply to any sci-fi style.

## Suggested follow-ups

- Add JSON schema validation in CI.
- Add per-entry citation metadata for primary references.
- Add image reference boards per style entry.
