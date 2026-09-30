"""
u5d_inject_table.py -- visibility table from the injection runs: n_fail(T, delta) versus the WKB index
n_WKB(T) = first n with t_n = 1/(2 sqrt al_n(zeta)) >= T, and versus pi*N(T) (N = Riemann-von Mangoldt count).
"""
import json, os, re, glob, mpmath as mp
here = os.path.dirname(os.path.abspath(__file__)); tab = os.path.join(os.path.dirname(here), 'tables')
mp.mp.dps = 30
Z = json.load(open(os.path.join(tab, 'zeta_real_P24000_S1000.json')))
al = [mp.mpf(r['v']) for r in Z['al']]
tn = [1 / (2 * mp.sqrt(a)) for a in al]
rows = []
for f in sorted(glob.glob(os.path.join(here, 'run_inject_*.out'))):
    for line in open(f):
        if line.startswith('{'):
            r = json.loads(line)
            T = mp.mpf(r['T'])
            nw = next((n for n, t in enumerate(tn, 1) if t >= T), None)
            NT = mp.re(mp.siegeltheta(T)) / mp.pi + 1
            rows.append({'T': r['T'], 'delta': r['delta'], 'n_fail': r['n_fail'], 'J_fail': (r['n_fail'] + 1) // 2 if r['n_fail'] else None,
                         'n_WKB': nw, 'lag': (r['n_fail'] - nw) if (r['n_fail'] and nw) else None,
                         'pi_N(T)': float(mp.pi * NT), 'digits_left': r['digits_at_last']})
print('%6s %7s %7s %6s %6s %5s %8s %7s' % ('T', 'delta', 'n_fail', 'J', 'n_WKB', 'lag', 'piN(T)', 'digits'))
for r in rows:
    print('%6s %7s %7s %6s %6s %5s %8.1f %7s' % (r['T'], r['delta'], r['n_fail'], r['J_fail'], r['n_WKB'], r['lag'], r['pi_N(T)'], r['digits_left']))
json.dump(rows, open(os.path.join(here, 'u5d_inject_table.json'), 'w'), indent=1)
