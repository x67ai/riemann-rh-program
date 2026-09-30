"""Unit fejer-form-s39, rung 1, step 1: every zeta datum over F_q, q in {5, 7, 11}, genus g in {1, 2}.
Zeta datum (proof-mine NOTE §4): L in Z[u], deg 2g, L(0)=1, FE L(u) = q^g u^{2g} L(1/(qu)); N_n = q^n+1-s_n >= 0;
closed-point counts b_d = (1/d) sum_{e|d} mu(d/e) N_e nonnegative integers; h = L(1) >= 1.  Admissibility is tested
for n, d <= 8 (the brief's LP window) AND for n, d <= 40 (robustness).  Exact integers throughout.
g = 1: L = 1 - t u + q u^2.  g = 2: L = 1 + a1 u + a2 u^2 + q a1 u^3 + q^2 u^4 = (1 - x1 u + q u^2)(1 - x2 u + q u^2),
x1, x2 the roots of X^2 + a1 X + (a2 - 2q).  RH (all |alpha| = sqrt q) <=> x1, x2 real with |x_j| <= 2 sqrt q (exact test).
Box: |x_j| <= q+1 is forced by N_n >= 0 (a reciprocal root of modulus > q makes some N_n < 0), so
|a1| <= 2q+2 and |a2 - 2q| <= (q+1)^2; the box below is that plus a margin of 3, and no hit may touch its edge."""
import json, math, sys
from sympy import mobius
NMAX = 40
def power_sums(c, nmax):
    # reciprocal roots are the roots of T^k + c1 T^{k-1} + ... + ck ; Newton's identities, exact
    k = len(c); s = [k]
    for n in range(1, nmax + 1):
        v = -sum(c[j - 1] * s[n - j] for j in range(1, min(n - 1, k) + 1))
        if n <= k: v -= n * c[n - 1]
        s.append(v)
    return s
def check(q, s, nmax):
    N = [None] + [q**n + 1 - s[n] for n in range(1, nmax + 1)]
    firstbad = None
    for n in range(1, nmax + 1):
        if N[n] < 0: firstbad = ('N', n); break
    b = [None]
    for d in range(1, nmax + 1):
        tot = sum(int(mobius(d // e)) * N[e] for e in range(1, d + 1) if d % e == 0)
        if tot % d != 0 or tot < 0:
            if firstbad is None or d < firstbad[1]: firstbad = ('b', d)
            break
        b.append(tot // d)
    return N, b, firstbad
def rh_g2(q, a1, a2):
    D = a1 * a1 - 4 * (a2 - 2 * q)
    if D < 0: return False, 'nonreal-x'
    # both real roots in [-2 sqrt q, 2 sqrt q]:  a1^2 <= 16 q  and  a2 + 2q >= 2|a1| sqrt q
    ok = a1 * a1 <= 16 * q and a2 + 2 * q >= 0 and (a2 + 2 * q)**2 >= 4 * a1 * a1 * q
    return ok, ('RH' if ok else 'real-offline')
out = {}
for q in (5, 7, 11):
    rows = []
    for t in range(-3 * q, 3 * q + 1):          # genus 1
        s = power_sums([-t, q], NMAX); N, b, bad = check(q, s, NMAX)
        h = 1 - t + q
        adm8 = bad is None or bad[1] > 8; adm40 = bad is None
        if adm8 and h >= 1:
            rows.append(dict(g=1, L=[1, -t, q], t=t, rh=(t * t <= 4 * q), kind=('RH' if t * t <= 4 * q else 'real-offline'),
                             h=h, N=N[1:9], b=b[1:9] if len(b) > 8 else b[1:], adm40=adm40, s=s[:9]))
    A1 = 2 * q + 5; lo2, hi2 = 2 * q - (q + 1)**2 - 3, 2 * q + (q + 1)**2 + 3
    edge = 0
    for a1 in range(-A1, A1 + 1):             # genus 2
        for a2 in range(lo2, hi2 + 1):
            s = power_sums([a1, a2, q * a1, q * q], NMAX); N, b, bad = check(q, s, NMAX)
            h = 1 + a1 + a2 + q * a1 + q * q
            adm8 = bad is None or bad[1] > 8; adm40 = bad is None
            if adm8 and h >= 1:
                if abs(a1) == A1 or a2 in (lo2, hi2): edge += 1
                rh, kind = rh_g2(q, a1, a2)
                rows.append(dict(g=2, L=[1, a1, a2, q * a1, q * q], a1=a1, a2=a2, rh=rh, kind=kind, h=h,
                                 N=N[1:9], b=b[1:9] if len(b) > 8 else b[1:], adm40=adm40, s=s[:9]))
    out[q] = rows
    for g in (1, 2):
        R = [r for r in rows if r['g'] == g]
        cnt = {}
        for r in R: cnt[(r['kind'], r['adm40'])] = cnt.get((r['kind'], r['adm40']), 0) + 1
        print("q=%d g=%d: zeta data (n,d<=8, h>=1): %d; by (kind, admissible to 40): %s" % (q, g, len(R), sorted(cnt.items())))
    print("q=%d g=2 box-edge hits: %d" % (q, edge))
    R1 = [r['t'] for r in rows if r['g'] == 1]
    print("q=%d g=1 admissible t (n,d<=8): %s; to 40: %s; RH-false: %s" % (q, R1, [r['t'] for r in rows if r['g'] == 1 and r['adm40']],
          [r['t'] for r in rows if r['g'] == 1 and not r['rh']]))
json.dump({str(k): v for k, v in out.items()}, open('r1_zeta_data.json', 'w'))
# reproduce the record: V (q=5, t=5) and the 111 non-real-x genus-2 hits of twin_g2 (n,d<=40, h>=1)
V = [r for r in out[5] if r['g'] == 1 and r['t'] == 5][0]
print("V (q=5,t=5): N_1..8 =", V['N'], " b_1..8 =", V['b'], " h =", V['h'], " adm40 =", V['adm40'])
nr = [r for r in out[5] if r['g'] == 2 and r['kind'] == 'nonreal-x' and r['adm40']]
print("q=5 g=2 non-real-x, admissible to 40, h>=1: %d (twin_g2 record: 111); V2 = (a1,a2)=(-1,11) present: %s" %
      (len(nr), any(r['a1'] == -1 and r['a2'] == 11 for r in nr)))
