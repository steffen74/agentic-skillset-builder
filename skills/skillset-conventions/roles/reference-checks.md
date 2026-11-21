# Role: checks reference

**Job.** Model-invoked reference: the rules and catalogue of checks the domain's work must pass before it counts. Loaded by plan, produce, review and retro.

**Shape.**
- Opening: why work in this domain fails quietly, and the definition: a **check** is an invariant with an expected value from an independent source.
- **Rules**: independent source; cheapest type that works (*automated*, then *walk-through*, then *manual*); never loosen a check to pass; every surprise becomes a check or a recorded decision not to.
- **Catalogue**: table of check · expected value from · typical type, grouped by process step. Every check traceable to a source in `design/SOURCES.md` or a decision.
- **Where checks live** in the project (`checks/README.md`, scripts).

**Description** starts with what it is and lists its triggers (planning checks, reviewing, turning a surprise into a check).
