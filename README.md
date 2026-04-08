# Retrofuturism Style Database

A lightweight, local-first reference repository for historical retrofuturism art directions.

This project is designed for AI art applications that need structured context about style eras, visual motifs, palettes, materials, and prompt tokens.

## What is included

- `data/retrofuturism_entries.json` — core style entries for major retrofuturism waves.
- `data/schema.json` — JSON schema for validating new entries.
- `src/retrofuturism_db/database.py` — tiny Python API for load/get/search.
- `src/retrofuturism_db/cli.py` — CLI for listing and querying styles.
- `examples/prompt_templates.md` — prompt blueprints for model integrations.

## Data model summary

Each entry includes:

- `id`, `era`, `title`, `summary`
- `influences`, `visual_cues`, `color_palette`
- `materials`, `architecture`, `fashion`
- `prompt_tokens`, `negative_tokens`, `source_notes`

## Example usage

### Python

```python
from retrofuturism_db import load_default_db

db = load_default_db()
print([entry.id for entry in db.list_entries()])
print(db.get("atompunk-space-age"))
print(db.search("art deco"))
```

### CLI

```bash
python -m retrofuturism_db.cli list
python -m retrofuturism_db.cli get atompunk-space-age
python -m retrofuturism_db.cli search "analog"
```

## Extending the database

1. Add new entries in `data/retrofuturism_entries.json`.
2. Follow `data/schema.json` for field structure.
3. Keep prompt tokens concise and visually grounded.
4. Prefer historically rooted terms over pure sci-fi jargon.

## Suggested next steps

- Add per-entry image references and citation metadata.
- Add JSON schema validation in CI.
- Publish as a pip package with typed API docs.
