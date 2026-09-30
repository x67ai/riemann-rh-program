# SHARED — unit `conj-O-s38` (Conjecture O: the relative square-root law for deletions)

Append-only log of batches. Newest block last. Times IST.

## 2026-10-01 02:20 — batch 0: start
- Read BRIEF.md; frontier NOTE §§4–7, read-F.md (§4(a) contract), read-O.md (§2 F5, §4 A8, §7 next unit).
- Digest `results/novel-wave-s37/insights-digest.md` was ON DISK at start (64 789 B, 02:17). Its §F.2 ranks this unit
  **2nd** ("U1 — Conjecture O by the Franel/Landau mean-square route ... LAUNCHED"), consolidator's notes (i) refutation
  corner = read-O A8 (integer c ≥ 2, α < ¾), (ii) task 1's gap = "the classical Carlson obstruction", (iii) α = 0.75
  top-window tension to be decided by the dyadic mean square. Quoted in NOTE §0.
- Data on disk (not recomputed): frontier `verify/data/*.csv` (X = 10⁹), `verify/data_big/*.csv` (X = 10¹⁰); CSV rows carry
  per-bin sumE2 = Σ(N(n) − ρ(n + ½))², so the dyadic mean square is recoverable exactly (+ρ²/12 per unit, see NOTE §3).
- Plan: task 1 (identity, Carlson route, missing lemma), task 2 (resonance), task 3 (dyadic mean square: rung finite R,
  random R, greedy c = 1, 2, a new feedback design; 8 extra seeds of T_0.75 at 10¹⁰), task 4 close.
- Source hygiene: MV vol. II draft (on disk under `fetched-r2/`) extracted to `sources/mv2-draft.txt` for Theorem G.16 /
  (G.28) (Montgomery–Vaughan Hilbert inequality, p. 427, lines 23037–23060).

## 2026-10-01 02:55 — batch 1: task 1, identity + the reflected route's limit
- `verify/t1_classsums.py` → `logs/t1_classsums.log` (22 s): additive class sums c(a/b) = ρμ(b)b/(2πiaφ(b)) exact on 9 finite
  sets (coeff. to 1e-13; (1/Q)∫E² = ρ2^|R|/12 in rationals); reflected diagonal: the brief's Euler product MISSES the coprimality
  factor (1 − p^{2σ−2}) — brute force = corrected product to 1e-31 on 4 sets, sketch off (R={2}, σ=0.2: 6.929 vs 9.215).
  Divergence locus (2σ < α_R) unchanged. Stirling |χ| spot check OK.
- NOTE §1.1–1.3 written: Prop 1.3 (RH, α_R < ½): β₂(R) ≥ α_R/4 for EVERY R (quantitative Carlson on D_R; MV (G.27) quoted
  at the page image, MV-II draft p. 427). Remark 1.3′: the brief's gap-lemma ("finite order ⟹ mean value") is FALSE as posed:
  η(2s) has finite order, mean square ≪ T^{2σ} on [1/6, ¼) and divergent diagonal there.
- Found the repair (writing next, §1.4): take LOGARITHMS (Hilberdink 2005's device, w-18a p. 336; Borel–Carathéodory as in
  Broucke–Hilberdink 2024 ll. 200–212): if P_R = Σ_{p∈R}p^{−s} continues analytically (finite order) to {σ > τ₀, |t| > T₀},
  τ₀ < α_R/2, then under RH β₂(R) ≥ α_R/2. Regular (Theorem-C) deletions satisfy this for EVERY c ⇒ corner A8 closed under RH.
