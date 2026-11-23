# Decisions

One entry per decision, newest first. People decide; the agent proposes and records.

## 2026-11-23: First release 0.1.0, public

- **Context:** The builder has built the Agentic Business Model Canvas (released as 0.9.0) and recapped Agentic Course Creation (0.3.0); the maintainer asked to prepare the release and make the repository public.
- **Decision:** Release 0.1.0, the version already in `plugin.json`. No separate dry run of the builder itself: its two real uses count as runs, and their signals are recorded in the two skillsets and in `examples/agentic-business-model-canvas.md`.
- **Reason:** The links from the released skillsets point here; the builder has been exercised end to end once.
- **Alternatives:** a higher pre-1.0 version (nothing marks the builder as nearly done); a dry run of `/setup-skillset` on a fresh case first (later, with the third skillset).
- **Canvas:** –

## 2026-11-22: GitHub Pages as the default site of a skillset

- **Context:** Skillsets get a course in `course/` (decision in the Agentic Business Model Canvas, K1–K4); users like course participants do not read repositories. Whether a host (e.g. opencampus GitBook) stays is uncertain.
- **Decision:** Every skillset can publish a site; the default is GitHub Pages, built by a GitHub Actions workflow that is part of the core (same for all skillsets, synced with `/sync-core`). The site contains README, canvas guide, the canvas as a page (from `render_canvas.py`) and as PDF, the course and docs. `/setup-skillset` and `/review-skillset` ask: GitHub Pages (default), another host, or none. Pages are switched on when the repository becomes public (Pages for private repositories needs a paid plan and is public anyway outside Enterprise Cloud).
- **Reason:** One default that works without depending on a platform whose future is unclear; a core workflow keeps all skillset sites alike.
- **Alternatives:** GitBook Git Sync; no site; a site only on request.
- **Canvas:** 7, 9
- **Status:** layout, questions and checks implemented 2026-11-22; tooling decided 2026-11-23: MkDocs Material, built in GitHub Actions (better navigation and readability for course participants; one build step in the core workflow). Workflow to implement with the first site (Agentic Business Model Canvas release).

## 2026-11-21: The builder itself starts as a private GitHub repository

- **Context:** Where to create the builder (Q18 of the grilling session).
- **Decision:** Build locally, create `steffen74/agentic-skillset-builder` as a private repository, push to a branch, no pull request until reviewed.
- **Reason:** First real test of the setup target logic; private until the first dry run.
- **Alternatives:** Maintainer creates the empty repository; local only.
- **Canvas:** 7

## 2026-11-21: New skillsets are built locally first; GitHub and ZIP are ways out

- **Context:** Where `/setup-skillset` creates a repository (Q17).
- **Decision:** Check the environment, offer only working options; always build locally; GitHub (default private until the first dry run passes) and ZIP as exports; the GitHub question returns at the first release.
- **Reason:** Works in every environment; visibility decided after the skillset has been tested.
- **Alternatives:** GitHub only; ZIP only.
- **Canvas:** 7

## 2026-11-21: Skill drafts are approved by role group

- **Context:** 12–15 skills per skillset (Q16).
- **Decision:** Mandatory stop points: canvas blocks, sources and licenses, domain canvas, skill map, skill drafts per role group, dry-run result, release.
- **Reason:** Approving each skill singly interrupts too often.
- **Alternatives:** Per skill; once at the end.
- **Canvas:** 7

## 2026-11-21: Matt Pocock's grilling is adapted into the grill role; writing-for-agents is referenced

- **Context:** Dependence on Matt Pocock's skills (Q15).
- **Decision:** The grill role skeleton carries an adapted `grilling`, so every skillset's grill skill has it; `writing-for-agents` is recommended and summarised in `skillset-conventions`, not copied.
- **Reason:** Every skillset needs a grill skill; duplicating `writing-for-agents` would drift.
- **Alternatives:** Require Matt Pocock's skills to be installed.
- **Canvas:** 5, 8

## 2026-11-21: Users include other instructors; the Changemaker build is the first test

- **Context:** Who uses the builder, and what it is tested on (Q13, Q14).
- **Decision:** Personas include instructors with domain expertise but no skill-writing experience. The first real run is the Changemaker skillset; a compact record of it goes to `examples/`.
- **Reason:** Dogfooding on a real skillset tests more than a reconstruction of an existing one.
- **Alternatives:** Maintainer only; reconstructing Agentic Course Creation as an example.
- **Canvas:** 2, 10

## 2026-11-21: The printed canvas is generated from the template

- **Context:** The printed canvases of the first two skillsets were made separately from their templates (Q12).
- **Decision:** `render_canvas.py --print` makes the A4 SVG (and `--pdf` the PDF) from the template; the SVG records the template's hash so a check sees when it is stale.
- **Reason:** Uniform layout, one source, no "the canvas exists three times" rule.
- **Alternatives:** Hand-drawn SVG per skillset.
- **Canvas:** 7, 8

## 2026-11-21: The core is distributed as copies with a lock file

- **Context:** How skillsets get the core (Q11).
- **Decision:** Copies, recorded in `.skillset-core.json` with hashes; verbatim and adapted modes; `/sync-core` updates. The core lives in the reference skill `skillset-core`, so it is installed with the builder.
- **Reason:** Each skillset stays installable with one command; submodules work badly with skill installers.
- **Alternatives:** Git submodule; a separate core plugin.
- **Canvas:** 7

## 2026-11-21: Design files live in the skillset repository under design/

- **Context:** Where the builder's working files go (Q10).
- **Decision:** `design/` in the skillset repository; `/setup-skillset` still asks about visibility.
- **Reason:** No participant data in them, and the derivation helps anyone adapting the skillset.
- **Alternatives:** A separate private repository.
- **Canvas:** 7

## 2026-11-21: Skill list of the builder

- **Context:** Q9.
- **Decision:** `setup-skillset`, `ask-builder`, `show-canvas` (core), `grill-practice`, `map-sources`, `design-canvas`, `to-skill-map`, `draft-skill`, `dry-run`, `review-skillset`, `skillset-retro`, `sync-core`; references `skillset-conventions`, `skillset-core`; maintainer `release-skillset`. Canvas and skill map stay separate, and so do dry run and review.
- **Reason:** Each is a separate decision with its own stop point, as in the sibling skillsets.
- **Alternatives:** Merging design-canvas with to-skill-map, or dry-run with review.
- **Canvas:** 9

## 2026-11-21: Language rule, retrofit and release skill

- **Context:** Q6–Q8.
- **Decision:** Content and conversation in the skillset's language, identifiers and maintainer files in English. The two existing skillsets adopt the core after the Changemaker skillset. A generic `release-skillset` is part of the core.
- **Reason:** Tool-friendly identifiers, users read their own language; retrofit after a third test; one release procedure.
- **Alternatives:** Everything translated; retrofit now.
- **Canvas:** 7, 11

## 2026-11-21: One canvas grammar, sources mapped explicitly, dry run mandatory

- **Context:** Q3–Q5.
- **Decision:** The canvas grammar is binding (owners, columns, log, open questions); block count and names are free, and a block may point to a domain canvas. Sources are read and licensed in their own step. A dry run on an example case is mandatory before release.
- **Reason:** One renderer for all, no bent domain methods; traceable rules; authors cannot test their own skills by reading them.
- **Alternatives:** Adopting a domain canvas's structure as is; no source step; optional dry run.
- **Canvas:** 5, 7, 8

## 2026-11-21: A builder with a shared core, as its own repository

- **Context:** The third skillset of the same kind (Q1, Q2).
- **Decision:** `steffen74/agentic-skillset-builder`: process skills that create independent skillset repositories, plus a shared core synced into each.
- **Reason:** Each skillset stays installable on its own, with its own users and language, while shared files stop drifting.
- **Alternatives:** Only process skills without a core; one plugin with all skillsets as extensions.
- **Canvas:** 1, 3
