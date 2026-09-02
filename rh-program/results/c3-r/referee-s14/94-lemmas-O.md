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

**Overall: PASS-WITH-REPAIRS. 0 FATAL, 4 MAJOR, 9 MINOR.** (Finite steps additionally machine-checked: `94-lemmas-O-checks.py` / `.json`, ALL_PASS = true; see §12b.)

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

---

## 6. LEMMA C — verdict **PASS**

**Statement under review:** "The restriction map Aut(C) → Aut(μ(C)) = Ẑ× is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree)."

### 6.1 Re-derivation, step by step, with the use of choice audited

Let C be **any** algebraically closed field of characteristic 0 (this is all that is needed; see F10).

**Step 1 (the target).** μ(C) is the torsion subgroup of C^×. In characteristic 0, for every n the polynomial X^n − 1 is separable and splits, so μ_n(C) is cyclic of order n and μ(C) = ∪_n μ_n(C) ≅ Q/Z. Hence End(μ(C)) = End(Q/Z) = Ẑ and **Aut(μ(C)) = Ẑ×**. Every σ ∈ Aut(C) maps μ(C) to μ(C) (it preserves orders), so the restriction map Aut(C) → Aut(μ(C)) = Ẑ× is well defined; concretely σ acts as ζ ↦ ζ^{u_σ} for a unique u_σ ∈ Ẑ×.

**Step 2 (cyclotomic surjectivity).** Q(μ_∞) ⊆ C is the subfield generated by all roots of unity, and Q(μ_∞)/Q is Galois with the cyclotomic character an isomorphism Gal(Q(μ_∞)/Q) ⥲ Ẑ×, σ ↦ u with σ(ζ) = ζ^u for all ζ ∈ μ(C). So every u ∈ Ẑ× is realized by an automorphism σ₁ of Q(μ_∞).

**Step 3 (to Q̄).** Q̄ ⊆ C is an algebraic closure of Q(μ_∞). By the isomorphism-extension theorem, σ₁ extends to an automorphism σ₂ of Q̄. (Uses Zorn's lemma.)

**Step 4 (across a transcendence basis).** Let B be a transcendence basis of C over Q̄. (Uses Zorn.) B is algebraically independent over Q̄, so Q̄[B] is a polynomial ring and σ₂ ⊗ id_B is a ring automorphism of Q̄[B], extending to an automorphism σ₃ of its fraction field Q̄(B) fixing B pointwise.

**Step 5 (to C).** C is algebraic over Q̄(B) (B is a transcendence basis) and algebraically closed, hence C is an algebraic closure of Q̄(B). By isomorphism extension again, σ₃ extends to σ ∈ Aut(C). (Uses Zorn.)

Then σ|_{μ(C)} = σ₁|_{μ(C)} = ( )^u. **Surjectivity proved.** ∎

**Choice audit.** Three appeals to Zorn (existence of the transcendence basis; two isomorphism extensions). This is unavoidable: for C = ℂ, the subgroup of Aut(ℂ) obtainable without choice is trivial in the relevant sense — the only automorphisms of ℂ that are Lebesgue-measurable/Baire-measurable are id and conjugation, whose images in Ẑ× are 1 and −1. So Lemma C is a genuinely non-constructive statement, and the σ's Proposition 1 produces are wild. **This does not weaken Proposition 1**, because Proposition 1 quantifies over selections and only needs the *existence* of such σ. But it is worth recording that the note's no-go is a ZFC statement whose witnesses are non-measurable.

**Interface step the note omits.** Proposition 1 needs u_σ ∈ Ẑ×_(p) = Aut(μ^{(p)}(C)), while Lemma C produces elements of Ẑ× = Aut(μ(C)). The link is the projection Ẑ× = ∏_ℓ Z_ℓ^× ↠ ∏_{ℓ≠p} Z_ℓ^× = Ẑ×_(p), which is surjective, so every u ∈ Ẑ×_(p) lifts. One clause; recorded under F11.

### 6.2 FINDING F10 (MINOR) — over-strong hypotheses, and a garbled clause

**Location:** §5, Lemma C statement and derivation.
(a) The parenthetical "(or any algebraically closed field of characteristic 0 **containing Q̄ with infinite transcendence degree**)" is strictly stronger than needed on both counts: every algebraically closed field of characteristic 0 contains Q̄ automatically, and transcendence degree 0 (C = Q̄) is fine — Steps 4–5 are then vacuous. As printed, the lemma appears not to cover C = Q̄, which [x-03]'s conditions before Cor. 4.4 (p. 27–28: "1) C× ≠ µ(C) i.e. C is not the algebraic closure of a finite field 2) card K₀ ≤ card C 3) char C = 0 or char K₀ = char C is positive") do permit for K₀ = Q.
(b) The derivation clause "then to C along a transcendence basis of C over Q̄ **and to the algebraic closure C of the lifted subfield**" transposes the two extensions and names C twice with two meanings. Replacement text in §11, F10.

---

## 7. LEMMA D — verdict **PASS** (all three parts; the flagged press point on E_max's (Image) checks out cleanly)

Throughout, σ ∈ Aut(C) acts by post-composition, σ·(x, P̄×) := (x, σ ∘ P̄×).

### 7.1 Part (i): commutation — re-derived, CORRECT

*Well-definedness.* σ ∘ P̄× : κ(x)^× → C^× is again a homomorphism, and σ acts bijectively (inverse σ^{−1}).
*With G.* [x-06] Thm 4.1, p. 11, verbatim: "σ ∈ G acts on X̊(C) via (x, P̄×)^σ = (x^σ, P̄× ◦ σ) and ν ∈ N acts G-equivariantly via F_ν(x, P̄×) = (x, P̄× ◦ ( )^ν)." The Galois action is pre-composition on the character and moves x; the Aut(C)-action is post-composition and fixes x. Both routes give (x^σ, τ ∘ P̄× ∘ σ). ✓ So the Aut(C)-action descends to X̊₀(C) = X̊(C)/G.
*With F_ν.* τ ∘ (P̄× ∘ ( )^ν) = (τ ∘ P̄×) ∘ ( )^ν. ✓ Hence it commutes with the transition maps of the colimit X̌(C) = colim_{N₀} X̊(C) ([x-03] p. 24), descends to X̌₀(C), and commutes with the induced Q₀^{>0}-action (generated by the F_ν and their inverses).
*With the flow.* On X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0} set τ[P, u] := [τP, u]. Well defined: [F_q P, q^{−1}u] ↦ [τ F_q P, q^{−1}u] = [F_q(τP), q^{−1}u] = [τP, u]. ✓ And φ^t[P,u] = [P, e^t u] ([x-06] p. 11, verbatim), so τ φ^t = φ^t τ and the R-coordinate is fixed. ✓

**Caveat that must be added (F7).** τ acts by **bijections, not homeomorphisms**. The topology on X̊(C) is pointwise convergence into C *with its valuation topology* ([x-03] §7, p. 40, quoted in §2(i) above); a wild σ ∈ Aut(ℂ) is discontinuous, hence σ ∘ (−) is not continuous for pointwise convergence. Proposition 1 does not need continuity — every step is set-theoretic — but the note nowhere says so, and a reader who assumes homeomorphisms will over-read the result. See F7.

### 7.2 Part (ii): class stability — re-derived class by class, CORRECT (including the flagged (Image) case)

The key elementary fact: for σ ∈ Aut(C), σ|_{C^×} is a group automorphism, so for any character χ : κ^× → C^×,
  **ker(σ ∘ χ) = ker(χ)**, and **σ|_{χ(κ^×)} : χ(κ^×) ⥲ (σ∘χ)(κ^×) is a group isomorphism.**
Everything follows. Class by class, against the verbatim definitions of §2(b):

| class | condition | why σ-stable |
|---|---|---|
| E_tors | (Tors): ker(χ\|_{μ(κ)}) finite, order in N₀ | ker unchanged; μ(κ) is in the source, untouched ✓ |
| **E_max** | (Tors) **and (Image)** | (Image) is a condition on the **image**: "if χ(κ^×) is torsion then κ^× is torsion". σ|: χ(κ^×) ⥲ (σχ)(κ^×) is a group isomorphism, so one image is torsion iff the other is, and κ^× is unchanged. Hence (Image) holds for χ iff for σ∘χ ✓ |
| E_f | ker χ finite | ker unchanged ✓ |
| E_fg | ker χ finitely generated | ker unchanged ✓ |
| E_fd | ker χ ⊗ Q finite dimensional | ker unchanged ✓ |
| E_fd0 | (ker χ\|_{κ(x₀)^×}) ⊗ Q finite dimensional | ker unchanged, and the restriction is taken in the source ✓ |

**The press point resolves affirmatively and easily.** (Image) is the only image-side condition among the six, and it is a *torsion* condition, hence invariant under any group automorphism of C^×; it does not see the ⊗Q-dimension of the image at all, so no dimension argument is needed. (The note's phrase "images map by σ, preserving torsion and ⊗Q-dimension" is correct but says more than (Image) requires; the ⊗Q clause is the *equivalent restatement* in Deninger's own text, "κ^× ⊗ Q ≠ 0 implies χ(κ^×) ⊗ Q ≠ 0", and σ preserves that too because σ| is an isomorphism onto the image.) Also verified: the stable/functorial variants on p. 29 ("(Stable Image)", and "the stable Galois invariant classes E are the functorial ones") are conditions on the source-side restriction and are equally σ-stable.

**Break attempt (failed).** I looked for a named class whose defining condition mentions the target field's structure beyond the group C^× — the only candidate is (Image), which is torsion-only. There is none. I also checked that σ-stability is compatible with Def. 4.1: the admissibility operations are pre-compositions (χ ∘ σ_κ, χ ∘ ( )^ν) and commute with post-composition, so σ carries admissible classes to admissible classes; combined with the table, each named class is carried to *itself*. ✓

### 7.3 Part (iii): the coordinate formula — re-derived, CORRECT

Let u_σ ∈ Ẑ×_(p) be the element with σ(ζ) = ζ^{u_σ} for all ζ ∈ μ^{(p)}(C) (well defined: μ^{(p)}(C) is characteristic in μ(C), and Aut(μ^{(p)}(C)) = Aut(⊕_{ℓ≠p} Q_ℓ/Z_ℓ) = ∏_{ℓ≠p} Z_ℓ^× = Ẑ×_(p) acting by power maps).

*Powers commute with homomorphisms, for profinite exponents.* Let f : A → B be a homomorphism of abelian torsion groups of prime-to-p exponent, u ∈ Ẑ_(p). For a ∈ A of order d, a^u means a^{u mod d}; since ord(f(a)) | d, u mod ord(f(a)) is determined by u mod d, so f(a^u) = f(a)^{u mod d} = f(a)^u. ✓ (This one-line check is implicit in the note's "power maps commute with any group homomorphism"; for Ẑ-exponents it is worth stating.)

*The formula.* χ_x has image in μ^{(p)}(C) (it is ι ∘ i_x^{−1} and κ(x)^× is prime-to-p torsion), so
  σ ∘ (χ_x ∘ ( )^a ∘ ( )^ν) = (σ|_{μ^{(p)}(C)} ∘ χ_x) ∘ ( )^a ∘ ( )^ν = (χ_x ∘ ( )^{u_σ}) ∘ ( )^a ∘ ( )^ν = χ_x ∘ ( )^{u_σ a} ∘ ( )^ν.
So in the coordinates (35), **σ : (a, ν) ↦ (u_σ a, ν)**. ✓ This is compatible with the fibre relation of (35) (a = p^n a′, ν′ = νp^n ⟹ u_σ a = p^n u_σ a′) and with the G-quotient (multiplication by u_σ is well defined on Ẑ×_(p)/N x₀^Ẑ since Ẑ×_(p) is commutative). Hence on B_p, **σ : [a] ↦ [u_σ a]**, a group translation. ✓ Since σ commutes with the Q^{>0}-action and preserves isotropy groups, it maps a periodic orbit of length log p to a periodic orbit of length log p, in the same packet (x is fixed). ✓

**F11 (MINOR).** The note justifies the formula by "because χ_x is an isomorphism onto μ^{(p)}(C) (injective character between groups ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, divisible-image argument as in Lemma A)". That surjectivity is **true** (I verified it: an injective endomorphism of Q_ℓ/Z_ℓ is multiplication by a unit, hence bijective) but **not needed** — the derivation above uses only that the image lies in μ^{(p)}(C). Conversely the note omits two steps that *are* needed: the order-divisibility check that makes Ẑ_(p)-powers commute with homomorphisms, and the projection Ẑ× ↠ Ẑ×_(p) linking Lemma C's output to u_σ. Replacement text in §11, F11.

---

## 8. PROPOSITION 1 — verdict **PASS**. The theorem is correct; I re-derived every input.

**Statement under review.** "Let E be any Aut(C)-stable class (all named example classes qualify) and let S ⊆ X₀^E be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B_p, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p …, and no Aut(C)-stable selection achieves one orbit per prime."

### 8.1 Re-derivation

Fix X₀ = Spec Z, a prime p, a point x of X over (p), and ι; this fixes χ_x, the coordinates (35), the bijection (38) and the base-class map β of §2(f).

1. **The periodic point lies in the packet with a base class.** By [x-03] Thm 6.1 (p. 39, quoted in §2(h)), the given periodic point of S lies on a periodic orbit γ contained in Γ_{x₀} for a unique closed point x₀; by hypothesis x₀ = (p). By §2(f), γ has a well-defined base class [a] := β(γ) ∈ B_p. ✓
2. **Realizing an arbitrary translation.** Given [c] ∈ B_p put u := c a^{−1} ∈ Ẑ×_(p) (B_p is a group and [a] is invertible). Lift u along the surjection Ẑ× ↠ Ẑ×_(p) to ũ ∈ Ẑ×, and apply **Lemma C** to obtain σ ∈ Aut(C) with σ|_{μ(C)} = ( )^{ũ}; then u_σ = u. ✓
3. **Transporting the orbit.** By **Lemma D(i)**, σ is a bijection of X₀^E commuting with the flow; by **Lemma D(ii)**, σ(X₀^E) = X₀^E; by hypothesis σ(S) = S. Hence σ(γ) ⊆ S is again a flow-orbit. Its period: σ commutes with the Q^{>0}-action, so the isotropy group is preserved; by [x-03] Thm 5.2 (p. 34, quoted in §2(g)) the isotropy is N x₀^Z = p^Z, so σ(γ) is periodic of the same length log p. ✓
4. **Its base class.** By **Lemma D(iii)**, β(σ(γ)) = [u_σ a] = [ua] = [c]. ✓
5. **Distinctness.** By §2(f) — the verbatim p. 33 sentence "the fibres are the Q₀^{>0}-orbits", or more directly [x-03] p. 2 and [x-06] Thm 4.2 p. 12 ("with fibres the compact orbits in Γ_{x₀}") — β is a bijection from orbits to base classes. Distinct base classes therefore lie on distinct orbits. ✓
6. **Count.** So S ⊇ {σ_c(γ) : [c] ∈ B_p}, a family of pairwise distinct periodic orbits of length log p indexed by B_p. ✓

**Uncountability of B_p, re-derived independently** (the note takes it from the adjudication; I did not):
* p^Ẑ is the image of the compact group Ẑ under the continuous homomorphism n ↦ p^n into Ẑ×_(p), hence compact, hence closed; so B_p = Ẑ×_(p)/p^Ẑ is a **profinite group**.
* For any finite set T of odd primes ℓ ∉ {p}, Ẑ×_(p) = ∏_{ℓ≠p} Z_ℓ^× ↠ ∏_{ℓ∈T} (Z/ℓ)^× ↠ ∏_{ℓ∈T} (Z/ℓ)^×/squares ≅ (Z/2)^{|T|}. The image of the single element p is one element g, so B_p surjects onto (Z/2)^{|T|}/⟨g⟩, of order ≥ 2^{|T|−1}. Since |T| is arbitrary, B_p has arbitrarily large finite quotients and is **infinite**.
* An infinite profinite group is uncountable: it is compact Hausdorff with no isolated points (a countable compact Hausdorff group would, by Baire, have an isolated point, hence be discrete, hence finite). ✓

**Conclusion.** For every Aut(C)-stable E and every Aut(C)-stable flow-invariant S ⊆ X₀^E, and every prime p: **either S ∩ Γ_p = ∅ or S ⊇ one periodic orbit of every base class, i.e. uncountably many.** In particular "exactly one closed orbit per prime" is unreachable. **Proposition 1 is CORRECT as stated.** ∎

### 8.2 Break attempt (failed)

I tried three routes to a counterexample.
* *Make Aut(C) act too small.* Blocked by Lemma C (surjectivity onto Ẑ×, then onto Ẑ×_(p)), which I verified independently in §6.
* *Make σ(γ) coincide with γ for all σ.* Would require u_σ ∈ p^Ẑ for all σ, contradicting surjectivity; or β not injective on orbits, contradicting the verbatim p. 33 / p. 2 / [x-06] Thm 4.2 statements.
* *Use an S that meets a packet only in non-periodic points.* Then the hypothesis "S contains one periodic point over p" fails; the proposition is silent, correctly, and the S4 requirement (one closed orbit per prime) is not met either. No counterexample.

### 8.3 Independent confirmation: Proposition 1 re-proves [x-03] Theorem 5.2's full-packet conclusion

Apply Proposition 1 with S = X₀^E itself, E any of the six named classes (all σ-stable by Lemma D(ii)). The packet locus is nonempty (χ_x has trivial kernel, so (x, χ_x) ∈ E_f ⊆ every named class). Hence the E-locus of Γ_p contains an orbit of **every** base class, i.e. every orbit, i.e. Γ^E_p = Γ_p. That is exactly [x-03] Thm 5.2's "If e.g. E ⊃ E_f then C^E_{x₀} = C_{x₀}" (p. 34) — obtained here by an independent route, and in fact for all six classes rather than only for E ⊇ E_f. **This is a genuine external check on Lemmas C and D together, and it passes.** The note asserts the same cross-check in one clause ("Proposition 1 conceptually explains [x-03] Thm 5.2's full-packet phenomenon"); I confirm it is a real derivation, not a slogan.

### 8.4 The Corollary — FINDING F3 (MAJOR)

**Statement under review.** "The local principle's coefficient-naturality (F1/F5) cannot be carried to the global setting: any global selection with the analogous naturality — **in particular, any selection defined uniformly from the abstract field C and the scheme data, since Deninger's construction takes an abstract algebraically closed C as input ([x-03] §5, 'Let C be an algebraically closed field which satisfies the conditions…') and transport of structure then makes every uniformly-defined locus Aut(C)-stable** — retains the full packet."

**The defect.** The bracketed justification cites [x-03] §5 (p. 31), which indeed says "Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4" — I verified it verbatim. But §5 constructs only the *Q^{>0}-set* C_{x₀}. The object Proposition 1 is about — the **dynamical system** X₀ = X̌₀(C)_E ×_{Q^{>0}} R^{>0}, and the sub-dynamical systems S4 asks for — is defined in **§7**, whose standing hypothesis is (p. 40, verbatim): "**In this section, C is an algebraically closed field with a valuation | | and the corresponding topology.**" The input to the dynamical system is therefore the *valued* field (C, | |), not the abstract field, and "defined uniformly from the abstract field C" is not the correct description of what a selection may consume. A selection may legitimately consume | |, and then it is Aut(C)-stable only under the subgroup Aut(C, | |) — which for C = ℂ with the usual modulus is {id, complex conjugation}, whose image in Ẑ× is {±1} and which therefore imposes essentially nothing.

This is not a fatal error: the note's own scope note (b) says "Wild automorphisms of C are discontinuous …, so Proposition 1 does NOT constrain selections using C's analytic structure", and §6 is written precisely to handle the |·|-consuming case. But the Corollary as printed advertises a reach the sources do not license, and its "in particular" clause is the sentence a downstream reader will quote.

**A second, sharper point the note misses, which should be in the repair.** The local/global analogy is *not* symmetric here, and the asymmetry is the real content. Every automorphism of a rank-1 valuation ring o is an isometry (|x| ≤ |y| ⟺ x/y ∈ o is a ring-theoretic condition; equivalently [x-03] Remark 14.17, p. 104, verbatim: "**Since automorphisms of o are p-adically continuous** we have compatible G × Aut(o)-operations on X̊_c(o), X̌_c(o), X⋄_c(o) and Y⋄ in the obvious way"). So locally, "valuation-using" and "full-coefficient-automorphism-equivariant" are *compatible* — which is exactly why Thm 15.6's selection can be both defined by |·| and Aut(o)-equivariant. Archimedeanly they are *mutually exclusive*: |·|_∞ is not definable from the field structure of ℂ, so an Aut(ℂ)-stable condition cannot use it and a |·|_∞-using condition cannot be Aut(ℂ)-stable. **That is why D1 and D2 must be read as a pair, not as two independent obstacles.**

**Fill.** Replace the "in particular" clause by a hypothesis that is a theorem rather than a schema: *isomorphism-invariance across coefficient fields.* Say that a class E is **coefficient-natural** if it is specified for every admissible coefficient field and satisfies E_{C′} = {σ ∘ χ : χ ∈ E_C} for every field isomorphism σ : C ⥲ C′; taking C′ = C this is literally Aut(C)-stability, so Proposition 1 applies with no schema at all. Then note explicitly that the six named classes are coefficient-natural, that Deninger's own "functorial" notion ([x-03] p. 29, verbatim: "It is also clear that the stable Galois invariant classes E are the functorial ones i.e. where (χ : κ× → C×) ∈ E implies (χ ◦ τ : κ̃× → C×) ∈ E for any homomorphism τ : κ̃ → κ of algebraically closed fields") is the source-side companion of the same idea, and that a selection consuming | | is by construction *not* coefficient-natural and is handled by §6, not §5. Replacement text in §11, F3.

**Severity MAJOR** (fillable; the note must change: the stated justification cites the wrong section, and the reach claimed for D1 is not what the sources support).

---

## 9. FINDING F4 (MAJOR) — "closed trichotomy" is contradicted by the note's own §6

**Location:** §0, verdict paragraph: "This is not one obstacle but a **closed trichotomy**, each branch decided here."

**The defect.** D1 covers Aut(C)-stable selections; D2 covers uniform archimedean-defect **threshold** conditions; D3 covers transported conditions. §6 then says, in the note's own words: "*What Lemma B does NOT close:* conditions on the archimedean defect PROFILE other than a uniform threshold (averaged, asymptotic, or comparative conditions). Note these are not blocked by Proposition 1 either, since |·|_∞ is not Aut(C)-invariant … **This narrow gap is the only surviving habitat for a points-selection global principle**." A trichotomy with an admitted surviving habitat is not closed. As shown in F3, the residue is not exotic: it is exactly the class of selections that consume the valuation §7 puts into the definition of the space, i.e. the whole of the analytically-defined selections minus the thresholds.

**Fill.** Replace "closed trichotomy" with an accurate three-decided-plus-one-open formulation, and carry the same correction into §8 item 1 (DQ-T is "DECIDED" only for the three branches). Replacement text in §11, F4. Note that this repair *does not* weaken the note's operational conclusion: the surviving habitat is empty of candidates in the sources (the note verifies this), and the note's own charter deliverable (DQ-M) is unaffected.

**Severity MAJOR** (a stated headline claim is false as worded and internally contradicted; the repair is a rewording, and the substance survives).

---

## 10. The two extra checks assigned to me

### 10.1 §3's freshman's-dream N-invariance argument — conclusion CORRECT, stated reason WRONG (F8, MINOR)

**Under review:** "The freshman's-dream asymmetry makes it precise: additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p. A mod-p-type selection and the full-Q^{>0} suspension design cannot coexist; one must give."

*p-stability:* verified. [x-03] Prop. 14.7, p. 94, verbatim: "For 0 < α < 1 we have F_p(Y̌_α) = Y̌_α and Y̌_α ⊂ Y̌, and hence Y̌_α = Y̌ for α ≥ 1/p." The proof on p. 95 uses F_p(I_y) = I_y for both inclusions. ✓

*Non-ℓ-stability:* the conclusion is right but the stated reason is the wrong computation. "(r+s)^ℓ ≢ r^ℓ + s^ℓ mod p" is a statement about the **source** ring; what has to fail is the defect of the **transported** map F_ν(P) = P ∘ ( )^ν. The correct computation (mine, §4.1 above, repeated here for the record): with P mod m = τ a ring homomorphism and a = τ(r), b = τ(s),
  (F_ν P)(r+s) − (F_ν P)(r) − (F_ν P)(s) = P((r+s)^ν) − P(r^ν) − P(s^ν) ≡ (a+b)^ν − a^ν − b^ν  (mod m).
Write ν = p^k m with p ∤ m. Then (a+b)^ν − a^ν − b^ν = ((a+b)^m − a^m − b^m)^{p^k}, and (a+b)^m − a^m − b^m is a nonzero polynomial over F_p when m > 1 (its ab^{m−1} coefficient is m ≢ 0 mod p), hence takes a nonzero value on the infinite field F̄_p; the defect then has absolute value 1 > |p|. Therefore
  **F_ν(Y̌) ⊆ Y̌ ⟺ ν ∈ p^{N₀}** — sharp, both directions, which is strictly more than the note states.

*Two strengthenings the note should take.* (a) The mismatch is **forced, not optional**, for X₀ = Spec Z: [x-03] p. 24, verbatim, "Let N₀ be the submonoid of N generated by a set of prime numbers char N₀ … We always assume that char N₀ ⊃ char X₀"; for X₀ = Spec Z, char X₀ is all primes, so N₀ = N. One cannot shrink N₀ to p^{N₀} and stay inside Deninger's global framework. (b) Def. 4.1's condition is **biconditional** ("χ is in E if and only if χ ◦ σ resp. χ_ν = χ ◦ ( )^ν is in E"), so both forward and backward ν-closure fail, not merely one. Replacement text in §11, F8.

### 10.2 §7's Haar formal count — arithmetic right, justification a non sequitur (F9, MINOR)

**Under review:** "At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is ∫_{B_p}(single-orbit term) dHaar = the single-orbit term, **since the integrand is constant (all orbits in Γ_p have length log p — [x-06] Thm 4.2)**."

*The cited fact is correct.* [x-06] Thm 4.2, p. 12, verbatim: "The compact subsets Γ_{x₀} ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| (= |R₀/m₀|) and they are pairwise disjoint. In fact Γ_{x₀} is a fibre space over the compact group Aut(F̄_p^×)/Aut(F̄_p) where p = char κ(x) with fibres the compact orbits in Γ_{x₀}." For X₀ = Spec Z, N x₀ = p, so every orbit in Γ_p has length log p. ✓ And ∫ of a constant against a probability Haar measure is that constant. ✓

*The reason is not sufficient.* An orbital term in any Ruelle/Lefschetz-type formula is not a function of length alone: it carries a transverse (holonomy/Poincaré-return) determinant factor and a multiplicity. Equality of lengths does not make the integrand constant. What could make it constant is a symmetry acting transitively on the orbits of the packet — and the note's only such symmetry is Lemma D(iii)'s B_p-translation via Aut(C), which by §7.1 above acts by **bijections that are not homeomorphisms**, so it cannot transport a topologically defined orbital weight. Nor can the flow or the Frobenii, which fix the base class (§2(f)).

*Also relevant, and the note should say it here.* The adjudication's own banked result 3 (`probe-9.3-adjudication.md` §4 item 3) records "the packet subspace topology is not (profinite) × (circle)". DQ-M's model-world statement in §8 posits exactly "a continuum B × S¹ of closed orbits", which is therefore known **not** to be a faithful model of Γ_p in its subspace topology. The note flags W12 in prose one paragraph earlier but does not connect it to DQ-M's model.

*What survives.* The trivial half — a Haar-averaged packet contributes the same *number* the T1 count wants, if the per-orbit contributions are equal — stands as a formal bookkeeping statement, and the note labels it "At the formal level". Nothing load-bearing rests on it: DQ-M is posed as open precisely because the analysis is missing. Replacement text in §11, F9. **Severity MINOR.**

---

## 11. REPAIRS — exact replacement text

Each item gives the text to substitute. Nothing else in the note need change.

**F1 (MAJOR) — §4, Lemma A.** Replace the statement's hypothesis clause and the parenthetical by:

> **Lemma A (derived).** Let o be a p-adically complete rank-1 valuation ring with quotient field C of characteristic 0, maximal ideal m and residue field k = o/m, and assume k is perfect of characteristic p with F̄_p ⊆ k (example: o = o_{C_p}, k = F̄_p). Let κ = F̄_p and let P : κ → o be multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ^× is a group homomorphism (its values then lie in μ^{(p)}(o), the prime-to-p roots of unity, because κ^× is prime-to-p torsion). Then
>  |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·] ∘ τ for a unique field embedding τ : κ ↪ k,
> where [·] is the Teichmüller section of the reduction isomorphism μ^{(p)}(o) ≅ μ^{(p)}(k). In particular mod-p additivity forces P|_{κ^×} to be injective.

and add, after the derivation, this converse in place of the Witt-vector parenthetical:

> (⇐) Let a = τ(r), b = τ(s) ∈ k and n ≥ 1. Put A = [a^{p^{−n}}], B = [b^{p^{−n}}], C = [a^{p^{−n}} + b^{p^{−n}}] = [(a+b)^{p^{−n}}]; then ε := A + B − C ∈ m. Now
>  [a] + [b] − [a+b] = (A^{p^n} + B^{p^n} − (A+B)^{p^n}) + ((A+B)^{p^n} − (A+B−ε)^{p^n}).
> The first bracket lies in p·o because p | C(p^n, i) for 0 < i < p^n. For the second, |x^p − y^p| ≤ max(|x−y|^p, |p||x−y|) gives by iteration |x^{p^n} − y^{p^n}| ≤ max_{0≤j≤n} |p|^j |x−y|^{p^{n−j}}, which is ≤ |p| for n large since |ε| < 1. Hence |[a] + [b] − [a+b]| ≤ |p|. (No Witt ring and no embedding W(k) ⊆ o is needed.) ∎

*Optional generality clause*, if the note wishes to keep arbitrary algebraically closed κ of characteristic p: replace "κ = F̄_p" by "κ an algebraically closed field of characteristic p admitting an embedding into k", delete the parenthetical about roots of unity, let [·] : k → o be the p-adic Teichmüller section [a] = lim_n ã_n^{p^n}, and replace the final step of (⇒) by: "P ∘ τ^{−1} is a multiplicative section of o ↠ τ(κ) and τ(κ) is perfect; by the estimate above every multiplicative section is given by a ↦ lim_n ã_n^{p^n}, hence P ∘ τ^{−1} = [·]|_{τ(κ)} and P = [·] ∘ τ."

**F2 (MAJOR) — §0 bullet (D3) and §4 Consequence 2.** In §0, replace "and the resulting class is precisely probe A's Theorem C cut E(a₀): non-canonical, theory-forfeiting, already adjudicated a design constraint, not a solution" by:

> and the resulting class T_j is not admissible (it is Aut(κ)-closed but not ν-closed for p ∤ ν), while its char-p members are exactly the injective members of probe A's Theorem-C cut E(a_j) and it selects the same single base class per prime. The admissible closure of the transport is therefore E(a_j): non-canonical, theory-forfeiting, already adjudicated a design constraint, not a solution.

In §4 Consequence 2, replace "So the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀: it exists, it is one arbitrary point of a Cantor torsor per prime, it is not admissible-with-theory (forfeits every certified theorem), and it is not N-invariant — precisely [x-03]'s p. 29 Remark." by:

> So the faithful transport of the local principle is a class T_j which is **not** admissible — it satisfies Def. 4.1's Aut(κ)-condition but fails its ν-condition for every ν ∉ p^{N₀}, precisely [x-03]'s p. 29 Remark "the resulting class E is not N-invariant" — and whose char-p members are exactly the injective members of the adjudicated Theorem-C cut E(a_j), with j in place of a₀. In particular T_j ⊊ E(a_j), the two cut every packet to the same single base class, and E(a_j) is the smallest admissible class containing T_j. The choice content is identical: one arbitrary point of the Cantor group B_p per prime. Passing to the admissible closure buys admissibility at the price of Deninger's certified theorems (E(a_j) ⊉ E_f); refusing to pass leaves a class outside Def. 4.1 altogether. Nothing new is gained either way.

**F3 (MAJOR) — §5, the Corollary.** Replace "in particular, any selection defined uniformly from the abstract field C and the scheme data, since Deninger's construction takes an abstract algebraically closed C as input ([x-03] §5, 'Let C be an algebraically closed field which satisfies the conditions…') and transport of structure then makes every uniformly-defined locus Aut(C)-stable" by:

> in particular, any **coefficient-natural** selection, i.e. one specified for every admissible coefficient field and satisfying E_{C′} = {σ ∘ χ : χ ∈ E_C} for every field isomorphism σ : C ⥲ C′ (take C′ = C: this is literally Aut(C)-stability, so no definability schema is needed). All six of Deninger's named classes are coefficient-natural, and coefficient-naturality is the target-side companion of his own "functorial" notion for classes ([x-03] p. 29). It must be stressed what this does **not** cover: the dynamical system itself is built in [x-03] §7 from a *valued* field — p. 40, "In this section, C is an algebraically closed field with a valuation | | and the corresponding topology" — so a selection may legitimately consume | |, and such a selection is stable only under Aut(C, | |), which for C = ℂ is {id, conjugation}. Here the local/global analogy breaks in a way worth naming: every automorphism of a rank-1 valuation ring is an isometry ([x-03] Remark 14.17, p. 104: "automorphisms of o are p-adically continuous"), so locally *valuation-using* and *fully Aut-equivariant* are compatible — which is exactly how Thm 15.6 manages to be both; archimedeanly they are mutually exclusive, because |·|_∞ is not definable from the field structure of ℂ. D1 therefore does not stand alone: it is the half of the dichotomy that D2 (§6) completes.

Also add, in Lemma D(i) or immediately after it: "σ acts by **bijections**, not homeomorphisms — a wild automorphism of C is discontinuous, and the topology on X̊(C) is pointwise convergence into C with its valuation topology ([x-03] §7, p. 40). Every step of Lemma D and Proposition 1 is set-theoretic and none uses continuity."

**F4 (MAJOR) — §0.** Replace "This is not one obstacle but a closed trichotomy, each branch decided here" by:

> This is not one obstacle but three, decided here, plus one explicitly delimited residue (§6): the trichotomy D1–D3 closes every coefficient-natural selection, every uniform archimedean-defect threshold, and every faithful transport of the local condition; what it does not close is a non-threshold condition on the archimedean defect **profile**, which is the one surviving habitat and for which the sources offer no candidate.

and in §8 item 1, replace "DQ-T (the transplant trichotomy) — DECIDED in this note, probe grade" by "DQ-T (the transplant trichotomy) — three branches DECIDED in this note, probe grade; the archimedean defect-profile residue named in §6 remains open".

**F5 (MINOR) — §2 Stage 2 and §6.** The sentence "Incidentally, if we consider points of W_rat(X) with values in rings without 'small multiplicative subgroups' like the complex number field C this process does not give more points" is on **printed page 6**, not page 5. Change both occurrences of "[x-03] intro p. 5" that carry this quote to "[x-03] intro p. 6". (The p. 5 citations for "There is a minimal condition E … but it does not look natural" are correct and stay.)

**F6 (MINOR) — §4, packet coordinates.** Replace "B_p := Ẑ×₍p₎/p^Ẑ = Aut(F̄_p)^×/Aut(F_p)^" by "B_p := Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p)" — the displayed formula on [x-03] p. 33 (and p. 2, and [x-06] p. 12). The printed version puts the × inside on the numerator (automorphisms of the *group* F̄_p^×) and the bar on the denominator (automorphisms of the *field* F̄_p); the note's transcription reverses both, and reversed it does not typecheck, since Aut(F_p) is trivial. (The mangling is what `pdftotext` produces on this file; verify displays on a page render.)

**F7 (MINOR) — Lemma D and Proposition 1.** Replace "closed orbit" by "periodic orbit" throughout (four occurrences in Lemma D(iii) and Proposition 1). In X₀ a periodic orbit is provably **not** a closed subset (`probe-9.3-adjudication.md` §4 item 3, corollary), so "closed orbit" is actively misleading in this program's vocabulary even though it is standard dynamics usage.

**F8 (MINOR) — §3, requirement 4.** Replace "The freshman's-dream asymmetry makes it precise: additivity mod p is ( )^p-stable (Prop. 14.7's computation) but not ( )^ℓ-stable for ℓ ≠ p, since (r+s)^ℓ ≢ r^ℓ + s^ℓ mod p." by:

> The freshman's-dream asymmetry makes it precise, and sharply. Additivity mod p is ( )^p-stable in both directions ([x-03] Prop. 14.7, p. 94: F_p(Y̌_α) = Y̌_α). For general ν it is not: with P mod m = τ a ring homomorphism and a = τ(r), b = τ(s),
>  (F_ν P)(r+s) − (F_ν P)(r) − (F_ν P)(s) ≡ (a+b)^ν − a^ν − b^ν (mod m),
> and writing ν = p^k m with p ∤ m the right side is ((a+b)^m − a^m − b^m)^{p^k}, a nonzero polynomial over F_p as soon as m > 1 (its ab^{m−1} coefficient is m), hence nonzero for suitable a, b ∈ F̄_p. So **F_ν(Y̌) ⊆ Y̌ ⟺ ν ∈ p^{N₀}**. Def. 4.1's condition is biconditional, so both directions of ν-closure fail. And the clash is forced rather than optional: [x-03] p. 24 requires char N₀ ⊃ char X₀, so for X₀ = Spec Z the acting monoid is all of N. A mod-p-type selection and the full-Q^{>0} suspension design cannot coexist; one must give.

**F9 (MINOR) — §7, Road 2.** Replace "since the integrand is constant (all orbits in Γ_p have length log p — [x-06] Thm 4.2)" by:

> if the per-orbit contributions are equal. [x-06] Thm 4.2 (p. 12) gives that all orbits in Γ_p have the same length log p, but a Ruelle/Lefschetz orbital term also carries a transverse determinant and a multiplicity, so equal length alone does not give equal contribution. The symmetry that would give it — the transitive B_p-translation of Lemma D(iii) — is implemented by field automorphisms of C, which act by bijections and not by homeomorphisms, so it cannot transport a topologically defined weight. **Constancy of the integrand is therefore itself part of DQ-M, not an input to it.** Note also that DQ-M's model world (a continuum B × S¹ of closed orbits) is known *not* to be a faithful model of Γ_p in its subspace topology, by W12 (`probe-9.3-adjudication.md` §4 item 3: "the packet subspace topology is not (profinite) × (circle)"); the model question is still well posed and still the right first probe, but a YES on it does not transfer to X₀ without separately settling the topology.

**F10 (MINOR) — §5, Lemma C.** Replace the statement's parenthetical and the derivation by:

> **Lemma C (derived; cyclotomic theory + Steinitz).** For every algebraically closed field C of characteristic 0 the restriction map Aut(C) → Aut(μ(C)) = Ẑ× is surjective; composing with the projection Ẑ× ↠ Ẑ×_(p) it is surjective onto Aut(μ^{(p)}(C)) = Ẑ×_(p). *Derivation:* μ(C) ≅ Q/Z, so Aut(μ(C)) = Aut(Q/Z) = Ẑ×. Given u ∈ Ẑ×, the cyclotomic character Gal(Q(μ_∞)/Q) ⥲ Ẑ× supplies σ₁ ∈ Aut(Q(μ_∞)) acting on roots of unity by ζ ↦ ζ^u; extend σ₁ to the algebraic closure Q̄ ⊆ C (isomorphism extension); extend to Q̄(B) by fixing a transcendence basis B of C over Q̄ pointwise; extend to C, which is an algebraic closure of Q̄(B) (isomorphism extension again). Each extension uses Zorn's lemma; the resulting σ is in general non-measurable, which does not affect Proposition 1, since only its existence is used. ∎

**F11 (MINOR) — §5, Lemma D(iii).** Replace "because χ_x is an isomorphism onto μ^{(p)}(C) (injective character between groups ≅ ⊕_{ℓ≠p}Q_ℓ/Z_ℓ, divisible-image argument as in Lemma A) and power maps commute with any group homomorphism" by:

> because χ_x takes values in μ^{(p)}(C), on which σ acts as ( )^{u_σ} for a unique u_σ ∈ Aut(μ^{(p)}(C)) = ∏_{ℓ≠p} Aut(Q_ℓ/Z_ℓ) = Ẑ×_(p) (obtained from Lemma C's u ∈ Ẑ× by the projection Ẑ× ↠ Ẑ×_(p)); and Ẑ_(p)-power maps commute with every homomorphism of prime-to-p torsion abelian groups — for a of order d, ord(f(a)) | d, so u mod ord(f(a)) is determined by u mod d and f(a^u) = f(a)^u.

**F12 (MINOR) — §6, Lemma B.** Replace "at every point of every packet (any prime p, any character P in any class E ⊆ E_tors)" by "at every point of every packet (any prime p, any multiplicative P whatever — the E-condition is not used)", and append to the lemma:

> More precisely 1 ≤ |P(2̄) − 2| ≤ 3, with the lower bound attained exactly when P(2̄) = 1. The upper bound closes off the escape of simply raising the threshold: any ε ≥ 3 is vacuous, and any ε ∈ [1, 3) gives a non-topologically-nilpotent defect ideal, which by (172) (p. 94) cannot induce the A_inf-analogue action that is Stage 3's entire purpose. The failure is also independent of normalization: since every nonzero value of P at a char-p point has modulus 1, the scale-relative variants |defect| ≤ ε·max(|P(r̄)|, |P(s̄)|) and |defect| ≤ ε·|P(r̄)P(s̄)| fail at r = s = 1 for the same ε < 1.

**F12b (MINOR) — §4, after Lemma A.** Append to the lemma statement: "In particular mod-p additivity forces P|_{κ^×} to be injective (τ is injective and [·] is), which is what §4 Consequences 1 and 2 use."

**F13 (MINOR) — §4, the consistency check.** Replace "and Hom(κ₀, k) is a single F_p-orbit of size r = deg(κ₀/F_p)" by "and after dividing by G one gets Y⋄_{0 s₀} ≅ Hom(κ₀, k) ([x-03] (224), p. 114), a single F_p-orbit of size r = deg(κ₀/F_p)".

**F14 (MINOR, bookkeeping) — §4 and §5.** For "distinct base classes lie on distinct orbits" cite, in addition to [x-03] p. 33 (which states it for Q^{>0}-orbits in C_{x₀}), the two places where it is stated directly for periodic orbits of the flow: [x-03] p. 2 ("with fibres the periodic orbits in Γ_{x₀}. Each periodic orbit of X₀ lies in exactly one packet Γ_{x₀}") and [x-06] Thm 4.2, p. 12 ("with fibres the compact orbits in Γ_{x₀}"). This removes the one suspension step the current citation leaves to the reader.

---

## 12. WHAT IS NOW ESTABLISHED AT REFEREE GRADE, AND ITS PRECISE SCOPE

At referee grade, from this pass: **Proposition 1 is a theorem.** For X₀ = Spec Z, for every class E of characters that is stable under post-composition by field automorphisms of C — which includes all six of Deninger's named classes E_tors, E_max, E_f, E_fg, E_fd, E_fd0, each verified stable one condition at a time against the verbatim definitions on [x-03] pp. 27–28, the (Image) condition of E_max included and easily so — and for every subset S ⊆ X₀^E that is flow-invariant and stable under the same post-composition, the following dichotomy holds at every prime p: either S contains no periodic point over p, or S contains a periodic orbit of length log p in every one of the uncountably many base classes of B_p = Ẑ×_(p)/p^Ẑ = Aut(F̄_p^×)/Aut(F̄_p). Hence no such S has exactly one closed orbit per prime. The proof consumes exactly four verified inputs — the coordinate surjection (35) and its fibre relation ([x-03] p. 32), the fibration of C_{x₀} over B_p with fibres the Q^{>0}-orbits ([x-03] p. 33, and directly for periodic orbits at [x-03] p. 2 and [x-06] Thm 4.2 p. 12), Theorem 6.1's assignment of every periodic orbit to a unique packet ([x-03] p. 39), and the isotropy computation of Theorem 5.2 ([x-03] p. 34) — together with Lemma C (surjectivity of Aut(C) → Ẑ×, a ZFC statement with non-measurable witnesses) and Lemma D (commutation, class stability, and the coordinate formula (a,ν) ↦ (u_σ a, ν)), all three parts of which I re-derived and none of which needs continuity of the Aut(C)-action. As an independent check, Proposition 1 reproves [x-03] Theorem 5.2's full-packet conclusion for all six named classes. Also at referee grade: **Lemma B**, in the strengthened form 1 ≤ |P(2̄) − 2| ≤ 3 at every point of every packet, from which the archimedean-threshold reading selects the empty set on the periodic locus for every ε < 1, for every normalization of the bound, and from which no larger threshold can restore the A_inf-analogue action; and **Lemma A**, in the corrected statement of §11 F1 (κ = F̄_p, k perfect with F̄_p ⊆ k), including the converse, for which I supply an elementary proof that replaces the note's Witt-vector one-liner.

The scope is narrower than the note's headline in three respects, all recorded as MAJOR findings. (1) The no-go binds **coefficient-natural** selections — those defined compatibly across coefficient fields — and *not* selections that consume the absolute value on C, which [x-03] §7 p. 40 puts into the definition of the space itself; the note's "uniformly from the abstract field C" clause cites §5, where the topology has not yet been introduced. (2) Consequently D1 and D2 are complements, not independent obstacles, and the trichotomy is **not closed**: the note's own §6 leaves non-threshold archimedean defect-profile conditions untouched, and that residue is exactly the |·|-consuming selections D1 cannot reach. (3) The transport reading (D3) yields a class that is *not* admissible and therefore is *not* the Theorem-C cut E(a₀); what is true, and enough, is that its char-p members are the injective members of E(a₀), that it selects the same single base class per prime, and that its admissible closure is E(a₀) — so the transport still buys nothing beyond the already-adjudicated non-canonical cut. None of these three corrections touches the note's operational verdict for the program: the transplant-as-selection route is closed for every canonical selection the sources make available, the surviving habitat is empty of candidates, and the charter's decidable sub-question DQ-M is unaffected. Nothing in this pass reopens `probe-9.3-adjudication.md`; its Theorem A, its G1 = NO, and its Theorem C stand untouched, and its §4 item 5b's description of the cuts as *admissible* is the record that F2 corrects the 9.4 note against.

---

## 12b. MACHINE CHECKS (finite verifications of the steps above)

Script `results/c3-r/referee-s14/94-lemmas-O-checks.py`, output `94-lemmas-O-checks.json`, run this session; **ALL_PASS = true**. These are finite checks of steps I asserted by hand, not substitutes for the derivations.

| check | what it verifies | result |
|---|---|---|
| B_min_defect / B_max_defect | modulus of (e^{iθ} − 2) over 10⁵ angles: minimum 1.0 (at θ = 0), maximum 3.0 (at θ = π) — Lemma B's sharp two-sided bound 1 ≤ abs(P(2̄) − 2) ≤ 3 | 1.0 / 3.0 ✓ |
| binom_pn_divisible_by_p | p divides C(p^n, i) for 0 < i < p^n, all p ∈ {2,3,5,7,11}, n ≤ 3 — the first bracket of Lemma A's converse (Step 4) | true ✓ |
| freshman_rows_all_consistent | for p ∈ {2,3,5,7} and 2 ≤ ν < 40 (152 pairs): (a+b)^ν − a^ν − b^ν has a nonzero coefficient mod p **iff ν is not a power of p** — the sharp form F_ν(Y̌) ⊆ Y̌ ⟺ ν ∈ p^{N₀} of F8 | true ✓ |
| C_nu_1_nonzero_when_p_nmid_nu | C(ν,1) = ν ≢ 0 mod p whenever p ∤ ν — the specific coefficient named in F8's replacement text | true ✓ |
| Bp_quotient_orders_grow | for p ∈ {2,3,5,7,13} and #T up to 10, the image of p in ∏_{ℓ∈T}(Z/ℓ)^×/squares leaves a quotient of order ≥ 2^{#T−1} ≥ 2^9 — B_p has arbitrarily large finite quotients, hence is infinite, hence uncountable | true ✓ |
| power_commutes_with_hom | f(a^u) = f(a)^u for every quotient map Z/d ↠ Z/e (with e dividing d) and every u coprime to d, d < 60 — the order-divisibility step in Lemma D(iii) | true ✓ |
| teichmuller_estimate_converges | the iteration δ ↦ max(δ^p, δ/p) drives every δ₀ < 1 below 1/p — the convergence used in Lemma A Steps 3b and 4 | true ✓ |
| prime_to_p_order_is_unit | d prime to p ⟹ d ≢ 0 mod p — the unit used to prove reduction injective on μ^{(p)}(o) | true ✓ |

---

## 13. SOURCES — every page read this session

**[x-03]** C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4, `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`, 119 pp. PDF page = printed page (verified). Read this session, in the fresh `pdftotext -layout` extraction unless marked:
* pp. 2–3 (introduction: packets, the fibration over Aut(F̄_p^×)/Aut(F̄_p), "Each periodic orbit of X₀ lies in exactly one packet"). **p. 2 also read on a 150-dpi page render.**
* pp. 5–6 (the "minimal condition E … does not look natural" line, p. 5; the "does not give more points" line and "the process of 'completion' … was necessary", both p. 6; "The answer is simple, Y⋄ consists of all the diagrams … mod p also additive", p. 6).
* p. 24 (definition of N₀ and the constraint char N₀ ⊃ char X₀).
* pp. 26–29 (the (Tors)/(Image) conditions; Def. 4.1; Prop. 4.2; Lemma 4.3; the conditions before Cor. 4.4; Cor. 4.4; the six example classes; the Remark "P is additive mod p … However the resulting class E is not N-invariant"; stable/functorial classes; Prop. 4.5).
* pp. 31–35 (§5: ι, χ_x = ι ∘ i_x^{−1}, (32)–(35), (36)–(37), (38)–(39), the isotropy computation, the fibration over Ẑ×_(p)/p^Ẑ and "the fibres are the Q₀^{>0}-orbits", the choice-dependence sentence, (40)–(46), Prop. 5.1, Thm 5.2 and its proof opening). **p. 33 read on a 150-dpi page render** (this is where F6 was caught).
* p. 39 (Thm 6.1 and the paragraph after it), p. 40 (the S4 question, and §7's opening: "C is an algebraically closed field with a valuation | | and the corresponding topology"; the pointwise-convergence topology; Lemma 7.1), pp. 41–42 (Lemma 7.2 and the topology on non-affine X, the quotient topology on X̊₀(C)).
* pp. 88–95 (§14 opening and its standing hypotheses on o; Defs. 14.1, 14.2; Props. 14.3, 14.4; (163)–(171); the [CD14] presentation of W_p(R) and the generators of I; Def. 14.5; Remark 14.6; (172)–(174); Prop. 14.7 and both of its proofs).
* pp. 96–101 (Prop. 14.8; Def. 14.9; Supplement 14.10; Prop. 14.11; Def. 14.12 = (183) and the Remark "I do not know how to transport such conditions to the points of X̌(C) …"; (184)–(185); Prop. 14.13; Prop. 14.14 and its proof).
* p. 104 (Remark 14.17: "automorphisms of o are p-adically continuous"; §15 opening and the Lubin–Tate setup).
* pp. 112–117 (Cor. 15.5 and the K₀ = Q_p example; p. 113's determination of the two (x,y) pairs and "the ring homomorphisms P̂_y : κ ↪ k ⊂ o^♭"; Thm 15.6 parts 1)–6) with (221)–(226) and the Remark; the proof of 6); Prop. 15.7; Prop. 15.8 and its proof).

**[x-06]** C. Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643, `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Read this session:
* pp. 10–13 (§4: the multiplicative map (11); Thm 4.1 with the G- and N-actions; the "too many periodic orbits … we can only impose an 'admissible' condition E" paragraph; **Thm 4.2 and the paragraph after it, pp. 11–12** — orbit lengths log N x₀, pairwise disjointness, the fibre space over Aut(F̄_p^×)/Aut(F̄_p) with fibres the compact orbits; Thm 4.3; the infinite-dimensionality/unitary-closure paragraph; Thm 4.4 and "not a homeomorphism"; the Kucharczyk–Scholze discussion and the Steinberg-relations sentence).

**Program-internal, read in full this session:** `results/c3-r/probe-9.3-adjudication.md`; `results/c3-r/probe-9.4-note.md`; `results/c3-r/probe-9.3-a.md` §4 (Theorem C and its reachability computation, §§4.1–4.3) — consulted to check finding F2 against probe A's actual definition of E(χ^{a₀}).

**Read for the corpus caveats, as instructed, before citing anything:** `results/corpus-routing.md`, header §"Standing corpus-wide caveats" (items 1–20). Neither [x-03] nor [x-06] appears on any vision-needed, page-mapping or text-layer-corruption list; the `pdftotext` accent/superscript loss documented above is a property of this particular file's font encoding and is the reason every load-bearing display in this report was re-read on a page render.

**Not consulted, and nothing here depends on them:** [r3s-08] (Morishita) and [D25] (rational Witt vectors) — neither is cited by the lemmas under review; the 9.3 adjudication's own W11 flag ("do not cite [r3s-08] for topology") is respected by omission.

— end of referee report O —
