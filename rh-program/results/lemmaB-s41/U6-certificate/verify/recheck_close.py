#!/usr/bin/env python3
"""Independent recheck of the closest cell decisions (CLOSE lines of an s8cert log) at 80 digits with mpmath
(its own pi; no GMP, no Machin enclosure). For each line: c = prod (1 + (k_i - 1/2) t), t = den/pi; verify
x_{k-1} < c < x_k and compare the relative margin with the logged lower bound. Usage: recheck_close.py <log> <16|32>"""
import sys, re
from mpmath import mp, mpf, pi
mp.dps = 80
log, den = sys.argv[1], int(sys.argv[2])
t = den / pi
x = lambda k: 1 + (k - mpf(1) / 2) * t
n = bad = 0; worst = None
for line in open(log):
    m = re.match(r"CLOSE k=(\d+) rel=(\S+) c~=(\S+) factors (.*)", line)
    if not m:
        continue
    k = int(m[1]); rel_log = float(m[2]); ks = [int(v) for v in m[4].split()]
    c = mpf(1)
    for ki in ks:
        c *= x(ki)
    ok = x(k - 1) < c < x(k)
    rel = min(c - x(k - 1), x(k) - c) / c
    n += 1
    if not ok or abs(float(rel) - rel_log) > 1e-6 * rel_log:
        bad += 1
        print("DISAGREE", line.strip(), "mp rel =", mp.nstr(rel, 8), "inside =", ok)
    if worst is None or rel < worst[0]:
        worst = (rel, k, ks, c)
print(f"# {log.split('/')[-1]}: {n} CLOSE decisions rechecked at {mp.dps} digits, disagreements: {bad}")
if worst:
    rel, k, ks, c = worst
    print(f"# closest: cell k = {k}, c = {mp.nstr(c, 25)}, factors (lattice indices) = {ks}")
    print(f"#   c - x_(k-1) = {mp.nstr(c - x(k - 1), 6)}, x_k - c = {mp.nstr(x(k) - c, 6)}, relative margin = {mp.nstr(rel, 6)}")
