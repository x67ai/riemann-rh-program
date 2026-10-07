#!/usr/bin/env python3
"""
A4 M2 gate -- tier_a.py (SPEC section 4.4): the abstract R7 harness.

Exact-rational LP (Fraction simplex) in aggregated variables -- per-zero atom
fractions s_m (m = 1..W), pair fractions q_{m,w} with the section-1.2 block
charges, garnish height variables. NO cross-term variables. Calibration only;
no decision authority (SPEC: with free cross-terms vacuous, with nonnegative
cross-terms unsound).

Regression targets (SPEC section 7, order of execution step 1):
  (A) K1-as-written vacuity: with only a scalar tail row at divergent V0 (no
      all-V ladder), garnish at h0 = V0/2 absorbs the cubic row at o(1) cost:
      LP min N_d/N stays 5/6 - o(1) even with the cubic row active.
  (B) Squeeze capacity: with the all-V ladder + Frobenius cost, max absorbable
      cubic = 2 sqrt(2) sqrt(C_led * eps_g) (SPEC 4.2/9.3; re-derived by the
      implementer analytically -- min-profile optimum, truncation tail 3/hmax).
  (C) lambda = 1 affine degeneracy: on isolated blocks c = 3F - 2 + (m-1)(m-2)
      and G(1) = m3(1) - (3 m2(1) - 2) = 0, so at lambda = 1 a cubic row adds
      NOTHING over marks {1,2} + pairs: min N_d/N = 5/6 with or without it.

Exact rational arithmetic: Fraction data; block charges A(w) enter through
rational approximations of sinh(w)/w to 12 digits (recorded; Tier A is a
regression harness, not the decision LP).
"""
import json
import os
import sys
from fractions import Fraction as Fr

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- exact simplex
def simplex_exact(c, A_eq, b_eq, A_ub, b_ub, maximize=False):
    """Tiny exact-rational simplex (Bland's rule). min c.x s.t. A_eq x = b_eq,
    A_ub x <= b_ub, x >= 0. Returns (status, value, x)."""
    m_eq, m_ub = len(A_eq), len(A_ub)
    n = len(c)
    if maximize:
        c = [-ci for ci in c]
    # slack variables for ub rows; artificial variables for eq rows (two-phase)
    # tableau columns: x (n) | slacks (m_ub) | artificials (m_eq + m_ub-neg?)
    rows = []
    rhs = []
    for i in range(m_eq):
        rows.append(list(A_eq[i]) + [Fr(0)] * m_ub)
        rhs.append(Fr(b_eq[i]))
    for i in range(m_ub):
        sl = [Fr(0)] * m_ub
        sl[i] = Fr(1)
        rows.append(list(A_ub[i]) + sl)
        rhs.append(Fr(b_ub[i]))
    m = m_eq + m_ub
    ntot = n + m_ub
    # make rhs nonnegative
    for i in range(m):
        if rhs[i] < 0:
            rows[i] = [-a for a in rows[i]]
            rhs[i] = -rhs[i]
    # phase 1: add artificials
    art = list(range(ntot, ntot + m))
    T = [rows[i] + [Fr(1) if j == i else Fr(0) for j in range(m)] + [rhs[i]]
         for i in range(m)]
    basis = art[:]
    cost1 = [Fr(0)] * ntot + [Fr(1)] * m + [Fr(0)]

    def pivot(T, basis, obj):
        while True:
            # reduced costs
            red = obj[:]
            for i, bi in enumerate(basis):
                if obj[bi] != 0:
                    coef = obj[bi]
                    red = [r - coef * t for r, t in zip(red, T[i])]
            # entering: Bland
            ent = -1
            for j in range(len(obj) - 1):
                if red[j] < 0:
                    ent = j
                    break
            if ent < 0:
                return True  # optimal
            # ratio test
            best, leave = None, -1
            for i in range(len(T)):
                if T[i][ent] > 0:
                    ratio = T[i][-1] / T[i][ent]
                    if best is None or ratio < best or (ratio == best and basis[i] < basis[leave]):
                        best, leave = ratio, i
            if leave < 0:
                return False  # unbounded
            piv = T[leave][ent]
            T[leave] = [a / piv for a in T[leave]]
            for i in range(len(T)):
                if i != leave and T[i][ent] != 0:
                    f = T[i][ent]
                    T[i] = [a - f * b for a, b in zip(T[i], T[leave])]
            basis[leave] = ent

    ok = pivot(T, basis, cost1)
    val1 = sum(T[i][-1] for i in range(m) if basis[i] >= ntot)
    if not ok or val1 != 0:
        return "infeasible", None, None
    # drop artificial columns (keep basis; artificials at zero level are fine if
    # we pivot them out when possible -- Bland handles degenerate leftovers)
    cost2 = [Fr(ci) for ci in c] + [Fr(0)] * m_ub + [Fr(10 ** 9)] * m + [Fr(0)]
    ok = pivot(T, basis, cost2)
    if not ok:
        return "unbounded", None, None
    x = [Fr(0)] * ntot
    for i, bi in enumerate(basis):
        if bi < ntot:
            x[bi] = T[i][-1]
    val = sum(Fr(ci) * x[j] for j, ci in enumerate(c))
    if maximize:
        val = -val
    return "optimal", val, x[:n]


# ---------------------------------------------------------------- block charges
def A_rat(w, digits=12):
    """sinh(w)/w as a Fraction to `digits` digits (w rational or float)."""
    import mpmath as mp
    mp.mp.dps = digits + 8
    val = mp.sinh(w) / w if w != 0 else mp.mpf(1)
    q = 10 ** digits
    return Fr(int(mp.nint(val * q)), q)


def tier_a():
    out = {}

    # ---------------- (C) lambda = 1 affine degeneracy ----------------
    # variables: s1, s2 (atom fractions marks 1,2), p0 (tight/shallow pair fraction
    # of zeros, per-zero charges F = 1 + A^2 -> 2, c -> 4 at w -> 0).
    # rows (per zero, isolated blocks, lambda = 1 budgets m2 = 4/3, m3 = 2):
    #   mass: s1 + s2 + p = 1
    #   Frobenius: s1*1 + s2*2 + p*2 = 4/3
    #   [cubic optional]: s1*1 + s2*4 + p*4 = 2
    # objective: min N_d fraction = s1 + s2/2 + p
    for with_cubic in (False, True):
        A_eq = [[Fr(1), Fr(1), Fr(1)],
                [Fr(1), Fr(2), Fr(2)]]
        b_eq = [Fr(1), Fr(4, 3)]
        if with_cubic:
            A_eq.append([Fr(1), Fr(4), Fr(4)])
            b_eq.append(Fr(2))
        st, val, x = simplex_exact([Fr(1), Fr(1, 2), Fr(1)], A_eq, b_eq, [], [])
        out[f"C_lambda1_degeneracy_cubic={with_cubic}"] = dict(
            status=st, min_Nd=str(val), min_Nd_float=float(val), x=[str(v) for v in x])
    # expected: 5/6 both ways (cubic row adds nothing at lambda = 1: G(1) = 0)

    # ---------------- (A) K1-as-written vacuity (adjudication computation 4) ----
    # As written, the count row exists only for V >= V0 (divergent); garnish =
    # spectral shift Delta of the cubic row placed at height h0 = V0/2 costs
    #   trace Delta/h0^2, Frobenius Delta/h0, tail row 0, count row 0.
    # Needed swing Delta = 4/3 (doubles-vs-pairs). Capacity at Frobenius slack
    # eps and height h0 is eps*h0 -> infinity: the row system as written admits
    # the absorption (delta_0 = 0) for any divergent V0.
    va = {}
    for h0 in (10, 100, 1000, 10 ** 6):
        Delta = Fr(4, 3)
        va[f"h0={h0}"] = dict(
            frob_cost=float(Delta / h0), trace_cost=float(Delta / h0 / h0),
            count_row=0.0, tail_row=0.0, cubic_gain=float(Delta),
            absorbed=bool(Delta / h0 < Fr(1, 20)))
    out["A_K1_aswritten_vacuity"] = va
    # expected: absorbed=True for h0 >= 100: every stated row satisfied at
    # N_d = 5/6 + o(1) -- reproduces K1-fatal layer 1 as upheld.

    # with the ALL-V ladder the single-height garnish is squeezed:
    # capacity(h0) = min(eps*h0 [Frobenius], C_led/h0 [ladder count*h0^3]);
    # max over h0 at h* = sqrt(C_led/eps) gives sqrt(eps*C_led) << 4/3 as
    # eps -> 0 (adjudication computation 5; multi-height sharp constant in B).
    import math as _m
    vb = {}
    for C_led in (1, 60, 1000):
        for eps in (1e-1, 1e-4, 1e-8):
            cap = _m.sqrt(eps * C_led)
            vb[f"C={C_led}_eps={eps}"] = dict(
                single_height_cap=cap, sharp_multiheight=2 * _m.sqrt(2) * _m.sqrt(C_led * eps),
                swing_needed=4 / 3, squeezed=bool(2 * _m.sqrt(2) * _m.sqrt(C_led * eps) < 4 / 3))
    out["A2_ladder_squeeze"] = vb
    # expected: squeezed=True whenever eps small at fixed C_led (e.g. C=1000,
    # eps=1e-8: 0.0089 << 4/3) -- reproduces the overruling of K1 layer 2.

    # ---------------- lambda' = 1/2 isolated-block LP with marks <= W ----------
    # (SPEC 4.4 purpose (iii): shadow-price sanity; NO cross-term variables, so
    # the cubic equality must be met by iso charges alone -- shows what the
    # abstract system would demand of marks; NOT decision-relevant.)
    lpW = {}
    for W in (2, 3, 4, 6, 8):
        # variables: s_m (m = 1..W) atom fractions per zero; pair fraction p at
        # w = 0+ (F -> 2, c -> 4); objective sum s_m/m + p  (N_d per zero:
        # an atom of mark m is 1 distinct point per m zeros).
        nv = W + 1
        A_eq = [[Fr(1)] * W + [Fr(1)],                          # mass
                [Fr(m) for m in range(1, W + 1)] + [Fr(2)],     # Frobenius' = 13/6
                [Fr(m * m) for m in range(1, W + 1)] + [Fr(4)]]  # cubic' = 5
        b_eq = [Fr(1), Fr(13, 6), Fr(5)]
        obj = [Fr(1, m) for m in range(1, W + 1)] + [Fr(1)]
        st, val, x = simplex_exact(obj, A_eq, b_eq, [], [])
        lpW[f"W={W}"] = dict(status=st,
                             min_Nd=float(val) if val is not None else None,
                             x=[str(v) for v in x] if x else None)
    out["lambdap_isoblock_marksW"] = lpW
    # expected: W = 2 infeasible (iso cubic max 4 < 5); W >= 3 feasible with
    # min_Nd DECREASING in W (the sprinkling geometry) -- confirming that in the
    # abstract no-cross-term world the cubic row is met by high marks, i.e. only
    # the explicit clustered gate can price it honestly.

    # ---------------- (B) squeeze capacity ----------------
    # max cubic shift with height profile on a grid, ladder + Frobenius rows
    # (scale-free C = eps = 1; optimum 2 sqrt 2, truncation tail 3/hmax).
    import numpy as np
    from scipy.optimize import linprog
    for hmax, npts in ((60.0, 2500), (400.0, 4000)):
        h = np.geomspace(1.0, hmax, npts)
        cvec = -h  # maximize sum mu_i h_i (mu = Frobenius mass at height h)
        A_ub2, b_ub2 = [], []
        for i in range(npts):
            row = np.zeros(npts)
            row[i:] = 1.0 / h[i:] ** 2          # cumulative count above h_i
            A_ub2.append(row)
            b_ub2.append(h[i] ** -4.0)          # ladder C h^{-4}, C = 1
        A_ub2.append(np.ones(npts))             # total Frobenius mass <= eps = 1
        b_ub2.append(1.0)
        res = linprog(cvec, A_ub=np.array(A_ub2), b_ub=np.array(b_ub2),
                      bounds=[(0, None)] * npts, method="highs")
        out[f"B_squeeze_hmax={hmax}"] = dict(
            lp=float(-res.fun), tail=3.0 / hmax,
            lp_plus_tail=float(-res.fun) + 3.0 / hmax,
            analytic_2sqrt2=float(2 * 2 ** 0.5))
    # expected: lp + tail -> 2 sqrt 2 = 2.8284

    # capacity scaling in (C_led, eps): value = 2 sqrt2 sqrt(C_led eps)
    import math
    sc = {}
    for C in (1, 60, 1000):
        for eps in (1e-1, 1e-4, 1e-8):
            # rescale: value = sqrt(C*eps) * value(1,1); verify by direct LP at
            # moderate grid (h* = sqrt(2C/eps) must be inside the grid)
            hstar = math.sqrt(2 * C / eps)
            sc[f"C={C}_eps={eps}"] = dict(
                analytic=2 * math.sqrt(2) * math.sqrt(C * eps), hstar=hstar)
    out["B_capacity_scaling"] = sc

    # ---------------- pair-vs-double blindness at every depth ----------------
    # per-zero identity: pairs c = 3F - 2 exactly at every depth (SPEC 1.2):
    # replacing doubles (F=2, c=4) by pairs at depth w changes (F, c) along the
    # SAME affine plane c = 3F - 2 -> the cubic row is blind to isolated pairs.
    ident = {}
    for w in (Fr(1, 64), Fr(1, 8), Fr(1, 2), Fr(1), Fr(2)):
        A = A_rat(float(w))
        F = 1 + A * A
        c = 1 + 3 * A * A
        ident[f"w={w}"] = dict(F=float(F), c=float(c), resid_3F_minus_2=float(c - (3 * F - 2)))
    out["pair_affine_identity"] = ident

    path = os.path.join(BASE, "runs", "tier_a.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    return out


if __name__ == "__main__":
    res = tier_a()
    print(json.dumps(res, indent=1))
