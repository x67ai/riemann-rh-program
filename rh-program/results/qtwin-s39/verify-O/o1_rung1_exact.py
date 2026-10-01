# o1 (reader's own code): genus 1 over F_5, L(u) = 1 - t u + 5 u^2, t REAL. Exact rational arithmetic (sympy), no floats in decisions.
# N_e(t) = 1 + 5^e - s_e(t), s_e = alpha^e + beta^e (s_0 = 2, s_1 = t, s_e = t s_{e-1} - 5 s_{e-2});  P_d(t) := d*b_d(t) = sum_{e|d} mu(d/e) N_e(t).
from sympy import symbols, Poly, Rational, divisors, sqrt, QQ
from sympy import mobius
import time
t = symbols('t')
D = 60
s = [Poly(2, t, domain=QQ), Poly(t, t, domain=QQ)]
for e in range(2, D+1):
    s.append(Poly(t, t, domain=QQ)*s[e-1] - 5*s[e-2])
N = [None] + [Poly(1 + 5**e, t, domain=QQ) - s[e] for e in range(1, D+1)]
P = [None] + [sum((int(mobius(d//e))*N[e] for e in divisors(d)), Poly(0, t, domain=QQ)) for d in range(1, D+1)]
assert all(c.q == 1 for d in range(1, D+1) for c in P[d].all_coeffs()), "d*b_d must have integer coefficients"
lo, hi = Rational(-5), Rational(6)
bad = []; t0 = time.time()
for d in range(1, D+1):
    p = P[d]
    # exact isolating intervals of all real roots, then exact sign tests between them inside [-5, 6]
    roots = p.intervals()            # list of ((a,b), mult) with rational a <= b
    pts = sorted(set([lo, hi] + [a for (a, b), m in roots if lo < a < hi] + [b for (a, b), m in roots if lo < b < hi]))
    # test a rational point strictly inside every isolating interval and between consecutive breakpoints
    tests = [(pts[i] + pts[i+1])/2 for i in range(len(pts)-1)]
    neg = [x for x in tests if p.eval(x) < 0]
    # roots strictly inside (-5, 6) with ODD multiplicity would mean a sign change
    odd_inside = [((a, b), m) for (a, b), m in roots if m % 2 == 1 and lo < a and b < hi]
    if neg or odd_inside:
        bad.append((d, neg[:3], odd_inside[:3]))
print("d <= %d: integer polys d*b_d(t) built; degree of P_60 = %d; time %.1fs" % (D, P[D].degree(), time.time()-t0))
print("values at the ends: P_1(6) = %s, P_2(-5) = %s, P_2(6) = %s; all P_d(6) == 0: %s" % (P[1].eval(6), P[2].eval(-5), P[2].eval(6), all(P[d].eval(6) == 0 for d in range(1, D+1))))
print("d with a negative value or an odd-order root strictly inside (-5,6):", bad if bad else "NONE")
print("outside: P_1(t) = 6 - t < 0 for t > 6; P_2(t) =", P[2].as_expr(), "< 0 for t < -5 (factor:", P[2].factor_list(), ")")
# (W3): Q-side q-part positivity of zeta(s)L(5^{-s}): s_n <= 1 for all n. Exact certificate with n <= 4.
# s_1 <= 1 <=> t <= 1; s_2 <= 1 <=> |t| <= sqrt(11); s_4 - 1 = t^4 - 20t^2 + 49 <= 0 <=> t^2 in [10 - sqrt(51), 10 + sqrt(51)].
# Hence s_1, s_2, s_4 <= 1 together <=> t in [-sqrt(11), -sqrt(10 - sqrt(51))] (since sqrt(10 - sqrt 51) = 1.69 > 1).
from sympy import Poly as _P, sqrt as _sq, Rational as R
for n in (1, 2, 4):
    print("W3: s_%d - 1 =" % n, (s[n] - 1).as_expr(), " real roots:", [float(r) for r in _P((s[n]-1).as_expr(), t).real_roots()])
A, B = -_sq(11), -_sq(10 - _sq(51))
print("interval allowed by s_1, s_2, s_4: [%s, %s] = [%.6f, %.6f]" % (A, B, float(A), float(B)))
p3 = _P((s[3] - 1).as_expr(), t)
print("s_3 - 1 =", p3.as_expr(), " real roots:", [float(r) for r in p3.real_roots()])
lo3, hi3 = R(-332, 100), R(-169, 100)          # rational box containing [A, B]
assert lo3 < A and B < hi3
print("roots of s_3 - 1 in [-3.32, -1.69]:", p3.count_roots(lo3, hi3), "; s_3(-2) - 1 =", p3.eval(-2), "> 0")
print("=> s_3 > 1 on the whole allowed interval: W3 EMPTY over R (exact).")
print("W4: coefficients of L(u) = 1 - t u + 5u^2 are >= 0 iff t <= 0; with W1: [-5, 0].  W2: RH-false iff |t| > 2 sqrt 5 =", float(2*_sq(5)))
