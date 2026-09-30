"""Seed M2, the Z side of class C (coordinates): three computations.
Z1  zeta(sigma) < 0 on (0,1): the Z-analog of V (a REAL off-line zero) does not exist, so over Z a one-sided upper bound
    psi(x) <= x + C x^theta already gives no zeros in Re s > theta (Landau), and Bombieri's twist step is not needed.
Z2  the Frobenius identity to second order: #{n mod p^2 : n^p = n mod p^2} (over F_q, f o phi = f^q holds identically,
    which is what makes Stepanov's auxiliary function vanish to order p^mu at every rational point).
Z3  Chebyshev's auxiliary integer C(2n, n): divisible by every prime in (n, 2n]; its size against the prime product."""
import math
import mpmath as mp

print("== Z1: eta(sigma) = sum (-1)^(n-1) n^-sigma > 0 and zeta(sigma) = eta/(1 - 2^(1-sigma)) < 0 on (0,1) ==")
mp.mp.dps = 30
worst = None
for k in range(1, 100):
    s = mp.mpf(k) / 100
    z = mp.zeta(s); e = mp.altzeta(s)
    assert e > 0 and z < 0, (s, z, e)
    val = float(z)
    worst = val if worst is None or val > worst else worst
print("sigma = 0.01..0.99 (99 points): all eta > 0, all zeta < 0; max zeta on grid = %.6f (at sigma -> 1 it tends to -inf, at 0 to -1/2)" % worst)
print("proof (elementary): eta(sigma) is an alternating series with decreasing terms, so 0 < 1 - 2^-sigma <= eta(sigma); and 1 - 2^(1-sigma) < 0")

print("\n== Z2: solutions of n^p = n in Z/p^2 (Frobenius identity to second order) ==")
rows = []
for p in [q for q in range(2, 110) if all(q % d for d in range(2, int(q**0.5) + 1))]:
    cnt = sum(1 for n in range(p * p) if (pow(n, p, p * p) - n) % (p * p) == 0)
    rows.append((p, cnt))
print("p : count  ->", ", ".join("%d:%d" % r for r in rows))
print("count == p for every p listed:", all(c == p for p, c in rows), "(the p Teichmuller residues; the other p^2 - p residues: order exactly 1)")

print("\n== Z3: Chebyshev's auxiliary integer C(2n,n) versus the primes it vanishes at ==")
N = 2 * 10**6
sieve = bytearray([1]) * (N + 1); sieve[0] = sieve[1] = 0
for i in range(2, int(N**0.5) + 1):
    if sieve[i]: sieve[i * i::i] = bytearray(len(range(i * i, N + 1, i)))
theta = [0.0] * (N + 1); acc = 0.0
for i in range(N + 1):
    if sieve[i]: acc += math.log(i)
    theta[i] = acc
for n in (10**3, 10**4, 10**5, 10**6):
    logC = math.lgamma(2 * n + 1) - 2 * math.lgamma(n + 1)
    prim = theta[2 * n] - theta[n]
    print("n=%7d: sum_{n<p<=2n} log p = %.1f ; log C(2n,n) = %.1f ; ratio = %.5f (2 log 2 = %.5f); per unit length %.5f" % (
        n, prim, logC, logC / prim, 2 * math.log(2), prim / n))
print("Stepanov's count over F_q has the sharp constant 1 (nu_1 <= q + O(sqrt q)); Chebyshev's auxiliary integer pays 2 log 2 = 1.386 per unit.")

print("\n== Z4: finite-support Chebyshev auxiliary integers F_x = prod_k (floor(x/k)!)^{c_k}: constant kappa = A T/(T-1) > 1 ==")
from fractions import Fraction
def cheb(c, T):
    assert sum(Fraction(ck, k) for k, ck in c.items()) == 0
    A = -sum(ck * math.log(k) / k for k, ck in c.items())
    g = lambda t: sum(ck * math.floor(t / k) for k, ck in c.items())
    L = 1
    for k in c: L = L * k // math.gcd(L, k)
    # integral of g(t) t^-2 over (0, inf): g is a step function, exact on [0, M], periodic tail handled by a long cutoff
    M = 2000 * L; pts = sorted({j * k for k in c for j in range(1, M // k + 1)})
    I = 0.0; prev = 0.0
    for a in pts:
        I += g(prev) * (1 / prev - 1 / a) if prev > 0 else 0.0
        prev = a
    ok = all(g(t + 1e-9) >= 0 for t in range(0, 5 * L)) and all(g(t + 1e-9) >= 1 for t in range(1, T))
    return A, I, A * T / (T - 1), ok
for name, c, T in [("Chebyshev 1852 (1,-1,-1,-1,+1 at 1,2,3,5,30)", {1: 1, 2: -1, 3: -1, 5: -1, 30: 1}, 6),
                   ("binomial C(2n,n) weights {1:1, 2:-2}: balance check", None, None)]:
    if c is None:
        print(name, "- sum c_k/k = 0:", sum(Fraction(v, k) for k, v in {1: 1, 2: -2}.items()) == 0); continue
    A, I, kappa, ok = cheb(c, T)
    print("%s: A = -sum c_k log k / k = %.6f ; int_0^inf g t^-2 dt (cutoff) = %.6f ; g>=0 and g>=1 on [1,%d): %s ; kappa = A T/(T-1) = %.6f > 1" % (name, A, I, T, ok, kappa))
cb = {1: 1, 2: -2}
A = -sum(ck * math.log(k) / k for k, ck in cb.items())
print("C(2n,n) as F_x with x = 2n, weights {1:1, 2:-2}: A = log 4 / ... per unit x: %.6f ; g = floor(t) - 2 floor(t/2) in {0,1}, = 1 on [1,2): kappa = 2A = %.6f" % (A, 2 * A))
