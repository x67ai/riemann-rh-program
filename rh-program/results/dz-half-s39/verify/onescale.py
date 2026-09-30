#!/usr/bin/env python3
"""onescale.py — the one-scale variance two ways, and the Lemma 2.1 identity on realized systems. Unit dz-half-s39.
Part A (grid): for x = 6..22 and kappa in {0.7, 1.0, 2.4}, n0 in {no 1.5, with 1.5}: sigma^2 as the exact sum over DZ's grid
  cells in (x/2, x] (way 1) vs the continuum integral int f c^2 (way 2) vs (x/log x) I(kappa; n0) (Theorem-B asymptotic).
Part B (realized): for a run prefix and x = 2^m: (a) the identity N(x) = N^c(x) + sum_{q in B} n0(x/q) checked exactly
  (N^c by re-enumerating P minus the block); (b) resample the block (Poisson process with intensity f on (x/2, x]) R times,
  E'(x) = N^c(x) + sum n0(x/q') - rho^c x exp(S'), compare Var(E') with sigma^2_cont (kappa = rho^c e^mu), check normality,
  and locate the realized E(x) in that conditional law.
Usage: onescale.py A | onescale.py B PREFIX TEMPLATE
"""
import sys, json, math, subprocess
import numpy as np
from scipy import stats
from dzcommon import f_template, envelope

GX, GW = np.polynomial.legendre.leggauss(8)

def cell_masses(f, lo, hi):
    mid, half = 0.5 * (lo + hi), 0.5 * (hi - lo)
    return sum(w * f(mid + half * g) for g, w in zip(GX, GW)) * half

def n0_of(y, has15):
    return 1.0 + (has15 & (y >= 1.5))

def cfun(v, x, kappa, has15):
    return n0_of(x / v, has15) - kappa * x * (-np.log1p(-1.0 / v))

def sigma2_grid(f, x, kappa, has15):
    pts = []
    for n in range(int(math.floor(x / 2)) - 1, int(math.ceil(x)) + 1):
        if n < 1:
            continue
        pts.append(n + np.arange(1 if n == 1 else 0, 2 ** n) / 2.0 ** n)
    v = np.concatenate(pts); lo = np.concatenate(([v[0] - 1e-9], v[:-1]))
    m = (v > x / 2) & (v <= x)
    p = cell_masses(f, lo[m], v[m])
    return float(np.sum(p * (1 - p) * cfun(v[m], x, kappa, has15) ** 2)), int(m.sum())

def sigma2_cont(f, x, kappa, has15, n=200001):
    brk = sorted({x / 2, x / 1.5, x})
    tot = 0.0
    for a, b in zip(brk[:-1], brk[1:]):
        t = np.linspace(a, b, n); y = f(t) * cfun(t, x, kappa, has15) ** 2
        y[-1] = f(np.array([b]))[0] * cfun(np.array([b - 1e-12 * b]), x, kappa, has15)[0] ** 2
        tot += np.trapezoid(y, t)
    return float(tot)

def I_kappa(kappa, has15):
    return (1 - (2 * math.log(1.5) + 4 * math.log(4 / 3)) * kappa + kappa ** 2) if has15 else (0.5 - 2 * kappa * math.log(2) + kappa ** 2)

def partA():
    f = f_template("R"); rows = []
    for x in [6, 8, 10, 12, 14, 16, 18, 20, 22]:
        for kappa in [0.7, 1.0, 2.4]:
            for has15 in [False, True]:
                g, npts = sigma2_grid(f, float(x), kappa, has15)
                c = sigma2_cont(f, float(x), kappa, has15)
                rows.append(dict(x=x, kappa=kappa, has15=has15, grid_points=npts, grid=g, cont=c,
                                 rel=(g - c) / c, asym=x / math.log(x) * I_kappa(kappa, has15)))
    for r in rows:
        print("x=%2d kappa=%.1f 1.5:%d pts=%8d grid=%.10g cont=%.10g rel=%+.2e asym=%.5g" % (
            r["x"], r["kappa"], r["has15"], r["grid_points"], r["grid"], r["cont"], r["rel"], r["asym"]))
    json.dump(rows, open("data/onescale_A.json", "w"), indent=1)

def poisson_block(name, f, x, rng):
    M = envelope(name, x / 2); k = rng.poisson(M * x / 2)
    u = x / 2 + (x / 2) * rng.random(k)
    return u[rng.random(k) < f(u) / M]

def partB(prefix, name, ms=(14, 17, 20, 23), reps=(4000, 4000, 2000, 500)):
    f = f_template(name); meta = json.load(open(prefix + ".json")); rho = meta["rho"]
    P = np.fromfile(prefix + ".primes.f64"); has15 = bool(np.any(P == 1.5))
    cnt = np.fromfile(prefix + ".i64", dtype=np.int64); K = 1024
    rng = np.random.default_rng([meta["seed"], 99, 20261001]); out = []
    for m, R in zip(ms, reps):
        x = 2.0 ** m
        Nx = 1 + int(np.sum(cnt[: m * K]))                   # bins of blocks 0..m-1 end at 2^m
        inB = (P > x / 2) & (P <= x); Bq = P[inB]
        Pc = P[(~inB) & (P <= x)]; Pc.tofile("data/_onescale_c.f64")
        r = subprocess.run(["./dzcount", "data/_onescale_c.f64", str(x), str(K), str(m), "data/_onescale_c.i64"],
                           capture_output=True, text=True, check=True)
        Nc = 1 + int(np.sum(np.fromfile("data/_onescale_c.i64", dtype=np.int64)))
        ident = Nx - (Nc + int(np.sum(n0_of(x / Bq, has15))))
        rhoc = rho * float(np.prod(1 - 1.0 / Bq))
        aB = -np.log1p(-1.0 / Bq); E_real = Nx - rho * x
        Es = np.empty(R)
        for t in range(R):
            q = poisson_block(name, f, x, rng)
            Es[t] = Nc + np.sum(n0_of(x / q, has15)) - rhoc * x * math.exp(np.sum(-np.log1p(-1.0 / q)))
        tt = np.linspace(x / 2, x, 400001); mu = float(np.trapezoid(f(tt) * -np.log1p(-1.0 / tt), tt))
        kappa = rhoc * math.exp(mu); s2 = sigma2_cont(f, x, kappa, has15)
        z = (Es - Es.mean()) / Es.std()
        row = dict(prefix=prefix, m=m, x=x, reps=R, N=Nx, Nc=Nc, identity_residual=ident, block_primes=int(Bq.size),
                   has15=has15, rho=rho, rhoc=rhoc, kappa=kappa, sigma2_cont=s2, asym=x / math.log(x) * I_kappa(kappa, has15),
                   var_emp=float(Es.var(ddof=1)), ratio=float(Es.var(ddof=1) / s2), skew=float(stats.skew(Es)),
                   exkurt=float(stats.kurtosis(Es)), ks_p=float(stats.kstest(z, "norm").pvalue),
                   E_real=E_real, z_real=float((E_real - Es.mean()) / Es.std()), mean_cond=float(Es.mean()))
        out.append(row); print(json.dumps(row))
    json.dump(out, open(prefix + ".onescale.json", "w"), indent=1)

if __name__ == "__main__":
    partA() if sys.argv[1] == "A" else partB(sys.argv[2], sys.argv[3])
