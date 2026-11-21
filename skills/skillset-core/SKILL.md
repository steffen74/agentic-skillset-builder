---
name: skillset-core
description: The core files every agentic skillset shares (show-canvas with the canvas renderer, the convention check, the release skill, decision and signal templates) and the script that copies and syncs them. Use when setting up a skillset repository, syncing its core, or changing a file that exists in more than one skillset.
---

# Skillset core

The **core** is the set of files that every skillset built with this builder carries in identical or adapted form. This folder is its single source: [`MANIFEST.json`](MANIFEST.json) lists each file, where it goes in a skillset repository and its mode; [`files/`](files/) holds the masters; [`scripts/core_sync.py`](scripts/core_sync.py) copies and syncs them.

| Core file | Goes to | Mode | Role |
|---|---|---|---|
| `show-canvas.SKILL.md` | `skills/show-canvas/SKILL.md` | adapted | Show the project's canvas as a page |
| `render_canvas.py` | `skills/show-canvas/scripts/` | verbatim | Canvas as HTML page, or as printable A4 SVG/PDF (`--print`, `--pdf`); labels in `en` and `de` |
| `check_skillset.py` | `scripts/` | verbatim | Convention checks for a skillset repository |
| `release-skillset.SKILL.md` | `.claude/skills/release-skillset/SKILL.md` | verbatim | Maintainer skill: version bump, changelog, printed canvas, tag, release |
| `DECISIONS.md`, `SIGNALS.md` | `skills/<setup skill>/templates/` | adapted | Templates for the project's decision log and signal log |

**Modes.** *Verbatim* files are copied byte for byte; a local change is a finding, and the fix goes into the core here, then out to every skillset with `/sync-core`. *Adapted* files are translated into the skillset's language or adapted to its vocabulary (a skillset may call its signal log `LOG.md`); when the master changes, `core_sync.py status` prints the master's diff so the change can be carried over by hand.

## Using the script

```
python3 <this skill's dir>/scripts/core_sync.py init   --target <repo> --setup <setup skill name>
python3 <this skill's dir>/scripts/core_sync.py status --target <repo>
python3 <this skill's dir>/scripts/core_sync.py apply  --target <repo>
python3 <this skill's dir>/scripts/core_sync.py record --target <repo> <path> …
python3 <this skill's dir>/scripts/core_sync.py skip   --target <repo> <path> …
```

`init` never overwrites an existing file. It writes `.skillset-core.json` (the lock: core version, and per file the hash of master and target at the last sync) and keeps the masters of adapted files in `.skillset-core/masters/` for the next diff. Both belong in the skillset repository's git history.

## Changing the core

A file belongs in the core when at least two skillsets need it and it says nothing domain-specific. To change one: edit the master in `files/`, bump `version` in `MANIFEST.json` (minor for new behaviour, patch for fixes), add a `CHANGELOG.md` entry, then run `/sync-core` on this repository itself and on every other skillset. A change made directly in a skillset's copy of a verbatim file shows up as a failed `core` check there.
