# Orchestrator's re-run of N2's decisive computation (Session 37): Haglund's Xi_27 by the LITERAL sum (13)-(14)
# in Arb balls at high precision (the sum cancels ~1060 digits at this height).
import sys, time
from flint import acb, arb, ctx
from haglund_direct_arb import XiN
bits = int(sys.argv[1]) if len(sys.argv) > 1 else 4800
ctx.prec = bits
N = 27
def show(label, z):
    t0 = time.time()
    v = XiN(N, z)
    print(label, "\n   Re:", v.real.str(12), "\n   Im:", v.imag.str(12), "  (%.1fs)" % (time.time()-t0), flush=True)
    return v
print("bits =", bits)
# (1) real-axis sign changes around the NOTE's real zeros t1 = 3144.894662218646757, t2 = 3145.599849576487141
for t in ["3144.8946", "3144.8947", "3145.5998", "3145.5999"]:
    show("Xi_27(%s)" % t, acb(arb(t)))
# (2) the claimed off-line zero  z0 = 3143.220682421536585287 + 0.3152587993782148453823 i
z0 = acb(arb("3143.220682421536585287"), arb("0.3152587993782148453823"))
v0 = show("Xi_27(z0)", z0)
# scale: value at a point 1e-6 away (derivative scale)
z1 = acb(arb("3143.220683421536585287"), arb("0.3152587993782148453823"))
v1 = show("Xi_27(z0 + 1e-6)", z1)
# (3) no real zero claimed in (3142.95, 3144.0): sample signs at a few points (not a proof)
for t in ["3142.95", "3143.2", "3143.5", "3144.0"]:
    show("Xi_27(%s)" % t, acb(arb(t)))
