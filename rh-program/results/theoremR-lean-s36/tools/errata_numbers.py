"""errata_numbers.py -- Session 36, theoremR-lean-s36 builder: the numbers behind PREDERIVATION-ERRATA.md.
[N1] item 7 (theoremS_bound): exact symbolic sharpness at x = r^2, L = 1 + r^2 + 2 g r; the g = 0 boundary; x < 0 infeasible;
     a seeded random search (x in [-5, 3 r^2 + 2]) for (g, x, L) meeting h1 and h2 with L above the bound -- expect none.
[N2] item 6 (theoremR): kappa < 0 is NOT contradictory -- cls = id, v(n) = Lambda(n)/kappa meets hA9 at every n >= 2 (fiber {n}).
[N3] item 8 (theoremS): the first prime that violates the bound, for a few (kappa, g).
[N4] items 2, 3: hypotheses needed / removable -- N = 0 makes log N = 0 (Mathlib's convention Real.log 0 = 0).
"""
import math, random
import sympy as sp

print("[N1] item 7")
g, s = sp.symbols("g s", nonnegative=True)
r = (1 + sp.sqrt(1 + 8 * g)) / 2
x = r ** 2
L = 1 + r ** 2 + 2 * g * r
h1_gap = sp.simplify(sp.expand(4 * g ** 2 * x - (1 + x - L) ** 2))
h2_gap = sp.simplify(sp.expand(4 * g ** 2 * x ** 2 - (1 + x ** 2 - L) ** 2))
bound = (1 + 2 * g) * (1 + r)
print("  r^2 - r - 2g =", sp.simplify(sp.expand(r ** 2 - r - 2 * g)))
print("  at x = r^2, L = 1 + r^2 + 2gr: 4g^2x - (1+x-L)^2 =", h1_gap, "; 4g^2x^2 - (1+x^2-L)^2 =", h2_gap)
print("  (1+2g)(1+r) - (1 + r^2 + 2gr) =", sp.simplify(sp.expand(bound - L)))
print("  factorization used: s^4 - s^2 - 2g s^2 - 2g s =", sp.factor(s ** 4 - s ** 2 - 2 * g * s ** 2 - 2 * g * s))
# g = 0: h1, h2 force L = 1 + x = 1 + x^2
xs = sp.symbols("xs", real=True)
print("  g = 0: solutions of x = x^2:", sp.solve(sp.Eq(xs, xs ** 2), xs), "-> L in {1, 2}; bound at g = 0:", sp.nsimplify(bound.subs(g, 0)))
random.seed(20260930)
viol = 0; feas = 0; neg_feas = 0
for _ in range(400000):
    gg = random.choice([0.0, random.uniform(0, 0.1), random.uniform(0, 3), random.uniform(0, 50)])
    rr = (1 + math.sqrt(1 + 8 * gg)) / 2
    xx = random.uniform(-5, 3 * rr * rr + 2)
    if xx >= 0:
        lo = max(1 + xx - 2 * gg * math.sqrt(xx), 1 + xx * xx - 2 * gg * xx)
        hi = min(1 + xx + 2 * gg * math.sqrt(xx), 1 + xx * xx + 2 * gg * xx)
        cands = [hi, lo, random.uniform(lo - 1, hi + 1)]
    else:
        cands = [1 + xx, 1 + xx * xx, random.uniform(-10, 10)]
    for LL in cands:
        ok1 = (1 + xx - LL) ** 2 <= 4 * gg * gg * xx + 1e-12
        ok2 = (1 + xx * xx - LL) ** 2 <= 4 * gg * gg * xx * xx + 1e-12
        if ok1 and ok2:
            feas += 1
            if xx < -1e-9: neg_feas += 1
            if LL > (1 + 2 * gg) * (1 + rr) + 1e-9: viol += 1
print(f"  random search: {feas} feasible (g, x, L) found, {neg_feas} with x < 0, {viol} above the bound")

print("[N2] item 6: kappa < 0 satisfiable")
def Lam(n):
    f = sp.factorint(n)
    return math.log(next(iter(f))) if len(f) == 1 else 0.0
for kappa in [-1.0, -0.5]:
    worst = max(abs(Lam(n) - kappa * (Lam(n) / kappa)) for n in range(2, 2001))
    print(f"  kappa = {kappa}: cls = id, v(n) = Lambda(n)/kappa; max over 2 <= n <= 2000 of |fiber sum - kappa v(n)| = {worst:.1e}")
print("  kappa = 0: hA9 at n = 2 would give a nonnegative sum containing Lambda(2) = log 2 =", round(math.log(2), 6), "equal to 0 -- contradictory")

print("[N3] item 8: first prime violating log p / kappa <= (1+2g)(1+r_g)")
for kappa, gg in [(1.0, 0.0), (1.0, 1.0), (1.0, 2.0), (math.log(2), 1.0), (0.5, 5.0)]:
    rr = (1 + math.sqrt(1 + 8 * gg)) / 2
    B = (1 + 2 * gg) * (1 + rr)
    p = sp.nextprime(int(math.exp(kappa * B)))
    print(f"  kappa = {kappa:.6f}, g = {gg}: bound B = {B:.6f}, exp(kappa B) = {math.exp(kappa * B):.3f}, first violating prime {p}")

print("[N4] items 2, 3: N = 0 gives log 0 = 0 in Mathlib; N == 0 on all primes makes the span {0} (finite) -- item 2 needs hpos;")
print("     item 3 with some N i = 0: hsupp would put every prime in the finite S -- impossible, so hpos is implied there.")
