#!/usr/bin/env python3
"""cmp_literal_blocks.py -- compares every `def` block of the TRUSTED comparator copy
comparator/ChallengeDeps/DBN/Instance02.lean with the corresponding block of the Zeta23 modules
(Zeta23/DBN/Instance02/{Rect,mp_NNNN,mp_Barrier,arb_NNNN,arb_Barrier,Asym_mp,Asym_arb}.lean), byte for byte
(`cmp` semantics: the block texts must be identical; the docstring line above each def is compared too).
A `def` block runs from its `/-- … -/` docstring (if any) to the line before the next blank line.
Independent of the emitters (regex only).  Exit 0 iff every block of both sides matches and the two name sets agree.

usage: cmp_literal_blocks.py <lean-root>
"""
import os, re, sys, glob

ROOT = sys.argv[1]
DEF = re.compile(r"^def\s+([A-Za-z0-9_']+)")

def blocks(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = {}
    for i, l in enumerate(lines):
        m = DEF.match(l)
        if not m: continue
        s = i
        if i > 0 and lines[i - 1].rstrip().endswith("-/"):
            j = i - 1
            while not lines[j].lstrip().startswith("/--"): j -= 1
            s = j
        e = i + 1
        while e < len(lines) and lines[e].strip() != "": e += 1
        out[m.group(1)] = "\n".join(lines[s:e])
    return out

trusted = blocks(os.path.join(ROOT, "comparator/ChallengeDeps/DBN/Instance02.lean"))
zeta = {}
srcs = {}
for p in sorted(glob.glob(os.path.join(ROOT, "Zeta23/DBN/Instance02/*.lean"))):
    for k, v in blocks(p).items():
        if k in zeta: raise SystemExit(f"duplicate def {k} in Zeta23 modules")
        zeta[k] = v; srcs[k] = os.path.relpath(p, ROOT)
# Rect.lean also defines row2T0n / row2T0d, which the trusted copy does not carry (not part of any statement)
extra_z = sorted(set(zeta) - set(trusted)); extra_t = sorted(set(trusted) - set(zeta))
n_ok = n_bad = 0; bad = []
for k in sorted(trusted):
    if k not in zeta: continue
    if trusted[k] == zeta[k]: n_ok += 1
    else: n_bad += 1; bad.append(k)
nbytes = sum(len(trusted[k].encode()) for k in trusted if k in zeta)
nrows = sum(trusted[k].count("⟨") for k in trusted if k.endswith(tuple(f"_rows_{c}" for c in range(20))))
print(f"trusted defs: {len(trusted)}; Zeta23 defs: {len(zeta)} (over {len(set(srcs.values()))} modules)")
print(f"blocks compared: {n_ok + n_bad}; identical: {n_ok}; DIFFERENT: {n_bad} {bad}")
print(f"bytes compared: {nbytes}; W1Row literals inside compared row chunks: {nrows}")
print(f"in Zeta23 only: {extra_z}; in trusted only: {extra_t}")
ok = n_bad == 0 and not extra_t and extra_z == ["row2T0d", "row2T0n"]
print("RESULT:", "IDENTICAL (modulo header/import/namespace lines; row2T0n/row2T0d not carried)" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
