#!/usr/bin/env python3
"""controls.py — control systems through the same pipeline (dzcount + analyze). Unit dz-half-s39.
  primes X OUT        : the rational primes <= X as g-primes; rho = 1 exactly (N(x) = floor x): beta = 0, and N(e) = floor(e)
                        at every edge is asserted by check_primes().
  det X OUT           : the deterministic grid system P_det: q_j = the smallest grid point v with F_R(v) >= j (j >= 1), i.e.
                        pi(v) = floor(F_R(v)) on the grid, F_R = int_1^v f_R. No selection. beta >= 1/2 by the s = 1/2 branch
                        point (NOTE §4.3); predicted drift E(x) ~ sqrt(2/pi) H(1/2) (x/log x)^{1/2} [heuristic transfer].
  t1 SEED X OUT       : the frontier's random surgery at alpha = 1: delete each rational prime p with probability
                        w_p = 1/(1 + log p) (pi_R(x) ~ x/log^2 x, so alpha_R = 1, sum_R 1/p < oo). rho = prod_{p in R}(1 - 1/p)
                        times the tail factor exp(S), S ~ N(-log(1 + 1/log X), 1/(X log^2 X)) for the deletions above X.
"""
import sys, json, math
import numpy as np
from dzcommon import FR, fR, Ein
from dzgen import round_up_to_grid

def sieve(X):
    n = int(X)
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.float64)

def det_primes(X):
    J = int(math.floor(float(FR(np.array([X]))[0])))
    j = np.arange(1, J + 1, dtype=float)
    v = np.where(j < 20, 1.0 + 0.3 * j, 0.7 * j * np.log(j))
    v = np.maximum(v, 1.0 + 1e-9)
    bad = FR(v) >= j
    v[bad] = 1.0 + 1e-9
    for _ in range(200):                     # F concave increasing: Newton from the left is monotone
        step = (j - FR(v)) / fR(v)
        v = v + step
        if np.max(np.abs(step) / v) < 1e-15:
            break
    # exact grid rule for small v: smallest grid point with F >= j (round up, then step down if the previous grid point
    # already has F >= j, which can only happen through float error)
    q = round_up_to_grid(v)
    q = np.unique(q)
    return q[q <= X], J

def main():
    kind = sys.argv[1]
    if kind == "primes":
        X, out = float(sys.argv[2]), sys.argv[3]
        P = sieve(X); rho = 1.0; meta = dict(kind="primes", X=X, n_primes=int(P.size), rho=rho)
    elif kind == "det":
        X, out = float(sys.argv[2]), sys.argv[3]
        P, J = det_primes(X)
        a = -np.log1p(-1.0 / P)
        logrho = float(np.sum(a)) - Ein(math.log(X)) + 1.0 / (2 * X * math.log(X))
        rho = math.exp(logrho)
        meta = dict(kind="det", X=X, n_primes=int(P.size), quantiles=J, rho=rho, first=P[:6].tolist())
    elif kind == "t1":
        seed, X, out = int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
        rng = np.random.default_rng([seed, 7, 20261001])
        Q = sieve(X); w = 1.0 / (1.0 + np.log(Q))
        dele = rng.random(Q.size) < w
        P = Q[~dele]; R = Q[dele]
        T = math.log(X)
        S = float(rng.normal(-math.log1p(1.0 / T), math.sqrt(1.0 / (X * T * T))))
        rho = math.exp(float(np.sum(np.log1p(-1.0 / R))) + S)
        meta = dict(kind="t1", seed=seed, X=X, n_primes=int(P.size), n_deleted=int(R.size), S_tail=S, rho=rho)
    else:
        raise SystemExit("unknown kind")
    meta.update(K=1024, J=27)
    P.astype(np.float64).tofile(out + ".primes.f64")
    json.dump(meta, open(out + ".json", "w"), indent=1)
    print(json.dumps(meta))

if __name__ == "__main__":
    main()
