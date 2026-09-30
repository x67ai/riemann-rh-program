# NOTE — unit `dz-half-s39`: Diamond–Zhang's random Beurling systems have β = ½ almost surely

**Writer:** Opus 5.5 (subagent of Session 39), 2026-10-01. Brief: `BRIEF.md`. Record read at the line: frontier
`read-O.md` §4 A3 and §7(a); frontier `NOTE.md` §4 Theorem B (as repaired by read-O F2); digest
`novel-wave-s37/insights-digest.md` §F.2 item 4 (U5a); Diamond–Zhang book (AMS Surv. 213, 2016) ch. 17 at the page
(`sources/t-50-diamond-zhang-2016-book.txt`, extracted from `fetched-r2/t-50-…-BOOK.pdf`); BDR z-02 p. 3 fn. 4.
Labels: [proved here], [quoted, file:line], [recalled, unverified], [computed], [heuristic].

## §0. Close

(written last)

## §1. The objects, read at the page

**1.1 The construction** [quoted, `sources/t-50-diamond-zhang-2016-book.txt`; book pp. 196–202]. A template density f ≥ 0 on
[1, ∞); an increasing sequence 1 = v₀ < v₁ < … → ∞; p_k := ∫_{v_{k−1}}^{v_k} f(v) dv (Lemma 17.5, "satisfies 0 < p_k ≤ 1 for
k ≥ k₀"); X_k independent with P[X_k = 1] = p_k, P[X_k = 0] = 1 − p_k (proof of Lemma 17.2, book p. 197); the g-primes are
the v_k with X_k = 1. DZ take the grid (17.13), book p. 201: "v₀ = 1 and v_k = n + ℓ/2ⁿ, for k = 2ⁿ + ℓ, n = 0, 1, 2, …,
1 ≤ ℓ < 2ⁿ". As printed the index set {2ⁿ + ℓ : 1 ≤ ℓ < 2ⁿ} omits k = 1, 2, 4, 8, …; the grid meant is
Γ := {1} ∪ {n + ℓ/2ⁿ : n ≥ 1, 0 ≤ ℓ < 2ⁿ} (Remark 17.6's "closed under addition and multiplication" needs the integers,
e.g. 1.5 + 1.5 = 3). Nothing below depends on the reading: the proof uses only independence, p_k = ∫_{cell} f, and
max{p_k : v_k ∈ (x/2, x]} → 0; on Γ that maximum is ≤ 2^{−⌊x/2⌋}.

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
  (on DZ's Γ: m(x) ≤ 2^{1−⌊x/2⌋} and the mesh is ≤ ½).
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
Σ_{k∈B} p_k(1 − p_k)c_k². There is a G-measurable x₁ < ∞ such that for x ≥ x₁
  σ² ≥ c_* κ² x / (2^{11}(N₀ + 1)² log x).
*Proof.* Put φ(y) := n₀(y) − κy on [1, 2). n₀ is constant on at most N₀ + 1 intervals of [1, 2), and on each φ is linear
with slope −κ, so {y : |φ(y)| < θ} meets each in an interval of length ≤ 2θ/κ. With θ := κ/(4(N₀ + 1)) the exceptional set
has measure ≤ ½; its complement J ⊂ [1, 2) has |J| ≥ ½ and at most 2(N₀ + 1) components. For v ≥ 2,
0 ≤ −log(1 − 1/v) − 1/v ≤ 1/v², so |c_k − φ(x/v_k)| ≤ κx/v_k² ≤ 4κ/x ≤ θ/2 once x ≥ 32(N₀ + 1); then |c_k| ≥ θ/2 whenever
x/v_k ∈ J. With J_x := {v ∈ (x/2, x] : x/v ∈ J} (≤ 2(N₀ + 1) intervals) and m(x) ≤ ½:
  σ² ≥ (θ²/8) Σ_{k∈B, x/v_k∈J} p_k ≥ (θ²/8)(∫_{J_x} f − (4N₀ + 6)m(x)),
since only cells straddling an endpoint of J_x are miscounted. By (H1) and v = x/y, dv = x dy/y²:
∫_{J_x} f ≥ (c_*/log x)·x∫_J dy/y² ≥ c_* x/(8 log x). For x large (G-measurably) the m(x) term is below half of this, so
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
because of the bound in 3.2.

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

(§3 continues)

## §4. Finite rung: simulation of the construction to 10⁸, five seeds, with controls

**4.1 Method** [computed; code in `verify/`, logs in `verify/logs/`, per-run data in `verify/data/`].
- *The construction, exactly.* `dzgen.py` draws every cell of Γ with its own Bernoulli(p_k) for the units n ≤ 22 (p_k by
  8-point Gauss–Legendre; max p_k = 0.4506, the cell (1, 1.5]). Above, a Poisson process with intensity f, each point
  rounded up to its grid point: its law differs from the exact Bernoulli selection by at most Σ_k p_k² ≤ 2⁻²² in total
  variation, over the whole range. f_C is the printed (17.44) (k = 1, 2 active below 10⁸; k = 3 needs log v ≥ 64); every
  proposal checks f ≤ envelope ((1 + c)f_R with c = 0.8366, i.e. (17.45)); the largest ratio met was < 1.
- *The density.* log ρ = Σ_{p≤X} −log(1 − 1/p) − Ein(log X) − 2Σ_k ∫_{log X}^∞ a_k(t)cos(γ_k t)dt + S_tail, from
  log ρ = log r_T + ∫₁^∞ v^{−1}(dΠ_P − f dv) and ∫₁^X f_R/v = Ein(log X), with r_T = Π_k|G(4^k(1 − ρ_k))|² for f_C
  (a_k(t) = g(e^{t/4^k})4^{−k}e^{−t/4^k}; residue identity log|G(4(1 − ρ₁))|² = −2∫₀^∞a₁cos(γ₁t)dt checked, §4.5).
  S_tail — the g-primes above X, which move ρ but not N(x ≤ X) — is sampled as N(1/(2X log X), 1/(X log X)): at X = 10⁸ its
  sd is 2.3·10⁻⁵, i.e. an uncertainty of ρ·x·2.3·10⁻⁵ in ρx, comparable to (x/log x)^{1/2} only at x ≈ X. This is the
  dependence of E(x) on primes beyond x, sampled in law rather than ignored.
- *The counting.* `dzcount.c` enumerates every g-integer ≤ 10⁸ (DFS over non-decreasing prime indices; up to 4.7·10⁸ per run)
  into the bins (e_i, e_{i+1}], e = 2^j(1 + i/1024); N(e) = 1 + cumulative count is exact at every edge (control: rational
  primes give N(e) = ⌊e⌋ at all 27 125 edges ≤ 10⁸, `logs/ctl_primes_exact.log`). E is sampled at the edges only (1024 per dyadic block).
- *Estimators* (`analyze.py`, as the frontier's `fit.py`): per block j, A_j = max|E|, the running sup M_j, the dyadic mean
  square MS_j; slopes on windows [10^a, 10⁸], a = 3, …, 6: "sup" (log M vs log x), "supL" (log(M·(log x)^{1/2})), "ms"
  (½ slope of log MS), "msL" (½ slope of log(MS·log x)). The L-versions test the one-scale prediction |E| ≍ (x/log x)^{1/2}.

(§4 continues)

## §5. Prior-art gate: is BDR fn. 4 settled after BDR?

(pending)

## §6. Distance from upstream, Instruments row, Untried, waste line

(pending)
