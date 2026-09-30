#!/usr/bin/env python3
"""Task 1 checks (conj-O-s38). Log: verify/logs/t1_classsums.log
(a) Additive class sums: for finite R, the Fourier coefficient of the Q-periodic E(x) = N_P(x) - rho x at frequency a/b
    (a/b reduced, b | Q) equals c(a/b) = rho mu(b) b / (2 pi i a phi(b)); Parseval sum = rho 2^|R| / 12 = (1/Q) int_0^Q E^2.
    Coefficients computed by exact integration of the piecewise-linear E over one period (closed form per unit interval).
(b) Reflected (Mellin) diagonal: sum_{a>=1} sum_{b in <R>, (a,b)=1} a^(2s-2) b^(-2s) (b/phi(b))^2
    = zeta(2-2s) prod_{p in R} (1 + p^(-2s) (1 - p^(2s-2)) / (1-1/p)^2)   [corrected: coprimality factor (1 - p^(2s-2))]
    versus the brief's sketch zeta(2-2s) prod (1 + p^(-2s)(1-1/p)^(-2)). Brute force over a <= A with exact tail via Hurwitz zeta.
(c) |chi(sigma+it)| (|t|/2pi)^(sigma-1/2) -> 1 (Stirling; used in Prop. C4 / Theorem Z), spot check with mpmath.
"""
from fractions import Fraction
from itertools import combinations
import cmath, math
import mpmath as mp

def squarefree_divisors(R):
    out = []
    for k in range(len(R) + 1):
        for c in combinations(R, k):
            m = 1
            for p in c: m *= p
            out.append((m, (-1) ** k, c))
    return out

def check_a(R, nfreq=6):
    Q = math.prod(R)
    rho = Fraction(1)
    for p in R: rho *= Fraction(p - 1, p)
    # N(n) for n = 0..Q-1: count of k in [1, n] coprime to Q
    N = [0] * (Q + 1)
    for n in range(1, Q + 1):
        N[n] = N[n - 1] + (1 if math.gcd(n, Q) == 1 else 0)
    # exact mean square over a period: int_n^{n+1} (e - rho t)^2 dt, e = N(n) - rho n
    ms = Fraction(0)
    for n in range(Q):
        e = N[n] - rho * n
        ms += e * e - e * rho + rho * rho / 3
    ms /= Q
    pred = rho * 2 ** len(R) / 12
    print(f"R={R} Q={Q} rho={rho}  (1/Q)int E^2 = {ms}  rho*2^|R|/12 = {pred}  equal={ms == pred}")
    # Fourier coefficients c(nu) = (1/Q) int_0^Q E(x) e(-nu x) dx, nu = a/b
    worst = 0.0
    rf = float(rho)
    for (b, mub, primes) in squarefree_divisors(R):
        if b == 1: continue
        phib = math.prod(p - 1 for p in primes)
        for a in range(1, nfreq + 1):
            if math.gcd(a, b) != 1: continue
            nu = a / b; w = 2j * math.pi * nu
            tot = 0j
            for n in range(Q):
                e = float(N[n] - rho * n)
                # int_n^{n+1} (e - rho t) exp(-w (n+t')) ... closed form with x = n + u, u in [0,1]
                ex0 = cmath.exp(-w * n); ex1 = cmath.exp(-w * (n + 1))
                I0 = (ex0 - ex1) / w                        # int exp(-w x) dx over [n, n+1]
                I1 = (n * ex0 - (n + 1) * ex1) / w + I0 / w  # int x exp(-w x) dx over [n, n+1]
                tot += (N[n]) * I0 - rf * I1
            c_num = tot / Q
            c_pred = rf * mub * b / (2j * math.pi * a * phib)
            worst = max(worst, abs(c_num - c_pred) / abs(c_pred))
    # Parseval of the predicted coefficients (all a != 0, both signs): (rho^2/12) prod (1 + (1-p^-2)/(1-1/p)^2)
    pars = rf * rf / 12 * math.prod(1 + (1 - p ** -2) / (1 - 1 / p) ** 2 for p in R)
    print(f"   max rel. error of c(a/b) vs rho mu(b) b/(2 pi i a phi(b)) over a<= {nfreq}: {worst:.2e};"
          f"  Parseval of predicted c = {pars:.12f} vs {float(pred):.12f}")

def check_b(R, s):
    s = mp.mpf(s)
    divs = squarefree_divisors(R)
    A = 200000
    tot = mp.mpf(0)
    for (b, mub, primes) in divs:
        g = mp.mpf(b) ** (-2 * s) * (mp.mpf(b) / math.prod(p - 1 for p in primes)) ** 2 if b > 1 else mp.mpf(1)
        # sum over a >= 1 coprime to b of a^(2s-2): brute force a <= A, tail by inclusion-exclusion Hurwitz
        head = mp.fsum(mp.mpf(a) ** (2 * s - 2) for a in range(1, A + 1) if math.gcd(a, b) == 1)
        tail = mp.mpf(0)
        for (d, mud, _) in squarefree_divisors(list(primes)):
            tail += mud * mp.mpf(d) ** (2 * s - 2) * mp.zeta(2 - 2 * s, mp.floor(A / d) + 1)
        tot += g * (head + tail)
    corr = mp.zeta(2 - 2 * s) * mp.fprod(1 + mp.mpf(p) ** (-2 * s) * (1 - mp.mpf(p) ** (2 * s - 2)) / (1 - mp.mpf(1) / p) ** 2 for p in R)
    sketch = mp.zeta(2 - 2 * s) * mp.fprod(1 + mp.mpf(p) ** (-2 * s) / (1 - mp.mpf(1) / p) ** 2 for p in R)
    print(f"R={R} sigma={s}: brute={mp.nstr(tot, 12)} corrected={mp.nstr(corr, 12)} sketch={mp.nstr(sketch, 12)}"
          f"  rel(brute-corrected)={mp.nstr(abs(tot - corr) / corr, 3)}")

def check_c():
    for sig in [0.1, 0.25, 0.4]:
        row = []
        for t in [50, 500, 5000]:
            s = mp.mpc(sig, t)
            chi = mp.power(2, s) * mp.power(mp.pi, s - 1) * mp.sin(mp.pi * s / 2) * mp.gamma(1 - s)
            row.append(mp.nstr(abs(chi) * mp.power(t / (2 * mp.pi), sig - 0.5), 8))
        print(f"sigma={sig}: |chi|(t/2pi)^(sigma-1/2) at t=50,500,5000: {row}")

if __name__ == "__main__":
    mp.mp.dps = 30
    print("(a) additive class sums, finite R")
    for R in ([2], [3], [2, 3], [2, 5], [3, 7], [2, 3, 5], [2, 3, 7], [2, 3, 5, 7], [3, 5, 7, 11]):
        check_a(R)
    print("(b) reflected Mellin diagonal (finite R)")
    for R, s in (([2], 0.2), ([2, 3], 0.3), ([2, 3, 5], 0.35), ([3, 7, 11], 0.1)):
        check_b(R, s)
    print("(c) Stirling spot check for chi")
    check_c()
