# SHARED — unit `lemmaG-s39` (dated blocks, appended as results land)

## 2026-10-01 05:40 — ladder rung 1 (lemmaG-s39)
- Rung 1a (finite R), third route (dilation recursion MS(R∪{q}) = 2(1−1/q)MS(R) via the homogeneity c(qξ) = c(ξ)/q): exact in rationals
  on 12 sets + 6 cross terms, ALL EXACT (`verify/logs/rung1_finite.log`).
- Rung 1b (F_q[T], RH true): **the degree-wise Conjecture O is FALSE** — deleting M(a,N) (necklace number) irreducibles of each degree N
  gives D_R(u) = 1 − au and E_R(n) ≡ 0 with α_R = log a/log q. Brute force in F_3[T] (degrees ≤ 8) and exact generating functions (≤ 60)
  confirm; regular (round(a^N/N)) and random deletions on the same rung sit at a^{n/2} (`verify/logs/rung1_ff.log`).
- Consequence being written up: any proof of O / Lemma G must use a property of ℚ absent in F_q[T] (injectivity of the norm on ⟨R⟩).
## 2026-10-01 06:05 — rung-1 consequence + instrument built (lemmaG-s39)
- NOTE §1.3 (G₁): Lemma G and O fail at rung 1 (necklace deletion); every input of Theorem Z's proof except zero-freeness of D_R
  holds there; a proof over ℚ must use injectivity of the norm on ⟨R⟩ (±1 coefficients of D_R, no aggregation).
- Instrument `verify/lg.c` (+ `lg_core.h`): families sq (nextprime(p²)), nsq (nextprime(n²)), weyl ({p√2} < p^{α−1}), neck
  (necklace clusters at 4^N, tight/spread), planted (greedy with a planted pole of D_R at 0.45 ± 5i, α = 0.6). Second route
  (`xcheck_small.py`, `xcheck_planted.py`): R-lists regenerated in Python equal; every bin's sumE2 recomputed by inclusion–exclusion
  over R-numbers agrees to print precision (≤ 5e−7); ρ(sq), ρ(nsq) by independent products agree to 3e−12, 3e−15.
- 1e9 batch launched 05:30 (`verify/run_all.sh`, log `verify/logs/run_all.log`).
## 2026-10-01 06:40 — theory batch: §2 criterion, §3 T-parts (lemmaG-s39)
- §2.1 local structure theorem (unconditional): right of β₂, every singularity of P_R is −κ log(s − s₀) + analytic with κ = Σ_m μ(m)ord_{ms₀}D_R/m
  (integer for Re s₀ > α_R/2, half-integer on α_R/2); §2.2 criterion: ANY other singularity at Re s₀ = σ₀ forces β₂ ≥ σ₀ (natural
  boundaries, poles, essential/algebraic singularities, non-integer log coefficients, D_R-poles off ζ's zeros); §2.3 (RH, α_R < ½): a
  counterexample has D_R ANALYTIC on σ > β₂ with infinitely many zeros — "zeros or poles" sharpened to "zeros, no poles".
- T2 (uncond.): R_k = {prime in [p^k, p^k + p^{k(5/8+ε)}]} has β₂ ≥ α_R/2 = 1/(2k) via the pole of D_R at ρ₁/k (ζ(ρ₁/k) ≠ 0 since
  0 < γ₁/k < 14.13); irregular at scale x^{α_R/2}; P_R neither continues nor has a natural boundary — Prop 1.6's anatomy holds, O holds.
- T3 (uncond.): R = {nextprime(n^k)}, k ≥ 3: P_R ∋ ζ(ks), pole at α_R ⇒ β₂ = α_R; predicted E ≈ A x^{1/k}(log x)^{−3/4}cos(2√(log x/k) + φ).
- T4 (uncond.): greedy deletions with a planted x^{α/2} modulation over all rational frequencies: P_R has a NATURAL BOUNDARY on σ = α/2
  (the brief's shape (ii), deterministic) ⇒ β₂ ≥ α/2; general modulated class covered (forbidden singularity: uncond.; integer: RH).
- T5 (uncond.): spread ℚ-necklace: κ = Φ(½) = 2(√2−1) ∉ ℤ at s = α_R ⇒ β₂ = α_R. Tight ℚ-necklace = exact transplant of rung 1
  (D_R = (1 − 2·4^{−s})·C, analytic past α_R/2, infinitely many zeros, no poles; criterion silent).
- Theorem F (RH): Theorem Z with a model G divided out — if D_R = G·C, C zero-free with divergent diagonal, G polynomially bounded with
  polynomial min-modulus on circles, then β₂ ≥ α_R/2. Cor F.1: tight ℚ-necklace obeys O (C carries the prime diagonal).
