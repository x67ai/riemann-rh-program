#!/usr/bin/env python3
"""
A4 M2 gate -- null_budgets.py (SPEC section 2).

Clustered sine-process null budgets by CUE Monte Carlo, through the SAME row
code path as every dictionary column (kernels.rows_for / lite Fourier rows).

Sampler: n x n Haar unitary via QR of complex Ginibre with R-diagonal phase
fix; eigenangles unfolded to circumference n (an n-periodic sine-process
approximant; k-level correlations -> sine process at O(1/n) in the smoothed
statistics used here). Implementer's independent seeds (distinct from the
formulator's verify suite).

Outputs runs/budgets.json:
  per (n, lambda'): m2_1 (lambda=1 Frobenius/zero), m2p, m3p (lambda') with
  batch-means SE + jackknife check; matched-n (n = 64, 128) also ladder counts
  E[n(V)]/n, C_led^min, occupancy shares; 1/n extrapolation vs closed forms
  m2 = 1/lam + lam/3, m3 = 1 + 1/lam^2 (anchor halt-check, SPEC 2.2/2.3).

Thermal: 4-way multiprocessing (policy: <= 4 concurrent heavy processes).
"""
import json
import math
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kernels import Geometry, make_config, c_coeffs, frob, cubic, b_matrix

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VGRID = (2, 3, 4, 6, 8, 12, 16)


def cue_angles(n, rng):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2)
    Q, R = np.linalg.qr(Z)
    Q = Q * (np.diagonal(R) / np.abs(np.diagonal(R)))
    ang = np.angle(np.linalg.eigvals(Q))
    return (np.sort(ang) + math.pi) * n / (2 * math.pi)  # positions in [0, n)


def batch_work(args):
    """One worker batch: R realizations at size n; returns per-realization rows."""
    if len(args) == 5:
        n, lamp, R, seed, with_eigs = args
        win1, winp = ("flat",), ("flat",)
    else:
        n, lamp, R, seed, with_eigs, win1, winp = args
    rng = np.random.default_rng(seed)
    geom = Geometry(n, 1.0, lamp, win1, winp)
    out = {"m2_1": [], "m2p": [], "m3p": [], "nV": [], "maxabs": []}
    for _ in range(R):
        th = cue_angles(n, rng)
        cfg = make_config(n, atoms=[(t, 1) for t in th])
        c = c_coeffs(cfg, geom.smax)
        out["m2_1"].append(frob(c, geom.a1, geom.J1) / n)
        out["m2p"].append(frob(c, geom.ap, geom.Jp) / n)
        out["m3p"].append(cubic(c, geom.W3p, geom.Jp) / n)
        if with_eigs:
            ev = np.linalg.eigvalsh(b_matrix(c, geom.up, geom.Jp))
            aev = np.abs(ev)
            out["nV"].append([int(np.sum(aev >= V)) for V in VGRID])
            out["maxabs"].append(float(aev.max()))
    return out


def se_stats(x, nbatch=20):
    """mean, batch-means SE, jackknife SE (consistency check)."""
    x = np.asarray(x, dtype=float)
    R = len(x)
    m = x.mean()
    nb = min(nbatch, R)
    bm = np.array([b.mean() for b in np.array_split(x, nb)])
    se_b = bm.std(ddof=1) / math.sqrt(nb)
    # jackknife over batches
    jk = np.array([np.delete(bm, i).mean() for i in range(nb)])
    se_j = math.sqrt((nb - 1) / nb * np.sum((jk - jk.mean()) ** 2))
    return float(m), float(se_b), float(se_j)


def run_size(n, lamp, R, with_eigs, pool, seed0, win1=("flat",), winp=("flat",)):
    """R realizations split over 4 workers."""
    per = [R // 4] * 4
    per[0] += R - sum(per)
    args = [(n, lamp, per[i], seed0 + i, with_eigs, win1, winp) for i in range(4)]
    t0 = time.time()
    parts = pool.map(batch_work, args)
    res = {k: sum((p[k] for p in parts), []) for k in parts[0]}
    stats = {}
    for k in ("m2_1", "m2p", "m3p"):
        m, sb, sj = se_stats(res[k])
        stats[k] = dict(mean=m, se=sb, se_jack=sj, R=R)
    if with_eigs and res["nV"]:
        nV = np.array(res["nV"], dtype=float)
        stats["nV_mean_per_zero"] = (nV.mean(axis=0) / n).tolist()
        stats["nV_se_per_zero"] = (nV.std(axis=0, ddof=1) / math.sqrt(R) / n).tolist()
        cmin = max(V ** 4 * nv for V, nv in zip(VGRID, nV.mean(axis=0) / n))
        stats["C_led_min"] = float(cmin)
        stats["max_abs_eig_mean"] = float(np.mean(res["maxabs"]))
        stats["max_abs_eig_max"] = float(np.max(res["maxabs"]))
    stats["wall_s"] = time.time() - t0
    return stats


def main():
    lamp = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    quick = "--quick" in sys.argv
    explore = "--explore" in sys.argv
    if explore:
        plan = [(64, 3000, True), (128, 1200, True), (256, 400, False),
                (512, 200, False), (1024, 80, False)]
    else:
        plan = [
            # (n, R, with_eigs)
            (64, 4000 if not quick else 400, True),
            (128, 2000 if not quick else 200, True),
            (256, 600 if not quick else 60, False),
            (512, 300 if not quick else 30, False),
            (1024, 120 if not quick else 12, False),
            (2048, 48 if not quick else 6, False),
        ]
    closed = dict(m2_1=4 / 3, m2p=1 / lamp + lamp / 3, m3p=1 + 1 / lamp ** 2)
    out = {"lambda_prime": lamp, "closed_forms": closed, "sizes": {}}
    with Pool(4) as pool:
        for i, (n, R, we) in enumerate(plan):
            st = run_size(n, lamp, R, we, pool, seed0=91_000_000 + 1000 * i + int(lamp * 100))
            out["sizes"][str(n)] = st
            print(f"n={n:5d} R={R:5d}: m2_1={st['m2_1']['mean']:.5f}({st['m2_1']['se']:.5f}) "
                  f"m2p={st['m2p']['mean']:.5f}({st['m2p']['se']:.5f}) "
                  f"m3p={st['m3p']['mean']:.5f}({st['m3p']['se']:.5f})  "
                  f"[{st['wall_s']:.0f}s]", flush=True)

    # 1/n extrapolation fit (weighted least squares, a + b/n) on the >= 128 sizes
    fit = {}
    for k in ("m2_1", "m2p", "m3p"):
        ns, ys, ses = [], [], []
        for n, R, we in plan:
            if n < 128:
                continue
            st = out["sizes"][str(n)][k]
            ns.append(n); ys.append(st["mean"]); ses.append(max(st["se"], 1e-9))
        A = np.vstack([np.ones(len(ns)), 1.0 / np.array(ns)]).T
        wgt = 1.0 / np.array(ses) ** 2
        AtA = A.T @ (A * wgt[:, None])
        atb = A.T @ (np.array(ys) * wgt)
        coef = np.linalg.solve(AtA, atb)
        cov = np.linalg.inv(AtA)
        a, b = coef
        se_a = math.sqrt(cov[0, 0])
        fit[k] = dict(extrap=a, extrap_se=se_a, slope=b,
                      closed=closed[k], anchor_ok=bool(abs(a - closed[k]) <= 2.5 * se_a))
    out["extrapolation"] = fit

    # occupancy shares (SPEC 2.3) from matched n = 64
    st64 = out["sizes"]["64"]
    out["occupancy_check"] = dict(
        frob_cross_share=1 - 1 / st64["m2p"]["mean"],
        cubic_cross_share=1 - 1 / st64["m3p"]["mean"])

    # halt condition: largest-n MC vs closed forms within 3 SE + finite-size envelope
    halt = []
    nbig = str(max(int(k) for k in out["sizes"]))
    stbig = out["sizes"][nbig]
    for k in ("m2_1", "m2p", "m3p"):
        dev = abs(stbig[k]["mean"] - closed[k])
        # allow the O(1/n) finite-size term measured by the fit slope
        env = abs(fit[k]["slope"]) / 2048 + 3 * stbig[k]["se"]
        if dev > env:
            halt.append(f"{k}: dev {dev:.5f} > envelope {env:.5f}")
    out["halt_flags"] = halt
    if halt:
        print("HALT CONDITION TRIPPED:", halt)
    else:
        print("anchors OK: largest-n MC within envelope of closed forms; "
              f"extrapolation anchor_ok = {[fit[k]['anchor_ok'] for k in fit]}")

    tagl = str(lamp).replace(".", "p")
    path = os.path.join(BASE, "runs", f"budgets_lam{tagl}.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("written", path)


if __name__ == "__main__":
    main()
