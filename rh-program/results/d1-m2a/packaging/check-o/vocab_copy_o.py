#!/usr/bin/env python3
"""CHECK-O step 3 support: is comparator/ChallengeDeps/DBN.lean really a character-for-character
copy of the Zeta23 statement vocabulary?  Job 2's own check (no code shared with
packaging/gen_challengedeps_dbn.py or cmp_literal_blocks.py).

For every `def` / `structure` / `abbrev` declaration in the trusted file, find the declaration of
the same name in the Zeta23 statement-layer sources and compare the two block texts verbatim
(docstring included; only the leading `/-- … -/` docstring and the declaration body).
Usage: vocab_copy_o.py <lean-tree>
"""
import os, re, sys

TREE = sys.argv[1]
TRUSTED = os.path.join(TREE, "comparator/ChallengeDeps/DBN.lean")
SOURCES = ["Zeta23/DBN/Defs.lean", "Zeta23/W1/Format.lean", "Zeta23/W1/Checker.lean",
           "Zeta23/W1/Soundness.lean", "Zeta23/DBN/BarrierCert.lean", "Zeta23/DBN/Asym.lean"]

DECL = re.compile(r"(?m)^(?:noncomputable\s+)?(?:private\s+)?(def|structure|abbrev|instance)\s+"
                  r"([A-Za-z_][A-Za-z0-9_'.]*)")

def blocks(path):
    """name -> (text, source-line). A block runs from its declaration line (with any immediately
    preceding docstring) up to the next declaration / section marker / namespace command."""
    src = open(path, encoding="utf-8").read()
    lines = src.split("\n")
    starts = []
    for m in DECL.finditer(src):
        ln = src[:m.start()].count("\n")          # 0-based
        starts.append((ln, m.group(2)))
    stops = set()
    for k, l in enumerate(lines):
        if (DECL.match(l) or l.startswith(("theorem ", "lemma ", "example ", "namespace ",
                                           "end ", "/-! ", "section", "open ", "set_option",
                                           "attribute", "deriving instance", "@[")) ):
            stops.add(k)
    # adjusted start of each declaration: its docstring line if it has one
    adj = []
    for ln, name in starts:
        b = ln
        if b > 0 and lines[b - 1].rstrip().endswith("-/"):
            j = b - 1
            while j >= 0 and not lines[j].lstrip().startswith("/--"):
                j -= 1
            if j >= 0:
                b = j
        adj.append((ln, b, name))
    out = {}
    for k, (ln, b, name) in enumerate(adj):
        # end: the next declaration's ADJUSTED start, or the next stop line, whichever comes first
        e = adj[k + 1][1] if k + 1 < len(adj) else len(lines)
        j = ln + 1
        while j < len(lines) and j not in stops:
            j += 1
        e = min(e, j)
        text = "\n".join(lines[b:e]).rstrip()
        out[name] = (text, b + 1)
    return out

tb = blocks(TRUSTED)
zb = {}
for s in SOURCES:
    for n, (t, l) in blocks(os.path.join(TREE, s)).items():
        zb.setdefault(n, (t, s, l))

print("CHECK-O — is ChallengeDeps/DBN.lean a character-for-character copy?  (Job 2's own check)")
print("trusted declarations: %d" % len(tb))
same, diff, missing = 0, [], []
for n in sorted(tb):
    if n not in zb:
        missing.append(n); continue
    t = tb[n][0].strip()
    z = zb[n][0].strip()
    if t == z:
        same += 1
    else:
        diff.append((n, zb[n][1], zb[n][2]))
print("found in the Zeta23 statement layer and IDENTICAL: %d" % same)
print("found but DIFFERENT: %d" % len(diff))
for n, s, l in diff:
    print("   DIFFERENT: %s  (Zeta23 %s:%d)" % (n, s, l))
    a = tb[n][0].strip().split("\n"); b = zb[n][0].strip().split("\n")
    for i in range(max(len(a), len(b))):
        x = a[i] if i < len(a) else "<none>"
        y = b[i] if i < len(b) else "<none>"
        if x != y:
            print("     trusted: %s" % x[:110])
            print("     zeta23 : %s" % y[:110])
print("not found in the Zeta23 statement layer: %d %s" % (len(missing), missing))
print("RESULT: %s" % ("VERBATIM COPY" if not diff and not missing else "DIVERGENCE"))
