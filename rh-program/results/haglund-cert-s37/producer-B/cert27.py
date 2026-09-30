"""cert27.py -- Theorem H of the brief for N = 27, with the code validated by ladder.py (xin.XiN_tail + winding.py).
  H1: Xi_27 changes sign between 3144.8946 and 3144.8947 (tail route, exact decimal points).
  H4: Xi_27 changes sign between 3145.5998 and 3145.5999.
  H2: winding number of Xi_27 on dS, S = c + [-r, r]^2, c = 3143.2206824215 + 0.3152587994 i, for r = 1e-3 down to the smallest.
  C27: control -- square centred at c + 0.01, r = 1e-3: winding number must be 0.
Usage: python3 cert27.py      (log: logs/cert27.log)
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ivc import *
from xin import *
from winding import *

LOGF = open(os.path.join(HERE, 'logs', 'cert27.log'), 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOGF.write(s + '\n')
    LOGF.flush()


set_prec(200)
RB = 190
N = 27
T0 = time.time()
log('cert27.py  mpmath %s  iv.prec = %d bits  relbits = %d  N = %d' % (mp.__version__, iv.prec, RB, N))
f = lambda z: XiN_tail(N, z, RB)


def sign_change(x0, x1, tag):
    sg = []
    for x in (x0, x1):
        t = time.time()
        F = f(point(x))
        log('  Xi_27(%s) in %s   (M = %d, zeta E-M N,m,bound = %s; %.2f s)' % (x, F.nstr(16), STATS['M'], STATS['zeta'], time.time() - t))
        sg.append(1 if lo(F.re) > 0 else (-1 if hi(F.re) < 0 else 0))
    ok = sg[0] * sg[1] == -1
    log('  => %s: strict opposite signs of the real parts: %s -> real zero of Xi_27 in (%s, %s): %s'
        % (tag, ok, x0, x1, 'CERTIFIED' if ok else 'NOT CERTIFIED'))
    return ok


log('\n(H1) real zero in (3144.8946, 3144.8947)')
H1 = sign_change('3144.8946', '3144.8947', 'H1')
log('\n(H4) second real zero in (3145.5998, 3145.5999)')
H4 = sign_change('3145.5998', '3145.5999', 'H4')
log('  time %.1f s' % (time.time() - T0))

cx, cy = '3143.2206824215', '0.3152587994'
Rad, rho, m, K, nbox = '0.1', '0.002', 24, 12, 32
c = point(cx, cy)
log('\n(H2) Taylor model of Xi_27 at c = %s + %s i:  R = %s, rho = %s, m = %d, K = %d, %d boxes' % (cx, cy, Rad, rho, m, K, nbox))
t = time.time()
D, MR, vals = taylor_model(f, c, Rad, rho, m, K, nbox, log=log)
log('  model built in %.1f s;  D_0 = %s' % (time.time() - t, D[0].nstr(12)))
log('  D_1 = %s' % D[1].nstr(12))
Fc = f(c)
alias = hi(R(MR) * (R(rho) / R(Rad)) ** m / (1 - (R(rho) / R(Rad)) ** m))
log('  direct f(c) = %s;  |f(c) - D_0| must be <= M_R q^m/(1-q^m) = %s' % (Fc.nstr(12), mp.nstr(alias, 4)))
log('  consistency: %s' % ((Fc - D[0]).absup() <= alias + D[0].rad() * 4 + Fc.rad() * 4))
res = {}
for r in ['1e-3', '1e-5', '1e-7', '1e-9', '1e-10', '5e-11', '4e-11', '3.7e-11', '3.5e-11']:
    rp = hi(R(r) * iv.sqrt(2))
    E = model_error(MR, Rad, rho, m, K, rp)
    try:
        k, st = winding(D, E, c, r, log=log)
    except RuntimeError as e:
        k = 'FAIL (%s)' % e
    res[r] = k
    log('  H2: r = %s -> winding number k = %s' % (r, k))
z0 = newton_on_model(D, c)
log('  model zero estimate (non-rigorous): %s' % mp.nstr(z0, 25))
cert = [r for r in res if res[r] == 1]
rmin = min(cert, key=lambda r: mp.mpf(r)) if cert else None
log('  smallest certified half-width with k = 1: %s' % rmin)

log('\n(C27) control square centred at c + 0.01, r = 1e-3 (same model; r\' = 0.01 + sqrt(2) 1e-3)')
sc = point('3143.2306824215', cy)
rp = hi(R('0.01') + R('1e-3') * iv.sqrt(2))
E = model_error(MR, Rad, rho, m, K, rp)
kc, _ = winding(D, E, c, '1e-3', log=log, sc=sc)
log('  C27: winding number k = %s (expected 0)' % kc)

log('\n(H2*) refinement: model re-centred at the Newton zero z* of the first model (rounded to 55 decimals)')
zs = newton_on_model(D, c, steps=8)
with mp.workdps(70):
    xs, ys = mp.nstr(zs.real, 55, strip_zeros=False), mp.nstr(zs.imag, 55, strip_zeros=False)
log('  z* = %s + %s i' % (xs, ys))
cs = point(xs, ys)
D2, MR2, _ = taylor_model(f, cs, Rad, '0.001', 40, K, nbox, log=log)
log('  refined model: D_0 = %s,  D_1 = %s' % (D2[0].nstr(8), D2[1].nstr(8)))
res2 = {}
for r in ['1e-30', '1e-40', '1e-45', '1e-48']:
    E = model_error(MR2, Rad, '0.001', 40, K, hi(R(r) * iv.sqrt(2)))
    try:
        k2, _ = winding(D2, E, cs, r, log=log)
    except RuntimeError as e:
        k2 = 'FAIL (%s)' % e
    res2[r] = k2
    log('  H2*: square z* + [-r, r]^2, r = %s -> winding number k = %s' % (r, k2))

log('\n(X4) direct enclosure at the brief/NOTE 22-digit point z22 = 3143.220682421536585287 + 0.3152587993782148453823 i')
F22 = f(point('3143.220682421536585287', '0.3152587993782148453823'))
log('  Xi_27(z22) in %s   (brief, Arb literal: (2.58e-1085) + (1.70e-1084) i)' % F22.nstr(12))

log('\n(H3) logic with r = 1e-3: Im z0 >= 0.3152587994 - 0.001 = 0.3142587994 > 0; Re z0 <= 3143.2216824215 <= 3143.2217 < 3144.8946')
ok3 = H1 and res.get('1e-3') == 1 and mp.mpf('3143.2206824215') + mp.mpf('1e-3') < mp.mpf('3144.8946')
log('SUMMARY: H1 %s; H4 %s; H2 k(r=1e-3) = %s, smallest r = %s; control k = %s; H3 %s; total %.1f s'
    % (H1, H4, res.get('1e-3'), rmin, kc, 'HOLDS' if ok3 else 'not established', time.time() - T0))
log('methods used for h(w): %s' % sorted(STATS['methods'].items()))
