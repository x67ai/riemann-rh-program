# NOTE — seed M1a `beurling-fe`: is Spec Z rigid among Beurling systems with Riemann's functional equation?

Session 37, 2026-09-30. Writer: Opus 5.5 (seed agent). Status: IN PROGRESS (sections are appended as they are finished).
Conventions: every load-bearing claim is (P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from `sources/`
at the line. `[recalled, unverified]` marks recalled statements, which carry no load. Novelty claims are `[novelty: single-check]`.

## 0. Definitions and the question

A Beurling system is a multiset P = {1 < p₁ ≤ p₂ ≤ …} ⊂ R with p_j → ∞; its integers 𝒩_P = {n_k} are the multiset of finite
products (with multiplicity), n₀ = 1 (empty product). Write c(x) ≥ 0 for the multiplicity of x as a generalized integer,
N_P(x) = Σ_{n_k ≤ x} 1, ζ_P(s) = Σ_k n_k^{−s} = Π_j (1 − p_j^{−s})^{−1}, assumed absolutely convergent for Re s > 1.

(FE) ξ_P(s) := π^{−s/2} Γ(s/2) ζ_P(s) continues meromorphically to C, with poles only at s = 0 and s = 1, both simple, and
ξ_P(s) = ξ_P(1 − s); plus the growth condition (G): (s − 1)s·ξ_P(s) is entire of finite order (Hamburger's standing condition).

QUESTION (charter). Is P = {rational primes} the only Beurling system satisfying (FE)+(G)?

## 1. Headline (the idea in one paragraph; the theorem with full proof is §4, its attack log §5)

Let μ = ρδ₀ + Σ_k(δ_{n_k} + δ_{−n_k}) (multiplicity counted), n_k ≥ 1, and suppose μ is tempered with μ̂ = μ
(convention f̂(ξ) = ∫f(x)e^{−2πixξ}dx). Take φ(x) = (1 − |x|)₊, so φ̂(ξ) = (sin πξ/πξ)² ≥ 0, zero exactly on Z∖{0}.
Since supp μ ∩ (−1, 1) = {0} and φ(±1) = 0:   ⟨μ, φ⟩ = ρ.   And ⟨μ, φ̂⟩ = ρ + 2Σ_k (sin πn_k/πn_k)².
μ̂ = μ gives ⟨μ, φ⟩ = ⟨μ, φ̂⟩ (φ is not Schwartz: justified by mollification, §3), hence Σ_k sin²(πn_k)/n_k² = 0:
EVERY GENERALIZED INTEGER IS A RATIONAL INTEGER. Then μ is supported on Z, so μ̂ is 1-periodic; μ̂ = μ forces μ 1-periodic:
the mass at every n ∈ Z equals the mass at 0, i.e. c(n) = ρ for all n ≥ 1; c(1) = 1 gives ρ = 1 and 𝒩_P = N (each once).
So ζ_P = ζ and P = {rational primes}. No Euler product, no uniform discreteness, no Hamburger is used — only
(i) dN_P ≥ 0, (ii) supp dN_P ⊂ [1, ∞), (iii) exact self-duality. The same proof covers CONTINUOUS Beurling systems.

## 2. Prior-art gate (standing order 1) — what is already a theorem (Q = quoted, file:line under `sources/`)

(a) The reformulation FE ⟺ Poisson/theta relation is classical and in print. Hamburger 1921–22 (as stated by Kahane–Mandelbrojt,
    `kahane-mandelbrojt-1958-asens75.txt` 41–75: conditions I–V, "l'équation fonctionnelle de Riemann" ⟺ "la relation θ" ⟺ Poisson);
    KM58 Théorème 1 (line 306: the FE condition "équivaut à la formule de Poisson … pour les fonctions f indéfiniment dérivables
    à décroissance rapide"); Bochner 1951 (Ann. Math. 53, 332–363; cited, not on disk); Hilberdink–Lapidus 2006 Theorem 3.2
    (`p3-22c1-…txt` 1042–1057: FE ⟺ F₁(x) = x⁻¹F₂(1/x) + H(x), H a finite residual) with the Addendum (1070) crediting Bochner.
(b) The Beurling FE question is recorded as OPEN in print: Hilberdink–Lapidus 2006 (p3-22c1 lines 125–128) "[we] examine when it
    can be 'completed' to satisfy a suitable generalised functional equation. We do not give a complete answer to the latter
    difficult question, but indicate several approaches and give a criterion for the existence of such a functional equation."
    Diamond–Zhang 2016, p. 1 (t-50 lines 356–360): systems with N(x) close to x "have neither an additive structure nor a 'zeta
    functional equation,' and for which the analogue of the Riemann hypothesis does not hold." (no rigidity statement made).
(c) Hamburger's theorems. Theorem D in Nakamura (`nakamura-2008.02570.txt` 170–177): F ordinary Dirichlet series (H1), P(s)F(s)
    entire of finite order (H2), ξ_F(1−s) = ξ_F(s) (H3) ⟹ F = Cζ. Knopp 1994 (Invent. Math. 117, 361–372; Nakamura 183–185 and the
    Springer summary `springer-BF01232248-abstract.md`): infinitely many solutions once (H1) is weakened. Hamburger's SECOND theorem
    as stated by Burnol (`burnol-1106.4749.txt` 140–160): f ordinary, g(s) = χ(s)f(1−s) a GENERAL Dirichlet series Σ b_n y_n^{−s}
    ⟹ y_{n+k} = y_n + 1, …; "Ainsi, si tous les y_n sont ⩾ 1, c'est que k = 1 et que f est un multiple de la fonction zêta" (line 160).
    Burnol Théorème 2 (lines 172–200): for f, g BOTH general, only an equivalence "supports in finitely many progressions of step 1".
    None of these covers f = g general with non-integer frequencies — the Beurling case — and none uses positivity.
(d) Fourier quasicrystals. Lev–Olevskii Theorem 1 (`u-30b-…txt` 51–53): support and spectrum both u.d. ⟹ Λ in finitely many translates
    of an arithmetic progression; their Theorem 2 (65–68): u.d. cannot be relaxed to "discrete" for SIGNED measures. Olevskii–Ulanovskii
    (`p2-19b-…txt` 40–46, Remark 1 at 342–348): an FQ with masses in N has support = real zero set of an exponential polynomial;
    their Proposition 1 (64–70): a positive tempered μ with |μ̂| tempered is translation-bounded. Gonçalves 2023 Theorem 5 (`u-28b-…txt`
    662–668): nonnegative u.d. measures bounded below on the support with a spectral gap (0, b) are classified by Hermite–Biehler E.
    KM58 Prop. 7/Théorème 4–5 and Corollaire (lines 958–1063): gap/density inequalities for complex coefficients; equality ⟹ Dirac combs.
(e) Beurling rigidity problems that ARE in print, and differ from this one: Olofsson 2010 (`olofsson-…txt`) Proposition 3.1 (623–633):
    |N(t) − [t]| = o(1) iff Q = rational primes; Conjecture 1.2 (101–104; Beurling's problem): o(log x) should suffice; Lagarias 1999
    (Forum Math. 11, 295–312; abstract `lagarias-1999-delone-abstract.md`): Delone systems contained in Z = all but finitely many
    primes plus finitely many composites; the non-integer Delone case is open (Olofsson 667–669). Hilberdink 2012 Theorem A
    (`p3-22c2-…txt` 97–103): N(x) − cx periodic (class T) ⟹ usual primes minus finitely many.
GATE VERDICT. The exact question (Beurling ζ_P with Riemann's FE ⟹ P = primes) is not settled in anything read; Hilberdink–Lapidus
call the (more general) question difficult and open. Searches (logged in `sources/arxiv-queries/`, web searches in SHARED) found no
statement of it. Not read (paywalled/not found): Bochner–Chandrasekharan 1956, Chandrasekharan–Mandelbrojt 1957/59, Lagarias 1999 body.
The unit proceeds; the novelty label on §4 is `[novelty: single-check]`, with the recalled caveat in §5(g).

## 3. The reformulation (charter item (1)), with exact hypotheses — (P)

Setting (covers discrete AND continuous systems). dN is a positive Borel measure on [1, ∞) with N(x) := dN([1, x]) = O(x^A) for
some A (so F(s) := ∫ x^{−s} dN(x) converges absolutely for Re s > A). Beurling: dN = exp*(dΠ) with dΠ ≥ 0 on (1, ∞), so dN ≥ 0,
dN({1}) = 1. For discrete P, dN = Σ_k δ_{n_k}. Put ψ(x) := ∫ e^{−πt²x} dN(t) (x > 0), ξ_F(s) := π^{−s/2}Γ(s/2)F(s),
μ := ρδ₀ + dN + dN^∨ (dN^∨ = reflection of dN to (−∞, −1]), g_x(t) := e^{−πxt²}, ĝ_x = x^{−1/2} g_{1/x}.

PROPOSITION R. For ρ ≥ 0 the following are equivalent:
 (A) ξ_F continues meromorphically to C, its only poles are simple poles at 0 and 1 with Res_{s=1} ξ_F = ρ, ξ_F(s) = ξ_F(1 − s),
     and (G') s(s − 1)ξ_F(s) = O(exp e^{ε|t|}) in every vertical strip, for every ε > 0 (finite order is a special case);
 (B) ρ + 2ψ(1/x) = √x·(ρ + 2ψ(x)) for all x > 0;
 (C) μ is a tempered distribution and μ̂ = μ.
Moreover under (A)–(C): N(x) = O(x), F converges absolutely for Re s > 1, and ρ = lim N(x)/x.

Proof. (A)⟹(B). Fix c > max(A, 1). Mellin inversion: ψ(x) = (1/4πi)∫_{(c)} ξ_F(s)x^{−s/2} ds (Fubini; ξ_F decays like e^{−π|t|/4}
on Re s = c by Stirling). On Re s = 1 − c the FE gives the same decay. H(s) := s(s−1)ξ_F(s) is entire, of growth (G') in the strip
1 − c ≤ σ ≤ c, and O(|t|^{c+2}e^{−π|t|/4}) on its edges; Phragmén–Lindelöf in the strip (admissible since (G') is below exp e^{π|t|/(2c−1)})
gives H bounded there, so ξ_F = O(|t|^{−2}) uniformly and the contour moves to Re s = 1 − c, crossing the poles:
residues of ½ξ_F(s)x^{−s/2}: ρ/(2√x) at s = 1 and −ρ/2 at s = 0 (FE: Res_{s=0} ξ_F = −Res_{s=1} ξ_F). The remaining integral,
by s ↦ 1 − s and the FE, is x^{−1/2}ψ(1/x). Hence ψ(x) = ρ/(2√x) − ρ/2 + x^{−1/2}ψ(1/x), which is (B).
(B)⟹(A). Riemann's computation: for Re s > max(A,1), ξ_F(s) = ∫₀^∞ ψ(x)x^{s/2−1}dx; split at 1 and use (B) on (0, 1):
ξ_F(s) = −ρ/s − ρ/(1 − s) + ∫₁^∞ ψ(x)(x^{s/2} + x^{(1−s)/2}) dx/x. ψ(x) ≤ e^{−π(x−1)}ψ(1) for x ≥ 1 (all t ≥ 1), so the integral is
entire, of order ≤ 1, symmetric under s ↦ 1 − s. All of (A) follows ((G') from order ≤ 1).
(B)⟹ N(x) = O(x): e^{−π}N(X) ≤ ψ(1/X²) = X^{−1}(ρ + 2ψ(X²))·... precisely, (B) at x = 1/X² gives 2ψ(1/X²) = X(ρ + 2ψ(X²)) − ρ ≤ X(ρ + 2ψ(1)),
and N(X) ≤ e^{π}ψ(1/X²). So μ has linear growth, is tempered, and F converges absolutely for Re s > 1.
(B)⟹(C). ⟨μ, g_x⟩ = ρ + 2ψ(x) and ⟨μ̂, g_x⟩ := ⟨μ, ĝ_x⟩ = x^{−1/2}(ρ + 2ψ(1/x)); (B) says these agree for all x > 0. T := μ̂ − μ is an
even tempered distribution annihilating every g_x; Lemma G gives T = 0.  (C)⟹(B): pair μ̂ = μ with g_x.
ρ = density: ⟨μ, g_x⟩ ~ x^{−1/2}ρ as x → 0 (from (B)) and Karamata, or directly §4 below (μ̂({0}) = ρ is the mean of μ). ∎

LEMMA G. An even T ∈ S'(R) with ⟨T, g_x⟩ = 0 for all x > 0 is zero.
Proof. y ↦ g_y is C^∞ from (0, ∞) to S with ∂_y^k g_y = (−πt²)^k g_y, so ⟨T, t^{2k}g_y⟩ = 0 for all k ≥ 0, y > 0. Fix y. The map
a ↦ g_y(· − a) is holomorphic from C to S, so u(a) := ⟨T, g_y(· − a)⟩ = (T ∗ g_y)(a) is entire, with u^{(j)}(0) = ⟨T, Q_j g_y⟩, Q_j a
polynomial of the parity of j: zero for odd j (odd test function, T even) and for even j (even polynomial). So T ∗ g_y ≡ 0 for every y;
since y^{1/2}g_y ∗ φ → φ in S as y → ∞, ⟨T, φ⟩ = lim ⟨T ∗ y^{1/2}g_y, φ⟩ = 0 (g_y even). ∎
(The equivalence (A)⟺(B) is Hamburger/Bochner/KM58/Hilberdink–Lapidus Thm 3.2, §2(a); it is re-proved here only to fix hypotheses.)
