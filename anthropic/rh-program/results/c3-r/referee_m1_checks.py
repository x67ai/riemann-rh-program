#!/usr/bin/env python3
"""Referee numerical spot checks for results/c3-r/m1-noncircularity.md (C3-r M1).
All checks are self-contained integer/rational arithmetic (no floats except final sqrt bounds).
"""
import itertools, math

report = []
def check(name, ok, detail=""):
    report.append((name, ok, detail))
    print(("PASS" if ok else "FAIL"), "|", name, "|", detail)

# ---------------------------------------------------------------
# 1. GF(p^k) arithmetic via polynomial rings (for p=7, k=1,2,3)
# ---------------------------------------------------------------
def make_gf(p, poly):
    """GF(p^k) with k = len(poly)-1, poly = monic irreducible coeffs [c0,c1,...,1] over F_p."""
    k = len(poly) - 1
    red = [c % p for c in poly]
    def mul(a, b):
        prod = [0] * (2 * k - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    prod[i + j] = (prod[i + j] + ai * bj) % p
        # reduce
        for i in range(len(prod) - 1, k - 1, -1):
            c = prod[i]
            if c:
                prod[i] = 0
                for j in range(k):
                    prod[i - k + j] = (prod[i - k + j] - c * red[j]) % p
        return tuple(prod[:k])
    def add(a, b):
        return tuple((x + y) % p for x, y in zip(a, b))
    elts = [tuple(t) for t in itertools.product(range(p), repeat=k)]
    return elts, add, mul

def count_ell_points(p, poly):
    """#E(GF(p^k)) for E: y^2 = x^3 + x + 1, GF(p^k) built from poly; includes point at infinity."""
    elts, add, mul = make_gf(p, poly)
    k = len(poly) - 1
    one = tuple([1] + [0] * (k - 1))
    n = 0
    squares = {}
    for y in elts:
        squares.setdefault(mul(y, y), 0)
        squares[mul(y, y)] += 1
    for x in elts:
        rhs = add(add(mul(mul(x, x), x), x), one)
        n += squares.get(rhs, 0)
    return n + 1  # point at infinity

# irreducible polys over F_7: x^2+1 (since -1 is a QNR mod 7: squares mod 7 = {0,1,2,4}); x^3 - 2 ?
# check x^2+1 irreducible: -1 not a square mod 7 -> yes.
# for GF(343): need cubic irreducible over F_7: x^3 + 2 ? cubes mod 7: {0,1,6} -> -2 = 5 not a cube -> x^3+2 irred.
N1 = count_ell_points(7, [0, 1])            # GF(7): trivial "extension" k=1, poly=x (dummy) -> handle separately
# simpler direct count over F_7:
N1 = 1 + sum(1 for x in range(7) for y in range(7) if (y * y - (x**3 + x + 1)) % 7 == 0)
N2 = count_ell_points(7, [1, 0, 1])         # GF(49) = F_7[x]/(x^2+1)
N3 = count_ell_points(7, [2, 0, 0, 1])      # GF(343) = F_7[x]/(x^3+2)
check("F7 curve counts N1,N2,N3 = 5,55,380 (note section 7 consistency note)",
      (N1, N2, N3) == (5, 55, 380), f"got {(N1, N2, N3)}")

# trace recursion cross-check: a = 8 - N1; N_k = q^k + 1 - (alpha^k + beta^k), s_k = a*s_{k-1} - q*s_{k-2}
a = 7 + 1 - N1
s = {1: a, 2: a * a - 2 * 7}
s[3] = a * s[2] - 7 * s[1]
check("trace recursion N2,N3 from a=3", (7**2 + 1 - s[2], 7**3 + 1 - s[3]) == (N2, N3),
      f"a={a}, predicted {(50 - s[2], 344 - s[3])}")

# Weil bound for g=1, k=1,2,3
ok = all(abs((7**k + 1) - N) <= 2 * 1 * math.sqrt(7**k) + 1e-9 for k, N in [(1, N1), (2, N2), (3, N3)])
check("Weil bound |N_k-(q^k+1)| <= 2g q^{k/2} (g=1, k=1,2,3)", ok,
      f"margins {[abs(7**k + 1 - N) - 2 * math.sqrt(7**k) for k, N in [(1, N1), (2, N2), (3, N3)]]}")

# smoothness of y^2 = x^3+x+1 over F_7: disc = -16(4a^3+27b^2), a=b=1
disc = (-16 * (4 + 27)) % 7
check("curve smooth over F_7 (disc != 0 mod 7)", disc != 0, f"disc mod 7 = {disc}")

# ---------------------------------------------------------------
# 2. Section 7 algebra: CS on D = r*Delta + s*Gamma  ==>  quadratic form
#    D^2 = r^2(2-2g) + 2 r s t + s^2 q (2-2g)  <=  2 (r+s)(r+s q)
#    <=> g r^2 - r s (t-1-q) + g q s^2 >= 0
#    symbolic expansion check with integer polynomials in (r,s,g,q,t)
# ---------------------------------------------------------------
# represent polynomials as dict {(er,es,eg,eq,et): coeff}
def pmul(A, B):
    C = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            C[k] = C.get(k, 0) + va * vb
    return {k: v for k, v in C.items() if v}
def padd(*Ps):
    C = {}
    for P in Ps:
        for k, v in P.items():
            C[k] = C.get(k, 0) + v
    return {k: v for k, v in C.items() if v}
def pscale(A, c):
    return {k: c * v for k, v in A.items() if c * v}
V = lambda i: {tuple(1 if j == i else 0 for j in range(5)): 1}  # r,s,g,q,t
r, s_, g, q, t = V(0), V(1), V(2), V(3), V(4)
const = lambda c: {(0, 0, 0, 0, 0): c}
two_minus_2g = padd(const(2), pscale(g, -2))
D2 = padd(pmul(pmul(r, r), two_minus_2g), pscale(pmul(pmul(r, s_), t), 2),
          pmul(pmul(pmul(s_, s_), q), two_minus_2g))
RHS = pscale(pmul(padd(r, s_), padd(r, pmul(s_, q))), 2)
diff = padd(RHS, pscale(D2, -1))  # RHS - D^2 >= 0 claimed
target = pscale(padd(pmul(pmul(r, r), g), pscale(pmul(pmul(r, s_), padd(t, const(-1), pscale(q, -1))), -1),
                     pmul(pmul(pmul(s_, s_), g), q)), 2)  # 2*(g r^2 - rs(t-1-q) + g q s^2)
check("symbolic identity: 2(r+s)(r+sq) - D^2 == 2[g r^2 - rs(t-1-q) + gq s^2]",
      diff == target, f"diff-target = {padd(diff, pscale(target, -1))}")

# discriminant logic: psd of binary form A r^2 + B rs + C s^2 (A,C >= 0) <=> B^2 <= 4AC
# instance check for the F_7 elliptic curve: g=1,q=7,t=N1=5 -> r^2 +3rs+7s^2 > 0
vals = [(rr, ss) for rr in range(-20, 21) for ss in range(-20, 21) if (rr, ss) != (0, 0)]
form_ok = all(rr * rr + 3 * rr * ss + 7 * ss * ss > 0 for rr, ss in vals)
check("F7 instance form r^2+3rs+7s^2 positive definite on grid", form_ok, "disc = 9-28 = -19 < 0")

# CS inequality instance on C x C for the F_7 curve: Delta^2 = Gamma^2 = 0 (g=1), Gamma.Delta = 5
# D = r Delta + s Gamma: D^2 = 10 rs; bidegree (r+s, r+7s); check D^2 <= 2(r+s)(r+7s) on grid
cs_ok = all(10 * rr * ss <= 2 * (rr + ss) * (rr + 7 * ss) for rr, ss in vals)
check("CS instance D^2 <= 2 d1 d2 on grid (F_7 elliptic, g=1)", cs_ok, "")

# ---------------------------------------------------------------
# 3. Genus-2 spot check: y^2 = x^5 + x + 3 over F_p, p in {7, 11, 13} (squarefree at all three, checked incl. quadratic extensions)
#    smooth hyperelliptic genus 2 (odd char, squarefree quintic), one point at infinity
# ---------------------------------------------------------------
def genus2_count(p):
    f = lambda x: (x**5 + x + 3) % p
    # squarefree check: gcd(f, f') over F_p via polynomial gcd
    def polymod(A, B):
        A = A[:]
        while len(A) >= len(B) and any(A):
            if A[-1] % p == 0:
                A.pop(); continue
            c = A[-1] * pow(B[-1], p - 2, p) % p
            for i in range(len(B)):
                A[len(A) - len(B) + i] = (A[len(A) - len(B) + i] - c * B[i]) % p
            A.pop()
        while A and A[-1] % p == 0:
            A.pop()
        return A
    F = [3, 1, 0, 0, 0, 1]  # 3 + x + x^5
    Fp = [1, 0, 0, 0, 5]    # f' = 5x^4 + 1
    Aq, Bq = F, Fp
    while Bq:
        Aq, Bq = Bq, polymod(Aq, Bq)
    squarefree = (len(Aq) == 1)
    sq = {}
    for y in range(p):
        sq[y * y % p] = sq.get(y * y % p, 0) + 1
    n = sum(sq.get(f(x), 0) for x in range(p))
    return n + 1, squarefree  # one point at infinity (odd-degree model, smooth projective model has 1)

for p in (7, 11, 13):
    Np, sf = genus2_count(p)
    bound = 2 * 2 * math.sqrt(p)
    check(f"genus-2 y^2=x^5+x+3 over F_{p}: smooth model & Weil bound",
          sf and abs(Np - (p + 1)) <= bound + 1e-9,
          f"N1={Np}, |N1-(p+1)|={abs(Np - p - 1)}, 4*sqrt(p)={bound:.3f}")

# ---------------------------------------------------------------
# 4. Signature corollary spot checks (Gram matrices)
# ---------------------------------------------------------------
def eig_signature(M):
    # symmetric integer matrices, small: use numpy if available else characteristic poly roots
    try:
        import numpy as np
        w = np.linalg.eigvalsh(np.array(M, dtype=float))
        pos = sum(1 for x in w if x > 1e-9); neg = sum(1 for x in w if x < -1e-9)
        return pos, neg, [round(float(x), 6) for x in w]
    except ImportError:
        return None
res = eig_signature([[0, 1], [1, 0]])
check("Num(C x C') fiber-basis Gram [[0,1],[1,0]] has signature (1,1)", res[:2] == (1, 1), f"eigs {res[2]}")
res = eig_signature([[0, 1, 1], [1, 0, 1], [1, 1, 0]])
check("E x E (End=Z) Gram in basis xi1,xi2,Delta has signature (1,2)", res[:2] == (1, 2), f"eigs {res[2]}")

# ---------------------------------------------------------------
# 5. Case-2 perturbation algebra (Theorem 4): E' = (H^2)E - (E.H)H  =>  E'.H = 0, D.E' = (H^2)(D.E)
#    verified as generic bilinear identities on random integer "intersection tables"
# ---------------------------------------------------------------
import random
random.seed(42)
ok = True
for _ in range(200):
    n = 4
    # random symmetric integer matrix as intersection form on a rank-4 lattice
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            M[i][j] = M[j][i] = random.randint(-5, 5)
    dot = lambda u, v: sum(u[i] * M[i][j] * v[j] for i in range(n) for j in range(n))
    H = [random.randint(-3, 3) for _ in range(n)]
    E = [random.randint(-3, 3) for _ in range(n)]
    D = [random.randint(-3, 3) for _ in range(n)]
    H2 = dot(H, H); EH = dot(E, H); DH = dot(D, H)
    Ep = [H2 * E[i] - EH * H[i] for i in range(n)]
    if dot(Ep, H) != 0:
        ok = False; break
    if dot(D, Ep) != H2 * dot(D, E) - EH * DH:
        ok = False; break
check("Case-2 identities E'.H=0 and D.E' = (H^2)(D.E)-(E.H)(D.H) (200 random lattices)", ok, "")

print()
fails = [r for r in report if not r[1]]
print(f"TOTAL {len(report)} checks, {len(fails)} failures")
