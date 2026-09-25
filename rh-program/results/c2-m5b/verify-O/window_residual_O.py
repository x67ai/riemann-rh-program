#!/usr/bin/env python3
"""window_residual_O.py — the Opus reader's independent companion to FORMULATION.md §1.4.
Own design, differing from the writer's on purpose:
 (1) zeros recomputed with mpmath.zetazero (n = 3000..3039) and compared with the writer's JSON;
 (2) data = the demodulated envelope S(u) = sum_k e^{-i(gamma_k - T)u} on a uniform grid u in (0, L], spacing 0.04
     (4x oversampled against the Nyquist spacing pi/(W/2) = 0.16), NO exclusion around +-log n (the windowed envelope has
     no prime atoms; the exclusion is immaterial for this object — a variant with the writer's exclusion is also run at 3 L's);
 (3) optimizer: bounded trust-region ('trf', x_scale='jac'; an unbounded Levenberg-Marquardt first run aliased, see (3')) with CONTINUATION in L — every L is started from the best solutions
     at the neighboring L's (an ascending and a descending sweep) as well as from 12 fresh merge-starts;
 (4) the Jacobian's singular-value spectrum at zeta's own positions (40 simples) as a function of L: the number of
     singular values above 1e-6 * the largest is the numerically identifiable number of position parameters — the
     prolate/Slepian count computed rather than inferred;
 (5) control (zoo V.4): 40 simples from perturbed starts sigma = 0.15 and 0.5, report deviation, residual and nfev.
"""
import numpy as np, mpmath, time, json
from scipy.optimize import least_squares
t0 = time.time(); rng = np.random.default_rng(777)
N = 40
gam = np.array([float(mpmath.zetazero(n).imag) for n in range(3000, 3040)])
wr = json.load(open("../verify/window_residual_out.json"))
print(f"zeros recomputed in {time.time()-t0:.1f} s; max |gamma - writer's gamma| = {np.max(np.abs(gam - np.array(wr['gamma']))):.2e}")
T = gam.mean(); W = gam[-1] - gam[0]; ell = np.log(T/(2*np.pi))
print(f"T = {T:.3f}, ell = {ell:.4f}, W = {W:.3f}, W*ell/2pi = {W*ell/(2*np.pi):.2f}")
def grid(L, h=0.04, excl=False):
    u = np.arange(h, L + 1e-9, h)
    if excl:
        keep = np.ones_like(u, bool); n = 2
        while np.log(n) < L + 1: keep &= np.abs(u - np.log(n)) > 0.1/n; n += 1
        u = u[keep]
    return u
def env(tau, m, u): return (m[:, None]*np.exp(-1j*np.outer(tau - T, u))).sum(0)
def solve(m, u, S, starts):
    def res(tau): E = env(tau, m, u) - S; return np.concatenate([E.real, E.imag])
    def jac(tau):
        ph = np.exp(-1j*np.outer(u, tau - T))*m[None, :]*(-1j*u[:, None]); return np.vstack([ph.real, ph.imag])
    out = []
    for s in starts:
        # positions confined to the window [gamma_1 - 1, gamma_40 + 1] (the first run, unbounded LM, let points escape
        # the window and ALIAS on the grid: off-grid max|E| ~ 4 at grid RMS 2e-4 — recorded in the log header)
        s = np.clip(s, gam[0] - 1 + 1e-9, gam[-1] + 1 - 1e-9)
        r = least_squares(res, s, jac=jac, bounds=(gam[0] - 1, gam[-1] + 1), method='trf', x_scale='jac', xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=3000)
        out.append((np.sqrt(np.mean(np.abs(env(r.x, m, u) - S)**2)), r.x, r.nfev))
    out.sort(key=lambda z: z[0]); return out
def merges(nd, k):
    """own merge rule: choose nd disjoint adjacent pairs (random, or the nd smallest gaps greedily), put a double at the pair mean."""
    res = []
    for trial in range(k):
        order = np.argsort(np.diff(gam)) if trial == 0 else rng.permutation(N - 1)
        used, pairs = set(), []
        for i in order:
            if len(pairs) == nd: break
            if i in used or i + 1 in used: continue
            used |= {i, i+1}; pairs.append(i)
        pts = [0.5*(gam[i]+gam[i+1]) for i in pairs] + [gam[i] for i in range(N) if i not in used]
        ms = [2.0]*len(pairs) + [1.0]*(N - 2*len(pairs))
        res.append((np.array(pts), np.array(ms)))
    return res
Ls = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0, ell, 8.0, 12.0]
out = {"gamma": gam.tolist(), "T": T, "W": W, "ell": ell}
# (4) Jacobian spectrum at zeta's positions
print("\n=== (4) Jacobian singular values at zeta's 40 positions (simple marks) ===")
out["svd"] = {}
for L in Ls:
    u = grid(L); ph = np.exp(-1j*np.outer(u, gam - T))*(-1j*u[:, None]); J = np.vstack([ph.real, ph.imag])
    sv = np.linalg.svd(J, compute_uv=False); rel = sv/sv[0]
    k6, k10 = int((rel > 1e-6).sum()), int((rel > 1e-10).sum())
    out["svd"][f"{L:.4f}"] = rel.tolist()
    print(f"  L = {L:6.3f}  count LW/pi = {L*W/np.pi:6.1f}  #sv > 1e-6*max: {k6:2d}   #sv > 1e-10*max: {k10:2d}   smallest rel sv {rel[-1]:.2e}")
# (3) the 1/6-doubles replacement with continuation
for nd in (7, 6):
    key = f"{N-2*nd}s+{nd}d"; m = np.array([2.0]*nd + [1.0]*(N-2*nd))
    print(f"\n=== {key} (N_d = {N-nd}, N_d/N = {(N-nd)/N:.3f}) ===")
    best = {}
    for sweep in ("up", "down"):
        seq = Ls if sweep == "up" else Ls[::-1]; prev = None
        for L in seq:
            u = grid(L); S = env(gam, np.ones(N), u)
            st = [p for p, _ in merges(nd, 12)] if sweep == "up" else []
            if prev is not None: st += [x for _, x, _ in prev[:4]]
            if sweep == "down": st += [best[L][1]]
            sol = solve(m, u, S, st); prev = sol
            if L not in best or sol[0][0] < best[L][0]: best[L] = (sol[0][0], sol[0][1])
    out[key] = {}
    for L in Ls:
        u = grid(L); S = env(gam, np.ones(N), u); Sn = np.sqrt(np.mean(np.abs(S)**2)); v, x = best[L]
        uu = np.arange(0.005, L, 0.005); og = np.max(np.abs(env(x, m, uu) - env(gam, np.ones(N), uu)))
        w = wr[key][f"{L:.4f}"]["relative"]
        out[key][f"{L:.4f}"] = {"rms": float(v), "relative": float(v/Sn), "offgrid_max": float(og), "writer_relative": w}
        print(f"  L = {L:6.3f} (alpha {L/ell:.3f}, count {L*W/np.pi:6.1f}): best RMS|E| = {v:.3e}, relative {v/Sn:.3e} (writer {w:.3e}); off-grid max|E| {og:.3e}")
    # writer's exclusion variant at three L's, warm-started
    for L in (2.0, 3.0, ell):
        u = grid(L, h=0.02, excl=True); S = env(gam, np.ones(N), u); Sn = np.sqrt(np.mean(np.abs(S)**2))
        sol = solve(m, u, S, [best[L][1]] + [p for p, _ in merges(nd, 4)])
        print(f"  [writer's grid 0.02 + exclusion 0.1/n] L = {L:6.3f}: relative {sol[0][0]/Sn:.3e}")
    print(f"  [{time.time()-t0:.0f} s]")
# (5) control
print("\n=== (5) control (V.4): 40 simples ===")
out["control"] = {}
for sig in (0.15, 0.5):
    for L in (1.0, 2.0, 2.5, 3.0, 3.5, 5.0, ell, 12.0):
        u = grid(L); S = env(gam, np.ones(N), u)
        sol = solve(np.ones(N), u, S, [np.sort(gam + rng.normal(0, sig, N)) for _ in range(4)])
        v, x, nf = sol[0]; dev = np.max(np.abs(np.sort(x) - gam))
        out["control"][f"{sig}/{L:.4f}"] = {"rms": float(v), "dev": float(dev), "nfev": int(nf), "bitwise_equal": bool(np.array_equal(np.sort(x), gam))}
        print(f"  sigma {sig}, L = {L:6.3f} (count {L*W/np.pi:6.1f}): best RMS = {v:.3e}, max|tau - gamma| = {dev:.3e}, nfev {nf}, bitwise equal to gamma: {np.array_equal(np.sort(x), gam)}")
json.dump(out, open("window_residual_O_out.json", "w"))
print(f"\ntotal {time.time()-t0:.1f} s")
