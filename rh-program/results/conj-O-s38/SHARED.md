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

## 2026-10-01 05:08 — reader O, batch 1: §1.1–1.7 re-derived; euler_O + thin_O 1e9 done; 1e10 batch running
- `verify-O/euler_O.py` → `logs/euler_O.log` (64 s): class sums by RAW (n, m) grouping = a^{s−1}b^{−s}μ(b)ρ/Π(1−1/p) to 1e-30
  (5 sets, real and complex s); corrected diagonal = brute to ≤ 6e-30; sketch off 12–55%. **F1: Prop 1.1(a) must include b = 1**
  (c(a/1) = ρ/(2πia) ≠ 0; Parseval without b = 1 is short by ρ²/12); the writer's check skipped b = 1. Parseval exact on 8 sets.
- Re-derived ✓: Prop 1.3, Theorem Z (Lemmas Z.a, Z.b, Z1–Z5), Cor Z.1, (G′), Prop 1.6(i)–(iii), §1.7. F2: Lemma G is, for each R
  under RH, equivalent to O₂(R) (vacuous if O holds) — a reformulation, to be labelled so. Minor: Rem 1.3′ shows α/3 is a barrier
  for growth-only input at α = ½, not that α/4 is the limit; Theorem B's mean-square form (a.s.) needs a 3-line Fubini/0–1 addition.
- `verify-O/thin_O.py` (own numpy sieve + PCG64 RNG + scipy E1 tail; tested vs brute force at 1e6, `logs/test_thin_O.log`):
  T_0.75 seed 1001 at X = 1e9 (Y = 4e9) in 17 s (`logs/thin_O_1e9.log`). Because it is this fast, 8 new seeds (1002–1009) at
  X = 1e10, Y = 2e10 run sequentially via `run_O_1e10.sh` (≈ 2 min each, one heavy process) → `data/bern_O_a0.75_s*_1e10_*.csv`.

## 2026-10-01 05:40 — reader O, batch 2: independent re-runs done; prior art read at the page
- 8 new seeds (1002–1009) of T_0.75 at X = 1e10 with own numpy code + PCG64 (≈ 2 min each, `logs/run_O_1e10.log`). Reader's
  own code with the WRITER's hash reproduces writer seed 5 at 1e10 bin for bin (nR, ρ, E(X) identical; bins to print precision;
  `logs/xhash_compare.log`) — the writer's data are exact.
- `seeds_O.py` reproduces every §3.3 number from the CSVs. New 8 seeds: top-window [1e7,1e10] sup-slope 0.399 ± 0.011
  (writer 12: 0.392 ± 0.016; pooled 20: 0.395 ± 0.010), but top-window MEAN-SQUARE slope 0.860 ± 0.039 (writer 12: 0.787 ± 0.059;
  pooled 20: 0.816 ± 0.039 — 1.7σ above α = 0.75, 1.9σ below 2/(3−α) = 0.889). Full window [1e4,1e10] ms: 0.754 ± 0.022 (≈ α).
  So "resolves toward α (mean square)" is not supported in the top window (F3). fr seeds 1–4 = top 4 of 12 (p = 1/495) is a
  post-selection effect (they prompted the question); fresh samples regress, as the NOTE says.
- `greedy_O.py`, `feedback_O.py`: §3.4–3.5 numbers reproduced (κ 3.00/2.80/2.32/5.92; corr runs 0.043 → … 0.441). F4: "provably
  log-powers" → the log-power form is a fit; what is proved is β₂ ≥ α/2.
- `stirling_O.py`: |χ|(t/2π)^{σ−½} = 1 + O(t^{−2}) by two routes (ζ(s)/ζ(1−s) and the Γ closed form), 18 digits agree.
- Prior art at the page: Hilberdink 2005 pp. 335–337 (images: Cor 2(a),(b), Rem B(i),(ii), Carlson needs (3.1), device uses
  φ_P = −ζ′_P/ζ_P); MV-II p. 427 Thm G.16 (G.26)–(G.28) (image) ✓; BH 2024 ll. 60–100, 197–215; BDR ll. 1160–1232 (their §5 already
  has log ζ_S(s) = log ζ(s+1−α) + O(√log|t|) on Re s ≥ α/2 + ε under RH — the analytic input of Cor Z.1 for c = 1, used there for
  upper bounds); Hilberdink 2010 + 2025 erratum (mean-value Ω for ζ_P, flawed proof). Reader arXiv sweep (10 queries,
  `verify-O/arxiv/`): nothing on Theorem Z / Lemma G.
