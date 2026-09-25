#!/usr/bin/env python3
"""Print the part-B replay table from checker-O/out/replayOB_cmp_*.json (markdown). Log: logs/replayOB_table_run.log."""
import json, os, glob
HERE = os.path.dirname(os.path.abspath(__file__))
rows = [json.load(open(p)) for p in glob.glob(os.path.join(HERE, 'out', 'replayOB_cmp_*.json'))]
rows.sort(key=lambda r: (r['L'], int(r['t_exact'])))
print('| t | L | terms (same as Job 1?) | wall s (thr) | W_O (own launch) | \\|ΔW\\| vs Job 1 harness | \\|ΔW\\| vs earlier replayO | bit-identical to replayO (W; P hi+lo; ARCH) | tol | CPU_Speed_Limit | verdict |')
print('|---|---|---|---|---|---|---|---|---|---|---|')
for r in rows:
    print(f"| {r['t_exact']} | {r['L']:g} | {r['n_terms_OB']} ({'same' if r['n_terms_OB']==r['n_terms_job1']==r['n_terms_replayO'] else 'DIFFER'}) | {r['wall_s']:.0f} ({r['threads']}) | {r['W_OB']:+.17e} | {r['dW_vs_job1']:.2e} | {r['dW_vs_replayO']:.2e} | {r['bit_identical_W_vs_replayO']}; {r['bit_identical_P_vs_replayO']}; {r['ARCH_identical_vs_replayO']} | {r['tolerance']:.2e} | {r['cpu_speed_limit_pre']}/{r['cpu_speed_limit_post']} | {'PASS' if r['PASS'] else 'FAIL'} |")
for L in sorted(set(r['L'] for r in rows)):
    rs = [r for r in rows if r['L'] == L]
    w = max(rs, key=lambda r: r['dW_vs_job1']); wo = max(rs, key=lambda r: r['dW_vs_replayO'])
    print(f"L = {L:g}: {len(rs)} points; PASS {sum(r['PASS'] for r in rs)}; worst |dW| vs Job 1 {w['dW_vs_job1']:.3e} at t = {w['t_exact']} (tol there {w['tolerance']:.3e}, ratio {w['dW_vs_job1']/w['tolerance']:.1e}); worst |dW| vs replayO {wo['dW_vs_replayO']:.3e} at t = {wo['t_exact']}; bit-identical W {sum(r['bit_identical_W_vs_replayO'] for r in rs)}/{len(rs)}; max ratio dW/(line) where line>0 {max(r['dW_vs_job1']/r['phase_line_eps_proven_l1_job1'] for r in rs):.2e}")
print(f"ALL: {len(rows)} points, FAIL {sum(not r['PASS'] for r in rows)}; worst |dW| vs Job 1 {max(r['dW_vs_job1'] for r in rows):.3e}")
