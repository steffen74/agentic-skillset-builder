# The process

The process follows the Skillset Canvas from left to right, but it is a loop: skills are drafted in role groups, dry-run, reviewed and released, and real use feeds signals back into the skillset, the builder and the core.

## Main flow

| Step | Skill | Agent does | Stop point (maintainer decides) | Canvas |
|---|---|---|---|---|
| 1. Set up | `/setup-skillset` | Checks the environment, scaffolds the repository, copies the core | Name, language, target (local, GitHub, ZIP), sources, example case | all |
| 2. Sharpen the practice | `/grill-practice` | Asks in rounds, recommends, looks up facts in the sources | Practice, users, outcomes, evidence, judgement boundary | 1–4, 6 |
| 3. Map sources | `/map-sources` | Reads every source, finds licenses, conflicts and gaps | Adopt, adapt, reference or leave out | 5 |
| 4. Design the canvas | `/design-canvas` | Drafts blocks and owners, writes template, guide, printed canvas | Blocks, names, owners, boundary | 7 |
| 5. Map the skills | `/to-skill-map` | Process, skill list with roles, files, glossary; finds gaps | Skill list, names, role groups | 7, 9 |
| 6. Draft | `/draft-skill` | Drafts each skill from its skeleton and sources | Each role group | 9 |
| 7. Dry run | `/dry-run` | Runs the skillset on the example case as a persona | Gap in a skill or accepted risk | 10 |
| 8. Review | `/review-skillset` | Conventions and practice axes | Release, fix or hold; public or private | 8, 9 |
| 9. Release | `release-skillset` | Version, changelog, printed canvas, tag, GitHub release | Version, go-ahead | – |
| 10. Retro | `/skillset-retro` | Explains signals at the right level: skillset, builder or core | Which changes to adopt | 10, 11 |

Steps 6–8 repeat per role group. Step 10 runs after every dry run that found something no check caught, and after real use.

## On-ramps

- **An existing skillset** (built before the builder): `/sync-core` adopts the core, then `/grill-practice` and `/map-sources` fill `design/` from what exists, then `/dry-run`.
- **A core change** (a fix in `render_canvas.py`, a new check): change it in `skills/skillset-core/files/`, then `/sync-core` on every skillset.
- **A user hit a problem**: `/skillset-retro` in the skillset repository; builder-level causes become issues here.

## Files in a skillset repository

| File | Content | Written by |
|---|---|---|
| `design/SKILLSET-CANVAS.md` | The Skillset Canvas | all builder skills |
| `design/PERSONAS.md` | Users with their knowledge state | `/grill-practice` |
| `design/SOURCES.md` | Sources, licenses, what is adopted | `/map-sources` |
| `design/SKILL-MAP.md` | Process, skills, shared files, glossary | `/to-skill-map`, `/draft-skill` |
| `design/DECISIONS.md` | Design decisions | all builder skills at stop points |
| `design/SIGNALS.md` | Dry runs, reviews, feedback | `/dry-run`, `/review-skillset`, `/skillset-retro` |
| `skills/<setup>/templates/` | The domain canvas template and project files | `/design-canvas`, `/draft-skill` |
| `canvas/` | Guide and printed canvas | `/design-canvas`, `release-skillset` |
| `.skillset-core.json` | Core lock | `/setup-skillset`, `/sync-core` |

The full layout is in `skills/skillset-conventions/LAYOUT.md`.
