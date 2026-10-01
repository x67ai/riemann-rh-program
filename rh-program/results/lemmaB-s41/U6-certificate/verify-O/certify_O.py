#!/usr/bin/env python3
"""certify_O.py D K base sa sb [digits] [extra sigma ...] — locate and certify the real zero of F_X, X = x_K (read-O, U6).
Secant iteration on ball midpoints, then sigma1 := root truncated to `digits` decimals; PROVED: lower end of the ball
F_X(sigma1) > 0 and upper end of F_X(sigma1 + 10^-digits) < 0. Extra sigmas are evaluated and printed."""
import sys, time
from flint import arb, fmpq
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from feval_O import System

def q(sv): return fmpq(int(sv.replace(".", "")), 10 ** len(sv.split(".")[1]))
def show(x): return x.str(22, radius=True)

D, K, base, sa, sb = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5]
digits = int(sys.argv[6]) if len(sys.argv) > 6 else 15
t0 = time.time()
S = System(D, K, base)
print("D=%d K=%d X=x_K=%s N(X)=%d E(X)=%s blocks=%d individual=%d (load %.1fs)"
      % (D, K, S.X.str(25), S.Ntot, S.EX.str(5), len(S.blocks), len(S.ind), time.time() - t0))
a, b = q(sa), q(sb); Fa, Fb = S.F(a), S.F(b)
print("F(%s) = %s\nF(%s) = %s" % (sa, show(Fa), sb, show(Fb)))
assert Fa > 0 and Fb < 0
fa, fb = Fa.mid(), Fb.mid()
for it in range(12):                                   # secant on midpoints (exact rationals for sigma)
    c = b - (b - a) * fmpq(int((fb * 2 ** 200).floor().unique_fmpz()), 2 ** 200) / \
        fmpq(int(((fb - fa) * 2 ** 200).floor().unique_fmpz()), 2 ** 200)
    c = fmpq(int((arb(c) * 10 ** (digits + 3)).floor().unique_fmpz()), 10 ** (digits + 3))
    Fc = S.F(c); a, fa, b, fb = b, fb, c, Fc.mid()
    if abs(arb(b - a)) < arb(10) ** (-digits - 2): break
root = b
s1 = fmpq(int((arb(root) * 10 ** digits).floor().unique_fmpz()), 10 ** digits)
for tries in range(6):
    F1 = S.F(s1); F2 = S.F(s1 + fmpq(1, 10 ** digits))
    if F1 > 0 and F2 < 0: break
    s1 = s1 - fmpq(1, 10 ** digits) if not F1 > 0 else s1 + fmpq(1, 10 ** digits)
def fmt(s, d=None):
    d = digits if d is None else d
    v = s * 10 ** d; n = int(v.p) // int(v.q); assert fmpq(n, 10 ** d) == s
    return "%s%d.%0*d" % ("-" if n < 0 else "", abs(n) // 10 ** d, d, abs(n) % 10 ** d)
print("CERTIFIED: F_X(%s) = %s > 0" % (fmt(s1), show(F1)))
print("           F_X(%s) = %s < 0" % (fmt(s1 + fmpq(1, 10 ** digits)), show(F2)))
print("           so the zero of F_X lies in (%s, %s); sigma1/2 = %s; (3 sigma1 - 2)/4 = %s" %
      (fmt(s1), fmt(s1 + fmpq(1, 10 ** digits)), fmt(s1 / 2, digits + 1), fmt((3 * s1 - 2) / 4, digits + 2)))
for sv in sys.argv[7:]:
    print("F_X(%s) = %s" % (sv, show(S.F(q(sv)))))
print("time %.1fs" % (time.time() - t0))
