#!/usr/bin/env python3
"""thin_O.py — reader O's independent re-run of Bernoulli thinning T_alpha (seed M1b). Pure numpy/scipy.

Independent of the writer's thin.c in every component: prime sieve (numpy, odd-only), randomness (numpy PCG64 seeded
by (seed, round(1e6*alpha)), not a hash), the tail of rho (scipy quad of int_{log Y}^inf e^{(alpha-1)v}/v dv, printed
next to mpmath's E1 for comparison), and the statistics (per-bin sup and RMS at x = n + U with U ~ Uniform[0,1) i.i.d.).

Usage: python3 thin_O.py MODE ALPHA X Y SEED [SEED ...]
  MODE bern : delete each prime p <= Y independently with probability min(1, p^(alpha-1)).
  MODE none : no deletion (the rational integers; rho = 1).  ALPHA, Y, SEED ignored but must be given.
  MODE fin  : delete the first K primes, K = int(ALPHA) (finite R; E is periodic; Prop 5.1 predicts the mean square
              rho * 2^K / 12 over a period).  Y, SEED ignored.
N_P(n) = #{m <= n : no prime factor of m lies in R} is exact for every n <= X (boolean sieve + cumulative sum).
Output (stdout, CSV): run,lo,hi,supabs,maxE,minE,rms,count  per log-bin of integers n (BPD bins per decade), where
supabs = sup over real x in [lo, hi+1) of |N_P(x) - rho x| (exact: N_P is constant on [n, n+1)).
"""
import sys, math, time
import numpy as np
from scipy.integrate import quad

BPD = 10
CHUNK = 10_000_000


def primes_upto(n):
    s = np.ones(n // 2 + 1, dtype=bool)  # index i <-> 2i+1
    s[0] = False
    for i in range(1, int(math.isqrt(n)) // 2 + 1):
        if s[i]:
            p = 2 * i + 1
            s[p * p // 2::p] = False
    ps = 2 * np.nonzero(s)[0] + 1
    ps = ps[ps <= n]
    return np.concatenate((np.array([2], dtype=np.int64), ps.astype(np.int64)))


def tail_integral(alpha, Y):
    """int_Y^inf u^(alpha-2)/log u du = int_{log Y}^inf e^{(alpha-1)v}/v dv (mean of -sum_{p>Y} w_p log(1-1/p))."""
    a = 1.0 - alpha
    L = math.log(Y)
    val, err = quad(lambda v: math.exp(-a * v) / v, L, np.inf, limit=200, epsabs=0, epsrel=1e-13)
    return val, err


def run_stats(run, mask, rho, X, rng_u, out):
    N = np.cumsum(mask, dtype=np.int64)  # N[n] = #{1 <= m <= n : m R-free}; mask[0] = False
    K = int(math.floor(BPD * math.log10(X))) + 1
    edges = [int(math.ceil(10 ** (k / BPD) - 1e-9)) for k in range(K + 1)] + [X + 1]
    edges = sorted(set(e for e in edges if e <= X + 1))
    for a, b in zip(edges[:-1], edges[1:]):  # integers n in [a, b-1]
        mx, mn, s2, cnt = -1e300, 1e300, 0.0, 0
        for c0 in range(a, b, CHUNK):
            c1 = min(b, c0 + CHUNK)
            n = np.arange(c0, c1, dtype=np.float64)
            Nn = N[c0:c1].astype(np.float64)
            ep = Nn - rho * n
            em = ep - rho
            mx = max(mx, float(ep.max()))
            mn = min(mn, float(em.min()))
            ex = ep - rho * rng_u.random(c1 - c0)
            s2 += float(np.dot(ex, ex))
            cnt += c1 - c0
        out.write("%s,%d,%d,%.6f,%.6f,%.6f,%.6e,%d\n" % (run, a, b - 1, max(mx, -mn), mx, mn, math.sqrt(s2 / cnt), cnt))
    out.flush()


def main():
    mode, alpha, X, Y = sys.argv[1], float(sys.argv[2]), int(float(sys.argv[3])), int(float(sys.argv[4]))
    seeds = [int(s) for s in sys.argv[5:]]
    out = sys.stdout
    t0 = time.time()
    if mode == "none":
        mask = np.ones(X + 1, dtype=bool); mask[0] = False
        out.write("# mode=none X=%d rho=1\n" % X)
        run_stats("none", mask, 1.0, X, np.random.default_rng(12345), out)
        return
    if mode == "fin":
        K = int(alpha)
        ps = primes_upto(1000)[:K]
        mask = np.ones(X + 1, dtype=bool); mask[0] = False
        for p in ps:
            mask[p::p] = False
        rho = float(np.prod(1.0 - 1.0 / ps.astype(np.float64)))
        Q = int(np.prod(ps))
        out.write("# mode=fin R=%s Q=%d rho=%.12f prop5.1_meansquare=%.12f\n" % (list(map(int, ps)), Q, rho, rho * 2 ** K / 12))
        run_stats("fin_K%d" % K, mask, rho, X, np.random.default_rng(54321), out)
        return
    ps = primes_upto(Y)
    w = np.minimum(1.0, np.exp((alpha - 1.0) * np.log(ps.astype(np.float64))))
    tail, terr = tail_integral(alpha, Y)
    try:
        import mpmath
        e1 = float(mpmath.e1((1 - alpha) * math.log(Y)))
    except Exception:
        e1 = float("nan")
    out.write("# mode=bern alpha=%.4f X=%d Y=%d pi(Y)=%d tail_quad=%.15e (err %.1e) E1=%.15e sieve_s=%.1f\n"
              % (alpha, X, Y, len(ps), tail, terr, e1, time.time() - t0))
    for seed in seeds:
        rng = np.random.default_rng([seed, int(round(alpha * 1e6))])
        dele = ps[rng.random(len(ps)) < w]
        logrho = math.fsum(np.log1p(-1.0 / dele.astype(np.float64)).tolist())
        rho = math.exp(logrho - tail)
        mask = np.ones(X + 1, dtype=bool); mask[0] = False
        for p in dele[dele <= X].tolist():
            mask[p::p] = False
        run = "bernO_a%.2f_s%d" % (alpha, seed)
        out.write("# run=%s nR(Y)=%d nR(X)=%d logrho_Y=%.12f rho=%.12f t=%.1f\n"
                  % (run, len(dele), int((dele <= X).sum()), logrho, rho, time.time() - t0))
        run_stats(run, mask, rho, X, np.random.default_rng([seed, 999]), out)
        del mask


if __name__ == "__main__":
    main()
