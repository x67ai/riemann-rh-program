#!/usr/bin/env python3
"""d4_point.py -- D4: one sweep point (t, L) end to end (BRIEF "Checkpoints (10(l))").
  1. process rule: refuse to launch when >= 4 CPU-heavy processes are running (ps pcpu > 50);
  2. pre-check of the phase line with the PNT estimate of l1(L) (M6 section 6: (2/L^2) int_0^1 e^{Lv/2} |A(v)| dv);
  3. the twisted sum (harness/d4_twisted_sum, --selftest 1000, --eps-phi <measured>) -> out/sum_zeta_t<t>_L<L>.json
     (reused if present and --reuse);
  4. the archimedean integral + pole terms + the bracket on two code paths (d4_arch.py) -> out/arch_zeta_t<t>_L<L>.json;
  5. the dd-phase self-test (d4_phase_selftest.py logic) on the sum JSON: measured eps_phi/t; the post-check of the phase
     line with the printed l1;
  6. delta_vis(t, L) = 0.1 (L_sign(0.1, t)/L)^{3/2}, L_sign(0.1, t) = 22.4 (log t / log 1e6)^{1/3} (BRIEF, sweep design;
     the factor-1.5 band on L_sign becomes the factor 1.5^{3/2} = 1.837 on delta_vis; the log(t/2pi) variant printed);
  7. Control 2 (zero side): the planted orbit at (t, L, delta_vis) (d4_planted.py) -> out/planted_*.json;
  8. Control 2 (coefficient side): the DH regression at (85.7, 10) (sub-second; must FIRE: W_DH < 0, P to 1e-12 of the record);
  9. W = pole + ARCH - P; the error budget in M6 section 3's shape; the stop-line evaluation:
       W < 0 and t <= 3 000 175 332 800 -> BUG (stop);  W < 0 above -> CANDIDATE (stop everything);
 10. out/zeta_t<exact t>_L<L>.json, a row in SHARED.md, a line in hashes.txt.
usage: d4_point.py --t <exact decimal> --L <L> [--threads 8] [--eps-phi 6.4e-31] [--reuse] [--tier rehearsal|1|2] [--label ...]
"""
import json, os, sys, math, time, datetime, subprocess, hashlib, argparse
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..')); OUT = os.path.join(ROOT, 'out')
BIN = os.path.join(HERE, 'd4_twisted_sum')
PT_HEIGHT = 3000175332800          # Platt-Trudgian Theorem 1, exact (read at the page: prior-art/platt-trudgian-2021.txt line 56)
T85 = "85.69934848537759"
DH_P_RECORD = 0.339995468928925    # M6 section 5.1
ALLOW = 1e-8
def now(): return subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
ap = argparse.ArgumentParser()
ap.add_argument('--t', required=True); ap.add_argument('--L', type=float, required=True); ap.add_argument('--threads', type=int, default=8)
ap.add_argument('--eps-phi', type=float, default=None, help='measured eps_phi per unit t (default: harness/eps_phi.json)')
ap.add_argument('--reuse', action='store_true'); ap.add_argument('--tier', default='rehearsal'); ap.add_argument('--label', default='')
ap.add_argument('--no-dh', action='store_true', help='skip the DH regression (only for re-assembly)')
A = ap.parse_args()
logf = open(os.path.join(HERE, 'd4_point_run.log'), 'a')
def out(s):
    print(s, flush=True); logf.write(s + "\n"); logf.flush()
t_str = A.t; L = A.L; Lg = f"{L:g}"
assert t_str.lstrip('-').isdigit(), "the height must be given as an exact integer (an integer-valued double)"
t_f = float(t_str); assert int(t_f) == int(t_str), f"{t_str} is not exactly representable as a double; use {int(t_f)}"
eps = A.eps_phi
if eps is None:
    eps = json.load(open(os.path.join(HERE, 'eps_phi.json')))['eps_phi_per_t']
T0 = time.time()
out(f"[{now()}] d4_point.py start: t = {t_str}, L = {L}, threads = {A.threads}, eps_phi/t = {eps:.3e}, tier = {A.tier} {A.label}")
# 1. process rule
heavy = [l for l in subprocess.run(['ps', '-Ao', 'pcpu,comm'], capture_output=True, text=True).stdout.splitlines()[1:] if float(l.split()[0]) > 50]
if len(heavy) >= 4 and not A.reuse:
    out(f"[{now()}] REFUSED to launch: {len(heavy)} CPU-heavy processes running: {heavy}"); sys.exit(3)
# 2. pre-check of the phase line with the PNT l1 estimate
M = 4096; w = np.arange(1, M)/M - 0.5
def braw(x):
    with np.errstate(all='ignore'): r = np.exp(-1.0/(1.0 - 4.0*x*x))
    return np.where(np.abs(x) < 0.5, np.nan_to_num(r), 0.0)
def braw_d1(x):
    with np.errstate(all='ignore'): q = 1.0 - 4.0*x*x; r = braw(x)*(-8.0*x/(q*q))
    return np.where(np.abs(x) < 0.5, np.nan_to_num(r), 0.0)
Z = braw(w).sum()/M
def A_of(v): return float(np.sum(braw_d1(w)*braw_d1(w - v))/M)/(Z*Z)
vs = np.linspace(0, 1, 2001); Av = np.array([A_of(v) for v in vs])
l1_est = float(2.0/L**2*np.trapezoid(np.exp(L*vs/2)*np.abs(Av), vs))
line_est = eps*t_f*l1_est
out(f"[{now()}] pre-check: l1(L={L}) PNT estimate = {l1_est:.4f}; phase line estimate eps*t*l1 = {line_est:.3e} against {ALLOW:.0e} -> {'REFUSE' if line_est > ALLOW else 'go'}")
if line_est > ALLOW:
    res = dict(date=now(), t_exact=t_str, L=L, refused_precheck=True, l1_estimate=l1_est, phase_line_estimate=line_est, eps_phi_per_t=eps)
    json.dump(res, open(os.path.join(OUT, f"zeta_t{t_str}_L{Lg}.json"), 'w'), indent=1)
    open(os.path.join(ROOT, 'SHARED.md'), 'a').write(f"\n| {now()} | Job 1 | {t_str} | {L} | REFUSED before launch: phase line estimate {line_est:.2e} > 1e-8 (eps {eps:.2e}, l1 est {l1_est:.1f}) |\n")
    sys.exit(4)
# 3. the twisted sum
sum_json = os.path.join(OUT, f"sum_zeta_t{t_str}_L{Lg}.json")
if not (A.reuse and os.path.exists(sum_json)):
    cmd = [BIN, '--mode', 'zeta', '--t', t_str, '--L', str(L), '--threads', str(A.threads), '--selftest', '1000', '--seed', '20260925', '--eps-phi', repr(eps), '--out', sum_json]
    out(f"[{now()}] running: {' '.join(cmd)}")
    t1 = time.time(); r = subprocess.run(cmd, capture_output=True, text=True); wall_sum = time.time() - t1
    open(os.path.join(HERE, 'd4_twisted_sum_run.log'), 'a').write(f"=== d4_point t={t_str} L={L} {now()} ===\n{r.stderr}\n")
    if r.returncode != 0: out(f"[{now()}] twisted sum FAILED rc={r.returncode}: {r.stderr[-500:]}"); sys.exit(5)
else:
    wall_sum = None
S = json.load(open(sum_json))
assert S['t_exact'] == t_str, (S['t_exact'], t_str)
# 4. ARCH + pole + bracket two paths
arch_json = os.path.join(OUT, f"arch_zeta_t{t_str}_L{Lg}.json")
if not (A.reuse and os.path.exists(arch_json)):
    r = subprocess.run([sys.executable, os.path.join(HERE, 'd4_arch.py'), '--kind', 'zeta', '--t', t_str, '--L', str(L), '--out', arch_json], capture_output=True, text=True)
    if r.returncode != 0: out(f"[{now()}] d4_arch.py FAILED: {r.stderr[-500:]}"); sys.exit(6)
AR = json.load(open(arch_json))
# 5. self-test
r = subprocess.run([sys.executable, os.path.join(HERE, 'd4_phase_selftest.py'), sum_json], capture_output=True, text=True)
ST = json.load(open(sum_json.replace('.json', '.selftest.json')))
eps_meas = ST['eps_phi_per_t_measured']
l1 = S['l1_norm']; phase_line = eps*t_f*l1; phase_line_meas = eps_meas*t_f*l1
refused = phase_line > ALLOW
# 6. delta_vis
Lsign = 22.4*(math.log(t_f)/math.log(1e6))**(1/3); dvis = 0.1*(Lsign/L)**1.5
Lsign2 = 22.4*(math.log(t_f/(2*math.pi))/math.log(1e6/(2*math.pi)))**(1/3); dvis2 = 0.1*(Lsign2/L)**1.5
band = (dvis/1.5**1.5, dvis*1.5**1.5)
# 7. Control 2, zero side
pl_json = os.path.join(OUT, f"planted_t{t_str}_L{Lg}_d{dvis:.6g}.json")
r = subprocess.run([sys.executable, os.path.join(HERE, 'd4_planted.py'), '--t', t_str, '--L', str(L), '--delta', repr(dvis), '--out', pl_json], capture_output=True, text=True)
if r.returncode != 0: out(f"[{now()}] d4_planted.py FAILED: {r.stderr[-500:]}"); sys.exit(7)
PL = json.load(open(pl_json))
# 8. Control 2, coefficient side: DH regression at (85.7, 10)
dh = dict(skipped=True)
if not A.no_dh:
    dh_json = os.path.join(OUT, f"dhreg_t{t_str}_L{Lg}.json")
    r = subprocess.run([BIN, '--mode', 'dh', '--t', T85, '--L', '10', '--threads', '2', '--out', dh_json], capture_output=True, text=True)
    D = json.load(open(dh_json)); arch_dh = json.load(open(os.path.join(OUT, 'arch_dh_t85.69934848537759_L10.json')))['arch']
    W_dh = arch_dh - D['P_dd']
    wit = {n: v for n, v in D['lambda_dh_witnesses']}
    dh = dict(P=D['P_dd'], P_record=DH_P_RECORD, P_diff=D['P_dd'] - DH_P_RECORD, arch=arch_dh, W=W_dh, fires=W_dh < 0, P_within_1e12=abs(D['P_dd'] - DH_P_RECORD) <= 1e-12,
              witnesses=dict(L3=wit.get(3), L4=wit.get(4), L6=wit.get(6), L12=wit.get(12)), json=os.path.basename(dh_json))
    dh['pass'] = bool(dh['fires'] and dh['P_within_1e12'])
# 9. W and the budget
pole = AR['pole'].get('pole_term_2Re', 0.0); pole_note = AR['pole']['method'] + (f" 10^{AR['pole']['log10_lemmaG_bound_on_pole_term']:.0f}" if 'log10_lemmaG_bound_on_pole_term' in AR['pole'] else '')
P = S['P_dd']; W = pole + AR['arch'] - P
interp = 3*max(abs(x[3]) for x in S['A_interp_check'])/abs(S['A0'])*l1
quad = 10*(abs(AR['conv_h']) + abs(AR['conv_H']))
pole_b = 10**AR['pole']['log10_lemmaG_bound_on_pole_term'] if 'log10_lemmaG_bound_on_pole_term' in AR['pole'] else abs(pole)
cos_rounding = 2.3e-16*l1      # |cos| evaluated in double: <= 1 ulp per term times the l1 mass
budget = phase_line + interp + quad + pole_b + cos_rounding + 1e-14
stop = None
if W < 0:
    stop = 'BUG: negative W at t <= PT height (stop line (2))' if t_f <= PT_HEIGHT else 'CANDIDATE: negative W above PT height (stop line (1)) -- STOP EVERYTHING'
controls_pass = bool(PL['pass_'] and (dh.get('pass', True)))
verdict = ('REFUSED (phase line)' if refused else ('STOP: ' + stop if stop else ('silent (W > 0)' if controls_pass else 'CONTROL FAILED -- no value recorded')))
res = dict(date=now(), tier=A.tier, label=A.label, t_exact=t_str, t_bits=S['t_bits'], L=L, X=S['X'], n_terms=S['n_terms'], n_primes=S['n_primes'], n_prime_powers=S['n_prime_powers'],
           P_dd=P, P_double_diagnostic=S['P_double'], P_dd_minus_P_double=S['P_dd_minus_P_double'], l1_norm=l1, l1_estimate_PNT=l1_est,
           eps_phi_per_t_used=eps, eps_phi_per_t_measured=eps_meas, selftest_max_phase_error=ST['max_phase_error'], selftest_max_log_error=ST['max_log_error'],
           selftest_prod_red_only=ST['max_phase_error_prod_red_only'], selftest_pass_3e31=ST['pass_'],
           phase_line=phase_line, phase_line_measured=phase_line_meas, phase_line_allowance=ALLOW, refused=refused,
           ARCH=AR['arch'], arch_conv_h=AR['conv_h'], arch_conv_H=AR['conv_H'], bracket_two_path_diff=max(AR['bracket_two_path_diff_at_t'], AR['bracket_two_path_worst_over_nodes']),
           pole=pole, pole_note=pole_note, W=W, W_sign='negative' if W < 0 else 'positive',
           budget=dict(phase_line=phase_line, interpolation=interp, arch_quadrature=quad, pole=pole_b, cos_rounding=cos_rounding, floor=1e-14, total=budget),
           W_over_budget=abs(W)/budget,
           delta_vis=dvis, delta_vis_band_factor_1p5=list(band), L_sign_0p1=Lsign, delta_vis_log_t_over_2pi_variant=dvis2,
           control2_zero_side=dict(delta=dvis, lambda_=PL['lambda_'], kernel_value=PL['pair_kernel_re'], expected=PL['expected'], rel_diff=PL['rel_diff'], pass_=PL['pass_'], json=os.path.basename(pl_json)),
           control2_coefficient_side_DH=dh, controls_pass=controls_pass, verdict=verdict, stop_line=stop,
           wall_sum_s=wall_sum, time_sum_s=S['time_sum_s'], ns_per_term_wall=S['ns_per_term_wall'], threads=S['threads'],
           binary_sha256=sha(BIN), source_sha256=sha(os.path.join(HERE, 'd4_twisted_sum.rs')), sum_json=os.path.basename(sum_json), sum_json_sha256=sha(sum_json),
           arch_json=os.path.basename(arch_json), arch_json_sha256=sha(arch_json), seconds_total=time.time() - T0)
pj = os.path.join(OUT, f"zeta_t{t_str}_L{Lg}.json")
json.dump(res, open(pj, 'w'), indent=1)
open(os.path.join(ROOT, 'hashes.txt'), 'a').write(f"{sha(pj)}  out/{os.path.basename(pj)}\n{res['sum_json_sha256']}  out/{res['sum_json']}\n{res['arch_json_sha256']}  out/{res['arch_json']}\n")
row = (f"| {now()} | Job 1 | {t_str} | {L} | X = {S['X']}, {S['n_terms']} terms | P = {P:+.15e} | ARCH = {AR['arch']:.15e} | pole {pole_note} | **W = {W:+.15e}** | budget {budget:.1e} | "
       f"phase line {phase_line:.2e} (ε {eps:.2e}; measured {eps_meas:.2e}) | δ_vis = {dvis:.4f} [{band[0]:.4f}, {band[1]:.4f}] | C2 zero side {PL['pair_kernel_re']:.12e} vs {PL['expected']:.12e} ({'PASS' if PL['pass_'] else 'FAIL'}) | "
       f"DH reg {('W = %.9f %s' % (dh['W'], 'FIRES' if dh['fires'] else 'SILENT')) if not dh.get('skipped') else 'skipped'} | sum {S['time_sum_s']:.1f} s ({S['ns_per_term_wall']:.1f} ns/term wall, {S['threads']} thr) | {verdict} | {sha(pj)[:16]} |")
open(os.path.join(ROOT, 'SHARED.md'), 'a').write(row + "\n")
out(f"[{now()}] {row}")
if stop: out(f"[{now()}] ***** {stop} *****")
