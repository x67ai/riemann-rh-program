#!/usr/bin/env python3
"""Job 2 (Opus) re-check of the D-R8 fix pass: the relabel, in all 14 places named in
BUILD-NOTES-fDH.md 7, character by character; and the old box-form THEOREM claim absent."""
import re, os, sys, json
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
def rd(p):
    return open(os.path.join(ROOT, p), encoding='utf-8', errors='replace').read()
def norm(t):
    return re.sub(r'\s+', ' ', t)
BN = rd('results/d1-m2a/dr8/BUILD-NOTES-fDH.md')
m = re.search(r'\*"(f_DH has at least one zero ρ with.*?)"\*', BN, re.S)
NEW = norm(m.group(1)).strip()
OLD = ("f_DH has at least one zero in R = [4/5, 41/50] × [85.69, 85.71] with Re s > 1/2 — "
       "kernel-checked modulo the displayed hypothesis H-ENCL_DH (the two producers' enclosures "
       "of f_DH on ∂R are true; producers untrusted).")
FILES = ['results/d1-m1/FORMAT.md', 'results/d1-m1/acceptance-report.md',
         'directions/D1-certified-refutation-arm.md', 'lean/README.md',
         'lean/Zeta23/W1/FDH.lean', 'lean/formalization.yaml', 'results/d1-m1/w1-schema.json',
         'results/d1-m1/producer_mp.py', 'results/d1-m1/producer_arb.py',
         'results/d1-m1/checker_ref.py', 'results/d1-m1/reference_checker.py',
         'results/d1-m1/acceptance/w1-mp-dh-livefire.json',
         'results/d1-m1/acceptance/w1-arb-dh-livefire.json',
         'results/d1-m2a/dr8/BUILD-NOTES-fDH.md']
fails = []
print("NEW label (%d chars):\n  %s\n" % (len(NEW), NEW))
print("%-52s %-5s %-5s %s" % ("file", "new", "old", "note"))
print("-" * 92)
for p in FILES:
    t = norm(rd(p))
    n, o = t.count(NEW), t.count(OLD)
    note = ""
    if n < 1:
        fails.append("%s: NEW label absent" % p); note = "NEW ABSENT"
    if o:
        # the old sentence may survive only as an explicitly dated 'was' quotation
        for mm in re.finditer(re.escape(OLD), t):
            ctx = t[max(0, mm.start()-300):mm.start()]
            if not re.search(r'was|superseded|until|relabel|before|history|v1|pricing', ctx, re.I):
                fails.append("%s: OLD label present, not marked as superseded" % p)
                note += " OLD UNMARKED"
            else:
                note += " old-as-history"
    print("%-52s %-5d %-5d %s" % (p, n, o, note))
print("\nPRICING-fDH.md (deliberately NOT edited; must carry a superseded note):")
pr = norm(rd('results/d1-m2a/dr8/PRICING-fDH.md'))
print("   old sentence occurrences: %d ; new sentence occurrences: %d" % (pr.count(OLD), pr.count(NEW)))
has_note = bool(re.search(r'supersed', pr, re.I))
print("   carries a 'superseded' annotation: %s" % has_note)
if not has_note:
    fails.append("PRICING-fDH.md 3.2 still asserts the old label with no superseded note")
print("\nThe old box-form claim as a THEOREM claim, over the lines the fix pass ADDED:")
import subprocess
out = subprocess.run(['git','diff','-U0','5fe6aa2','HEAD','--','.',
                      ':!results/d1-m2a/dr8/check-o',
                      ':!results/d1-m2a/dr8/CHECK-fDH-O.md', ':!results/d1-m2a/dr8/CHECK-fDH-O-axioms.log'],
                     capture_output=True, text=True, cwd=ROOT).stdout
cur=None; added={}
for l in out.split('\n'):
    if l.startswith('+++ b/'): cur=l[6:]; added.setdefault(cur,[])
    elif l.startswith('+') and not l.startswith('+++') and cur: added[cur].append(l[1:])
tot=sum(len(v) for v in added.values())
print("   lines added since 5fe6aa2: %d across %d files" % (tot, len(added)))
PHRASES = [("RH-for-DH disproved", None), ("fully machine-checked", None),
           ("in R = [4/5, 41/50]", "box-form claim")]
for ph, _ in PHRASES:
    hits=[]
    for f, lines in added.items():
        for l in lines:
            if ph.lower() in l.lower():
                hits.append((f, l.strip()))
    print('   "%s": %d added line(s)' % (ph, len(hits)))
    for f, l in hits:
        ok = False
        low = l.lower()
        if ph == "in R = [4/5, 41/50]":
            # allowed only as the parenthetical, or inside a quoted OLD label marked as superseded
            ok = ("transcript's rectangle is R" in l) or ("was" in low) or ("supersed" in low) or ("relabel" in low)
        else:
            ok = bool(re.search(r'never|not |must never|no claim|does not', low))
        print("      [%s] %s\n         %s" % ("OK" if ok else "FINDING", f, l[:300]))
        if not ok:
            fails.append('unallowed "%s" in an added line of %s' % (ph, f))
print("\nVERDICT: %s" % ("PASS" if not fails else "%d FINDING(S)" % len(fails)))
for f in fails: print("  - " + f)
sys.exit(1 if fails else 0)
