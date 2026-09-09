#!/usr/bin/env python3
"""statement_identity.py -- the parent's "statement-identity quick check" for the DBN topic: strips comments from
comparator/Challenge/DBN.lean and comparator/Solution/DBN.lean, extracts every root-namespace `theorem NAME … :=`
statement (from `theorem` to the `:=` that ends the statement, whitespace-normalized), and confirms the challenge's
statements are textually identical to the solution's, name by name, and that the challenge's name set equals the
config's `theorem_names`.  Exit 0 iff identical.   usage: statement_identity.py <lean-root>
"""
import json, os, re, sys

ROOT = sys.argv[1]

def strip_comments(src):
    out = []; i = 0; n = len(src); depth = 0
    while i < n:
        if src.startswith("/-", i):
            depth += 1; i += 2; continue
        if depth > 0:
            if src.startswith("-/", i): depth -= 1; i += 2
            else: i += 1
            continue
        if src.startswith("--", i):
            j = src.find("\n", i); i = n if j < 0 else j; continue
        out.append(src[i]); i += 1
    return "".join(out)

def statements(path, only_root=True):
    code = strip_comments(open(os.path.join(ROOT, path), encoding="utf-8").read())
    # drop everything inside `namespace DBNBridge … end DBNBridge` (the solution's bridge; not challenge statements)
    code = re.sub(r"namespace DBNBridge.*?end DBNBridge", "", code, flags=re.S)
    stmts = {}
    for m in re.finditer(r"^theorem\s+([A-Za-z0-9_']+)(.*?):=", code, flags=re.S | re.M):
        name, body = m.group(1), m.group(2)
        stmts[name] = " ".join(body.split())
    return stmts

ch = statements("comparator/Challenge/DBN.lean")
so = statements("comparator/Solution/DBN.lean")
cfg = json.load(open(os.path.join(ROOT, "comparator/config-dbn.json")))["theorem_names"]
ok = True
print(f"challenge statements: {len(ch)}; solution statements: {len(so)}; config theorem_names: {len(cfg)}")
for name in sorted(set(ch) | set(so)):
    a, b = ch.get(name), so.get(name)
    if a is None or b is None:
        print(f"  {name}: MISSING on {'solution' if b is None else 'challenge'} side"); ok = False
    elif a == b:
        print(f"  {name}: IDENTICAL ({len(a)} chars, comments stripped, whitespace-normalized)")
    else:
        print(f"  {name}: DIFFERENT\n    challenge: {a}\n    solution:  {b}"); ok = False
if set(cfg) != set(ch):
    print(f"  config/challenge name mismatch: {sorted(set(cfg) ^ set(ch))}"); ok = False
else:
    print(f"  config-dbn.json theorem_names = the challenge's {len(cfg)} names, in order: {cfg == list(ch)}")
# the trusted side must not import Zeta23; the solution must not import the challenge
for path, forbidden in (("comparator/ChallengeDeps/DBN.lean", "Zeta23"), ("comparator/ChallengeDeps/DBN/Instance02.lean", "Zeta23"),
                        ("comparator/Challenge/DBN.lean", "Zeta23"), ("comparator/Solution/DBN.lean", "Challenge.DBN")):
    code = strip_comments(open(os.path.join(ROOT, path), encoding="utf-8").read())
    imps = re.findall(r"^import\s+(\S+)", code, flags=re.M)
    bad = [x for x in imps if x == forbidden or x.startswith(forbidden + ".")]
    print(f"  {path}: imports {imps}; forbidden `{forbidden}…`: {bad if bad else 'none'}")
    if bad: ok = False
# every proof on the challenge side is `sorry`
code = strip_comments(open(os.path.join(ROOT, "comparator/Challenge/DBN.lean"), encoding="utf-8").read())
proofs = re.findall(r":=\s*by\s*(\S+)", code)
print(f"  challenge proofs: {proofs} -> all sorry: {all(p == 'sorry' for p in proofs) and len(proofs) == len(ch)}")
if not (all(p == "sorry" for p in proofs) and len(proofs) == len(ch)): ok = False
print("RESULT:", "IDENTICAL" if ok else "MISMATCH")
sys.exit(0 if ok else 1)
