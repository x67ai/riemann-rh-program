#!/usr/bin/env python3
"""dh_exact_eval.py -- M6 rung 1 fix pass (2026-09-17): EXACT evaluation of Lambda_DH(n) in Z[kappa] for the n listed by
verify/dh_count_L20.rs (the elements of S whose f64 value is at or below the threshold theta), by the recursion restricted to the
divisor lattice of n (Lambda_DH(n) depends only on Lambda_DH(d) for d | n).  Same representation as verify/dh_true_count.py:
Lambda_DH(n) = sum_{p | n} c_p(n) log p with c_p(n) in Z[kappa] = Z[x]/(x^4 + 2x^3 - 6x^2 - 2x + 1), stored as tuples of four
integers.  Prints, for each n, the exact coefficient vectors (the element is zero iff all vanish) and the real value at 60 and
120 digits; reports the number of exact zeros in the list, hence the TRUE count |S| - (#exact zeros in the list) at the given L.
Sanity check: for n = 2^k the closed form Lambda_DH(2^k) = [(-1)^{k-1} kappa^k - 2(-1)^{k/2-1} [k even]] log 2, which follows
from the 2-part of F2 being (1 + kappa y)/(1 + y^2), y = 2^{-s} (a rational function), is verified on every power of 2 in the list.
usage: dh_exact_eval.py <listfile> <S_size> <L> <outjson>"""
import sys, os, json, math, time, datetime
from itertools import product
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
listfile, S_size, L, outjson = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
t0 = time.time()
ns = [int(x) for x in open(listfile) if x.strip()]
print(f"[{now()}] dh_exact_eval.py: L = {L}, |S| = {S_size}, {len(ns)} listed n from {listfile}")
Z4 = (0, 0, 0, 0)
def kmul(u, v):
    r = [0]*7
    for i in range(4):
        ui = u[i]
        if ui == 0: continue
        for j in range(4): r[i + j] += ui*v[j]
    for deg in (6, 5, 4):
        c = r[deg]
        if c:
            r[deg] = 0; r[deg - 1] += -2*c; r[deg - 2] += 6*c; r[deg - 3] += 2*c; r[deg - 4] += -c
    return tuple(r[:4])
A = {1: (1, 0, 0, 0), 2: (0, 1, 0, 0), 3: (0, -1, 0, 0), 4: (-1, 0, 0, 0)}
def factor(n):
    f = []; p = 2
    while p*p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0: n //= p; e += 1
            f.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1: f.append((n, 1))
    return f
def exact_lambda(n):
    """the exact Lambda_DH(n) as {p: coeff4}, by the recursion over the divisor lattice of n."""
    f = factor(n); primes = [p for p, _ in f]; exps = [e for _, e in f]
    lattice = list(product(*[range(e + 1) for e in exps]))         # exponent tuples
    def val(t): 
        v = 1
        for p, k in zip(primes, t): v *= p**k
        return v
    lam = {}
    for t_ in sorted(lattice, key=val):
        d = val(t_)
        if d == 1: continue
        r = d % 5
        cur = {} if r == 0 else {p: tuple(c*k for c in A[r]) for p, k in zip(primes, t_) if k}
        if r != 0:
            for s_ in product(*[range(k + 1) for k in t_]):       # sub-divisors d' | d
                dp = val(s_)
                if dp == 1 or dp == d: continue
                ld = lam[dp]
                if not ld: continue
                aj = (d // dp) % 5
                if aj == 0: continue
                av = A[aj]
                for p, c in ld.items():
                    prod = kmul(av, c); old = cur.get(p, Z4)
                    new = (old[0] - prod[0], old[1] - prod[1], old[2] - prod[2], old[3] - prod[3])
                    if new == Z4: cur.pop(p, None)
                    else: cur[p] = new
        lam[d] = cur
    return lam[n]
mp.mp.dps = 120
s5 = mp.sqrt(5); KAP = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
def kval(u): return u[0] + u[1]*KAP + u[2]*KAP**2 + u[3]*KAP**3
def rval(el): return mp.fsum(kval(c)*mp.log(p) for p, c in el.items())
zeros = []; vals = []; pow2_ok = True
for i, n in enumerate(ns):
    el = exact_lambda(n)
    if not el:
        zeros.append(n); print(f"    n = {n} = {factor(n)}: EXACT ZERO"); continue
    v120 = rval(el)
    mp.mp.dps = 60; v60 = rval(el); mp.mp.dps = 120
    vals.append((abs(v120), n))
    f = factor(n)
    if len(f) == 1 and f[0][0] == 2:
        k = f[0][1]
        closed = ((-1)**(k - 1)*KAP**k - (2*(-1)**(k//2 - 1) if k % 2 == 0 else 0))*mp.log(2)
        if abs(closed - v120) > mp.mpf(10)**-100: pow2_ok = False; print(f"    CLOSED-FORM MISMATCH at 2^{k}")
    if i < 25 or i % 250 == 0 or len(f) == 1:
        print(f"    n = {n} = {'*'.join(f'{p}^{e}' if e > 1 else str(p) for p, e in f)}: {len(el)} log-coefficients, |Lambda_DH(n)| = {mp.nstr(abs(v120), 6)} (60 vs 120 digits: {mp.nstr(abs(v60 - v120), 2)})")
vals.sort()
print(f"[{now()}] {len(ns)} listed n: {len(zeros)} exact zeros, {len(ns) - len(zeros)} nonzero;  smallest |Lambda_DH| among the nonzero: {mp.nstr(vals[0][0], 6)} at n = {vals[0][1]};  largest listed: {mp.nstr(vals[-1][0], 6)} at n = {vals[-1][1]};  powers of 2 against the closed form: {pow2_ok};  {time.time()-t0:.1f}s")
true_count = S_size - len(zeros)
print(f"[{now()}] TRUE COUNT at L = {L:g}: |S| - (exact zeros in the list) = {S_size} - {len(zeros)} = {true_count}")
json.dump(dict(date=now(), L=L, S_size=S_size, listed=len(ns), exact_zeros=zeros, nonzero=len(ns) - len(zeros), min_abs=mp.nstr(vals[0][0], 12), argmin=vals[0][1],
               pow2_closed_form_ok=pow2_ok, true_count=true_count, seconds=time.time()-t0), open(outjson, 'w'), indent=1)
