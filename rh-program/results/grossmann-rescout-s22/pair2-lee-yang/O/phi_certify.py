#!/usr/bin/env python3
"""Scout O -- the closed-form obstruction (scout-O.md 5.3), decided EXACTLY for every class.

phi_j(C, s) := [z^2] of P(s z/sqrt q) (1+z)^{-j}  =  b2 - j b1 + j(j+1)/2,
  b1 = s a1/sqrt q, b2 = a2/q (g = 2);  b1 = s a1/sqrt q, b2 = 1 (g = 1).
LEMMA: if phi_j <= 0 for some integer j with 2g - j not in {0, 1}, then P(s z/sqrt q)(1+z)^m is
the (normalized) partition function of NO finite +-1 ferromagnet (J_ij in [0, inf), uniform
fugacity) on 2g + m sites, for ANY m >= 0.  (Functional L = [z^2](Z (1+z)^{-(m+j)}): value
C(e,2) + d >= 0 at every cluster vertex, C(2g-j, 2) > 0 at the all-free vertex, phi_j at T.)
Also the exact 'root at z = 1' test.  Compares with the LP/search records."""
import json, math, os, sys
from fractions import Fraction
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import feasibility as F

JS = [j for j in range(-80, 81)]

def phi_bad(p, a1, a2, s, g):
    bad = []
    for j in JS:
        if (2 * g - j) in (0, 1):
            continue
        X = (Fraction(a2, p) if g == 2 else Fraction(1)) + Fraction(j * (j + 1), 2)
        Y = Fraction(-j * s * a1)
        if F.sign_xy(X, Y, p) <= 0:
            bad.append(j)
    return bad

def load(n):
    return json.load(open(os.path.join(HERE, n)))

out = {}
for g, files in ((1, ["cluster_polytope_g1.json"]), (2, ["cluster_polytope_g2p%d.json" % p for p in (3, 5, 7)])):
    recs = sum((load(f) for f in files), [])
    agree = disagree = 0
    tally = {"noflip": {"phi-certified": 0, "realized": 0, "open": 0},
             "class_or_twist": {"phi-certified-both": 0, "realized-either": 0, "open": 0}}
    open_list = []
    js_used = {}
    for r in recs:
        st = {}
        for key, s in (("noflip", 1), ("flip", -1)):
            bad = phi_bad(r["p"], r["a1"], r.get("a2", 0), s, g)
            lp = r[key]["status"]
            if bad:
                st[key] = "phi-certified"
                js_used[min(bad, key=abs)] = js_used.get(min(bad, key=abs), 0) + 1
                if lp == "realized":
                    disagree += 1
                    print("CONTRADICTION", r, key)
                else:
                    agree += 1
            elif lp == "realized":
                st[key] = "realized"; agree += 1
            else:
                st[key] = "open"
                if lp.startswith("certified"):
                    disagree += 1; print("LP-certified but phi silent:", r["p"], r["a1"], r.get("a2"), key)
                open_list.append((r["p"], r["a1"], r.get("a2"), key))
        tally["noflip"][st["noflip"]] += 1
        if "realized" in st.values():
            tally["class_or_twist"]["realized-either"] += 1
        elif st["noflip"] == st["flip"] == "phi-certified":
            tally["class_or_twist"]["phi-certified-both"] += 1
        else:
            tally["class_or_twist"]["open"] += 1
    print("g=%d: %d classes; phi vs LP/search records: agree %d, disagree %d" % (g, len(recs), agree, disagree))
    print("  tally:", json.dumps(tally))
    print("  j of the smallest-|j| violated phi (counts):", dict(sorted(js_used.items())))
    print("  open (phi > 0 for all j, not realized by the search):", open_list)
    out[g] = {"tally": tally, "open": open_list}
json.dump(out, open(os.path.join(HERE, "phi_certify.json"), "w"), indent=0)
