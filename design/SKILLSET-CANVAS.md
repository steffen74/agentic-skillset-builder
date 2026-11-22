# Skillset Canvas

**Skillset:** Agentic Skillset Builder
**Maintainers:** Steffen Brandt
**Language:** en
**Version:** 2026-11-21

> Owners: 👤 maintainer decides · 🤖 agent drafts, maintainer approves.
> Keep each block short. Details go in the files in `design/`; decisions go in `design/DECISIONS.md`.

---

## Purpose

### 1. Practice 👤
Building process- and canvas-based agentic skillsets for a kind of work (data science, course creation, impact startups). Today the third skillset is built by copying the second: core files drift apart, domain rules creep in that no source supports, and nobody tests the skills as a user would.

### 2. Users 👤
Course instructors at opencampus.sh and similar, with domain expertise and a canvas or method they teach, little experience writing agent skills; plus the maintainer of the existing skillsets. See `PERSONAS.md`.

### 3. Outcomes 👤
- A skillset repository with canvas, process, skills, core and `design/`, installable with `npx skills` and as a Claude Code plugin.
- Every domain rule traceable to a source or decision.
- A shared core that keeps all skillsets in step.

Not: generating content for the skillset's domain; replacing the maintainer's judgement on what the skillset is for.

### 4. Evidence 👤
- `check_skillset.py` passes; a dry run on the example case without open blockers before each release.
- The Changemaker skillset gets built with the builder without editing the builder mid-way more than a few times (each edit logged as a signal).

---

## Design

### 5. Sources 🤖
Agentic Data Science and Agentic Course Creation (blueprint, MIT/CC BY 4.0, own work); Matt Pocock's skills (structure, `writing-for-agents`, `grilling`, `code-review`, MIT). See `SOURCES.md`.

### 6. Judgement boundary 👤
Agent: reading sources, licenses, drafting canvas and skills, running checks and dry runs, environment checks. Maintainer: practice, users, outcomes, which sources to adopt, blocks and owners, skill list, every approval, release, visibility. Typical slip: the agent filling a gap in the sources with plausible domain rules.

### 7. Process and stop points 👤
setup → grill → sources → domain canvas → skill map → draft (by role group) → dry run → review → release; retro loops back into skillset, builder and core. See `SKILL-MAP.md`.

### 8. Checks 🤖
Automated: `check_skillset.py` (plugin list, frontmatter, skill references, AGENTS section, printed canvas, core). Manual and dry run: `skillset-conventions/CHECKS.md`. Renderer: HTML output for the sibling canvases unchanged.

---

## Build and improve

### 9. Skills 🤖
Eleven user-invoked skills, two reference skills, one maintainer skill, all drafted. See `SKILL-MAP.md`.

### 10. Dry-run signals 🤖
First real run: building the Agentic Business Model Canvas skillset. See `SIGNALS.md`.

### 11. Improvements 👤
Planned after the Changemaker skillset: adopt the core in Agentic Data Science and Agentic Course Creation with `/sync-core`.

---

## Open questions
- Implement: optional course in `course/` (grill question, review check, dry-run artefacts as exercises) and GitHub Pages as default site via a core workflow. (Agent, after the ABMC dry run)
- Pages tooling: Jekyll (no build) or MkDocs Material (build in Actions)? (Steffen, when implementing)
- Is opencampus.gitbook.io reachable from the session that builds the Changemaker skillset, or is there a source repository for the handbook? (Steffen, before `/map-sources`)

## Decision log
See `design/DECISIONS.md`.
