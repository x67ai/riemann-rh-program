"""
u5_inject.py -- visibility pricing (zoo IV.9) for the real-side fingerprint: add ONE off-line quadruple
{±T ± i delta} (in t; s = 1/2 ± delta + iT and conjugates) to zeta's zero set, i.e. E -> E (1 - w/z)(1 - w/zbar),
z = (T + i delta)^2, so c_m -> c_m + 2 Re z^{-(m+1)} exactly.  Report the first S-index n_fail with al_n < 0
(certified) and the deviation profile |al_n^inj / al_n - 1| (announcement: how early the failure is visible).

Usage: python3 u5_inject.py FUNC P M  T1,d1  T2,d2 ...
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, acb, arb_series, ctx
import mpmath as mp
import fp_core as fc
import fp_moments as fm

FUNC = sys.argv[1]; P = int(sys.argv[2]); M = int(sys.argv[3])
pairs = [tuple(a.split(',')) for a in sys.argv[4:]]
here = os.path.dirname(os.path.abspath(__file__))
logf = open(os.path.join(here, 'u5_inject.log'), 'a')
def say(*a):
    t = ' '.join(str(x) for x in a); print(t, flush=True); logf.write(t + '\n'); logf.flush()

t0 = time.time()
cm = fm.real_moments(FUNC, P, M)
ctx.prec = P
base = fc.sfrac_from_series(cm, M - 1, stop_on_zero=True) if False else None
tabfile = os.path.join(os.path.dirname(here), 'tables', 'zeta_real_P24000_S1000.json')
ref = [mp.mpf(r['v']) for r in json.load(open(tabfile))['al']] if FUNC == 'zeta' else None
say('--- %s P=%d M=%d moments ready %.1fs' % (FUNC, P, M, time.time() - t0))
mp.mp.dps = 70

def sfrac_until_fail(c, extra=6):
    """Viskovatov with early exit 'extra' steps after the first certified-negative coefficient."""
    L = len(c); ctx.cap = L
    F = arb_series([x / c[0] for x in c]); al = []; cur = L; nfail = None
    for n in range(1, L):
        ctx.cap = cur
        g = (1 - 1 / F).coeffs()
        if len(g) < 2:
            break
        a = g[1]; al.append(a)
        if a.contains(0):
            break
        if a < 0 and nfail is None:
            nfail = n
        if nfail is not None and n >= nfail + extra:
            break
        newc = [x / a for x in g[1:cur]]; cur -= 1; ctx.cap = cur
        F = arb_series(newc)
    return al, nfail

results = []
for Ts, ds in pairs:
    t1 = time.time()
    T = arb(Ts); d = arb(ds)
    z = acb(T, d) ** 2
    zi = 1 / z
    add = []
    p = zi
    for m in range(M):
        add.append(2 * p.real)
        p = p * zi
    c2 = [cm[m] + add[m] for m in range(M)]
    al, nfail = sfrac_until_fail(c2)
    prof = {}
    if ref is not None:
        thresholds = [1e-50, 1e-30, 1e-20, 1e-10, 1e-5, 1e-3, 1e-1]
        for th in thresholds:
            k = next((n for n in range(1, len(al) + 1)
                      if abs(mp.mpf(al[n - 1].str(66, radius=False)) / ref[n - 1] - 1) > th), None)
            prof['%.0e' % th] = k
    lastdig = fc.digits(al[-1]) if al else None
    rec = {'T': Ts, 'delta': ds, 'n_fail': nfail, 'n_computed': len(al), 'digits_at_last': lastdig,
           'first_n_with_rel_dev_above': prof, 'secs': round(time.time() - t1, 1)}
    if nfail:
        rec['al_around_fail'] = [al[n - 1].str(8, radius=False) for n in range(max(1, nfail - 3), min(len(al), nfail + 3) + 1)]
    say(json.dumps(rec))
    results.append(rec)
json.dump(results, open(os.path.join(here, 'u5_inject_%s_%d.json' % (FUNC, int(time.time()))), 'w'), indent=1)
