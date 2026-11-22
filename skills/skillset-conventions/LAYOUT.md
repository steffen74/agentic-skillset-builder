# Layout of a skillset repo

```
README.md                    why, the three parts (canvas, process, skills), skill table, install, credits
AGENTS.md                    maintainer instructions + `## Agentic skillset builder` section
CLAUDE.md                    `@AGENTS.md`
CONTRIBUTING.md              feedback wanted, skill conventions (points to skillset-conventions)
CHANGELOG.md                 `## Unreleased` on top
LICENSE                      MIT, for the skills
LICENSE-docs.md              CC BY 4.0, for canvas, templates and docs (unless a source license requires otherwise)
NOTICE.md                    adapted sources (Matt Pocock's skills, the domain sources from design/SOURCES.md)
.gitignore                   build/, __pycache__/
.claude-plugin/plugin.json   name, version, description, explicit `skills` list
.claude-plugin/marketplace.json
.claude/skills/release-skillset/SKILL.md   core, verbatim
.skillset-core.json          core lock; .skillset-core/masters/ for adapted masters
canvas/README.md             canvas guide, block by block
canvas/<name>-canvas.svg|pdf generated with render_canvas.py --print
docs/principles.md           the habits the skillset encodes, with related work
docs/process.md              main flow with stop points, on-ramps, files in a project
scripts/check_skillset.py    core, verbatim
skills/<setup>/templates/    canvas template (single source) and the other project files
skills/show-canvas/          core
skills/<other skills>/
design/                      how the skillset was designed (see below)
examples/<case>/             the case used for dry runs; examples/<case>/run-<date>/ keeps a dry run's project, transcripts and git bundle as worked example and exercise material
course/                      optional self-study course for the skillset's users, built with Agentic Course Creation from the dry-run material
site: GitHub Pages (default) built from README, canvas/, course/, docs/ by a core workflow, switched on when the repository is public
```

## `design/` (written by the builder's skills)

| File | Content | Written by |
|---|---|---|
| `SKILLSET-CANVAS.md` | The Skillset Canvas for this skillset | all builder skills |
| `PERSONAS.md` | Who runs the skills, with their knowledge state | `/grill-practice` |
| `SOURCES.md` | Sources, license, what is adopted from each | `/map-sources` |
| `SKILL-MAP.md` | Process, stop points, skill list with roles and files, glossary | `/to-skill-map` |
| `DECISIONS.md` | Design decisions | all builder skills at stop points |
| `SIGNALS.md` | Dry runs, check results, feedback from use | `/dry-run`, `/review-skillset`, `/skillset-retro` |

## `## Agentic skillset builder` section of the skillset repo's `AGENTS.md`

```markdown
## Agentic skillset builder

- Canvas: `design/SKILLSET-CANVAS.md` (read before any work on this skillset; update when something is decided)
- Language: <code, e.g. de>
- Design files: `design/` (personas, sources, skill map, decisions, signals)
- Canvas template: `skills/<setup>/templates/<CANVAS>.md`
- Printed canvas: `canvas/<name>-canvas.svg` and `.pdf`, made with `python3 skills/show-canvas/scripts/render_canvas.py skills/<setup>/templates/<CANVAS>.md --print --lang <code> --out canvas/<name>-canvas.svg --pdf canvas/<name>-canvas.pdf --subtitle "<tagline>" --footer "<Name> Canvas v<X.Y> · <license> · <repo URL>"`
- Example case: `examples/<case>/`
- Checks: `python3 scripts/check_skillset.py`
- Core: `.skillset-core.json`, synced with `/sync-core` from the agentic skillset builder
```
