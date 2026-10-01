#!/usr/bin/env python3
"""gdiv_O.py -- Opus reader (Session 41). For an integer n given by its factorization, list the divisors d <= 1e9 of n
that are g-primes of S5(0.8), using MY generator's list (gp_O_1e9.u32, uint32 pairs (q, m), from s5gen_O.c).
Writes one line per g-prime divisor: q followed by its exponent vector over the primes of n (in the given order).
Usage: gdiv_O.py NAME 'p1^e1,p2^e2,...' OUTFILE"""
import sys, hashlib, math
import numpy as np

GP = '/private/tmp/rh-s41-read-s5mult/gp_O_1e9.u32'

def divisors_le(primes, exps, bound):
    out = []
    def rec(i, d, vec):
        if i == len(primes):
            out.append((d, tuple(vec)))
            return
        p = primes[i]; x = d
        for e in range(exps[i] + 1):
            if x > bound:
                break
            vec.append(e); rec(i + 1, x, vec); vec.pop()
            x *= p
    rec(0, 1, [])
    return out

def main():
    name, fac, outf = sys.argv[1], sys.argv[2], sys.argv[3]
    primes, exps = [], []
    for t in fac.split(','):
        p, e = t.split('^') if '^' in t else (t, '1')
        primes.append(int(p)); exps.append(int(e))
    n = 1
    for p, e in zip(primes, exps):
        n *= p ** e
    raw = np.memmap(GP, dtype=np.uint32, mode='r').reshape(-1, 2)
    q = np.asarray(raw[:, 0]); m = np.asarray(raw[:, 1])
    assert np.all(np.diff(q.astype(np.int64)) > 0) and np.all(m == 1)
    divs = [(d, v) for d, v in divisors_le(primes, exps, 10**9) if d >= 2]
    ds = np.array([d for d, _ in divs], dtype=np.int64)
    pos = np.searchsorted(q, ds)
    pos[pos >= len(q)] = len(q) - 1
    hit = q[pos].astype(np.int64) == ds
    sel = sorted((d, v) for (d, v), h in zip(divs, hit) if h)
    with open(outf, 'w') as f:
        f.write('# %s n=%d primes=%s exps=%s\n' % (name, n, primes, exps))
        for d, v in sel:
            f.write('%d %s\n' % (d, ' '.join(map(str, v))))
    tau = 1
    for e in exps:
        tau *= e + 1
    cost = 0
    for d, v in sel:
        c = 1
        for e, ve in zip(exps, v):
            c *= e + 1 - ve
        cost += c
    digest = hashlib.sha256(''.join('%d\n' % d for d, _ in sel).encode()).hexdigest()
    print('%s: n=%d log10=%.6f tau=%d divisors<=1e9 (>=2)=%d g-prime divisors=%d largest=%d DPcells=%d sha(list of q)=%s'
          % (name, n, math.log10(n), tau, len(divs), len(sel),
             sel[-1][0], cost, digest))

if __name__ == '__main__':
    main()
