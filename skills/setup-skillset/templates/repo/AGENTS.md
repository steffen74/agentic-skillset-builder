# AGENTS.md

Instructions for agents working on this repository (the skills themselves, not a project that uses them).

- Skill conventions: see [CONTRIBUTING.md](CONTRIBUTING.md).
- When a change affects users of the skills or the canvas (anything under `skills/`, `.claude-plugin/` or `canvas/`), add an entry under `## Unreleased` in `CHANGELOG.md`.
- Releases go through the `release-skillset` skill (`.claude/skills/release-skillset/`); leave `version` in `.claude-plugin/plugin.json` to it.
- New skills under `skills/` are also added to the `skills` list in `.claude-plugin/plugin.json`.
- The canvas template is the single source of the canvas; regenerate the printed canvas from it (command below) whenever it changes.
- Files listed in `.skillset-core.json` come from the core of the Agentic Skillset Builder; change verbatim ones there, then sync with `/sync-core`.
- {{Visibility rule, e.g.: never put content of a real project (participants' ideas, names, numbers) into this public repository.}}

## Agentic skillset builder

- Canvas: `design/SKILLSET-CANVAS.md` (read before any work on this skillset; update when something is decided)
- Language: {{code}}
- Design files: `design/` (personas, sources, skill map, decisions, signals)
- Canvas template: `skills/{{setup skill}}/templates/{{CANVAS file}}`
- Printed canvas: `canvas/{{slug}}-canvas.svg` and `.pdf`, made with `python3 skills/show-canvas/scripts/render_canvas.py skills/{{setup skill}}/templates/{{CANVAS file}} --print --lang {{code}} --out canvas/{{slug}}-canvas.svg --pdf canvas/{{slug}}-canvas.pdf --subtitle "{{tagline}}" --footer "{{Canvas name}} v0.1 · CC BY 4.0 · github.com/{{owner}}/{{repo}}"`
- Example case: `examples/{{case}}/`
- Checks: `python3 scripts/check_skillset.py`
- Core: `.skillset-core.json`, synced with `/sync-core` from the Agentic Skillset Builder
