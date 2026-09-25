#!/usr/bin/env python3
"""window_residual.py — FORMULATION.md §1, the numerical companion of Theorem F1(b).

Take 40 genuine zeros of zeta near t = 3553 (mpmath.zetazero, n = 3000..3039; the same source as
results/c2-m5/verify/zeta_periodized_check.py). The window's transform is
    c(u) = sum_k e^{-i gamma_k u} = e^{-iTu} S_zeta(u),   S_zeta(u) := sum_k e^{-i(gamma_k - T)u},
where the ENVELOPE S is band-limited to |xi| <= W/2 (Nyquist spacing pi/(W/2) ~ 0.16 in u) while
c itself oscillates on the scale 2pi/T ~ 0.0018 — so the least-squares match is done on the envelope
(the first version of this script fitted c on a 0.013-grid and aliased; recorded in the note).
Candidate: a marks-{1,2} configuration inside the window with N_d/N closest to 5/6
(26 simples + 7 doubles: N_d/N = 0.825; 28 + 6: 0.85), free positions tau_j,
    S_c(u) = sum_j m_j e^{-i(tau_j - T)u}.
Theorem F1(b): E(u) := S_c(u) - S_zeta(u) cannot vanish on any interval (e^{-iTu}E is a nonzero
entire function), so the least-squares residual of E on a grid of u in (0, L] that avoids the prime
atoms +-log n (where a free positive pi_L could absorb a mismatch; excluded radius 0.1/n, a fixed
fraction of the local atom spacing 1/n) is bounded below by a positive number for every L.
We measure that floor:
    r(L) := min over positions of RMS_grid |E|, absolute and relative to RMS_grid |S_zeta|,
and check every fit OFF the grid (max |E| on a 4x finer grid including the excluded windows).
Control (zoo V.4): the same fit with 40 simple marks from a perturbed start — must recover the
zeta positions (residual ~0, positions ~exact) once the Slepian count LW/pi exceeds 40, and is
allowed to find OTHER positions with residual ~0 below the count (that is the "free regime").
scipy least_squares with an analytic Jacobian; multi-start; < 10 minutes on one process.
"""
import numpy as np, mpmath, time, json
from scipy.optimize import least_squares
t0 = time.time()
rng = np.random.default_rng(20260925)
n0, N = 3000, 40
gam = np.array([float(mpmath.zetazero(n).imag) for n in range(n0, n0 + N)])
T = gam.mean(); ell = np.log(T/(2*np.pi)); W = gam[-1] - gam[0]
print(f"zeros n = {n0}..{n0+N-1}: T = {T:.3f}, ell = log(T/2pi) = {ell:.4f}, window length W = {W:.3f}, mean gap {W/(N-1):.5f} vs 2pi/ell = {2*np.pi/ell:.5f}")
print(f"zetazero time {time.time()-t0:.1f} s; envelope Nyquist spacing pi/(W/2) = {np.pi/(W/2):.4f}; grid spacing 0.02")
lo, hi = gam[0] - 1.0, gam[-1] + 1.0
def grid(L, h=0.02, c=0.1):
    u = np.arange(h, L + h/2, h); keep = np.ones_like(u, dtype=bool); n = 2
    while np.log(n) < L + 1:
        keep &= np.abs(u - np.log(n)) > c/n; n += 1
    return u[keep]
def env(tau, marks, u):   # S(u) = sum m_j e^{-i (tau_j - T) u}
    return (marks[:, None] * np.exp(-1j*np.outer(tau - T, u))).sum(0)
def fit(marks, u, S, starts):
    best = None
    def res(tau):
        E = env(tau, marks, u) - S
        return np.concatenate([E.real, E.imag])
    def jac(tau):
        ph = np.exp(-1j*np.outer(u, tau - T)) * marks[None, :] * (-1j*u[:, None])   # dS/dtau_j
        return np.vstack([ph.real, ph.imag])
    for s in starts:
        r = least_squares(res, s, jac=jac, bounds=(lo, hi), method='trf', xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=600)
        v = np.sqrt(np.mean(np.abs(env(r.x, marks, u) - S)**2))
        if best is None or v < best[0]: best = (v, r.x)
    return best
def merge_starts(n_double, k=10):
    gaps = np.diff(gam); out = []
    choices = [np.argsort(gaps)[:n_double]] + [rng.choice(N - 1, n_double, replace=False) for _ in range(k - 1)]
    for ch in choices:
        used = set(); pts = []; marks = []
        for i in sorted(ch):
            if i in used or i + 1 in used: continue
            used.update({i, i + 1}); pts.append(0.5*(gam[i] + gam[i+1])); marks.append(2)
        for i in range(N):
            if i not in used: pts.append(gam[i]); marks.append(1)
        while marks.count(2) < n_double:
            j = [i for i, m in enumerate(marks) if m == 1]; a, b = rng.choice(j, 2, replace=False)
            pts[a] = 0.5*(pts[a] + pts[b]); marks[a] = 2; del pts[b]; del marks[b]
        idx = np.argsort(pts); out.append((np.array(pts)[idx], np.array(marks)[idx]))
    return out
def offgrid(tau, marks, L):
    uu = np.arange(0.005, L, 0.005); Sz = env(gam, np.ones(N), uu)
    return np.max(np.abs(env(tau, marks, uu) - Sz)), np.sqrt(np.mean(np.abs(Sz)**2))
results = {"gamma": gam.tolist(), "T": T, "ell": ell, "W": W}
Ls = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, ell, 8.0, 12.0]
for n_double in (7, 6):
    key = f"{N-2*n_double}s+{n_double}d"; nd = N - n_double
    print(f"\n=== configuration {key}: N_d = {nd}, mass {N}, N_d/N = {nd/N:.4f} ===")
    results[key] = {}
    for L in Ls:
        u = grid(L); S = env(gam, np.ones(N), u); Sn = np.sqrt(np.mean(np.abs(S)**2))
        starts = merge_starts(n_double, k=8); marks = starts[0][1].astype(float)
        st = [s[0] for s in starts] + [np.sort(rng.uniform(lo, hi, nd)) for _ in range(4)]
        v, x = fit(marks, u, S, st); og, _ = offgrid(x, marks, L)
        results[key][f"{L:.4f}"] = {"rms_residual": float(v), "rms_S": float(Sn), "relative": float(v/Sn), "offgrid_max": float(og), "n_grid": int(len(u)), "count_LW_over_pi": float(L*W/np.pi)}
        print(f"  L = {L:6.3f} (alpha = {L/ell:.3f}; count LW/pi = {L*W/np.pi:6.1f} vs {nd} positions): min RMS |E| = {v:.3e}  "
              f"(RMS S = {Sn:.3f}; relative {v/Sn:.3e}; off-grid max |E| = {og:.3e}; grid {len(u)})   [{time.time()-t0:.0f} s]")
print("\n=== control (zoo V.4): 40 simple marks, perturbed start (sigma = 0.15) ===")
results["control"] = {}
for L in (1.0, 2.0, 3.0, 3.5, 5.0, ell, 12.0):
    u = grid(L); S = env(gam, np.ones(N), u)
    st = [np.sort(gam + rng.normal(0, 0.15, N)) for _ in range(4)]
    v, x = fit(np.ones(N), u, S, st); og, _ = offgrid(x, np.ones(N), L); dev = np.max(np.abs(np.sort(x) - gam))
    results["control"][f"{L:.4f}"] = {"rms_residual": float(v), "offgrid_max": float(og), "max_position_dev": float(dev), "count_LW_over_pi": float(L*W/np.pi)}
    print(f"  L = {L:6.3f} (count {L*W/np.pi:6.1f} vs 40): min RMS |E| = {v:.3e}; off-grid max |E| = {og:.3e}; max |tau - gamma| = {dev:.2e}"
          + ("   <- positions recovered" if dev < 1e-4 else "   <- OTHER positions with the same band envelope (free regime)" if og < 1e-5 else ""))
json.dump(results, open("window_residual_out.json", "w"), indent=1)
print(f"\ntotal {time.time()-t0:.1f} s")
