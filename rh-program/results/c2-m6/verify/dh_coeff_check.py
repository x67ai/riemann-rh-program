#!/usr/bin/env python3
"""dh_coeff_check.py -- independent (Python/mpmath, dps 30) recomputation of the DH coefficient side at L = 10:
Lambda_DH(n) for n <= X = floor(e^10) by the divisor recursion at 30 digits (no Rust), the phases cos(t log n) at 30 digits,
A(log n / L) by an own numpy trapezoid (M = 8192, checked against mpmath quad at three points), and the sum.  Also counts
the n coprime to 5 with Lambda_DH(n) = 0 and lists the first of them, and prints max |Lambda_DH(n)|."""
import math, json, datetime, sys
import numpy as np, mpmath as mp
mp.mp.dps = 30
T85 = mp.mpf('85.69934848537759'); L = 10; X = int(math.floor(math.exp(L)))
s5 = mp.sqrt(5); kap = (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)
a = [mp.mpf(0), mp.mpf(1), kap, -kap, mp.mpf(-1)]
lam = [mp.mpf(0)]*(X + 1)
for n in range(2, X + 1): lam[n] = a[n % 5]*mp.log(n)
for d in range(2, X + 1):
    ld = lam[d]
    if ld == 0: continue
    j = 2; m = 2*d
    while m <= X:
        if j % 5: lam[m] -= a[j % 5]*ld
        j += 1; m += d
zeros_coprime = [n for n in range(2, X + 1) if n % 5 and lam[n] == 0]
print(f"witnesses: Lambda_DH(3) = {mp.nstr(lam[3], 15)}, (4) = {mp.nstr(lam[4], 15)}, (6) = {mp.nstr(lam[6], 15)}, (12) = {mp.nstr(lam[12], 15)}")
print(f"n <= {X} coprime to 5 with Lambda_DH(n) == 0 exactly (mpmath): {len(zeros_coprime)}; first 30: {zeros_coprime[:30]}")
print(f"max |Lambda_DH(n)| = {mp.nstr(max(abs(v) for v in lam), 8)} at n = {max(range(2, X+1), key=lambda n: abs(lam[n]))};  sum Lambda/sqrt n = {mp.nstr(mp.fsum(lam[n]/mp.sqrt(n) for n in range(2, X+1)), 12)}")
# A(v) by numpy trapezoid
M = 8192; w = np.arange(1, M)/M - 0.5
with np.errstate(all='ignore'):
    q = 1 - 4*w*w; braw = np.exp(-1/q); bd1 = braw*(-8*w/(q*q))
braw[~np.isfinite(braw)] = 0; bd1[~np.isfinite(bd1)] = 0; Z = braw.sum()/M
def A(v):
    v = abs(v)
    if v >= 1: return 0.0
    ws = w - v
    with np.errstate(all='ignore'):
        qs = 1 - 4*ws*ws; b2 = np.where(np.abs(ws) < 0.5, np.exp(-1/qs)*(-8*ws/(qs*qs)), 0.0)
    return float((bd1*b2).sum()/M/(Z*Z))
# check A against mpmath quad at three points
def Araw_mp(v):
    v = mp.mpf(v)
    B1 = lambda x: (mp.e**(-1/(1-4*x*x))*(-8*x/(1-4*x*x)**2) if abs(x) < mp.mpf(1)/2 else mp.mpf(0))
    Zq = mp.quad(lambda x: mp.e**(-1/(1-4*x*x)) if abs(x) < mp.mpf(1)/2 else 0, [-0.5, -0.25, 0, 0.25, 0.5])
    lo = max(-0.5, v - 0.5); pts = [lo + (0.5 - lo)*k/8 for k in range(9)]
    return mp.quad(lambda x: B1(x)*B1(x - v), pts)/Zq**2
print("A(v) trapezoid vs mpmath quad:", [(v, A(v), float(Araw_mp(v)), A(v) - float(Araw_mp(v))) for v in (0.0, 0.3, 0.7)])
terms = []; l1 = mp.mpf(0)
for n in range(2, X + 1):
    if lam[n] == 0: continue
    wn = lam[n]/mp.sqrt(n)*2*mp.mpf(A(float(mp.log(n))/L))/L**3
    terms.append(wn*mp.cos(T85*mp.log(n))); l1 += abs(wn)
P = mp.fsum(terms)
print(f"P_DH(85.7, 10) independent (mpmath Lambda, dps 30) = {mp.nstr(P, 20)};  terms = {len(terms)};  l1 = {mp.nstr(l1, 10)}")
rs = json.load(open('out/dh_t85p7_L10.json'))
print(f"Rust P_dd = {rs['P_dd']!r}; difference = {mp.nstr(P - mp.mpf(rs['P_dd']), 4)};  Rust terms = {rs['n_terms']}, l1 = {rs['l1_norm']}")
json.dump(dict(P_mp=mp.nstr(P, 25), P_rust=rs['P_dd'], diff=float(P - mp.mpf(rs['P_dd'])), n_terms=len(terms), n_zero_coprime=len(zeros_coprime), first_zero_coprime=zeros_coprime[:30]), open('out/dh_coeff_check.json', 'w'), indent=1)
