#!/usr/bin/env python3
"""Reader-O checks of NOTE Prop. 1.1 (conj-O-s38), own code. Log: logs/euler_O.log
(A) reflected form: class sums of zeta(1-s)D_R(s) = sum_n sum_{m|Q} mu(m) n^(s-1) m^(-s) computed by RAW GROUPING of the pairs
    (n, m) by the reduced fraction n/m = a/b (complete classes only), against the claimed a^(s-1) b^(-s) mu(b) rho / prod_{p|b}(1-1/p);
    then the diagonal sum_{a,b} |class|^2 (a <= A from the brute classes, a > A by Hurwitz zeta with inclusion-exclusion) against
    the corrected product rho^2 zeta(2-2sig) prod(1 + p^(-2sig)(1-p^(2sig-2))(1-1/p)^(-2)) and the brief's sketch (no (1-p^(2sig-2))).
(B) additive form: Fourier coefficients c(a/b) of the Q-periodic E, INCLUDING b = 1, by exact integration, against
    rho mu(b) b/(2 pi i a phi(b)); Parseval sums with and without the b = 1 frequencies.
(C) Parseval constant (1/Q) int_0^Q E^2 = rho 2^|R| / 12 in exact rationals.
"""
import math
from fractions import Fraction
from itertools import combinations
import mpmath as mp

def sqfree_divs(R):
    out = []
    for k in range(len(R) + 1):
        for c in combinations(R, k):
            out.append((math.prod(c), (-1) ** k, c))
    return out

def part_A(R, s, Nmax):
    Q = math.prod(R); divs = sqfree_divs(R)
    rho = mp.fprod([1 - mp.mpf(1) / p for p in R])
    classes = {}
    for (m, mu, _) in divs:
        ms = mp.power(m, -s)
        for n in range(1, Nmax + 1):
            g = math.gcd(n, m); key = (n // g, m // g)
            classes[key] = classes.get(key, 0) + mu * mp.power(n, s - 1) * ms
    A = Nmax // Q                        # classes with a <= A are complete (k | Q/b, n = k a <= Q a)
    worst = mp.mpf(0); diag = mp.mpf(0); Cb = {}
    for (a, b), v in classes.items():
        if a > A: continue
        pb = [p for p in R if b % p == 0]
        pred = mp.power(a, s - 1) * mp.power(b, -s) * (-1) ** len(pb) * rho / mp.fprod([1 - mp.mpf(1) / p for p in pb])
        worst = max(worst, abs(v - pred) / abs(pred)); diag += abs(v) ** 2
        if a == 1: Cb[b] = v * mp.power(b, s)          # class constant from the brute class a = 1
    sig = mp.re(s); tail = mp.mpf(0)
    for b, C in Cb.items():                              # a > A, (a, b) = 1: sum a^(2sig-2) by inclusion-exclusion
        pb = [p for p in R if b % p == 0]
        t = mp.mpf(0)
        for (d, mud, _) in sqfree_divs(pb):
            t += mud * mp.power(d, 2 * sig - 2) * mp.zeta(2 - 2 * sig, mp.floor(mp.mpf(A) / d) + 1)
        tail += abs(C) ** 2 * mp.power(b, -2 * sig) * t
    corr = rho ** 2 * mp.zeta(2 - 2 * sig) * mp.fprod([1 + mp.power(p, -2 * sig) * (1 - mp.power(p, 2 * sig - 2)) / (1 - mp.mpf(1) / p) ** 2 for p in R])
    sketch = rho ** 2 * mp.zeta(2 - 2 * sig) * mp.fprod([1 + mp.power(p, -2 * sig) / (1 - mp.mpf(1) / p) ** 2 for p in R])
    tot = diag + tail
    print(f"(A) R={R} s={mp.nstr(s, 4)} Nmax={Nmax} A={A}: class-sum max rel err={mp.nstr(worst, 3)};"
          f" diagonal={mp.nstr(tot, 14)} corrected={mp.nstr(corr, 14)} (rel {mp.nstr(abs(tot - corr) / corr, 3)}) sketch={mp.nstr(sketch, 10)}")

def coeff(R, a, b):
    """(1/Q) int_0^Q E(x) e(-a x/b) dx exactly (mpmath), E = N - rho x piecewise linear."""
    Q = math.prod(R); rho = Fraction(math.prod(p - 1 for p in R), Q)
    w = 2j * mp.pi * mp.mpf(a) / b; N = 0; tot = mp.mpc(0)
    for n in range(Q):
        if math.gcd(n, Q) == 1: N += 1                  # N(x) = #{1 <= k <= x : (k, Q) = 1}; n = 0 contributes nothing
        e0, e1 = mp.exp(-w * n), mp.exp(-w * (n + 1))
        I0 = (e0 - e1) / w; I1 = (n * e0 - (n + 1) * e1) / w + I0 / w
        tot += N * I0 - mp.mpf(rho.numerator) / rho.denominator * I1
    return tot / Q

def part_B(R, amax=4):
    Q = math.prod(R); rho = mp.mpf(math.prod(p - 1 for p in R)) / Q
    worst = mp.mpf(0); c1 = None
    for (b, mu, pr) in sqfree_divs(R):
        phib = math.prod(p - 1 for p in pr)
        for a in range(1, amax + 1):
            if math.gcd(a, b) != 1: continue
            c = coeff(R, a, b); pred = rho * mu * b / (2j * mp.pi * a * phib)
            worst = max(worst, abs(c - pred) / abs(pred))
            if b == 1 and a == 1: c1 = c
    full = rho ** 2 / 12 * mp.fprod([1 + mp.mpf(p + 1) / (p - 1) for p in R])
    print(f"(B) R={R}: max rel err of c(a/b), b | Q INCLUDING b = 1, a <= {amax}: {mp.nstr(worst, 3)};  c(1/1) = {mp.nstr(c1, 10)}"
          f" vs rho/(2 pi i) = {mp.nstr(rho / (2j * mp.pi), 10)};  Parseval all b: {mp.nstr(full, 12)} = rho 2^|R|/12 = "
          f"{mp.nstr(rho * 2 ** len(R) / 12, 12)};  without b = 1: {mp.nstr(full - rho ** 2 / 12, 12)}")

def part_C(R):
    Q = math.prod(R); rho = Fraction(math.prod(p - 1 for p in R), Q); N = 0; tot = Fraction(0)
    for n in range(Q):
        if math.gcd(n, Q) == 1: N += 1
        e = N - rho * n                                    # E(n + u) = e - rho u, int_0^1 = e^2 - e rho + rho^2/3
        tot += e * e - e * rho + rho * rho / 3
    ms = tot / Q; pred = rho * 2 ** len(R) / 12
    print(f"(C) R={R}: (1/Q) int E^2 = {ms}  rho 2^|R|/12 = {pred}  equal={ms == pred}")

if __name__ == "__main__":
    mp.mp.dps = 30
    for R, s, Nmax in (([2], mp.mpf("0.2"), 60000), ([2, 3], mp.mpc("0.3", "7.5"), 60000), ([2, 3, 5], mp.mpf("0.35"), 90000),
                       ([3, 7, 11], mp.mpc("0.1", "-3"), 231000), ([2, 5, 13], mp.mpf("0.45"), 130000)):
        part_A(R, s, Nmax)
    for R in ([2], [2, 3], [3, 5], [2, 3, 5]):
        part_B(R)
    for R in ([2], [3], [2, 3], [2, 3, 5], [3, 5, 7], [2, 3, 5, 7], [2, 3, 5, 7, 11], [5, 7, 11, 13]):
        part_C(R)
