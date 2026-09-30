"""Seed M2: the numerical line of each proof, for V = (q, t) = (5, 5) and the control E0 = (5, 4).
Exact integers / sympy where the verdict depends on it. Each block prints the inequality a proof derives,
the value on V (first violation, with its place) and on E0 (must pass)."""
import math, itertools
import numpy as np
from sympy import Matrix, sqrt, Rational, nsimplify, symbols, expand, I, Abs, N as Nnum

q = 5
CASES = {"V (t=5)": 5, "E0 (t=4)": 4}
def tr(t, n):  # alpha^n + beta^n
    s = [2, t]
    for k in range(2, n + 1): s.append(t * s[-1] - q * s[-2])
    return s[n]
def Nn(t, n): return q**n + 1 - tr(t, n)

print("== L1 Hasse (Sutherland L8 Thm 8.3): deg(r*pi - s) = r^2 q - r s t + s^2 >= 0 ==")
for name, t in CASES.items():
    vals = {(r, s): r * r * q - r * s * t + s * s for r in range(-6, 7) for s in range(-6, 7) if (r, s) != (0, 0)}
    mn = min(vals.values()); wit = sorted([k for k, v in vals.items() if v == mn], key=lambda k: abs(k[0]) + abs(k[1]))[:4]
    print("%s: min over 0<|r|,|s|<=6 = %d at %s ; deg(pi-1) = %d = N_1 ; disc t^2-4q = %d" % (name, mn, wit, q - t + 1, t * t - 4 * q))
print("V: pi - 2 has formal degree (alpha-2)(beta-2) =", (5 - 2 * 5 + 4), "; alpha - 2 = (1+sqrt5)/2 = golden ratio, a unit of norm -1")
print("V: deg(1 - pi^n) = N_n >= 1 for all n (zeta-level degrees positive):", [Nn(5, n) for n in range(1, 7)])

print("\n== L2 Castelnuovo-Severi / Hodge index on C x C (Milne pp. 9-10, Thm 1.5, Cor 1.6, Ex 1.7) ==")
def gram(t, nmax=1, g=1):
    # basis: C1 (= C x pt), C2 (= pt x C), Gamma_{pi^0} = Delta, ..., Gamma_{pi^nmax}
    # d1(Gamma_f) = D.C1 = deg f, d2 = D.C2 = 1 (Milne Ex 1.7); Gamma_{pi^i}.Gamma_{pi^j} = q^i N_{j-i} (i<j),
    # Gamma_{pi^i}^2 = q^i (2 - 2g) (Milne Ex 1.7 with def = 2 g deg f)
    B = ["C1", "C2"] + ["G%d" % i for i in range(nmax + 1)]
    M = [[0] * len(B) for _ in B]
    M[0][1] = M[1][0] = 1
    for i in range(nmax + 1):
        a = 2 + i
        M[a][0] = M[0][a] = q**i; M[a][1] = M[1][a] = 1
        M[a][a] = q**i * (2 - 2 * g)
        for j in range(i + 1, nmax + 1):
            M[a][2 + j] = M[2 + j][a] = q**i * Nn(t, j - i)
    return B, Matrix(M)
for name, t in CASES.items():
    for nmax in (1, 3):
        B, G = gram(t, nmax)
        ev = np.linalg.eigvalsh(np.array(G.tolist(), dtype=float))
        pos = sum(1 for e in ev if e > 1e-9); neg = sum(1 for e in ev if e < -1e-9)
        print("%s basis %s: rank %d, (+,-) = (%d,%d)  [Hodge index requires exactly one +]" % (name, B, G.rank(), pos, neg))
    # def(m Delta + n Gamma_pi) = 2 d1 d2 - D^2 ; Thm 1.5 says >= 0
    def defect(m, n):
        d1 = m + n * q; d2 = m + n; D2 = m * m * 0 + 2 * m * n * Nn(t, 1) + n * n * 0
        return 2 * d1 * d2 - D2
    bad = [(m, n, defect(m, n)) for m in range(-4, 5) for n in range(-2, 3) if defect(m, n) < 0]
    print("   def(m*Delta + n*Gamma_pi) < 0 at:", bad[:4], "(none)" if not bad else "")
    lhs = abs(Nn(t, 1) - q - 1); rhs = 2 * math.sqrt(q)
    print("   Cor 1.6 at (Delta, Gamma_pi): |N_1 - q - 1| = %d <= 2g sqrt(q) = %.4f ? %s" % (lhs, rhs, lhs <= rhs))
for n in range(1, 7):
    a = tr(5, n); a0 = tr(4, n)
    print("  extension degree n=%d: V a_n=%d, 2 q^(n/2)=%.2f -> CS on span(Delta, Gamma_pi^n) %s ; E0 a_n=%d %s" % (
        n, a, 2 * q**(n / 2), "VIOLATED" if a * a > 4 * q**n else "ok", a0, "VIOLATED" if a0 * a0 > 4 * q**n else "ok"))

print("\n== L3 Rosati (Milne Thm 1.27, Cor 1.29, Thm 1.30): Tr(x x^dagger) > 0 on Q[pi], pi^dagger = q/pi ==")
x5 = symbols('x')
for name, t in CASES.items():
    disc = t * t - 4 * q
    al = (t + sqrt(disc)) / 2; be = (t - sqrt(disc)) / 2
    # on the 2-dim formal V_l, pi = diag(al, be), pi^dagger = q/pi = diag(be, al); x = m + n pi
    def trace_form(m, n): return expand((m + n * al) * (m + n * q / al) + (m + n * be) * (m + n * q / be))
    vals = {(m, n): nsimplify(trace_form(m, n)) for m in range(-4, 5) for n in range(-2, 3) if (m, n) != (0, 0)}
    mn = min(vals.values())
    print("%s: Q[pi] = Q(sqrt(%d)) (%s); Tr(x x^dag) at x = pi - 2: %s ; min over box = %s" % (
        name, disc, "real quadratic" if disc > 0 else "imaginary quadratic", vals[(-2, 1)], mn))
    print("   Cor 1.29 test rho(pi^dag) = conj(rho(pi)) for rho(pi)=alpha: q/alpha = %s, conj(alpha) = %s, equal: %s" % (
        Nnum(q / al, 8), Nnum(al.conjugate(), 8), bool(abs(Nnum(q / al - al.conjugate())) < 1e-12)))
print("   Thm 1.30 input e(pi x, pi y) = q e(x,y): on a 2-dim space e is unique up to scalar and scales by det(pi) = q = 5 for BOTH (V supplies it).")

print("\n== L4 Stepanov-Bombieri (Bourbaki 430, Thm 1 (5), (7); Sec. III (8)-(10)) ==")
def bomb7(Q, p=5, g=1):
    # (7): nu_1 <= l + m Q/p^mu + 1 with mu = alpha/2 (Q = p^alpha), m = p^mu + 2g, l = [g p^mu/(g+1)] + g + 1
    al_exp = round(math.log(Q, p)); assert p**al_exp == Q and al_exp % 2 == 0
    mu = al_exp // 2; pm = p**mu; m = pm + 2 * g; l = (g * pm) // (g + 1) + g + 1
    cond = (l * pm < Q) and (l + 1 - g) * (m + 1 - g) > l * pm + m + 1 - g
    return l + m * Q // pm + 1, cond, Q + (2 * g + 1) * math.isqrt(Q) + 1
for r in (2, 4, 6):
    Q = q**r; b7, ok, b5 = bomb7(Q)
    for name, t in CASES.items():
        Nr = Nn(t, r); tw = 2 * (Q + 1) - Nr   # g = 1: x-coordinate double cover; (9): N + N^tw = 2(Q+1)
        print("r=%d Q=%d [(7) hyp ok: %s] bound(7)=%d bound(5)=%d | %s: N=%d %s ; twist N^tw=2(Q+1)-N=%d %s ; lower bound 2(Q+1)-bound(7)=%d %s" % (
            r, Q, ok, b7, b5, name, Nr, "ok" if Nr <= b7 else "VIOLATES", tw, "ok" if tw <= b7 else "VIOLATES (8)",
            2 * (Q + 1) - b7, "ok" if Nr >= 2 * (Q + 1) - b7 else "VIOLATED"))
print("Bombieri p.239 example: omega1=q, omega2=1 -> nu_r = q^r - q^r - 1 + 1 = 0 for all r; zeta = 1, class number L(1) = (1-q)(1-1) = 0.")
print("V is sharper: nu_r = N_r >= 1, b_d >= 1, class number 1 (baseline.log).")

print("\n== L4b control: E0 and its quadratic twist over F_25 by brute force (F_25 = F_5[X]/(X^2+X+2)?) ==")
p = 5
def f25_elems(): return [(a, b) for a in range(p) for b in range(p)]
# find an irreducible monic X^2 + c1 X + c0 over F_5
irr = next((c1, c0) for c1 in range(p) for c0 in range(p) if all((x * x + c1 * x + c0) % p for x in range(p)))
def mul(u, v):  # (u0 + u1 X)(v0 + v1 X), X^2 = -c1 X - c0
    c1, c0 = irr; a0 = u[0] * v[0]; a1 = u[0] * v[1] + u[1] * v[0]; a2 = u[1] * v[1]
    return ((a0 - a2 * c0) % p, (a1 - a2 * c1) % p)
def add(u, v): return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)
def pw(u, e):
    r = (1, 0)
    while e:
        if e & 1: r = mul(r, u)
        u = mul(u, u); e >>= 1
    return r
def count_y2_x3_ax(a):  # y^2 = x^3 + a x over F_25, projective
    tot = 1
    for x in f25_elems():
        fx = add(mul(mul(x, x), x), mul(a, x))
        if fx == (0, 0): tot += 1
        elif pw(fx, 12) == (1, 0): tot += 2
    return tot
nonsq = next(d for d in f25_elems() if d != (0, 0) and pw(d, 12) != (1, 0))
a_tw = mul((2, 0), mul(nonsq, nonsq))
n_e0, n_tw = count_y2_x3_ax((2, 0)), count_y2_x3_ax(a_tw)
print("irreducible X^2 + %d X + %d ; #E0(F_25) = %d (pred 20) ; #E0^tw(F_25) = %d (pred 2*26-20 = 32) ; sum = %d = 2(Q+1) = 52" % (irr[0], irr[1], n_e0, n_tw, n_e0 + n_tw))

print("\n== L5 Deligne Weil I: (7.1) on X = C^k (k even, dim k): q^((k-1)/2) <= |alpha^k| <= q^((k+1)/2); (3.2) Rankin: |alpha|^(2k) <= q^(k*w+1) ==")
for name, t in CASES.items():
    disc = t * t - 4 * q
    roots = [abs(complex(t / 2, math.sqrt(-disc) / 2))] * 2 if disc < 0 else [(t + math.sqrt(disc)) / 2, (t - math.sqrt(disc)) / 2]
    for k in (2, 4, 6):
        lo, hi = q**((k - 1) / 2), q**((k + 1) / 2)
        st = ["%.3f %s" % (r**k, "ok" if lo - 1e-9 <= r**k <= hi + 1e-9 else "VIOLATED") for r in roots]
        print("%s  C^%d: bounds [%.3f, %.3f] ; |alpha|^k, |beta|^k = %s" % (name, k, lo, hi, st))
    for k in (1, 2, 3):
        st = ["%.2f<=%d %s" % (r**(2 * k), q**(k + 1), "ok" if r**(2 * k) <= q**(k + 1) + 1e-9 else "VIOLATED") for r in roots[:1]]
        print("%s  Rankin 2k=%d (weight w=1): %s" % (name, 2 * k, st))

print("\n== L6 Laumon (Thm 4.1.3): H^1 of a curve is pure of weight 1; formal weights 2 log|alpha|/log q ==")
for name, t in CASES.items():
    disc = t * t - 4 * q
    roots = [math.sqrt(q)] * 2 if disc < 0 else [(t + math.sqrt(disc)) / 2, (t - math.sqrt(disc)) / 2]
    print("%s: weights %s" % (name, [round(2 * math.log(r) / math.log(q), 5) for r in roots]))

print("\n== L7 special curves: Gauss sums over F_5 (|g|^2 = q) and Jacobi sums (norm q, in Z[i]) ==")
import cmath
gen = 2  # generator of F_5^*
dlog = {pow(gen, k, p): k for k in range(4)}
def chi(j, x): return 0 if x % p == 0 else cmath.exp(2j * math.pi * j * dlog[x % p] / 4)
psi = lambda x: cmath.exp(2j * math.pi * x / p)
for j in (1, 2, 3):
    g = sum(chi(j, x) * psi(x) for x in range(1, p))
    print("character of order %d: |g|^2 = %.12f" % (4 // math.gcd(j, 4), abs(g)**2))
Js = sorted({(round(J.real), round(J.imag)) for a in (1, 2, 3) for b in (1, 2, 3) if (a + b) % 4
             for J in [sum(chi(a, x) * chi(b, 1 - x) for x in range(p))]})
print("Jacobi sums J(chi^a, chi^b), a+b != 0 mod 4:", Js, "; norms:", sorted({x * x + y * y for x, y in Js}))
print("E0 Frobenius 2+i: among units*Jacobi sums: %s ; V alpha = (5+sqrt5)/2 real, alpha^2 = %.4f != 5" % (
    any((2 + 1j) == u * complex(*J) for J in Js for u in (1, -1, 1j, -1j)), ((5 + math.sqrt(5)) / 2)**2))

print("\n== L8 Hrushovski Example 11.4 (S = Delta): |e| <= (2g(2 deg deg^t - S.S^t))^(1/2) q^(1/2) = 2g sqrt(q) ==")
for name, t in CASES.items():
    e = Nn(t, 1) - q - 1; bnd = math.sqrt(2 * 1 * (2 * 1 * 1 - 0)) * math.sqrt(q)
    print("%s: e = %d, bound = %.4f -> %s" % (name, e, bnd, "ok" if abs(e) <= bnd else "VIOLATED"))
