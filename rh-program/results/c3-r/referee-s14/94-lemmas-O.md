# REFEREE REPORT O — probe 9.4 note, §§3–7: Lemmas A, B, C, D and Proposition 1 (the transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission).
**Date:** 2026-09-02 (Session 14).
**Referee:** referee O, one of two independent referees on this item (standing order 7). I did not see, and do not assume anything about, the other referee's findings.
**Note under review:** `results/c3-r/probe-9.4-note.md` (probe 9.4, dated 2026-08-26), read in full.
**Binding prior record read in full first:** `results/c3-r/probe-9.3-adjudication.md`.
**Debt discharged here:** 9.4 note §8 item 1 (DQ-T), i.e. Lemmas A–D and Proposition 1 (§§4–6), plus the two extra checks assigned to me: §3's freshman's-dream N-invariance argument and §7's Haar formal count.
**Standing order 5:** every source claim below was read this session from the on-disk PDF at the stated printed page, via a fresh `pdftotext -layout` extraction plus, where a display was ambiguous, a 150-dpi page render read by vision. Nothing is recalled. Program-internal results taken without re-derivation are named as such; where I re-derived them anyway I say so.

---

## 0. VERDICT SUMMARY (stated first)

| Item | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| **Lemma A** (mod-p-additive ⟺ Teichmüller, incl. converse) | **PASS-WITH-REPAIRS** | 0 | 1 (F1) | 2 (F12b, F13) |
| **Lemma B** (archimedean defect bound selects ∅ on the periodic locus) | **PASS** (verified, and strengthened) | 0 | 0 | 1 (F12) |
| **Lemma C** (Aut(C) ↠ Aut(μ(C)) = Ẑ×, via Steinitz) | **PASS** | 0 | 0 | 1 (F10) |
| **Lemma D** (Aut(C)-action: equivariance + class stability + packet coordinates) | **PASS** | 0 | 0 | 2 (F7, F11) |
| **Proposition 1** (the equivariance no-go) | **PASS** — theorem correct as stated, every input verified | 0 | 0 | 1 (F7) |
| **The Corollary to Prop. 1** (reach of the no-go) | **PASS-WITH-REPAIRS** | 0 | 1 (F3) | 0 |
| **§4 Consequence 2 / D3** (transport collapses to the Theorem-C cut) | **PASS-WITH-REPAIRS** | 0 | 1 (F2) | 0 |
| **§0 framing "closed trichotomy"** | **FAIL as worded** (self-contradicted by §6) | 0 | 1 (F4) | 0 |
| **§3 freshman's-dream N-invariance argument** | **PASS-WITH-REPAIRS** (conclusion right, reason wrong) | 0 | 0 | 1 (F8) |
| **§7 Haar formal count** | **PASS-WITH-REPAIRS** (arithmetic right, justification a non sequitur) | 0 | 0 | 1 (F9) |
| Citation hygiene | — | 0 | 0 | 2 (F5, F6) |

**Overall: PASS-WITH-REPAIRS. 0 FATAL, 4 MAJOR, 9 MINOR.**

The mathematical core of DQ-T survives intact. **Proposition 1 is a correct theorem** and I re-derived it end to end; so are Lemmas B, C and D. **Lemma A is true but is stated in a generality its proof does not reach**, and the repair is routine (I give two). The four MAJOR findings are all against *claims the note makes around* the lemmas — the identification of the transported class with E(a₀), the advertised reach of the no-go corollary, and the word "closed" in "closed trichotomy" — not against any lemma statement. Nothing here reopens the 9.3 adjudication.

---

## 1. Method, and exactly what I read

I re-derived every step of §§3–7 from scratch, in my own words, from the primary sources, and only then compared with the note. Where the note cites a location I opened that location and quoted it. Where I found a gap I tried both to fill it (replacement text given in §11) and to break it (counterexample attempts reported in situ).

Extractions made fresh this session: `pdftotext -layout` on `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf` (119 pp; PDF page = printed page throughout, verified) and on `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. `pdftotext` silently drops overlines and superscript `×` in this file, so every displayed formula I quote as load-bearing was additionally checked on a 150-dpi `pdftoppm` render read by vision (this is how finding **F6** was caught). Full page list in §12.

---

## 2. The substrate: packet coordinates, re-derived and verified verbatim

Everything in §§4–5 of the note runs on [x-03] §5. I verified the following on the printed pages named.

**(a) Admissibility, [x-03] Def. 4.1, p. 27, verbatim:**

> "**Definition 4.1.** A class E of characters χ : κ× → C× on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ◦ σ resp. χ_ν = χ ◦ ( )^ν is in E. Moreover the characters in E should satisfy (Tors)."

The two side conditions, same page, verbatim:

> "(Tors) the group ker(χ)_tors = ker(χ |_{µ(κ)}) is finite and |(ker χ)_tors| ∈ N₀."
> "(Image) Only if char κ > 0. If χ(κ×) is torsion, then κ× is torsion as well, i.e. κ× ⊗ Q ≠ 0 implies χ(κ×) ⊗ Q ≠ 0."

**(b) The six named classes, [x-03] p. 28, verbatim:**

> "Example. 1) E_tors : (Tors) holds  2) E_max : (Tors) and (Image) hold  3) E_f : (Tors) and ker χ is finite. Equivalently: | ker χ| ∈ N₀  4) E_fg : (Tors) and ker χ is finitely generated  5) E_fd : (Tors) and ker χ ⊗ Q is finite dimensional  6) E_fd0 : (Tors) and (ker χ |_{κ(x₀)×}) ⊗ Q is finite dimensional where x₀ = π(x) under the projection π : X → X₀."
> "We have inclusions in the appropriate sense E_f ⊂ E_fg ⊂ E_fd ⊂ E_fd0 ⊂ E_max ⊂ E_tors."

**(c) N₀ is not free to be small.** [x-03] p. 24, verbatim: "Let N₀ be the submonoid of N generated by a set of prime numbers char N₀ … **We always assume that char N₀ ⊃ char X₀**, the set of positive residue characteristics of the points of X₀. The main cases of interest are char N₀ = char X₀ and N₀ = N." For X₀ = Spec Z, char X₀ is the set of *all* primes, so **char N₀ = all primes and N₀ = N is forced**. (This is a stronger anchor than the note uses; see F8.)

**(d) The character parametrization, [x-03] (34)–(35), p. 32, verbatim:**

> "N x₀^Ẑ = Gal(κ(x)/κ(x₀)) ֒→ Aut(κ(x)×) = Ẑ×_(p)."  (34)
> "The monoid Ẑ×_(p) × N₀ acts by pre-composition on the set S of homomorphisms P̄× : κ(x)× → C× with finite cyclic kernel of order in N₀. We have a Ẑ×_(p) × N₀-equivariant surjection: Ẑ×_(p) × N₀ ↠ S , (a, ν) ↦ χ_x · (a, ν) := χ_x ◦ ( )^a ◦ ( )^ν."  (35)
> "Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp^n and a = p^n a′ for some n ∈ Z."

and, same page, "Given x and composing the fixed injection ι : µ(K) ֒→ µ(C) above with (32) we obtain the injective character χ_x = ι ◦ i_x^{−1} : κ(x)× ֒→ C×". Also p. 32: the fibre pr₀^{−1}(x₀) "consists of the G-orbits of all pairs (x, P̄×) … and P̄× : κ(x)× → C× satisfies (Tors). Since κ(x)× is torsion this means that ker P̄× = (ker P̄×)_tors is finite hence cyclic and |ker P̄×| ∈ N₀." So the set S of (35) **is** exactly the set of (Tors)-characters at x. The note's §4 statement of the coordinates is therefore correct as written.

**(e) The fibration — the anchor Proposition 1 consumes. [x-03] p. 33.** `pdftotext` renders the display as "Ẑ×(p)/p^Ẑ = Aut(Fp)/Aut(Fp)". On the vision render of PDF page 33 the display reads, verbatim:

> "The set C_{x₀} fibres over the compact group
>   Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) ,
> and the fibres are the Q₀^{>0}-orbits in C_{x₀}. … The maps (37), (38) and the fibration map depend on our choices of x and ι."

Also verified on the same render: (39), and (38) on p. 32 —

> "(Ẑ×_(p)/N x₀^Ẑ) ×_{p^Z} Q₀^{>0} ⥲ C_{x₀}"  (38)

with the following sentence, p. 32–33: "It follows that all points P₀ ∈ C_{x₀} have isotropy subgroup (Q₀^{>0})_{P₀} = N x₀^Z."

**Two independent stronger anchors for the same fact, which the note does not use.** [x-03] p. 2, verbatim: "If p = char κ(x₀), then Γ_{x₀} is fibred over the compact group Aut(F̄_p^×)/Aut(F̄_p) = Ẑ×_(p)/p^Ẑ, **with fibres the periodic orbits in Γ_{x₀}. Each periodic orbit of X₀ lies in exactly one packet Γ_{x₀}.**" And [x-06] Thm 4.2, p. 12, verbatim: "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}."

These two say directly what Proposition 1 needs — *distinct base classes ⟹ distinct **periodic orbits of the flow*** — whereas the note's cited p. 33 line says it for **Q^{>0}-orbits in C_{x₀}**, one suspension step earlier. The gap is one line (suspension orbits ↔ Q^{>0}-orbits, [x-03] Thm 6.1 p. 39), so this is not a defect, but the note should cite the direct anchors. Recorded under F14 (cosmetic, folded into MINOR bookkeeping).

**(f) For X₀ = Spec Z the packet is a product.** N x₀ = p, so N x₀^Ẑ = p^Ẑ and (38) reads C_p ≅ B_p ×_{p^Z} Q₀^{>0}. The p^Z-action on the first factor is multiplication by p^{−n}, which is trivial on B_p = Ẑ×_(p)/p^Ẑ. Hence **C_p ≅ B_p × (Q₀^{>0}/p^Z) as a Q^{>0}-set**, the fibration is the first projection, and its fibres are exactly the Q^{>0}-orbits — the "fibres are the orbits" sentence, re-derived. Consequently the base-class map
  β : {Q^{>0}-orbits in C_p} ⥲ B_p
is a bijection, for each fixed choice of (x, ι). **This is the only form of the (38) consumption Proposition 1 needs, and it is correct.**

**(g) Theorem 5.2, p. 34, verbatim:** "For any point P₀ ∈ C^E_{x₀} the isotropy group of P₀ is (Q₀^{>0})_{P₀} = N x₀^Z where N x₀ = |κ(x₀)|. **If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}.**"

**(h) Theorem 6.1, p. 39, verbatim:** "The theorem asserts that the points x₀ of X₀ with finite residue field correspond bijectively to the 'packets' Γ^E_{x₀} of periodic orbits of length log N x₀ in the R-dynamical system X₀. **Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀** of X₀ with finite residue field."

**(i) The coefficient field carries a valuation.** [x-03] §7, p. 40, verbatim: "**In this section, C is an algebraically closed field with a valuation | | and the corresponding topology.** We begin with the affine case X₀ = spec R₀ … we give X̊(C) the topology of pointwise convergence. It is the subspace topology induced by the Tychonov topology of C^R … Since R is countable, X̊(C) is a metrizable topological space." *This is the anchor behind finding F3.*

---

## 3. LEMMA A — verdict **PASS-WITH-REPAIRS** (one MAJOR: hypotheses under-stated)

### 3.1 What the local condition actually is (verified, because Lemma A must match it)

[x-03] §14 opening, p. 89, verbatim: "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p. … **In the following we only consider the monoid N₀ generated by p i.e. the F_p = ( )^p action.**"

[x-03] Def. 14.5, p. 94, verbatim:
> "Y̌_α = {(x, y, P̌_y) ∈ X̌_c(o) | |f(P̌_y)| ≤ α for all f ∈ I_y} = {(x, y, P̌_y) ∈ X̌_c(o) | |P̌_y(r + s) − P̌_y(r) − P̌_y(s)| ≤ α for r, s ∈ Ô^♭_{{x},y}}. … For α = 1/p we are looking at multiplicative maps P̌_y which mod p are also additive. Set Y̌ = Y̌_{1/p}."

Def. 14.12 = (183), p. 99, is the same with P̂_y on the completed space; Props. 14.7 (p. 94) and 14.13 (p. 100) are verbatim as the note's (F2) reports, and the ultrametric self-improvement computation on p. 95 is exactly "≤ max(α^{p^ν}, 1/p)". So the normalization is |p| = 1/p and "defect ≤ |p|" is the fixed point of the local principle. **Lemma A's bound is the right bound.**

Crucially, the defect is tested on the **tilt** Ô^♭_{{x},y}. At the closed point the tilt is the residue field itself: [x-03] p. 113, verbatim, "The corresponding local rings O_{{x},η} are o_K resp. κ = o_K/m_K with p-adic completions Ô_{{x},η} given by ô_K resp. κ … and tilts Ô^♭_{{x},y} equal to ô^♭_K and lim_{( )^p} κ ⥲ κ." So at the closed point the condition is literally on r, s ∈ κ, and κ = o_K/m_K = **F̄_p** (K an algebraic closure of a p-adic field). **Lemma A's setting matches Deninger's closed-point fibre exactly — with κ = F̄_p.**

### 3.2 Re-derivation of Lemma A, in full, my own

Standing hypotheses I will use (see F1 for why they are not the note's): o a p-adically complete rank-1 valuation ring, fraction field C of characteristic 0, maximal ideal m, residue field k = o/m of characteristic p, **k perfect** and **F̄_p ⊆ k**. Absolute value normalized by |p| = 1/p. κ an algebraically closed field of characteristic p. P : κ → o with P(0) = 0, P(1) = 1, P|_{κ^×} : κ^× → o a monoid map.

**Step 0 (values are units).** P(r)P(r^{−1}) = P(1) = 1, so P(κ^×) ⊆ o^×.

**Step 1 ({|x| ≤ |p|} = po).** For x ∈ o: |x| ≤ |p| ⟺ |x/p| ≤ 1 ⟺ x/p ∈ o (o is a valuation ring with fraction field C, p ≠ 0) ⟺ x ∈ po. And po ⊆ m since |p| < 1. **So the defect bound "≤ |p|" says exactly: defect ∈ po ⊆ m.**

**Step 2 (⇒: reduction is a field embedding).** Suppose |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ. Reduce mod m and write τ := (P mod m) : κ → k. By Step 1, τ(r+s) = τ(r) + τ(s); τ is multiplicative because P is; τ(1) = 1, τ(0) = 0. So τ is a ring homomorphism from a field with τ(1) ≠ 0, hence **injective**: τ : κ ↪ k. (This forces F̄_p ⊆ k, since κ ⊇ F̄_p.) τ is uniquely determined by P.

**Step 3 (⇒: P is the multiplicative lift of τ).** P|_{κ^×} is a multiplicative lift of τ|_{κ^×} along o^× ↠ k^×. Two sub-cases.
 *(3a) κ = F̄_p (the case the note actually uses).* Then κ^× is torsion of prime-to-p exponent, so P(κ^×) ⊆ μ^{(p)}(o). Reduction is injective on μ^{(p)}(o): if ζ ∈ μ_d(o), d prime to p, and ζ ≡ 1 mod m, write ζ = 1 + x with x ∈ m; then 0 = ζ^d − 1 = x·(ζ^{d−1} + … + 1) and ζ^{d−1} + … + 1 ≡ d mod m with |d| = 1 (d prime to p, residue char p), so the second factor is a unit and x = 0. Reduction is also surjective onto μ^{(p)}(k): roots of unity of C have absolute value 1, hence lie in o, so μ^{(p)}(o) = μ^{(p)}(C) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ; likewise μ^{(p)}(k) ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ because F̄_p ⊆ k and x^{ℓ^n} − 1 is separable in char p; an injective homomorphism between two copies of ⊕_{ℓ≠p} Q_ℓ/Z_ℓ has, on each ℓ-primary part, a divisible nonzero image, and the only such subgroup of Q_ℓ/Z_ℓ is Q_ℓ/Z_ℓ itself. So reduction is an isomorphism μ^{(p)}(o) ⥲ μ^{(p)}(k); call its inverse [·]. Now P(r) and [τ(r)] are both in μ^{(p)}(o) with the same reduction, hence equal. Together with P(0) = 0 = [τ(0)], **P = [·] ∘ τ**.
 *(3b) general κ (needed for the statement as the note writes it).* Now κ^× need not be torsion, so 3a is unavailable. Use instead the uniqueness of multiplicative sections. For x, y ∈ o with |x − y| = δ < 1 one has x^p − y^p = Σ_{i=1}^{p} C(p,i) y^{p−i}(x−y)^i, hence |x^p − y^p| ≤ max(δ^p, |p|δ); iterating, |x^{p^n} − y^{p^n}| ≤ max_{0≤j≤n} |p|^j δ^{p^{n−j}} → 0. Hence for a ∈ k the limit [a] := lim_n ã_n^{p^n} (ã_n ∈ o any lift of a^{p^{−n}}, which exists since k is perfect) is well defined, is multiplicative, and lifts a; and **any** multiplicative section s of o ↠ k satisfies s(a) = s(a^{p^{−n}})^{p^n} = [a] by the same estimate. Apply this to the subfield τ(κ) ⊆ k, which is perfect (κ is), and to the multiplicative section P ∘ τ^{−1} of o ↠ τ(κ): it must equal [·]|_{τ(κ)}. Hence **P = [·] ∘ τ** again.

**Step 4 (⇐: the converse — the note's flagged press point).** Let τ : κ ↪ k be any field embedding and P = [·] ∘ τ. Multiplicativity is clear. For the defect, fix a = τ(r), b = τ(s) ∈ k and let n ≥ 1. Put A = [a^{p^{−n}}], B = [b^{p^{−n}}], C = [(a+b)^{p^{−n}}] = [a^{p^{−n}} + b^{p^{−n}}] (char p). All three reduce to their arguments, so ε := A + B − C ∈ m. Then
  [a] + [b] − [a+b] = A^{p^n} + B^{p^n} − (A+B−ε)^{p^n}
  = (A^{p^n} + B^{p^n} − (A+B)^{p^n}) + ((A+B)^{p^n} − (A+B−ε)^{p^n}).
The first bracket lies in p·o because every binomial coefficient C(p^n, i), 0 < i < p^n, is divisible by p. The second is bounded by max_{0≤j≤n} |p|^j |ε|^{p^{n−j}} by the estimate of Step 3b, which is ≤ |p| once n is large (each term is ≤ |p| for j ≥ 1, and |ε|^{p^n} → 0). Hence **|[a] + [b] − [a+b]| ≤ |p|**, i.e. the defect of [·] ∘ τ is ≤ |p|. ∎

**Step 5 (uniqueness).** τ = P mod m is determined by P; conversely [·] ∘ τ determines τ. So the correspondence is a bijection {mod-p-additive multiplicative P} ⥲ {field embeddings κ ↪ k}.

**Both directions therefore hold. Lemma A is TRUE.** Note a bonus the note does not state and should: by Step 2 the embedding τ is injective, so **mod-p additivity forces P|_{κ^×} to be injective** — a fact used implicitly in §4 Consequence 1 and in §4 Consequence 2.

### 3.3 The note's own converse argument, audited

The note gives: "[a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring)". Audited step by step:
* "first component agrees": the 0-th Witt component of a difference is the difference of 0-th components (w₀ = x₀), and [a]+[b] has 0-th component a+b while [a+b] = (a+b, 0, 0, …). ✓ So the difference lies in ker(W(k) → k) = V W(k). ✓
* "V F = p on Witt vectors of a perfect ring": p·x = V(F(x)) holds on W(A) for every F_p-algebra A; F is bijective when A is perfect, so V W(k) = V F W(k) = p W(k). ✓
* "**W(k) ⊆ o**": this is the one step that is *asserted*, not argued, and it is the least obvious. It is true here — the ring map W(k) → o lifting id_k exists (W(k) is the initial p-complete p-torsion-free lift of the perfect ring k; concretely (a_n)_n ↦ Σ p^n [a_n^{p^{−n}}], convergent since o is p-adically complete), Teichmüller lifts go to Teichmüller lifts (both are *the* multiplicative section, Step 3b), and the map is injective because W(k) is a DVR, its only primes are 0 and (p), and p ↦ p ≠ 0 in the characteristic-0 domain o. But this is three non-trivial facts hidden in a parenthesis.

**Recommendation (not a defect, a strengthening):** replace the Witt-vector converse by the elementary Step 4 above, which uses only the ultrametric inequality, the divisibility of C(p^n, i), and perfectness of k — no Witt ring, no embedding W(k) ⊆ o, no universal property. Replacement text in §11.

### 3.4 FINDING F1 (MAJOR) — Lemma A's stated hypotheses do not support its stated proof

**Location:** §4, Lemma A, statement and derivation.

**The defect.** Lemma A is stated for "κ an algebraically closed field of characteristic p", and its statement carries the parenthetical "(values automatically in μ^{(p)}(o), the prime-to-p roots of unity, **since κ^× is prime-to-p torsion**)". That parenthetical is **false for every algebraically closed field of characteristic p other than F̄_p**: if κ has positive transcendence degree over F_p, κ^× is not torsion. Concretely, κ = the algebraic closure of F_p(t) has t ∈ κ^× of infinite order, and P(t) is then an arbitrary unit of o, not a root of unity. Since the (⇒) half of the note's derivation ends with "P(r) and [τ(r)] are prime-to-p roots of unity with the same reduction, hence equal", **the derivation does not establish the lemma in the generality in which it is stated**. Moreover with κ ≠ F̄_p the symbol "[·] ∘ τ" is not even defined by the note's own [·], which the note introduces only as "the Teichmüller section of the reduction μ^{(p)}(o) ≅ μ^{(p)}(k)": τ(κ) is not contained in μ(k) ∪ {0}. Two further hypotheses are missing: the isomorphism μ^{(p)}(o) ≅ μ^{(p)}(k) requires **F̄_p ⊆ k**, and the converse requires **k perfect** (the note's own "V F = p on Witt vectors of a perfect ring" silently uses it); neither is in the note's §2 standing hypotheses on o, which say only "residue field k of characteristic p".

**Break attempt (failed — the statement itself is true).** I looked for a multiplicative P : κ → o, κ algebraically closed of char p with κ^× non-torsion, with defect ≤ |p| but P ≠ [·] ∘ τ. None exists: Step 3b shows any such P is the unique multiplicative section composed with τ. So there is **no counterexample**; the finding is a proof/hypothesis gap, not a false claim.

**Fill (two, either suffices).** (i) *Narrow*: add "κ = F̄_p" (equivalently "κ^× torsion"). This costs nothing — the only use in the note is at packet points, where κ(x) ≅ F̄_p ([x-03] p. 31, "For every point x ∈ X over x₀ the residue field κ(x) is an algebraic closure of κ(x₀)"), and in the consistency check with Thm 15.6, where κ = o_K/m_K = F̄_p ([x-03] p. 113). (ii) *General*: keep arbitrary κ and replace Step 3's endgame by the uniqueness of multiplicative sections (Step 3b above), with [·] the p-adic Teichmüller section of o ↠ k. Exact replacement text in §11, F1.

**Severity MAJOR** (fillable, but the note must change: the statement as printed is not established, and one parenthetical in it is false).

### 3.5 The consistency check against Theorem 15.6 — verified, with one elision

The note writes: "this matches Theorem 15.6's closed-point fiber Y⋄_s = Hom(κ, k) (p. 114) … and Hom(κ₀, k) is a single F_p-orbit of size r = deg(κ₀/F_p), which suspends to one closed orbit of length r·log p = log N(π₀) — Thm 15.6(6)."

Verified verbatim, [x-03] p. 113–114: "**Y⋄_s := pr_X^{−1}(s) = Hom(κ, k)**"; (224) "**Y⋄_{0 s₀} := pr_{X₀}^{−1}(s₀) ⥲ ∐_{τ₀} {0}/o×_{K₀} = Hom(κ₀, k)**"; and 15.6(6), verbatim: "**The only periodic (i.e. finite) orbit of the F_p-action on Y⋄₀ is Y⋄_{0 s₀}. It has order log_p N(π₀) = r if q = p^r.**" Also p. 113, verbatim: "For (x, y) = (s, s) the continuous local ring homomorphisms P̂^♭_y : κ → o^♭ with P̂^♭_y(f) ≠ 0 for all 0 ≠ f ∈ lim_{( )^p} κ ≅ κ **are simply the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭**." So the note's reading is right: over the closed point the mod-p-additive points are precisely the field embeddings — exactly Lemma A.

**F13 (MINOR).** The note's sentence runs Y⋄_s = Hom(κ, k) and Hom(κ₀, k) together without naming the intervening G-quotient. Hom(κ, k) with κ = F̄_p is infinite; it is its quotient Y⋄_{0 s₀} = Y⋄_s/G ≅ Hom(κ₀, k) ((224), p. 114) that has r elements and is the single periodic F_p-orbit. One clause fixes it (§11, F13).

### 3.6 Consequence 1 (why the local principle succeeds) — re-derived, CORRECT

Fix κ = F̄_p and o with k = F̄_p. The injective characters κ^× → μ^{(p)}(o) form a torsor under Aut_group(κ^×) = Ẑ×_(p) (fix χ₀; every other is χ₀ ∘ ( )^a). By Lemma A the mod-p-additive multiplicative maps are exactly {[·] ∘ τ : τ ∈ Hom_ring(κ, k)} = {[·] ∘ τ : τ ∈ Aut(F̄_p)}, a torsor under Aut_ring(κ) = Ẑ, whose image in Aut_group(κ^×) is p^Ẑ by (34). Hence

  mod-p additivity cuts a Ẑ×_(p)-torsor down to a p^Ẑ-torsor, and the residual ambiguity is **exactly** Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p) = B_p.

That is the displayed identity of [x-03] p. 33 and p. 2. Consequence 1 is **correct**, and it is the sharpest sentence in the note. (The identity itself is Deninger's, as the note's own dated NOVELTY block already records; only the use is the note's.)

---

## 4. §4 Consequence 2 / D3 (the transport reading) — verdict **PASS-WITH-REPAIRS** (one MAJOR)

### 4.1 Re-derivation

Fix a prime p, a point x over (p), and ι, hence χ_x and the coordinates (35). To impose the *local* condition on a *global* (C-valued) character one must move the values into a coefficient ring with residue characteristic p. Choose an isomorphism j : μ^{(p)}(C) ⥲ μ^{(p)}(C_p); the set of such j is a torsor under Aut(μ^{(p)}(C_p)) = Ẑ×_(p) (both groups are ≅ ⊕_{ℓ≠p} Q_ℓ/Z_ℓ, and an injective endomorphism of Q_ℓ/Z_ℓ is multiplication by a unit of Z_ℓ). Define

  T_j := { χ : κ(x)^× → C^× | j ∘ χ̄ has additivity defect ≤ |p| in o_{C_p} }.

*Which characters are in T_j?* Write χ = χ_x ∘ ( )^c, c ∈ Ẑ_(p) (every character of F̄_p^× has this form, uniquely: Hom(⊕_{ℓ≠p}Q_ℓ/Z_ℓ, C^×) = ∏_{ℓ≠p} End(Q_ℓ/Z_ℓ) = Ẑ_(p)). By Lemma A, j ∘ χ is mod-p additive iff it equals [·] ∘ τ for a field embedding τ : F̄_p ↪ F̄_p, i.e. τ ∈ Aut(F̄_p) = Ẑ acting on F̄_p^× through p^Ẑ ⊂ Ẑ×_(p). Since [·] ∘ τ is injective, this forces c ∈ Ẑ×_(p), and then it pins c to a single coset: **{c : χ_x^c ∈ T_j} = a_j · p^Ẑ for a single class [a_j] ∈ B_p determined by j**. As j runs over its Ẑ×_(p)-torsor, [a_j] runs over all of B_p. So:

**(D3, correct form.)** For each choice of j, T_j is nonempty and meets the packet Γ_p in exactly one periodic orbit, of base class [a_j]; and every base class arises from some j. The choice content is exactly one arbitrary point of the Cantor group B_p per prime — precisely the choice content of probe A's Theorem C(b) cut.

*Is T_j admissible?* **No.** T_j is closed under χ ↦ χ ∘ σ for σ ∈ Aut(F̄_p) (because [·] ∘ τ ∘ σ = [·] ∘ (τσ) and τσ ∈ Hom(F̄_p, F̄_p)). But it is **not** closed under ν-powers for p ∤ ν: with P = [·] ∘ τ and a = τ(r), b = τ(s),
  (F_ν P)(r+s) − (F_ν P)(r) − (F_ν P)(s) ≡ (a+b)^ν − a^ν − b^ν  (mod m),
and (a+b)^ν − a^ν − b^ν is a nonzero polynomial over F_p whenever p ∤ ν (its coefficient of a b^{ν−1} is C(ν,1) = ν ≢ 0), so it takes nonzero values on the infinite field F̄_p; the defect then has absolute value 1 > |p|. Hence T_j fails Def. 4.1's ν-condition. (For ν = p^k m with p ∤ m and m > 1 the same holds, since (a+b)^ν − a^ν − b^ν = ((a+b)^m − a^m − b^m)^{p^k}.) **Conclusion: F_ν(T_j) ⊆ T_j iff ν ∈ p^{N₀}.**

### 4.2 FINDING F2 (MAJOR) — the transported class is asserted to *be* E(a₀), and simultaneously to be non-N-invariant; these cannot both hold

**Location:** §0 bullet (D3) ("the resulting class is precisely probe A's Theorem C cut E(a₀)"), and §4 Consequence 2 ("the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: … it is not admissible-with-theory (forfeits every certified theorem), **and it is not N-invariant**").

**The defect.** Probe A's E(χ^{a₀}) is by construction the **minimal admissible class** containing the injective character χ^{a₀} (`probe-9.3-a.md` §4.1, Theorem C(b): "the minimal admissible class E(χ^{a₀}) … **is admissible in the sense of Def. 4.1**"; the adjudication §4 item 5b calls these "one-orbit-per-prime **admissible** cuts"). Admissible means, by Def. 4.1 read verbatim above, biconditionally closed under all ν ∈ N₀ — i.e. **N₀-invariant**. So E(a₀) *is* N-invariant, and a class that "is not N-invariant" cannot *be* E(a₀). The note asserts both in one sentence. Independently, the computation in §4.1 above shows the transported class T_j is genuinely not admissible, so the false half of the sentence is the identification, not the non-invariance.

Note also that the note's own §3 makes the identification impossible: §3 requirement 4 argues at length that a mod-p-type selection and Def. 4.1's ν-closure "cannot coexist". §4's identification contradicts §3.

**Fill.** The conclusion of D3 is unaffected and can be stated correctly: T_j ⊊ E(a_{j}), T_j's char-p members are exactly the injective members of E(a_{j}), the two select the same single base class per prime, and E(a_{j}) is the smallest admissible class containing T_j. (That T_j ⊆ E(a_j) is immediate from the reachability computation of `probe-9.3-a.md` §4.1, which I checked: the injective members of E(a₀) have exponent in a₀·p^Ẑ, which is exactly T_j's exponent set.) Replacement text in §11, F2.

**Break attempt.** Could T_j accidentally be admissible for some special j? No: the obstruction computed above is uniform in j (it depends only on ν and p). Could E(a₀) fail to be admissible, rescuing the identification the other way? No: it is admissible by construction as a minimal admissible class.

**Severity MAJOR** (the note's stated identity is false; the surviving statement is weaker but carries the same verdict).

---

## 5. LEMMA B — verdict **PASS** (verified; I also strengthen it)

### 5.1 Re-derivation

Let X₀ = Spec Z, X its normalization in Q̄ (so Γ(X, O) = the ring of algebraic integers), x a point of X over (p), and P̄× : κ(x)^× → C^× any character, P̄ its extension by zero to κ(x). The global analogue of the local evaluation is the multiplicative map ZΓ(X, O) → C, [α] ↦ P̄(α(x)) ([x-06] p. 10, verbatim: "for f ∈ Γ(X, O_X) consider its images [f] in W_rat(O_X(X)) … we obtain a multiplicative map from Γ(X, O_X) into the C-algebra of C-valued function on W_rat(X)(C)"), so the additivity defect on the generator [r+s] − [r] − [s] of the ideal I is P̄(r̄+s̄) − P̄(r̄) − P̄(s̄) with r̄, s̄ ∈ κ(x). Take r = s = 1 ∈ Γ(X, O). Then

  defect = P̄(2̄) − 2·P̄(1̄) = P̄(2̄) − 2.

*Case p = 2.* 2̄ = 0 in κ(x), so P̄(2̄) = 0 and |defect| = 2.
*Case p odd.* κ(x) ≅ F̄_p, so κ(x)^× is torsion; hence P̄(2̄) ∈ μ(C) and |P̄(2̄)| = 1. Writing P̄(2̄) = e^{iθ}, |e^{iθ} − 2|² = 5 − 4cos θ ≥ 1, with equality iff P̄(2̄) = 1.

**So |P̄(2̄) − 2| ≥ 1 at every point of every packet, with 1 ≤ |defect| ≤ 3.** Consequently the locus "archimedean additivity defect ≤ ε" is **empty on the periodic locus for every ε < 1**. ∎

The second half of the note's Lemma B is also correct: the local completion mechanism (172), p. 94 verbatim — "Choose an element ω_α ∈ o with α ≤ |ω_α| < 1. Then (x, y, P̌_y) ∈ Y̌_α gives a ring homomorphism P̌_y : ZÔ^♭ → o with P̌_y(I_y) ⊂ ω_α o and hence an induced ring homomorphism W_p(P̌_y) : W_p(Ô^♭) = lim ZÔ^♭/I_y^n → lim o/ω_α^n = o" — requires the defect ideal to be *topologically nilpotent*. With |defect| ≥ 1 the I-adic filtration does not converge and there is no A_inf-analogue action. ✓

### 5.2 Is "the periodic locus" the right locus? — YES, and I verified it

[x-06] Thm 4.2, p. 11–12, verbatim: "{x₀ ∈ X₀^E | φ^t(x₀) = x₀ for some t > 0} = ∐_{x₀} Γ_{x₀}. Here x₀ runs over the closed points of X₀". Every periodic point therefore lies over a closed point, whose residue field has characteristic p > 0, which is exactly where the computation applies. And by [x-03] Thm 6.1 (p. 39) "Any periodic orbit γ in X₀ is contained in Γ^E_{x₀} for a uniquely determined point x₀". So: **an archimedean-threshold class contains no character at a char-p point, hence its system has no periodic orbits at all.** That is the right locus, and the strongest possible failure — not "too many orbits" but "none". The locus complement (char-0 points, κ(η) = Q̄) is untouched and untouchable by this test, correctly, since there κ(η)^× is not torsion and P(2) may be any nonzero complex number; the note does not claim otherwise.

### 5.3 Two robustness checks the note does not make (both confirm it)

*(a) Scale-normalized thresholds fail too.* At a char-p point all nonzero values of P̄ lie on the unit circle, so max(|P̄(r̄)|, |P̄(s̄)|) ∈ {0, 1} and |P̄(r̄)P̄(s̄)| ∈ {0, 1}. The relative conditions |defect| ≤ ε·max(|P̄(r̄)|,|P̄(s̄)|) and |defect| ≤ ε·|P̄(r̄)P̄(s̄)| therefore also fail at r = s = 1 for every ε < 1. The failure is not an artifact of the normalization choice.
*(b) The threshold cannot merely be raised.* Since |defect| ≤ 3 everywhere on a packet, a threshold ε ≥ 3 is vacuous (selects everything) and any ε ∈ [1, 3) is a genuine but *non-nilpotent* condition, which by (172) cannot produce the A_inf-action that is the whole purpose of Stage 3 ([x-03] intro p. 6, verbatim: "we asked ourself if there was a canonical F_p-subsystem Y⋄ of X⋄_c(o) on which not only the elements of ZΓ(X, O)^{∧♭} but even the elements of A_inf(X) could be viewed as o-valued functions. The answer is simple, Y⋄ consists of all the diagrams in X⋄_c(o) whose maps are not only multiplicative but mod p also additive"). So there is no threshold at all that both selects and extends.

### 5.4 FINDING F12 (MINOR) — unused hypothesis, and two unstated sharpenings

**Location:** §6, Lemma B statement. The hypothesis "any character P in any class E ⊆ E_tors" is not used anywhere in the computation, which needs only that κ(x) has characteristic p and that P is multiplicative with P(1) = 1 extended by zero. Stating it invites the misreading that the emptiness is a property of the admissible classes rather than of the archimedean coefficient field. The note should also record the two-sided bound 1 ≤ |P(2̄) − 2| ≤ 3 (which is what closes off "just raise ε") and the scale-normalized robustness check. Replacement text in §11, F12.

**F12b (MINOR, on Lemma A).** Symmetrically, Lemma A's statement should record the corollary "mod-p additivity ⟹ P|_{κ^×} injective", since §4 Consequence 1 and §4 Consequence 2 both use it.
