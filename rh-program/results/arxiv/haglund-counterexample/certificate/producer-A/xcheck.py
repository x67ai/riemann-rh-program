# xcheck.py -- producer A, unit haglund-cert-s37: route L (literal sum, 4800 bits) against route T (tail route, 256 and
# 1024 bits) at 14 exact points on and inside the H2 squares.  Balls must overlap.   Run: python3 xcheck.py > xcheck.log
import time
from flint import acb, arb, ctx
from hag_core import XiN_L, XiN_T

N = 27
CX, CY = "3143.2206824215", "0.3152587994"
def pt(dx, dy):
    return (CX, dx, CY, dy)
pts = [("centre c", pt("0", "0")),
       ("z0* (NOTE 50-digit zero, truncated)", ("3143.220682421536585287", "0", "0.3152587993782148453823", "0")),
       ("r=1e-3 corner SW", pt("-1e-3", "-1e-3")), ("r=1e-3 corner SE", pt("1e-3", "-1e-3")),
       ("r=1e-3 corner NE", pt("1e-3", "1e-3")), ("r=1e-3 corner NW", pt("-1e-3", "1e-3")),
       ("r=1e-3 mid S", pt("0", "-1e-3")), ("r=1e-3 mid E", pt("1e-3", "0")),
       ("r=1e-3 mid N", pt("0", "1e-3")), ("r=1e-3 mid W", pt("-1e-3", "0")),
       ("r=4e-11 corner SW", pt("-4e-11", "-4e-11")), ("r=4e-11 corner SE", pt("4e-11", "-4e-11")),
       ("r=4e-11 corner NE", pt("4e-11", "4e-11")), ("r=4e-11 corner NW", pt("-4e-11", "4e-11"))]
T0 = time.time()
allok = True
for name, (cx, dx, cy, dy) in pts:
    out = {}
    for route, prec in [("L", 4800), ("T", 256), ("T", 1024)]:
        ctx.prec = prec
        z = acb(arb(cx) + arb(dx), arb(cy) + arb(dy))     # exact decimal point, as an Arb box made at this precision
        t0 = time.time()
        out[(route, prec)] = (XiN_L(N, z) if route == "L" else XiN_T(N, z)), time.time() - t0
    L = out[("L", 4800)][0]
    print("%s: z = (%s %s) + (%s %s) i" % (name, cx, dx, cy, dy))
    for key, (v, dt) in out.items():
        print("   %s %5d: %s + %s i   (rad %s, %s) (%.2fs)" % (key[0], key[1], v.real.str(14, more=True), v.imag.str(14, more=True),
              v.real.rad().str(2, radius=False), v.imag.rad().str(2, radius=False), dt))
    for key in [("T", 256), ("T", 1024)]:
        v = out[key][0]
        ok = L.overlaps(v)
        allok = allok and ok
        print("   L vs %s%d: overlap %s ; |L - T| <= %s" % (key[0], key[1], ok, abs(L - v).upper().str(3, radius=False)), flush=True)
print("XCHECK VERDICT: all %d points overlap (L vs T at 256 and 1024 bits): %s ; total %.1fs" % (len(pts), allok, time.time() - T0))
