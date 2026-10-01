#!/usr/bin/env python3
"""Compare s8cert checkpoints (CHK lines: N, pi, sup E at V = floor(10^(h/2))) with the s8o log of Session 40
(free-greedy-s40/compute/verify-O/logs/o_<name>_1e10.log), read as data only. Usage: crosscheck.py <name>"""
import sys, re, os
name = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
mine = os.path.join(here, "logs", f"s8cert_{name}_1e10.log")
s40 = os.path.join(here, "..", "..", "..", "free-greedy-s40", "compute", "verify-O", "logs", f"o_{name}_1e10.log")
A = {}
for line in open(mine):
    m = re.match(r"CHK V=(\d+) N=(\d+) pi=(\d+) supE=([\d.]+)", line)
    if m: A[int(m[1])] = (int(m[2]), int(m[3]), float(m[4]))
B = {}
for line in open(s40):
    if line.startswith('#'): continue
    f = line.split()
    if len(f) >= 4: B[int(f[0])] = (int(f[1]), int(f[2]), float(f[3]))
print(f"# s8cert ({os.path.basename(mine)}) vs s8o ({os.path.relpath(s40, here)})")
print("# V  N(s8cert) N(s8o)  pi(s8cert) pi(s8o)  supE(s8cert) supE(s8o)  |dsupE|")
bad = 0
for V in sorted(A):
    if V not in B: continue
    a, b = A[V], B[V]
    ok = a[0] == b[0] and a[1] == b[1]
    bad += not ok
    print(f"{V} {a[0]} {b[0]} {a[1]} {b[1]} {a[2]:.10f} {b[2]:.10f} {abs(a[2]-b[2]):.1e} {'OK' if ok else 'MISMATCH'}")
print(f"# checkpoints compared: {sum(1 for V in A if V in B)}, count mismatches: {bad}")
