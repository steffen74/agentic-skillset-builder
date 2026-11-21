---
name: setup-skillset
description: "Start a new agentic skillset: create its repository (locally, optionally on GitHub or as a ZIP), copy the core, scaffold the design files. Run once per skillset before the other builder skills."
disable-model-invocation: true
---

# Set up a skillset

Create the **skillset repo** and the files every other builder skill reads. Load `skillset-conventions` (and its `LAYOUT.md`) and `skillset-core`. Explore, present, confirm, then write.

## 1. Explore

- What the user named: the kind of work, a handbook or other source, an existing repository to retrofit.
- The environment, before offering any target: is `git` installed; is `gh` installed and signed in (`gh api user --jq .login`), and as whom; is the working directory writable; is the user inside an existing git repository.
- Existing skillsets the user maintains (other `agentic-*` repositories, if visible): their naming, owner, and language, so the new one fits.

## 2. Ask

Take the sections in order, one answer each, leading with your recommendation. Skip what exploration settled.

- **A. Name.** The skillset's display name, the repository name (`agentic-<domain>` in kebab case), the plugin name (same as the repository), and the setup skill's name in the project (`setup-<noun>`, e.g. `setup-model`).
- **B. Language.** The language of content and conversation (identifiers stay English; see `LANGUAGE.md`).
- **C. Target.** Offer only the options exploration showed to work:
  1. **Local git repository** in a new folder (`git init`, first commit, no remote).
  2. **Local and on GitHub**: owner, name, visibility. Recommend **private** until the first dry run passes; `/review-skillset` proposes making it public.
  3. **ZIP** of the folder, for users without git.
  Every option builds locally first; GitHub and ZIP are ways out. With option 1, the GitHub question returns at the first release.
- **D. Sources.** Where the domain logic comes from (handbook URL, documents, existing canvases, own practice). A list is enough; `/map-sources` does the rest. Check now whether each URL is reachable from this environment, and say which are not.
- **E. Example case.** A realistic case for dry runs (a fictitious project the skillset's users would bring). One sentence is enough; `/grill-practice` sharpens it.

**Stop point**: summarise A–E and get a yes before writing anything.

## 3. Write

1. Create the folder and copy [`templates/repo/`](templates/repo/) into it (`gitignore` becomes `.gitignore`). Fill every `{{placeholder}}` you can from A–E; leave the rest visible for later skills, which fill them as the design settles.
2. Copy [`templates/design/`](templates/design/) to `design/`, plus `DECISIONS.md` and `SIGNALS.md` from the `skillset-core` masters. Fill the canvas header, block 1 with the one-sentence practice as a draft, block 5 with the source list from D.
3. Run `core_sync.py init --target <repo> --setup <setup skill>` (see `skillset-core`). Adapt the copied `adapted` files to the language from B, then `core_sync.py record` them.
4. Create `examples/<case>/README.md` with the case from E.
5. Record A–C in `design/DECISIONS.md`.
6. `git init`, `git add -A`, first commit (`chore: scaffold skillset with the Agentic Skillset Builder`). For target 2: `gh repo create <owner>/<name> --<visibility> --source . --push`; if that is refused, tell the user, ask them to create the empty repository, and push into it. For target 3: write the ZIP next to the folder.

`python3 scripts/check_skillset.py` fails on `printed-canvas` until `/design-canvas` exists; everything else in its output names what is missing.

Done when the repository exists at the chosen target, the user has its path or URL, and `design/SKILLSET-CANVAS.md` has its header filled. Suggest `/grill-practice`.
