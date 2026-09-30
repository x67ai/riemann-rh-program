"""ladder.py -- brief section 4, R1-R3, run with the SAME code as the N = 27 certificate (xin.XiN_tail + winding.py).
  R1: sign changes of Xi_1 on (14.04543957, 14.04543959) and of Xi_2 on (39.5324810797, 39.5324810799)  [Haglund p. 4 table]
      + cross-check: tail route vs literal sum (13) at the same exact points (enclosures must overlap).
  R2: winding number 1 of Xi_1 on squares around Haglund's Appendix zero 20.62534600592171760132974 + 2.697151842339519632505712 i
  R3: negative control -- winding number 0 on a square with no zero of Xi_1.
Usage: python3 ladder.py     (log: logs/ladder.log)
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ivc import *
from xin import *
from winding import *

LOGF = open(os.path.join(HERE, 'logs', 'ladder.log'), 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOGF.write(s + '\n')
    LOGF.flush()


set_prec(200)
RB = 190
T0 = time.time()
log('ladder.py  mpmath %s  iv.prec = %d bits  relbits = %d' % (mp.__version__, iv.prec, RB))


def sign_change(N, x0, x1):
    out = []
    for x in (x0, x1):
        F = XiN_tail(N, point(x), RB)
        L = XiN_lit(N, point(x), RB)
        overlap = not (hi(F.re) < lo(L.re) or hi(L.re) < lo(F.re) or hi(F.im) < lo(L.im) or hi(L.im) < lo(F.im))
        log('  Xi_%d(%s): tail  %s   (M = %d)' % (N, x, F.nstr(16), STATS['M']))
        log('  Xi_%d(%s): literal %s   overlap with tail: %s' % (N, x, L.nstr(16), overlap))
        sgn = 1 if lo(F.re) > 0 else (-1 if hi(F.re) < 0 else 0)
        out.append((sgn, overlap))
    ok = out[0][0] * out[1][0] == -1 and out[0][1] and out[1][1]
    log('  => R1(N=%d): real parts have strict opposite signs: %s  -> a real zero of Xi_%d in (%s, %s): %s'
        % (N, out[0][0] * out[1][0] == -1, N, x0, x1, 'CERTIFIED' if ok else 'FAILED'))
    return ok


def square_run(N, cx, cy, radii, Rad, rho, m, K, nbox, tag):
    c = point(cx, cy)
    f = lambda z: XiN_tail(N, z, RB)
    t = time.time()
    log('%s: Xi_%d, centre c = %s + %s i;  Taylor model R = %s, rho = %s, m = %d, K = %d' % (tag, N, cx, cy, Rad, rho, m, K))
    D, MR, vals = taylor_model(f, c, Rad, rho, m, K, nbox, log=log)
    log('  |D_0| ~ %s  |D_1| ~ %s  (model built in %.1f s)' % (mp.nstr(abs(D[0].mid()), 6), mp.nstr(abs(D[1].mid()), 6), time.time() - t))
    res = {}
    for r in radii:
        rp = hi(R(r) * iv.sqrt(2))
        E = model_error(MR, Rad, rho, m, K, rp)
        k, st = winding(D, E, c, r, log=log)
        log('  %s: half-width r = %s  ->  winding number k = %s' % (tag, r, k))
        res[r] = k
    z0 = newton_on_model(D, c)
    log('  model zero estimate (non-rigorous): %s' % mp.nstr(z0, 25))
    return res, z0


ok1 = True
log('\n(R1) Haglund p. 4: largest real zeros of Xi_1, Xi_2')
ok1 &= sign_change(1, '14.04543957', '14.04543959')
ok1 &= sign_change(2, '39.5324810797', '39.5324810799')
log('  R1 time %.1f s' % (time.time() - T0))

log('\n(R2) Haglund Appendix, first non-real zero of Xi_1 in Q (smallest modulus, Im > 0)')
r2, z2 = square_run(1, '20.62534600592171760132974', '2.697151842339519632505712', ['1e-3', '1e-8'],
                    '0.5', '0.01', 24, 12, 32, 'R2')
log('  R2 time %.1f s' % (time.time() - T0))

log('\n(R3) negative control: square centre 17 + 1 i, half-width 1/4 (Haglund list: no zero of Xi_1 there)')
r3, _ = square_run(1, '17', '1', ['0.25'], '1.5', '0.6', 48, 24, 48, 'R3')
log('  R3 time %.1f s' % (time.time() - T0))

log('\nSUMMARY: R1 %s;  R2 winding numbers %s (expected 1);  R3 winding number %s (expected 0);  total %.1f s'
    % ('certified' if ok1 else 'FAILED', r2, r3, time.time() - T0))
log('methods used for h(w): %s' % sorted(STATS['methods'].items()))
