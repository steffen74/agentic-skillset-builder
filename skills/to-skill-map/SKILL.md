---
name: to-skill-map
description: Turn the canvas into the skillset's process and skill map - steps with stop points, skills with roles, the files they share, and the glossary.
disable-model-invocation: true
---

# To skill map

Write the plan every skill is drafted from. Read `design/SKILLSET-CANVAS.md`, the domain canvas template, `canvas/README.md`, `design/SOURCES.md`, `design/PERSONAS.md`, `design/DECISIONS.md`. Load `skillset-conventions`, including its role catalogue (`roles/README.md`). Do not interview again; if the domain canvas is missing, stop and suggest `/design-canvas`.

## 1. Draft

Fill `design/SKILL-MAP.md`:

1. **Process**: the domain's steps from the sources and block 7, as an ASCII diagram with its loops (signals back into fixes, retro back into checks and rules), and as a table: step, skill, what the agent does, the stop point, canvas blocks.
2. **Skills**: one row per skill with its role from the catalogue, user-invoked or reference, the files it reads and writes, its canvas blocks, status *planned*, and the Matt Pocock skill or sibling-skillset skill it is adapted from. Name skills with English verbs and the domain noun (`grill-model`, `to-pitch`); keep `show-canvas` as is. Reuse a sibling skillset's skill name when the role is the same, so users of several skillsets recognise it.
3. **Files in a project**: every file the skills share, with writer and readers. Every file read must have a writer; the canvas file and the decision log are always present.
4. **Glossary**: every domain term the skills use, in the skillset's language, with its English identifier where one exists, and its source.

## 2. Check the map

Before presenting, check and list as problems:

- a 👤 block no skill settles, or a 🤖 block no skill drafts;
- a file read but never written;
- a person-owned decision in a step without a stop point;
- a required role missing (setup, router, show-canvas, grill, plan, produce, check, retro, reference skills for checks and boundary);
- a skill that serves no outcome of the Skillset Canvas.

## 3. Stop point

Present the map with the problems first and a recommendation for each. The maintainer decides the skill list, names and order. Also settle the **role groups** for drafting and approval (default: core and setup, then grill and plan, then produce and check, then retro and reference). Log the choices in `design/DECISIONS.md`, and update blocks 7 and 9 of the Skillset Canvas and *Filled by* in `canvas/README.md`.

Done when the maintainer has confirmed `design/SKILL-MAP.md` and every problem is fixed or listed under **Open questions**. Suggest `/draft-skill` for the first skill of the first role group.
