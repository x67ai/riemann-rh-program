#!/usr/bin/env python3
"""controls_table.py -- M6 rung 1: assemble the V.4 control table from the on-disk outputs (every number to its file).
Prime/coefficient side: W_rhs = pole + ARCH - P  (Lean `literatureRHS`; pole = ghat(i/2) + ghat(-i/2), zeta only).
Zero side: W_zero from zero_side_zeta.json (own transform at 30-40 digits) and zero_side_dh.json (record and FULL configurations).
Error budget per (t, L): (i) sieve/Lambda exactness (integer sieve: exact; Lambda_DH recursion: witnesses to 12 digits), (ii) the phase
(dd vs double difference, P_dd_minus_P_double), (iii) A(v) interpolation (interp-vs-quad checks), (iv) the archimedean quadrature
(h- and H-convergence), (v) the pole term (computed / bounded), (vi) zero-side truncation (tail bounds) and zero precision.
"""
import json, os, math, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
def now(): return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ld = lambda f: json.load(open(os.path.join(HERE, 'out', f)))
arch = ld('ef_rhs_arch.json'); zz = ld('zero_side_zeta.json')
try: zd = ld('zero_side_dh.json')
except FileNotFoundError: zd = None
rows = []
print(f"[{now()}] V.4 controls, prime/coefficient side against the zero side")
print("  kind      t        L   |   pole term      ARCH (arch. integral)   P (twisted sum)        W_rhs = pole + ARCH - P   |   W_zero                    |  W_rhs - W_zero   budget")
for kind, tkey, tag_rs, tzero in [('zeta', 't85.6993', 'zeta_t85p7', 85.7), ('zeta', 't1e+06', 'zeta_t1e6', 1e6), ('dh', 't85.6993', 'dh_t85p7', 85.7)]:
    for L in (10, 20):
        a = arch['arch'][f"{kind}_{tkey}_L{L}"]; rs = ld(f"{tag_rs}_L{L}.json")
        if kind == 'zeta' and tzero == 85.7: pole = arch['pole'][f"zeta_t85.7_L{L}"]['pole_term_2Re']; pole_note = 'computed'
        elif kind == 'zeta': pole = 0.0; pole_note = f"bounded: 10^{arch['pole'][f'zeta_t1e6_L{L}']['log10_lemmaG_bound_on_pole_term']:.0f}"
        else: pole = 0.0; pole_note = 'none (DH entire)'
        W_rhs = pole + a['arch'] - rs['P_dd']
        if kind == 'zeta':
            zs = zz['t85'][str(float(L))] if tzero == 85.7 else zz['t1e6'][str(L)]
            W_zero = float(zs['W_total']) if 'W_total' in zs else float(zs['W_direct'])
            tail = float(zs['tail_bound']); zero_note = f"{zs['n_zeros']} zeros, tail <= {tail:.1e}"
            W_zero_full = W_zero; W_zero_record = W_zero
        else:
            if zd is None: W_zero = float('nan'); W_zero_full = W_zero_record = float('nan'); zero_note = 'zero_side_dh.json pending'; tail = float('nan')
            else:
                r = zd['rows'][str(L)]; W_zero_full = float(r['W_full']); W_zero_record = float(r['W_record']); W_zero = W_zero_full
                tail = float(r['tail_online_bound']) + float(r['tail_offline_beyond_900_bound'])
                zero_note = f"FULL config (argument-principle count {'matches' if not zd['argument_principle']['mismatch'] else 'MISMATCH'}), record config {W_zero_record:.10f}, tails <= {tail:.1e}"
        # the error budget: sum of the stated pieces
        phase = abs(rs['P_dd_minus_P_double'])            # the double phase's error; the dd phase's own error is < 1e-24 (dd-log self-test 2e-31 x t)
        interp = max(abs(x[3]) for x in rs['A_interp_check'])*rs['l1_norm']/max(abs(rs['A0']), 1)   # relative interpolation error times the l1 mass
        quad = abs(a['conv_h']) + abs(a['conv_H'])
        K = json.load(open(os.path.join(HERE, 'out', 'kernel_derivative_sup.json')))['K_sup_dF']
        zero_prec = (1133*K/L*5.6e-11 if (kind == 'zeta' and tzero == 1e6) else 0.0)   # campaign zeros at dps 15: worst |dgamma| = 5.6e-11 over 20 re-verified (zero_side_zeta.json)
        budget = zero_prec + 1e-24*abs(rs['t']) + 3*interp + 10*quad + (abs(pole) if kind == 'zeta' and tzero == 85.7 else 0) + (tail if not math.isnan(tail) else 0) + 1e-14
        row = dict(kind=kind, t=rs['t'], L=L, pole=pole, pole_note=pole_note, arch=a['arch'], arch_conv_h=a['conv_h'], arch_conv_H=a['conv_H'], P=rs['P_dd'],
                   P_double=rs['P_double'], phase_dd_minus_double=rs['P_dd_minus_P_double'], W_rhs=W_rhs, W_zero=W_zero, W_zero_record=W_zero_record,
                   diff=W_rhs - W_zero, budget=budget, zero_precision_term=zero_prec, n_terms=rs['n_terms'], X=rs['X'], zero_note=zero_note, time_sum_s=rs['time_sum_s'], time_lambda_s=rs['time_lambda_s'])
        rows.append(row)
        print(f"  {kind:5} {rs['t']:10.4f} {L:3d} | {pole:+.3e} ({pole_note[:9]}) {a['arch']:+.15f}  {rs['P_dd']:+.15f}  {W_rhs:+.15f}  |  {W_zero:+.15f}  |  {W_rhs - W_zero:+.2e}   {budget:.1e}   [{zero_note}]")
json.dump(dict(date=now(), rows=rows), open(os.path.join(HERE, 'out', 'controls_table.json'), 'w'), indent=1)
print(f"[{now()}] wrote out/controls_table.json")
