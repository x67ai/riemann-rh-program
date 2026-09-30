"""Unit fejer-form-s39, rung 1, step 2: the GENUINE curves, by brute force (no theory used).
g = 1: every short Weierstrass curve y^2 = x^3 + a x + b over F_q (q = 5, 7, 11; char != 2, 3), disc != 0; t = q + 1 - N_1.
g = 2: every y^2 = f(x), f squarefree of degree 5 or 6 over F_q (q odd, so every genus-2 curve has such a model).
  q = 5: ALL f (75 000; deg 5 included because y^2 = x^5 - x has all of P^1(F_5) as branch points, so no deg-6 model moves
  a rational non-branch point to infinity).  q = 7: normal forms (leading coefficient in {1, nu} mod squares; the x^5 (deg 6)
  or x^4 (deg 5) coefficient killed by a translation, legal since 6, 5 are units mod 7); every genus-2 curve over F_7 has a
  deg-6 model (P^1(F_7) has 8 > 6 points).  Point counts over F_q and F_{q^2} = F_q[i]/(i^2 - nu); quadratic character of
  F_{q^2} is chi_q(Norm).  a1 = N_1 - q - 1, s_2 = q^2 + 1 - N_2, a2 = (a1^2 - s_2)/2.  Output: the realized (a1, a2)."""
import json, itertools
import numpy as np
def sqfree(f, p):
    # f = [c0..cd] over F_p, cd != 0; squarefree iff gcd(f, f') = 1
    def trim(a):
        while a and a[-1] % p == 0: a.pop()
        return a
    def rem(a, b):
        a = a[:]; inv = pow(b[-1], p - 2, p)
        while len(a) >= len(b) and a:
            c = a[-1] * inv % p; sh = len(a) - len(b)
            for i in range(len(b)): a[sh + i] = (a[sh + i] - c * b[i]) % p
            trim(a)
        return a
    a = trim([c % p for c in f]); b = trim([(i * f[i]) % p for i in range(1, len(f))])
    if not b: return False
    while b: a, b = b, rem(a, b)
    return len(a) == 1
def chi_table(p):
    t = np.full(p, -1); t[0] = 0
    for x in range(1, p): t[x * x % p] = 1
    return t
def counts(polys, p, nu):
    """polys: int array (P, 7) of coefficients c0..c6.  Returns affine sums over F_p and F_{p^2}."""
    chi = chi_table(p)
    P = polys.shape[0]
    x = np.arange(p)
    val = np.zeros((P, p), dtype=np.int64)
    for k in range(6, -1, -1): val = (val * x[None, :] + polys[:, k:k + 1]) % p
    S1 = (1 + chi[val]).sum(axis=1)
    a = np.repeat(np.arange(p), p); b = np.tile(np.arange(p), p)
    re = np.zeros((P, p * p), dtype=np.int64); im = np.zeros((P, p * p), dtype=np.int64)
    for k in range(6, -1, -1):
        re, im = (re * a + nu * im * b + polys[:, k:k + 1]) % p, (re * b + im * a) % p
    nrm = (re * re - nu * im * im) % p
    S2 = (1 + chi[nrm]).sum(axis=1)
    return S1, S2
res = {}
for q in (5, 7, 11):   # genus 1
    chi = chi_table(q); ts = set()
    for a_, b_ in itertools.product(range(q), repeat=2):
        if (4 * a_**3 + 27 * b_**2) % q == 0: continue
        N1 = 1 + sum(1 + chi[(x**3 + a_ * x + b_) % q] for x in range(q)); ts.add(int(q + 1 - N1))
    res['g1_q%d' % q] = sorted(ts)
    print("q=%d genus 1: realized traces t = %s (Hasse |t| <= %.3f)" % (q, sorted(ts), 2 * q**0.5))
for q, nu, full in ((5, 2, True), (7, 3, False)):   # genus 2 (nu a non-residue)
    chi = chi_table(q); polys = []
    for deg in (5, 6):
        leads = range(1, q) if full else (1, nu)
        for lead in leads:
            free = deg - (0 if full else 1)
            for cs in itertools.product(range(q), repeat=free):
                c = list(cs) + ([0] if not full else []) + [lead]   # c0..c_{deg-1}, (killed coeff), lead
                c = c[:deg + 1]
                if not full: c = list(cs) + [0, lead]
                if sqfree(c, q): polys.append((c + [0] * 7)[:7] + [deg])
    arr = np.array(polys, dtype=np.int64); deg = arr[:, 7]; C = arr[:, :7]
    S1, S2 = counts(C, q, nu)
    lead = np.where(deg == 6, C[:, 6], C[:, 5])
    inf1 = np.where(deg == 6, 1 + chi[lead % q], 1); inf2 = np.where(deg == 6, 2, 1)
    N1 = S1 + inf1; N2 = S2 + inf2
    a1 = N1 - q - 1; s2 = q * q + 1 - N2; a2x2 = a1 * a1 - s2
    assert np.all(a2x2 % 2 == 0)
    pairs = sorted(set(zip(a1.tolist(), (a2x2 // 2).tolist())))
    res['g2_q%d' % q] = pairs
    print("q=%d genus 2: %d squarefree models; %d realized (a1, a2) pairs" % (q, len(polys), len(pairs)))
json.dump(res, open('r1_genuine.json', 'w'))
