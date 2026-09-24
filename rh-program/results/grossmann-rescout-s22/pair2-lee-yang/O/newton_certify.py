#!/usr/bin/env python3
"""Scout O -- upgrade every numerical realization to a 50-digit Newton-refined one.
For each realized record: start from the stored J (rounded to 1e-10), fix the edges with J < 1e-7 at
J = 0 exactly (allowed: J = 0 is a finite coupling), and run minimum-norm Newton steps on
Q_k(J) - T_k (k = 1..n//2) in mpmath at 50 digits over the remaining couplings.  Success =
max relative residual < 1e-40, every refined J > 0, displacement < 1e-6 from the stored point
(quadratic convergence to an exact solution next to the found one)."""
import itertools, json, os, sys
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import feasibility as F
mp.mp.dps = 50

def refine(n, J0, T):
    edges = list(itertools.combinations(range(n), 2))
    subsets = list(itertools.product((0, 1), repeat=n))
    cuts = [[e for e, (i, j) in enumerate(edges) if S[i] != S[j]] for S in subsets]
    sizes = [sum(S) for S in subsets]
    K = n // 2
    J = [mp.mpf(x) for x in J0]
    free = [e for e in range(len(J)) if J0[e] > 1e-7]
    for e in range(len(J)):
        if e not in free:
            J[e] = mp.mpf(0)
    start = [J[e] for e in free]
    for it in range(40):
        Q = [mp.mpf(0)] * (K + 1); D = [[mp.mpf(0)] * len(free) for _ in range(K + 1)]
        for S, cset, k in zip(subsets, cuts, sizes):
            if k == 0 or k > K:
                continue
            w = mp.e ** (-2 * mp.fsum(J[e] for e in cset))
            Q[k] += w
            for a, e in enumerate(free):
                if e in cset:
                    D[k][a] += -2 * w
        r = mp.matrix([Q[k] - T[k] for k in range(1, K + 1)])
        rel = max(abs((Q[k] - T[k]) / T[k]) for k in range(1, K + 1))
        if rel < mp.mpf(10) ** -40:
            disp = max([abs(J[e] - s) for e, s in zip(free, start)] + [mp.mpf(0)])
            return True, float(rel), float(disp), float(min([J[e] for e in free] + [mp.mpf(1)])), it
        A = mp.matrix([[D[k][a] for a in range(len(free))] for k in range(1, K + 1)])
        try:
            step = A.T * mp.lu_solve(A * A.T, r)
        except ZeroDivisionError:
            return False, float(rel), None, None, it
        for a, e in enumerate(free):
            J[e] -= step[a]
    return False, float(rel), None, None, 40

out = []; ok = bad = 0
for fn in ["cluster_polytope_g1.json"] + ["cluster_polytope_g2p%d.json" % p for p in (3, 5, 7)]:
    for r in json.load(open(os.path.join(HERE, fn))):
        g = 2 if "a2" in r else 1
        for key, s in (("noflip", 1), ("flip", -1)):
            o = r[key]
            if o["status"] != "realized":
                continue
            att = o["search"][-1]; n = att["n"]; m = att["m"]
            a = [1, r["a1"], r["a2"], r["p"] * r["a1"], r["p"] ** 2] if g == 2 else [1, r["a1"], r["p"]]
            parts = F.target_parts(r["p"], a, s, m)
            T = [mp.mpf(X.numerator) / X.denominator + (mp.mpf(Y.numerator) / Y.denominator) / mp.sqrt(r["p"]) for X, Y in parts]
            succ, rel, disp, jmin, it = refine(n, att["J"], T)
            ok += succ; bad += (not succ)
            tag = (r["p"], r["a1"], r.get("a2"), key, m)
            out.append({"class": tag, "ok": succ, "rel": rel, "disp": disp, "min_free_J": jmin, "iters": it})
            if not succ:
                print("NOT CERTIFIED:", tag, "rel %.2e" % rel, flush=True)
print("Newton-refined realizations: certified %d, not certified %d" % (ok, bad))
cert = [x for x in out if x["ok"]]
print("max displacement %.2e; max final relative residual %.1e; min refined free J %.3e"
      % (max(x["disp"] for x in cert), max(x["rel"] for x in cert), min(x["min_free_J"] for x in cert)))
json.dump(out, open(os.path.join(HERE, "newton_certify.json"), "w"), indent=0)

# ---- classification of the records Newton did not certify (appended pass)
import math
print("--- uncertified records: double-zero test and exact product alternative ---")
num_only = []
for x in out:
    if x["ok"]:
        continue
    p, a1, a2, key, m = x["class"]
    s = 1 if key == "noflip" else -1
    D = a1 * a1 - 4 * a2 + 8 * p          # = q * (w1 - w2)^2 ; 0 iff a double zero
    c1 = s * a1 / math.sqrt(p); c2 = a2 / p
    w = -c1 / 2                            # the double w-root when D = 0
    prod = (D == 0 and w / 2 < 0 and m == 0)
    print(x["class"], "D=%d" % D, "double zero" if D == 0 else "", "cos(theta)=%.4f" % (w / 2) if D == 0 else "",
          "-> EXACT: two identical untwisted pairs, e^{-2J} = %.6f" % (-w / 2) if prod else "-> numerical only")
    if not prod:
        num_only.append(x["class"])
print("uncertified and without an exact product realization:", len(num_only), num_only)
g2_noflip = [c for c in num_only if c[2] is not None and c[3] == "noflip"]
print("  of which g=2 literal (noflip) records:", len(g2_noflip), g2_noflip)
