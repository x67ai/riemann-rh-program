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
Moreover under (A)–(C): N(x) = O(x) and F converges absolutely for Re s > 1.

Proof. (A)⟹(B). Fix c > max(A, 1). Mellin inversion: ψ(x) = (1/4πi)∫_{(c)} ξ_F(s)x^{−s/2} ds (Fubini; ξ_F decays like e^{−π|t|/4}
on Re s = c by Stirling). On Re s = 1 − c the FE gives the same decay. H(s) := s(s−1)ξ_F(s) is entire, of growth (G') in the strip
1 − c ≤ σ ≤ c, and O(|t|^{c+2}e^{−π|t|/4}) on its edges; Phragmén–Lindelöf in the strip (admissible since (G') is below exp e^{π|t|/(2c−1)})
gives H bounded there, so ξ_F = O(|t|^{−2}) uniformly and the contour moves to Re s = 1 − c, crossing the poles:
residues of ½ξ_F(s)x^{−s/2}: ρ/(2√x) at s = 1 and −ρ/2 at s = 0 (FE: Res_{s=0} ξ_F = −Res_{s=1} ξ_F). The remaining integral,
by s ↦ 1 − s and the FE, is x^{−1/2}ψ(1/x). Hence ψ(x) = ρ/(2√x) − ρ/2 + x^{−1/2}ψ(1/x), which is (B).
(B)⟹(A). Riemann's computation: for Re s > max(A,1), ξ_F(s) = ∫₀^∞ ψ(x)x^{s/2−1}dx; split at 1 and use (B) on (0, 1):
ξ_F(s) = −ρ/s − ρ/(1 − s) + ∫₁^∞ ψ(x)(x^{s/2} + x^{(1−s)/2}) dx/x. ψ(x) ≤ e^{−π(x−1)}ψ(1) for x ≥ 1 (all t ≥ 1), so the integral is
entire, of order ≤ 1, symmetric under s ↦ 1 − s. All of (A) follows ((G') from order ≤ 1).
(B)⟹ N(x) = O(x): for t ≤ X, e^{−πt²/X²} ≥ e^{−π}, so N(X) ≤ e^{π}ψ(1/X²); (B) at x = X² gives 2ψ(1/X²) = X(ρ + 2ψ(X²)) − ρ
≤ X(ρ + 2ψ(1)) for X ≥ 1. So N(X) ≤ ½e^{π}(ρ + 2ψ(1))X: μ has linear growth, is tempered, F converges absolutely for Re s > 1.
(B)⟹(C). ⟨μ, g_x⟩ = ρ + 2ψ(x) and ⟨μ̂, g_x⟩ := ⟨μ, ĝ_x⟩ = x^{−1/2}(ρ + 2ψ(1/x)); (B) says these agree for all x > 0. T := μ̂ − μ is an
even tempered distribution annihilating every g_x; Lemma G gives T = 0.  (C)⟹(B): pair μ̂ = μ with g_x.
(That ρ is the density lim N(x)/x follows from (B) by Karamata [recalled, not used]; in §4 it comes out a posteriori.) ∎

LEMMA G. An even T ∈ S'(R) with ⟨T, g_x⟩ = 0 for all x > 0 is zero.
Proof. y ↦ g_y is C^∞ from (0, ∞) to S with ∂_y^k g_y = (−πt²)^k g_y, so ⟨T, t^{2k}g_y⟩ = 0 for all k ≥ 0, y > 0. Fix y. The map
a ↦ g_y(· − a) is holomorphic from C to S, so u(a) := ⟨T, g_y(· − a)⟩ = (T ∗ g_y)(a) is entire, with u^{(j)}(0) = ⟨T, Q_j g_y⟩, Q_j a
polynomial of the parity of j: zero for odd j (odd test function, T even) and for even j (even polynomial). So T ∗ g_y ≡ 0 for every y;
since y^{1/2}g_y ∗ φ → φ in S as y → ∞, ⟨T, φ⟩ = lim ⟨T ∗ y^{1/2}g_y, φ⟩ = 0 (g_y even). ∎
(The equivalence (A)⟺(B) is Hamburger/Bochner/KM58/Hilberdink–Lapidus Thm 3.2, §2(a); it is re-proved here only to fix hypotheses.)

## 4. THEOREM T — the positive Hamburger theorem (rigidity of Spec Z among Beurling systems) — (P)

THEOREM T. Let dN ≥ 0 be a Borel measure on [1, ∞) of polynomial growth, F(s) = ∫x^{−s}dN(x), and suppose (A) of Proposition R
holds for some ρ ≥ 0 (Riemann's FE, poles of ξ_F only at 0 and 1 and simple, growth (G')). Then dN = ρ·Σ_{n≥1} δ_n, i.e. F = ρζ.
COROLLARY T1 (Beurling, discrete). A Beurling prime system P whose ζ_P satisfies Riemann's FE in the sense (A) is the set of rational
primes, each once. COROLLARY T2 (Beurling, continuous/mixed). No Beurling system with dΠ ≥ 0 not purely atomic on the rational primes
satisfies (A); in particular no continuous Beurling system does. COROLLARY T3 (general Dirichlet series). Σ a_k λ_k^{−s} with a_k ≥ 0,
λ_k ≥ 1, satisfying (A), equals (Σ_{λ_k = 1} a_k)·ζ(s).

Proof. Step 0. By Proposition R, μ := ρδ₀ + dN + dN^∨ is tempered, μ̂ = μ, and N(x) = O(x), so ∫ t^{−2} dN(t) < ∞.
Step 1 (the Fejér identity). φ(x) := (1 − |x|)₊, φ̂(ξ) = (sin πξ/πξ)² =: S(ξ) ≥ 0, S(ξ) = 0 ⟺ ξ ∈ Z∖{0}. Let η ∈ C_c^∞ be even, η ≥ 0,
∫η = 1, supp η ⊂ [−1, 1], η_ε(x) = ε^{−1}η(x/ε), φ_ε := φ ∗ η_ε ∈ C_c^∞ (0 < ε < 1). Then φ̂_ε(ξ) = S(ξ)η̂(εξ) with |η̂| ≤ 1, η̂(0) = 1, and
μ̂ = μ gives ⟨μ, φ_ε⟩ = ⟨μ, φ̂_ε⟩. Left side: φ_ε(0) → 1; for t ≥ 1, φ_ε(t) = ∫φ(t − y)η_ε(y)dy is nonzero only if t − y < 1 with |y| ≤ ε,
i.e. t < 1 + ε, and then φ(t − y) ≤ 1 − (t − y) ≤ y ≤ ε; so 0 ≤ ∫φ_ε dN ≤ ε·N(2) → 0 and ⟨μ, φ_ε⟩ → ρ. Right side:
⟨μ, φ̂_ε⟩ = ρ + 2∫ S(t)η̂(εt) dN(t) → ρ + 2∫ S dN by dominated convergence (|Sη̂(ε·)| ≤ min(1, (πt)^{−2}) ∈ L¹(dN)). Hence
      ∫_{[1,∞)} (sin πt / πt)² dN(t) = 0.                                                          (F)
As dN ≥ 0 and the integrand is continuous, ≥ 0, and vanishes on [1, ∞) exactly at N, dN is carried by N: dN = Σ_{n≥1} a_n δ_n, a_n ≥ 0.
Step 2 (periodicity). μ = Σ_{n∈Z} a_n δ_n with a₀ = ρ, a_{−n} = a_n = O(|n|). For ψ ∈ S: ⟨μ̂, ψ(· + 1)⟩ = ⟨μ, e^{2πiξ}ψ̂(ξ)⟩ = Σ a_n e^{2πin}ψ̂(n)
= ⟨μ̂, ψ⟩, so μ̂ is 1-periodic; μ = μ̂ is 1-periodic, a_{n+1} = a_n for all n, a_n = a₀ = ρ. So dN = ρΣ_{n≥1}δ_n and F = ρζ. ∎(T)
T1: dN({1}) = 1 (the empty product; every p_j > 1) forces ρ = 1: each n ≥ 1 is a generalized integer exactly once, no other number is.
Induction on x (the p_j are locally finite): c(x) = #{j : p_j = x} + #{factorizations of x into ≥ 2 generalized primes, all < x};
by the induction hypothesis the second term is #{factorizations of x into ≥ 2 rational primes} = 0 for x prime, 1 for x composite,
0 for x ∉ N; c(x) = 1_N(x) then gives #{j : p_j = x} = 1 exactly for x a rational prime. ∎(T1)  T2: T and dN({1}) = 1 give dN = Σ_{n≥1}δ_n,
so ∫x^{−s}dΠ = log F(s) = log ζ(s) and, by uniqueness of Laplace–Stieltjes transforms, dΠ = Σ_p Σ_k k^{−1}δ_{p^k}: purely atomic on prime
powers (directly: dN ≥ δ₁ + dΠ, so any non-atomic part of dΠ would survive into dN). ∎  T3: apply T to dN = Σ a_k δ_{λ_k}. ∎
Where each hypothesis enters: POSITIVITY (dN ≥ 0) only in "(F) ⟹ dN carried by N"; the GAP (dN carried by [1, ∞)) only in
"⟨μ, φ_ε⟩ → ρ"; EXACTNESS of the FE (poles only at 0, 1) only in Step 0 (no residual term in μ̂ − μ). The Euler product is used only
for dN({1}) = 1 and to recover P from 𝒩_P; Λ ≥ 0 only through its consequence dN ≥ 0. `[novelty: single-check]` (see §5(g)).
