---
name: map-sources
description: Inventory the sources of a skillset's domain logic - handbook, methods, existing canvases, own practice - with license, what each contributes and where they conflict.
disable-model-invocation: true
---

# Map sources

Make every rule the skillset will contain traceable to a source or a decision. Read `design/SKILLSET-CANVAS.md` (blocks 1–6), `design/SOURCES.md` and `design/DECISIONS.md`.

## 1. Inventory

For every source in block 5 and every source those sources point to (a handbook chapter that names three canvases names three more sources):

- **Read it**, in full, from the original location. For a long handbook, dispatch one sub-agent per chapter with the question "which steps, canvases, fields, criteria, examples and warnings does this chapter contain?". A source you cannot reach (network, login) is listed with status *not reached*, and you ask the maintainer for access or a copy; never reconstruct it from memory.
- **License**: find it on the source itself (footer, license page, repository `LICENSE`). Unknown means *unknown*, not "probably free". Note what the license requires: attribution text, share-alike, no derivatives, non-commercial.
- **Contribution**: which canvas blocks, process steps, checks and terms the source can supply.

Write each to the inventory table in `design/SOURCES.md`, with the date you accessed it.

## 2. Compare

- **Conflicts**: where sources disagree (two canvases name the same field differently, two methods order the steps differently), list both positions.
- **Gaps**: outcomes from block 3 that no source covers. They are filled by the maintainer's practice or by a decision, never silently by the agent.
- **License consequences**: what adopting each element would mean for the skillset's licenses (a CC BY-SA canvas adapted into the template makes the template CC BY-SA; a canvas under all rights reserved can be referenced, not copied).

## 3. Stop point

Present the inventory with the problems first: unreached sources, unknown licenses, conflicts, gaps, license consequences. For each, recommend: adopt, adapt, reference only, or leave out. Ask as multiple-choice questions with their own context (see `skillset-conventions`). Record each decision in `design/DECISIONS.md`, fill *What is adopted*, *Conflicts* and *Left out* in `design/SOURCES.md`, and summarise block 5 of the canvas in a few lines.

Done when every source has a license entry or an open question with an owner, and every conflict has a decision. Suggest `/design-canvas`.
