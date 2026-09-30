# SHARED — seed N3 `fingerprint` (Jacobi / Schur / Verblunsky parameters of ζ)

Append-only, dated blocks, one per unit of work. Agent: Opus 5.5 (default effort), wave S36, 2026-09-30.

---

## 2026-09-30 17:58 — Unit 0: setup, objects, plan

**Read:** WAVE-CHARTER.md (all), STATUS.md 72–103, BARRIER-ZOO §0, I.1, IV.1, IV.9, V.4, V.5 (heads).

**Tooling found:** python-flint 0.6.0 (Arb ball arithmetic) is installed; `arb_series.zeta` (Hurwitz, with
`deflate=True`), `lgamma`, `log` on power series. Timing: Taylor series of ζ at s = 1/2, length 1300,
12 000 bits, 13.5 s. This makes the moment route *rigorous* (every number is a ball with a proved radius), so
"verified digits" = digits certified by the ball radius, not printed digits. mpmath 1.3.0 (pure-Python
backend) for the independent zeros route (`mpmath.zetazero`).

**Objects as I will use them (derivations go in NOTE §1; each is checked on toys in Unit 1):**

- E(w) := Ξ(√w) = ξ(1/2 + i√w), genus 0 in w, zeros w_k = γ_k² (γ_k > 0 or Re γ_k > 0, one per ± pair).
- Power sums s_m := Σ_{γ>0} γ^{−2m} = (−1)^{m+1} m c_{2m}, where log ξ(1/2 + x) = Σ c_k x^k.
- Stieltjes function F(w) := −E′(w)/E(w) = Σ_{γ>0} 1/(γ² − w) = Σ_{m≥0} s_{m+1} w^m
  = ∫ dν(y)/(1 − wy),  ν := Σ_{γ>0} γ^{−2} δ_{γ^{−2}} (weight = location × multiplicity).
- S-fraction F = c_0/(1 − α_1 w/(1 − α_2 w/(1 − …))), c_m = s_{m+1}; J-fraction by even contraction:
  a_0 = α_1, a_n = α_{2n} + α_{2n+1}, b_n² = α_{2n−1}α_{2n}.
- Circle side: z_ρ := 1 − 1/ρ; C(z) := 2 ξ′/ξ(1/(1 − z)) (Carathéodory under RH);
  σ := Σ_ρ |ρ|^{−2} δ_{z_ρ} (finite; NOT Σ_ρ δ_{z_ρ}, which is infinite);
  moments m_n = λ_{n+1} − 2λ_n + λ_{n−1} (λ_0 = 0, λ_{−n} = λ_n), m_0 = 2λ_1; Verblunsky α_n^V of σ/m_0.

**Plan:** U1 toys (real-rooted polynomial; complex pair; sin√w/√w with exact S-fraction 1/((2n+1)(2n+3)); circle
toys) → U2 ζ tables by Arb (moments at 1/2; Li at 1) → U3 zeros cross-check (mpmath.zetazero + smooth tail)
→ U4 mining → U5 controls (curve over F_q exact; L(χ₄); DH; F_{a,q}) → U6 task (d) → U7 prior art → NOTE.

## 2026-09-30 18:10 — Unit 1: toys (verify/u1_toys.py, .log, .json) — ALL PASS

- T1 (E = Π_{k≤6}(1 − w/k²), exact rationals): S-fraction signs `+++++++++++0` — 11 positive, α_12 = 0 exactly
  (a 6-atom measure on (0,∞) terminates at α_{2K}). ✓
- T2 (one complex pair among 6 atoms, 4 placements): Hankel det signs = Heine-formula signs (rel. agreement
  1e-40) in every case; first failure of D_n = det(c_{i+j}) at n = r+1 or r+2, r = number of real atoms with
  larger |y| than the pair (r = 0 → n = 2; r = 3 → n = 4; r = 4 → n = 6, twice). The S-fraction goes negative at
  the matching index. Prediction rule confirmed: the failure index is the depth of the complex atom in the
  measure (in the "frozen" regime; for dense spectra more atoms must be killed — see visibility, later units).
- T3 (sin√w/√w): exact S-fraction α_n = 1/((2n+1)(2n+3)) for n = 1..60 ✓ (Lambert/Gauss). Precision law in Arb:
  certified digits at P = 800 bits: n = 1:239, 10:226, 20:205, 30:180, 40:151, 50:122, 60:91 — loss ≈ 2.5–3.1
  digits per S-index at n ≈ 50 (grows like ~2 log10 n per step). Planning figure for ζ: α_n up to n ≈ 600 needs
  ≈ 3000+ digits.
- C1/C2 (circle; ξ-like finite products): m_n from λ_n (second differences) = m_n from atoms (1e-60) ✓;
  Levinson = Schur algorithm (independent) to 1e-41 before termination ✓; on-line 6 atoms: |α_5| = 1 exactly
  (termination) ✓; one pair off the line (β = 0.8 at γ = 5, or β = 0.55 at γ = 8): |α_5| = 1.00448 resp.
  1.0000019 > 1 → Toeplitz positivity fails at index 5, while λ_1..λ_10 are all positive (Li blind at n ≤ 10). ✓
- Pattern: circle Verblunsky coefficients alternate in sign with |α_n| close to 1 (the measure σ lives on a
  small arc around z = 1).

## 2026-09-30 18:40 — Unit 2: ζ real-side table (certified) + first mining (verify/u2_prod.py, u2b_conditioning.py, u4_mine_real.py)

- **Conditioning measured (u2b):** intrinsic precision loss ≈ 4.7–6.6 decimal digits per index on BOTH sides (real
  S-fraction and circle Verblunsky), growing slowly with n. Ball arithmetic is tight on the real side (certified ≈
  actual − 10 digits) but blows up on the circle side (Levinson/Schur dependency) → circle side is run in midpoint
  arithmetic at two precisions + two algorithms (Levinson vs Schur), verified digits = agreement.
- **ζ real side, P = 24 000 bits, M = 1000 (tables/zeta_real_P24000_S1000.json):** s_1..s_1000 and the S-fraction
  α_1..α_999 of F(w) = Σ_{γ>0} 1/(γ² − w), ALL CERTIFIED POSITIVE (ball arithmetic; ≥ 1192 certified digits at
  n = 999, 7216 at n = 1). Hence det(s_{i+j+1})_{n×n} > 0 for n ≤ 500 and det(s_{i+j+2}) > 0 for n ≤ 499 (Grommer
  data, certified). FE check: all odd Taylor coefficients of log ξ at 1/2 contain 0. ξ(1/2) = 0.4971207781883141099….
  s_1 = 0.023104993115418970789, s_2 = 3.7172599285269686165e-5, s_3 = 1.441739314009732797e-7.
  α_1..α_10 = 0.0016088556745971, 0.0022696444618758, 0.0012309447733972, 0.0010732871255927, 0.00072505601164270,
  0.00067059821555097, 0.00054658061766807, 0.00056250296730745, 0.00051079519107545, 0.00048491414387630.
- **Asymptotic law (WKB/Abel inversion of the zero density, NOTE §3):** α_n ≈ W(n/2π)²/(16 n²), W = Lambert W.
  Test A_n := 4n√α_n vs L_n = W(n/2π): n = 100: 2.0723 vs 2.0496; 500: 3.2529 vs 3.2104; 999: 3.7557 vs 3.7477.
  Residual A_n − L_n: mean +0.0076, std 0.042 on n ∈ [500, 999] — the law holds to ≈ ±2% with OSCILLATING
  (not drifting) residuals — candidate imprint of S(t) (zero fluctuations) → to be tested for log p lines.
- **Exact sum rule** Σ_n α_n = s_1 (tr J_s² for the zero-diagonal Jacobi matrix with spectrum {±1/γ}): partial sum
  n ≤ 999 plus WKB tail = 0.0230982 vs s_1 = 0.0231050 (tail is approximate) ✓.
- **Information content:** the site n corresponds (WKB turning point) to height t_n ≈ 2n/L_n; α_n for n ≤ 999 encode
  the zeros up to t ≈ 533 (≈ 293 zeros): about π coefficients per zero.
- Running now: ζ circle side (λ_n, Verblunsky) N = 1000 at 24 000/30 000 bits → tables/zeta_circle_P24000_S1000.json.

## 2026-09-30 19:15 — Unit 2b: ζ circle side + the Szegő identity (u2_prod.py circle; u4_mine_circle.py)

- **ζ circle side, N = 1000 (tables/zeta_circle_P24000_S1000.json):** λ_1..λ_1001 certified positive (Arb balls,
  ≥ 6891 certified digits); Verblunsky α_0..α_999 of σ = Σ_ρ |ρ|^{−2}δ_{1−1/ρ} by Levinson at 24 000 and 30 000 bits
  and by the Schur algorithm (independent) — verified digits (min agreement) 7223 at n = 0, 2528 at n = 800;
  all |α_n| < 1. λ_1..λ_5 = 0.02309570896612103, 0.09234573522804667, 0.2076389205543248, 0.3687904794922416,
  0.5755427144611775; λ_1000 = 2326.053161686466. α_0..α_5 = 0.9991968067208526, −0.9988664119479066,
  0.9993846794038305, −0.9994634913667254, 0.9996375132820949, −0.9996647738964953.
- **Sign law (all n ≤ 999):** α_n = (−1)^n |α_n| (σ lives on the arc |θ| ≤ 2 arctan(1/(2·14.13)) ≈ 0.0707 around z = 1).
- **Circle asymptotic law:** ε_n := 1 − |α_n| ≈ W(n/2π)²/(32 n²); ratio ε_n/pred at n = 100, 400, 800, 998, 999:
  1.035, 0.972, 1.008, 1.003, 0.989 (oscillating, as on the real side).
- **Proposition S (Szegő identity; proof = Szegő's mapping theorem + push-forward computation, NOTE §2):** the
  Verblunsky data of σ ARE the Jacobi data (Geronimus relations) of μ_Sz = Σ_{γ>0} 4v δ_v, v = 1/(2|ρ|²), i.e. of the
  SHIFTED real problem F̃(w) = Σ_{γ>0} 1/(1/4 + γ² − w) (log ξ expanded at s = 1 in w = s(1−s)). Checked: Route A
  (α_n → Geronimus) vs Route B (log ξ(1+u) ∘ u(w), u = (√(1−4w) − 1)/2 → S-fraction, Arb) agree to 3.6e-53
  (diagonal) and 4.8e-50 (off-diagonal) for n = 1..149 (limited by the 60-digit table strings). So the seed's two
  families (i) and (ii) are ONE object at two expansion points (s = 1/2 vs s = 1), not two.
- Intrinsic conditioning is the same on both sides (≈ 6 digits per index), as Proposition S predicts.
- **Prior art (first sweep, verify/u7_arxiv.py, verify/arxiv/summary.json):** Zhang arXiv:1510.03420 (genus-0 entire
  function has only positive zeros ⟺ Hausdorff moment condition on power sums; applied to RH) — Grommer-type
  criterion is on arXiv; Voros arXiv:1403.4558, 1602.03292, 1703.02844, 2204.01036 (superzeta functions = our power
  sums; Keiper–Li asymptotic criterion; DH analogs "selectively react to zeros off the critical line");
  Suzuki arXiv:2206.03682 (screw function; an analog of Weil positivity / Li's criterion); Romik arXiv:1902.06330;
  Johansson arXiv:1309.2877 (Arb; Keiper–Li record computations); Farmer arXiv:2008.07206 (criteria for useful RH
  equivalences). No hit for Jacobi/Verblunsky/Schur parameters of ζ's zero measure (single check; V.5: not evidence).

## 2026-09-30 19:45 — Unit 3 (zeros route, independent) + Unit 5a (controls, first batch)

**U3 (verify/u3_zeros.py, u3a_zeros_chunk.py; run_u3.out; u3_zeros_N30000.json):** 30 001 zeros by Arb
(acb.zeta_zeros, certified on the line, 138 bits; tables/zeta_zeros_arb.txt); mpmath.zetazero (independent code)
agrees to 2e-34..4e-31 at n = 1..10⁴. Tail beyond T = 25755.53 (N(T) = 30000 exactly; S(T) = −0.39795) by the
smooth density θ′/π plus the boundary term −f(T)S(T). Against the Arb Taylor route:
- s_1: 1.7e-12 rel (predicted ≤ 2.6e-11); s_2: 3.2e-18; s_3: 1.9e-24; s_4: 1.2e-30; s_5..s_12: 2–4e-34 (zeros' 34 digits).
- λ_n: |diff| = 3.95e-14·n² exactly for n = 1..1000 (tail-model residual ∝ n²; λ_1000 agrees to 4e-8).
- S-fraction α_n by Lanczos with full reorthogonalization on ±1/γ + discretized tail: rel diff 5e-13..2.7e-11 for
  n = 1..400 (real side) and the same for the SHIFTED problem (circle side via Proposition S).
- Two lessons recorded: (i) the plain discretized Stieltjes procedure is UNSTABLE for these compact Jacobi operators
  (O(1) errors by n = 50) — Lanczos+reorth is needed; (ii) the tail is not optional: without it the sin toy's α_n
  are off by 1.4e-3 at n = 100 and 7e-3 at n = 400 with 30 000 zeros (sensitivity ~ n/N), with it 4e-8.
- Bugs caught and fixed in-run (logged): zeros parsed at 15 digits (mp.dps set late); a missing Jacobian e^v in the
  shifted tail weight (gave 1e-3 errors); 53-bit constants in the function-field script.

**U5a controls (verify/run_controls.sh → run_controls.out; u5_function_field.py → .log/.json):**
- Curves over F_q (exact, RH-true): y² = x³+x+1/F₅ (c1 = −3), y² = x⁵+x+1/F₅ (L = (1+5T²)², supersingular square),
  y² = x⁵+2x+3/F₇ (c1 = −1, c2 = 7): α_1..α_299 ALL certified positive. The w-side S-fraction does NOT terminate
  (periodic zeros); WKB with constant density: 4n√α_n → 2·(distinct-zero density)·π = 2g log q: observed 3.06–3.41
  (pred 3.22), 3.21888 (pred 2 log 5 = 3.21888, double zeros count once: multiplicity only rescales weights),
  7.61–8.18 (pred 7.78). "Fake curves" with Hasse broken (c1 = 5, 6, 9 over F₅): α_1 < 0 (index 1).
- L(s, χ₄) (RH-true): α_1..α_599 certified positive (16 000 bits). ✓
- F_{2,2} = ζ(s)(1 + 2·2^{−s} + 2^{1−2s}) (Hasse-bounded local factor, |a| < 2√2, RH-true): α_1..α_599 certified
  positive. ✓
- F_{a,q} RH-false (a > 2√q): (3,2), (2.9,2): first negative α at S-index 3 (J-index 2); (4.5,5): S-index 4 (J 2).
- Euler factor removed, symmetrized, ξ(s)(1 − p^{−s})(1 − p^{s−1}) (= F_{−(p+1),p}): p = 2, 3, 7: α_1 < 0 (index 1);
  p = 10⁹+7: α_2 < 0 (J-index 1). Positivity dies at the first index — see task (d).
- Running: DH real side (16 000 bits, M = 600).

## 2026-09-30 20:20 — Unit 5b: Davenport–Heilbronn — the fingerprint is a MAP of the off-line zeros (u2_prod dh real; u5b_dh_offline.py/.json)

- DH real side (16 000 bits, M = 600, tables/dh_real_P16000_S600.json): α_1..α_147 certified positive; first negative
  α_148 (J-index 74: b_74² < 0). Negative S-indices up to 599: {148, 150, 217, 219, 351, 353, 372, 374, 539, 541} —
  five isolated "−+−" motifs (α_m < 0, α_{m+1} ≫ 0, α_{m+2} < 0), everything else certified positive.
- Newton on f_DH (dh.py, 30 digits, |f| ≤ 8e-30) from literature seeds gives the five off-line zeros with t ≤ 241:
  0.808517182456637 + 85.699348485377592i, 0.650830080609737 + 114.163342730757i, 0.574356050450806 + 166.479305913168i,
  0.724257694626810 + 176.702461242856i, 0.869530579640643 + 240.404672351441i.  (The recalled seed
  0.646008 + 240.935500i did NOT reproduce — Newton from it converged to the last root listed; recorded as a recall error.)
- ONE-TO-ONE: motif k sits right after the WKB turning point t_n = 1/(2√α_n) passes the height of off-line zero k:
  motif 148 ↔ 85.70 (t_142..147 = 84.3, 87.8, 88.8, 90.4, 94.6, 109); 217 ↔ 114.16 (t ≈ 117–125); 351 ↔ 166.48
  (t ≈ 169–181); 372 ↔ 176.70 (t ≈ 181–185); 539 ↔ 240.40 (t ≈ 238–256). Lag ≤ ~6 indices.
- **Visibility law (IV.9), first form:** an off-line quadruple at height T (displacement δ = 0.07..0.37 here) is
  flagged at S-index n_fail ≈ the first n with t_n ≥ T, i.e. n_fail ≈ π N(T) + O(T) (π coefficients per zero), at a
  precision cost of ≈ 6 digits per index. For DH's first zero: n = 148 at ~900 digits lost. Li's criterion needs
  n ~ T²/δ (≈ 3×10⁵ for this zero; Voros's exponential-asymptotic analysis) — the Jacobi fingerprint sees the same
  zero ~2000 times earlier in index. Injection study (δ → 0 dependence) next.

## 2026-09-30 18:52 (clock read) — Unit 5c: counting theorem, conductor law, Theorem D identities; TIMESTAMP CORRECTION

- **Timestamp correction:** the blocks headed 19:15, 19:45 and 20:20 were ESTIMATED, not read from the clock; they
  were written between ≈ 18:15 and 18:45. From this block on, times are read with `date`.
- **Hermite–Krein count (NOTE §5; proof: Cauchy interlacing + Runge):** with J off-line quadruples resolved, the Hankel
  form (c_{i+j}) has exactly J negative squares; each sign flip of D_n = det(c_{i+j}) produces TWO consecutive negative
  b_k² and (when the shifted family det(c_{i+j+1}) flips at the same k) a "−+−" S-motif. Data: DH negative J-indices
  {74,75, 109,110, 176,177, 186,187, 270,271} = 5 pairs ↔ 5 off-line zeros ↔ 5 S-motifs; F_{3,2}: J pairs (2,3),
  (5,6), (13,14), (20,21), … one per lattice zero of 1 + 3·2^{−s} + 2^{1−2s}. The fingerprint is an off-line-zero
  COUNTER, not only a positivity test.
- **Conductor/density form of the law:** α_n ≈ W(q n/2π)²/(16 n²) with q the analytic conductor (zero density
  (1/2π) log(q t/2π)): χ₄ (q = 4) ratio A_n/W = 0.97–1.035 on n = 50..590; DH (q = 5, off the motifs) 0.95–1.02;
  F_{2,2} (extra lattice density log 2/π ⇒ q_eff = 4) 0.998 at n = 590. The leading law sees only the density.
- **Theorem D identities (verify/u6_theoremD_checks.py):** s_m(ξ·g_p) − s_m(ξ) = Σ_{k∈Z} (2πk/log p + i/2)^{−2m}
  to 1e-37..1e-43 for p = 2, 3, 7, 10⁹+7, m = 1..6; c_0(ξ g_p) = s_1(ξ) − (log p)²/(4 sinh²(log p/4)):
  −3.937097 (p = 2), −3.877815 (3), −3.675740 (7), +0.009524 (10⁹+7). The k = 0 node sits at y = −4 (zeros of g_p
  at s = 0, 1) with mass −4 and dominates every moment: s_m − s_m(ξ) ≈ (−4)^m.

## 2026-09-30 18:57 — Unit 5d/8: PSLQ (null), circle controls, first injections; NOTE.md drafted

- **PSLQ (verify/u8_pslq.py):** sanity recovers s_1 = −4 + (π²+8G)/8 + (ζ″/ζ − (ζ′/ζ)²)(1/2)/2. Final battery at 300
  digits (inputs recomputed at 1300 bits), coefficients ≤ 10⁸, basis {1, π, π², log π, log 2, γ, G, ζ(3), ζ″/ζ(1/2),
  (ζ′/ζ(1/2))²}: NO relation for α_1..α_6, b_1², b_2², Verblunsky α_0, 1 − α_0. Method lessons logged: ζ′/ζ(1/2) is
  basis-dependent (ξ′(1/2) = 0); 60-digit runs give spurious height-10⁵ relations.
- **Circle controls:** χ₄: λ_1..λ_601 certified positive, all |α_n| < 1 (n < 600) ✓. Euler-removed ξ·g_p: the Li
  expansion point s = 1 IS a zero of g_p (Carathéodory function has a pole at z = 0: failure at index 0). F_{3,2}:
  |α_n| ≥ 1 first at n = 2 (then 4, 9, 11, 24, …). DH at 24 000 bits returned non-finite λ_n (n ≥ 2) — rerun queued at
  16 000 bits (run_queue2.sh). F_{3,2} Li: λ_1..λ_151 positive (Li blind at these indices).
- **Injections (verify/u5_inject.py; ζ + one off-line quadruple (T ± iδ)):** first negative α at S-index
  T = 30: 20 (δ = 0.3), 29 (0.03), 32 (0.003); T = 60: 64, 69, 72 — failure index grows only ~logarithmically as δ → 0
  (precision, not index, pays for small δ). Every failure is a "−+−" motif. The "deviation from plain ζ" profile is
  not diagnostic (an injected pair ADDS mass; α_1 moves by > 1e-3); announcement study vs the on-line DOUBLE zero
  queued (u5c_announce.py).
- NOTE.md drafted (§0 verdict K for task (d) via Theorem D; §1 errata E-1..E-7; §2 Prop. S; §4 law; §5 counting;
  §6 Theorem D; §8 PSLQ); pending: injection table, DH circle, primes, next step.

## 2026-09-30 19:04 — Unit 5e: visibility table (verify/u5d_inject_table.py/.json; run_inject_1..3.out)

ζ + one off-line quadruple {±T ± iδ}, first certified negative α (S-index; always a "−+−" motif) vs n_WKB(T) (first n
with t_n(ζ) ≥ T) and πN(T):
T=30: δ 0.3/0.03/0.003 → 20/29/32 (n_WKB 13, πN 11.2); T=60 → 64/69/72 (50; 40.4);
T=100: δ 0.3/0.1/0.03/0.01/0.003/0.001 → 121/125/128/130/133/135 (105; 91.1);
T=200: 0.3/0.03/0.003 → 293/307/314 (275; 248.8); T=300: 0.3/0.03 → 483/519 (455; 432.6).
Lag n_fail − n_WKB: 7..28 at δ = 0.3; + ≈5 (T=100) to ≈36 (T=300) indices per decade of 1/δ: logarithmic in δ.
Precision consumed ≈ 6 digits/index (7224 → 5794 digits at n = 519). Shape law (u4c_shape.py): NO monotonicity or
convexity law — α_n increases at 441/998 steps, log-convexity fails 501×, log-concavity 496×; A_n = 4n√α_n decreases at
458/998 steps: only the smooth WKB envelope is regular.
Queued/running: DH circle at 16 000 bits (the 24 000-bit run gave non-finite λ_n for n ≥ 2 — not diagnosed; the 8 000-bit
probe at length 1003 is clean), then u4b_primes.py, then u5c_announce.py.

## 2026-09-30 19:07 — Unit 5f: DH circle side; division by an Euler factor; primes run 1 (broken, rerun queued)

- **DH circle (16 000 bits, N = 600; tables/dh_circle_P16000_S600.json):** λ_1..λ_601 ALL certified positive (Li blind),
  while |α_n| > 1 exactly at {147,149, 216,218, 350,352, 371,373, 538,540} = real-side motifs shifted by one
  (Proposition S, confirmed on an RH-false function).
- **Dividing by the symmetrized Euler factor** (one Euler factor ADDED; u2_prod.py FUNC dvl:p): s_2 < 0 < s_1 ⇒ α_1 < 0
  for p = 2, 3, 10⁹+7. Both directions of task (d) fail at index 1.
- **Primes run 1 (u4b_primes_run1_broken.log):** INVALID — the Gauss–Laguerre tail reached t ≈ T·e^230, the Lanczos vectors
  underflowed (overflow/divide warnings), truncation check vs Arb off by 0.24 at n ≤ 600. Kept only as a record. What
  it did show independently of the Lanczos: the periodogram of the zero displacements d_k = γ_k − t_k (t_k: N0(t_k) =
  k − 1/2) has its top lines at 0.693, 1.098, 1.610, 1.946, 1.387, 2.398, 2.566, 2.197 = log 2, 3, 5, 7, 4, 11, 13, 9.
  Rerun with a Gauss–Legendre tail on v ∈ [0, 40] and K = 8000 queued (run_queue4.sh).

## 2026-09-30 19:09 — Unit 5g: how the failure announces itself (verify/u5c_announce.py → run_queue3.out, u5c_announce.json)

ζ + off-line quadruple (T ± iδ) compared with ζ + the on-line DOUBLE zero at T (the configuration it collapses to), and
with ζ + the on-line split pair T ± δ. T = 85.6993 (DH's height), δ = 0.30852: first negative α at n = 100 (DH itself:
148 — higher zero density). |α(off)/α(double) − 1| vs |α(split)/α(double) − 1|: n = 1: 3.238e-7 / 3.238e-7; n = 10:
3.546e-6 / 3.546e-6; n = 40: 1.104e-4 / 1.104e-4; n = 60: 1.449e-3 / 1.424e-3; n = 80: 6.96e-3 / 6.10e-3; n = 98:
0.205 / 0.062; n = 99: 0.79 / 0.15; n = 100: 12.2 / 0.25 (flip); n ≥ 120: equal again (4.7e-2 / 4.7e-2). T = 40,
δ = 0.1: flip at 38; equal to 3 digits at n ≤ 20; 7.6e-2 / 4.9e-2 at n = 36. **Reading:** below the resolution index
the fingerprint responds to an off-line pair exactly as to an on-line pair split by ±δ with the δ² response of opposite
sign (equal magnitudes to ≤ 1e-3 relative until ~20 indices before the flip); an O(1) distinction appears only ~3
indices before the flip. No early warning — the IV.9 "deceptive" regime, measured.

## 2026-09-30 19:10 — Unit 7: primes in the fingerprint (verify/u4b_primes.py; logs run1_broken, run2_n999, final)

Smooth-ζ model zeros t_k (N0(t_k) = k − 1/2), 8000 zeros + Gauss–Legendre tail on v ∈ [0, 40]; Lanczos+reorth accuracy on
ζ's own zeros vs Arb: 6.6e-8 (n ≤ 300), 4.4e-7 (n ≤ 600), 8.9e-2 beyond (float64 degradation) → analysis on n ≤ 600.
r_n = α_n(ζ)/α_n(model) − 1, rms 0.037. Periodogram vs t_n: 0.695 (log 2, 139× median), 1.106 (log 3, 64×), 1.403
(log 4, 19×), 1.634 (log 5, weak), log 7 2.5× (absent), plus 0.407 ≈ log(3/2) (≈ 18×) — a combination tone absent from
the displacement spectrum (which shows log 2, 3, 5, 7, 4, 11, 17, 9). Transfer: ≈ 1% of displacement line power for
ω ≤ 1.6, ≈ 10× lower at log 7: low-pass (window of a few zero spacings) + nonlinear mixing. No arithmetic beyond the
explicit formula.

## 2026-09-30 19:14 — CLOSE: NOTE.md final (33 kB). Verdict (K) for the seed's mechanism (task (d)).

- Z = Theorem D (NOTE §6, proved): multiplying/dividing by a symmetrized local factor g_{a,q} acts on every fingerprint as
  an infinite Uvarov transformation (add/subtract the factor's zero lattice); positivity preserved for every input when
  |a| ≤ 2√q, destroyed for every input when |a| > 2√q; ζ's Euler factors are a = −(p+1), (√p − 1)² > 0 on the wrong
  side; the coordinates diverge along the Euler product. Computed failures at index 1 for p = 2, 3, 7, 10⁹+7, both
  directions. Core is output-based: ξg_p, ξ/g_p are RH-false, so no transformation of any form can do the step.
- Survivors (instrument grade): certified tables (α_1..α_999 > 0; Verblunsky n ≤ 999); Proposition S (the two seed
  families are one object; checked to 1e-50); conjecture W (α_n ≈ W(qn/2π)²/16n²); Proposition M (Hermite–Krein count;
  DH map: 5 motifs ↔ 5 off-line zeros); visibility table; announcement study (no early warning); primes only via the
  explicit formula (low-pass + mixing); PSLQ null; no shape law.
- Next step (NOTE §11): use N3 as the certified off-line-pair counter for N1/N2 approximants; secondary: prove W.
- No processes left running. Nothing committed (charter).
