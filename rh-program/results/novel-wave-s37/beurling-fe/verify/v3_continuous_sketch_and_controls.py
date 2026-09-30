#!/usr/bin/env python3
"""v3 -- seed M1a beurling-fe.  NOTE §8(a) and §9.
Part A  The orchestrator's continuous sketch: zeta_P = zeta * G,
        G(s) = (s-rho)(s-rhobar)(s-1+rho)(s-1+rhobar) / ((s-a)^2 (s-1+a)^2),  rho = beta + i gamma, beta > 1/2.
        log G(s) = int_1^inf x^{-s} f(x) dx with f(x) = [2x^a + 2x^{1-a} - 2(x^beta + x^{1-beta}) cos(gamma log x)]/(x log x).
        Checks: G(1-s) = G(s) at random points; the Mellin identity log G(s) = int x^{-s} f dx at s = 3, 2+5i; min f on (1, 1e8]
        for a >= beta (claimed >= 0) and for a < beta (expected negative somewhere).
Part B  Control 1, the virtual curve over F_5: Z(u) = (1-5u+5u^2)/((1-u)(1-5u)); b_d (closed points) >= 0 integers to d = 60;
        FE residual; zeros.  Genus-1 scan over F_5: L(u) = 1 - t u + 5u^2, t in Z, which t give b_d >= 0 for all d <= 60,
        and which of those violate Hasse |t| <= 2 sqrt 5.
Part C  Control 2, F_{5,5} = zeta(s)(1 + 5*5^{-s} + 5^{1-2s}): Lambda_F(5^k)/log 5 for k <= 6 (negative at 25), zeros of the factor.
"""
import cmath, math
import mpmath as mp
mp.mp.dps = 30

print("=== Part A: continuous sketch ===")
def G(s, beta, gamma, a):
    r = mp.mpc(beta, gamma)
    num = (s - r) * (s - mp.conj(r)) * (s - 1 + r) * (s - 1 + mp.conj(r))
    return num / ((s - a) ** 2 * (s - 1 + a) ** 2)
def f(x, beta, gamma, a):
    L = mp.log(x)
    return (2 * x ** a + 2 * x ** (1 - a) - 2 * (x ** beta + x ** (1 - beta)) * mp.cos(gamma * L)) / (x * L)
for (beta, gamma, a) in [(0.8, 20, 0.8), (0.8, 20, 0.9), (0.6, 14.1, 0.6), (0.8, 20, 0.7)]:
    sym = max(abs(G(s, beta, gamma, a) - G(1 - s, beta, gamma, a)) for s in [mp.mpc(0.3, 7.1), mp.mpc(2.2, -3), mp.mpc(-1.4, 0.5)])
    mel = []
    for s in [mp.mpf(3), mp.mpc(2, 5)]:
        I = mp.quad(lambda u: mp.e ** (-s * u) * f(mp.e ** u, beta, gamma, a) * mp.e ** u, [0, 1, 5, 20, 60, 200])
        mel.append(abs(mp.e ** I - G(s, beta, gamma, a)))   # compare exp: log branch-free
    xs = [1 + 10 ** (-6 + 14 * k / 20000.0) for k in range(20001)]   # log-spaced from 1+1e-6 to 1e8
    fmin = min(float(f(mp.mpf(x), beta, gamma, a)) for x in xs)
    print(f"  beta={beta} gamma={gamma} a={a}:  |G(s)-G(1-s)| <= {mp.nstr(sym, 3)}   |exp(int x^-s f) - G| = "
          f"{[mp.nstr(m, 3) for m in mel]}   min f on grid = {fmin:.4e}  ({'>= 0' if fmin >= 0 else 'NEGATIVE'})")

print("\n=== Part B: virtual curve over F_5 (control 1) ===")
def closed_points(q, t, D):
    # reciprocal roots of L(u) = 1 - t u + q u^2
    sp = [2, t]                                  # s_n = alpha^n + beta^n, exact: s_n = t s_{n-1} - q s_{n-2}
    for n in range(2, D + 1): sp.append(t * sp[-1] - q * sp[-2])
    N = [0] + [q ** n + 1 - sp[n] for n in range(1, D + 1)]
    b = [0] * (D + 1)
    for d in range(1, D + 1):   # Moebius inversion: N_n = sum_{d|n} d b_d
        b[d] = N[d] - sum(e * b[e] for e in range(1, d) if d % e == 0)
        assert b[d] % d == 0; b[d] //= d
    return N, b
N, b = closed_points(5, 5, 60)
print("  N_1..N_6 =", N[1:7], "  b_1..b_6 =", b[1:7], "  min_{d<=60} b_d =", min(b[1:]), " all integers: True")
u = mp.mpf('0.0137') + 0.021j
Z = lambda u: (1 - 5 * u + 5 * u ** 2) / ((1 - u) * (1 - 5 * u))
print("  FE residual |Z(1/(5u)) - Z(u)| (genus 1: Z(1/(qu)) = Z(u)) at a test point:", mp.nstr(abs(Z(1 / (5 * u)) - Z(u)), 3))
r1 = (5 + math.sqrt(5)) / 2
print(f"  reciprocal roots (5 +- sqrt5)/2; zeros of zeta_C(s) at Re s = log((5+sqrt5)/2)/log 5 = {math.log(r1)/math.log(5):.5f} and {1 - math.log(r1)/math.log(5):.5f}")
ok = []
for t in range(-12, 13):
    N, b = closed_points(5, t, 60)
    if min(N[1:]) >= 0 and min(b[1:]) >= 0:
        ok.append(t)
print("  genus-1 over F_5, L = 1 - t u + 5u^2: t with b_d >= 0 for all d <= 60:", ok)
print("    of these, Hasse |t| <= 2 sqrt 5 = 4.472 holds for", [t for t in ok if abs(t) <= 2 * math.sqrt(5)],
      "; RH-FALSE admissible t:", [t for t in ok if abs(t) > 2 * math.sqrt(5)])

print("\n=== Part C: F_{5,5} (control 2) ===")
# log(1 + 5u + 5u^2) with u = 5^{-s}: roots of 1 + 5u + 5u^2 = (1 - A u)(1 - B u), A + B = -5, AB = 5
A = (-5 + math.sqrt(5)) / 2; B = (-5 - math.sqrt(5)) / 2
for k in range(1, 7):
    lam = 1 - (A ** k + B ** k)        # Lambda_F(5^k)/log 5 = 1 (from zeta) - (A^k + B^k)
    print(f"  Lambda_F(5^{k})/log 5 = {lam:+.4f}")
for root in [(-5 + math.sqrt(5)) / 10, (-5 - math.sqrt(5)) / 10]:
    print(f"  zero of 1+5u+5u^2 at u = {root:.6f}: 5^(-sigma) = |u|  =>  sigma = {-math.log(abs(root))/math.log(5):.5f}")
