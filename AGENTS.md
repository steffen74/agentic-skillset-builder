# AGENTS.md

Instructions for agents working on this repository (the builder itself, not a skillset built with it).

- Conventions: see [CONTRIBUTING.md](CONTRIBUTING.md) and `skills/skillset-conventions/`.
- When a change affects users of the builder or of the skillsets it builds (anything under `skills/`, `.claude-plugin/` or `canvas/`), add an entry under `## Unreleased` in `CHANGELOG.md`.
- Releases go through `release-skillset` (`.claude/skills/release-skillset/`); leave `version` in `.claude-plugin/plugin.json` to it.
- New skills under `skills/` are also added to the `skills` list in `.claude-plugin/plugin.json`.
- The core lives in `skills/skillset-core/files/`, listed in `skills/skillset-core/MANIFEST.json`. To change a core file: edit it there, bump `version` in the manifest, then `python3 skills/skillset-core/scripts/core_sync.py apply --target .` (and `status` for adapted files) so this repository's own copies follow. Never edit the copies (`skills/show-canvas/`, `scripts/check_skillset.py`, `.claude/skills/release-skillset/`) directly.
- After changing `render_canvas.py`, check that its HTML output for the canvases of Agentic Data Science and Agentic Course Creation is unchanged unless the change is intended.

## Agentic skillset builder

- Canvas: `design/SKILLSET-CANVAS.md` (read before any work on the builder; update when something is decided)
- Language: en
- Design files: `design/` (personas, sources, skill map, decisions, signals)
- Canvas template: `skills/setup-skillset/templates/design/SKILLSET-CANVAS.md`
- Printed canvas: `canvas/skillset-canvas.svg` and `.pdf`, made with `python3 skills/show-canvas/scripts/render_canvas.py skills/setup-skillset/templates/design/SKILLSET-CANVAS.md --print --lang en --out canvas/skillset-canvas.svg --pdf canvas/skillset-canvas.pdf --subtitle "The agent does the legwork, the maintainer decides, a dry run comes before release." --footer "Skillset Canvas v0.1 · CC BY 4.0 · github.com/steffen74/agentic-skillset-builder"`
- Example case: the Agentic Business Model Canvas skillset (built next; a compact record goes to `examples/`)
- Checks: `python3 scripts/check_skillset.py`
- Core: `.skillset-core.json`; this repository is the core's source
