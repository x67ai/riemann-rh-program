# ladder.py -- producer A, unit haglund-cert-s37: dress rehearsal R1-R3 (BRIEF section 4) with the SAME code as N = 27.
# Run: python3 ladder.py > ladder.log      (every printed number is an Arb enclosure)
import sys, time, platform
import flint
from flint import acb, arb, ctx
from hag_core import XiN_L, XiN_T, square_vertices, winding

T0 = time.time()
print("python", platform.python_version(), "| python-flint", flint.__version__, "| FLINT", getattr(flint, "__FLINT_VERSION__", "?"))

# (C0) convention check: acb(x).gamma_upper(s) = Gamma(s, x).  Gamma(1,2) = e^-2, Gamma(3,2) = 2 e^-2 (1+2+2) = 10 e^-2.
ctx.prec = 128
g1, g3 = acb(2).gamma_upper(1), acb(2).gamma_upper(3)
print("C0 Gamma(1,2) =", g1.real.str(20), " e^-2 =", arb(-2).exp().str(20), " overlap:", g1.overlaps(acb(arb(-2).exp())))
print("C0 Gamma(3,2) =", g3.real.str(20), " 10e^-2 =", (10 * arb(-2).exp()).str(20), " overlap:", g3.overlaps(acb(10 * arb(-2).exp())))

def sign_change(N, lo, hi, prec, route):
    ctx.prec = prec
    f = (lambda z: XiN_L(N, z)) if route == "L" else (lambda z: XiN_T(N, z))
    t0 = time.time()
    a = f(acb(arb(lo))).real
    b = f(acb(arb(hi))).real
    ok = (a > 0 and b < 0) or (a < 0 and b > 0)
    print("R1 N=%d route %s prec %d: Xi_N(%s) in %s (rad %s) ; Xi_N(%s) in %s (rad %s) ; certified sign change: %s (%.2fs)" % (
        N, route, prec, lo, a.str(30, more=True), a.rad().str(3, radius=False), hi, b.str(30, more=True), b.rad().str(3, radius=False),
        ok, time.time() - t0))
    return ok

# (R1) Haglund p. 4 table: largest real zero 14.0454395788 (N=1), 39.5324810798 (N=2)
r1 = []
for route in ["L", "T"]:
    r1.append(sign_change(1, "14.04543957", "14.04543959", 256, route))
    r1.append(sign_change(2, "39.5324810797", "39.5324810799", 256, route))
print("R1 all certified:", all(r1))

# (R2) Haglund Appendix p. 15: non-real zero of Xi_1 of smallest modulus in Q, 20.62534600592171760132974 + 2.697151842339519632505712 i
ctx.prec = 256
f1 = lambda z: XiN_T(1, z)
k2 = winding(f1, square_vertices("20.62534600592171760132974", "2.697151842339519632505712", "1e-10"), K0=8, tag="R2[N=1,r=1e-10]")
print("R2 winding number (expected 1):", k2)

# (R3) negative controls (squares containing no zero; expected winding 0), same code
k3a = winding(f1, square_vertices("21.12534600592171760132974", "2.697151842339519632505712", "0.1"), K0=8, tag="R3a[N=1,shift+0.5,r=0.1]")
print("R3a winding number (expected 0):", k3a)
k3b = winding(f1, square_vertices("20.62534600622171760132974", "2.697151842339519632505712", "1e-10"), K0=8, tag="R3b[N=1,shift+3e-10,r=1e-10]")
print("R3b winding number (expected 0; the zero lies 2e-10 left of this square):", k3b)
print("LADDER VERDICT: R1 %s, R2 %s, R3 %s ; total %.1fs" % (all(r1), k2 == 1, (k3a == 0 and k3b == 0), time.time() - T0))
