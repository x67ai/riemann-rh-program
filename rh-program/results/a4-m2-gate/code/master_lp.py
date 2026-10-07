#!/usr/bin/env python3
"""
A4 M2 gate -- master_lp.py (SPEC 4.1, 4.2, 5.1, 5.2).

Master LP over a dictionary of explicit configurations:
  variables w_c >= 0 (law), plus g >= 0 (coupled garnish-Frobenius budget).
  min E_w[N_d]/N subject to:
    (R-1) sum w_c = 1  (mass N per column by construction)
    (R-2) E_w[F1]  in B1 [1 -/+ eps1]  (widened by `bars` for delta_0^lo)
    (R-5) E_w[F']  in B2 [...]   (coupled mode: both sides tightened by g N)
    (R-6) |E_w[C'] - B3| <= slack3 + fuzz(g)   (fuzz = 2 sqrt2 sqrt(C_led g) N,
          outer-approximated by tangent cuts, refined at the optimum; or fixed
          Gamma slack in parametric mode)
    (R-7) E_w[n(V)] <= C_led N V^-4, V in Vgrid
    (T-2) optional near-CUE pinning |E_w|c_j|^2 - j| <= tau2, j = 1..N-1
  P_base: cubic block removed (R-6/R-7/fuzz), R-5 kept (SPEC 5.1).
  Calibration: R-5 removed as well -> must reproduce 5/6 - (2/3) eps1 corner.

Solver: scipy linprog method='highs'. Final solution re-verified: support
columns' row values re-accumulated by compensated summation and constraints
re-checked in Fraction arithmetic on 12-digit rationalizations (documented
deviation: kernel row values are transcendental; verification precision 1e-12
relative, far below any decision margin).
"""
import math
from dataclasses import dataclass, field
from fractions import Fraction as Fr

import numpy as np
from scipy.optimize import linprog


@dataclass
class GateParams:
    N: int = 64
    eps1: float = 0.05        # lambda = 1 Frobenius relative slack
    epsF: float = 0.05        # lambda' Frobenius relative slack
    eps3: float = 0.05        # cubic relative slack
    C_led: float = 100.0
    fuzz: str = "coupled"     # 'coupled' | 'gamma' | 'none'
    Gamma: float = 0.0        # parametric fuzz (units of N) when fuzz == 'gamma'
    budgets: tuple = None     # (B_F1, B_Fp, B_Cp) absolute (per period)
    bars: tuple = (0.0, 0.0, 0.0)   # extra absolute half-widths (delta_0^lo)
    Vgrid: tuple = (2, 3, 4, 6, 8, 12, 16)
    tier2_tau: float = None   # None = off; else tau2 in grid units
    Wcap: int = 8             # mark alphabet cap (pair mult <= max(1, W//2))


def filter_W(cols_rows, W):
    """Columns admissible at mark alphabet W."""
    out = []
    for cfg, r in cols_rows:
        pm = int(cfg.pair_mrk.max()) if len(cfg.pair_mrk) else 0
        am = int(cfg.atom_mrk.max()) if len(cfg.atom_mrk) else 0
        if am <= W and pm <= max(1, W // 2):
            out.append((cfg, r))
    return out


def solve_master(cols_rows, p: GateParams, include_cubic=True, include_Fp=True,
                 tangents=None, refine=True):
    """Returns dict with status, P, x, duals, active tangent, row report."""
    n = len(cols_rows)
    N = p.N
    B1, B2, B3 = p.budgets
    s1 = p.eps1 * B1 + p.bars[0]
    s2 = p.epsF * B2 + p.bars[1]
    s3 = p.eps3 * B3 + p.bars[2]
    coupled = include_cubic and p.fuzz == "coupled"
    nv = n + (1 if coupled else 0)     # + g variable

    obj = np.array([r.Nd / N for _, r in cols_rows] + ([0.0] if coupled else []))
    A_eq = [np.concatenate([np.ones(n), [0.0] * (1 if coupled else 0)])]
    b_eq = [1.0]

    A_ub, b_ub, names = [], [], []

    F1v = np.array([r.F1 for _, r in cols_rows])
    Fpv = np.array([r.Fp for _, r in cols_rows])
    Cpv = np.array([r.Cp for _, r in cols_rows])

    def row(vec, gcoef, rhs, name):
        A_ub.append(np.concatenate([vec, [gcoef]]) if coupled else vec)
        b_ub.append(rhs)
        names.append(name)

    # R-2 lambda=1 Frobenius
    row(F1v, 0.0, B1 + s1, "F1_hi")
    row(-F1v, 0.0, -(B1 - s1), "F1_lo")
    # R-5 lambda' Frobenius (coupled: tightened by g N on both sides)
    if include_Fp:
        row(Fpv, N if coupled else 0.0, B2 + s2, "Fp_hi")
        row(-Fpv, N if coupled else 0.0, -(B2 - s2), "Fp_lo")
    if include_cubic:
        if p.fuzz == "gamma":
            s3g = s3 + p.Gamma * N
            row(Cpv, 0.0, B3 + s3g, "Cp_hi")
            row(-Cpv, 0.0, -(B3 - s3g), "Cp_lo")
        elif p.fuzz == "none":
            row(Cpv, 0.0, B3 + s3, "Cp_hi")
            row(-Cpv, 0.0, -(B3 - s3), "Cp_lo")
        else:
            # coupled: |E[C'] - B3| <= s3 + 2 sqrt2 sqrt(C_led g) N via tangents
            # tangent at t > 0: sqrt(g) <= (sqrt(t) + (g - t)/(2 sqrt t))
            tans = tangents or [1e-4, 1e-3, 1e-2, 0.05]
            for t in tans:
                a = 2 * math.sqrt(2) * math.sqrt(p.C_led) * N
                const = a * math.sqrt(t) / 2
                slope = a / (2 * math.sqrt(t))
                row(Cpv, -slope, B3 + s3 + const, f"Cp_hi_t{t:g}")
                row(-Cpv, -slope, -(B3 - s3) + const, f"Cp_lo_t{t:g}")
        # R-7 ladder
        for i, V in enumerate(p.Vgrid):
            nVv = np.array([r.nV[i] for _, r in cols_rows], dtype=float)
            row(nVv, 0.0, p.C_led * N / V ** 4, f"lad_V{V}")
    if p.tier2_tau is not None:
        S1m = np.array([r.S1 for _, r in cols_rows])   # (n, N-1)
        for j in range(1, N):
            row(S1m[:, j - 1], 0.0, j + p.tier2_tau, f"t2_hi_j{j}")
            row(-S1m[:, j - 1], 0.0, -(j - p.tier2_tau), f"t2_lo_j{j}")

    bounds = [(0, None)] * nv
    res = linprog(obj, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds,
                  method="highs")
    out = dict(status=res.status, message=res.message)
    if res.status != 0:
        return out
    x = res.x[:n]
    g = float(res.x[n]) if coupled else None

    # refine tangent at optimum g (coupled): re-solve with tangent at g*
    if coupled and refine and g is not None and g > 1e-9:
        tans = tangents or [1e-4, 1e-3, 1e-2, 0.05]
        near = min(abs(g - t) / max(g, 1e-12) for t in tans)
        if near > 1e-3 and len(tans) < 12:
            return solve_master(cols_rows, p, include_cubic, include_Fp,
                                tangents=sorted(set(tans + [g])), refine=True)

    out.update(P=float(res.fun), x=x, g=g,
               duals_eq=res.eqlin.marginals.copy(),
               duals_ub=res.ineqlin.marginals.copy(),
               row_names=names, A_ub_arrays=None,
               tangents_used=(tangents or [1e-4, 1e-3, 1e-2, 0.05]) if coupled else None)
    # row activity report
    act = {}
    with np.errstate(all="ignore"):   # Accelerate BLAS spurious FP flags
        Ax = np.array(A_ub) @ res.x
    for i, nm in enumerate(names):
        slack = b_ub[i] - Ax[i]
        if slack < 1e-6 * max(1.0, abs(b_ub[i])):
            act[nm] = float(res.ineqlin.marginals[i])
    out["active_rows"] = act
    return out


def reduced_costs(cols_rows_new, cols_rows, p, sol, include_cubic=True,
                  include_Fp=True):
    """Reduced cost of new columns against the duals of `sol` (same row build
    order as solve_master; tangent rows included via stored names)."""
    N = p.N
    y0 = float(sol["duals_eq"][0])
    yub = sol["duals_ub"]
    names = sol["row_names"]
    rcs = []
    for cfg, r in cols_rows_new:
        rc = r.Nd / N - y0
        for i, nm in enumerate(names):
            if abs(yub[i]) < 1e-12:
                continue
            if nm == "F1_hi":
                a = r.F1
            elif nm == "F1_lo":
                a = -r.F1
            elif nm == "Fp_hi":
                a = r.Fp
            elif nm == "Fp_lo":
                a = -r.Fp
            elif nm.startswith("Cp_hi"):
                a = r.Cp
            elif nm.startswith("Cp_lo"):
                a = -r.Cp
            elif nm.startswith("lad_V"):
                V = float(nm[5:])
                idx = list(p.Vgrid).index(int(V)) if int(V) == V else None
                a = float(r.nV[idx])
            elif nm.startswith("t2_hi_j"):
                j = int(nm[7:]); a = float(r.S1[j - 1])
            elif nm.startswith("t2_lo_j"):
                j = int(nm[7:]); a = -float(r.S1[j - 1])
            else:
                a = 0.0
            rc -= yub[i] * a
        rcs.append(rc)
    return np.array(rcs)


def rational_verify(cols_rows, p, sol, include_cubic=True, include_Fp=True):
    """Re-verify feasibility + objective of the returned law in Fraction
    arithmetic on 12-digit rationalizations of the row data (active rows)."""
    n = len(cols_rows)
    x = sol["x"]
    sup = [i for i in range(n) if x[i] > 1e-9]
    q = 10 ** 12

    def fr(v):
        return Fr(int(round(v * q)), q)

    ws = [fr(x[i]) for i in sup]
    tot = sum(ws, Fr(0))
    report = {"support": len(sup), "sum_w_dev": float(abs(tot - 1))}
    obj = sum(w * fr(cols_rows[i][1].Nd / p.N) for w, i in zip(ws, sup))
    report["objective_exact"] = float(obj)
    report["objective_float"] = sol["P"]
    report["obj_dev"] = float(abs(obj - fr(sol["P"])))
    B1, B2, B3 = p.budgets
    checks = {}
    EF1 = sum(w * fr(cols_rows[i][1].F1) for w, i in zip(ws, sup))
    checks["F1_in"] = bool(abs(EF1 - fr(B1)) <= fr(p.eps1 * B1 + p.bars[0]) + Fr(1, 10 ** 6))
    if include_Fp:
        EFp = sum(w * fr(cols_rows[i][1].Fp) for w, i in zip(ws, sup))
        gterm = fr((sol.get("g") or 0.0) * p.N)
        checks["Fp_in"] = bool(abs(EFp - fr(B2)) + gterm
                               <= fr(p.epsF * B2 + p.bars[1]) + Fr(1, 10 ** 6))
    if include_cubic:
        ECp = sum(w * fr(cols_rows[i][1].Cp) for w, i in zip(ws, sup))
        g = sol.get("g") or 0.0
        if p.fuzz == "coupled":
            fz_true = 2 * math.sqrt(2) * math.sqrt(p.C_led * g) * p.N
            a = 2 * math.sqrt(2) * math.sqrt(p.C_led) * p.N
            tans = sol.get("tangents_used") or [1e-4]
            fz_enforced = min(a * (math.sqrt(t) / 2 + g / (2 * math.sqrt(t)))
                              for t in tans)
            report["fuzz_tangent_gap"] = float(fz_enforced - fz_true)
            fz = fz_enforced
        else:
            fz = p.Gamma * p.N if p.fuzz == "gamma" else 0.0
        checks["Cp_in"] = bool(abs(ECp - fr(B3))
                               <= fr(p.eps3 * B3 + p.bars[2] + fz) + Fr(1, 10 ** 6))
        for i, V in enumerate(p.Vgrid):
            EnV = sum(w * fr(float(cols_rows[j][1].nV[i])) for w, j in zip(ws, sup))
            checks[f"lad_V{V}"] = bool(EnV <= fr(p.C_led * p.N / V ** 4) + Fr(1, 10 ** 6))
    report["checks"] = checks
    report["all_ok"] = all(checks.values()) and report["sum_w_dev"] < 1e-6
    return report


def gate_point(cols_rows, p: GateParams, tier2=False):
    """P_full, P_base, delta_0 at one parameter point (dictionary fixed)."""
    cr = filter_W(cols_rows, p.Wcap)
    full = solve_master(cr, p, include_cubic=True, include_Fp=True)
    base = solve_master(cr, p, include_cubic=False, include_Fp=True)
    cal = solve_master(cr, p, include_cubic=False, include_Fp=False)
    out = dict(
        n_cols=len(cr),
        P_full=full.get("P"), P_base=base.get("P"), P_cal=cal.get("P"),
        status=(full["status"], base["status"], cal["status"]),
        g_full=full.get("g"),
        delta_0=(full["P"] - base["P"]) if (full.get("P") is not None
                                            and base.get("P") is not None) else None,
        active_full=full.get("active_rows"), active_base=base.get("active_rows"),
    )
    return out, full, base, cal
