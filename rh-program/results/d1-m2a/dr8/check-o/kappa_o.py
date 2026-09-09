#!/usr/bin/env python3
"""Job 2 (Opus) independent kappa re-derivation for D-R8.  Written from scratch; Job 1's
dr8/kappa_check.py is NOT imported, read or executed.  Four independent routes:

  A  the contract line, read by regex from results/d1-m1/FORMAT.md 9.2 (the pricing's source
     of the object) and from results/ccm-dh-test/dh.py, evaluated at 80 digits;
  B  the Lean literal's tokens, re-read by regex from lean/Zeta23/W1/FDH.lean and evaluated
     independently (Real.sqrt -> mp.sqrt, the same parenthesization);
  C  the Gauss-sum closed form: kappa = tan(theta) with e^{2 i theta} = tau(chi)/(i sqrt 5),
     chi the quartic character mod 5 with chi(2) = i;
  D  dh.py's own kappa() body, re-read by regex and re-evaluated (not imported).

Prints all four to 60 digits and the pairwise differences.  Exit != 0 on any disagreement
beyond 10^-50.
"""
import re, sys, os
from mpmath import mp, mpf, sqrt, exp, pi, mpc, atan, tan, im, re as mpre, arg, fabs

mp.dps = 80
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))

def rd(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read()

fails = []
print("Job 2 independent kappa re-derivation (mpmath, mp.dps = %d)" % mp.dps)
print("repo root: %s" % ROOT)
print()

# ---------- A: the contract line ----------
fmt = rd('results/d1-m1/FORMAT.md')
dh  = rd('results/ccm-dh-test/dh.py')
CONTRACT = r'kap\s*=\s*\(sqrt\(10-2\*sqrt5\)\s*-\s*2\)/\(sqrt5\s*-\s*1\)'
a_fmt = re.search(CONTRACT, fmt)
a_dh  = re.search(CONTRACT, dh)
print("A. contract line  'kap = (sqrt(10-2*sqrt5) - 2)/(sqrt5 - 1)'")
print("   found verbatim in results/d1-m1/FORMAT.md : %s" % bool(a_fmt))
print("   found verbatim in results/ccm-dh-test/dh.py: %s" % bool(a_dh))
if not (a_fmt and a_dh):
    fails.append("contract line not found verbatim in both sources")
sqrt5 = sqrt(mpf(5))
kA = (sqrt(10 - 2*sqrt5) - 2) / (sqrt5 - 1)
print("   radicand 10 - 2*sqrt5 = %s  (> 0: %s)" % (mp.nstr(10 - 2*sqrt5, 20), bool(10 - 2*sqrt5 > 0)))
print("   denominator sqrt5 - 1 = %s  (!= 0: %s)" % (mp.nstr(sqrt5 - 1, 20), bool(sqrt5 - 1 != 0)))
print("   kappa_A = %s" % mp.nstr(kA, 60))
print()

# ---------- B: the Lean literal, re-read ----------
lean = rd('lean/Zeta23/W1/FDH.lean')
m = re.search(r'def\s+kappaDH\s*:\s*ℝ\s*:=\s*(.+)', lean)
print("B. Lean literal, re-read from lean/Zeta23/W1/FDH.lean:")
if not m:
    fails.append("kappaDH definition not found in FDH.lean")
    kB = None
else:
    expr = m.group(1).strip()
    print("   %s" % expr)
    # translate token by token; refuse anything unexpected
    tokens = re.findall(r'Real\.sqrt|[0-9]+|[-+*/()]', expr)
    joined = ''.join(tokens)
    # Lean writes application by juxtaposition: rewrite `Real.sqrt ARG` to `sqrt(ARG)` where ARG
    # is either a balanced parenthesized group or a single numeral.  Anything else is refused.
    def lean_to_py(t):
        out = ''
        i = 0
        while i < len(t):
            if t.startswith('Real.sqrt', i):
                i += len('Real.sqrt')
                while i < len(t) and t[i] == ' ':
                    i += 1
                if i < len(t) and t[i] == '(':
                    d, j = 0, i
                    while j < len(t):
                        if t[j] == '(':
                            d += 1
                        elif t[j] == ')':
                            d -= 1
                            if d == 0:
                                break
                        j += 1
                    if d != 0:
                        raise ValueError('unbalanced parentheses after Real.sqrt')
                    out += 'sqrt(' + lean_to_py(t[i + 1:j]) + ')'
                    i = j + 1
                else:
                    m2 = re.match(r'[0-9]+', t[i:])
                    if not m2:
                        raise ValueError('Real.sqrt applied to an unrecognized argument')
                    out += 'sqrt(' + m2.group(0) + ')'
                    i += m2.end()
            else:
                out += t[i]
                i += 1
        return out
    py = lean_to_py(expr)
    print("   as Python: %s" % py)
    if not re.fullmatch(r'[\sA-Za-z0-9_.+\-*/()]+', py):
        fails.append("unexpected characters in kappaDH expression")
    # only these identifiers may appear
    ids = set(re.findall(r'[A-Za-z_][A-Za-z0-9_.]*', expr))
    print("   identifiers used: %s" % sorted(ids))
    if ids - {'Real.sqrt'}:
        fails.append("kappaDH uses identifiers other than Real.sqrt: %s" % (ids - {'Real.sqrt'}))
    kB = eval(py, {'sqrt': sqrt, '__builtins__': {}}, {})
    print("   kappa_B = %s" % mp.nstr(kB, 60))
print()

# ---------- C: the Gauss-sum closed form ----------
# chi mod 5, quartic, chi(2) = i.  2 is a primitive root mod 5: 2^1=2, 2^2=4, 2^3=3, 2^4=1.
chi = {}
g, v = 2, mpc(0, 1)          # chi(2) = i
x, e = 1, mpc(1, 0)
for k in range(1, 5):
    x = (x * g) % 5
    e = e * v
    chi[x] = e
assert chi[1] == 1 and chi[2] == mpc(0, 1)
tau = sum(chi[a] * exp(2j * pi * a / 5) for a in range(1, 5))
eps = tau / (mpc(0, 1) * sqrt5)
theta = arg(eps) / 2
kC = tan(theta)
print("C. Gauss-sum closed form (chi mod 5 quartic, chi(2) = i):")
print("   chi values: " + ", ".join("chi(%d) = %s" % (a, mp.nstr(chi[a], 12)) for a in sorted(chi)))
print("   tau(chi)   = %s" % mp.nstr(tau, 30))
print("   |tau|      = %s   (sqrt 5 = %s)" % (mp.nstr(abs(tau), 30), mp.nstr(sqrt5, 30)))
print("   eps_chi    = tau/(i sqrt5) = %s   (|eps| = %s)" % (mp.nstr(eps, 30), mp.nstr(abs(eps), 20)))
print("   theta      = %s" % mp.nstr(theta, 40))
print("   kappa_C    = tan(theta) = %s" % mp.nstr(kC, 60))
print()

# ---------- D: dh.py's own kappa() body, re-evaluated ----------
mk = re.search(r'def kappa\(\):(.*?)(?=\ndef |\Z)', dh, re.S)
print("D. dh.py kappa() body, re-read and re-evaluated (not imported):")
kD = None
if mk:
    body = mk.group(1)
    print("".join("   |%s\n" % l for l in body.strip('\n').split('\n')))
    ns = {'mp': mp, '__builtins__': {}}
    src = "def _k():\n" + body + "\n"
    src = src.replace('mp.sqrt', 'mp.sqrt')
    try:
        exec(compile(src, '<dh.kappa>', 'exec'), ns)
        kD = ns['_k']()
        print("   kappa_D = %s" % mp.nstr(kD, 60))
    except Exception as ex:
        fails.append("could not re-evaluate dh.py kappa(): %r" % (ex,))
        print("   FAILED: %r" % (ex,))
else:
    fails.append("dh.py kappa() not found")
print()

# ---------- comparisons ----------
TOL = mpf(10) ** (-50)
vals = [('A contract', kA), ('B Lean', kB), ('C Gauss sum', kC), ('D dh.py', kD)]
vals = [(n, v) for n, v in vals if v is not None]
print("PAIRWISE DIFFERENCES (tolerance 1e-50):")
for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        d = fabs(mpf(vals[i][1].real if hasattr(vals[i][1], 'real') else vals[i][1])
                 - mpf(vals[j][1].real if hasattr(vals[j][1], 'real') else vals[j][1]))
        ok = d < TOL
        print("   |%-11s - %-11s| = %-12s  %s" % (vals[i][0], vals[j][0], mp.nstr(d, 6), "OK" if ok else "MISMATCH"))
        if not ok:
            fails.append("%s vs %s differ by %s" % (vals[i][0], vals[j][0], mp.nstr(d, 6)))
print()
print("kappa (60 digits) = %s" % mp.nstr(kA, 60))
print("leading digits    = %s   (pricing 1.1 says 0.28407904...)" % mp.nstr(kA, 9))
if mp.nstr(kA, 9) != '0.28407904' and not str(mp.nstr(kA, 10)).startswith('0.28407904'):
    fails.append("leading digits are not 0.28407904")
print()
if fails:
    print("VERDICT: FAIL")
    for f in fails:
        print("  - " + f)
    sys.exit(1)
print("VERDICT: PASS  (four independent routes agree to > 50 digits; >= 30 demanded)")
