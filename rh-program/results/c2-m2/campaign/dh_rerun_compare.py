#!/usr/bin/env python3
"""dh_rerun_compare.py -- Session 23 item 0(c) (DH-RERUN-BRIEF.md): side-by-side tables RECORD / RE-RUN / relative for the DH
control rows of the three re-run scripts, the cancellation identity W_Z - W_Z' = W(orbit) checked both ways, the x6.24 ratio at L*,
the on-line-zero displacements, and the brief's three stop conditions.  Reads only; writes dh_rerun_compare.log beside this file.
  1. verify/dh_negative_control_out.json (record)            vs verify/dh_negative_control_rerun_out.json
  2. logs/dh_offline_scan.log, the record's own control stage (its rows survive only in the log at %.6e / 4 digits; the JSON's
     control_rows were overwritten by dh_control_new_heights.py)  vs dh_offline_scan_rerun.json (and, cross-check, vs 3.'s re-run)
  3. dh_offline_scan.json control_rows (record, full double)  vs dh_control_new_heights_rerun.json
"""
import json, os, re, math, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); V = os.path.join(HERE, '..', 'verify')
L = []
def p(s=''): print(s); L.append(s)
def rel(a, b):
    return (b - a)/a if a != 0 else (0.0 if b == 0 else float('inf'))
def fmt(x, d=10):
    return ('%.' + str(d) + 'e') % x
def sha(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()
STOP = []
# ------------------------------------------------------------------------------------------------ 1. dh_negative_control
rec = json.load(open(os.path.join(V, 'dh_negative_control_out.json')))
run = json.load(open(os.path.join(V, 'dh_negative_control_rerun_out.json')))
p("=" * 140)
p("1. verify/dh_negative_control.py (record, 2026-09-16 18:23) vs dh_negative_control_rerun.py (re-run, refinement on S(u) at 40 digits); t = %r (record) / %r (re-run), delta = %r / %r, L* = %r / %r" % (rec['t'], run['t'], rec['delta'], run['delta'], rec['L_star'], run['L_star']))
zr, zn = rec['dh_online_zeros_window'], run['dh_online_zeros_window']
p("   on-line zeros in +-30: %d recorded, %d re-run; displacements re-run - recorded: min |d| = %.3e, max |d| = %.3e (at u = %.6f); re-run max |f_DH(1/2+i gamma)| = %.2e, max |S| = %.2e"
  % (len(zr), len(zn), min(abs(a - b) for a, b in zip(zr, zn)), max(abs(a - b) for a, b in zip(zr, zn)), zr[max(range(len(zr)), key=lambda i: abs(zr[i] - zn[i]))], run['dh_online_max_abs_f'], run['dh_online_max_abs_S']))
if len(zr) != len(zn): STOP.append("script 1: on-line zero count changed %d -> %d" % (len(zr), len(zn)))
if run['dh_online_max_abs_f'] > 1e-25: STOP.append("script 1: max |f_DH| = %.2e > 1e-25" % run['dh_online_max_abs_f'])
p("   phase count %r / %r;  reflected direct L20 %r / %r;  reflected bound L* %r / %r" % (rec['phase_count_window'], run['phase_count_window'], rec['reflected_online_direct_L20'], run['reflected_online_direct_L20'], rec['reflected_online_bound_Lstar'], run['reflected_online_bound_Lstar']))
p()
p("| L | W_Z' recorded | W_Z' re-run | relative | W_Z recorded | W_Z re-run | W_Z - W_Z' recorded | W_Z - W_Z' re-run | rel. diff of the difference | ratio rec | ratio re-run | rel | fires rec / re-run |")
p("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
mx1 = 0.0; mxid = 0.0; mxsep = 0.0
for a, b in zip(rec['rows'], run['rows']):
    assert abs(a['L'] - b['L']) < 1e-12
    r1 = rel(a['W_Zprime'], b['W_Zprime']); mx1 = max(mx1, abs(r1))
    da = a['W_Z'] - a['W_Zprime']; db = b['W_Z'] - b['W_Zprime']; rid = rel(da, db); mxid = max(mxid, abs(rid))
    rs = max(abs(rel(a['separation'], b['separation'])), abs(rel(a['ratio'], b['ratio'])), abs(rel(a['bound_clause6'], b['bound_clause6']))); mxsep = max(mxsep, rs)
    fa, fb = a['separation'] >= 1, b['separation'] >= 1
    if fa != fb: STOP.append("script 1: fires column moved at L = %g" % a['L'])
    if rs > 1e-8: STOP.append("script 1: separation/ratio moved by %.2e relative at L = %g" % (rs, a['L']))
    if a['L'] <= 20 and abs(r1) > 0.02: STOP.append("script 1: W_Z' moved by %.2e relative at L = %g" % (r1, a['L']))
    p("| %s | %s | %s | %+.3e | %s | %s | %s | %s | %+.2e | %.6f | %.6f | %+.1e | %s / %s |" % (('%.5f' % a['L']).rstrip('0').rstrip('.'), fmt(a['W_Zprime']), fmt(b['W_Zprime']), r1, fmt(a['W_Z']), fmt(b['W_Z']), fmt(da, 12), fmt(db, 12), rid, a['ratio'], b['ratio'], rel(a['ratio'], b['ratio']), fa, fb))
p()
ls = [r for r in run['rows'] if abs(r['L'] - run['L_star']) < 1e-9][0]; lr = [r for r in rec['rows'] if abs(r['L'] - rec['L_star']) < 1e-9][0]
p("   the x6.24 ratio at L* = %.6f: |W_Z - W_Z'| = %.6f (record %.6f), bound delta^2 e^{delta L/2} = %.4f (record %.4f), ratio = %.6f (record %.6f); relative change %+.2e" % (run['L_star'], ls['separation'], lr['separation'], ls['bound_clause6'], lr['bound_clause6'], ls['ratio'], lr['ratio'], rel(lr['ratio'], ls['ratio'])))
p("   script 1 summary: rows changed (W_Z' or W_Z) %d of %d; max |relative change of W_Z'| = %.3e; identity residual max |rel. diff of (W_Z - W_Z')| = %.2e; max rel. move of separation/ratio/bound = %.2e; runtime record %.0f s, re-run %.0f s"
  % (sum(1 for a, b in zip(rec['rows'], run['rows']) if a['W_Zprime'] != b['W_Zprime'] or a['W_Z'] != b['W_Z']), len(rec['rows']), mx1, mxid, mxsep, rec['runtime_s'], run['runtime_s']))
p("   positive control (zeta, untouched by construction): " + "; ".join("L=%g: %r / %r" % (a['L'], a['W_zeta'], b['W_zeta']) for a, b in zip(rec['positive_control'], run['positive_control'])))
# ------------------------------------------------------------------------------------------------ 3. dh_control_new_heights
recJ = json.load(open(os.path.join(HERE, 'dh_offline_scan.json')))
run3 = json.load(open(os.path.join(HERE, 'dh_control_new_heights_rerun.json')))
p(); p("=" * 140)
p("3. campaign/dh_control_new_heights.py (record rows in dh_offline_scan.json, 2026-09-16 22:19) vs dh_control_new_heights_rerun.py (re-run); scan step 0.05, refinement on S(u) at 40 digits")
rows3 = {}
for a, b in zip(recJ['found_in_strip'], run3['found_in_strip']):
    if 'control_rows' not in a: continue
    assert a['t'] == b['t']
    zr, zn = a['online_window'], b['online_window']
    p("   t = %.6f, delta = %.6f: %d / %d on-line zeros; displacements min |d| = %.3e, max |d| = %.3e; re-run max |f_DH| at the refined points = %.2e; orbit |f| after Newton on f_DH: %.1e / %.1e"
      % (a['t'], a['delta'], len(zr), len(zn), min(abs(x - y) for x, y in zip(zr, zn)), max(abs(x - y) for x, y in zip(zr, zn)), b['online_max_abs_f'], a['abs_f_refined'], b['abs_f_refined']))
    if len(zr) != len(zn): STOP.append("script 3: count changed at t = %.3f" % a['t'])
    if b['online_max_abs_f'] > 1e-25: STOP.append("script 3: max |f_DH| = %.2e at t = %.3f" % (b['online_max_abs_f'], a['t']))
    p("| t = %.6f | L | W_Z' recorded | W_Z' re-run | relative | W_Z recorded | W_Z re-run | W_Z - W_Z' rec | W_Z - W_Z' re-run | ratio rec | ratio re-run | fires rec / re-run |" % a['t'])
    p("|---|---|---|---|---|---|---|---|---|---|---|---|")
    mx = 0.0; mxs = 0.0; ch = 0
    for x, y in zip(a['control_rows'], b['control_rows']):
        assert abs(x['L'] - y['L']) < 1e-12
        r1 = rel(x['W_Zprime'], y['W_Zprime']); mx = max(mx, abs(r1)); ch += (x['W_Zprime'] != y['W_Zprime'])
        rs = max(abs(rel(x['sep'], y['sep'])), abs(rel(x['ratio'], y['ratio'])), abs(rel(x['bound'], y['bound'])), abs(rel(x['main'], y['main']))); mxs = max(mxs, rs)
        fa, fb = x['sep'] >= 1, y['sep'] >= 1
        if fa != fb: STOP.append("script 3: fires moved at t = %.3f, L = %g" % (a['t'], x['L']))
        if rs > 1e-8: STOP.append("script 3: sep/ratio moved by %.2e at t = %.3f, L = %g" % (rs, a['t'], x['L']))
        if x['L'] <= 20 and abs(r1) > 0.02: STOP.append("script 3: W_Z' moved by %.2e at t = %.3f, L = %g" % (r1, a['t'], x['L']))
        p("| | %.2f | %s | %s | %+.3e | %s | %s | %s | %s | %.4f | %.4f | %s / %s |" % (x['L'], fmt(x['W_Zprime'], 6), fmt(y['W_Zprime'], 6), r1, fmt(x['W_Z'], 6), fmt(y['W_Z'], 6), fmt(x['W_Z'] - x['W_Zprime'], 6), fmt(y['W_Z'] - y['W_Zprime'], 6), x['ratio'], y['ratio'], fa, fb))
    p("   t = %.6f summary: W_Z' rows changed %d of %d; max |relative change of W_Z'| = %.3e; max rel. move of sep/ratio/bound/main = %.2e (the identity W_Z - W_Z' = main = -2 delta^2 c(delta L)^2 holds by construction in the campaign library: W_Z := W_Z' + main)" % (a['t'], ch, len(a['control_rows']), mx, mxs))
    rows3[round(a['t'], 6)] = b['control_rows']
    p()
p("   runtime: record %.0f s, re-run %.0f s" % (recJ['controls_seconds'], run3['controls_seconds']))
# ------------------------------------------------------------------------------------------------ 2. dh_offline_scan (control stage)
p(); p("=" * 140)
p("2. campaign/dh_offline_scan.py control stage (record rows from logs/dh_offline_scan.log, printed at 7 significant digits / ratio at 4; scan step 0.1) vs dh_offline_scan_rerun.py (re-run; the orbit search read from dh_offline_scan.json, not redone)")
txt = open(os.path.join(HERE, 'logs', 'dh_offline_scan.log')).read().splitlines()
recrows = {}
i = 0
while i < len(txt):
    m = re.match(r"\s+CONTROL at t = ([0-9.]+), delta = ([0-9.]+): (\d+) DH on-line zeros", txt[i])
    if m:
        t = round(float(m.group(1)), 6); rows = []; n = int(m.group(3)); i += 1
        while i < len(txt) and txt[i].startswith("   L="):
            mm = re.match(r"\s+L=\s*([0-9.]+): W_Z = (\S+)\s+W_Z' = (\S+)\s+main = (\S+)\s+\|W_Z - W_Z'\|/bound = (\S+)\s+fires\(>=1\): (True|False)", txt[i])
            rows.append(dict(L=float(mm.group(1)), W_Z=float(mm.group(2)), W_Zprime=float(mm.group(3)), main=float(mm.group(4)), ratio=float(mm.group(5)), fires=(mm.group(6) == 'True'))); i += 1
        recrows[t] = (n, rows)
    else: i += 1
run2 = json.load(open(os.path.join(HERE, 'dh_offline_scan_rerun.json')))
for b in run2['found_in_strip']:
    if 'control_rows' not in b: continue
    t = round(b['t'], 6); n, rows = recrows[t]
    p("   t = %.6f, delta = %.6f: %d recorded (log) / %d re-run on-line zeros at scan step 0.1; re-run max |f_DH| at the refined points = %.2e" % (b['t'], b['delta'], n, len(b['online_window']), b['online_max_abs_f']))
    if n != len(b['online_window']): STOP.append("script 2: count changed at t = %.3f" % t)
    if b['online_max_abs_f'] > 1e-25: STOP.append("script 2: max |f_DH| = %.2e at t = %.3f" % (b['online_max_abs_f'], t))
    p("| t = %.6f | L | W_Z' recorded (log) | W_Z' re-run | relative | W_Z recorded (log) | W_Z re-run | ratio rec (log) | ratio re-run | fires rec / re-run | W_Z' re-run of script 3 (step 0.05) | rel. (2 vs 3, both refined) |" % b['t'])
    p("|---|---|---|---|---|---|---|---|---|---|---|---|")
    mx = 0.0; mxs = 0.0; mx23 = 0.0; ch = 0
    r3 = {round(r['L'], 2): r for r in rows3.get(t, [])}
    for x, y in zip(rows, b['control_rows']):
        assert abs(x['L'] - y['L']) < 0.01, (x['L'], y['L'])
        r1 = rel(x['W_Zprime'], y['W_Zprime']); mx = max(mx, abs(r1)); ch += (abs(r1) > 5e-7)
        rs = abs(rel(x['ratio'], y['ratio'])); mxs = max(mxs, rs)
        fb = y['sep'] >= 1
        if x['fires'] != fb: STOP.append("script 2: fires moved at t = %.3f, L = %g" % (t, x['L']))
        if rs > 5e-4: STOP.append("script 2: ratio moved beyond the log's 4 printed digits at t = %.3f, L = %g" % (t, x['L']))
        if x['L'] <= 20 and abs(r1) > 0.02: STOP.append("script 2: W_Z' moved by %.2e at t = %.3f, L = %g" % (r1, t, x['L']))
        z3 = r3.get(round(y['L'], 2)); r23 = rel(y['W_Zprime'], z3['W_Zprime']) if z3 else float('nan'); mx23 = max(mx23, abs(r23)) if z3 else mx23
        p("| | %.2f | %s | %s | %+.3e | %s | %s | %.4g | %.4g | %s / %s | %s | %+.1e |" % (y['L'], fmt(x['W_Zprime'], 6), fmt(y['W_Zprime'], 6), r1, fmt(x['W_Z'], 6), fmt(y['W_Z'], 6), x['ratio'], y['ratio'], x['fires'], fb, fmt(z3['W_Zprime'], 6) if z3 else 'n/a', r23))
    p("   t = %.6f summary: W_Z' rows changed %d of %d (beyond the log's 7 printed digits); max |relative change of W_Z'| = %.3e; max rel. move of the ratio column = %.2e (against 4 printed digits); the two refined re-runs (scan step 0.1 here, 0.05 in script 3) agree on W_Z' to max rel. %.2e" % (t, ch, len(rows), mx, mxs, mx23))
    p()
p("   runtime: re-run control stage %.0f s (the record's 1712 s included the 30-minute orbit search, which is not redone)" % run2['seconds'])
p(); p("=" * 140)
p("STOP CONDITIONS (DH-RERUN-BRIEF.md 10(m)): " + ("NONE fired" if not STOP else "FIRED: " + "; ".join(STOP)))
for f in ['dh_negative_control_rerun.py', 'dh_negative_control_rerun_run.log', 'dh_negative_control_rerun_out.json']:
    p("   sha256 %s  verify/%s" % (sha(os.path.join(V, f)), f))
for f in ['dh_offline_scan_rerun.py', 'dh_offline_scan_rerun.json', 'logs/dh_offline_scan_rerun.log', 'dh_control_new_heights_rerun.py', 'dh_control_new_heights_rerun.json', 'logs/dh_control_new_heights_rerun.log']:
    p("   sha256 %s  campaign/%s" % (sha(os.path.join(HERE, f)), f))
open(os.path.join(HERE, 'dh_rerun_compare.log'), 'w').write("\n".join(L) + "\n")
