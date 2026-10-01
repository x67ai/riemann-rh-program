# NOTE — unit `dz-half-s39`: Diamond–Zhang's random Beurling systems have β = ½ almost surely

**Writer:** Opus 5.5 (subagent of Session 39), 2026-10-01. Brief: `BRIEF.md`. Record read at the line: frontier
`read-O.md` §4 A3 and §7(a); frontier `NOTE.md` §4 Theorem B (as repaired by read-O F2); digest
`novel-wave-s37/insights-digest.md` §F.2 item 4 (U5a); Diamond–Zhang book (AMS Surv. 213, 2016) ch. 17 at the page
(`sources/t-50-diamond-zhang-2016-book.txt`, extracted from `fetched-r2/t-50-…-BOOK.pdf`); BDR z-02 p. 3 fn. 4.
Labels: [proved here], [quoted, file:line], [recalled, unverified], [computed], [heuristic].

## §0. Close

**Close: T** (a proof, every step written; single writer — the standing dual read is still owed).

**THEOREM (BDR fn. 4, for almost every realization)** [proved here, §2]. Let P_B be the g-prime system of Diamond–Zhang
Theorem 17.14, i.e. the independent Bernoulli selection from the grid (17.13) with p_k = ∫_{v_{k−1}}^{v_k} f_C. Almost
surely
  lim sup_{x→∞} |N_B(x) − k₂x| / (x/log x)^{1/2} > 0,
so N_B(x) − k₂x ≠ O(x^τ) for every τ < ½. Together with DZ 17.14(i) (N_B − k₂x = O(x^{1/2}exp{c(log x)^{2/3}})) and (iv)
(ψ_B − x ≠ O(x^{1−δ})): **β₀ = ½ and P_B is a [1, ½]-system, for almost every realization**, and after any finite change of
its g-primes (Remark 17.12; Lemma 2.5). The same holds for Theorem 17.11's P_R, which is moreover a [½, ½]-system a.s.
(Corollary 2.6) — the exponents BDR l. 123–124 say "could not be determined". BDR's "Most likely the value of β₀ equals 1/2"
is therefore correct, and the sharpest in-print test of Conjecture U lands on U's boundary α = 2β (consistent, not refuting).

**How the named risk was handled.** The dependence across (x/2, x] is exact and one-dimensional: every g-integer ≤ x holds at
most one block prime, and the block enters the density only as ρ = ρ^c e^{S}, S = Σ_{block} X_k(−log(1 − 1/v_k)) (Lemma 2.1).
Linearizing e^{S} leaves a remainder R with E[R²|G]^{1/2} ≪ κ/log x (Lemma 2.3); the linear part has conditional variance
≥ c κ²x/((N₀+1)² log x) (Lemma 2.2) and is Gaussian by Berry–Esseen. Anti-concentration alone then gives the theorem; no
0–1 law is needed. The brief's stop condition (dependence uncontrollable) was not met. **Second, independent proof**
(Prop. 2.4): ζ_B = ζ_C e^{−F₁+F₂} with −F₁ ≥ 0 and the random part of F₂ unbounded above as σ → ½+ a.s. (CLT + Kolmogorov),
so ζ_B is unbounded at ½ and Landau's step forbids N_B − k₂x = O(x^τ), τ < ½.

**Finite rung** (§4; X = 10⁸, 5 seeds per template, enumeration of every g-integer). Sup-slopes over [10³, X]: 0.492 ± 0.012
(P_R), 0.479 ± 0.020 (P_B); log-corrected mean-square slopes 0.519, 0.522. Top window [10⁶, X]: 0.514 ± 0.054, 0.381 ± 0.060,
inside the measured per-seed two-decade systematic ±0.14. One scale, on realized systems (§3.3): the identity of Lemma 2.1 holds
exactly (8/8), the conditional variance equals the Theorem-B value (ratios 0.967–1.070), the conditional law is Gaussian.
Controls: ℙ (0.000; N(e) = ⌊e⌋ exactly), the frontier's T_0.90 (0.440 ± 0.011, reproducing its α/2) and T_0.95 (0.482 ± 0.015),
the deterministic grid system P_det (β ≥ ½ proved by the prime-square branch point, ½ in the data; E/(x/log x)^{1/2} = −0.5995
measured vs −0.5998 predicted, §4.3), and T₁ (β = 1, a negative control explained in §4.4).

**What it does not say.** (i) Nothing about the exceptional null set: a particular subsequence of the grid satisfying DZ's
(17.46) with β < ½ is not excluded (U-1 — that is Conjecture U at α = 1 in DZ's class). (ii) Nothing about ζ: the statement is
about a random Beurling world, where the mechanism is the variance of the selection and, separately, the prime squares.
(iii) Prior art (§5): no paper after BDR settles fn. 4 (arXiv and BDR's citers searched 2026-10-01; Broucke 2507.13780 gives
the upper bound only, with a different discretization).

**Also new, smaller** (§4.3, §5): the grid construction without any randomness already has β ≥ ½ (a (2s − 1)^{−1/2} branch
point from the prime squares; = ½ in the data, constant predicted and measured); and, conditionally on one property of the template not
checked at the page, Broucke's Theorem 1.6 systems are exact [1, ½]-systems (Remark 5.1, U-3).

## §1. The objects, read at the page

**1.1 The construction** [quoted, `sources/t-50-diamond-zhang-2016-book.txt`; book pp. 196–202]. A template density f ≥ 0 on
[1, ∞); an increasing sequence 1 = v₀ < v₁ < … → ∞; p_k := ∫_{v_{k−1}}^{v_k} f(v) dv (Lemma 17.5, "satisfies 0 < p_k ≤ 1 for
k ≥ k₀"); X_k independent with P[X_k = 1] = p_k, P[X_k = 0] = 1 − p_k (proof of Lemma 17.2, book p. 197); the g-primes are
the v_k with X_k = 1. DZ take the grid (17.13), book p. 201: "v₀ = 1 and v_k = n + ℓ/2ⁿ, for k = 2ⁿ + ℓ, n = 0, 1, 2, …,
1 ≤ ℓ < 2ⁿ". As printed the index set {2ⁿ + ℓ : 1 ≤ ℓ < 2ⁿ} omits k = 1, 2, 4, 8, …; the grid meant is
Γ := {1} ∪ {n + ℓ/2ⁿ : n ≥ 1, 0 ≤ ℓ < 2ⁿ} (Remark 17.6's "closed under addition and multiplication" needs the integers,
e.g. 1.5 + 1.5 = 3). Nothing below depends on the reading: the proof uses only independence, p_k = ∫_{cell} f, and
max{p_k : v_k ∈ (x/2, x]} → 0; on Γ that maximum is ≤ 2^{2−⌊x/2⌋}.

**1.2 The two templates.** Theorem 17.11 (the RH example P_R): f_R(v) = (1 − v⁻¹)/log v (book p. 206, "Consider the template
continuous density"). Theorem 17.14 (the DLVP example P_B): f_C of (17.44), book p. 218,
f_C(v) = (1 − v⁻¹)/log v − 2Σ_{k≥1} (g(v^{4^{−k}})/4^k) v^{−4^{−k}} cos(γ_k log v), γ_k = e^{4^k}, β_k = 1 − 4^{−k}
(p. 214), g = Σ_n χ^{*n}/n with χ = 1_{[e,e²]} (17.30); and (17.45), p. 218: "(1 − c)(1 − v⁻¹)/log v ≤ f_C(v) ≤
(1 + c)(1 − v⁻¹)/log v holds for v ≥ e⁴", c = 2c₁/(1 − e⁻⁴), c₁ = 0.410616… (p. 216), so c = 0.8366… < 1 [computed].
For v < e⁴, f_C = f_R (p. 218). Both templates therefore satisfy
  (H) c_* /log v ≤ f(v) ≤ C_*/log v for v ≥ v_*, with (c_*, C_*) = (0.49, 1) for f_R (v_* = 100), (0.16, 1.84) for f_C.

**1.3 What DZ prove about the result** [quoted]. Thm 17.14 (book p. 208): "(i) N_B(x) = k₂x + O(x^{1/2} exp{c(log x)^{2/3}})
with k₂ > 0; (ii) ζ_B(s) is analytic for σ > 1/2 except for a simple pole at s = 1 with residue k₂; (iii) ζ_B(s) has
infinitely many zeros on the curve σ = 1 − 1/log t, t ≥ e², and no zeros to its right; (iv) lim sup / lim inf of
(ψ_B(x) − x)/(x exp{−2√log x}) = 2 / −2." Thm 17.11 (p. 205): the same (i)–(ii) for N_R with k₁ > 0, no zeros in σ > ½, and
"(iv) π_R(x) = li(x) + O(x^{1/2})". The proofs select the subsequence by Lemma 17.2, whose conclusion holds off a
Borel–Cantelli null set (Remark 17.4: "for almost all subsequences (in the statistical sense)"), then argue
deterministically; so (i)–(iv) hold for almost every realization. DZ's representation (p. 219):
ζ_B(s) = ζ_C(s) exp{−F₁(s) + F₂(s)}, F₁(s) = ∫{v^{−s} + log(1 − v^{−s})}dπ_B(v), F₂(s) = ∫ v^{−s}{dπ_B(v) − f_C(v)dv}, both
analytic on σ > ½. Remark 17.12 (p. 205): "by making a finite number of changes in the g-primes … we can produce a system
that … satisfies k₁ = 1 … (These remarks apply as well for the example in Theorem 17.14.)"

**1.4 The question** [quoted, z-02 l. 133–136, 165]. BDR: "that of a [1, β₀]-system⁴ is in [7, Ch. 17] (which is based on
the papers [6] and [17]) for some β₀ ≤ 1/2"; fn. 4: "Most likely the value of β₀ equals 1/2, but in principle it is still
possible that β₀ could be smaller." Also l. 122–124, on Zhang's system: "Due to the probabilistic nature of the method,
no precise value of α and β could be determined." BDR's definition (l. 97–101): β = lim sup log|N(x) − ax|/log x.
**1.5 DMV** [quoted, fr `sources/p1-02-…txt` l. 935–945]: DMV's Lemma 9 uses the same selection ("let X_k be independent
Bernoulli variables with parameters p_k = ∫_{v_{k−1}}^{v_k} 1 dΠ_C(v) … The v_k must increase sufficiently slowly to
ensure that p_k ≤ 1/2"), so §2 applies to DMV's random system as soon as dΠ_C satisfies (H) (not checked at the page).

## §2. The theorem and its proof

**2.0 Setting.** Γ = {1 = v₀ < v₁ < …} any increasing sequence → ∞ with v₁ > 1; X_k independent Bernoulli(p_k); P = {v_k : X_k = 1};
N(x) = number of g-integers ≤ x (formal products, with multiplicity). Hypotheses:
- (H0) p_k = ∫_{v_{k−1}}^{v_k} f(v) dv ∈ (0, 1] with f ≥ 0 measurable on [1, ∞).
- (H1) c_*/log v ≤ f(v) ≤ C_*/log v for v ≥ v_* (the constants of §1.2 for f_R, f_C).
- (H2) m(x) := max{p_k : (v_{k−1}, v_k] ∩ (x/2, x] ≠ ∅} → 0 and max{v_k − v_{k−1} : v_k ≤ 2x} ≤ 1 for large x
  (on DZ's Γ: m(x) ≤ 2^{2−⌊x/2⌋}, since f ≤ 1.84 and the cells meeting (x/2, x] have width ≤ 2^{1−⌊x/2⌋}; the mesh is ≤ ½).
- (H3) almost surely N(x)/x → ρ ∈ (0, ∞) (for P_R, P_B: DZ 17.11(i), 17.14(i), which hold a.s., §1.3).
Write E(x) := N(x) − ρx and s_x := (x/log x)^{1/2}.

**Theorem 1 (the one-scale lower bound)** [proved here]. Under (H0)–(H3), almost surely
  lim sup_{x→∞} |N(x) − ρx| / (x/log x)^{1/2} > 0.
In particular, almost surely N(x) − ρx ≠ O(x^τ) for every τ < ½.

**Corollary 2 (BDR fn. 4)** [proved here, given DZ's (i)–(iv) quoted in §1.3]. For almost every realization of the
Diamond–Zhang construction of Theorem 17.14, the system P_B satisfies N_B(x) − k₂x = Ω((x/log x)^{1/2}) and
N_B(x) − k₂x = O(x^{1/2}exp{c(log x)^{2/3}}); hence β(P_B) = ½, and with 17.14(iv) (ψ_B − x ≠ O(x^{1−δ}) for every δ > 0)
α(P_B) = 1: **P_B is a [1, ½]-system, so β₀ = ½ for almost every realization.** The same holds after any finite change of
the g-primes (Remark 17.12's normalization; Lemma 2.5). For Theorem 17.11's P_R: β(P_R) = ½ and α(P_R) = ½ a.s.
(Corollary 2.6), so Zhang's system is a [½, ½]-system — the value BDR l. 123–124 say "could not be determined".

*Scope, stated exactly.* The statement is about the random construction (every realization off a null set). It says
nothing about a particular subsequence of Γ that satisfies DZ's (17.46) but lies in the exceptional null set; whether
every such subsequence has β ≥ ½ is Conjecture U at α = 1 restricted to DZ's class (Untried, §6).

**2.1 Notation for one scale.** Fix x ≥ 4. B = B_x := {k : v_k ∈ (x/2, x]} (finite); G = G_x := σ(X_k : k ∉ B).
N^c(y) := number of g-integers ≤ y built from P ∖ (x/2, x] (G-measurable). n₀(y) := number of g-integers ≤ y built from
the g-primes in (1, 2); N₀ := n₀(2−) − 1, the number of g-integers in (1, 2) (finite a.s.; on DZ's Γ, N₀ ∈ {0, 1}).
a_k := −log(1 − 1/v_k); μ := Σ_{k∈B} p_k a_k; S := Σ_{k∈B} X_k a_k; D := S − μ. ρ^c := lim_{y→∞} N^c(y)/y.
κ := ρ^c e^{μ}; c_k := n₀(x/v_k) − κ x a_k (k ∈ B).

**Lemma 2.1 (the one-scale identity; all the dependence across (x/2, x] in one factor)** [proved here]. For x ≥ 4, a.s.:
(a) N(x) = N^c(x) + Σ_{k∈B} X_k n₀(x/v_k);  (b) ρ^c exists, is G-measurable, and ρ = ρ^c e^{S};
(c) E(x) = Y + L + R with Y := N^c(x) + Σ_{k∈B} p_k n₀(x/v_k) − κx (G-measurable), L := Σ_{k∈B}(X_k − p_k)c_k,
R := −κx(e^{D} − 1 − D).
*Proof.* (a) Two block primes q, q′ ∈ (x/2, x] have qq′ > x²/4 ≥ x, so a g-integer m ≤ x contains at most one block prime,
with multiplicity one (q² > x). If it contains q then m = qm′ with m′ ≤ x/q < 2, and m′ is built from g-primes < 2 ≤ x/2,
none in the block; m′ is counted by n₀(x/q). Otherwise m is counted by N^c(x). (b) For any g-prime q of a system Q,
the g-integers of Q are the q^j·m, j ≥ 0, m a g-integer of Q ∖ {q}; so N_{Q∖{q}}(y) = N_Q(y) − N_Q(y/q), and N_Q(y) ∼ ρ_Q y
implies N_{Q∖{q}}(y) ∼ ρ_Q(1 − 1/q)y. Removing the finitely many block primes one at a time from P (where (H3) holds):
ρ^c = ρ Π_{k∈B}(1 − 1/v_k)^{X_k} = ρe^{−S}. ρ^c = lim N^c(y)/y is a function of (X_k)_{k∉B}. (c) E(x) = N^c(x) +
Σ X_k n₀(x/v_k) − ρ^c x e^{S}, and e^{S} = e^{μ}(1 + D + (e^{D} − 1 − D)), with D = Σ_{k∈B}(X_k − p_k)a_k. Hence
ρ^c x e^{S} = κx + κxΣ_{k∈B}(X_k − p_k)a_k − R; substitute X_k n₀ = p_k n₀ + (X_k − p_k)n₀ and collect. ∎

*Remark (what "the dependence across (x/2, x]" is).* Conditionally on G the block variables are independent; they are coupled
in E(x) only through the random density, ρ = ρ^c e^{S}, a smooth function of the single linear statistic S. The
frontier's Theorem B has the same structure (its κ_p, repaired in read-O F2, is the G-measurable part of this factor);
here the coupling is kept exact and paid for by R, which is quadratic in D (Lemma 2.3).

**Lemma 2.2 (the conditional variance is ≍ x/log x)** [proved here]. Assume (H1), (H2). Let σ² := Var(L | G) =
Σ_{k∈B} p_k(1 − p_k)c_k². There is x₁ = x₁(N₀) < ∞, depending only on N₀ (which is G_x-measurable for every x ≥ 4)
and on the deterministic m(·), v_*, c_* — not on κ — such that for x ≥ x₁
  σ² ≥ c_* κ² x / (2^{11}(N₀ + 1)² log x).
*Proof.* Put φ(y) := n₀(y) − κy on [1, 2). n₀ is constant on at most N₀ + 1 intervals of [1, 2), and on each φ is linear
with slope −κ, so {y : |φ(y)| < θ} meets each in an interval of length ≤ 2θ/κ. With θ := κ/(4(N₀ + 1)) the exceptional set
has measure ≤ ½; its complement J ⊂ [1, 2) has |J| ≥ ½ and at most 2(N₀ + 1) components. For v ≥ 2,
0 ≤ −log(1 − 1/v) − 1/v ≤ 1/v², so |c_k − φ(x/v_k)| ≤ κx/v_k² ≤ 4κ/x ≤ θ/2 once x ≥ 32(N₀ + 1); then |c_k| ≥ θ/2 whenever
x/v_k ∈ J. With J_x := {v ∈ (x/2, x] : x/v ∈ J} (≤ 2(N₀ + 1) intervals) and m(x) ≤ ½:
  σ² ≥ (θ²/8) Σ_{k∈B, x/v_k∈J} p_k ≥ (θ²/8)(∫_{J_x} f − (4N₀ + 6)m(x)),
since only cells straddling an endpoint of J_x are miscounted. By (H1) and v = x/y, dv = x dy/y²:
∫_{J_x} f ≥ (c_*/log x)·x∫_J dy/y² ≥ c_* x/(8 log x). For x ≥ x₁(N₀) — x ≥ max(2v_*, 32(N₀ + 1)), m(x) ≤ ½ and (4N₀ + 6)m(x) ≤ c_*x/(16 log x) — the m(x) term is below half of this, so
σ² ≥ θ² c_* x/(128 log x) = c_* κ² x/(2^{11}(N₀+1)² log x). ∎

**Lemma 2.3 (the coupling remainder is negligible)** [proved here]. Assume (H1), (H2). For x ≥ x₂ (deterministic),
E[D² | G] = Σ_{k∈B} p_k(1 − p_k)a_k² ≤ 5C_*/(x log x), and for every u > 0,
  P(|R| > u | G) ≤ E[D² | G]·(1 + eκx/(2u)).
*Proof.* a_k ≤ 1/v_k + 1/v_k² ≤ (2/x)(1 + 2/x) on B, and Σ_{k∈B} p_k ≤ ∫_{x/2−1}^{x} f ≤ C_* x/log x for large x, which gives the
first bound. On {|D| ≤ 1}, |e^{D} − 1 − D| ≤ (e/2)D², so {|R| > u} ⊂ {|D| > 1} ∪ {D² > 2u/(eκx)}; apply Chebyshev to both. ∎

**Proof of Theorem 1.** Fix λ > 0. By Lemma 2.1, {|E(x)| ≤ λs_x} ⊂ {|Y + L| ≤ 2λs_x} ∪ {|R| > λs_x}. Given G, L is a sum of
independent centered terms ξ_k = (X_k − p_k)c_k with |ξ_k| ≤ M := N₀ + 1 + 3κ and Σ E|ξ_k|³ ≤ Mσ². The Berry–Esseen
inequality for non-identically distributed summands [recalled, unverified: Esseen 1945, any absolute constant C₀] gives
sup_t |P(L ≤ t | G) − Φ(t/σ)| ≤ C₀M/σ, so for every G-measurable Y
  P(|Y + L| ≤ 2λs_x | G) ≤ 4λs_x/(σ√(2π)) + 2C₀M/σ.
Insert Lemma 2.2 (σ ≥ √c_* κ s_x/(2^{5.5}(N₀+1))) and Lemma 2.3 (u = λs_x): for x ≥ max(x₁, x₂),
  P(|E(x)| ≤ λs_x | G) ≤ Φ_x := min{1, Kλ(N₀ + 1)/κ + ε_x},  K := 2^{7.5}/√(2πc_*),
  ε_x := 2^{6.5}C₀(N₀ + 1 + 3κ)(N₀ + 1)/(√c_* κ s_x) + (5C_*/(x log x))(1 + eκ√(x log x)/(2λ));
for x < max(x₁, x₂) put Φ_x := 1. Now κ = κ_x = ρ e^{μ−S}, with 0 ≤ μ ≤ 5C_*/log x and E S = μ, so κ_x → ρ in probability;
N₀ does not depend on x ≥ 4; x₁ < ∞ a.s. Hence Φ_x → min{1, Kλ(N₀ + 1)/ρ} in probability, and by bounded convergence
  lim sup_{x→∞} P(|E(x)| ≤ λs_x) ≤ lim E Φ_x = h(λ) := E min{1, Kλ(N₀ + 1)/ρ}.
Since ρ > 0 and N₀ < ∞ a.s., h(λ) → 0 as λ ↓ 0. Finally, with A_{x₀} := {|E(n)| ≤ λs_n for all integers n ≥ x₀},
P(A_{x₀}) ≤ inf_{n≥x₀} P(|E(n)| ≤ λs_n) ≤ lim sup_n P(|E(n)| ≤ λs_n) ≤ h(λ), so P(lim sup_n |E(n)|/s_n < λ) ≤
P(∪_{x₀} A_{x₀}) ≤ h(λ). Letting λ ↓ 0: P(lim sup |E|/s_x = 0) = 0. As x^τ = o(s_x) for τ < ½, the last claim follows. ∎

*Remarks on the proof.* (i) No 0–1 law is needed (Theorem B used Kolmogorov's; here the anti-concentration bound h(λ) → 0
does the work). (ii) The only inputs from DZ are the construction and (H3); the variance comes from the block alone.
(iii) The constant K is wasteful; §3 computes σ² exactly.

**Proposition 2.4 (second, independent proof of β ≥ ½: ζ_B is unbounded at s = ½)** [proved here]. For P_B (and P_R with
ζ_C replaced by s/(s − 1)), almost surely lim sup_{σ→½+} |ζ_B(σ)| = +∞; hence ζ_B has no analytic continuation to any
neighborhood of s = ½, and N_B(x) − k₂x ≠ O(x^τ) for every τ < ½.
*Proof.* (1) Landau step: if E(x) = O(x^τ), τ < ½, then ζ_B(s) = s∫₁^∞ N_B(x)x^{−s−1}dx = k₂s/(s − 1) + s∫₁^∞ E(x)x^{−s−1}dx
continues analytically to σ > τ, s ≠ 1, and is bounded on [½, ½ + δ]. (2) On real σ ∈ (½, 1), DZ's representation (§1.3)
gives ζ_B(σ) = ζ_C(σ)exp{−F₁(σ) + F₂(σ)}, with −F₁(σ) = Σ_p Σ_{j≥2} p^{−jσ}/j ≥ 0. (3) |ζ_C(σ)| ≥ c₀ > 0 on [½, 1): by
(17.39), ζ_C = (s/(s − 1))Π_k |G(4^k(σ − ρ_k))|² on the real axis, and for z = 4^k(σ − ρ_k), Re z = 1 − 4^k(1 − σ) ≥ 1 − 4^k/2,
|z| ≥ 4^k e^{4^k}, so by (17.22) |G(z) − 1| ≤ (|e^{−z}| + |e^{−2z}|)/|z| ≤ (e^{−4^k/2−1} + e^{−2})/4^k ≤ 0.19·4^{−k}; the product is
≥ Π_k(1 − 0.19·4^{−k})² > 0 and |σ/(σ − 1)| ≥ 1 [computed from the printed definitions]. (4) F₂(σ) = W(σ) + Δ(σ), with
W(σ) := Σ_k (X_k − p_k)v_k^{−σ} and Δ(σ) := Σ_k ∫_{v_{k−1}}^{v_k}(v_k^{−σ} − v^{−σ})f(v)dv, |Δ(σ)| ≤ Σ_k p_k σ v_{k−1}^{−σ−1}
(mesh ≤ 1) — bounded on [½, 1). W converges a.s. for σ > ½ (independent centered terms, Σ p_k v_k^{−2σ} < ∞). Its variance
V(σ) = Σ p_k(1 − p_k)v_k^{−2σ} ≥ (1/8)∫_{v_*}^∞ f(v)v^{−2σ}dv → ∞ as σ → ½+ (by (H1), since v_k ≤ 2v on each late cell and
p_k ≤ ½); the summands are bounded by 1, so Lindeberg's CLT gives W(σ)/V(σ)^{1/2} ⇒ N(0, 1) as σ → ½+. Hence for all M,
δ: P(sup_{(½,½+δ)} W > M) ≥ lim_{σ→½+} P(W(σ) > M) = ½, so P(lim sup_{σ→½+} W(σ) = +∞) ≥ ½. Changing finitely many X_k moves
W by a bounded amount uniformly on (½, 1), so this is a tail event: its probability is 1 (Kolmogorov). (5) On that event,
|ζ_B(σ)| ≥ c₀ e^{W(σ) − sup|Δ|} is unbounded as σ → ½+, contradicting (1). ∎
*What the two proofs share and what they do not.* Both use only the block/tail randomness of the selection; Prop. 2.4 needs
DZ's continuation to σ > ½ and gives β ≥ ½ only; Theorem 1 is elementary and quantitative (Ω((x/log x)^{1/2})). The
prime squares push the same way: −F₁(σ) ≥ ½Σ_p p^{−2σ} → +∞ (a (2σ − 1)^{−1/2}-type branch point, §4.4's deterministic
control); for P_B it is not needed.

**Lemma 2.5 (finite changes)** [proved here]. Let P′ differ from P by adding or removing finitely many g-primes, with
densities ρ, ρ′ > 0. For every τ > 0, E = O(x^τ) ⟺ E′ = O(x^τ); and E = o(s_x) ⟺ E′ = o(s_x).
*Proof.* One prime q at a time: if P′ = P ∖ {q} then N_P(x) = Σ_{j≥0} N_{P′}(x/q^j), ρ = ρ′/(1 − 1/q), hence
E(x) = Σ_{j≥0} E′(x/q^j) and E′(x) = E(x) − E(x/q) (with |E(y)| ≤ 1 + ρy for y < 1). Both maps preserve O(x^τ), τ > 0, and
o(s_x), since Σ_j (x/q^j)^τ ≪ x^τ and Σ_{j: x/q^j ≥ 2} s_{x/q^j} ≪ s_x. ∎

**Corollary 2.6 (the primes of P_R)** [proved here]. Under (H0)–(H2), a.s. ψ_P(x) − x ≠ O(x^τ) for every τ < ½. With
17.11(iv) (π_R(x) = li(x) + O(x^{1/2}), whence ψ_R(x) = x + O(x^{1/2}log x)), α(P_R) = ½ a.s.
*Proof.* Same one-scale argument, simpler: ψ_P(x) = ψ^c(x) + Σ_{k∈B} X_k log v_k exactly (block primes have no power ≤ x);
the block part is linear, with conditional variance Σ_{k∈B} p_k(1 − p_k)log² v_k ≍ x log x by (H1), so Berry–Esseen gives
P(|ψ_P(x) − x| ≤ λ(x log x)^{1/2} | G) ≤ K′λ + o(1), and the end of the proof of Theorem 1 applies. ∎

**Proof of Corollary 2.** (H0)–(H2) hold for f_C and f_R on DZ's grid (§1.1–1.2); (H3) and the O-bound are DZ's (i).
Theorem 1 gives the Ω-bound, so β(P_B) = ½ with BDR's definition (l. 97–101); 17.14(iv) gives α = 1; Lemma 2.5 carries
all of it through Remark 17.12's finite changes; Corollary 2.6 gives α(P_R) = ½. ∎

## §3. The variance, computed two ways

The quantity is the one-scale conditional variance of Lemma 2.2, σ² = Var(L | G) = Σ_{k∈B} p_k(1 − p_k)c_k², with
c_k = c(v_k), c(v) := n₀(x/v) − κx a(v), a(v) = −log(1 − 1/v).

**3.1 Way 1 — the exact sum over DZ's grid** [computed, `verify/onescale.py` part A]. For x ≤ 24 the cells of Γ in
(x/2, x] are few enough (≤ 2^{24}) to enumerate: p_k by 8-point Gauss–Legendre on each cell, c_k at the grid point, the sum
taken exactly. For larger x the grid has ~x·2^{x}/2 points in the block and only way 2 is available — which is legitimate,
because of the bound in 3.2. Result (`logs/onescale_A.log`, κ ∈ {0.7, 1, 2.4}, both n₀): relative gap grid − continuum
−1.8·10⁻¹ at x = 6 (56 cells), −6.8·10⁻² at x = 8, −1.1·10⁻² at x = 12, −1.9·10⁻³ at x = 16, −1.6·10⁻⁴ at x = 22 (κ = 0.7,
1.5 ∉ P; 4 192 256 cells), down to 7.6·10⁻⁷ (κ = 1, 1.5 ∈ P): it shrinks like 2^{−x/2}, as the bound says. The
Theorem-B asymptotic (x/log x)I(κ; n₀) is 10–20 % off at x = 22 — the O(1/log x) — and 3–5 % off at x = 2²³ (3.3).

**3.2 Way 2 — the Theorem-B (continuum) route** [proved here]. Put σ²_cont := ∫_{x/2}^{x} f(v)c(v)² dv. Then
  |σ² − σ²_cont| ≤ m(x)·Σ_{k∈B} p_k c_k² + 2M·h(x)·(5κ/x)·∫_{x/2−1}^{x} f + 2(N₀ + 2)M²m(x),
where h(x) is the mesh of Γ on the block (≤ 2^{−⌊x/2⌋}) and M = max|c|: the first term is the −p_k² part, the second the
Riemann-sum error on the smooth pieces (|c′(v)| ≤ κx/v² ≤ 4κ/x·(1 + o(1)) there), the third the ≤ N₀ + 2 cells that straddle
a jump of n₀(x/·) or an end of the block. On Γ the right side is ≤ 2^{−x/2}x^{O(1)}: way 1 and way 2 agree to double
precision once x ≳ 100. Substituting v = x/y and f(v) = f(x)(1 + O(1/log x)) on the block (for f_R; for f_C the k = 1 term of
(17.44) has period 2πv/e⁴ ≈ 0.115v in v and does not average out over one block, so σ²_cont is computed with f_C itself):
  σ²_cont = (x/log x)·I(κ; n₀)·(1 + O(1/log x)),   I(κ; n₀) := ∫₁² (n₀(y) − κy)² dy/y².
On Γ the only grid point in (1, 2) is 1.5, so there are two cases [computed by hand; checked in `onescale.py`]:
  1.5 ∉ P (N₀ = 0): I = ½ − 2κ log 2 + κ²;   1.5 ∈ P (N₀ = 1): I = 1 − (2 log(3/2) + 4 log(4/3))κ + κ² = 1 − 1.96166κ + κ².
Both are ≥ min over κ > 0, i.e. ≥ ½ − (log 2)² = 0.0195 and ≥ 1 − 1.96166²/4 = 0.0380 respectively: **the one-scale variance
never degenerates on DZ's grid** (Lemma 2.2's constant 2^{−11}c_* is far from sharp). This is the frontier's
σ_B² = Σ_{p∈B}v_p(κ_p x/p − 1)² with v_p ↦ f(v)dv and the ½-offsets of the coprime sums T_d replaced by n₀.

**3.3 Way 3 — the conditional law itself, on realized systems** [computed, `verify/onescale.py` part B,
`logs/onescale_B.log`]. For two runs (P_R seed 1: 1.5 ∉ P, κ ≈ 2.38; P_B seed 1: 1.5 ∈ P, κ ≈ 4.69) and x = 2^m, m = 14,
17, 20, 23: (a) N^c(x) recomputed by enumerating P minus the block, and Lemma 2.1(a) N(x) = N^c(x) + Σ_{q∈B} n₀(x/q) checked
exactly — residual 0 in all 8 cases (852 to 268 388 block primes); (b) the block resampled (Poisson with intensity f on
(x/2, x], 4000/4000/2000/500 replicates) with the exact coupling E′ = N^c(x) + Σ n₀(x/q′) − ρ^c x e^{S′} (no linearization).

| run, x | σ²_cont/(x/log x) | I(κ; n₀) | Var(E′)/σ²_cont | skew, exc. kurt. | KS p | z of realized E(x) |
|---|---|---|---|---|---|---|
| P_R s1, 2¹⁴ | 2.995 | 2.864 | 0.987 | −0.06, +0.01 | 0.91 | +0.54 |
| P_R s1, 2¹⁷ | 2.970 | 2.863 | 0.967 | −0.08, +0.02 | 0.36 | +1.67 |
| P_R s1, 2²⁰ | 2.940 | 2.850 | 1.032 | −0.01, +0.05 | 0.92 | −1.09 |
| P_R s1, 2²³ | 2.930 | 2.852 | 1.070 | +0.12, −0.18 | 0.97 | −0.30 |
| P_B s1, 2¹⁴ | 14.33 | 13.77 | 1.033 | −0.03, −0.04 | 0.99 | −0.40 |
| P_B s1, 2¹⁷ | 14.28 | 13.81 | 0.995 | −0.04, −0.06 | 0.88 | −0.20 |
| P_B s1, 2²⁰ | 14.22 | 13.82 | 1.041 | +0.01, +0.11 | 0.90 | +0.48 |
| P_B s1, 2²³ | 14.15 | 13.81 | 1.048 | −0.00, −0.00 | 0.72 | +0.44 |

The variance ratios are 1 within their sampling error (sd √(2/R) = 0.022, 0.022, 0.032, 0.063); the conditional law is
Gaussian (Berry–Esseen regime); the realized E(x) is a typical draw from it. So the exact coupling through e^{S} changes
nothing measurable (Lemma 2.3), and the one-scale variance is the Theorem-B number. The ratio σ²_cont/((x/log x)I) − 1 =
0.03–0.05 is the O(1/log x) of 3.2.

## §4. Finite rung: simulation of the construction to 10⁸, five seeds, with controls

**4.1 Method** [computed; code in `verify/`, logs in `verify/logs/`, per-run data in `verify/data/`].
- *The construction, exactly.* `dzgen.py` draws every cell of Γ with its own Bernoulli(p_k) for the units n ≤ 22 (p_k by
  8-point Gauss–Legendre; max p_k = 0.4506, the cell (1, 1.5]). Above, a Poisson process with intensity f, each point
  rounded up to its grid point: its law differs from the exact Bernoulli selection by at most Σ_k p_k² ≤ 2⁻²² in total
  variation, over the whole range. f_C is the printed (17.44) (k = 1, 2 active below 10⁸; k = 3 needs log v ≥ 64); every
  proposal checks f ≤ envelope ((1 + c)f_R with c = 0.8366, i.e. (17.45)); the largest ratio met was < 1.
- *The density.* log ρ = Σ_{p≤X} −log(1 − 1/p) − Ein(log X) − 2Σ_k ∫_{log X}^∞ a_k(t)cos(γ_k t)dt + S_tail, from
  log ρ = log r_T + ∫₁^∞ v^{−1}(dΠ_P − f dv) and ∫₁^X f_R/v = Ein(log X), with r_T = Π_k|G(4^k(1 − ρ_k))|² for f_C
  (a_k(t) = g(e^{t/4^k})4^{−k}e^{−t/4^k}; the identity log|G(4(1 − ρ₁))|² = −2∫₀^∞a₁cos(γ₁t)dt, which tests g, 4^k, γ_k and
  the sign of (17.44) at once, holds: −0.0032445 closed form vs −0.0032483 by quadrature at step 10⁻⁴, the gap halving with
  the step; f_C/f_R ∈ [0.237, 1.763] ⊂ [1 − c, 1 + c] on 2·10⁶ points of [e⁴, 10⁸]; `logs/residue_check.log`).
  S_tail — the g-primes above X, which move ρ but not N(x ≤ X) — is sampled as N(1/(2X log X), 1/(X log X)): at X = 10⁸ its
  sd is 2.3·10⁻⁵, i.e. an uncertainty of ρ·x·2.3·10⁻⁵ in ρx, comparable to (x/log x)^{1/2} only at x ≈ X. This is the
  dependence of E(x) on primes beyond x, sampled in law rather than ignored.
- *The counting.* `dzcount.c` enumerates every g-integer ≤ 10⁸ (DFS over non-decreasing prime indices; up to 4.7·10⁸ per run)
  into the bins (e_i, e_{i+1}], e = 2^j(1 + i/1024); N(e) = 1 + cumulative count is exact at every edge (control: rational
  primes give N(e) = ⌊e⌋ at all 27 125 edges ≤ 10⁸, `logs/ctl_primes_exact.log`). E is sampled at the edges only (1024 per dyadic block).
- *Estimators* (`analyze.py`, as the frontier's `fit.py`): per block j, A_j = max|E|, the running sup M_j, the dyadic mean
  square MS_j; slopes on windows [10^a, 10⁸], a = 3, …, 6: "sup" (log M vs log x), "supL" (log(M·(log x)^{1/2})), "ms"
  (½ slope of log MS), "msL" (½ slope of log(MS·log x)). The L-versions test the one-scale prediction |E| ≍ (x/log x)^{1/2}.
- *Reproducibility.* All RNGs are seeded (numpy PCG64; seeds in the scripts). The 27 g-prime lists (1.09 GB) were deleted
  after analysis; their SHA-256 are in `verify/data/PRIMES-MANIFEST.sha256`, and `run_main.sh` / `run_ta.sh` regenerate them
  (≈ 10 min). Kept: per-run bin counts (`*.i64`), metadata (`*.json`), statistics (`*.stats.json`), one-scale and drift files.

**4.2 Results** [computed; `verify/logs/aggregate.txt`, `data/aggregate.json`; ± = seed standard error]. X = 10⁸ for every row.

| system | sup [10³, X] | sup [10⁴, X] | sup [10⁶, X] | msL [10³, X] | msL [10⁶, X] |
|---|---|---|---|---|---|
| P_R (DZ 17.11), 5 seeds | 0.492 ± 0.012 | 0.509 ± 0.027 | 0.514 ± 0.054 | 0.519 ± 0.012 | 0.498 ± 0.086 |
| P_B (DZ 17.14), 5 seeds | 0.479 ± 0.020 | 0.457 ± 0.028 | 0.381 ± 0.060 | 0.522 ± 0.020 | 0.398 ± 0.091 |
| P_det (Γ, no selection) | 0.422 | 0.429 | 0.441 | 0.500 | 0.499 |
| T_0.90 (frontier), 5 seeds | 0.445 ± 0.019 | 0.440 ± 0.011 | 0.437 ± 0.046 | 0.485 ± 0.029 | 0.475 ± 0.073 |
| T_0.95 (frontier), 5 seeds | 0.497 ± 0.007 | 0.482 ± 0.015 | 0.497 ± 0.036 | 0.548 ± 0.012 | 0.541 ± 0.048 |
| T₁ (w_p = 1/(1 + log p)), 5 seeds | 0.928 ± 0.001 | 0.937 ± 0.001 | 0.945 ± 0.000 | 0.970 ± 0.001 | 0.975 ± 0.000 |
| ℙ (rational primes) | 0.000 | 0.000 | 0.000 | — | — |

Reading. (i) Both DZ templates sit on ½ over the full window: raw sup-slopes 0.48–0.49 (the predicted raw slope of
(x/log x)^{1/2} over [10³, 10⁸] is ½ − 1/(2 ln x) ≈ 0.46–0.48), and the log-corrected mean-square slope msL = 0.52 for both.
(ii) The top window [10⁶, 10⁸] for P_B gives 0.381 ± 0.060: per seed 0.50, 0.18, 0.31, 0.47, 0.45. Local two-decade slopes of
the block sup swing with sd 0.148 (P_R), 0.139 (P_B), 0.109 (T_0.95) over the 20 (seed, window) pairs, means 0.471, 0.479,
0.488 (`logs/local_slopes.log`); the low top-window seeds (s2, s3) are the ones whose normalized amplitude E/(x/log x)^{1/2}
falls over 10⁶–10⁸ (s3: −66 at 2·10⁵ to −28 at 10⁸). Finite-range slopes of these systems carry a ±0.14 systematic per
seed; no window, seed or estimator gives a value consistent with a smaller exponent across windows. (iii) ℙ gives 0 and
N(e) = ⌊e⌋ exactly; T_0.90 reproduces the frontier's α/2 = 0.45 (its writer: 0.457 ± 0.012), so the pipeline is calibrated
against the frontier's; T_0.95 sits between α/2 = 0.475 and Theorem A's 1/(3 − α) = 0.488 — the random surgery approaches
the DZ value ½ from below as α ↑ 1, as Theorem B says it must.

**4.3 The deterministic control P_det: the prime squares alone give β = ½** [proved here: lower bound; heuristic: constant].
P_det puts the j-th g-prime at the first grid point with F_R ≥ j, so π − F_R ∈ (−1, 0] and B(w) := Σ_q q^{−w} − ∫₁^∞ v^{−w}f_R dv
is analytic on Re w > 0. From log ζ_det(s) = Σ_{k≥1} k^{−1}Σ_q q^{−ks} and ∫ v^{−w}f_R = log(w/(w − 1)):
  ζ_det(s) = (s/(s − 1)) e^{B(s)} · [(2s/(2s − 1)) e^{B(2s)}]^{1/2} · Π_{k≥3} [(ks/(ks − 1)) e^{B(ks)}]^{1/k},
with every factor analytic and zero-free near s = ½ (B(ks) = O(1/k) makes the product converge) except (2s − 1)^{−1/2}: a branch point, so ζ_det is not analytic at ½ and, by
the Landau step of Prop. 2.4, N_det − ρx ≠ O(x^τ) for τ < ½. Its constant: (2s − 1)^{1/2}ζ_det(s) → H(½) = −exp(B(½) + ½B(1) +
Σ_q[−log(1 − q^{−1/2}) − q^{−1/2} − 1/(2q)]) = −0.7517 from the realized quantiles; the Selberg–Delange transfer
[heuristic] gives E_det(x) ≈ √(2/π)H(½)(x/log x)^{1/2} = −0.5998(x/log x)^{1/2}. Measured block means: −0.587 (10⁵), −0.595
(1.6·10⁶), −0.597 (6.3·10⁶), −0.597 (2.5·10⁷), −0.5995 (8.4·10⁷) (`verify/predict_det.py`, `data/ctl_det.predict.json`). So **the grid
construction has β ≥ ½ even with the randomness removed** (= ½ in the data; the upper bound is not proved here): the template prices Π (all prime powers) while the g-primes
count π, and the excess ½π(√x) of prime squares is a branch point at s = ½ with ζ_T(½) = −1 < 0. In the random system the
same factor (2s − 1)^{−1/2} multiplies e^{F₂(s)}, whose random part is unbounded as σ → ½+ (Prop. 2.4); Prop. 2.4 uses the latter,
Theorem 1 the block variance — neither needs the branch point, which is a third, independent reason for β ≥ ½ that is
not robust (a system whose g-primes target Π − ½Π(√·) − … instead of Π should not have it [heuristic]).

**4.4 Two diagnostics** [computed; heuristic reading]. (a) T₁ (deletion probability 1/(1 + log p), α_R = 1) has slopes
0.93–0.98: its mean system ζ(s)Π_p(1 − w_p p^{−s}) carries −ρ log(s − 1) at s = 1 itself (Σ_p w_p p^{−s} has derivative
≈ log(s − 1)), so E ≈ +c·x/log x and β(T₁) = 1. The Theorem-B lower bound ½ holds there but is not sharp; the DZ selection
has no such term because E[dπ_P] = f dv exactly. (b) `verify/drift_check.py` tests E(x) ≈ √(2/π)Ĥ(½ + 1/log x)(x/log x)^{1/2},
Ĥ(s) = (2s − 1)^{1/2}ζ_P(s) from each run's own primes: right sign and order for the high-density P_B seeds (correlation
0.89, 0.61, 0.96 for s1, s3, s4) but low by a factor 1.1–2.5, and uninformative for ρ < 0.6, where the random part
dominates. The random systems' amplitude is not captured by Ĥ alone; this is recorded, not used.

**4.5 What the finite rung says.** Every estimator on every random system of the DZ class sits on ½ over the full window,
with a ±0.14 per-seed systematic on two-decade windows; the one-scale variance is measured at its Theorem-B value with a
Gaussian conditional law (§3.3); the deterministic grid system sits on ½ with a predicted constant (§4.3). Nothing at
10⁸ points below ½. The rung is evidence; §2 is the proof.

## §5. Prior-art gate: is BDR fn. 4 settled after BDR?

**Searched (2026-10-01).** arXiv API: abs:Beurling AND abs:generalized (221 entries, `sources/arxiv-beurling-generalized-sorted.xml`)
and the phrases "generalized primes", "Beurling primes", "Beurling integers", "Beurling number", "generalized integers",
"g-primes" (`sources/arxiv-q-*.xml`); the generalized-number papers after 2023-09-01 are listed in
`sources/arxiv-generalized-numbers-2023-09-to-2026-10.txt` (2602.07690 Tranoy–Vindas, Wiener–Ikehara and Chebyshev bounds;
2511.13496 Oukil; 2507.13780 Broucke; 2409.10051 and 2407.12746, zero density; 2406.00736 Vindas, M(x) = o(x);
2401.06892; 2311.11127 Ruzsa, lacunarity). Semantic Scholar citers of 2309.01567 (`sources/s2-citations-BDR-2309.01567.json`):
2507.13780, 2407.12746, 2307.00239, 2209.01689. None of the abstracts concerns the integer exponent of the DZ/DMV/Zhang
random systems.

**The one candidate, read at the page.** Broucke 2507.13780 (`sources/broucke-2025-2507.13780v1.txt`) Thm 1.6 (l. 246–254)
generalizes DZ 17.14 to prescribed contours: "(1) N_P(x) = Ax + O_ε(x^{1/2+ε}) for some A > 0 and every ε > 0" — an upper
bound only — and discretizes with the Broucke–Vindas procedure (l. 1263–1273: Thm 5.1, "|π_P(x) − F(x)| ≤ 2", applied with
F = Π_c), not with DZ's independent selection. **BDR fn. 4 is not settled in print; Corollary 2 settles it for almost every
realization.**

**What print already has, so that the claim is not overstated.** BDR Cor. 3.3 (z-02 l. 668–679) gets β = ½ exactly by a
planted pole at s = ½ ("N_P(x) − ax ≪ x^{1/2−ε} cannot hold … as that would make … ζ_P analytic around 1/2"); Cor. 3.4 gets
[α, ½] for α < ½ from Hilberdink's max{α, β} ≥ ½; Remark 3.5(1) (l. 688–711) gets [1, β] for β₀ < β < 1 from DZ's system.
Hence a [1, ½]-system already follows from print by a case split (β₀ = ½: P_B; β₀ < ½: Remark 3.5(1) at β = ½). What was
open is the value β₀ of the DZ construction — the "sharpest in-print test of Conjecture U" (digest §F.2 item 4), since
β₀ < ½ would have refuted U at α = 1.

**Remark 5.1 (a by-product for BV-discretized systems)** [proved here, conditional]. Let P satisfy |π_P − Π_c| ≤ C with Π_c
the full prime-power template of ζ_c, as in BV, BDR and Broucke. Then B(w) = ∫v^{−w}d(π_P − Π_c) is analytic on Re w > 0 and,
as in §4.3, on real σ ↓ ½, ζ_P(σ) = ζ_c(σ)e^{B(σ)}[ζ_c(2σ)e^{B(2σ)}]^{1/2}Π_{k≥3}[ζ_c(kσ)e^{B(kσ)}]^{1/k} with ζ_c(2σ) ~ r/(2σ − 1).
If ζ_c is continuous and non-zero at s = ½ from the right (true for DZ's ζ_C by the |G − 1| ≤ 0.19·4^{−k} bound of Prop. 2.4;
for Broucke's ζ_c NOT checked at the page), then |ζ_P(σ)| → ∞, so β ≥ ½ by the Landau step: Broucke's Theorem 1.6 systems
would be [1, ½]-systems exactly. Labelled conditional; listed as Untried U-3.

## §6. Distance from upstream, Instruments row, Untried, waste line

**6.1 Distance from upstream (KICKSTART 10(n)).** Nearest published objects: the frontier's Theorem B (fr `NOTE.md` §4,
l. 215–236, as repaired by read-O F2) and DZ Thm 17.14 / 17.11 (book pp. 205, 208) with BDR fn. 4 (z-02 l. 165). Exactly new
here: (1) the one-scale bound moved from Bernoulli *thinning of ℙ* (the integers ℕ fixed, deletions random) to Bernoulli
*selection of the primes themselves* from a grid, where the density depends on the block; the dependence is carried exactly
by ρ = ρ^c e^{S} (Lemma 2.1), and the 0–1 law is replaced by anti-concentration alone (h(λ) → 0), giving the quantitative
Ω((x/log x)^{1/2}); (2) Corollary 2: β₀ = ½ for almost every DZ realization (P_B a [1, ½]-system), and α = β = ½ for P_R;
(3) Prop. 2.4, an independent proof by unboundedness of ζ_B at s = ½; (4) §4.3, the deterministic grid system has β ≥ ½ through
the prime-square branch point (= ½ in the data), with a predicted constant matched to 0.05 %; (5) Remark 5.1 (conditional). Not new: the
one-scale mechanism (read-O §4 A3's sketch), Berry–Esseen, Landau's Mellin step (BDR Cor. 3.3 uses it). Dual check: Theorem 1
and Prop. 2.4 are two proofs by different routes; the read-O slot of the standing dual read still applies.

**6.2 Instruments row** (shape of `directions/B2-refutation-program.md` "Instruments"; not inserted — this unit edits nothing
outside its folder):

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Integer-error exponent β of the Diamond–Zhang random systems (DZ book Thms 17.11, 17.14; BDR fn. 4 "Most likely the value of β₀ equals 1/2") | **PROVED a.s.: β(P_B) = β(P_R) = ½**, N − ρx = Ω((x/log x)^{1/2}) a.s. (Theorem 1; second proof Prop. 2.4; upper bound DZ (i)); α(P_B) = 1, α(P_R) = ½: P_B is a [1, ½]-system, on Conjecture U's line α = 2β. Finite rung X = 10⁸, 5 seeds per template: sup-slopes [10³, X] 0.492 ± 0.012 (P_R), 0.479 ± 0.020 (P_B), msL 0.519, 0.522; top window [10⁶, X] 0.514 ± 0.054, 0.381 ± 0.060 (per-seed two-decade systematic ±0.14); one-scale conditional variance / Theorem-B value 0.967–1.070 (8 cases), identity residual 0. Controls: ℙ 0.000 (N(e) = ⌊e⌋ exact); P_det (grid, no selection) E/(x/log x)^{1/2} = −0.5995 vs predicted −0.5998; T_0.90 0.440 ± 0.011, T_0.95 0.482 ± 0.015 (frontier family); T₁ (w_p = 1/(1 + log p)) 0.93 (β = 1, mean-system log-singularity at s = 1). Holds for almost every realization only; the exceptional null set is Untried U-1 | `results/dz-half-s39/NOTE.md` §0, §2, §3.3, §4.2; `results/dz-half-s39/verify/logs/aggregate.txt` | 2026-10-01 |

**6.3 Untried** (KICKSTART 10(m); fit reason; first rung):
- **U-1 The exceptional null set.** Does every subsequence of Γ satisfying DZ's (17.46) have β ≥ ½? This is Conjecture U at
  α = 1 inside DZ's class. Fit: S1 (discrete, Λ ≥ 0); a negative answer refutes U (read-O §4 preamble). First rung: a
  derandomized selection whose primes target Π_C − ½Π_C(√·) − … (no prime-square branch point) on [10³, 10⁸]: measure β.
- **U-2 The sharp order.** Is lim sup |E|/(x/log x)^{1/2} = ∞ a.s.? Heuristically the dyadic blocks add Var E(x) ≍
  x log log x/log x; the data show seed-dependent amplitudes 0.3–66. Fit: instrument. First rung: the block-variance sum
  against MS_j on the 10 runs on disk.
- **U-3 Remark 5.1 at the page.** Check that Broucke's ζ_c (2507.13780 §4–5) is continuous and non-zero at s = ½ from the right;
  then his Thm 1.6 systems are deterministic [1, ½]-systems. Fit: none (bookkeeping of print). First rung: §5.4, (5.3)–(5.9).
- **U-4 Natural boundary.** Is σ = ½ a natural boundary of ζ_B a.s. (Kahane-type theorem for Bernoulli-coefficient Dirichlet
  series, read at the page)? Fit: S2-adjacent (where a zero detector built on N must stop). First rung: the literature.
- **U-5 DMV's system.** Check (H1) for DMV's dΠ_C at the page; then DMV Thm 1's random system has β ∈ [½, θ] a.s.

**6.4 Waste line** (KICKSTART 10(o)). Spent for nothing: (a) the T₁ control (5 runs, ~1 min) — designed as "surgery at α = 1"
but its mean system carries log(s − 1) at s = 1, so β(T₁) = 1; label (ii) tool/design, re-queued as T_0.90/T_0.95 (done);
(b) a residue check through a 60M-point Irwin–Hall sum, killed at 5.5 min — the alternating sum cancels catastrophically for
n ≳ 20; label (ii) tool, replaced by the renewal equation; (c) the first arXiv query over http wrote no file; label (ii),
re-run over https. Found nothing, correctly: the prior-art search (no paper after BDR settles fn. 4).
