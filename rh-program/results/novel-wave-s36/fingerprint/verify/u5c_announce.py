"""
u5c_announce.py -- how does a failure announce itself?  Compare zeta + off-line quadruple (T +- i delta) with
zeta + the on-line DOUBLE zero at T (delta = 0: the configuration it collapses to), so that only the 'off-line-ness'
differs (an injected pair ADDS zeros, so comparing with plain zeta would mostly measure the added mass).
D_n := |al_n(off)/al_n(on) - 1| as a function of n, up to and past the first negative al_n(off).
Also: same height, on-line pair split to T +- delta (the 'real-epsilon' mimic of an imaginary splitting).
"""
import sys, os, json, time
sys.path.insert(0, os.path.dirname(__file__))
from flint import arb, acb, arb_series, ctx
import mpmath as mp
import fp_core as fc
import fp_moments as fm
here = os.path.dirname(os.path.abspath(__file__))
P, M = 24000, 1000
cm = fm.real_moments('zeta', P, M)
ctx.prec = P

def sfrac_n(c, nmax):
    L = len(c); ctx.cap = L
    F = arb_series([x / c[0] for x in c]); al = []; cur = L
    for n in range(1, nmax + 1):
        ctx.cap = cur
        g = (1 - 1 / F).coeffs(); a = g[1]; al.append(a)
        if a.contains(0):
            break
        newc = [x / a for x in g[1:cur]]; cur -= 1; ctx.cap = cur; F = arb_series(newc)
    return al

def inject(zlist):
    """zlist: list of complex w-zeros (as acb); returns moments with sum_z z^{-(m+1)} added (real part)."""
    c2 = list(cm)
    for z in zlist:
        zi = 1 / z; p = zi
        for m in range(M):
            c2[m] = c2[m] + p.real
            p = p * zi
    return c2

out = {}
for (Ts, ds, nmax) in [('85.699348485377592', '0.308517182456637', 200), ('40', '0.1', 120)]:
    T = arb(Ts); d = arb(ds)
    zoff = acb(T, d) ** 2
    off = sfrac_n(inject([zoff, zoff.conjugate()]), nmax)
    on2 = sfrac_n(inject([acb(T * T), acb(T * T)]), nmax)
    spl = sfrac_n(inject([acb((T - d) ** 2), acb((T + d) ** 2)]), nmax)
    nf = next((n for n, a in enumerate(off, 1) if a < 0), None)
    rows = []
    mp.mp.dps = 50
    for n in range(1, min(len(off), len(on2), len(spl)) + 1):
        a_off = mp.mpf(off[n - 1].str(60, radius=False)); a_on = mp.mpf(on2[n - 1].str(60, radius=False))
        a_sp = mp.mpf(spl[n - 1].str(60, radius=False))
        rows.append((n, float(abs(a_off / a_on - 1)) if a_on != 0 else None, float(abs(a_sp / a_on - 1))))
    print('T = %s, delta = %s: first negative al_n (off-line) at n = %s' % (Ts, ds, nf))
    for (n, dv, ds_) in rows:
        if n in (1, 2, 5, 10, 20, 40, 60, 80, 100, 120, 130, 140, 145, 146, 147, 148, 149, 150, 160, 180, 200) or (nf and abs(n - nf) <= 2):
            print('   n=%4d  |al(off)/al(on-double)-1| = %.3e   |al(on-split T+-delta)/al(on-double)-1| = %.3e' % (n, dv, ds_))
    out['%s,%s' % (Ts, ds)] = {'n_fail': nf, 'rows': rows}
json.dump(out, open(os.path.join(here, 'u5c_announce.json'), 'w'), indent=1)
