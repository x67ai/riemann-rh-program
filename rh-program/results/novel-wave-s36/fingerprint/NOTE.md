# N3 `fingerprint` — the Jacobi / Schur / Verblunsky parameters of ζ, mined for structure

Wave S36, seed N3. Agent: Opus 5.5 (default effort), 2026-09-30. Scripts, logs and JSON under `verify/`; tables under
`tables/`; running log `SHARED.md`. Every number below is (a) certified by Arb ball arithmetic, or (b) the agreement of
two independent computations, as stated at the line. `[recalled, unverified]` marks anything not re-derived or read.

## §0 Verdict

**Close: (K) KILLED — for the seed's mechanism (task (d)).** Multiplying ξ by one Euler factor acts on every
fingerprint (Hankel / S- and J-fraction / Verblunsky data) as an infinite *Uvarov* transformation — the addition of
the fixed point-mass lattice of the factor's zeros — and never as a Christoffel or Geronimus transformation. Theorem D
(§6, proved) classifies the local multipliers g_{a,q}(s) = a/√q + q^{s−1/2} + q^{1/2−s} (ζ(1 + aq^{−s} + q^{1−2s})
completed): positivity of the fingerprint is preserved for EVERY input when |a| ≤ 2√q (the Hasse–Ramanujan bound;
a ≠ −2√q, where g(1/2) = 0), and destroyed for EVERY input when |a| > 2√q. The symmetrized Euler factor of ζ at p is the case a = −(p+1), and
p + 1 − 2√p = (√p − 1)² > 0: Euler factors sit strictly on the destroying side, for every p. No prime-by-prime
positivity induction exists in these coordinates; in addition the coordinates themselves diverge along the Euler
product (§6(v)). Computed: removing (symmetrized) the factor at p = 2, 3, 7 makes α_1 < 0; at p = 10⁹+7, b_1² < 0.
Z (the proved statement): Theorem D.

What survives, as instruments and theorems (not as a route to RH):
1. **Certified tables.** For ζ: s_1..s_1000 (power sums Σ_{γ>0} γ^{−2m}), the S-fraction α_1..α_999 of
   Σ_{γ>0} 1/(γ² − w) — ALL certified positive (Arb, ≥ 1192 certified digits at n = 999) — hence det(s_{i+j+1})_{n×n} > 0
   for n ≤ 500; λ_1..λ_1001 (certified); Verblunsky α_0..α_999 (verified, ≥ 2500 digits at n = 800), all |α_n| < 1.
   Independent zeros route (30 001 Arb zeros + tail): s_m, λ_n, α_n agree to 1e-11..1e-34 (§3).
2. **Proposition S (proved; checked to 1e-50):** the seed's two families are ONE object: the Li/Verblunsky data are
   the Szegő–Geronimus transform of the S-fraction of the SHIFTED zero measure Σ|ρ|^{−2}δ_{|ρ|^{−2}} (expansion at
   s = 1 instead of s = 1/2).
3. **Asymptotic law (conjecture W, derived by WKB/Abel inversion from the zero density; §4):**
   α_n = W(qn/2π)²/(16 n²)·(1 + ε_n), W = Lambert W, q the analytic conductor; ε_n oscillates (|ε_n| ≲ 7% for
   n ≥ 50; 37% at n = 10) and does not drift: ζ (n ≤ 999), χ₄, DH, F_{2,2}, three curves over F_q. Circle side: 1 − |α_n| ≈ W(n/2π)²/(32 n²).
   Exact sum rule Σ_n α_n = s_1 (proved).
4. **Counting theorem (Proposition M, proved; §5):** the Hankel form has exactly as many negative squares as there are
   off-line zero pairs resolved; generically each shows as two consecutive negative b_n²; DH's fingerprint shows exactly five "−+−" motifs up to n = 599, one per off-line zero with
   t ≤ 241, each at the S-index where the WKB height t_n = 1/(2√α_n) first exceeds that zero's height.
5. **Visibility (zoo IV.9; §5):** the fingerprint flags an off-line zero at height T at S-index ≈ n_WKB(T) + lag
   (n_WKB ≈ πN(T) + O(T); lag 7–64, logarithmic in 1/δ; injections T = 30..300, δ = 0.3..0.001; DH: n = 148 for
   T = 85.7) at ≈ 6 digits per index; Li's λ_n need n ~ T²/δ (≈ 3×10⁵ for DH's zero) — and on F_{3,2} Li is still
   positive for n ≤ 151 while |α_2| > 1 on the circle.
6. **Primes (§7):** the prime side enters only through the zero fluctuations (explicit formula): the residual of α_n
   against a smooth-density model (rms 3.7%) shows lines at log 2, log 3, log 4, log 5 through a low-pass transfer
   (log 7 filtered out at t ≤ 360) plus a nonlinear combination tone at log(3/2). No arithmetic beyond the explicit
   formula; no closed form or integer relation (PSLQ, §8); no monotonicity or convexity law (§4).

Disguise audit (IV.1): the fingerprint positivity IS Weil positivity with multiplier 1, restricted to the flag
V_n = span{(s − 1/2)^{−(2j+1)} : j < n} (real side) or to Laguerre-type functions (circle side, Bombieri–Lagarias
for λ_n [recalled, unverified]); the α_n are the Cholesky pivots of the Weil Gram matrix on that flag. It is a
re-dress, not a generator (S4 fails). As a falsification channel it passes V.4: it fires on DH, F_{a,q} (a > 2√q),
Euler-removed ξ and fake curves; silent on ζ, χ₄, F_{2,2}, three curves over F_q.

## §1 Objects, equivalences, and what the seed got wrong

Ξ(t) = ξ(1/2 + it), E(w) := Ξ(√w) (genus 0 in w, E(0) = ξ(1/2) = 0.4971207781883141099…), zeros w_k = γ_k², one
per ± pair. s_m := Σ_k w_k^{−m}; F(w) := −E′/E = Σ_{m≥0} c_m w^m, c_m = s_{m+1}; F(w) = ∫ dν(y)/(1 − wy) with
ν := Σ_k w_k^{−1} δ_{1/w_k} (mass = location × multiplicity). log ξ(1/2 + x) = Σ c′_k x^k gives s_m = (−1)^{m+1} m c′_{2m}.

**(E1) Grommer–Hamburger.** All w_k real positive ⟺ H_n = (c_{i+j})_{i,j<n} ≻ 0 ∀n ⟺ the J-fraction
F = c_0/(1 − a_0w − b_1²w²/(1 − a_1w − …)) has all b_n² > 0 ⟺ the S-fraction F = c_0/(1 − α_1w/(1 − α_2w/…)) has
all α_n > 0. Proof of the non-trivial direction: if all H_n ≻ 0, Hamburger gives a positive τ with moments c_m,
compactly supported (|c_m| ≤ CR^m), so ∫dτ/(1 − wy) is analytic off a real set and equals F near 0; F's poles are
then real, and comparing residues at w = 1/y gives τ({y}) = m·y, forcing y > 0 (a negative real zero w < 0 would
need negative mass). Contraction: a_0 = α_1, a_n = α_{2n} + α_{2n+1}, b_n² = α_{2n−1}α_{2n}. The zero-diagonal
Jacobi matrix with off-diagonals √α_n has spectrum {±1/γ}: this is the "Hilbert–Pólya matrix in disguise".

**(E2) Circle.** z_ρ := 1 − 1/ρ maps Re s = 1/2 to |z| = 1. C(z) := 2ξ′/ξ(1/(1 − z)) (chain rule: (1 − z)²φ′/φ =
ξ′/ξ(s), φ(z) = ξ(1/(1−z))) has Re C > 0 on |z| < 1 ⟺ RH (Re 1/(s − ρ) = (σ − β)/|s − ρ|²). Under RH its Herglotz
measure is σ := Σ_ρ |ρ|^{−2} δ_{z_ρ} (|1 − z_ρ|² = |ρ|^{−2}; total mass Σ_ρ |ρ|^{−2} = 2λ_1), with trigonometric moments
m_n = λ_{n+1} − 2λ_n + λ_{n−1} (λ_0 = 0, λ_{−n} = λ_n; derived from Σ_{n≥1} m_n z^n = (1 − z)²Φ(z) − λ_1,
Φ = φ′/φ = Σ λ_{n+1} z^n). Unconditionally m_n = −Σ_ρ (1 − z_ρ)² z_ρ^{n−1}; an off-line pair gives |z| > 1 and
exponential growth, so RH ⟺ (m_{j−k}) ≻ 0 ∀n ⟺ |α_n| < 1 ∀n (Verblunsky = Schur parameters, Geronimus).

**ERRATA against the seed.**
- E-1: "Σ_γ 1/(γ² − x) = −(d/dx) log Ξ(√x)" holds for γ > 0 only (one per ± pair); over all γ it is twice that.
- E-2: the Hankel determinants must start at s_1: det(s_{i+j+1}) (Hamburger) and det(s_{i+j+2}) (Stieltjes); s_0 = ∞.
  Either family alone is equivalent to RH (E1), but their first failures differ; the S-fraction needs both.
- E-3: "Verblunsky data of the Lévy-type measure Σ_ρ δ_{1−1/ρ}" — that measure is infinite. The Carathéodory function
  2ξ′/ξ(1/(1 − z)) is the Herglotz transform of σ = Σ_ρ |ρ|^{−2}δ_{z_ρ} = |1 − z|²·(Σ_ρ δ_{z_ρ}).
- E-4: "RH ⟺ all |γ_n| ≤ 1" should be strict, |α_n| < 1 (|α_n| = 1 means finite support).
- E-5: "a curve of genus g over F_q has a terminating J-fraction" — false in the seed's variable. Its zeros in t are
  periodic ((±θ_j + 2πk)/log q), so ν has infinitely many atoms and the S-fraction does not terminate (computed:
  299 positive coefficients, §4). What terminates is the Frobenius-variable measure Σ_j δ_{2√q cos θ_j} (g atoms):
  there RH is a SUPPORT condition (atoms in [−2√q, 2√q]), and ζ over Q has no such variable.
- E-6: "(i) and (ii)" are not two independent parameter families: Proposition S.
- E-7: "no closed form is on the record": each α_n is a rational function of s_1..s_{n+1}, and each s_m is a
  polynomial in ζ^{(k)}(1/2)/ζ(1/2), ψ^{(k)}(1/4), log π (Taylor coefficients of log ξ); the sequence has closed forms
  in that trivial sense. No arithmetic recurrence was found (§8).

## §2 Proposition S (one object, two expansion points)

Let x = z + 1/z = 2cos θ. Under RH, 2 − x_ρ = |1 − z_ρ|² = |ρ|^{−2}, so the push-forward of σ is
μ = Σ_{γ>0} 2|ρ|^{−2} δ_{2−|ρ|^{−2}}, i.e. μ(2 − ·) = 2ν̃ with ν̃ := Σ_{γ>0} |ρ|^{−2} δ_{|ρ|^{−2}}, the zero measure of
Ẽ(w) := ξ(s), w = s(1 − s) = 1/4 + t² (the real-side construction expanded at s = 1). Szegő's mapping theorem (Simon,
OPUC Thm 13.1.7 [recalled; the relations are checked numerically here]) gives, with α_{−1} = −1:
  (1 − α_{2n−1})α_{2n} − (1 + α_{2n−1})α_{2n−2} = 2 − α̃_{2n} − α̃_{2n+1}  (n ≥ 1; n = 0: 2α_0 = 2 − α̃_1),
  (1 − α_{2n−1})(1 − α_{2n}²)(1 + α_{2n+1}) = α̃_{2n+1} α̃_{2n+2}  (n ≥ 0),
where α̃ is the S-fraction of ν̃. **Check (verify/u4_mine_circle.py):** Route A (Verblunsky from λ_n by Levinson) vs
Route B (log ξ(1 + u) composed with u = (√(1 − 4w) − 1)/2, then S-fraction, Arb): agreement 3.6e-53 (diagonal),
4.8e-50 (off-diagonal) for n = 1..149 — the limit of the 60-digit table strings. Consequences: |α_n| < 1 ∀n ⟺ α̃_n > 0
∀n; α̃_1 = 2(1 − α_0); ε_n := 1 − |α_n| ≈ α̃_{n+1}/2; the sign law α_n = (−1)^n|α_n| (verified n ≤ 999) says σ lives on
an arc around z = 1 (|θ| ≤ 2 arctan(1/(2γ_1)) = 0.0707). The circle side carries no information the shifted real side
lacks, and the conditioning of both is the same (≈ 6 digits per index, measured).

## §3 Tables and their verification

**Computation (verify/u2_prod.py, fp_core.py).** Arb power series: log ξ(1/2 + x) = log(1/2) + log(1/4 − x²) −
(s/2)log π + lgamma(s/2) + log(−ζ(s)) to x^{2000} at 24 000 bits (114 s); log ξ(1 + w) with the deflated ζ-series.
S-fraction by the Viskovatov recursion F_n = (1 − 1/F_{n−1})/(α_n w) in ball arithmetic (tight: certified digits =
actual − 10, measured against a 2P run, verify/u2b_conditioning.py). Verblunsky by Levinson (midpoint arithmetic,
24 000 and 30 000 bits) and by the Schur algorithm (independent): ball arithmetic is useless there (dependency blow-up:
0 certified digits by n = 30 from 900), so verified digits = min agreement of the three runs.
**Intrinsic conditioning:** 4.7–6.6 digits lost per index on both sides (sin toy: 2.5–3.1).

**ζ, real side (tables/zeta_real_P24000_S1000.json).** s_1 = 0.023104993115418970789, s_2 = 3.7172599285269686165e-5,
s_3 = 1.441739314009732797e-7, s_4 = 6.6303168025299086987e-10, s_5 = 3.2136641506166012161e-12.
α_1..α_10 = 0.0016088556745971410, 0.0022696444618758230, 0.0012309447733972452, 0.0010732871255926878,
0.00072505601164270264, 0.00067059821555096551, 0.00054658061766806790, 0.00056250296730744522,
0.00051079519107545476, 0.00048491414387629513. J-fraction: a_0..a_4 = 0.0016088556746, 0.0035005892353,
0.0017983431372, 0.0012171788332, 0.0010732981584; b_1²..b_5² = 3.65153037181e-6, 1.3211571776e-6, 4.86221267582e-7,
3.07453219311e-7, 2.47691812776e-7. All 999 α_n and 499 b_n² certified positive.
**ζ, circle side (tables/zeta_circle_P24000_S1000.json).** λ_1..λ_5 = 0.02309570896612103, 0.09234573522804667,
0.2076389205543248, 0.3687904794922416, 0.5755427144611775 (λ_1 = 1 + γ/2 − log(4π)/2 to 30 digits); λ_100 =
118.6037753767913, λ_1000 = 2326.053161686466. α_0..α_5 = 0.9991968067208526, −0.9988664119479066,
0.9993846794038305, −0.9994634913667254, 0.9996375132820949, −0.9996647738964953.

**Independent zeros route (verify/u3_zeros.py; u3_zeros_N30000.json).** 30 001 zeros from Arb (acb.zeta_zeros,
certified on the line); mpmath.zetazero (a different code) agrees to 2e-34..4e-31. Tail beyond T = 25755.53 (N(T) =
30 000 exactly, S(T) = −0.39795): ∫ f θ′/π − f(T)S(T), residual ~ |f(T)| log T/T. Results: s_1 1.7e-12 relative
(predicted ≤ 2.6e-11), s_2 3.2e-18, s_3 1.9e-24, s_4 1.2e-30, s_5..s_12 ≤ 4.5e-34 (the zeros' 34 digits);
|Δλ_n| = 3.95e-14·n² for n = 1..1000; α_n (Lanczos with full reorthogonalization on ±1/γ + discretized tail) 5e-13..
2.7e-11 for n ≤ 400, same on the shifted side. Two findings about method: the plain discretized Stieltjes procedure is
unstable for these compact Jacobi operators (O(1) errors by n = 50); and the tail is essential (without it the sin toy
is off by 1.4e-3 at n = 100 with 30 000 zeros: the coefficients are sensitive to the deep tail at level ~ n/N).

## §4 The asymptotic law (conjecture W)

**Derivation (WKB + Abel inversion).** For a zero-diagonal Jacobi matrix with slowly varying off-diagonals b_n → 0,
the semiclassical count is #{eigenvalues > λ} ≈ (1/π)Σ_n arccos(λ/2b_n)_+. Writing n(g) := #{n : 2b_n > g} this is the
Abel-type equation N(λ) = (1/π)∫_λ^∞ n(g) λ dg/(g√(g² − λ²)). With N(λ) = N_ζ(1/λ) ≈ (1/2πλ)log(q/(2πeλ)) (q = 1 for
ζ) the ansatz n(g) = (A/g)(log(1/g) + B) gives (A/πλ)(log(1/λ) + B − 1 + log 2), using ∫_1^∞ dx/(x²√(x²−1)) = 1 and
∫_1^∞ log x dx/(x²√(x²−1)) = ∫_0^{π/2} −cos φ log cos φ dφ = 1 − log 2. Hence A = 1/2, B = log(q/4π):
n(g) = (1/2g)log(q/(4πg)). Inverting at g = 2b_n: 2b_n = L_n/(2n) with L_n e^{L_n} = qn/2π, so
  **α_n = b_n² ≈ W(qn/2π)²/(16 n²),   t_n := 1/(2√α_n) ≈ 2n/W(qn/2π)** (the WKB turning-point height of site n).
Consistency: sin√w/√w (γ_k = πk, q-free density 1/π) gives α_n ≈ 1/(4n²) — exact α_n = 1/((2n+1)(2n+3)); Bessel
zeros give 1/(4(ν+n)(ν+n+1)) — same leading term [recalled, unverified for general ν; ν = 1/2 computed exactly here].
N(t_n) ≈ n/π: about π coefficients per zero; α_n for n ≤ 999 encode the zeros up to t ≈ 533 (≈ 293 zeros).
**Evidence (verify/u4_mine_real.py, u4_mine_circle.py, u5_function_field.py):** A_n := 4n√α_n vs W(n/2π):
n = 100: 2.0723 / 2.0496; 500: 3.2529 / 3.2104; 999: 3.7557 / 3.7477; residual mean +0.0076, std 0.042 on [500, 999],
oscillating, no drift. χ₄ (q = 4): ratios 0.970–1.035 (n = 50..590); DH (q = 5) 0.95–1.02 off the motifs; F_{2,2}
(extra lattice density log 2/π, q_eff = 4): 0.998 at n = 590. Curves over F_q (constant density g log q/π):
4n√α_n → 2g log q: 3.06–3.41 vs 3.22 (E/F₅), 7.61–8.18 vs 7.78 (genus 2/F₇); the supersingular y² = x⁵ + x + 1/F₅
(L = (1 + 5T²)², double zeros) gives 3.21888 = 2 log 5 — multiplicity only rescales masses and drops out.
Circle: ε_n/(W(n/2π)²/32n²) = 1.035, 0.972, 1.008, 1.003, 0.989 at n = 100, 400, 800, 998, 999.
**Sum rule (proved):** tr J² = 2Σα_n = Σ_{±γ} γ^{−2} ⇒ Σ_n α_n = s_1; partial sum n ≤ 999 plus WKB tail = 0.0230982 vs
s_1 = 0.0231050. **Status:** WKB eigenvalue asymptotics for Jacobi matrices are a theorem in the forward direction
under regularity hypotheses on b_n [recalled, unverified];
here it is used backward without an a priori regularity proof, so the law is a conjecture; its leading term carries no
arithmetic beyond the density (conductor) — the "new invariant" hoped for in the seed is the Riemann–von Mangoldt
density in Jacobi coordinates.

## §5 Counting, the DH map, and visibility

**Proposition M (Hermite–Krein count; proof here).** Let the zero set of E contain exactly J non-real pairs
{w*, w̄*} (and no negative real w), all others real positive. Then H_n = (c_{i+j})_{i,j<n} has at most J negative
eigenvalues for every n, and exactly J for n large. Proof: ∫P²dν = ∫P²dν_+ + Σ_pairs 2Re(w*^{−1}P(1/w*)²); each pair
term is a real quadratic form of rank ≤ 2 and signature ≤ (1, 1), so the negative index is ≤ J; by Runge (supp ν_+ ⊂
[0, y_1] has connected complement and 1/w* ∉ supp) polynomials exist that are small on supp ν_+ and realize each
pair's negative direction, so the index reaches J; by Cauchy interlacing the index is non-decreasing in n and moves
by at most one per step. Hence D_n = det H_n changes sign exactly J times (assuming no D_n = 0); a change between k and k+1 gives b_k² < 0
and b_{k+1}² < 0 (b_k² = D_{k+1}D_{k−1}/D_k²), so generically (non-adjacent flips) **#{n: b_n² < 0} = 2J**; when the
shifted family det(c_{i+j+1}) flips at the same k the S-fraction shows the motif α_{2k} < 0, α_{2k+1} > 0,
α_{2k+2} < 0 ("−+−"). This is the
entire-function form of Hermite's theorem (signature of the Newton-sum Hankel form counts real roots) [recalled] and
is Krein's count in the Hamburger setting [recalled, unverified attribution]; Grommer's criterion is J = 0.
**Toys (verify/u1_toys.py):** complex pair at depth r (r real atoms with larger |y|): first failure at J-index r+1 or
r+2, matching Heine's subset formula to 1e-40.
**DH (tables/dh_real_P16000_S600.json; verify/u5b_dh_offline.py).** α_1..α_147 certified positive; negative S-indices
up to 599: {148,150, 217,219, 351,353, 372,374, 539,541}; negative J-indices {74,75, 109,110, 176,177, 186,187,
270,271}. Newton on f_DH (|f| ≤ 8e-30) gives the off-line zeros with t ≤ 241: 0.808517182456637 + 85.699348485378i,
0.650830080609737 + 114.163342730757i, 0.574356050450806 + 166.479305913168i, 0.724257694626810 + 176.702461242856i,
0.869530579640643 + 240.404672351441i (one recalled seed, 0.646008 + 240.935500i, did not reproduce). Motif k sits
where t_n first exceeds the k-th height: t_142..t_147 = 84.3, 87.8, 88.8, 90.4, 94.6, 109 before motif 148 (85.70);
≈ 117–125 before 217 (114.16); 169–181 before 351 (166.48); 181–185 before 372 (176.70); 238–256 before 539
(240.40). The fingerprint is a spectral MAP of the off-line zeros, with lag ≤ 6 indices at these depths.
**Visibility pricing (verify/u5_inject.py, u5d_inject_table.py/.json).** ζ plus ONE injected off-line quadruple
{±T ± iδ} (E → E(1 − w/z)(1 − w/z̄), z = (T + iδ)², exact in the moments), 24 000 bits. n_fail = first certified
α_n < 0 (always a "−+−" motif); n_WKB(T) = first n with t_n(ζ) ≥ T:

| T | δ = 0.3 | 0.1 | 0.03 | 0.01 | 0.003 | 0.001 | n_WKB(T) | πN(T) |
|---|---|---|---|---|---|---|---|---|
| 30 | 20 | – | 29 | – | 32 | – | 13 | 11.2 |
| 60 | 64 | – | 69 | – | 72 | – | 50 | 40.4 |
| 100 | 121 | 125 | 128 | 130 | 133 | 135 | 105 | 91.1 |
| 200 | 293 | – | 307 | – | 314 | – | 275 | 248.8 |
| 300 | 483 | – | 519 | – | – | – | 455 | 432.6 |

Law: n_fail ≈ n_WKB(T) + lag, lag = 7..28 at δ = 0.3 and growing by ≈ 5 (T = 100) to ≈ 36 (T = 300) indices per decade
of 1/δ — logarithmic in δ: a displacement of 10⁻³ is flagged only 14 indices after one of 0.3 at T = 100. The index is
cheap; the price is precision (≈ 6 digits per index: 1430 digits consumed at n = 519).
**How a failure announces itself (verify/u5c_announce.py).** Compare ζ + {T ± iδ} with ζ + the on-line double zero at
T and with ζ + the on-line split pair T ± δ. At T = 85.6993, δ = 0.30852 (flip at n = 100):
|α(off)/α(double) − 1| vs |α(split)/α(double) − 1| = 3.2e-7 / 3.2e-7 (n = 1), 1.10e-4 / 1.10e-4 (40), 1.45e-3 / 1.42e-3
(60), 6.96e-3 / 6.10e-3 (80), 0.21 / 0.06 (98), 12.2 / 0.25 (100), equal again after (4.7e-2 at n = 120). Below its
resolution index an off-line pair is indistinguishable from an on-line pair split by ±δ (the δ² response enters with
the opposite sign, which neighboring real zeros can mimic); an O(1) signal appears ~3 indices before the flip. There is
no early warning: the IV.9 "deceptive" regime, measured. Li's criterion needs λ_n < 0, i.e. |z_ρ|^n ≳ (n/2)log n with
|z_ρ| − 1 ≈ δ/T²: n ~ (T²/δ) log(T²/δ) ≈ 3×10⁵ for DH's first zero. Computed (tables/dh_circle_P16000_S600.json):
DH's λ_1..λ_601 are ALL certified positive, while its Verblunsky coefficients have |α_n| > 1 exactly at
{147, 149, 216, 218, 350, 352, 371, 373, 538, 540} — the real-side motifs shifted by one, as Proposition S predicts.
Cost: fingerprint index ≈ πN(T) at ≈ 6 digits/index (≈ 19 N(T) digits); Li index T²/δ at ≈ 0.03 digits/index
(binomial cancellation). Both are far costlier than direct zero location (Odlyzko–Schönhage
[recalled]); neither is a practical detector beyond small T, but the fingerprint wins over Li by a factor ~T/(δ log T)
in index.

## §6 Task (d): Theorem D — Euler factors are Uvarov transformations on the wrong side of the Hasse bound

For q > 1, a ∈ R, ℓ = log q, set g_{a,q}(s) := a/√q + q^{s−1/2} + q^{1/2−s} = q^{s−1/2}(1 + aq^{−s} + q^{1−2s}), so
g_{a,q}(1/2 + it) = a/√q + 2cos(tℓ), g_{a,q}(s) = g_{a,q}(1 − s), and ζ(s)(1 + aq^{−s} + q^{1−2s}) completes to
ξ(s)g_{a,q}(s). The symmetrized Euler factor is (1 − p^{−s})(1 − p^{s−1}) = −p^{−1/2} g_{−(p+1),p}(s). Let 𝓛 be the real
entire functions Λ of order ≤ 1 with Λ(s) = Λ(1 − s), real on the line, Λ(1/2) ≠ 0.

**Theorem D.** For Λ ∈ 𝓛 and g = g_{a,q} with a ≠ −2√q:
(i) (Uvarov form) ν_{Λg} = ν_Λ + ν_g, ν_g := Σ_{k∈Z} w_k^{−1} δ_{1/w_k}, w_k = ((θ + 2πk)/ℓ)², cos θ = −a/(2√q);
    equivalently s_m(Λg) = s_m(Λ) + Σ_k w_k^{−m}. Division gives ν_{Λ/g} = ν_Λ − ν_g.
(ii) If |a| < 2√q (θ real), every node 1/w_k is real positive with positive mass: multiplication by g preserves the
    positivity of every fingerprint, for every Λ (an infinite Uvarov transformation with positive masses).
(iii) If |a| > 2√q, θ = iη or π + iη with η = arccosh(|a|/2√q) > 0: every node is non-real except, for a < −2√q, the
    node k = 0 at w_0 = −η²/ℓ² < 0, whose mass is negative. Λg has zeros off the line, so by (E1) its fingerprint fails
    at a finite index for EVERY Λ; the same holds for Λ/g (−ν_g is not positive). No Christoffel, Geronimus or Uvarov
    transformation with real nodes and positive masses coincides with it.
(iv) (Euler factors) a = −(p + 1): |a| − 2√p = (√p − 1)² > 0 for every p > 1, and η = ℓ/2, so the nodes are the
    zeros of the Euler factor at s = 0, 1 and s = 2πik/ℓ, 1 + 2πik/ℓ (t = ±i/2 + 2πk/ℓ). Multiplying or dividing ξ by
    one Euler factor never preserves positivity; the fingerprint has no prime-by-prime positivity induction.
(v) (No limit) For Z_X := Π_{p≤X} [(1 − p^{−s})(1 − p^{s−1})]^{−1}, s_1(Z_X) = Σ_{p≤X} ℓ_p²/(4 sinh²(ℓ_p/4)) → ∞
    (Σ_p (log p)² p^{−1/2} diverges): the fingerprint coordinates diverge along the Euler product.
Proof: (i) zeros of a product are the union of zeros; F = −E′/E is additive. The zeros of g: 2cos(tℓ) = −a/√q.
(ii)–(iii) read off θ. (iv) AM–GM. (v) Σ_{k∈Z} (k + iβ)^{−2} = −π²/sinh²(πβ) with β = ℓ/4π gives
Σ_k w_k^{−1} = −ℓ²/(4 sinh²(ℓ/4)) for the Euler case; a pole contributes the negative of a zero. ∎
**Checks (verify/u6_theoremD_checks.py; run_controls.out).** s_m(ξg_p) − s_m(ξ) equals the lattice sum to 1e-37..1e-43
(p = 2, 3, 7, 10⁹+7; m ≤ 6); c_0(ξg_p) = −3.937097, −3.877815, −3.675740, +0.009524. The node at y = −4 (w_0 = −1/4:
the Euler factor's zeros at s = 0, 1) dominates: s_m − s_m(ξ) ≈ (−4)^m. First failure: α_1 < 0 (p = 2, 3, 7);
b_1² < 0 (p = 10⁹+7). Division (one Euler factor ADDED, ξ/g̃_p; `dvl:p` in u2_prod.py): s_2 < 0 < s_1, so α_1 < 0 for
p = 2, 3, 10⁹+7. On the circle side the Euler-removed function vanishes at the Li point s = 1 itself (g_p(1) = 0), so
C(z) has a pole at z = 0: failure at index 0. Closed-form certificate: by Poisson, Σ_k (k + iβ)^{−6} = −(2π)⁶/120·Σ_{m≥1} m⁵e^{−2πmβ} < 0, so
c_2(ξg_p) = s_3(ξ) − (ℓ⁶/120)Li_{−5}(p^{−1/2}) < 0 for all p up to ≈ 10³⁰, a negative diagonal Hankel entry.
F_{a,q} with a > 2√q: first failure at S-index 3 ((3, 2), (2.9, 2)) and 4 ((4.5, 5)); F_{2,2} (|a| < 2√2): all 599
coefficients certified positive. "Fake curves" (Hasse broken, c1 = 5, 6, 9 over F₅): α_1 < 0.
**Rung 1 (curves over F_q), as analogy.** Multiplying an L-polynomial by an Euler factor (1 − T^d)^{±1} adds zeros or
poles on |T| = 1 (weight 0), never on |T| = q^{−1/2}; the positivity-preserving multipliers are exactly the weight-1
factors 1 − aT + qT² with |a| ≤ 2√q (isogeny factors of Jacobians; Hasse). In cohomological terms the Euler product is
the trace formula over H⁰ ⊕ H¹ ⊕ H² while fingerprint positivity is an H¹ statement: adding a point changes H⁰/H²-type
data and is invisible to H¹ positivity. For Q this is an analogy, not a theorem.

## §7 How the primes enter

The α_n are functions of the zero set only, so primes can enter only through the zeros' fluctuations (explicit
formula: S(t) ≈ −(1/π)Σ_p p^{−1/2} sin(t log p) + …). Test (verify/u4b_primes.py, .log; runs 1–2 logged as broken/partial):
a "smooth-ζ" model with zeros t_k at N0(t_k) = k − 1/2 (N0 = θ/π + 1; t_1 = 14.518, t_2 = 20.654, …), 8000 zeros +
Gauss–Legendre tail, α_n(model) by Lanczos with full reorthogonalization (accuracy checked on ζ's own zeros against the
Arb table: 6.6e-8 for n ≤ 300, 4.4e-7 for n ≤ 600; unusable beyond 600 in float64). Residual r_n = α_n(ζ)/α_n(model) − 1
(rms 0.037 on n ∈ [50, 600]), periodogram against the WKB height t_n, compared with the periodogram of the zero
displacements d_k = γ_k − t_k over the same t-range:
- displacements: lines at 0.693, 1.099, 1.609, 1.947, 1.386, 2.396, 2.834, 2.197 = log 2, 3, 5, 7, 4, 11, 17, 9 (the
  explicit formula, as expected);
- fingerprint residual: top peaks 0.695 (log 2; 139× the median power), 1.106 (log 3; 64×), 1.403 (log 4; 19×), 1.634
  (log 5; weak), log 7: 2.5× (not detected); and a peak at 0.407 ≈ log(3/2) = 0.405 (≈ 18× median) that is ABSENT from
  the displacement spectrum.
Reading: the fingerprint carries the explicit formula's prime lines through a low-pass transfer — line power ≈ 1% of the
displacement lines for ω ≤ 1.6, dropping ≈ 10× by ω = log 7 at these heights (t_n ≈ 60–360; α_n averages the zeros over a
window of a few spacings around t_n) — and, being a nonlinear functional of the zeros, it mixes them (log 3 − log 2).
No prime structure appears that is not already in the zeros; the fingerprint is not an arithmetic coordinate system.

## §8 Integer relations and closed forms

verify/u8_pslq.py (.log/.json). Sanity first: PSLQ recovers s_1 = −4 + (π² + 8G)/8 + (1/2)(ζ″/ζ − (ζ′/ζ)²)(1/2)
(relation [−8, −32, 1, 8, 4, −4] on [s_1, 1, π², G, ζ″/ζ, (ζ′/ζ)²]; G = Catalan, ψ′(1/4) = π² + 8G). A first basis
containing ζ′/ζ(1/2) returned the basis's own relation ζ′/ζ(1/2) = (π + 2 log π + 6 log 2 + 2γ)/4 (from ξ′(1/2) = 0),
and a first run at 60 digits returned spurious relations of height ~10⁵ (expected for 11 numbers at 60 digits); both
recorded as method lessons. Final run: inputs recomputed at 1300 bits (≥ 362 certified digits), PSLQ at 300 digits,
coefficients ≤ 10⁸, basis {1, π, π², log π, log 2, γ, G, ζ(3), ζ″/ζ(1/2), (ζ′/ζ(1/2))²}: **no relation** for
α_1..α_6, b_1², b_2², the Verblunsky α_0 or 1 − α_0. The only closed forms are the trivial ones of E-7 (each α_n is
a rational function of s_1..s_{n+1}; each s_m a polynomial in Taylor data of log ξ at 1/2).

## §9 Brief-time protocol

Scope: instrument + refutation channel (the positivity is RH, not a proof of it). I.1: DH and F_{a,q} satisfy the
functional equation and fail the test — the test consumes the zeros, not an axiom; the DH/Epstein filter is passed in
the V.4 sense (fires on RH-false inputs) but the fingerprint has no generator that DH could violate. IV.1:
equivalent-redress (§0). IV.9: priced (§5). S1: no Euler-product input is consumed (Theorem D shows the Euler product
cannot be fed in prime by prime). S2: yes — a single off-line pair is flagged (DH). S3: yes — Proposition M counts
off-line pairs; an on-line double zero only doubles a positive mass (curves: double zeros drop out entirely).
S4: fails (no generator). V.5: no conclusion here rests on absence of literature.

## §10 Prior art (arXiv export API, 2026-09-30; verify/u7_arxiv.py, verify/arxiv/*.xml) [novelty: single-check]

- R. Zhang, arXiv:1510.03420 ("On Power Sums of Positive Numbers"): "a necessary and sufficient condition for a
  genus 0 entire function f(z) has only positive zeros by applying Hausdorff moment problem and Mergelyan's theorem",
  applied to RH — the Grommer-type equivalence (E1) is on arXiv.
- A. Voros, arXiv:1403.4558, 1602.03292, 1703.02844, 2204.01036: superzeta functions ("symmetric functions of the
  zeros", our s_m), Keiper–Li large-order asymptotics and "a sharp exponential-asymptotic criterion for the Riemann
  Hypothesis"; the deformed sequences "also work on the Davenport–Heilbronn counterexamples … tests that selectively
  react to zeros off the critical line". The Li-side visibility is his; the Jacobi-side map (§5) is not in these
  abstracts.
- J. C. Lagarias, arXiv:math/0404394 (Li coefficients for automorphic L-functions; relation to Weil's quadratic
  functional; asymptotics). F. Johansson, arXiv:1309.2877 (Arb; "record computations of … Keiper-Li coefficients").
- M. Suzuki, arXiv:2206.03682 (screw function; "an analog of so-called Weil's positivity or Li's criterion").
- D. Romik, arXiv:1902.06330 (Hermite / Meixner–Pollaczek / continuous Hahn expansions of Ξ; coefficient asymptotics)
  — expansions of Ξ itself, not Jacobi data of its zero measure.
- F. Štampach, P. Šťovíček, arXiv:1403.8083: "a Jacobi (tridiagonal) matrix J_L whose eigenvalues coincide with
  reciprocal values of the zeros of the regular Coulomb wave function" — the exactly solvable analogues (Bessel,
  Coulomb) of our J.
- D. W. Farmer, arXiv:2008.07206 (criteria for when an RH equivalence is useful; Jensen polynomials not plausible).
- Searches with no hit: Verblunsky/Schur parameters + zeta; "Jacobi matrix" + "Riemann zeros"; Grommer + zeta;
  Christoffel/Uvarov/Geronimus transformations + zeta/Euler product; Laguerre–Pólya + Euler product.
  Not found on arXiv (journal papers, recalled): Grommer (1914), Bombieri–Lagarias (1999, J. Number Theory) and
  Lagarias (1999, positivity of ξ′/ξ) [recalled, unverified].

## §11 Next step

**Why the Euler-factor route cannot be repaired by changing the transformation.** Theorem D's core does not depend on
the form of the operation: ξ·g_p and ξ/g_p have zeros or poles off the line, so NO operation whatsoever that maps ξ's
data to theirs can preserve positivity. Any prime-by-prime induction therefore needs intermediate objects that are
RH-true at every finite stage and are NOT ζ with finitely many Euler factors changed. Theorem D(ii) identifies the
one-prime objects that qualify: a/√q + 2cos(t log q) with |a| ≤ 2√q — in the variable z = q^{−it} this is
a/√q + z + 1/z, a one-variable Lee–Yang polynomial exactly when |a| ≤ 2√q. ζ's own factor is
p^{−1/2}((√p + 1/√p) − z − 1/z), with zeros at |z| = p^{±1/2}: it misses the Lee–Yang class by the AM–GM gap
(√p − 1)². This is the precise single-prime obstruction for seed N1 (products of one-prime Lee–Yang factors cannot carry
ζ's local factors; the coupling between primes has to do it).

**Single most promising next step:** make N3 the wave's common, certified diagnostic instead of a route. Proposition M
counts off-line pairs exactly, flags a pair at height T by index ≈ n_WKB(T) + O(log 1/δ), and runs from Taylor data at
s = 1/2 alone (≈ 6 digits per index). Apply it to the RH-true approximation schemes of N1 (Lee–Yang approximants on the
Bohr torus) and N2 (staircase chains): for each approximant compute α_1..α_n in Arb, locate motifs, and measure
coefficientwise convergence to ζ's table (tables/zeta_real_P24000_S1000.json). A scheme whose members stay motif-free
while converging coefficientwise yields certified height-by-height statements; a member with a motif is a certified
counterexample to that scheme's conjecture, with its height read off from t_n. Probability that this yields RH: ≈ 0
from this seed alone; value: a precise, cheap, falsifiable instrument for the seeds that do carry a generator.
Secondary (mathematics, not RH): prove conjecture W and the low-pass transfer of §7 (a Tauberian/semiclassical theorem
for compact Jacobi operators with log-regularly-varying spectra).

## §12 Files

verify/: fp_core.py (algorithms), fp_moments.py, u1_toys.py/.log/.json, u2_prod.py (+ logs per run), u2b_conditioning.py,
u3a_zeros_chunk.py, u3_zeros.py/.log/.json, u4_mine_real.py, u4_mine_circle.py, u4b_primes.py, u5_function_field.py,
u5_inject.py, u5b_dh_offline.py, u6_theoremD_checks.py, u7_arxiv.py, run_controls*.sh/.out, arxiv/.
tables/: zeta_real_P24000_S1000.json, zeta_circle_P24000_S1000.json, zeta_shifted_real_P12000_S420.json,
zeta_zeros_arb.txt (30 001 zeros), chi4_*, dh_*, faq-*, eul-*.
