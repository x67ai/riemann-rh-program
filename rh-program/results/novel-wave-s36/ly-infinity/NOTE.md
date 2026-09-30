# N1 `ly-infinity` — Lee–Yang functions of the primes, and infinite-rank Fourier quasicrystals

Opus 5.5 (default effort), novel-approach wave, Session 36, 2026-09-30. Folder `results/novel-wave-s36/ly-infinity/`. Every computation cited is a script in `verify/` with its log beside it; every source is quoted from `sources/` (text extracted with `pdftotext -layout`). Nothing recalled carries load; recalled items are labeled.

## §0 Verdict — (K) KILLED

**The route "a sequence of Lee–Yang functions of finitely many primes converging locally uniformly to ξ, then Hurwitz" cannot yield RH, because of Theorem K (§2):** every non-constant restriction t ↦ P(p^{−it} : p ∈ S) of a Lee–Yang polynomial in finitely many prime variables (any finite set S, any multidegree, any coefficients, for example det(I − Z U) with any unitary coupling U among the prime channels; also with one extra arbitrary archimedean inner channel of degree one) has at least 3 zeros (at least 2 with the archimedean channel) in (−14.1, 14.1). Ξ(t) = ξ(½ + it) has no zero there (computed: argument principle over [−0.5, 1.5] × [−14.1, 14.1] gives −1.5·10⁻³⁰), and exactly two, at ±14.13472514, once |t| < 21. By Hurwitz, no zero-free multiples of such functions converge to Ξ on a neighborhood of [−14.2, 14.2]. The lemma underneath is prior art: Alon–Vinzant's counting theorem, which I re-derived and extended to inner channels. Its application to Ξ is mine `[novelty: single-check]`.

**What is killed, exactly.** The seed's positivity generator is multivariate stability in the prime (Bohr-lift) variables. That is exactly what dies. The bigger class of real-rooted Dirichlet polynomials escapes the theorem. By Alon–Cohen–Vinzant, those are Lee–Yang only along another positive basis of the frequency group, which may contain log(m/n) → 0. But in that class the Hurwitz route is *equivalent* to RH by Laguerre–Pólya approximation (Proposition 3), so it has no content.

**The mechanism of the kill is the archimedean place.**
- Prime channels are inner functions of the prime variables. They add zero density ⟨d, log p⟩/2π ≥ |d|·log 2/2π at every height, with error at most |d|.
- ξ's zero density is purely archimedean: (1/2π)·log(t/2π), which is below log 2/2π for t < 4π. The primes contribute only the bounded-on-average S(t).
- So a prime part of weight W can agree with ζ only above height ≈ 2π·e^W (Proposition 4). The seed's monomial P^{−it} is the archimedean phase linearized at height 2πP.

**Controls.**
- **RH-false.** Davenport–Heilbronn fails the construction's axiom: the prime lift of its S-part c·L_S(χ) + c̄·L_S(χ̄) is not stable once S ⊇ {2, 3, 7}. Its S-truncations carry an off-line zero that converges to DH's own, 0.808517 + 85.699348i (distance 0.193 at X = 7, 0.0081 at X = 10⁴). F_{a,q} fails at the local factor (Ramanujan at q).
- **RH-true.** Curves over F_q *are* rank-one Lee–Yang restrictions, exactly. ζ's S-parts are products of stable factors.
- So the construction passes zoo I.1 at the axiom level. But it is blind to ζ's own zeros, and Theorem K forbids the limit.

**The orchestrator's addendum (Hamburger's theorem as the acceptance test; §6).** It is sound and it genuinely reduces what must be *verified*: support in log N plus Riemann's functional equation, instead of the weights Λ(n). But it is not a positivity mechanism, and its hypotheses are sharp:
- Nakamura's f(s, χ) = 7^s·L(s, χ) + G(χ)·L(s, χ̄) (χ the cubic character mod 7) satisfies *exactly* Riemann's functional equation (residual 10⁻³⁰) and has 31 zeros off the line with 0 < t < 45. Its frequencies are log(n/7).
- DH and F_{a,q} are excluded only by their different functional equations (conductor 5 and conductor q²). That is uniqueness, not arithmetic.
- Every finite model fails the test at the archimedean factor.

It collapses to "Hilbert–Pólya plus a converse theorem", with the Γ-factor as the entire unsolved design problem.

**Frontier left open (not a mechanism, not a G).** Coupled multichannel systems det(I − V(s)U) with several archimedean inner channels. There the counting error |d| could, in principle, absorb the prime winding at low height. A numerical search (k ≤ 6 slow channels, two objectives) found no evasion; the optimum always decouples the prime channel (§4).

## §1 Re-derivation of the seed, and ERRATA

Notation: s = ½ + it, z_p := p^{1/2−s} (so z_p = p^{−it} on the line, |z_p| < 1 exactly when Re s > ½), c_p := p^{−1/2}, S a finite prime set, P = Πp, E_S(s) := Π_{p∈S}(1 − p^{−s}).

(1) **Re-derived, correct.** Q(z) := Π(1 − c_p z_p) restricts to E_S(s), and Q̃(z) := Π(z_p − c_p) restricts to P^{1/2−s}E_S(1−s). So
- f_± = E_S(s) ± P^{1/2−s}E_S(1−s) = E_S(s)(1 ± B(s)), where B = Π b_p and b_p(z) = (z − c_p)/(1 − c_p z).
- |z − c|² − |1 − cz|² = (|z|² − 1)(1 − c²), so |b_p| < 1, = 1, > 1 in, on, and outside the unit disc.
- Zeros of f_± therefore lie only on Re s = ½, and P_± = Q ± Q̃ has no zeros in D^S ∪ E^S. It is Lee–Yang in the sense of ACV p. 1 ("no zeros in Ωⁿ both for Ω = D and Ω = {z ∈ C : |z| > 1}").
- As Dirichlet polynomials, E_S(s) = Σ_{n|P} μ(n)n^{−s} and P^{1/2−s}E_S(1−s) = μ(P)P^{−1/2}Σ_{n|P} μ(n)n^{1−s}.

For det(I − Z(s)U), U unitary:
- For z ∈ Dⁿ, ‖ZU‖ < 1, so there are no zeros. For z ∈ Eⁿ, det(I − ZU) = det(Z)·det(−U)·det(I − U*Z⁻¹) ≠ 0. Lee–Yang for every U. This is Kurasov–Sarnak's "spectral pair", their eq. (5), p. 2.
- Expanding by principal minors gives Σ_{n|P} μ(n)·det(U_{S(n)})·√n·n^{−s}. The seed's formula is correct.
- Jacobi's identity for unitary U gives det U_{T^c} = det U·conj(det U_T). Hence P^{1/2−s}·F*(1−s) = (−1)^{|S|}·conj(det U)·F(s). The functional equation is correct (conductor P, no Γ-factor).

**E1 (the lift adds nothing for product type).** For f_± the multivariate stability is just "a product of one-variable Hermite–Biehler factors is Hermite–Biehler". The multivariate structure has content only for non-product P (for example det(I − ZU) with non-diagonal U).

**E2 (sign; computed).**
- The seed's A = Π(1 − p^{−1/2−it}) is the partial product of 1/ζ. Its phase enters the zero condition with the *opposite* sign to ζ's:
  - zeros of f_+ satisfy t·log P − 2πS_X(t) ≡ π (mod 2π) + O(Σ p^{−1});
  - ζ's smooth model is 2ϑ(t) + 2πS_X(t) ≡ π;
  - here S_X(t) := −(1/π)Σ_{p≤X} p^{−1/2}·sin(t log p).
- Measured at the height where densities match (`b_alignment.log`): mean distance from each ζ zero to the nearest model zero, in units of the mean spacing, at T* = 1319.47 / 14514.16 / 188684.05 (39 / 187 / 493 zeros):

| model | T* = 1319.47 | T* = 14514.16 | T* = 188684.05 |
|---|---|---|---|
| prime-free baseline (mid-Gram points) | 0.237 | 0.211 | 0.230 |
| seed's Lee–Yang function | 0.361 | 0.282 | 0.272 |
| aligned Lee–Yang, Π(1 + p^{−s}) | 0.144 | 0.168 | 0.183 |

- The seed's function is worse than using no primes at all.
- The correct Lee–Yang choice puts the Blaschke zero at −c_p, i.e. Π(1 + p^{−s}). That is right at first order but wrong at even repetitions. This is the "Maslov sign" problem that Kuipers–Hummel–Richter (arXiv:1307.6055, p. 2) solve with infinite families of graphs.
- Inside the Lee–Yang class, the truncated geometric factor Σ_{k≤K}(c_p z_p)^k is stable (zeros on |z| = √p) and correct to repetition K. The price is density K·log P/2π.

**E3 (step 2, "the product form is exactly where the Euler product enters"): half right.**
- The construction needs every S-part's lift to be a product of one-variable stable factors: Euler product plus Ramanujan (|Satake| = 1). DH and F_{a,q} violate this (§5).
- But the property is blind to the *values* log p (any positive frequencies work, so it holds for Beurling primes) and blind to ζ's zeros (ζ's S-parts never vanish).

**E4 (step 3).** The change of variables is legitimate: for finite S it meets zoo III.15's test (positivity in the fugacities z_p, zeros on a torus line). But the torus line carries the wrong density law: constant ⟨d, ℓ⟩/2π instead of (1/2π)·log(t/2π) (Alon–Vinzant Theorem 1.9(1)). For locally uniform approximation the variable mismatch reappears as a density mismatch.

**E5 (step 4).**
- (a) Kurasov–Sarnak, p. 1, verbatim: Guinand's "example 4 page 264 coming from the explicit formula in the theory of primes does not give a Fourier quasicrystal, even assuming the Riemann hypothesis". The archimedean term of the explicit formula is absolutely continuous, and the prime atoms Λ(n)n^{−1/2} have exponentially growing mass, compensated only by the pole terms. So "the zeros of ζ (if on the line) form a Fourier quasicrystal" is false as stated.
- (b) Replacing P^{−it} by e^{−2iϑ(t)} leaves the Lee–Yang class, since the archimedean phase is not a torus character. That variant *is* Gonek's ζ_X (arXiv:0704.3448, p. 16): ζ_X(s) = P_X(s) + χ(s)·\overline{P_X(s)} is **non-analytic**. Its "Riemann Hypothesis" (Theorem 6.2, p. 18) holds by construction, and Hurwitz cannot act on it. The analytic version A(s) + χ(s)A(1−s) has off-line zeros once X passes a height-dependent threshold (§3). Gonek himself (p. 16) calls the analytic version (35) "not a good guess".
- (c) "The Lee–Yang class is closed under locally uniform limits" is true for real-rootedness. But limits of prime-variable Lee–Yang restrictions keep a zero in every interval longer than 2π/log 2, and Ξ does not (Theorem K).

**E6.** "A sequence of Lee–Yang functions of finitely many primes converging to ξ would prove RH" is true but empty in the prime-variable class (Theorem K) and tautological in the ACV class (Proposition 3).

**E7 (the named obstruction is not the operative one).** "The divergence of Σ p^{−1} on the critical line" is not what blocks the limit.
- The zero density of any Lee–Yang restriction is ⟨d, log p⟩/2π, and it is **independent of the coefficients**.
- So no renormalization of the weights c_p can change it: smooth cutoffs w(log p/log X), σ ↓ ½, higher-degree Blaschke factors (which raise d) or non-diagonal U all fail. That covers the whole search space of task (b).

## §2 Theorems (statements, proofs, scope)

**Theorem 1 (counting along inner channels).**
- *Setting.* Let P ∈ C[v_1..v_m] be Lee–Yang of multidegree d (d_j = deg_{v_j} P, |d| = Σd_j). Let v_j(s) be meromorphic inner functions of Re s > ½: |v_j| < 1 there, unimodular on the line, extended by v_j(1 − s̄) = 1/conj v_j(s). Put F(s) = P(v(s)).
- *Claim.* F has no zeros off Re s = ½ (away from poles). For t_1 < t_2, neither a zero of F:
  |N_F(t_1, t_2) − (1/2π)·Σ_j d_j·|Δ_{[t_1,t_2]} arg v_j(½ + it)|| < |d|.
- *Kronecker-line case.* For v_j = p_j^{1/2−s} this is Alon–Vinzant (arXiv:2307.13498, Theorem 1.9, p. 5): "µ_{p,ℓ}([x, x+T]) = ⟨d,ℓ⟩T/2π + err(x,T) … |err(x,T)| ≤ |d|", and "the gap between any pair of consecutive atoms … is at most 2π|d|/⟨d,ℓ⟩", tight (Remark 1.10).

*Proof (re-derived).*
1. P has no zeros on Dᵐ, so it has a continuous log L there with P(0) ≠ 0.
2. Go from 0 to v one coordinate at a time. Each step is a one-variable polynomial in v_j (the others fixed in D), of degree ≤ d_j, with all roots ω satisfying |ω| ≥ 1. Since Re(1 − v_j/ω) > 0, each step changes Im L by less than d_jπ/2. Hence |Im L(v) − Im L(0)| < |d|π/2 on Dᵐ.
3. On Eᵐ write P(v) = v^d·P†(1/v), with P† := v^d·P(1/v). P† has no zeros on Dᵐ (ACV p. 1: "p is a Lee–Yang polynomial if both p and p† … are Schur stable"). So arg P = Σ d_j·arg v_j + (a term within |d|π/2 of a constant).
4. Apply the argument principle to the thin rectangle [½ − ε, ½ + ε] × [t_1, t_2], traversed counterclockwise, and let ε → 0 (the channels' poles lie strictly left of the line, so small ε avoids them).
   - The right edge (v ∈ Dᵐ) contributes a change in (−|d|π, |d|π).
   - Every arg v_j(½ + it) decreases in t (for example arg p^{−it} = −t·log p). So the left edge (v ∈ Eᵐ), traversed downward, contributes +Σ d_j·|Δ arg v_j| up to (−|d|π, |d|π).
   - The horizontal edges contribute o(1).
   Divide by 2π. ∎

**Corollary 2 (gaps in prime variables).** If v_j = p_j^{1/2−s} (primes, repetition allowed), then ⟨d, log p⟩ ≥ |d|·log 2. So every open interval of length L has
  N > |d|·(L·log 2/2π − 1).
- Every non-constant restriction has a zero in every interval of length > 2π/log 2 = 9.06472.
- In (−14.1, 14.1) (L = 28.2) it has N > 2.1110·|d|, i.e. at least 3 zeros.
- Computed (`k1_gap_theorem.log`): for 33 Haar-random det(I − Z(t)U) with 1–8 prime slots, the worst |N − W·L/2π| is 3.13 < |d| in every case, and every maximal gap is within the bound. One prime attains 9.0647 exactly.

**Theorem K (no Hurwitz route through prime-variable Lee–Yang functions).**
- *Setting.* U := {|Re t| < 14.2, |Im t| < ½}. f_k(t) := P_k(v(½ + it)), where P_k is Lee–Yang in the prime channels p^{1/2−s} (p ∈ S_k finite), optionally with one extra archimedean channel Θ_k(s) of degree ≤ 1 (any meromorphic inner function). h_k is holomorphic and zero-free on U.
- *Claim.* h_k·f_k does not converge uniformly on compact subsets of U to Ξ.

*Proof.*
1. Ξ's zeros in U are exactly the two simple zeros ±14.13472514 (`k1_xi_lowzeros.log`: nzeros(14.2) = 1; argument principle on the central box = 0).
2. By Hurwitz, on a compact subdomain containing ±14.1347, h_k·f_k has exactly two zeros for large k.
3. The zeros of f_k are real (Theorem 1). By Theorem 1 with L = 28.2:
   - without the archimedean channel, N > 2.111·|d_fin| ≥ 2.1, so N ≥ 3;
   - with it, N > 2.111·|d_fin| − 1 ≥ 1.1, so N ≥ 2, all inside (−14.1, 14.1), where Ξ has none.
4. If d_fin = 0 the primes are absent, and the archimedean-only case is not the seed's route. ∎

The same argument shows: any locally uniform limit (with zero-free multipliers) of non-constant prime-variable Lee–Yang restrictions has a zero in every interval of length > 2π/log 2. Lean-ready shape: `¬ ∃ f h, (∀ k, IsPrimeLYRestriction (f k)) ∧ (∀ k, ∀ z ∈ U, h k z ≠ 0) ∧ TendstoLocallyUniformlyOn (fun k z ↦ h k z * f k z) Xi atTop U`. The only numerical input is the two facts about Ξ in U.

**Proposition 3 (the dichotomy: the ACV class is tautological).** Under RH, Ξ is a locally uniform limit of zero-free multiples of real-rooted Dirichlet polynomials. Conversely (Hurwitz), such a limit is real-rooted.

*Proof.*
1. Under RH, Ξ(t) = Ξ(0)·Π_{γ>0}(1 − t²/γ²), convergent since Σγ⁻² < ∞. Truncate the product.
2. Replace each factor (γ − t) by sin(ε(γ − t))/ε with 2ε = log(m/n) → 0.
3. Then e^{−iεt}·n^{−it}·sin(ε(γ − t)) = c_1·m^{−it} + c_2·n^{−it}, a real-rooted two-term Dirichlet polynomial.
4. Products preserve both properties. ∎

The lifts m^{−it} − c·n^{−it} are not Lee–Yang in the prime variables: for 3 and 2, z_3 − c·z_2 vanishes at (½, c/2) ∈ D². That is why this class escapes Theorem K, and also why it carries no mechanism.

**Proposition 4 (prime channels add density; receding threshold).** Suppose F is as in Theorem K (one scalar archimedean channel) and its zeros coincide with ζ's on an interval I at height t. Then
  N_ζ(I) ≥ W|I|/2π − |d_fin| − 1,  with W = ⟨d_fin, log p⟩,
while N_ζ(I) = (1/π)·Δ_Iϑ + O(log t). So agreement on windows with |I| ≫ |d_fin| + log t requires log(t/2π) ≳ W, i.e. t ≳ 2π·e^W. Prime channels of total weight W can only "switch on" above height 2π·e^W; as W → ∞ the admissible region recedes.

**Lemma F (frozen channels; used in §4).** Let P(v_0, v_1..v_k) be Lee–Yang of degree 1 in v_0, and c ∈ T^k with deg_{v_0} P(·, c) = 1. Then the root ω of P(·, c) has |ω| = 1.

*Proof.* The root ω_r of P(·, rc) has |ω_r| ≥ 1 for r < 1 (no zeros in D^{k+1}) and ≤ 1 for r > 1 (no zeros in E^{k+1}). Let r → 1. ∎

So with frozen archimedean channels there is exactly one zero per revolution of a prime channel, for every coupling U.

## §3 Computations for task (b)

*Heights and density.* A Lee–Yang restriction on S has density log P/2π and matches ζ's density only at T* with 2ϑ′(T*) = log P, i.e. T* ≈ 2πP. At fixed T, adding primes drives its zero count to ∞ (Corollary 2; `b_alignment.py` records the linearization error H²/4T*, at most 0.10 rad).

*Alignment table (§1 E2)*, from the same runs. The archimedean variants use the exact phase: zeros of Re(e^{iϑ}A).

| model | X | T* = 1319 | T* = 14514 | T* = 188684 |
|---|---|---|---|---|
| exact Euler product | S | 0.084 | 0.113 | 0.135 |
| exact Euler product | 100 | 0.045 | 0.050 | 0.083 |
| exact Euler product | 1000 | 0.020 | 0.039 | 0.051 |
| exact Euler product | 10⁴ | — | 0.024 | 0.037 |
| Π(1 + p^{−s}) | 10⁴ | — | 0.060 (196 model zeros vs 187) | 0.086 |
| seed's A | 1000 | 0.40 (53 vs 39) | 0.36 (216 vs 187) | 0.36 (504 vs 493) |

- The exact Euler product converges to ζ's zeros, as Gonek proves under RH (Theorem 9.1, p. 32), but it is not real-rooted.

*Real-rootedness of the analytic archimedean models F = A(s) + χ(s)A(1−s)* (`b3_arch_realrootedness.log`; argument-principle count in |σ − ½| < 0.45 minus sign changes on the line):
- The Lee–Yang positive control gives exactly 0 off-line zeros.
- For entire A (the squarefree and seed products), in all 30 cases, off-line zeros appeared exactly when min_I φ′ < 0 (every case with min φ′ > 0, down to 0.036, had none), with φ := ϑ + arg A(½ + it). On the line F/(2e^{−iϑ}) = |A|·cos φ, and φ′ = ϑ′ − (prime sum, whose maximum is ≈ Σ_{p≤X} log p/√p ~ 2√X by Kronecker).

| height T | squarefree model clean at | first off-line zeros | at X = 1000 |
|---|---|---|---|
| 1319 (ϑ′ = 2.67) | X ≤ 13 (min φ′ 0.25) | X = 30: 6 zeros (min φ′ −1.28) | 294 |
| 14514 (ϑ′ = 3.87) | X ≤ 13 | X = 30: 2 zeros | 394 |
| 188680 (ϑ′ = 5.16) | X ≤ 30 (min φ′ 1.11) | X = 100: 32 zeros | 390 |

- The exact Euler product (poles on σ = 0, 1) already has off-line zeros at X = 7 (6 / 6 / 2), from zero–pole dipoles.
- The trade-off: real-rootedness at height T needs X ≲ X_max(T), which grows only like a power of log T (Gonek, Theorem 8.1, p. 27: X < exp(C₃·log t/Φ(t))). Tracking ζ's zeros to o(spacing) needs primes up to T^θ. The part of S(t) carried by primes in (X, T^θ] has variance ≈ (1/2π²)·log(log T/log X) `[recalled, unverified: Selberg]`, which stays unbounded.
- Visibility (zoo IV.9): this detector sees nothing of an off-line zero of ζ, since every model's zeros are generated, not detected.

## §4 Task (d): inverse design, and the coupling frontier

`d_inverse_design.py` (+ .log/.json). The model is F_U = det(I − Z(t)U) with prime slots p_j at T*. U is fitted by L-BFGS-B, 12 restarts, on the zeros of the first half-window and tested on the second. There are n² parameters, n² − (n−1) effective after the gauge U → DUD⁻¹. Results (mean distance/spacing, TEST half):

| prime slots (T*) | effective params | train/test zeros | fitted U: train → TEST | best of 200 random U: TEST | prime-free baseline: TEST | aligned product, no fit: TEST |
|---|---|---|---|---|---|---|
| 2,3,5,7 (1319.47) | 13 | 20/19 | 0.081 → **0.168** | 0.336 | 0.247 | **0.146** |
| 2,3,5,7,11 (14514.16) | 21 | 49/49 | 0.085 → **0.215** | 0.278 | 0.2195 | **0.191** |
| 2,2,3,5,7 (2638.94) | 21 | 30/32 | 0.086 → **0.191** | 0.269 | 0.228 | 0.251 |

A fourth configuration (2,…,13 at T* = 188684) was stopped to respect the 10-minute rule (noted in the log).

**Assessment.**
- In-sample the fit is 2.1–2.5× better than out-of-sample. Out-of-sample it is at best modestly better than the prime-free baseline, equal to it for 2,…,11, and worse than the parameter-free aligned product in 2 of 3 cases.
- So the fit is parameter counting plus the density match (the window is placed where W = 2ϑ′), not arithmetic.
- The fitted |U| is fully mixed (entries 0.07–0.74, no near-diagonal or permutation structure), and |diag U| shows no relation to p^{−1/2}.
- This is what one expects, heuristically: a Lee–Yang restriction is almost periodic, while ζ's zeros are not (their density drifts and S(t) has unbounded variance). No U of fixed finite rank should track them out of sample. This expectation is not proved; the table is the evidence.

**Coupling frontier** (`d2_gap_evasion_by_coupling.log`, `d2b_gap_evasion_eigenphase.log`). One prime channel 2^{−it} (19.5468 rad of winding on (−14.1, 14.1)) was coupled by U ∈ U(k+1) to k = 1..6 slowly winding archimedean Blaschke channels (a − ½ = 12, 25, 50, 100, 200, 400).
- The fewest zeros found was 3 for every k, with two different objectives. The optimum decouples the prime channel (objective 6.080·10⁻² for every k).
- Theorem 1 permits zero crossings once k ≥ 4, because the error term is |d| = k + 1. Lemma F shows that any evasion must come from the motion of the slow channels.
- Status: **open**.

## §5 Task (e): controls

- **Davenport–Heilbronn (`e_controls.log`).**
  - f_DH = c·L(s,χ) + c̄·L(s,χ̄), with χ(2) = i and c = (1 − iκ)/2 (checked against `results/ccm-dh-test/dh.py` to 6.4·10⁻¹¹ at 2 + 3i).
  - Primes ≡ ±1 (mod 5) give common factors. Primes ≡ ±2 give the lifted numerator N_S = c·Π(1 − χ̄(p)c_p z_p) + c̄·Π(1 − χ(p)c_p z_p).
  - N_S = 0 exactly when Π M_p(z_p) = −c̄/c = e^{−2.588i}, with M_p a Cayley factor of maximal argument 2·arctan(c_p) over the closed disc. Necessary condition for instability: Σ 2·arctan(p^{−1/2}) > 2.588.
  - The scan: stable for S_2 = {2, 3} (sum 2.278); **unstable for S_2 = {2, 3, 7}** (3.001; zero at polyradius ≈ 0.84).
  - The S-truncated DH series has zeros with σ > ½ already at X = 7 (0.633 + 85.780i). They converge to DH's off-line zero 0.8085172 + 85.6993485i: distance 0.193 (X = 7), 0.075 (30), 0.016 (1000), 0.0081 (10⁴).
  - Hypothesis violated: "the lift of every S-part is a product of one-variable stable factors" (the Euler product). This is the I.1 filter passed at the axiom level.
- **F_{a,q} = ζ(s)(1 + a·q^{−s} + q^{1−2s})** (re-derived: coefficients 1 + a[q|n] + q[q²|n], Euler product, functional equation with conductor q²).
  - The local factor in z = q^{1/2−s} is 1 + (a/√q)z + z², Lee–Yang exactly when a ≤ 2√q.
  - Examples: q = 5, a = 5 gives zeros at σ = 0.2010 and 0.7990; q = 2, a = 3 at σ = 0 and 1; q = 5, a = 4 on the line.
  - Hypothesis violated: Ramanujan at q.
- **RH-true.**
  - For E/F_5 with every a_5 ∈ [−4, 4], and for the genus-2 datum (3; 0, −2) of zoo III.15, the completed zeta is a rank-one Lee–Yang restriction exactly (roots of modulus 1 to 10⁻¹²). The non-curve (13, 8) is not.
  - L(s, χ₄) S-parts are products of stable factors, so the construction applies verbatim.
- **What this means.** The construction is Euler-product-sensitive, but the sensitivity sits where it can say nothing about ζ's zeros: ζ's S-parts never vanish, and the limit is forbidden by Theorem K.
- **Visibility (zoo IV.9).**
  - DH's off-line zero (depth 0.3085 at height 85.7) is visible to the S-part detector from X = 7 on: an off-line zero of D_S appears at 0.633 + 85.780i, displaced 0.19. It is localized to 0.01 from X ≈ 3000. The detector fired on the negative control.
  - The same detector has no visibility threshold for ζ at any height or X: every S-part of an Euler product with |Satake| = 1 is zero-free on Re s > 0. It stays silent on the positive controls (L(s, χ₄), ζ) by construction, not by measurement.
  - Theorem K's "detector" is the low-lying gap. It says nothing about off-line zeros; it is arithmetic-blind. It would equally forbid the route for any L-function whose completed function has a zero-free central interval longer than 2π/log 2.

## §6 Task (f), and the orchestrator's addendum (Hamburger)

**(f) Candidate object.** An *arithmetic Lee–Yang determinant* is
  D_{S,A,U}(s) = det(I − V(s)U),  V = diag(p^{1/2−s} (p ∈ S, with multiplicity), a_1(s), …, a_k(s)),
where U is unitary and the a_j are meromorphic inner functions of Re s > ½ (archimedean channels; for example the Blaschke factors of the Γ-function's product). An *infinite-rank Lee–Yang function* (ILY) is a locally uniform limit of zero-free multiples of such D; the infinite-dimensional U case needs Fredholm regularization.
- **Proposed statement:** "RH ⟺ Ξ is ILY with nontrivial prime channels."
- **Status:**
  - False for prime channels alone, and for prime channels plus one archimedean channel of degree ≤ 1 (Theorem K).
  - Tautological if the prime basis is abandoned (Proposition 3).
  - Open for several coupled slow archimedean channels (§4). That is the precise residual question.
- **Nearest published objects, and the exact difference:**
  - (i) Kurasov–Sarnak spectral pairs (arXiv:2004.05678, eq. (5), p. 2) and the Alon–Vinzant / ACV classification: the difference is the archimedean channels, which are not torus characters.
  - (ii) Gonçalves (arXiv:2312.11185v3, Theorem 3, p. 8): positive Fourier summation pairs ⟷ Hermite–Biehler E with A/B almost periodic in C⁺. In Remark 6 (p. 11), under GRH, the difference of the zero measures of two even primitive L-functions of different moduli is a (signed) summation pair of his Theorem 4 class, with a = log(N₁/N₂)·1_0 + Σ Λ(n)n^{−1/2}(χ₁ − χ₂)(n)[1_{±log n/2π}]: the archimedean term cancels. The difference: ξ *alone* has non-almost-periodic A/B (its Weyl term). Only differences or ratios of equal-Γ L-functions enter the almost-periodic class.
  - (iii) Favorov (arXiv:2311.02728, Prop. 3): almost periodic zero sets have a density, which excludes ξ's zero set.

**Addendum.**

(1) *The theorem at the page.* Burnol (arXiv:1106.4749v2, p. 2) states Hamburger's theorem. My translation: "Let f be meromorphic in the whole complex plane and of finite order (in particular with at most finitely many poles). If f(s) is represented for Re(s) > 1 by an absolutely convergent Dirichlet series Σ aₙn⁻ˢ, and the meromorphic function g(s) = χ(s)f(1 − s) also admits, for Re(s) ≫ 1, a convergent representation Σ bₙn⁻ˢ, then f is a multiple of the zeta function." Here χ(s) = π^{s−1/2}·Γ((1−s)/2)/Γ(s/2).
- Burnol (pp. 1–2) weakens the hypotheses: with g only bounded in a half-plane, f is "une combinaison linéaire finie de ζ(s), ζ(s+2), ζ(s+4), …".
- Knopp's "abundance" when finiteness of poles is dropped is `[recalled, unverified]`.
- The acceptance test in the orchestrator's form: (i) F/(π^{−s/2}Γ(s/2)) = Σ aₙn⁻ˢ absolutely convergent in a half-plane, so the orbit side is supported on log N; (ii) F(s) = F(1−s); (iii) finite order and poles only at 0, 1. Then F = c·ξ (times s(s−1)).

(2) *Does it weaken what must be verified?* Yes. The weights Λ(n) need not be matched; support and functional equation suffice. But each hypothesis is sharp:
- Nakamura (arXiv:2008.02570v4, abstract): f(s, χ) = q^s·L(s,χ) + i^{−κ}·G(χ)·L(s, χ̄) "satisfies Riemann's functional equation appearing in Hamburger's theorem if χ is even" and "has infinitely many zeros off the critical line σ = 1/2 if χ is non-real".
- Computed (`f_hamburger_checks.log`) for q = 7, χ cubic:
  - the functional equation holds to 1.0·10⁻³⁰;
  - 31 off-line zeros with 0 < t < 45, e.g. 0.6335674 + 1.6010817i, 1.0636457 + 4.2630456i, 0.8639106 + 8.7056136i;
  - the frequencies are log(n/7). So relaxing (i) from log N to a rescaled lattice already admits RH-false functions with **exactly ζ's functional equation**.
- DH and F_{a,q} are excluded by (ii) only, through their different functional equations (conductor 5 with Γ((s+1)/2); conductor q²). That is uniqueness, not arithmetic. At conductor q² the analogous space contains ζ(s)(1 + b·q^{−s} + q^{1−2s}) for every b, crossing the RH boundary at b = 2√q.
- So the test passes zoo I.1 by rigidity at conductor 1. The Euler product is never consumed; the whole burden sits on the design class.

(3) *The finite models.*
- Lee–Yang f_S: (i) holds (integer lattice: divisors of P); (iii) holds; (ii) fails. It satisfies its own functional equation (conductor P, no Γ: residual 2·10⁻³²), and Riemann's has residual 0.67 and 6.0. The Hamburger-type space for its own functional equation is all self-inversive Dirichlet polynomials on divisors of P, of dimension d(P): no rigidity.
- The analytic archimedean model A(s) + χ(s)A(1−s): (ii) holds (residual 10⁻³¹). (i) fails. (iii) fails: |F(3 + 10⁻⁶)| = 2.6·10¹², because A(−2) = 65000 ≠ 0, so the poles of χ at 3, 5, 7, … survive. Finite Euler products cannot supply the trivial zeros.
- Gonek's ζ_X is not meromorphic.
- A quantum graph with edge lengths log p satisfies (i) for free but fails (ii); its smooth density is constant (Kuipers–Hummel–Richter, p. 1: "The smooth part is completely different").

(4) *Verdict.* The design inversion is sound mathematics and a genuine reduction of *verification*. As a *mechanism* it collapses to Hilbert–Pólya plus a converse theorem (Hamburger/Hecke).
- The unsolved design problem is exactly a real-rooting generator for "integer-lattice Dirichlet series times the Γ-factor".
- Theorem 1 and Proposition 4 add a structural constraint: in any inner-function (Lee–Yang, Hermite–Biehler, unitary-secular) construction, prime channels add density, while ξ's density is entirely archimedean. The primes can therefore sit only in the *outer* part of a Hermite–Biehler function for ξ, never as inner torus channels of positive weight, unless an infinite-dimensional coupling hides their winding (the open frontier of §4).
- Not zoo IV.1 (no Weil form appears). It is on the record as Hilbert–Pólya folklore plus a converse theorem.

## §7 Prior-art verdict (read at the page)

- **Classification of Fourier quasicrystals by Lee–Yang polynomials:**
  - Kurasov–Sarnak arXiv:2004.05678 (stable pairs; p. 1 on Guinand/ζ);
  - Olevskii–Ulanovskii (C. R. 2020, corpus p2-19b, Theorem 1 p. 1: a Fourier quasicrystal with unit masses is the zero set of an exponential polynomial with real simple zeros);
  - Alon–Cohen–Vinzant arXiv:2303.03201v3, Theorem 1.1 (a real-rooted exponential polynomial is e^{λ₀x}·p(exp(ixℓ)) along a Q-independent positive ℓ, *not* the prime basis);
  - Alon–Vinzant arXiv:2307.13498, Theorem 1.9 (the counting lemma used here);
  - Alon–Kummer–Kurasov–Vinzant arXiv:2407.11184;
  - Alon–Kummer arXiv:2507.16029v3 (abstract read: periodic hypersurfaces supporting directional lighthouse measures are essentially Lee–Yang torus zero sets; no ζ content).
- **Infinite rank / Dirichlet series:** Favorov arXiv:2311.02728 and 2411.07190; Gonçalves arXiv:2312.11185v3 (Hermite–Biehler classification; the ζ-type Guinand differences, Remark 6).
- **The archimedean-phase variant:** Gonek arXiv:0704.3448.
- **Quantum graphs mimicking ζ:** Kuipers–Hummel–Richter arXiv:1307.6055.
- **Hamburger:** Burnol arXiv:1106.4749; Nakamura arXiv:2008.02570.
- **Null searches** (export API, logged in `verify/arxiv_search.log`): "Fourier quasicrystal" AND (zeta OR Riemann); "crystalline measure" AND zeta; "stable polynomial" AND "Dirichlet series"; "Riemann hypothesis" AND "stable polynomials"; "Euler product" AND "Hermite-Biehler". A null search is not evidence (V.5). The application Theorem K `[novelty: single-check]`.

## §8 The single most promising next step

Decide the coupling frontier. Either prove the sharpened counting bound
  N_F(I) ≥ (W_prime(I) − Σ_j W_{a_j}(I))/2π − 1
for det(I − V(s)U) with prime and archimedean inner channels (the error controlled by the archimedean *windings*, not by |d|), or construct a U that removes a prime channel's zeros from (−14.1, 14.1) using k ≥ 4 slow channels.
- Lemma F is the base case, and the §4 search is the evidence for the bound.
- If the bound holds, Theorem K extends to every finite-rank inner/unitary construction, and the orchestrator's design problem is forced into infinite rank with an explicit channel count (≥ W|I|/2π per window).
- If it fails, the counterexample is the first object in which prime channels coexist with ξ's low-height gap. That object is the seed for the Hamburger-tested design class.
- First rung: function fields, where Lemma F is exact.

Files: `NOTE.md`, `SHARED.md`, `sources/` (text of 17 papers; `arxiv-queries/`), `verify/` scripts and logs: `arxiv_search`, `k1_gap_theorem`, `k1_xi_lowzeros`, `b_alignment`, `b3_arch_realrootedness`, `d_inverse_design`, `d2_gap_evasion_by_coupling`, `d2b_gap_evasion_eigenphase`, `e_controls`, `f_hamburger_checks`.

## Close

**(K) KILLED.** The seed's route (Lee–Yang functions of finitely many primes, restricted to the Kronecker line, converging to ξ, then Hurwitz) cannot yield RH, because of Theorem K. Every non-constant such function (also with one archimedean inner channel of degree one) has at least 3 (respectively 2) zeros in (−14.1, 14.1), while Ξ has none there. The computed counterexample-shaped fact is Ξ's zero-free central box. The proved statement is Theorem 1 with Corollary 2 (prime channels add zero density ≥ log 2/2π per unit weight at every height; ξ's density is purely archimedean). Zoo Group-IV candidate: "prime channels add density" (Theorem 1 plus Proposition 4), with the coupled multichannel case as its open edge (§8).
