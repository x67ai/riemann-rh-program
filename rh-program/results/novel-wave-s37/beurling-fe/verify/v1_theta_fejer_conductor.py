#!/usr/bin/env python3
"""v1 -- seed M1a beurling-fe (Session 37).  Numerical companion to NOTE §3, §4, §8(b).

Part 1  Riemann's theta relation (Prop. R (B)) for Z: rho + 2psi(1/x) = sqrt(x)(rho + 2psi(x)), rho = 1.
Part 2  The Fejer quantity S_F = sum_k sinc^2(n_k), sinc(t) = sin(pi t)/(pi t), for Z (zero) and three
        Beurling near-misses, with the theta-relation defect at x = 1/2, 2 (the FE must fail for them, by Theorem T).
Part 3  Conductor-q identity (NOTE §8(b), Theorem C):  rho_q (1 - q^{-1/2}) = 2 q^{-1/2} sum_k c_k sinc^2(n_k/q),
        rho_q = sqrt(q) Res_{s=1} F, checked on F = zeta(s)(1 + q^{1/2-s}) (q = 2, 4, 9) and F_{5,5} = zeta(s)(1+5*5^{-s}+5^{1-2s});
        each also checked to satisfy the conductor-q theta relation (so the identity is tested on genuine solutions).
Pure computation; no claim rests on floating point beyond what is printed.
"""
import math
import mpmath as mp

mp.mp.dps = 60

def sinc2(t):
    if t == 0:
        return 1.0
    v = math.sin(math.pi * t) / (math.pi * t)
    return v * v

def beurling_integers(primes, X):
    """All products (with multiplicity) of the multiset 'primes' that are <= X. Returns sorted list."""
    primes = sorted(primes)
    out = [1.0]
    def rec(start, val):
        for i in range(start, len(primes)):
            v = val * primes[i]
            if v > X * (1 + 1e-12):
                break
            out.append(v)
            rec(i, v)
    rec(0, 1.0)
    out.sort()
    return out

def rational_primes(X):
    s = bytearray([1]) * (X + 1); s[0] = s[1] = 0
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i*i::i] = bytearray(len(s[i*i::i]))
    return [i for i in range(X + 1) if s[i]]

def psi(freqs, masses, x):
    return mp.fsum(m * mp.e ** (-mp.pi * mp.mpf(f) ** 2 * x) for f, m in zip(freqs, masses))

print("=== Part 1: theta relation for Z (rho = 1) ===")
Z = list(range(1, 200)); ones = [1] * len(Z)
for x in [mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf(1), mp.mpf('1.9'), mp.mpf('3.3')]:
    d = (1 + 2 * psi(Z, ones, 1 / x)) - mp.sqrt(x) * (1 + 2 * psi(Z, ones, x))
    print(f"  x = {float(x):4.2f}   defect = {mp.nstr(d, 5)}")

print("\n=== Part 2: Fejer sum S_F = sum_k sinc^2(n_k) and theta defect for near-miss Beurling systems ===")
X = 20000
P = rational_primes(X)
systems = {
    "Z (rational primes)": (P, 1.0),
    "2 -> 2.01": ([2.01] + P[1:], (1 - 1/2) / (1 - 1/2.01)),
    "(P minus {2}) + {sqrt 2}": ([math.sqrt(2)] + P[1:], (1 - 1/2) / (1 - 2 ** -0.5)),
    "P + {1.5}": ([1.5] + P, 1 / (1 - 1/1.5)),
}
for name, (pr, rho) in systems.items():
    N = beurling_integers(pr, X)
    SF = sum(sinc2(n) for n in N)
    tail = rho / (math.pi ** 2 * X)          # sum_{n_k > X} (pi n_k)^-2 <~ rho/(pi^2 X)
    Nsmall = [n for n in N if n <= 60]
    defs = []
    for x in [mp.mpf('0.5'), mp.mpf(2)]:
        d = (rho + 2 * psi(Nsmall, [1] * len(Nsmall), 1 / x)) - mp.sqrt(x) * (rho + 2 * psi(Nsmall, [1] * len(Nsmall), x))
        defs.append(mp.nstr(d, 4))
    print(f"  {name:28s} rho = {rho:.6f}  #n_k<=X: {len(N):6d}  S_F = {SF:.3e} (tail <= {tail:.1e})  theta defect x=1/2,2: {defs}")

print("\n=== Part 3: conductor-q identity on genuine conductor-q solutions ===")
def conductor_example(q, coeff, rhoF, coeff_mp, rhoF_mp, nmax=200000):
    rq = math.sqrt(q)
    lhs = rq * rhoF * (1 - 1 / rq)
    rhs = 2 / rq * sum(coeff(n) * sinc2(n / q) for n in range(1, nmax))
    # theta relation with frequencies n/sqrt(q)
    fr = [mp.mpf(n) / mp.sqrt(q) for n in range(1, 400)]; ms = [coeff_mp(n) for n in range(1, 400)]
    rq_mp = mp.sqrt(q) * rhoF_mp
    tdef = max(abs((rq_mp + 2 * psi(fr, ms, 1 / x)) - mp.sqrt(x) * (rq_mp + 2 * psi(fr, ms, x)))
               for x in [mp.mpf('0.6'), mp.mpf(1), mp.mpf('1.7')])
    return lhs, rhs, tdef
cases = [
    ("zeta(s)(1+2^{1/2-s})  q=2", 2, lambda n: 1 + (math.sqrt(2) if n % 2 == 0 else 0), 1 + math.sqrt(2) / 2,
     lambda n: 1 + (mp.sqrt(2) if n % 2 == 0 else 0), 1 + mp.sqrt(2) / 2),
    ("zeta(s)(1+4^{1/2-s})  q=4", 4, lambda n: 1 + (2 if n % 4 == 0 else 0), 1 + 2 / 4,
     lambda n: 1 + (2 if n % 4 == 0 else 0), mp.mpf(3) / 2),
    ("zeta(s)(1+9^{1/2-s})  q=9", 9, lambda n: 1 + (3 if n % 9 == 0 else 0), 1 + 3 / 9,
     lambda n: 1 + (3 if n % 9 == 0 else 0), mp.mpf(4) / 3),
    ("F_{5,5}               q=25", 25, lambda n: 1 + (5 if n % 5 == 0 else 0) + (5 if n % 25 == 0 else 0), 1 + 1 + 5 / 25,
     lambda n: 1 + (5 if n % 5 == 0 else 0) + (5 if n % 25 == 0 else 0), mp.mpf(11) / 5),
]
for name, q, cf, rhoF, cfm, rhoFm in cases:
    lhs, rhs, tdef = conductor_example(q, cf, rhoF, cfm, rhoFm)
    print(f"  {name}:  rho_q(1-q^-1/2) = {lhs:.10f}   2q^-1/2 sum c_k sinc^2(n_k/q) = {rhs:.10f}   theta-rel defect {mp.nstr(tdef, 3)}")
print("\nDone.")
