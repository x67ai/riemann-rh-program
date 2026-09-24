#!/usr/bin/env python3
"""d4_phase_selftest.py -- D4: the per-height double-double phase self-test (BRIEF (i)(c) and the ladder).
Reads the `phase_selftest` rows [n, log_hi, log_lo, red_hi, red_lo, cos] a d4_twisted_sum JSON printed for N pseudo-random
n <= X, and checks the WHOLE phase path against mpmath at 50 digits:
  log error   = |(log_hi + log_lo) - log n|                                (the dd log alone)
  phase error = |(red_hi + red_lo) - ((t log n) mod 2pi)| taken mod 2pi    (log + exact product + two-stage reduction)
  cos error   = |cos - cos(t log n)|
Pass criterion (BRIEF): max phase error <= 3e-31 * t.  Also printed: the phase error with the log's own error removed
(the product/reduction error alone), so the two contributions are separated.  Appends a block to the JSON's sidecar
out/<name>.selftest.json and a line to harness/d4_phase_selftest_run.log.
usage: d4_phase_selftest.py out/zeta_t<...>_L<...>.json [more JSONs]
"""
import json, sys, os, datetime, time
import mpmath as mp
mp.mp.dps = 50
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
HERE = os.path.dirname(os.path.abspath(__file__))
log = open(os.path.join(HERE, 'd4_phase_selftest_run.log'), 'a')
def out(s):
    print(s); log.write(s + "\n"); log.flush()
twopi = 2*mp.pi
for path in sys.argv[1:]:
    t0 = time.time()
    j = json.load(open(path))
    rows = j.get('phase_selftest', [])
    t = mp.mpf(j['t_exact']) if j.get('t_exact') and j['t_exact'].lstrip('-').isdigit() else mp.mpf(j['t'])
    tf = float(j['t'])
    assert mp.mpf(tf) == t, "t_exact must equal the double t"
    maxlog = maxph = maxph_prodred = maxcos = mp.mpf(0); nmax = None
    for n, lh, ll, rh, rl, c in rows:
        n = int(n)
        logn = mp.log(n)
        dd_log = mp.mpf(lh) + mp.mpf(ll)
        e_log = abs(dd_log - logn)
        phi_true = mp.fmod(t*logn, twopi)
        if phi_true > mp.pi: phi_true -= twopi
        dd_phi = mp.mpf(rh) + mp.mpf(rl)
        d = mp.fmod(dd_phi - phi_true, twopi)
        if d > mp.pi: d -= twopi
        if d < -mp.pi: d += twopi
        e_ph = abs(d)
        # product/reduction alone: compare dd_phi with t * dd_log (the dd log taken as exact input) mod 2pi
        phi_in = mp.fmod(t*dd_log, twopi)
        d2 = mp.fmod(dd_phi - phi_in, twopi)
        if d2 > mp.pi: d2 -= twopi
        if d2 < -mp.pi: d2 += twopi
        e_pr = abs(d2)
        e_cos = abs(mp.mpf(c) - mp.cos(t*logn))
        if e_ph > maxph: maxph = e_ph; nmax = n
        maxlog = max(maxlog, e_log); maxph_prodred = max(maxph_prodred, e_pr); maxcos = max(maxcos, e_cos)
    allow = mp.mpf('3e-31')*t
    ok = maxph <= allow
    eps_measured = float(maxph/t) if t != 0 else 0.0
    res = dict(date=now(), json=os.path.basename(path), t_exact=j.get('t_exact'), L=j['L'], X=j['X'], n_rows=len(rows), seed=j.get('selftest_seed'),
               max_log_error=float(maxlog), max_phase_error=float(maxph), max_phase_error_prod_red_only=float(maxph_prodred), max_cos_error=float(maxcos),
               n_at_max=nmax, allowance_3e31_t=float(allow), pass_=bool(ok), eps_phi_per_t_measured=eps_measured, seconds=time.time()-t0)
    out(f"[{now()}] {os.path.basename(path)}: t = {j.get('t_exact')}, L = {j['L']}, X = {j['X']}, {len(rows)} rows (seed {j.get('selftest_seed')}): "
        f"max |dd log - log n| = {float(maxlog):.3e}; max phase error (whole path, mod 2pi) = {float(maxph):.3e} rad at n = {nmax} "
        f"[product+reduction alone {float(maxph_prodred):.3e}]; max cos error = {float(maxcos):.3e}; allowance 3e-31 t = {float(allow):.3e} -> "
        f"{'PASS' if ok else 'FAIL'}; measured eps_phi/t = {eps_measured:.3e}  ({time.time()-t0:.1f}s)")
    side = path.replace('.json', '.selftest.json')
    json.dump(res, open(side, 'w'), indent=1)
