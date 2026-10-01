#!/usr/bin/env python3
"""gain_O.py D K base sigma1 — NOTE Remark 1.5's gain (1/2) X^-s1 / |F_X'(s1)|, with F_X' enclosed by the difference
quotient over [s1, s1 + 1e-9] (mean value theorem; F_X is smooth there), and the s40-style criterion's sigma
(the zero of F_X - X^-s/2) for comparison (read-O, U6)."""
import sys
from flint import arb, fmpq
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from feval_O import System
D, K, base = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
s1 = fmpq(int(sys.argv[4].replace(".", "")), 10 ** len(sys.argv[4].split(".")[1]))
S = System(D, K, base); X = S.X
d = fmpq(1, 10 ** 9); slope = (S.F(s1 + d) - S.F(s1)) / arb(d)
half = X ** (-arb(s1)) / 2
print("D=%d X=x_K=%s s1=%s: F' ~ %s ; (1/2)X^-s1 = %s ; gain = %s" % (D, X.str(12), sys.argv[4], slope.str(8),
      half.str(6), (half / abs(slope)).str(4)))
