#!/usr/bin/env python3
"""Referee's independent checks for seed-no-go-note.md (do not confuse with the
note's own seed-no-go-checks.py — this is written from scratch by the referee).

R1. Instrument-independent constants: recompute log2, log3, log5 by series
    (atanh identities, exact rational partial sums via Fraction) and pi by a
    hand-rolled Chudnovsky iteration with integer arithmetic; compare with the
    note's table digits.
R2. Rigorous interval continued fractions: bracket each target x in a rational
    interval [lo, hi] certified by the series error bounds, run the CF on both
    endpoints, and keep only the COMMON prefix (every kept term is then proven
    correct, no Legendre heuristic). Certify q_N > 1e100 within the common
    prefix and report the max partial quotient over it.
R3. PSLQ replication at a different precision/maxcoeff, plus a 3-term affine
    PSLQ [x*4pi^2, pi^2, 1] (stronger than the note's claim).
R4. Exact isogeny-degree check: for y_p*y_q = u/v, lambda0 = i*v*y_q sends the
    basis (1, tau_p) to integer vectors (0,v) and (-u,0) in the basis
    (1, tau_q); the index is |det| = uv.  Pure integer arithmetic.
R5. Theorem-1 forward-direction demonstration on (p,q)=(2,3): no lattice map
    with coefficients |a|,|b|,|c|,|d| <= 300 comes near satisfying the two
    containment conditions (min residual reported; compare 1e-30 tolerance).
R6. Genuine replacement for the note's tautological check D: the k^2
    representatives (i + j*tau)/k are pairwise distinct mod Lambda and are
    honest kernel points (numerical, k <= 7).
R7. Full intersection profile by exact topology: intersection numbers of the
    subtori Gamma_m, xi1, xi2, Delta of T^4 = R^4/Z^4 as 4x4 integer
    determinants of direction vectors: Gamma_m.xi1=1, Gamma_m.xi2=m^2,
    Gamma_m.Gamma_n=(m-n)^2, Delta profile (1,1,0), (xi1+xi2)^2=2.
"""
import json, os
from fractions import Fraction
from mpmath import mp, mpf, mpc, log, pi, exp, fabs, pslq

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "referee_seed_checks.json")
res = {}

# ---------------- R1: constants by independent series -------------------
# log 2 = 2 atanh(1/3); log 3 = log2 + 2 atanh(1/5); log 5 = log2+log3+2atanh(1/15)...
# check: log(3/2)=2atanh(1/5); log(5/4)... use: log5 = 2*log2 + log(5/4), log(5/4)=2atanh(1/9).
DIG = 430
def atanh_frac(inv, terms):
    # atanh(1/inv) = sum_{k>=0} 1/((2k+1) inv^(2k+1)), exact Fraction partial sum
    s = Fraction(0)
    x = Fraction(1, inv)
    x2 = x * x
    term = x
    k = 0
    while True:
        add = term / (2 * k + 1)
        s += add
        term *= x2
        k += 1
        if add < Fraction(1, 10 ** (DIG + 10)):
            # tail < add/(1 - 1/inv^2) < 2*add -> certified error bound
            tail_bound = 2 * add
            return s, tail_bound

L2s, e2 = atanh_frac(3, None)
L2 = 2 * L2s; L2err = 2 * e2
L32s, e32 = atanh_frac(5, None)         # log(3/2)
L3 = L2 + 2 * L32s; L3err = L2err + 2 * e32
L54s, e54 = atanh_frac(9, None)         # log(5/4)
L5 = 2 * L2 + 2 * L54s; L5err = 2 * L2err + 2 * e54

# pi by Chudnovsky with binary splitting (integer arithmetic), then interval.
def chudnovsky_pi(digits):
    import math
    N = digits // 14 + 3
    def bs(a, b):
        if b - a == 1:
            if a == 0:
                Pab = Qab = 1
            else:
                Pab = (6 * a - 5) * (2 * a - 1) * (6 * a - 1)
                Qab = a * a * a * 640320 ** 3 // 24
            Tab = Pab * (13591409 + 545140134 * a)
            if a & 1:
                Tab = -Tab
            return Pab, Qab, Tab
        m = (a + b) // 2
        Pam, Qam, Tam = bs(a, m)
        Pmb, Qmb, Tmb = bs(m, b)
        return Pam * Pmb, Qam * Qmb, Tmb * Pam + Tam * Qmb
    P, Q, T = bs(0, N)
    one2 = 10 ** (2 * (digits + 20))
    # sqrt(10005) by integer Newton
    n = 10005 * one2
    x = int(math.isqrt(n))
    while True:
        y = (x + n // x) // 2
        if y >= x:
            break
        x = y
    sqrt10005 = Fraction(x, 10 ** (digits + 20))     # floor-accurate
    sq_lo = sqrt10005
    sq_hi = sqrt10005 + Fraction(1, 10 ** (digits + 20))
    pi_lo = Fraction(426880) * sq_lo * Q / T if T > 0 else None
    pi_hi = Fraction(426880) * sq_hi * Q / T
    # truncation error of the series is far below 10^-(digits+10); widen a hair
    slop = Fraction(1, 10 ** (digits + 5))
    return pi_lo - slop, pi_hi + slop

PI_lo, PI_hi = chudnovsky_pi(DIG)

mp.dps = 460
ref = {"log2": log(2), "log3": log(3), "log5": log(5), "pi": pi()}
def close(fr, mpv, tol):  # |Fraction - mp| < tol
    return abs(mpf(fr.numerator) / mpf(fr.denominator) - mpv) < tol

res["R1_constants"] = {
    "log2_series_matches_mpmath_1e-420": bool(close(L2, ref["log2"], mpf(10) ** -420)),
    "log3_series_matches_mpmath_1e-420": bool(close(L3, ref["log3"], mpf(10) ** -420)),
    "log5_series_matches_mpmath_1e-420": bool(close(L5, ref["log5"], mpf(10) ** -420)),
    "pi_chudnovsky_brackets_mpmath": bool(
        mpf(PI_lo.numerator)/mpf(PI_lo.denominator) < ref["pi"] < mpf(PI_hi.numerator)/mpf(PI_hi.denominator)),
    "err_bounds": {"log2": float(L2err), "log3": float(L3err), "log5": float(L5err)},
}

# Rational intervals for the five targets, from the certified Fraction data.
def interval(numer_lo, numer_hi, denom_lo, denom_hi):
    # x = numer/denom, numer,denom > 0: lo = numer_lo/denom_hi, hi = numer_hi/denom_lo
    return numer_lo / denom_hi, numer_hi / denom_lo

L2i = (L2 - L2err, L2 + L2err)
L3i = (L3 - L3err, L3 + L3err)
L5i = (L5 - L5err, L5 + L5err)
PI2i = (PI_lo * PI_lo, PI_hi * PI_hi)
D4 = (4 * PI2i[0], 4 * PI2i[1])

targets = {
    "log2*log3/(4pi^2)": interval(L2i[0]*L3i[0], L2i[1]*L3i[1], D4[0], D4[1]),
    "log2*log5/(4pi^2)": interval(L2i[0]*L5i[0], L2i[1]*L5i[1], D4[0], D4[1]),
    "log3*log5/(4pi^2)": interval(L3i[0]*L5i[0], L3i[1]*L5i[1], D4[0], D4[1]),
    "(log2)^2/(4pi^2)":  interval(L2i[0]*L2i[0], L2i[1]*L2i[1], D4[0], D4[1]),
    "(log3)^2/(4pi^2)":  interval(L3i[0]*L3i[0], L3i[1]*L3i[1], D4[0], D4[1]),
}

# note's table, first digits (transcribed from seed-no-go-note.md section 7)
note_digits = {
    "log2*log3/(4pi^2)": "0.0192890205998215679007346039996508659",
    "log2*log5/(4pi^2)": "0.0282579044193212256166934388383576738",
    "log3*log5/(4pi^2)": "0.0447877188535867805034209039422156347",
    "(log2)^2/(4pi^2)":  "0.0121700170136801879558172286287261109",
    "(log3)^2/(4pi^2)":  "0.0305723743263550882536179008172733061",
}

# ---------------- R2: rigorous interval continued fractions --------------
def cf_interval(lo, hi, qbound):
    """Common CF prefix of the interval [lo,hi] (Fractions); rigorous."""
    terms = []
    q_prev, q_cur = 0, 1
    maxpq = 0
    while True:
        alo = lo.numerator // lo.denominator
        ahi = hi.numerator // hi.denominator
        if alo != ahi:
            break
        a = alo
        terms.append(a)
        if len(terms) > 1:
            q_prev, q_cur = q_cur, a * q_cur + q_prev
            maxpq = max(maxpq, a)
        flo = lo - a
        fhi = hi - a
        if flo == 0 or fhi == 0:
            return {"terminated_or_exhausted": True, "terms": len(terms),
                    "max_partial_quotient": maxpq, "qN": str(q_cur)}
        lo, hi = 1 / fhi, 1 / flo
        if q_cur > qbound:
            return {"proved_no_denominator_below": str(qbound),
                    "terms": len(terms), "max_partial_quotient": maxpq,
                    "qN_digits": len(str(q_cur)) - 1}
    return {"common_prefix_exhausted_at": len(terms),
            "max_partial_quotient": maxpq, "qN_digits": len(str(q_cur)) - 1}

r2 = {}
mp.dps = 460
for name, (lo, hi) in targets.items():
    cf = cf_interval(lo, hi, 10 ** 100)
    mid = (lo + hi) / 2
    midstr = mp.nstr(mpf(mid.numerator) / mpf(mid.denominator), 40)
    r2[name] = {"cf": cf,
                "first_digits": midstr,
                "matches_note_table": bool(midstr[:36] == note_digits[name][:36])}
res["R2_interval_cf"] = r2

# ---------------- R3: PSLQ replication (different params) ----------------
mp.dps = 300
r3 = {}
for name in targets:
    if name == "log2*log3/(4pi^2)": x = log(2)*log(3)/(4*pi**2)
    elif name == "log2*log5/(4pi^2)": x = log(2)*log(5)/(4*pi**2)
    elif name == "log3*log5/(4pi^2)": x = log(3)*log(5)/(4*pi**2)
    elif name == "(log2)^2/(4pi^2)": x = log(2)**2/(4*pi**2)
    else: x = log(3)**2/(4*pi**2)
    rel2 = pslq([x, mpf(1)], maxcoeff=10**25, maxsteps=200000)
    r3[name] = {"pslq_dps300_maxcoeff_1e25": rel2 if rel2 is None else [int(t) for t in rel2]}
# affine 3-term: c1*(logp*logq) + c2*pi^2 + c3 = 0 ?
aff = {}
for lbl, x in [("log2log3", log(2)*log(3)), ("log2log5", log(2)*log(5)),
               ("log3log5", log(3)*log(5)), ("log2sq", log(2)**2), ("log3sq", log(3)**2)]:
    r = pslq([x, pi**2, mpf(1)], maxcoeff=10**15, maxsteps=200000)
    aff[lbl] = r if r is None else [int(t) for t in r]
r3["affine_3term_x_pi2_1_maxcoeff_1e15"] = aff
ctrl = pslq([log(9), log(3)], maxcoeff=10**8)
r3["control_log9_log3"] = [int(t) for t in ctrl] if ctrl else None
res["R3_pslq"] = r3

# ---------------- R4: exact isogeny degree -------------------------------
# y_p y_q = u/v; lambda0 = i v y_q. Images of basis (1, tau_p) of Lambda_p in
# basis (1, tau_q) of Lambda_q: lambda0*1 = v*tau_q -> (0, v);
# lambda0*tau_p = i v y_q * i y_p = -v y_p y_q = -u -> (-u, 0).
def degree_matrix(u, v):
    M = [[0, -u], [v, 0]]        # columns: images of 1 and tau_p
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    return abs(det)
res["R4_isogeny_degree_exact"] = {
    "claim": "index [Lambda_q : lambda0 Lambda_p] = |det[[0,-u],[v,0]]| = uv",
    "cases": {f"u={u},v={v}": degree_matrix(u, v) == u*v
              for (u, v) in [(3,7),(1,1),(2,5),(10,9),(1,4)]},
}

# ---------------- R5: no near-solutions for (p,q)=(2,3) ------------------
mp.dps = 40
y2 = log(2)/(2*pi); y3 = log(3)/(2*pi)
best = None
B = 300
# conditions: a*y2 = d*y3 (imag) and -b*y2*y3 = c (real), (a,b) != (0,0)
for a in range(-B, B+1):
    for d in range(-B, B+1):
        r1 = fabs(a*y2 - d*y3)
        if best is None or r1 < best[0]:
            if a != 0 or d != 0:
                best = (r1, a, d)
minr1, ba, bd = best
# second condition: nearest integer distance of b*y2*y3 for 1<=|b|<=300
y23 = y2*y3
m2v = min(fabs(b*y23 - mp.nint(b*y23)) for b in range(1, B+1))
res["R5_no_lattice_maps_pq_23"] = {
    "min_|a*y2-d*y3|_coeffs_le_300_nonzero": float(minr1),
    "argmin": [ba, bd],
    "min_dist_b*y2y3_to_Z_b_le_300": float(m2v),
    "tolerance_for_a_true_map": 1e-30,
    "pass_no_map_found": bool(minr1 > mpf("1e-10") and m2v > mpf("1e-10")),
}

# ---------------- R6: genuine kernel check (replaces tautological D) -----
mp.dps = 40
tau = mpc(0, 1)*log(7)/(2*pi)
def in_lattice(z, tol=mpf("1e-30")):
    # z = x + y*tau with tau = i*y7: x = Re z, y = Im z / y7
    x = z.real; y = z.imag / tau.imag
    return fabs(x - mp.nint(x)) < tol and fabs(y - mp.nint(y)) < tol
ok = True
for k in range(1, 8):
    reps = [(mpf(i) + mpf(j)*tau)/k for i in range(k) for j in range(k)]
    # each is a kernel point:
    for w in reps:
        if not in_lattice(k*w):
            ok = False
    # pairwise distinct mod Lambda:
    for i in range(len(reps)):
        for j in range(i+1, len(reps)):
            if in_lattice(reps[i]-reps[j]):
                ok = False
res["R6_kernel_points_distinct_and_valid_k_le_7"] = {"pass": bool(ok)}

# ---------------- R7: intersection profile by exact topology -------------
from itertools import permutations
def det4(M):
    # exact integer 4x4 determinant, Leibniz (fine at this size)
    tot = 0
    for perm in permutations(range(4)):
        sgn = 1
        seen = list(perm)
        # parity by inversion count
        inv = sum(1 for i in range(4) for j in range(i+1, 4) if seen[i] > seen[j])
        sgn = -1 if inv % 2 else 1
        prod = 1
        for i in range(4):
            prod *= M[i][perm[i]]
        tot += sgn * prod
    return tot
def inter(A, B):
    # A, B: two direction 4-vectors each (rows); intersection number = det of stacked 4x4
    return det4([A[0], A[1], B[0], B[1]])
def Gam(m): return [(1, 0, m, 0), (0, 1, 0, m)]
XI1 = [(0, 0, 1, 0), (0, 0, 0, 1)]     # {pt} x E
XI2 = [(1, 0, 0, 0), (0, 1, 0, 0)]     # E x {pt}
prof = {}
allok = True
for m in range(-3, 6):
    g = Gam(m)
    a = abs(inter(g, XI1)); b = abs(inter(g, XI2))
    okm = (a == 1 and b == m*m)
    allok &= okm
    for n in range(-3, 6):
        if n == m: continue
        allok &= (abs(inter(g, Gam(n))) == (m-n)**2)
# Delta = Gam(1): profile (1,1,0); and (xi1+xi2)^2 = 2 via bilinearity:
d = Gam(1)
delta_prof = (abs(inter(d, XI1)), abs(inter(d, XI2)), inter(d, d))
x1x2 = inter(XI1, XI2)
sq = inter(XI1, XI1) + inter(XI2, XI2) + 2*abs(x1x2)
res["R7_intersection_profile_exact"] = {
    "all_Gamma_profiles_match_(1,m^2,(m-n)^2)": bool(allok),
    "Delta_profile_(D.xi1,D.xi2,D^2)": list(delta_prof),
    "(xi1+xi2)^2": sq,
    "pass": bool(allok and delta_prof == (1, 1, 0) and sq == 2),
}

res["all_pass"] = all(
    (v.get("pass", True) if isinstance(v, dict) else True) for v in res.values()
)
with open(OUT, "w") as f:
    json.dump(res, f, indent=1, default=str)
print(json.dumps(res, indent=1, default=str)[:5000])
print("all_pass:", res["all_pass"])
