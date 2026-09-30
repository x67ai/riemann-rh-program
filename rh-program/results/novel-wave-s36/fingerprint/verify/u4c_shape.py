"""
u4c_shape.py -- does any simple monotonicity / convexity law hold for the zeta fingerprint (n <= 999)?
Counts violations of: al_{n+1} <= al_n; log-convexity al_n^2 <= al_{n-1} al_{n+1}; log-concavity; monotonicity of
A_n = 4 n sqrt(al_n) (increasing, as W(n/2pi) is); same for the J-fraction b_n^2 and the circle eps_n = 1 - |alpha_n|.
"""
import json, os, mpmath as mp
mp.mp.dps = 40
here = os.path.dirname(os.path.abspath(__file__)); tab = os.path.join(os.path.dirname(here), 'tables')
Z = json.load(open(os.path.join(tab, 'zeta_real_P24000_S1000.json')))
C = json.load(open(os.path.join(tab, 'zeta_circle_P24000_S1000.json')))
al = [mp.mpf(r['v']) for r in Z['al']]; b2 = [mp.mpf(r['v']) for r in Z['b2']]
eps = [1 - abs(mp.mpf(r['v'])) for r in C['alpha']]
def count(seq, name):
    N = len(seq)
    dec = [n for n in range(1, N) if not (seq[n] <= seq[n - 1])]
    lcx = [n for n in range(1, N - 1) if not (seq[n] ** 2 <= seq[n - 1] * seq[n + 1])]
    lcv = [n for n in range(1, N - 1) if not (seq[n] ** 2 >= seq[n - 1] * seq[n + 1])]
    print('%-10s N=%d  increases: %d (first %s)  log-convexity violations: %d  log-concavity violations: %d'
          % (name, N, len(dec), [d + 1 for d in dec[:6]], len(lcx), len(lcv)))
    return {'N': N, 'increases': len(dec), 'first_increases': [d + 1 for d in dec[:10]], 'logconvex_viol': len(lcx), 'logconcave_viol': len(lcv)}
out = {'al': count(al, 'al_n'), 'b2': count(b2, 'b_n^2'), 'eps': count(eps, 'eps_n')}
A = [4 * (n + 1) * mp.sqrt(al[n]) for n in range(len(al))]
decA = [n + 1 for n in range(1, len(A)) if A[n] < A[n - 1]]
print('A_n = 4n sqrt(al_n): decreases at %d of %d steps (first %s)' % (len(decA), len(A) - 1, decA[:8]))
out['A_decreases'] = len(decA)
json.dump(out, open(os.path.join(here, 'u4c_shape.json'), 'w'), indent=1)
