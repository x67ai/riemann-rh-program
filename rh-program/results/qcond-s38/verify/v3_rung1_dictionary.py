"""v3 (qcond-s38, task 3): the rung-1 calibration.  Genus 1 over F_5: L(u) = 1 - t u + 5 u^2 = (1 - a u)(1 - b u), a + b = t, ab = 5.
F_5 side:   Z(u) = L(u)/((1-u)(1-5u));  N_n = 5^n + 1 - s_n  (s_n = a^n + b^n, s_n = t s_{n-1} - 5 s_{n-2}, s_0 = 2, s_1 = t);
            b_d = (1/d) sum_{e|d} mu(d/e) N_e  (closed points of degree d).
  (F1) b_d >= 0 for d <= 60 (Beurling over F_5)      (F2) N_n >= 0 for n <= 60 (log Z >= 0 coefficientwise)
  (F3) Landau over F_5: no zero of L inside the pole radius |u| < 1/5, i.e. max(|a|,|b|) <= 5     (RH) |t| <= 2 sqrt 5
Q side, the transplant F = zeta(s) L(5^-s) (conductor 25, the u.d. class of Theorem U_q):
  (Q1) dN >= 0: c(n) = 1 (5 ∤ n), 1 - t (5 || n), 6 - t (25 | n)
  (Q2) E1 of NOTE §2.2: rho_q = 5 L(1/5) = 6 - t >= 1
  (Q3) Prop. E at p = 2 (a prime of weight 1 of zeta*L(5^-s)): (5 - t)/2 >= (2/5) S(1/25)
  (Q4) Pi >= 0 on the q-part <=> log[L(u)/(1-u)] >= 0 coefficientwise <=> s_n <= 1 for all n  (Theorem L' says: never)
  (Q5) Theorem L' conclusion: D = L(5^-s) zero-free (never, for any t: deg L = 2 with leading coefficient 5)
The exact dictionary: (Q4) is (F2)/(F1) with the pole factor 1/(1 - 5u) REMOVED — over F_5 the pole of Z lives in the same
local variable u as the zeros of L; over Q the pole of zeta at s = 1 is spread over all primes and is invisible on <5>.
"""
from fractions import Fraction
import math

def mobius(n):
    res, k, p = 1, n, 2
    while p*p <= k:
        if k % p == 0:
            k //= p
            if k % p == 0:
                return 0
            res = -res
        p += 1
    if k > 1:
        res = -res
    return res

def S(x):
    return 1.0 if x == 0 else (math.sin(math.pi*x)/(math.pi*x))**2

def row(t, NMAX=60):
    s = [2, t]
    for n in range(2, NMAX+1):
        s.append(t*s[-1] - 5*s[-2])
    N = [None] + [5**n + 1 - s[n] for n in range(1, NMAX+1)]
    b = [None] + [sum(mobius(d//e)*N[e] for e in range(1, d+1) if d % e == 0)//d for d in range(1, NMAX+1)]
    F1 = all(x >= 0 for x in b[1:])
    F2 = all(x >= 0 for x in N[1:])
    disc = t*t - 20
    if disc >= 0:
        r1, r2 = (t + math.sqrt(disc))/2, (t - math.sqrt(disc))/2
        amax = max(abs(r1), abs(r2))
    else:
        amax = math.sqrt(5)
    F3 = amax <= 5 + 1e-12
    RH = t*t <= 20
    Q1 = (1 - t >= 0) and (6 - t >= 0)
    Q2 = (6 - t) >= 1
    Q3 = (5 - t)/2 >= 0.4*S(1/25)
    Q4 = all(sn <= 1 for sn in s[1:])
    firstQ4 = next((n for n in range(1, NMAX+1) if s[n] > 1), None)
    minb = min(b[1:])
    return dict(t=t, RH=RH, F1=F1, F2=F2, F3=F3, Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, firstQ4=firstQ4, minb=minb, b=b[1:6], amax=amax)

if __name__ == "__main__":
    yn = lambda v: "yes" if v else " - "
    print(" t | RH  | F1 b_d>=0 | F2 N_n>=0 | F3 |a|<=5 | Q1 dN>=0 | Q2 rho>=1 | Q3 Euler-Fejer p=2 | Q4 Pi>=0 on <5> (first bad 5^n) | Q5 D zero-free | min b_d (d<=60) | b_1..b_5")
    rows = [row(t) for t in range(-12, 13)]
    for r in rows:
        print(f"{r['t']:3d}| {yn(r['RH'])} |    {yn(r['F1'])}    |    {yn(r['F2'])}    |   {yn(r['F3'])}    |   {yn(r['Q1'])}    |   {yn(r['Q2'])}     |        {yn(r['Q3'])}         |   {yn(r['Q4'])} (n={r['firstQ4']})"
              f"                 |      -         | {r['minb']:>16d} | {r['b']}")
    sets = {k: [r['t'] for r in rows if r[k]] for k in ('RH', 'F1', 'F2', 'F3', 'Q1', 'Q2', 'Q3', 'Q4')}
    for k, v in sets.items():
        print(f"{k}: t in {v}")
    print("F1 ∩ not RH (RH-false Beurling data over F_5):", [t for t in sets['F1'] if t not in sets['RH']])
    print("Q4 (the Q-side q-part positivity) admits:", sets['Q4'], " -- matches Theorem L' (no t survives).")
