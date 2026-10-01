# Orchestrator (Session 40): independent brute force of Theorem R1 (necklace deletion) in F_q[T], q = 3 and q = 5.
# Polynomials as integers in base q (monic of degree n: leading digit 1).  Multiply all pairs to mark reducibles;
# delete the LAST M(a, N) irreducibles of each degree (any choice works), count R-free monic polynomials by
# multiplicative closure (generate all products of non-deleted irreducibles).
import itertools, sys
from sympy import mobius, divisors
def run(q, a, D):
    def mul(f, g):  # coefficient lists, low degree first
        h = [0] * (len(f) + len(g) - 1)
        for i, x in enumerate(f):
            if x:
                for j, y in enumerate(g): h[i + j] = (h[i + j] + x * y) % q
        return tuple(h)
    monic = {n: [tuple(c) + (1,) for c in itertools.product(range(q), repeat=n)] for n in range(1, D + 1)}
    red = set()
    for n1 in range(1, D):
        for n2 in range(n1, D - n1 + 1):
            for f in monic[n1]:
                for g in monic[n2]: red.add(mul(f, g))
    irr = {n: [f for f in monic[n] if f not in red] for n in range(1, D + 1)}
    M = lambda a, N: sum(mobius(N // d) * a**d for d in divisors(N)) // N
    keep = []
    for n in range(1, D + 1):
        assert len(irr[n]) == M(q, n)
        keep += irr[n][:len(irr[n]) - M(a, n)]
    # count R-free monic polynomials of each degree: closure under multiplication by kept irreducibles
    free = {0: {(1,)}}
    for n in range(1, D + 1): free[n] = set()
    for p in keep:                      # each kept irreducible, unbounded multiplicity, ascending degree order
        dp = len(p) - 1
        for n in range(dp, D + 1):
            for f in list(free[n - dp]): free[n].add(mul(f, p))
    return [len(free[n]) for n in range(1, D + 1)], [q**n - a * q**(n - 1) for n in range(1, D + 1)], [M(a, n) for n in range(1, D + 1)]
for q, a, D in [(3, 2, 7), (5, 2, 4), (5, 3, 4)]:
    got, want, m = run(q, a, D)
    print(f"q={q} a={a}: deleted per degree {m}; R-free counts {got}; q^n - a q^(n-1) = {want}; equal: {got == want}")
