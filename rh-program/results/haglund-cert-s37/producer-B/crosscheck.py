"""crosscheck.py -- independent checks of the N = 27 tail-route enclosures (none is load-bearing for Theorem H).
 (X1) Xi(z) boxes (Stirling + Euler-Maclaurin, 200 bits) contain mpmath's ordinary high-precision zeta/gamma values (non-rigorous ref).
 (X2) the kernel h(w) = X^{-w} Gamma(w, X) at X = 784 pi, at the four arguments of Phi_28(c): integration by parts (200 bits)
      vs Gamma(w) minus the lower series (1400 bits) -- two different proved expansions; boxes must overlap.
 (X3) the LITERAL sum (13)  Xi_27 = sum_{n<=27} Phi_n  at 4400 bits (no zeta, no E-M, no identity (12)) vs the tail route
      at the H1 and H4 endpoints; boxes must overlap and have the same strict sign.
Usage: python3 crosscheck.py [X1] [X2] [X3]   (log: logs/crosscheck-<parts>.log; each point is logged when done)
"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ivc import *
from xin import *
import specfun

PARTS = sys.argv[1:] or ['X1', 'X2', 'X3']
LOGF = open(os.path.join(HERE, 'logs', 'crosscheck-%s.log' % ''.join(PARTS)), 'w')


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    LOGF.write(s + '\n')
    LOGF.flush()


def overlap(A, B):
    return not (hi(A.re) < lo(B.re) or hi(B.re) < lo(A.re) or hi(A.im) < lo(B.im) or hi(B.im) < lo(A.im))


T0 = time.time()
PTS = ['3144.8946', '3144.8947', '3145.5998', '3145.5999']
CX, CY = '3143.2206824215', '0.3152587994'
set_prec(200)
log('crosscheck.py  mpmath %s  backend %s' % (mp.__version__, mp.libmp.BACKEND))

log('\n(X1) Xi boxes vs mpmath ordinary functions (mp.prec = 400)')
mp.mp.prec = 400
for (x, y) in ([(p, '0') for p in PTS] + [(CX, CY)] if 'X1' in PARTS else []):
    B = Xi(point(x, y), 190)
    z = mp.mpc(mp.mpf(x), mp.mpf(y))
    s = mp.mpf('0.5') + 1j * z
    ref = s * (s - 1) / 2 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
    ok = lo(B.re) <= ref.real <= hi(B.re) and lo(B.im) <= ref.imag <= hi(B.im)
    log('  Xi(%s + %s i): box %s ; mpmath %s ; contained: %s' % (x, y, B.nstr(14), mp.nstr(ref, 14), ok))

log('\n(X2) h(w) at X = 784 pi, w in {s/2+2, (1-s)/2+2, s/2+1, (1-s)/2+1}, s = 1/2 + i c')
res = []
for bits, meth in ([(200, 'ibp'), (4400, 'lower')] if 'X2' in PARTS else []):
    set_prec(bits)
    z = point(CX, CY)
    s = s_of(z)
    X = iv.pi * 784
    half = R('0.5')
    ws = [s * half + 2, (1 - s) * half + 2, s * half + 1, (1 - s) * half + 1]
    t = time.time()
    if meth == 'ibp':
        hs = [specfun.h_ibp(w, X, 190) for w in ws]
    else:
        hs = [specfun.h_lower(w, X, bits - 40, Kmax=40000) for w in ws]   # relbits ~ prec: the lower sum cancels ~1e135
    res.append(hs)
    log('  %s (%d bits, %.1f s): %s' % (meth, bits, time.time() - t, '; '.join(h.nstr(12) for h in hs)))
if res:
    log('  overlap of the two routes for all four w: %s' % all(overlap(a, b) for a, b in zip(res[0], res[1])))
    log('  relative radius: ibp %s ; lower %s' % (', '.join(mp.nstr(h.rad() / abs(h.mid()), 3) for h in res[0]),
                                                 ', '.join(mp.nstr(h.rad() / abs(h.mid()), 3) for h in res[1])))
    log('  (4400 bits for the lower route: its recurrence u_k = u_(k-1) X/(w+k) rotates the box ~5000 times, and the wrapping of'
        ' rectangular complex boxes -- plus the ~1e135 cancellation -- must be absorbed by precision; at 1400 bits the box was useless)')

log('\n(X3) literal sum (13) at 4400 bits vs tail route at 200 bits')
set_prec(200)
tails = {x: XiN_tail(27, point(x), 190) for x in (PTS if 'X3' in PARTS else [])}
set_prec(4400)
for x in (PTS if 'X3' in PARTS else []):
    t = time.time()
    z = point(x)
    L = C(0)
    for n in range(1, 28):
        L = L + Phi(n, z, 4360)
        if n % 9 == 0:
            print('    ... n = %d done (%.0f s)' % (n, time.time() - t), flush=True)
    T = tails[x]
    sgnL = 1 if lo(L.re) > 0 else (-1 if hi(L.re) < 0 else 0)
    sgnT = 1 if lo(T.re) > 0 else (-1 if hi(T.re) < 0 else 0)
    log('  Xi_27(%s): literal %s  (%.0f s)' % (x, L.nstr(16), time.time() - t))
    log('  Xi_27(%s): tail    %s ;  overlap %s ; same strict sign %s' % (x, T.nstr(16), overlap(L, T), sgnL == sgnT != 0))
log('\ntotal %.0f s' % (time.time() - T0))
