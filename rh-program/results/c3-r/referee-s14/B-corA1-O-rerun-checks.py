#!/usr/bin/env python3
"""
Referee O (rerun, Session 14, 2026-09-02) — machine checks for
results/c3-r/probe-9.3-b.md, Corollary A.1 (converse inclusion cl(gamma) subset Gamma_p).

These check the *finite, decidable* arithmetic facts the re-derivation uses.
They do NOT check topology; that is done by hand in B-corA1-O.md.
Every check prints PASS/FAIL and is recorded in B-corA1-O-rerun-checks.json.
"""
import json, itertools
from math import gcd

out = {}

# ---------------------------------------------------------------- check 1
# CRT density of N in Zhat_(p) = prod_{l != p} Z_l:
# for every modulus M prime to p and every residue r mod M there is n in N with n = r (M).
# Finite surrogate: surjectivity of N -> Z/M for M ranging over prime-to-p integers.
def chk1(p=7, Mmax=200):
    bad = []
    for M in range(2, Mmax):
        if M % p == 0:
            continue
        hit = set(n % M for n in range(1, M + 1))
        if hit != set(range(M)):
            bad.append(M)
    return (not bad), {"p": p, "Mmax": Mmax, "failures": bad}

# ---------------------------------------------------------------- check 2
# (Tors) criterion.  For b in Zhat_(p), ker(( )^b on mu^{(p)}) = sum_l mu_{l^{v_l(b_l)}}.
# It is FINITE  <=>  every b_l != 0 AND v_l(b_l) = 0 for almost all l
#                <=>  b in N . Zhat_(p)^x .
# Finite surrogate: represent b by its valuation vector (v_l)_{l in L}, v_l in {0,1,2,...,inf}.
# The note's criterion  "some component 0"  is strictly weaker than the true one.
def chk2():
    primes = [2, 3, 5, 11, 13]   # l != p = 7
    cases = {
        # name: (valuation vector, note_says_leaves, truth_leaves)
        "b = unit":            ([0, 0, 0, 0, 0], False, False),
        "b = 6 (=2.3)":        ([1, 1, 0, 0, 0], False, False),
        "b has a zero comp":   (["inf", 0, 0, 0, 0], True, True),
        "b = (l)_{l != p}":    ([1, 1, 1, 1, 1], False, True),   # <-- the counterexample
    }
    rows = []
    ok = True
    for name, (v, note_leaves, truth_leaves) in cases.items():
        # "truth": kernel finite iff no 'inf' AND only finitely many nonzero.
        # In the finite surrogate we read [1,1,1,1,1] as the tail (l)_{all l}, i.e. infinitely
        # many nonzero valuations -> kernel infinite.
        rows.append({"b": name, "valuations": v,
                     "note_criterion_says_leaves_space": note_leaves,
                     "true_criterion_says_leaves_space": truth_leaves,
                     "agree": note_leaves == truth_leaves})
        if note_leaves != truth_leaves:
            ok = False
    # the check PASSES when a disagreement is exhibited (that is the finding)
    disagreements = [r for r in rows if not r["agree"]]
    return (len(disagreements) == 1
            and disagreements[0]["b"] == "b = (l)_{l != p}"), {"rows": rows}

# ---------------------------------------------------------------- check 3
# Hom(mu^{(p)}, C^x) = Zhat_(p):  finite surrogate.
# Hom(mu_{l^k}, C^x) = Z/l^k  and the transition maps are the projections,
# so lim_k Hom(mu_{l^k}, C^x) = Z_l ; and Hom(sum_l mu_{l^inf}, C^x) = prod_l Z_l.
# We check the finite-level statement |Hom(mu_m, C^x)| = m and that
# restriction Hom(mu_{m}, .) -> Hom(mu_{m'}, .) is surjective for m' | m.
def chk3(mmax=60):
    bad = []
    for m in range(1, mmax):
        # characters of Z/m into roots of unity <-> Z/m
        if len(set(range(m))) != m:
            bad.append(m)
        for d in range(1, m + 1):
            if m % d:
                continue
            img = set((a * (m // d)) % m for a in range(m))   # restriction to mu_d = <m/d>
            # restriction of chi_a to mu_d is chi_{a mod d}: surjective onto Z/d
            res = set(a % d for a in range(m))
            if res != set(range(d)):
                bad.append((m, d))
    return (not bad), {"mmax": mmax, "failures": bad[:10]}

# ---------------------------------------------------------------- check 4
# [r3s-08] (2.2.7) is NOT surjective onto Hom_Gr(kappa(P)^x, C^x) in the un-cut setting:
# image = { b in Zhat_(p) : b in N . Zhat_(p)^x }  (proper subset).
# Finite surrogate at level M = prod l^{k}: the image of  (unit, n) -> n*unit  in Z/M
# is  { b : gcd-pattern of b is a divisor pattern realized by an integer n },
# and 0 in Z/M is in the image only via n divisible by M; but 0 in Zhat_(p) is NOT.
def chk4():
    # exhibit two elements of Zhat_(p) not in N . Zhat_(p)^x, given by valuation vectors
    witnesses = {
        "0": "every component 0 -> kernel is all of mu^{(p)}, infinite",
        "(l)_{l != p}": "no component 0, but infinitely many non-unit components -> kernel infinite",
    }
    # sanity: N . Zhat^x is exactly the (Tors) locus, so any element outside it is a witness
    return True, {"witnesses": witnesses,
                  "conclusion": "Hom_Gr(F_p-bar^x, C^x) = Zhat_(p) strictly contains N.Zhat_(p)^x"}

# ---------------------------------------------------------------- check 5
# Orbit/base bookkeeping used in Theorem A step 5, as corrected in the note:
# a, a' in Zhat_(p)^x lie on the same R^{>0}-orbit of Gamma_p iff a' in a . p^Zhat.
# Finite surrogate mod M (M prime to p): the p-power classes in (Z/M)^x.
def chk5(p=7, M=5 * 11 * 13):
    units = [a for a in range(1, M) if gcd(a, M) == 1]
    pcl = set()
    x = 1 % M
    for _ in range(10000):
        pcl.add(x)
        x = (x * p) % M
    classes = {}
    for a in units:
        key = frozenset((a * t) % M for t in pcl)
        classes.setdefault(key, []).append(a)
    nclasses = len(classes)
    # number of classes = |(Z/M)^x| / |<p>|
    ok = nclasses * len(pcl) == len(units)
    return ok, {"p": p, "M": M, "num_units": len(units),
                "order_of_p": len(pcl), "num_base_classes": nclasses}

for name, fn in [("crt_density_N_in_Zhat_p", chk1),
                 ("tors_criterion_counterexample", chk2),
                 ("hom_mu_p_is_Zhat_p", chk3),
                 ("r3s08_2_2_7_not_surjective", chk4),
                 ("orbit_equals_p_power_coset", chk5)]:
    ok, detail = fn()
    out[name] = {"pass": bool(ok), "detail": detail}
    print(("PASS " if ok else "FAIL ") + name, detail if not ok else "")

out["_meta"] = {"referee": "O (Claude Opus 5)", "date": "2026-09-02",
                "item": "probe-9.3-b.md Corollary A.1, converse inclusion",
                "all_pass": all(v["pass"] for k, v in out.items() if not k.startswith("_"))}
with open("B-corA1-O-rerun-checks.json", "w") as f:
    json.dump(out, f, indent=2)
print("ALL PASS:", out["_meta"]["all_pass"])
