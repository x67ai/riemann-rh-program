# Arb/FLINT f_t / H_t producer leg (M2a item (c)) — build record, derivation map, validation, run record, cross-check, cut lines

**Status:** built, validated and run 2026-09-02 (Session 14, D1 M2a; workflow `d1-audit-m2a-s14`, item (c)).
**Trust language (binding, D-R3/D-R8; SPEC.md §0):** everything in this leg is UNTRUSTED producer-side work by design.
An accepted transcript is "kernel-checked modulo the displayed hypotheses" (H1, H2 = H2-B here, H3) once the Lean
checker of the M2a Lean stream consumes it; today's acceptances are by the untrusted reference checker
`barrier_ref_checker.py`. Nothing here is "fully machine-checked". The Λ bracket of record is 0 ≤ Λ ≤ 0.2 (never
"Λ < 0.2"). Producer correctness is CONDITIONAL on Arb's ball contract (inclusion isotonicity, D-P0 of the M1 leg,
`results/d1-m1/producer_arb.py`) and on the quoted Polymath15 estimates.

## 1. What was built (files in this directory)

| component | file | status |
|---|---|---|
| producer-side negative controls of the reference checker on the real transcript (12 mutations of prism 0: gate equality, boxes, argument rows, floor, row count, seam, mesh walk) | `arb-negative-controls.txt` | 12/12 as expected (weakened-but-valid enclosures accepted; every check violation rejected at the named check) |
| the Arb-leg barrier producer: P15 f_t evaluator (two-variable Taylor/moment evaluator with derived remainders), Theorem 1.3 defect E, displacement D, mesh, rows, chain, manifest | `producer_arb.py` (1 408 lines; every transcribed formula at PDF page and derivations D-A1…D-A18 in the module docstring) | DONE |
| moment cache (lossless dyadic mid/rad, D-A14) | `arb-cache/moments-b6e2fae75cbdb737e271.json` (85 KB; row-2 box, N₀ = 630783, K = 36, J = 40, 320 bits; 61.4 s to compute) | DONE |
| **the row-2 barrier transcript (Lane B)** | `transcripts/row2-arb/instance02-barrier-manifest.json` + `instance02-prism-0000…0071.json` (72 prisms, 10 771 rows, 2.9 MB) + `producer.log`, `producer-console.log`, `instance02-progress.json` | **COMPLETE chain 0 → t₀ = 93/500; reference checker ACCEPT** |
| the N = 5000 test instance shared with the mpmath leg (rectangle [314159300, 314159301] × [y₀, 1], same t₀) | `transcripts/mini-arb/` (3 prisms, cut at 15558943/10⁹; a test, NOT a certificate instance) | ACCEPT (chain segment [0, 0.0156]) |
| validation harness (mpmath reference, independent code path) | `validate_arb_ft.py` → `arb-validation-run.txt` (A–C), `arb-validation-run-DE.txt` (D–E), `arb-validation-run-full.txt` (clean re-run) | see §4 — ALL PASS |
| SPEC P-11 cell-wise cross-check tool (Arb vs mpmath prism files at a common seam) | `crosscheck_legs.py` → `arb-crosscheck-legs-run.txt` | see §5 |
| chain statistics | `arb-row2-chain-stats.txt` | see §3 |

Independence discipline (P-1, D-R3): this leg shares with the mpmath leg ONLY `SPEC.md`, `barrier-schema.json` and the
checker-side `barrier_ref_checker.py`; no evaluation code, no helper, no constant computed elsewhere. The exact
ball→integer helpers are the M1 Arb leg's own (D-P1…D-P5, D-P7 of `results/d1-m1/producer_arb.py`). The mpmath leg's
`ft_mp.py` / `producer_mp.py` bodies were not read while building this leg (only its notes' formula list, which is a
transcription of the paper).

## 2. Where the load-bearing mathematics lives (standing order 5)

All of it is in the module docstring of `producer_arb.py`, transcribed from the on-disk arXiv v2
`fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf` (PDF page = printed page; re-read this session with
`pdftotext -layout` for pages 1–6, 30–31, 38–40, 46–48): (6), (7), (9), (10), (11) p4; Theorem 1.3 (13)–(22) p6;
Proposition 6.6 (i)–(vi) p31 — (vi) used through the **10.50 weld** of SPEC D-2.4 (never the displayed 10.44 of (24));
(80) p38; (84) p40; (92) and the s_** identity of Lemma 8.4's proof p46. Derivations (each cited at the code line that
uses it; the numbering continues the M1 leg's D-P series):

* **D-A1** the form implemented is (92): f_t = Σ_{n≤N} b_n n^{−s_*} + γ Σ_{n≤N} b_n n^{−s_**}, s_* = s₊ + (t/2)α(s₊),
  s_** = s₋ + (t/2)α(s₋), s± = (1 ∓ iz)/2 — equal to (14) through conj(α(s₊)) = α(conj s₊) (α has real coefficients and
  Log(conj w) = conj Log w off the cut; Im s₊ = −x/2 ≠ 0); P15 p46 states s_** = conj(s_*) − y + κ. **Source finding
  (shared with the mpmath leg's D-F1):** the second sum of (14) carries an overline on s_* in the PDF that `pdftotext`
  drops, so SPEC §2.3's quotation of (14) reads `n^{s*+κ}`; the (92) form is unambiguous and is what both legs implement.
  The docstring's earlier remark "α(conj s) = conj α(s) was NOT needed" was wrong and is corrected.
* **D-A2** the defect: e_A + e_B ≤ (e^{δ₁} − 1)[F + N^{2|κ|} G] with F, G the two Dirichlet-sum majorants, δ₁ of (84),
  |κ| from (22), from 6.6(iv),(v) with the n-dependent exponent majorized by δ₁ (|log(x/4πn²)| ≤ log(x/4π) for n ≤ N,
  x ≥ 200); e_{C,0} by the 10.50 form. Every factor is a ball over the box's coordinate INTERVALS (x ∈ [X, X+1],
  y ∈ [y₀, 1], t ∈ [τ, t₀]) — the sup by inclusion isotonicity.
* **D-A3** box-uniform majorants R_k^±(t) of Σ b_n n^{−Re s_*} log^k n and of |γ| Σ b_n n^{−Re s_**} log^k n, using (20) for
  |γ| and inf Re α over the box; **D-A9** their monotonicity in t (log N ≤ 2 inf Re α, checked as a certified inequality:
  13.35 vs 26.7 at row 2), so values at the seam are sups over [τ, t₀].
* **D-A4** the evaluator: two-variable expansion in (δ, τ) about the box centre z_c and t_c = t₀/2 with STORED MOMENTS
  M_m = Σ_n c_n log^m n (m ≤ K + 2J = 116) and the (q_n)^j = (L²/4 − α_c L/2)^j binomial tables; per seam the τ-sums
  collapse into K+1 coefficients; per point a Horner evaluation. **D-A5** truncation remainders
  |e^{a+b} − T_K(a)T_J(b)| ≤ e^{|a|+|b|}(|a|^{K+1}/(K+1)! + |b|^{J+1}/(J+1)!) with the derivative weights.
  **D-A6** the α-freezing correction (|e^w − 1| ≤ η := w_max e^{w_max}, w_max = (t₀/2) sup|α(s₊(z)) − α_c| log N) —
  η ≈ 1.2·10⁻¹³ at row 2, the dominant width (≈ 10⁻¹⁰) of every value ball.
* **D-A7** γ = exp(Λ(z) + t w(z)) with Λ, Λ′, Λ″, w, w′, w″ from (7), (8): Taylor-with-remainder along the segment from
  z_c (convex box). **D-A8** the crude box-uniform second derivatives D_zz, D_tt, D_zt (Lemma 8.4's calculus with box
  balls in place of the paper's constants) — kept as the fallback alternative.
* **D-A10 / D-A10′** hull boxes: |f(z) − f(z_m)| ≤ |f′(z_m)| h + (h²/2) sup_seg |f″|, the sup from the D-A17 second
  derivative evaluated on the segment's hull box (D-P4 + D-P0); the smaller of this and D-A10's D_zz form is used.
* **D-A11 / D-A15 / D-A15′** the displacement: |g_t − g_τ| ≤ 2E_p + Δ·Mt (Theorem 1.3 at both times, mean value in t),
  Mt ≥ sup_{∂R×prism}|∂_t f| by the sharpest of three rigorous bounds per segment — the prism-context hull of f_t (D-A15:
  all τ-sums collapsed with τ = the prism INTERVAL), the prism midpoint + D_zt h, and (D-A15′) |f_t(z_m, τ)| +
  h sup_seg|f_zt(·, τ)| + Δ sup_{seg×prism}|f_tt| — the last wins on every segment of every prism at row 2.
* **D-A12** Theorem 1.3 at t = 0 (SPEC P-7): the limit argument (dominated convergence for H_t with |e^{tu²}Φ(u)cos(zu)| ≤
  e^{u²/2}|Φ(u)|e^{|Im z|u}, continuity of B_t, f_t and of the D-A2 majorant in t); recorded in prism 0's
  `producer.comment`. **D-A13** N constant on the closed box (monotone in x and t; both extreme corners certified).
* **D-A14** the moment cache: lossless arf/mag mantissa-exponent pairs, reloaded as hull_ball(mid − rad, mid + rad) — the
  reloaded ball contains the stored ball; every reloaded ball is re-verified for containment.
* **D-A16** adaptive mesh: 16 equal exact-rational pieces per edge, bisected while the hull radius exceeds
  (1/6)·(pre-scan min|f|) or C6 fails.
* **D-A17** the second derivatives f_zz, f_zt, f_tt: T_n = X_n e^{w}, T_n′ = T_n(iL/2 + w′), T_n″ = T_n((iL/2 + w′)² + w″),
  d²T_n/dt² = T_n q_n(z)², d²T_n/dz dt = T_n[(iL/2 + w′)q_n(z) + (iL/4)α′(s₊)], with |w′| ≤ L(t₀/4)A₁′, |w″| ≤ L(t₀/8)A₂″;
  subtracting the expanded derivatives and summing gives the three correction terms and the three truncation remainders
  (orders (K−2, J), (K−1, J−1), (K, J−2)); the γS₂ derivatives by Leibniz with l = ∂_z log γ, w = ∂_t log γ
  (t-independent), l_z, w_z.
* **D-A18** the minus-sum corrections enter AFTER the γ multiplication with the Leibniz factors (|l|c₀ + c₁ for f_z, …).
  **Gap found and fixed in the inherited draft:** the pre-23:30 draft of this file omitted the |l|c₀ and |w|c₀ terms in
  f_z and f_t (≈ 10⁻⁹ numerically at row 2; a rigor gap nonetheless).

Exact arithmetic discipline (M1 D-P1/D-P2): every ball → exact rational [mid − rad, mid + rad] from the exact dyadic
mid/rad, floor/ceil on Fractions at scale K (10¹²) or A (10⁶); `lower()`/`upper()` only as a redundant bracketing assert;
no float touches any emitted number (floats pick the mesh size and the trial Δ; every gate is re-verified exactly).

## 3. Run record — the row-2 barrier transcript (`transcripts/row2-arb/`, `arb-row2-chain-stats.txt`)

Instance: P15 Table 1 row 2, R = [5000000194858, 5000000194859] × [16733/100000, 1], t₀ = 93/500, N₀ = 630783
(D-A13 certified at the four corners). Box constants (row 2): inf Re α = 13.3547, sup|α| = 13.378,
sup|α(s₊(z)) − α_c| = 9.6·10⁻¹⁴, sup|α′| = 2.0·10⁻¹³, ρ = max|z − z_c| = 0.6506, C⁺ = Σ|c_n| = 4.53, C⁻ = 860,
Q = max|q_n| = 44.9.

* Moments: 61.4 s once (cached). Per evaluation: 0.3–0.4 ms (Horner over K+1 = 37 coefficients × 2 series + γ).
  Thin-point widths 1.2·10⁻¹⁰ (t = 0.014) to 7·10⁻¹³ (t = 0.17), dominated by the D-A6 term; truncation remainders at
  seam 0: 6.6·10⁻¹⁶ (f), 3.8·10⁻¹⁴ (f_z), 2.1·10⁻¹² (f_zz) for the plus sum; ×200 for the minus sum (C⁻/C⁺).
* **The chain: 72 prisms, 10 771 rows, 144 s of producer time (2.4 min wall), reference checker ACCEPT (C-B0…C-B13).**
  Δt from 1.08·10⁻³ (t = 0) to 1.05·10⁻² (t → t₀); rows per prism 289 (t = 0; bottom 200 / right 32 / top 16 / left 41)
  down to 64; floors Fn/Fd from 4.3825 (t = 0; pre-scan min|f| = 4.683 — P15's X-selection heuristic holds at row 2)
  down to 1.4679 (last prism); E/K = 4.119·10⁻⁴ at seam 0 (e_{C,0} = 4.119·10⁻⁴, e_A + e_B = 4.7·10⁻¹⁰; SPEC's indicative
  4.12·10⁻⁴ confirmed as a certified value) falling to 1.65·10⁻⁷; D/K from 3.90 (prism 0) to 1.10; Mt (sup|∂_t f| over
  the prism) from 3620 (seam value 1793 + Δ·sup|f_tt|) to 104. Winding sums at seam 0: [−142, 147]/10⁶.
* Scales K = 10¹², A = 10⁶ (even, P-4); every prism's rows are 13-digit integers; the mesh numerators are exact rationals
  with denominators 2^k·16 (bisection of [X, X+1] and of [y₀, 1]).
* Cost extrapolation (the task's "measure first"): the two-prism probe measured 2.4 s per prism at t = 0 with the seam
  |∂_t f| ≈ 1.8·10³ decaying like e^{−28t}, giving ≈ 60–80 prisms for the chain — the full chain then ran in one process in
  2.4 minutes, so no sub-box or coarsened mesh was needed; the transcript is the FULL certificate for [0, t₀] on R.
  Per-prism cost is dominated by the mesh rows (0.9 s) and the 3–4 displacement trials (0.5 s each).

**The chain-segment mechanism** (`--t-start/--t-end`, `merge`) exists for parallel runs and was exercised only in the
sense that every run writes a `chain_segment` record; the row-2 chain was produced by one process from t = 0 (no merge).

## 4. Validation record (`validate_arb_ft.py` → `arb-validation-run.txt`)

Reference: mpmath 1.3.0 (dps 45), independent code path — H₀ = ξ(½ + iz/2)/8 (P15 (1)–(2) p1) with `mp.zeta`/`mp.gamma`,
and for t > 0 the heat-kernel form H_t(z) = (2π)^{−1/2} ∫ e^{−w²/2} H₀(z + i√(2t) w) dw, **derived as D-V1** in the file
(complete-the-square identity + Fubini on the super-exponential decay of Φ), checked against the direct u-integral (4) at
x ∈ {50, 120, 200} at the cancellation-adjusted precision; B_t from (6)–(11) re-implemented in mpmath. Quadrature: 81
Gauss–Legendre panels on [−16, 16] — the convergence study is quoted in the file's docstring (29 panels: 3.4·10⁻¹⁴;
41: 6.7·10⁻¹⁹; 81 vs 121: < 10⁻²⁵). Containment is decided in exact rational arithmetic on the ball's mid/rad against the
reference's exact binary value with a declared 10⁻²⁵ decimal slack (the M1 harness lesson).

**Results (`arb-validation-run.txt` = sections A, A′, B, C of the 23:37 run; `arb-validation-run-DE.txt` = sections D, E
re-run at 00:34 after two harness fixes recorded in the first file's postscript; `arb-validation-run-full.txt` = a clean
full re-run with the fixed harness, launched 00:36, for a single record):**

| section | test | result |
|---|---|---|
| A | D-V1 heat-kernel form vs the direct u-integral (4) at x ∈ {50, 120, 200}, at cancellation-adjusted dps 58/70/84 | relative differences 6·10⁻⁵⁶, 4·10⁻⁵⁵, 6·10⁻⁵⁷ |
| A′ | reference stability, dps 45 / 81 panels vs dps 60 / 121 panels at four (x, y, t) incl. (10⁴, y₀, 0.2) | relative differences 1–2·10⁻⁴² (reference good to ~40 digits) |
| **B** | **containment of g = H_t/B_t in the Arb enclosure f_t ± (rad_f + E) at 48 points**: x ∈ {200, 1000, 3000, 10⁴} × t ∈ {0, 1/20, 93/500, 1/5} × y ∈ {y₀, 1/2, 1} (direct-sum evaluator + D-A2 defect, N = 3…28) | **48/48 contained; worst \|g − f\|/E = 0.5465**; rad_f ∈ [4.3·10⁻⁹⁴, 2.4·10⁻⁹¹]; E ∈ [2.36·10⁻², 0.945] (e_{C,0}-dominated; e_A + e_B ≤ 1.3·10⁻²) |
| **C** | the Taylor/moment evaluator (the transcript evaluator, `BoxEvaluator`/`SeamContext`) on the box [10⁴, 10⁴+1] × [y₀, 1] × [0, t₀], N = 28: seam balls f ± E_box vs the reference at 14 boundary points (t = 0: 8 points; t = 93/500: 6) | **14/14 contained; worst ratio 0.4616**; rad_f = 1.0–1.5·10⁻⁴ (the D-A6 α-freezing term at x = 10⁴, as computed: η R₀ with dA = 3.3·10⁻⁵; at row 2 the same term is 10⁻¹⁰) |
| D | the six derivative balls f_z, f_t, f_zz, f_zt, f_tt vs central differences (h = 10⁻⁶) of the direct sum at 8 (z, t); D-A15 prism-context balls (Δ = 1/200) contain the direct values at 4 times in the prism at 6 (z, prism) | 46/46 (every finite difference inside its ball's half-width + the FD truncation tolerance; prism balls 10⁻²…5·10⁻² wide contain all direct values) |
| E | hull boxes (`seg_box`, D-A10/D-A10′) on four boundary segments of length 1/50 contain 9 interior direct-sum values each | 36/36; D-A10′ wins on all four (r = 8·10⁻⁴ … 1.2·10⁻² against D-A10's 7·10⁻³ … 1.7·10⁻²) |

So 62 reference points in region (5) at x ≤ 10⁴, all contained, with Theorem 1.3's margin used to at most 55 %; the
widths of the f_t balls themselves are 10⁻⁹⁴…10⁻⁹¹ (direct) and 10⁻⁴ (Taylor at x = 10⁴; 10⁻¹⁰ at row 2). What the test
proves and does not: it verifies the transcription of Theorem 1.3 (f_t, γ, α, M₀, the majorant) as a theorem at moderate
x, and the evaluator's arithmetic against an independent library; it cannot reach x ≈ 5·10¹² (no reference exists there),
where the Taylor evaluator is instead checked against the direct 630783-term sum at 6 random boundary points and times
(`producer_arb.py crosscheck`: all overlapping, Taylor widths 7·10⁻¹³…1.2·10⁻¹⁰ against direct widths 10⁻⁸⁴…10⁻⁸⁰) and,
at the seam t = 0, cell-wise against the mpmath leg (§5).

**Harness lessons (recorded):** (i) the direct u-integral needs dps ≈ 35 + πx/(8 ln 10) — at x = 200 that is 84 digits, and
a 1e-20 agreement threshold at dps 35 fails for the harness's reason, not the evaluator's; (ii) mpmath's `quad` with 29
panels was only 3·10⁻¹⁴ accurate on this integrand (81 panels: < 10⁻²⁵); (iii) a midpoint comparison is the wrong test for a
ball whose width is the quantity of interest — test containment; (iv) `float()` of |B_t| ≈ 10⁻¹⁷⁰⁰ underflows.

## 5. Two-producer cross-check (SPEC P-11; `crosscheck_legs.py`, `arb-crosscheck-legs-run.txt`)

The two legs choose different prism lengths, so only the seam τ = 0 is common (at both instances). Cell-wise on the
common mesh refinement, every pair of overlapping segments must have intersecting value boxes:

| instance | Arb rows | mp rows | overlapping pairs | disjoint | E (Arb) | E (mp) | floor (Arb) | floor (mp) |
|---|---|---|---|---|---|---|---|---|
| row 2, seam 0 | 289 | 184 | 465 | **0** | 4.1192·10⁻⁴ | 4.1192·10⁻⁴ | 4.3825 | 4.6294 |
| mini (N = 5000), seam 0 | 85 | 184 | 261 | **0** | 6.9421·10⁻³ | 6.9418·10⁻³ | 0.2373 | 0.0551 |

E agrees to five digits (both legs bound the same majorant; the Arb value is the larger by < 10⁻⁴ relative — the
D-A2 N^{2|κ|} factor against the mp leg's D-F4). The seam-time sup|∂_t f| agrees: Arb 1793 (row 2, t = 0) vs the mp
leg's DT = 2053 for its first prism [0, 0.00114] (an interval-t bound, so ≥ the seam value) and Arb 13.48 vs mp 13.47 on
the mini instance. The floors differ by design (mesh policy: the Arb leg's hull radius is min|f|/6; the mp leg's plain
interval boxes on the mini instance are wider). Both certify winding 0 with sum widths ≪ A/2. **Verdict: CONSISTENT —
no stop-the-line event.** The remaining prisms are not seam-aligned; a full per-seam comparison would need one leg to
re-run on the other's seam list (both producers accept a seam list only through their Δ policy — a follow-up item,
not required by P-11's "per prism" wording for the two-producer rule to have been exercised at the hardest seam t = 0).

## 6. Cut lines and what is NOT in this leg (honest)

1. **Lane A (the asymptotic region at t₀: window rows + the Lemma-T tail row) is not produced here**; the task item is
   the barrier transcript. The evaluator (`ft_direct`, `E_bound`, the R-sum majorants) is what a lane-A producer needs;
   the mollified floor T (SPEC P-9) and Q₁…Q₄ (P-10) are not implemented.
2. **Theorem 1.3 at t = 0 is the limit argument D-A12** (producer obligation P-7), recorded in prism 0, flagged for M2b.
3. **The mesh is not minimal** (r_max = min|f|/6 uniform over the boundary) and the prism count (72) is above the mpmath
   leg's 39 because the Δ·sup|f_tt| term uses a hull-evaluated second derivative; both chains are small (10⁴ rows) and
   nothing hinges on it.
4. **The cross-check covers the seam t = 0 only** (§5).
5. **The Lean emission (P-12)** of `transcripts/row2-arb/` into per-prism modules is the Lean stream's item; nothing in
   `lean/Zeta23/` was changed by this leg.
6. **Platform trust:** Arb's inclusion isotonicity and correctly-rounded `mid()/rad()` (M1 capability table) and the
   `arb(fmpq)` containment re-verified at every conversion; no proof.
