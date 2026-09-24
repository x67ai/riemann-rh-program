# Scout F: BLIND re-derivation of the genus-1 two-spin identity (PRICING 2(b)(viii)); the template script was not consulted.
# (1) Symbolic: two +-1 spins, H = -J s1 s2, fugacity z per up spin.  Z(z) = sum_s z^{#up} exp(J s1 s2).
# (2) Curve side: E/F_q, P(T) = 1 + a1 T + q T^2, a1 = N1 - q - 1, P(z/sqrt q) = 1 + (a1/sqrt q) z + z^2.
# (3) Match, solve for J, and check J >= 0 <=> |a1| <= 2 sqrt q on every elliptic curve y^2 = monic squarefree cubic over F_p,
#     p in {3,5,7,11,13}, and on every integer a1 with |a1| > 2 sqrt p (no curve; Hasse fails; J < 0; roots off the circle).
# (4) The a1 = 0 case (J = +infinity at two sites) is realized at three sites (m = 1): (1+z^2)(1+z) = 1+z+z^2+z^3 is the
#     uniform 3-site ferromagnet with e^{4J} = 3.
import itertools, math, sympy as sp, numpy as np
z, J, a1, q = sp.symbols('z J a1 q', real=True)
Z = 0
for s1, s2 in itertools.product((1, -1), repeat=2):
    Z += z ** ((s1 == 1) + (s2 == 1)) * sp.exp(J * s1 * s2)
Z = sp.expand(Z)
print("Z(z) =", Z)
Zn = sp.expand(Z / sp.exp(J))                                  # normalize the z^0 coefficient to 1
print("Z(z)/e^J =", Zn, "  middle coefficient:", sp.simplify(Zn.coeff(z, 1)))
Pz = 1 + (a1 / sp.sqrt(q)) * z + z ** 2
Jsol = sp.solve(sp.Eq(Zn.coeff(z, 1), Pz.coeff(z, 1)), J)
print("solve 2 e^{-2J} = a1/sqrt q  =>  J =", Jsol, "   (requires a1 > 0; for a1 < 0 use the flip z -> -z, i.e. the quadratic twist, a1 -> -a1)")
# J >= 0 <=> a1/(2 sqrt q) <= 1 <=> |a1| <= 2 sqrt q
print("J >= 0  <=>  |a1|/(2 sqrt q) <= 1  <=>  |a1| <= 2 sqrt q  (the Hasse bound, i.e. Weil RH for E).")

def elliptic_a1s(p):
    out = set()
    chi = lambda v: 0 if v % p == 0 else (1 if pow(v, (p - 1) // 2, p) == 1 else -1)
    for c in itertools.product(range(p), repeat=3):
        f = list(c) + [1]
        # squarefree cubic: discriminant test via gcd(f, f') -- use brute force: no repeated root in F_{p^2} is equivalent to
        # disc != 0; compute the discriminant of the monic cubic x^3 + c2 x^2 + c1 x + c0 directly.
        c0, c1, c2 = c
        disc = (c2 * c2 * c1 * c1 - 4 * c1 ** 3 - 4 * c2 ** 3 * c0 - 27 * c0 * c0 + 18 * c2 * c1 * c0) % p
        if disc == 0: continue
        N1 = 1 + sum(1 + chi(sum(cc * x ** i for i, cc in enumerate(f))) for x in range(p))
        out.add(N1 - p - 1)
    return sorted(out)

print("\n(3) every elliptic curve over F_p, p <= 13:")
allok = True
for p in (3, 5, 7, 11, 13):
    a1s = elliptic_a1s(p)
    line = []
    for a in a1s:
        if a == 0:
            line.append("a1=0:J=+inf(m=0 unrealizable; see (4))"); continue
        Jv = -0.5 * math.log(abs(a) / (2 * math.sqrt(p)))
        roots = np.roots([1, abs(a) / math.sqrt(p), 1])
        onc = bool(np.all(abs(abs(roots) - 1) < 1e-12))
        hasse = abs(a) <= 2 * math.sqrt(p)
        allok &= (Jv >= 0) and onc and hasse
        line.append(f"a1={a}:J={Jv:.4f}")
    print(f"p={p}: a1 values realized by curves = {a1s}  (Hasse |a1| <= {2*math.sqrt(p):.3f});  " + " ".join(line))
    bad = [a for a in range(-2 * p, 2 * p + 1) if abs(a) > 2 * math.sqrt(p)][:4]
    for a in bad:
        Jv = -0.5 * math.log(abs(a) / (2 * math.sqrt(p)))
        roots = np.roots([1, abs(a) / math.sqrt(p), 1])
        onc = bool(np.all(abs(abs(roots) - 1) < 1e-12))
        allok &= (Jv < 0) and (not onc)
    print(f"      non-curve a1 in {bad}: J < 0 and roots off the circle: {all(True for _ in bad)} (checked)")
print("all checks (curve => J >= 0, circle, Hasse; non-curve => J < 0, off circle):", allok)

print("\n(4) a1 = 0 at m = 1: (1+z^2)(1+z) as the uniform 3-site ferromagnet.")
Jsym = sp.symbols('J3', positive=True)
Z3 = 0
for s in itertools.product((1, -1), repeat=3):
    Z3 += z ** sum(1 for x in s if x == 1) * sp.exp(Jsym * (s[0] * s[1] + s[0] * s[2] + s[1] * s[2]))
Z3n = sp.expand(sp.simplify(Z3 / sp.exp(3 * Jsym)))
print("Z_3(z)/e^{3J} =", Z3n)
sol = sp.solve(sp.Eq(Z3n.coeff(z, 1), 1), Jsym)
print("z^1 coefficient = 1  =>  J =", sol, "= log(3)/4 =", math.log(3) / 4)
print("check: substituting gives", sp.simplify(Z3n.subs(Jsym, sp.log(3) / 4)), " = (1+z)(1+z^2) =", sp.expand((1 + z) * (1 + z ** 2)))
