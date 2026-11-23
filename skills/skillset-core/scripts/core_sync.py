#!/usr/bin/env python3
"""Copy the core of the agentic skillset builder into a skillset repository and keep it in sync.

  core_sync.py init   --target DIR --setup setup-x   # copy missing core files, write .skillset-core.json
  core_sync.py status --target DIR                   # what changed in the core, what changed locally
  core_sync.py apply  --target DIR                   # update verbatim files that were not changed locally
  core_sync.py record --target DIR PATH [PATH ...]   # mark adapted files as synced after adapting them
  core_sync.py skip   --target DIR PATH [PATH ...]   # this skillset does not use a core file (record why in DECISIONS)

Modes (from MANIFEST.json next to this script's folder):
  verbatim  copied byte for byte; a local change is a finding, the fix goes into the builder's core
  adapted   translated or adapted per skillset; when the core master changes, `status` prints the
            master's diff so the agent can carry the change into the adapted file, then `record` it

The lock file .skillset-core.json in the target records, per file, the sha of the core master and of the
target file at the last sync. Masters of adapted files are kept in .skillset-core/masters/ so the next
diff has something to compare with. Standard library only.
"""
import argparse
import difflib
import hashlib
import json
import pathlib
import shutil
import sys

CORE = pathlib.Path(__file__).resolve().parent.parent
LOCK = ".skillset-core.json"
MASTERS = pathlib.Path(".skillset-core/masters")


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()[:12]


def sha(path):
    return sha_bytes(path.read_bytes()) if path.exists() else None


def manifest():
    return json.loads((CORE / "MANIFEST.json").read_text(encoding="utf-8"))


def load_lock(target):
    path = target / LOCK
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def save_lock(target, lock):
    lock["files"].sort(key=lambda f: f["path"])
    (target / LOCK).write_text(json.dumps(lock, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def master_copy(target, entry):
    return target / MASTERS / pathlib.Path(entry["core"]).name


def snapshot(target, entry):
    if entry["mode"] == "adapted":
        dest = master_copy(target, entry)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CORE / entry["core"], dest)


def record_entry(target, entry, path):
    return {"core": entry["core"], "path": path, "mode": entry["mode"],
            "core_sha": sha(CORE / entry["core"]), "sha": sha(target / path)}


def cmd_init(a):
    target = a.target
    m = manifest()
    lock = load_lock(target) or {"core_version": m["version"], "source": m["source"], "setup": a.setup, "files": []}
    known = {f["core"] for f in lock["files"]}
    for entry in m["files"]:
        if entry["core"] in known:
            continue
        path = entry["path"].replace("{setup}", lock.get("setup") or a.setup)
        dest = target / path
        if dest.exists():
            lock["files"].append({"core": entry["core"], "path": path, "mode": entry["mode"],
                                  "core_sha": None, "sha": None})
            print(f"exists, not overwritten: {path} (compare it with the core, then `record` or `skip` it)")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(CORE / entry["core"], dest)
        snapshot(target, entry)
        lock["files"].append(record_entry(target, entry, path))
        note = " (adapt to the skillset's language, then `record` it)" if entry["mode"] == "adapted" else ""
        print(f"copied {entry['mode']}: {path}{note}")
    lock["core_version"] = m["version"]
    save_lock(target, lock)
    print(f"wrote {LOCK} (core {m['version']})")


def status(target):
    m = manifest()
    lock = load_lock(target)
    if lock is None:
        sys.exit(f"{target / LOCK} not found: run `init` first.")
    by_core = {f["core"]: f for f in lock["files"]}
    rows = []
    for entry in m["files"]:
        f = by_core.get(entry["core"])
        if f is None:
            rows.append((entry, None, "new", "new core file: `init` copies it"))
            continue
        if f["mode"] == "skipped":
            rows.append((entry, f, "skipped", "not used by this skillset"))
            continue
        core_changed = sha(CORE / entry["core"]) != f["core_sha"]
        local = target / f["path"]
        local_changed = sha(local) != f["sha"]
        if f.get("sha") is None and f.get("core_sha") is None:
            state, note = "adopt", "existing file not yet compared with the core: replace and `record`, merge and `record`, or `skip`"
        elif not local.exists():
            state, note = "missing", "file deleted: restore with `init` after removing it from the lock, or `skip`"
        elif f["mode"] == "verbatim":
            state, note = {(False, False): ("ok", ""),
                           (True, False): ("update", "`apply` copies the new core version"),
                           (False, True): ("local-change", "move the change into the builder's core or restore the file"),
                           (True, True): ("conflict", "core and local file both changed: merge by hand, then `record`")}[
                (core_changed, local_changed)]
        else:
            state, note = ("adapt", "core master changed: carry the diff below into the adapted file, then `record`") \
                if core_changed else ("ok", "")
        rows.append((entry, f, state, note))
    return lock, rows


def cmd_status(a):
    lock, rows = status(a.target)
    print(f"core in target: {lock.get('core_version')} · core here: {manifest()['version']}")
    for entry, f, state, note in rows:
        path = f["path"] if f else entry["path"]
        print(f"{state:13} {path}" + (f"  - {note}" if note else ""))
        if state == "adapt":
            old = master_copy(a.target, entry)
            old_lines = old.read_text(encoding="utf-8").splitlines(keepends=True) if old.exists() else []
            new_lines = (CORE / entry["core"]).read_text(encoding="utf-8").splitlines(keepends=True)
            sys.stdout.writelines(difflib.unified_diff(old_lines, new_lines, f"core (last sync)/{entry['core']}",
                                                       f"core (now)/{entry['core']}"))
    if any(state not in ("ok", "skipped") for _, _, state, _ in rows):
        sys.exit(1)


def cmd_apply(a):
    lock, rows = status(a.target)
    by_path = {f["path"]: f for f in lock["files"]}
    for entry, f, state, _ in rows:
        if state == "update":
            shutil.copyfile(CORE / entry["core"], a.target / f["path"])
            by_path[f["path"]].update(record_entry(a.target, entry, f["path"]))
            print(f"updated: {f['path']}")
    lock["core_version"] = manifest()["version"]
    save_lock(a.target, lock)
    print("Run `status` again for files that need adapting or a merge.")


def cmd_record(a, skip=False):
    lock = load_lock(a.target)
    if lock is None:
        sys.exit(f"{a.target / LOCK} not found: run `init` first.")
    entries = {e["core"]: e for e in manifest()["files"]}
    for path in a.paths:
        f = next((f for f in lock["files"] if f["path"] == path), None)
        if f is None:
            sys.exit(f"{path} is not in {LOCK}.")
        entry = entries[f["core"]]
        if skip:
            f.update({"mode": "skipped", "core_sha": sha(CORE / entry["core"]), "sha": None})
            master_copy(a.target, entry).unlink(missing_ok=True)
        else:
            f.update(record_entry(a.target, entry, path))
            snapshot(a.target, entry)
        print(f"{'skipped' if skip else 'recorded'}: {path}")
    save_lock(a.target, lock)


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in ("init", "status", "apply", "record", "skip"):
        s = sub.add_parser(name)
        s.add_argument("--target", type=pathlib.Path, default=pathlib.Path.cwd())
        if name == "init":
            s.add_argument("--setup", required=True, help="name of the skillset's setup skill, e.g. setup-course")
        if name in ("record", "skip"):
            s.add_argument("paths", nargs="+")
    a = p.parse_args()
    a.target = a.target.resolve()
    {"init": cmd_init, "status": cmd_status, "apply": cmd_apply,
     "record": cmd_record, "skip": lambda a: cmd_record(a, skip=True)}[a.cmd](a)


if __name__ == "__main__":
    main()
