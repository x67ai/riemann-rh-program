# NOTE — unit `free-greedy-s40/theory`: S8, the free greedy system — identities, mechanism, proof problem

Session 40, started 2026-10-01 11:25 IST. Writer: Opus 5.5 (agent). Labels as in the charter §4: **[proved here]**, **[computed]**
(script + log in `verify/`), **[quoted]** (source at page/line, in `sources/` or the named folder), **[recalled, unverified]** (never
load-bearing), **[novelty: single-check]**. Notation: S8(ρ) as in `../CHARTER.md` §1; t := 1/ρ; T(x) = ρ(x − 1) + 1; N, π = π_P, C =
composites, E = N − T, D = −E, V(x) = ρ(x − 1) − C(x); counting functions are right-continuous (count ≤ x).

## §0. Close (filled last)

(pending)

## §1. The exact identities (task 1)

**1.0 Construction (well-definedness)** [proved here]. Let p₀ := 1. Given p₁ < … < p_k, let G_k be the multiset of finite products of
p₁, …, p_k (G₀ = {1}), N_k(x) := #(G_k ∩ [1, x]) with multiplicity, D_k(x) := T(x) − N_k(x), and p_{k+1} := inf{x ≥ p_k : D_k(x) ≥ ½}.
Claims, by induction on k: (i) p_{k+1} < ∞ and D_k(p_{k+1}) = D_k(p_{k+1}−) = ½, so no element of G_k sits at p_{k+1}; (ii) N(x) = N_k(x)
for x < p_{k+1}, where N counts the full multiset G = ∪G_k, and N(p_{k+1}) = N_k(p_{k+1}) + 1, so D(p_{k+1}) = −½; (iii) p_{k+1} ≥ p_k + t.
*Proof.* (i) N_k(x) ≤ Π_{i≤k}(1 + log x/log p_i) is polynomial in log x, so D_k(x) → ∞; D_k is right-continuous, rises with slope ρ
between jumps and jumps only downward; D_k(p_k) = −½ by (ii) at the previous step (D₀(1) = 0). So the set in the definition is
nonempty, its infimum x* has D_k(x*) ≥ ½ by right-continuity, D_k < ½ on [p_k, x*), hence D_k(x*−) ≤ ½, and having no upward jumps
D_k(x*) ≤ D_k(x*−). So both equal ½ and D_k does not jump at x*. (ii) An element of G \ G_k contains some p_j, j > k, so it is p_{k+1}
itself or ≥ min(p_{k+2}, p₁p_{k+1}) > p_{k+1}. (iii) On [p_k, x), D_k(x) ≤ −½ + ρ(x − p_k) < ½ while x < p_k + t. ∎
So p_k → ∞, N(x) < ∞ for every x, and the sweep of the charter is exactly this recursion (the tie rule — a composite at a deficit time
is counted first — is the infimum convention: a jump at x* makes D_k(x*) < ½).

**Lemma 1.1 (one-sided bound)** [proved here]. For all x ≥ 1: E(x) > −½, and E(x−) ≥ −½, with E(x−) = −½ only at a g-prime or at a
tie (an element of G at a point where D reaches ½). *Proof.* On [1, p₁) and on each [p_k, p_{k+1}), D = D_k < ½ by the definition of
p_{k+1} as an infimum (and D(p_k) = −½). So D < ½ everywhere and E = −D > −½. Left limits are limits of values. If D(x−) = ½ with
x ≠ p_{k+1}, then D(x) < ½ forces a jump at x. ∎

**Lemma 1.2 (spacing and lattice)** [proved here]. p_{k+1} − p_k ≥ t, and p_{k+1} = 1 + (n_{k+1} − ½)t with n_{k+1} := N(p_{k+1}−) ∈
ℤ_{≥1}, n_k strictly increasing. *Proof.* Spacing is 1.0(iii). D_k(p_{k+1}) = ½ reads ρ(p_{k+1} − 1) + 1 − N_k(p_{k+1}) = ½, and
N_k(p_{k+1}) = N(p_{k+1}−) by 1.0(i)–(ii). ∎ (So p₁ = 1 + t/2: 1.6366 for ρ = π/4, as in the prototype.)

**Lemma 1.3 (free monoid)** [proved here, given that t is transcendental]. If t is transcendental: (i) distinct multisets of g-primes
have distinct products; (ii) no composite lies on L := {1 + (m − ½)t : m ∈ ℤ}, so ties never occur. *Proof.* p_k = f_k(t) with
f_k(X) := 1 + (n_k − ½)X ∈ ℚ[X] of degree 1 (n_k − ½ ≠ 0), irreducible, constant term 1; distinct k give distinct linear coefficients,
so the f_k are pairwise non-associate primes of the UFD ℚ[X]. A product Π f_k^{e_k} has constant term 1, and by unique factorization
it determines (e_k). Evaluation at a transcendental t is injective on ℚ[X], giving (i). A composite is Π f_k^{e_k}(t) with Σe_k ≥ 2, a
polynomial of degree ≥ 2, never equal as a polynomial to 1 + (m − ½)X; injectivity again gives (ii). ∎
Scope: ρ = π/4 has t = 4/π, transcendental by Lindemann's theorem [recalled, unverified]; for ρ = e/π, t = π/e is not known to be
irrational [recalled, unverified], so 1.3 is not available there. Nothing below outside 1.4 uses 1.3: Theorem 1.6 holds for every ρ.

**Lemma 1.4 (reflection identity)** [proved here]. Assume no ties (true for transcendental t by 1.3(ii)). Let M(x) := sup_{1≤y≤x} V(y)
(V is càdlàg, so the sup is attained as a value V(y*) or a left limit V(y*−)). Then π(x) = ⌊M(x) + ½⌋ (the max(0, ·) of the charter is
redundant, since M ≥ V(1) = 0) and E(x) = M(x) − V(x) + r(x) with r(x) := ⌊M(x) + ½⌋ − M(x) ∈ (−½, ½].
*Proof.* N = 1 + π + C gives E = π − V identically. Take x ∈ [p_k, p_{k+1}), so π(x) = k. For y ≤ x: V(y) = π(y) − E(y) < k + ½ by
Lemma 1.1; V(y−) = π(y−) − E(y−) ≤ k + ½ with equality only if E(y−) = −½ and π(y−) = k, i.e. (no ties) y = p_{k+1} > x. So
M(x) < k + ½. And M(x) ≥ V(p_k) = k − E(p_k) = k − ½ (k ≥ 1; for k = 0, M ≥ V(1) = 0). So M(x) ∈ [k − ½, k + ½). ∎
*Boundary convention.* With a tie at y ≤ x (possible for rational ρ), V(y−) = π(y−) + ½ and the floor overcounts by one; the correct
statement is then the hitting-time form p_{k+1} = inf{y > p_k : V(y) ≥ k + ½} with V right-continuous (from 1.0).
**Corollary 1.4′ (E is a composite discrepancy).** E(x) = sup_{1≤y≤x}( #(composites in [y, x]) − ρ(x − y) ) + r(x), since V(y−) − V(x)
= C(x) − C(y−) − ρ(x − y). Hence sup_{u≤x} E(u) equals, within ½, the largest excess of composites over ρ·length on a subinterval of
[1, x]. Bounding E from above is exactly a one-sided discrepancy bound for the composites; E ≥ −½ is free.

**Lemma 1.5 (template, Mellin identity)** [proved here]. dT = δ₁ + ρ du on [1, ∞) has ζ_c(s) = 1 + ρ∫_1^∞u^{−s}du = (s − 1 + ρ)/(s − 1).
For Re s > 1, log ζ_c(s) = ∫_1^∞ u^{−s}(1 − u^{−ρ}) du/log u: both sides have s-derivative 1/(s − 1 + ρ) − 1/(s − 1) and tend to 0 as
s → +∞. So the template's Π_c has density (1 − u^{−ρ})/log u ≥ 0, ψ_c(x) = x − 1 − (x^{1−ρ} − 1)/(1 − ρ), and ζ_c has one zero, s = 1 − ρ.
For a discrete system with E(u) = O(u^θ), θ < 1: for Re s > 1, ζ_P(s) = s∫_1^∞ N(u)u^{−s−1}du = ζ_c(s) + sÊ(s), Ê(s) := ∫_1^∞ E(u)u^{−s−1}du,
and the right side continues ζ_P analytically to Re s > θ minus the simple pole at 1 (residue ρ). Truncated: ζ_P(s) = F_X(s) +
s∫_X^∞ E u^{−s−1}du with F_X(s) = Σ_{n≤X} n^{−s} + ρX^{1−s}/(s − 1) − E(X)X^{−s} = ζ_c(s) + s∫_1^X E u^{−s−1}du (expand
Σ_{n≤X} n^{−s} = X^{−s}N(X) + s∫_1^X N u^{−s−1}du and s∫_X^∞ T u^{−s−1}du = ρsX^{1−s}/(s − 1) + (1 − ρ)X^{−s}). Checked: the two forms of
F_X agree to 10⁻¹¹ at twelve σ (logs below).

**Theorem 1.6 (one-sided integer regularity forces a real zero)** [proved here] [novelty: single-check]. Let P be any discrete Beurling
system (g-primes 1 < p₁ ≤ p₂ ≤ …, N counted with multiplicity), ρ ∈ (0, 1), E(u) := N(u) − ρ(u − 1) − 1, and suppose
(A) E(u) ≥ −c for all u ≥ 1, some c ∈ [0, 1); (B) E(u) = O(u^θ) for some θ < 1 (no constant needed).
Then for θ < σ < 1: ζ_P(σ) ≥ 1 − c − ρ/(1 − σ). If σ₀ := 1 − ρ/(1 − c) > θ, then ζ_P has a real zero σ* ∈ [σ₀, 1) (in (σ₀, 1) if E > −c on a
set of positive measure), and ψ_P(x) − x ≠ O(x^a) for every a < σ*: P is an [α, β]-system with α ≥ σ* and β ≤ θ.
*Proof.* By 1.5, ζ_P(σ) = 1 − ρ/(1 − σ) + σ∫_1^∞E u^{−σ−1}du ≥ 1 − ρ/(1 − σ) − cσ∫_1^∞u^{−σ−1}du = 1 − c − ρ/(1 − σ); this is ≥ 0 at σ₀ and
the integral inequality is strict when E > −c on positive measure. ζ_P is real-analytic on (θ, 1) and ζ_P(σ) → −∞ as σ → 1⁻ (pole,
residue ρ > 0, while σÊ(σ) stays bounded). The intermediate value theorem gives σ*. For the last claim: for Re s > 1,
−ζ′_P/ζ_P(s) = s∫_1^∞ψ_P(u)u^{−s−1}du (ψ_P(u) ≤ N(u) log u). If ψ_P(u) − u = O(u^a), a < σ*, then H(s) := s∫_1^∞(ψ_P(u) − u)u^{−s−1}du is
analytic on Re s > a and −ζ′_P/ζ_P = s/(s − 1) + H on Re s > 1, hence on the connected set {Re s > max(a, θ)} minus the zeros of ζ_P and
the point 1. But −ζ′_P/ζ_P has a pole of residue −(order) at σ*, where s/(s − 1) + H is analytic. Contradiction. ∎
**Corollary 1.7 (S8).** c = ½ by Lemma 1.1, with E > −½ everywhere. (i) If E_{S8(ρ)}(u) = O(u^θ) for some θ < 1 − 2ρ, then ζ_P has a real
zero in (1 − 2ρ, 1), and α > 1 − 2ρ. (ii) If ρ ≤ ¼ and θ ≤ ½ − ρ: α > 1 − 2ρ ≥ max{½, 2θ} ≥ max{½, 2β}, so **Conjecture U is false.**
(iii) Finite certificate, any ρ: if F_X(σ₁) > ½X^{−σ₁} and θ < σ₁, then ζ_P(σ₁) > 0 (the tail exceeds −½X^{−σ₁} by Lemma 1.1, with no
upper bound on E used), so the real zero lies in (σ₁, 1). Only the existence of the continuation needs (B), and only qualitatively.

(§1 continues below.)

## §2. The mechanism (task 2)

(pending)

## §3. The proof problem (task 3)

(pending)

## §4. The Rouché theorem for S8 (task 4)

(pending)

## §5. Prior art at the page (task 5)

(pending)

## §6. Instruments rows, Untried, waste line, distance from upstream

(pending)
