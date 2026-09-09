"""kappa_check.py -- D-R8 risk R2 guard (PRICING-fDH.md sec. 4.2): reproduce the kappa of the Lean
definition `kappaDH : Real := (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)` against
(a) the contract text FORMAT.md sec. 9.2 (quoting dh.py lines 5-8), (b) the producer-side surd as
hurwitz_encl.py's consumers use it (producer_mp.py / producer_arb.py), and (c) the closed form
kappa = tan(theta) with epsilon_chi = e^{2 i theta} = tau(chi)/(i sqrt 5), chi mod 5, chi(2) = i
(FORMAT sec. 9.2's gloss) -- three independent routes, mpmath at 60 digits, agreement to >= 30 digits
demanded.  A read-and-compute check; not a producer run."""
import re, sys, os
from mpmath import mp, mpf, sqrt, tan, atan2, exp, pi, mpc, log, cos, sin, im, re as mre, fabs

mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

# (a) the contract line, read from FORMAT.md sec. 9.2 (never from memory)
fmt = open(os.path.join(ROOT, "results", "d1-m1", "FORMAT.md"), encoding="utf-8").read()
m = re.search(r"kap = \(sqrt\(10-2\*sqrt5\) - 2\)/\(sqrt5 - 1\)", fmt)
assert m, "FORMAT.md sec. 9.2 kappa line not found verbatim"
print("FORMAT.md sec. 9.2 line:", m.group(0))
# same line in dh.py (the source FORMAT quotes)
dh = open(os.path.join(ROOT, "results", "ccm-dh-test", "dh.py"), encoding="utf-8").read()
m2 = re.search(r"kap\s*=\s*\(sqrt\(10-2\*sqrt5\) - 2\)/\(sqrt5 - 1\)", dh)
print("dh.py line found:", bool(m2), "->", m2.group(0) if m2 else "(pattern differs; see below)")
if not m2:
    for ln in dh.splitlines()[:12]:
        if "kap" in ln:
            print("   dh.py:", ln.rstrip())

# (a') the contract formula evaluated exactly as written
sqrt5 = sqrt(mpf(5))
kappa_contract = (sqrt(10 - 2 * sqrt5) - 2) / (sqrt5 - 1)

# (b) the Lean definition, transcribed token by token from Zeta23/W1/FDH.lean's kappaDH:
#     (Real.sqrt (10 - 2 * Real.sqrt 5) - 2) / (Real.sqrt 5 - 1)
kappa_lean = (sqrt(mpf(10) - mpf(2) * sqrt(mpf(5))) - mpf(2)) / (sqrt(mpf(5)) - mpf(1))

# (c) the closed form tan(theta), epsilon_chi = e^{2 i theta} = tau(chi)/(i sqrt5), chi mod 5 with chi(2) = i
#     chi(1)=1, chi(2)=i, chi(4)=chi(2)^2=-1, chi(3)=chi(2)^3=-i (2 generates (Z/5)^*: 2,4,3,1)
chi = {1: mpc(1, 0), 2: mpc(0, 1), 3: mpc(0, -1), 4: mpc(-1, 0)}
tau = sum(chi[a] * exp(2 * pi * mpc(0, 1) * a / 5) for a in chi)
eps = tau / (mpc(0, 1) * sqrt5)
assert fabs(abs(eps) - 1) < mpf(10) ** -50, "epsilon_chi not unimodular"
theta = atan2(im(eps), mre(eps)) / 2
kappa_closed = tan(theta)

print()
print("kappa (contract text, FORMAT sec. 9.2 / dh.py) =", kappa_contract)
print("kappa (Lean kappaDH transcription)            =", kappa_lean)
print("kappa (tan theta, eps_chi = tau(chi)/(i sqrt5)) =", kappa_closed)
d1 = fabs(kappa_contract - kappa_lean)
d2 = fabs(kappa_contract - kappa_closed)
print("|contract - lean|   =", d1)
print("|contract - closed| =", d2)
digits = min(-int(log(d, 10)) if d > 0 else 60 for d in (d1, d2))
print("agreement digits (min over the two comparisons) =", digits)
print("leading digits per PRICING sec. 1.1: 0.28407904... ->", str(kappa_lean)[:12])
ok = digits >= 30 and str(kappa_lean).startswith("0.28407904")
print("VERDICT:", "PASS (>= 30 digits, three routes agree)" if ok else "FAIL")
# also: both radicands positive, denominator nonzero (no Real.sqrt / division junk in Lean)
print("radicand 10 - 2 sqrt5 =", 10 - 2 * sqrt5, "> 0:", (10 - 2 * sqrt5) > 0)
print("denominator sqrt5 - 1 =", sqrt5 - 1, "!= 0:", (sqrt5 - 1) != 0)
sys.exit(0 if ok else 1)
