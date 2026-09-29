"""h4_numbers.py -- Session 33 builder's recomputation (standing order 5) of every load-bearing number of the H4 unit:
the anchor values abar(1/4), abar(1/2) with u_j = 1/65 on the band |j| <= 32 and circle N = 64; F1 - S2 at
(d, mu) = (1/4, 1/20) by the closed form of Prop. 4.5, by the direct integer-frequency row (the paper's section 2.3 row with
the closed-form weights), and by the mod-65-reduced row (the wrong row, for contrast); the four integer power sums
S_2, S_4, S_6, S_8 over j in [-32, 32] (exact integers); the certificate's rational bounds L (lower, degree 2, pi >= 3.141592)
and U (upper, degree 8, pi <= 3.141593) and the certified value 2 mu^2 U^2 - 4 mu (L^2 - 1); the first-order error budget;
the integer-mark chain at m = 1.  Nothing here is a certificate: the Lean module PairCert.lean is.  mpmath at 30 digits;
the power sums and the rational bounds are exact (fractions)."""
from fractions import Fraction as Fr
import mpmath as mp
mp.mp.dps = 30
n = 32; M = 2*n + 1; N = 2*n
u = mp.mpf(1)/M
def abar(x):
    return sum(u*mp.cosh(2*mp.pi*j*x/N) for j in range(-n, n+1))
def W2(s):
    return mp.mpf(M - abs(s))/M**2
def phi0(s):        # vacancy lattice: 2n at s = 0 mod M, -1 otherwise (|s| <= 2n so only s = 0)
    return mp.mpf(2*n) if s % M == 0 else mp.mpf(-1)
d = mp.mpf(1)/4; mu = mp.mpf(1)/20
beta = 2*mp.pi*d/N
a1, a2 = abar(d), abar(2*d)
print("abar(1/4) =", mp.nstr(a1, 12))
print("abar(1/2) =", mp.nstr(a2, 12))
closed = 2*mu**2*a2**2 - 4*mu*(a1**2 - 1)
print("F1 - S2 closed form =", mp.nstr(closed, 12))
print("  2 mu^2 abar(2d)^2 =", mp.nstr(2*mu**2*a2**2, 10), "; 4 mu (abar(d)^2 - 1) =", mp.nstr(4*mu*(a1**2-1), 10))
# direct integer-frequency row
row = sum(W2(s)*(phi0(s) + 2*mu*mp.cosh(beta*s))**2 for s in range(-2*n, 2*n+1))
S2 = 2*n + 2*mu**2
print("F1 (integer-frequency row) =", mp.nstr(row, 15), "; S2 =", mp.nstr(S2, 10), "; F1 - S2 =", mp.nstr(row - S2, 12))
# the mod-65-reduced row (cosh at the reduced residue in [-32, 32]): the WRONG row, for contrast with the note section 1.1
def red(s):
    r = s % M
    return r - M if r > n else r
rowred = sum(W2(s)*(phi0(s) + 2*mu*mp.cosh(beta*red(s)))**2 for s in range(-2*n, 2*n+1))
print("F1 (mod-65-reduced row) - S2 =", mp.nstr(rowred - S2, 10), "  (not the paper's row)")
# (MI) at the anchor: T = 3M - 2N_d with M = 64 + 2 mu, N_d = 64 + 2
Tm = 3*(64 + 2*mu) - 2*66
print("T = 3M - 2N_d =", mp.nstr(Tm, 8), "; F1 - T =", mp.nstr(row - Tm, 6), "; S2 - T =", mp.nstr(S2 - Tm, 6), "= 2(mu-1)(mu-2) =", mp.nstr(2*(mu-1)*(mu-2), 6))
# the sum of weights and (T1) at x = d, 2d, 0
print("sum_s W2 =", mp.nstr(sum(W2(s) for s in range(-2*n, 2*n+1)), 12))
print("(T1) at d: sum_s W2 cosh(beta s) - abar(d)^2 =", mp.nstr(sum(W2(s)*mp.cosh(beta*s) for s in range(-2*n,2*n+1)) - a1**2, 5))
print("(T1) at 2d: sum_s W2 cosh(2 beta s) - abar(2d)^2 =", mp.nstr(sum(W2(s)*mp.cosh(2*beta*s) for s in range(-2*n,2*n+1)) - a2**2, 5))
# power sums, exact
S = {k: sum(j**k for j in range(-n, n+1)) for k in (2, 4, 6, 8)}
print("power sums:", S)
# certificate bounds, exact rationals
def L_of(pi):   # lower bound on abar(1/4): sum (1/65)(1 + (pi j/128)^2/2)
    return 1 + Fr(pi)**2 * S[2] / (2 * 128**2 * M)
def U_of(pi):   # upper bound on abar(1/2): sum (1/65)(1 + x^2/2 + x^4/24 + x^6/720 + x^8/20160), x = pi j/64
    c = Fr(pi)
    return 1 + c**2*S[2]/(2*64**2*M) + c**4*S[4]/(24*64**4*M) + c**6*S[6]/(720*64**6*M) + c**8*S[8]/(20160*64**8*M)
piL, piU = Fr("3.141592"), Fr("3.141593")
L, U = L_of(piL), U_of(piU)
print("coefficients: L = 1 + pi^2 *", S[2], "/", 2*128**2*M, "=", Fr(S[2], 2*128**2*M))
print("  U = 1 + pi^2 *", Fr(S[2], 2*64**2*M), "+ pi^4 *", Fr(S[4], 24*64**4*M), "+ pi^6 *", Fr(S[6], 720*64**6*M), "+ pi^8 *", Fr(S[8], 20160*64**8*M))
print("L(3.141592) =", float(L), "; U(3.141593) =", float(U))
mu_q = Fr(1, 20)
cert = 2*mu_q**2*U**2 - 4*mu_q*(L**2 - 1)
print("certified bound 2 mu^2 U^2 - 4 mu (L^2 - 1) =", float(cert), " (exact rational, numerator digits:", len(str(cert.numerator)), ")")
print("  margin spent versus the record:", float(cert) - float(closed))
# the max |x| for the upper bound hypothesis |x| <= 9/2
print("max |pi j / 64| =", float(piU*32/64), "<= 4.5")
# error budget, first order
print("first-order budget: dBound/dL = -8 mu abar(1/4) =", mp.nstr(-8*mu*a1, 6), "; dBound/dU = 4 mu^2 abar(1/2) =", mp.nstr(4*mu**2*a2, 6))
print("  tolerances alone: delta1 <", mp.nstr(-closed/(8*mu*a1), 5), "; delta2 <", mp.nstr(-closed/(4*mu**2*a2), 5))
print("  actual: abar(1/4) - L =", mp.nstr(a1 - mp.mpf(L.numerator)/L.denominator, 6), "; U - abar(1/2) =", mp.nstr(mp.mpf(U.numerator)/U.denominator - a2, 6))
# per-cosh errors of the generic bounds at the extreme arguments
x = mp.pi/4; print("cosh(pi/4) - 1 - x^2/2 =", mp.nstr(mp.cosh(x) - 1 - x**2/2, 6))
x = mp.pi/2; print("poly8(pi/2) - cosh(pi/2) =", mp.nstr(1 + x**2/2 + x**4/24 + x**6/720 + x**8/20160 - mp.cosh(x), 6))
# the integer-mark chain at m = 1, d = 1/4: 2 m^2 A^2 - 4 m (a^2 - 1) >= 2 m (m A^2 - A + 1)
for m in (1, 2):
    val = 2*m**2*a2**2 - 4*m*(a1**2 - 1); low = 2*m*(m*a2**2 - a2 + 1)
    print("m =", m, ": F1 - S2 =", mp.nstr(val, 6), ">= chain lower bound", mp.nstr(low, 6))
print("Cauchy-Schwarz check: abar(1/4)^2 =", mp.nstr(a1**2, 8), "<= (1 + abar(1/2))/2 =", mp.nstr((1+a2)/2, 8))
