# NOTE — unit `U1-lookahead` (stream `lemmaB-s41`): a placement rule with a proved bound, or a proof that a class of rules cannot have one

Session 41, started 16:58 IST 2026-10-01. Writer: Opus 5.5 (agent). Labels as in the charter §4: **[proved here]**, **[computed]**
(script + log in `verify/`), **[quoted]** (source opened at the line), **[recalled, unverified]** (never load-bearing).
Notation as in `../../free-greedy-s40/theory/NOTE.md`: t = 1/ρ, T(x) = ρ(x − 1) + 1, E = N − T, R(u) = N(u) − ρu = 1 − ρ + E(u),
Π_P(u) = Σ_{p^k ≤ u} 1/k (Riemann prime counting of the system), log ζ_P(s) = ∫u^{−s}dΠ_P for Re s > 1. Template: dΠ_c = (1 − u^{−ρ})du/log u,
ζ_c(s) = (s − 1 + ρ)/(s − 1) (s40 Lemma 1.5). "Threshold τ": a g-prime is placed when T − N reaches τ, so E ≥ −τ and r₀ = 1 − ρ − τ.

## §0. Close (filled last)

(pending)

## §1. The design space, and what "the mean" is

**1.1 Rules.** A *rule* chooses the g-primes one at a time. Every rule considered here is a *fill rule*: it never lets the deficit
T − N exceed τ, so (A) holds with r₀ = 1 − ρ − τ by construction; the freedom is (i) WHEN a prime is placed (any time up to its deficit
time x*, "early placement", charter §2(d)), (ii) WHERE inside the allowed window [x* − w, x*], and (iii) what the rule may look at
(the composites up to p₁x are fixed once the primes below x are, so a block rule on [B, p₁B) sees all its composites in advance).
Greedy S8 is w = 0. The class R(w) = all fill rules with early-placement windows of width ≤ w(x) at scale x.
**1.2 The one degree of freedom.** For any discrete system, dΠ_P = log*(dN) (the inverse of the multiplicative exponential), and
dN = δ₁ + ρ du + dE. So the whole system is determined by the single function E, and a rule is a way of choosing E inside the set of
functions for which log*(δ₁ + ρdu + dE) is a positive discrete prime measure (atoms 1/k at prime powers). (A) is E ≥ −τ, (B) is
E = O(u^θ). Positivity of log* is the only constraint, and it is global and nonlinear.
**1.3 The mean.** In the s40 routes (a)/(b) the composite count in a window I is split as C(I) = A(I) + M(I), A the compensator (the
composite count with the last-placed factor of each composite averaged over its placement window), M a martingale (route a) or a
potential-controlled deviation (route b). Fluctuation control bounds M; both routes broke at **Lemma M**: A(I) ≤ ρ|I| − c|I|/log y for
all I ⊂ [y, 2y], |I| ≥ log³y. Since C(I) = ρ|I| − π(I) + ΔE(I), Lemma M is a lower bound on the smoothed density of the system's OWN
primes in windows of length ≥ log³y. "Controllable by construction" would mean: the rule fixes that smoothed density in advance.
§2 shows that a rule which fixes the prime counting function in advance (deterministically, to within u^{α′}, α′ < ½) cannot satisfy (B)
below ½ at all; §3 shows what look-ahead and early placement can and cannot change for the rules that do not fix it.

## §2. Rules that fix the primes in advance cannot reach (B) below ½ — the relative Hilberdink wall

**Quoted input (Q1).** Hilberdink, JNT 112 (2005), Cor. 2(b) [quoted: `../../novel-wave-s37/beurling-frontier/sources/w-18a-…txt`
l. 211–214; its proof l. 659–673 uses only Theorem 1 (l. 195), Remark B(ii) and Remark C (l. 496–501)]: *if N_P(x) = ρx + O(x^β) with
ρ > 0, β < ½, then for every η′ ∈ (β, ½), ζ_P has infinitely many zeros in η′ < Re s < 1.* (P any discrete Beurling system.)

**Theorem 2.1 (relative wall)** [proved here, from Q1]. Let P be a discrete Beurling system and Π_ref a real measure on [1, ∞) with
∫u^{−σ}d|Π_ref| < ∞ for σ > 1, such that ζ_ref(s) := exp∫u^{−s}dΠ_ref(u) continues meromorphically to Re s > γ₀ with only finitely many
zeros and poles there, for some γ₀ < ½. Then the two statements
  (i) Π_P(u) − Π_ref(u) = O(u^{α′}) for some α′ < ½,   (ii) N_P(u) − ρu = O(u^θ) for some θ < ½ and some ρ > 0,
cannot both hold.
*Proof.* Put D := Π_P − Π_ref. For Re s > 1, log ζ_P(s) − log ζ_ref(s) = ∫u^{−s}dD(u) = −D(1) + s∫_1^∞D(u)u^{−s−1}du =: η̂(s) (the boundary
term at ∞ vanishes by (i)); by (i) the integral converges absolutely and η̂ is analytic on Re s > α′. So ζ_P = ζ_ref·e^{η̂} on Re s > 1, and
the right side is meromorphic on Re s > max(α′, γ₀) with only finitely many zeros (those of ζ_ref; e^{η̂} has none). By (ii),
ζ_P(s) = s∫_1^∞N_P(u)u^{−s−1}du = ρs/(s − 1) + s∫_1^∞(N_P(u) − ρu)u^{−s−1}du continues meromorphically to Re s > θ. By uniqueness of
continuation the two agree on Re s > γ₁ := max(α′, γ₀, θ) < ½, so ζ_P has finitely many zeros in Re s > γ₁. Q1 with β = θ and any
η′ ∈ (γ₁, ½) gives infinitely many zeros in Re s > η′ > γ₁. Contradiction. ∎
**Corollary 2.2 (deterministic prescription is dead)** [proved here]. (a) Let F be any function and suppose a rule produces g-primes with
π_P(u) = F(u) + O(u^{α″}), α″ < ½ (e.g. the Beatty/rounding rule π_P = ⌊F + ½⌋, α″ = 0, with or without feedback, as long as the bound
holds). Put Π_F(u) := Σ_{k≥1}F(u^{1/k})/k. Then Π_P − Π_F = Σ_k(π_P − F)(u^{1/k})/k = O(u^{α″} + u^{α″/2}log u), so if ζ_F is meromorphic and
finitely zeroed right of some γ₀ < ½, the system has N_P − ρu ≠ O(u^θ) for every θ < ½. For the Möbius-corrected template
F_c(u) := Σ_k μ(k)Π_c(u^{1/k})/k one has Σ_k F_c(u^{1/k})/k = Σ_n(Σ_{j|n}μ(j))Π_c(u^{1/n})/n = Π_c(u), so ζ_F = ζ_c = (s − 1 + ρ)/(s − 1):
**every rule whose primes follow the template to within u^{α″}, α″ < ½, has integer error Ω(u^{γ}) for all γ < ½.**
(b) The naive prescription F = Π_c (no prime-power correction) fails even more directly: Π_F gives ζ_F = Π_k ζ_c(ks)^{1/k}, which has the
branch point ((2s − 1 + ρ)/(2s − 1))^{1/2} at s = ½; then ζ_P = ζ_F·e^{η̂} is not meromorphic at s = ½, while (ii) would make it analytic
there. So N_P − ρu ≠ O(u^θ) for θ < ½ [proved here, same continuation argument].
**Corollary 2.3 (the primes of a (B)-system are wild)** [proved here]. If N_P − ρu = O(u^θ) with θ < ½, then for every reference as in 2.1,
Π_P − Π_ref ≠ O(u^{γ}) for every γ < ½. In particular, if Lemma B_ρ holds for S8(ρ), then Π_{S8} − Π_c ≠ O(u^{γ}) for all γ < ½.
**Remarks.** (1) Hilberdink's own final section (w-18a l. 677–700) builds exactly such a prescription relative to ψ = x
(p_n = R^{−1}(n)) and concludes β ≥ ½ from his Theorem 1; BDR state the same for the reference ζ = s/(s − 1): "any method for
approximating systems in the extended sense by discrete systems (P, N) which yields O(x^θ) control on either Π_P(x) or N_P(x), where
θ < 1/2, should have an uncertainty of size at least x^{1/2−ε} … on the other counting function. If not, then approximating the extended
system (Π(x), N(x)) = (Li(x), x), for which ζ(s) = s/(s − 1), would yield an [α, β]-system with max{α, β} < 1/2, contradicting
Hilberdink's result" [quoted, z-02 l. 172–177]. That argument needs a zero-free reference (it goes through Theorem 1, which needs
ψ = x + O(x^{<½})); Theorem 2.1 goes through Cor. 2(b) instead and so allows references WITH finitely many zeros — in particular the
template, whose zero 1 − ρ is exactly the one a never-undershooting system must carry (s40 Theorem 1.6). (2) Not covered: random prescriptions (Poisson thinning
of a density has |Π_P − Π_ref| ≍ u^{1/2} up to logs, the borderline α′ = ½), and rules whose primes are not close to any finitely-zeroed
reference — among them greedy S8, whose ψ_P is far from smooth (s40 charter §2 table: sup|ψ_P − x| local exponents 0.6–1.0).
(3) What this kills in the charter's language: a rule cannot make the mean "controllable by construction" by fixing the prime counting
function in advance to sub-square-root accuracy; whatever the compensator of a (B)-system is, the primes it is built from carry
irregularities of size u^{½−ε} that no smooth finitely-zeroed formula describes.

## §3. Closed-loop rules: what look-ahead and early placement can and cannot change

**Proposition 3.1 (greedy is pointwise optimal inside a block; look-ahead over the known composites gains nothing)** [proved here].
Fix the primes below B and let C be the (fixed) composites in [B, Bh), Bh = p₁B. Among all placements of primes in [B, Bh) obeying the
fill constraint E(x−) ≥ −τ for every x ∈ [B, Bh), greedy has the fewest primes up to every point: π_R(B, x] ≥ π_G(B, x], hence
E_R(x) ≥ E_G(x) for all x ∈ [B, Bh).
*Proof.* A prime q ≥ B has q·m ≥ p₁B = Bh for every g-integer m > 1, so the placement in [B, Bh) does not change C there, and
E(x) = f(x) + π(B, x] with f(x) := E(B−) + C(B, x] − ρ(x − B) common to all placements. Suppose the claim fails and let x₀ be the least
point with π_G(B, x₀] > π_R(B, x₀]. Then x₀ is a greedy prime, so E_G(x₀−) = −τ, and f is continuous at x₀ (by the tie convention a
composite at x₀ is counted first and would lift E_G(x₀−) above −τ). Minimality gives π_R(B, x₀) ≥ π_G(B, x₀) = π_G(B, x₀] − 1 ≥
π_R(B, x₀], so R has no prime at x₀ and π_R(B, x₀) = π_G(B, x₀); hence E_R(x₀) = f(x₀) + π_G(B, x₀) = E_G(x₀−) = −τ, and E_R decreases
with slope −ρ until the next event x₁ > x₀, so E_R(x₁−) < −τ: the constraint fails. ∎
*Consequence.* The charter's look-ahead "over the already-determined composites in (x, p₁x]" cannot improve on greedy anywhere in the
block it looks at: every deviation from greedy (early placement, choice of position) raises E there, and can pay off only through the
composites it creates in LATER blocks — which are not yet determined when the choice is made.

**Proposition 3.2 (the leading constant is a global functional)** [proved here]. (a) If P₀ ⊂ P is a set of g-primes of a system P,
then N_P(x) ≥ N_{P₀}(x) for all x (the monoid of P₀ is a sub-multiset). (b) If Π_{P₀} − Π_c = D with D(u) = O(u^ε) for every ε > 0 (e.g. the rounding rule, where D = O(log log u)), then ζ_{P₀} = ζ_c·e^{η̂}
with η̂ analytic on Re s > 0, ζ_{P₀} has no zeros on Re s = 1 and its only pole there is s = 1, with residue ρ₀ = ρ·e^{η̂(1)},
η̂(1) = −D(1) + ∫_1^∞D(u)u^{−2}du; by the Wiener–Ikehara theorem [recalled, unverified; standard] N_{P₀}(x) ~ ρ₀x.
(c) Hence any rule containing an open-loop sub-rule P₀ with ρ₀ > ρ has E_P(x) ≥ (ρ₀ − ρ)x(1 + o(1)): (B) fails for every θ < 1, and no
feedback can repair it, since feedback only adds primes.
*Proof.* (a) is inclusion of multisets. (b) as in Theorem 2.1 with α′ = 0; e^{η̂} has neither zeros nor poles and ζ_c has its only zero
at 1 − ρ < 1. (c) by (a) and (b). ∎
The constant ρ₀ = ρe^{η̂(1)} weighs D by u^{−2}: it is set mostly by the SMALLEST primes of P₀, i.e. by the discretization at scales
where no rule has any freedom, and no finite tuning of the prescription at large scales corrects it. A closed-loop (fill) rule gets the
constant right automatically, because it tracks N itself; this is why every working rule must be closed-loop at the level of N.

**Proposition 3.3 (integer bounds at smaller scales do not control the composites at the next scale — a barrier for scale induction
over R(w))** [proved here]. Let P be a discrete system satisfying (A) with |E_P(x)| ≤ ½K x^θ for x ≤ y₀ (some K > 0, θ ∈ (0, 1)). Fix
J ≥ 1 and put a_j := y₀/p_j (j ≤ J). Let δ₀ > 0 be the least relative gap between distinct elements of the finite set
{m·p_i : i ≤ J, m ∈ G, m < p_J} (distinct products are distinct reals when t is transcendental, s40 Lemma 1.3). Suppose that for each
j the window [a_j, a_j + H_j], with H_j < δ₀a_j/2, contains n_j := ⌈¼K a_j^θ⌉ primes of P. Let P′ be P with those primes moved to
the point a_j (early placement; repeated g-primes are allowed in a Beurling system, or spread them over [a_j, a_j + ε]). Then
(i) E_{P′} ≥ E_P ≥ −τ everywhere ((A) is kept); (ii) |E_{P′}(x)| ≤ K x^θ for all x < y₀ once y₀ is large; (iii)
E_{P′}(y₀) ≥ E_P(y₀) + Σ_{j≤J} n_j ≥ −τ + ¼K y₀^θ Σ_{j≤J} p_j^{−θ}, which exceeds K y₀^θ as soon as Σ_{j≤J}p_j^{−θ} > 4 + o(1)
(possible: Σ_p p^{−θ} ≥ Σ_p 1/p = ∞ for any system with N ~ ρx).
*Proof.* Moving primes down moves every g-integer down or leaves it, so N_{P′} ≥ N_P pointwise: (i). For x < y₀, N_{P′}(x) − N_P(x)
counts g-integers n = q·m with q a moved prime of bunch j and x ∈ [m·a_j, m·q); then m < x/a_j < p_j, so m lies in the finite set of the
statement, and x lies in [m a_j, m(a_j + H_j)), an interval of relative width < δ₀/2; two such intervals for different (j, m) would put
m p_{j′} and m′ p_j within relative distance δ₀ of each other, so for each x at most one pair (j, m) contributes, adding ≤ n_j ≤
¼K a_j^θ + 1 ≤ ¼K x^θ + 1. With E_P ≤ ½K x^θ this gives (ii) for x ≥ (4/K)^{1/θ}. (iii): the p_j-dilates of bunch j, originally in
[y₀, y₀ + p_jH_j], all sit at y₀ in P′, while no g-integer of P below y₀ moves above it. ∎
*Reading.* P′ is greedy S8 with J bunches of early placements: a rule in R(w), w = max H_j ≍ K y₀^θ log y₀ (for S8 the hypothesis on the
windows is the observed prime density, `verify/` logs; for the statement it is a hypothesis). Moving n_j primes changes the prime count of
any window by at most n_j, so P′ also inherits every short-interval prime-count bound of P in windows of length ≫ K v^θ log v. **So no
argument that passes from bounds on E (or on prime counts in windows of length ≫ v^θ) at scales below y to the bound at y can work
uniformly over R(w); a proof of (B) must use the specific rule — the fine positions of its primes at all smaller scales.** This is the
deterministic face of the s40 finding that random early placement makes E worse.

## §4. A design result: the threshold moves the real zero to 1 − τ, so U needs only θ < ½ − τ/2, for every density

**Theorem 4.1 (power bump)** [proved here]. Let P be a discrete Beurling system, ρ ∈ (0, 1), τ ∈ (0, 1), with
E(u) := N(u) − ρ(u − 1) − 1 ≥ −τ for all u ≥ 1, and E(u) = O(u^θ) for some θ < 1. Put p* := 1 + τ/ρ, a := log p*,
k(u) := ⌊log u / a⌋ and
  Λ_{ρ,τ}(σ) := 1 − τ − ρ/(1 − σ) + σ∫_1^∞ (k(u) − ρ(u − 1) + τ)⁺ u^{−σ−1} du.
Then ζ_P(σ) ≥ Λ_{ρ,τ}(σ) for θ < σ < 1. Hence if θ < σ₁ < 1 and Λ_{ρ,τ}(σ₁) > 0, ζ_P has a real zero in (σ₁, 1) and α(P) > σ₁.
*Proof.* (1) The first g-prime satisfies p₁ ≤ p*: on [1, p₁) only the unit is counted, so E(u) = −ρ(u − 1), and E ≥ −τ there
forces p₁ ≤ 1 + τ/ρ. (2) Every power p₁ʲ is a g-integer, so N(u) ≥ 1 + #{j ≥ 1 : p₁ʲ ≤ u} ≥ 1 + k(u) (p₁ ≤ p* makes the count
larger), i.e. E(u) ≥ k(u) − ρ(u − 1); with E ≥ −τ, E(u) ≥ −τ + (k(u) − ρ(u − 1) + τ)⁺. (3) By s40 Lemma 1.5 (valid on σ > θ by
continuation), ζ_P(σ) = 1 − ρ/(1 − σ) + σ∫_1^∞E(u)u^{−σ−1}du; insert (2) and use σ∫_1^∞u^{−σ−1}du = 1. (4) ζ_P is real-analytic on
(θ, 1) and ζ_P(σ) → −∞ as σ → 1⁻ (pole with residue ρ > 0); the intermediate value theorem gives the zero; α > σ₁ as in s40 Thm 1.6. ∎
(The integral is a finite sum: on [p*^k, min(p*^{k+1}, c_k)], c_k := 1 + (k + τ)/ρ, the integrand is (k + τ + ρ − ρu)u^{−σ−1}, with
primitive −(k + τ + ρ)u^{−σ}/σ − ρu^{1−σ}/(1 − σ); beyond the first k with p*^k ≥ c_k and p* ≥ 1 + 1/(k + ρ + τ) all pieces are empty.)
**Theorem 4.1 always improves s40 Theorem 1.6**: dropping the integral leaves 1 − τ − ρ/(1 − σ), whose root is r₀/(r₀ + ρ),
r₀ = 1 − ρ − τ. The improvement comes from discreteness (the forced powers of p₁); the continuous template has E ≡ 0 and its zero
stays at 1 − ρ.
**Corollary 4.2 (what U now needs)** [proved here]. If a discrete system with E ≥ −τ has N(u) − ρu = O(u^θ) with θ < σ₁/2 and
Λ_{ρ,τ}(σ₁) > 0, Conjecture U is false (α > σ₁ > 2θ ≥ 2β, and σ₁ > ½). Certified instances [computed, `verify/powerbump_iv.py`,
mpmath interval arithmetic at 50 digits with integration endpoints rounded inward, so every rounding lowers the bound; log
`verify/powerbump_iv.log`]:

| ρ | τ | σ₁ | certified Λ(σ₁) ≥ | U refuted by (B) with θ < | s40 route (Cor 1.7) needed |
|---|---|---|---|---|---|
| π/16 | ½ | 0.763 | 0.000612 | 0.3815 | θ ≤ 0.304 (Thm 1.6), 0.395 (computed certificate) |
| π/16 | 1/10 | 0.911 | 0.0127 | 0.4555 | — |
| π/16 | 1/50 | 0.979 | 0.461 | 0.4895 | — |
| π/16 | 1/100 | 0.989 | 1.653 | 0.4945 | — |
| π/32 | ½ | 0.888 | 0.00287 | 0.444 | θ ≤ 0.402, 0.445 (certificate) |
| π/32 | 1/100 | 0.990 | 0.426 | 0.495 | — |
| π/8 | 1/100 | 0.989 | 2.306 | 0.4945 | none (ρ > ¼) |
| π/4 | 1/10 | 0.869 | 0.0112 | 0.4345 | none |
| π/4 | 1/100 | 0.989 | 3.612 | 0.4945 | none |
| 0.95π/3 | 1/100 | 0.989 | 4.308 | 0.4945 | none |
| π/4 | 1/1000 | 0.998 | 387.9 | 0.499 | none |

**Proposition 4.3 (σ_L → 1)** [proved here]. Let σ_L(ρ, τ) be the largest root of Λ_{ρ,τ}. For every ρ ∈ (0, 1) and c > 1 there is
τ₀(ρ, c) > 0 with σ_L(ρ, τ) ≥ 1 − cτ for τ < τ₀. So for every ε > 0 some threshold makes "(B) with some θ < ½ − ε" sufficient.
*Proof.* Take σ = 1 − cτ, U := 1/(ρa) and note τ/(2ρ) ≤ a ≤ τ/ρ for τ ≤ ρ. On [1, U], k(u) ≥ log u/a − 1 and
(k − ρ(u − 1) + τ)⁺ ≥ log u/a − 1 − ρu; dropping (U, ∞) only lowers the integral. With ∫_1^U log u·u^{−σ−1}du ≥ ∫_1^U log u·u^{−2}du
= 1 − (1 + log U)/U, ∫_1^U u^{−σ−1}du ≤ 1/σ and ∫_1^U u^{−σ}du ≤ U^{1−σ}log U:
Λ(σ) ≥ −τ − ρ/(cτ) + (σ/a)(1 − ρa(1 + log U)) − ρσU^{cτ}log U ≥ (ρ/τ)(1 − 1/c) − C_ρ(1 + log(1/τ)) for τ < τ₁(ρ, c),
using σ/a ≥ (1 − cτ)ρ/τ, ρa ≤ τ, U ≤ 2/τ and U^{cτ} ≤ (2/τ)^{cτ} ≤ 2. The right side is positive for τ small. ∎
**Sharpness** [computed: `verify/zero_tau_1e7.log`, `zero_tau_1e8.log`, `zero_bigrho_1e7.log`, roots by `verify/powerbump_bound.py`,
log `powerbump_bound.log`]. Real zero σ* of F_X for the greedy τ-systems (double precision, X = 10⁷; identical to 6 digits at 10⁸
for τ = 1/50, 1/100) against the bound's root σ_L: π/16: τ = ½: 0.79476 vs 0.76318; ¼: 0.84021 vs 0.83163; 1/10: 0.91235 vs 0.91150;
1/20: 0.95195 vs 0.95181; 1/50: 0.97998 vs 0.97997; 1/100: 0.98993 vs 0.98992. π/4: 1/10: 0.87079 vs 0.86923; 1/100: 0.98953 vs
0.98953 (at τ = ½ the bound has no root, the measured zero is 0.51451). For small τ the real zero of the whole system is the power bump
of its first prime, to 4–5 digits. (Mechanism: the bump E ≈ (ρ/τ)log(1/τ) on [1, ≈ 1/(ρa)] gives Ê(σ) ≈ ρ/τ, and 1 + σÊ − ρ/(1 − σ) = 0
gives 1 − σ* ≈ τ.) The low prime density of these systems in the computed range (π(W)·log x/|W| ≈ 0.30 at 10⁸ for τ = 1/50) is the
same fact seen from ψ: ψ_P(x) ≈ x − x^{σ*}/σ*.
**What it changes.** s40 needed ρ < ¼ and θ ≤ ½ − ρ (θ < 0.395 with a computed certificate) for one explicit system. Now: **one
never-undershooting discrete system of ANY density, with undershoot depth 1/100 and integer error O(u^{0.494}), refutes U**; and the
greedy rule with threshold 1/100 costs nothing at large scales (top half-decade sup E = 13.99 at 10⁸ against 16.36 for τ = ½,
`verify/zero_tau_1e8.log`). The proof target is now the weakest sub-square-root statement — exactly the boundary of Hilberdink's wall.
**Corollary 4.4 (the dichotomy, sharpened)** [proved here, from 4.2]. Either Conjecture U fails, or every discrete system with E ≥ −1/100
has β ≥ 0.4945 for each of ρ = π/32, π/16, π/8, π/4, 0.95π/3 — in particular the greedy rule with threshold 1/100, whose measured sup E on
[10^{7.5}, 10⁸] is 13.99 (π/16). (s40's form: β(S8(π/16)) > 0.395.) Under U the integer error of these explicit systems would have to
reach u^{0.4945} — about 9,000 at u = 10⁸ — eventually.
**Remark 4.5 (contrapositive, for U5).** If a discrete system has (B) with exponent θ and ζ_P has no real zero in (θ, 1) (ℕ, number
fields), then ζ_P < 0 on (θ, 1) (it tends to −∞ at 1 and never changes sign), so Λ_{ρ,τ} < 0 on all of (θ, 1) with τ := −inf E,
i.e. σ_L(ρ, τ) ≤ θ: a system without a real zero must undershoot by at least the τ at which σ_L(ρ, τ) = θ (ℕ: −inf E → 1, p₁ = 2,
and the bump is a single unit triangle on [1, 3)).

## §5. Every candidate rule, tested [computed]

Generator `verify/rules.cpp` / `rules2.cpp` (blocks [B, p₁B); double precision, ordering not certified). Validation: equal to the
s40 numbers (π/4, 10⁶: N = 785,400, π = 78,134, sup E = 39.53; π/16, 10⁷: sup E = 12.84, π = 633,514, largest gap 336.1, σ* = 0.794755,
F_{10⁷}(0.79) = +0.022231 as in read-O) and to an independent 50-digit brute force (`verify/validate_bf.py`, `validate_bf.log`: N, π,
sup E, inf E equal for τ ∈ {0.02, 0.25, 0.5} at π/16 and τ = ½ at π/4, X = 2·10⁴). A boundary bug (composites p₁ᵏ on block edges lost
when B/q rounds up; the s40 `s8w_block.py` has the same search) was found by that check and fixed; runs before the fix are in
`verify/superseded/`. All numbers below: `verify/batches_v2.log` (script `run_batches.sh`), `zero_tau_1e8.log`, `look_pi16_1e8.log`.
"LM" = min over windows W ⊂ [X/√10, X] (step |W|/2) of π(W)·log x/|W| at |W| = log³X — the empirical Lemma M margin; mean in brackets.

| rule (π/16) | sup E at 10⁷ | sup E at 10⁸ | LM at 10⁸ (mean) | verdict |
|---|---|---|---|---|
| greedy, τ = ½ (S8) | 12.84 | 16.36 | 0.77 (0.97) | baseline; 0.048·log²X |
| greedy, τ = ¼ | 11.45 | 14.93 | 0.77 (0.94) | same law |
| greedy, τ = 1/10 | 9.22 | 12.31 | 0.68 (0.79) | same law |
| greedy, τ = 1/50 | 30.72 (bump at x ≈ 50; top half-decade 10.30) | 30.72 (top 13.67) | 0.25 (0.30) | same law at large x; σ* = 0.980 |
| greedy, τ = 1/100 | 73.27 (bump) | 73.27 (top 13.99) | 0.14 (0.17) | same law; σ* = 0.990 |
| early, fixed offset W = 1, 2.5, 5, 10, 20, 100 | 52.3, 11.3, 10.2, 15.7, 52.4, 5852 | — | — | erratic; large W bunches primes on B (Prop 3.3 in action) |
| look-ahead (W, K, J, H) = (5,6,3,2) / (5,11,6,5) / (5,6,6,2) / (2.5,6,6,2) / (10,11,6,5) | 10.89 / 9.26 / 12.44 / 10.75 / 11.34 | 13.23 (5,6,3,2) / 14.24 (5,11,6,5) | — | −3…−28 % at 10⁷, −13…−19 % at 10⁸; law unchanged (0.039–0.042·log²X) |
| open loop: primes at λF_c = k − ½ + feedback, λ = 1 / 0.97 / 0.95 | 3.4e5 / 2.2e5 / 1.3e5 | 3.4e6 / 2.1e6 / 1.2e6 | — | linear in x (Prop 3.2) |
| open loop, λ = 0.9 / 0.8 | 50.9 / 32.6 | 70.7 / 40.4 | 0.87 / 0.78 | ≈ x^{0.14} / x^{0.09} |
| Poisson(λF_c) + feedback, λ = 1; λ = 0.9 seeds 1, 2, 3 | 1.1e5; 115, 8.7e4, 2.2e5 | 1.1e6; 168, 6.4e5, 2.0e6 | — | linear unless the seed undershoots |

π/32, greedy τ = ½, 10⁸: sup E = 9.86 (0.029·log²X), LM 0.72 (0.85). Anatomy of the top excursion (greedy τ = ½, π/16): at 10⁷ E rises
0.37·log²X from the last prime inside a gap of 0.82·log²X; at 10⁸ 0.62·log²X inside a gap of 1.52·log²X — excursions live inside
single prime gaps of length ≍ log²x (s40 Prop 2.1).
**Readings.** (1) Lemma M is TRUE in the data with a wide margin: in every window of length log³x the system's own prime density is
≥ 0.77 (π/16) and ≥ 0.72 (π/32) of 1/log x at 10⁸, against a mean 0.97 / 0.85; at length ¼log³x it is 0.47; at log²x it is 0 (gaps of
length ≍ log²x exist). The margin decreases slowly with X (π/16: 0.81 at 10⁷, 0.77 at 10⁸). (2) No rule beats greedy by more than a
constant factor; the rules that fix the prime density in advance are far worse, as §2–§3 predict: linear growth when the realized
density constant ρe^{η̂(1)} overshoots ρ, power growth when it undershoots. (3) The threshold changes the constants at small scales
and the real zero (§4), not the large-scale excursion law.

## §6. What is left, and what any proof has to use

**6.1 The target, in its weakest form.** *Lemma B_τ:* for some ρ ∈ (0, 1) and some τ with a certified Λ_{ρ,τ}(σ₁) > 0, a discrete
system with E ≥ −τ (e.g. greedy with threshold τ) has N − ρu = O(u^θ) for some θ < σ₁/2 — with τ = 1/100, any θ < 0.4945, for any of
the five densities of §4. By s40 Prop. 2.1 (with threshold τ: E = 1 − τ just after a prime and −τ just before the next, so
C(p_k, p_{k+1}) = ρg_k − 1 and E ≤ ρG(x) − τ), g-prime gaps O(x^θ) suffice. Not proved; not even E = o(x) (U3's question).
**6.2 Constraints on any proof (from §2–§3).** A proof (i) cannot fix the primes in advance to sub-square-root accuracy (Thm 2.1:
the primes of every (B)-system are wild at scale u^{½−ε}, Cor. 2.3); (ii) cannot gain from look-ahead over the composites already
determined (Prop. 3.1); (iii) cannot tune constants at small scales by design, except through N itself (Prop. 3.2: the density
constant ρe^{η̂(1)} is a global functional); (iv) cannot be a scale induction that uses only bounds on E, or prime counts in windows of
length ≫ v^θ, at smaller scales, uniformly over early-placement rules (Prop. 3.3: aligned bunching keeps all such bounds and breaks the
next scale). It must use the fine positions of the specific rule's primes — for greedy, the idle set of the queue — at all smaller
scales.
**6.3 The mean, written exactly** [proved here, from the multiplicative structure]. For a window W at scale y, with ϑ(W) := Σ_{p∈W}log p,
Σ_{n∈W}log n = Σ_{m∈G}ψ(W/m) (each n = d·m with d a prime power, m ∈ G), hence
  ϑ(W) = Σ_{n∈W} log n − Σ_{m∈G, m>1} ψ(W/m) − Σ_{p^k∈W, k≥2} log p.
With N(W) = ρ|W| + ΔE(W), Lemma M (ϑ(W) ≥ c|W| for |W| ≥ log³y) is equivalent to the one-sided bound
  Σ_{m∈G, m>1} ψ(W/m) ≤ (ρ log y − c)|W| + O((1 + |ΔE(W)|) log y + |W|²/y),
an upper bound for the sum, over all dilated windows W/m at smaller scales, of the system's prime counts there — for greedy, of the
queue's idle steps. Its mean is fixed by global constants (Σ_{m≤y}1/m = ρ log y + c_G + o(1), c_G = 1 − ρ + ∫_1^∞E(u)u^{−2}du), and the
content of Lemma M is that **the idle sets of the queue at different scales never line up under dilation by g-integers beyond
fluctuations of order |W|/log y**. Prop. 3.3 shows that line-ups are possible inside R(w); the data (§5: margin ≥ 0.72 at |W| = log³x to
10⁸) say greedy does not produce them. This decorrelation statement is the missing estimate, stated for the rule itself.
**6.4 Untried, and where it belongs.** (a) Measure the cross-scale correlation of the idle sets directly (the sum in 6.3 split by the
size of m), and look for a monotone quantity controlling it — U7. (b) Push Theorem 4.1 with more forced g-integers (for greedy, p₂, p₃
are explicit, and the powers and products of the first r primes are forced): it should move σ_L for τ = ½ from 0.763 toward the
measured 0.795 and give closed-form certificates for every τ — a cheap extension. (c) For U6: locating the zero no longer needs a
computed certificate (Thm 4.1 suffices); an ordering-certified run of greedy with τ = 1/100 to 10⁹–10¹⁰ is the informative computation,
since U predicts (Cor. 4.4) that its integer error must eventually reach u^{0.4945}. (d) For U5: an obstruction to U's failure must now
handle never-undershooting systems whose real zero is within τ of 1 (Prop. 4.3), and Remark 4.5 is the quantitative form of "no real
zero ⟹ undershoot".
