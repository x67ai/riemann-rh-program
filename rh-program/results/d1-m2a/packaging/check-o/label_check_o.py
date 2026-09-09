#!/usr/bin/env python3
"""CHECK-O step 6: the label check and the import discipline (Job 2's own script).

(1) The exact SPEC §3.7 short label, "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3",
    must be present in every file where a label appears.
(2) "fully machine-checked" must never be used AS A LABEL.  Every occurrence is reported with
    its line, and classified: PROHIBITION (the sentence forbids the phrase) vs USE.
(3) Challenge/DBN.lean and ChallengeDeps/DBN*.lean must contain no `import Zeta23…`.
(4) Solution/DBN.lean must never import Challenge.DBN.
Usage: label_check_o.py <lean-tree> <rh-program dir>
"""
import os, re, sys

TREE, PROG = sys.argv[1], sys.argv[2]

LABEL = "kernel-checked modulo H1, H2 (H2-B, H2-A, H-TAIL), H3"
BAD = "fully machine-checked"

TARGETS = [
    (os.path.join(TREE, "comparator/ChallengeDeps/DBN.lean"), "comparator/ChallengeDeps/DBN.lean"),
    (os.path.join(TREE, "comparator/ChallengeDeps/DBN/Instance02.lean"), "comparator/ChallengeDeps/DBN/Instance02.lean"),
    (os.path.join(TREE, "comparator/Challenge/DBN.lean"), "comparator/Challenge/DBN.lean"),
    (os.path.join(TREE, "comparator/Solution/DBN.lean"), "comparator/Solution/DBN.lean"),
    (os.path.join(TREE, "comparator/PrintAxioms/DBN.lean"), "comparator/PrintAxioms/DBN.lean"),
    (os.path.join(TREE, "comparator/config-dbn.json"), "comparator/config-dbn.json"),
    (os.path.join(PROG, "lean/README.md"), "lean/README.md"),
    (os.path.join(PROG, "lean/formalization.yaml"), "lean/formalization.yaml"),
    (os.path.join(PROG, "results/d1-m2a/packaging/FIDELITY.md"), "packaging/FIDELITY.md"),
]

print("CHECK-O step 6 — label check (Job 2's own script)")
print("exact label sought: %r" % LABEL)
print()
print("%-46s %6s %10s" % ("file", "label", "'fully...'"))
print("(config-dbn.json is a machine config and carries no label text: exempt, vacuous)")
fail = []
occurrences = []
for path, rel in TARGETS:
    text = open(path, encoding="utf-8").read()
    # normalize whitespace (incl. line breaks) so a wrapped label still counts
    flat = re.sub(r"\s+", " ", text)
    nl = flat.count(LABEL)
    nb = text.count(BAD)
    print("%-46s %6d %10d" % (rel, nl, nb))
    if nl == 0 and rel != "comparator/config-dbn.json":
        fail.append("label absent from " + rel)
    for k, line in enumerate(text.split("\n"), 1):
        if BAD in line:
            occurrences.append((rel, k, line.strip()))
print()
print("every occurrence of %r, classified:" % BAD)
PROHIB = re.compile(r"never|forbid|not\b|no\b|NEVER", re.I)
uses = 0
for rel, k, line in occurrences:
    # look at the 40 characters before the phrase
    idx = line.find(BAD)
    lead = line[max(0, idx - 60):idx]
    kind = "PROHIBITION" if PROHIB.search(lead) else "USE  <-- NOT PERMITTED"
    if kind.startswith("USE"): uses += 1
    print("  %-11s %s:%d: …%s%s…" % (kind, rel, k, lead[-50:], BAD))
if uses:
    fail.append("%d use(s) of %r as a label" % (uses, BAD))
print()
print("occurrences: %d; all prohibitions: %s" % (len(occurrences), uses == 0))

print()
print("import discipline:")
def strip_c(s):
    out, i, depth, n = [], 0, 0, len(s)
    while i < n:
        if s.startswith("/-", i): depth += 1; out.append("  "); i += 2; continue
        if s.startswith("-/", i) and depth: depth -= 1; out.append("  "); i += 2; continue
        if depth: out.append("\n" if s[i] == "\n" else " "); i += 1; continue
        if s.startswith("--", i):
            j = s.find("\n", i); j = n if j < 0 else j
            out.append(" " * (j - i)); i = j; continue
        out.append(s[i]); i += 1
    return "".join(out)

def imports(path):
    return re.findall(r"(?m)^import\s+(\S+)", strip_c(open(path, encoding="utf-8").read()))
for rel in ["comparator/Challenge/DBN.lean", "comparator/ChallengeDeps/DBN.lean",
            "comparator/ChallengeDeps/DBN/Instance02.lean"]:
    imp = imports(os.path.join(TREE, rel))
    bad = [i for i in imp if i == "Zeta23" or i.startswith("Zeta23.")]
    print("  %-46s imports %s; Zeta23 imports: %s" % (rel, imp, bad or "none"))
    if bad: fail.append("%s imports %s" % (rel, bad))
    # also: the raw text must contain no `import Zeta23` at all
    txt = strip_c(open(os.path.join(TREE, rel), encoding="utf-8").read())
    for k, line in enumerate(txt.split("\n"), 1):
        if re.match(r"\s*import\s+Zeta23", line):
            fail.append("%s:%d %s" % (rel, k, line.strip()))
srel = "comparator/Solution/DBN.lean"
simp = imports(os.path.join(TREE, srel))
sbad = [i for i in simp if i == "Challenge" or i.startswith("Challenge.")]
print("  %-46s imports %s; Challenge imports: %s" % (srel, simp, sbad or "none"))
if sbad: fail.append("%s imports the challenge module %s" % (srel, sbad))

print()
if fail:
    print("RESULT: FAIL")
    for f in fail: print("  - " + f)
    sys.exit(1)
print("RESULT: CLEAN")
