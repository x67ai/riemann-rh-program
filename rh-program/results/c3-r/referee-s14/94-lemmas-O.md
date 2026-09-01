# REFEREE REPORT O — probe 9.4 note, Lemmas A–D and Proposition 1 (transplant trichotomy D1–D3)

**Program:** RH program, direction C3-r (geometric substrate, reduced recommission). **Session 14.**
**Date:** 2026-09-02.
**Referee:** referee O (one of two independent referees on this item; standing order 7). No contact with, and no assumption about, the second referee's findings.
**Note under review:** `results/c3-r/probe-9.4-note.md` (read in full, all 136 lines).
**Binding prior record read in full first:** `results/c3-r/probe-9.3-adjudication.md`.
**Item:** §§3–7 of the note insofar as they carry Lemmas A, B, C, D and Proposition 1, plus the two auxiliary derivations the charter names (§3's freshman's-dream N-invariance argument; §7's Haar formal count).

**Method actually used.** Every source sentence quoted below was read this session from the on-disk PDF with `pdftotext -layout` (poppler 26.08.0), and one ambiguous display was additionally read by rendering the page to PNG and reading the image (see §1.3). Every lemma is re-derived here from scratch, in full, so that this report can be checked without the note. Where the note's proof does not carry its statement, both a fill (replacement text) and a break (counterexample search) were attempted and both attempts are reported. Nothing below is asserted from memory; the two places where I use a standard fact I could not read on disk are marked **[RU]** and are not load-bearing (each has an on-disk-only substitute proof supplied).

---

## 0. VERDICT SUMMARY (stated first)

| Item | Verdict | Findings |
|---|---|---|
| **Lemma A** (§4) — mod-p-additive multiplicative maps = Teichmüller class, **with converse** | **PASS-WITH-REPAIRS** | 2 MAJOR (A-1 hypothesis is false in the stated generality; A-2 the converse's Witt justification is not valid under the note's own hypotheses — the statement is nevertheless TRUE, and a self-contained proof is supplied), 2 MINOR |
| **Lemma B** (§6) — archimedean defect bound selects the empty set on the periodic locus | **PASS** (strengthened) | 0 MAJOR, 2 MINOR. The lemma is correct, sharp, and in fact holds on a strictly larger locus than the note claims. |
| **Lemma C** (§5) — Aut(C) ↠ Aut(μ(C)) = Ẑ<sup>×</sup> | **PASS** | 0 MAJOR, 2 MINOR (an unnecessary hypothesis; one garbled clause). Each of the four extension steps and the exact use of choice re-derived. |
| **Lemma D** (§5) — Aut(C)-action commutes with everything and preserves all six named classes | **PASS** | 0 MAJOR, 3 MINOR. (Image) for E_max — the note's own press point — checks, one class at a time. D(iii)'s coordinate formula checks. |
| **Proposition 1** (§5) — the equivariance no-go (D1) | **PASS** (strengthened) | 0 MAJOR, 1 MINOR (the cited anchor is one page weaker than the available one). The uncountability input and the distinct-base-classes-are-distinct-orbits input both re-derived and confirmed. |
| **§3 freshman's-dream N-invariance argument** | **PASS** (strengthened) | 0 findings; a strictly stronger obstruction is supplied (§8.1). |
| **§7 Haar formal count** | **PASS-WITH-REPAIRS** | 1 MAJOR (H-1: "the integrand is constant" is not established by equality of orbit lengths; a correct homogeneity proof is supplied, and it runs through Lemma D). |
| **Citation/transcription layer across §§2–7** | — | 5 MINOR (one of them a displayed identity that is false as transcribed; verified against a page render). |

**Overall on the assigned item: PASS-WITH-REPAIRS. FATAL 0 · MAJOR 3 · MINOR 15.**

**The trichotomy D1–D3 survives the pass.** None of the three MAJOR findings touches the truth of D1, D2 or D3. A-1 and A-2 are defects in the *statement and proof* of Lemma A, not in the fact Lemma A is used for (the case κ ≅ F̄_p, which is the only case the note ever applies); H-1 is in Road 2, which is a positive-road proposal explicitly parked in DQ-M and carries none of the trichotomy. After the repairs listed in §10 the note's §0 verdict is, in my judgment, established at referee grade in the precise scope stated in §11.

---

## 1. Sources: what was opened, and the verbatim anchors

### 1.1 [x-03] Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4
`fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`, 160 PDF pages. **In this file the printed page number equals the PDF page number** (checked on pp. 33, 40, 116 against the printed folio in the extraction). All page references below are therefore unambiguous.

Anchors read verbatim this session (quotations are transcriptions of the `pdftotext -layout` output, with LaTeX overlines/hats restored where the extractor drops them; where restoration was not obvious I rendered the page — see §1.3):

**(a) p. 27, Definition 4.1 (admissibility), and the two conditions.**
> "(Tors) the group ker(χ)<sub>tors</sub> = ker(χ |µ(κ)) is finite and |(ker χ)<sub>tors</sub>| ∈ N₀.
> (Image) Only if char κ > 0. If χ(κ<sup>×</sup>) is torsion, then κ<sup>×</sup> is torsion as well, i.e. κ<sup>×</sup> ⊗ Q ≠ 0 implies χ(κ<sup>×</sup>) ⊗ Q ≠ 0.
> Conditions (Tors) and (Image) are weakened versions of injectivity of χ.
> **Definition 4.1.** A class E of characters χ : κ<sup>×</sup> → C<sup>×</sup> on algebraically closed fields κ is (N₀−)admissible if for any σ ∈ Autκ resp. ν ∈ N₀ the character χ is in E if and only if χ ◦ σ resp. χ<sub>ν</sub> = χ ◦ ( )<sup>ν</sup> is in E. Moreover the characters in E should satisfy (Tors)."

**(b) pp. 28–29, the six named example classes.**
> "Example. 1) E<sub>tors</sub> : (Tors) holds
> 2) E<sub>max</sub> : (Tors) and (Image) hold
> 3) E<sub>f</sub> : (Tors) and ker χ is finite. Equivalently: | ker χ| ∈ N₀
> 4) E<sub>fg</sub> : (Tors) and ker χ is finitely generated
> 5) E<sub>fd</sub> : (Tors) and ker χ ⊗ Q is finite dimensional
> 6) E<sub>fd0</sub> : (Tors) and (ker χ |κ(x₀)<sup>×</sup>) ⊗ Q is finite dimensional where x₀ = π(x) under the projection π : X → X₀.
> We have inclusions in the appropriate sense E<sub>f</sub> ⊂ E<sub>fg</sub> ⊂ E<sub>fd</sub> ⊂ E<sub>fd0</sub> ⊂ E<sub>max</sub> ⊂ E<sub>tors</sub>."

**(c) p. 29, the two Remarks the note leans on.**
> "Remark. … Incidentally, in the p-adic case where we will deal with multiplicative maps P into a p-adic valuation ring and N₀ = p<sup>Z</sup>, the right condition E is the following: P is additive mod p. This can be rephrased in terms of absolute values and translated to the case where C is the complex number field. **However the resulting class E is not N-invariant.**"

and, on the same page, a *different* technical use of the word "stable":
> "We call a class E of characters χ : κ<sup>×</sup> → C<sup>×</sup> on algebraically closed fields κ **stable** if χ ∈ E implies that χ |κ̃<sup>×</sup> ∈ E for all algebraically closed subfields κ̃ ⊂ κ. All classes in the example are stable except for (Image) and hence E<sub>max</sub>."

**(d) p. 31, the standing hypothesis on C, and the choice of ι.**
> "Let C be an algebraically closed field which satisfies the conditions before Corollary 4.4." … "Fix an injective homomorphism ι : µ(K) ↪ µ(C). It exists by our assumptions on char K₀ and char C." … "The reduction map O<sub>X,x</sub> → κ(x) induces an isomorphism i<sub>x</sub> : µ<sup>(p)</sup>(K) = µ<sup>(p)</sup>(O<sub>X,x</sub>) →∼ κ(x)<sup>×</sup>." (=(32))

(The conditions before Cor. 4.4, p. 28: "1) C<sup>×</sup> ≠ µ(C) i.e. C is not the algebraic closure of a finite field 2) card K₀ ≤ card C 3) char C = 0 or char K₀ = char C is positive.")

**(e) p. 32, (34) and (35) — the packet coordinates.**
> "The group of automorphisms of the abelian group κ(x)<sup>×</sup> is given by Ẑ<sup>×</sup><sub>(p)</sub> where Ẑ<sub>(p)</sub> = ∏<sub>l≠p</sub> Z<sub>l</sub>. We have a natural inclusion
> N x₀<sup>Ẑ</sup> = Gal(κ(x)/κ(x₀)) ↪ Aut(κ(x)<sup>×</sup>) = Ẑ<sup>×</sup><sub>(p)</sub> .   (34)
> Here on the left, N x₀ corresponds to the Frobenius automorphism y ↦ y<sup>N x₀</sup> in the Galois group. The monoid Ẑ<sup>×</sup><sub>(p)</sub> × N₀ acts by pre-composition on the set S of homomorphisms P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> with finite cyclic kernel of order in N₀. We have a Ẑ<sup>×</sup><sub>(p)</sub> × N₀-equivariant surjection:
> Ẑ<sup>×</sup><sub>(p)</sub> × N₀ ↠ S , (a, ν) ↦ χ<sub>x</sub> · (a, ν) := χ<sub>x</sub> ◦ ( )<sup>a</sup> ◦ ( )<sup>ν</sup> .   (35)
> Two elements (a, ν) and (a′, ν′) are in the same fibre of this map if and only if ν′ = νp<sup>n</sup> and a = p<sup>n</sup>a′ for some n ∈ Z."

and, immediately before, the identification of the fibre:
> "The fibre pr₀<sup>−1</sup>(x₀) consists of the G-orbits of all pairs (x, P<sup>×</sup>) where x is a point of X over x₀ and P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> satisfies (Tors). Since κ(x)<sup>×</sup> is torsion this means that ker P<sup>×</sup> = (ker P<sup>×</sup>)<sub>tors</sub> is finite hence cyclic and | ker P<sup>×</sup>| ∈ N₀."

**(f) pp. 32–33, (38), (39) and the fibration — the sentence Proposition 1 consumes.**
> "(Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup>) ×<sub>p<sup>Z</sup></sub> Q₀<sup>>0</sup> →∼ C<sub>x₀</sub> .   (38)" … "It follows that all points P₀ ∈ C<sub>x₀</sub> have isotropy subgroup (Q₀<sup>>0</sup>)<sub>P₀</sub> = N x₀<sup>Z</sup>." … "(Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup>) ×<sub>p<sup>Z/ deg x₀</sup></sub> (Q₀<sup>>0</sup>/N x₀<sup>Z</sup>) →∼ C<sub>x₀</sub> .   (39)
> **The set C<sub>x₀</sub> fibres over the compact group Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) , and the fibres are the Q₀<sup>>0</sup>-orbits in C<sub>x₀</sub>.**" … "**The maps (37), (38) and the fibration map depend on our choices of x and ι.**"

**(g) p. 34, Theorem 5.2.**
> "**Theorem 5.2.** Let E be an admissible class with E ⊂ E<sub>max</sub>. The following decomposition holds … {P₀ ∈ X̌₀(C)<sub>E</sub> | (Q₀<sup>>0</sup>)<sub>P₀</sub> ≠ 1} = ∐<sub>x₀</sub> C<sup>E</sup><sub>x₀</sub> . (47) For any point P₀ ∈ C<sup>E</sup><sub>x₀</sub> the isotropy group of P₀ is (Q₀<sup>>0</sup>)<sub>P₀</sub> = N x₀<sup>Z</sup> where N x₀ = |κ(x₀)|. If e.g. E ⊃ E<sub>f</sub> then C<sup>E</sup><sub>x₀</sub> = C<sub>x₀</sub>."

**(h) p. 38, §6 — the suspension, and a *sharper* form of the fibration statement than the note cites.**
> "Let R<sup>>0</sup> be the group of positive real numbers under multiplication and consider the suspension X₀ = X̌₀(C)<sub>E</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup>. It is the quotient of X̌₀(C)<sub>E</sub> × R<sup>>0</sup> by the right Q₀<sup>>0</sup>-action given by (P₀, u)q = (P₀q, q<sup>−1</sup>u) = (F<sub>q</sub>(P₀), q<sup>−1</sup>u) for q ∈ Q₀<sup>>0</sup>." … "φ<sup>t</sup>([P₀, u]) = [P₀, ue<sup>t</sup>]." … "Γ<sub>x₀</sub> = C<sub>x₀</sub> ×<sub>Q₀<sup>>0</sup></sub> R<sup>>0</sup> ⊂ X₀." … "(Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup>) ×<sub>p<sup>Z/ deg x₀</sup></sub> R<sup>>0</sup>/N x₀<sup>Z</sup> →∼ Γ<sub>x₀</sub> . **Thus all R<sup>>0</sup>-orbits in Γ<sub>x₀</sub> are circles R<sup>>0</sup>/N x₀<sup>Z</sup> and Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) with fibres the R<sup>>0</sup>-orbits in Γ<sub>x₀</sub>.**"

**(i) p. 39, Theorem 6.1.**
> "**Theorem 6.1.** Let E be an admissible class with E ⊂ E<sub>max</sub>. The following decomposition holds … {x₀ ∈ X₀ | (R<sup>>0</sup>)<sub>x₀</sub> ≠ 1} = ∐<sub>x₀</sub> Γ<sup>E</sup><sub>x₀</sub> . For any point x₀ ∈ Γ<sup>E</sup><sub>x₀</sub> the isotropy group of x₀ is (R<sup>>0</sup>)<sub>x₀</sub> = N x₀<sup>Z</sup>. … Any periodic orbit γ in X₀ is contained in Γ<sup>E</sup><sub>x₀</sub> for a uniquely determined point x₀ of X₀ with finite residue field."

**(j) p. 89, §14 opening — the *local* setup and the reduced monoid.**
> "Let o be a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p. … **In the following we only consider the monoid N₀ generated by p i.e. the F<sub>p</sub> = ( )<sup>p</sup> action.**"

**(k) p. 94, Definition 14.5 and the (172) extension mechanism.**
> "**Definition 14.5.** For any real number 0 < α < 1 define the G-invariant subset Y̌<sub>α</sub> of X̌<sub>c</sub>(o) as follows … Y̌<sub>α</sub> = {(x, y, P̌<sub>y</sub>) ∈ X̌<sub>c</sub>(o) | |P̌<sub>y</sub>(r + s) − P̌<sub>y</sub>(r) − P̌<sub>y</sub>(s)| ≤ α for r, s ∈ Ô<sup>♭</sup><sub>{x̄},y</sub>} . … For α = 1/p we are looking at multiplicative maps P̌<sub>y</sub> which mod p are also additive. Set Y̌ = Y̌<sub>1/p</sub>."
> "Choose an element ω<sub>α</sub> ∈ o with α ≤ |ω<sub>α</sub>| < 1. Then (x, y, P̌<sub>y</sub>) ∈ Y̌<sub>α</sub> gives a ring homomorphism P̌<sub>y</sub> : ZÔ<sup>♭</sup><sub>{x̄},y</sub> → o with P̌<sub>y</sub>(I<sub>y</sub>) ⊂ ω<sub>α</sub>o and hence an induced ring homomorphism W<sub>p</sub>(P̌<sub>y</sub>) : W<sub>p</sub>(Ô<sup>♭</sup>) = lim ZÔ<sup>♭</sup>/I<sub>y</sub><sup>n</sup> → lim o/ω<sub>α</sub><sup>n</sup> = o . (172)"
> "**Proposition 14.7.** For 0 < α < 1 we have F<sub>p</sub>(Y̌<sub>α</sub>) = Y̌<sub>α</sub> and Y̌<sub>α</sub> ⊂ Y̌, and hence Y̌<sub>α</sub> = Y̌ for α ≥ 1/p."

with the proof (p. 95) whose estimate is exactly the one the note cites as (F2):
> "=|(P̌<sub>y</sub>(r + s) − P̌<sub>y</sub>(r) − P̌<sub>y</sub>(s))<sup>p<sup>ν</sup></sup> + pc| for some c ∈ o ≤ max(|P̌<sub>y</sub>(r+s)−P̌<sub>y</sub>(r)−P̌<sub>y</sub>(s)|<sup>p<sup>ν</sup></sup>, |p|) ≤ max(α<sup>p<sup>ν</sup></sup>, 1/p)."

and a second proof of 14.7 which is, in effect, the (⇒) half of Lemma A in Deninger's own hands:
> "All maps in the diagram are ring homomorphisms except for the Teichmüller map [ ]. It follows that the composition Ô<sup>♭</sup> → o → o/p (176) is additive i.e. that P̌<sub>y</sub> ∈ Y̌<sub>1/p</sub>."

**(l) p. 99, Definition 14.12 = (183) and the "I do not know how to transport" Remark.**
> "Y<sup>⋄</sup><sub>α</sub> = {(x, y, P̂<sub>y</sub>) ∈ X<sup>⋄</sup><sub>c</sub>(o) | |P̂<sub>y</sub>(r + s) − P̂<sub>y</sub>(r) − P̂<sub>y</sub>(s)| ≤ α for r, s ∈ Ô<sup>♭</sup><sub>{x̄},y</sub>} ." (183)
> "**I do not know how to transport such conditions to the points of X̌(C), where X is a scheme of finite type over spec Z and C is the complex number field.**"

**(m) pp. 100–101, Propositions 14.13 and 14.14.** 14.13 is the ⋄-analogue of 14.7. 14.14: "Let A be a p-adically complete ring. Then there is a natural bijection between (continuous) multiplicative maps χ : lim<sub>( )<sup>p</sup></sub> A → o with χ(1) = 1, χ(0) = 0 for which the composition χ̄<sup>♭</sup> : A<sup>♭</sup> ≅ lim A → o → o/p (186) is additive and (continuous) ring homomorphisms χ<sup>♭</sup> : A<sup>♭</sup> → o<sup>♭</sup>."

**(n) p. 104, Remark 14.17 — the equivariance the note calls (F5).**
> "In particular G × Aut(o) operates F<sub>p</sub>-equivariantly on X<sup>•</sup>(o) = W<sub>rat</sub>(X)(o) and X̌(o). **Since automorphisms of o are p-adically continuous** we have compatible G × Aut(o)-operations on X<sup>•</sup><sub>c</sub>(o), X̌<sub>c</sub>(o), X<sup>⋄</sup><sub>c</sub>(o) and Y<sup>⋄</sup> in the obvious way."

**(o) pp. 105–106, the §15 hypotheses on o (this is where "algebraically closed" enters, NOT §14).**
> "From now on let o be a p-adically complete rank one valuation ring with (complete) algebraically closed quotient field C of characteristic zero. Let m be its maximal ideal and k its algebraically closed residue field of characteristic p. Then o<sup>♭</sup> is a complete rank one valuation ring of equicharacteristic p with complete algebraically closed quotient field C<sup>♭</sup> of characteristic p, maximal ideal m<sup>♭</sup> = lim<sub>( )<sup>p</sup></sub> m/po and residue field k. **Then k is also a subfield of o<sup>♭</sup> such that k ⊂ o<sup>♭</sup> → k is the identity.** One example is C = C<sub>p</sub> = Q̂̄<sub>p</sub>."

**(p) pp. 113–114, Theorem 15.6, parts 1 and 6, and the closed-point fibre.**
> "**Theorem 15.6.** … 1) There is a natural **G × Aut(o) × ⟨F<sub>p</sub>⟩-equivariant identification** Y<sup>⋄</sup> = Hom<sub>cont</sub>(ô<sup>♭</sup><sub>K</sub>, o<sup>♭</sup>) sending (x, y, P̂<sub>y</sub>) to P̂<sup>♭</sup><sub>y</sub>. Under the projection pr<sub>X</sub> : Y<sup>⋄</sup> → X<sub>top</sub> we have Y<sup>⋄</sup><sub>η</sub> := pr<sub>X</sub><sup>−1</sup>(η) = Hom<sub>cont,inj</sub>(ô<sup>♭</sup><sub>K</sub>, o<sup>♭</sup>) and **Y<sup>⋄</sup><sub>s</sub> := pr<sub>X</sub><sup>−1</sup>(s) = Hom(κ, k).**"
> "… (224) Y<sup>⋄</sup><sub>0s₀</sub> := pr<sub>X₀</sub><sup>−1</sup>(s₀) →∼ ∐<sub>τ₀</sub> {0}/o<sup>×</sup><sub>K₀</sub> = Hom(κ₀, k)."
> "6) **The only periodic (i.e. finite) orbit of the F<sub>p</sub>-action on Y<sup>⋄</sup><sub>0</sub> is Y<sup>⋄</sup><sub>0s₀</sub>. It has order log<sub>p</sub> N(π₀) = r if q = p<sup>r</sup>.**"

and, on p. 113, the identification of the (s,s)-stratum which is exactly Lemma A's setting:
> "For (x, y) = (s, s) the continuous local ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ → o<sup>♭</sup> with P̂<sup>♭</sup><sub>y</sub>(f) ≠ 0 for all 0 ≠ f ∈ lim<sub>( )<sup>p</sup></sub> κ ≅ κ are simply the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>."
and, same page, the identification of the relevant local ring: "The corresponding local rings O<sub>{x̄},η</sub> are o<sub>K</sub> resp. κ = o<sub>K</sub>/m<sub>K</sub> with p-adic completions Ô<sub>{x̄},η</sub> given by ô<sub>K</sub> resp. κ."

**(q) p. 116, Proposition 15.8.**
> "For X₀ = spec Z<sub>p</sub> and o = o<sub>p</sub>, the set Y̌₀ ⊂ Y<sup>⋄</sup><sub>0</sub> consists of the F<sub>p</sub>-fixed point s₀ = (o<sup>♭</sup><sub>p</sub> → F<sub>p</sub> → o<sup>♭</sup><sub>p</sub>)G and the (infinite) F<sub>p</sub><sup>Z</sup>-orbit of η₀ = (o<sup>♭</sup><sub>p</sub> →<sup>id</sup> o<sup>♭</sup><sub>p</sub>)G."

**(r) p. 6 (NOT p. 5), the two intro sentences the note uses.**
> "Incidentally, if we consider points of W<sub>rat</sub>(X) with values in rings without "small multiplicative subgroups" like the complex number field C **this process does not give more points**."
> "The answer is simple, Y<sup>⋄</sup> consists of all the diagrams in X<sup>⋄</sup><sub>c</sub>(o) whose maps are not only multiplicative but mod p also additive."
> "Thus the process of "completion" to pass from X̌₀(o) to X<sup>⋄</sup><sub>0</sub>(o) was necessary to obtain something interesting."

(p. 5 carries "There is a minimal condition E for which our theorems hold but it does not look natural.")

### 1.2 [x-06] Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643
`fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Printed page = PDF page.

**p. 11, the suspension and the F6 sentence.**
> "Set X₀ = (X̌₀(C) × R<sup>>0</sup>)/Q<sup>>0</sup> where Q<sup>>0</sup> acts diagonally. Let t ∈ R act on X₀ by setting φ<sup>t</sup>[P, u] = [P, e<sup>t</sup>u]."
> "In general, the dynamical system (X₀, φ<sup>t</sup>) **has too many periodic orbits, since the N-space W<sub>rat</sub>(X₀)(C) does not know enough about the addition in O<sub>X₀</sub>. In the local p-adic situation below, we know the right modification to make. However in the global case presently we can only impose an "admissible" condition E** on the characters P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> in the description of Theorem 4.1."

**pp. 11–12, Theorem 4.2 — the orbit-length statement §7 consumes.**
> "**Theorem 4.2.** Let X₀ be normal of finite type over spec Z … Then we have {x₀ ∈ X₀<sup>E</sup> | φ<sup>t</sup>(x₀) = x₀ for some t > 0} = ∐<sub>x₀</sub> Γ<sub>x₀</sub>. Here x₀ runs over the closed points of X₀ … **The compact subsets Γ<sub>x₀</sub> ⊂ X₀ consist of periodic orbits of length log N x₀ where N x₀ = |κ(x₀)| … and they are pairwise disjoint. In fact Γ<sub>x₀</sub> is a fibre space over the compact group Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) where p = char κ(x) with fibres the compact orbits in Γ<sub>x₀</sub>.**"
> "… packets of periodic orbits all of which have length log N x₀ i.e. log p if X₀ = spec Z."

**p. 13, Theorem 4.4 and the non-homeomorphism remark** (Road 3): quoted correctly by the note; verified verbatim.

### 1.3 One display that the text layer cannot resolve — read by page render
`pdftotext` drops LaTeX overlines and floats superscripts onto their own line, so the display on [x-03] p. 33 extracts as the meaningless string `Aut(Fp )/Aut(Fp )`. I rendered PDF page 33 at 220 dpi (`pdftoppm -r 220 -x 300 -y 480 -W 1400 -H 260`) and read the image. The display is unambiguously

> **Ẑ<sup>×</sup><sub>(p)</sub> / p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>) / Aut(F̄<sub>p</sub>) ,**

i.e. *automorphisms of the multiplicative group modulo automorphisms of the field*, which is exactly the identity the note's own §4 "Consequence 1" is about. See finding **T-1**.

### 1.4 [D25] Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1
`fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf` (the promotion the note's §10 asked for has happened; the file is on disk). Intro, spanning printed pp. 2–3, read verbatim:
> "The algebra ZA knows nothing about the addition in A. However, the larger G is, the more information the ring W<sub>rat</sub>(A) has about the additive structure of A. It may be interesting to experiment with stronger descent conditions than the Galois descent above to obtain replacements of W<sub>rat</sub>(A) which know even more about the additive structure of A to remedy the defects in the constructions of [KS16] and [Den24]."

### 1.5 [r3s-08] Morishita, arXiv:2508.15971
Text extracted this session but **not consulted for any claim in this report**; the note uses it only in §7 Road 3 through the ledger's W11 flag, which is outside my item and which the 9.3 adjudication (§4 item 4) already ruled must not be cited for topology.

### 1.6 Program-internal documents
`results/c3-r/probe-9.3-adjudication.md` (read in full), `results/c3-r/probe-9.4-note.md` (read in full), `results/corpus-routing.md` standing caveats 1–20 (read; caveat 1 — "OCR is Claude's vision only" — is why §1.3 was done by page render and not by a third-party OCR pass).

---

## 2. The standing picture, re-derived (needed by all five statements)

Throughout, X₀ = Spec Z, X = Spec Z̄ its normalization in Q̄, G = Gal(Q̄/Q), C an algebraically closed field satisfying the conditions before [x-03] Cor. 4.4 (for us C = the complex numbers), ι : µ(Q̄) ↪ µ(C) a fixed injection, p a prime, x ∈ X over x₀ = (p), κ(x) ≅ F̄<sub>p</sub>, and χ<sub>x</sub> = ι ∘ i<sub>x</sub><sup>−1</sup> : κ(x)<sup>×</sup> ↪ C<sup>×</sup>.

**(2.1) χ<sub>x</sub> is an isomorphism onto µ<sup>(p)</sup>(C).** i<sub>x</sub> : µ<sup>(p)</sup>(Q̄) →∼ κ(x)<sup>×</sup> is an isomorphism by (32) (§1.1(d)). ι is injective, hence order-preserving, hence carries µ<sup>(p)</sup>(Q̄) into µ<sup>(p)</sup>(C). Both groups are abstractly ⊕<sub>ℓ≠p</sub> Q<sub>ℓ</sub>/Z<sub>ℓ</sub>. On each ℓ-primary part ι is an injection Q<sub>ℓ</sub>/Z<sub>ℓ</sub> → Q<sub>ℓ</sub>/Z<sub>ℓ</sub>; the image of a divisible group is divisible, and the only nonzero divisible subgroup of Q<sub>ℓ</sub>/Z<sub>ℓ</sub> is the whole of it (its proper subgroups are the finite cyclic ℓ<sup>n</sup>-torsion groups). Hence ι|µ<sup>(p)</sup> is onto µ<sup>(p)</sup>(C), and χ<sub>x</sub> : κ(x)<sup>×</sup> →∼ µ<sup>(p)</sup>(C). ∎ (This is the note's "divisible-image argument"; it is correct.)

**(2.2) Aut(µ<sup>(p)</sup>(C)) = Ẑ<sup>×</sup><sub>(p)</sub>, acting by exponentiation.** End(⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub>) = ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub> = Ẑ<sub>(p)</sub> and the units are Ẑ<sup>×</sup><sub>(p)</sub>; the action is ζ ↦ ζ<sup>u</sup>. Deninger states the same for κ(x)<sup>×</sup> on p. 32 ("The group of automorphisms of the abelian group κ(x)<sup>×</sup> is given by Ẑ<sup>×</sup><sub>(p)</sub>").

**(2.3) The packet, for X₀ = Spec Z, is literally B<sub>p</sub> × S¹.** deg x₀ = 1 and N x₀ = p, so in (39) the group p<sup>Z/deg x₀</sup> is trivial and the fibre product is a direct product. Combining (39) with the §6 display (§1.1(h)):
> Γ<sub>p</sub> ≅ (Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>) × (R<sup>>0</sup>/p<sup>Z</sup>) = B<sub>p</sub> × S¹,
where B<sub>p</sub> := Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>, and the R<sup>>0</sup>-action is on the second factor alone. Consequently:
* each fibre of Γ<sub>p</sub> → B<sub>p</sub> is **exactly one** flow orbit, a circle of flow-time length log p (since φ<sup>t</sup> multiplies u by e<sup>t</sup> and the identification is by p<sup>Z</sup>);
* **distinct base classes lie on distinct orbits, and every orbit has a well-defined base class**;
* the flow acts trivially on B<sub>p</sub>.
This is the input Proposition 1 consumes. It is available *verbatim* on p. 38 for the suspension, one line stronger than the p. 33 statement the note cites (which is about C<sub>x₀</sub> and Q<sup>>0</sup>-orbits and needs the — easy — translation "same Q<sup>>0</sup>-orbit upstairs ⟺ same flow orbit downstairs"). See finding **P-1**.

**(2.4) B<sub>p</sub> is an uncountable profinite group — re-derived, not imported.** p<sup>Ẑ</sup> is by definition the closure of ⟨p⟩ in the compact group Ẑ<sup>×</sup><sub>(p)</sub>, hence closed, hence B<sub>p</sub> is a profinite group. For a finite set T of odd primes ℓ ≠ p, reduction gives a surjection Ẑ<sup>×</sup><sub>(p)</sub> = ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub><sup>×</sup> ↠ ∏<sub>ℓ∈T</sub> (Z/ℓ)<sup>×</sup>/((Z/ℓ)<sup>×</sup>)² ≅ (C₂)<sup>|T|</sup>. The image of the closed subgroup p<sup>Ẑ</sup> is the closed subgroup generated by the image of p, of order ≤ 2. Hence B<sub>p</sub> surjects onto a group of order ≥ 2<sup>|T|−1</sup>, and |T| is unbounded, so B<sub>p</sub> is infinite. An infinite profinite group is uncountable: it is compact Hausdorff, hence a Baire space; a countable Baire space has an isolated point; a topological group with an isolated point is discrete; a compact discrete group is finite — contradiction. ∎ (Agrees with the adjudication §2; independently re-derived here.)

**(2.5) The (34)-inclusion.** Frobenius acts on κ(x)<sup>×</sup> ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> by y ↦ y<sup>p</sup>, i.e. by the unit p ∈ Ẑ<sup>×</sup><sub>(p)</sub>; Deninger records the map Gal(κ(x)/κ(x₀)) → Aut(κ(x)<sup>×</sup>) as an **inclusion** (34), so Aut<sub>ring</sub>(F̄<sub>p</sub>) = Ẑ ≅ p<sup>Ẑ</sup> ⊆ Ẑ<sup>×</sup><sub>(p)</sub> = Aut<sub>group</sub>(F̄<sub>p</sub><sup>×</sup>) and B<sub>p</sub> = coker. This is the identity the p. 33 display states (§1.3) and is the backbone of the note's §4 Consequence 1. **Verified as a source statement**; I did not re-prove the injectivity of Ẑ → Ẑ<sup>×</sup><sub>(p)</sub> and do not need it (nothing below uses more than surjectivity of Ẑ<sup>×</sup><sub>(p)</sub> ↠ B<sub>p</sub>).

---

## 3. LEMMA A — verdict **PASS-WITH-REPAIRS** (2 MAJOR, 2 MINOR)

### 3.1 What the note states

> "Let o be as in §2 (residue field k algebraically closed of char p), κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ<sup>×</sup> is a group homomorphism into o (values automatically in µ<sup>(p)</sup>(o), the prime-to-p roots of unity, since κ<sup>×</sup> is prime-to-p torsion). Then
> |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ **iff** P = [·]∘τ for a unique field embedding τ: κ ↪ k, where [·] is the Teichmüller section of the reduction µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k)."

### 3.2 FINDING A-1 (MAJOR) — the hypothesis "κ an algebraically closed field of characteristic p" is wrong; the statement is only well-posed for κ ≅ F̄<sub>p</sub>

**The defect.** The parenthetical "values automatically in µ<sup>(p)</sup>(o) … since κ<sup>×</sup> is prime-to-p torsion" is **false** for a general algebraically closed field of characteristic p. κ<sup>×</sup> is a torsion group precisely when κ is algebraic over F<sub>p</sub>, i.e. (κ being algebraically closed) when κ = F̄<sub>p</sub>. **Counterexample to the parenthetical:** κ = the algebraic closure of F<sub>p</sub>(t). Then t ∈ κ<sup>×</sup> has infinite order, and for a multiplicative P : κ → o the value P(t) is a unit of o of infinite order in general — it need not be a root of unity at all. (Concretely: o = o<sub>C<sub>p</sub></sub>, κ = the algebraic closure of F<sub>p</sub>((t))<sup>perf</sup>'s residue-level analogue; split κ<sup>×</sup> ≅ µ<sup>(p)</sup>(κ) × V with V a Q-vector space and send V to any subgroup of 1 + m by a Q-linear map. Nothing forces torsion values.)

**Consequence for the conclusion.** The right-hand side "P = [·]∘τ for a field embedding τ : κ ↪ k, where [·] is the Teichmüller section of µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k)" does not even **typecheck** unless τ(κ) ⊆ µ<sup>(p)</sup>(k) ∪ {0}, i.e. unless κ<sup>×</sup> is torsion, i.e. unless κ = F̄<sub>p</sub>. So the biconditional as printed is not a well-formed statement in the generality it claims. (The correct statement in that generality is the tilt statement, which is [x-03] Prop. 14.14 + Thm 15.6(1): mod-p-additive multiplicative χ : A → o correspond to ring maps A<sup>♭</sup> → o<sup>♭</sup>, and the section is the sharp map o<sup>♭</sup> → o, not a section of µ<sup>(p)</sup>(o) ≅ µ<sup>(p)</sup>(k).)

**Does it matter?** Not for anything the note does. Every application of Lemma A in §4 and §5 is at a char-p packet point of X₀ = Spec Z, where κ(x) ≅ F̄<sub>p</sub>. The repair is a one-clause hypothesis restriction (§10, R-A1). The finding is nevertheless MAJOR, not MINOR: a printed lemma carries a false justification and an ill-posed conclusion, and standing order 7 forbids softening that because the case actually used is fine.

### 3.3 FINDING A-2 (MAJOR) — the converse's justification is not valid under the note's own hypotheses (the statement is true; a self-contained proof is supplied)

**What the note offers.** "(⇐) [a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring), so the defect of [·]∘τ has absolute value ≤ |p|."

Three separate problems, in increasing order of seriousness.

1. **"first ghost … coordinates agree" is the wrong invariant.** For a ring A of characteristic p the ghost components of a Witt vector are w<sub>n</sub>(x) = x₀<sup>p<sup>n</sup></sup> (every other term carries a factor p = 0), so the ghost map W(k) → k<sup>N</sup> is very far from injective and carries no information here. What is true, and what the argument needs, is the statement about the **0-th Witt component**: the map W(A) → A, x ↦ x₀, is a ring homomorphism, so [a] + [b] − [a+b] has 0-th Witt component (a+b) − (a+b) = 0, i.e. lies in ker(x ↦ x₀) = V W(k). Wording, but it is the wording that makes the step checkable.
2. **"V F = p on Witt vectors of a perfect ring"** is a correct standard fact but I could not read it on disk in this corpus; by standing order 5 I record it as **[RU]** and do not let the argument rest on it.
3. **"W(k) ⊆ o" is not established, and cannot be established from the hypotheses the note states.** The note's §2 setup gives o a p-adically complete rank-1 valuation ring with residue field k = o/**m**. In general **m** ⊋ p·o (for o = o<sub>C<sub>p</sub></sub>, p·o = {|x| ≤ |p|} is a proper subset of **m** = {|x| < 1}), so the classical statement "A p-adically complete with A/pA perfect of char p admits a unique W(A/pA) → A" does not apply, and no multiplicative section k → o has been produced. It *is* recoverable — [x-03] p. 106 supplies k ⊂ o<sup>♭</sup>, and W(k) ⊆ W(o<sup>♭</sup>) →<sup>θ</sup> o is injective on W(k) because W(k) is a DVR with uniformizer p and θ(p) = p ≠ 0 — but that recovery uses Fontaine's θ and the perfectoid structure, i.e. exactly the machinery Lemma A is supposed to be an *elementary substitute* for, and the note invokes none of it.

**FILL (this is the repair; it is fully self-contained and uses only the rank-1 valuation and integer binomial coefficients).**

> **Claim.** Let o be a rank-1 valuation ring with residue characteristic p, m its maximal ideal, and let ζ, ξ ∈ µ<sup>(p)</sup>(o) ∪ {0} with reductions a, b ∈ F̄<sub>p</sub> ⊆ k. Let w ∈ µ<sup>(p)</sup>(o) ∪ {0} be the unique element with reduction a + b (unique by (3.4.1) below). Then |ζ + ξ − w| ≤ |p|.
>
> *Proof.* If a or b is 0 the corresponding root of unity is 0 and the statement is trivial (defect 0). If a + b = 0 with p odd, then b = −a, and since −1 ∈ µ<sup>(p)</sup>(o) has reduction −1 we get ξ = −ζ, so ζ + ξ − 0 = 0. If a + b = 0 with p = 2 then b = a, ξ = ζ, and the defect is 2ζ of absolute value |2| = |p|. So assume a, b, a+b all nonzero.
>
> Let m = lcm(ord ζ, ord ξ, ord w), prime to p, and choose f ≥ 1 with q := p<sup>f</sup> ≡ 1 (mod m). Then ζ<sup>q</sup> = ζ, ξ<sup>q</sup> = ξ, w<sup>q</sup> = w.
>
> Since p | C(p, i) for 0 < i < p, we have (u+v)<sup>p</sup> ≡ u<sup>p</sup> + v<sup>p</sup> (mod p·o) for all u, v ∈ o; and u ≡ v (mod p·o) ⟹ u<sup>p</sup> ≡ v<sup>p</sup> (mod p·o). Iterating f times, (ζ + ξ)<sup>q</sup> ≡ ζ<sup>q</sup> + ξ<sup>q</sup> = ζ + ξ (mod p·o).
>
> Put x := (ζ + ξ) − w. Because reduction mod **m** is a ring map and (ζ+ξ) and w have the same reduction a+b, we have x ∈ **m**, i.e. |x| < 1. Since p | C(q, i) for 0 < i < q (q = p<sup>f</sup>), expanding (w + x)<sup>q</sup> gives (ζ+ξ)<sup>q</sup> ≡ w<sup>q</sup> + x<sup>q</sup> = w + x<sup>q</sup> (mod p·o). Comparing with the previous display, ζ + ξ ≡ w + x<sup>q</sup> (mod p·o), i.e. **x ≡ x<sup>q</sup> (mod p·o)**.
>
> Iterating (again using u ≡ v ⟹ u<sup>q</sup> ≡ v<sup>q</sup> mod p·o), x ≡ x<sup>q<sup>n</sup></sup> (mod p·o) for every n ≥ 1. Because o has rank 1 and |x| < 1, |x<sup>q<sup>n</sup></sup>| = |x|<sup>q<sup>n</sup></sup> → 0, so |x<sup>q<sup>n</sup></sup>| < |p| for n large. The ultrametric inequality then gives |x| = |(x − x<sup>q<sup>n</sup></sup>) + x<sup>q<sup>n</sup></sup>| ≤ max(|p|, |x<sup>q<sup>n</sup></sup>|) = |p|. ∎

No Witt vectors, no W(k) ⊆ o, no p-adic completeness, no perfectness of k, no [RU]. It also yields the sharp constant: the p = 2, a + b = 0 case attains |p| exactly, so |p| cannot be improved.

**BREAK attempt (failed, as it should).** Can the converse fail for some rank-1 valuation ring with residue char p? No: the proof above uses only (i) integers prime to p are units, (ii) the ultrametric inequality with |x| < 1 ⟹ |x|<sup>q<sup>n</sup></sup> → 0, both automatic. Can the *biconditional* fail because some non-injective character is mod-p additive? No: if the defect is ≤ |p| then P mod **m** is a ring homomorphism from a field sending 1 ↦ 1, hence injective, hence P itself is injective (P(r) = 1 for r ≠ 1 would force P̄(r) = P̄(1)); so characters χ<sub>x</sub>·(a, ν) with prime-to-p part of ν greater than 1 are never mod-p additive, consistently with the classification below.

### 3.4 Lemma A re-derived in full (for κ ≅ F̄<sub>p</sub>, k algebraically closed of char p, o a p-adically complete rank-1 valuation ring with residue field k)

**(3.4.1) Reduction is an isomorphism µ<sup>(p)</sup>(o) →∼ µ<sup>(p)</sup>(k).**
*Injective.* Let ζ ∈ µ<sup>(p)</sup>(o) with ζ ≡ 1 mod **m**, say ζ<sup>d</sup> = 1 with (d, p) = 1. Write ζ = 1 + y, y ∈ **m**. Then 0 = ζ<sup>d</sup> − 1 = y·(ζ<sup>d−1</sup> + … + 1) and ζ<sup>d−1</sup> + … + 1 = d + y′ with y′ ∈ **m**. Since (d,p) = 1, d is a unit of o (its reduction is d ≠ 0 in k, char k = p), hence d + y′ is a unit; o is a domain, so y = 0.
*Surjective.* µ<sup>(p)</sup>(o) = µ<sup>(p)</sup>(C) (any root of unity in C has |ζ| = 1, hence lies in o<sup>×</sup>) ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> since C is algebraically closed of characteristic 0; and µ<sup>(p)</sup>(k) ≅ ⊕<sub>ℓ≠p</sub>Q<sub>ℓ</sub>/Z<sub>ℓ</sub> since k is algebraically closed of characteristic p. An injection between two such groups has divisible ℓ-primary image, hence (as in (2.1)) full image. ∎
Write [·] : µ<sup>(p)</sup>(k) ∪ {0} → µ<sup>(p)</sup>(o) ∪ {0} for the inverse, extended by [0] = 0. Note µ<sup>(p)</sup>(k) = F̄<sub>p</sub><sup>×</sup> (a prime-to-p root of unity in k is algebraic over F<sub>p</sub>), so [·] is defined on all of F̄<sub>p</sub> ⊆ k.

**(3.4.2) (⇒).** Suppose |P(r+s) − P(r) − P(s)| ≤ |p| for all r, s ∈ κ. In a valuation ring |y| ≤ |p| ⟺ y/p ∈ o ⟺ y ∈ p·o, and p ∈ **m**; so the defect lies in **m**. Hence τ := (P mod **m**) : κ → k is additive; it is multiplicative and unital because P is; so τ is a ring homomorphism, and injective because κ is a field with τ(1) = 1 ≠ 0. For r ∈ κ<sup>×</sup> = µ<sup>(p)</sup>(κ) (here κ = F̄<sub>p</sub> — this is where A-1 bites in the general case) the value P(r) satisfies P(r)<sup>d</sup> = P(r<sup>d</sup>) = 1 with d = ord(r) prime to p, so P(r) ∈ µ<sup>(p)</sup>(o); and τ(r) ∈ µ<sup>(p)</sup>(k) has the same order. Both P(r) and [τ(r)] lie in µ<sup>(p)</sup>(o) with reduction τ(r), so by (3.4.1) they are equal. With P(0) = 0 = [τ(0)] this gives P = [·]∘τ. Uniqueness of τ is immediate (τ = P mod **m**). ∎

**(3.4.3) (⇐).** Immediate from the Claim in §3.3, applied with ζ = [τ(r)], ξ = [τ(s)], w = [τ(r)+τ(s)] = [τ(r+s)] (τ is additive). ∎

**(3.4.4) Independent confirmation against the source.** [x-03] p. 113 identifies the (x,y) = (s,s) stratum of Y<sup>⋄</sup>: the local ring is O<sub>{s},s</sub> = κ with Ô = κ and Ô<sup>♭</sup> ≅ κ, so Deninger's defect condition (183) is *literally* a condition on r, s ∈ κ — the same test Lemma A poses — and he computes the answer to be "simply the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>", i.e. Thm 15.6(1)'s **Y<sup>⋄</sup><sub>s</sub> = Hom(κ, k)** (p. 114). Lemma A says the same thing on the o-side, the two being matched by the multiplicative section. **So Lemma A's content is confirmed, at referee grade, against Theorem 15.6 itself**, and the note's "consistency check" paragraph is right. (The threshold |p| = 1/p is also right: Def. 14.5 sets Y̌ = Y̌<sub>1/p</sub>, and Prop. 14.7 shows Y̌<sub>α</sub> = Y̌<sub>1/p</sub> for every α ≥ 1/p, so |p| is the canonical constant, not a choice.)

### 3.5 The two Consequences drawn from Lemma A — both check

**Consequence 1 (why the local principle succeeds).** The isomorphisms κ(x)<sup>×</sup> → µ<sup>(p)</sup>(o) form a torsor under Aut<sub>group</sub>(κ(x)<sup>×</sup>) = Ẑ<sup>×</sup><sub>(p)</sub> (2.2). By Lemma A the mod-p-additive ones are exactly {[·]∘τ : τ ∈ Hom(F̄<sub>p</sub>, k)}, and Hom(F̄<sub>p</sub>, k) is a torsor under Aut<sub>ring</sub>(F̄<sub>p</sub>) = Ẑ (every embedding has the same image, the algebraic closure of F<sub>p</sub> in k). Under (34)/(2.5) the image of Aut<sub>ring</sub> in Aut<sub>group</sub> is p<sup>Ẑ</sup>. Hence mod-p additivity cuts a Ẑ<sup>×</sup><sub>(p)</sub>-torsor down to a p<sup>Ẑ</sup>-torsor, and the residue is exactly B<sub>p</sub> = coker(Aut<sub>ring</sub> ↪ Aut<sub>group</sub>). **Verified.** This is precisely the group the p. 33 display names (§1.3) — and, as finding T-1 records, the note's own transcription of that display obscures the point it is making.

**Consequence 2 (the transport reading, = D3) — verified, with one precision (finding A-4).** Fix an isomorphism j : µ<sup>(p)</sup>(C) → µ<sup>(p)</sup>(o<sub>C<sub>p</sub></sub>). By (2.1) and (3.4.1), θ := [·]<sup>−1</sup> ∘ j ∘ χ<sub>x</sub> : κ(x)<sup>×</sup> → F̄<sub>p</sub><sup>×</sup> is a group isomorphism. For b ∈ Ẑ<sup>×</sup><sub>(p)</sub>, j ∘ (χ<sub>x</sub> ∘ ( )<sup>b</sup>) = [·] ∘ (θ ∘ ( )<sup>b</sup>), and by Lemma A this is mod-p additive **iff** θ ∘ ( )<sup>b</sup> is the restriction to κ(x)<sup>×</sup> of a field isomorphism κ(x) → F̄<sub>p</sub>. The field isomorphisms form a p<sup>Ẑ</sup>-sub-torsor of the Ẑ<sup>×</sup><sub>(p)</sub>-torsor of group isomorphisms, so {b : mod-p additive} is a single coset b₀·p<sup>Ẑ</sup>, i.e. **exactly one base class in B<sub>p</sub>**; and characters with prime-to-p part of ν greater than 1 are excluded (§3.3, BREAK paragraph). Varying j over its Ẑ<sup>×</sup><sub>(p)</sub>-torsor translates b₀ and sweeps all of B<sub>p</sub>. **All of this checks.**

**FINDING A-4 (MINOR).** The note writes that the transported class "**is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀". Strictly it is not: the transported condition is not admissible in the sense of Def. 4.1 (it fails the ν-closure — that is exactly §3's freshman's-dream point), whereas E(a₀) is by construction an admissible class. The correct statement is that the transported condition *selects the same single base class* as E(a₀), so that its admissible closure is E(a₀) and D3's conclusion is unaffected. Replacement text in §10 (R-A4).

**FINDING A-3 (MINOR).** The note's §2 attributes its coefficient setup ("o = a p-adically complete rank-1 valuation ring with **algebraically closed** quotient field C of characteristic 0 and residue field k of characteristic p") to "[x-03] §§13–14, pp. 78, 89". On p. 89 Deninger assumes only "a p-adically complete rank one valuation ring with quotient field C, maximal ideal m and residue field k of characteristic p" — no algebraic closedness of C, none of k. The algebraically-closed hypotheses (both of them) are introduced at the start of the §15 discussion, pp. 105–106. Since Lemma A's proof *uses* k algebraically closed (surjectivity in (3.4.1)) and C algebraically closed (µ<sup>(p)</sup>(C) full), the citation must point at pp. 105–106.

---

## 4. LEMMA B — verdict **PASS** (strengthened; 0 MAJOR, 2 MINOR)

### 4.1 The statement and its re-derivation

> "**Lemma B.** For X₀ = Spec Z, at every point of every packet (any prime p, any character P in any class E ⊆ E<sub>tors</sub>), the test r = s = 1 gives |P(1̄+1̄) − P(1̄) − P(1̄)| = |P(2̄) − 2| ≥ 1 … Hence the class 'archimedean defect ≤ ε at char-p points' is **empty on the periodic locus for every ε < 1**."

**Re-derivation.** Let x ∈ X = Spec Z̄ lie over (p), so κ(x) ≅ F̄<sub>p</sub>, and let P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> be any character, P its extension by zero to κ(x) → C. Take r = s = 1̄.

*Case p = 2.* 1̄ + 1̄ = 0 in F̄₂, so P(0) = 0 and the defect is |0 − 1 − 1| = 2 ≥ 1.

*Case p odd.* 2̄ ∈ F<sub>p</sub><sup>×</sup> ⊆ κ(x)<sup>×</sup> has finite multiplicative order d | p − 1, so P(2̄)<sup>d</sup> = P(2̄<sup>d</sup>) = P(1̄) = 1 and P(2̄) ∈ µ(C) has |P(2̄)| = 1. Hence, in the complex absolute value,
> |P(2̄) − 2| ≥ |2| − |P(2̄)| = 2 − 1 = 1,
with equality exactly when P(2̄) = 1. ∎

So no character at a char-p point can have archimedean additivity defect < 1 at the single pair (1̄, 1̄), let alone uniformly. Since by Thm 6.1 / [x-06] Thm 4.2 the periodic locus of X₀ is ∐<sub>x₀</sub> Γ<sup>E</sup><sub>x₀</sub> with κ(x) = F̄<sub>p</sub> at every such point, **the ε-threshold class contains no periodic point at all, for every ε < 1.** ✔

**The (F3) half also checks.** [x-03] (172) (p. 94, quoted in §1.1(k)) needs ω<sub>α</sub> ∈ o with α ≤ |ω<sub>α</sub>| < 1 in order to define W<sub>p</sub>(P̌<sub>y</sub>) : lim ZÔ<sup>♭</sup>/I<sup>n</sup> → lim o/ω<sub>α</sub><sup>n</sup> = o. With a defect bounded **below** by 1 no such ω exists and the I-adic evaluation does not converge; there is no A<sub>inf</sub>-analogue action. ✔ The note's page anchor (p. 94) is correct.

### 4.2 Is "the periodic locus" the right locus? — the charter's explicit press point

**Answer: it is the right locus for a general arithmetic X₀, and for X₀ = Spec Z the lemma in fact holds on a strictly larger locus. The note's stated reason is one notch weaker than the reason that is actually available.**

The note justifies |P(2̄)| = 1 by "κ(x)<sup>×</sup> is torsion". That is true at packet points (κ(x) = F̄<sub>p</sub>) but is not what the argument needs. What the argument needs is only that **2̄ ∈ F<sub>p</sub><sup>×</sup> is torsion**, which holds at *every* point x of *any* arithmetic X with char κ(x) = p, whether or not κ(x)<sup>×</sup> is torsion. Hence:

> **Lemma B′ (strengthening, referee-derived).** Let X₀ be integral normal of finite type over Spec Z and x ∈ X with char κ(x) = p > 0. Then for every character P<sup>×</sup> : κ(x)<sup>×</sup> → C<sup>×</sup> (no class hypothesis at all), |P(1̄+1̄) − P(1̄) − P(1̄)| ≥ 1. Consequently the ε-threshold class is empty on the whole positive-characteristic locus X̌(C)<sub>p</sub>, ε < 1 — not merely on its periodic part.

Two further robustness checks, both of which the charter's phrasing invites:

1. **It survives the "wrong-stage" objection.** A packet point of X₀ is a class [P₀, u] with P₀ ∈ C<sub>x₀</sub>, and C<sub>x₀</sub> = ⋃<sub>ν</sub> F<sub>ν</sub><sup>−1</sup>pr₀<sup>−1</sup>(x₀): the point is a *Frobenius-inverted* character. But the object a class E constrains is the character P<sup>×</sup> at the ν = 1 stage (Def. 4.1 is a condition on χ : κ<sup>×</sup> → C<sup>×</sup>), and Lemma B is applied there. ✔
2. **It survives the "tilt-formulation" objection.** One might try to pose the defect on a projective limit rather than on κ(x), as Deninger does locally on Ô<sup>♭</sup>. For the p-tower, lim<sub>( )<sup>p</sup></sub> κ(x) ≅ κ(x) (Frobenius is bijective on a perfect field), so 2̄ still lies in the domain and the test is unchanged. ✔ (For the full monoid N₀ = N the projective limit is not even a ring — see §8.1 — so the question does not arise.)

### 4.3 FINDING B-1 (MINOR) — the inference about Deninger's intent is not supported

The note closes §6 with: "Deninger's own asserted translation (p. 29) cannot live here in nonempty form as a threshold condition, so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it. [Judgment-grade reading, flagged.]"

The premise is too strong. The threshold class **is** nonempty as a class of characters in Deninger's sense, and it is non-N-invariant, exactly as p. 29 says:

* *Nonempty.* Def. 4.1 ranges over characters χ : κ<sup>×</sup> → C<sup>×</sup> for algebraically closed κ of **any** characteristic. If κ ⊆ C is an algebraically closed subfield of characteristic 0 and χ is the inclusion, the additivity defect is identically **0**. (Tors) holds (ker χ = 1). So the ε-threshold class is nonempty for every ε ≥ 0.
* *Not N-invariant.* For that same χ, χ ∘ ( )<sup>ν</sup> has defect |(r+s)<sup>ν</sup> − r<sup>ν</sup> − s<sup>ν</sup>|, unbounded on κ. So χ ∈ E while χ<sub>ν</sub> ∉ E: Def. 4.1's biconditional fails, which is precisely Deninger's verdict.

So the threshold reading reproduces Deninger's remark exactly, and the note's ground for preferring the transport reading evaporates. **What survives, and it is the whole point of D2, is stronger and cleaner than the note claims:** the threshold class is nonempty but lives *entirely over characteristic-zero points*, so the selected system has **no periodic orbits whatsoever** — it does not merely fail to cut the packet to one orbit, it cuts it to nothing, and Deninger's own N-invariance objection is then not even the binding one. Replacement text in §10 (R-B1). This is a MINOR finding (the note flags the sentence judgment-grade and D2 does not depend on it), but the corrected reading is a better result than the one printed.

### 4.4 FINDING B-2 (MINOR) — the parenthetical justification should be the sharp one

"since P(2̄) is a root of unity or 0 (κ(x)<sup>×</sup> is torsion; 0 occurs iff p = 2)" → the operative fact is that 2̄ ∈ F<sub>p</sub><sup>×</sup> is torsion. Replacement text in §10 (R-B2); it converts Lemma B into Lemma B′ at zero cost.

### 4.5 BREAK attempts on Lemma B (all failed)

* *Can some other pair (r,s) rescue a small defect?* Yes for individual pairs — e.g. with P(r) = 1, P(s) = ω a primitive cube root of unity and P(r+s) = −ω², the defect is 0 — which is exactly why a **universally quantified** threshold is needed and why r = s = 1 is the right witness. The note picked the correct witness.
* *Can P(2̄) fail to be a root of unity?* Only if 2̄ had infinite order in κ(x)<sup>×</sup>, impossible in characteristic p.
* *Can one weaken the condition to "defect ≤ ε on the maximal ideal only", as in the local case where topologically nilpotent elements abound?* At a char-p point of Spec Z̄ the relevant evaluation is on Z ⊆ Z̄ (through O<sub>{x̄},y</sub>), and 1 and 2 are always in the domain, so the witness survives. No escape found.

---

## 5. LEMMA C — verdict **PASS** (0 MAJOR, 2 MINOR)

### 5.1 Statement

> "**Lemma C (derived; Steinitz).** The restriction map Aut(C) → Aut(µ(C)) = Ẑ<sup>×</sup> is surjective for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree). *Derivation:* u ∈ Ẑ<sup>×</sup> defines an automorphism of Q(µ<sub>∞</sub>) (cyclotomic theory); extend to Q̄ (isomorphism extension), then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield (Steinitz; uses AC). ∎"

### 5.2 Re-derivation, one step at a time (as the charter demands)

Let C be algebraically closed of characteristic 0.

**Step 0 (the target group).** Q ⊆ C, so Q̄ ⊆ C and µ(C) = µ(Q̄) ≅ Q/Z. Aut(Q/Z) = End(Q/Z)<sup>×</sup> = Ẑ<sup>×</sup>. Any σ ∈ Aut(C) carries roots of unity to roots of unity of the same order, so restriction Aut(C) → Aut(µ(C)) = Ẑ<sup>×</sup> is a well-defined group homomorphism. ✔

**Step 1 (cyclotomic).** The cyclotomic character Gal(Q(µ<sub>∞</sub>)/Q) →∼ Ẑ<sup>×</sup> is an isomorphism, so for u ∈ Ẑ<sup>×</sup> there is σ<sub>u</sub> ∈ Aut(Q(µ<sub>∞</sub>)) with σ<sub>u</sub>(ζ) = ζ<sup>u</sup> for all ζ ∈ µ(Q̄). ✔ (Choice-free: this is the Kronecker–Weber/irreducibility-of-cyclotomic-polynomials statement.)

**Step 2 (to Q̄).** σ<sub>u</sub> : Q(µ<sub>∞</sub>) → Q(µ<sub>∞</sub>) ⊆ Q̄ is an embedding of a field into an algebraically closed field, and Q̄ is algebraic over Q(µ<sub>∞</sub>); by the isomorphism-extension theorem it extends to an embedding τ : Q̄ → Q̄. τ(Q̄) is an algebraically closed subfield containing Q and Q̄ is algebraic over Q, so τ(Q̄) = Q̄ and τ ∈ Aut(Q̄). ✔ (**Uses Zorn's lemma** — the extension theorem is a maximal-extension argument.)

**Step 3 (across a transcendence basis).** Let B be a transcendence basis of C over Q̄ (**Zorn**; B may be empty). Q̄(B) is purely transcendental over Q̄, so τ together with id<sub>B</sub> defines a field automorphism τ′ of Q̄(B): well-defined because B is algebraically independent over Q̄, hence Q̄(B) is the fraction field of a polynomial ring on B and any automorphism of Q̄ extends coefficient-wise. ✔

**Step 4 (to C).** C is algebraically closed and algebraic over Q̄(B) (definition of transcendence basis), i.e. C is an algebraic closure of Q̄(B). Apply the isomorphism-extension theorem again (**Zorn**) to τ′ : Q̄(B) → Q̄(B) ⊆ C: it extends to an embedding σ : C → C, and as in Step 2 σ(C) is an algebraically closed subfield over which C is algebraic, so σ ∈ Aut(C). ✔

**Conclusion.** σ|<sub>µ(C)</sub> = σ<sub>u</sub>|<sub>µ</sub> = ( )<sup>u</sup>. Surjectivity established. Composing with the projection Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub> (which is surjective, being a coordinate projection of ∏<sub>ℓ</sub>Z<sub>ℓ</sub><sup>×</sup> onto ∏<sub>ℓ≠p</sub>Z<sub>ℓ</sub><sup>×</sup>), **every u ∈ Ẑ<sup>×</sup><sub>(p)</sub> is realized as u<sub>σ</sub> for some σ ∈ Aut(C)** — which is the form Lemma D and Proposition 1 actually use. ✔

**Exact use of choice.** AC enters exactly three times: existence of a transcendence basis (Step 3) and the two isomorphism-extension applications (Steps 2 and 4). Nothing else in Lemmas C, D or Proposition 1 uses choice. The σ produced for u ∉ {±1} is necessarily a **wild** (discontinuous) automorphism: a continuous automorphism of C fixes Q pointwise, hence R pointwise by density and continuity, hence is id or complex conjugation, whose u is +1 or −1. The note states this correctly in its scope note (b). ✔

### 5.3 FINDING C-1 (MINOR) — an unnecessary and misleading hypothesis

The parenthetical "(or any algebraically closed field of characteristic 0 containing Q̄ with **infinite transcendence degree**)" is not needed: Steps 0–4 above work for *every* algebraically closed field of characteristic 0, including Q̄ itself (B = ∅). Stating a superfluous hypothesis invites a later reader to think the lemma is unavailable for the algebraically closed C that Deninger's construction actually admits ([x-03] p. 28 allows e.g. C = Q̂̄<sub>p</sub> or C = F<sub>p</sub>((t))<sup>-</sup>-type fields, and p. 31 takes "an algebraically closed field which satisfies the conditions before Corollary 4.4"). Replacement text in §10 (R-C1).

### 5.4 FINDING C-2 (MINOR) — a garbled clause

"then to C along a transcendence basis of C over Q̄ and to the algebraic closure C of the lifted subfield" — "the algebraic closure C of the lifted subfield" is not parsable as written (C is the ambient field, not something one takes the algebraic closure of). Replacement text in §10 (R-C2) states Steps 3 and 4 cleanly.

### 5.5 BREAK attempt (failed)

Is there any obstruction to realizing a given u ∈ Ẑ<sup>×</sup>? The only conceivable one would be a constraint imposed by C's transcendental part; Step 3 shows there is none, because the automorphism can be taken to fix a transcendence basis pointwise. In particular the constructed σ can even be chosen to fix a prescribed transcendence basis, which is more than the lemma claims.

---

## 6. LEMMA D — verdict **PASS** (0 MAJOR, 3 MINOR)

Throughout σ ∈ Aut(C) acts on X<sup>•</sup>(C) by **post**-composition, (x, P<sup>×</sup>) ↦ (x, σ ∘ P<sup>×</sup>).

### 6.1 D(i): commutation — re-derived

* **Well-defined.** σ|<sub>C<sup>×</sup></sub> is a group automorphism of C<sup>×</sup>, so σ ∘ P<sup>×</sup> is again a character κ(x)<sup>×</sup> → C<sup>×</sup>. ✔
* **With G.** By [x-06] Thm 4.1 (p. 11, quoted §1.2), σ<sub>G</sub> ∈ G acts by (x, P<sup>×</sup>)<sup>σ<sub>G</sub></sup> = (x<sup>σ<sub>G</sub></sup>, P<sup>×</sup> ∘ σ<sub>G</sub>): **pre**-composition (plus a move of the base point). Post- and pre-composition commute: σ ∘ (P<sup>×</sup> ∘ σ<sub>G</sub>) = (σ ∘ P<sup>×</sup>) ∘ σ<sub>G</sub>. ✔
* **With F<sub>ν</sub>.** F<sub>ν</sub>(x, P<sup>×</sup>) = (x, P<sup>×</sup> ∘ ( )<sup>ν</sup>), again pre-composition. ✔ Hence σ passes to X̌(C) = colim<sub>N₀</sub> and commutes with the Q<sup>>0</sup>-action, and descends to X̌₀(C) = X̌(C)/G. ✔
* **On the suspension.** With the [x-03] p. 38 convention (P₀, u)q = (F<sub>q</sub>(P₀), q<sup>−1</sup>u), define σ[P₀, u] := [σP₀, u]. Well-defined because σF<sub>q</sub> = F<sub>q</sub>σ. It commutes with φ<sup>t</sup>[P₀,u] = [P₀, ue<sup>t</sup>] since it does not touch the second coordinate. ✔ **Note that only algebra is used: no continuity of σ is needed anywhere, and none is available (see D-1).**

### 6.2 D(ii): class stability — **one class at a time**, including (Image) for E<sub>max</sub> (the note's own press point)

Two elementary facts do all the work.
> **(K)** ker(σ ∘ χ) = ker χ, because σ|<sub>C<sup>×</sup></sub> is injective; likewise ker((σ∘χ)|<sub>µ(κ)</sub>) = ker(χ|<sub>µ(κ)</sub>).
> **(I)** σ|<sub>C<sup>×</sup></sub> restricts to a group isomorphism χ(κ<sup>×</sup>) →∼ (σ∘χ)(κ<sup>×</sup>). Hence the image is torsion for σ∘χ iff it is for χ, and (image) ⊗ Q ≠ 0 for one iff for the other.

| class | defining condition ([x-03] pp. 27–29, verbatim §1.1(a),(b)) | preserved? | why |
|---|---|---|---|
| **E<sub>tors</sub>** | (Tors): ker(χ)<sub>tors</sub> = ker(χ|<sub>µ(κ)</sub>) finite and of order in N₀ | **yes, biconditionally** | (K): the group in question is literally unchanged |
| **E<sub>f</sub>** | (Tors) and ker χ finite | **yes** | (K) |
| **E<sub>fg</sub>** | (Tors) and ker χ finitely generated | **yes** | (K) |
| **E<sub>fd</sub>** | (Tors) and ker χ ⊗ Q finite dimensional | **yes** | (K) |
| **E<sub>fd0</sub>** | (Tors) and (ker χ|<sub>κ(x₀)<sup>×</sup></sub>) ⊗ Q finite dimensional | **yes** | (K), applied to the restriction to κ(x₀)<sup>×</sup>, which is also unchanged; the point x₀ = π(x) is untouched by σ |
| **E<sub>max</sub>** | (Tors) and **(Image)**: *only if char κ > 0*; if χ(κ<sup>×</sup>) is torsion then κ<sup>×</sup> is torsion, equivalently κ<sup>×</sup> ⊗ Q ≠ 0 ⟹ χ(κ<sup>×</sup>) ⊗ Q ≠ 0 | **yes, biconditionally** | (I) for the hypothesis/consequent involving χ; the other side of the implication ("κ<sup>×</sup> is torsion", "κ<sup>×</sup> ⊗ Q ≠ 0") **does not mention χ at all** and is therefore untouched. Explicitly: if (Image) holds for χ and (σ∘χ)(κ<sup>×</sup>) is torsion, then by (I) χ(κ<sup>×</sup>) is torsion, so κ<sup>×</sup> is torsion; and symmetrically with σ<sup>−1</sup>. |

**All six named classes are Aut(C)-stable, and (Image) is the *easiest* of them, not the hardest** — because it is the one condition that constrains the image, and post-composition by an automorphism is precisely the operation an image-condition cannot see. The note's flagged worry resolves in the note's favor. ✔

**Attempted BREAK on (Image).** One looks for χ with χ(κ<sup>×</sup>) torsion but (σ∘χ)(κ<sup>×</sup>) not, or vice versa. Impossible: σ|<sub>C<sup>×</sup></sub> is an automorphism of an abelian group, and "is a torsion group" is an isomorphism invariant. No counterexample exists. Similarly for the ⊗Q form (A ⊗ Q = 0 ⟺ A torsion). ✔

**Consistency with admissibility.** Def. 4.1's own operations (pre-composition by Aut κ, and ν-th powers) commute with post-composition by σ, so if E is admissible then σ(E) is admissible; combined with the table, σ(E) = E for the six named classes. ✔

### 6.3 FINDING D-2 (MINOR) — the note's one-line reason mislabels which condition uses which invariant

The note writes: "kernels are unchanged — ker(σ∘P) = ker P — and images map by σ, preserving torsion and ⊗Q-dimension". The ⊗Q-**dimension** conditions (E<sub>fd</sub>, E<sub>fd0</sub>) are conditions on **kernels**, not images; the image-side ⊗Q statement belongs to (Image) alone. As written the sentence reads as if E<sub>fd</sub>/E<sub>fd0</sub> were being handled on the image side, which would be a non-argument. Replacement text in §10 (R-D2) — the table above.

### 6.4 FINDING D-3 (MINOR) — "stable" collides with a technical term in the same source

[x-03] p. 29 defines "**stable** class" to mean closed under restriction to algebraically closed subfields, and records that "**All classes in the example are stable except for (Image) and hence E<sub>max</sub>**." The note uses "stable" for Aut(C)-stability and asserts that E<sub>max</sub> *is* stable. Both statements are true, of different notions, about the same class, three pages apart in the same paper. A reader collating them will conclude one of the two documents is wrong. Replacement: say "Aut(C)-stable" everywhere, with a one-clause footnote distinguishing it from [x-03] p. 29's "stable". (R-D3.)

### 6.5 D(iii): the coordinate formula — re-derived

Let σ ∈ Aut(C) and let u<sub>σ</sub> ∈ Ẑ<sup>×</sup><sub>(p)</sub> be the image of σ|<sub>µ(C)</sub> ∈ Ẑ<sup>×</sup> under Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub>, i.e. σ(ζ) = ζ<sup>u<sub>σ</sub></sup> for ζ ∈ µ<sup>(p)</sup>(C) (legitimate by (2.2)). By (2.1), χ<sub>x</sub> takes values in µ<sup>(p)</sup>(C), so for r ∈ κ(x)<sup>×</sup>
> (σ ∘ χ<sub>x</sub>)(r) = χ<sub>x</sub>(r)<sup>u<sub>σ</sub></sup> = χ<sub>x</sub>(r<sup>u<sub>σ</sub></sup>) = (χ<sub>x</sub> ∘ ( )<sup>u<sub>σ</sub></sup>)(r),
using that χ<sub>x</sub> is a homomorphism of Ẑ<sub>(p)</sub>-modules. Hence for any (a, ν) ∈ Ẑ<sup>×</sup><sub>(p)</sub> × N₀,
> σ ∘ (χ<sub>x</sub> ∘ ( )<sup>a</sup> ∘ ( )<sup>ν</sup>) = (σ ∘ χ<sub>x</sub>) ∘ ( )<sup>a</sup> ∘ ( )<sup>ν</sup> = χ<sub>x</sub> ∘ ( )<sup>u<sub>σ</sub>a</sup> ∘ ( )<sup>ν</sup>,
i.e. **(a, ν) ↦ (u<sub>σ</sub>a, ν)** in the (35)-coordinates. ✔ This is compatible with (35)'s fibres ((a,ν) ~ (p<sup>n</sup>a′, νp<sup>n</sup>)) because multiplication by u<sub>σ</sub> commutes with multiplication by p<sup>n</sup>, and with the G-quotient by N x₀<sup>Ẑ</sup> ⊆ p<sup>Ẑ</sup> because Ẑ<sup>×</sup><sub>(p)</sub> is abelian. So σ descends to translation by u<sub>σ</sub> on Ẑ<sup>×</sup><sub>(p)</sub>/N x₀<sup>Ẑ</sup> and to translation by [u<sub>σ</sub>] on **B<sub>p</sub>**. ✔ σ ∘ P<sup>×</sup> has the same kernel as P<sup>×</sup>, so σ preserves S (the set (35) surjects onto) and hence acts on C<sub>x₀</sub> and, by D(i), on Γ<sub>x₀</sub>, carrying flow orbits of period log p to flow orbits of period log p. ✔

The note's "divisible-image argument as in Lemma A" is correct but stronger than needed: only χ<sub>x</sub>(κ(x)<sup>×</sup>) ⊆ µ<sup>(p)</sup>(C) is used, not surjectivity.

### 6.6 FINDING D-1 (MINOR, but it must be added) — the Aut(C)-action is **not** continuous, and the note nowhere says so

[x-03] §7 (p. 40, read verbatim: "Viewing X<sup>•</sup>(C) as a set of multiplicative maps P : R → C … we give X<sup>•</sup>(C) the topology of pointwise convergence") makes the topology pointwise convergence **into C with its own topology**. A wild σ ∈ Aut(C) is discontinuous on C, hence P<sub>n</sub> → P pointwise does **not** imply σP<sub>n</sub> → σP pointwise. Therefore:

* σ is a bijection of X₀ commuting with the flow, **not** a homeomorphism;
* Lemma D must not be combined with any closure or compactness statement. In particular the identity σ(cl(A)) = cl(σ(A)) is **false in general**, so Proposition 1 may not be chained with the 9.3 adjudication's Theorem A (a closure statement) without further argument.

This is not an error in the note — Proposition 1 uses only set-level stability and flow-commutation, and nothing in §§4–6 chains σ with a closure. It is a gap in the note's *scope statement*, and a foreseeable trap for the next consumer, since Theorem A and Proposition 1 are about the same packet. Replacement text in §10 (R-D1).

*A partial positive remark, since it may be wanted later:* on the packet the two do in fact cohere, because Theorem A's convergence is **coordinatewise eventually exact** (adjudication §2, step 3: χ(r̄<sup>n<sub>k</sub>a₀</sup>) = χ(r̄<sup>c</sup>) exactly, eventually, for each fixed r). An eventually-constant sequence stays eventually constant under any map, so σ does carry those particular convergent sequences to convergent sequences with limit σ(lim). That is a statement about those sequences, not about continuity, and it should be argued explicitly wherever it is used.
