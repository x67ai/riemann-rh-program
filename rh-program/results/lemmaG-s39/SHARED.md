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
## 2026-10-01 07:20 — computation batch (lemmaG-s39), X = 1e9 and 1e10
- Exact dyadic M(X) for 5 deterministic families + 2 controls to 1e10 (table NOTE §4.2). Controls fire: planted pole 0.45 ± 5i read at
  slope 0.906–0.940 (pred. 0.90); tight ℚ-necklace M/M_diag = 371 at 1e9 (coherent clusters, sup-slope 0.479 ≈ α_R); spread necklace
  slope 0.885 (T5's (log)^{−3.66} law); Weyl pseudo-random sets scatter like T_α.
- sq = {nextprime(p²)}: pure-power slope 0.422 on [1e6,1e10], M/M_diag 0.9 → 0.32 — the trigger fires on a PROVED set (T2). Explained:
  bin-mean E matches the 200-zero explicit formula Σ c_ρ x^{ρ/2} (corr 0.998 for x ≥ 1e8): log-periodic beat of ζ's low zeros.
- nsq = {nextprime(n²)}: T3's Bessel law J₁(√(2 ln x)) fits with R² = 0.995 at the residue-fixed frequency (best among w ∈ [0.7,1.3]).
- Cluster lemma checked: R_tight clusters span h_N ≈ c_N log 4^N; max|E| near cluster ≈ 1.9 c_N (N ≤ 16).
- No K-candidate; every sub-diagonal window is a proved mechanism.
## 2026-10-01 08:05 — prior art, close (lemmaG-s39)
- Prior art at the line (NOTE §5): Hilberdink 2005 Rem. B(ii) (relative form = §2.3), DMV 2006, Broucke–Vindas 2024 Thm 1.2 (nearest to
  the Weyl family), Avdeeva 2015 (stationary law; applies to sq only), Fabry/Pólya (void for {log p}), Breuer–Simon 2011 (Szegő, random,
  ergodic — all power series), Estermann–Dahlquist (constant local factor). arXiv q4–q6: 0 hits (not a novelty claim, zoo V.5).
- Correction made in §1.3(c): Theorem Z's hypothesis is VOID at rung 1 (Pringsheim + t-periodicity replicate the forced real zero at
  α_R at every height); the ℚ-input is ℚ-independence of log p (commensurability is what manufactures the necklace's off-axis zeros).
- CLOSE: G with T-parts (NOTE §6). (RH, α_R < ½) every counterexample lies in 𝒞_self; the diagonal method is silent there by
  definition, and the F_q[T] analogue of 𝒞_self contains the necklace (O false). Smallest unknown class: 𝒞_self over ℚ (no member known).
  Natural-boundary route for hash/pseudo-random R BLOCKED; missing input named: bilinear equidistribution of {pθ} at scale p^{α−1}.
- T2 second route: |ζ(ρ₁/k)| = 1.126, 0.665, 0.510, 0.448 (k = 2..5); C(ρ₁/2) = 0.036 − 0.361i (`verify/logs/t2_values.log`).
## 2026-10-01 08:30 — UNIT CLOSED (lemmaG-s39)
- NOTE.md final:    48965 bytes,      401 lines, SHA-256 37622108812a9942…; instrument verify/lg.c 5b90a5581fdc845e…, lg_core.h 97f26f6099f4e69c….
- Close: G with T-parts and a rung-1 counterexample (NOTE §6). Stop lines: no printed theorem decides Lemma G here; no K-candidate;
  natural-boundary route for hash/pseudo-random R blocked, missing input named (bilinear equidistribution of {pθ} at scale p^{α−1}).
- Untried entries UT-L1…UT-L5 in NOTE §6 (rung-1 → ℚ spread threshold; Weyl pair correlation; 𝒞_self membership test; trigger
  recalibration; T3 Bessel law across a period). Waste: two killed rung1_ff.py launches (label (ii), ~15 min).
## 2026-10-01 11:15 IST — read-O (Opus reader) batch 1: rung 1 (lemmaG-s39)
- NOTE read whole at SHA-256 37622108…9c72 (401 lines). read-O.md started; verify-O/ holds own code only.
- Thm R1 re-derived ✓. Own brute force (all monic polys, trial division): F_3 (a=2, deg ≤ 8), F_5 (a=2,3,4, deg ≤ 5), F_7 (a=3,
  deg ≤ 4), three deletion rules each (first/last/random choice of the M(a,N) irreducibles): N_P(n) = q^n − aq^{n−1} in all 15 cases.
  Exact series route: D_R ≡ 1 − 2u mod u^61; regular-control ρ and D_R coefficients equal to the unit's digit for digit.
- Every form of O (sup, mean-square, cumulative) fails at rung 1. Minor wording items only (ranges quoted from step-sampled n;
  "|ζ_P| ≤ C|t| trivially" false at rung 1 but unused; injectivity on ⟨R⟩ ≠ ℚ-independence in general).
