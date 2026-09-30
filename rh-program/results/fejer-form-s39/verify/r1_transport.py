"""Unit fejer-form-s39, rung 1, step 5: the Fejer pairing on the norm group q^Z (positions side) and its transport.
A_n = coefficients of Z(u) = L(u)/((1-u)(1-qu)) (effective-divisor counts); Theta_n = (q-1)A_n + h (n >= 0), = h (n < 0).
(R) Theta_n = q^{n-g+1} Theta_{2g-2-n} for all n (class-summed Riemann-Roch = the FE on the positions side) -- checked exactly.
Fejer defect at window k >= 1 (the dual box of a degree -k box; NOTE §4): D_k = Theta_{2g-2+k} - h = (q-1) A_{2g-2+k}.
Claim checked: D_k = h (q^{g-1+k} - 1) exactly; D_k > 0 on every datum (V-blind).  Product formula:
h = prod_j [ (sqrt q - 1)^2 + 2 sqrt q (1 - cos theta_j) ]; class-number window (sqrt q - 1)^{2g} <= h <= (sqrt q + 1)^{2g}."""
import json, math, cmath
from fractions import Fraction as Fr
Z = json.load(open('r1_zeta_data.json'))
def series(L, q, nmax):
    # coefficients of L(u) / ((1-u)(1-qu)) up to u^nmax, exact
    inv = [(q**(n + 1) - 1) // (q - 1) for n in range(nmax + 1)]      # 1/((1-u)(1-qu))
    return [sum(L[k] * inv[n - k] for k in range(len(L)) if k <= n) for n in range(nmax + 1)]
out = {}
for q in (5, 7, 11):
    for g in (1, 2):
        rows = [r for r in Z[str(q)] if r['g'] == g]
        st = dict(n=len(rows), R_ok=0, Dk_formula_ok=0, Dk_nonpos=0, prod_ok=0, An_neg=0,
                  cn_false_low=0, cn_false_high=0, cn_false_inside=0, cn_true_outside=0, n_false=0)
        for r in rows:
            L, h = r['L'], r['h']; A = series(L, q, 2 * g + 6)
            if min(A) < 0: st['An_neg'] += 1
            Th = lambda n: (q - 1) * A[n] + h if n >= 0 else h
            ok = all(Fr(Th(n)) == Fr(q)**(n - g + 1) * Th(2 * g - 2 - n) for n in range(-4, 2 * g + 3))
            st['R_ok'] += ok
            Dk = [Th(2 * g - 2 + k) - h for k in (1, 2, 3)]
            st['Dk_formula_ok'] += all(Dk[k - 1] == h * (q**(g - 1 + k) - 1) for k in (1, 2, 3))
            st['Dk_nonpos'] += any(d <= 0 for d in Dk)
            # angles: x_j = 2 sqrt q cos theta_j
            if g == 1: xs = [r['t']]
            else:
                a1, a2 = r['a1'], r['a2']; D = a1 * a1 - 4 * (a2 - 2 * q)
                sq = cmath.sqrt(D); xs = [(-a1 + sq) / 2, (-a1 - sq) / 2]
            prod = 1
            for x in xs: prod *= (q**0.5 - 1)**2 + 2 * q**0.5 * (1 - x / (2 * q**0.5))
            st['prod_ok'] += abs(prod - h) < 1e-6 * max(1, h)
            lo, hi = (q**0.5 - 1)**(2 * g), (q**0.5 + 1)**(2 * g)
            if r['rh']:
                st['cn_true_outside'] += not (lo - 1e-9 <= h <= hi + 1e-9)
            else:
                st['n_false'] += 1
                if h < lo: st['cn_false_low'] += 1
                elif h > hi: st['cn_false_high'] += 1
                else: st['cn_false_inside'] += 1
        out['g%d_q%d' % (g, q)] = st
        print('g%d_q%d' % (g, q), json.dumps(st))
V = [r for r in Z['5'] if r['g'] == 1 and r['t'] == 5][0]
A = series(V['L'], 5, 8)
print("V: A_0..A_8 =", A, " = 1, (5^n - 1)/4:", [1] + [(5**n - 1) // 4 for n in range(1, 9)])
print("V: h = %d, D_1 = D(k=1) = %d = h(q^g - 1); class-number floor (sqrt5-1)^2 = %.6f; log-form delta = log h - 2g log(sqrt q - 1) = %.6f"
      % (V['h'], 4 * A[1], (5**0.5 - 1)**2, math.log(V['h']) - 2 * math.log(5**0.5 - 1)))
print("g = 1 affine transport: h = (sqrt q - 1)^2 + 2 sqrt q * (1 - cos theta); free positivity h >= 1  <=>  1 - cos theta >= %.6f = w(V)"
      % ((1 - (5**0.5 - 1)**2) / (2 * 5**0.5)))
json.dump(out, open('r1_transport_summary.json', 'w'), indent=1)
