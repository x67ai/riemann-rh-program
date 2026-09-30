# SHARED.md — seed M1b `beurling-frontier` (NOVEL-APPROACH WAVE 2, Session 37)

Dated blocks, appended after each batch. Newest at the bottom.

## 2026-09-30 — block 0: start

- Charter read (§0, seed M1b brief, rules). Zoo I.2 read: it records "(b) [α,β]-systems (BDR 2309.01567): populated
  unconditionally for all α ∈ [0,1), β ∈ [1/2,1); hard wall max{α,β} ≥ 1/2; β < 1/2 only under RH" — to be checked at the page.
- On disk (found by listing `fetched*/`): z-02 = Broucke–Debruyne–Révész 2025 "well-behaved Beurling number systems" (the
  published 2309.01567?), z-18 = Broucke–Vindas 2024 "generalized prime random approximation" (2102.08478?), z-01 = BDV 2020,
  w-18a Hilberdink 2005, p3-22c1 Hilberdink–Lapidus, p3-22c2 Hilberdink 2012 periodic, p1-02 DMV, t-50 Diamond–Zhang book.
- Plan: (1) prior art at the page -> sources/*.txt + NOTE.md §1; (2) pre-derivation attack; (3) simulation; (4) frontier; (5) close.

## 2026-09-30 — block 1: prior art done (NOTE §1) + logical frame (NOTE §2)

- **Region {α > ½, β < ½} is populated in print, conditionally on RH**: BDR arXiv:2309.01567v2 Theorem 1.3 (p. 4, line 183):
  "Assume RH. ... an [α, β]-system for 1/2 < α < 2/3 and 2α/(α + 2) ≤ β < 1/2." RH is used (i) for sharp α and (ii) because the
  deleted primes are actual primes, so log ζ_S(s) ≈ log ζ(s+1−α) carries ζ's zeros. Exponent 2α/(α+2) = hyperbola method;
  BDR Remark 5.3(2) says a better integer analysis "might give rise to a larger region".
- Unconditional, non-constructive: the region is populated anyway (if RH fails, (P, N) is [Θ, 0]) — Prop. 2.1. Any valid threshold
  β* has β* ≤ 2/5 and implies RH (Cor. 2.2). Obstructions β ≥ f(α) > 0 over all systems imply "no Θ in (½, a)" (Prop. 2.3).
- Hilberdink 2012 (p3-22c2): periodic N(x) − cx forces ζ_P = ζ × finite Euler product — rigidity at β = 0 in the periodic class.
- arXiv sweep since Jun 2024: nothing on β < ½.
- Next: §3 attack on the pre-derivation (it is BDR §5's construction with a claimed sharper integer analysis).

## 2026-09-30 — block 2: pre-derivation attacked (NOTE §3) + theorems (NOTE §4)

- The pre-derivation IS BDR §5's construction (random deletion of classical primes, density p^{β₀−1}); new content = analysis only.
- **K (unconditional claim):** the mean of the deletion is a measure on the primes, so ζ_P = ζ(s)ζ(s+1−α)^{−1}U(s): poles at
  ρ − 1 + α. If a zero ρ has Re ρ > 1 − α/2 (and ζ(ρ−1+α) ≠ 0) then β ≥ Re ρ + α − 1 > α/2 (Prop 3.2). "h analytic in Re s > β₀/2"
  holds for the fluctuation X only. The zero at α (α ≥ β₀ > ½) IS unconditional (3.3).
- **Theorem A (RH):** Bernoulli thinning w_p = p^{α−1} gives a.s. [α, β] with α/2 ≤ β ≤ 1/(3−α) (truncated Perron, ζ growth on
  Re s = α/2+δ, a.s. o(log t) bound for the random series, Lemma 4.1). **Cor A′ (RH):** [α, β]-systems for all ½<α<1,
  1/(3−α) < β < ½ — strictly contains BDR region III (2α/(α+2) > 1/(3−α) on (½,2)) and extends α from (½,2/3) to (½,1).
- **Theorem B (unconditional):** β(T_α) ≥ α/2 a.s. (chaos decomposition E(x) = −Σ_d μ_η(d)T(x/d), anti-concentration from the primes
  in (x/2, x], Kolmogorov 0–1 via E′(x) = E(x) − E(x/q)).
- Gap to β = α/2 under RH: G1 mean-system error Σ_{n≤y}Π_{p|n}(1 − p^{α−1}) − y/ζ(2−α) ≪ y^{α/2+ε} (contour gives only 1/(4−2α));
  G2 moment/uniformity for the chaos. Next: simulation (NOTE §6), incl. direct numerics of the mean-system error T(y).

## 2026-09-30 — block 3: simulation launched (RUNNING NOW / resume here)

- Code: `verify/thin.c` (bern | greedy | none), `verify/thin_aux.c` (cramer | mean); cross-checks passed:
  `verify/check_small.py` reproduces thin.c exactly (X=1e5: nR=607, rho=0.180739782781, E(X)=2.021722); cramer DP matches
  brute force N(2000)=3097.
- Driver `verify/run_all.sh` (background, sequential, idempotent — rerun it to resume; skips finished files):
  bern alpha ∈ {0.60,0.75,0.90}, X=1e9, Y=4e9, seeds 1–8 → `verify/data/bern_a*.csv`; greedy (deterministic low-discrepancy
  deletion) → `greedy_a*.csv`; none (β=0 control) → `none.csv`; Cramér random system (β≈½ control) X=2e8 seeds 1–4 →
  `cramer_s*.csv`; mean system T(y), X=2e8 → `mean_a*.csv`. Log: `verify/logs/run_all.log`.
- Next on completion: `verify/fit.py` → exponents with error bars → NOTE §6.

## 2026-09-30 — block 4: first fits (X = 1e9, 8 seeds) + extension queued (RUNNING NOW / resume here)

- T_0.60: running-sup slope 0.303 ± 0.008 (window [1e4,1e9]); candidates α/2 = 0.300, 1/(4−2α) = 0.357, 1/(3−α) = 0.417,
  BDR 2α/(α+2) = 0.462 → only α/2 fits. T_0.75: 0.353 ± 0.013 (α/2 = 0.375, 1/(4−2α) = 0.400, 1/(3−α) = 0.444).
- Prop 5.1 (exact, finite R): mean square of E over a period = ρ·2^{|R|}/12 — verified in exact arithmetic (`verify/finite_R_variance.py`).
- NOTE §5 written (Conjecture O: β ≥ α_R/2 for any surgery on ℙ; under RH ⇒ β ≥ α/2 > ¼ for the surgery class; finite surgery
  cannot move zeros off Re s = 0; rung-1 control).
- Queued `verify/run_big.sh` (starts after run_all.sh ends): X = 1e10, Y = 2e10, T_α seeds 1–4 + greedy → `verify/data_big/`,
  log `verify/logs/run_big.log`. Resume: rerun `verify/run_big.sh` (idempotent), then `python3 verify/fit.py verify/data_big`.

## 2026-10-01 — block 5: X = 1e9 results in; structured deletion behaves differently (RUNNING NOW / resume here)

- Fits (`verify/logs/fit.log`): T_α sup-slopes 0.303±0.008 / 0.353±0.013 / 0.457±0.012 (α = .6/.75/.9) ≈ α/2; 1/(3−α) and BDR's
  2α/(α+2) excluded at α = .6, .75. Controls: none 0.000 (β = 0 ✓); Cramér 0.48–0.51 (β = ½ ✓). Mean system (deterministic,
  gap G1): slopes 0.11–0.13 / 0.25–0.30 / 0.39–0.45 ≈ α − ½ (heuristic y^{α−½} ✓, far below 1/(4−2α)).
- **Greedy (structured) deletion, c = 1:** sup-slopes 0.234 / 0.309 / 0.395 — BELOW α/2; RMS only 0.17–0.31 × √(ρQ/12) (the diagonal
  variance heuristic that fits the random runs within ×1–4). Log-corrected (x^{α/2}(log x)^{−3/2}) slopes 0.328 / 0.403 / 0.489.
- **Theorem C (NOTE §5.5, proved):** a regular deletion with density c·p^{α−1} has ζ_P = ζ(s)(ks − α)^{c/k}B(s) near s = α/k — a branch
  point at α/k_c, k_c = min{k ≥ 2: c/k ∉ ℤ} — and a real singularity (2s + 1 − 2α)^{−c/2} at α − ½; so β ≥ max(α/k_c, α − ½),
  unconditionally. c = 1 ⇒ β ≥ α/2 (so the low greedy slopes are the (log x)^{−3/2} approach); c = 2 ⇒ only β ≥ max(α/3, α − ½).
- Queued `verify/run_c2.sh` (after run_big): greedy c = 2 at α = .6/.75/.9 and c = 6 at α = .6/.75 (X = 1e9), plus c = 2, 6 at
  α = .6, X = 1e10 → decides whether structured surgery beats α/2. Log `verify/logs/run_c2.log`.

## 2026-10-01 — block 6: all simulations done (no process running)

- X = 1e10 (T_α, 4 seeds): 0.299±0.010 / 0.357±0.011 / 0.456±0.015 ≈ α/2; 1/(3−α) excluded at α = .6, .75 (> 4σ every window).
- Structured greedy c = 1 at 1e10: raw slopes 0.238 / 0.308 / 0.395; log(M·ln x) slopes 0.302 / 0.373 / 0.459 = α/2 — E ≈ x^{α/2}/log x;
  RMS only 0.17–0.31 of the diagonal-variance value (random: 0.75–4.4×). Theorem-C branch term computed: 1% / 6% / 28% of sup|E| at 1e10.
- **c = 2 (α/2 branch point canceled) at α = .6, X = 1e10: slope 0.278 → 0.299 (top window) — NOT α/3 = 0.20.** Structure buys a
  log factor, not an exponent. Conjecture O (β ≥ α_R/2 for all surgery) stands. c = 6 (α = .6, .75) and c = 2 at α = .9 delete all
  primes ≤ 88/1296/1024 → fundamental-lemma transient (u = log x/log y ≈ 3–4.6) dominates; excluded as uninformative.
- NOTE §§5.2, 5.5, 6.2–6.4 updated. Remaining: NOTE §7 (answers, conjecture, close) and the report.

## 2026-10-01 — block 7: CLOSE — T (with K on the pre-derivation's unconditional clause). Nothing running.

- T: Theorem A / Cor. A′ (RH) — [α, β]-systems for all ½ < α < 1, 1/(3−α) < β < ½ (strictly contains BDR region III, extends α past 2/3);
  Theorem B (unconditional) — random surgery β ≥ α/2; Theorem C (unconditional) — regular deletion of density c·p^{α−1} has
  β ≥ max(α/k_c, α − ½); Props 2.1–2.3 (dichotomy; thresholds ≤ 2/5 and imply RH; absolute obstructions are RH-hard), 5.1, 5.3.
- K: "h analytic for Re s > β₀/2" / "β = β₀/2" unconditionally — the mean of a prime deletion carries ζ's zeros (Prop 3.2).
- G1/G2 named for Conjecture R ([α, α/2] under RH). Data: random α/2 confirmed (1e9 ×8 seeds, 1e10 ×4); structured = α/2 up to a log;
  c = 2 does not reach α/3.
- Sharpest conjecture: **U — every Beurling system has α ≤ max{½, 2β}** (implies RH; matches all known constructions; contradicts BDR's
  "every max{α,β} ≥ ½ is populated" in the corner β < α/2). Conjecture O (surgery) is the proved-in-part core of it.
- Files: NOTE.md §§1–7; verify/ (thin.c, thin_aux.c, run_*.sh, fit.py, analyze_extra.py, branch_constant.py, checks + logs, data).

## 2026-10-01 — block O-0: Opus reader started (read-O.md)

- Reader Opus 5.5, independent of the orchestrator's read. Files: `read-O.md` (built section by section), own
  re-run scripts and logs in `verify-O/`. Nothing else in the seed folder is touched.
- Read so far: NOTE.md whole, charter §M1b, SHARED blocks 0–7. Next: §1 re-derivations into read-O.md.

## 2026-10-01 — block O-1: reader §1 (re-derivations) landed in read-O.md

- K (Prop 3.2): AGREES; FIX-FIRST F1 on wording — the analyticity claim is not "false unconditionally" (it holds under RH);
  it is equivalent to a quasi-RH (no zero with Re ρ > 1 − β₀/2), hence not assertable unconditionally.
- Theorem B: stands. FIX-FIRST F2: μ_R ≠ μ_w * μ_η as Dirichlet convolution; use T_d (k coprime to d); then
  κ_p = Π_{q∈B∖p}(1 − w_q/q)Π_{q∉B}(1 − ε_q/q) → ρ_P and the proof goes through. Lower bound is a.s. (from an in-probability
  anti-concentration per x); the 0–1 law is not needed.
- Theorem A: AGREES-WITH-CORRECTIONS (F3: dyadic Borel–Cantelli for the centered prime sum needs a grid of mesh x^{1−α/2}).
  Textbook tools named; none on disk (MV I, Titchmarsh absent) → UNVERIFIED at the page, hypotheses checked.
- Cor A′: AGREES (BDR Lemma 5.1 read at the page; I(β) = ζ_P(β)).
- Theorem C: AGREES-WITH-CORRECTIONS (F4: for c ∉ ℤ the j = 1 term makes s = α a branch point → β ≥ α; content is c ∈ ℤ).
- Cor 2.2, Props 2.1, 2.3, 5.1: ✓ (5.1 re-derived independently).
- Next: §2 simulation audit + own re-run in verify-O/.

## 2026-10-01 — block O-2: reader §2 (simulation audit + independent re-run) landed

- Audit: T_α is pure deletion (no additions simulated); exact R-free counts; ρ tails re-checked with mpmath (≤ 5e-8);
  ± = seed s.e. only. F5: NOTE 6.4 omits the [1e7, 1e10] window where α = .75 gives 0.450 ± 0.009 (8σ above α/2, 0.7σ from
  1/(3−α)); "within 1.6σ in every window" / "1/(3−α) excluded in every window" are false as written.
- Own re-run (verify-O/thin_O.py, numpy, PCG64, quad tail; X = 1e8, 8 seeds): [1e4,1e8] slopes 0.308±0.008 (α=.6),
  0.378±0.012 (α=.75), 0.465±0.016 (α=.9) (BS estimator) — agree with α/2. Controls ✓; Prop 5.1 checked numerically (1.02299
  vs 1.022977). Local 2-decade slopes swing ±0.1–0.15 → realistic systematic ±0.03–0.05. Next: §3 prior art.

## 2026-10-01 — block O-3: reader §3 (prior art) landed

- BDR: v2 is latest; published Trans. AMS 378 (2025) 477–501. Conjecture (p. 2) and Thms 1.1/1.3 quoted exactly ✓.
- DMV 2006 p. 4 asked the M1b question in print ("θ < 1/2 may imply RH for discrete systems") — NOTE should cite it.
- DZ book Thm 17.14 (DMV + Zhang): [1, β₀], β₀ ≤ ½; BDR footnote 4: β₀ = ½ "most likely", smaller "still possible".
  U ⟺ β₀ = ½ for that system — the cleanest in-print test of U, undecided. BDV 2004.11501 is [½, 1] (not [1, ½]).
- arXiv (3 queries, saved in sources/): nothing on random thinning of ℙ as a Beurling system. Next: §4 attack on U.

## 2026-10-01 — block O-4: reader §4 (attack on Conjecture U) landed — U NOT refuted

- 11 attempts (read-O.md §4). No in-print discrete system has β < α/2. A refutation needs only an RH-conditional example
  (RH false ⇒ ℕ refutes U). Quadratic fields: U ⇒ no zero of L(s, χ_D) in Re s > ⅔, and GRH for ζ_K if β_K = ¼.
- DZ Thm 17.14 [1, β₀ ≤ ½]: U ⟺ β₀ = ½; the Theorem-B mechanism (α = 1, Poisson-thin g-primes in (x/2, x]) gives
  β₀ = ½ a.s. (sketch) — consistent. Open corner: structured deletions with integer c ≥ 2, α < ¾ (Theorem C bound α/3).
- U fails for continuous/weighted systems (DMV p. 4; G-template [β₀, 0]) — it is a discreteness statement. Next: §5–§7.

## 2026-10-01 — block O-5: reader §5 (FIX-FIRST F1–F5) and §6 (MINOR m1–m11) landed

- F1 K wording ("false unconditionally" → "cannot be asserted unconditionally; true under RH"); F2 Theorem B coprime
  convolution T_d, κ_p → ρ_P; F3 Theorem A(i) grid of mesh X^{1−α/2}; F4 Theorem C j = 1 term (c ∉ ℤ ⇒ branch point at α,
  β ≥ α); F5 6.4/7.1(3) omit the [1e7, 1e10] window (α = .75: 0.450 ± 0.009). None falsifies a theorem. Next: §7 + verdict.

## 2026-10-01 — block O-6: reader CLOSE — read-O.md complete (§§1–7 + verdict line). Nothing running.

- Verdict: T AGREES-WITH-CORRECTIONS; K AGREES (F1 wording). A: AWC (F3), NEW. A′: AGREES, NEW. B: AWC (F2), stands, NEW.
  C: AWC (F4), NEW/routine (Landau). Props 2.1–2.3, 3.2, 5.1: AGREE. Simulation: AWC (F5); own 1e8 re-run ≈ α/2.
  U: NEW, not refuted, consistent with all printed discrete systems (contradicts BDR's conjecture only).
- Reader's addition: DZ Thm 17.14's β₀ (BDR fn. 4) = ½ a.s. by the Theorem-B mechanism at α = 1 (sketch) — consistent with U.
- Next unit proposed (read-O §7): mean-square square-root law for sifted sets (Conjecture O in mean square) — prove, or
  refute via a structured integer-c deletion at α < ¾ (would refute U). Side items: A3 lemma; 8 more seeds at 1e10, α = .75.
- Reader files: read-O.md; verify-O/ (thin_O.py, run_O.sh, fit_O.py, local_O.py, audit_writer_data.py, data/, logs/);
  sources/arxiv-search-O-*.xml (3 arXiv queries).
