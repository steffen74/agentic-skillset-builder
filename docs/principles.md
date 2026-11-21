# Principles

Eight habits the builder encodes, and passes on to every skillset it builds.

## 1. The agent does the legwork, the maintainer decides

Reading a handbook, comparing canvases, checking licenses, drafting skills, running dry runs: the agent’s job. Which practice the skillset serves, who it is for, which decisions stay with its users, what counts as done: put to the maintainer with a recommendation.

## 2. Practice before canvas, canvas before skills

Start from the work people do and where agents fail them, derive outcomes and their evidence, then design the canvas, and only then the skills. A skill that serves no outcome is cut; an outcome that no skill reaches is a gap.

## 3. The judgement boundary is a design decision

For every decision in the domain, the canvas says who owns it. A skill that lets the agent take a decision the user owns is the skillset equivalent of leakage: it runs without errors and quietly makes the result worse. Every user-owned decision is a stop point.

## 4. Every rule has a source

Domain rules in a skill trace to a source in `design/SOURCES.md` or to a decision in `design/DECISIONS.md`. Sources come with their license, and the license decides what may be copied, adapted or only referenced.

## 5. You cannot check your own skills by reading them

The author knows every missing step. A **dry run** on an example case, by a runner that knows only the skills and a persona that knows only what a user knows, finds the stalls, guesses and overreach that reading does not.

## 6. One grammar, one core

All skillsets share the canvas grammar, the skill roles and the core files. Users of several skillsets recognise them; improvements to the core reach every skillset through `/sync-core`; nothing shared is maintained by hand in two places.

## 7. Every surprise becomes a check

When a dry run or a real user finds a problem, fix it, then ask why no check caught it. The answer becomes a check in the skillset, a rule in the builder, or a change to the core, so the next skillset does not repeat it.

## 8. The design is part of the skillset

Canvas, personas, sources, skill map, decisions and signals live in `design/` of the skillset repository. Anyone adapting the skillset can see why it is the way it is.

## Related work

- **Matt Pocock’s skills** ([mattpocock/skills](https://github.com/mattpocock/skills)): the skill structure, `writing-for-agents` for the writing, `grilling` for the interviews, `code-review` for two-axis reviews.
- **Canvas methods** such as the Business Model Canvas (Osterwalder and Pigneur) and its social and lean variants: the one-page, block-by-block form that the skillset canvases borrow, with owners and checks added.
- **Backward design** (Wiggins and McTighe): outcomes and evidence before content, applied to skills.
