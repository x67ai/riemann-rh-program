#!/usr/bin/env python3
"""CHECK-O-B item (ii): numerical cross-check of the tail-integral identities proved in Clause5.lean §4-§5.
 (a) a*gamma_n - gamma_n' = s^n (the derivative identity behind hasDerivAt_exp_mul_gammaPoly), n = 0..12, symbolic (sympy);
 (b) int_{s0}^inf s^n e^{-a s} ds = e^{-a s0} gamma_n(a, s0) (integral_pow_mul_exp_Ioi), quadrature at 40 digits;
 (c) int_{u0}^inf phi_m(u) du = (2/L^{m+1}) e^{-2 cB s0} Gamma_m(s0), s0 = sqrt(L u0) (integral_phi_Ioi), m = 2, 3;
 (d) d/du Phi_m(u) = phi_m(u) (hasDerivAt_Phi) by a centered finite difference."""
import sympy as sp, mpmath as mp
mp.mp.dps = 40
a, s = sp.symbols('a s', positive=True)
def gp(n, a, s): return sum(sp.factorial(n)/sp.factorial(j)*s**j/a**(n+1-j) for j in range(n+1))
ok = all(sp.simplify(a*gp(n, a, s) - sp.diff(gp(n, a, s), s) - s**n) == 0 for n in range(13))
print("(a) a*gamma_n - d/ds gamma_n = s^n for n = 0..12:", ok)
ok2 = all(sp.simplify(gp(n+1, a, s) - (s**(n+1)/a + (n+1)/a*gp(n, a, s))) == 0 for n in range(12))
print("    recursion gamma_{n+1} = s^{n+1}/a + ((n+1)/a) gamma_n for n = 0..11:", ok2)
def gpm(n, a, s): return mp.fsum(mp.factorial(n)/mp.factorial(j)*s**j/a**(n+1-j) for j in range(n+1))
cB = 2/mp.sqrt(72*mp.e)
for (n, av, s0) in ((0, mp.mpf(2), mp.mpf(1)), (5, 2*cB, mp.mpf(10)), (9, 2*cB, mp.sqrt(73)*50), (9, 2*cB, mp.mpf(427))):
    I = mp.quad(lambda x: x**n*mp.exp(-av*x), [s0, s0+50, s0+400, mp.inf])
    R = mp.exp(-av*s0)*gpm(n, av, s0)
    print(f"(b) n={n} a={mp.nstr(av,8)} s0={mp.nstr(s0,8)}: quad {mp.nstr(I,20)}  closed {mp.nstr(R,20)}  rel {mp.nstr(abs(I-R)/R,3)}")
def GammaM(m, s): return gpm(2*m+1, 2*cB, s) + cB*gpm(2*m+2, 2*cB, s) + cB**2/4*gpm(2*m+3, 2*cB, s)
def phi(m, L, u): return u**m*(1 + cB/2*mp.sqrt(L*u))**2*mp.exp(-2*cB*mp.sqrt(L*u))
def Phi(m, L, u): return -(2/L**(m+1)*(mp.exp(-2*cB*mp.sqrt(L*u))*GammaM(m, mp.sqrt(L*u))))
for m in (2, 3):
    for (L, u0) in ((mp.mpf(50), mp.mpf(3650)), (mp.mpf(100), mp.mpf(7300)), (mp.mpf(1), mp.mpf(5))):
        I = mp.quad(lambda u: phi(m, L, u), [u0, 2*u0, 10*u0, mp.inf])
        R = 2/L**(m+1)*mp.exp(-2*cB*mp.sqrt(L*u0))*GammaM(m, mp.sqrt(L*u0))
        h = mp.mpf('1e-12')*u0
        d = (Phi(m, L, u0+h) - Phi(m, L, u0-h))/(2*h)
        print(f"(c,d) m={m} L={mp.nstr(L,5)} u0={mp.nstr(u0,6)}: quad {mp.nstr(I,18)} closed {mp.nstr(R,18)} rel {mp.nstr(abs(I-R)/R,3)};"
              f"  Phi'(u0) {mp.nstr(d,15)} phi(u0) {mp.nstr(phi(m,L,u0),15)} rel {mp.nstr(abs(d-phi(m,L,u0))/phi(m,L,u0),3)}")
