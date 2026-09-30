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
