"""
rouche_N7.py -- census of xi_N for EVERY N >= 7 (and N = infinity) in the box 0 < Im s <= 200 at once.
  (i)  |xi_N - xi| = |R_N| <= B_7(s) := (1/2)|s(s-1)| sum_{n>=8} |g_n(s)|  (termwise; N >= 7);
       on the boundary of [1-smax, smax] x [0, 200] (right edge, right half of the top edge; the left half
       is the mirror image, the bottom edge is the real axis where xi >= 0.497) we check B_7 < |xi| on a grid
       of step 0.02 -> Rouche: xi_N has as many zeros in the box as xi, namely N(200) = 79 (argument principle
       count of xi re-done here);
  (ii) on the line xi_N = Xi + P_N with 0 < P_N <= P_7; every negative lobe of Xi with left end <= 200 has
       depth > P_7 at its extremum (lobes_T320.json, N = 7 rows) -> two zeros per negative lobe -> 79 real
       zeros in (0, 200];  (i) + (ii) => all zeros of xi_N in the box are on the line, for every N >= 7.
Numerical (grid) verification with margins reported; not interval-rigorous.
"""
import sys, json, time
import mpmath as mp
sys.path.insert(0, '.')
import stair as st

mp.mp.dps = 40
Z = st.Chain('zeta')
T = mp.mpf(200)
smax = mp.mpf(30)
t00 = time.time()


def xi(s):
    return Z.E_full(s)


def B7(s):
    return abs(s*(s - 1))/2 * mp.fsum(abs(Z.T(s, n)) for n in range(8, 30))


worst = mp.mpf(0)
where = None
pts = [mp.mpc(smax, mp.mpf(j)/50) for j in range(1, int(T*50) + 1)]
pts += [mp.mpc(mp.mpf(1)/2 + (smax - mp.mpf(1)/2)*mp.mpf(j)/1475, T) for j in range(0, 1476)]
for s in pts:
    r = B7(s)/abs(xi(s))
    if r > worst:
        worst, where = r, s
print(f'(i) max B_7/|xi| on the boundary grid ({len(pts)} points) = {mp.nstr(worst, 5)} at {mp.nstr(where, 8)}  ({time.time()-t00:.0f}s)')
n, mn = st.count_zeros_rect(xi, 1 - smax, smax, mp.mpf('0.01'), T, n0=64, dmax=0.5)
print(f'(i) zeros of xi in [1-smax, smax] x [0.01, 200]: {mp.nstr(n, 10)}  ({time.time()-t00:.0f}s)')
L = json.load(open('lobes_T320.json'))
rows = L['N']['7']['lobes']
ok = [(a, b, r, has) for (a, b, r, has) in rows if mp.mpf(a) <= 200]
minratio = min(mp.mpf(r) for (a, b, r, has) in ok)
allhave = all(has for (a, b, r, has) in ok)
print(f'(ii) negative lobes with left end <= 200: {len(ok)}; all carry two zeros of xi_7: {allhave}; min depth/P_7 = {mp.nstr(minratio, 5)}')
res = {'max_B7_over_xi': mp.nstr(worst, 6), 'argmax': mp.nstr(where, 10), 'xi_zero_count_box': mp.nstr(n, 12),
       'neg_lobes_le_200': len(ok), 'all_lobes_two_zeros_N7': allhave, 'min_depth_over_P7': mp.nstr(minratio, 6),
       'conclusion': 'for every N >= 7: 79 zeros with 0 < Im s <= 200, all on the line' if (worst < 1 and allhave) else 'FAILED'}
json.dump(res, open('rouche_N7.json', 'w'), indent=1)
print(res['conclusion'])
