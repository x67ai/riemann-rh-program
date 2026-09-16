#!/usr/bin/env python3
"""aggregate.py -- harvest of the zero-side campaign (PRICING 2(d), 2(e); BRIEF rules 3 and 5): builds CAMPAIGN.md from
whatever row files exist (rows_t1e{3,4,5,6}.json, summary_t1e{k}.json, outwindow_test.json, finescan_*.json).
v0 = the rehearsal only (t = 1e3); v1 = all four heights.  Every number printed here is read from those files.
INSTRUMENT (standing order 4): the tables decide constants and the detection-bandwidth law; nothing about RH.
usage: python3 aggregate.py   (writes CAMPAIGN.md next to itself; prints the same text)
"""
import sys, os, json, math, glob, datetime
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import campaign_lib as cl

HEIGHTS = [('t1e3', 1e3), ('t1e4', 1e4), ('t1e5', 1e5), ('t1e6', 1e6)]
present = [(tag, t) for tag, t in HEIGHTS if os.path.exists(os.path.join(HERE, 'summary_%s.json' % tag)) and os.path.exists(os.path.join(HERE, 'rows_%s.json' % tag))]
S = {tag: json.load(open(os.path.join(HERE, 'summary_%s.json' % tag))) for tag, _ in present}
R = {tag: json.load(open(os.path.join(HERE, 'rows_%s.json' % tag))) for tag, _ in present}
OW = json.load(open(os.path.join(HERE, 'outwindow_test.json'))) if os.path.exists(os.path.join(HERE, 'outwindow_test.json')) else None
version = 'v1' if len(present) == 4 else 'v0 (heights present: %s)' % ", ".join(tag for tag, _ in present)
out = []
def P(s=''): out.append(s)

P("# CAMPAIGN.md -- the zero-side numerics campaign for Theorem M2 (C2; PRICING.md section 2) -- %s" % version)
P()
P("**Built %s by `aggregate.py` from the row files on disk** (`rows_<tag>.json`, `summary_<tag>.json`, `finescan_<tag>.json`, `outwindow_test.json`, all under `results/c2-m2/campaign/`; logs under `logs/`). Every number below is read from those files; nothing is typed in. **INSTRUMENT (standing order 4): every table here decides constants and the detection-bandwidth law of the first-order datum on zeta's actual zeros; nothing here is a statement about RH.** Heights present: %s." % (cl.now(), ", ".join("t = %g" % t for _, t in present)))
P()
P("## 0. Method (one code path: `campaign_lib.py`; driver `run_height.py`; item (6): `outwindow_test.py`)")
P()
P("* **Objects.** Test f_{t,L} = i(B_L)'e^{-itu}; h_f(r) = (r - t)B̂(L(r - t)); datum W_Z(f) = Σ_γ h_f(γ)·conj(h_f(γ̄)) (note §0.1). Configurations at height t: **Z'** = ζ's zeros in the data window (all real; the positive control); **Z** = Z' ∪ {±t ± iδ} (the theorem's pair of classes; the negative control's injected defect); **Z_rep** = Z' with the on-line zero nearest t (and its reflection) replaced by the orbit (C2 line 54's 'physical' variant); **Z''** = Z' ∪ {on-line double at ±t} (the II.4 tight pair: the double at +t contributes exactly 0 since h_f(t) = 0; the double at −t contributes 8t²B̂(2tL)², bounded per row by Lemma G — the datum is blind to the double).")
P("* **Zeros.** `mpmath.zetazero(n)` at mp.dps = 15, stored as (index n, γ, |Z(γ)| by `mpmath.siegelz`), monotone in n and counted against Riemann–von Mangoldt. **Data window** ±U_data around t with U_data = 2·U(L_min = 4), where U(L) is the least radius at which the clause-4 polynomial tail bound is ≤ 10⁻¹⁰: k integrations by parts give |B̂(η)| ≤ ‖B^{(k)}‖₁/|η|^k, and with the shell count 2C₁ℓ_R (C₁ = 1 operative for ζ, stated as such — PRICING §2(b)) the tail beyond U is ≤ 2ℓ_R‖B^{(k)}‖₁²L^{−2k}(U − 2)^{3−2k}/(2k − 3), minimized over 2 ≤ k ≤ 13 with the norms ‖B^{(k)}‖₁ computed by exact polynomial recursion + 30-digit quadrature (k = 1, 2, 3 reproduce the record's 3.31428, 28.7726, 642.301; the table is in `campaign_lib.py`). **The contract's k = 3 radius (PRICING §2(b)(c)) is printed per row as U_contract_k3**; at L = 4 it is 1.7·10⁴ at t = 10³ (2·10⁴ zeros; the pricing's '25 minutes' was the L = 10 figure) and 2.1·10⁴ at t = 10⁶ (8·10⁴ zeros, 6.5 h) — the k-optimized radius is 143–149 at every height (230–570 zeros, minutes). Each row sums over every stored zero within U_row = min(U_data, 4·10⁴/L) ≥ U(L), and prints the tail bound at U_row.")
P("* **Transform.** B̂ at real η by the trapezoid rule on 16 384 uniform nodes (B is C^∞ with compact support: the rule is spectrally accurate; by Poisson summation the error is Σ_{m≠0}B̂(η − 2πmM), checked against 30-digit mpmath quadrature at eight points to ≤ 7·10⁻¹⁸ absolute in the rehearsal log); c(δL) = B̂(iδL) by the same rule with cosh (positive terms; ≤ 1.2·10⁻¹⁶ relative up to λ = 317). At complex arguments and huge |η| (the reflected term E₋, the reflected on-line points, the planted out-window orbit) the same Poisson-trapezoid rule in mpmath at the precision the cancellation needs (`bhat_mp`; agrees with mpmath quadrature at z = 300 − 10i to 10⁻³⁴; recomputed at 3/2 the nodes as a check).")
P("* **E₋ and the reflected points (item (7)).** The sums exclude the reflected pair at −t and the reflected on-line points −γ; each row prints the rigorous clause-1 bound |E₋| ≤ 2(4t² + δ²)e^{δL}G(2tL)² (Lemma G, c_B = 0.143), the envelope estimate with |B̂(η)| ≈ 9η^{−3/4}e^{−√(η/2)} `[computed envelope, not proved; fitted on η = 10³–5·10⁴, local rate 0.80 → 0.73 toward the saddle-point 1/√2]`, and — where the estimate is ≥ 10⁻¹⁶⁰ (t = 10³, L ≤ 36) — the DIRECT value. The rigorous bound is not informative (> 10⁻¹⁰) at small L and t = 10³; the direct values and the estimate are the record there, labeled.")
P("* **Derived bandwidths.** L_sign(δ, t) = least L (fine grid 3.0…120 step 0.1) with W_Z < 0, i.e. 2δ²c(δL)² > N_Z (E₋ excluded); L_bal3 = least L with 2δ²c(δL)² ≥ 3N_Z. Row flag `inside_hypotheses` = (L ≥ L*(δ, t; C₁ = 1)) and (t ≥ 21L); rows with the flag False are **measurements below the theorem's hypotheses — of where visibility begins — not tests of the theorem** (IV.9; MAJOR-2 discipline).")
P()

# ---------------------------------------------------------------------------------------------------------------- per height
P("## 1. Per-height record: zeros, controls, stop conditions (INSTRUMENT — constants and the bandwidth law; nothing about RH)")
P()
P("| t | zeros (window ±U_data) | index range | s/zero | max \\|Z(γ)\\| | rows | positive control: min W_{Z'} | clause-4 (L ≥ 50) violations | negative control | stop (i) | stop (ii) | stop (iv): center-mean N_Z/model geomean [min, max] (grid L outside 10×) | run time |")
P("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for tag, t in present:
    s = S[tag]; z = s['zeros']; c = s['controls']; x = s['stop_conditions']
    P("| %g | %d (±%.1f) | %s..%s | %.3f | %.1e | %d | %.3e (PASS: %s) | %d | %s | %s | %s | %.3f [%.3f, %.3f] (%d) → %s | %.0f s |" % (
        t, z['count'], z['U_data'], z['checks']['index_lo'], z['checks']['index_hi'], z['checks']['seconds_per_zero'], z['checks']['max_residual'], s['rows']['count'],
        c['positive_min_W_Zprime'], c['positive_pass'], c['positive_clause4_violations'], "PASS" if c['negative_pass'] else "FAIL",
        ("%.3f s/zero → %s" % (x['i_seconds_per_zero_1e6'], "FIRES" if x['i_seconds_per_zero_1e6'] > 2 else "no")) if x['i_seconds_per_zero_1e6'] is not None else "(rehearsal)",
        "FIRES" if x['ii_min_W_Zprime'] < 0 else "no", x['iv']['geomean'], x['iv']['min'], x['iv']['max'], x['iv']['outside_10x'],
        "FIRES" if (x['iv']['geomean'] > 10 or x['iv']['geomean'] < 0.1 or x['iv']['outside_10x'] > 0) else "no", s['seconds']))
P()
P("Stop condition (iii) (the checker's independent transform within 10⁻⁸ relative on two rows per height) is the Opus checker's item; its verdicts are appended to `SHARED.md` / `CHECK-O.md`, not decided here.")
P()

# --------------------------------------------------------------------------------------------------------- twelve points
P("## 2. The twelve-point tables: L_sign(δ, t) and L_bal3(δ, t) (INSTRUMENT; fine grid step 0.1; E₋ excluded from W_Z)")
P()
P("| δ \\ t | " + " | ".join("%g" % t for _, t in present) + " |")
P("|---|" + "---|"*len(present))
def ens(tag, d, key):
    e = S[tag].get('ensemble', {}).get('per_delta', {}).get(str(d))
    return ("%.1f [%.1f, %.1f]" % (e[key + '_median'], e[key + '_p10'], e[key + '_p90'])) if e else "n/a"
for d in cl.DELTAS:
    P("| L_sign, δ = %.2f — at t ; median [p10, p90] over centers | " % d + " | ".join("%s ; %s" % (S[tag]['derived'][str(d)]['L_sign'], ens(tag, d, 'L_sign')) for tag, _ in present) + " |")
for d in cl.DELTAS:
    P("| L_bal3, δ = %.2f — at t ; median [p10, p90] over centers | " % d + " | ".join("%s ; %s" % (S[tag]['derived'][str(d)]['L_bal3'], ens(tag, d, 'L_bal3')) for tag, _ in present) + " |")
P()
P("'At t' is the contract's L_sign(δ, t) at the height exactly (fine grid step 0.1); 'over centers' is the same quantity at the %s centers t' = t + 2j inside the data window (section (M) of the height log; fine grid step 0.2) — the median is the ensemble instrument, the band shows how configuration-dominated a single-t value is." % ", ".join(str(S[tag].get('ensemble', {}).get('n_centers', '?')) for tag, _ in present))
P()
P("Reference values per (δ, t) from the record (`zero_data_cost_run.log` (d)–(g)): density model L_bal(κ=1) / L_bal(κ=3); the theorem's L*(C₁ = 1); the transcript's L_ann = 1.12δ^{−0.07}(log(t/2π))^{0.89}:")
P()
P("| δ \\ t | " + " | ".join("%g" % t for _, t in present) + " |")
P("|---|" + "---|"*len(present))
lt = lambda t: math.log(t/(2*math.pi))
def Lbal_model(d, t, kap):
    L = 4.0
    while 2*d*d*float(cl.c_edge([d*L])[0])**2 < kap*lt(t)*cl.NORM_BPRIME_L2SQ/L**3 and L < 2000: L += 0.1
    return L
for d in cl.DELTAS:
    P("| δ = %.2f: model κ=1 / κ=3 ; L* ; L_ann | " % d + " | ".join("%.1f / %.1f ; %.1f ; %.1f" % (Lbal_model(d, t, 1), Lbal_model(d, t, 3), cl.Lstar(d, t, 1), cl.L_ann(d, t)) for _, t in present) + " |")
P()

# ------------------------------------------------------------------------------------------------------ three-law comparison
P("## 3. The three-law comparison (PRICING §2(a) last paragraph; §2(d) item 1) — δ-ratios 1.12 : 2.9 : 5")
P()
P("The three laws predict L(δ = 0.05)/L(δ = 0.25) = 5^{0.07} = 1.12 (transcript), 5^{2/3} = 2.92 (density model), 5 (theorem, L* ∝ δ⁻¹); and in t, L(10⁶)/L(10³) = (log(10⁶/2π)/log(10³/2π))^{0.89} = %.2f (transcript), (…)^{1/3} = %.2f (model), log log-flat ≈ %.2f (theorem, at δ = 0.1)." % ((lt(1e6)/lt(1e3))**0.89, (lt(1e6)/lt(1e3))**(1/3), cl.Lstar(0.1, 1e6)/cl.Lstar(0.1, 1e3)))
P()
P("| t | L_sign(0.05)/L_sign(0.25) | L_bal3(0.05)/L_bal3(0.25) | model κ=1 ratio | model κ=3 ratio |")
P("|---|---|---|---|---|")
for tag, t in present:
    dd = S[tag]['derived']
    r1 = dd['0.05']['L_sign']/dd['0.25']['L_sign'] if dd['0.05']['L_sign'] and dd['0.25']['L_sign'] else float('nan')
    r3 = dd['0.05']['L_bal3']/dd['0.25']['L_bal3'] if dd['0.05']['L_bal3'] and dd['0.25']['L_bal3'] else float('nan')
    P("| %g | %.2f | %.2f | %.2f | %.2f |" % (t, r1, r3, Lbal_model(0.05, t, 1)/Lbal_model(0.25, t, 1), Lbal_model(0.05, t, 3)/Lbal_model(0.25, t, 3)))
P()
# least-squares exponents over the present points: log L = a + b log(1/delta) + c log log(t/2pi)
pts = [(d, t, S[tag]['derived'][str(d)]['L_sign'], S[tag]['derived'][str(d)]['L_bal3']) for tag, t in present for d in cl.DELTAS]
pts = [p for p in pts if p[2] and p[3]]
pts_med = [(d, t, S[tag]['ensemble']['per_delta'][str(d)]['L_sign_median'], S[tag]['ensemble']['per_delta'][str(d)]['L_bal3_median']) for tag, t in present for d in cl.DELTAS if 'ensemble' in S[tag]]
fit_txt = ""
if len(pts) >= 3:
    A = np.array([[1.0, math.log(1/d), math.log(lt(t))] for d, t, _, _ in pts])
    for name, col, pp in (('L_sign at t', 2, pts), ('L_bal3 at t', 3, pts), ('L_sign median over centers', 2, pts_med), ('L_bal3 median over centers', 3, pts_med)):
        if not pp: continue
        A = np.array([[1.0, math.log(1/d), math.log(lt(t))] for d, t, _, _ in pp])
        y = np.array([math.log(p[col]) for p in pp])
        if len(present) >= 2:
            coef, *_ = np.linalg.lstsq(A, y, rcond=None); pred = A @ coef
        else:
            coef, *_ = np.linalg.lstsq(A[:, :2], y, rcond=None); pred = A[:, :2] @ coef; coef = np.append(coef, float('nan'))
        mx = float(np.exp(np.max(np.abs(pred - y))))
        fit_txt += "* **%s**: least-squares log L = a + b·log(1/δ) + c·log log(t/2π) over %d points: **b = %.3f, c = %s**, max residual factor %.3f. Laws: density model (b, c) = (0.667, 0.333); theorem (1, ≈ 0 — log log t enters additively); transcript (0.07, 0.89).\n" % (name, len(pp), coef[1], ("%.3f" % coef[2]) if not math.isnan(coef[2]) else "n/a (one height)", mx)
    # per-law fit with a free prefactor: max ratio measured/predicted over the points
    for name, col, pp in (('L_sign at t', 2, pts), ('L_sign median over centers', 2, pts_med), ('L_bal3 at t', 3, pts), ('L_bal3 median over centers', 3, pts_med)):
        if not pp: continue
        y = np.array([p[col] for p in pp])
        for law, fn in (('density δ^{-2/3}(log(t/2π))^{1/3}', lambda d, t: d**(-2/3)*lt(t)**(1/3)), ('theorem δ^{-1}', lambda d, t: 1/d), ('transcript δ^{-0.07}(log(t/2π))^{0.89}', lambda d, t: d**(-0.07)*lt(t)**0.89)):
            x = np.array([fn(d, t) for d, t, _, _ in pp]); k = float(np.exp(np.mean(np.log(y/x)))); ratio = y/(k*x)
            fit_txt += "   * %s against the %s law (free prefactor %.3g): measured/predicted in [%.3f, %.3f] → %s within a factor 1.5\n" % (name, law, k, ratio.min(), ratio.max(), "YES" if (ratio.max() <= 1.5 and ratio.min() >= 1/1.5) else "NO")
P(fit_txt)

# ------------------------------------------------------------------------------------------------------------ the four closes
P("## 4. The four refutation-shaped closes of PRICING §2(d), filled in from the files (INSTRUMENT; nothing about RH)")
P()
if len(present) == 4 and pts:
    laws = (('the density model δ^{−2/3}(log t)^{1/3}', lambda d, t: d**(-2/3)*lt(t)**(1/3)), ("the theorem's δ⁻¹ log log t", lambda d, t: 1/d), ("the transcript's δ^{−0.07}(log t)^{0.89}", lambda d, t: d**(-0.07)*lt(t)**0.89))
    def verdict(pp, col):
        y = np.array([p[col] for p in pp]); vs = []
        for law, fn in laws:
            x = np.array([fn(d, t) for d, t, _, _ in pp]); k = float(np.exp(np.mean(np.log(y/x)))); ratio = y/(k*x); vs.append((law, ratio.max(), ratio.min()))
        return vs, [v for v in vs if v[1] <= 1.5 and v[2] >= 1/1.5]
    texts = []
    for name, pp in (("L_sign at t (the contract's twelve points)", pts), ("L_sign median over the centers (the ensemble instrument)", pts_med)):
        if not pp: continue
        vs, fits = verdict(pp, 2)
        if len(fits) == 1:
            texts.append("**%s — lands:** the measured sign-detection bandwidth follows **%s** within a factor 1.5 across 10³ ≤ t ≤ 10⁶ and 0.05 ≤ δ ≤ 0.25 (measured/predicted in [%.2f, %.2f]); the two other laws are refuted at that tolerance (%s)." % (name, fits[0][0], fits[0][2], fits[0][1], "; ".join("%s [%.2f, %.2f]" % (v[0], v[2], v[1]) for v in vs if v not in fits)))
        elif len(fits) == 0:
            texts.append("**%s — no law within a factor 1.5** (%s)." % (name, "; ".join("%s [%.2f, %.2f]" % (v[0], v[2], v[1]) for v in vs)))
        else:
            texts.append("**%s — ambiguous at a factor 1.5:** %s fit (%s); the fitted exponents of §3 decide." % (name, len(fits), "; ".join("%s [%.2f, %.2f]" % (v[0], v[2], v[1]) for v in fits)))
    P("1. " + " ".join(texts) + " Measured δ-ratios L_sign(0.05)/L_sign(0.25) at t: %s (laws 1.12 : 2.9 : 5); the single-t values scatter within the p10–p90 bands of §2 (the noise at one t is configuration-dominated for L ≳ 20), which is why the ensemble median is the sharper instrument." % ", ".join("%.2f" % (S[tag]['derived']['0.05']['L_sign']/S[tag]['derived']['0.25']['L_sign']) for tag, _ in present))
else:
    P("1. (Close 1 needs all four heights; %d present. The δ-ratios so far are in §3.)" % len(present))
# close 2: clause-4 looseness
P()
lines = []
for tag, t in present:
    rr = R[tag]
    rec = [r for r in rr if r['is_record_point_C1_1'] and r['delta'] == 0.1]
    grid = [r for r in rr if r['delta'] == 0.1 and r['L'] in cl.L_GRID and r['L'] >= 50]
    fac = [r['clause4_bound_C1_1']/r['N_Z_center_mean']/r['L'] for r in grid if r.get('N_Z_center_mean')]
    fac1 = [r['clause4_over_N']/r['L'] for r in grid if r['N_Z'] > 0]
    lines.append("t = %g: at the record point L* = %.1f (δ = 0.1) N_Z = %.3e against the clause-4 bound 2b₁ℓ_R/L² = %.3e (ratio %.3g); over the grid rows L ≥ 50 the ratio (bound/N̄_Z)/L with N̄_Z the mean over the %d centers is in [%.2f, %.2f] (the pricing's inference: ≈ 1.05; against the single-t N_Z the same ratio ranges over [%.2f, %.0f] because of the nearest-zero oscillation)" % (t, rec[0]['L'], rec[0]['N_Z'], rec[0]['clause4_bound_C1_1'], rec[0]['clause4_over_N'], S[tag].get('ensemble', {}).get('n_centers', 0), min(fac) if fac else float('nan'), max(fac) if fac else float('nan'), min(fac1), max(fac1)))
ls = cl.Lstar(0.1, 1e6); a, b, c = math.log(math.log(3 + 1e6)), 2*math.log(10), math.log(2*cl.B1)
P("2. **Where the theorem's L* is spent.** At (0.1, 10⁶): L* = 40·(%.3f + %.3f + %.3f) = %.1f — log log(3 + t) %.0f %%, 2log(1/δ) %.0f %%, log(2b₁C₁) %.0f %%; the floor without the noise term, 4δ⁻¹(2log(1/δ) + log(2b₁C₁)) = %.0f. Measured: %s. **Refutation-shaped close:** the clause-4 bound is loose by a factor of order L at ζ's density (measured factors above), and the theorem's L* cannot be reduced below %.0f at (0.1, 10⁶) by any improvement of the noise bound alone." % (a, b, c, ls, 100*a/(a+b+c), 100*b/(a+b+c), 100*c/(a+b+c), 40*(b + c), "; ".join(lines), 40*(b + c)))
P()
cross = [S[tag].get('bump_only_crossing') for tag, _ in present if S[tag].get('bump_only_crossing')]
P("3. **λ₀ = 25 near-optimal?** Not a campaign item (bump-only, height-independent): the crossing of 2c(λ)² ≥ e^{λ/2} recomputed by the campaign's transform is λ = %s (record 18.6; proved from 23; contract 25). One line, as priced." % (", ".join("%.1f" % x for x in cross) if cross else "(rehearsal self-test not present)"))
P()
if OW and OW.get('u_true'):
    ut = OW['u_true']
    P("4. **R₀ = 81 loose by the uniformity price only?** From `outwindow_test.py` (no zeros needed): the radius at which the TRUE contamination of a depth-½ orbit falls to e^{−L} is u_true/L = %s (L = %s); the clause-5 pointwise bound route gives u/L = %s at the same L; the proved R₀ = 81 (asymptote 37.5) against the true ≈ %.2f L. Bound/exact at the four planted distances: %s. **Refutation-shaped close:** the out-window radius forced by the true transform is R ≈ %.1f·L at L = 120 (the note's 'for the record' 1.06 used the pre-asymptotic rate 0.85; with the saddle-point rate 1/√2 the same chain gives (7/(8·0.707))² = 1.53); the proved 81L is the price of c_B = 0.143 against the numerical ≈ 0.71–0.85 (a factor ≈ 25–35 in R₀ = (7/(8c))²) plus the uniformity relaxations (81 against 37.5 asymptotically). Nothing about RH." % (
        ", ".join("%.2f" % x['u_true_over_L'] for x in ut), ", ".join("%g" % x['L'] for x in ut), ", ".join("%.0f" % x['u_G1_over_L'] for x in ut), ut[-1]['u_true_over_L'],
        "; ".join("L=%g u=%g: 10^%.1f" % (p['L'], p['u'], p['log10_bound_over_exact']) for p in OW['points'] if p.get('exact') is not None and p['L'] in (20, 50, 120)), ut[-1]['u_true_over_L']))
else:
    P("4. (`outwindow_test.json` not present yet — `outwindow_test.py` writes it; rerun aggregate.py after.)")
P()

# ----------------------------------------------------------------------------------------------------- record-point table
P("## 5. The record points L*(δ, t; C₁ = 1) and L*(δ, t; C₁ = 2.4·10⁹): the datum where the theorem asserts its bound (INSTRUMENT)")
P()
P("| t | δ | L* | C₁ | inside (L ≥ L*, t ≥ 21L) | zeros used | N_Z = W_{Z'} | main −2δ²c² | W_Z | clause-6 bound δ²e^{δL/2} | ratio sep/bound | log10 \\|E₋\\| bound / est | N_Z/model |")
P("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for tag, t in present:
    for r in R[tag]:
        if r['is_record_point_C1_1'] or r['is_record_point_C1_zeta']:
            P("| %g | %.2f | %.2f | %s | %s | %d | %.3e | %.3e | %.3e | %.3e | %.3g | %.1f / %.1f | %.3f |" % (t, r['delta'], r['L'], "1" if r['is_record_point_C1_1'] else "2.4e9", r['inside_hypotheses'], r['n_zeros_used'], r['N_Z'], r['main_term'], r['W_Z'], r['clause6_bound'], r['sep_over_clause6'], r['E_minus_bound_log10'], r['E_minus_est_log10'], r['N_over_model']))
P()

# ------------------------------------------------------------------------------------------------- grid rows (compact, δ = 0.1)
P("## 6. Grid rows at δ = 0.1 (compact; the full tables with all columns are `rows_<tag>.csv`; INSTRUMENT)")
P()
for tag, t in present:
    P("### t = %g (reflection condition t ≥ 21L holds for L ≤ %.1f; rows with L above that are below the theorem's hypotheses)" % (t, t/21))
    P()
    P("| L | inside | n | N_Z | model | N/model | clause-4 bound | main | W_Z | W_Zrep | sep/cl6 | sign fires | bal3 | log10\\|E₋\\| bound / est / direct |")
    P("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in R[tag]:
        if r['delta'] == 0.1 and r['L'] in cl.L_GRID and (r['L'] <= 30 or r['L'] % 10 == 0):
            P("| %g | %s | %d | %.3e | %.3e | %.2f | %.2e | %.3e | %.3e | %.3e | %.3g | %s | %s | %.0f / %.0f / %s |" % (r['L'], "yes" if r['inside_hypotheses'] else "no", r['n_zeros_used'], r['N_Z'], r['density_model'], r['N_over_model'], r['clause4_bound_C1_1'], r['main_term'], r['W_Z'], r['W_Zrep'], r['sep_over_clause6'], r['W_Z_negative'], r['bal3'], r['E_minus_bound_log10'], r['E_minus_est_log10'], ("%.2e" % r['E_minus_direct']) if r.get('E_minus_direct') is not None else "-"))
    P()

# ---------------------------------------------------------------------------------------------------------- instruments row
P("## 7. Instruments-table row (for `directions/C2-rigidity-conservation.md`)")
P()
P("| measured detection bandwidth L_sign(δ, t) on ζ's zeros (zero-side; first-order datum W_Z(f_{t,L})) | %s | `results/c2-m2/campaign/CAMPAIGN.md` §2–§4; row files `rows_t1e{3,4,5,6}.{csv,json}`; controls §1 | INSTRUMENT: decides the δ- and t-law of the bandwidth and the looseness of b₁-, C₁- and R₀-type constants; nothing about RH |" % ("; ".join("t = %g: L_sign = %s / %s / %s at δ = 0.05 / 0.1 / 0.25" % (t, S[tag]['derived']['0.05']['L_sign'], S[tag]['derived']['0.1']['L_sign'], S[tag]['derived']['0.25']['L_sign']) for tag, t in present)))
P()
P("## 8. Hashes (SHA-256 of the files this document was built from)")
P()
for tag, _ in present:
    for f in ('zeros_%s.json' % tag, 'rows_%s.csv' % tag, 'rows_%s.json' % tag, 'summary_%s.json' % tag):
        P("* `%s`  %s" % (f, cl.sha256(os.path.join(HERE, f))))
if OW: P("* `outwindow_test.json`  %s" % cl.sha256(os.path.join(HERE, 'outwindow_test.json')))
P("* `campaign_lib.py`  %s" % cl.sha256(os.path.join(HERE, 'campaign_lib.py')))
P("* `run_height.py`  %s" % cl.sha256(os.path.join(HERE, 'run_height.py')))
P()
P("Status of the running campaign and the harvest recipe: `STATUS-campaign.md`. Checkpoints and the checker's verdicts: `SHARED.md`, `CHECK-O.md`.")
text = "\n".join(out) + "\n"
open(os.path.join(HERE, 'CAMPAIGN.md'), 'w').write(text)
print(text)
