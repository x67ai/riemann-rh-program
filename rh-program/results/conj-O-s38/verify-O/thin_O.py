#!/usr/bin/env python3
"""Reader-O independent re-run (conj-O-s38): Bernoulli thinning T_alpha, exact R-free counts, numpy only.
Shares no code with verify/: own segmented prime sieve, own RNG (numpy PCG64 seeded by [seed, round(1e6*alpha)],
uniforms drawn in increasing prime order), own rho tail (scipy exp1), own binning.
  usage: thin_O.py ALPHA X Y SEED OUTPREFIX
Outputs OUTPREFIX_dec.csv  (20 bins/decade, edges ceil(10^(k/20)))  and  OUTPREFIX_dya.csv (dyadic [2^j, 2^(j+1)-1]):
  lo,hi,maxEplus,minEminus,sumEc2,count   with E+(n) = N(n) - rho n, E-(n) = N(n) - rho(n+1), Ec(n) = N(n) - rho(n+1/2),
so sup|E| over real x in the bin = max(maxEplus, -minEminus) and int_bin E^2 = sumEc2 + count*rho^2/12 (E linear on [n,n+1)).
"""
import sys, math, time
import numpy as np
from scipy.special import exp1

def base_primes(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for q in range(2, int(n ** 0.5) + 1):
        if s[q]: s[q * q::q] = False
    return np.nonzero(s)[0]

def prime_segments(Y, seg=2 * 10**8):
    """yield arrays of primes in [lo, hi) for consecutive segments, increasing (odd-only sieve)."""
    bp = base_primes(int(math.isqrt(Y)) + 1)
    bp_odd = bp[bp >= 3]
    yield np.array([2], dtype=np.int64)
    lo = 3
    while lo <= Y:
        hi = min(lo + seg, Y + 1)
        if lo % 2 == 0: lo += 1
        n = (hi - lo + 1) // 2                     # odd numbers lo, lo+2, ..., < hi
        flag = np.ones(n, dtype=bool)
        for q in bp_odd:
            q = int(q)
            if q * q >= hi: break
            st = max(q * q, ((lo + q - 1) // q) * q)
            if st % 2 == 0: st += q
            flag[(st - lo) // 2::q] = False
        pr = lo + 2 * np.nonzero(flag)[0].astype(np.int64)
        if lo <= 1 < hi: pr = pr[pr > 1]
        yield pr
        lo = hi

M64 = np.uint64(0xFFFFFFFFFFFFFFFF)
def splitmix64(x):
    """numpy re-implementation of the splitmix64 finalizer (spec read from the frontier's thin.c; wraps mod 2^64)."""
    with np.errstate(over="ignore"):
        x = x + np.uint64(0x9E3779B97F4A7C15)
        x = (x ^ (x >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
        x = (x ^ (x >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
        return x ^ (x >> np.uint64(31))

def hash_unif(pr, seed, salt):
    with np.errstate(over="ignore"):
        k = splitmix64(np.array([(seed * 0xD1B54A32D192ED03) & 0xFFFFFFFFFFFFFFFF ^ salt], dtype=np.uint64))[0]
    h = splitmix64(pr.astype(np.uint64) ^ k)
    return (h >> np.uint64(11)).astype(np.float64) * (1.0 / 9007199254740992.0)

def main():
    alpha = float(sys.argv[1]); X = int(float(sys.argv[2])); Y = int(float(sys.argv[3])); out = sys.argv[5]
    hashmode = sys.argv[4].startswith("h"); seed = int(sys.argv[4].lstrip("h"))   # 'h5' = the writer's splitmix64 hash, seed 5
    t0 = time.time()
    rng = np.random.Generator(np.random.PCG64([seed, int(round(alpha * 1e6))]))
    dele = []; logs = []; nY = 0
    for pr in prime_segments(Y):
        u = hash_unif(pr, seed, int(round(alpha * 1e6))) if hashmode else rng.random(pr.size)
        w = np.exp((alpha - 1.0) * np.log(pr.astype(np.float64)))
        d = pr[u < w]
        dele.append(d); logs.append(math.fsum(np.log1p(-1.0 / d.astype(np.float64)).tolist())); nY += d.size
    dele = np.concatenate(dele)
    tail = -exp1((1.0 - alpha) * math.log(Y))
    logrho = math.fsum(logs); rho = math.exp(logrho + tail)
    dX = dele[dele <= X]
    print(f"# alpha={alpha} X={X} Y={Y} seed={seed} nR(Y)={nY} nR(X)={dX.size} logrho_Y={logrho:.12f} tail={tail:.12f} rho={rho:.12f}"
          f" primes_done={time.time()-t0:.1f}s", flush=True)
    np.save(out + "_Rprimes.npy", dX)
    dec = np.unique(np.ceil(10.0 ** (np.arange(0, 20 * math.log10(X) + 1) / 20.0) - 1e-9).astype(np.int64))
    dec = dec[dec <= X]; dec = np.append(dec, X + 1)
    dya = 2 ** np.arange(0, int(math.log2(X)) + 1, dtype=np.int64); dya = np.append(dya[dya <= X], X + 1)
    acc = {}
    for name, ed in (("dec", dec), ("dya", dya)):
        k = ed.size - 1
        acc[name] = [ed, np.full(k, -np.inf), np.full(k, np.inf), np.zeros(k), np.zeros(k, dtype=np.int64)]
    small = dX[dX < 10**8]; large = dX[dX >= 10**8]
    B = 10**8; Ncum = 0; sub = 25 * 10**6
    for lo in range(1, X + 1, B):
        hi = min(lo + B, X + 1)
        f = np.ones(hi - lo, dtype=bool)
        for p in small.tolist():
            st = ((lo + p - 1) // p) * p
            if st < hi: f[st - lo::p] = False
        st = ((lo + large - 1) // large) * large
        st = st[st < hi]; f[st - lo] = False
        for a in range(lo, hi, sub):
            b = min(a + sub, hi)
            N = Ncum + np.cumsum(f[a - lo:b - lo], dtype=np.int64); Ncum = int(N[-1])
            n = np.arange(a, b, dtype=np.float64)
            Ep = N - rho * n; Em = Ep - rho; Ec = Ep - 0.5 * rho
            for name in acc:
                ed, mx, mn, s2, ct = acc[name]
                j0 = int(np.searchsorted(ed, a, side="right") - 1); j1 = int(np.searchsorted(ed, b - 1, side="right") - 1)
                idx = np.clip(ed[j0:j1 + 1], a, None) - a
                mx[j0:j1 + 1] = np.maximum(mx[j0:j1 + 1], np.maximum.reduceat(Ep, idx))
                mn[j0:j1 + 1] = np.minimum(mn[j0:j1 + 1], np.minimum.reduceat(Em, idx))
                s2[j0:j1 + 1] += np.add.reduceat(Ec * Ec, idx)
                ct[j0:j1 + 1] += np.diff(np.append(idx, b - a))
        print(f"# block {lo}..{hi-1} N={Ncum} t={time.time()-t0:.1f}s", flush=True)
    for name in acc:
        ed, mx, mn, s2, ct = acc[name]
        with open(f"{out}_{name}.csv", "w") as fh:
            fh.write(f"# thin_O alpha={alpha} X={X} Y={Y} seed={seed} rho={rho!r} nR(X)={dX.size} nR(Y)={nY}\n")
            for j in range(ed.size - 1):
                if ct[j] > 0:
                    fh.write(f"{ed[j]},{min(ed[j+1]-1, X)},{mx[j]:.6f},{mn[j]:.6f},{s2[j]:.9e},{ct[j]}\n")
    print(f"# done N(X)={Ncum} E(X)={Ncum - rho*X:.4f} total={time.time()-t0:.1f}s", flush=True)

if __name__ == "__main__":
    main()
