#!/usr/bin/env python3
"""d4_sidecar_eps_proven.py -- D4 fix pass (CHECK-O-A.md (b), (f)): the landed rehearsal JSONs are NOT re-run and NOT edited.
For each out/zeta_t*_L*.json on disk at the time of the fix pass, write a dated sidecar out/<name>.sidecar.json:
  (b) the phase line recomputed with eps_proven = 1.0266395604864687e-30 (eps * t * l1, the run's own printed l1), the budget total
      recomputed with that line, the refusal flag recomputed (must stay False);
  (f) for out/zeta_t1000000000000_L28.35.json: the key `binary_sha256` (f6256ded..., hashed at assembly by d4_point.py v1) names a
      binary that did NOT run the sum; the sum was produced by harness/d4_twisted_sum.v1 (f97fc582...), recorded in the JSON as
      `binary_sha256_ran`; the sidecar states which key means what. For the other JSONs one build ran throughout.
Each sidecar's hash is appended to hashes.txt."""
import json, glob, os, hashlib, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..')); OUT = os.path.join(ROOT, 'out')
EPS = json.load(open(os.path.join(HERE, 'eps_phi.json')))['eps_phi_per_t']; assert EPS == 1.0266395604864687e-30
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
d = subprocess.run(['date'], capture_output=True, text=True).stdout.strip()
for pj in sorted(glob.glob(os.path.join(OUT, 'zeta_t*_L*.json'))):
    if pj.endswith('.sidecar.json'): continue
    j = json.load(open(pj)); t = float(j['t_exact']); l1 = j['l1_norm']
    line = EPS*t*l1; b = j['budget']; total = line + b['interpolation'] + b['arch_quadrature'] + b['pole'] + b['cos_rounding'] + b['floor']
    sc = dict(date=d, sidecar_of=os.path.basename(pj), sidecar_of_sha256=sha(pj), note="phase line recomputed with eps_proven (fix (b), CHECK-O-A.md section 2(b)); the landed JSON is not edited and the point is not re-run",
              eps_phi_per_t_used_in_run=j['eps_phi_per_t_used'], eps_phi_per_t_proven=EPS, eps_source="checker-O/job1_ddlog_bound.py (bit-exact emulation; a-priori bound)",
              phase_line_in_run=j['phase_line'], phase_line_eps_proven=line, refused_eps_proven=line > j['phase_line_allowance'], budget_total_in_run=b['total'], budget_total_eps_proven=total,
              W=j['W'], W_over_budget_eps_proven=abs(j['W'])/total, control1_tolerance_eps_proven=1e-10 + line)
    if os.path.basename(pj) == 'zeta_t1000000000000_L28.35.json':
        sc['binary_hash_annotation'] = dict(fix="(f), CHECK-O-A.md section 2(f)", binary_sha256_in_json=j['binary_sha256'], meaning_of_binary_sha256_in_json="the binary hashed by d4_point.py v1 at ASSEMBLY time (second build, harness/d4_twisted_sum, f6256ded...): it did NOT run this sum",
              binary_that_ran=j.get('binary_sha256_ran'), meaning_of_binary_that_ran="harness/d4_twisted_sum.v1 (first build, f97fc582...), which produced out/sum_zeta_t1000000000000_L28.35.json via harness/run_bg_rehearsal.sh; the two builds differ only by the --selftest-only flag (source ceeb3a28... vs c1149d54..., hashes.txt)",
              reader_rule="for this JSON read `binary_sha256_ran` as the binary that ran; from the fix pass on, `binary_sha256` in every new JSON is hashed at launch and IS the binary that ran (d4_point.py v2)")
    else:
        sc['binary_hash_annotation'] = dict(binary_sha256_in_json=j['binary_sha256'], note="one build ran this point end to end; the key names the binary that ran")
    sp = pj.replace('.json', '.sidecar.json'); json.dump(sc, open(sp, 'w'), indent=1)
    open(os.path.join(ROOT, 'hashes.txt'), 'a').write(f"{sha(sp)}  out/{os.path.basename(sp)} (fix-pass sidecar, {d})\n")
    print(f"[{d}] {os.path.basename(sp)}: line {j['phase_line']:.3e} -> {line:.3e} (eps_proven), budget {b['total']:.3e} -> {total:.3e}, refused {line > 1e-8}, |W|/budget {abs(j['W'])/total:.2e}")
