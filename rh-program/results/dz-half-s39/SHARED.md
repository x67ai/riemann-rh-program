# SHARED.md — unit `dz-half-s39` (Session 39)

Dated blocks, appended after each batch. Newest at the bottom.

## 2026-10-01 — block 0: the record read

- Brief read whole. Record read at the line: fr read-O §4 A3 (the sketch), §7(a) (companion item), §5 F2 (the T_d / κ_p
  repair); fr NOTE §4 Theorem B (repaired form, lines 215–236); digest §F.2 item 4 (U5a contract clause).
- DZ book is on disk: `fetched-r2/t-50-diamond-zhang-2016-beurling-generalized-numbers-ams-surv213-BOOK.pdf` (258 pp.);
  text extracted to `sources/t-50-diamond-zhang-2016-book.txt` (book p. 195 = PDF p. 208).
- At the page: Thm 17.14 (book p. 208): "(i) N_B(x) = k₂x + O(x^{1/2} exp{c(log x)^{2/3}}) with k₂ > 0 … (iv) lim sup/inf
  (ψ_B(x) − x)/(x exp{−2√log x}) = ±2". Grid (17.13) (book p. 201): "v₀ = 1 and v_k = n + ℓ/2ⁿ, for k = 2ⁿ + ℓ,
  n = 0, 1, 2, …, 1 ≤ ℓ < 2ⁿ" — as printed the index set misses k = 2ⁿ (typo; the grid meant is {n + ℓ/2ⁿ}).
  Selection: Lemma 17.5, p_k = ∫_{v_{k−1}}^{v_k} f; Lemma 17.2's proof: X_k independent Bernoulli(p_k).
  Template for 17.14: f_C of (17.44), with (17.45) "(1 − c)(1 − v⁻¹)/log v ≤ f_C(v) ≤ (1 + c)(1 − v⁻¹)/log v, v ≥ e⁴".
- BDR z-02 l. 133–136 + fn. 4 (l. 165): "that of a [1, β₀]-system⁴ is in [7, Ch. 17] … for some β₀ ≤ 1/2" / "⁴Most likely
  the value of β₀ equals 1/2, but in principle it is still possible that β₀ could be smaller."
- Noted: DZ §17.10's hybrid P_X adds an infinite, realization-dependent set {w_n}; out of scope (the target is P_B, and P_R).

## 2026-10-01 — block 1: prior-art gate run; proof route fixed

- arXiv API (https, 2026-10-01): `sources/arxiv-beurling-generalized-sorted.xml` (abs:Beurling AND abs:generalized, 221
  entries) + six phrase queries `sources/arxiv-q-*.xml`; filtered list `sources/arxiv-generalized-numbers-2023-09-to-2026-10.txt`
  (17 hits after 2023-09-01; the number-system ones: 2602.07690 Tranoy–Vindas, 2511.13496, 2507.13780 Broucke, 2409.10051,
  2407.12746, 2406.00736 Vindas, 2401.06892, 2311.11127 Ruzsa). Semantic Scholar citers of 2309.01567:
  `sources/s2-citations-BDR-2309.01567.json` (4: 2507.13780, 2407.12746, 2307.00239, 2209.01689).
- Nearest candidate read at the page: Broucke 2507.13780 (`sources/broucke-2025-2507.13780v1.txt`) Thm 1.6 (l. 246–254):
  "(1) N_P(x) = Ax + O_ε(x^{1/2+ε})" — upper bound only; discretized by the Broucke–Vindas procedure (l. 1263–1273, Thm 5.1,
  "|π_P(x) − F(x)| ≤ 2"), not DZ's independent selection. Does not settle fn. 4.
- BDR itself (z-02 l. 668–715): Cor. 3.3 gets β = ½ exactly via a planted pole at s = ½; Remark 3.5(1) builds [1, β] for
  β₀ < β < 1 from DZ's system. So existence of a [1, ½]-system is already implied (if β₀ < ½ take β = ½ in Rem. 3.5(1)); what
  is open in print is the VALUE β₀ for DZ's construction (fn. 4). That is the unit's target.
- Two proof routes found: (A) Theorem-B one scale (x/2, x] with the exact identity ρ = ρ_{B^c}·Π_{q∈B}(1 − 1/q)^{−X_q}, so the
  whole dependence across the block is the factor e^{S}; linearize, L² remainder; conditional Berry–Esseen; no 0–1 law
  needed; gives E(x) = Ω(√(x/log x)) a.s. (B) Mellin: ζ_B = ζ_C e^{−F₁+F₂} on σ > ½ (DZ p. 219), −F₁ ≥ 0 on reals, F₂'s random
  part W(σ) has lim sup_{σ→½+} W = +∞ a.s. (CLT + Kolmogorov 0–1), so ζ_B is unbounded near ½ and β ≥ ½ by Landau.

## 2026-10-01 — block 2: NOTE §1 and §2 written (the proof)

- §1: construction, templates, DZ's (i)–(iv) and representation, BDR's question, DMV's identical selection — at the page.
- §2: Theorem 1 [proved here]: under (H0) p_k = ∫_cell f, (H1) f ≍ 1/log v, (H2) cells in (x/2, x] have p → 0,
  (H3) density ρ > 0 a.s. — lim sup |N(x) − ρx|/(x/log x)^{1/2} > 0 a.s. Corollary 2: P_B is a [1, ½]-system a.s.
  (β₀ = ½); P_R is [½, ½] a.s. (Cor. 2.6 for α). Lemma 2.1 is the exact one-scale identity E = Y + L + R, with the whole
  cross-block coupling in ρ = ρ^c e^{S}; Lemma 2.2 σ² ≥ c_*κ²x/(2^{11}(N₀+1)² log x); Lemma 2.3 R = O_P(κ/log x).
  Prop. 2.4: independent second proof (ζ_B unbounded as σ → ½+, a.s.). Lemma 2.5: finite changes preserve O(x^τ) and o(s_x).
- Nothing in the proof failed; the brief's stop condition (dependence uncontrollable) is NOT met.

## 2026-10-01 — block 3: finite-rung code written; main batch launched (05:21)

- `verify/dzcommon.py` (f_R, f_C with g from Irwin–Hall for log u ≤ 5 and from the renewal equation
  q(w) = w1_{[1,2]}(w) + ∫_{w−2}^{w−1} q, q = w·g(e^w), above; (17.31) asserted). Envelope check: f_C/f_R on [e⁴, 10⁸] stays in
  [1 − c, 1 + c], c = 0.8366 (every Poisson proposal also asserts f ≤ envelope).
- `verify/dzgen.py`: exact Bernoulli selection on every cell of Γ for units n ≤ 22; Poisson-with-grid-rounding above (TV ≤ 2⁻²²);
  ρ from the Euler sum + Ein(log X) + the f_C oscillatory tail + a sampled Gaussian tail for the g-primes > X.
- `verify/dzcount.c`: DFS enumeration of all g-integers ≤ X into bins (e_i, e_{i+1}], e = 2^j(1 + i/1024); control: rational
  primes to 10³ give N(e) = ⌊e⌋ at every edge (exact).
- `verify/controls.py`: rational primes (β = 0), P_det (quantile system on Γ, no selection), T₁ (delete p w.p. 1/(1 + log p)).
- Early finding (10⁵ tests): E(x) < 0 throughout for both DZ and P_det, |E| ≈ c(x/log x)^{1/2} — the (2s − 1)^{−1/2} branch
  point from the prime squares with ζ_T(½) = −1 < 0 (NOTE §4.3). The one-scale variance is a small part of MS at 10⁵
  (I(κ) ≈ 2.9 vs MS/(x/log x) ≈ 35–60 for R seed 1).
- NOTE §3.1–3.2 written: σ² two ways with the error bound; I(κ; n₀) closed forms; min I > 0 on DZ's grid (0.0195, 0.0380).

## 2026-10-01 — block 4: main batch harvested (05:21–05:27; `verify/logs/run_main.log`, `verify/logs/aggregate.txt`)

- DZ R (P_R), 5 seeds, X = 10⁸: sup-slope 0.492 ± 0.012 on [10³, X], 0.514 ± 0.054 on [10⁶, X]; ms 0.474 → 0.455; L-versions
  0.52–0.55. DZ C (P_B), 5 seeds: sup 0.479 ± 0.020 on [10³, X], falling to 0.381 ± 0.060 on [10⁶, X]; ms 0.477 → 0.360.
  Per seed (C): E/(x/log x)^{1/2} at 10³…10⁸ is a large, seed-dependent, slowly varying NEGATIVE drift (e.g. −25 … −42 … −33
  for s1; −51 … −66 … −28 for s3): the top-window slope deficit is the decline of this factor over 10⁶–10⁸, not a smaller
  exponent (mechanism test: `verify/drift_check.py`, §4.4).
- Controls: rational primes — N(e) = ⌊e⌋ at all 27 125 edges (exact); sup-slope 0.000. P_det (Γ, quantiles, no selection):
  slopes 0.42–0.46 (msL 0.49–0.50), E/(x/log x)^{1/2} → −0.595…−0.597 (blocks 10⁶–2.5·10⁷) against the branch-point
  prediction √(2/π)H(½) = −0.5998, H(½) = −0.7517 from the realized quantiles (`verify/predict_det.py`) — 0.5 % agreement.
- T₁ (delete p w.p. 1/(1 + log p)): slopes 0.93–0.95, E ≈ +c·x/log x. Correct but not the intended calibration: the mean
  system has a −ρ log(s − 1) singularity AT s = 1, so β(T₁) = 1. Replaced as the near-α = 1 surgery control by the frontier's
  own T_α at α = 0.90, 0.95 (`verify/run_ta.sh`, running); T₁ kept and reported as a negative control.
- Fixed: `analyze.py` normalized the partial top block by 1.5·2^26 (artifact at j = 26); now the mean edge of the block.

## 2026-10-01 — block 5: controls, one-scale verification, NOTE §3 and §4 written

- T_0.90 (frontier's own family, 5 seeds, 10⁸): sup 0.445 ± 0.019 [10³, X], 0.440 ± 0.011 [10⁴, X] — reproduces the
  frontier writer's 0.457 ± 0.012 / α/2 = 0.45 (pipeline calibrated). T_0.95: 0.497 ± 0.007, 0.482 ± 0.015 (α/2 = 0.475,
  1/(3 − α) = 0.488). Local two-decade slopes: sd 0.148 (P_R), 0.139 (P_B), 0.109 (T_0.95) — `logs/local_slopes.log`.
- P_det after the partial-block fix: top block −0.5995 vs predicted −0.5998 (H(½) = −0.7517); `logs/predict_det.log`.
- onescale A (grid vs continuum): relative gap 1.8·10⁻¹ (x = 6) → 1.6·10⁻⁴ (x = 22), ~2^{−x/2}. onescale B: Lemma 2.1(a)
  identity residual 0 in 8/8 cases; Var(E′)/σ²_cont = 0.967–1.070 (sampling sd 0.022–0.063); KS p 0.36–0.99; realized
  |z| ≤ 1.67. I(κ) closed forms match σ²_cont/(x/log x) to 3–5 %.
- drift_check (heuristic): Ĥ(½ + 1/log x) gets sign/order for high-ρ P_B seeds, amplitude low ×1.1–2.5; recorded only.
- NOTE §3 (3.1–3.3) and §4 (4.1–4.5) written. Next: §5 prior art, §6 distance/Instruments/Untried/waste, §0 close.

## 2026-10-01 — block 6: NOTE complete (§0–§6); residue check; self-review of §2

- `verify/residue_check.py`: log|G(4(1 − ρ₁))|² = −0.0032445 (closed form) vs −0.0032483 (quadrature, step 10⁻⁴; gap halves
  with the step) — g, 4^k, γ_k and the sign of (17.44) confirmed; (17.45) on 2·10⁶ points: f_C/f_R ∈ [0.237, 1.763].
- NOTE §5 (prior art: not settled in print; BDR Cor. 3.3/Rem. 3.5 bound what is new; Remark 5.1 conditional upgrade of
  Broucke Thm 1.6), §6 (distance line, Instruments row text, Untried U-1…U-5, waste line), §0 (close T as a theorem) written.
- Self-review of §2 line by line: Lemma 2.1 algebra re-derived; constants of Lemma 2.2 (2^{11}), Lemma 2.3 (5C_*), K = 2^{7.5}/√(2πc_*)
  re-checked; two fixes: m(x) ≤ 2^{2−⌊x/2⌋} on Γ (f_C ≤ 1.84), and x₁ depends only on N₀ (not on κ_x).

## 2026-10-01 — block 7: CLOSE — T

- Close T: for almost every realization of DZ Thm 17.14, N_B(x) − k₂x = Ω((x/log x)^{1/2}); with DZ (i), (iv): β₀ = ½, P_B is a
  [1, ½]-system (BDR fn. 4 answered "yes, ½" a.s.); P_R is [½, ½] a.s. Two proofs (Theorem 1, one scale, dependence exact via
  ρ = ρ^c e^{S}; Prop. 2.4, ζ_B unbounded at ½). Stop condition not met; no paper after BDR settles fn. 4.
- Finite rung X = 10⁸, 5 seeds × 2 templates + controls (ℙ, P_det, T_0.90, T_0.95, T₁): see NOTE §4.2 and §3.3.
- Housekeeping: 27 g-prime lists (1.09 GB) deleted after analysis; SHA-256 in `verify/data/PRIMES-MANIFEST.sha256`; seeded
  scripts regenerate them. Final pass: P_det claims corrected to "β ≥ ½ proved, ½ in the data".
- Owed: the standing dual read (read-O slot) on §2; Instruments row and Untried U-1…U-5 are in NOTE §6 for the bookkeeping
  agent (this unit edited nothing outside its folder).

## 11:12 IST 2026-10-01 — read-O (Opus reader), batch 1: §1 re-derivations written

- NOTE hash b5ff31f1… (407 lines) confirmed. Book ch. 17 read at the lines (Lemma 17.2/17.5/17.7, (17.13), Thm 17.11/17.14,
  (17.22), (17.30), (17.39), (17.44)–(17.47), §17.10); BDR fn. 4 and Cor. 3.3–Rem. 3.5 at the lines; Broucke Thm 1.6 at the line.
- Theorem 1 re-derived ✓ (Lemmas 2.1–2.3, Berry–Esseen step, constants K, ε_x). The passage to "lim sup > 0 a.s." is the Fatou
  bound P(lim inf A_n) ≤ lim inf P(A_n): valid, no cross-scale independence needed. Prop. 2.4 ✓ (Mellin step suffices;
  |G − 1| ≤ 0.19·4^{−k} on [½, 1) ✓). Lemma 2.5, Cor. 2.6, Cor. 2, §3.2 closed forms, §4.3 (proved part), Remark 5.1 ✓.
- Record items so far: m1 §17.10's normalization may add an INFINITE sequence {w_n} (book l. 13506–13513), so "finite changes"
  does not cover Remark 17.12 as the book carries it out (the theorem survives: deterministic w_n go into N^c, ρ^c);
  m3 §0's "E[R²|G]^{1/2} ≪ κ/log x" is not what Lemma 2.3 proves; m4 W(σ) defined for all σ at once (one clause).
- Next: own re-run in verify-O/ (exact grid variance; simulation at 10⁷), prior art.

## 11:28 IST 2026-10-01 — read-O (Opus reader), batch 2: independent re-run done (verify-O/)

- Grid variance (closed-form cell integrals, no quadrature): 54/54 grid sums = NOTE to 10 digits; N₀ = 0 continuum 27/27 to
  10 digits; N₀ = 1 continuum off by 10⁻⁶–10⁻⁵ in the NOTE (fixed-grid rule across the jump at v = 2x/3) → the NOTE's smallest
  gap "7.6·10⁻⁷" is really −1.53·10⁻⁶ (m5). All other quoted gaps reproduce.
- Own simulation at X = 10⁷ (exact Bernoulli on the true grid to unit 52, Poisson above; ρ with primes streamed to 10⁹), 5 seeds
  per template: sup [10³, X] 0.496 ± 0.022 (P_R), 0.485 ± 0.026 (P_B); msL 0.533, 0.530 — within 1 se of the NOTE's 10⁸ values.
  Controls: rational primes exact at 47 600 edges; residue identity to 16 digits; zero envelope violations.
- One scale on own realized systems: identity residual 0 (16/16); Var(E′)/σ²_cont 0.915–1.046 (all < 2 sd from 1); KS p ≥ 0.34.
- Observation: E < 0 on ≥ 89 % of the top two octaves in 9/10 runs (branch-point sign, random amplitude). Next: prior art.
