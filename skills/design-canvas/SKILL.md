---
name: design-canvas
description: Design the canvas a new skillset gives its users - blocks, owners, boundary, hints - as the template, the guide and the printed SVG and PDF.
disable-model-invocation: true
---

# Design the canvas

Design the **domain canvas**: the one page the skillset's users fill in their project. Read `design/SKILLSET-CANVAS.md` (blocks 1–7), `design/SOURCES.md`, `design/PERSONAS.md`, `design/DECISIONS.md`. Load `skillset-conventions` for the canvas grammar. If blocks 1–4 or 6 are empty, stop and suggest `/grill-practice`; if sources have open license questions that affect the canvas, settle them first with `/map-sources`.

## 1. Draft the blocks

Work from the users' outcomes backwards:

- Start with the **columns** in the domain's words, following *purpose → design → build and improve*.
- Derive the **blocks** from the outcomes (block 3 of the Skillset Canvas) and the adopted sources. Where an established domain canvas exists (adopted or referenced in `design/SOURCES.md`), decide per field: becomes a block, is grouped into one block that points to a companion file (for example the nine fields of a business model canvas in `MODEL.md`), or is left out. Keep the agentic canvas about decisions, evidence, checks and signals; the domain canvas can live beside it.
- Give every block an **owner** from the judgement boundary (block 6): 👤 where it is a trade-off, 🤖 where it is facts or legwork.
- Name the **boundary** block: the domain's silent failure (see `skillset-conventions`).
- Put **checks**, **signals** and **improvements** blocks in the last columns, as the sibling skillsets do, so the loop closes.
- For each block, write a hint (prompting questions) and a `print:` line with two short prompts.

Present a mapping table: block → owner → source (or decision) → which outcome it serves. Next to it, the block-by-block correspondence with the Agentic Data Science and Agentic Course Creation canvases, so users of several skillsets see the shared grammar.

**Stop point**: the maintainer decides blocks, names, owners and the boundary. Log the structural choices in `design/DECISIONS.md`.

## 2. Write the canvas

1. **Template**: `skills/<setup>/templates/<CANVAS>.md` in the skillset's language, following the grammar exactly (header fields, `> Owners:` line, `---` rules, numbered blocks with owner emoji, hint and `print:` comments, *Open questions* and *Decision log* after the last rule). This file is the single source of the canvas.
2. **Guide**: `canvas/README.md`, block by block: purpose, prompts, typical mistakes, *Filled by* (skills from the skill map, or *to be decided* until `/to-skill-map` exists), and the correspondence table.
3. **Printed canvas**: run the command from the `- Printed canvas:` line of `AGENTS.md`. Look at the result (render the SVG or PDF to an image) and fix overflowing prompts by shortening the `print:` lines, not by changing the script.

Run `python3 scripts/check_skillset.py`; `printed-canvas` passes now.

Done when template, guide and printed canvas exist, the maintainer has seen the printed version, and block 7 of the Skillset Canvas names the domain canvas. Suggest `/to-skill-map`.
