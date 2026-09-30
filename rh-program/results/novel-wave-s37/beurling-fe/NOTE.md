# NOTE — seed M1a `beurling-fe`: is Spec Z rigid among Beurling systems with Riemann's functional equation?

Session 37, 2026-09-30. Writer: Opus 5.5 (seed agent). Status: COMPLETE — CLOSE T (§10); read at the line Session 38, 2026-10-01: read-F (Fable) AGREES, read-O (Opus) AGREES-WITH-CORRECTIONS — F1, m1–m8, P1–P2 applied, §12 added; `NOTE.pre-reader.md` kept. Sections were written in order as results landed; read §4 and §10 first.
Conventions: every load-bearing claim is (P) proved here, (C) computed in `verify/` with its log, or (Q) quoted from `sources/`
at the line. `[recalled, unverified]` marks recalled statements, which carry no load. Novelty claims are `[novelty: single-check]`.

## 0. Definitions and the question

A Beurling system is a multiset P = {1 < p₁ ≤ p₂ ≤ …} ⊂ R with p_j → ∞; its integers 𝒩_P = {n_k} are the multiset of finite
products (with multiplicity), n₀ = 1 (empty product). Write c(x) ≥ 0 for the multiplicity of x as a generalized integer,
N_P(x) = Σ_{n_k ≤ x} 1, ζ_P(s) = Σ_k n_k^{−s} = Π_j (1 − p_j^{−s})^{−1}, assumed absolutely convergent for Re s > 1.

(FE) ξ_P(s) := π^{−s/2} Γ(s/2) ζ_P(s) continues meromorphically to C, with poles only at s = 0 and s = 1, both simple, and
ξ_P(s) = ξ_P(1 − s); plus the growth condition (G): (s − 1)s·ξ_P(s) is entire of finite order (Hamburger's standing condition;
the theorems below need only the weaker (G') of §3).

QUESTION (charter). Is P = {rational primes} the only Beurling system satisfying (FE)+(G)?

## 1. Headline (the idea in one paragraph; the theorem with full proof is §4, its attack log §5)

Let μ = ρδ₀ + Σ_k(δ_{n_k} + δ_{−n_k}) (multiplicity counted), n_k ≥ 1, and suppose μ is tempered with μ̂ = μ
(convention f̂(ξ) = ∫f(x)e^{−2πixξ}dx). Take φ(x) = (1 − |x|)₊, so φ̂(ξ) = (sin πξ/πξ)² ≥ 0, zero exactly on Z∖{0}.
Since supp μ ∩ (−1, 1) = {0} and φ(±1) = 0:   ⟨μ, φ⟩ = ρ.   And ⟨μ, φ̂⟩ = ρ + 2Σ_k (sin πn_k/πn_k)².
μ̂ = μ gives ⟨μ, φ⟩ = ⟨μ̂, φ⟩ = ⟨μ, φ̂⟩ (φ is not Schwartz: justified by mollification, §4 Step 1), hence Σ_k sin²(πn_k)/n_k² = 0:
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
statement of it. Not read at the first gate: Bochner–Chandrasekharan 1956, Chandrasekharan–Mandelbrojt 1957/59, Lagarias 1999 body.
Second reader (read-O §3, Session 38) read: Chandrasekharan–Mandelbrojt 1959 (Bull. AMS, whole), Bochner–Chandrasekharan 1956 p. 336 and
Chandrasekharan–Narasimhan 1961 p. 1 (JSTOR previews), Cohn–Elkies 2003, Cohn–Kumar 2007, Lev–Olevskii 2015, Meyer 2016, Kolountzakis 2016,
Radchenko–Viazovska 2019 — none contains T. Still unread: BC56 beyond p. 336, CM57, Córdoba 1988/89, Lagarias 1999 body.
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
primes, each once. COROLLARY T2 (Beurling, continuous/mixed). If dN = exp*(dΠ) with dΠ ≥ 0 and ∫x^{−σ}dΠ(x) < ∞ for some σ (⟺ N has polynomial
growth; read-O m2) satisfies (A), then
dΠ = Σ_p Σ_k k^{−1}δ_{p^k} (the rational primes); in particular no continuous Beurling system satisfies (A). COROLLARY T3 (general Dirichlet series). Σ a_k λ_k^{−s} with a_k ≥ 0,
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
Where each hypothesis enters: POSITIVITY (dN ≥ 0) twice — in Prop. R's linear-growth bound (Step 0; it puts S in L¹(dN) for the
dominated convergence of Step 1) and in "(F) ⟹ dN carried by N"; it cannot be dropped (read-O R1, §8(e)). The GAP (dN carried by [1, ∞)) only in
"⟨μ, φ_ε⟩ → ρ"; EXACTNESS of the FE (poles only at 0, 1) only in Step 0 (no residual term in μ̂ − μ). The Euler product is used only
for dN({1}) = 1 and to recover P from 𝒩_P; Λ ≥ 0 only through its consequence dN ≥ 0. `[novelty: dual-checked (read-O §3, Session 38): not in print as read; measure core = routine adaptation of Cohn–Elkies p. 695 + Siegel]` (see §5(g)).

## 5. Attack log — on Theorem T, and on the charter's sketches (attacked first, as ordered)

(a) φ = (1−|x|)₊ is not Schwartz: handled by mollification in Step 1 (only φ_ε ∈ C_c^∞ is paired with μ̂ = μ). ✓
(b) (A) gives the theta relation, i.e. μ̂ = μ only against Gaussians: Lemma G upgrades it to μ̂ = μ in S′. ✓
(c) ρ = 0 is not excluded by hypothesis: T then gives dN = 0, contradicting dN({1}) = 1; so no Beurling system has ρ = 0. ✓
(d) The growth hypothesis (G') is used once (Phragmén–Lindelöf in Prop. R). It is Burnol's hypothesis (2) (`burnol-1106.4749.txt`
    lines 106–107; also Thms 2–3, lines 183, 217); Hamburger's own is finite order. Whether (G') can be dropped for Beurling systems is NOT addressed here.
    (H1) is not needed: Prop. R proves absolute convergence for Re s > 1 from (B); so Knopp's phenomenon (§2(c)) cannot occur here.
(e) "Poles only at 0 and 1, simple" is essential: with extra poles μ̂ − μ is a nonzero residual R and Step 1 becomes 2∫S dN = ⟨R, φ⟩
    (§8(d)); the orchestrator's continuous RH-false systems live exactly there.
(f) The charter's sketches, attacked:
    (f1) Charter (1) writes μ = δ₀ + Σ(δ_{n_k} + δ_{−n_k}). WRONG IN GENERAL, harmless: the mass at 0 is ρ = Res_{s=1}ξ_P (Prop. R);
         ρ = 1 is a CONCLUSION of T (T1), not an input.
    (f2) Charter (3) "expected tools: Lev–Olevskii; Serre–Stark for weight ½; positivity + free generation". None is needed for T.
         Lev–Olevskii + the semigroup property give an independent second proof in the u.d. case (§6). Serre–Stark is irrelevant at
         conductor 1; at conductor q > 1 it would need full Γ₀(4N)-modularity, which one functional equation does not supply
         (Perelli, `arxiv-1605.02354-…txt` 546–554: Hecke groups G(λ), λ > 2 — infinite-dimensional solution spaces).
    (f3) Charter (4) "translation-boundedness follows from positivity + self-duality (prove)": TRUE — Olevskii–Ulanovskii Prop. 1
         (`p2-19b-…txt` 64–100, quoted in full on disk) applies to μ ≥ 0 with μ̂ = μ; a posteriori it is also immediate from T.
    (f4) Charter (5), the orchestrator's Phragmén–Lindelöf worry ("G entire of finite order ⟹ G ≡ 1 only when G = ζ_P/ζ is
         entire, which is not automatic"): SUPERSEDED. T2 needs no hypothesis on G = ζ_P/ζ (which may have poles at zeros of ζ):
         an entire completed function (poles only at 0, 1) is impossible for every continuous Beurling system. Verdict §8(a).
    (f5) §0(f) "Beurling systems … have Euler product and Λ ≥ 0 but no FE": now a THEOREM at conductor 1 (T1, T2).
(g) Novelty caveat. The measure-theoretic core of T — μ ≥ 0, μ = ρδ₀ + ν with supp ν ⊂ {|x| ≥ 1}, μ̂ = μ ⟹ μ = ρδ_Z — is the equality
    case of the one-dimensional linear-programming (Delsarte/Cohn–Elkies) bound with the Fejér function (Cohn–Elkies 2003, Ann. Math. 157,
    p. 695: "(1 − |x|)χ[−1,1](x) … a sharp bound", proved for periodic packings; the uniqueness statement for positive self-dual measures is
    not printed there — read-O §3 row 12). The core is a routine adaptation of that pairing plus Siegel's periodicity step
    (Bochner–Chandrasekharan 1956, p. 336; Steuding's notes Thm 3.8). What is `[novelty: single-check]` is
    its use as a positive Hamburger theorem for general Dirichlet series (T3) and for Beurling systems (T1, T2), which the gate did
    not find in print and which Hilberdink–Lapidus 2006 record as open in greater generality. Not for external use before a second check.
(h) Non-vacuity (C: `verify/v1_theta_fejer_conductor.log`, Part 2): Z gives S_F := Σ sinc²(n_k) = 7e−29 (roundoff) and theta defect 0 at
    60 digits; the near-misses "2 → 2.01", "(P∖{2}) ∪ {√2}" (Olofsson's example), "P ∪ {1.5}" give S_F = 2.0e−3, 6.1e−2, 8.9e−2 and
    theta defects of order 1e−3 to 0.8 — the FE fails, as T requires.

## 6. The uniformly discrete case (charter item (3)) — an independent second proof, by the tools the charter expected — (P)+(Q)

PROPOSITION U. If 𝒩_P is uniformly discrete and ζ_P satisfies (A), then 𝒩_P ⊂ N and ζ_P = ζ. (Implied by T; proved without Step 1.)
Proof. By Prop. R, μ̂ = μ with μ ≥ 0; support = spectrum = {0} ∪ ±𝒩_P, u.d. Lev–Olevskii Theorem 1 (`u-30b-…txt` 51–53) ⟹ 𝒩_P ⊂ ∪_{j≤m}(τ_j + hZ).
(i) 𝒩_P ⊂ Q (Hilberdink's device, `p3-22c2-…txt` 536–556): 𝒩_P is infinite (p₁^k), so some coset contains an infinite A ⊂ 𝒩_P. For
x ∈ 𝒩_P, xA ⊂ 𝒩_P (semigroup), so two a ≠ a′ in A have xa, xa′ in one coset: x(a − a′) ∈ hZ and a − a′ ∈ hZ∖{0}, hence x ∈ Q.
(ii) Then h = (a − a′)/k ∈ Q, every coset meeting 𝒩_P has a rational τ_j, so 𝒩_P ⊂ D^{−1}Z for some D ∈ N. If x = a/b ∈ 𝒩_P in lowest
terms, x^k ∈ 𝒩_P ⊂ D^{−1}Z for all k, so b^k | D for all k and b = 1: 𝒩_P ⊂ N. (iii) ζ_P = Σ c(n)n^{−s} is an ordinary Dirichlet
series; (H1) by Prop. R, (H2) with P(s) = s − 1 (finite order: the (B)⟹(A) computation gives ξ_F of order ≤ 1), (H3) is (A); Hamburger (Theorem D, `nakamura-2008.02570.txt` 170–177)
gives ζ_P = Cζ, C = c(1) = 1. ∎   (Free generation is not used, only the semigroup property; positivity only via Lev–Olevskii's
hypotheses being met by μ̂ = μ.) The two proofs share nothing but Prop. R: a dual-route check of T on the u.d. class.

## 7. The non-uniformly-discrete case (charter item (4)) — settled by T; the experiment and what it shows

VERDICT. Refuted: there is no exotic system, uniformly discrete or not (T1), discrete or continuous (T2). T never uses discreteness of
𝒩_P beyond local finiteness, and never uses Lev–Olevskii; so the Lev–Olevskii Theorem 2 phenomenon (non-periodic SIGNED crystalline
measures once u.d. is dropped, `u-30b-…txt` 65–68) and the Kurasov–Sarnak positive integer-mass examples cannot produce a Beurling
system: in the self-dual case positivity plus the gap (0, 1) already pin the support to Z.
LEMMA TB (charter: "translation-boundedness follows from positivity + self-duality (prove)") (P). If μ ≥ 0 is tempered and μ̂ ≥ 0
(in particular if μ̂ = μ ≥ 0), then sup_a μ([a − δ, a + δ]) < ∞. Proof: take h ∈ C_c^∞ even, h ≥ 0, h ≢ 0, and k := h ∗ h; then k ≥ 0,
k̂ = ĥ² ≥ 0, and k ≥ c > 0 on some [−δ, δ]. For every a, c·μ([a−δ, a+δ]) ≤ ⟨μ, k(· − a)⟩ = ⟨μ̂, e^{2πiaξ}k̂(ξ)⟩ ≤ ⟨μ̂, k̂⟩ < ∞,
using μ̂ ≥ 0 and |e^{2πiaξ}k̂| = k̂ (the middle equality is Parseval for the tempered pair μ, μ̂; k is even). ∎ (Same as
Olevskii–Ulanovskii Prop. 1 in spirit, `p2-19b-…txt` 64–100; there |μ̂| tempered replaces μ̂ ≥ 0.)

EXPERIMENT (C: `verify/v2_lsq_exotic_search.{py,log}`, `verify/v2b_near_solutions_exposed.{py,log}`). Least squares on the theta
relation over 42 log-spaced points x ∈ [½, 2] (none equals 1; read-O m4), unknowns ρ and K free generalized primes in (1, 12) (all generalized primes below 12, so
the truncation is exact to e^{−72π} ~ 1e−98), 300 random starts per K = 1..7, double precision. Result: for every K ≥ 2 the optimizer
returns RMS defect ~1e−16 at ρ = 1.000000 with primes {2, 3, arbitrary…}, e.g. {2, 3, 8.470247} (K = 3) and {2, 3, 5.5606, 7.5802,
9.1104, 10.3413, 10.5167} (K = 7). These are NUMERICAL NEAR-SOLUTIONS, NOT EXAMPLES: on x ≥ ½ a generalized integer n enters ψ with
weight ≤ e^{−πn²/2}, which is below double precision (8e−18) for n ≥ 5, so the grid sees only the integers 1, 2, 3, 4. Re-examined at
60 digits on x = 2^{−3}..2^{3} (v2b) their theta defects are 1e−4 (ρ = 1) to 0.12–0.54 (ρ = true residue), and their Fejér sums
S_F = Σ sinc²(n_k) are 1.7e−3, 5.4e−3, 2.6e−3, 8.7e−3 — against 3e−61 and 7e−29 for Z. LESSON (the charter's warning made concrete):
Gaussian test functions on a bounded x-range are exponentially blind to large generalized integers; the Fejér test function, whose
transform decays only like ξ^{−2}, sees every n_k with weight ≍ n_k^{−2}. That is why T is proved with it and not with theta values.

## 8. Relaxations (charter item (5)), each to a verdict

(a) CONTINUOUS BEURLING PRIME MEASURES — the orchestrator's sketch. ζ_P = ζ·G, G(s) = (s−ρ)(s−ρ̄)(s−1+ρ)(s−1+ρ̄)/((s−a)²(s−1+a)²),
    ρ = β + iγ, β > ½. log G(s) = ∫₁^∞ x^{−s} f(x) dx, f = [2x^a + 2x^{1−a} − 2(x^β + x^{1−β})cos(γ log x)]/(x log x) (from
    log((s−c)/(s−a)) = ∫₁^∞ x^{−s}(x^a − x^c)dx/(x log x)). f ≥ 0 when a ≥ β because |cos| ≤ 1 and c ↦ x^c + x^{1−c} increases on
    c ≥ ½ for x ≥ 1 (P). C (`verify/v3_…log` Part A): G(1−s) = G(s) to 1e−27; exp∫x^{−s}f = G at s = 3, 2+5i to 1e−19; min f on
    (1, 1e8] = 2e−9, 8e−4, 7e−11 for (β,γ,a) = (.8,20,.8), (.8,20,.9), (.6,14.1,.6); −0.077 for a = 0.7 < β = 0.8.
    VERDICT: the sketch is CORRECT (dΠ ≥ 0, FE exact, RH false, price = double poles at a, 1 − a inside the strip). The question
    "is an ENTIRE completed function possible?" is answered NO by T2, for every continuous or mixed Beurling system under (G'),
    with no hypothesis on G = ζ_P/ζ. The continuous relaxation is populated by RH-false systems iff extra poles are allowed.
(b) FE WITH A CONDUCTOR. Λ_F(s) := (q/π)^{s/2}Γ(s/2)F(s), (A) for Λ_F.
    THEOREM C. dN ≥ 0 on [1, ∞), polynomial growth, dN({1}) > 0, (A) for Λ_F. Then q ≥ 1; q = 1 iff F = ρζ; and for q > 1
         ρ_q(1 − q^{−1/2}) = 2q^{−1/2} ∫ (sin(πt/q)/(πt/q))² dN(t),   ρ_q := √q·Res_{s=1}F > 0.                        (C_q)
    Proof (P). Λ_F(s) = π^{−s/2}Γ(s/2)∫x^{−s}dN_q with dN_q the image of dN under t ↦ t/√q, carried by [r, ∞), r = q^{−1/2}.
    Prop. R holds verbatim for measures carried by [r, ∞) (use ψ(x) ≤ e^{−πr²(x−1)}ψ(1)), so μ_q = ρ_qδ₀ + dN_q + dN_q^∨ is self-dual,
    ρ_q ≥ 0 (a residue of a positive Dirichlet integral). Pair with φ_r = φ(·/r) exactly as in Step 1 (φ_r = 0 on |x| ≥ r, where dN_q
    lives; φ̂_r(ξ) = rS(rξ); rt = u/q for t = u/√q): this is (C_q). If q < 1 then r > 1, the left side is ≤ 0 and the right ≥ 0, so
    ρ_q = 0 and dN is carried by qN; then μ_q is carried by the lattice √qZ, so μ̂_q = μ_q is 1/√q-periodic and
    the atom of dN_q at t = 1/√q (the image of dN({1}) > 0) has the mass of the atom at 0, which is ρ_q = 0 — contradicting dN({1}) > 0. q = 1 is T. If q > 1 and ρ_q = 0,
    (C_q) again carries dN by qN, which misses the atom at 1 (1 ∉ qN for q > 1); so ρ_q > 0. ∎  `[novelty: dual-checked (read-O §1, Session 38)]` (an LP corollary; the analog
    of "degree-1 conductor ≥ 1, equality only for ζ" in the Selberg class, Kaczorowski–Perelli `[recalled, via zoo I.7; not load]`
    — there with Euler product and Ramanujan, here with positivity only).
    C: (C_q) holds on genuine solutions — ζ(s)(1 + q^{1/2−s}), q = 2, 4, 9, and F_{5,5} (q = 25): 0.70711 / 1.5 / 2.66667 / 8.8 on both
    sides up to the truncation tail (`verify/v1_…log` Part 3; each also satisfies its conductor-q theta relation to 1e−60).
    VERDICT (q > 1): OPEN, and sharply located. Positive-coefficient solutions exist at every q > 1 (above) but all those found fail
    Λ ≥ 0 (F_{5,5}: Λ(25)/log 5 = −14, Λ(5⁴)/log 5 = −174, v3 Part C; ζ(s)(1 + q^{1/2−s}) for EVERY q > 1: the factor puts mass
    −q^k/(2k) at q^{2k} while ζ puts at most 1 at any point, so Λ(q^{2k}) < 0 for large k — e.g. q = √2: Λ(8)/log 8 = 1/3 − 2^{3/2}/6 < 0). The FE alone is weak at q > 1: one functional equation does not force
    modularity and the spaces are infinite-dimensional (Perelli `arxiv-1605.02354-…txt` 586–595, Hecke G(λ), λ > 2). QUESTION Q_cond:
    is there a Beurling system (dΠ ≥ 0) with Riemann's FE at some conductor q > 1? This is where a rung-Z twin could live (§9).
(c) FE UP TO A FINITE EULER FACTOR. Hypothesis: for finite S₊ ⊂ P and finite S₋ ⊂ (1, ∞), ζ_P(s)·Π_{S₊}(1 − p^{−s})·Π_{S₋}(1 − p^{−s})^{−1}
    satisfies (A). That product is ζ_{P′}, P′ = (P ∖ S₊) ⊎ S₋, a Beurling zeta; T1 gives P′ = rational primes, so S₋ ⊂ primes and
    P = (primes ∖ S₋) ⊎ S₊ (S₊ ARBITRARY reals > 1; S₋ = Hilberdink 2012's "all but finitely many primes", Olofsson's (3)). Weighted
    variants (factors (1 − αp^{−s})^{±1}, 0 ≤ α ≤ 1, keeping dΠ ≥ 0) reduce the same way. VERDICT: populated, but every member has the
    zeros of ζ plus zeros/poles on Re s = 0 only: RH for ζ_P ⟺ RH for ζ. No new control. (P)
(d) FINITELY MANY EXTRA POLES (Hamburger's (H2) allows them). If ξ_F has extra poles s_j in 0 < Re s < 1 (a set symmetric under
    s ↦ 1 − s), Prop. R's proof gives μ̂ − μ = R ≠ 0, R a finite sum of homogeneous distributions |t|^{s_j−1}(log|t|)^m — locally
    integrable, since Re s_j > 0 (this is Hilberdink–Lapidus's residual H, `p3-22c1-…txt` 1052–1057, on the Fourier side). Step 1 then gives
            2 ∫ (sin πt/πt)² dN(t) = ⟨R, φ⟩,  and generally  2∫ψ̂ dN = ρ(ψ(0) − ψ̂(0)) + ⟨R, ψ⟩ for all ψ ∈ C_c(−1,1), ψ̂ ≥ 0.   (F_R)
    So non-integral generalized integers are paid for exactly by residual mass inside the gap (−1, 1). Necessary: ⟨R, φ⟩ ≥ 0, with
    equality iff dN is carried by N. VERDICT: populated by RH-false CONTINUOUS systems ((a); there R ≠ 0); for DISCRETE Beurling
    systems with extra poles: open (Broucke–Vindas discretization, zoo I.2(d), keeps Λ ≥ 0 but cannot keep an exact FE). (P) for (F_R).
(e) POSITIVITY DROPPED (complex coefficients, frequencies ≥ 1). T's Step 1 fails. In print: Hamburger's second theorem (f ordinary,
    dual frequencies ≥ 1 ⟹ cζ; Burnol line 160) and Burnol Théorème 2 (both general: equivalence only). Finite constructions ζ·D
    cannot escape (D(s) = D(1−s) maps frequency m to 1/m, so frequencies ≥ 1 force D constant — (P), one line). VERDICT (revised Session 38 — read-O R1, FIX-FIRST F1, re-derived by the orchestrator): SETTLED, populated by RH-FALSE signed solutions.
    Construction: χ₅ the Legendre symbol mod 5 (even, τ = +√5); the twisted comb Σχ₅(n)δ_{n/√5} is self-dual; the dilated pairs
    δ_{αZ} + α^{−1}δ_{Z/α} are self-dual; the pair α = √5 with weight −√5 and the pair α = √5/2 with weight +√5 remove the atoms at 1/√5
    and 2/√5 (the masses at 0 add to −√5 − 1 + √5 + 2 = 1); μ_s = δ₀ + ν, ν signed and carried by |x| ≥ √5/2 > 1, μ̂_s = μ_s (theta
    relation to 5.5e−40; the Fejér identity holds BY CANCELLATION). F = 5^{s/2}L(s, χ₅) + D(s)ζ(s) has Riemann's exact FE, simple poles at 0, 1,
    residue 1, finite order, every frequency > 1 — and a zero at s₀ = 1.32691215092364 + 33.2635142708346i (|F(s₀)| = 5e−41; 5 zeros in
    [−1,2]×[0.5,40], 3 on the line). `verify-O/o3, o4, o4b`. The family is infinite-dimensional (every even real primitive χ mod q with root
    number +1). A NEW RH-FALSE CONTROL: exact Γ-factor, conductor 1, gap intact, no Euler product, dN signed — it isolates POSITIVITY (not
    the FE, not the gap) as the input that rigidifies; T3's a_k ≥ 0 cannot be dropped.
(f) DOUBLE POLE AT s = 1 (N(x) ~ Ax log x) with Riemann's Γ-factor: R contains c₁ + c₂ log|t|; (F_R) applies. Not pursued.

## 9. Controls (mandatory; outputs printed in `verify/v3_continuous_sketch_and_controls.log`)

CONTROL 1 — the virtual curve over F₅ (rung 1). A Beurling system over F_q is b_d ∈ Z_{≥0} (closed points of degree d),
Z(u) = Π_d (1 − u^d)^{−b_d}; frequencies are q^d, integral BY CONSTRUCTION.
(i) The analog of T holds at genus 0, trivially and without positivity (P): if Z is meromorphic on C with only simple poles at 1 and
    1/q and Z(1/(qu)) = qu²Z(u) (the P¹ equation), then L(u) := (1 − u)(1 − qu)Z(u) is entire with L(1/(qu)) = L(u), so
    L(u) → L(0) = 1 as u → ∞; Liouville gives L ≡ 1 and Z = 1/((1 − u)(1 − qu)). (Hamburger ↔ this Liouville step; T's Step 1,
    which manufactures integrality, has no work to do over F_q.)
(ii) It FAILS at genus g ≥ 1: Z(1/(qu)) = q^{1−g}u^{2−2g}Z(u) leaves L of degree 2g with g free coefficients, and b_d ≥ 0 cuts out a
    region containing RH-false points. C: over F₅, g = 1, L = 1 − tu + 5u²: among t ∈ {−12, …, 12}, b_d ≥ 0 for all d ≤ 60 exactly for t ∈ {−5, …, 6};
    Hasse |t| ≤ 2√5 holds for t ∈ {−4, …, 4}; RH-FALSE admissible: t = ±5 (t = 6 is the empty system Z ≡ 1). The virtual curve is
    t = 5: N₁..N₆ = 1, 11, 76, 451, 2501, 13376; b₁..b₆ = 1, 5, 25, 110, 500, 2215; min_{d≤60} b_d = 1; FE residual 8e−32; zeros at
    Re s = 0.79899, 0.20101.
(iii) Dictionary. The completed function-field zeta has ζ_C(1 − s) = q^{(2g−2)(s−½)}ζ_C(s): "conductor" q^{2g−2}, minimal (q^{−2}) exactly
    at g = 0, where it is rigid — the analog of Theorem C (minimal conductor 1, attained only by ζ). The virtual curve sits ONE STEP
    above the minimum. Its Q-side analog is therefore not conductor 1 (where T forbids any twin) but conductor q > 1: Q_cond (§8(b)).
    WHY the rigidity fails there and not over Q at conductor 1: over F_q the free data is the L-polynomial, and positivity (b_d ≥ 0)
    is cheap — Möbius inversion of N_n = q^n + 1 − Σα_i^n asks roughly |α_i| < q plus finitely many small-degree checks, far weaker
    than Hasse's |α_i| = √q, because ~q^d/d closed points of degree d absorb the change; over Q, T shows that positivity + the
    archimedean gap (0, 1) leave no free data at all at conductor 1.
CONTROL 2 — F_{5,5} = ζ(s)(1 + 5·5^{−s} + 5^{1−2s}). Nonnegative integer coefficients; FE at conductor 25 (theta relation to 1e−60, v1);
    identity (C_q) holds (8.8 = 8.8, v1); zeros of the factor at σ = 0.79899, 0.20101 (v3) — the SAME numbers as the virtual curve,
    because 1 + 5u + 5u² is the L-polynomial of the admissible t = −5 genus-1 datum over F₅. Over F₅ that datum has b_d ≥ 0; over Q
    the same polynomial sits on the single prime 5, where ζ's own Λ-mass is 1/k at 5^k, and Λ_F(5^k)/log 5 = 6, −14, 51, −174, 626, −2249
    (v3): Λ(25) < 0. T does not apply (q = 25 ≠ 1). LESSON: at conductor > 1, positive coefficients + exact FE do NOT imply RH;
    only Λ ≥ 0 removes F_{5,5} from the Beurling class — the one-prime obstruction of N3 (the Hasse margin at a single prime),
    seen from the Beurling side. Q_cond asks precisely whether Λ ≥ 0 can coexist with an exact FE at q > 1.

## 10. CLOSE — T (theorem)

THEOREM T (positive Hamburger theorem; rigidity of Spec Z among Beurling systems). If dN ≥ 0 is carried by [1, ∞), has polynomial
growth, and ξ_F(s) = π^{−s/2}Γ(s/2)∫x^{−s}dN(x) satisfies Riemann's functional equation with poles only at 0 and 1 (simple) and growth
(G'), then dN = ρΣ_{n≥1}δ_n. Hence the rational primes are the ONLY Beurling system — discrete or continuous, uniformly discrete or
not — whose zeta satisfies Riemann's functional equation (T1, T2); and a general Dirichlet series with nonnegative coefficients and
frequencies ≥ 1 satisfying it is a multiple of ζ (T3). Proof §4 (Fejér kernel + periodicity; ≈ 15 lines on top of Prop. R, §3).
SCOPE (exact): Γ-factor π^{−s/2}Γ(s/2), conductor 1, poles only at 0, 1 (simple), growth (G'), dN ≥ 0 on [1, ∞). Uses neither the
Euler product (beyond dN({1}) = 1) nor uniform discreteness nor Hamburger. Second, independent proof on the u.d. class (Prop. U,
§6: Lev–Olevskii + Hilberdink's pigeonhole + Hamburger). Companion: THEOREM C (§8(b)) — conductor q ≥ 1, equality only for ζ, and the
identity (C_q) for q > 1.
STATUS. (P) with full proofs in §3, §4, §6, §8(b); numerics in `verify/` (v1, v2, v2b, v3, logs) are consistency checks, not load.
Recalled, not load-bearing: the LP/Cohn–Elkies folklore remark (§5(g)); Karamata (§3); Kaczorowski–Perelli analogy (§8(b)).
`[novelty: dual-checked (read-O §3, Session 38)]` for T1–T3 and C: not printed in any source read (three bodies unverified: BC56 beyond p. 336,
CM57, Córdoba); the measure-theoretic core is a routine adaptation of Cohn–Elkies p. 695 + Siegel's periodicity (§5(g)).
NEAREST PUBLISHED OBJECTS (10(n)). T3 ↔ Hamburger's second theorem (Burnol 1106.4749 line 160: f ordinary, dual frequencies ≥ 1 ⟹ cζ).
T1/T2 ↔ the open question of Hilberdink–Lapidus 2006 (p3-22c1 lines 125–128) and Diamond–Zhang p. 1. C ↔ degree-1 conductor rigidity
in the Selberg class (zoo I.7). (F_R) ↔ Hilberdink–Lapidus Theorem 3.2(b) residual H.

WHAT THIS MEANS FOR THE PROGRAM (read against §0(d)–(f) of the charter).
1. The rung-Z twin question has answer NO at conductor 1: there is no RH-false (or any other) Beurling system with Riemann's exact FE.
   The axiom set {Euler product, Λ ≥ 0, exact Riemann FE (poles only at 0, 1; growth (G'))} has exactly ONE model, ζ — and
   {dN ≥ 0 on [1,∞), polynomial growth, exact FE} has exactly the models ρζ, ρ ≥ 0 (one up to scale; read-O m3).
   So no "axiomatic" RH proof from these axioms has any leverage beyond a proof for ζ itself, and no control exists inside the class;
   N4's survivor property (4) ("fail on the rung-1 twin") has no conductor-1 counterpart over Q.
2. The rigidity is ARCHIMEDEAN and ADDITIVE: it is the equality case of a Fourier-side linear-programming inequality (Fejér), using
   positivity only as dN ≥ 0 — the orchestrator's reading ("RH needs multiplicative and additive structure together") is sharpened:
   at conductor 1 the additive structure plus bare positivity ALREADY determines everything, so the multiplicative structure is
   never tested. RH-false controls with Λ ≥ 0 and an exact FE exist only after paying one of two prices: extra poles in the strip
   (orchestrator's continuous systems, §8(a), (d)) or — possibly — conductor q > 1 (Q_cond, open; F_{5,5} misses only Λ ≥ 0). Without positivity there is a third price, already paid at conductor 1 with the gap
   intact: signed coefficients (read-O R1, §8(e): a zero at 1.32691 + 33.26351i).
3. Extremal reading (answers the shape proposed in the tournament read-F §4): ζ is the UNIQUE equality case of an inequality among
   positive self-dual measures with gap 1, and the defect 2Σ_k sinc²(n_k) is a positive form — but in the POSITIONS OF THE
   GENERALIZED INTEGERS, not in the zeros. Transporting it to the zero side is not done here and is not claimed.
SUCCESSOR QUESTIONS (ranked). (1) Q_cond: a Beurling system (dΠ ≥ 0) with Riemann's FE at conductor q > 1 — construct or refute;
this is the Q-side location of the virtual-curve twin (§9(iii)). (2) Discrete Beurling systems with FE and finitely many extra poles
(§8(d)). (3) The signed solutions with gap (§8(e), populated and RH-false by read-O R1): is every one a finite combination of twisted and
dilated Poisson combs (§12)?
Charter stop condition: met in the form "the question is settled" — by proof, not by a printed theorem and not by an example.

## 11. Addendum — first moves on Q_cond (recorded for the successor unit; nothing here is load-bearing)

(i) No FINITE Euler-factor modification of ζ reaches conductor q > 1 (P): E(s) = Π(1 − a_i^{−s})^{±1} has all zeros/poles on Re s = 0,
    while E(s)/E(1 − s) = q^{1/2−s} would need them mirrored onto Re s = 1.
(ii) Writing E = ζ_P/ζ = q^{1/4 − s/2}H(s) with H(s) = H(1 − s) (necessary and sufficient for the conductor-q FE), H must grow like
    q^{|σ|/2} in both real directions; every H tried (2cosh((s−½)ℓ/2) products, F_{a,q}-type additions) gives Λ < 0 at high powers
    of the largest frequency (§8(b)). No proof that this is forced.
(iii) An LP family that uses the multiplicative structure (P): for a generalized prime p, ν − D_pν ≥ 0 (coefficients of ζ_{P∖{p}}), and
    FT(ν − D_pν) = ν − p^{−1}D_{1/p}ν + ρ_q(1 − 1/p)δ₀ (the Lebesgue parts cancel). Pairing with the Fejér function of width r gives
        ρ_q(1 − 1/p) ≥ (2/p) Σ_{n_k < p} c_k (1 − n_k/p),   and for finite S ⊂ P the Möbius-weighted analog (equality for Z).
    Combining these Euler-side inequalities with (C_q) is the natural first attack on Q_cond (construct-or-refute).

## 12. Addendum (Session 38, from read-O R2, re-derived by the orchestrator) — the two-system version of T

THEOREM T′ (Hilberdink–Lapidus (3.5) with Riemann's Γ-factor on both sides). Let dN₁, dN₂ ≥ 0 on [1, ∞) have polynomial growth,
ξ_i(s) := π^{−s/2}Γ(s/2)∫x^{−s}dN_i, and suppose ξ₁(s) = ξ₂(1 − s), the poles of ξ₁ only at 0 and 1 (simple), and (G′) for ξ₁. Then
dN₁ = dN₂ = ρΣ_{n≥1}δ_n. Proof. With ρ_i = Res_{s=1}ξ_i the FE gives Res_{s=0}ξ₁ = −ρ₂; the contour shift of Prop. R gives
ρ₁ + 2ψ₂(1/x) = √x(ρ₂ + 2ψ₁(x)) and linear growth of both N_i. For μ₁ := ρ₂δ₀ + dN₁ + dN₁^∨ and μ₂ := ρ₁δ₀ + dN₂ + dN₂^∨ this reads
⟨μ̂₂, g_x⟩ = ⟨μ₁, g_x⟩, so μ̂₂ = μ₁ (Lemma G) and μ̂₁ = μ₂. Pairing with the mollified Fejér function both ways: ρ₂ = ρ₁ + 2∫S dN₂ and
ρ₁ = ρ₂ + 2∫S dN₁; adding, ∫S dN₁ + ∫S dN₂ = 0, so both vanish (positivity), ρ₁ = ρ₂ = ρ, and both measures live on N; then μ₂ = μ̂₁ is
1-periodic and carried by Z, so μ₂ = ρδ_Z = μ₁. ∎ So two DIFFERENT Beurling systems cannot be Riemann-FE partners either — the
positive answer to Hamburger's "f and g both general" problem (Burnol Thm 2 gives only an equivalence, with complex coefficients).
Reader's ranked next questions: (1) Q_cond; (2) can (G′) be dropped for dN ≥ 0; (3) classify the signed solutions with gap (§8(e)):
is every one a finite combination of twisted and dilated Poisson combs; (4) the two-system version at conductor q > 1 (with Theorem C).
