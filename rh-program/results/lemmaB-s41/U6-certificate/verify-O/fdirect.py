#!/usr/bin/env python3
"""fdirect.py — direct ball summation of F_X(s) over every g-integer listed in an s8gen dump (composites as factor
lists of lattice indices, g-primes as 'P m' lines, plus the g-integer 1): an independent check of the block-moment
evaluation in feval_O.py (read-O, U6). Usage: fdirect.py D K dumpfile s1 [s2 ...]"""
import sys
from flint import arb, fmpq, ctx
ctx.prec = 256
D, K, fn = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
t = arb(D) / arb.pi(); rho = arb.pi() / D; X = 1 + (arb(K) - arb(1) / 2) * t
xs = lambda n: 1 + (arb(n) - arb(1) / 2) * t
logs = [arb(0)]                                  # log of the g-integer 1
with open(fn) as f:
    for line in f:
        if line.startswith("PRIMES"): continue
        if line.startswith("P "): logs.append(xs(int(line.split()[1])).log()); continue
        fac = [int(v) for v in line.split()[1:]]
        logs.append(sum((xs(n).log() for n in fac), arb(0)))
N = len(logs); EX = arb(N) - K - arb(1) / 2
print("direct: N(X)=%d E(X)=%s" % (N, EX.str(5)))
for sv in sys.argv[4:]:
    s = arb(fmpq(int(sv.replace(".", "")), 10 ** len(sv.split(".")[1])))
    tot = sum(((-s * L).exp() for L in logs), arb(0))
    val = tot + rho * X ** (1 - s) / (s - 1) - EX * X ** (-s)
    print("direct F(%s) = %s" % (sv, val.str(20, radius=True)))
