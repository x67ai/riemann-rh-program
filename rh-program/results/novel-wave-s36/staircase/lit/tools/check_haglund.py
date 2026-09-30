#!/usr/bin/env python3
"""Check (mpmath, 40 digits) how Haglund's approximant Xi_N(z) (arXiv:0910.5228, eqs. (10),(13),(14))
relates to the truncation of Riemann's incomplete-gamma series used by the staircase seed:
    xi_N(s) := 1/2 + 1/2 s(s-1) sum_{n<=N} g_n(s),
    g_n(s)  = (pi n^2)^{-s/2} Gamma(s/2, pi n^2) + (pi n^2)^{-(1-s)/2} Gamma((1-s)/2, pi n^2),   s = 1/2 + i z.
Claim derived by hand from Gamma(w+1,a) = w Gamma(w,a) + a^w e^{-a}:
    Phi_n(z) = 1/2 s(s-1) g_n(s) + (4 pi n^2 - 1) e^{-pi n^2}
so  Xi_N(z) = xi_N(s) - c_N,  c_N = sum_{n>N} (4 pi n^2 - 1) e^{-pi n^2}  (using sum_{n>=1} (4 pi n^2-1) e^{-pi n^2} = 1/2).
Also evaluates Xi_1 at the zeros Haglund lists in his Appendix (p. 16).
"""
from mpmath import mp, mpf, mpc, gammainc, pi, exp, nsum, inf, quad, cos, zeta, gamma

mp.dps = 40


def G(z, a, b):  # Haglund eq. (10): Gamma(b+iz,a)/a^(b+iz) + Gamma(b-iz,a)/a^(b-iz)
    return gammainc(b + 1j * z, a) / a ** (b + 1j * z) + gammainc(b - 1j * z, a) / a ** (b - 1j * z)


def Phi(n, z):  # Haglund eq. (14)
    a = pi * n ** 2
    return 2 * pi ** 2 * n ** 4 * G(z / 2, a, mpf(9) / 4) - 3 * pi * n ** 2 * G(z / 2, a, mpf(5) / 4)


def g(n, s):
    a = pi * n ** 2
    return a ** (-s / 2) * gammainc(s / 2, a) + a ** (-(1 - s) / 2) * gammainc((1 - s) / 2, a)


def xiC1(N, s):
    return mpf(1) / 2 + s * (s - 1) / 2 * sum(g(n, s) for n in range(1, N + 1))


print("sum_{n>=1}(4 pi n^2 - 1) e^{-pi n^2} =", nsum(lambda n: (4 * pi * n ** 2 - 1) * exp(-pi * n ** 2), [1, inf]))
for z in [mpc(3.7, 0), mpc(20.6, 2.7), mpc(-5.1, 11.3), mpc(40, 0.25)]:
    s = mpf(1) / 2 + 1j * z
    for n in (1, 2):
        lhs = Phi(n, z)
        rhs = s * (s - 1) / 2 * g(n, s) + (4 * pi * n ** 2 - 1) * exp(-pi * n ** 2)
        print(f"z={complex(z)} n={n}: |Phi_n - [s(s-1)/2 g_n + (4pi n^2-1)e^(-pi n^2)]| = {mp.nstr(abs(lhs - rhs), 5)}  |Phi_n|={mp.nstr(abs(lhs), 5)}")

# Haglund eq. (2)-(3): Xi_1(z) = int_0^inf cos(z t) phi_1(t) dt, phi_1(t)=exp(-pi e^{2t})(8 pi^2 e^{4.5t} - 12 pi e^{2.5t})
z0 = mpf(3.7)
I = quad(lambda t: cos(z0 * t) * exp(-pi * exp(2 * t)) * (8 * pi ** 2 * exp(4.5 * t) - 12 * pi * exp(2.5 * t)), [0, 1, 2, 4])
print("Xi_1(3.7) via integral (2):", mp.nstr(I, 20), " via (14):", mp.nstr(Phi(1, z0).real, 20))
# full Xi versus Riemann xi at a sample point (N large)
s = mpf(1) / 2 + 1j * z0
xi = s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)
print("xi(1/2+3.7i) =", mp.nstr(xi, 20), "  sum_{n<=4} Phi_n(3.7) =", mp.nstr(sum(Phi(n, z0) for n in range(1, 5)), 20))

c1 = nsum(lambda n: (4 * pi * n ** 2 - 1) * exp(-pi * n ** 2), [2, inf])
print("c_1 = sum_{n>=2}(4 pi n^2-1)e^{-pi n^2} =", mp.nstr(c1, 15))
# Haglund's appendix zeros of Xi_1 (p. 16)
for zz in [mpc("14.04543957882981756479858"), mpc("20.62534600592171760132974", "2.697151842339519632505712"),
           mpc("96.90904939663401491219210", "40.51951660155401879741380")]:
    s = mpf(1) / 2 + 1j * zz
    print(f"Haglund zero z={mp.nstr(zz, 12)}: |Xi_1(z)| = {mp.nstr(abs(Phi(1, zz)), 5)};  |xi_1^C1(s)| = {mp.nstr(abs(xiC1(1, s)), 5)}  (s = {mp.nstr(s, 8)})")
