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

**1.8 Verification on data** [computed]. `verify/s8_check.py` (generator = the prototype's core, same event order and tie rule):
ρ = π/4 at X = 10⁶ and ρ = 0.8 at X = 10⁶ — zero violations of Lemma 1.1 (E > −½ after every event, E(x−) ≥ −½), Lemma 1.2 (gaps ≥ t;
every prime on the lattice), Lemma 1.4 (π = ⌊M + ½⌋ with M including left limits; E − (M − V) ∈ (−½, ½]); ties = 0 in both (for ρ = 0.8,
rational, none occurred below 10⁶); the two forms of F_X agree to ≤ 1.1·10⁻¹¹ (logs `s8_check_pi4_1e6.log`, `s8_check_r08_1e6.log`).
At 10⁷ (`s8_check_pi4_1e7.log`) the reflection check trips 353,814 times at tolerance 10⁻⁶ only because the prototype updates the deficit
incrementally (max |E − (π − V)| = 2.1·10⁻⁵ by 10⁷); `verify/s8_realzero.py` and `verify/s8_mech.py` place primes by the exact lattice
formula of Lemma 1.2 and reproduce the prototype's counts (N(10⁶) = 785,400, π = 78,134 for ρ = π/4).
Real zero of F_X (bisection; `verify/mech_sweep_*_1e6.log`, `mech_pi16_1e7.log`, `rz_*.log`), X = 10⁶ unless stated:

| ρ | 1 − 2ρ (Thm 1.6 floor) | 1 − ρ (template zero) | σ* (real zero of F_X) | sup E to X | sup E / log²X |
|---|---|---|---|---|---|
| π/64 = 0.0491 | 0.9018 | 0.9509 | 0.947634 | 3.51 | 0.018 |
| π/32 = 0.0982 | 0.8037 | 0.9018 | 0.895076 | 6.39 | 0.034 |
| π/16 = 0.1963 | 0.6073 | 0.8037 | 0.794752 (10⁶), 0.794755 (10⁷) | 9.64 (10⁶), 12.84 (10⁷) | 0.050, 0.049 |
| π/8 = 0.3927 | 0.2146 | 0.6073 | 0.656529 | 15.35 | 0.080 |
| π/6 = 0.5236 | < 0 | 0.4764 | 0.521753 | 21.33 | 0.112 |
| π/4 = 0.7854 | < 0 | 0.2146 | 0.514036 (10⁶); F_X(½) = 0.06707 at 10⁷ | 39.53 | 0.207 |
| 0.95π/3 = 0.9948 | < 0 | 0.0052 | 0.402156 | 82.38 | 0.432 |

Every F_X respects the floor ½ − ρ/(1 − σ) of Theorem 1.6 (`rz_pi16_1e6.log`, columns 2 and 4). For ρ ≤ ¼ the zero is the template's
zero 1 − ρ moved left by 0.003–0.009; for ρ ∈ (¼, π/4] it sits in (½, 0.66) though Theorem 1.6 alone gives nothing there; at ρ ≈ 1 it
falls below ½ (ℕ itself, ρ = 1 and E = −{x} ∈ (−1, 0], has ζ < 0 on (0, 1) and no real zero).

## §2. The mechanism (task 2)

**Proposition 2.1 (gap identity)** [proved here]. Let g_k := p_{k+1} − p_k and C(a, b) the number of composites in the open interval.
(i) E(x) = ½ + C(p_k, x] − ρ(x − p_k) for x ∈ [p_k, p_{k+1}); (ii) ρg_k = 1 + C(p_k, p_{k+1}); (iii) sup_{u≤x}E(u) ≤ ρG(x) − ½, G(x) :=
max{g_k : p_{k+1} ≤ x} (and the gap containing x). *Proof.* E(p_k) = ½ (1.0(ii)); no prime lies in (p_k, p_{k+1}), so N grows only by
composites there, giving (i). E(p_{k+1}−) = −½ (1.0(i)) inserted in (i) gives (ii). From (i), E(x) ≤ ½ + C(p_k, p_{k+1}) = ρg_k − ½. ∎
So **(B) follows from a prime-gap bound G(x) = O(x^θ)**. The converse fails: composites spread evenly over a long gap keep E small.
Data (π/16, 10⁷): G = 336.1, ρG − ½ = 65.5 against sup E = 12.84 (`verify/mech_pi16_1e7.log`); G ≈ 1.3 log²x.

**2.2 Linearization, the clip, and the real zero.** Write R(u) := N(u) − ρu = 1 − ρ + E(u). For Re s > 1,
ζ_P(s) = ρs/(s − 1) + s∫_1^∞R(u)u^{−s−1}du, and with the template R_c ≡ 1 − ρ this is ζ_c. A perturbation dw of the prime measure from
dΠ_c gives ζ_P = ζ_c·exp(ŵ), so to first order sÊ = ζ_c·ŵ: exact tracking (E ≡ 0) forces ŵ ≡ 0, the continuous template, which no
discrete system can be. The zeros of ζ_P are the points where ŵ has a logarithmic singularity, i.e. where sÊ(s) = −ζ_c(s): the neutral
modes of the loop. The clip (π′ ≥ 0, the rule can add g-integers but never remove one) is what makes E one-signed below: E > −½, i.e.
R(u) ≥ ½ − ρ =: r₀ for all u (attained at every prime: R(p−) = ½ − ρ; `verify/lin_sweep_1e6.log`, column inf R).
*Remark 1.6′ (the cleanest form of Theorem 1.6)* [proved here]. If R(u) ≥ r₀ > 0 for all u and R = O(u^θ), then
ζ_P(σ) ≥ r₀ − ρσ/(1 − σ) > 0 for θ < σ < r₀/(r₀ + ρ), and ζ_P has a real zero in [r₀/(r₀ + ρ), 1). An integer count that never dips
below its linear part forces a real (Siegel-type) zero; ℕ escapes because ⌊u⌋ − u ≤ 0. U needs r₀/(r₀ + ρ) > ½, i.e. r₀ > ρ: for S8,
½ − ρ > ρ, i.e. ρ < ¼.
*Where the zero sits.* ζ_c has a simple zero at s₀ = 1 − ρ with ζ_c′(s₀) = −1/ρ, so to first order σ* ≈ s₀ + ρζ_P(s₀). Test
(`verify/s8_lin.py`, X = 10⁶) [computed]: π/64: 0.947841 vs σ* = 0.947634; π/32: 0.895479 vs 0.895076; π/16: 0.794932 vs 0.794752;
π/8: 0.671073 vs 0.656529 (second order visible); π/4: the linearization fails (shift 0.92), the zero at 0.514 is not the template's.
For ρ ≤ ¼ the real zero of S8 is the template zero 1 − ρ, displaced left by ρ|ζ_P(1 − ρ)| ≈ 0.003–0.009 because the early stretch
E(u) = −ρ(u − 1) on [1, p₁) dominates the weight u^{−σ−1}. For ρ ≥ ¼ it is a genuinely nonlinear zero in (½, 0.66).

**2.3 The queue heuristic, tested.** By Prop. 2.1, E is exactly the content of a queue: unit arrivals (composites), constant service
rate ρ, reflection at −½ effected by unit insertions (primes). If composites at scale u were Poisson of rate ρ − μ, μ ≈ (1 − u^{−ρ})/log u
the prime density, the quasi-stationary law of E has the Cramér–Lundberg tail e^{−κh}, κ solving (ρ − μ)(e^κ − 1) = ρκ, so
κ ≈ 2μ/ρ ≈ 2/(ρ log u), mean ≈ ρ log u/2, and the running maximum ≈ log(x)/κ ≈ (ρ/2)·log²x. [heuristic, not proved]
Data, π/16, top half-decade [10^6.5, 10⁷] (`mech_pi16_1e7.log`) [computed]: time-mean of E 0.907 vs 1.58 predicted (ratio 0.57, both
∝ log x: the mean grows by 0.16 per decade, predicted 0.23); tail rate 0.981 vs 0.632 (ratio 1.55, stable over four half-decades:
1.48–1.65). So composite arrivals are SUB-Poissonian, effective variance ≈ 0.6 of Poisson, and sup E ≈ 0.3ρ·log²x: measured
sup E/log²x = 0.018, 0.034, 0.049, 0.080, 0.112, 0.207 at ρ = π/64 … π/4 (§1.8), i.e. (0.37–0.53)·ρ, against 0.3ρ predicted.
The heuristic's law — polylogarithmic E, tail rate ∝ 1/(ρ log u) — matches; its constant does not, and the discrepancy (sub-Poisson
variance) is the trace of the correlations a proof would have to control.

**2.4 Real parts.** Hilberdink 2005 Cor. 2(b) [quoted: `novel-wave-s37/beurling-frontier/sources/w-18a…txt` l. 210–213, JNT 112
p. 336]: if N_P(x) = ρx + O(x^β), β < ½, then for every γ ∈ (β, ½), ψ_P(x) − x = Ω(x^γ) and ζ_P has infinitely many zeros in
γ < Re s < 1. So (B) with θ < ½ forces infinitely many zeros right of θ, not right of ½; nothing printed that we have read forces
sup Re = 1. The real zero is a fixed σ* < 1, stable to 3·10⁻⁶ between 10⁶ and 10⁷ (π/16). Whether complex zeros climb toward 1
is the compute unit's question (its task 3(ii)); see §4 for what arrives.

## §3. The proof problem (task 3)

(pending)

## §4. The Rouché theorem for S8 (task 4)

(pending)

## §5. Prior art at the page (task 5)

(pending)

## §6. Instruments rows, Untried, waste line, distance from upstream

(pending)
