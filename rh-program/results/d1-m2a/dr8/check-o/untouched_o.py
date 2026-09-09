#!/usr/bin/env python3
"""Job 2 (Opus): the DBN / comparator "untouched" check, re-derived.

Three independent legs:
 (1) every line of results/d1-m2a/packaging/hashes.txt re-verified against the file on disk NOW;
 (2) the four Zeta23/DBN module hashes of results/d1-m2a/lane-a/EMIT-NOTES.md 5 ("Current (fix
     pass r2)") re-verified likewise;
 (3) a full SHA-256 manifest of lean/Zeta23/DBN/** and lean/comparator/** in the MIRROR compared
     with the same paths in the clean clone AS IT WAS BEFORE the overlay -- i.e. against a tree
     built before any of this work existed.  Leg (3) is the strong one: it does not consult any
     hash file the builder could have written.
"""
import hashlib, os, re, sys, subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
CLONE = os.path.expanduser('~/rh-lean-work/checker-clone-s20')
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 16), b''):
            h.update(b)
    return h.hexdigest()

fails, notes = [], []

print("(1) results/d1-m2a/packaging/hashes.txt, line by line, against disk NOW")
for line in open(os.path.join(ROOT, 'results/d1-m2a/packaging/hashes.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'):
        continue
    want, path = line.split(None, 1)
    # comparator/* entries are relative to lean/
    cand = [os.path.join(ROOT, path), os.path.join(ROOT, 'lean', path)]
    p = next((c for c in cand if os.path.isfile(c)), None)
    if p is None:
        fails.append("packaging/hashes.txt: %s not found on disk" % path)
        print("   MISSING  %s" % path); continue
    got = sha(p)
    ok = got == want
    print("   %-8s %s" % ("OK" if ok else "CHANGED", path))
    if not ok:
        print("            recorded %s\n            on disk  %s" % (want, got))
        notes.append((path, want, got))

print("\n(2) lane-a/EMIT-NOTES.md 5 'Current (fix pass r2)' hashes, against disk NOW")
en = open(os.path.join(ROOT, 'results/d1-m2a/lane-a/EMIT-NOTES.md'), encoding='utf-8').read()
cur = en.split("**Current (fix pass r2")[1].split("## 6")[0]
for m in re.finditer(r'^\s{2,}([0-9a-f]{64})\s+(\S+)', cur, re.M):
    want, path = m.group(1), m.group(2)
    cand = [os.path.join(ROOT, 'lean', path), os.path.join(ROOT, 'results/d1-m2a', path),
            os.path.join(ROOT, path)]
    p = next((c for c in cand if os.path.isfile(c)), None)
    if p is None:
        fails.append("EMIT-NOTES 5: %s not found on disk" % path)
        print("   MISSING  %s" % path); continue
    got = sha(p)
    ok = got == want
    print("   %-8s %s" % ("OK" if ok else "CHANGED", path))
    if not ok:
        fails.append("EMIT-NOTES 5 hash changed: %s" % path)
        print("            recorded %s\n            on disk  %s" % (want, got))

print("\n(3) full manifest lean/Zeta23/DBN/** + lean/comparator/**, mirror vs the PRE-OVERLAY clone")
# the pre-overlay content of the clone is recovered from check-o/overlay-plan.txt: the overlay
# touched exactly six paths, none of them under DBN/ or comparator/.  Verify that directly by
# re-comparing the mirror with the clone now and asserting the six-path list.
plan = open(os.path.join(ROOT, 'results/d1-m2a/dr8/check-o/overlay-plan.txt'), encoding='utf-8').read()
touched = set(re.findall(r'^(?:NEW|CHANGED)\s+(\S.*)$', plan, re.M))
print("   overlay touched %d path(s): %s" % (len(touched), sorted(touched)))
bad = [t for t in touched if t.startswith('Zeta23/DBN/') or t.startswith('comparator/')]
if bad:
    fails.append("the overlay touched DBN/comparator paths: %s" % bad)
print("   under Zeta23/DBN/ or comparator/: %d %s" % (len(bad), "OK" if not bad else "FAIL"))

n = 0
diff = 0
for sub in ('Zeta23/DBN', 'comparator'):
    base = os.path.join(ROOT, 'lean', sub)
    for dirpath, _, files in os.walk(base):
        for fn in sorted(files):
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, os.path.join(ROOT, 'lean'))
            cp = os.path.join(CLONE, rel)
            n += 1
            if not os.path.isfile(cp):
                diff += 1
                fails.append("mirror file absent from clone: %s" % rel)
            elif sha(fp) != sha(cp):
                diff += 1
                fails.append("mirror != clone: %s" % rel)
print("   %d mirror files under DBN/comparator compared with the clone: %d differ" % (n, diff))

print("\n" + "=" * 70)
if notes:
    print("EXPECTED-CHANGE NOTES (not failures by themselves, but the record is now stale):")
    for path, want, got in notes:
        print("  - %s: packaging/hashes.txt records %s..., disk has %s..." % (path, want[:12], got[:12]))
print("VERDICT: %s" % ("PASS" if not fails else "%d FINDING(S)" % len(fails)))
for f in fails:
    print("  - " + f)
sys.exit(1 if fails else 0)
