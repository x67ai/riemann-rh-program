# Orchestrator re-derivation (Session 26) of scout O's P1 claim: on Borger's W*(Spec Z), with ghost components
# G_1 (a_1) and G_n (a_n), the intersection G_1 ∩ G_n = Spec(Z ⊗_{W(Z)} Z) = Spec(Z / I_n), I_n = {a_1 - a_n : a in W(Z)},
# and deg := log #(Z/I_n) equals Λ(n).  Input (printed): W(Z) = ghost vectors (a_j) in Z^N with
# a_j ≡ a_{pj} (mod p^{1+v_p(j)}) for all j and all primes p  (Borger, arXiv:0801.1691 p. 10, (1.10), as quoted by scout O).
# Method: brute force over ghost vectors supported on indices ≤ N with entries in a box; compute gcd of all a_1 - a_n.
# Also checks I_n = {a_1 : a_n = 0} (constants are ghost vectors), which is the tensor-product ideal.
import itertools, math, sys
from sympy import primerange, factorint
N = int(sys.argv[1]) if len(sys.argv) > 1 else 12
B = int(sys.argv[2]) if len(sys.argv) > 2 else 6   # entries in [-B, B]
primes = list(primerange(2, N + 1))
idx = list(range(1, N + 1))
def vp(p, j):
    c = 0
    while j % p == 0: j //= p; c += 1
    return c
def is_ghost(a):  # a: dict j -> a_j for j ≤ N; congruences only among indices ≤ N
    for p in primes:
        for j in idx:
            if p * j <= N and (a[j] - a[p * j]) % (p ** (1 + vp(p, j))) != 0:
                return False
    return True
# Enumerate ghost vectors as follows: a_j determined freely for j not divisible by any prime? No — enumerate all boxes
# would be |2B+1|^N; instead build vectors by choosing a_j for j in increasing order subject to the congruences with divisors.
def gen():
    a = {}
    def rec(k):
        if k > N:
            yield dict(a); return
        for v in range(-B, B + 1):
            ok = True
            for p in primes:
                if k % p == 0:
                    j = k // p
                    if (a[j] - v) % (p ** (1 + vp(p, j))) != 0: ok = False; break
            if ok:
                a[k] = v
                yield from rec(k + 1)
                del a[k]
    yield from rec(1)
vecs = list(gen())
assert all(is_ghost(a) for a in vecs)
print(f"N={N} B={B}: {len(vecs)} ghost vectors enumerated")
def Lambda(n):
    f = factorint(n)
    return math.log(list(f)[0]) if len(f) == 1 else 0.0
ok = True
for n in range(2, N + 1):
    g1 = 0
    for a in vecs: g1 = math.gcd(g1, abs(a[1] - a[n]))
    g2 = 0
    for a in vecs:
        if a[n] == 0: g2 = math.gcd(g2, abs(a[1]))
    deg = math.log(g1) if g1 > 0 else float('inf')
    lam = Lambda(n)
    flag = "OK" if (g1 == g2 and abs(deg - lam) < 1e-12) else "MISMATCH"
    if flag != "OK": ok = False
    print(f"n={n:2d}  gcd(a1-an)={g1:2d}  gcd(a1 | an=0)={g2:2d}  deg=log#(Z/I)={deg:.6f}  Λ(n)={lam:.6f}  {flag}")
print("ALL n ≤", N, "AGREE: deg(G_1 ∩ G_n) = Λ(n)" if ok else "SOME MISMATCH")
