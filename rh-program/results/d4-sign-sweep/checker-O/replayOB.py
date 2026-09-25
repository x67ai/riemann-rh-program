#!/usr/bin/env python3
"""D4 Job 2 part B (Opus 5): OWN Control-1 launches of checker-O/twsumO, strictly one at a time.
Usage: replayOB.py <L> <t1> <t2> ...   (L as in Job 1's file names: 22 or 28.35)
Before each launch: ps check (no twsumO / d4_twisted_sum / d4_point running; any process >50% CPU is logged);
pmset -g therm read and CPU_Speed_Limit recorded (threads drop to 6 if < 100, stop line (5)).
Writes checker-O/out/replayOB_t<t>_L<L>.json (twsumO's own output) and checker-O/out/replayOB_cmp_t<t>_L<L>.json
(the comparison), appends one SHARED.md row per point, logs to checker-O/logs/replayOB_run.log."""
import sys, os, json, subprocess, time, hashlib, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'out'); LOG = os.path.join(HERE, 'logs', 'replayOB_run.log')
EPS = 1.0266395604864687e-30
TW = os.path.join(HERE, 'twsumO')
def now(): return time.strftime('%a %b %d %H:%M:%S IST %Y')
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def log(s):
    print(s, flush=True); open(LOG, 'a').write(s + '\n')
def shared(row): open(os.path.join(ROOT, 'SHARED.md'), 'a').write(row + '\n')
def heavy():
    out = subprocess.run(['ps', '-Ao', 'pcpu,comm'], capture_output=True, text=True).stdout.splitlines()[1:]
    hot = [l.strip() for l in out if l.split() and float(l.split()[0]) > 50]
    mine = [l for l in hot if re.search(r'twsumO|d4_twisted_sum|d4_point', l)]
    return hot, mine
def therm():
    s = subprocess.run(['pmset', '-g', 'therm'], capture_output=True, text=True).stdout
    m = re.search(r'CPU_Speed_Limit\s*=\s*(\d+)', s)
    return (int(m.group(1)) if m else None), ' '.join(s.split())
L = sys.argv[1]; ts = sys.argv[2:]
assert sha(TW) == 'd57080a8eeee7da8e59322df2446c976a3b8ee64a18cf6064975dced489d0f45', 'twsumO hash changed'
threads = 8
for t in ts:
    rj = os.path.join(OUT, f'replayOB_t{t}_L{L}.json'); cj = os.path.join(OUT, f'replayOB_cmp_t{t}_L{L}.json')
    if os.path.exists(cj): log(f'[{now()}] RESUME: {t} L={L} already compared'); continue
    while True:
        hot, mine = heavy()
        log(f'[{now()}] pre-launch ps (>50% CPU): {hot if hot else "none"}')
        if not mine: break
        log(f'[{now()}] waiting: heavy process of the program running: {mine}'); time.sleep(60)
    lim, traw = therm()
    log(f'[{now()}] pmset -g therm: CPU_Speed_Limit = {lim} | {traw}')
    if lim is not None and lim < 100 and threads == 8:
        threads = 6; log(f'[{now()}] STOP LINE (5): CPU_Speed_Limit {lim} < 100 -> remaining replays at 6 threads')
        shared(f'| {now()} | Job 2 (Opus 5) part B | {t} | {L} | STOP LINE (5): pmset CPU_Speed_Limit = {lim} < 100; remaining replays at 6 threads |')
    shared(f'| {now()} | Job 2 (Opus 5) part B | {t} | {L} | LAUNCH own Control-1 replay: checker-O/twsumO (d57080a8eeee7da8), {threads} thr; pre-launch ps: {"nothing heavy of the program" }; CPU_Speed_Limit = {lim} |')
    log(f'[{now()}] LAUNCH twsumO -mode zeta -t {t} -L {L} -threads {threads} -out {os.path.relpath(rj, ROOT)}')
    t0 = time.time()
    with open(LOG, 'a') as lf:
        rc = subprocess.run([TW, '-mode', 'zeta', '-t', t, '-L', L, '-threads', str(threads), '-out', rj], stdout=lf, stderr=subprocess.STDOUT).returncode
    wall = time.time() - t0
    lim2, traw2 = therm()
    log(f'[{now()}] twsumO rc={rc}, wall {wall:.1f} s; post-run CPU_Speed_Limit = {lim2}')
    if rc != 0 or not os.path.exists(rj):
        log(f'[{now()}] STOP: twsumO rc={rc}'); shared(f'| {now()} | Job 2 (Opus 5) part B | {t} | {L} | STOP: twsumO rc={rc} |'); sys.exit(13)
    R = json.load(open(rj)); assert R['t_exact'] == t, (R['t_exact'], t)
    J = json.load(open(os.path.join(ROOT, 'out', f'zeta_t{t}_L{L}.json')))
    c1 = json.load(open(os.path.join(ROOT, 'out', f'control1_t{t}_L{L}.json')))
    rOp = os.path.join(ROOT, 'out', f'replayO_t{t}_L{L}.json')
    if not os.path.exists(rOp): rOp = os.path.join(HERE, 'out', f'zetaO_t{t}_L{L}.json')  # the PT edge: Job 2's part-A run
    RO = json.load(open(rOp))
    line_mine = EPS * float(t) * R['l1']; line_job1 = EPS * float(t) * J['l1_norm']
    tol = 1e-10 + line_job1
    dP = abs(J['P_dd'] - R['P']); dW = abs(J['W'] - R['W'])
    dPO = abs(RO['P'] - R['P']); dWO = abs(RO['W'] - R['W'])
    ok = dP <= tol and dW <= tol and dWO <= tol
    res = dict(date=now(), t_exact=t, L=float(L), who='Job 2 (Opus 5) part B, own launch', twsumO_sha256=sha(TW),
               replay_json=os.path.relpath(rj, ROOT), replay_json_sha256=sha(rj), job1_json=os.path.basename(J.get('_path', f'zeta_t{t}_L{L}.json')),
               job1_json_sha256=sha(os.path.join(ROOT, 'out', f'zeta_t{t}_L{L}.json')), earlier_replay=os.path.relpath(rOp, ROOT), earlier_replay_sha256=sha(rOp),
               P_job1=J['P_dd'], W_job1=J['W'], P_replayO_earlier=RO['P'], W_replayO_earlier=RO['W'], P_OB=R['P'], P_OB_lo=R.get('P_lo'), W_OB=R['W'], ARCH_OB=R['ARCH'], ARCH_job1=J['ARCH'],
               dP_vs_job1=dP, dW_vs_job1=dW, dP_vs_replayO=dPO, dW_vs_replayO=dWO, bit_identical_W_vs_replayO=(RO['W'] == R['W']), bit_identical_P_vs_replayO=(RO['P'] == R['P'] and RO.get('P_lo') == R.get('P_lo')),
               ARCH_identical_vs_replayO=(RO['ARCH'] == R['ARCH']), n_terms_OB=R['n_terms'], n_terms_job1=J['n_terms'], n_terms_replayO=RO['n_terms'],
               l1_OB=R['l1'], l1_job1=J['l1_norm'], phase_line_eps_proven_l1_job1=line_job1, phase_line_eps_proven_l1_OB=line_mine, tolerance=tol,
               control1_job1_dW=c1['dW'], control1_job1_tol=c1['tolerance'], PASS=ok, wall_s=wall, sum_s=R.get('sum_s'), threads=threads,
               cpu_speed_limit_pre=lim, cpu_speed_limit_post=lim2)
    json.dump(res, open(cj, 'w'), indent=1)
    shared(f"| {now()} | Job 2 (Opus 5) part B, own launch (twsumO d57080a8eeee7da8) | {t} | {L} | terms {R['n_terms']} ({'same' if R['n_terms'] == J['n_terms'] else 'DIFFER'}) | P_O = {R['P']:+.15e} | ARCH_O = {R['ARCH']:.15e} | — | **W_O = {R['W']:+.15e}** | \\|ΔP\\| = {dP:.1e}, \\|ΔW\\| = {dW:.1e} vs Job 1's harness; \\|ΔW\\| = {dWO:.1e} vs the earlier replayO ({'bit-identical' if RO['W'] == R['W'] else 'not bit-identical'}) | tol {tol:.2e} (line {line_job1:.2e}) | — | — | — | sum {R.get('sum_s', 0):.0f} s, {threads} thr, CPU_Speed_Limit {lim}/{lim2} | **Control 1 {'PASS' if ok else 'FAIL'}** | {sha(rj)[:16]} |")
    log(f"[{now()}] {t} L={L}: W_OB {R['W']:+.17e}; dW vs Job1 {dW:.2e}; dW vs replayO {dWO:.2e} (bit-identical {RO['W'] == R['W']}); tol {tol:.2e} -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        log(f'[{now()}] ***** STOP LINE (1): Control 1 FAIL at {t} L={L} *****')
        shared(f'| {now()} | Job 2 (Opus 5) part B | {t} | {L} | **STOP LINE (1) — Control 1 FAIL** |'); sys.exit(14)
log(f'[{now()}] batch L={L} complete: {len(ts)} points')
