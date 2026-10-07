# h1.py -- producer A, unit haglund-cert-s37: clause H1 (and optional H4) of Theorem H by BOTH routes.
# Run: python3 h1.py > h1.log
#   H1: Xi_27 changes sign between 3144.8946 and 3144.8947;  H4: between 3145.5998 and 3145.5999.
#   Xi_27 is real and continuous on the real line (G(x;a,b) = 2 Re[Gamma(b+ix,a)/a^{b+ix}] for real x), so a certified
#   sign change at two exact decimal points gives a real zero strictly between them (IVT).
import time
from flint import acb, arb, ctx
from hag_core import XiN_L, XiN_T

N = 27
T0 = time.time()

def ev(route, prec, t):
    ctx.prec = prec
    z = acb(arb(t))                      # exact decimal carried as an Arb ball containing it (made at this precision)
    t0 = time.time()
    v = XiN_L(N, z) if route == "L" else XiN_T(N, z)
    x = v.real
    print("  route %s prec %5d: Xi_27(%s) in %s  (rad %s; Im part %s) (%.2fs)" % (
        route, prec, t, x.str(15, more=True), x.rad().str(3, radius=False), v.imag.str(3, more=True), time.time() - t0), flush=True)
    return x

def cert(lo, hi, label):
    ok_all = True
    for route, prec in [("T", 256), ("T", 1024), ("L", 4800), ("L", 6400)]:
        a, b = ev(route, prec, lo), ev(route, prec, hi)
        ok = (a < 0 and b > 0) or (a > 0 and b < 0)
        print("%s route %s prec %d: certified sign change on [%s, %s]: %s" % (label, route, prec, lo, hi, ok), flush=True)
        ok_all = ok_all and ok
        # L and T must agree (overlapping balls) -- checked below per point
    return ok_all

ok1 = cert("3144.8946", "3144.8947", "H1")
ok4 = cert("3145.5998", "3145.5999", "H4")

# cross-check of the two routes at the four endpoints (balls must overlap)
print("L/T overlap at the H1/H4 endpoints:")
for t in ["3144.8946", "3144.8947", "3145.5998", "3145.5999"]:
    ctx.prec = 4800
    vL = XiN_L(N, acb(arb(t)))
    ctx.prec = 256
    vT = XiN_T(N, acb(arb(t)))
    print("  t=%s  L %s | T %s | overlap %s | |L-T| <= %s" % (t, vL.real.str(12, more=True), vT.real.str(12, more=True),
          vL.overlaps(vT), (vL - vT).real.abs_upper().str(3, radius=False)), flush=True)
print("H1 VERDICT: %s ; H4 VERDICT: %s ; total %.1fs" % (ok1, ok4, time.time() - T0))
