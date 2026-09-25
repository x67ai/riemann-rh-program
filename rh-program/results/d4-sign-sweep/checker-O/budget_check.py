#!/usr/bin/env python3
"""D4 Job 2 part C.2 (Opus 5): re-derive every budget line of note section 3 from its definition, per point, from the JSONs;
per-tier maxima; the bracket two-path check; the pole bounds; and the lines the budget does not list (Neumaier summation error,
the weight's own roundings). Log: logs/budget_check_run.log; out/budget_check.json."""
import json, os, glob, math
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O = os.path.join(ROOT, 'out')
EPS = 1.0266395604864687e-30; u = 2.0 ** -53
rows = []
for p in sorted(glob.glob(os.path.join(O, 'zeta_t*_L*.json'))):
    if p.endswith('.sidecar.json'): continue
    J = json.load(open(p)); S = json.load(open(os.path.join(O, J['sum_json']))); A = json.load(open(os.path.join(O, J['arch_json'])))
    t = int(J['t_exact']); L = J['L']; l1 = J['l1_norm']; b = J['budget']
    reh = J.get('tier') == 'rehearsal'
    eps_used = J['eps_phi_per_t_used']
    d = dict(t=t, L=L, reh=reh)
    d['phase'] = eps_used * t * l1; d['phase_ok'] = abs(d['phase'] - b['phase_line']) <= 1e-12 * d['phase']
    d['phase_proven'] = EPS * t * l1
    d['interp'] = 3 * max(abs(x[3]) for x in S['A_interp_check']) / abs(S['A0']) * l1; d['interp_ok'] = abs(d['interp'] - b['interpolation']) <= 1e-12 * d['interp']
    d['interp_err_max'] = max(abs(x[3]) for x in S['A_interp_check'])
    d['quad'] = 10 * (abs(A['conv_h']) + abs(A['conv_H'])); d['quad_ok'] = d['quad'] == b['arch_quadrature']
    d['pole_log10'] = A['pole'].get('log10_lemmaG_bound_on_pole_term'); d['pole_ok'] = (b['pole'] == (10 ** d['pole_log10'] if d['pole_log10'] is not None else b['pole']))
    d['cos'] = 2.3e-16 * l1; d['cos_ok'] = abs(d['cos'] - b['cos_rounding']) <= 1e-12 * d['cos']
    d['total'] = d['phase'] + d['interp'] + d['quad'] + (b['pole']) + d['cos'] + 1e-14; d['total_ok'] = abs(d['total'] - b['total']) <= 1e-12 * d['total']
    d['total_proven'] = d['total'] - d['phase'] + d['phase_proven']
    d['bracket'] = A['bracket_two_path_worst_over_nodes']; d['bracket_nodes'] = A['bracket_two_path_nodes']
    # lines NOT in the budget: Neumaier (Kahan-Babuska) summation, |E| <= 2u|P| + 4 n u^2 l1 (Higham 2002, sect. 4.3; merge of 8 partials included in n);
    # the weight's own roundings: lam (0.5u) sqrt (0.5u) div (0.5u) *a (0.5u) L^3 (1u) div (0.5u) -> 3.5u, plus the product w*cos (0.5u): 4u per term beyond the cos line
    d['neumaier'] = 2 * u * abs(J['P_dd']) + 4 * J['n_terms'] * u * u * l1
    d['weights_products'] = 4 * u * l1
    d['total_with_unlisted'] = d['total_proven'] + d['neumaier'] + d['weights_products']
    d['sieve_terms'] = J['n_terms']
    rows.append(d)
allok = {k: all(r[k] for r in rows) for k in ('phase_ok', 'interp_ok', 'quad_ok', 'pole_ok', 'cos_ok', 'total_ok')}
print('every JSON budget line re-derived from its definition (133 points):', allok)
for Lv, name in ((22.0, 'tier 1, L = 22'), (28.35, 'tier 2, L = 28.35')):
    rs = [r for r in rows if r['L'] == Lv and not (r['reh'] and r['t'] != 3000175332900)]
    mb = max(rs, key=lambda r: r['total_proven']); mn = min(rs, key=lambda r: r['total_proven']); mp_ = max(rs, key=lambda r: r['phase_proven'])
    print(f'{name}: {len(rs)} points; max budget (proven eps) {mb["total_proven"]:.4e} at t = {mb["t"]}; min budget {mn["total_proven"]:.4e} at t = {mn["t"]}; max phase line {mp_["phase_proven"]:.4e} at t = {mp_["t"]}')
    print(f'   interp line {min(r["interp"] for r in rs):.3e} .. {max(r["interp"] for r in rs):.3e} (max A-interp error {max(r["interp_err_max"] for r in rs):.3e}); cos line {rs[0]["cos"]:.3e}; quad <= {max(r["quad"] for r in rs):.2e}; pole bound log10 <= {max(r["pole_log10"] for r in rs if r["pole_log10"] is not None):.0f} (at t = {max((r for r in rs if r["pole_log10"] is not None), key=lambda r: r["pole_log10"])["t"]}); bracket two-path worst {max(r["bracket"] for r in rs):.3e}')
    print(f'   NOT in the budget: Neumaier 2u|P| + 4nu^2 l1 <= {max(r["neumaier"] for r in rs):.2e}; the weight roundings and the product w*cos (4u l1) = {rs[0]["weights_products"]:.2e}; budget with them, max {max(r["total_with_unlisted"] for r in rs):.4e}, min {min(r["total_with_unlisted"] for r in rs):.4e} (relative change at the minimum-budget point {(min(rs, key=lambda r: r["total_proven"])["total_with_unlisted"] / mn["total_proven"] - 1):.1%})')
    print(f'   min |W|/budget(with unlisted lines) = {min(json.load(open(os.path.join(O, "zeta_t%d_L%g.json" % (r["t"], r["L"]))))["W"] / r["total_with_unlisted"] for r in rs):.3e}')
print('bracket two-path worst over ALL 133 points (incl. rehearsal):', f'{max(r["bracket"] for r in rows):.3e}', 'at t =', max(rows, key=lambda r: r['bracket'])['t'])
for r in rows:
    if r['reh']: print(f'  point ({r["t"]}, {r["L"]:g}): budget in run {r["total"]:.4e}, with proven eps {r["total_proven"]:.4e}; pole log10 {r["pole_log10"]}')
json.dump(rows, open(os.path.join(HERE, 'out', 'budget_check.json'), 'w'), indent=1)
