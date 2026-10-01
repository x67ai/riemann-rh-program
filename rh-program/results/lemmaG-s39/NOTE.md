# NOTE — unit `lemmaG-s39`: Lemma G (the exact missing lemma of Conjecture O) — deterministic irregular classes, the rung-1 test, and the exact residual class

Session 39, 2026-10-01. Agent: Opus 5.5 (default effort). Brief: `BRIEF.md`. Labels: **[proved here]**, **[computed]** (script + log
under `verify/`), **[quoted file:line]**, **[recalled, unverified]**, **[heuristic]**, **[novelty: single-check]**. Paths: `cO/` =
`results/conj-O-s38/`, `fr/` = `results/novel-wave-s37/beurling-frontier/`, `dg` = `results/novel-wave-s37/insights-digest.md`.
Notation as in cO/NOTE.md ll. 7–11: R ⊂ ℙ, Σ_{p∈R}1/p < ∞, α_R = lim sup log π_R(x)/log x, D_R(s) = Π_{p∈R}(1 − p^{−s}),
ζ_P = ζ·D_R, E = N_P − ρx, P_R(s) = Σ_{p∈R}p^{−s}, β₂(R) the mean-square exponent. L(s) := log D_R = −Σ_k P_R(ks)/k.

## §0. Summary and close (written at the close)

(pending)

## §1. The ladder (standing order 10(b)): finite R, then the function-field rung — where Conjecture O is FALSE

**1.1 Rung 1a — finite R, by a third route (the dilation recursion)** [proved here; computed: `verify/rung1_finite.py` →
`verify/logs/rung1_finite.log`]. *Lemma 1.1.* Let R be finite, Q = Π_{p∈R}p, MS(R) := (1/Q)∫_0^Q E_R², and q ∉ R prime. Then
(i) E_{R∪{q}}(x) = E_R(x) − E_R(x/q) (fr Thm B step (2)); (ii) (1/(Qq))∫_0^{Qq}E_R(x)E_R(x/q)dx = MS(R)/q; hence (iii)
MS(R ∪ {q}) = 2(1 − 1/q)MS(R), and from MS(∅) = ∫_0^1({x} − ½)²dx = 1/12, MS(R) = ρ2^{|R|}/12 (= fr Prop. 5.1 = cO Prop. 1.1(a)).
*Proof of (ii).* Substituting x = qy, the left side is (1/Q)∫_0^Q E_R(qy)E_R(y)dy. With the additive expansion E_R(y) = Σ_ξ c(ξ)e(ξy),
c(a/b) = ρμ(b)b/(2πi·a·φ(b)) (cO Prop. 1.1(a), b | Q, (a, b) = 1), the frequency qξ = (qa)/b is again reduced ((q, b) = 1), and
c(qa/b) = c(a/b)/q: the coefficients are homogeneous of degree −1 in the numerator. So the integral is Σ_ξ c(ξ)·conj(c(qξ)) =
(1/q)Σ_ξ|c(ξ)|² = MS(R)/q (Parseval). (iii): MS(R∪{q}) = (1/(Qq))∫_0^{Qq}(E_R(x) − E_R(x/q))² = MS + MS − 2MS/q. ∎
This route uses only the homogeneity c(qξ) = c(ξ)/q — not Franel's integral (fr 5.1) and not the full Parseval sum (cO 1.1).
*Computed:* the one-period mean square in exact rationals (piecewise-linear integration, not Fourier) equals ρ2^{|R|}/12 for 12 sets
(from ∅ to {2, 3, 5, 7, 11}; e.g. MS{3, 7, 11} = 80/231), and the cross term (ii) equals MS/q exactly for 6 pairs (R, q), e.g.
⟨E_{3,5}, E_{3,5}(·/7)⟩ = 8/315 = (8/45)/7. **Rung 1a reproduced by a third route: ALL EXACT.**

**1.2 Rung 1b — the function-field rung: the degree-wise Conjecture O fails, by a necklace deletion.**
Setting (the program's rung-1 convention, fr §5.4: degree-wise counts, since over ℝ the norms q^n are discrete): ambient = the monic
irreducibles of F_q[T]; |P| = q^{deg P}; for a set R of irreducibles, N_P(n) := #{monic f of degree n with no factor in R}, ρ_R :=
Π_{P∈R}(1 − |P|^{−1}), E_R(n) := N_P(n) − ρ_R q^n, α_R := lim sup log π_R(x)/log x (π_R(q^n) = #{P ∈ R : deg P ≤ n}). The ambient
itself has N(n) = q^n exactly (E ≡ 0) and satisfies RH (Weil). M(a, N) := (1/N)Σ_{d|N}μ(N/d)a^d (necklace numbers; M(q, N) = the
number of monic irreducibles of degree N; x ↦ M(x, N) is increasing on integers x ≥ 1).
*Theorem R1 (rung-1 counterexample to O)* [proved here; computed; novelty: single-check]. Let 2 ≤ a < q be integers and R any set of
monic irreducibles containing exactly M(a, N) of degree N for every N ≥ 1. Then Σ_{P∈R}|P|^{−1} < ∞, α_R = log a/log q, and
N_P(n) = q^n − a·q^{n−1}, ρ_R = 1 − a/q, **E_R(n) = 0 for every n ≥ 1.** So β = −∞ < α_R/2: the degree-wise analog of Conjecture O
is false at rung 1, although the ambient satisfies RH.
*Proof.* The cyclotomic identity 1 − au = Π_{N≥1}(1 − u^N)^{M(a,N)} in ℤ[[u]] (logarithms: −Σ_n a^n u^n/n = −Σ_n (u^n/n)Σ_{N|n}N·M(a, N),
and Σ_{N|n}N·M(a, N) = a^n is Möbius inversion). The R-free monic polynomials have generating function
Π_{P∉R}(1 − u^{deg P})^{−1} = (1 − qu)^{−1}Π_{P∈R}(1 − u^{deg P}) = (1 − au)/(1 − qu), so N_P(n) = q^n − aq^{n−1}; at u = 1/q (absolute
convergence, a < q) the identity gives ρ_R = 1 − a/q. Σ_{P∈R}|P|^{−1} = Σ_N M(a, N)q^{−N} ≤ Σ_N (a/q)^N < ∞; π_R(q^n) = Σ_{N≤n}M(a, N)
≍ a^n/n. ∎
*Computed* (`verify/rung1_ff.py` → `verify/logs/rung1_ff.log`): (A) brute force in F_3[T] with a = 2 — the 3, 3, 8, 18, 48, 116, 312, 810
irreducibles of degrees 1–8 found by sieving, the first M(2, N) = 2, 1, 2, 3, 6, 9, 18, 30 of each degree deleted, the R-free monic
polynomials counted directly: N_P(n) = 1, 3, 9, 27, 81, 243, 729, 2187 = 3^{n−1} for n = 1…8, all equal to q^n − aq^{n−1}. (B) exact
generating functions to degree 60: D_R(u) = 1 − 2u exactly (coefficients d₂ = … = d₁₂ = 0); ρ_R = 1/3; E(n) = 0 to the 80-digit
precision of the ρ product. Controls on the same rung: the *regular* deletion r_N = round(2^N/N) has |E(n)|·n^{3/2}/2^{n/2} oscillating
between −0.37 and +0.26 for n = 20…60 — |E(n)| ≍ a^{n/2}n^{−3/2}, the rung-1 face of fr Theorem C (c = 1): round(a^N/N) − M(a, N) ≈
a^{N/2}/N for even N makes D_R ≈ (1 − au)(1 − au²)^{1/2}, a square-root branch point at |u| = a^{−1/2}; the *random* deletion (each
irreducible of degree N independently with probability a^N/(N·M(q, N)), seed 20261001) has E(n)/2^{n/2} = −0.14 … 0.46 for n = 6…22 —
the rung-1 face of fr Theorem B. **Rung 1b: regular and random deletions sit at α_R/2; the necklace deletion is exactly regular.**

**1.3 What rung 1b says about Lemma G and about any proof of O** [proved here; novelty: single-check].
Write u = q^{−s}, so σ = Re s and |u| = q^{−σ}; α_R = log a/log q.
(a) *Lemma G is false at rung 1.* For the necklace deletion β = −∞ < α_R/2, but P_R(u) := Σ_{P∈R}u^{deg P} = Σ_N M(a, N)u^N =
−Σ_{m≥1}(μ(m)/m)log(1 − au^m) has logarithmic branch points at u^m = 1/a, i.e. at s = α_R/m + 2πik/(m log q), k ∈ ℤ, for every
squarefree m — on σ = α_R/2 at every height πk/log q (m = 2). So P_R continues past α_R/2 off the real axis in no half-plane
{σ > τ₀, |t| > T₀}, τ₀ < α_R/2, single-valuedly: the hypothesis of Theorem Z fails and its conclusion fails too.
(b) *The anatomy of cO Prop. 1.6 is realized, in a world satisfying RH.* D_R = ζ_P/ζ_amb = 1 − au has infinitely many zeros, at
s = α_R + 2πik/log q (real part α_R > α_R/2 − ε for every ε), and no poles; the branch points of P_R are the images ρ′/m of these zeros
with the rational coefficients the local structure theorem (§2.1 below) requires (−1 at the zeros, ½ at their halves).
(c) *Which inputs of Theorem Z's proof hold for the necklace deletion.* The Euler product over R; |D_R(s)| ≤ 1 + a for σ ≥ 0 and
|ζ_P| ≤ C|t| trivially (steps Z1, Z3 — polynomial bounds); nonnegative integer multiplicities; Σ|P|^{−1} < ∞; α_R > 0; MV spacing of
the frequencies N log q; RH for the ambient. What fails is ZERO-FREENESS of D_R, i.e. analyticity of L = log D_R (step Z2), hence
Borel–Carathéodory (Z4). Theorem Z itself transfers to rung 1 verbatim (zero-free D_R with the continuation ⟹ β₂ ≥ α_R/2), and the
regular and random rung-1 deletions of §1.2 obey O.
(d) *The ℚ-input any proof must use.* Over ℚ the Dirichlet coefficients of D_R are μ(m)·1_{⟨R⟩}(m): one coefficient ±1 per
squarefree R-number, at pairwise distinct frequencies log m (unique factorization in ℤ; the norm is injective on ⟨R⟩). At rung 1 the
degree-n coefficient of D_R is the aggregate Σ_{f∈⟨R⟩, deg f = n}μ(f) over all squarefree R-products of norm qⁿ, and the necklace
choice makes every aggregate with n ≥ 2 vanish. *Statement (G₁).* Conjecture O (and Lemma G) is not a consequence of the properties
listed in (c) — they hold at rung 1, where O fails; a proof must use the injectivity of the norm on ⟨R⟩, equivalently that the
coefficient sequence of D_R is ±1 on a set of counting exponent α_R with no cancellation between distinct R-numbers.
*Nearest published object.* The cyclotomic (necklace) identity 1 − au = Π_N(1 − u^N)^{M(a,N)} is classical (Metropolis–Rota;
Moreau 1872) [recalled, unverified]; the rung-1 dictionary "RH-true curve with perfectly regular divisor counts" is fr §5.4's virtual
curve V (a whole system over 5^ℤ). Difference: here a DELETION from the exact system F_q[T] (Weil-RH ambient, a genuine function
field), with α_R > 0 prescribed, is exactly regular — a statement about Conjecture O's own class, which V is not.

