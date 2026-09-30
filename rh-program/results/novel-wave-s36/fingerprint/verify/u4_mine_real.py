"""
u4_mine_real.py -- mine the real-side table of zeta (S-fraction al_n of F(w) = sum_{gamma>0} 1/(gamma^2 - w)).

(1) first values; (2) WKB law al_n ~ L_n^2/(16 n^2), L_n = log(n/(2 pi L_n)) [derivation NOTE sec. 3];
(3) even/odd structure; (4) exact sum rule sum_n al_n = s_1; (5) smooth-model comparison: the same S-fraction for
the zero set t_k with N0(t_k) = k - 1/2 (N0 = theta/pi + 1), computed by the stable Stieltjes procedure (float64),
residual r_n = al_n(zeta)/al_n(model) - 1, and its periodogram against t_n (turning point) to look for log p lines.
"""
import sys, os, json
import numpy as np
import mpmath as mp
here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
mp.mp.dps = 40
R = json.load(open(os.path.join(tabdir, 'zeta_real_P24000_S1000.json')))
al = [mp.mpf(r['v']) for r in R['al']]
dig = [r['dig'] for r in R['al']]
s = [None] + [mp.mpf(r['s']['v']) if False else (mp.mpf(r['v']) if r else None) for r in R['s'][1:]]
logf = open(os.path.join(here, 'u4_mine_real.log'), 'w')
def say(*a):
    t = ' '.join(str(x) for x in a); print(t, flush=True); logf.write(t + '\n'); logf.flush()

say('certified digits range:', min(dig), '..', max(dig), ' count', len(al))
say('s_1..s_6 =', [mp.nstr(v, 20) for v in s[1:7]])
say('al_1..al_20:')
for n in range(1, 21):
    say('  al_%d = %s' % (n, mp.nstr(al[n - 1], 25)))
a_j = [mp.mpf(r['v']) for r in R['a']]; b2 = [mp.mpf(r['v']) for r in R['b2']]
say('J-fraction a_0..a_9 =', [mp.nstr(v, 12) for v in a_j[:10]])
say('J-fraction b_1^2..b_10^2 =', [mp.nstr(v, 12) for v in b2[:10]])

def Ln(n):
    # L e^L = n/(2 pi)  <=>  L = log(n/(2 pi L))
    return mp.re(mp.lambertw(mp.mpf(n) / (2 * mp.pi)))
say('\nWKB check: A_n := 4 n sqrt(al_n) versus L_n (predicted A_n -> L_n):')
rows = []
for n in (10, 20, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 998, 999):
    A = 4 * n * mp.sqrt(al[n - 1]); L = Ln(n)
    rows.append((n, A, L))
    say('  n=%4d  A_n=%.10f  L_n=%.10f  A_n-L_n=%+.6f  A_n/L_n=%.6f' % (n, A, L, A - L, A / L))
# smoothed (average of neighbors to kill even/odd modulation)
say('\neven/odd: al_{n+1}/al_n at n = 1..12:', [mp.nstr(al[n] / al[n - 1], 8) for n in range(1, 13)])
say('ratio al_{2k}/al_{2k-1} and al_{2k+1}/al_{2k} at k = 100, 250, 450:',
    [(k, mp.nstr(al[2 * k - 1] / al[2 * k - 2], 10), mp.nstr(al[2 * k] / al[2 * k - 1], 10)) for k in (100, 250, 450)])
# sum rule
Sfin = mp.fsum(al)
tail = mp.fsum(Ln(n) ** 2 / (16 * n * n) for n in range(1000, 200000)) + Ln(200000) ** 2 / (16 * 200000)
say('\nsum rule: sum_{n<=999} al_n = %s ; + WKB tail (n>=1000) ~ %s ; total %s ; s_1 = %s'
    % (mp.nstr(Sfin, 15), mp.nstr(tail, 6), mp.nstr(Sfin + tail, 12), mp.nstr(s[1], 15)))

# fit A_n = L_n + c0 + c1/log n + oscillation?
ns = np.arange(50, 1000)
A = np.array([float(4 * n * mp.sqrt(al[n - 1])) for n in ns])
L = np.array([float(Ln(int(n))) for n in ns])
d = A - L
say('\nA_n - L_n: mean over n in [50,999] = %.6f, over [500,999] = %.6f, std [500,999] = %.6f'
    % (d.mean(), d[450:].mean(), d[450:].std()))
# even/odd split
de = d[(ns % 2) == 0]; do = d[(ns % 2) == 1]
say('   even n mean %.6f, odd n mean %.6f (n in [50,999])' % (de.mean(), do.mean()))
json.dump({'wkb_rows': [(n, float(A_), float(L_)) for n, A_, L_ in rows],
           'A_minus_L_mean_500_999': float(d[450:].mean())}, open(os.path.join(here, 'u4_mine_real.json'), 'w'), indent=1)
