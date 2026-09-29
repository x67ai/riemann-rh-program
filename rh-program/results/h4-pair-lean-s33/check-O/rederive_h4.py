"""Checker-written (Session 33, CHECK-O): independent recomputation of the H4 anchor numbers from the record's definitions
(pair-channel.md §1, §3; paper.md §2.3, §4.2). The builder's tools/h4_numbers.py was neither read nor imported."""
from mpmath import mp, mpf, cosh, pi, exp, cos, sin, mpc, fabs
from fractions import Fraction as Fr
mp.dps = 40
n = 32; M = 2*n+1; N = 2*n
B = range(-n, n+1)
u = mpf(1)/M
def abar(x): return sum(u*cosh(2*pi*j*x/N) for j in B)
d, mu = mpf(1)/4, mpf(1)/20
a1, a2 = abar(d), abar(2*d)
print("abar(1/4) =", mp.nstr(a1, 15)); print("abar(1/2) =", mp.nstr(a2, 15))
closed = 2*mu**2*a2**2 - 4*mu*(a1**2 - 1)
print("F1 - S2 closed form =", mp.nstr(closed, 15))
# direct row: W2 by its definition (count of j in B with s-j in B) / M^2, c_s = vacancy DFT at the UNREDUCED s + pair at site 0
def W2(s): return sum(1 for j in B if (s-j) in B) * u*u
zeta = exp(2j*pi/M)
def cs(s):
    atoms = sum(zeta**(((s*k) % M)) for k in range(1, M))       # unit atoms on sites k = 1..2n
    return atoms + 2*mu*cosh(2*pi*s*d/N)                         # pair at site 0: character = 1
F1 = sum(W2(s)*abs(cs(s))**2 for s in range(-2*n, 2*n+1))
S2 = 2*n + 2*mu**2
print("F1 direct =", mp.nstr(F1, 15), " S2 =", mp.nstr(S2, 15), " F1 - S2 direct =", mp.nstr(F1 - S2, 15),
      " |direct - closed| =", mp.nstr(fabs(F1 - S2 - closed), 3))
# W2 closed form check and sum W2 = 1
print("max |W2(s) - (M-|s|)/M^2| =", mp.nstr(max(fabs(W2(s) - (M-abs(s))*u*u) for s in range(-2*n, 2*n+1)), 3),
      " sum W2 =", mp.nstr(sum(W2(s) for s in range(-2*n, 2*n+1)), 20))
# (T1) at d and 2d
for x in (d, 2*d):
    print("T1 at x =", x, ":", mp.nstr(fabs(sum(W2(s)*cosh(2*pi*s*x/N) for s in range(-2*n, 2*n+1)) - abar(x)**2), 3))
# a row reduced mod 65 (the shipped gridRowQ convention applied to the pair factor), to see that it differs
def cs_red(s):
    r = s % M; r = r - M if r > n else r
    return sum(zeta**(((s*k) % M)) for k in range(1, M)) + 2*mu*cosh(2*pi*r*d/N)
F1r = sum(u*u*abs(cs_red(j1+j2))**2 for j1 in B for j2 in B)
print("reduced-mod-65 row F1 - S2 =", mp.nstr(F1r - S2, 10))
# (MI) at the anchor: M = 64 + 2mu, N_d = 64 + 2, T = 3M - 2N_d
Mass = 64 + 2*mu; Nd = 66; T = 3*Mass - 2*Nd
print("T =", mp.nstr(T, 10), " F1 - T =", mp.nstr(F1 - T, 10), " S2 - T =", mp.nstr(S2 - T, 10), " 2(mu-1)(mu-2) =", mp.nstr(2*(mu-1)*(mu-2), 10))
# power sums, exact integers
S = {k: sum(j**k for j in range(-32, 33)) for k in (2, 4, 6, 8)}
print("power sums:", S)
# certificate bound: abar(1/4) >= L := 1 + (p/128)^2 * S2/(2*65) with p = 3.141592  (cosh t >= 1 + t^2/2, t = 2 pi j (1/4)/64 = pi j/128)
# abar(1/2) <= U := (1/65) sum_j poly8(pi j/64) with p = 3.141593 (all terms increasing in p)
pL, pU = Fr(3141592, 10**6), Fr(3141593, 10**6)
L = 1 + (pL/128)**2 * S[2] / (2*65)
def poly8sum(p, c):   # (1/65) sum_j [1 + (cj)^2/2 + (cj)^4/24 + (cj)^6/720 + (cj)^8/20160], c = p/64
    return (65 + c**2*S[2]/2 + c**4*S[4]/24 + c**6*S[6]/720 + c**8*S[8]/20160) / 65
U = poly8sum(pU, pU/64)
mu_ = Fr(1, 20)
bound = 2*mu_**2*U**2 - 4*mu_*(L**2 - 1)
print("L =", float(L), " U =", float(U), " certified bound 2mu^2U^2 - 4mu(L^2-1) =", float(bound), " exact < 0:", bound < 0)
print("margin spent: closed - bound =", mp.nstr(closed - mpf(bound.numerator)/bound.denominator, 8))
print("L vs abar(1/4):", mp.nstr(a1 - mpf(L.numerator)/L.denominator, 6), " U - abar(1/2):", mp.nstr(mpf(U.numerator)/U.denominator - a2, 6))
# largest cosh argument at 2d = 1/2: pi*32/64 = pi/2 < 9/2
print("max |x| in cosh_le_poly8 use: 2*pi*32*(1/2)/64 =", mp.nstr(2*pi*32*(mpf(1)/2)/64, 10))
# E5: per-cosh error at pi/4: cosh x - (1 + x^2/2), and the estimate x^4/24 cosh x
x = pi/4
print("E5: cosh(pi/4) - 1 - x^2/2 =", mp.nstr(cosh(x) - 1 - x**2/2, 6), "; x^4/24*cosh(x) =", mp.nstr(x**4/24*cosh(x), 6))
# E7: 3294198/2^20
print("E7: 3294198/2^20 =", mp.nstr(mpf(3294198)/2**20, 15), " > 3.141592:", Fr(3294198, 2**20) > Fr(3141592, 10**6), " pi =", mp.nstr(pi, 12))
# Prop 4.5 threshold mu* = 2(abar(d)^2-1)/abar(2d)^2 at d = 1/4
print("mu* at d = 1/4:", mp.nstr(2*(a1**2-1)/a2**2, 10))
# chain spot check: integer m = 1 at d = 1/4
m = 1; print("m = 1, d = 1/4: expression =", mp.nstr(2*m**2*a2**2 - 4*m*(a1**2-1), 10), " lower 2m(mA^2 - A + 1) =", mp.nstr(2*m*(m*a2**2 - a2 + 1), 10))
print("log-convexity at d = 1/4: abar(d)^2 =", mp.nstr(a1**2, 10), " (1+abar(2d))/2 =", mp.nstr((1+a2)/2, 10))
# the literal rational of PairCert.cert_numeric, as written in the file
pu, pl = Fr(3141593, 10**6), Fr(3141592, 10**6)
Uc = 1 + (pu/64)**2*22880/(2*65) + (pu/64)**4*14492192/(24*65) + (pu/64)**6*10924353440/(720*65) + (pu/64)**8*8964042662432/(20160*65)
Lc = 1 + (pl/128)**2*22880/(2*65)
q = 2*Fr(1,20)**2*Uc**2 - 4*Fr(1,20)*(Lc**2 - 1)
print("cert_numeric rational: value", float(q), " numerator digits", len(str(abs(q.numerator))), " denominator digits", len(str(q.denominator)), " equals my bound:", q == bound)
# E5-adjacent: the poly8 excess at pi/2 and the one-exponential remainder bound
x = pi/2
print("poly8(pi/2) - cosh(pi/2) =", mp.nstr(1 + x**2/2 + x**4/24 + x**6/720 + x**8/20160 - cosh(x), 6), "; 2(pi/2)^8/40320 =", mp.nstr(2*x**8/40320, 6))
print("E7 alternative: 3294197/2^20 =", mp.nstr(mpf(3294197)/2**20, 12), "< 3.141592:", Fr(3294197, 2**20) < pl, "; 3294200/2^20 =", mp.nstr(mpf(3294200)/2**20, 12), "> 3.141593:", Fr(3294200, 2**20) > pu)
# n = 0 sanity of prop45 (M = 1: W2(0) = 1, abar = 1, vacancy lattice empty, c_0 = 2mu): F1 = 4 mu^2; RHS S2 + 2mu^2 - 0 = 4mu^2
print("n = 0: F1 = 4mu^2 =", mp.nstr(4*mu**2, 6), "; S2 + 2mu^2*1 - 4mu*0 =", mp.nstr(2*mu**2 + 2*mu**2, 6))
