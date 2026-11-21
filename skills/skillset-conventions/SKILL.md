---
name: skillset-conventions
description: Conventions for agentic skillsets - canvas grammar, owners and stop points, skill roles, files in AGENTS.md, language rule, repository layout and the checks a skillset passes before release. Use when designing a canvas, drafting or reviewing a skill of a skillset, or deciding where something goes.
---

# Skillset conventions

An **agentic skillset** is a canvas, a process and a set of agent skills for one kind of work, in one repository (the **skillset repo**). People install it into their own repository (the **project**), where the skills read and write the canvas and its companion files. The habit every skillset encodes: **the agent finds facts and does the legwork, the person decides, and work passes explicit checks before it counts.**

## Canvas grammar

The canvas is one Markdown file with a fixed grammar, so the core renderer (`render_canvas.py`) reads every skillset's canvas:

```markdown
# <Name> Canvas
**<Field>:** <!-- e.g. Project, Team, Version -->
> Owners: 👤 <role> decides · 🤖 agent drafts, <role> approves.

---

## <Column>
### 1. <Block> 👤
<!-- Hint: what goes here, as questions. -->
<!-- print: first short prompt | second short prompt -->

---

## Open questions
## Decision log
```

- **Columns** follow the arc *purpose → design → build and improve*, named in the domain's words. Three columns, 9–12 blocks, numbered through.
- Every block has one **owner**: 👤 the person decides (the agent may recommend), or 🤖 the agent drafts and the person approves. Facts are 🤖, trade-offs are 👤.
- One block is the **boundary**: the line whose crossing is the domain's typical silent failure (data science: information not known at prediction time; course creation: knowledge learners do not have yet; skillset design: decisions the agent takes instead of the person). Everything across it is a leak, a gap or an untested assumption, and a skill checks it.
- A block may point to an existing domain canvas or method (for example *Business Model Canvas, see `MODEL.md`*) instead of rebuilding it.
- `**Version:**` holds the date of the last update, so the renderer can show decisions newer than the canvas.
- Each block has a `print:` comment with two short prompts (about 40 characters each) for the printed canvas.
- The canvas template exists once, in `skills/<setup skill>/templates/`. The printed SVG/PDF in `canvas/` is generated from it with `render_canvas.py --print`, and `canvas/README.md` is the guide with purpose, prompts, typical mistakes and *Filled by* per block.

## Owners and stop points

Every decision a person owns is a **stop point**: the agent recommends, the person decides, the decision is logged in `DECISIONS.md` with date, reason, alternatives and canvas block. Ask decisions as multiple-choice questions that carry their own context (what and where, why it matters, constraints, two to four options with consequences, recommendation first). Use the environment's question tool when there is one.

## Skill roles

Each skill of a skillset plays one **role**. [roles/README.md](roles/README.md) is the catalogue; each role has a skeleton file there, read when drafting or reviewing a skill of that role. Every skillset has at least: setup, router, show-canvas (core), grill, plan, one or more produce skills, a check (walk-through or review) and retro, plus reference skills for its checks and its boundary.

- User-invoked skills set `disable-model-invocation: true` and have a one-line, human-facing description. Reference skills keep a model-facing description that starts with what they are and lists their triggers.
- Skills follow Matt Pocock's `writing-for-agents`: short, ordered steps that each end on a completion criterion, reference behind pointers, leading words instead of restated triads, positive instructions.
- Skills read and write only the files named in the skillset's section of the project's `AGENTS.md`; they never invent locations.

## Language

Read [LANGUAGE.md](LANGUAGE.md) when the skillset's language is not English.

## Repository layout and checks

Read [LAYOUT.md](LAYOUT.md) when creating or reorganising a skillset repo, and [CHECKS.md](CHECKS.md) when reviewing a skillset or turning a dry-run finding into a check.
