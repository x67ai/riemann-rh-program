#!/usr/bin/env python3
"""dh_series_check.py -- diagnostic: is sum_n Lambda_DH(n) n^{-s} equal to -f_DH'/f_DH(s)?  Tested at s = 3 + 5i and s = 4 + 20i
(partial sums to N = 22026; tail ~ log N / N^{sigma-1}).  Also: the argument-principle count on the WIDER rectangle [-2, 3] x window."""
import math, sys, os, json
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test')); import dh
mp.mp.dps = 25
X = 22026
s5 = mp.sqrt(5); kap = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1); a = [mp.mpf(0), mp.mpf(1), kap, -kap, mp.mpf(-1)]
lam = [mp.mpf(0)]*(X + 1)
for n in range(2, X + 1): lam[n] = a[n % 5]*mp.log(n)
for d in range(2, X + 1):
    ld = lam[d]
    if ld == 0: continue
    j = 2; m = 2*d
    while m <= X:
        if j % 5: lam[m] -= a[j % 5]*ld
        j += 1; m += d
for s in (mp.mpc(3, 5), mp.mpc(4, 20), mp.mpc(2.5, 85.7)):
    series = mp.fsum(lam[n]*mp.power(n, -s) for n in range(2, X + 1))
    direct = -mp.diff(dh.f_dh, s)/dh.f_dh(s)
    tailest = mp.log(X)*mp.power(X, 1 - s.real)/(s.real - 1)
    print(f"s = {mp.nstr(s, 6)}: sum Lambda_DH(n) n^-s (n <= {X}) = {mp.nstr(series, 15)};  -f'/f(s) = {mp.nstr(direct, 15)};  diff = {mp.nstr(abs(series - direct), 3)};  tail estimate {mp.nstr(tailest, 2)}")
# also the same for a = Dirichlet series of f itself: sum a(n) n^-s vs f_DH(s) at s = 3 + 5i
s = mp.mpc(3, 5)
print("check f_DH itself: sum a(n) n^-s =", mp.nstr(mp.fsum(a[n % 5]*mp.power(n, -s) for n in range(1, X + 1)), 15), " f_dh(s) =", mp.nstr(dh.f_dh(s), 15))
# wider rectangle count
mp.mp.dps = 20
t = mp.mpf('85.69934848537759'); W0 = 60
def arg_change(a_, b_, n):
    tot = mp.mpf(0); mx = mp.mpf(0); prev = None
    for k in range(n + 1):
        val = dh.f_dh(a_ + (b_ - a_)*mp.mpf(k)/n)
        if prev is not None: d = mp.arg(val/prev); tot += d; mx = max(mx, abs(d))
        prev = val
    return tot, mx
c = [mp.mpc(-2, t - W0), mp.mpc(3, t - W0), mp.mpc(3, t + W0), mp.mpc(-2, t + W0), mp.mpc(-2, t - W0)]
tot = mp.mpf(0); mx = 0
for (p, q, n) in [(c[0], c[1], 1000), (c[1], c[2], 6000), (c[2], c[3], 1000), (c[3], c[4], 6000)]:
    d_, m_ = arg_change(p, q, n); tot += d_; mx = max(mx, m_)
print(f"argument principle on [-2, 3] x [t-60, t+60]: N = {mp.nstr(tot/(2*mp.pi), 8)} (max step {mp.nstr(mx, 3)})")
