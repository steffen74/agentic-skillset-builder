# Checks for a skillset

A skillset fails quietly: a skill that points to a file no other skill writes, a canvas block nobody fills, a stop point the agent skips. A **check** has an expected value from an independent source. Prefer *automated* (`scripts/check_skillset.py`), then *dry run* (`/dry-run`), then *manual*.

| Check | Expected value from | Type |
|---|---|---|
| Every skill is listed in `plugin.json`, every listed skill exists | The `skills/` tree | automated (`plugin-list`) |
| Every `name:` equals its folder; every skill has a description within 1024 characters | The folder names | automated (`frontmatter`) |
| Every slash-command reference in backticks in Markdown names an existing skill | The skill names | automated (`skill-refs`) |
| `AGENTS.md` names language, canvas template, printed canvas | `LAYOUT.md` | automated (`agents`) |
| The printed canvas was made from the current template | Template hash in the SVG | automated (`printed-canvas`) |
| Verbatim core files are unchanged | `.skillset-core.json` | automated (`core`) |
| Every 👤 block has a skill that settles it, every 🤖 block a skill that drafts it | Canvas template, *Filled by* in `canvas/README.md` | manual |
| Every file a skill reads is written by `setup` or by another skill | `design/SKILL-MAP.md` file table | manual or dry run |
| Every person-owned decision in a skill is a stop point with a log entry | Canvas owners | dry run |
| The router covers every user-invoked skill, and its table order follows the process | `design/SKILL-MAP.md` | manual |
| Every step ends on a completion criterion | `writing-for-agents` | manual |
| Content is in the skillset's language; identifiers are English | `LANGUAGE.md` | manual |
| Every adopted source has a license entry, and `NOTICE.md` covers it | `design/SOURCES.md` | manual |
| No rule contradicts its source without a decision explaining why | `design/SOURCES.md` | manual |
| A dry run on the example case is newer than the last skill change, without open blockers | `design/SIGNALS.md` | manual |
| Links resolve | The web | automated (link checker, when available) |

Every dry-run finding becomes a check, a skill change, or a recorded decision that it is not worth one. Add new checks to this file in the builder when they apply to all skillsets, otherwise to the skillset's own `CONTRIBUTING.md`.
