# Skill map

## Process

See [docs/process.md](../docs/process.md) for the diagram and the step table.

## Skills

| Skill | Role | User-invoked | Reads | Writes | Canvas blocks | Status | Adapted from |
|---|---|---|---|---|---|---|---|
| `setup-skillset` | setup | yes | environment, sources list | repository, `design/`, `.skillset-core.json` | all | drafted | `setup-matt-pocock-skills` |
| `ask-builder` | router | yes | `design/` | – | – | drafted | `ask-matt` |
| `show-canvas` | core | yes | canvas, decisions | `build/canvas.html` | all | drafted | S1, S2 |
| `grill-practice` | grill | yes | `design/` | canvas 1–4, 6, personas, decisions | 1–4, 6 | drafted | `grilling` |
| `map-sources` | inventory | yes | sources | `SOURCES.md`, canvas 5, decisions | 5 | drafted | – |
| `design-canvas` | produce | yes | `design/` | canvas template, `canvas/` | 7 | drafted | – |
| `to-skill-map` | plan | yes | `design/`, canvas template | `SKILL-MAP.md`, canvas 7, 9 | 7, 9 | drafted | `to-spec` |
| `draft-skill` | produce | yes | `SKILL-MAP.md`, roles, sources | `skills/<name>/`, `plugin.json`, `NOTICE.md` | 9 | drafted | – |
| `dry-run` | walk-through | yes | skills, personas, example case | `SIGNALS.md`, `SKILL-MAP.md` status | 10 | drafted | S2 `walk-through` |
| `review-skillset` | review | yes | repository, `design/` | `DECISIONS.md`, statuses | 8, 9 | drafted | `code-review` |
| `skillset-retro` | retro | yes | `SIGNALS.md`, issues | fixes, checks, builder issues | 10, 11 | drafted | `retro` |
| `sync-core` | – (maintenance) | yes | `.skillset-core.json` | core files, lock | – | drafted | – |
| `skillset-conventions` | checks + boundary reference | no | – | – | 6, 8 | drafted | `writing-for-agents` (summary) |
| `skillset-core` | core reference | no | – | – | – | drafted | – |
| `release-skillset` | maintainer | yes | changes since tag | version, changelog, canvas, tag | – | drafted | S1 `release-plugin` |

## Files in a skillset repository

See [docs/process.md](../docs/process.md#files-in-a-skillset-repository).

## Glossary

| Term | Meaning |
|---|---|
| skillset | A canvas, a process and agent skills for one kind of work, in one repository |
| skillset repo | The repository of a skillset |
| project | A repository where users apply a skillset |
| core | Files every skillset shares, synced from `skillset-core` |
| role | The job a skill plays in the process (setup, grill, plan …) |
| boundary | The block whose crossing is the domain's silent failure |
| stop point | A step's end where the user decides |
| dry run | Running a skillset on its example case as a persona |
