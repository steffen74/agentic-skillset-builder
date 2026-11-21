# Contributing

Feedback from real use is the most valuable contribution. Useful issues describe:

- a moment where the work went wrong and no check or skill caught it, with what happened,
- a situation where a skill led the agent astray, with what happened and what you expected,
- a canvas block that was unclear or missing in practice.

{{The retro skill}} drafts such issues for you, including the proposed change to a skill.

## Conventions for skills

This skillset follows the conventions of the [Agentic Skillset Builder](https://github.com/steffen74/agentic-skillset-builder) (`skillset-conventions`): canvas grammar, owners and stop points, skill roles, the language rule, and Matt Pocock’s `writing-for-agents`. In short:

- User-invoked skills set `disable-model-invocation: true` and have a one-line human-facing description. Reference skills keep a model-facing description with their triggers.
- Every decision the user owns is an explicit **stop point**: the agent recommends, the user decides, the decision is logged.
- Skills read and write the files named in the skillset’s section of the project’s `AGENTS.md`; they do not invent new locations.
- Language: {{language}} for content; English for skill names, file names and maintainer files.
- Run `python3 scripts/check_skillset.py` before every pull request.
