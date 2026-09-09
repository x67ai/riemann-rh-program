#!/usr/bin/env python3
"""CHECK-O: the parent's statement-identity quick check, re-derived by Job 2 (no code shared with
packaging/statement_identity.py).  Extracts each `theorem NAME … :=` from Challenge/DBN.lean and
Solution/DBN.lean with comments stripped, normalizes whitespace, and compares.
Also checks config-dbn.json's theorem_names against the challenge's names, in order.
Usage: stmt_identity_o.py <lean-tree>
"""
import json, os, re, sys
TREE = sys.argv[1]

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

def stmts(rel, skip_ns=None):
    code = strip_c(open(os.path.join(TREE, rel), encoding="utf-8").read())
    lines = code.split("\n")
    # cut out a namespace block entirely (the solution's DBNBridge helpers)
    if skip_ns:
        keep, drop = [], False
        for l in lines:
            if re.match(r"^namespace\s+%s\s*$" % skip_ns, l): drop = True; continue
            if re.match(r"^end\s+%s\s*$" % skip_ns, l): drop = False; continue
            if not drop: keep.append(l)
        lines = keep
    out, i = [], 0
    while i < len(lines):
        m = re.match(r"^theorem\s+([A-Za-z_][A-Za-z0-9_']*)", lines[i])
        if m:
            buf, j = [], i
            while j < len(lines):
                buf.append(lines[j])
                if ":=" in lines[j]: break
                j += 1
            text = "\n".join(buf)
            text = text[:text.rindex(":=")]
            out.append((m.group(1), re.sub(r"\s+", " ", text).strip()))
            i = j + 1
        else:
            i += 1
    return out

ch = stmts("comparator/Challenge/DBN.lean")
so = stmts("comparator/Solution/DBN.lean", skip_ns="DBNBridge")
cfg = json.load(open(os.path.join(TREE, "comparator/config-dbn.json")))

print("CHECK-O — statement identity, Job 2's own extraction")
print("challenge statements: %d; solution root statements: %d; config theorem_names: %d"
      % (len(ch), len(so), len(cfg["theorem_names"])))
sd = dict(so)
bad = 0
for n, t in ch:
    if n not in sd:
        print("  %s: MISSING on the solution side" % n); bad += 1; continue
    ok = (t == sd[n])
    print("  %-36s %s (%d chars)" % (n, "IDENTICAL" if ok else "DIFFERENT", len(t)))
    if not ok:
        bad += 1
        print("     challenge: %s" % t)
        print("     solution : %s" % sd[n])
names_ok = cfg["theorem_names"] == [n for n, _ in ch]
print("  config-dbn.json theorem_names == the challenge's names, in order: %s" % names_ok)
print("  permitted_axioms: %s" % cfg["permitted_axioms"])
print("  enable_nanoda: %s" % cfg.get("enable_nanoda"))
if not names_ok: bad += 1
extra = [n for n, _ in so if n not in dict(ch)]
print("  solution root theorems not in the challenge: %s" % (extra or "none"))
if extra: bad += 1
print("RESULT: %s" % ("IDENTICAL" if bad == 0 else "DIVERGENCE"))
sys.exit(0 if bad == 0 else 1)
