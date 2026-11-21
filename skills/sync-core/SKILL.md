---
name: sync-core
description: "Bring the core files (canvas renderer, show-canvas, convention check, release skill, templates) of a skillset repository up to date with the builder, or adopt the core in an existing skillset. Type the repository path after the command."
disable-model-invocation: true
---

# Sync core

Keep the files every skillset shares identical where they should be identical, and carry core changes into adapted copies. Load `skillset-core`; its `scripts/core_sync.py` does the bookkeeping. Target: the repository typed with the command, otherwise the current one.

## 1. Status

Run `core_sync.py status --target <repo>`. Without `.skillset-core.json`, the skillset has not adopted the core yet: go to step 3.

Done when every core file has a state: *ok*, *update*, *adapt*, *local-change*, *conflict*, *new*, *missing* or *skipped*.

## 2. Bring it up to date

- **update**: `core_sync.py apply` copies the new version of verbatim files that were not changed locally.
- **adapt**: carry the printed diff of the master into the adapted file, in the skillset's language and vocabulary, then `core_sync.py record <path>`.
- **local-change**: someone edited a verbatim file in the skillset. Read the change. If it is an improvement for every skillset, move it into the builder's core (see `skillset-core`, *Changing the core*) and sync from there; otherwise restore the core version. **Stop point**: the maintainer picks.
- **conflict**: merge by hand, showing both changes; then `record`.
- **new**: `core_sync.py init --target <repo> --setup <setup skill>` copies new core files (it never overwrites).
- **missing**: restore it, or `skip` it with a decision in `design/DECISIONS.md` (or the skillset's decision log).

Then run `python3 scripts/check_skillset.py` in the target.

## 3. Adopt the core in an existing skillset

For a skillset built before the builder existed:

1. `core_sync.py init --target <repo> --setup <setup skill>`. Files that already exist are reported, not overwritten.
2. For each reported file, compare it with the core master. Identical: `record` it. Same role but different (for example `render_canvas.py` of an older version, a signal log called `LOG.md`): **stop point**, either replace it with the core version and `record`, keep it and `skip` the core file, or merge.
3. Add the `## Agentic skillset builder` section to the target's `AGENTS.md` (format in `skillset-conventions/LAYOUT.md`), generate the printed canvas with the core renderer if the old one was drawn by hand, and add a `CHANGELOG.md` entry.

## 4. Finish

Summarise what changed per file, with the core version before and after. Changes to `skills/` or `canvas/` need a release of the target skillset (`release-skillset`); say so.

Done when `core_sync.py status` reports only *ok* and *skipped*, and `check_skillset.py` passes its `core` check.
