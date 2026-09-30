"""selftest.py -- unit checks of the building blocks against mpmath's ordinary (non-interval) functions.  Not load-bearing:
the certificate's rigor rests on the interval enclosures + proved bounds; these tests only guard against coding slips.
Usage: python3 selftest.py      (log: logs/selftest.log)
"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ivc import *
from specfun import h_ibp, h_lower, gamma, zeta_em
from xin import Xi, Phi, point

LOGF = open(os.path.join(HERE, 'logs', 'selftest.log'), 'w')
FAIL = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOGF.write(s + '\n')
    LOGF.flush()


def contains(B, ref, name):
    ok = lo(B.re) <= ref.real <= hi(B.re) and lo(B.im) <= ref.imag <= hi(B.im)
    rel = B.rad() / abs(ref) if ref != 0 else B.rad()
    log('  %-44s contains ref: %s   rad/|ref| = %s' % (name, ok, mp.nstr(rel, 3)))
    if not ok:
        FAIL.append(name)


set_prec(200)
mp.mp.prec = 400
log('selftest.py  mpmath %s' % mp.__version__)
log('(S1) Bernoulli numbers (exact) vs mpmath.bernoulli')
for n in (2, 4, 6, 8, 10, 12, 24, 60, 120):
    b = bernoulli(n)
    ok = abs(mp.mpf(b.numerator) / b.denominator - mp.bernoulli(n)) <= abs(mp.bernoulli(n)) * mp.mpf(2) ** -300
    log('  B_%d ok: %s' % (n, ok))
    if not ok:
        FAIL.append('B%d' % n)
log('(S2) clog_gen on random boxes (3000 boxes x 5 samples)')
random.seed(1)
bad = 0
for _ in range(3000):
    x0, y0 = random.uniform(-3, 3), random.uniform(-3, 3)
    dx, dy = random.uniform(0, 1), random.uniform(0, 1)
    Bx = C(iv.mpf([x0, x0 + dx]), iv.mpf([y0, y0 + dy]))
    try:
        L = clog_gen(Bx)
    except ValueError:
        continue
    for _ in range(5):
        l = mp.log(mp.mpc(x0 + random.random() * dx, y0 + random.random() * dy))
        if not (lo(L.re) <= l.real <= hi(L.re) and lo(L.im) <= l.imag <= hi(L.im)):
            bad += 1
log('  violations: %d' % bad)
if bad:
    FAIL.append('clog_gen')
log('(S3) complex box arithmetic')
contains(C('1.5', '-2') * C(3, 4), mp.mpc(1.5, -2) * mp.mpc(3, 4), 'product')
contains(C('1.5', '-2') / C(3, 4), mp.mpc(1.5, -2) / mp.mpc(3, 4), 'quotient')
contains(cexp(C(1, 2)), mp.exp(mp.mpc(1, 2)), 'exp')
log('(S4) Gamma, zeta, h, Xi, Phi_n at low height and at N = 27 height')
for w in [mp.mpc('0.3', '7.2'), mp.mpc('-1.1', '10.3'), mp.mpc('0.0923', '1571.6')]:
    contains(gamma(C(R(w.real), R(w.imag))), mp.gamma(w), 'Gamma(%s)' % mp.nstr(w, 6))
for s in [mp.mpc('0.5', '14.0454'), mp.mpc('-2.2', '20.6'), mp.mpc('0.1847', '3143.22')]:
    contains(zeta_em(C(R(s.real), R(s.imag)), 190)[0], mp.zeta(s), 'zeta(%s)' % mp.nstr(s, 7))
for w, X in [(mp.mpc('0.3', '7.2'), 4), (mp.mpc('2.25', '-10.3'), 9), (mp.mpc('-0.1', '10.3'), 4), (mp.mpc('3.2', '5'), 400)]:
    ref = (mp.pi * X) ** (-w) * mp.gammainc(w, mp.pi * X)
    Wb = C(R(w.real), R(w.imag))
    for meth in (h_ibp, h_lower):
        b = meth(Wb, iv.pi * X, 190)
        if b is None:
            log('  %-44s declined (not convergent to 2^-190)' % ('%s w=%s X=%dpi' % (meth.__name__, mp.nstr(w, 4), X)))
        elif meth is h_lower and X == 400:
            log('  %-44s (cancellation regime, box radius %s: not used there)' % ('h_lower w=%s X=400pi' % mp.nstr(w, 4), mp.nstr(b.rad(), 3)))
            if not (lo(b.re) <= ref.real <= hi(b.re)):
                FAIL.append('h_lower400')
        else:
            contains(b, ref, '%s w=%s X=%dpi' % (meth.__name__, mp.nstr(w, 4), X))
for (x, y) in [('14.04543957', '0'), ('20.625346', '2.697152'), ('3143.2206824215', '0.3152587994')]:
    z = mp.mpc(mp.mpf(x), mp.mpf(y))
    s = mp.mpf('0.5') + 1j * z
    contains(Xi(point(x, y), 190), s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s), 'Xi(%s + %s i)' % (x, y))
    for n in ((1, 2, 3) if float(x) < 100 else (28,)):
        X = mp.pi * n * n
        hh = lambda w: X ** (-w) * mp.gammainc(w, X)
        ref = 2 * X ** 2 * (hh(s / 2 + 2) + hh((1 - s) / 2 + 2)) - 3 * X * (hh(s / 2 + 1) + hh((1 - s) / 2 + 1))
        contains(Phi(n, point(x, y), 190), ref, 'Phi_%d(%s + %s i)' % (n, x, y))
log('SELFTEST %s' % ('PASSED' if not FAIL else 'FAILED: %s' % FAIL))
