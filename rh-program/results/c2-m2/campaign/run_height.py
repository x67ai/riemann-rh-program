#!/usr/bin/env python3
"""run_height.py -- one height of the zero-side numerics campaign for Theorem M2 (PRICING.md section 2; BRIEF.md rule 2-3).
INSTRUMENT (standing order 4): the tables decide constants and the detection-bandwidth law; nothing about RH.

usage: python3 run_height.py --t 1e3 --tag t1e3 [--selftest] [--direct-cap 60] [--check-1e6-cost]
writes (all under results/c2-m2/campaign/):  zeros_<tag>.json, rows_<tag>.csv, rows_<tag>.json, summary_<tag>.json,
logs/height_<tag>.log (a progress line every 500 zeros; date stamps; the four stop conditions of PRICING 2(e) quoted).
"""
import sys, os, json, math, time, argparse, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np, mpmath as mp
import campaign_lib as cl

ap = argparse.ArgumentParser()
ap.add_argument('--t', type=float, required=True)
ap.add_argument('--tag', required=True)
ap.add_argument('--selftest', action='store_true', help='rehearsal: transform self-tests, envelope fit, derivative norms, bump-only crossing')
ap.add_argument('--direct-cap', type=int, default=60, help='max number of direct E_- evaluations (rows with estimate >= 1e-160)')
ap.add_argument('--check-1e6-cost', action='store_true', help='stop condition (i): time zetazero at n ~ 1.75e6')
ap.add_argument('--window-factor', type=float, default=2.0, help='U_data = factor * U_kopt(L_min = 4)')
args = ap.parse_args()
t = args.t; tag = args.tag
os.makedirs(os.path.join(HERE, 'logs'), exist_ok=True)
logf = open(os.path.join(HERE, 'logs', 'height_%s.log' % tag), 'a')
def log(s):
    print(s, flush=True); logf.write(s + '\n'); logf.flush()
T0 = time.time()
log("=" * 120)
log("[%s] run_height.py START  t = %g  tag = %s  (mp.dps = 15 for zeros; numpy %s; mpmath %s)" % (cl.now(), t, tag, np.__version__, mp.__version__))
log("INSTRUMENT: this run decides constants and the detection-bandwidth law of the first-order datum on zeta's zeros; nothing here is about RH.")
summary = dict(t=t, tag=tag, date_start=cl.now(), record_constants=dict(b1=cl.B1, C1_zeta=cl.C1_ZETA, c_B=cl.C_B, C_B=cl.CB_BIG, R0=cl.R0,
               lambda0=cl.LAMBDA0, C0=cl.C0, refl_c=cl.REFL_C, normBprime_L2sq=cl.NORM_BPRIME_L2SQ, Z=cl.Z_TRAP, envelope_A=cl.ENVELOPE_A))

# ---------------------------------------------------------------------------------------------------------------- self-tests
if args.selftest:
    log("\n(S) SELF-TESTS of the one code path (rehearsal only)")
    with mp.workdps(30):
        Zq = mp.quad(lambda v: mp.exp(-1/(1-4*v*v)), [-0.5, -0.25, 0, 0.25, 0.5])
        log("   Z by 30-digit quadrature = %s ; Z by the M = %d trapezoid = %.16f ; |diff| = %.1e" % (mp.nstr(Zq, 17), cl.M_NODES, cl.Z_TRAP, abs(cl.Z_TRAP - float(Zq))))
        worst = 0.0
        for eta in (0, 4.6727, 20, 100, 500, 3000, 20000, 39000):
            n = max(8, int(abs(eta))//3 + 8); pts = [-mp.mpf(1)/2 + mp.mpf(k)/n for k in range(n+1)]
            ref = mp.quad(lambda v: mp.exp(-1/(1-4*v*v))*mp.cos(eta*v), pts)/Zq
            val = float(cl.bhat_real([eta])[0]); worst = max(worst, abs(val - float(ref)))
            log("   Bhat(%g): trapezoid %.16e  quad %s  |diff| %.1e" % (eta, val, mp.nstr(ref, 17), abs(val - float(ref))))
        log("   -> max absolute difference over the eight points: %.1e (the datum's accuracy floor per term is ~2u|Bhat|*this)" % worst)
        summary['selftest_bhat_max_absdiff'] = worst
        worstc = 0.0
        for lam in (0, 5, 25, 100, 317):
            ref = mp.quad(lambda v: mp.exp(-1/(1-4*v*v))*mp.cosh(lam*v), [-0.5, -0.25, 0, 0.25, 0.5])/Zq
            val = float(cl.c_edge([lam])[0]); rel = abs(val - float(ref))/float(ref); worstc = max(worstc, rel)
            log("   c(%g): trapezoid %.15e  quad %s  rel %.1e" % (lam, val, mp.nstr(ref, 16), rel))
        summary['selftest_c_max_reldiff'] = worstc
    # envelope of |Bhat| at large eta (for the [computed envelope, not proved] estimates of E_- and the reflected points)
    log("   envelope of |Bhat(eta)| at large eta by bhat_mp (Poisson-trapezoid in mpmath, nodes recomputed at 3/2 M as a check):")
    env = {}
    for eta in (500, 1000, 2000, 5000, 10000, 20000, 50000):
        guess = math.exp(cl.log_env(eta))*1e-4
        vals = []; d0 = None
        for sh in (0, 1.0, 2.0, 3.0, 4.0, 5.0):
            r = cl.bhat_mp(mp.mpc(eta + sh, 0), guess, max_work=2e8, check=(sh == 0))
            if sh == 0: d0 = r[3]; Mn, dpsn = r[1], r[2]
            vals.append(abs(r[0]))
        e = float(max(vals)); rate = -math.log(e)/math.sqrt(eta); A = e*eta**0.75*math.exp(math.sqrt(eta/2))
        env[eta] = dict(envelope=e, local_rate=rate, A_fit=A, check_diff=float(d0), M=Mn, dps=dpsn)
        log("   eta=%6d: max|Bhat| over [eta, eta+5] = %.4e  local rate -ln/sqrt(eta) = %.4f  A in A eta^-3/4 e^-sqrt(eta/2) = %.3f  (M=%d dps=%d, 3/2-M check diff %.1e)" % (eta, e, rate, A, Mn, dpsn, float(d0)))
    log("   -> the library's ENVELOPE_A = %.1f (saddle-point form; the record's 'rate 0.849' is the pre-asymptotic local rate at eta ~ 256-8192; asymptotic rate 1/sqrt2 = 0.7071) [computed envelope, not proved]" % cl.ENVELOPE_A)
    summary['envelope'] = {str(k): v for k, v in env.items()}
    # derivative norms
    t1 = time.time(); nm = cl.derivative_norms(13)
    dev = max(abs(nm[k]/cl.DERIV_NORMS_RECORD[k] - 1) for k in nm)
    log("   ||B^(k)||_1, k = 1..13, recomputed in %.1f s: %s" % (time.time() - t1, ", ".join("%d: %.9g" % (k, nm[k]) for k in sorted(nm))))
    log("   -> against the stored table: max relative deviation %.1e; k = 1, 2, 3 against the record (3.31428, 28.7726, 642.301): %.6f %.5f %.4f" % (dev, nm[1], nm[2], nm[3]))
    summary['derivative_norms'] = nm; summary['derivative_norms_max_reldev'] = dev
    # bump-only crossing (PRICING 2(d) item 3): least lambda with 2 c(lambda)^2 >= e^{lambda/2}
    lams = np.arange(10, 40, 0.1); cc = cl.c_edge(lams); cross = float(lams[np.argmax(2*cc*cc >= np.exp(lams/2))])
    log("   bump-only crossing: least lambda (step 0.1) with 2 c(lambda)^2 >= e^(lambda/2) = %.1f  (zero_data_cost_run.log (h): 18.6; proved from 23; contract lambda0 = 25)" % cross)
    summary['bump_only_crossing'] = cross

# ------------------------------------------------------------------------------------------------- stop condition (i) probe
if args.check_1e6_cost:
    log("\n(i) STOP CONDITION (i) PROBE: zetazero at n ~ 1.75e6")
    with mp.workdps(15):
        t1 = time.time(); g = None
        for n in range(1747146, 1747151): g = mp.zetazero(n).imag
        per = (time.time() - t1)/5
    log("   [%s] 5 consecutive zeros at n = 1747146..1747150 (gamma = %s): %.3f s per zero  (threshold 2 s: %s)" % (cl.now(), mp.nstr(g, 12), per, "FIRES" if per > 2 else "does not fire"))
    summary['stop_i_seconds_per_zero_1e6'] = per; summary['stop_i_fires'] = bool(per > 2)

# ---------------------------------------------------------------------------------------------------------------- zeros
L_min = min(cl.L_GRID)
Uk4, k4 = cl.U_kopt(L_min, t)
U_data = args.window_factor*Uk4
log("\n(Z) ZEROS: truncation radius at L_min = %g for absolute tail <= 1e-10 (k-optimized polynomial route, C1 = 1 operative): U = %.2f (k = %d); the contract's k = 3 radius would be %.1f (%.0f zeros against %.0f)"
    % (L_min, Uk4, k4, cl.U_contract3(L_min, t), cl.N_rvm(t + cl.U_contract3(L_min, t)) - cl.N_rvm(max(t - cl.U_contract3(L_min, t), 14)), cl.N_rvm(t + Uk4) - cl.N_rvm(max(t - Uk4, 14))))
log("   data window: U_data = %g x U = %.2f  ->  [%.2f, %.2f]; expected zeros (RvM) %.0f" % (args.window_factor, U_data, t - U_data, t + U_data, cl.N_rvm(t + U_data) - cl.N_rvm(max(t - U_data, 14))))
log("   [%s] fetching zeros with mpmath.zetazero at mp.dps = 15 (progress every 500) ..." % cl.now())
zs, zchk = cl.fetch_zeros(t, U_data, log=log, progress_every=500)
zpath = os.path.join(HERE, 'zeros_%s.json' % tag)
json.dump(dict(t=t, U_data=U_data, dps=15, date=cl.now(), checks=zchk, columns=["index", "gamma", "abs_Z_gamma_siegelz"], zeros=zs), open(zpath, 'w'), indent=0)
log("   written %s (%d zeros; sha256 %s)" % (zpath, len(zs), cl.sha256(zpath)))
summary['zeros'] = dict(count=len(zs), U_data=U_data, U_kopt_Lmin=Uk4, k_opt_Lmin=k4, checks=zchk, file=os.path.basename(zpath), sha256=cl.sha256(zpath))
if not zchk['monotone']:
    log("   !! zeros not monotone in the index -- STOP this leg (mis-identified zero)"); sys.exit(2)
if abs(zchk['count'] - zchk['rvm_expected']) > 6 + 0.5*math.log(t):
    log("   !! zero count differs from the RvM count by more than the S(T)-type allowance -- STOP this leg"); sys.exit(2)
gammas = np.array([z[1] for z in zs])

# ------------------------------------------------------------------------------------------------------------------ rows
log("\n(R) ROWS on the L-grid %g..%g step 2 plus the record points L*(delta, t; C1 = 1) and L*(delta, t; C1 = 2.4e9), delta in %s" % (cl.L_GRID[0], cl.L_GRID[-1], cl.DELTAS))
for d in cl.DELTAS:
    log("   delta = %.2f: L*(C1 = 1) = %.3f, L*(C1 = 2.4e9) = %.3f, transcript L_ann = %.2f, reflection condition t >= 21 L holds for L <= %.1f" % (d, cl.Lstar(d, t, 1), cl.Lstar(d, t, cl.C1_ZETA), cl.L_ann(d, t), t/cl.REFL_C))
t1 = time.time()
rows = cl.compute_rows(t, gammas, U_data, log=log)
log("   [%s] %d rows computed in %.1f s" % (cl.now(), len(rows), time.time() - t1))
# direct E_- where the envelope estimate is >= 1e-160 (feasible at t = 1e3, small L; item (7))
ndirect = 0; t1 = time.time()
for r in rows:
    if r['E_minus_est_log10'] >= -160 and ndirect < args.direct_cap and r['L'] in cl.L_GRID:
        Em, Mn, dpsn = cl.E_minus_direct(t, r['delta'], r['L'])
        if Em is not None:
            r['E_minus_direct'] = Em; r['E_minus_direct_M'] = Mn; r['E_minus_direct_dps'] = dpsn; ndirect += 1
log("   direct E_- (bhat_mp at -2tL - i delta L) at %d rows in %.1f s; elsewhere the clause-1 bound and the envelope estimate are the record" % (ndirect, time.time() - t1))
# per-row printout (compact)
log("\n   t=%g  columns: delta L | inside(L>=L*,t>=21L) reflOK dL>=25 | n_used U_row tail(U_row) U_k3 | N_Z=W_Z'  model  N/model  cl4bound cl4/N | c(dL) main W_Z W_Zrep | cl6bound sep/cl6 sign bal3 | log10|E-|bound log10|E-|est E-direct" % t)
for r in rows:
    log("   %.2f %7.2f | %-5s %-5s %-5s | %4d %7.2f %.1e %8.1f | %.6e %.3e %7.3f %.3e %8.2f | %.6e %.6e %.6e %.6e | %.4e %9.4g %-5s %-5s | %7.1f %7.1f %s"
        % (r['delta'], r['L'], r['inside_hypotheses'], r['reflection_ok'], r['deltaL_ge_25'], r['n_zeros_used'], r['U_row'], r['tail_bound_at_U_row'], r['U_contract_k3'],
           r['N_Z'], r['density_model'], r['N_over_model'], r['clause4_bound_C1_1'], r['clause4_over_N'], r['c_deltaL'], r['main_term'], r['W_Z'], r['W_Zrep'],
           r['clause6_bound'], r['sep_over_clause6'], r['W_Z_negative'], r['bal3'], r['E_minus_bound_log10'], r['E_minus_est_log10'],
           ("%.3e" % r['E_minus_direct']) if r['E_minus_direct'] is not None else "-"))
log("   (rows with inside = False are MEASUREMENTS BELOW THE THEOREM'S HYPOTHESES -- where visibility begins -- not tests of the theorem; IV.9 / MAJOR-2 discipline)")
prefix = os.path.join(HERE, 'rows_%s' % tag)
cl.write_rows(rows, prefix)
log("   written %s.csv / .json (sha256 %s / %s)" % (prefix, cl.sha256(prefix + '.csv'), cl.sha256(prefix + '.json')))
summary['rows'] = dict(count=len(rows), csv=os.path.basename(prefix + '.csv'), json=os.path.basename(prefix + '.json'), sha256_csv=cl.sha256(prefix + '.csv'), sha256_json=cl.sha256(prefix + '.json'))

# ------------------------------------------------------------------------------------------------------------ fine scan
log("\n(F) DERIVED BANDWIDTHS on the fine L-grid 3.0..120 step 0.1: L_sign = least L with W_Z < 0 (= 2 delta^2 c^2 > N_Z; E_- excluded), L_bal3 = least L with 2 delta^2 c^2 >= 3 N_Z")
t1 = time.time(); fs = cl.fine_scan(t, gammas, U_data)
log("   [%s] fine scan done in %.1f s (%d L-values)" % (cl.now(), time.time() - t1, len(fs['L_grid'])))
lt = math.log(t/(2*math.pi))
for d in cl.DELTAS:
    p = fs['per_delta'][str(d)]
    log("   delta = %.2f: L_sign = %s (flips after: %s; at grid bottom: %s)   L_bal3 = %s (flips after: %s)   | density model L_bal(k=1)/L_bal(k=3) from zero_data_cost: see aggregate; transcript L_ann = %.2f; theorem L* = %.1f"
        % (d, p['L_sign'], p['L_sign_flips_after'], p.get('L_sign_at_grid_bottom'), p['L_bal3'], p['L_bal3_flips_after'], cl.L_ann(d, t), cl.Lstar(d, t, 1)))
summary['derived'] = fs['per_delta']
json.dump(dict(t=t, L_grid=fs['L_grid'], N_Z=fs['N_Z']), open(os.path.join(HERE, 'finescan_%s.json' % tag), 'w'))

# ------------------------------------------------------------------------------------------------------------- controls
log("\n(C) V.4 CONTROLS at t = %g (both, before any number is quoted)" % t)
minWp = min(r['W_Zprime'] for r in rows); argmin = min(rows, key=lambda r: r['W_Zprime'])
log("   POSITIVE control (zeta's zeros, all real; the channel must stay silent): min over all rows of W_Z' = %.6e at L = %g  -> %s" % (minWp, argmin['L'], "PASS (>= 0)" if minWp >= 0 else "FAIL (< 0): STOP CONDITION (ii) FIRES"))
viol = [r for r in rows if r['clause4_asserted'] and r['W_Zprime'] > r['clause4_bound_C1_1']]
log("   POSITIVE control against the clause-4 bound 2 b1 l_R/L^2 (asserted for L >= 50): %d violations of %d asserted rows -> %s" % (len(viol), sum(1 for r in rows if r['clause4_asserted']), "PASS" if not viol else "FAIL"))
finemin = min(fs['N_Z'])
log("   POSITIVE control on the fine grid (1171 L-values): min N_Z = %.3e -> %s" % (finemin, "PASS" if finemin >= 0 else "FAIL"))
neg_ok = True
for d in cl.DELTAS:
    Ls = fs['per_delta'][str(d)]['L_sign']
    rr = [r for r in rows if r['delta'] == d]
    after = [r for r in rr if Ls is not None and r['L'] >= Ls]
    allneg = all(r['W_Z_negative'] for r in after)
    rec = [r for r in rr if r['is_record_point_C1_1'] or r['is_record_point_C1_zeta']]
    ratio_ok = all(r['sep_over_clause6'] >= 1 for r in rec)
    neg_ok = neg_ok and allneg and ratio_ok
    log("   NEGATIVE control (the planted orbit at depth %.2f is the injected defect; the channel must fire): W_Z < 0 at every grid row L >= L_sign = %s: %s; ratio |W_Z - W_Z'|/(delta^2 e^{delta L/2}) >= 1 at the record points: %s (%s)"
        % (d, Ls, allneg, ratio_ok, ", ".join("L=%.1f: %.3g" % (r['L'], r['sep_over_clause6']) for r in rec)))
log("   -> NEGATIVE control %s; POSITIVE control %s" % ("PASS" if neg_ok else "FAIL", "PASS" if (minWp >= 0 and not viol and finemin >= 0) else "FAIL"))
summary['controls'] = dict(positive_min_W_Zprime=minWp, positive_min_at_L=argmin['L'], positive_clause4_violations=len(viol), positive_fine_min=finemin, negative_pass=neg_ok,
                           positive_pass=bool(minWp >= 0 and not viol and finemin >= 0))

# ------------------------------------------------------------------------------------------------------- stop conditions
log("\n(X) STOP CONDITIONS of PRICING 2(e), quoted and checked:")
grid_rows = [r for r in rows if r['delta'] == cl.DELTAS[0] and r['L'] in cl.L_GRID]
ratios = np.array([r['N_over_model'] for r in grid_rows]); Lg = np.array([r['L'] for r in grid_rows])
gm = float(np.exp(np.mean(np.log(ratios)))); out10 = int(np.sum((ratios > 10) | (ratios < 0.1))); out10_le50 = int(np.sum(((ratios > 10) | (ratios < 0.1)) & (Lg <= 50)))
s_i = summary.get('stop_i_seconds_per_zero_1e6', None)
log("   (i) 'zetazero at n ~ 1.75e6 exceeds 2 s per zero on this machine in the rehearsal (data cost x7 -- reprice the L-grid's bottom)': %s"
    % (("measured %.3f s/zero -> %s" % (s_i, "FIRES" if s_i > 2 else "does not fire")) if s_i is not None else "not probed in this run (probed in the rehearsal); this height's own rate %.3f s/zero" % zchk['seconds_per_zero']))
log("   (ii) 'the rehearsal's positive control at t = 1e3 shows W_Z' < 0 at any L (an on-line configuration cannot give a negative datum)': min W_Z' = %.3e over %d rows and %d fine-grid L -> %s" % (min(minWp, finemin), len(rows), len(fs['N_Z']), "FIRES" if min(minWp, finemin) < 0 else "does not fire"))
log("   (iii) 'the checker's independent transform disagrees with the builder's on any row by more than 1e-8 relative': the checker's item (Opus half slot, SHARED.md); not decidable by the builder -- pending")
log("   (iv) 'the density model and the measured N_Z differ by more than a factor 10 at 1e3 (then the model is wrong and 2(d) item 2's inference is withdrawn)': N_Z/model over the %d grid rows: min %.3f, max %.3f, geometric mean %.3f; rows outside [0.1, 10]: %d (of which %d at L <= 50) -> %s"
    % (len(grid_rows), ratios.min(), ratios.max(), gm, out10, out10_le50, "FIRES" if (gm > 10 or gm < 0.1 or out10_le50 > 0) else "does not fire"))
summary['stop_conditions'] = dict(i_seconds_per_zero_1e6=s_i, ii_min_W_Zprime=min(minWp, finemin), iii="pending checker", iv=dict(min=float(ratios.min()), max=float(ratios.max()), geomean=gm, outside_10x=out10, outside_10x_L_le_50=out10_le50),
                                  any_fires=bool((s_i is not None and s_i > 2) or min(minWp, finemin) < 0 or gm > 10 or gm < 0.1 or out10_le50 > 0))
summary['date_end'] = cl.now(); summary['seconds'] = time.time() - T0
spath = os.path.join(HERE, 'summary_%s.json' % tag)
json.dump(summary, open(spath, 'w'), indent=1, default=float)
log("\n[%s] run_height.py DONE  t = %g  in %.1f s  (summary %s; any stop condition fires: %s)" % (cl.now(), t, time.time() - T0, os.path.basename(spath), summary['stop_conditions']['any_fires']))
