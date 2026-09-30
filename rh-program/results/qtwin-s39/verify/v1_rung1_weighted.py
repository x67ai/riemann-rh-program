"""v1 (qtwin-s39): rung 1 FIRST, for the weighted mechanism.  Genus 1 over F_5, L(u) = 1 - t u + 5 u^2 with t REAL
(weights: b_d >= 0 real, no integrality).  s_n = a^n + b^n (a + b = t, ab = 5), N_n = 5^n + 1 - s_n, b_d = (1/d) sum_{e|d} mu(d/e) N_e.
(W1) weighted Beurling over F_5: b_d(t) >= 0 for all d <= DMAX -- the admissible real-t set, computed exactly (sympy real roots).
(W2) RH over F_5: |t| <= 2 sqrt 5.   (W3) the Q-side q-part positivity of the transplant zeta(s) L(5^-s) (QC §3, D4):
     log[L(u)/(1-u)] >= 0 coefficientwise  <=>  s_n <= 1 for all n >= 1 -- certified EMPTY over all real t by s_1..s_4.
(W4) positive Poisson mixtures at rung 1 (L with nonnegative coefficients) <=> t <= 0.
"""
import sympy as sp
from fractions import Fraction
t = sp.Symbol('t', real=True)
DMAX = 36

def mobius(n):
    res, k, p = 1, n, 2
    while p*p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            res = -res
        p += 1
    return -res if k > 1 else res

s = [sp.Integer(2), t]
for n in range(2, DMAX+1):
    s.append(sp.expand(t*s[-1] - 5*s[-2]))
N = [None] + [sp.expand(5**n + 1 - s[n]) for n in range(1, DMAX+1)]
b = [None] + [sp.expand(sum(mobius(d//e)*N[e] for e in range(1, d+1) if d % e == 0)/d) for d in range(1, DMAX+1)]

def nonneg_set(poly):
    """closed set {t real : poly(t) >= 0} as a list of intervals (floats), via exact real-root isolation."""
    P = sp.Poly(poly, t)
    roots = sorted(set(float(r) for r in sp.Poly(P, t).real_roots()))
    pts = [-1e9] + roots + [1e9]
    out = []
    for lo, hi in zip(pts[:-1], pts[1:]):
        mid = (lo + hi)/2 if abs(lo) < 1e8 and abs(hi) < 1e8 else (hi - 1 if lo < -1e8 else lo + 1)
        if P.eval(sp.Rational(mid)) >= 0:
            out.append((lo, hi))
    # merge
    m = []
    for lo, hi in out:
        if m and abs(m[-1][1] - lo) < 1e-12:
            m[-1] = (m[-1][0], hi)
        else:
            m.append((lo, hi))
    return m

def intersect(A, B):
    out = []
    for a0, a1 in A:
        for b0, b1 in B:
            lo, hi = max(a0, b0), min(a1, b1)
            if lo <= hi:
                out.append((lo, hi))
    return out

if __name__ == "__main__":
    adm = [(-1e9, 1e9)]
    for d in range(1, DMAX+1):
        adm = intersect(adm, nonneg_set(b[d]))
        if d in (1, 2, 3, 4, 5, 6, 8, 12, 18, 24, 30, 36):
            print(f"(W1) after b_1..b_{d:2d} >= 0: admissible t in " + ", ".join(f"[{lo:.10f}, {hi:.10f}]" for lo, hi in adm))
    rh = 2*5**0.5
    print(f"(W2) RH over F_5: |t| <= {rh:.10f}")
    for lo, hi in adm:
        print(f"     RH-FALSE part of the weighted-admissible set: [{lo:.10f}, {-rh:.10f}) U ({rh:.10f}, {hi:.10f}]" if lo < -rh and hi > rh else "")
    # exact endpoints: which b_d is active at each end
    for lo, hi in adm:
        for end in (lo, hi):
            act = [d for d in range(1, DMAX+1) if abs(float(sp.Poly(b[d], t).eval(sp.Float(end, 30)))) < 1e-6*max(1, 5**d/d)]
            print(f"     endpoint {end:.12f}: active constraints b_d = 0 for d in {act}")
    # (W3) certificate: s_1..s_4 <= 1 has no real solution
    sets = [nonneg_set(sp.expand(1 - s[n])) for n in range(1, 5)]
    for n in range(1, 5):
        print(f"(W3) s_{n} <= 1  <=>  t in " + ", ".join(f"[{lo:.6f}, {hi:.6f}]" for lo, hi in sets[n-1]))
    I = [(-1e9, 1e9)]
    for S in sets:
        I = intersect(I, S)
    print(f"(W3) intersection over n = 1..4: {I}   (EMPTY => the Q-side q-part positivity admits no real t: Theorem L' at rung 1, weights allowed)")
    print("(W4) positive Poisson mixtures at rung 1: L = 1 - t u + 5 u^2 has nonnegative coefficients <=> t <= 0;"
          f" weighted-Beurling-and-mixture: t in {intersect(adm, [(-1e9, 0.0)])}")
    # integer check against QC v3: integer t admissible for b_d >= 0, d <= DMAX
    ints = [k for k in range(-12, 13) if all(sp.Poly(b[d], t).eval(k) >= 0 for d in range(1, DMAX+1))]
    print(f"     integer t with b_d >= 0 (d <= {DMAX}): {ints}  (QC v3: -5..6)")
