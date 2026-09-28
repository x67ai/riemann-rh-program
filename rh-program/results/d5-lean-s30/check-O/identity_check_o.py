#!/usr/bin/env python3
"""identity_check_o.py -- CHECKER's own statement-identity check for a comparator topic (a per-topic generalization of
results/d1-m2a/packaging/statement_identity.py): comments stripped, every root `theorem NAME ... :=` statement
whitespace-normalized, challenge vs solution name by name; challenge name set == config theorem_names (in order);
imports of ChallengeDeps/Challenge/Solution listed, Zeta23 forbidden on every side, Challenge.* forbidden in Solution;
every challenge proof is `by sorry`.  usage: identity_check_o.py <lean-root> <Topic> <config.json> <deps-module-file>"""
import json, os, re, sys
ROOT, TOPIC, CFG, DEPS = sys.argv[1:5]
def strip(src):
    out=[];i=0;n=len(src);d=0
    while i<n:
        if src.startswith("/-",i): d+=1;i+=2;continue
        if d:
            if src.startswith("-/",i): d-=1;i+=2
            else: i+=1
            continue
        if src.startswith("--",i):
            j=src.find("\n",i); i=n if j<0 else j; continue
        out.append(src[i]); i+=1
    return "".join(out)
def code(p): return strip(open(os.path.join(ROOT,p),encoding="utf-8").read())
def stmts(p):
    c=code(p); c=re.sub(r"namespace\s+(\S+).*?end\s+\1","",c,flags=re.S)  # drop helper namespaces
    return {m.group(1):" ".join(m.group(2).split()) for m in re.finditer(r"^theorem\s+([A-Za-z0-9_'.]+)(.*?):=",c,flags=re.S|re.M)}
chp="comparator/Challenge/%s.lean"%TOPIC; sop="comparator/Solution/%s.lean"%TOPIC
ch=stmts(chp); so=stmts(sop); cfg=json.load(open(os.path.join(ROOT,CFG)))["theorem_names"]
ok=True
print(f"topic {TOPIC}: challenge root theorems {len(ch)}; solution root theorems {len(so)}; config names {len(cfg)}")
for nme in cfg:
    a,b=ch.get(nme),so.get(nme)
    if a is None or b is None: print(f"  {nme}: MISSING ({'challenge' if a is None else 'solution'})"); ok=False
    elif a==b: print(f"  {nme}: IDENTICAL ({len(a)} chars)")
    else: print(f"  {nme}: DIFFERENT\n    C: {a}\n    S: {b}"); ok=False
print(f"  config names == challenge names in order: {cfg==list(ch)}; extra solution root theorems: {sorted(set(so)-set(ch))}")
if cfg!=list(ch): ok=False
for p,forb in ((DEPS,["Zeta23"]),(chp,["Zeta23"]),(sop,["Zeta23","Challenge"])):
    imps=re.findall(r"^import\s+(\S+)",code(p),flags=re.M)
    bad=[x for x in imps if any(x==f or x.startswith(f+".") for f in forb)]
    print(f"  {p}: imports {imps}; forbidden {forb}: {bad or 'none'}"); ok&= not bad
pr=re.findall(r":=\s*by\s*(\S+)",code(chp)); allsorry=all(x=="sorry" for x in pr) and len(pr)==len(ch)
print(f"  challenge proofs: {len(pr)} x {sorted(set(pr))} -> all sorry: {allsorry}"); ok&=allsorry
print("RESULT:", "IDENTICAL" if ok else "MISMATCH"); sys.exit(0 if ok else 1)
