#!/usr/bin/env python3
"""d4_note_table.py -- D4: rebuild the note's section 6 (the per-height table) from out/zeta_t*_L*.json + out/control1_*.json
(Control 1 rows; Job 2's own replays under checker-O/out are used where the control1 JSON says so), in place between the markers
<!-- S6-TABLE-BEGIN --> and <!-- S6-TABLE-END --> of d4-sweep-note.md; and out/sweep_summary.json (counts, min W, delta_vis
ranges, wall, the silence intervals) for sections 7, 11, 12. Run after every landing; every number is read from a JSON, none typed."""
import json, glob, os, math, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..')); OUT = os.path.join(ROOT, 'out')
NOTE = os.path.join(ROOT, 'd4-sweep-note.md'); PT = 3000175332800
def now(): return subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
plan = json.load(open(os.path.join(HERE, 'sweep_plan.json')))
kof = {p['t_exact']: p['k'] for p in plan['tier1']}
rows = []
for pj in glob.glob(os.path.join(OUT, 'zeta_t*_L*.json')):
    if pj.endswith('.sidecar.json'): continue
    J = json.load(open(pj))
    if 'verdict' not in J or J.get('tier') == 'rehearsal' and float(J['t_exact']) < PT: pass
    t = J['t_exact']; L = J['L']; Lg = f"{L:g}"
    c1p = os.path.join(OUT, f"control1_t{t}_L{Lg}.json"); C = json.load(open(c1p)) if os.path.exists(c1p) else None
    if C is None:   # the rehearsal points replayed by Job 2 part A (checker-O/compare.json)
        for r in json.load(open(os.path.join(ROOT, 'checker-O', 'out', 'compare.json'))):
            if r['job1_source'].endswith(os.path.basename(pj)):
                C = dict(P_replay=r['P_checkerO'], W_replay=r['W_checkerO'], dP=r['dP'], dW=r['dW'], tolerance=r['tolerance'], PASS=r['PASS'], who="Job 2 part A (checker-O/compare.json)", replay_json=r['checkerO_json'], replay_wall_s=None)
    rows.append((float(t), t, L, J, C, pj))
rows.sort(key=lambda r: (r[2], r[0]))
def lab(t, L, J):
    if J.get('tier') == 'rehearsal': return 'rehearsal' if float(t) != 3000175332900 else 'PT edge'
    if t in kof: return f"k={kof[t]}"
    return 'control' if 'control' in (J.get('label') or '') else J.get('tier')
hdr = ("| # | t (exact double) | L | X | terms | P₁ (harness) | P₂ (twsumO) | ARCH | W₁ | W₂ | \\|W₁−W₂\\| | tol | phase line | budget | δ_vis [band ÷×1.837] | Control 2 planted / expected (rel) | DH | wall: sum s / replay s | hashes (JSON₁ / JSON₂) | verdict |\n"
       "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
lines = [hdr]; summ = {}
for tf, t, L, J, C, pj in rows:
    c2 = J['control2_zero_side']; dh = J['control2_coefficient_side_DH']; b = J['budget']
    rp = C['replay_json'] if C else None
    h2 = sha(os.path.join(ROOT, rp))[:8] if (rp and os.path.exists(os.path.join(ROOT, rp))) else (sha(os.path.join(ROOT, 'checker-O', rp))[:8] if rp and os.path.exists(os.path.join(ROOT, 'checker-O', rp)) else '—')
    lines.append(f"| {lab(t, L, J)} | {t} | {L:g} | {J['X']} | {J['n_terms']} | {J['P_dd']:+.15e} | {C['P_replay']:+.15e} | {J['ARCH']:.15e} | **{J['W']:+.15e}** | {C['W_replay']:+.15e} | {C['dW']:.1e} | {C['tolerance']:.2e} | {J['phase_line']:.2e} | {b['total']:.1e} | {J['delta_vis']:.4f} [{J['delta_vis_band_factor_1p5'][0]:.3f}, {J['delta_vis_band_factor_1p5'][1]:.3f}] | {c2['kernel_value']:.12e} / {c2['expected']:.12e} ({c2['rel_diff']:.1e}, {'PASS' if c2['pass_'] else 'FAIL'}) | {'FIRES' if dh.get('fires') else 'NO'}, {'PASS' if dh.get('pass') else 'FAIL'} | {J['time_sum_s']:.1f} / {(('%.0f' % C['replay_wall_s']) if C and C.get('replay_wall_s') else '—')} | {sha(pj)[:8]} / {h2} | {J['verdict']}{'' if C['PASS'] else ' — CONTROL 1 FAIL'} |"
                 if C else f"| {lab(t, L, J)} | {t} | {L:g} | {J['X']} | {J['n_terms']} | {J['P_dd']:+.15e} | (replay pending) | {J['ARCH']:.15e} | **{J['W']:+.15e}** | — | — | — | {J['phase_line']:.2e} | {b['total']:.1e} | {J['delta_vis']:.4f} | {c2['kernel_value']:.12e} / {c2['expected']:.12e} | {'FIRES' if dh.get('fires') else 'NO'} | {J['time_sum_s']:.1f} / — | {sha(pj)[:8]} / — | {J['verdict']} (Control 1 pending) |")
    key = f"L{L:g}"; S = summ.setdefault(key, dict(L=L, n=0, n_above_PT=0, min_W=None, min_W_t=None, max_W=None, dvis_min=None, dvis_max=None, t_min=None, t_max=None, sum_wall_s=0.0, replay_wall_s=0.0, all_silent=True, all_control1_pass=True, all_controls_pass=True, max_dW=0.0, max_phase_line=0.0, points=[]))
    S['n'] += 1; S['n_above_PT'] += int(tf > PT); S['sum_wall_s'] += J['time_sum_s'] or 0; S['replay_wall_s'] += (C.get('replay_wall_s') or 0) if C else 0
    S['all_silent'] &= J['verdict'] == 'silent (W > 0)'; S['all_controls_pass'] &= bool(J['controls_pass']); S['all_control1_pass'] &= bool(C and C['PASS'])
    if C: S['max_dW'] = max(S['max_dW'], C['dW'])
    S['max_phase_line'] = max(S['max_phase_line'], J['phase_line'])
    if S['min_W'] is None or J['W'] < S['min_W']: S['min_W'] = J['W']; S['min_W_t'] = t
    S['max_W'] = J['W'] if S['max_W'] is None else max(S['max_W'], J['W'])
    S['dvis_min'] = J['delta_vis'] if S['dvis_min'] is None else min(S['dvis_min'], J['delta_vis']); S['dvis_max'] = J['delta_vis'] if S['dvis_max'] is None else max(S['dvis_max'], J['delta_vis'])
    S['t_min'] = t if S['t_min'] is None or tf < float(S['t_min']) else S['t_min']; S['t_max'] = t if S['t_max'] is None or tf > float(S['t_max']) else S['t_max']
    S['points'].append(dict(t=t, W=J['W'], dvis=J['delta_vis'], verdict=J['verdict'], control1=(C['PASS'] if C else None)))
summ['date'] = now(); summ['n_total'] = len(rows)
json.dump(summ, open(os.path.join(OUT, 'sweep_summary.json'), 'w'), indent=1)
table = "\n".join(lines)
s = open(NOTE).read(); B = "<!-- S6-TABLE-BEGIN -->"; E = "<!-- S6-TABLE-END -->"
assert B in s and E in s, "markers missing in the note"
i0 = s.index(B) + len(B); i1 = s.index(E)
s = s[:i0] + f"\n*(regenerated {summ['date']} by `harness/d4_note_table.py` from the JSONs; {len(rows)} rows; every number read from `out/zeta_t*_L*.json`, `out/control1_*.json` or `checker-O/out/compare.json`.)*\n\n" + table + "\n" + s[i1:]
open(NOTE, 'w').write(s)
for k, S in summ.items():
    if k.startswith('L'): print(f"[{summ['date']}] {k}: {S['n']} points ({S['n_above_PT']} above PT), t {S['t_min']} .. {S['t_max']}, min W {S['min_W']:+.6e} at {S['min_W_t']}, max W {S['max_W']:+.4e}, dvis [{S['dvis_min']:.4f}, {S['dvis_max']:.4f}], all silent {S['all_silent']}, controls {S['all_controls_pass']}, control1 {S['all_control1_pass']} (max dW {S['max_dW']:.1e}), max line {S['max_phase_line']:.2e}, sum wall {S['sum_wall_s']:.0f} s, replay wall {S['replay_wall_s']:.0f} s")
