#!/usr/bin/env python3
"""bracket_O.py D K base sigma1 theta — re-derivation of the NOTE's Theorem 6.2 table (read-O, U6).
For each tail hypothesis beyond X = x_K, the bound B(s) of NOTE Lemma 6.1 (re-derived in read-O §1.6):
  (a) E <= Kc log^2 u:        B = Kc X^-s (L^2 + 2L/s + 2/s^2), L = log X
  (b) E <= C u^th:            B = C s X^(th-s)/(s - th)
  (c) int_Y^2Y E^2 <= Y^(1+2th) (Y >= X):  B = s X^(th-s)/(1 - 2^(th-s))
finds by bisection on the 10^-9 grid the smallest sigma2 with F_X(sigma2) + B(sigma2) < 0 PROVED (upper end of the
ball), and checks that F_X + B is proved > 0 one grid step below."""
import sys
from flint import arb, fmpq
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from feval_O import System

D, K, base = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
s1 = fmpq(int(sys.argv[4].replace(".", "")), 10 ** len(sys.argv[4].split(".")[1]))
th = arb(fmpq(int(sys.argv[5].replace(".", "")), 10 ** len(sys.argv[5].split(".")[1])))
S = System(D, K, base); X = S.X; L = X.log()
rows = [("E <= 0.1 log^2 u", lambda s: arb("0.1") * X ** (-s) * (L ** 2 + 2 * L / s + 2 / s ** 2)),
        ("E <= log^2 u", lambda s: X ** (-s) * (L ** 2 + 2 * L / s + 2 / s ** 2)),
        ("E <= 10 log^2 u", lambda s: 10 * X ** (-s) * (L ** 2 + 2 * L / s + 2 / s ** 2)),
        ("E <= 100 log^2 u", lambda s: 100 * X ** (-s) * (L ** 2 + 2 * L / s + 2 / s ** 2)),
        ("E <= u^th", lambda s: s * X ** (th - s) / (s - th)),
        ("E <= 100 u^th", lambda s: 100 * s * X ** (th - s) / (s - th)),
        ("int_Y^2Y E^2 <= Y^(1+2th)", lambda s: s * X ** (th - s) / (1 - arb(2) ** (th - s)))]
print("D=%d K=%d sigma1=%s theta=%s" % (D, K, sys.argv[4], sys.argv[5]))
for name, B in rows:
    G = lambda n: (lambda s: S.F(s) + B(arb(s)))(fmpq(n, 10 ** 9))
    lo = int(s1 * 10 ** 9) if False else (int(s1.p) * 10 ** 9) // int(s1.q)   # floor(sigma1 1e9)
    hi = lo + 1
    while not (G(hi) < 0): hi = lo + 2 * (hi - lo)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if G(mid) < 0: hi = mid
        else: lo = mid
    g_hi, g_lo = G(hi), G(hi - 1)
    ok = "proved > 0 one step below" if g_lo > 0 else "NOT proved > 0 one step below"
    print("%-28s sigma2 = 0.%09d  sigma2 - sigma1 = %s  [F+B](sigma2) = %s ; %s" % (name, hi,
          (arb(fmpq(hi, 10 ** 9)) - arb(s1)).str(4), g_hi.str(5, radius=True), ok))
