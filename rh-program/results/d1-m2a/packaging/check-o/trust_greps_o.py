#!/usr/bin/env python3
"""CHECK-O step 5: trust greps, re-run strictly and independently (Job 2's own script;
it shares no code with packaging/trust_greps.py).

Comments and docstrings are stripped FIRST (nested `/- … -/`, `/-- … -/`, `--` to end of line,
and `/-! … -/` section markers, all of which the nesting-aware stripper handles), then the
remaining CODE is searched for the eight patterns of KICKSTART 10(j) as whole words, plus four
extra patterns a skeptic would want (`sorryAx`, `native_decide`'s kernel witness `ofReduceBool`
is already in the eight, `trust_me`, `lean_evalConst`, `#eval`).

Scope: the six comparator DBN files and every module under Zeta23/DBN/.
Usage: trust_greps_o.py <lean-tree>
"""
import os, re, sys

TREE = sys.argv[1]

FILES = ["comparator/ChallengeDeps/DBN.lean",
         "comparator/ChallengeDeps/DBN/Instance02.lean",
         "comparator/Challenge/DBN.lean",
         "comparator/Solution/DBN.lean",
         "comparator/PrintAxioms/DBN.lean",
         "comparator/config-dbn.json"]
for root, _, fs in os.walk(os.path.join(TREE, "Zeta23/DBN")):
    for f in sorted(fs):
        if f.endswith(".lean"):
            FILES.append(os.path.relpath(os.path.join(root, f), TREE))
FILES = sorted(set(FILES))

PATTERNS = ["axiom", "native_decide", "unsafe", "implemented_by", "extern", "opaque",
            "sorry", "ofReduceBool", "sorryAx", "trust_me", "lean_evalConst", "#eval"]

def strip_comments_keep_lines(s):
    """blank out comment characters but keep newlines, so line numbers survive."""
    out, i, depth, n = [], 0, 0, len(s)
    while i < n:
        c = s[i]
        if s.startswith("/-", i):
            depth += 1; out.append("  "); i += 2; continue
        if s.startswith("-/", i) and depth:
            depth -= 1; out.append("  "); i += 2; continue
        if depth:
            out.append("\n" if c == "\n" else " "); i += 1; continue
        if s.startswith("--", i):
            j = s.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i)); i = j; continue
        out.append(c); i += 1
    return "".join(out)

raw = {p: 0 for p in PATTERNS}
codehits = {p: [] for p in PATTERNS}
for rel in FILES:
    path = os.path.join(TREE, rel)
    text = open(path, encoding="utf-8").read()
    code = strip_comments_keep_lines(text) if rel.endswith(".lean") else text
    for p in PATTERNS:
        rx = re.compile(r"(?<![A-Za-z0-9_])" + re.escape(p) + r"(?![A-Za-z0-9_])")
        raw[p] += len(rx.findall(text))
        for k, line in enumerate(code.split("\n"), 1):
            for _ in rx.finditer(line):
                codehits[p].append((rel, k, line.strip()))

print("CHECK-O step 5 — trust greps, Job 2's own script, comments stripped first")
print("files scanned: %d (%d comparator DBN, %d Zeta23/DBN modules)"
      % (len(FILES), 6, len(FILES) - 6))
print()
print("%-16s %10s %10s" % ("pattern", "raw(text)", "code-only"))
for p in PATTERNS:
    print("%-16s %10d %10d" % (p, raw[p], len(codehits[p])))
print()
print("code-only hits, by line:")
bad = 0
for p in PATTERNS:
    for rel, k, line in codehits[p]:
        ok = (p == "sorry" and rel == "comparator/Challenge/DBN.lean")
        print("  %-14s %s:%d: %s%s" % (p, rel, k, line[:70], "" if ok else "   <-- NOT PERMITTED"))
        if not ok: bad += 1
n_sorry = len(codehits["sorry"])
print()
print("permitted (challenge placeholders): %d; other code hits: %d" % (n_sorry, bad))
print("RESULT: %s" % ("CLEAN" if bad == 0 and n_sorry == 7 else "NOT CLEAN"))
sys.exit(0 if bad == 0 and n_sorry == 7 else 1)
