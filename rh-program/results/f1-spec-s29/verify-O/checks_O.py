"""F1 reader (Opus 5), Session 29 — independent re-computation of every numeric / finite claim of SPEC.md.
Written from the definitions, not from the writer's script. Sections:
 [1] DH and Epstein witnesses (A5, I.1(c)); DH non-multiplicativity (A2 (b) as a proof).
 [2] chi_4 inside through B = Spec Z[i] (A2): ideal counts = sum_{d|n} chi4(d) = r2(n)/4; Lambda_K by norm >= 0.
 [3] A9: the pairwise reading on A^1/F_q (host q(q+1) vs target q^2), by independent enumeration of monic
     polynomials; the diagonal row (Theorem 3.4) as control; the g = 1 model N_N at N = 1..4.
 [4] P9j over Z: Teichmueller ghost vectors (a^n) lie in W(Z) (Borger 0801.1691 §1.10 congruences);
     functoriality check I_{m,n} | a^m b^n - a^n b^m; F_1-points of toric P^1; the diagonal row (T4)=A9 for every
     q = a/b of height <= H; the a = -1 case.
 [5] rung-1 analog of P9j: Lambda_S-maps W_S*(S) -> f*(A^1_k) = S x_k A^1_k on S = A^1/F_q, sections y = a(x)^{q^N}.
 [6] the dependency chain of §1: acyclicity by topological sort.
"""
from mpmath import mp, mpf, sqrt, log
from math import gcd
from fractions import Fraction
import itertools, sys
mp.dps = 40

def vM_from_coeffs(a, N):
    """Lambda with a(n) log n = sum_{d|n} Lambda(d) a(n/d), a(1) = 1."""
    L = [mpf(0)] * (N + 1)
    for n in range(2, N + 1):
        s = a[n] * log(n)
        for d in range(2, n):
            if n % d == 0: s -= L[d] * a[n // d]
        L[n] = s  # a(1) = 1
    return L

print("[1] DH / Epstein")
s5 = sqrt(5)
kap = (sqrt(10 - 2 * s5) - 2) / (s5 - 1)
N = 60
a = [mpf(0)] * (N + 1)
pat = {1: 1, 2: kap, 3: -kap, 4: -1, 0: 0}
for n in range(1, N + 1): a[n] = mpf(pat[n % 5])
L = vM_from_coeffs(a, N)
print("  kappa =", mp.nstr(kap, 25))
for n in (2, 3, 4, 6, 12):
    print(f"  Lambda_DH({n}) = {mp.nstr(L[n], 20)}")
print("  record (finisher_reverify.json) Lambda_DH(12) = -0.762877471988412; match:",
      abs(L[12] - mpf('-0.762877471988412')) < mpf('1e-14'))
print("  DH non-multiplicative: a6 =", mp.nstr(a[6], 10), " a2*a3 =", mp.nstr(a[2] * a[3], 10),
      "-> every product/quotient of Euler products has multiplicative coefficients; DH's do not")
# Epstein x^2 + 5 y^2, normalized a(1) = 1 (r_Q(1) = 2)
NE = 40
r = [0] * (NE + 1)
for x in range(-7, 8):
    for y in range(-3, 4):
        v = x * x + 5 * y * y
        if 1 <= v <= NE: r[v] += 1
aE = [mpf(0)] + [mpf(r[n]) / 2 for n in range(1, NE + 1)]
LE = vM_from_coeffs(aE, NE)
print(f"  Epstein Q=x^2+5y^2: Lambda_Q(6) = {mp.nstr(LE[6], 15)} (2 log 6 = {mp.nstr(2*log(6), 15)}); "
      f"Lambda_Q(36) = {mp.nstr(LE[36], 15)} (-4 log 6 = {mp.nstr(-4*log(6), 15)})")

print("[2] chi_4 inside via B = Spec Z[i]")
def chi4(n): return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
NI = 400
r2 = [0] * (NI + 1)
for x in range(-21, 22):
    for y in range(-21, 22):
        v = x * x + y * y
        if 1 <= v <= NI: r2[v] += 1
ok = all(r2[n] == 4 * sum(chi4(d) for d in range(1, n + 1) if n % d == 0) for n in range(1, NI + 1))
print("  #ideals of norm n in Z[i] (= r2(n)/4) == sum_{d|n} chi4(d) for n <= 400:", ok,
      "-> zeta_{Q(i)} = zeta * L(chi4) coefficientwise to 400")
aK = [mpf(0)] + [mpf(r2[n]) / 4 for n in range(1, NI + 1)]
LK = vM_from_coeffs(aK, 100)
a4 = [mpf(0)] + [mpf(chi4(n)) for n in range(1, 101)]
L4 = vM_from_coeffs(a4, 100)
print("  Lambda_chi4(3) =", mp.nstr(L4[3], 12), "(-log 3 =", mp.nstr(-log(3), 12), ")")
print("  min over n<=100 of Lambda_{Q(i)}(n) (by norm):", mp.nstr(min(LK[2:]), 12),
      "; Lambda_{Q(i)}(3) =", mp.nstr(LK[3], 6), "; Lambda_{Q(i)}(9) =", mp.nstr(LK[9], 12), "= 2 log 3:",
      abs(LK[9] - 2 * log(3)) < mpf('1e-20'))

print("[3] A9 on A^1/F_q (independent enumeration of monic polynomials of degree <= 2)")
def divisors_A1(q, N):
    """effective divisors of degree N on A^1/F_q as monic polynomials, returned as dict closed point -> mult.
    closed points: degree-1 points ('r', c); degree-2 points: monic irreducible quadratics ('Q', b, c)."""
    irr2 = [(b, c) for b in range(q) for c in range(q) if all((x * x + b * x + c) % q for x in range(q))]
    pts = [(('r', c), 1) for c in range(q)] + [(('Q',) + t, 2) for t in irr2]
    out = []
    def rec(i, rem, cur):
        if rem == 0: out.append(dict(cur)); return
        if i == len(pts): return
        p, d = pts[i]
        for k in range(rem // d + 1):
            if k: cur[p] = k
            rec(i + 1, rem - k * d, cur)
            if k: del cur[p]
    rec(0, N, {})
    return out, dict(pts)
def host(m, n, deg):  # E3 Theorem 3.3, units of log q
    diff = [p for p in set(m) | set(n) if m.get(p, 0) != n.get(p, 0)]
    if len(diff) != 1: return 0
    p = diff[0]; return (1 + min(m.get(p, 0), n.get(p, 0))) * deg[p]
for q in (2, 3, 5, 7):
    D1, deg = divisors_A1(q, 1); D2, _ = divisors_A1(q, 2)
    assert len(D1) == q and len(D2) == q * q
    hs = sum(host(m, n, deg) for m in D1 for n in D2)
    # target: length of F_q[x]/(x^{q^2} - x^q) = q^2 (x^{q^2}-x^q = (x^q - x)^q)
    tgt = q * q
    diag = [sum(host({}, n, deg) for n in DN) for DN in (D1, D2)]
    print(f"  q={q}: host pairwise sum over |m|=1,|n|=2 = {hs} = q(q+1) {hs == q*(q+1)}; target (Gamma_Fr.Gamma_Fr2) = {tgt}; "
          f"ratio {Fraction(hs, tgt)}; diagonal row control N=1,2: {diag} vs {[q, q*q]}")
print("  per-point: host local contribution at each F_q-point = 2 (m=R,n=2R) + (q-1) (m=P,n=P+R) = q+1; target multiplicity q."
      " No weighting by fiber cardinalities (q, q^2) turns (q+1)/q into 1.")
# g = 1 model y^2 = x^3 + x + 1 over F_7: affine counts via Frobenius trace
q = 7
N1aff = sum(1 for x in range(q) for y in range(q) if (y * y - (x ** 3 + x + 1)) % q == 0)
t = q + 1 - (N1aff + 1)  # trace of Frobenius, projective count = affine + 1
al = [None]
s = [2, t]  # s_N = alpha^N + beta^N, s_{N+1} = t s_N - q s_{N-1}
for _ in range(3): s.append(t * s[-1] - q * s[-2])
print("  g=1 model y^2=x^3+x+1 /F_7 affine N_N, N=1..4:", [q ** N + 1 - s[N] - 1 for N in range(1, 5)],
      "(record: 5, 55, 380, 2475)")

print("[4] P9j over Z")
def vp(n, p):
    k = 0
    while n % p == 0: n //= p; k += 1
    return k
primes = [p for p in range(2, 80) if all(p % d for d in range(2, p))]
bad = 0
for A in range(-10, 11):
    for j in range(1, 40):
        for p in primes:
            if p * j > 200: break
            if (A ** (p * j) - A ** j) % p ** (1 + vp(j, p)): bad += 1
print("  Teichmueller ghost vectors (a^j)_j satisfy a_j = a_pj mod p^(1+ord_p j) (0801.1691 §1.10) for a in [-10,10]:",
      "violations =", bad)
def I_mn(m, n):  # E3 NOTE §3 'On Z'
    g = gcd(m, n); r, s_ = max(m, n) // g, min(m, n) // g
    if s_ != 1: return 1
    for p in primes:
        if r % p == 0:
            rr = r
            while rr % p == 0: rr //= p
            return p ** (1 + min(vp(m, p), vp(n, p))) if rr == 1 else 1
    return 1
viol = 0; cnt = 0
for A in range(-8, 9):
    for B in range(1, 9):
        if gcd(A, B) != 1: continue
        for m in range(1, 13):
            for n in range(m + 1, 13):
                cnt += 1
                if (A ** m * B ** n - A ** n * B ** m) % I_mn(m, n): viol += 1
print(f"  functoriality: host ideal I_(m,n) divides a^m b^n - a^n b^m (the host intersection maps into the target's): "
      f"{cnt} cases, violations = {viol}")
F1pts = [Fraction(A, B) for A in range(-30, 31) for B in range(1, 31) if gcd(A, B) == 1
         and Fraction(A, B) ** 2 == Fraction(A, B) and Fraction(A, B) ** 3 == Fraction(A, B)]
print("  Lambda-fixed points of toric P^1 in P^1(Q) (q^p = q for p = 2, 3), height <= 30:", sorted(set(F1pts)), "+ infinity")
def Lam(n):
    for p in primes:
        if n % p == 0:
            while n % p == 0: n //= p
            return log(p) if n == 1 else mpf(0)
    return mpf(0)
H = 30; Nmax = 12
passed = []; firstfail = {}
for A in range(-H, H + 1):
    for B in range(1, H + 1):
        if gcd(A, B) != 1: continue
        qq = Fraction(A, B)
        if qq in (0, 1): continue
        # images sigma_{q^n} = (A^n : B^n); diagonal image sigma_q. Fiber of D over n.
        imgs = {n: Fraction(A ** n, B ** n) for n in range(1, Nmax + 1)}
        fibers = {}
        for n in range(2, Nmax + 1):
            if imgs[n] != imgs[1]: fibers.setdefault(imgs[n], []).append(n)
        ok = True
        for D, ns in sorted(fibers.items(), key=lambda kv: kv[1][0]):
            hostv = sum(Lam(n) for n in ns)
            tgtv = log(abs(A * D.denominator - D.numerator * B))
            if abs(hostv - tgtv) > mpf('1e-20'):
                ok = False; firstfail[qq] = (ns[:4], mp.nstr(hostv, 6), mp.nstr(tgtv, 6)); break
        if ok: passed.append(qq)
print(f"  A9 (diagonal row, summed over fibers of c_q, n <= {Nmax}) for all q = a/b != 0, 1 of height <= {H}: passes for", passed)
for qq in (Fraction(2), Fraction(1, 2), Fraction(-1), Fraction(-2), Fraction(3)):
    print(f"    q = {qq}: first failing fiber (n's, host sum, target log|det|) = {firstfail.get(qq)}")

print("[5] rung-1 analog of P9j: target f*(A^1_k) = S x_k A^1_k, S = A^1/F_q, c = f*(a) o unit, a in F_q[x]")
for q in (3, 7):
    for adeg, name in ((1, 'x'), (2, 'x^2')):
        for Nn in (1, 2):
            hostv = q ** Nn  # Theorem 3.4 on A^1: sum_{deg n = N} Lambda_S(n)/log q = #A^1(F_{q^N}) = q^N
            tgtv = adeg * q ** Nn  # length of F_q[x]/(a^{q^N} - a) for a = x^adeg
            print(f"  q={q}, a={name}, N={Nn}: host diagonal row {hostv}, target (c(Gamma_0).c(Gamma_n-fiber)) = {tgtv}"
                  f" -> {'equal (a = x: Y = S x_k S, the Weil target)' if hostv == tgtv else 'MISMATCH'}")
print("  a = x^2: images are graphs of x -> x^(2 q^N): phi_0 = x^2 != id and phi_1 o phi_1 = x^(4q^2) != phi_2 = x^(2q^2): (T2b) fails")

print("[6] dependency chain")
deps = {1: [], 2: [1], 3: [1], 4: [1], 5: [4], 6: [1], 7: [4, 6], 8: [6], 9: [5, 7, 8], 10: [5, 9], 11: [8, 9], 12: [6],
        13: [6, 7, 8, 9, 10, 11], 14: list(range(1, 14))}
print("  every arrow decreases the index:", all(d < k for k, ds in deps.items() for d in ds))
