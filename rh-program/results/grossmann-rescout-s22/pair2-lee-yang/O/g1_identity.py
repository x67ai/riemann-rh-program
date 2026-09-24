#!/usr/bin/env python3
"""Scout O -- blind re-derivation of the g = 1 two-spin identity (PRICING 2(b)(viii)), symbolic.
Two +-1 spins, H = -J s1 s2, fugacity z per up spin: Z = sum over 4 states z^{#up} e^{J s1 s2}."""
import json, math, os, sympy as sp
HERE = os.path.dirname(os.path.abspath(__file__))
J, z, c = sp.symbols("J z c", real=True)
Z = sum(z ** ((s1 + 1) // 2 + (s2 + 1) // 2) * sp.exp(J * s1 * s2) for s1 in (-1, 1) for s2 in (-1, 1))
Zn = sp.expand(sp.simplify(Z / sp.exp(J)))
print("Z(z) =", sp.simplify(Z))
print("Z(z)/e^J =", Zn)
# match 1 + c z + z^2 (c = a1/sqrt q):  2 e^{-2J} = c
sol = sp.solve(sp.Eq(2 * sp.exp(-2 * J), c), J)
print("J solving 2e^{-2J} = c :", sol)
# roots of z^2 + 2x z + 1 on |z|=1 iff x^2 <= 1 (product of roots = 1; real distinct roots otherwise)
x = sp.symbols("x", real=True)
print("discriminant of z^2 + 2 x z + 1:", sp.discriminant(z ** 2 + 2 * x * z + 1, z), "(<= 0 iff |x| <= 1)")
print("x = e^{-2J} <= 1  iff  J >= 0; x in (0, 1] needs c = 2x in (0, 2]:  c <= 2  iff  |a1| <= 2 sqrt q")
cls = json.load(open(os.path.join(HERE, "classes_g1.json")))
rows = []
for r in cls:
    p, a1 = r["p"], r["a1"]
    if a1 == 0:
        rows.append((p, a1, "noflip needs c = 0: J = +inf (not finite); flip likewise"))
        continue
    s = 1 if a1 > 0 else -1           # orientation making the middle coefficient positive
    Jv = -0.5 * math.log(abs(a1) / (2 * math.sqrt(p)))
    rows.append((p, a1, "orientation %s  J = %.6f  J>=0: %s  Hasse: %s" % (
        "noflip" if s == 1 else "flip(z->-z)", Jv, Jv >= 0, a1 * a1 <= 4 * p)))
for t in rows:
    print("p=%d a1=%d: %s" % t)
ok = all(("J>=0: True" in t[2]) == True for t in rows if t[1] != 0)
print("all 60 enumerated g=1 classes with a1 != 0: J >= 0 (finite) ->", ok,
      "| classes with a1 = 0 (J = +inf):", sum(1 for t in rows if t[1] == 0))
for (p, a1) in [(13, 8), (5, 5)]:
    Jv = -0.5 * math.log(abs(a1) / (2 * math.sqrt(p)))
    print("CONTROL non-curve datum p=%d a1=%d (Hasse fails): J = %.6f < 0: %s" % (p, a1, Jv, Jv < 0))
