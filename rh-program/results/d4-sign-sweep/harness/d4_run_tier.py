#!/usr/bin/env python3
"""d4_run_tier.py -- D4 sweep at scale (BRIEF "The sweep design", "Checkpoints (10(l))"; the fixed plan harness/sweep_plan.json).
One tier, one point at a time, ONE 8-thread process at any moment:
  for each planned height (tier 1: the 121-height ladder at L = 22 then the two covered-range controls; tier 2: 1e14, 1e16, 1e18,
  the 1e20-th-zero control, ladder k = 117 at L = 28.35 -- the PT-edge point is landed and has Job 2's PASS row):
   1. RESUME rule: a point whose out/zeta_t<t>_L<L>.json exists with a verdict is not recomputed (a killed session resumes here);
   2. harness/d4_point.py --t <t> --L <L> --threads 8 --tier <tier>  (both controls at every point; the SHARED row; hashes.txt);
   3. Control 1 at EVERY point: Job 2's independent Go evaluator checker-O/twsumO (binary hash recorded) is run BY JOB 1 on the
      same (t, L) with 8 threads AFTER the Job-1 process has exited (never concurrently) -> out/replayO_t<t>_L<L>.json; the
      differences |P1 - P2|, |W1 - W2| against the tolerance 1e-10 + eps_proven * t * l1 -> out/control1_t<t>_L<L>.json and a
      SHARED row (who: "Job 1 running Job 2's twsumO"); a point with a landed checker-O/out/zetaO_* JSON (Job 2's own replay) is
      compared against that instead of re-run;
   4. STOP lines (the runner exits non-zero and writes the row): any verdict other than "silent (W > 0)" (a candidate, a bug, a
      control failure, a refusal); a Control-1 FAIL; a tier-2 point whose sum exceeds 2 h;
   5. an "alive" row in SHARED.md every 30 minutes of wall time while a point is running; `pmset -g therm` and the heavy-process
      count logged before every tier-2 point.
usage: d4_run_tier.py --tier 1|2 [--no-replay]"""
import json, os, sys, time, subprocess, hashlib, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..')); OUT = os.path.join(ROOT, 'out')
TWSUMO = os.path.join(ROOT, 'checker-O', 'twsumO'); CHK_OUT = os.path.join(ROOT, 'checker-O', 'out')
def now(): return subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
ap = argparse.ArgumentParser(); ap.add_argument('--tier', required=True); ap.add_argument('--no-replay', action='store_true'); A = ap.parse_args()
plan = json.load(open(os.path.join(HERE, 'sweep_plan.json'))); EPS = json.load(open(os.path.join(HERE, 'eps_phi.json')))['eps_phi_per_t']
logf = open(os.path.join(HERE, f'd4_run_tier{A.tier}_run.log'), 'a')
def log(s):
    print(s, flush=True); logf.write(s + "\n"); logf.flush()
def shared(row): open(os.path.join(ROOT, 'SHARED.md'), 'a').write(row + "\n")
if A.tier == '1':
    L = plan['tier1_L']; pts = [(p['t_exact'], f"tier 1 ladder k={p['k']}") for p in plan['tier1']] + [(p['t_exact'], "tier 1 " + p['role'][:60]) for p in plan['tier1_controls']]
else:
    L = plan['tier2_L']; pts = [(p['t_exact'], "tier 2 " + p['role'][:70]) for p in plan['tier2']]
Lg = f"{L:g}"; twsumo_sha = sha(TWSUMO)
log(f"[{now()}] d4_run_tier.py tier {A.tier}: {len(pts)} points at L = {L}; eps_proven {EPS:.6e}; twsumO {twsumo_sha[:16]}; resume rule on")
last_alive = time.time()
def alive(what):
    global last_alive
    if time.time() - last_alive >= 1800: shared(f"| {now()} | Job 1 | alive — running {what} |"); last_alive = time.time()
def run_watched(cmd, what, logpath):
    with open(logpath, 'a') as lf:
        p = subprocess.Popen(cmd, stdout=lf, stderr=subprocess.STDOUT)
        while p.poll() is None: time.sleep(20); alive(what)
    return p.returncode
def heavy(): return [l for l in subprocess.run(['ps', '-Ao', 'pcpu,comm'], capture_output=True, text=True).stdout.splitlines()[1:] if float(l.split()[0]) > 50]
for t, label in pts:
    pj = os.path.join(OUT, f"zeta_t{t}_L{Lg}.json"); what = f"({t}, {L}) {label}"
    if A.tier == '2':
        th = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True).stdout.replace("\n", " | "); log(f"[{now()}] before {what}: pmset -g therm: {th}; heavy processes: {heavy()}")
    if os.path.exists(pj) and 'verdict' in json.load(open(pj)):
        log(f"[{now()}] RESUME: {what} already landed ({pj}); not recomputed")
    else:
        while len(heavy()) >= 1: log(f"[{now()}] waiting: heavy processes {heavy()}"); time.sleep(60)
        t0 = time.time()
        rc = run_watched([sys.executable, os.path.join(HERE, 'd4_point.py'), '--t', t, '--L', str(L), '--threads', '8', '--tier', A.tier, '--label', label], what, os.path.join(HERE, f'd4_run_tier{A.tier}_points.log'))
        if rc != 0 or not os.path.exists(pj):
            log(f"[{now()}] STOP: d4_point.py rc={rc} at {what}"); shared(f"| {now()} | Job 1 | {t} | {L} | STOP: d4_point.py exited rc={rc} (refused before launch, or a failure) at {label} — the leg stops here |"); sys.exit(10)
        log(f"[{now()}] landed {what} in {time.time()-t0:.0f} s")
    J = json.load(open(pj))
    if J['verdict'] != 'silent (W > 0)':
        log(f"[{now()}] ***** STOP at {what}: verdict = {J['verdict']}; stop_line = {J.get('stop_line')} *****"); shared(f"| {now()} | Job 1 | {t} | {L} | **STOP — {J['verdict']}** (stop_line: {J.get('stop_line')}); the leg stops here; nothing further is started |"); sys.exit(11)
    if A.tier == '2' and J.get('wall_sum_s') and J['wall_sum_s'] > 7200:
        log(f"[{now()}] STOP: tier-2 point exceeded 2 h ({J['wall_sum_s']:.0f} s) at {what}"); shared(f"| {now()} | Job 1 | {t} | {L} | STOP: the sum took {J['wall_sum_s']:.0f} s > 2 h (stop line (7)); re-price before continuing |"); sys.exit(12)
    # Control 1
    if A.no_replay: continue
    c1 = os.path.join(OUT, f"control1_t{t}_L{Lg}.json")
    if os.path.exists(c1): log(f"[{now()}] RESUME: Control 1 at {what} already on disk"); continue
    job2 = [f for f in os.listdir(CHK_OUT) if f.startswith('zetaO_t') and f.endswith(f"_L{Lg}.json") and json.load(open(os.path.join(CHK_OUT, f))).get('t_exact') == t]
    if job2:
        rj = os.path.join(CHK_OUT, job2[0]); who = "Job 2's own replay (checker-O/out)"; wall = json.load(open(rj)).get('wall_s')
    else:
        rj = os.path.join(OUT, f"replayO_t{t}_L{Lg}.json"); who = f"Job 1 running Job 2's twsumO ({twsumo_sha[:16]})"
        while len(heavy()) >= 1: log(f"[{now()}] waiting before replay: {heavy()}"); time.sleep(60)
        t0 = time.time()
        rc = run_watched([TWSUMO, '-mode', 'zeta', '-t', t, '-L', str(L), '-threads', '8', '-out', rj], "Control-1 replay of " + what, os.path.join(HERE, f'd4_run_tier{A.tier}_replay.log'))
        wall = time.time() - t0
        if rc != 0 or not os.path.exists(rj): log(f"[{now()}] STOP: twsumO rc={rc} at {what}"); shared(f"| {now()} | Job 1 | {t} | {L} | STOP: the Control-1 replay (twsumO) failed rc={rc} |"); sys.exit(13)
    R = json.load(open(rj)); assert R['t_exact'] == t, (R['t_exact'], t)
    line = EPS*float(t)*J['l1_norm']; tol = 1e-10 + line; dP = abs(J['P_dd'] - R['P']); dW = abs(J['W'] - R['W']); ok = dP <= tol and dW <= tol
    res = dict(date=now(), t_exact=t, L=L, who=who, twsumO_sha256=twsumo_sha, job1_json=os.path.basename(pj), job1_json_sha256=sha(pj), replay_json=os.path.relpath(rj, ROOT), replay_json_sha256=sha(rj),
               P_job1=J['P_dd'], P_replay=R['P'], dP=dP, W_job1=J['W'], W_replay=R['W'], dW=dW, ARCH_job1=J['ARCH'], ARCH_replay=R['ARCH'], l1_job1=J['l1_norm'], l1_replay=R.get('l1'),
               n_terms_job1=J['n_terms'], n_terms_replay=R.get('n_terms'), phase_line_eps_proven=line, tolerance=tol, PASS=ok, replay_wall_s=wall, replay_threads=R.get('threads'))
    json.dump(res, open(c1, 'w'), indent=1)
    open(os.path.join(ROOT, 'hashes.txt'), 'a').write(f"{sha(rj)}  {os.path.relpath(rj, ROOT)}\n{sha(c1)}  out/{os.path.basename(c1)}\n")
    shared(f"| {now()} | {who} | {t} | {L} | terms {R.get('n_terms')} ({'same' if R.get('n_terms') == J['n_terms'] else 'DIFFER'}) | P_O = {R['P']:+.15e} | ARCH_O = {R['ARCH']:.15e} | — | **W_O = {R['W']:+.15e}** | \\|ΔP\\| = {dP:.1e}, \\|ΔW\\| = {dW:.1e} | tol {tol:.2e} (line {line:.2e}) | — | — | — | sum {wall:.0f} s, 8 thr | **Control 1 {'PASS' if ok else 'FAIL'}** | {sha(c1)[:16]} |")
    log(f"[{now()}] Control 1 at {what}: dP {dP:.2e} dW {dW:.2e} tol {tol:.2e} -> {'PASS' if ok else 'FAIL'} ({who}, {wall:.0f} s)")
    if not ok: log(f"[{now()}] ***** STOP: Control 1 FAIL at {what} *****"); shared(f"| {now()} | Job 1 | {t} | {L} | **STOP — Control 1 FAIL** (the two implementations disagree beyond 1e-10 + phase line); the leg stops here |"); sys.exit(14)
log(f"[{now()}] tier {A.tier} COMPLETE: {len(pts)} points, all silent, Control 1 PASS at every point")
