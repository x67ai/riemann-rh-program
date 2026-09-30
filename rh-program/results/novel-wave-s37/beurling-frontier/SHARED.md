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
