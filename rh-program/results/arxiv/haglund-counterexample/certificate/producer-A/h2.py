# h2.py -- producer A, unit haglund-cert-s37: clause H2 of Theorem H by a rigorous winding number, route T on ball inputs.
# Run: python3 h2.py > h2.log
#   S = c + [-r, r]^2, c = 3143.2206824215 + 0.3152587994 i (exact decimals).  f = Xi_27 by route T (hag_core.XiN_T, M = 31).
#   Same winding code as the ladder (R2/R3).  Controls at N = 27: squares that must return 0.
import sys, time
from flint import acb, arb, ctx
from hag_core import XiN_T, square_vertices, winding

N = 27
CX, CY = "3143.2206824215", "0.3152587994"
f = lambda z: XiN_T(N, z)
T0 = time.time()
res = {}
runs = [
    ("H2[r=1e-3,prec=256]", CX, CY, "1e-3", 256, 1),
    ("H2[r=1e-3,prec=512]", CX, CY, "1e-3", 512, 1),
    ("H2[r=1e-6,prec=256]", CX, CY, "1e-6", 256, 1),
    ("H2[r=1e-10,prec=256]", CX, CY, "1e-10", 256, 1),
    ("H2[r=4e-11,prec=256]", CX, CY, "4e-11", 256, 1),
    # controls (expected winding 0): shifted +2.5e-3 in Re (the zero lies 1.5e-3 left of the square);
    # shifted +1.5e-10 in Re with r = 1e-10 (the zero, at c + 3.66e-11 - 2.18e-11 i, lies 1.3e-11 left of the square)
    ("CTL27a[c+2.5e-3,r=1e-3]", "3143.2231824215", CY, "1e-3", 256, 0),
    ("CTL27b[c+1.5e-10,r=1e-10]", "3143.2206824216500", CY, "1e-10", 256, 0),
]
for tag, cx, cy, r, prec, expect in runs:
    ctx.prec = prec
    k = winding(f, square_vertices(cx, cy, r), K0=16, maxdepth=16, out=lambda s: print(s, flush=True), tag=tag)
    res[tag] = (k, expect)
    print("%s RESULT winding = %s (expected %d) -> %s" % (tag, k, expect, "OK" if k == expect else "MISMATCH"), flush=True)
print("SUMMARY:")
for tag, (k, e) in res.items():
    print("  %-28s winding %s expected %d %s" % (tag, k, e, "OK" if k == e else "MISMATCH"))
print("H2 VERDICT: %s ; total %.1fs" % (all(k == e for k, e in res.values()), time.time() - T0))
