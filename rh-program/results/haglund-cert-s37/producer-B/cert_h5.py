"""cert_h5.py -- optional clause H5 of the brief: the sibling statement for the seed chain  xi_N(s) = 1/2 + (1/2) s(s-1) sum_{n<=N} g_n(s)
(staircase NOTE sections 1 and 4), N = 24, evaluated as  xi_24 = xi - (1/2) s(s-1) sum_{n>24} g_n  with the kernels of cert27.py.
  (L) ladder for this evaluator: at N = 1, 2 the tail route and the defining finite sum overlap (two low points).
  (a) xi_24(1/2 + i t) is real; sign changes on (2510.2026, 2510.2027) and (2510.7086, 2510.7087).
  (b) winding number of z -> xi_24(1/2 + i z) on squares centred at c5 = 2508.2839748053 + 0.3159896243 i (s = 0.1840103757 + 2508.2839748053 i,
      the mirror 1 - conj(s) of the NOTE's zero 0.8159896243 + 2508.2839748053 i), r = 1e-3 down; control square at c5 + 0.01.
Usage: python3 cert_h5.py      (log: logs/cert_h5.log)
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ivc import *
from xin import *
from winding import *

LOGF = open(os.path.join(HERE, 'logs', 'cert_h5.log'), 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOGF.write(s + '\n')
    LOGF.flush()


def overlap(A, B):
    return not (hi(A.re) < lo(B.re) or hi(B.re) < lo(A.re) or hi(A.im) < lo(B.im) or hi(B.im) < lo(A.im))


set_prec(200)
RB = 190
T0 = time.time()
log('cert_h5.py  mpmath %s  iv.prec = %d' % (mp.__version__, iv.prec))
log('\n(L) seed-chain evaluator: tail route vs defining sum')
for N, (x, y) in [(1, ('14.0', '0')), (1, ('20.6', '2.7')), (2, ('39.5', '0')), (2, ('30.1', '1.3'))]:
    T = xiN_seed_tail(N, point(x, y), RB)
    L = xiN_seed_lit(N, point(x, y), RB)
    log('  xi_%d(1/2 + i(%s + %s i)): tail %s ; defining sum %s ; overlap %s' % (N, x, y, T.nstr(14), L.nstr(14), overlap(T, L)))

N = 24
f = lambda z: xiN_seed_tail(N, z, RB)
log('\n(a) real zeros of xi_24 on the critical line')
okA = True
for x0, x1 in [('2510.2026', '2510.2027'), ('2510.7086', '2510.7087')]:
    sg = []
    for x in (x0, x1):
        F = f(point(x))
        log('  xi_24(1/2 + i %s) in %s   (M = %d)' % (x, F.nstr(16), STATS['M']))
        sg.append(1 if lo(F.re) > 0 else (-1 if hi(F.re) < 0 else 0))
    ok = sg[0] * sg[1] == -1
    okA &= ok
    log('  => sign change on (%s, %s): %s' % (x0, x1, 'CERTIFIED' if ok else 'NOT CERTIFIED'))

cx, cy = '2508.2839748053', '0.3159896243'
Rad, rho, m, K, nbox = '0.1', '0.002', 24, 12, 32
c = point(cx, cy)
log('\n(b) Taylor model of z -> xi_24(1/2 + i z) at c5 = %s + %s i: R = %s, rho = %s, m = %d, K = %d' % (cx, cy, Rad, rho, m, K))
D, MR, _ = taylor_model(f, c, Rad, rho, m, K, nbox, log=log)
log('  D_0 = %s ; D_1 = %s' % (D[0].nstr(10), D[1].nstr(10)))
res = {}
for r in ['1e-3', '1e-6', '1e-9', '1e-10']:
    E = model_error(MR, Rad, rho, m, K, hi(R(r) * iv.sqrt(2)))
    try:
        k, _ = winding(D, E, c, r, log=log)
    except RuntimeError as e:
        k = 'FAIL (%s)' % e
    res[r] = k
    log('  H5: r = %s -> winding number k = %s' % (r, k))
zs = newton_on_model(D, c, steps=8)
log('  model zero (non-rigorous): z = %s  (s = 1/2 + i z = %s)' % (mp.nstr(zs, 30), mp.nstr(mp.mpf('0.5') + 1j * zs, 30)))
sc = point('2508.2939748053', cy)
E = model_error(MR, Rad, rho, m, K, hi(R('0.01') + R('1e-3') * iv.sqrt(2)))
kc, _ = winding(D, E, c, '1e-3', log=log, sc=sc)
log('  control square c5 + 0.01, r = 1e-3: k = %s (expected 0)' % kc)
ok = okA and res.get('1e-3') == 1 and kc == 0
log('\nSUMMARY H5: real zeros certified %s; winding at r = 1e-3: %s; control %s; => a zero z5 of xi_24(1/2 + i z) with Im z5 > 0.3149 and '
    'Re z5 < 2508.2850 < 2510.2026 < a real zero: ordering invariant FAILS for xi_24: %s  (%.0f s)'
    % (okA, res.get('1e-3'), kc, 'CERTIFIED' if ok else 'NOT CERTIFIED', time.time() - T0))
log('methods: %s' % sorted(STATS['methods'].items()))
