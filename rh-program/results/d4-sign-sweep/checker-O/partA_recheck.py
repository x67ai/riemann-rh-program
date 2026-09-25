#!/usr/bin/env python3
"""D4 Job 2 part B/C session, the part-A re-check of the two changed items (b) eps governance and (f) binary_sha256.
Log: checker-O/logs/partA_recheck_run.log; output checker-O/out/partA_recheck.json. Reads only; edits nothing of Job 1's."""
import json, os, glob, hashlib, subprocess, re, tempfile
from decimal import Decimal, getcontext
getcontext().prec = 60
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); H = os.path.join(ROOT, 'harness'); O = os.path.join(ROOT, 'out')
EPS = 1.0266395604864687e-30
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
R = {}
print('== (b) eps governance ==')
E = json.load(open(os.path.join(H, 'eps_phi.json')))
print('eps_phi.json eps_phi_per_t =', repr(E['eps_phi_per_t']), '| equals proven:', E['eps_phi_per_t'] == EPS)
print('  basis starts:', E['basis'][:60], '| contains BINDING:', 'BINDING' in E['basis'], '| contains PROVEN:', 'PROVEN' in E['basis'])
print('  measured_sample_max:', {k: v for k, v in E['measured_sample_max'].items()})
print('  retired:', E['retired'])
# the binary without --eps-phi
with tempfile.TemporaryDirectory() as td:
    p = subprocess.run([os.path.join(H, 'd4_twisted_sum')], cwd=td, capture_output=True, text=True, timeout=60)
    print('binary run with NO arguments (no --eps-phi): exit code', p.returncode, '| stderr:', p.stderr.strip(), '| stdout bytes', len(p.stdout), '| files written:', os.listdir(td))
    p2 = subprocess.run([os.path.join(H, 'd4_twisted_sum'), '--t', '1e6', '--L', '10', '--out', 'x.json'], cwd=td, capture_output=True, text=True, timeout=60)
    print('binary run with --t 1e6 --L 10 --out x.json, no --eps-phi: exit code', p2.returncode, '| stderr:', p2.stderr.strip()[:300], '| files written:', os.listdir(td))
    R['no_eps_exit'] = [p.returncode, p.stderr.strip(), p2.returncode]
src = open(os.path.join(H, 'd4_twisted_sum.rs')).read()
m = re.search(r'const EPS_PHI_PER_T: f64 = ([0-9.e-]+);', src); print('source EPS_PHI_PER_T =', m.group(1), '| equals proven:', float(m.group(1)) == EPS)
hb, hs = sha(os.path.join(H, 'd4_twisted_sum')), sha(os.path.join(H, 'd4_twisted_sum.rs'))
print('binary on disk', hb, '| source on disk', hs)
ht = open(os.path.join(ROOT, 'hashes.txt')).read().splitlines()
i0 = next(i for i, l in enumerate(ht) if l.startswith('# --- fix pass'))
blk = ht[i0:i0 + 12]
print('hashes.txt fix-pass block header:', blk[0][:100])
for l in blk[1:]:
    if l.startswith('#'): break
    print('   ', l[:130])
print('binary in fix-pass block:', any(l.startswith(hb) and l.endswith('harness/d4_twisted_sum') for l in blk), '| source in block:', any(l.startswith(hs) and l.endswith('d4_twisted_sum.rs') for l in blk))
# own l1 from twsumO outputs (sum over all n <= X of |w_n|, w_n = 2 Lambda(n) n^-1/2 L^-3 A(log n / L), exact sieve)
l1 = {}
l1['20'] = json.load(open(os.path.join(HERE, 'out', 'zetaO_t1e12_L20.json')))['l1']
l1['22'] = json.load(open(os.path.join(HERE, 'out', 'replayOB_t3000175332800_L22.json')))['l1']
l1['28.35'] = json.load(open(os.path.join(HERE, 'out', 'zetaO_t3000175332900_L28.35.json')))['l1']
tc = {}
for L, v in l1.items():
    tc[L] = 1e-8 / (EPS * v); print(f'own l1(L = {L}) = {v!r} (twsumO, exact sum of |w_n| over n <= X) -> t_ceil = 1e-8/(eps*l1) = {tc[L]:.4e}')
print('  plan l1_used:', E['l1_used'], '| plan t_ceil:', E['t_ceil'])
P = json.load(open(os.path.join(H, 'sweep_plan.json')))
lad = {e['k']: e for e in P['tier1']}
t2 = {e['t_exact']: e for e in P['tier2']}; t2r = {e['t_exact']: e for e in P['tier2_refused']}
print('plan tier1 entries with phase_line_L22 and accepted:', sum(('phase_line_L22' in e and 'accepted' in e) for e in P['tier1']), '/', len(P['tier1']), '; accepted', sum(e['accepted'] for e in P['tier1']))
print('plan tier1 controls with line and accepted:', [(e['t_exact'], e['phase_line_L22'], e['accepted']) for e in P['tier1_controls']])
print('plan tier2 entries:', [(e['t_exact'], f"{e['phase_line_L28.35']:.3e}", e['accepted']) for e in P['tier2']])
print('plan tier2_refused:', [(e['t_exact'], f"{e['phase_line_L28.35']:.3e}", e['accepted']) for e in P['tier2_refused']])
for k in (117, 118):
    t = int(lad[k]['t_exact']); line = EPS * t * l1['28.35']
    print(f'ladder k = {k}: t = {t}; own line at L = 28.35 = {line:.4e} -> {"accepted" if line <= 1e-8 else "REFUSED"}')
line20 = EPS * 1e20 * l1['28.35']; print(f't = 1e20 at L = 28.35: own line {line20:.4e} -> {"accepted" if line20 <= 1e-8 else "REFUSED"}')
mx = max(EPS * int(e['t_exact']) * l1['22'] for e in P['tier1'] + P['tier1_controls']); print(f'largest own tier-1 line at L = 22: {mx:.4e}')
# the ladder heights round(PT*10^(k/16)) as doubles
PT = 3000175332800; bad = []
for k in range(121):
    v = int(float(round(Decimal(PT) * (Decimal(10) ** (Decimal(k) / 16)))))
    if str(v) != lad[k]['t_exact']: bad.append((k, v, lad[k]['t_exact']))
print('ladder recomputed round(PT*10^(k/16)) -> nearest double, k = 0..120: mismatches', bad)
# every landed JSON: eps and phase line
print('-- landed JSONs: eps_phi_per_t_used and phase_line = eps*t*l1_norm --')
Z = sorted(p for p in glob.glob(os.path.join(O, 'zeta_t*_L*.json')) if not p.endswith('.sidecar.json'))
rows = []
for p in Z:
    J = json.load(open(p)); t = int(J['t_exact']); L = J['L']
    sc = p.replace('.json', '.sidecar.json'); S = json.load(open(sc)) if os.path.exists(sc) else None
    e = J['eps_phi_per_t_used']; line_rec = J['phase_line']; line_calc = e * t * J['l1_norm']
    ok_rec = abs(line_rec - line_calc) <= 1e-12 * max(line_calc, 1e-300)
    line_proven = EPS * t * J['l1_norm']
    prov = (e == EPS) or (S is not None and S['eps_phi_per_t_proven'] == EPS and abs(S['phase_line_eps_proven'] - line_proven) <= 1e-12 * line_proven)
    # the binary's own printed line in the sum JSON (6 significant digits)
    sj = json.load(open(os.path.join(O, J['sum_json']))) if J.get('sum_json') and os.path.exists(os.path.join(O, J['sum_json'])) else {}
    sline = sj.get('phase_line'); seps = sj.get('eps_phi_per_t')
    ok_sum = (sline is None) or (float(f'{line_rec:.6e}') == sline)
    rows.append(dict(f=os.path.basename(p), t=t, L=L, eps=e, eps_is_proven=(e == EPS), sidecar=bool(S), proven_ok=prov, line_rec=line_rec, line_matches=ok_rec, sum_line=sline, sum_eps=seps, sum_line_matches=ok_sum,
                     tier=J.get('tier'), bin=J.get('binary_sha256'), bin_ran=J.get('binary_sha256_ran'), hashed_at=J.get('binary_hashed_at'), sum_reused=J.get('sum_reused')))
sw = [r for r in rows if r['tier'] in ('1', '2', 1, 2)]; rh = [r for r in rows if r not in sw]
print('landed zeta JSONs:', len(rows), '| sweep (tier 1/2):', len(sw), '| other (rehearsal):', len(rh), [ (r['t'], r['L']) for r in rh])
print('sweep JSONs with eps_phi_per_t_used == proven:', sum(r['eps_is_proven'] for r in sw), '; not:', [(r['t'], r['L'], r['eps']) for r in sw if not r['eps_is_proven']])
print('all 133: phase_line == eps_used*t*l1_norm (rel 1e-12):', sum(r['line_matches'] for r in rows), '/', len(rows), '; failures', [(r['t'], r['L']) for r in rows if not r['line_matches']])
print('all 133: proven line present (in the JSON or its sidecar) and equal to eps_proven*t*l1_norm:', sum(r['proven_ok'] for r in rows), '/', len(rows), '; failures', [(r['t'], r['L']) for r in rows if not r['proven_ok']])
print('binary-printed phase line (sum JSON, 6 digits) equals the JSON line to 6 digits:', sum(r['sum_line_matches'] for r in rows), '/', len(rows), '; no sum line:', sum(r['sum_line'] is None for r in rows), '; failures', [(r['t'], r['L'], r['sum_line'], r['line_rec']) for r in rows if not r['sum_line_matches']])
print('sum JSON eps_phi_per_t values over the sweep:', sorted(set(str(r['sum_eps']) for r in sw)))
print('-- sidecars --')
for sc in sorted(glob.glob(os.path.join(O, 'zeta_t*.sidecar.json'))):
    S = json.load(open(sc)); tgt = os.path.join(O, S['sidecar_of']); J = json.load(open(tgt))
    t = int(J['t_exact']); pl = EPS * t * J['l1_norm']
    print(f"{os.path.basename(sc)}: of-sha matches file {S['sidecar_of_sha256'] == sha(tgt)}; eps_run {S['eps_phi_per_t_used_in_run']:.4e} == JSON {S['eps_phi_per_t_used_in_run'] == J['eps_phi_per_t_used']}; line_proven {S['phase_line_eps_proven']:.4e} (own {pl:.4e}); refused {S['refused_eps_proven']}; budget run/proven {S['budget_total_in_run']:.4e}/{S['budget_total_eps_proven']:.4e} (rel change {(S['budget_total_eps_proven']-S['budget_total_in_run'])/S['budget_total_in_run']:.1e}); W == JSON {S['W'] == J['W']}; tol {S['control1_tolerance_eps_proven']:.10e}; binary annotation keys {list(S.get('binary_hash_annotation', {}).keys())}")
print('== (f) binary_sha256 ==')
from collections import Counter
print('sweep JSONs by binary_sha256:', Counter(r['bin'][:16] for r in sw))
print('sweep JSONs whose binary_sha256 != 2be891b6...:', [(r['t'], r['L'], r['bin'][:16], r['hashed_at']) for r in sw if r['bin'] != hb])
print('sweep JSONs with binary_hashed_at "launch...":', sum(bool(r['hashed_at']) and r['hashed_at'].startswith('launch') for r in sw), '; sum_reused True:', [(r['t'], r['L']) for r in sw if r['sum_reused']])
print('rehearsal JSONs:', [(r['t'], r['L'], r['bin'][:16], (r['bin_ran'] or '')[:16]) for r in rh])
code = open(os.path.join(H, 'd4_point.py')).read().splitlines()
for i, l in enumerate(code, 1):
    if 'bin_sha_launch' in l: print(f'd4_point.py line {i}: {l.strip()[:170]}')
for i, l in enumerate(code, 1):
    if 'run_watched' in l or "subprocess" in l and 'BIN' in l:
        print(f'd4_point.py line {i} (a binary call): {l.strip()[:150]}'); 
json.dump(dict(l1=l1, t_ceil=tc, rows=rows), open(os.path.join(HERE, 'out', 'partA_recheck.json'), 'w'), indent=1)
