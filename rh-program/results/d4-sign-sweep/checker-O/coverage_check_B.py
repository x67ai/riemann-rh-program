#!/usr/bin/env python3
"""D4 Job 2 part C.3 (Opus 5): the part-A coverage check extended to the landed sweep. The fourteen windows re-derived from the
page (Gourdon 2004 sect. 4.3.1 table; Odlyzko 1992 Table 1.2 (PDF p. 140) with p. 5's reading rule, last = first + count - 1;
Odlyzko 2001 p. 3), heights of zero #n by inverting the R-vM main term (mpmath, 40 digits); (a) every one of the 129 LANDED
heights (from out/zeta_*.json) against every window, unpadded and padded by 1000 spacings, with its margin in spacings; (b) the
covered measure and fraction of [PT, 1e20] (union of the unpadded windows, and of Job 1's plan windows); (c) the two controls'
containment. Log: logs/coverage_check_B_run.log; out/coverage_check_B.json."""
import json, os, glob, mpmath as mp
mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O = os.path.join(ROOT, 'out')
def T_of(n):
    n = mp.mpf(n); f = lambda T: T / (2 * mp.pi) * mp.log(T / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8 - n
    return mp.findroot(f, 2 * mp.pi * n / mp.log(n))
def sp(T): return 2 * mp.pi / mp.log(T / (2 * mp.pi))
W = []
for e, a, b in [(14, 3, 2 * 10**9), (15, 0, 2 * 10**9 - 1), (16, 1, 2 * 10**9 - 1), (17, 0, 2 * 10**9), (18, 1, 2 * 10**9 - 1), (19, 0, 2 * 10**9 + 1), (20, 4, 2 * 10**9 - 1)]:
    W.append(('Gourdon 2004 #1e%d+%d..+%d' % (e, a, b), 10**e + a, 10**e + b))
for N, cnt, off in [(10**14, 1685452, -736), (10**16, 16480973, -5946), (10**18, 16671047, -8839), (10**19, 16749725, -13607), (10**20, 175587726, -30769710), (2 * 10**20, 101305325, -633984)]:
    W.append(('Odlyzko 1992 T1.2 N=%g: N%+d..N%+d' % (N, off, off + cnt - 1), N + off, N + off + cnt - 1))
W.append(('Odlyzko 2001 p.3 #13048994265258476 +1006374896', 13048994265258476, 13048994265258476 + 1006374896 - 1))
PT = mp.mpf(3000175332800); TOP = mp.mpf(10)**20
win = []
for name, n1, n2 in W:
    t1, t2 = T_of(n1), T_of(n2); win.append(dict(src=name, t1=t1, t2=t2, pad=1000 * sp(t1)))
print('the 14 windows (unpadded R-vM heights):')
for w in win: print(f"  {w['src']:<52} [{mp.nstr(w['t1'], 15)}, {mp.nstr(w['t2'], 15)}] width {mp.nstr(w['t2'] - w['t1'], 4)}")
print('Odlyzko 1992 last-zero offsets (first + count - 1):', [w['src'].split(': ')[1] for w in win if 'T1.2' in w['src']])
# (b) measure
def union_len(iv):
    iv = sorted((max(a, PT), min(b, TOP)) for a, b in iv if b > PT and a < TOP); tot = 0; cur = None
    for a, b in iv:
        if cur is None or a > cur[1]: 
            if cur: tot += cur[1] - cur[0]
            cur = [a, b]
        else: cur[1] = max(cur[1], b)
    if cur: tot += cur[1] - cur[0]
    return tot
m_mine = union_len([(w['t1'], w['t2']) for w in win]); m_pad = union_len([(w['t1'] - w['pad'], w['t2'] + w['pad']) for w in win])
plan = json.load(open(os.path.join(ROOT, 'harness', 'sweep_plan.json')))
m_plan = union_len([(mp.mpf(w['t_lo']), mp.mpf(w['t_hi'])) for w in plan['covered_windows']])
rng = TOP - PT
print(f'covered measure in [PT, 1e20]: mine unpadded {mp.nstr(m_mine, 6)} (fraction {mp.nstr(m_mine / rng, 4)}); mine padded by 1000 spacings {mp.nstr(m_pad, 6)} ({mp.nstr(m_pad / rng, 4)}); Job 1 plan windows {mp.nstr(m_plan, 6)} ({mp.nstr(m_plan / rng, 4)}); plan states {plan["covered_measure_in_t"]:.6e} ({plan["covered_fraction"]:.4e})')
print('plan windows vs mine (t_lo diff, t_hi diff):')
for w, pw in zip(sorted(win, key=lambda w: w['t1']), sorted(plan['covered_windows'], key=lambda w: w['t_lo'])):
    print(f"  {w['src'][:30]:<30} | plan {pw['zeros'][:44]:<44} | dlo {mp.nstr(mp.mpf(pw['t_lo']) - w['t1'], 4)} dhi {mp.nstr(mp.mpf(pw['t_hi']) - w['t2'], 4)}")
# (a) the landed heights
Z = [json.load(open(p)) for p in glob.glob(os.path.join(O, 'zeta_t*_L*.json')) if not p.endswith('.sidecar.json')]
sw = [J for J in Z if not (J.get('tier') == 'rehearsal' and int(J['t_exact']) != 3000175332900)]
ctrl = {'15202440115920748544', '2513274122900000'}
hits = []; margins = []
for J in sw:
    t = mp.mpf(J['t_exact'])
    ins = [w['src'] for w in win if w['t1'] - w['pad'] <= t <= w['t2'] + w['pad']]
    if J['t_exact'] in ctrl: continue
    if ins: hits.append((J['t_exact'], J['L'], ins))
    d = min(min(abs(t - w['t1']), abs(t - w['t2'])) / sp(t) for w in win)
    margins.append((d, J['t_exact'], J['L']))
margins.sort()
print(f'landed sweep points {len(sw)}; non-control points {len(sw) - sum(J["t_exact"] in ctrl for J in sw)}; inside any padded window: {hits}')
print('the three closest non-control heights to any window edge (in mean spacings):', [(mp.nstr(d, 4), t, L) for d, t, L in margins[:3]])
# (c) controls
z20 = mp.mpf('15202440115920747268.629029')
c = mp.mpf(15202440115920748544); c2 = mp.mpf(2513274122900000); s01 = T_of(13048994265258476); e01 = T_of(13048994265258476 + 1006374896 - 1)
print(f'control 15202440115920748544: {mp.nstr((c - z20) / sp(c), 6)} mean spacings above the page value of zero #1e20 -> zero #1e20 + {int(mp.nint((c - z20) / sp(c)))} inside [#1e20 - 30769710, #1e20 + 144818015] and [#1e20 + 4, #1e20 + 2e9 - 1]: {-30769710 <= (c - z20) / sp(c) <= 144818015 and 4 <= (c - z20) / sp(c) <= 2e9 - 1}')
print(f'control 2513274122900000: {mp.nstr(c2 - s01, 6)} in t above the R-vM start of Odlyzko 2001 ({mp.nstr((c2 - s01) / sp(c2), 5)} zeros); above the page start 2.51327412288e15 by {mp.nstr(c2 - mp.mpf("2.51327412288e15"), 5)}; below the window end by {mp.nstr(e01 - c2, 5)} in t')
json.dump(dict(windows=[dict(src=w['src'], t1=str(w['t1']), t2=str(w['t2'])) for w in win], measure_mine=str(m_mine), measure_plan=str(m_plan), hits=hits, closest=[(str(d), t, L) for d, t, L in margins[:5]]), open(os.path.join(HERE, 'out', 'coverage_check_B.json'), 'w'), indent=1)
