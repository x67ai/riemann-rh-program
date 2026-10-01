# NOTE — unit `free-greedy-s40/theory`: S8, the free greedy system — identities, mechanism, proof problem

Session 40, started 2026-10-01 11:25 IST. Writer: Opus 5.5 (agent). Labels as in the charter §4: **[proved here]**, **[computed]**
(script + log in `verify/`), **[quoted]** (source at page/line, in `sources/` or the named folder), **[recalled, unverified]** (never
load-bearing), **[novelty: single-check]**. Notation: S8(ρ) as in `../CHARTER.md` §1; t := 1/ρ; T(x) = ρ(x − 1) + 1; N, π = π_P, C =
composites, E = N − T, D = −E, V(x) = ρ(x − 1) − C(x); counting functions are right-continuous (count ≤ x).

## §0. Close

**Close: T + G** (no K against the construction; stop conditions (a), (b), (d) not met, (c) not met: neither route closes).
**The finding that reorganizes the problem — Theorem 1.6** [proved here; novelty: new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén (both reads: rF:35, rO:221–224; §5)]: for ANY
discrete Beurling system with R(u) := N(u) − ρu ≥ r₀ > 0 for all u ≥ 1 and R = O(u^θ) (any constant), ζ_P(σ) ≥ r₀ − ρσ/(1 − σ) on (θ, 1),
so if θ < r₀/(r₀ + ρ), ζ_P has a REAL zero σ* ∈ [r₀/(r₀ + ρ), 1) and α ≥ σ*. An integer count that never dips below its linear part forces a Siegel-type
zero; ℕ escapes only because ⌊u⌋ − u ≤ 0. S8's greedy rule gives r₀ = ½ − ρ for free (E > −½, Lemma 1.1), hence (Cor. 1.7):
**for ρ < ¼, Conjecture U is false as soon as S8(ρ) has N(x) − ρx = O(x^θ) for some θ ≤ ½ − ρ** — no box, no Rouché margin, no explicit
constant, no computation. With finite certificates (§4.1; F_{10⁷}(0.79) = +0.0222 for π/16, F_{10⁶}(0.89) = +0.0434 for π/32, ordering margins ≥ 5.1·10⁻¹³ (π/16, both decision classes) and ≥ 7.6·10⁻¹⁰ (π/32) relative there, against ≲ 10⁻¹⁵ rounding; reproduced by an independent double-double generator with every close decision re-checked at 60 digits, read-O §2) the needed exponent relaxes to θ < 0.395 (π/16) and θ < 0.445 (π/32). Dichotomy: either U fails, or
these two explicit queue-like systems have β > 0.395 and β > 0.445 — while their measured sup E is 0.049·log²x (π/16, flat on 10⁶–10^7.5) and
0.029·log²x (π/32, to 10⁸; local exponent 0.04 on the last decade).
**T — proved, complete on the page:** Lemmas 1.0–1.5 (well-definedness; E > −½; primes on the lattice 1 + (k − ½)/ρ, gaps ≥ 1/ρ; free
monoid for transcendental 1/ρ; the reflection identity π = ⌊sup V + ½⌋, E = drawdown + r, r ∈ (−½, ½], exact when no composite sits on the
lattice — with ties the floor overcounts by one and the hitting-time form is the right one; the template ζ_c = (s − 1 + ρ)/(s − 1), prime
density (1 − u^{−ρ})/log u, ζ_P = ζ_c + sÊ); Theorem 1.6, Remark 1.6′, Cor. 1.7; Prop. 2.1 (E = ½ + composites − ρ·elapsed on every
prime gap, so E ≤ ρ·(largest gap) − ½: clipping is the only source of E beyond rounding); the Legendre form π(I) = ρ|I|M(√b) + ΔE(I) +
S(I) with the unconditional margin M(z) ≥ M_lat(z) ≍ z^{−ρ} (§3.4); the Dichotomy (§3.0); Theorems 4.1–4.2 (real-zero brackets).
**G — the exact missing estimate:** **Lemma B_ρ** — for one ρ < ¼, the integer error of S8(ρ) is O(x^θ) for some θ ≤ ½ − ρ (qualitative).
Sufficient forms: Lemma G_ρ (g-prime gaps O(x^θ)); Lemma S (the one-sided bound S(I) ≥ −½ρ|I|M(√u) − O(u^θ) on the Möbius sum S(I) of E-increments at smaller scales; two-sided square-root cancellation in S(I) is FALSE for S8 — S(u, 2u] carries the Mertens bias (1 − 2e^{−γ} + o(1))u/log u, read-O F1 — so the sieve form is a short-interval prime statement, not a PNT-free shortcut). Routes (a) (randomized
placement + Freedman) and (b) (potential function) both control fluctuations around a compensator and break at bounding the compensator
(Lemma M), which is a short-interval PNT for the system — the same statement again; route (a)'s missing estimate in analytic form is a
zero-free strip with growth bounds (Lemma Z). Randomization is numerically COUNTERPRODUCTIVE (§3.1: offsets of width 50 raise sup E at
10⁷ from 12.8 to 58–171): S8's regularity is a deterministic, sub-Poissonian correlation effect.
**Mechanism (task 2), tested:** E is exactly a queue content (Prop. 2.1); the Poisson-queue heuristic gets the law right (polylog E, tail
rate ∝ 1/(ρ log x)) and the constant wrong by a factor 1.45–1.65, found by two producers (π/16 here, π/4 by the compute unit to 10⁹);
sup E ≈ (0.20–0.37)·ρ·log²x for ρ ∈ [π/64, π/4] at X = 10⁶ (0.43 at 0.95π/3), around the sub-Poisson prediction 0.3ρ. The real zero is the template zero 1 − ρ displaced by ρζ_P(1 − ρ) (first-order law accurate to
4·10⁻⁴ for ρ ≤ π/16); for ρ ∈ (¼, π/4] it is a nonlinear zero in (½, 0.66) (π/4: 0.514); at ρ ≈ 1 it drops below ½. For π/16 it is the
rightmost zero below height 60 (exploratory count; one complex zero at 0.5733 + 30.7797i). Nothing printed or measured forces sup Re = 1.
**Prior art (§5; Opus side of the dual check):** stop conditions (a), (b) not met. Nearest printed object: Broucke–Debruyne–Révész
Thm 1.3 (RH-conditional; real zero at α ∈ (½, ⅔) with β ≥ 2α/(α + 2) — it obeys U). S8's template is Diamond 1970 p. 24 (continuous;
this settles the orchestrator's question: Diamond's "quite simple examples" are continuous, simplifying Malliavin 1961 §6, whose discrete
variant has no integer bound). Lagarias 1999 does not apply (S8 is not in ℤ⁺ and not uniformly discrete). No feedback or integer-first
construction and no one-sided ⇒ real-zero lemma in print; BDR p. 17 call the integer-first route natural but "extremely difficult" for
the primes, and Theorem 1.6 is that difficulty resolved for never-undershooting systems.
**For the compute unit:** include t = 0 in every zero search; sup E and the largest g-prime gap for π/16 and π/32 to 10⁹–10¹⁰ with the
double-double generator are now the most informative numbers for U.

## §1. The exact identities (task 1)

**1.0 Construction (well-definedness)** [proved here]. Let p₀ := 1. Given p₁ < … < p_k, let G_k be the multiset of finite products of
p₁, …, p_k (G₀ = {1}), N_k(x) := #(G_k ∩ [1, x]) with multiplicity, D_k(x) := T(x) − N_k(x), and p_{k+1} := inf{x ≥ p_k : D_k(x) ≥ ½}.
Claims, by induction on k: (i) p_{k+1} < ∞ and D_k(p_{k+1}) = D_k(p_{k+1}−) = ½, so no element of G_k sits at p_{k+1}; (ii) N(x) = N_k(x)
for x < p_{k+1}, where N counts the full multiset G = ∪G_k, and N(p_{k+1}) = N_k(p_{k+1}) + 1, so D(p_{k+1}) = −½; (iii) p_{k+1} ≥ p_k + t for k ≥ 1 (p₁ = 1 + t/2).
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
*When ties cannot occur* [proved here]. If t = 1/ρ = p/q in lowest terms with p ODD, lattice points are (2q + (2k − 1)p)/(2q), odd
numerator over 2q; a product of j ≥ 2 g-primes has odd numerator over (2q)^j, a lattice point written over (2q)^j has numerator
odd·(2q)^{j−1}, even. So no composite ever sits on the lattice and Lemma 1.4 holds exactly. This covers the charter's control ρ = 0.8
(t = 5/4, primes (10k + 3)/8) — although there EQUAL composites (multiplicities) do occur: (33/8)(1743/8) = (83/8)(693/8), and 25,180 equal-valued pairs below 10⁶ (read-O, exact integers). With p even
(e.g. ρ = ½: primes at even integers, 2·4 = 8 on the lattice) ties do occur.
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

**Theorem 1.6 (one-sided integer regularity forces a real zero)** [proved here] [novelty: new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén (both reads: rF:35, rO:221–224)]. Let P be any discrete Beurling
system (g-primes 1 < p₁ ≤ p₂ ≤ …, N counted with multiplicity), ρ ∈ (0, 1), E(u) := N(u) − ρ(u − 1) − 1, and suppose
(A) E(u) ≥ −c for all u ≥ 1, some c ∈ [0, 1); (B) E(u) = O(u^θ) for some θ < 1 (no constant needed).
Then for θ < σ < 1 (θ ≥ 0 is automatic: E jumps by integers): ζ_P(σ) ≥ 1 − c − ρ/(1 − σ). If σ₀ := 1 − ρ/(1 − c) > θ, then ζ_P has a real zero σ* ∈ (σ₀, 1) (open at σ₀ because E, strictly decreasing between consecutive g-integers, equals −c only on a countable set; for continuous systems the closed endpoint can be attained, e.g. by the template), and ψ_P(x) − x ≠ O(x^a) for every a < σ*: P is an [α, β]-system with α ≥ σ* and β ≤ θ.
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
| π/32 = 0.0982 | 0.8037 | 0.9018 | 0.895076 (10⁶), 0.895077 (10⁸) | 6.39 (10⁶), 9.86 (10⁸) | 0.034, 0.029 |
| π/16 = 0.1963 | 0.6073 | 0.8037 | 0.794752 (10⁶), 0.794755 (10⁷, 5·10⁷) | 9.64 (10⁶), 12.84 (10⁷), 14.71 (10^7.5) | 0.050, 0.049, 0.049 |
| π/8 = 0.3927 | 0.2146 | 0.6073 | 0.656529 | 15.35 | 0.080 |
| π/6 = 0.5236 | < 0 | 0.4764 | 0.521753 | 21.33 | 0.112 |
| π/4 = 0.7854 | < 0 | 0.2146 | 0.514036 (10⁶); F_X(½) = 0.06707 at 10⁷ | 39.53 | 0.207 |
| 0.95π/3 = 0.9948 | < 0 | 0.0052 | 0.402156 | 82.38 | 0.432 |

Every F_X respects the floor ½ − ρ/(1 − σ) of Theorem 1.6 (`rz_pi16_1e6.log`, columns 2 and 4). For ρ ≤ ¼ the zero is the template's
zero 1 − ρ moved left by 0.003–0.009; for ρ ∈ (¼, π/4] it sits in (½, 0.66) though Theorem 1.6 alone gives nothing there; at ρ ≈ 1 it
falls below ½ (ℕ itself, ρ = 1 and E = −{x} ∈ (−1, 0], has ζ < 0 on (0, 1) and no real zero).

## §2. The mechanism (task 2)

**Proposition 2.1 (gap identity)** [proved here]. Let g_k := p_{k+1} − p_k and C(a, b) the number of composites in the open interval.
for k ≥ 1: (i) E(x) = ½ + C(p_k, x] − ρ(x − p_k) for x ∈ [p_k, p_{k+1}); (ii) ρg_k = 1 + C(p_k, p_{k+1}); (iii) sup_{u≤x}E(u) ≤ ρG(x) − ½, G(x) :=
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
*Clipping is the only source of positive E beyond rounding* [proved here, from Prop. 2.1]: E = ½ at every prime, and E(x) − ½ =
C(p_k, x] − ρ(x − p_k) inside a gap, so E exceeds ½ exactly when composites outpace the rate ρ — when the prime density the loop
would need, ρ − (composite rate), is negative and the rule can only refuse. In the brief's normalization: with a signed prime measure
the loop could track T up to rounding; the actual measure is that signed one plus a clip measure κ ≥ 0, and to first order
sÊ = ζ_c·κ̂, so the neutral modes (zeros of ζ_P) are where the clip's transform is resonant.
*Remark 1.6′ (the cleanest form of Theorem 1.6)* [proved here]. If R(u) ≥ r₀ > 0 for all u and R = O(u^θ) with θ < r₀/(r₀ + ρ),
then ζ_P(σ) ≥ r₀ − ρσ/(1 − σ) > 0 for θ < σ < r₀/(r₀ + ρ), and ζ_P has a real zero in [r₀/(r₀ + ρ), 1). An integer count that never dips
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
sup E/log²x = 0.018, 0.034, 0.050, 0.080, 0.112, 0.207 at ρ = π/64 … π/4 (§1.8), i.e. (0.37, 0.34, 0.26, 0.20, 0.21, 0.26)·ρ, scattered around the 0.3ρ predicted.
Second route, independent code (compute unit, ρ = π/4 to 10⁹, `SHARED.md` batch 1): tail rate λ with λ·log x ≈ 3.7–3.9 over
10⁶–10⁹ against 2/ρ = 2.55, ratio 1.45–1.55 — the same factor as here for π/16; sup E = 95.86 (0.223·log²x at 10⁹).
The heuristic's law — polylogarithmic E, tail rate ∝ 1/(ρ log u) — matches; its constant does not, and the discrepancy (sub-Poisson
variance) is the trace of the correlations a proof would have to control.

**2.4 Real parts.** Hilberdink 2005 Cor. 2(b) [quoted: `novel-wave-s37/beurling-frontier/sources/w-18a…txt` l. 210–213, JNT 112
p. 336]: if N_P(x) = ρx + O(x^β), β < ½, then for every γ ∈ (β, ½), ψ_P(x) − x = Ω(x^γ) and ζ_P has infinitely many zeros in
γ < Re s < 1. So (B) with θ < ½ forces infinitely many zeros right of θ, not right of ½; nothing printed that we have read forces
sup Re = 1. The real zero is a fixed σ* < 1, stable to 3·10⁻⁶ between 10⁶ and 10⁷ (π/16). Whether complex zeros climb toward 1
is the compute unit's question (its task 3(ii)); see §4 for what arrives.
*Exploratory count, π/16* [computed, not a certificate: `verify/s8_wind.py`, `s8_newton.py`, logs `wind_pi16_1e5.log`,
`newton_pi16.log`]: argument principle for F_{10⁵} gives winding 0 on [0.80, 0.99] × [0.5, 60] (min|F_X| = 0.52 on the boundary) and 1
on [0.55, 0.80] × [0.5, 60], the zero sitting in [30, 45]; Newton: 0.573197 + 30.779514i (X = 10⁵), 0.573259 + 30.779677i (10⁶). So below
height 60 the real zero σ* = 0.7948 is the rightmost zero, and α(S8(π/16)) should equal σ* if no zero far up lies further right.
*Heuristic for the complex zeros* [heuristic, not proved]. ζ_P(s) = Σ_{n≤|t|}n^{−s} + (rest), and the rest is governed by E: beyond
u ≈ |t| the oscillation u^{−it} is slower than E's unit-scale jumps and only E's slow (polylog) variation survives, so the tail is
O(|t|·polylog·|t|^{−σ}); the head Σ_{n≤|t|}n^{−s} behaves like a sum with independent phases of size (Σ n^{−2σ})^{1/2} ≈ |t|^{½−σ} for
σ < ½ and O(polylog) for σ > ½. So |ζ_P| should be Lindelöf-like for σ > ½ and grow like |t|^{½−σ} for σ < ½; Jensen's formula then
puts the bulk of the zeros near σ = ½, with the real zero and a sparse set of exceptions to the right. Nothing in this picture forces
sup Re = 1, and nothing gives a zero-free strip either; a density estimate of Révész type (§5) bounds how sparse the exceptions are.

## §3. The proof problem (task 3)

**3.0 What is left after Theorem 1.6.** The contract asks for (i) a PROVED integer bound and (ii) a certified zero. Theorem 1.6 makes
(ii) free for any system whose integer count never undershoots: if R(u) = N(u) − ρu ≥ r₀ > ρ, then (B) with ANY θ < ½·r₀/(r₀ + ρ)
gives α ≥ σ* > max{½, 2θ} and U fails — no box, no Rouché margin, no explicit constant. For S8(ρ), r₀ = ½ − ρ, so everything rests on
> **Lemma B_ρ.** For S8(ρ) with some ρ < ¼: N(x) − ρx = O(x^θ) for some θ ≤ ½ − ρ (data: O(log²x)).
With the finite certificate of Cor. 1.7(iii) the exponent can be relaxed to θ < σ₁/2 where F_X(σ₁) > ½X^{−σ₁}: for ρ = π/16,
F_{10⁷}(0.79) > 0 (σ* = 0.794755), so θ < 0.395 suffices; for ρ = π/32, F_{10⁶}(0.89) > 0 (`verify/bracket_pi32_1e6.log`), so θ < 0.445.
**Dichotomy** [proved here, from Theorem 1.6]. For each ρ < ¼: either Conjecture U fails, or β(S8(ρ)) > ½ − ρ (if β ≥ 1 − 2ρ this is
trivial; if β < 1 − 2ρ, Theorem 1.6 gives α > 1 − 2ρ ≥ ½ and U forces 2β ≥ α). Certified: β(S8(π/16)) > 0.395 (from F_{10⁷}(0.79) > 0),
β(S8(π/32)) > 0.4018 by Theorem 1.6 alone and > 0.445 from F_{10⁶}(0.89) = +0.0434 > 0; numerically σ*/2 = 0.397 and 0.448. The data (§1.8, §2.3) show sup E ≈ 0.049 log²x for π/16 over four decades (local exponent 0.12 on
[10⁶, 10⁷]). U, if true, would force this explicit queue-like system to develop power-law excursions of exponent > 0.395. For π/32 to 10⁸
(`verify/mech_pi32_1e8.log`, 31 s, 3.2 GB) [computed]: sup E = 4.83, 6.39, 8.93, 9.86 at 10⁵…10⁸ (sup E/log²x = 0.036, 0.034, 0.034, 0.029;
local exponent 0.04 on the last decade) against U's certified > 0.445; largest g-prime gap 397 = 1.17·log²x; σ* = 0.895077. Caveat: the
double run's ordering margin falls to 6.5·10⁻¹⁵ (relative) at 7.1·10⁷, about twice the rounding bound, so it is certainly S8 only below
that point — immaterial for these statistics, decisive for a certificate (use the compute unit's double-double generator).
By Prop. 2.1, Lemma B_ρ follows from **Lemma G_ρ**: the g-primes of S8(ρ) have gaps O(x^θ) (data: G(x) ≈ 1.3 log²x for π/16).

**3.1 Route (a): randomized placement + martingale concentration — breaks at the compensator.**
*Rule S8^w.* Composites below a point y involve only g-primes below y/p₁, so the deficit time x*_k (the first point where D, computed
with p₁, …, p_{k−1}, reaches ½) is known before any prime near it must be placed. Place p_k uniformly in [max(x*_k − w, 1 + t/2), x*_k], independently (a draw ≤ 1 is not a g-prime; the runs place p₁ at its deficit time)
(early placement — the brief's late window [x*, x* + w] would let E dip to −½ − ρw and shrink r₀ to ½ − ρ − ρw). [proved here]: for every
realization, E > −½ (no prime comes after its deficit time, so D < ½ throughout), so r₀ = ½ − ρ and Theorem 1.6 applies to EVERY
realization that satisfies (B); E ≤ (excursion) + ρw. Hence **U is refuted as soon as S8^w satisfies (B) with positive probability**
(probabilistic method; the realization need not be computed).
*The rule tested* [computed: `verify/s8w_block.py` (block generator: composites in [B, p₁B) use only g-integers below B, so early primes
cause no ordering problem; w = 0 reproduces S8 exactly — N, π, sup E, σ* identical to `s8_mech.py`), logs `s8w_pi16_1e6_sweep.log`,
`s8w_pi16_1e7_w50.log`]. ρ = π/16, X = 10⁷ (10⁶ in brackets), two seeds: w = 2.5 (half a prime spacing): sup E = 11.30 [9.78, 8.51]
vs 12.84 [9.64] deterministic; w = 10: [15.74, 11.51]; w = 50: 58.2 and 171.2 [34.0, 82.0], i.e. 0.22 and 0.66·log²X, the second seed
growing by 2.1 per decade (local exponent 0.32). Every realization has inf E(x−) = −½ exactly (at p₁, placed at its deficit time) and E > −½
after every event, as proved. The real zero moves right with w: σ* = 0.809/0.801 (w = 2.5), 0.848/0.824 (10), 0.867/0.878 (50); π(10⁷)
falls from 633,514 to 556,046–626,208 (earlier primes give earlier composites). **Randomization makes the integer error WORSE**: the
deterministic composite stream is sub-Poissonian (§2.3) and random offsets of width ≫ t destroy that order. So the regularity of S8 is a
deterministic correlation effect, and route (a) must work with a rougher system than the one it is meant to explain; for U this is
harmless only if S8^w still has θ ≤ ½ − ρ, and the w = 50 data do not show that cleanly.
*Concentration step.* Order the primes; F_k = σ(p₁, …, p_k). For an interval I, C(I) = Σ_k Y_k with Y_k := #{n ∈ I composite : the largest INDEX among n's prime factors is k} (for w > t
positions need not increase with the index), which is F_k-measurable. Doob: C(I) = Σ_k(Y_k − E[Y_k|F_{k−1}]) + A(I), A(I) := Σ_k E[Y_k|F_{k−1}] (the
compensator: each prime's contribution averaged over its own window, the rest frozen). Freedman's inequality [recalled, unverified:
D. Freedman, Ann. Probab. 3 (1975), Thm 1.6] would give, uniformly over a weighted countable net of intervals, with positive
probability, C(I) ≤ A(I) + O(√(A(I)·log y) + M log y), M = max Y_k (bounded by the local density of g-integers at scale y/p_k, itself an
inductive hypothesis). Then E ≤ polylog would follow from Cor. 1.4′ IF
> **Lemma M (compensator).** For all y and all I ⊂ [y, 2y] with |I| ≥ log³y: A(I) ≤ ρ|I| − c|I|/log y, some c > 0.
(For |I| < log³y the excess C(I) − ρ|I| ≤ C(I) is bounded by the local density; for |I| ≥ log³y the slack c|I|/log y beats the deviation
√(|I| log y).) This is the step on which route (a) BREAKS, at this line: A(I) = Σ_{m∈G}∫_{I/m} ω_m(v)dv, where ω_m(v) = (1/w)#{k : v ∈ W_k,
P⁺(m) < p_k} is the window density of primes at scale v = u/m — so A is the composite count with each dilate m·P smoothed over width
w·m. By N = 1 + π + C and Prop. 2.1, C(I) = ρ|I| − π(I) + ΔE(I), so A(I) ≤ ρ|I| − c|I|/log y is equivalent (up to smoothing errors) to
"the smoothed system leaves room for ≥ c|I|/log y primes in every such I": a short-interval lower bound for the primes of the system at scale log³y — it implies Lemma G (gaps ≪ log³y), not conversely. The induction on dyadic blocks does not close: A(I) is past-measurable (for ρ ≤ ½ it depends only on g-primes below y),
but no hypothesis on scales below y that we can formulate bounds it, because the first-order expansion of A around the template,
A(I)/|I| ≈ ρ − π_c′(u)(1 − Ê(1)) + Σ_m π_c′(u/m)δ(u/m)/m (δ = relative deviation of the smoothed prime density at scale u/m), has its
two correction terms of the same order as the margin π_c′(u) ≈ 1/log u; they must cancel to leading order (the residue of ζ_P at 1 is
exactly ρ), and that cancellation is a global Mellin identity, not a local inequality. Widening the window (w ≍ log⁵y, still with
E > −½ by early placement) kills the ΔE/w smoothing errors but not this cancellation problem.
*What would close it.* Lemma M follows from a smoothed PNT with relative error o(1/ log u) uniformly in mesoscopic windows, which in turn
follows from a zero-free strip Re s > 1 − δ for ζ_P with polynomial growth there [recalled, unverified: the standard explicit-formula
argument]. So route (a) converts Lemma B into **Lemma Z: ζ_{S8^w} has a zero-free strip Re s > 1 − δ with |ζ_P|^{±1} ≪ |t|^A there** — a
statement about the infinite system that is itself not available without (B). Recorded as the exact missing estimate of route (a).

**3.2 Route (b): derandomization by a potential function — breaks at the same line.** Choose p_k among K candidates in [x*_k − w, x*_k]
to minimize Φ_k = Σ_I λ_I^{-1}·cosh(λ_I(C_k(I) − A_k(I))) over a weighted countable family of intervals (dyadic lengths, grid of
left ends, all scales; weights summable), where C_k(I) and A_k(I) are the partial sums of Y_j and of their candidate-averages, j ≤ k.
The decision at step k changes only Y_k(I), a known function of the candidate (the composites whose largest-index prime is p_k are
fixed once p_k is), bounded by M; the averaging argument (E over a uniform candidate of Φ_k ≤ Φ_{k−1}·(1 + O(λ²·Var))) gives, for a
deterministic explicit rule, |C(I) − A(I)| ≤ O(√(A(I)·log(1/weight_I)) + M log(1/weight_I)) for all I in the family — this part is the
standard Spencer–Raghavan potential argument [recalled, unverified; not written out here, not needed below]. It controls the
FLUCTUATION of the composite count around its candidate-average, exactly like 3.1, and leaves the MEAN A(I) untouched: route (b)
reduces to Lemma M with A the candidate-average, and breaks at the same line. The brief's implication "square-root discrepancy for
composite counts suffices for polylog E, because intervals longer than log³x have slack |I|/log x" is correct as a lemma (Cor. 1.4′
plus the arithmetic in 3.1) [proved here, given its hypothesis] — but the slack |I|/log x is a property of the MEAN, and the mean is
what neither route can bound.

**3.3 Route (c): what is proved completely, and the exact missing estimate.**
*Proved (unconditional, complete on the page):* Lemmas 1.0–1.5, Theorem 1.6 and Remark 1.6′ (one-sided integer regularity ⇒ real
zero ⇒ α ≥ σ*), Cor. 1.7 (for S8(ρ), ρ < ¼: (B) with θ ≤ ½ − ρ refutes U), Prop. 2.1 (E ≤ ρ·(prime gap) − ½), the Dichotomy of 3.0.
*Not obtained:* any unconditional upper bound on E for S8 or S8^w — not even E = o(x). Every attempt (crude counting by smallest or
largest prime factor; the Chebyshev identity Σ_{n∈J}log n = Σ_d Λ(d)N(J/d); the self-limiting argument "no primes ⇒ only y-smooth
composites") needs the composite density to stay below ρ by a margin, which is the PNT for the system, which needs (B).
*G — the exact missing estimate.* **Lemma B_ρ** (3.0) for one ρ < ¼; by Prop. 2.1 it suffices to prove **Lemma G_ρ** (g-prime gaps
O(x^θ), θ ≤ ½ − ρ); routes (a)/(b) reduce it further, for the randomized rule, to **Lemma M**, which is implied (via the explicit formula) by **Lemma Z** (zero-free strip with growth bounds) for S8^w. Evidence for B_ρ: §1.8 and §2.3 (sup E/log²x flat, 0.049 for π/16 on
[10³, 10⁷]; gaps G ≈ 1.3 log²x); the analog of Lemma H of `u-offsurgery-s39/NOTE.md` §4, with two differences that matter: B_ρ is
qualitative (no constant, any θ ≤ ½ − ρ), and S8 has no multiplicity mechanism (Lemma 1.3) of the kind that sank S5.
*Why it is hard, stated as a fact about the literature (to be checked in §5):* every discrete system with PROVED β < ½ that we know is
arithmetic (ℕ, ideals of number fields, finite modifications of these), and for every such system ζ_P is ζ_K times a factor positive
on (0, 1), hence negative on (0, 1) when ζ_K is — so by Remark 1.6′ none of those with ζ_K < 0 on (0, 1) can satisfy R ≥ r₀ > ρ (for a field with a Siegel zero the question is open: Theorem 1.6 is a Siegel-zero criterion there). A proof of B_ρ would be the
first sub-square-root integer bound for a non-arithmetic discrete system; that is Diamond–Montgomery–Vorhauer's open question
(p1-02 p. 4) in the discrete case, now in the sharp form "one-sided regularity + O(x^θ)".

**3.4 The sieve form of the missing estimate** [proved here unless marked]. Freeness (no ties needed: multiples of a squarefree d in
the free monoid are exactly d·G; so t transcendental, and with N := 0 below 1, i.e. ΔE(J) = −ρ|J| for J ⊂ (0, 1), for the terms d > b) gives Legendre's identity for the system: for I = (a, b] with a ≥ √b,
π(I) = Σ_{d | P(√b)} μ(d)·#(G ∩ I/d), P(z) := product of the g-primes ≤ z (a g-integer in I with no g-prime factor ≤ √b is prime).
Inserting #(G ∩ J) = ρ|J| + ΔE(J) and telescoping Σ_{q≤z}(1/q)Π_{p<q}(1 − 1/p) = 1 − M(z), M(z) := Π_{q≤z}(1 − 1/q):
  π(I) = ρ|I|·M(√b) + ΔE(I) + S(I),  S(I) := Σ_{d | P(√b), d > 1} μ(d)·ΔE(I/d).
So on a prime gap I (π(I) = 0): ΔE(I) = −ρ|I|M(√b) − S(I). The composites' "mean" deficit ρ|I|M(√b) is an exact function of the
g-primes ≤ √b — no PNT enters — and it has an unconditional floor: the g-primes are a subset of the lattice 1 + (ℤ_{≥1} − ½)t, so
M(z) ≥ M_lat(z) := Π_{lattice points ≤ z}(1 − 1/·) ≍ z^{−ρ}. Data (`verify/s8_mertens.py`, π/16, 10⁶) [computed]: M_lat(z)·z^ρ → 1.0127
(constant from z = 10³ on); M(z)·log z = 2.54, 2.70, 2.78, 2.81 at 10³…10⁶ (a Mertens law with constant ≈ 2.8–2.9); Legendre's
identity checked exactly on three intervals of length 200 near 2.5·10⁵ and 3.3·10⁵.
**Lemma S (the missing estimate in sieve form).** For all u and all intervals I ⊂ [u, 2u]: S(I) ≥ −½ρ|I|M(√u) − O(u^θ).
By the gap identity, Lemma S for ALL I gives E ≤ O(u^θ) + ½ directly (E(x) − ½ = −ρ|I|M − S(I) on I = (p_k, x]).
Two conditional consequences of the floor M ≥ M_lat — both VACUOUS, because their hypothesis is false for S8 (read-O F1: it would force ψ_P(x) ~ 2e^{−γ}x via Diamond–Zhang Thm 5.10): (i) square-root cancellation with polylog loss, |S(I)| ≪ √|I|·log u + log²u, would give
E ≤ max_h(−ρhM + √h·log u) + log²u = log²u/(4ρM(√u)) + log²u ≪ u^{ρ/2}·log²u (the arithmetic is right; the hypothesis is not);
U needs θ ≤ ½ − ρ, true for all ρ < ⅓, which covers the range ρ < ¼ of Theorem 1.6; (ii) the Mertens law M(z)·log z → e^{−γ}/ρ is a theorem once N ~ ρx (Diamond–Zhang Thm 5.10; 2.8595 for π/16, data 2.78 at 10⁵); with it a one-sided bound S(I) ≥ (1 − 2e^{−γ} − δ)|I|/log u − O(√|I|·log u) would give E = O(log³u), but that bound is a lower bound for primes in all intervals of length ≫ log⁴u. The data's E ≍ log²u, ∝ ρ (§2.3), show that S cancels even better
than independent increments would (independence gives Var S(I) ≈ ρ|I|·Σ_{d|P}1/d ≍ ρ|I| log u, while Var C(I) ≈ 0.6ρ|I| is measured
through the tail rate): the increments ΔE(I/d) at different scales are strongly anti-correlated, as the identity forces.
The trivial bound |S(I)| ≤ 2·sup|E|·#{d} is of size u, which is why Legendre's sieve, here as for ℕ, gives nothing by itself.
Lemma S is a Möbius-cancellation statement for E at smaller scales; it implies Lemma B (by the identity above; the converse would need π(I) ≥ ½ρ|I|M(√u) − O(u^θ) on every I), so it is a
reformulation, not progress — but it isolates the one place where randomness (route (a)) would have to act: the ΔE(I/d) for different
d live at different scales; the predictable part (E's drift at scale u/d) CANNOT be uncorrelated with μ(d): the correlation is what produces the Mertens bias (1 − 2e^{−γ})|I|/log u of S(I) (read-O F1), so a martingale argument can at most control fluctuations around that bias, i.e. give a one-sided statement.

## §4. The Rouché theorem for S8 (task 4) — superseded on the real axis by Theorem 1.6

**4.1 Real zeros: the certificates** [proved here, modulo the floating-point evaluation below] [computed: `verify/s8_bracket.py`,
`bracket_pi16_1e7.log`, `bracket_pi4_1e7.log`]. Tail bound used for the upper end (only the UPPER side of E is needed there; the lower
side is Lemma 1.1): if E(u) ≤ K log²u for u > X, then σ∫_X^∞E u^{−σ−1}du ≤ K·σX^{−σ}(log²X/σ + 2 log X/σ² + 2/σ³) =: K·τ_X(σ).
*Theorem 4.1 (S8(π/16)).* (i) If E(u) = O(u^θ) for some θ < 0.79 (any constant), ζ_P has a real zero in (0.79, 1): F_{10⁷}(0.79) =
+0.022231 > ½·10^{−5.53} = 1.5·10⁻⁶, so ζ_P(0.79) > 0 by Lemma 1.1, and ζ_P → −∞ at 1⁻. Hence α > 0.79, and if θ ≤ 0.395, **U is false**.
(ii) If moreover E(u) ≤ 33.7·log²u for u > 10⁷, the zero lies in (0.79, 0.80): F_{10⁷}(0.80) = −0.025711 and τ(0.80) = 7.616·10⁻⁴
(margin: measured sup E/log²x ≈ 0.049, a factor 690 below 33.7); with K < 121, in (0.78, 0.81).
*Theorem 4.2 (S8(π/4)).* (i) If E(u) = O(u^θ), θ < ½: real zero in (½, 1) (F_{10⁷}(½) = +0.067067 > 1.6·10⁻⁴); α > ½; U false if θ ≤ ¼.
(ii) If E(u) ≤ 3.78·log²u for u > 10⁷: zero in (0.50, 0.55) (F(0.55) = −0.173679, τ = 0.04591); if E(u) ≤ 0.3438·log²u: in (0.50, 0.52) (|F_{10⁷}(0.52)| = 0.025933, τ(0.52) = 0.075411)
(the compute unit's sup E = 95.86 at 4.85·10⁷ is 0.306·log²x there — inside 0.344 but with little room; `SHARED.md`, compute batch 1).
*For every ρ < ¼ no computation is needed* (Cor. 1.7(ii)); the computation only raises the floor from 1 − 2ρ to σ₁.
*Floating-point budget.* The deficit process sees only counts at the threshold times x* = 1 + (N − ½)/ρ; counting both decision classes (a composite just below its live threshold, or just above a threshold where a prime was placed), the closest call up to 10⁷ is 5.07·10⁻¹³ (π/16; 1.06·10⁻¹¹ for the first class alone) and 6.41·10⁻¹⁴ (π/4, a 4-factor product; 5.6·10⁻¹³ for the first class) in relative terms, against ≲ 10⁻¹⁵ rounding for that product and ≲ 10⁻¹⁴ for the longest products (up to 32 factors for π/4, 12 for π/16), and ρ itself is off by 4·10⁻¹⁷ relative. So the event order of the double-precision runs is exactly that of
S8(ρ) to 10⁷, positions are right to 3·10⁻¹⁵ relative, and |error of F_X| ≤ 10⁻¹² — negligible against every margin above. (The compute
unit found near-ties at relative 3.8·10⁻¹⁷ near 10⁹: past ~10⁸ only its double-double generator is S8.)

**4.2 Complex zeros: the K′ template, ready for the compute unit's box.** If B is a box in Re s > θ with winding number w of F_X on ∂B
and m_B := min_{∂B}|F_X|, and |E(u)| ≤ K log²u for u > X, then on ∂B the tail T_X(s) = s∫_X^∞E u^{−s−1}du satisfies
|T_X(s)| ≤ K·|s|·X^{−σ}(log²X/σ + 2 log X/σ² + 2/σ³), so ζ_P has exactly w zeros in B as soon as K < K_B := m_B / max_{∂B}(that factor),
by Rouché (ζ_P = F_X + T_X on Re s > θ, Lemma 1.5; B must avoid s = 1, where F_X and ζ_P share the pole — for a box containing 1 the winding number is zeros minus one). The analog of K′ then reads: "if |E(u)| ≤ K_B log²u for u > X, ζ_P has exactly w
zeros in B, α ≥ min Re B, and U is false if additionally β < min Re B / 2". Complex zeros are no longer needed for α > ½ (4.1 gives
it), but one with real part above σ* would relax the exponent needed in Lemma B_ρ (for π/4 from θ ≤ 0.257 to θ < Re/2).
Numbers: pending the compute unit's task 3(iii) box (see §0 for the state at close).

## §5. Prior art at the page (task 5)

Reader: an Opus subagent of this unit (the Opus side of the dual-model check; the orchestrator checks separately). Full record with
quotes at page/line: `sources/prior-art-log.txt` (24 entries, summary at its end); every source opened is saved as `sources/pa-*.txt`
(arXiv queries one at a time ≥ 6 s apart; Firecrawl used for two pages; the key was not written anywhere). All items below [quoted]
unless marked.
**Stop conditions.** (a) No printed theorem forbids θ < ½ with a zero right of ½ for discrete systems: Hilberdink 2005 Thm 1 (JNT 112,
p. 335) gives only max{α, β} ≥ ½, and Cor. 2(b) (p. 336) FORCES, for β < ½, infinitely many zeros in {η′ < Re s < 1} for every η′ ∈ (β, ½);
Neamah–Hilberdink (via Broucke–Vindas, z-18 p. 9: α = γ = Θ ≥ ½ when β < ½, γ the Möbius-sum exponent), Hilberdink–Kaziulyte 2023 and
Broucke–Hilberdink 2024 are Ω-lower bounds on prime irregularity — all consistent with S8, none an obstruction. (b) No printed
construction gives the target. Unconditionally there is no discrete system with θ < ½ and a zero right of ½ at all. Conditionally on RH,
Broucke–Debruyne–Révész (arXiv:2309.01567v2, Thm 1.3, p. 4; z-02 l. 183–184) give discrete [α, β]-systems with ½ < α < 2/3 and
2α/(α + 2) ≤ β < ½, whose zeta has a REAL zero at s = α (zeta_{α,β} = ζ(s)ζ(s/β)/ζ_S(s), ζ_S with a pole at α; derived from l. 1186–1200)
— the nearest printed object, and it obeys U (2β ≥ 4α/(α + 2) > α). At the boundary θ = ½, unconditional: Zhang 2007 / Diamond–Zhang
Thm 17.14 (N-error x^{½}e^{c(log x)^{2/3}}, zeros on σ = 1 − 1/log t), Révész IMRN 2023 Thm 8, Broucke arXiv:2409.10051 Thm 6.3.
Open-problem statements in print: DMV 2006 p. 4 ("it may still be the case that (3) with θ < ½ does imply RH for discrete Beurling
generalized numbers"); Diamond–Zhang p. 196 ("optimality is not known for θ ≤ ½").
**Q1 — feedback / greedy / integer-first constructions: not found** (Diamond–Zhang book grep; DMV; Zhang 2007 abstract; BDV 2020; BDR;
Broucke–Vindas; Révész; Broucke 2024–25; Hilberdink 2005/2012; Malliavin 1961; Diamond 1970; Lagarias 1999; Olofsson 2010; Ruzsa 2023;
745 on-disk arXiv abstracts and 11 fresh queries). Every printed construction is "continuous template + random discretization" or
"perturb the rational primes". The nearest sentence is BDR p. 16–17 (z-02 l. 999–1003): "As the integers have to display the best
behavior, it seems natural to define a Beurling system through the sequence of the integers rather than the primes. Yet, it appears
that for sequences defined through this philosophy, it is often extremely difficult to show which behavior the primes must admit."
S8 is exactly such a system, and Theorem 1.6 answers BDR's difficulty for the never-undershooting case: the primes MUST have α ≥ σ*,
from the integers alone. (M. Watkins's web notes on "prime evolution", 1999/2004, speculate about feedback toward the classical primes;
no rule, theorem or zero — `sources/pa-watkins-evolutionnotes*.`)
**Q6 — Diamond's "quite simple examples" (orchestrator's question).** Printed in Diamond, Illinois J. Math. 14 (1970), p. 24
(`sources/pa-diamond1970-p24-transcription.txt`): "For c ∈ (0, 1/2), we consider the 'zeta function' (s − 1 + c)/(s − 1) = ∫x^{−s}(δ +
c dx) … whose continuation has a zero at s = 1 − c > 1/2", with prime measure τ_c(x) = ∫_1^x (1 − t^{−c})/log t dt — **S8's template,
continuous**, simplifying Malliavin, Acta Math. 106 (1961) §6, pp. 295–297 (`sources/pa-malliavin1961-sec6-transcription.txt`), whose
regular-N example is also continuous (one zero, anywhere in (0, 1)); Malliavin's discrete variant (g-primes at the jumps of ⌊π⌋) has
a single zero in σ > 0 and NO stated integer bound, and by Hilberdink's Cor. 2(b) its integer exponent is ≥ ½ (one zero only). Lagarias
1999 p. 4 reads Malliavin as giving discrete N = Ax + O(x^ε) — not supported at Malliavin's page.
**Q4 — Lagarias, Forum Math. 11 (1999) 295–312** (author's preprint, `sources/pa-lagarias1999-delone.txt`): hypotheses = the Delone
property r ≤ n_{i+1} − n_i ≤ R (l. 47–50) AND S ⊂ ℤ⁺; Thm 1.1 (l. 178–186): the generators are G = (P \ E) ∪ C with E a finite set of
primes, C a finite set of composites; Thm 1.2 (l. 194–213): ζ_S = ζ × finite Euler product and n_S(x) = Ax + O(1). Real Delone semigroups
are an open question there (l. 225–227); Ruzsa (arXiv:2311.11127, p. 1) conjectures there are none. S8 is outside every hypothesis: its
g-integers are not in ℤ⁺ and are not uniformly discrete (up to 9 in a unit window at 10⁷). Whether S8's gaps are bounded above is not
decided (they are ≤ (½ + E(x₀))/ρ after x₀).
**Q5 — what is forced near Re s = 1.** Under N = ρx + O(x^θ), θ < 1, only Landau's region σ > 1 − c(1 − θ)/log|t| (DMV 2006 p. 3, (4);
Diamond–Zhang p. 195, (17.1)); no strip. Density theorems that apply to real norms (Révész, JLMS 111 (2025) Thm 1: N(σ, T) ≤
C·T^{12(1−σ)/(1−θ)}log⁵T for σ > (1 + θ)/2; Broucke–Debruyne 2023 Thm 1.2, exponent c(1 − α)/(1 − θ) with c → 4; Broucke 2409.10051
Thm 1.2) bound how many zeros lie right of ½ — for S8 with θ ≈ 0 they would be sparse — but forbid none. Discrete examples with zeros
approaching Re s = 1 all have N-error exponent ≥ ½ (DMV Thm 1: any θ ∈ (½, 1); Zhang 2007 / Diamond–Zhang Thm 17.14: x^{½}e^{c(log x)^{2/3}};
Broucke 2507.13780 Thm 1.6: x^{½+ε}). This supports §2.4: nothing forces sup Re = 1 for S8.
**Q7 — the one-sided lemma.** The template zero at 1 − ρ is in print (Diamond 1970 p. 24; implicit in Hilberdink 2012 Thm 2.1, z-p3-22c2).
The general statement — Theorem 1.6 / Remark 1.6′, a one-sided bound N(u) − ρu ≥ r₀ forcing a real zero in [r₀/(r₀ + ρ), 1) for any
discrete system with N − ρx = O(x^θ) — was NOT found in any source checked (log entry [19]; an arXiv query for Beurling + "real zero" /
"Siegel zero" / "exceptional zero" returned one off-topic hit). The positivity-plus-pole-plus-intermediate-value mechanism is in print for Epstein zeta functions (Bateman–Grosswald, Acta Arith. 9 (1964) p. 367: "Since Z(s) approaches −∞ when s approaches 1 from below, it follows from Theorem 3 that Z(s) vanishes in (½, 1) if k ≥ 7.0556"), and the step "a zero forces α ≥ its real part" is Phragmén's, stated for Beurling systems in Révész, IMRN 2023 (t-14b l. 230–231); the Beurling-setting statement with a one-sided bound on N, and its use against U, are this unit's [novelty: new as a statement on a printed core; single-check].
**Also relevant.** Olofsson, "Properties of the Beurling generalized primes" (preprint 2010; on disk `novel-wave-s37/beurling-fe/
sources/olofsson-2010-properties-beurling-primes.txt`): discrete Q ≠ P with |N(x) − ⌊x⌋| < c·ln x exist (Thm 1.3, l. 112–116; Q = P minus
finitely many primes plus finitely many g-primes, so ζ_Q = ψ(s)ζ(s) and its zeros right of 0 are Riemann's); Conjecture 1.2 (l. 101–105):
lim sup |N(x) − ⌊x⌋|/ln x > 0 for Q ≠ P; remark (l. 659–664): equal values force at least logarithmic growth of the error — the printed
form of the charter's multiplicity diagnosis of S5, and the reason S8's free monoid of distinct reals is the right setting. Olofsson's
systems cannot satisfy R ≥ r₀ > ρ (ζ_Q < 0 on (0, 1)), consistently with Remark 1.6′.
**Novelty (single-check, Opus side).** S8 as a construction (the orchestrator's): no feedback/integer-first construction in print. Theorem
1.6, the Dichotomy, Prop. 2.1, the early-placement rule S8^w and the sieve form of §3.4: not found. The template and its zero: classical
(Diamond 1970; Malliavin 1961). The open question S8 targets is stated in print as open (DMV p. 4; Diamond–Zhang p. 196).

## §6. Instruments rows, Untried, waste line, distance from upstream

**Instruments rows** (shape of `directions/B2-refutation-program.md`; records, never ranks; not applied — for the digest)

| Quantity | Current best value | Result file | Dated |
|---|---|---|---|
| Real zero of ζ_P for the free greedy system S8(ρ) (Theorem 1.6: forced in (1 − 2ρ, 1) by E > −½ plus any bound E = O(x^θ), θ < 1 − 2ρ) | σ* of F_X: π/64 0.947634, π/32 0.895076, π/16 0.794755 (X = 10⁷; 0.794752 at 10⁶), π/8 0.656529, π/6 0.521753, π/4 0.514036, 0.95π/3 0.402156 (X = 10⁶); certified brackets: π/16 ζ_P(0.79) > 0 given only qualitative (B) (F_{10⁷}(0.79) = +0.022231), zero in (0.79, 0.80) if E ≤ 33.7 log²u beyond 10⁷; π/4 ζ_P(½) > 0 (F = +0.067067), zero in (0.50, 0.55) if E ≤ 3.78 log²u. First-order law σ* ≈ (1 − ρ) + ρζ_P(1 − ρ) good to 4·10⁻⁴ for ρ ≤ π/16. Two producers for the certificate values (theory, double precision; read-O, double-double with a 60-digit recheck); ordering margin ≥ 6.4·10⁻¹⁴ relative to 10⁷ (both decision classes) | `free-greedy-s40/theory/NOTE.md` §1.6–1.8, §2.2, §4.1; `theory/verify/bracket_pi16_1e7.log`, `bracket_pi4_1e7.log`, `mech_sweep_*_1e6.log`, `lin_sweep_1e6.log` | 2026-10-01 |
| Integer error of S8(ρ) in the U-relevant range ρ < ¼ (Lemma B_ρ: θ ≤ ½ − ρ refutes U) | π/16: sup E = 3.04, 3.54, 6.88, 9.64, 12.84, 14.71 at 10³…10⁷, 10^7.5, sup E/log²x = 0.064, 0.042, 0.052, 0.050, 0.049, 0.049; largest g-prime gap 336.1 at 10⁷, 432.9 at 10^7.5 (1.3–1.5 log²x; ordering margin 6.1·10⁻¹⁴ to 5·10⁷, both decision classes); π/32: 6.39 at 10⁶, 9.86 at 10⁸ (sup E/log²x 0.029; gap 397); π/64: 3.51 at 10⁶. U forces β(S8(π/16)) > 0.395, β(S8(π/32)) > 0.445 (certified). One producer (theory, Python, double precision) | `theory/NOTE.md` §1.8, §3.0; `theory/verify/mech_pi16_1e7.log`, `mech_pi16_5e7.log`, `mech_pi32_1e8.log`, `mech_sweep_*_1e6.log` | 2026-10-01 |
| Law of E of S8 vs the Poisson-queue heuristic (tail e^{−κh}, κ ≈ 2/(ρ log x)) | measured tail rate = (1.45–1.65)·2/(ρ log x): π/16 on [10³, 10⁷] (theory), π/4 on [10⁶, 10⁹] (compute unit, λ·log x ≈ 3.7–3.9 vs 2.55); time-mean of E = 0.57·ρ log x/2 (π/16); composite arrivals sub-Poissonian, effective variance ≈ 0.6. Two producers | `theory/NOTE.md` §2.3; `theory/verify/mech_pi16_1e7.log`; `free-greedy-s40/SHARED.md` compute batch 1 | 2026-10-01 |
| Mertens law of S8 (the sieve margin of §3.4) | π/16: M(z)·log z = 2.54, 2.70, 2.78, 2.81 at z = 10³…10⁶; proved floor M(z) ≥ M_lat(z) with M_lat(z)·z^ρ → 1.0127. One producer | `theory/NOTE.md` §3.4; `theory/verify/mertens_pi16_1e6.log` | 2026-10-01 |

**Untried** (format of the directions' lists)
- **UT-F1 Prove Lemma B_ρ** for one ρ < ¼ (π/16 is the natural choice): E = O(x^θ) for some θ ≤ ½ − ρ, any constant. With Theorem 1.6
  it refutes U with no computation. The sieve form (§3.4) is NOT a shortcut: two-sided square-root cancellation in S(I) is false for S8 (Mertens bias, Diamond–Zhang Thm 5.10; read-O F1); the usable form is the one-sided Lemma S, which amounts to a short-interval lower bound for the primes of S8. Target: B2.
- **UT-F2 the one-sided Lemma S for the randomized rule S8^w** (early placement keeps E > −½ for every realization, §3.1): a martingale ordered by the scale u/d of the increments ΔE(I/d), controlling fluctuations AROUND the Mertens bias (decorrelation of μ(d) from the drift is false, read-O F1). Positive probability
  suffices for U. Target: B2.
- **UT-F3 Large-X evidence at small ρ.** sup E and the largest g-prime gap for π/16, π/32 to 10⁹–10¹⁰ with the double-double generator
  (cheap: N = ρX); U predicts power-law excursions of exponent > 0.395 (π/16) and > 0.445 (π/32), both certified (§3.0). Target: B2 (compute).
- **UT-F4 Rigorous bracket at scale.** π/16: F_X(0.79) > 0 and F_X(0.80) < 0 by interval arithmetic at X = 10⁹ (not needed for U when
  ρ < ¼; it lifts the floor 1 − 2ρ = 0.607 to 0.79 and relaxes the needed θ to 0.395). Target: B2.
- **UT-F5 Is Theorem 1.6 a Siegel-zero criterion elsewhere?** For any zeta with Euler product, positive coefficients and residue ρ:
  "the coefficient count never falls below ρu + r₀, r₀ > ρ ⇒ real zero ≥ r₀/(r₀ + ρ)". For number fields the hypothesis fails by the
  Ω₋ results for lattice-point errors, consistently with GRH; check whether the criterion is classical (§5). Target: C2.

**Waste line (10(o)).** Spent without result: the 10⁷ reflection check on the prototype's incremental generator (20 s; it tripped on
float drift, which is itself a finding passed to the compute unit); a sequence of crude unconditional bounds for E (smallest/largest
prime factor counting, the Chebyshev identity, the "no primes ⇒ only smooth composites" argument) — none gives even E = o(x), recorded in
§3.3; the first draft of §3.4 had the cancellation exponent wrong (θ = ρ + ε instead of ρ/2 + ε), corrected before close; two SHARED
stamps were mistyped and corrected to the machine clock. Not done: a rigorous multi-scale proof of route (a) (judged a multi-week
project, §3.1, §3.4); interval-arithmetic certification (not needed for ρ < ¼); runs past 10⁷ (the charter's CPU rule held: four or
more heavy processes were running for most of the session).

**Distance from upstream (10(n)).** Theorem 1.6, Remark 1.6′, Cor. 1.7, Prop. 2.1, the Legendre form of §3.4 and the Dichotomy use no
printed input: the Mellin identity of Lemma 1.5 and the "zero ⇒ α ≥ Re" step are written out in full here. The one quoted input is
Hilberdink 2005 Cor. 2(b) (§2.4, used only to describe what is forced, not in any proof). The construction S8 is the orchestrator's
(charter); the randomized early-placement rule, the sieve form and the real-zero mechanism are this unit's.
