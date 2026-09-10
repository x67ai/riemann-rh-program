#!/usr/bin/env python3
"""
C2 M5 pricing -- diagnostic 2 (Session 21, 2026-09-10): does the N-periodic model exclude ZETA ITSELF?

Take N consecutive genuine zeta zeros (mpmath.zetazero, n = n0 .. n0+N-1), periodize them with exactly
N zeros per period (the LP's density row), and apply the same cone rows as cone_rows_check.py:
 (a) the two-tooth test  h = hat_0 + (hat_k + hat_{-k})/2  at every lattice frequency u_k = k ell/N,
     which is a legitimate Sigma_L element and gives  |c_k| <= (N/ell) cosh(u_k/2) [P(tooth_k) + 4 hhat(T)];
 (b) the full cone-test LP at several rotations.
If the periodized zeta configuration is "excluded", the exclusion of the extremal in the periodic
world is a MODEL ARTIFACT (lattice Fourier support vs. prime-power-log support), not a fact about marks.
Also run on the crystal extremal with the same N for side-by-side comparison.
"""
import json, math, time, sys
import numpy as np
import mpmath
from scipy.optimize import linprog

sys.path.insert(0, __file__.rsplit('/', 1)[0])
t0 = time.time()
N = 198          # multiple of 6 so the crystal exists at the same N
n0 = 3000

# ---- genuine zeros
mpmath.mp.dps = 20
zeros = np.array([float(mpmath.zetazero(n).imag) for n in range(n0, n0 + N)])
T = float(zeros.mean())
ell = math.log(T / (2 * math.pi))
gap = (zeros[-1] - zeros[0]) / (N - 1)            # empirical mean gap over the window
period_tau = N * gap
theta = (zeros - zeros[0]) / gap                    # positions in mean-gap units, in [0, N)
print(f"zeros {n0}..{n0+N-1}: T={T:.3f} ell={ell:.4f} mean gap={gap:.5f} (RvM 2pi/ell={2*math.pi/ell:.5f}) elapsed {time.time()-t0:.1f}s", flush=True)

# ---- sieve for P(tooth)
NP = 200000
is_p = np.ones(NP + 1, dtype=bool); is_p[:2] = False
for i in range(2, int(NP ** 0.5) + 1):
    if is_p[i]: is_p[i*i::i] = False
LAM = np.zeros(NP + 1)
for p in np.nonzero(is_p)[0]:
    q = int(p); lp = math.log(q)
    while q <= NP:
        LAM[q] = lp; q *= int(p)
NN = np.arange(NP + 1, dtype=float); LOGN = np.zeros(NP + 1); LOGN[1:] = np.log(NN[1:])
WPRIME = np.zeros(NP + 1); WPRIME[2:] = 4.0 * LAM[2:] / (NN[2:] + 1.0)

def P_tooth(k, D):
    sel = (np.abs(LOGN - k * D) < D) & (NN >= 2)
    return float(np.sum(WPRIME[sel] * (1 - np.abs(LOGN[sel] - k * D) / D)))

def c_coeffs(theta, marks, K, rot=0.0):
    k = np.arange(K)
    return (marks[None, :] * np.exp(-2j * math.pi * np.outer(k, theta + rot) / N)).sum(axis=1)

def cone_lp(obj, K):
    ngrid = 4 * K + 1
    phi = np.linspace(0, math.pi, ngrid); kk = np.arange(1, K)
    A = -np.ones((ngrid, K)); A[:, 1:] = -2 * np.cos(np.outer(phi, kk))
    res = linprog(-obj, A_ub=A, b_ub=np.zeros(ngrid), bounds=[(1, 1)] + [(0, None)] * (K - 1), method="highs")
    if res.status != 0: return None, None
    h = res.x
    phi2 = np.linspace(0, math.pi, 16 * ngrid)
    C = h[0] + 2 * (h[1:] @ np.cos(np.outer(kk, phi2)))
    return h, float(C.min())

OUT = {"N": N, "n0": n0, "T": T, "ell": ell, "gap": gap}
configs = {"zeta_periodized": (theta, np.ones(N)),
           "crystal": (np.arange(N, dtype=float), np.array([2 if s % 6 == 0 else (0 if s % 6 == 3 else 1) for s in range(N)], dtype=float))}
for L_tag, L in [("log2-", 0.999 * math.log(2)), ("2", 2.0), ("4", 4.0), ("ell", ell), ("2ell", 2 * ell)]:
    D = ell / N; K = int(math.floor(L / D))
    ptooth = np.array([P_tooth(k, D) for k in range(K)])
    for name, (th, mk) in configs.items():
        c = c_coeffs(th, mk, K)
        # (a) two-tooth test: |c_k| vs bound
        bound = (N / ell) * np.cosh(np.arange(K) * D / 2) * ptooth
        viol = [(int(k), float(abs(c[k])), float(bound[k]), float(ptooth[k])) for k in range(1, K) if abs(c[k]) > bound[k] + 1e-9]
        prime_free = [int(k) for k in range(1, K) if ptooth[k] == 0.0]
        # (b) LP at rotations
        best = -1e99; best_rot = None; hmin = None
        for rot in np.linspace(0, 6, 12, endpoint=False):
            cr = c_coeffs(th, mk, K, rot)
            e = (ell / N) * np.real(cr) / np.cosh(np.arange(K) * D / 2); e[0] = 0
            obj = e - ptooth * 0.0   # placeholder replaced below
            # P(h) for piecewise-linear h on the lattice = sum_k h_k P(hat_k); hat_k mass identical to tooth_k except k=0 (no primes below D)
            pvec = ptooth.copy(); pvec[0] = 0.0
            obj = e - pvec
            h, cmin = cone_lp(obj, K)
            if h is None: continue
            v = float(obj @ h)
            if v > best: best, best_rot, hmin = v, float(rot), cmin
        rec = {"config": name, "L_tag": L_tag, "L": L, "K": K, "n_prime_free_teeth": len(prime_free),
               "n_two_tooth_violations": len(viol), "worst_two_tooth": max(viol, key=lambda r: r[1] - r[2]) if viol else None,
               "max_c_at_prime_free": max((abs(c[k]) for k in prime_free), default=0.0),
               "LP_max_violation": best, "LP_rot": best_rot, "LP_hhat_min_check": hmin}
        OUT.setdefault("rows", []).append(rec)
        print(f"{name:16s} L={L_tag:5s} K={K:3d} prime-free teeth={len(prime_free):3d} two-tooth violations={len(viol):3d} "
              f"max|c_k| at prime-free k={rec['max_c_at_prime_free']:.3f} LP max[E-P]={best:+.4e} (rot {best_rot}, hhat_min {hmin})", flush=True)
OUT["elapsed_s"] = time.time() - t0
json.dump(OUT, open(__file__.replace("zeta_periodized_check.py", "zeta_periodized_out.json"), "w"), indent=1, default=float)
print(f"elapsed {OUT['elapsed_s']:.1f}s")
