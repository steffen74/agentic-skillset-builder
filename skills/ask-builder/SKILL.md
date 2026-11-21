---
name: ask-builder
description: Ask which skillset builder skill fits your situation. A router over the skills in this repo.
disable-model-invocation: true
---

# Ask builder

Read `design/SKILLSET-CANVAS.md`, `design/SKILL-MAP.md` and the `## Agentic skillset builder` section of `AGENTS.md`. If any is missing and the user is starting a new skillset, the answer is `/setup-skillset`; if they are inside an existing skillset repo without them, `/sync-core` followed by `/grill-practice`.

Then recommend **one** next skill, with one sentence on why, based on the first gap you find:

| If … | Recommend |
|---|---|
| Blocks 1–4 or 6, or `design/PERSONAS.md`, are empty or vague | `/grill-practice` |
| Block 5 or `design/SOURCES.md` is empty, a source was added, or a license is unknown | `/map-sources` |
| Purpose and sources are settled, but there is no canvas template in `skills/<setup>/templates/` | `/design-canvas` |
| The domain canvas exists, but `design/SKILL-MAP.md` has no process and skill list | `/to-skill-map` |
| A skill in the skill map is *planned* | `/draft-skill <skill>` (next in the order of the role groups) |
| All skills of a role group are drafted, but no dry run covers them | `/dry-run` |
| A dry run is done, but the skillset is not reviewed | `/review-skillset` |
| The skillset was used for real, or a dry run found a problem no check caught | `/skillset-retro` |
| `core_sync.py status` reports updates, or a file exists in two skillsets in different versions | `/sync-core` |

If the user describes a situation instead, map it to the table. When two rows apply, recommend the earlier one.
