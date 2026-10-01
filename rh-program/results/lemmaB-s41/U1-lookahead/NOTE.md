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
