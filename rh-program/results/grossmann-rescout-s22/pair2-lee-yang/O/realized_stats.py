#!/usr/bin/env python3
"""Scout O -- statistics of the realizations found (g = 2, literal orientation)."""
import json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
d = sum((json.load(open(os.path.join(HERE, "cluster_polytope_g2p%d.json" % p))) for p in (3, 5, 7)), [])
c = collections.Counter(); jm = []; errs = []; dev = []; mpos_eq = 0; tot = 0; fiber = collections.Counter()
for r in d:
    o = r["noflip"]
    if o["status"] == "realized":
        a = o["search"][-1]
        c[o["m_real"]] += 1; jm.append(a["Jmax"]); errs.append(a["mp_rel_coef_err"]); dev.append(a["max_root_modulus_dev"])
        tot += 1; mpos_eq += (o["m_real"] == o["m_pos"])
        n = a["n"]; fiber[n * (n - 1) // 2 - n // 2] += 1
print("g=2 literal realizations: %d; by m: %s" % (tot, dict(sorted(c.items()))))
print("realized at m = m_pos (the first m with positive coefficients): %d of %d" % (mpos_eq, tot))
print("Jmax over all realizations: max %.3f, median %.3f; >10: %d" % (max(jm), sorted(jm)[len(jm)//2], sum(1 for x in jm if x > 10)))
print("40-digit recomputed relative coefficient error: max %.1e; max ||root|-1|: %.1e" % (max(errs), max(dev)))
print("fiber dimension C(n,2) - floor(n/2) (unknowns minus equations) at the realizing n:", dict(fiber))
