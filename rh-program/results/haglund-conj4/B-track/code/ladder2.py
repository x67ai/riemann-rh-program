"""B-track ladder part 2: the certified facts of main.tex Theorem main (N = 27), and route T vs the literal sum."""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb
out = {}
def log(*a):
    print(*a); sys.stdout.flush()
# L5: route T (dps 30) against the literal sum (14) at dps 80, N = 1..4
L5 = []
for N in [1, 2, 3, 4]:
    for (x, y) in [(5, 0), (30, 0), (40, 3), (60, 25), (100, 10), (150, 60)]:
        mp.mp.dps = 80
        lit = hb.XiN_lit(N, mp.mpc(x, y))
        mp.mp.dps = 30
        T = hb.XiN(N, mp.mpc(x, y))
        mp.mp.dps = 80
        r = dict(N=N, z=[x, y], lit80=mp.nstr(lit, 12), rel_T30_vs_lit80=float(abs(T - lit)/abs(lit)))
        L5.append(r); log('L5', r)
out['L5'] = L5
# L3: sign change of Xi_27 on (3144.8946, 3144.8947); route T at dps 30 and 60
L3 = []
for dps in [30, 60]:
    mp.mp.dps = dps
    a = hb.XiN(27, mp.mpf('3144.8946')); b = hb.XiN(27, mp.mpf('3144.8947'))
    r = dict(dps=dps, at_8946=mp.nstr(a, 12), at_8947=mp.nstr(b, 12), sign_change=bool(a*b < 0))
    L3.append(r); log('L3', r)
    x1 = hb.bisect_real(lambda x: hb.XiN(27, x), mp.mpf('3144.8946'), mp.mpf('3144.8947'))
    x2 = hb.bisect_real(lambda x: hb.XiN(27, x), mp.mpf('3145.5998'), mp.mpf('3145.5999'))
    log('L3 zeros', dps, mp.nstr(x1, 20), mp.nstr(x2, 20)); L3.append(dict(dps=dps, x1=mp.nstr(x1, 20), x2=mp.nstr(x2, 20)))
out['L3'] = L3
# L4: the non-real zero of Xi_27 (Theorem main (b))
ref = mp.mpc('3143.220682421536585287281295989417800119', '0.315258799378214845382286373009271765')
L4 = []
for dps in [30, 60]:
    mp.mp.dps = dps
    z, st, it, d = hb.newton(lambda z: hb.XiN(27, z), mp.mpc('3143.2206824215', '0.3152587994'))
    mp.mp.dps = 60
    r = dict(dps=dps, z=mp.nstr(z, 25), dist_to_zstar=float(abs(z - ref)), newton_its=it)
    L4.append(r); log('L4', r)
out['L4'] = L4
json.dump(out, open('../data/ladder2.json', 'w'), indent=1)
log('saved L3-L5')
# L3-literal: the literal sum (13) at dps 1100 at the two endpoints (slow)
mp.mp.dps = 1100
t0 = time.time()
for x in ['3144.8946', '3144.8947']:
    v = mp.re(hb.XiN_lit(27, mp.mpf(x)))
    log('L3-literal dps1100', x, mp.nstr(v, 15), 'time %.0f s' % (time.time() - t0))
    out.setdefault('L3lit', []).append(dict(x=x, value=mp.nstr(v, 15)))
json.dump(out, open('../data/ladder2.json', 'w'), indent=1)
log('saved L3-literal')
