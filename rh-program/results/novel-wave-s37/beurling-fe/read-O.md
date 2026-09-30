# read-O — OPUS READER on seed M1a `beurling-fe` (NOTE.md, Theorem T "positive Hamburger")

Reader: Opus 5.5 (second model of the dual-model check; standing orders 5, 7, 11). Date: 2026-10-01.
Independent of the orchestrator's parallel read (its folder `verify-F/` was not opened).
Scripts and logs of this read: `verify-O/`. Conventions as in NOTE: ✓ = re-derived at the line; GAP = stated with the fix.

VERDICT LINE: (pending — written when §1–§4 land)

## §1. Re-derivations at the line (NOTE §3, §4, §6, §7, §8(a)(b), §9)

(a) Proposition R. (A)⟹(B) ✓. Mellin inversion ψ(x) = (1/4πi)∫_{(c)}ξ_F(s)x^{−s/2}ds, c > max(A,1): justified by Fubini against the
    Cahen–Mellin integral (∫|Γ((c+iτ)/2)|dτ · ∫t^{−c}dN < ∞); ψ(x) < ∞ for all x > 0 by polynomial growth. Edges: |ξ_F(c+it)| ≤
    π^{−c/2}|Γ((c+it)/2)|F(c) = O(|t|^{(c−1)/2}e^{−π|t|/4}); on Re s = 1−c the same by the FE; H(s) = s(s−1)ξ_F(s) is entire with
    H(1−s) = H(s). Strip width 2c−1; PL needs growth < exp e^{α|t|} with α < π/(2c−1): (G′) with ε < π/(2c−1) gives it ✓. So H is
    bounded, ξ_F = O(|t|^{−2}) uniformly, horizontal segments vanish. (G′) is used HERE ONLY ✓ (the NOTE says so, §5(d)).
    Residues ✓: Res_{s=0}ξ_F = −Res_{s=1}ξ_F is FORCED by the FE (ξ_F(s) = ξ_F(1−s) ~ ρ/(1−s−1)); they are not an extra hypothesis.
    The reflected integral: ∫_{(1−c)}f(s)ds = ∫_{(c)}f(1−s)ds, giving x^{−1/2}ψ(1/x) ✓. Final line ρ + 2ψ(1/x) = √x(ρ + 2ψ(x)) ✓.
    Side remark (no fix needed): ρ ≥ 0 is automatic — (A)⟹(B)⟹(C) and Steps 1–2 never use its sign (the linear-growth bound
    holds with |ρ| in place of ρ), and Step 2 ends with a_n = ρ for n ≥ 1, a_n ≥ 0. The hypothesis "for some ρ ≥ 0" is redundant.
    (B)⟹(A) ✓ (split at 1: ξ_F = ρ/(s−1) − ρ/s + ∫₁^∞ψ(x)(x^{s/2} + x^{(1−s)/2})dx/x; ψ(x) ≤ e^{−π(x−1)}ψ(1) uses t ≥ 1 AND dN ≥ 0;
    in fact s(s−1)ξ_F = O(|t|²) in strips, stronger than (G′)). (B)⟹N(X) ≤ ½e^π(ρ + 2ψ(1))X ✓ — this step USES dN ≥ 0
    (N(X) ≤ e^πψ(1/X²) and ψ decreasing). (B)⟹(C) ✓ (ĝ_x = x^{−1/2}g_{1/x} with f̂(ξ) = ∫f e^{−2πixξ}; μ, g_x even).
    Lemma G ✓ (u(a) = ⟨T, g_y(·−a)⟩ entire; all Taylor coefficients vanish by parity + ⟨T, t^{2k}g_y⟩ = 0; y^{1/2}g_y ∗ φ → φ in S).
    Karamata remark (not load): (B) ⟹ ψ(y) ~ (ρ/2)y^{−1/2} (y→0+) ⟹ N(x) ~ ρx ✓ (Laplace variable u = t²).

(b) Step 1, the Fejér pairing ✓. φ = (1−|x|)₊ = 1_{[−½,½]} ∗ 1_{[−½,½]}, φ̂ = S = (sin πξ/πξ)² ≥ 0, S = 0 exactly on Z∖{0} ✓.
    MEASURE side: φ vanishes on |x| ≥ 1, the support of dN + dN^∨ (φ(±1) = 0 absorbs the atom at 1) ⟹ ⟨μ, φ⟩ = ρ.
    TRANSFORM side: ⟨μ, φ̂⟩ = ρ + 2∫S dN ≥ ρ. Sign ✓: equality forces ∫S dN = 0.
    Mollification ✓: supp φ_ε ⊂ [−1−ε, 1+ε]; for 1 ≤ t < 1+ε, φ(t−y) ≤ 1 − t + y ≤ ε, so 0 ≤ ∫φ_ε dN ≤ ε·dN([1,1+ε)) → 0;
    φ̂_ε = S·η̂(ε·), |η̂| ≤ 1, dominated by min(1,(πt)^{−2}) ∈ L¹(dN) BECAUSE N(x) = O(x) — i.e. because of the positivity used in (a).
    Conclusion "dN carried by N" ✓ (inner regularity: dN(K) = 0 for every compact K ⊂ {S > 0} ∩ [1,∞)).
    GAP (not an error, prose): NOTE §4 line 126 says positivity enters "only in (F) ⟹ dN carried by N". It also enters in Step 0
    through Prop. R's linear-growth bound, without which S ∉ L¹(dN) is possible for polynomial growth O(x^A), A ≥ 2, and the
    dominated-convergence step fails. MINOR pair m1 (§5).

(c) Step 2, periodicity ✓. With μ = Σ_{n∈Z}a_nδ_n, a_n = O(|n|): ⟨μ̂, ψ(·+1)⟩ = Σa_n e^{2πin}ψ̂(n) = ⟨μ̂, ψ⟩, so μ̂ = μ is
    invariant under x ↦ x+1 and a_{n+1} = a_n ✓. Hence dN = ρΣ_{n≥1}δ_n, F = ρζ, and ρ = Res_{s=1}ξ_F is consistent ✓.
    Cross-check: Poisson summation makes ρδ_Z self-dual, so the conclusion is attained (T is sharp, not vacuous) ✓.

(d) T1–T3.
    T1 ✓. dN({1}) = 1 (every p_j > 1) ⟹ ρ = 1; c(x) = #{j : p_j = x} + #{multisets of ≥ 2 indices with product x, all factors < x};
    strong induction over the locally finite values of the p_j; unique factorization gives the second term 1 (x composite), 0 (x
    prime or x ∉ N) ✓. Polynomial growth is supplied by NOTE §0's standing assumption (ζ_P absolutely convergent for Re s > 1) ✓.
    T2 ✓ with one HIDDEN HYPOTHESIS. Diamond–Zhang's definition of a g-number system (t-50 lines 592–593: "a pair of right
    continuous increasing functions Π and N on [1, ∞) satisfying dN = exp∗ dΠ and Π(1) = 0") carries NO growth condition; growth
    is an extra assumption there (t-50 lines 1817–1823, "(4.1) lim sup N(x)/x^α < ∞"). So polynomial growth is NOT automatic in the
    Beurling framework: a system with super-polynomial N has no half-plane of convergence and (A) is not even formulable. T2 must
    say "with ∫x^{−σ}dΠ < ∞ for some σ" (⟺ ∫x^{−σ}dN = exp∫x^{−σ}dΠ < ∞ ⟺ N polynomial). MINOR pair m2 (it is implicit in (A)).
    The rest ✓: Π(1) = 0 ⟹ dN({1}) = 1; log F = log ζ with the branch fixed by both sides → 0 as σ → +∞; uniqueness of the
    Laplace–Stieltjes transform ⟹ dΠ = Σ_pΣ_k k^{−1}δ_{p^k}; the one-line alternative dN ≥ δ₁ + dΠ ✓.
    T3 ✓ (a_k ≥ 0 makes conditional = absolute convergence, so polynomial growth is automatic once (A) is meaningful; dN({1}) =
    Σ_{λ_k=1}a_k = ρ). Does T3 use dN ≥ 0 only through the pairing? NO: also through Prop. R's linear growth (see (b)); and the
    reader's §6 shows positivity cannot be dropped at all (an explicit signed counterexample with every frequency > 1).
    Prop. U (§6) ✓: Lev–Olevskii Thm 1 (u-30b lines 51–53, complex measures, u.d. support and spectrum) applies; pigeonhole
    x(a − a′) ∈ hZ, a − a′ ∈ hZ∖{0} ⟹ x ∈ Q ✓; b^k | D ∀k ⟹ b = 1 ✓; Nakamura Thm D (lines 170–177: (H1) abs. conv. σ > 1,
    (H2) P(s)F(s) entire of finite order, (H3)) — all three are supplied ✓. Lemma TB (§7) ✓ (k = h∗h, k̂ = ĥ² ≥ 0, Parseval with
    F^{−1}[k(·−a)] = e^{2πiaξ}k̂; μ̂ ≥ 0 gives |⟨μ̂, e^{2πia·}k̂⟩| ≤ ⟨μ̂, k̂⟩).

(e) Theorem C ✓. dN_q = image of dN under t ↦ t/√q, carried by [r,∞), r = q^{−1/2}; ρ_q = Res_{s=1}Λ_F = √q·Res F ✓.
    Pairing with φ_r = φ(·/r), φ̂_r(ξ) = rS(rξ), r/√q = 1/q: ρ_q = rρ_q + 2r∫S(t/q)dN(t), i.e. (C_q) ✓ (sign and factors re-derived).
    q < 1: both sides of (C_q) have opposite signs ⟹ ρ_q = 0, dN carried by qN; μ_q carried by √qZ and 1/√q-periodic ⟹ 1/q ∈ N and
    mass(1/√q) = mass(0) = 0, i.e. dN({1}) = 0 — contradiction ✓. q > 1, ρ_q = 0 ⟹ dN carried by qN ∌ 1 — contradiction ✓.
    "q = 1 iff F = ρζ": ρζ satisfies the conductor-q FE iff q^{s−1/2} ≡ 1 iff q = 1 ✓.
    Hand check of (C_q) (no computer): F = ζ(s)(1 + q^{1/2−s}), dN = Σδ_n + √qΣδ_{qn}; Poisson with f̂ = q(1 − q|ξ|)₊ gives
    Σ_{n≥1}S(n/q) = (q−1)/2; both sides of (C_q) equal (q−1)/√q exactly ✓. F_{5,5}: ρ_q = 5·(1+1+1/5) = 11, LHS 11·(4/5) = 8.8;
    RHS (2/5)(Σ_{n≥1}S(n/25) + 5Σ_{n≥1}S(n/5)) = (2/5)(12 + 10) = 8.8 ✓ exactly (the NOTE's 8.8 = 8.8 is not a truncation accident).

(f) §8(a) continuous sketch ✓: G(1−s) = G(s) checked factor by factor; log((s−c)/(s−a)) = ∫₁^∞x^{−s}(x^a − x^c)dx/(x log x)
    (derivatives in s agree, both → 0 as s → +∞) ✓; f ≥ 0 for a ≥ β ≥ ½ since ∂_c(x^c + x^{1−c}) = log x(x^c − x^{1−c}) ≥ 0 ✓.
    §8(b) Λ < 0 claims ✓: log(1 + q^{1/2}q^{−s}) has mass −q^j/(2j) at q^{2j}; q = √2: dΠ(8) = 1/3 − 2^{3/2}/6 = −0.138 ✓.
    F_{5,5} ✓: P(s) = 1 + 5^{1−s} + 5^{1−2s} satisfies P(1−s) = 25^{s−1/2}P(s), so the conductor is 25 ✓; with 1 + 5u + 5u² =
    (1−αu)(1−βu), Λ(5^k)/log 5 = 1 − (α^k + β^k) = 6, −14, 51 ✓. §9 genus 0 ✓ (L(1/(qu)) = L(u), L → L(0) = 1 at ∞, Liouville);
    genus 1, t = 5: roots of 5u² − 5u + 1 at |u| = 0.7236, 0.2764 ⟹ Re s = 0.20101, 0.79899 ✓; t = 6 is Z ≡ 1 ✓.
    §8(d) (F_R) ✓ (sign: 2∫S dN = ⟨R, φ⟩ with R := μ̂ − μ; ψ̂ ≥ 0 forces ψ̂ real hence even).
    §8(e) ✗ as a VERDICT (not as mathematics): "open" is wrong — see §6 R1 and FIX-FIRST F1.

## §2. Independent re-run (`verify-O/`, own routes; the writer's scripts were read for inputs only, never re-executed)

o1 `o1_fejer_exact.{py,log}` — the Fejér sum in CLOSED FORM. Route: Poisson for x ↦ S(ex) gives T(e) := Σ_{n≥1}S(ne) =
  ½[e^{−1}(1 + 2Σ_{1≤k<e}(1 − k/e)) − 1] (= 0 iff e ∈ N); a near-solution is P = primes ∖ {5,7,11} ∪ {free primes} (2, 3 cancel),
  dN_P = dN_Z ⊛ E (E = signed Euler-factor measure), so S_F = Σ_e E(e)T(e) — no truncation in n (writer: brute sum to 20000).
  Sanity: T(1.5) = 1/18 = 0.0555555555556 = brute sum + mean-value tail. Results (atoms e ≤ 1e10; e ≤ 1e6 agrees to 1e−13):
    K=3 S_F = 1.654343e−3 (writer 1.6541e−3) · K=4 5.358231e−3 (5.3576e−3) · K=5 2.612375e−3 (2.6116e−3) · K=6 3.075454e−3 (not in v2b)
    · K=7 8.744635e−3 (8.7432e−3) · Z: S_F = T(1) = 0 EXACTLY. The writer's values sit 2e−7..1.4e−6 below the exact ones = their
    truncation tail. Every near-solution violates (F) by 2S_F = 3.3e−3 … 1.7e−2; Z satisfies it exactly. ✓ NOTE §5(h), §7.
o2 `o2_theta_defect_jtheta.{py,log}` — theta defect by Jacobi theta: ψ_P(x) = Σ_e E(e)ψ_Z(e²x), ψ_Z via mpmath jtheta, 40 digits,
  x = 2^{−6}..2^{6}. ρ = 1 on 2^{−3}..2^{3}: 1.09e−4, 8.69e−5, 1.08e−4, 2.50e−5, 9.83e−5 (K = 3..7) — matches v2b to 3 digits ✓.
  ρ = ρ_true (the residue (B) demands; 0.7068, 0.8559, 0.9340, 1.0760, 1.2032): max |D| = 1.32, 0.73, 0.18, 0.64, 1.59 on the wider
  range. Z: 1.8e−40. Mellin side: |E(s) − E(1−s)| at s = 0.3+7i = 0.77, 0.35, 0.87, 0.44, 0.18 (FE fails outright) ✓.
o3 `o3_signed_counterexample.{py,log}` — POSITIVITY IS NECESSARY (new; see §6 R1). μ_s = Σ_{n∈Z}χ₅(n)δ_{n/√5} − (√5δ_{√5Z} + δ_{Z/√5})
  + (√5δ_{(√5/2)Z} + 2δ_{(2/√5)Z}): atoms at 1/√5, 2/√5 cancel exactly (0, 0); mass at 0 is 1; smallest positive atom √5/2 = 1.1180;
  first atoms 1.1180: +√5, 1.3416: −2, 1.7889: +2. Theta relation to 5.5e−40; Fejér: Σ_{t>0}m(t)S(t) = 0 (closed form, −1e−41), so
  (F) HOLDS with non-integral atoms; ξ_F(s) = ξ_F(1−s) to 1e−41; Res_{s=1}F = D(1) = 1.
o4/o4b `o4_signed_rh_false.{py,log}`, `o4b_locate_offline.{py,log}` — that signed F is RH-FALSE: zero at
  s = 1.32691215092364 + 33.2635142708346i (|F| = 5e−41; FE partner −0.3269 + 33.2635i, |ξ_F| = 5e−52), inside the half-plane of
  absolute convergence. Argument principle on [−1,2]×[0.5,40]: 5 zeros; sign changes of ξ_F(½+it): 3 (t = 19.1868, 25.6164,
  36.5260) — the deficit 2 is exactly the off-line pair. (A first version of o4 keyed its grid by floats and missed the zero;
  fixed, logged in the script.)
o5 `o5_conductor_new_example.{py,log}` — (C_q) on a positive example the writer did not use: F = ζ(s)(1 + 5^{1/2−s}) + L(s,χ₅), q = 5,
  coefficients 1 + χ₅(m) + √5·1_{5|m} ≥ 0: LHS = RHS = 4/√5 = 1.788854382 (m ≤ 2e5 + exact periodic tail); the sub-identity
  Σχ₅(m)S(m/5) = 0 to 2e−16; conductor-5 FE to 1e−31 ✓. (It fails Λ ≥ 0 — a Selberg-class-free positive solution, as NOTE §8(b) says.)

## §3. Prior-art gate, at the page (local corpus grepped after pdftotext of all 462 corpus PDFs; web one request at a time)

Legend for the last column: CONTAINS T / STRONGER / INCOMPARABLE / METHOD (prints T's method, not T's statement).
New files saved under `sources/`: arxiv-math0110009 (Cohn–Elkies), arxiv-math0607446 (Cohn–Kumar), arxiv-1312.6884 (Lev–Olevskii
Invent), arxiv-1502.06283 (Kolountzakis), arxiv-1701.00265 (Radchenko–Viazovska), cm-1959-bams (Chandrasekharan–Mandelbrojt,
AMS archive), meyer-2016-pnas.md (Firecrawl), zbmath/ (API records), jstor-1969614-landing.md; queries in arxiv-queries/reader-*.

| # | source | where read | what it proves | relation to T |
|---|---|---|---|---|
| 1 | Hamburger 1921–22, standard form | Nakamura 2008.02570 Thm D (sources, lines 170–177); Steuding course notes §3.3 Thm 3.8 (corpus p3-29a; proof ends "the residues at in and i(n+1) are equal. Thus, a(n) = a(n+1)"); Burnol 1106.4749 lines 140–160 (second theorem); Titchmarsh §2.13 not in the corpus (only cited) | ORDINARY Dirichlet series, complex coefficients, P(s)F(s) entire of finite order, Riemann FE ⟹ F = Cζ; second theorem: f ordinary, g = χf(1−s) general with frequencies ≥ 1 ⟹ cζ | INCOMPARABLE: Hamburger needs integer frequencies on one side and no positivity; T takes general frequencies on BOTH sides (f = g) and needs a_k ≥ 0. T's Step 2 (periodicity ⟹ equal coefficients) is Hamburger/Siegel's classical device (see #4) |
| 2 | Kahane–Mandelbrojt 1958, ASENS 75, 57–80 | sources/kahane-mandelbrojt…txt: intro 41–75; Thm 1 306; Prop. 7 958–1010; Thm 4 + Cor. 1025–1043; Thm 5 + Cor. 1047–1063 | complex coefficients: FE ⟺ Poisson-type formula (Thm 1); every closed interval of length D(spectrum) meets the support (Prop. 7); spectral gaps ≤ Δ(support), Δ(λ)Δ(μ) ≥ 1 (Thm 4, Cor.); EQUALITY only for Dirac combs up to dilation/translation (Thm 5); even case Δ = 1: ζ, (2^s−1)ζ, (2^{1−s}−1)ζ (Cor.) | INCOMPARABLE. KM's rigidity is the equality case of a DENSITY inequality. On T's μ it yields only Δ(supp μ) ≥ 1 (the gap (0,1) in the spectrum), an inequality; T's identification needs the positivity-based gap pairing. KM58 does not contain T, nor T3 |
| 3 | Chandrasekharan–Mandelbrojt, Bull. AMS 65 (1959) 358–362 | sources/cm-1959-bams.txt p. 358–359 (Thms 1–3, Lemma 2) | complex a_n, b_n: h_λh_μ = 1 and δ odd ⟹ λ_n, μ_n arithmetic progressions (Thm 1); via CM57 Thm 1 (quoted p. 359): D_μ < ∞ ⟹ λ_{n+1} − λ_n ≤ D_μ, D_λD_μ ≥ 1, h_λh_μ ≤ 1 | INCOMPARABLE: needs the uniform-gap product = 1 (so uniform discreteness); T needs no separation. On the u.d. class it would give T only if h = 1 were known — it is not |
| 4 | Bochner–Chandrasekharan, Ann. Math. 63 (1956) 336–360 | p. 336 ONLY (JSTOR public preview, read in the browser 2026-10-01); body UNVERIFIED (login wall); subject per CM59 p. 358 (read): upper bounds for the number of linearly independent solutions, uniqueness "in certain cases" | p. 336: Hamburger's theorem incl. his case g(1−s) = Σb_nλ_n^{−1+s}; Siegel's proof: FE ⟹ modular relation (1.2) ⟹ (1.3), whose periodicity gives a_k = a_{k+1} | not contained as far as read; body UNVERIFIED. T's Step 2 = Siegel's periodicity step printed here |
| 5 | Chandrasekharan–Narasimhan, Ann. Math. 74 (1961) 1–23 | p. 1 only (JSTOR preview, browser); body UNVERIFIED | FE (Hecke type) ⟺ arithmetical (Voronoi–Riesz) identities | INCOMPARABLE (equivalences, no rigidity) |
| 6 | Hilberdink–Lapidus 2006 | sources/p3-22c1…txt 125–128 (open question), 1025–1030 ((3.5): G₁(1−s)ζ₁(1−s) = G₂(s)ζ₂(s), "two (possibly different) prime systems"), Thm 3.2 1042–1057, Addendum (Bochner 1951) ~1070 | FE ⟺ modular identity with a finite residual H; which Beurling systems satisfy (3.5) is called "difficult", left open | T answers (3.5) for G₁ = G₂ = π^{−s/2}Γ(s/2), and — reader's R2 (§6) — even for ζ₁ ≠ ζ₂. NEW relative to HL |
| 7 | Lagarias 1999, Forum Math. 11, 295–312 | title checked: "Beurling generalized integers with the Delone property" (De Gruyter capture, sources/lagarias-1999-delone-abstract.md line 92); no arXiv preprint (reader query, 0 hits); body UNVERIFIED (paywall). No 1999 Lagarias paper titled "… and the Riemann hypothesis" was found | abstract: Delone g-integer semigroups contained in Z = all but finitely many primes plus finitely many composites | INCOMPARABLE (no FE in the abstract) |
| 8 | Córdoba 1988 (CRAS 306, 373–376) / 1989 ("Dirac combs", LMP 17, 191–196) | primary NOT reachable; statement as reported by Lev–Olevskii 2015 p. 2 (sources/arxiv-1312.6884…txt, read) | "if µ is the sum of equal atoms along a discrete set Λ and µ̂ is a positive pure point measure, then Λ is just a lattice" | INCOMPARABLE: equal masses + discreteness + positive pure-point spectrum; T allows arbitrary positive masses and even continuous dN, but needs μ̂ = μ and the gap. Primary UNVERIFIED |
| 9 | Lev–Olevskii, Invent. Math. 200 (2015) 585–606; RMI 32 (2016) | arXiv 1312.6884 Thms 1–3 (sources, lines ~95–125); u-30b lines 51–53, 65–68 | 1-D complex measures with u.d. support and spectrum ⟹ support in finitely many translates of one lattice (Thm 1); positive in Rⁿ (Thm 2); explicit structure (Thm 3); u.d. cannot be relaxed to "discrete" for signed measures (2016 Thm 2) | INCOMPARABLE (T drops u.d., needs positivity + self-duality + gap). LO Thm 1 powers the NOTE's second proof (Prop. U) on the u.d. class ✓ |
| 10 | Meyer, PNAS 113 (2016) 3152–3158 | Firecrawl capture sources/meyer-2016-pnas.md lines 41–51, 125–127, 185–275 | crystalline measures that are not generalized Dirac combs (Guinand-type, signed); a signed self-dual comb σ = Σχ(k)δ_{k/2} (χ: 0, 2, −1 by k mod 4; line 265) — atoms at ±1/2, no gap | INCOMPARABLE (no positivity or gap theorem). Consistent with the reader's signed example R1 |
| 11 | Kolountzakis, JFAA 22 (2016) | arXiv 1502.06283 abstract + §1 (sources) | simple signed discrete Fourier pairs not obtainable from finitely many PSF applications | INCOMPARABLE |
| 12 | Cohn–Elkies, Ann. Math. 157 (2003) 689–714 | arXiv math/0110009 (sources): Thm 3.1 lines 242–253 (p. 694); the 1-D example lines 306–316 (p. 695): "(1 − |x|)χ[−1,1](x) … its Fourier transform is (sin πt/πt)² … a sharp bound"; §5 lines 461–505 (p. 698–699): for a lattice, sharpness forces f = 0 on Λ∖{0}, f̂ = 0 on Λ*∖{0}; proof of Thm 3.1 is for PERIODIC packings via Poisson summation | the LP bound; in dimension 1 with T's Fejér function it is sharp for Z | METHOD. T's Step 1 is exactly the Cohn–Elkies 1-D pairing with their function, applied to a positive self-dual measure instead of a periodic packing. The uniqueness statement "μ ≥ 0, μ = ρδ₀ on (−1,1), μ̂ = μ ⟹ μ = ρδ_Z" is NOT printed (CE only discuss which f is sharp for a given lattice). NOTE §5(g)'s recalled remark is thereby VERIFIED in this sense |
| 13 | Cohn–Kumar, JAMS 20 (2007) 99–148 | arXiv math/0607446 §9, Prop. 9.6 (sources, lines ~2305–2320) | in R¹ the energy LP bound is sharp for Z among periodic configurations (completely monotonic potentials), with ĥ supported in [−1,1] | METHOD/INCOMPARABLE (configurations and energies, not self-dual measures) |
| 14 | Radchenko–Viazovska, Publ. IHÉS 129 (2019) | arXiv 1701.00265 lines 140–230 (sources) | Fourier interpolation from f(±√n), f̂(±√n); remarks that the formula yields crystalline measures μ_x | does NOT discuss uniqueness of Poisson summation for positive self-dual measures with a gap; not relevant beyond context |
| 15 | Olevskii–Ulanovskii 2020; Gonçalves 2023; Favorov 2024; Kurasov–Sarnak 2020 (all on disk) | p2-19b 62–72; u-28b 662–668; u-34b 66–110; u-20b line 10, 785–795 | O–U Prop. 1: μ ≥ 0, |μ̂| tempered ⟹ translation-bounded. Gonçalves Thm 5: nonnegative u.d. measures with masses ≥ δ and spectral gap (0, b) ↔ Hermite–Biehler E. Favorov: non-negative Poisson measures are a.p.; uniqueness from agreement on large balls; structure under separation. K–S: positive crystalline measures that are not Dirac combs exist | INCOMPARABLE (each needs u.d./mass bounds/closeness to a known measure, none uses self-duality + gap). By T, none of the K–S positive measures can be self-dual with gap (−1,1)∖{0} |

GATE VERDICT (reader). (i) THEOREM T in its Dirichlet-series/Beurling form (and T1–T3) is NOT printed in any source read above; the
closest printed rigidity theorems (Hamburger, KM58 Thm 5, CM59 Thm 1) need integer frequencies or a density/uniform-gap equality
and allow complex coefficients — incomparable with T (positivity, no discreteness). Hilberdink–Lapidus record the question as open.
Status: NEW, now dual-checked, with three bodies UNVERIFIED (Bochner–Chandrasekharan 1956 beyond p. 336, Chandrasekharan–Mandelbrojt
1957, Córdoba 1988/89 primary). (ii) The MEASURE CORE is a routine adaptation of printed methods — Cohn–Elkies p. 695 (the pairing,
same function) plus Siegel's periodicity (BC56 p. 336; Steuding Thm 3.8) — but the uniqueness statement itself was not found in print.
Label it "folklore-grade method, statement unprinted (as read)". It is NOT "KNOWN (cite page)".
