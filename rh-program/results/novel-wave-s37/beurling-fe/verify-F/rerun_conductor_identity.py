#!/usr/bin/env python3
"""read-F re-run (orchestrator, Fable 5.1, Session 38): the M1a NOTE's conductor identity (C_q) checked by an
INDEPENDENT exact route (Poisson: sum_{n in Z} sinc^2(n/q) = q for integer q >= 1, so sum_{n>=1} = (q-1)/2), and the
Fejer sum S_F on one of v2's numerical near-solutions, enumerated directly (not via v1/v2b)."""
from mpmath import mp, mpf, sin, pi, sqrt
mp.dps = 30
def S(x):
    x = mpf(x)
    return mpf(1) if x == 0 else (sin(pi*x)/(pi*x))**2
print("== (1) sum_{n>=1} sinc^2(n/q) vs (q-1)/2  [partial sum to N plus tail bound q/(pi^2 N)] ==")
N = 200000
for q in (1, 2, 4, 9, 25):
    s = sum(S(mpf(n)/q) for n in range(1, N+1))
    tail = mpf(q)/(pi**2 * N)   # sum_{n>N} (q/(pi n))^2 <= q^2/(pi^2 N); crude, q<=25
    print(f"q={q:2d}: partial={float(s):.8f}  (q-1)/2={float((q-1)/2):.4f}  tail<= {float(tail*q):.2e}")
print("== (2) (C_q) for F = zeta(s)(1 + q^{1/2-s}): LHS rho_q(1-q^{-1/2}) with rho_q = sqrt(q)(1+q^{-1/2}); RHS 2 q^{-1/2} (q-1)/2 ==")
for q in (2, 4, 9):
    lhs = sqrt(q)*(1+1/sqrt(q))*(1-1/sqrt(q)); rhs = 2/sqrt(q)*mpf(q-1)/2
    print(f"q={q}: LHS={float(lhs):.6f} RHS={float(rhs):.6f}  (NOTE v1 Part 3 prints {[0.70711,1.5,2.66667][[2,4,9].index(q)]})")
print("== (3) F_{5,5} = zeta(s)(1 + 5*5^{-s} + 5*25^{-s}), q = 25: LHS = 5*(1+1+1/5)*(1-1/5) ; RHS = (2/5)[sum S(n/25) + 5 sum S(n/5)] ==")
lhs = 5*(mpf(2)+mpf(1)/5)*(1-mpf(1)/5); rhs = mpf(2)/5*(mpf(24)/2 + 5*mpf(4)/2)
print(f"LHS={float(lhs):.4f} RHS={float(rhs):.4f} (NOTE: 8.8 = 8.8)")
print("== (4) Fejer sum S_F = sum sinc^2(n_k) over generalized integers <= X of the near-solution {2, 3, 8.470247} (v2, K=3) ==")
import itertools, math
c = 8.470247; X = 10**6
tot = 0.0; cnt = 0
for k in range(1, 20):
    ck = c**k
    if ck > X: break
    for a in range(0, 25):
        if ck*2**a > X: break
        for b in range(0, 15):
            n = ck*2**a*3**b
            if n > X: break
            tot += float(S(n)); cnt += 1
print(f"non-integer generalized integers <= {X}: {cnt}; S_F = {tot:.4e}  (NOTE v2b: 1.7e-3 for this system; Z gives 0 exactly)")
print("== (5) theta relation rho+2psi(1/x) = sqrt(x)(rho+2psi(x)) at x=2 for Z (rho=1) and for the near-solution (rho=1) ==")
from mpmath import exp
def psi_Z(x): return sum(exp(-pi*n*n*x) for n in range(1, 60))
x = mpf(2); print(f"Z: defect = {float(1+2*psi_Z(1/x) - sqrt(x)*(1+2*psi_Z(x))):.3e}")
def psi_near(x):
    tot = mpf(0)
    for k in range(0, 6):
        for a in range(0, 30):
            for b in range(0, 20):
                n = mpf(c)**k * 2**a * 3**b
                if n > 60: break
                tot += exp(-pi*n*n*x)
    return tot
print(f"near-solution: defect = {float(1+2*psi_near(1/x) - sqrt(x)*(1+2*psi_near(x))):.3e}  (nonzero: the FE fails, as T requires)")
