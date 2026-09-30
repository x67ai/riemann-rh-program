#!/usr/bin/env python3
"""dzgen.py — one realization of the Diamond–Zhang random g-prime system on the grid (17.13), up to X.
Usage: dzgen.py TEMPLATE(R|C) SEED X OUTPREFIX
Grid Γ = {1} ∪ {n + l/2^n : n >= 1, 0 <= l < 2^n}; cell k = (v_{k-1}, v_k]; p_k = ∫_cell f; X_k ~ Bernoulli(p_k) independent.
Units n <= NEX: every grid point enumerated, p_k by 8-point Gauss-Legendre on the cell, exact Bernoulli draw.
Units n > NEX: Poisson process with intensity f (chunked thinning, envelope checked), each point rounded UP to its grid
point (exact for n <= 45; below float resolution beyond). Total-variation distance to the exact Bernoulli selection
<= sum over cells of p_k^2 <= 2^{-NEX} (NOTE §4.1).
Density: log rho = sum_{p<=X} -log(1-1/p) - Ein(log X) - C_tail(X) + S_tail, where C_tail is the template's oscillatory tail
(0 for R) and S_tail ~ N(m, s^2) is the contribution of the g-primes > X (a sum over a Poisson process of tiny terms;
Gaussian to O((log X / X)^{1/2}) in the Kolmogorov distance), sampled with the same RNG.
Writes OUTPREFIX.primes.f64 (sorted float64) and OUTPREFIX.json.
"""
import sys, json, math, time
import numpy as np
from dzcommon import fR, fC, f_template, envelope, Ein, g_of_logu

NEX = 22

def exact_units(f, rng):
    gx, gw = np.polynomial.legendre.leggauss(8)
    primes, probs_max = [], 0.0
    prev = 1.0
    for n in range(1, NEX + 1):
        l0 = 1 if n == 1 else 0
        v = n + np.arange(l0, 2 ** n, dtype=float) / 2.0 ** n
        lo = np.concatenate(([prev], v[:-1])); hi = v
        mid = 0.5 * (lo + hi); half = 0.5 * (hi - lo)
        p = np.zeros_like(v)
        for xi, wi in zip(gx, gw):
            p += wi * f(mid + half * xi)
        p *= half
        probs_max = max(probs_max, float(p.max()))
        sel = rng.random(v.size) < p
        primes.append(v[sel]); prev = float(v[-1])
    return np.concatenate(primes), prev, probs_max

def round_up_to_grid(u):
    n = np.floor(u)
    out = u.copy()
    m = n <= 45
    if m.any():
        nn = n[m]; scale = np.exp2(nn)
        out[m] = nn + np.ceil((u[m] - nn) * scale) / scale
    return out

def poisson_units(name, f, a0, X, rng):
    pts, a, nprop, maxratio = [], a0, 0, 0.0
    while a < X:
        b = min(X, a * 1.05 + 1.0)
        M = envelope(name, a)
        k = rng.poisson(M * (b - a)); nprop += k
        u = np.sort(a + (b - a) * rng.random(k))
        fu = f(u)
        r = fu / M
        if r.size:
            maxratio = max(maxratio, float(r.max()))
        acc = rng.random(k) < r
        pts.append(u[acc]); a = b
    u = np.concatenate(pts)
    v = np.unique(round_up_to_grid(u))
    return v, nprop, maxratio, int(u.size - v.size)

def oscillatory_tail(name, X):
    """2 sum_k int_{log X}^inf a_k(t) cos(gamma_k t) dt (k = 1 numerically, k = 2 leading IBP term); 0 for R."""
    if name == "R":
        return 0.0
    T = math.log(X)
    lam1, gam1 = 4.0, math.exp(4.0)
    t = np.linspace(T, T + 240.0, 2_400_001)
    a1 = (g_of_logu(t / lam1) / lam1) * np.exp(-t / lam1)
    I1 = np.trapezoid(a1 * np.cos(gam1 * t), t)
    lam2, gam2 = 16.0, math.exp(16.0)
    I2 = 0.0
    if T >= lam2:
        a2T = float(g_of_logu(np.array([T / lam2]))[0] / lam2 * math.exp(-T / lam2))
        I2 = -a2T * math.sin(gam2 * T) / gam2
    return 2.0 * (I1 + I2)

def main():
    name, seed, X, out = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    f = f_template(name)
    rng = np.random.default_rng([seed, 0 if name == "R" else 1, 20261001])
    t0 = time.time()
    P1, last, pmax = exact_units(f, rng)
    P2, nprop, maxratio, ndup = poisson_units(name, f, last, X, rng)
    assert maxratio <= 1.0 + 1e-12, maxratio
    P = np.concatenate((P1, P2[P2 > last]))
    P = P[P <= X]
    assert np.all(np.diff(P) > 0)
    a = -np.log1p(-1.0 / P)
    logsum = float(np.sum(a))
    T = math.log(X)
    m_tail = 1.0 / (2 * X * T)          # int_X^inf (a(v) - 1/v) f(v) dv, leading order
    s_tail = math.sqrt(1.0 / (X * T))   # (int_X^inf a(v)^2 f(v) dv)^{1/2}, leading order
    S_tail = float(rng.normal(m_tail, s_tail))
    osc = oscillatory_tail(name, X)
    logrho_X = logsum - Ein(T) - osc
    rho = math.exp(logrho_X + S_tail)
    P.astype(np.float64).tofile(out + ".primes.f64")
    meta = dict(template=name, seed=seed, X=X, n_primes=int(P.size), n_exact_units=NEX, pmax_exact=pmax,
                poisson_proposals=int(nprop), envelope_max_ratio=maxratio, grid_collisions=ndup,
                prime_1p5=bool(np.any(P == 1.5)), logsum=logsum, Ein=Ein(T), osc_tail=osc, S_tail=S_tail,
                s_tail=s_tail, rho=rho, rho_without_tail=math.exp(logrho_X), seconds=time.time() - t0)
    json.dump(meta, open(out + ".json", "w"), indent=1)
    print(json.dumps(meta))

if __name__ == "__main__":
    main()
