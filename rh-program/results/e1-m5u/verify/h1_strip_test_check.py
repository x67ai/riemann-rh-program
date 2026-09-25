#!/usr/bin/env python3
"""E1 section 2 clause 1 (H1 on the strip): numerical sanity check of the test family g = (psi * psi~) / cosh(u/2).
Claim [derivation]: for real even psi with compact support, the orbit sum over {+-x +- iy}, |y| <= 1/2, of ghat is
4 Re ghat(x+iy) = 4 Int g(u) cos(xu) cosh(yu) du >= 0, strictly > 0 for |y| < 1/2, because k = psi*psi~ is positive-definite and
cosh(yu)/cosh(u/2) is the characteristic function of a strictly positive density (Fourier transform of 1/cosh(u/2) is 2 pi / cosh(pi x)).
Check: sample Re ghat(x+iy) on a grid, and the transform of cosh(yu)/cosh(u/2). mpmath quadrature. Conventions: FORMULATION section 0.1."""
import mpmath as mp
mp.mp.dps = 20
psi = lambda u: (1 - u**2)**3 if abs(u) < 1 else mp.mpf(0)      # C^2 bump, supp [-1,1]
k = lambda u: mp.quad(lambda v: psi(v) * psi(v - u), [-1, 1]) if abs(u) < 2 else mp.mpf(0)   # psi * psi~ (psi even real), supp [-2,2]
def re_ghat(x, y):
    return mp.quad(lambda u: k(u) / mp.cosh(u / 2) * mp.cos(x * u) * mp.cosh(y * u), [-2, 0, 2])
print("Re ghat(x+iy) for g = (psi*psi~)/cosh(u/2), psi = (1-u^2)^3 on [-1,1]:")
mn = mp.mpf(10)
for y in [0, 0.25, 0.49, 0.5]:
    row = []
    for x in [0, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 15]:
        v = re_ghat(x, y); row.append(v); mn = min(mn, v)
    print(f"  y = {y:4}: " + " ".join(f"{float(v):+.3e}" for v in row))
print(f"minimum over the grid: {float(mn):+.3e}  (claim: >= 0 everywhere on |y| <= 1/2, > 0 for |y| < 1/2)")
# the comparison: plain psi*psi~ (no sech factor): orbit sum 4 Re khat(x+iy) can be NEGATIVE off the line
def re_khat(x, y):
    return mp.quad(lambda u: k(u) * mp.cos(x * u) * mp.cosh(y * u), [-2, 0, 2])
print("control: Re khat(x+iy) for k = psi*psi~ alone (no sech factor), y = 0.5, minimum over x in [0, 40] step 0.25:")
vals = [(x / 4, re_khat(x / 4, 0.5)) for x in range(0, 161)]
xm, vm = min(vals, key=lambda t: t[1])
print(f"  min = {float(vm):+.3e} at x = {xm}; (the derivation only says the plain family's orbit sum is not signed in general; no sign is claimed for this psi)")
# transform of cosh(yu)/cosh(u/2): Int e^{iux} cosh(yu)/cosh(u/2) du = 2 pi cosh(pi x) cos(pi y)/|cosh(pi x - i pi y)|^2 > 0 for |y| < 1/2
# (from Int e^{iux}/cosh(u/2) du = 2 pi / cosh(pi x) and the shift x -> x -/+ iy); oscillatory quadrature (mp.quadosc) for the slowly decaying y near 1/2
for y in [0, 0.25, 0.49]:
    x = 1.3
    num = 2 * mp.quadosc(lambda u: mp.cosh(y * u) / mp.cosh(u / 2) * mp.cos(x * u), [0, mp.inf], period=2 * mp.pi / x)
    formula = 2 * mp.pi * mp.cosh(mp.pi * x) * mp.cos(mp.pi * y) / abs(mp.cosh(mp.pi * x - 1j * mp.pi * y))**2
    print(f"FT of cosh({y}u)/cosh(u/2) at x = {x}: quadrature {float(num):.10f}, closed form {float(formula):.10f}")
