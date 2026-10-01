#!/usr/bin/env python3
"""sigma_1(X) for every snapshot x_K ~ 10^d of one system, with the s8o real zero of F_{10^d} (Session-40 log, data only).
Usage: sigma_table.py <name: pi16|pi32> <lo> <hi>"""
import sys, os, re, glob
from fractions import Fraction as Fr
from feval import Moments
from certify import largest_pos, q, sign

name = sys.argv[1]; den = 16 if name == "pi16" else 32
lo, hi = Fr(sys.argv[2]), Fr(sys.argv[3])
here = os.path.dirname(os.path.abspath(__file__))
s8o = {}
p = os.path.join(here, "..", "..", "..", "free-greedy-s40", "compute", "verify-O", "logs", f"realzero_o_{name}.txt")
for line in open(p):
    m = re.match(r"X=([\d.e+]+) N=(\d+) E\(X\)=(\S+) real zero (\S+)", line)
    if m: s8o[round(float(m[1]))] = (int(m[2]), float(m[3]), m[4])
files = sorted(glob.glob(os.path.join(here, "data", f"{name}_K*.mom")), key=lambda f: int(re.search(r"_K(\d+)", f)[1]))
print(f"# {name}: sigma_1 = largest 12-decimal sigma with F_X(sigma) > 0 proved (arb); X = x_K; s8o column: real zero of F_X at X = 10^d")
print("# K  x_K  N(x_K)  E(x_K)  sigma_1  F_X(sigma_1)  F_X(sigma_1+1e-12)<0 proved?  | s8o: N(10^d) E(10^d) zero")
for f in files:
    mo = Moments(f, den)
    if mo.K < 90000:
        continue
    F = mo.F
    if not (sign(F(q(lo))) == 1 and sign(F(q(hi))) == -1):
        print(f"{mo.K} bracket fails"); continue
    s1, s1b = largest_pos(F, lo, hi, 12)
    f1, f2 = F(q(s1)), F(q(s1b))
    xk = float(mo.X.mid())
    d = round(__import__('math').log10(xk))
    o = s8o.get(10**d, ("-", "-", "-"))
    print(f"{mo.K} {xk:.6f} {mo.N} {mo.eK}.5 {float(s1):.12f} {f1.str(3, radius=True)} {sign(f2) == -1} | {o[0]} {o[1]} {o[2]}")
    sys.stdout.flush()
