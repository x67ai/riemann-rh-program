# NOTE — unit `lemmaG-s39`: Lemma G (the exact missing lemma of Conjecture O) — deterministic irregular classes, the rung-1 test, and the exact residual class

Session 39, 2026-10-01. Agent: Opus 5.5 (default effort). Brief: `BRIEF.md`. Labels: **[proved here]**, **[computed]** (script + log
under `verify/`), **[quoted file:line]**, **[recalled, unverified]**, **[heuristic]**, **[novelty: single-check]**. Paths: `cO/` =
`results/conj-O-s38/`, `fr/` = `results/novel-wave-s37/beurling-frontier/`, `dg` = `results/novel-wave-s37/insights-digest.md`.
Notation as in cO/NOTE.md ll. 7–11: R ⊂ ℙ, Σ_{p∈R}1/p < ∞, α_R = lim sup log π_R(x)/log x, D_R(s) = Π_{p∈R}(1 − p^{−s}),
ζ_P = ζ·D_R, E = N_P − ρx, P_R(s) = Σ_{p∈R}p^{−s}, β₂(R) the mean-square exponent. L(s) := log D_R = −Σ_k P_R(ks)/k.

## §0. Summary and close (written at the close)

*The digest, quoted* (`results/novel-wave-s37/insights-digest.md`, SHA-256 e86f642a47cf4bde…). §B2 (l. 136): "B2 (the price of a zero;
the line). Under surgery on the rational primes a zero at Re s = α > ½ costs integer error at least x^{α/2} — proved for random and for
regular deletions, conjectured for every deletion — and RH is the endpoint β = 0 of the line α = 2β, not the β = 0 case of a threshold."
§F.2 item 2 (ll. 363–369): "2. U1 — Conjecture O by the Franel/Landau mean-square route, with a structured-R counterexample hunt …
Why second: its proof branch is RELATIVE — by Prop. 2.3 it cannot bear on ζ, whose own α_R is 0 — so only its refutation branch touches
the line α = 2β that contains RH; still the cheapest theorem-grade unit on the table." This unit is cO's next unit (a): "Lemma G for
one irregular deterministic class (e.g. hash-defined R: prove a natural boundary of P_R at α/2 …)" (cO/NOTE.md §4).

*Summary.* **Close G, with T-parts and a rung-1 counterexample** (stated as a theorem in §6). (1) *Ladder.* Finite R reproduced by a
third route (a dilation recursion, exact in rationals, §1.1). At the function-field rung the degree-wise Conjecture O is FALSE: deleting
M(a, N) irreducibles of each degree N from F_q[T] gives D_R = 1 − au and E ≡ 0 with α_R = log a/log q (Thm R1; brute force + exact
generating functions). That deletion satisfies every input of Theorem Z's proof except zero-freeness of D_R, so no proof of O or of
Lemma G can rest on those inputs alone; it must use the injectivity of the norm on ⟨R⟩ (§1.3). (2) *Over ℚ, unconditional.* The
singularities of P_R right of β₂ are exactly logarithmic germs with κ = Σμ(m)ord_{ms₀}D_R/m (Thm 2.1); any other singularity at Re s₀
forces β₂ ≥ Re s₀ (Cor. 2.2). This proves O on four deterministic classes irregular at scale x^{α_R/2}: primes near p^k (T2, via the
pole of 1/ζ(ks) at ρ₁/k), primes near n^k (T3, β₂ = α_R), modulated deletions — including deterministic R with a natural boundary of
P_R on σ = α_R/2 (T4) — and spread necklaces (T5, β₂ = α_R). Under RH a counterexample needs D_R analytic past β₂ with infinitely many
ZEROS and no poles (Prop. 2.3, sharpening cO Prop. 1.6). (3) *Over ℚ, RH.* Theorem F (Theorem Z with a model divided out) proves O for
every R whose D_R-zeros are carried by a polynomially controlled model, including the tight ℚ-necklace — the exact transplant of the
rung-1 counterexample, whose realization factor carries the prime diagonal. Every counterexample lies in the class 𝒞_self (§6), where
the diagonal method is provably silent; 𝒞_self over ℚ is the smallest class where the answer is unknown, with no member known.
(4) *Computation* (exact dyadic mean squares to 10¹⁰, five deterministic families and two controls, second routes throughout): no
K-candidate. The one sub-diagonal family, sq = {nextprime(p²)} (slope 0.422 on [10⁶, 10¹⁰]), carries a theorem (T2), and its E is the
sum over ζ's zeros at ρ/2 (200-zero explicit formula, correlation 0.998 for x ≥ 10⁸): a second calibration of the stop-line trigger
beside cO's κ. T3's Bessel law fits nsq with R² = 0.995 at the residue-fixed frequency; the planted-pole control is read at slope
0.906–0.940 against 0.90. (5) *Blocked route, named.* For hash-defined / pseudo-random R the natural-boundary route is blocked: every
natural-boundary theorem read at the page needs gaps, shift structure, independence, or a constant local factor. The missing input for
the Weyl family is a bilinear equidistribution estimate for {pθ} at scale p^{α−1}.

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

## §2. Over ℚ: the local structure of P_R left of the product, the criterion, and the sharpened anatomy

**2.1 Theorem (local structure; unconditional)** [proved here; novelty: single-check]. Let R be any deletion; β₂ := β₂(R) ≤ α_R
(|E(x)| ≤ Q_R(x) + xΣ_{m∈⟨R⟩, m>x}1/m ≪ x^{α_R+ε}). Then:
(a) D_R = ζ_P/ζ is meromorphic on {σ > β₂}. For w there put n(w) := ord_w D_R ∈ ℤ. Then n(w) = 0 if Re w > α_R, and n(w) < 0
only at zeros of ζ, with n(w) ≥ −ord_w ζ.
(b) For Re s₀ > β₂ the sum κ(s₀) := Σ_{m≥1}μ(m)n(ms₀)/m is finite, and P_R continues analytically along every path in {σ > β₂}
avoiding the discrete set Σ_R := {w/m : n(w) ≠ 0, m ≥ 1}; near s₀ every branch is P_R(s) = −κ(s₀)log(s − s₀) + h(s), h analytic at s₀.
(c) Hence κ(s₀) = n(s₀) ∈ ℤ if Re s₀ > α_R/2; κ(s₀) = n(s₀) − n(2s₀)/2 ∈ ½ℤ if Re s₀ = α_R/2; κ(s₀) ∈ (1/L)ℤ, L = lcm{m ≤ α_R/Re s₀},
if β₂ < Re s₀ < α_R/2.
*Proof.* (a) On σ > β₂, ζ_P(s) = ρs/(s − 1) + s∫_1^∞E(x)x^{−s−1}dx is analytic except for the simple pole at 1 (cO Prop. 1.3(i)); ζ is
meromorphic with a simple pole at 1, so D_R = ζ_P/ζ is meromorphic with D_R(1) = ρ ≠ 0. For Re w > α_R the product converges
absolutely and is ≠ 0. Where ζ(w) ≠ 0, w ≠ 1, D_R is analytic; so poles sit at zeros of ζ, of order ≤ ord_w ζ. (b) For σ > α_R,
L(s) = −Σ_k P_R(ks)/k gives, by Möbius inversion, P_R(s) = −Σ_m μ(m)m^{−1}L(ms). L = log D_R continues along paths avoiding the zeros
and poles of D_R. On a compact K ⊂ {σ > β₂} the terms with m > (α_R + 2)/min_K σ have Re(ms) > α_R + 2 and are O(2^{−m·min_K σ})
uniformly, so the series defines the continuation along every admissible path; Σ_R ∩ K is finite (w/m ∈ K with n(w) ≠ 0 forces
Re w ≤ α_R, so m ≤ α_R/min_K σ, and D_R has finitely many zeros and poles in the compact mK). Near s₀, D_R(w) = (w − ms₀)^{n(ms₀)}g_m(w)
with g_m analytic and nonzero at ms₀, so L(ms) = n(ms₀)log(s − s₀) + (analytic), and summing gives (b). (c): for m ≥ 2 and
Re s₀ > α_R/2, Re(ms₀) > α_R, so n(ms₀) = 0; at Re s₀ = α_R/2 only m = 2 survives besides m = 1 (μ(2) = −1). ∎
**2.2 Corollary (the criterion; unconditional).** β₂(R) ≥ Re s₀ for every point s₀ at which P_R (continued from σ > α_R along some
path) has a singularity NOT of the form −κ log(s − s₀) + analytic with κ in the set 2.1(c) allows. In particular:
(i) a natural boundary of P_R on σ = σ_b gives β₂ ≥ σ_b (= cO Prop. 1.6(i));
(ii) a pole, an essential singularity, an algebraic branch point or a non-isolated singularity at Re s₀ = σ₀ gives β₂ ≥ σ₀;
(iii) a logarithmic singularity with κ ∉ ℤ at Re s₀ > α_R/2 gives β₂ ≥ Re s₀; at Re s₀ = α_R/2, κ + n(2s₀)/2 ∉ ℤ gives β₂ ≥ α_R/2;
(iv) a logarithmic singularity with κ ∈ ℤ, κ < 0 at Re s₀ > α_R/2 with ord_{s₀}ζ < −κ (e.g. ζ(s₀) ≠ 0) gives β₂ ≥ Re s₀ (D_R would
have a pole of order −κ at s₀, which (a) forbids right of β₂).
*Proof.* If β₂ < Re s₀, Theorem 2.1 applies at s₀, and in (i) on a neighbourhood of a whole segment of the line. ∎
*What it buys.* For a concrete R, Conjecture O (even β₂ ≥ σ₀ > α_R/2) reduces to exhibiting ONE forbidden singularity of P_R at
Re s₀ ≥ α_R/2. It sharpens cO Prop. 1.6(i) from "no natural boundary" to an exact list of the admissible local germs.
**2.3 Proposition (the anatomy sharpened; RH)** [proved here]. Assume RH, α_R < ½, and β₂(R) < α_R/2. Then (a) D_R is ANALYTIC on
σ > β₂ (its poles could only sit at zeros of ζ, which lie on σ = ½ > α_R, where n = 0), with |D_R(s)| ≪_δ |t|^{O(1)} on σ ≥ β₂ + δ,
|t| ≥ 1 (cO Theorem Z steps Z1, Z3); (b) for every τ₀ ∈ (β₂, α_R/2), D_R has infinitely many ZEROS in τ₀ < σ ≤ α_R. *Proof of (b).*
If only finitely many, take T₀ above them: L = log D_R is analytic on U = {σ > τ₀, |t| > T₀} with Re L ≤ O(log|t|), so |L| ≪ log|t|
on {σ ≥ τ₀ + η} (Lemma Z.a), and P_R = −Σ_m μ(m)L(ms)/m is analytic on U (ms ∈ U for s ∈ U) with |P_R| ≪ log|t|: Theorem Z's hypothesis,
so β₂ ≥ α_R/2, a contradiction. ∎ This replaces cO Prop. 1.6(ii)'s "zeros or poles" by "zeros, no poles" (α_R < ½); rung 1 (§1.3(b))
realizes exactly this anatomy.

## §3. Deterministic irregular classes on which O is a theorem (the T-parts)

Gap inputs used below, all [recalled, unverified; standard]: Ingham 1937, p_{n+1} − p_n ≪ p_n^{5/8+ε}; Huxley 1972, π(y + y^{7/12+ε}) − π(y)
≍ y^{7/12+ε}/log y; the first nontrivial zero ρ₁ = ½ + 14.1347…i is simple and ζ has no zero in {0 < σ < 1, 0 < |t| < 14.13}.

**3.1 Theorem T2 (prime-power mimics; unconditional)** [proved here; novelty: single-check]. Let k ≥ 2, θ′ := 5/8 + ε, and for each
prime p ≥ p₀ let r_p be a prime in [p^k, p^k + p^{kθ′}] (it exists by Ingham; the intervals are disjoint for p ≥ p₀). Put R_k := {r_p}.
Then α_R = 1/k, and **β₂(R_k) ≥ 1/(2k) = α_R/2.** Under RH, D_R has a pole at every ρ/k (all on σ = α_R/2) and P_R has logarithmic
branch points there: P_R neither continues past α_R/2 off the axis nor has a natural boundary on σ = α_R/2.
*Proof.* |r_p^{−s} − p^{−ks}| = |s∫_{p^k}^{r_p}u^{−s−1}du| ≤ |s|p^{kθ′}p^{−k(σ+1)}, summable over p iff σ > σ_C := 1/k − 1 + θ′, and
σ_C < 1/(2k) because θ′ < 1 − 1/(2k). So C(s) := Π_{p≥p₀}(1 − r_p^{−s})/(1 − p^{−ks}) converges absolutely on σ > σ_C (analytic,
zero-free), and D_R(s) = C(s)·Π_{p<p₀}(1 − p^{−ks})^{−1}·ζ(ks)^{−1}. At s₀ := ρ₁/k: Re s₀ = 1/(2k) > σ_C, 0 < Im s₀ = γ₁/k < γ₁, so
ζ(s₀) ≠ 0, while 1/ζ(ks) has a simple pole at s₀ and the other factors are finite and ≠ 0: D_R has a pole at s₀. If β₂ < Re s₀,
Theorem 2.1(a) would force ζ(s₀) = 0. Hence β₂ ≥ 1/(2k). π_R(x) = π(x^{1/k}) + O(1) gives α_R = 1/k. ∎
*Why the class matters.* π_R(x) − li(x^{1/k}) = Ω_±(x^{1/(2k)}(log x)^{−1}log log log x) (Littlewood) [recalled]: R_k is irregular at
scale x^{α_R/2}, outside Cor. Z.1 and outside cO Lemma G's decomposition clause (any M with π_R = M + O(x^θ), θ < α_R/2, carries the
branch points of P(ks) at ρ/k). Under RH ζ_P/ζ = D_R has infinitely many POLES of real part α_R/2: the anatomy of cO Prop. 1.6
(necessary for a counterexample) holds, and O holds anyway — the anatomy is not sufficient. If RH is false with a zero ρ, Re ρ = Θ > ½,
and ζ(ρ/k) ≠ 0, the pole at ρ/k gives β₂(R_k) ≥ Θ/k > α_R/2: these deterministic deletions see an off-line zero directly.
*Nearest published object:* the squarefree-number error Q(x) − 6x/π², whose Ω-results come from the poles of 1/ζ(2s) at ρ/2
(Evelyn–Linfoot; Montgomery–Vaughan 1981) [recalled, unverified]. Difference: the "squares" are replaced by single primes r_p ≈ p^k,
which makes the object a deletion of primes (Conjecture O's class) with α_R = 1/k.

**3.2 Theorem T3 (a pole of P_R at α_R; unconditional)** [proved here]. Let k ≥ 3, r_n a prime in [n^k, n^k + n^{kθ′}] (n ≥ n₀; distinct,
as (n+1)^k − n^k ≫ n^{k−1} > n^{kθ′}), R := {r_n}. Then α_R = 1/k and **β₂(R) = α_R** (the maximum; β₂ ≤ α_R always).
*Proof.* As in 3.1, P_R(s) = ζ(ks) − Σ_{n<n₀}n^{−ks} + H(s) with H analytic on σ > θ′ − 1 + 1/k (< 1/k): P_R has a simple pole at
s = 1/k = α_R, which Corollary 2.2(ii) forbids right of β₂. ∎ For k = 2 (r_n = nextprime(n²)) the same holds as long as the r_n are
distinct (Legendre's conjecture; checked for n ≤ 3·10⁵ in the run, 0 collisions). *Predicted law* [heuristic: Mellin inversion around the
essential singularity exp(−(1/k)/(s − 1/k)) of D_R]: E(x) ≈ A·x^{1/k}(log x)^{−3/4}cos(2√(log x/k) + φ) — for k = 2 a frequency
√(2 log x) in √log x, with no free parameter. Tested in §4.

**3.3 Theorem T4 (modulated deletions; a deterministic natural boundary at α_R/2; unconditional)** [proved here; novelty: single-check].
Let 0 < α < 1, c > 0, F_c(x) = Σ_{p≤x}min(1, cp^{α−1}), and T = F_c + G with G(x) = x^{α/2}Σ_j a_j cos(γ_j log x), where (γ_j) is an
enumeration of the positive rationals by height and a_j = ε·2^{−j}/(1 + γ_j) (ε small). The greedy set R ("delete p iff #R∩[2, p) < T(p)")
has |π_R − T| ≤ 1 for large x (T increases by ≤ 1 between consecutive primes there). Then α_R = α and **P_R has a natural boundary on
σ = α/2; so β₂(R) ≥ α/2.** More generally, for any R with π_R = F_c + G + O(x^θ), θ < α/2: if Ĝ(s) := ∫u^{−s}dG(u) has at some s₀,
Re s₀ ≥ α/2, a singularity forbidden by Corollary 2.2, then β₂ ≥ Re s₀; if Ĝ continues with finite order past α/2 off the axis, then
β₂ ≥ α/2 under RH (the proof of Cor. Z.1 verbatim).
*Proof.* P_R(s) = cP(s + 1 − α) + (entire) + Σ_j (a_j/2)(s_j/(s − s_j) + s̄_j/(s − s̄_j)) + H(s), s_j := α/2 + iγ_j, H analytic on σ > 0
(partial summation, |π_R − T| ≤ 1); the j-series converges on σ > α/2 (Σa_j|s_j| < ∞), and near each s_j the term cP(s + 1 − α)
(argument w = 1 − α/2 + iγ_j, Re w ∈ (½, 1)) is analytic or has at most a logarithmic singularity (at a zero of ζ), which cannot cancel a
pole. At s = s_j + δ, δ ↓ 0, the j-th term is a_js_j/(2δ) → ∞ while the
others are bounded by Σ_{i≠j}a_i|s_i|/|γ_i − γ_j| ≤ Σ_i a_i|s_i|q_iq_j < ∞ (q = denominators; |γ_i − γ_j| ≥ 1/(q_iq_j)). So every s_j is a
singularity, and {s_j} is dense on σ = α/2. Corollary 2.2(i)–(ii). ∎ (One planted j already gives β₂ ≥ α/2; the density is what makes
the brief's natural-boundary shape (ii) true for a deterministic R.)

**3.4 The rung-1 counterexample transplanted to ℚ: necklace deletions.** a = 2, λ = log 4, c_N := M(2, N) (§1.2). Over ℚ the
frequency N log q cannot carry c_N primes, so the cluster must be realized by distinct primes near 4^N. Two transplants, both α_R = ½:
R_tight = the first c_N primes after 4^N (they lie in [4^N, 4^N + 4^{(7/12+ε)N}] for large N, Huxley); R_spr = {nextprime(4^N + j⌊4^N/c_N⌋) :
0 ≤ j < c_N} (distinct for large N: 4^N/c_N ≈ N2^N exceeds the Ingham gap 4^{(5/8+ε)N}).
*Theorem T5 (spread necklace; unconditional)* [proved here]. **β₂(R_spr) = α_R = ½.** *Proof.* |r^{−s} − (4^N(1 + j/c_N))^{−s}| ≤
|s|(4^{(5/8+ε)N} + c_N)4^{−N(σ+1)}, so summing the c_N terms of each N, P_R(s) = Σ_N 4^{−Ns}Σ_{j<c_N}(1 + j/c_N)^{−s} + (analytic on
σ > 1/8 + ε). Euler–Maclaurin: Σ_{j<c}(1 + j/c)^{−s} = cΦ(s) + ½(1 − 2^{−s}) + O(|s|²/c), Φ(s) := ∫_1^2v^{−s}dv. So
P_R(s) = Φ(s)𝒩(s) + (analytic near s = ½), 𝒩(s) := Σ_N c_N4^{−Ns} = −Σ_m (μ(m)/m)log(1 − 2·4^{−ms}), whose m = 1 term is
−log(s − ½) + analytic near ½ (the m ≥ 2 terms are analytic there). Hence near s₀ = ½ = α_R, P_R = −Φ(s)log(s − ½) + analytic: the
coefficient Φ(½) = 2(√2 − 1) = 0.828… is not an integer (and the germ is not even of the form κ·log + analytic), which Corollary 2.2
forbids at Re s₀ = α_R > α_R/2. So β₂ ≥ ½ = α_R ≥ β₂. ∎ [Predicted: D_R ≈ (s − ½)^{0.828}B(s), E ≈ C·x^{1/2}(log x)^{−1.83}, M ≈
X(log X)^{−3.66}: local mean-square slope ≈ 1 − 3.66/ln X = 0.82 at 10⁹ — §4.]
*The tight necklace is the exact transplant.* On σ > 1/12 + ε, D_R(R_tight) = (1 − 2·4^{−s})·C(s) with
C(s) := Π_{N,j}(1 − r_{N,j}^{−s})/(1 − 4^{−Ns}) absolutely convergent (Σ_N c_N·4^{(7/12+ε)N}·4^{−N(σ+1)} < ∞), analytic and zero-free
(the cyclotomic identity Π_N(1 − 4^{−Ns})^{c_N} = 1 − 2·4^{−s} is §1.2's with u = 4^{−s}). So D_R continues analytically past α_R/2 = ¼
with infinitely many simple zeros at ½ + 2πik/log 4, no poles; P_R has logarithmic branch points with the coefficients 2.1(c) allows
(κ = 1 on σ = ½, κ = −½ on σ = ¼): exactly rung 1's anatomy (§1.3(b)), and Corollary 2.2 is silent. What separates it from rung 1 is
the factor C, whose logarithm carries the coefficient −1 at every log r (r ∈ R) — the prime diagonal. That is what the next theorem uses.

**3.5 Theorem F (model factorization; RH)** [proved here; novelty: single-check]. Let α_R < ½, τ₀ < α_R/2, T₀ ≥ 1, and suppose D_R
continues analytically to Ω := {σ > τ₀, |t| > T₀} and factors there as D_R = G·C with:
(F1) C analytic and zero-free on Ω ∪ {σ > α_R}; log C (the branch → 0 as σ → +∞) equals, for σ > σ₁, an absolutely convergent
Σ_λ b_λe^{−λs} with frequencies λ ≥ λ₀ > 0 separated by |λ − λ′| ≥ e^{−K max(λ,λ′)};
(F2) G analytic on Ω, G → 1 as σ → +∞ uniformly in t, |G| ≤ C₀|t|^A on Ω, and polynomial minimum modulus on circles: for every centre
z₀ = α_R + 2 + it₀ (|t₀| large) and radius ρ₁ ≤ α_R + 2 − τ₀ there is ρ′ ∈ [ρ₁ − η, ρ₁] with log|G| ≥ −A log|t₀| on |s − z₀| = ρ′ (η > 0 fixed);
(F3) for every σ < α_R/2: Σ_{λ≤log N}|b_λ|²e^{−2σλ} ≥ N^{δ₀(σ)} for infinitely many N, some δ₀(σ) > 0.
**Then β₂(R) ≥ α_R/2.** (Theorem Z is the case G ≡ 1, where (F3) is Σ_{p∈R}p^{−2σ} = ∞.)
*Proof.* Theorem Z's proof (cO §1.4) with L replaced by log C. Suppose β₂ < α_R/2 and fix τ, δ, σ* as there with τ > max(β₂, τ₀),
η < δ/4. (Z1), (Z3) are unchanged: |D_R| ≪ |t|^{O(1)} on σ ≥ τ + δ/2 (this is where RH enters). On the circles of (F2),
log|C| = log|D_R| − log|G| ≤ O(log|t₀|); Lemma Z.a needs Re g ≤ M only on the boundary circle, so (Z4) gives |log C| ≪ log|t| on
σ ≥ τ + δ. (Z5) runs with A_N(s) := Σ_λ b_λe^{−λs}e^{−e^λ/N} and N := T^{1/(K+1)}: the Mellin–Barnes shift uses only analyticity and
the log bound of log C, and the Montgomery–Vaughan inequality (G.27) holds for any distinct reals; the separation keeps its error term
below the diagonal, as in cO §1.7. Result: Σ_{λ≤log N}|b_λ|²e^{−2σ*λ} ≪ (log N)², contradicting (F3). ∎
*Corollary F.1 (RH): β₂(R_tight) ≥ α_R/2.* G := 1 − 2·4^{−s}: periodic in t with simple zeros on σ = ½ only, |G| ≤ 3 on σ ≥ 0, and a
radius ρ′ ∈ [ρ₁ − η, ρ₁] keeping the circle at distance ≥ η/10 from the zeros exists (the zeros are 2π/log 4 ≈ 4.5 apart), so (F2)
holds with a constant lower bound. (F1): log C has frequencies k log r (r ∈ R) and n log 4, distinct (r^k ≠ 4^n) and separated by
≥ 1/(2e^λ); absolutely convergent for σ > ½. (F3): b = −1 at every log r, r ∈ R, so the diagonal is ≥ Σ_{r∈R, r≤N}r^{−2σ}
≥ N^{½ − 2σ − ε} infinitely often. ∎ So the faithful transplant of the rung-1 counterexample obeys O (under RH): the realization factor
C — the gap between log r and N log 4 — carries the full prime diagonal.

**3.6 Lemma (cluster lemma; unconditional, elementary)** [proved here]. If (y, y + h] (integers) contains c primes of R, all > z, and
ρ_z := Π_{p∈R, p≤z}(1 − 1/p), then E(y + h) − E(y) ≤ (ρ_z − ρ)h + 2^{π_R(z)} − c; so max(|E(y)|, |E(y+h)|) ≥ J/2 with
J := c − 2^{π_R(z)} − (ρ_z − ρ)h. *Proof.* E(y+h) − E(y) = #{R-free n ∈ I} − ρh, and #{R-free n ∈ I} ≤ #{n ∈ I : (n, Π_{p∈R,p≤z}p) = 1} − c
≤ ρ_z h + 2^{π_R(z)} − c (Legendre). ∎ For R_tight (computed, `verify/cluster_check.py` → `logs/cluster_check.log`, N ≤ 16): the cluster
spans h_N with h_N/(c_N log 4^N) = 0.98, 1.05, 0.99, 1.00, 1.00 (N = 12…16); the guaranteed jump J_N ≈ 0.8c_N (N = 16: J = 3273 for
c_N = 4080); the measured max|E| next to the cluster is 1.9c_N (7781). So |E| ≍ x^{1/2}/log x at x = 4^N: β(R_tight) = α_R on the
computed range — as long as the clusters stay this tight (h_N ≪ c_N log 4^N), sup|E| ≥ x^{α_R}/(C log x) infinitely often.

## §4. Computation at scale (the instrument; evidence, not theorems)

**4.1 Instrument and second routes** [computed]. `verify/lg.c` + `lg_core.h` build each family's R, ρ (long double; tails analytic:
1/ζ(k)-type, N₁/(N₁+1), mean tails, cyclotomic), the R-free bitset to X, and bins in the format of cO's `thin2.c` (its statistics code
unchanged; an optional side file of per-bin sums of E); the truncated Franel diagonal M_diag = ρ²W/12 by depth-first enumeration of
squarefree R-numbers. The exact dyadic statistic is cO's (`dyadic_ms_cO.py`, a verbatim copy of cO/verify/dyadic_ms.py), driven by
`verify/dyadic.py`. Second routes: (i) `xcheck_small.py`, `xcheck_planted.py` (X = 10⁵): every R regenerated in Python is identical; every
bin's Σ E² recomputed with N(n) = Σ_{m∈⟨R⟩, m≤n}μ(m)⌊n/m⌋ — inclusion–exclusion, not the sieve — agrees to print precision (≤ 5·10⁻⁷);
ρ(sq), ρ(nsq) by independent products agree to 3·10⁻¹², 3·10⁻¹⁵. (ii) `controls.py` runs this pipeline on cO's own greedy data and
reproduces cO §3.4's row exactly (0.577 / 0.594 / 0.598, κ = 2.80). (iii) The family-specific predictions below are independent routes
to the same numbers. Runs (`run_all.sh`, `run_big.sh`; logs `run_all.log`, `run_big.log`): 10⁹ and 10¹⁰, 1–140 s each, one at a time.

**4.2 Results at X = 10¹⁰** (`logs/dyadic_1e10.log`, `logs/controls.log`; 10⁹ in `logs/dyadic_1e9.log` — same values on the common range).
| family (theorem) | Q_R slope | ms-slope [10⁴,X] / [10⁶,X] / top 3 dec. | sup-slope | M/M_diag at 10⁴, 10⁶, 8·10⁷, 10⁹ | κ |
|---|---|---|---|---|---|
| sq = {nextprime(p²)} (T2: β₂ ≥ ¼ uncond.) | 0.499 | 0.431 / 0.422 / 0.431 | 0.231 | 1.06, 0.91, 0.81, 0.32 | 1.41 |
| nsq = {nextprime(n²)} (T3: β₂ = ½) | 0.635* | 0.511 / 0.438 / 0.485 | 0.279 | 19.9, 35.9, 11.7, 6.55 | 3.69 |
| Weyl {p : {p√2} < p^{−0.4}} (none; pseudo-random) | 0.604 | 0.478 / 0.745 / 0.552 | 0.266 | 36.4, 0.83, 10.5, 9.87 | −2.88 |
| Weyl {p : {p√2} < p^{−0.25}} (none) | 0.749 | 0.687 / 0.650 / 0.546 | 0.352 | 2.05, 2.16, 4.93, 1.36 | 1.72 |
| tight ℚ-necklace (F.1: β₂ ≥ ¼ under RH) | 0.500 | 0.801 / 0.792 / 0.789 | 0.479 | 16.3, 46.1, 165, 371 | −5.23 |
| spread ℚ-necklace (T5: β₂ = ½) | 0.492 | 0.770 / 0.869 / 0.885 | 0.341 | 2.41, 1.56, 6.90, 20.7 | −6.78 |
| planted pole 0.45 ± 5i, α = 0.6 (RH-false-type control) | 0.600 | 0.906 / 0.913 / 0.940 | 0.428 | 13.4, 63.4, 174, 489 | −5.58 |
| T_0.75 seeds 1–4 (Theorem B control; fr data) | 0.750 | 0.69–0.76 / 0.77–0.93 / 0.76–1.04 | 0.34–0.39 | 1.8–116 (all ≥ 1.7) | −2.9…−0.1 |
| greedy c = 1, α = 0.75 (fr Thm C; cO data) | 0.750 | 0.577 / 0.594 / 0.598 | 0.308 | 0.73, 0.22, 0.12, 0.073 | 2.80 |
(*nsq's R-number count grows like X^{1/2}e^{c√log X}, since Π(1 + n^{−2s}) ≈ exp ζ(2s): its local exponent is 0.635, not ½.)

**4.3 Pattern discovery and the family-specific second routes.**
(a) *sq is driven by the zeros of ζ, at the line α_R/2* [computed: `verify/sq_explicit.py` → `logs/sq_explicit_200.log`]. Under RH,
Mellin inversion of ζ(s)C(s)/ζ(2s)·x^s/s gives E(x) = Σ_ρ c_ρx^{ρ/2} + O(x^{0.03}), c_ρ = ζ(ρ/2)C(ρ/2)/(ρζ′(ρ)) (|c_{ρ₁}| = 0.0364,
|c_{ρ₂}| = 0.0210, |c_{ρ₅}| = 0.0256), with C(ρ/2) from the 9592 R-primes of the run. Each bin's mean of E against the exact bin average
of the 200-zero sum, normalized by x^{1/4}: correlation 0.882 on all 120 bins with x ≥ 10⁴, **0.980 for x ≥ 10⁶ and 0.998 for x ≥ 10⁸**
(residual rms 0.0093 against a signal rms 0.069). So the pure-power deficit of sq (slope 0.422 on [10⁶, 10¹⁰]; M/M_diag = 0.32 in the
10⁹ window) is a log-periodic beat of the low zeros (frequencies (γ − γ′)/2 in log X), not a log-power and not a counterexample:
β₂ ≥ ¼ is Theorem T2.
(b) *nsq follows Theorem T3's law with the residue-fixed frequency* [computed: `verify/nsq_bessel.py` → `logs/nsq_bessel.log`]. Fitting
E/x^{1/2} = K₁f₁(L) + K₂f₁′(L), f₁(L) = J₁(w√(2L))/√L, L = ln x, to the 120 bin means (10⁴ ≤ x ≤ 10¹⁰): R² = 0.9952 at the predicted
w = 1, against 0.9927 (w = 1.05), 0.9869 (0.95), 0.975 (0.9), 0.979 (1.1), 0.950 (1.2, 1.3) — best at the prediction. The data span less
than one period of the Bessel oscillation, so this is supportive, not decisive. E/x^{1/2} falls from −0.10 (10⁴) through 0 near 10⁹ —
why the mean-square slope on [10⁶, 10¹⁰] (0.438) understates β₂ = ½ = α_R.
(c) *The rung-1 transplant is the worst deletion on the record.* The tight ℚ-necklace — whose D_R has exactly rung 1's analytic
anatomy (§3.4) — has M/M_diag = 371 at 10⁹ and sup-slope 0.479 ≈ α_R: coherent clusters (§3.6). Spreading the clusters turns its zeros
into branch points (T5): slope 0.885 against T5's (log X)^{−3.66} law, whose local slope 1 − 3.66/ln X is 0.80–0.84 over the window
(consistent up to O(1/log X) corrections).
(d) *Controls.* The planted pole at σ₁ = 0.45 > α/2 = 0.3 is read off at slope 0.906 / 0.913 / 0.940 against 2σ₁ = 0.90; the Weyl
(pseudo-random) sets scatter around α like the T_α seeds (M/M_diag 0.83–36 vs 1.8–116); greedy c = 1 reproduces cO.
(e) *The stop-line trigger.* "Pure-power mean-square slope below α_R − δ over ≥ 3 decades" fires for sq (δ ≈ 0.08) and greedy c = 1
(δ ≈ 0.16) — both sets on which β₂ ≥ α_R/2 is an UNCONDITIONAL theorem (T2; fr Thm C). cO's κ-calibration answers the greedy case
(a log-power); the sq case needs a second calibration — log-periodic modulation by zeros (here of ζ itself, at ρ/2) — which a κ-fit
reads as κ = 1.41. **No family is a K-candidate**: every sub-diagonal window is explained by a proved mechanism.

## §5. Prior-art gate (standing orders 1, 7) and distance-from-upstream lines (10(n))

Read at the line (files in `sources/` unless prefixed fr/ or cO/):
- **Hilberdink 2005** (fr `sources/w-18a…txt` ll. 222–258): Theorem A (zero order of log ζ_P for σ > max(α, β)), Remark B(ii) ("if … ζ_P(s)
  has finitely many zeros here, then … zero order in this range"), and Carlson's mean value under the separation (3.1). Our §2.3 is its
  relative form: a counterexample to O needs infinitely many zeros of D_R; Theorem F is Carlson applied after dividing by a model G.
- **Diamond–Montgomery–Vorhauer 2006** (fr `sources/p1-02…txt` ll. 183–200): a Beurling system with N_B well behaved and ζ_B with infinitely
  many zeros on σ = 1 − a/log t — RH-type failure with regular integers in the CONTINUOUS-density world. Relevant to U, not to O's
  relative form; our deletions are discrete subsets of ℙ.
- **Broucke–Vindas 2024** (fr `sources/z-18…txt` ll. 34–45, 97–111): the DMV–Zhang discrete random approximation (Thm 1.1) and Thm 1.2:
  for any F ≪ x/log x a generalized-prime system with |π_P − F| ≤ 2 and Σ_{p_j≤x}p_j^{−it} − ∫u^{−it}dF ≪ √x + √(x log(|t|+1)/log x).
  Nearest object to the Weyl (pseudo-random) family; difference: BV choose real g-primes by a random construction and PROVE square-root
  discrepancy in every frequency; our Weyl sets are explicit subsets of ℙ with no proved discrepancy (that is the missing input of §6(c)).
  "Zhang" enters here (BV's ref. [15], the DMVZ method); DZ's book (`sources/dz-2016-book.txt`, 14,436 lines) has no function-field example.
- **Avdeeva 2015** (cO `sources/avdeeva…txt` ll. 117–135, Thm 1): if the semigroup ⟨B⟩ has count AN^α + O(N^β), β < α < 1, 2 ∉ B, the
  shift-averaged variance of B-free counts in intervals of length N is ∼ CN^α — the stationary square-root law. It applies to sq
  (Π(1 − r_p^{−s})^{−1} = ζ(2s)·(analytic on σ > 0.03): count A√N + O(N^β)), not to nsq (count √N·e^{c√log N}), not to the necklaces
  (log-periodic count), not to the Weyl sets (x^α/log x): it never reaches the single interval [0, x] of Conjecture O.
- **Fabry gap theorem and Pólya's refinement** (`sources/wiki-fabry-gap-theorem.txt`, quoting Fabry 1896/1899, Pólya 1929, Erdős 1945):
  exponents of density D = lim sup k/n_k = 0 give a natural boundary; every arc longer than 2πD carries a singularity. The Dirichlet-series
  form (Pólya) [recalled, unverified] needs frequencies λ_k with positive gaps and finite density; {log p : p ∈ R} has gaps → 0 and
  counting function ≍ e^{α_Rλ}/λ (density ∞): the theorem is void for P_R.
- **Breuer–Simon 2011** (`sources/breuer-simon-…txt` ll. 180–260, 618–700): Szegő's theorem (finitely-valued coefficients ⇒ natural
  boundary unless eventually periodic, Thm 5.1), Steinhaus/Paley–Zygmund/Kahane random series (Thm 6.1: independent, non-degenerate
  coefficients ⇒ strong natural boundary a.s.), ergodic nondeterministic coefficients (Thm 1.7). All are POWER series: the proofs use
  "right limits", i.e. the shift structure of the exponent set ℕ. The frequency set {log p} has no shift structure.
- **Estermann 1928 / Dahlquist 1952** via Bhowmik–Schlage-Puchta (`sources/bhowmik-…txt` ll. 30–60): Π_p W(p^{−s}) with the SAME local
  factor W at every prime is either a finite product of ζ(νs)^{c_ν} or has σ = 0 as natural boundary. D_R has local factor 1 − x on R and
  1 off R — outside their scope; our T2 is an Estermann-type transplant (W = 1 − x^k moved onto primes r_p ≈ p^k), landing in the
  finite-product case (1/ζ(ks)).
- Searches (`sources/arxiv-q1…q6.xml`): q3 found arXiv 2606.24536 (zeta-regularization on the natural boundary of the prime zeta
  function; not about thin sets); q4–q6 (Beurling + function field; generalized primes + necklace; Euler product + thin set): 0 hits.
  Under zoo V.5 a null search is not evidence of novelty.

**Distance-from-upstream lines.** Thm 2.1/Cor. 2.2 ↔ Landau–Walfisz's structure of P(s) = Σμ(m)m^{−1}log ζ(ms) (singularities at ρ/m, 1/m)
[recalled] and cO Prop. 1.6(i); difference: for an arbitrary thin R, relative to β₂, with the exact list of admissible germs (integer /
half-integer / 1/L coefficients). Thm R1 ↔ the cyclotomic identity [recalled] and fr §5.4's virtual curve; difference: a deletion inside
F_q[T] (O's own class) that is exactly regular. T2 ↔ squarefree-number Ω-results and Estermann's finite-product case; difference: primes
near p^k, a deletion with α_R = 1/k. T3 ↔ none found (a deletion whose P_R has a pole at α_R; its Bessel law in √log x). T4 ↔ Hadamard /
Breuer–Simon natural boundaries by planted singularities; difference: planted in a prime count through a greedy deletion. T5, F, F.1 ↔
Hilberdink 2005 Thm 1 / cO Theorem Z (F is Z with a model G divided out); the ℚ-necklaces ↔ none (transplants of R1). Lemma 3.6 ↔ Legendre.

## §6. Close — G, with T-parts and a rung-1 counterexample

**Theorem (the close).** (T, unconditional) For every deletion R, the singularities of P_R right of β₂(R) are exactly the germs
−κ log(s − s₀) + analytic, κ = Σ_m μ(m)ord_{ms₀}D_R/m (Thm 2.1); every other singularity at Re s₀ forces β₂ ≥ Re s₀ (Cor. 2.2). Hence
Conjecture O holds unconditionally on four deterministic classes, each irregular at scale x^{α_R/2} and outside Cor. Z.1: prime-power
mimics (T2, β₂ ≥ α_R/2), primes next to k-th powers (T3, β₂ = α_R), modulated deletions with a forbidden Mellin singularity —
including deterministic R whose P_R has a NATURAL BOUNDARY on σ = α_R/2 (T4) — and spread necklaces (T5, β₂ = α_R).
(T, RH) Theorem F: O holds whenever, past α_R/2, D_R = G·C with C zero-free carrying a divergent diagonal and G polynomially controlled
in size and in minimum modulus on circles; in particular for the tight ℚ-necklace, the exact transplant of the rung-1 counterexample.
(G) At rung 1 (F_q[T], RH true) Lemma G and the degree-wise Conjecture O are FALSE (Thm R1: E ≡ 0, α_R = log a/log q), and the
counterexample satisfies every input of Theorem Z's proof except zero-freeness of D_R. Define, over ℚ, 𝒞_self := {R : for some
τ₀ < α_R/2, D_R continues to {σ > τ₀, |t| > T₀} with polynomial growth and infinitely many zeros, and NO factorization D_R = G·C with
(F1)–(F2) has a divergent diagonal (F3)}. Then: **(RH, α_R < ½) every counterexample to Conjecture O lies in 𝒞_self** (Prop. 2.3 +
Theorem F); **the proof class "Carlson–Montgomery–Vaughan diagonal on log(D_R/G)" — Theorem Z, Theorem F — cannot yield Lemma G on
𝒞_self, because there, by definition, every admissible G leaves log(D_R/G) with a convergent diagonal; and the class is not vacuous in
the axioms that method consumes: its F_q[T] analogue contains the necklace deletion, which violates O.** A proof must use the
injectivity of the norm on ⟨R⟩ (§1.3(d)). **Smallest class where the answer is unknown: 𝒞_self over ℚ.** No member is known; every
construction of a D_R with infinitely many zeros past α_R/2 on the record (the ℚ-necklaces) is covered by T5 or Theorem F.
*The brief's T-shape, corrected.* "P_R continues past α_R/2 off the axis, or has a natural boundary at α_R/2" is not a dichotomy for
deterministic R: R_k (T2) and the tight ℚ-necklace have neither — P_R has logarithmic branch points on or beyond σ = α_R/2 — and O holds
for both. The right shape is Corollary 2.2's list plus Theorem F.
*Stop lines (the brief's).* No printed theorem decides Lemma G on these classes (§5). No K-candidate: every sub-diagonal window
(sq, slope 0.422 on [10⁶, 10¹⁰]; greedy c = 1) lies on a set where O is an unconditional theorem (§4.3(e)). **The natural-boundary
route for hash-defined / pseudo-random R IS blocked, by a named missing input:** a natural-boundary (or single forbidden-singularity)
theorem for Σ_{p∈R}p^{−s} with 1_R a deterministic pseudo-random selection. Every natural-boundary theorem read at the page needs one of
(a) gaps and finite frequency density (Fabry–Pólya; {log p} has gaps → 0 and infinite density), (b) the shift structure of ℕ (Szegő,
Breuer–Simon right limits), (c) independence (Steinhaus–Paley–Zygmund–Kahane; Theorem B), (d) one local factor at every prime
(Estermann–Dahlquist). For the Weyl family the concrete missing input is a pair-correlation (bilinear) equidistribution estimate for
{pθ} over primes p ∈ (x/2, x] at the scale p^{α−1}, i.e. with frequencies h up to p^{1−α} — the input that turns Theorem B's one-scale
argument deterministic (cf. Broucke–Vindas 2024, Thm 1.2, which builds such square-root discrepancy for random real g-primes).

**Instruments rows** (column shape of `directions/B2-refutation-program.md` "Instruments": Quantity | Current best value | Result file |
Dated; records, never ranks):
| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Conjecture O at the function-field rung (degree-wise; F_q[T], RH true) | FALSE: necklace deletion (M(a, N) irreducibles of degree N) has E ≡ 0 with α_R = log a/log q; brute force F_3[T] deg ≤ 8, generating functions deg ≤ 60; regular (round(a^N/N)) and random rung-1 deletions at |E(n)| ≍ a^{n/2}n^{−3/2} and ≍ a^{n/2} | `results/lemmaG-s39/NOTE.md` §1.2–1.3; `verify/logs/rung1_ff.log` | 2026-10-01 |
| Deterministic deletions with O (β₂ ≥ α_R/2) a theorem beyond Cor. Z.1 | unconditional: R_k = primes near p^k (β₂ ≥ 1/(2k)); primes near n^k, k ≥ 3 (β₂ = α_R); planted natural boundary at α/2; spread ℚ-necklace (β₂ = α_R). RH: every model-factorizable D_R (Theorem F), incl. the tight ℚ-necklace | `results/lemmaG-s39/NOTE.md` §3, §6 | 2026-10-01 |
| Exact dyadic mean square of deterministic deletions at X = 10¹⁰ | sq = {nextprime(p²)}: slope 0.422 on [10⁶, 10¹⁰] on a PROVED set, explained by ζ's zeros (200-zero explicit formula, corr 0.998 for x ≥ 10⁸); nsq: Bessel law R² 0.995; tight / spread necklaces 0.79 / 0.885; planted-pole control 0.906–0.940 vs 2σ₁ = 0.90 | `results/lemmaG-s39/NOTE.md` §4; `verify/logs/dyadic_1e10.log`, `sq_explicit_200.log`, `nsq_bessel.log` | 2026-10-01 |

**Untried entries** (KICKSTART 10(m): fit reason + first ladder rung):
- **UT-L1 The ℚ-limit of the rung-1 counterexample.** A continuous family between rung 1 and ℚ: Beurling necklaces with c_N g-primes in
  [e^{Nλ}, e^{Nλ}(1 + η_N)] inside the ambient ℙ ∪ (those g-primes), deleted again — find the threshold spread η_N at which O switches on
  (Theorem F needs Σ_N c_N η_N e^{−Nλσ} < ∞ for some σ < θ/2; at η_N = 0 O fails). Fit: S1 (the input is exactly norm-injectivity, the
  property §1.3(d) isolates). First rung: R1 itself (η = 0), then η_N = e^{−κN} for a ladder of κ, computed exactly with this unit's `lg.c`.
- **UT-L2 Pair-correlation input for pseudo-random deletions.** Prove M(X) ≫ X^{α}/log X for the Weyl set {p : {p√2} < p^{α−1}} from a
  bilinear equidistribution estimate for {pθ} at scale p^{α−1} (the named missing input of §6). Fit: S2 (a single planted defect — the
  §4 planted pole — is visible to the statistic; the estimate would make the visibility deterministic). First rung: F_q[T] with irreducibles
  selected by a hash of their coefficient vector (pair correlations computable exactly), then ℚ at α = 0.75.
- **UT-L3 Membership test for 𝒞_self.** Given R, search for a model G with (F1)–(F2) and divergent diagonal, or certify none: e.g. test
  whether D_R(s)·Π_ρ(1 − s/ρ)^{−1} over its computed zeros has bounded log-diagonal. Fit: S1, S5 (it must survive the rung-1 necklace, the
  method's named no-go). First rung: rung 1 (answer known: the necklace is in the F_q[T]-analogue of 𝒞_self), then the tight ℚ-necklace
  (answer known: not in 𝒞_self).
- **UT-L4 The stop-line trigger, recalibrated twice.** Restate cO's K-trigger with both calibrations found so far — log-powers (κ; greedy)
  and zero-driven log-periodic beats (sq; explicit formula) — and test it on sq to 10¹⁴ through the explicit formula alone (no sieve).
  Fit: bookkeeping for B2's refutation instruments (no S1–S5 content). First rung: sq at 10¹⁰ (on disk), where the beat is measured.
- **UT-L5 T3's Bessel law across a full period.** nsq to 10¹¹ (the next zero crossing of J₁(√(2 ln x)) is near 5·10¹⁰): a quantitative
  instrument for "pole of P_R at α_R ⇒ essential singularity of D_R". Fit: S2-type visibility calibration. First rung: k = 3 to 10¹⁰.

*Recalled inputs* (load-bearing, not read at the page here): Ingham's gap bound and Huxley's short-interval PNT (T2–T5 spreads; BHP 0.525
would also do), the first zero of ζ and its simplicity (T2), Littlewood's Ω± (only for "irregular at scale x^{α_R/2}", not for any
theorem), Stirling and the RH bounds for ζ, 1/ζ (as in cO §4, via Theorem Z/F), the cyclotomic identity (re-derived in §1.2's proof).
Quoted at the line: Hilberdink 2005, DMV 2006, Broucke–Vindas 2024, Avdeeva 2015, Breuer–Simon 2011, Bhowmik–Schlage-Puchta 2010, the
Fabry/Pólya statements (§5).
*Waste line (10(o)).* Spent for nothing: the first two launches of `verify/rung1_ff.py` (a (1 − u^N)^{r_N} product looped r_N ≈ 10¹⁶ times;
a Python loop over 1.4·10⁹ irreducibles to sample the random deletion) — label (ii), tool/time: replaced by the binomial expansion and
binomial sampling, ≈ 15 min lost; three arXiv queries returned 503/empty on the first attempt (network, retried). Nothing else: every
run fed a section ("found nothing, correctly" for K: no candidate, with a proved reason for each sub-diagonal window).
