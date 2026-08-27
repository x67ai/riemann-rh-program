#!/usr/bin/env python3
"""
A4 M2 gate -- column_gen.py (SPEC 3.3): pricing search / column generation.

Master LP alternates with a pricing search: minimize the reduced cost over
configuration space by multi-start local optimization in positions (analytic
gradients of all kernel sums) plus discrete neighborhood moves in marks/depths.
Stop when S restarts produce no column with reduced cost < -1e-6.

Reduced cost of configuration c against a master solution's duals:
  rc(c) = N_d(c)/N - y0 - wF1*F1(c) - wFp*Fp(c) - wCp*Cp(c)
          - sum_V yV*n(V;c) - sum_j wT2_j*|c_j|^2
(w* are signed combinations of the hi/lo row duals; yV <= 0 ladder duals.)
The smooth part (everything except n(V)) is minimized by L-BFGS-B with the
analytic gradient below; the exact rc (with ladder counts) is scored after.

Gradient: with cf_s = c_s (full index, cf_{-s} = conj cf_s),
  d rc / d theta_i = 2 Re sum_{s>=1} K_s * (-2 pi i s / N) * phi_i(s),
  phi_i(s) = m_i e^{-2 pi i s theta_i/N} (x 2 cosh(2 pi s d_i / N) for pairs),
  K_s = wF1*2*a1(s)*conj(c_s) + wFp*2*ap(s)*conj(c_s) + wT2_s*2*conj(c_s)
        + wCp * D_s,   D_s = dCp/dcf_s (three W3 contractions).
Verified against finite differences (self-test).
"""
import math
import time
from multiprocessing import Pool

import numpy as np
from scipy.optimize import minimize

from kernels import (Geometry, Config, make_config, c_coeffs, c_full, rows_for,
                     frob, cubic)
from dictionary import DEPTH_GRID

RC_TOL = -1e-6


# ---------------------------------------------------------------- dual coefficients
def dual_coeffs(sol, p):
    """Signed dual weights from a solve_master solution."""
    names = sol["row_names"]
    lam = sol["duals_ub"]
    w = dict(y0=float(sol["duals_eq"][0]), wF1=0.0, wFp=0.0, wCp=0.0,
             yV={}, wT2=None)
    wT2 = {}
    for i, nm in enumerate(names):
        L = float(lam[i])
        if L == 0.0:
            continue
        if nm == "F1_hi":
            w["wF1"] += L
        elif nm == "F1_lo":
            w["wF1"] -= L
        elif nm == "Fp_hi":
            w["wFp"] += L
        elif nm == "Fp_lo":
            w["wFp"] -= L
        elif nm.startswith("Cp_hi"):
            w["wCp"] += L
        elif nm.startswith("Cp_lo"):
            w["wCp"] -= L
        elif nm.startswith("lad_V"):
            w["yV"][int(nm[5:])] = L
        elif nm.startswith("t2_hi_j"):
            wT2[int(nm[7:])] = wT2.get(int(nm[7:]), 0.0) + L
        elif nm.startswith("t2_lo_j"):
            wT2[int(nm[7:])] = wT2.get(int(nm[7:]), 0.0) - L
    w["wT2"] = wT2 if wT2 else None
    return w


def rc_exact(cfg, geom, w, p):
    """Exact reduced cost (includes ladder counts)."""
    r, _ = rows_for(cfg, geom)
    rc = r.Nd / p.N - w["y0"] - w["wF1"] * r.F1 - w["wFp"] * r.Fp \
        - w["wCp"] * r.Cp
    for i, V in enumerate(p.Vgrid):
        L = w["yV"].get(V, 0.0)
        if L:
            rc -= L * float(r.nV[i])
    if w["wT2"]:
        c = c_coeffs(cfg, geom.smax)
        for j, wt in w["wT2"].items():
            rc -= wt * float(np.abs(c[j]) ** 2)
    return rc, r


# ---------------------------------------------------------------- smooth part + grad
def rc_smooth_grad(theta, skel, geom, w):
    """Smooth reduced-cost part and gradient w.r.t. all positions.
    skel: (n_atoms, atom_mrk, pair_mrk, pair_d); theta = concat positions."""
    na = len(skel["atom_mrk"])
    ap_ = theta[:na] % geom.N
    pp_ = theta[na:] % geom.N
    cfg = Config(geom.N, ap_, skel["atom_mrk"], pp_, skel["pair_mrk"],
                 skel["pair_d"])
    smax = geom.smax
    c = c_coeffs(cfg, smax)
    J1, Jp = geom.J1, geom.Jp
    F1 = frob(c, geom.a1, J1)
    Fp = frob(c, geom.ap, Jp)
    Cp = cubic(c, geom.W3p, Jp)
    val = cfg.n_distinct() / geom.N - w["y0"] - w["wF1"] * F1 \
        - w["wFp"] * Fp - w["wCp"] * Cp
    if w["wT2"]:
        for j, wt in w["wT2"].items():
            val -= wt * float(np.abs(c[j]) ** 2)
    # K_s kernel, s = 1..smax
    s = np.arange(1, smax + 1)
    K = np.zeros(smax + 1, dtype=complex)     # index s
    # |c|^2 rows: a1 support 2J1, ap support 2Jp
    A1 = np.zeros(smax + 1)
    A1[: 2 * J1 + 1] = geom.a1[2 * J1:]
    Ap = np.zeros(smax + 1)
    Ap[: 2 * Jp + 1] = geom.ap[2 * Jp:]
    K += -(w["wF1"] * 2 * A1 + w["wFp"] * 2 * Ap) * np.conj(c)
    if w["wT2"]:
        for j, wt in w["wT2"].items():
            K[j] += -wt * np.conj(c[j])   # single positive-j row: no +/-s doubling
    if w["wCp"] != 0.0:
        # D_s = dCp/dcf_s, three W3 contractions on full index
        n4 = 4 * Jp + 1
        cf = c_full(c[: 2 * Jp + 1])           # index a+2Jp, a in [-2Jp, 2Jp]
        W3 = geom.W3p
        # term1: sum_b W3[k,b] cf_b cf_{-k-b}; term2: sum_a W3[a,k] cf_a cf_{-a-k}
        # term3: sum_{a+b=-k} W3[a,b] cf_a cf_b
        idx = np.arange(n4)
        D = np.zeros(n4, dtype=complex)        # index k+2Jp
        # cf_{-k-b}: index (-k-b)+2Jp = 4Jp - (k+2Jp) - (b+2Jp) + 2Jp
        for ki in range(n4):
            k = ki - 2 * Jp
            bi = idx
            mi = 4 * Jp - ki - bi + 2 * Jp     # index of -k-b
            ok = (mi >= 0) & (mi < n4)
            D[ki] += np.sum(W3[ki, bi[ok]] * cf[bi[ok]] * cf[mi[ok]])
            D[ki] += np.sum(W3[bi[ok], ki] * cf[bi[ok]] * cf[mi[ok]])
            # term3: a + b = -k: b = -k - a: index bi3 = mi again with roles swapped
            ai = idx
            bi3 = 4 * Jp - ki - ai + 2 * Jp
            ok3 = (bi3 >= 0) & (bi3 < n4)
            D[ki] += np.sum(W3[ai[ok3], bi3[ok3]] * cf[ai[ok3]] * cf[bi3[ok3]])
        # fold into K at positive s: dCp/dtheta = 2 Re sum_{s>=1} Dpos_s cdot_s
        # where Dpos_s = D at cf index s (since cf_{-s}-terms are conjugates)
        Dpos = np.zeros(smax + 1, dtype=complex)
        Dpos[1: 2 * Jp + 1] = D[2 * Jp + 1:]
        K += -w["wCp"] * Dpos
    # gradient: for each position i, sum_s 2 Re(K_s * (-2 pi i s/N) phi_i(s))
    grad = np.zeros(len(theta))
    fac = -2j * np.pi * s / geom.N
    if na:
        ph = np.exp(-2j * np.pi * np.outer(s, ap_) / geom.N) * \
            skel["atom_mrk"][None, :].astype(float)
        grad[:na] = 2 * np.real((K[1:] * fac) @ ph)
    if len(pp_):
        ph = np.exp(-2j * np.pi * np.outer(s, pp_) / geom.N) * \
            (2 * skel["pair_mrk"][None, :].astype(float)) * \
            np.cosh(2 * np.pi * np.outer(s, skel["pair_d"]) / geom.N)
        grad[na:] = 2 * np.real((K[1:] * fac) @ ph)
    # note: val/grad exclude ladder terms (piecewise constant)
    return val, grad


def local_opt(skel, theta0, geom, w, maxiter=120):
    res = minimize(rc_smooth_grad, theta0, args=(skel, geom, w),
                   jac=True, method="L-BFGS-B",
                   options=dict(maxiter=maxiter, ftol=1e-12, gtol=1e-9))
    return res.x


# ---------------------------------------------------------------- discrete moves
def to_cfg(skel, theta, N, tag=""):
    na = len(skel["atom_mrk"])
    return Config(N, theta[:na] % N, skel["atom_mrk"].copy(),
                  theta[na:] % N, skel["pair_mrk"].copy(),
                  skel["pair_d"].copy(), tag)


def cfg_to_skel(cfg):
    return (dict(atom_mrk=cfg.atom_mrk.copy(), pair_mrk=cfg.pair_mrk.copy(),
                 pair_d=cfg.pair_d.copy()),
            np.concatenate([cfg.atom_pos, cfg.pair_pos]))


def discrete_moves(cfg, geom, w, p, rng, tries=24):
    """Candidate mark/depth moves around cfg; return best (rc, cfg) found."""
    best_rc, _ = rc_exact(cfg, geom, w, p)
    best = None
    Wcap = p.Wcap
    pm_cap = max(1, Wcap // 2)
    N = geom.N
    for _ in range(tries):
        a_pos = list(cfg.atom_pos); a_m = list(cfg.atom_mrk)
        p_pos = list(cfg.pair_pos); p_m = list(cfg.pair_mrk)
        p_d = list(cfg.pair_d)
        kind = rng.integers(0, 6)
        try:
            if kind == 0 and len(a_pos) >= 2:      # merge two atoms
                i, j = rng.choice(len(a_pos), 2, replace=False)
                if a_m[i] + a_m[j] <= Wcap:
                    a_m[i] += a_m[j]
                    del a_pos[j], a_m[j]
                else:
                    continue
            elif kind == 1 and a_pos:              # split an atom
                i = rng.integers(0, len(a_pos))
                if a_m[i] >= 2:
                    m1 = rng.integers(1, a_m[i])
                    a_pos.append(a_pos[i] + rng.uniform(0.15, 0.6))
                    a_m.append(a_m[i] - m1)
                    a_m[i] = m1
                else:
                    continue
            elif kind == 2 and a_pos:              # double -> pair
                cand = [i for i in range(len(a_pos)) if a_m[i] % 2 == 0
                        and a_m[i] // 2 <= pm_cap]
                if not cand:
                    continue
                i = cand[rng.integers(0, len(cand))]
                wd = DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]
                p_pos.append(a_pos[i]); p_m.append(a_m[i] // 2)
                p_d.append(geom.depth_from_w(wd))
                del a_pos[i], a_m[i]
            elif kind == 3 and p_pos:              # pair -> atom (double)
                i = rng.integers(0, len(p_pos))
                if 2 * p_m[i] <= Wcap:
                    a_pos.append(p_pos[i]); a_m.append(2 * p_m[i])
                    del p_pos[i], p_m[i], p_d[i]
                else:
                    continue
            elif kind == 4 and p_pos:              # pair depth move
                i = rng.integers(0, len(p_pos))
                wd = DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]
                p_d[i] = geom.depth_from_w(wd)
            elif kind == 5 and len(a_pos) >= 2:    # mark transfer
                i, j = rng.choice(len(a_pos), 2, replace=False)
                if a_m[i] >= 2 and a_m[j] + 1 <= Wcap:
                    a_m[i] -= 1; a_m[j] += 1
                    if a_m[i] == 0:
                        del a_pos[i], a_m[i]
                else:
                    continue
            else:
                continue
        except ValueError:
            continue
        cand = make_config(N, atoms=list(zip(a_pos, a_m)),
                           pairs=list(zip(p_pos, p_m, p_d)), tag="cg")
        if cand.mass() != N:
            continue
        rc, _ = rc_exact(cand, geom, w, p)
        if rc < best_rc - 1e-9:
            best_rc, best = rc, cand
    return best_rc, best


# ---------------------------------------------------------------- restart skeletons
def random_skeleton(N, Wcap, geom, rng, support_cfgs=None):
    """One restart's starting configuration."""
    mode = rng.integers(0, 4)
    if mode == 0 and support_cfgs:
        cfg = support_cfgs[rng.integers(0, len(support_cfgs))]
        skel, theta = cfg_to_skel(cfg)
        theta = theta + rng.normal(0, 0.35, len(theta))
        return skel, theta
    # targeted doubles corner with decorations
    if mode == 1:
        k = int(rng.integers(max(0, N // 6 - 4), N // 6 + 6))
        n3 = int(rng.integers(0, 3)) if Wcap >= 3 else 0
        npr = int(rng.integers(0, 3))
        mass = N - 2 * k - 3 * n3 - 2 * npr
        if mass < 0:
            k = N // 6; n3 = 0; npr = 0; mass = N - 2 * k
        marks = [2] * k + [3] * n3 + [1] * mass
        atoms = [(rng.uniform(0, N), m) for m in marks]
        pairs = [(rng.uniform(0, N), 1,
                  geom.depth_from_w(DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]))
                 for _ in range(npr)]
        cfg = make_config(N, atoms=atoms, pairs=pairs)
        return cfg_to_skel(cfg)
    # random composition
    mass = N
    atoms, pairs = [], []
    k2 = int(rng.integers(0, N // 3))
    mass -= 2 * k2
    atoms += [(rng.uniform(0, N), 2) for _ in range(k2)]
    for m in range(3, Wcap + 1):
        km = int(rng.integers(0, 3))
        km = min(km, mass // m)
        mass -= m * km
        atoms += [(rng.uniform(0, N), m) for _ in range(km)]
    npr = min(int(rng.integers(0, 4)), mass // 2)
    mass -= 2 * npr
    pairs = [(rng.uniform(0, N), 1,
              geom.depth_from_w(DEPTH_GRID[rng.integers(0, len(DEPTH_GRID))]))
             for _ in range(npr)]
    atoms += [(rng.uniform(0, N), 1) for _ in range(mass)]
    cfg = make_config(N, atoms=atoms, pairs=pairs)
    return cfg_to_skel(cfg)


# ---------------------------------------------------------------- worker
_GEOM_CACHE = {}


def _get_geom(desc):
    if desc not in _GEOM_CACHE:
        N, lam1, lamp, win1, winp = desc
        _GEOM_CACHE[desc] = Geometry(N, lam1, lamp, win1, winp)
    return _GEOM_CACHE[desc]


def _restart_task(args):
    """One pricing restart. args = (seed, geom_desc, w, p, support_blobs)."""
    seed, desc, w, p, support_blobs = args
    geom = _get_geom(desc)
    support = [Config(geom.N, np.array(b[0]), np.array(b[1], dtype=int),
                      np.array(b[2]), np.array(b[3], dtype=int),
                      np.array(b[4])) for b in support_blobs]
    rng = np.random.default_rng(seed)
    skel, theta0 = random_skeleton(geom.N, p.Wcap, geom, rng, support or None)
    try:
        theta = local_opt(skel, theta0, geom, w)
    except Exception:
        return None
    cfg = to_cfg(skel, theta, geom.N, tag="cg")
    rc, _ = rc_exact(cfg, geom, w, p)
    best_rc, best_cfg = rc, cfg
    # discrete move rounds
    for _ in range(3):
        rc2, cand = discrete_moves(best_cfg, geom, w, p, rng)
        if cand is None:
            break
        skel2, th2 = cfg_to_skel(cand)
        try:
            th2 = local_opt(skel2, th2, geom, w, maxiter=60)
        except Exception:
            pass
        cand2 = to_cfg(skel2, th2, geom.N, tag="cg")
        rc3, _ = rc_exact(cand2, geom, w, p)
        if min(rc2, rc3) < best_rc - 1e-9:
            best_rc = min(rc2, rc3)
            best_cfg = cand2 if rc3 <= rc2 else cand
        else:
            break
    return best_rc, (best_cfg.atom_pos.tolist(), best_cfg.atom_mrk.tolist(),
                     best_cfg.pair_pos.tolist(), best_cfg.pair_mrk.tolist(),
                     best_cfg.pair_d.tolist())


def cfg_blob(cfg):
    return (cfg.atom_pos.tolist(), cfg.atom_mrk.tolist(),
            cfg.pair_pos.tolist(), cfg.pair_mrk.tolist(), cfg.pair_d.tolist())


def price(geom, w, p, support_cfgs, S, pool, seed0=0):
    """S restarts on a persistent pool; return [(rc, Config)] with rc < RC_TOL."""
    desc = (geom.N, geom.lam1, geom.lamp, geom.win1, geom.winp)
    blobs = [cfg_blob(c) for c in (support_cfgs or [])]
    tasks = [(int(seed0 + i), desc, w, p, blobs) for i in range(S)]
    results = pool.map(_restart_task, tasks)
    found = []
    for r in results:
        if r is None:
            continue
        rc, tup = r
        if rc < RC_TOL:
            cfg = Config(geom.N, np.array(tup[0]), np.array(tup[1], dtype=int),
                         np.array(tup[2]), np.array(tup[3], dtype=int),
                         np.array(tup[4]), tag=f"cg_rc{rc:.5f}")
            found.append((rc, cfg))
    found.sort(key=lambda t: t[0])
    return found


# ---------------------------------------------------------------- self-test
if __name__ == "__main__":
    # gradient check vs finite differences
    N = 64
    geom = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    rng = np.random.default_rng(7)
    w = dict(y0=0.3, wF1=-0.004, wFp=0.002, wCp=-0.0007, yV={}, wT2={3: 0.001, 17: -0.002})
    from master_lp import GateParams
    p = GateParams(N=N, budgets=(85.3, 138.7, 320.0))
    skel, theta = random_skeleton(N, 8, geom, rng)
    v0, g0 = rc_smooth_grad(theta, skel, geom, w)
    gfd = np.zeros_like(theta)
    h = 1e-6
    for i in range(len(theta)):
        tp = theta.copy(); tp[i] += h
        vp, _ = rc_smooth_grad(tp, skel, geom, w)
        tm = theta.copy(); tm[i] -= h
        vm, _ = rc_smooth_grad(tm, skel, geom, w)
        gfd[i] = (vp - vm) / (2 * h)
    err = np.max(np.abs(g0 - gfd)) / max(1e-12, np.max(np.abs(gfd)))
    print(f"gradient check: rel err = {err:.2e} (n_pos={len(theta)})")
    assert err < 1e-5, "gradient mismatch"
    t0 = time.time()
    th = local_opt(skel, theta, geom, w)
    v1, _ = rc_smooth_grad(th, skel, geom, w)
    print(f"local opt: {v0:.6f} -> {v1:.6f} in {time.time()-t0:.2f}s")
