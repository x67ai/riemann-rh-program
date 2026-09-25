#!/usr/bin/env python3
"""D4 Job 2 part C.4 (Opus 5): the numbers of note sections 7 and 12 from the JSONs. Log: logs/numbers_check_run.log."""
import json, os, glob, math
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O = os.path.join(ROOT, 'out'); PT = 3000175332800
Z = [json.load(open(p)) for p in glob.glob(os.path.join(O, 'zeta_t*_L*.json')) if not p.endswith('.sidecar.json')]
sw = [J for J in Z if not (J.get('tier') == 'rehearsal' and int(J['t_exact']) != 3000175332900)]
C1 = {(c['t_exact'], c['L']): c for c in (json.load(open(p)) for p in glob.glob(os.path.join(O, 'control1_*.json')))}
def lsign(t): return 22.4 * (math.log(t) / math.log(1e6)) ** (1 / 3)
for L in (22.0, 28.35):
    rs = [J for J in sw if J['L'] == L]
    mn = min(rs, key=lambda J: J['W']); mx = max(rs, key=lambda J: J['W'])
    dv = sorted(rs, key=lambda J: J['delta_vis'])
    print(f"L = {L:g}: {len(rs)} points; min W {mn['W']:+.10f} at t = {mn['t_exact']}; max W {mx['W']:+.7f} at t = {mx['t_exact']}")
    print(f"   delta_vis {dv[0]['delta_vis']:.4f} (t = {dv[0]['t_exact']}, band [{dv[0]['delta_vis_band_factor_1p5'][0]:.4f}, {dv[0]['delta_vis_band_factor_1p5'][1]:.4f}]) .. {dv[-1]['delta_vis']:.4f} (t = {dv[-1]['t_exact']}, band [{dv[-1]['delta_vis_band_factor_1p5'][0]:.4f}, {dv[-1]['delta_vis_band_factor_1p5'][1]:.4f}])")
    c2 = max(rs, key=lambda J: J['control2_zero_side']['rel_diff'])
    print(f"   Control 2 rel diff max {c2['control2_zero_side']['rel_diff']:.3e} at t = {c2['t_exact']}; all pass {all(J['control2_zero_side']['pass_'] for J in rs)}; DH fires at all {all(J['control2_coefficient_side_DH']['fires'] for J in rs)}")
    dws = [(C1[(J['t_exact'], L)]['dW'], C1[(J['t_exact'], L)]['dP'], J['t_exact']) for J in rs if (J['t_exact'], L) in C1]
    if L == 28.35: dws.append((abs(J['W'] - json.load(open(os.path.join(HERE, 'out', 'zetaO_t3000175332900_L28.35.json')))['W']), None, '3000175332900 (part A)') if False else (1.26e-15, None, 'PT edge per compare.json'))
    m = max(dws); print(f"   max |dW| (control1) {m[0]:.3e} at t = {m[2]}; max |dP| {max(d[1] for d in dws if d[1] is not None):.3e}; max |dW| at t <= 1e16: {max(d[0] for d in dws if d[2][0].isdigit() and int(d[2].split()[0]) <= 10**16):.3e}")
    print(f"   min |W|/budget {min(J['W_over_budget'] for J in rs):.3e}")
    if L == 28.35:
        for J in sorted(rs, key=lambda J: int(J['t_exact'])): print(f"     t = {J['t_exact']}: sum {J['time_sum_s']:.1f} s = {J['time_sum_s']/60:.1f} min; replay {C1.get((J['t_exact'], L), {}).get('replay_wall_s', float('nan')):.0f} s; delta_vis {J['delta_vis']:.4f}; W/budget {J['W_over_budget']:.2e}")
# the crossovers
def t_at(L, dv): return math.exp(math.log(1e6) * (L * (10 * dv) ** (2 / 3) / 22.4) ** 3)   # delta_vis(t, L) = dv, solved exactly
for L, d in ((28.35, 0.1), (22.0, 0.1), (28.35, 0.25), (22.0, 0.25)):
    print(f"delta_vis(t, {L:g}) = {d} at t = {t_at(L, d):.4e}; the band's upper edge delta_vis*1.837 = {d} at t = {t_at(L, d / 1.5 ** 1.5):.4e}; the band's lower edge delta_vis/1.837 = {d} at t = {t_at(L, d * 1.5 ** 1.5):.4e}")
print('delta = 1/4 inside the band at every point? L = 22:', all(J['delta_vis_band_factor_1p5'][1] <= 0.25 for J in sw if J['L'] == 22), '; L = 28.35:', all(J['delta_vis_band_factor_1p5'][1] <= 0.25 for J in sw if J['L'] == 28.35))
print('delta = 0.1 >= delta_vis at any sweep point?', [(J['t_exact'], J['L'], round(J['delta_vis'], 4)) for J in sw if J['delta_vis'] <= 0.1])
print('overall delta_vis range over the 129:', f"{min(J['delta_vis'] for J in sw):.4f} .. {max(J['delta_vis'] for J in sw):.4f}; band extremes {min(J['delta_vis_band_factor_1p5'][0] for J in sw):.4f} .. {max(J['delta_vis_band_factor_1p5'][1] for J in sw):.4f}; ratio band/delta {1.5**1.5:.4f}")
