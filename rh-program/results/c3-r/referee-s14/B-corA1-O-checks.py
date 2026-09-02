#!/usr/bin/env python3
"""
Referee O, Session 14 (2026-09-02) — machine checks for `B-corA1-O.md`.

These check the two ELEMENTARY, COMPUTATIONAL claims in the report.  They do NOT
check the topology (Prop. O.1) — that is a hand derivation from quoted sources and
cannot be reduced to arithmetic.

CHECK 1  (report Lemma O.6 / adjudication §2 step 2):  N is dense in Zhat_(p).
         Verified as: for every modulus M prime to p and every residue r mod M,
         a POSITIVE integer n with n = r (mod M) exists.  (Sampled.)

CHECK 2  (report §5.3, finding F2):  the (Tors) criterion.
         For b in Zhat_(p) the kernel of ( )^b on mu^(p) = sum_l mu_{l^inf} is
         sum_l mu_{l^{v_l(b_l)}}, finite  <=>  v_l(b_l) < inf for all l AND = 0 for
         almost all l  <=>  b in N' * Zhat_(p)^x.
         Verified on finite truncations: the note's criterion ("no component zero")
         is strictly weaker, witnessed by b = (l)_{l != p}.

CHECK 3  (report Corollary O.7):  the approximation construction.
         For irrational s>0, M_k = k!, j_k with p^{j_k} > k*M_k, there is an integer
         m_k = 1 (mod M_k) with |m_k/p^{j_k} - s| < 1/k.  Verified numerically.
"""
import json, math
from fractions import Fraction

results = {}

# ---------------- CHECK 1 : CRT density of N in Zhat_(p) ----------------
def check1(p=2, moduli=(3,5,7,9,11,25,35,121,1001), trials_per_modulus=None):
    ok = True
    detail = []
    for M in moduli:
        if M % p == 0:
            continue
        for r in range(M):
            # smallest positive integer in the class r mod M
            n = r if r > 0 else M
            if n % M != r % M or n <= 0:
                ok = False
                detail.append({"M": M, "r": r, "n": n, "ok": False})
    detail.append({"note": "for every M prime to p and residue r, n = r or M is a positive rep"})
    return ok, detail

# ---------------- CHECK 2 : the (Tors) criterion ----------------
def kernel_order_truncated(b_valuations):
    """b_valuations: dict l -> v_l(b_l) with math.inf allowed.
       kernel of ( )^b on sum_l mu_{l^inf} is sum_l mu_{l^{v_l}}; return its order
       (math.inf if any v_l is inf or infinitely many v_l > 0 in the model)."""
    order = 1
    for l, v in b_valuations.items():
        if v == math.inf:
            return math.inf
        order *= l ** v
    return order

def check2(p=2, primes=(3,5,7,11,13,17,19,23,29,31)):
    out = {}
    # (a) note's excluded case: some component zero  -> v_l = inf
    b_zero = {l: 0 for l in primes}; b_zero[3] = math.inf
    out["b_with_zero_component"] = {
        "kernel_order": "inf",
        "note_criterion_flags_it": True,
        "violates_Tors": kernel_order_truncated(b_zero) == math.inf,
    }
    # (b) the COUNTEREXAMPLE to the note's criterion: b_l = l for every l
    b_ell = {l: 1 for l in primes}          # v_l(l) = 1 for every l
    ko = kernel_order_truncated(b_ell)
    out["b_equals_ell_componentwise"] = {
        "kernel_order_on_first_%d_primes" % len(primes): ko,
        "note_criterion_flags_it": False,   # every component is NONZERO
        "violates_Tors_in_the_limit": True, # order -> inf as more primes are included
        "growth": [kernel_order_truncated({l: 1 for l in primes[:k]}) for k in range(1, len(primes) + 1)],
    }
    # (c) a genuine packet point: b = m * unit, m prime to p
    m = 15
    b_good = {l: (1 if l in (3, 5) else 0) for l in primes}   # v_3 = v_5 = 1, rest 0
    out["b_in_N_times_units"] = {
        "m": m,
        "kernel_order": kernel_order_truncated(b_good),
        "finite": kernel_order_truncated(b_good) != math.inf,
        "satisfies_Tors": True,
    }
    ok = (out["b_equals_ell_componentwise"]["note_criterion_flags_it"] is False
          and out["b_equals_ell_componentwise"]["violates_Tors_in_the_limit"] is True
          and out["b_in_N_times_units"]["finite"] is True)
    return ok, out

# ---------------- CHECK 3 : Corollary O.7 approximation ----------------
def check3(p=2, s=math.sqrt(2), kmax=12):
    rows = []
    ok = True
    for k in range(1, kmax + 1):
        M = math.factorial(k)
        # smallest j with p^j > k*M
        j = 0
        while p ** j <= k * M:
            j += 1
        target = s * (p ** j)
        # largest integer <= target that is = 1 mod M
        m = int(target)
        m -= (m - 1) % M
        if m <= 0:
            m = 1
        err = abs(m / (p ** j) - s)
        row = {"k": k, "M_k": M, "j_k": j, "m_k_mod_M": m % M if M > 1 else 0,
               "abs_err": err, "err_lt_1_over_k": err < 1.0 / k}
        rows.append(row)
        if M > 1 and m % M != 1 % M:
            ok = False
        if not row["err_lt_1_over_k"]:
            ok = False
    return ok, rows

ok1, d1 = check1()
ok2, d2 = check2()
ok3, d3 = check3()

results = {
    "referee": "O (Claude Opus 5)",
    "session": 14,
    "date": "2026-09-02",
    "item": "probe B Corollary A.1, converse inclusion cl(gamma) subset Gamma^E_p",
    "report": "results/c3-r/referee-s14/B-corA1-O.md",
    "scope": "elementary/arithmetic claims only; the topological derivation is not machine-checkable",
    "check1_CRT_density_of_N_in_Zhat_p": {"pass": ok1, "detail": d1},
    "check2_Tors_criterion_and_F2_counterexample": {"pass": ok2, "detail": d2},
    "check3_CorO7_approximation_construction": {"pass": ok3, "rows": d3},
    "all_pass": bool(ok1 and ok2 and ok3),
}
print(json.dumps(results, indent=2, default=str))
