# Contributing

Feedback from building and using skillsets is the most valuable contribution. Useful issues describe:

- a problem in a skillset that the builder let through (no skeleton, check or dry-run question caught it), with what happened,
- a builder skill that led the agent astray, with what happened and what you expected,
- a file that two skillsets need in the same form, as a candidate for the core.

`/skillset-retro` drafts such issues for you, including the proposed change as a diff.

## Conventions

The conventions this builder teaches apply to the builder itself: see `skills/skillset-conventions/`. In short:

- Follow Matt Pocock’s `writing-for-agents`: short, ordered steps with completion criteria, reference behind pointers, leading words, positive instructions.
- User-invoked skills set `disable-model-invocation: true` and have a one-line human-facing description. Reference skills keep a model-facing description with their triggers.
- Every maintainer decision is an explicit **stop point**: the agent recommends, the maintainer decides, the decision is logged.
- Role skeletons in `skills/skillset-conventions/roles/` are the single source for what a role does; builder skills point to them.
- Core files live only in `skills/skillset-core/files/`; this repository's own copies are synced with `core_sync.py` like any other skillset’s.
- Run `python3 scripts/check_skillset.py` before every pull request.
