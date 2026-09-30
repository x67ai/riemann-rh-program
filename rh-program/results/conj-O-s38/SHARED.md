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

## 2026-10-01 02:38 — batch 1: task 1, identity + the reflected route's limit
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

## 2026-10-01 02:45 — batch 2: task 1 closed (G with T-parts), task 2 closed
- NOTE §1.4 Theorem Z [proved here, RH, single-check]: if P_R continues analytically with finite order to {σ > τ₀, |t| > T₀},
  τ₀ < α_R/2, then β₂(R) ≥ α_R/2 (mean-square form of O). Proof = Hilberdink's order-zero/Carlson device on log(ζ_P/ζ):
  (Z1) E ⇒ ζ_P ≪ |t|; (Z2) log D_R analytic, D_R zero-free; (Z3) RH ⇒ |D_R| ≪ |t|² (PL in the band, Lemma Z.b proved);
  (Z4) Borel–Carathéodory (Lemma Z.a proved) ⇒ |log D_R| ≪ log t; (Z5) smoothed Dirichlet polynomial + MV (G.27) ⇒
  Σ_{p∈R,p≤N}p^{−2σ} ≪ log²N, contradiction for 2σ < α_R.
- §1.5 Corollary Z.1 [RH]: every regular deletion (π_R = Σ min(1, cp^{α−1}) + O(x^θ), θ < α/2), EVERY c ⇒ β₂ ≥ α/2. The A8
  corner (c = 2 etc.) is closed as a refutation corner (U ⇒ RH, so RH-conditional suffices).
- §1.6 Lemma G (the exact missing lemma for general R) + Prop 1.6 (anatomy of a counterexample: P_R has no natural boundary in
  σ > β₂; ζ_P must have infinitely many zeros with Re in (τ₀, ½) for every τ₀ < α_R/2; π_R irregular at scale x^{α_R/2}).
- §1.7 additions: covered under a separation hypothesis; the A-clause "any A" is probably false as stated (near-cancelling
  additions a_p = p(1 + e^{−p}); heuristic).
- §2 task 2: named obstruction "sub-polynomial resonance"; the L² (Parseval) converse = Theorem Z.
- Next: task 3 (dyadic mean square from the on-disk CSVs; finite-R rung; new feedback design; 8 more T_0.75 seeds at 1e10).

## 2026-10-01 02:57 — batch 3: task 3, 8 extra seeds of T_0.75 at 1e10 (the F5 tension)
- `verify/thin_fr.c` = byte-identical copy of fr `verify/thin.c` (SHA-256 6d359b51…); seed 1, α = 0.75, X = 1e9 re-run
  reproduces every fr bin (`verify/data/xcheck_bern_a0.75_s1_1e9.csv`). Seeds 5–12 at X = 1e10, Y = 2e10: 72–76 s each,
  2.5 GB (`verify/run_seeds.sh`, `logs/run_seeds.log`, data `verify/data_big/bern_a0.75_s*.csv`).
- `verify/t3_seeds.py` → `logs/t3_seeds.log`. Top window [1e7, 1e10] sup-slope: seeds 1–4 0.450 ± 0.009 (= read-O F5),
  seeds 5–12 **0.363 ± 0.014**, all 12 **0.392 ± 0.016** (α/2 = 0.375: +1.1σ; 1/(3−α) = 0.444: −3.3σ). Dyadic mean-square
  slope, all 12: [1e4, 1e10] 0.723 ± 0.018, [1e7, 1e10] 0.787 ± 0.059 (α = 0.75; 2/(3−α) = 0.889). The four-seed excess was a
  small-sample fluctuation; the tension resolves toward α/2 (sup) and α (mean square).
- Preview (fr greedy data, `dyadic_ms.py`): greedy c = 1, α = 0.6: pure-power mean-square slope 0.445 over [1e4, 1e10] —
  below α − 0.15 over six decades, but Corollary Z.1 (RH) proves β₂ = α/2 for this set, so the deficit is a log-power
  (M ≈ X^α(ln X)^{−κ}, κ ≈ 3): the stop line's literal trigger "below X^{α−δ} over three decades" is met by a set that is
  provably NOT a counterexample (under RH). Log-corrected fits and the Franel-diagonal ratio next (`run_t3.sh` running).

## 2026-10-01 03:25 — batch 4: task 3 done (rungs 1–3 + the new design)
- Rung 1 (`t3_rung1.py`): finite R = {2..13}, {3..19} reproduce ρ2^|R|/12 (period mean square 7e-14, 7e-12; dyadic windows → 2e-5).
- Rung 2 (`t3_analysis.py`, `t3_ratio.py`, `t3_kappa.py`; R-numbers enumerated exactly by `rnums.c`, every R-set regenerated
  matches the fr headers' nR(X)): T_α mean-square slopes sit between X^α/ln X and X^α; M/M_diag flat, 5–70 (random R exceeds the
  truncated Franel diagonal several-fold).
- Rung 3: greedy c = 1, 2 at α = 0.6, 0.75 have pure-power slopes 0.13–0.31 below α over ≥ 3 decades and M/M_diag falling with
  κ ≈ 2.3–3 (5.9 for c = 2, α = 0.75, transient). The stop line's literal trigger is met by sets where β₂ ≥ α/2 is a THEOREM
  (c = 1 unconditionally: fr Theorem C in mean-square form, one line; c = 2 under RH: Cor Z.1) ⇒ log-power, not a counterexample.
- New design: online error-feedback deletion (`thin2.c` mode feedback; plain + `corr`; a first `corr` build had the correction sign
  reversed — kept as `*_corrplus_*`, labelled, unused). No run beats greedy durably; `corr` α = 0.75 fell to M/M_diag = 0.024 at
  1.6e8 but turns up (0.44 at 2.5e9, slope 1.23 on [1e7,1e10]); its 1e9 "success" was an artefact of freezing D beyond X.
  Mechanism (proved identity): E(x) = e(x) + ρx∫_x^∞(D(u) − D(x))u^{−2}du + O(1 + D²/x); deleting q changes E(y) by −E(y/q).
- Task 3 close: N (no structured counterexample; tension resolved; calibration lesson for the stop line).

## 2026-10-01 03:35 — batch 5: close
- Prior art (arXiv, 1 request at a time, 3 s spacing; `sources/arxiv-O-q*.xml`): nearest published object for the square-root
  law is Avdeeva 2015 (arXiv 1512.00149, fetched to `sources/avdeeva-2015-1512.00149v1.*`), Theorem 1 p. 3: SHIFT-AVERAGED variance
  of B-free counts in intervals of length N ∼ C·N^α for regular B-semigroups (constant carries Γ(2−α)ζ(2−α) = the reflected
  diagonal at σ = α/2). No Ω-result for the single interval [0, x] found. Theorem Z's device = Hilberdink 2005 (w-18a p. 336) and
  its Remark B(ii) (finitely-many-zeros hypothesis) — here on ζ_P/ζ.
- rdump/*.bin (194 MB, regenerable R-prime lists) deleted; rn/*.csv kept. Drivers made robust to the missing dumps.
- NOTE §0 (digest ranking quoted: U1 ranked 2nd in §F.2), §4 close written. **Close: G (Lemma G) with T-parts (Theorem Z, Cor Z.1,
  Prop 1.3, Remark 1.3′, Theorem C in mean-square form, corrected Prop 1.1); task 2 named obstruction; task 3 N; K none.**
- Stop line: task 1 closed (G). The task-3 trigger fired only in pure-power slope on sets covered by theorems (flagged).

## 2026-10-01 04:56 — reader O, batch 0: start (Opus reader of conj-O-s38)
- NOTE.md read whole: 41,290 B, 340 lines, SHA-256 c1050e62fd1892ff67c01354bd7abe2e0f3f03e517361caec3faeb02f32188e4.
  Also read: BRIEF, SHARED blocks 0–5, verify/ (scripts + logs), fr NOTE §§4–7, fr read-O, fr read-F. Not read (independence):
  the orchestrator's `read-F.md` of this unit (appeared 04:50).
- Deliverables: `read-O.md` (built section by section), `verify-O/` (own code only; nothing imported from `verify/`).
- Plan: §1 re-derivations (Prop 1.1 both forms, Parseval, Prop 1.3, Rem 1.3′, Theorem Z + Lemmas Z.a/Z.b, Cor Z.1, Lemma G/G′,
  Prop 1.6, §1.7, §2, §3 claims); §2 re-runs (Euler identity by raw class grouping, rung 1 exact, 12-seed stats from the CSVs,
  one new numpy seed T_0.75 at 1e9 with own RNG); §3 prior art at the page; Stirling spot check.
