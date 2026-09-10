#!/usr/bin/env python3
"""Exact two-tooth cone rows (PRICING.md Sec. 1.4 (c)): h = hat_0^(d) + (hat_k^(d) + hat_{-k}^(d))/2, tooth width d <= lattice spacing D.
hhat = d sinc^2(xi d/2) (1 + cos(u_k xi)) >= 0 exactly; h >= 0; supp in [-u_k - d, u_k + d].  Row (1.2) in the periodic model:
   |c_k| <= (N/ell) cosh(u_k/2) [P(tooth_k^(d)) + 4 hhat(T)],   P(tooth) = 4 sum_n Lambda(n) hat_k^(d)(log n)/(n+1).
Reports, per configuration and T, the number of lattice modes violating, and the narrow-tooth limit d -> 0 (P -> 0)."""
import math, json, numpy as np
NP = 3_000_000
is_p = np.ones(NP+1, bool); is_p[:2] = False
for i in range(2, int(NP**0.5)+1):
    if is_p[i]: is_p[i*i::i] = False
LAM = np.zeros(NP+1)
for p in np.nonzero(is_p)[0]:
    q = int(p); lp = math.log(q)
    while q <= NP: LAM[q] = lp; q *= int(p)
NN = np.arange(NP+1, dtype=float); LOGN = np.zeros(NP+1); LOGN[1:] = np.log(NN[1:]); W = np.zeros(NP+1); W[2:] = 4*LAM[2:]/(NN[2:]+1)
def P_tooth(u, d):
    sel = (np.abs(LOGN-u) < d) & (NN >= 2)
    return float(np.sum(W[sel]*(1-np.abs(LOGN[sel]-u)/d))) if u - d < math.log(NP) else 4*d  # PNT beyond sieve
N = 192
def marks(kind, rng=None):
    m = np.ones(N, int)
    if kind == "crystal": m[0::6] = 2; m[3::6] = 0
    elif kind == "dipole": m[0::6] = 2; m[1::6] = 0
    else:
        idx = rng.permutation(N); m[idx[:N//6]] = 2; m[idx[N//6:N//3]] = 0
    return m
rng = np.random.default_rng(20260910)
OUT = []
for T in [1e6, 1e12, 1e20]:
    ell = math.log(T/(2*math.pi)); D = ell/N
    for kind in ["crystal", "dipole", "random"]:
        m = marks(kind, rng); k = np.arange(N+1); c = np.abs((m[None,:]*np.exp(-2j*math.pi*np.outer(k, np.arange(N))/N)).sum(1))
        for dfrac in [1.0, 0.1]:
            d = D*dfrac
            bound = np.array([(N/ell)*math.cosh(k_*D/2)*(P_tooth(k_*D, d) + 4*d*np.sinc(T*d/(2*math.pi))**2*abs(math.cos(T*k_*D))) for k_ in range(N+1)])
            for Ltag, L in [("log2-", 0.999*math.log(2)), ("ell/6", ell/6), ("ell/3", ell/3), ("ell", ell)]:
                K = int(L/D)
                ks = [k_ for k_ in range(1, K+1) if c[k_] > bound[k_] + 1e-9]
                nz = [k_ for k_ in range(1, K+1) if c[k_] > 1e-9]
                worst = max(ks, key=lambda k_: c[k_]/max(bound[k_],1e-300)) if ks else None
                rec = dict(T=T, N=N, config=kind, tooth_width_over_D=dfrac, L_tag=Ltag, L=L, K=K, modes_nonzero=len(nz), modes_violating=len(ks),
                           worst_k=worst, worst_c=float(c[worst]) if worst else None, worst_bound=float(bound[worst]) if worst else None,
                           worst_u=worst*D if worst else None)
                OUT.append(rec)
                print(f"T=1e{int(round(math.log10(T)))} {kind:8s} d/D={dfrac:<4} L={Ltag:6s} K={K:3d} nonzero modes={len(nz):3d} violating={len(ks):3d}"
                      + (f"  worst k={worst} u={worst*D:.3f} |c|={c[worst]:.2f} bound={bound[worst]:.3f}" if worst else ""))
json.dump(OUT, open("two_tooth_exact_out.json", "w"), indent=1, default=float)
