#!/usr/bin/env python3
"""o3 -- OPUS READER, seed M1a beurling-fe.  POSITIVITY IS NECESSARY in Theorem T / T3: an explicit SIGNED solution.

chi = Legendre symbol mod 5 (even, real, primitive, tau(chi) = +sqrt5, root number +1).  Put a = sqrt5 and
  mu_s := sum_{n in Z} chi(n) delta_{n/a}  -  ( a delta_{aZ} + delta_{Z/a} )  +  ( a delta_{(a/2)Z} + 2 delta_{(2/a)Z} ).
Each bracket is self-dual (FT delta_{cZ} = c^{-1} delta_{Z/c}; twisted Poisson with tau(chi) = sqrt5), so mu_s^ = mu_s.
Atoms in (0,1): at 1/a: chi(1) - 1 = 0; at 2/a: chi(2) - 1 + 2 = 0.  Mass at 0: -(a+1) + (a+2) = 1.  So mu_s = delta_0 + nu,
supp nu in {|x| >= 1}: the hypotheses of T minus positivity.  Dirichlet series (frequencies >= 1, real coefficients):
  F(s) = 5^{s/2} L(s,chi) + D(s) zeta(s),  D(s) = -5^{s/2} - 5^{(1-s)/2} + a (a/2)^{-s} + 2 (a/2)^{s},  D(s) = D(1-s).
Checks: (a) atoms of mu_s in (0, 2]; (b) theta relation Theta(1/x) = sqrt(x) Theta(x) at 40 digits; (c) Fejer identity
sum_{t>0} m(t) S(t) = 0 (closed forms, and direct summation); (d) the FE of xi_F at two points; (e) Res_{s=1} F.
"""
import mpmath as mp
mp.mp.dps = 40
a = mp.sqrt(5)
chi = lambda n: [0, 1, -1, -1, 1][n % 5]

# (a) atoms, positive side, up to X
X = 60
atoms = {}
def add(t, w):
    key = mp.nstr(t, 25); atoms[key] = (t, atoms.get(key, (t, 0))[1] + w)
for n in range(1, int(X * a) + 1): add(n / a, chi(n))                  # chi part
for n in range(1, int(X / a) + 1): add(n * a, -a)                      # -a delta_{aZ}
for n in range(1, int(X * a) + 1): add(n / a, -1)                      # -delta_{Z/a}
for n in range(1, int(2 * X / a) + 1): add(n * a / 2, a)               # +a delta_{(a/2)Z}
for n in range(1, int(X * a / 2) + 1): add(2 * n / a, 2)               # +2 delta_{(2/a)Z}
pos = sorted((t, w) for t, w in atoms.values() if abs(w) > mp.mpf(10) ** -30)
print("(a) atoms of mu_s in (0,2] (position: mass):", ", ".join(f"{mp.nstr(t,6)}: {mp.nstr(w,6)}" for t, w in pos if t <= 2))
print("    smallest positive atom:", mp.nstr(pos[0][0], 10), "  cancelled atoms at 1/sqrt5, 2/sqrt5:",
      [mp.nstr(atoms[mp.nstr(k / a, 25)][1], 3) for k in (1, 2)])

# (b) theta relation.  th(c, y) := sum_{n in Z} exp(-pi n^2 c^2 y) = jtheta3(0, e^{-pi c^2 y})
th = lambda c, y: mp.jtheta(3, 0, mp.exp(-mp.pi * c * c * y))
thchi = lambda y: mp.fsum(chi(n) * mp.exp(-mp.pi * n * n * y / 5) for n in range(-400, 401))
Theta = lambda y: thchi(y) - a * th(a, y) - th(1 / a, y) + a * th(a / 2, y) + 2 * th(2 / a, y)
worst = max(abs(Theta(1 / x) - mp.sqrt(x) * Theta(x)) for x in [mp.mpf(2) ** k for k in range(-4, 5) if k])
print("(b) max |Theta(1/x) - sqrt(x) Theta(x)| over x = 2^-4..2^4:", mp.nstr(worst, 5), "  Theta(1) =", mp.nstr(Theta(1), 12))

# (c) Fejer identity.  T(c) = sum_{n>=1} S(c n) in closed form (o1); chi part: sum_{n>=1} chi(n) S(n/a) = (1/2)<mu_chi, phi> = 1/a
def T(c):
    c = mp.mpf(c); K = int(mp.ceil(c)) - 1
    return ((1 + 2 * (K - mp.mpf(K) * (K + 1) / (2 * c))) / c - 1) / 2
closed = 1 / a - (a * T(a) + T(1 / a)) + (a * T(a / 2) + 2 * T(2 / a))
S = lambda t: (mp.sin(mp.pi * t) / (mp.pi * t)) ** 2
direct = mp.fsum(w * S(t) for t, w in pos)
print("(c) sum_{t>0} m(t) S(t): closed form =", mp.nstr(closed, 6), "  direct over atoms t <= 60 =", mp.nstr(direct, 6),
      "(tail O(1/60))   => <mu,phi> = <mu,phi^> = 1 + 2*0 = rho = 1 with NON-integral atoms")

# (d) FE of xi_F and (e) residue
L5 = lambda s: mp.dirichlet(s, [0, 1, -1, -1, 1])
Dfun = lambda s: -mp.power(5, s / 2) - mp.power(5, (1 - s) / 2) + a * mp.power(a / 2, -s) + 2 * mp.power(a / 2, s)
F = lambda s: mp.power(5, s / 2) * L5(s) + Dfun(s) * mp.zeta(s)
xi = lambda s: mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * F(s)
for s in (mp.mpc(0.3, 7), mp.mpc(2.5, -3)):
    print(f"(d) s = {mp.nstr(s,3)}: |xi_F(s) - xi_F(1-s)| = {mp.nstr(abs(xi(s) - xi(1 - s)), 5)}   |xi_F(s)| = {mp.nstr(abs(xi(s)), 6)}")
print("(e) Res_{s=1} F = D(1) =", mp.nstr(Dfun(1), 12), "  (rho = 1); F(3) from the atoms t <= 60:",
      mp.nstr(mp.fsum(w * t ** -3 for t, w in pos), 8), " closed form F(3) =", mp.nstr(F(3), 8))
