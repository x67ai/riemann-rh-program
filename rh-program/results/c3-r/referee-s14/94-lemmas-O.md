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

---

## 7. PROPOSITION 1 (D1, the equivariance no-go) — verdict **PASS** (0 MAJOR, 1 MINOR), and it proves slightly more than it states

### 7.1 Statement

> "**Proposition 1.** Let E be any Aut(C)-stable class (all named example classes qualify) and let S ⊆ X₀<sup>E</sup> be Aut(C)-stable and flow-invariant. If S contains one periodic point over the prime p, then for EVERY base class [c] ∈ B<sub>p</sub>, S contains a closed orbit of length log p with base class [c]. In particular S contains uncountably many closed orbits over p …, and **no Aut(C)-stable selection achieves one orbit per prime**."

### 7.2 Re-derivation, line by line

Let x₀ = (p), E Aut(C)-stable and admissible with E ⊆ E<sub>max</sub> (so that Thm 5.2/6.1 apply), and S ⊆ X₀<sup>E</sup> both Aut(C)-stable and flow-invariant. Suppose z ∈ S is periodic.

1. **z lies in a packet, on an orbit with a base class.** By Thm 6.1 (p. 39, §1.1(i)) the periodic set of X₀ is ∐<sub>x₀</sub>Γ<sup>E</sup><sub>x₀</sub> and every periodic orbit lies in exactly one Γ<sup>E</sup><sub>x₀</sub>; take x₀ = (p). Its flow orbit γ ⊆ S (S is flow-invariant) is a circle of length log N x₀ = log p. By (2.3) γ is a fibre of Γ<sub>p</sub> → B<sub>p</sub>; let [a] ∈ B<sub>p</sub> be its base class. ✔
2. **Every base class is reachable by an automorphism.** Given [c] ∈ B<sub>p</sub>, write [c] = [ua] with u ∈ Ẑ<sup>×</sup><sub>(p)</sub> (B<sub>p</sub> is a group, so u = ca<sup>−1</sup> works, defined modulo p<sup>Ẑ</sup>). By **Lemma C** (§5.2, Step 4 + the Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub> projection) there is σ ∈ Aut(C) with u<sub>σ</sub> = u. ✔
3. **σ(γ) is a periodic orbit of the same length in the base class [c].** By **Lemma D(i)** σ commutes with φ<sup>t</sup>, so σ(γ) is a φ-orbit of the same period log p. By **Lemma D(ii)** σ preserves E, so σ(γ) ⊆ X₀<sup>E</sup>. By **Lemma D(iii)** σ moves the base class by [a] ↦ [u<sub>σ</sub>a] = [c]. ✔
4. **σ(γ) ⊆ S.** S is Aut(C)-stable. ✔
5. **Distinct base classes ⟹ distinct orbits.** By (2.3), Γ<sub>p</sub> ≅ B<sub>p</sub> × S¹ with the flow acting on the second factor only, so the fibres of Γ<sub>p</sub> → B<sub>p</sub> are exactly the flow orbits. Source anchor, **verbatim, [x-03] p. 38**: "Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> … with fibres the R<sup>>0</sup>-orbits in Γ<sub>x₀</sub>." ✔
6. **Uncountability.** B<sub>p</sub> is an infinite profinite group, hence uncountable — re-derived independently at (2.4). ✔
7. **Conclusion.** S ⊇ {one orbit in every base class} = Γ<sub>p</sub>, an uncountable family; in particular S does not have exactly one orbit over p. Since p was arbitrary among primes over which S has a periodic point, no Aut(C)-stable S achieves one orbit per prime. ∎ ✔

**The proposition is correct as stated.** No step is missing and no hypothesis is unused (E's Aut(C)-stability is used in step 3; S's flow-invariance in step 1; S's Aut(C)-stability in step 4; Lemma C's surjectivity in step 2; the fibration in step 5).

### 7.3 It proves slightly more: **Γ<sup>E</sup><sub>p</sub> = Γ<sub>p</sub> for every Aut(C)-stable admissible E meeting the packet**

Take S = X₀<sup>E</sup> itself (Aut(C)-stable because E is, flow-invariant by construction). Steps 1–7 then give: *if X₀<sup>E</sup> contains one periodic point over p, it contains the full packet Γ<sub>p</sub>.* Compare [x-03] Thm 5.2, which gets C<sup>E</sup><sub>x₀</sub> = C<sub>x₀</sub> from the very different hypothesis E ⊇ E<sub>f</sub>. So Proposition 1 supplies an **independent second proof of the full-packet phenomenon, under a hypothesis (Aut(C)-stability) that is not comparable with E ⊇ E<sub>f</sub>**; and the two agree on every named class, all of which satisfy both. The note calls this a "conceptual explanation" of Thm 5.2 in its consistency check (c); it is more than that — it is a theorem with an independent hypothesis, and it is worth stating as such because it is the cleanest available formulation of D1's positive content. (Suggested addition, §10, R-P2. Not a defect.)

### 7.4 FINDING P-1 (MINOR) — the cited anchor is one page weaker than the one available

The note supports step 5 with "the fibers of the (38)-fibration are the Q<sup>>0</sup>-orbits ([x-03] p. 33)". That statement is about C<sub>x₀</sub> ⊆ X̌₀(C) and Q<sup>>0</sup>-orbits, and needs the (easy, but unstated) translation "two points of C<sub>x₀</sub> lie on the same flow orbit of the suspension iff they lie on the same Q<sup>>0</sup>-orbit". The statement Proposition 1 actually wants is printed on **p. 38** for the suspension itself and needs no translation. Replacement text in §10 (R-P1). *For completeness, the translation the note needs, verified:* by the p. 38 definition of the suspension, [P₀,u] and [P₀′,u′] lie on one φ-orbit iff ∃t, [P₀, ue<sup>t</sup>] = [P₀′,u′] iff ∃q ∈ Q<sup>>0</sup>: P₀′ = F<sub>q</sub>(P₀) — i.e. iff P₀, P₀′ lie on one Q<sup>>0</sup>-orbit. ✔

### 7.5 The Corollary and its two scope notes

**Corollary (the transplant no-go).** "any global selection with the analogous naturality — in particular, any selection defined uniformly from the abstract field C and the scheme data … retains the full packet. A viable global selection must break Aut(C)-symmetry."

* The *input* facts are correctly cited and I verified them: Deninger's construction takes an abstract algebraically closed C as input ([x-03] p. 31, verbatim §1.1(d); repeated at p. 38 for §6), and the local principle is equivariant for the full coefficient automorphism group ([x-03] Thm 15.6(1), "**G × Aut(o) × ⟨F<sub>p</sub>⟩-equivariant**", p. 113, and Remark 14.17, p. 104). ✔
* The note's **(F1)** justification for why Aut(o)-equivariance is free also checks: in a rank-1 valuation ring the order on the value group is definable from divisibility, so a ring automorphism induces an order-automorphism λ of the value group; but σ(p) = p forces λ(v(p)) = v(p), and an order-automorphism of a rank-1 (hence Archimedean, hence R-embeddable) value group fixing one nonzero element is the identity. Hence |σ(y)| = |y| and the defect condition is Aut(o)-invariant. ✔ This is exactly what Deninger's "Since automorphisms of o are p-adically continuous" (p. 104) asserts.
* **The bridge "canonical ⟹ Aut(C)-stable" is a definability schema, not a theorem, and the note says so.** I concur with that self-assessment, and I record that the schema is *not* needed for the sharp form of D1: Proposition 1 itself is a theorem, and §7.3 shows it already forces full packets for every Aut(C)-stable admissible class. The schema is only needed to pass from "Aut(C)-stable" to "canonical", and it should stay flagged.
* Consistency check (c) — "the Theorem-C cuts E(a₀) are not Aut(C)-stable" — checks against the adjudication (§4 item 5b, read: E(a₀) reaches only the base classes a₀·p<sup>Ẑ</sup>), since σ sends χ<sup>a₀</sup> to χ<sup>u<sub>σ</sub>a₀</sup>, of base class [u<sub>σ</sub>a₀] ≠ [a₀] for u<sub>σ</sub> ∉ p<sup>Ẑ</sup>. I did **not** re-derive Theorem C itself (out of scope for this item; the adjudication states it re-derived the reachability step). ✔ No inconsistency found.

### 7.6 BREAK attempts on Proposition 1 (all failed)

* *An Aut(C)-stable one-orbit-per-prime S?* Steps 1–7 exclude it outright.
* *Weaken "Aut(C)-stable" to "σ(S) ⊆ S for all σ"?* Same conclusion: Aut(C) is a group, so σ(S) ⊆ S for all σ forces σ(S) = S.
* *Drop E's Aut(C)-stability and keep S's?* Then step 3's "σ(γ) ⊆ X₀<sup>E</sup>" fails, and indeed the Theorem-C cuts show the conclusion then fails: E(a₀) is admissible, flow-invariant, one orbit per prime, and *not* Aut(C)-stable. **So the hypothesis is necessary and the proposition is sharp.** This is the same fact the note records as consistency check (c); I confirm it functions as a sharpness witness, not merely a consistency remark.
* *Could σ fail to preserve periodicity because it is discontinuous?* No: periodicity is φ<sup>t</sup>z = z for some t > 0, a purely algebraic condition, and σφ<sup>t</sup> = φ<sup>t</sup>σ (§6.1). ✔

---

## 8. The two auxiliary derivations named in the charter

### 8.1 §3's freshman's-dream N-invariance argument — **PASS**, with a strictly stronger obstruction available

**What the note says.** "additivity mod p is ( )<sup>p</sup>-stable (Prop. 14.7's computation) but not ( )<sup>ℓ</sup>-stable for ℓ ≠ p, since (r+s)<sup>ℓ</sup> ≢ r<sup>ℓ</sup> + s<sup>ℓ</sup> mod p. A mod-p-type selection and the full-Q<sup>>0</sup> suspension design cannot coexist."

**Re-derivation.** *p-stability* is [x-03] Prop. 14.7 verbatim ("F<sub>p</sub>(Y̌<sub>α</sub>) = Y̌<sub>α</sub>", p. 94), proved via F<sub>p</sub>(I<sub>y</sub>) = I<sub>y</sub>. ✔ *Failure of ℓ-stability*: let P be mod-p additive, so P̄ := P mod p is a ring homomorphism into the characteristic-p ring o/p. Then F<sub>ℓ</sub>(P) = P ∘ ( )<sup>ℓ</sup> has reduction P̄ ∘ ( )<sup>ℓ</sup>, and for a, b in the domain, P̄((a+b)<sup>ℓ</sup>) = P̄(a+b)<sup>ℓ</sup> while P̄(a<sup>ℓ</sup>) + P̄(b<sup>ℓ</sup>) = P̄(a)<sup>ℓ</sup> + P̄(b)<sup>ℓ</sup>; these differ whenever the ℓ-th power map on the image fails additivity. **Explicit witness:** κ = F̄<sub>5</sub>, τ = id, P = [·], ℓ = 3. Then F₃(P)(r) = [r³], whose reduction is r ↦ r³ on F̄₅, and (1+1)³ = 8 = 3 ≠ 2 = 1³ + 1³. So F₃(P) is not mod-p additive while P is: Def. 4.1's biconditional (§1.1(a), "χ is in E **if and only if** χ ∘ σ resp. χ<sub>ν</sub> is in E") fails. ✔ And this is not an artifact of the note's reading — it is Deninger's own verdict on p. 29 ("the resulting class E is not N-invariant") and the reason he restricts to N₀ = p<sup>Z</sup> in §14 (p. 89, verbatim). ✔

**Strengthening (referee-derived).** There is a second, structurally prior obstruction that the note does not name and that is worth banking, because it blocks the *tilt-style* formulation before the ν-closure question is even reached. Deninger's local condition is posed on Ô<sup>♭</sup> = lim<sub>( )<sup>p</sup></sub>Ô — a **ring**, because in characteristic p the transition map ( )<sup>p</sup> is a ring homomorphism. The global design (Def. 4.1, [x-03] (28)–(29), p. 25) uses the full monoid N₀ and forms lim<sub>N₀</sub> κ(x)<sup>×</sup> with transition maps ( )<sup>ν</sup> for **all** ν ∈ N₀. For ν not a power of p the map ( )<sup>ν</sup> is not additive, so lim<sub>N₀</sub> κ(x) carries **no ring structure at all** and the phrase "P̌(r+s) − P̌(r) − P̌(s)" has no referent there. In other words the mismatch is not only that a mod-p condition fails to be N-invariant; it is that the object on which Deninger poses the condition locally has no global counterpart once N₀ = N. Recommended as an addition to §3 (R-N1); it makes requirement 4 of §3 a structural impossibility rather than a stability failure.

### 8.2 §7's Haar formal count — **PASS-WITH-REPAIRS** (1 MAJOR)

**What the note says.** "the packet base B<sub>p</sub> is a compact group, its Haar probability measure is translation-invariant, and by Lemma D(iii) Aut(C) acts on B<sub>p</sub> by group translations — so **Haar measure is canonical AND Aut(C)-equivariant** … The flow fixes the base (§4), so the measure is flow-invariant. At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is ∫<sub>B<sub>p</sub></sub>(single-orbit term) dHaar = the single-orbit term, **since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p — [x-06] Thm 4.2)**."

**What checks.**
* B<sub>p</sub> is a compact (profinite) group (2.4), so it carries a unique Haar probability measure. ✔
* Aut(C) acts on B<sub>p</sub> by translations (Lemma D(iii), §6.5) and translations preserve Haar. ✔
* The flow acts trivially on B<sub>p</sub> (2.3), so Haar on the base is flow-invariant. ✔
* **[x-06] Thm 4.2 says exactly what the note says it says**, read verbatim this session (§1.2): "The compact subsets Γ<sub>x₀</sub> ⊂ X₀ consist of periodic orbits of length log N x₀ … Γ<sub>x₀</sub> is a fibre space over the compact group Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) … with fibres the compact orbits", and one line later "all of which have length log N x₀ i.e. log p if X₀ = spec Z". ✔

**A referee-grade strengthening the note misses.** [x-03] p. 33 warns "The maps (37), (38) and the fibration map **depend on our choices of x and ι**". That is exactly the ambiguity that makes a *point* of B<sub>p</sub> non-canonical (the whole content of D3). But changing ι to ι ∘ ( )<sup>u</sup> replaces a by ua and changing x within its G-orbit acts through N x₀<sup>Ẑ</sup> ⊆ p<sup>Ẑ</sup>, which is trivial on B<sub>p</sub>: **the entire ambiguity is by translations, and Haar measure is the unique translation-invariant probability measure.** So the Haar candidate is canonical *for exactly the reason that the point-selection is not* — a sharper way to say Road 2's thesis than the note states, and one that follows from anchors already read. (R-H2.)

**FINDING H-1 (MAJOR).** "since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p)" does **not** establish what it is asked to establish. In every trace formula the program is aiming at, the orbital contribution of a closed orbit is not a function of its length alone: in the Guillemin-type/foliated-flow formulas the local factor at a closed orbit carries the transverse Poincaré data as well as the length (this is precisely the ledger's R4 difficulty, and it is why H4-type hypotheses about simple isolated orbits appear at all). Equality of lengths across the packet is therefore not a proof that the integrand is constant, and the sentence as written would let a later reader believe the count "comes out right" for a reason that has not been checked.

*FILL (supplied, and it runs through Lemma D — i.e. through this very item).* The right reason is **homogeneity**, not length:

> Let W be any assignment γ ↦ W(γ) of a weight to the closed orbits of Γ<sub>p</sub> that is natural for automorphisms of the ambient dynamical system commuting with the flow. By Lemma D, every σ ∈ Aut(C) is such an automorphism, and by Lemma D(iii) together with Lemma C the induced action on the set of closed orbits of Γ<sub>p</sub> ≅ B<sub>p</sub> × S¹ is the **transitive** translation action on B<sub>p</sub>. Hence W is constant on Γ<sub>p</sub>, and ∫<sub>B<sub>p</sub></sub>W dHaar = W(γ) for any single γ, Haar being a probability measure.

This is strictly better than the length argument: it is a proof, it explains *why* the packet is the natural unit, and it makes Road 2's viability depend on precisely the right thing — that the trace formula's orbital weight be natural, which is a hypothesis one can state and then test in DQ-M. It also inherits Proposition 1's exact scope: it says nothing about weights that are *not* natural in this sense, and nothing about whether the distributional trace exists (DQ-M's actual content). Replacement text in §10 (R-H1).

**What is NOT repaired, and must stay open.** The repair establishes constancy of a natural weight; it does not establish (i) that a distributional trace exists for a flow with a continuum of closed orbits, (ii) that its orbital side is an integral over the packet at all rather than something else, or (iii) that the transverse/leafwise analysis survives the non-Hausdorffness recorded by the 9.3 adjudication (§4 item 3, W12). The note is right to route all three to DQ-M and right to say the published frameworks on disk exclude orbit continua by hypothesis. Road 2's status is unchanged by this repair: **the formal count is now correctly justified, and it remains formal.**

---

## 9. Citation and transcription layer (5 MINOR findings)

**T-1 (MINOR, a displayed identity that is false as transcribed).** §4 of the note prints the packet base as
> "B<sub>p</sub> := Ẑ<sup>×</sup>₍p₎/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub>)<sup>×</sup>/Aut(F<sub>p</sub>)^"
Taken literally this is false: Aut(F<sub>p</sub>) is trivial (F<sub>p</sub> has no nontrivial field automorphisms), so the right-hand side would be all of Aut(F̄<sub>p</sub>)<sup>×</sup> and the quotient by p<sup>Ẑ</sup> would have been discarded. The source display, read from a page render because `pdftotext` drops the overlines and floats the superscript (§1.3), is
> **Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> = Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>)** ([x-03] p. 33; the same display recurs on p. 38 and in [x-06] p. 12).
The × belongs **inside** the first Aut, on F̄<sub>p</sub>; the second Aut is of the **field** F̄<sub>p</sub>, not of F<sub>p</sub>. The corrected reading is literally the note's own §4 Consequence 1 — "coker(Aut<sub>ring</sub> ↪ Aut<sub>group</sub>)" — so the transcription slip obscures the note's best sentence. Nothing downstream consumes the mis-transcription. *(The 9.3 adjudication §2 carries the same artifact; that is the adjudicator's file to fix, not mine.)*

**T-2 (MINOR).** "this process does not give more points" is on **[x-03] p. 6**, not p. 5. The note cites p. 5 twice (§2 Stage 2, and §6). (p. 5 does carry the separate "minimal condition E … does not look natural" line, which the note cites correctly.)

**T-3 (MINOR).** The [D25] quotation in §7 Road 1 inserts "= (ZĀ)<sup>G</sup>" inside the quotation marks: the source reads "the more information the ring W<sub>rat</sub>(A) has about the additive structure of A". The gloss is correct (it is the paper's own display (3)) but must be bracketed or moved outside the quotation.

**T-4 (MINOR).** §1 lists "§14 pp. 89–100" for "Defs. 14.1/14.2/14.5/14.12, Props. 14.7/14.13/14.14". Def. 14.12 is on p. 99, Prop. 14.13 on p. 100 and Prop. 14.14 spans **pp. 100–101** (its proof begins on p. 101); the range should read 89–101.

**T-5 (MINOR).** §10 records [D25] as "scratchpad copy only … flagged for `fetched-r3/` promotion". The promotion has happened: the file is on disk at `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf` (verified this session; the intro quotation was read from it). The bookkeeping item is discharged, and the note's suggested filename differs from the one actually used.

---

## 10. REPAIRS — exact replacement text

*(The note is not edited by me. Each item below gives the text to substitute, for the adjudicator to apply.)*

**R-A1 (MAJOR, Lemma A statement, §4).** Replace the hypothesis clause
> "…κ an algebraically closed field of characteristic p, and P: κ → o multiplicative with P(0) = 0, P(1) = 1, whose restriction to κ<sup>×</sup> is a group homomorphism into o (values automatically in µ<sup>(p)</sup>(o), the prime-to-p roots of unity, since κ<sup>×</sup> is prime-to-p torsion)."

by

> "…**κ ≅ F̄<sub>p</sub> an algebraic closure of F<sub>p</sub>** (this is the only case used below: for X₀ = Spec Z every char-p residue field κ(x) is such — and it is also the only case in which the statement is well posed, since for a general algebraically closed field of characteristic p the group κ<sup>×</sup> is not torsion and the right-hand side below does not typecheck; the correct statement in that generality is the tilt statement, [x-03] Prop. 14.14 and Thm 15.6(1)), and P: κ → o multiplicative with P(0) = 0, P(1) = 1. Its restriction to κ<sup>×</sup> is then automatically a homomorphism into µ<sup>(p)</sup>(o): every r ∈ κ<sup>×</sup> has finite order d prime to p, so P(r)<sup>d</sup> = P(r<sup>d</sup>) = 1."

**R-A2 (MAJOR, Lemma A converse, §4).** Replace
> "(⇐) [a] + [b] − [a+b] ∈ V W(k) = p W(k) in the Witt ring W(k) ⊆ o (first ghost/component coordinates agree; V F = p on Witt vectors of a perfect ring), so the defect of [·]∘τ has absolute value ≤ |p|."

by the self-contained argument (no Witt vectors, no embedding of W(k) into o, no p-adic completeness):

> "(⇐) Let a = τ(r), b = τ(s) ∈ F̄<sub>p</sub> ⊆ k and put ζ = [a], ξ = [b], w = [a+b] ∈ µ<sup>(p)</sup>(o) ∪ {0}. If a, b or a+b is 0 the defect is 0, except when p = 2 and a+b = 0, where it is 2ζ of absolute value |2| = |p|. Otherwise let m = lcm(ord ζ, ord ξ, ord w), prime to p, and pick f with q := p<sup>f</sup> ≡ 1 (mod m), so ζ<sup>q</sup> = ζ, ξ<sup>q</sup> = ξ, w<sup>q</sup> = w. Since p divides C(p,i) for 0 < i < p, u ≡ v (mod p·o) implies u<sup>p</sup> ≡ v<sup>p</sup> (mod p·o) and (u+v)<sup>p</sup> ≡ u<sup>p</sup> + v<sup>p</sup> (mod p·o); iterating f times, (ζ+ξ)<sup>q</sup> ≡ ζ + ξ (mod p·o). Put x = ζ + ξ − w; reduction mod **m** is a ring map and ζ+ξ, w have the same reduction a+b, so |x| < 1. Since p divides C(q,i) for 0 < i < q, expanding (w+x)<sup>q</sup> gives (ζ+ξ)<sup>q</sup> ≡ w + x<sup>q</sup> (mod p·o), whence **x ≡ x<sup>q</sup> (mod p·o)** and, iterating, x ≡ x<sup>q<sup>n</sup></sup> (mod p·o) for all n. As o has rank one and |x| < 1, |x|<sup>q<sup>n</sup></sup> → 0 < |p|, so by the ultrametric inequality |x| ≤ max(|p|, |x|<sup>q<sup>n</sup></sup>) = |p| for n large. Hence the defect of [·]∘τ is ≤ |p|, and the bound |p| is attained (p = 2, s = r), so it is sharp. ∎"

**R-A3 (MINOR, §2).** "([x-03] §§13–14, pp. 78, 89)" → "([x-03] §14 p. 89 for the p-adically complete rank-1 valuation ring and the reduced monoid N₀ = p<sup>Z</sup>; **§15 pp. 105–106 for the additional hypotheses that C is algebraically closed of characteristic 0 and k algebraically closed of characteristic p**, which Lemma A uses)".

**R-A4 (MINOR, §4 Consequence 2).** "So the faithful transport of the local principle **is** the adjudicated Theorem-C cut E(a₀), with j in place of a₀" → "So the faithful transport of the local principle **selects exactly the single base class that the adjudicated Theorem-C cut E(a₀) reaches**, with j in place of a₀. (The transported condition is not itself admissible — it fails Def. 4.1's ν-closure, by §3 — so the object comparable to E(a₀) is its admissible closure; the two select the same base class, which is all D3 uses.)"

**R-B1 (MINOR, §6 closing paragraph).** Replace
> "…and Deninger's own asserted translation (p. 29) cannot live here in nonempty form as a threshold condition, so his intended reading is presumably the transport reading of §4 (D3), consistent with his 'not N-invariant' verdict on it. [Judgment-grade reading, flagged.]"

by

> "…Note that the threshold class is **not** empty as a class of characters: over an algebraically closed subfield κ ⊆ C of characteristic 0 the inclusion has defect 0 and satisfies (Tors), and it is not N-invariant (χ ∘ ( )<sup>ν</sup> has unbounded defect), exactly as [x-03] p. 29 says. Deninger's remark is therefore consistent with the threshold reading, and this note does not claim to identify his intended reading. **What Lemma B establishes is sharper and independent of that question: the threshold class lives entirely over characteristic-zero points, so the system it selects has no periodic orbits at all** — the failure is not that it cuts the packet badly, but that it deletes the packet. [The identification of Deninger's intent remains open and carries no weight here.]"

**R-B2 (MINOR, Lemma B statement).** "since P(2̄) is a root of unity or 0 (κ(x)<sup>×</sup> is torsion; 0 occurs iff p = 2)" → "since 2̄ ∈ F<sub>p</sub><sup>×</sup> has finite order dividing p − 1, so P(2̄) is a root of unity, of modulus 1 (and P(2̄) = 0 exactly when p = 2, where 2̄ = 0). **Note this uses only that 2̄ is torsion, not that κ(x)<sup>×</sup> is: the lemma therefore holds at every point of positive residue characteristic of any arithmetic X₀, a strictly larger locus than the periodic one.**"

**R-C1 (MINOR, Lemma C statement).** "for C the complex numbers (or any algebraically closed field of characteristic 0 containing Q̄ with infinite transcendence degree)" → "**for every algebraically closed field C of characteristic 0** (in particular for the complex numbers, and for every C admitted by [x-03] p. 28)".

**R-C2 (MINOR, Lemma C derivation).** Replace the derivation sentence by:
> "*Derivation.* (1) The cyclotomic character Gal(Q(µ<sub>∞</sub>)/Q) →∼ Ẑ<sup>×</sup> gives σ<sub>u</sub> with σ<sub>u</sub>(ζ) = ζ<sup>u</sup>. (2) Q̄ is algebraic over Q(µ<sub>∞</sub>), so σ<sub>u</sub> extends to an embedding Q̄ → Q̄ (isomorphism extension, Zorn), which is onto because its image is algebraically closed and contains Q. (3) Choose a transcendence basis B of C over Q̄ (Zorn) and extend to Q̄(B) by the identity on B. (4) C is an algebraic closure of Q̄(B), so extend once more (Zorn) to σ ∈ Aut(C). Then σ|<sub>µ(C)</sub> = ( )<sup>u</sup>. Choice is used exactly three times, at (2), (3), (4); for u ∉ {±1} the resulting σ is necessarily discontinuous. Composing with Ẑ<sup>×</sup> ↠ Ẑ<sup>×</sup><sub>(p)</sub>, **every u ∈ Ẑ<sup>×</sup><sub>(p)</sub> arises as u<sub>σ</sub>**, which is the form used below. ∎"

**R-D1 (MINOR, add to Lemma D as a new clause (iv), and to §5's scope note).**
> "**(iv) Scope: σ is a flow-commuting bijection, not a homeomorphism.** The topology on X<sup>•</sup>(C) is pointwise convergence into C ([x-03] §7, p. 40), and a wild σ ∈ Aut(C) is discontinuous on C, so σ need not preserve convergence. Everything in (i)–(iii) and in Proposition 1 is purely set- and flow-theoretic and does not use continuity. **Consequently Lemma D may not be chained with any closure or compactness statement — in particular σ(cl A) = cl(σA) is false in general, and Proposition 1 must not be composed with the 9.3 adjudication's Theorem A (a closure law on the same packet) without a separate argument.** Where such a composition is wanted, note that Theorem A's convergence is coordinatewise *eventually exact*, and eventual constancy is preserved by any map; that observation, not continuity, is what would have to be invoked."

**R-D2 (MINOR, Lemma D(ii) justification).** Replace "kernels are unchanged — ker(σ∘P) = ker P — and images map by σ, preserving torsion and ⊗Q-dimension; Def. 4.1's operations are pre-compositions, which commute with σ" by
> "two facts suffice. (K) ker(σ∘P) = ker P and ker((σ∘P)|<sub>µ(κ)</sub>) = ker(P|<sub>µ(κ)</sub>), because σ|<sub>C<sup>×</sup></sub> is injective — this settles (Tors) and hence E<sub>tors</sub>, and the kernel conditions of E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub> (all of which are conditions on ker χ, including the ⊗Q-dimension ones). (I) σ|<sub>C<sup>×</sup></sub> restricts to a group isomorphism onto the image, so 'the image is torsion' — equivalently 'image ⊗ Q ≠ 0' — is unchanged; the other half of (Image), 'κ<sup>×</sup> is torsion', does not mention χ. This settles (Image) and hence E<sub>max</sub>. Both are biconditional. Finally Def. 4.1's own operations are pre-compositions, which commute with σ, so σ(E) is admissible whenever E is."

**R-D3 (MINOR, terminology).** Everywhere the note says a class is "stable", write "**Aut(C)-stable**", and add once: "not to be confused with [x-03] p. 29's technical term *stable* (closed under restriction to algebraically closed subfields), under which E<sub>max</sub> is explicitly **not** stable."

**R-P1 (MINOR, Proposition 1 proof).** "distinct base classes lie on distinct orbits since the fibers of the (38)-fibration are the Q<sup>>0</sup>-orbits ([x-03] p. 33)" → "distinct base classes lie on distinct orbits: for X₀ = Spec Z, deg x₀ = 1, so [x-03] p. 38 gives Γ<sub>p</sub> ≅ (Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup>) × (R<sup>>0</sup>/p<sup>Z</sup>) = B<sub>p</sub> × S¹ with '**all R<sup>>0</sup>-orbits in Γ<sub>x₀</sub> are circles R<sup>>0</sup>/N x₀<sup>Z</sup> and Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> … with fibres the R<sup>>0</sup>-orbits</sup>' ([x-03] p. 38, verbatim) — i.e. exactly one closed orbit per base class."

**R-P2 (addition, not a defect; §5 after Proposition 1).**
> "**Corollary 1′.** For every Aut(C)-stable admissible E ⊆ E<sub>max</sub> whose locus meets Γ<sub>p</sub>, one has Γ<sup>E</sup><sub>p</sub> = Γ<sub>p</sub>. (Apply Proposition 1 with S = X₀<sup>E</sup>.) This is an independent second proof of [x-03] Thm 5.2's full-packet conclusion under a hypothesis not comparable with E ⊇ E<sub>f</sub>, and it is the sharpest theorem-grade form of D1."

**R-N1 (addition, §3, after the freshman's-dream paragraph).**
> "There is a structurally prior obstruction as well. Deninger poses the local condition on Ô<sup>♭</sup> = lim<sub>( )<sup>p</sup></sub>Ô, which is a *ring* because ( )<sup>p</sup> is a ring homomorphism in characteristic p. The global design uses the full monoid N₀ = N and forms lim<sub>N₀</sub>κ(x) with transition maps ( )<sup>ν</sup> for all ν; for ν not a power of p these are not additive, so the global projective limit **carries no ring structure** and the expression 'P̌(r+s) − P̌(r) − P̌(s)' has no referent on it. Requirement 4 is therefore not merely a stability failure but an absence of the object on which the local condition is posed."

**R-H1 (MAJOR, §7 Road 2).** Replace
> "At the formal level the T1 count then comes out right: the packet's aggregate orbit contribution is ∫<sub>B<sub>p</sub></sub>(single-orbit term) dHaar = the single-orbit term, since the integrand is constant (all orbits in Γ<sub>p</sub> have length log p — [x-06] Thm 4.2)."

by

> "At the formal level the T1 count then comes out right, and for a reason stronger than equality of lengths (which by itself does not make an orbital weight constant, since such weights carry transverse data as well as length — ledger R4). The reason is **homogeneity**: let W be any assignment of a weight to the closed orbits of Γ<sub>p</sub> that is natural for automorphisms of the ambient system commuting with the flow. By Lemma D every σ ∈ Aut(C) is such an automorphism, and by Lemma D(iii) with Lemma C the induced action on the set of closed orbits of Γ<sub>p</sub> ≅ B<sub>p</sub> × S¹ ([x-03] p. 38) is the **transitive** translation action on B<sub>p</sub>. Hence W is constant on Γ<sub>p</sub> and ∫<sub>B<sub>p</sub></sub>W dHaar = W(γ) for any single γ. (All orbits do also have the common length log p — [x-06] Thm 4.2, read verbatim — but that is a corollary of the homogeneity, not the reason for it.) **What this does not supply**: the existence of the distributional trace, the identification of its orbital side as an integral over the packet, and the survival of the leafwise analysis in a space that is non-Hausdorff along packets (adjudication §4 item 3) — all three remain DQ-M."

**R-H2 (addition, §7 Road 2).**
> "Note also *why* Haar is canonical here although the packet coordinates are not: [x-03] p. 33 warns that '(37), (38) and the fibration map depend on our choices of x and ι', but changing ι to ι ∘ ( )<sup>u</sup> translates the base class by u and changing x acts through N x₀<sup>Ẑ</sup> ⊆ p<sup>Ẑ</sup>, trivial on B<sub>p</sub>. The whole ambiguity is by translations, and Haar is the unique translation-invariant probability measure on B<sub>p</sub>. The measure is canonical for precisely the reason that no point of B<sub>p</sub> is."

**R-T1 … R-T5 (MINOR, citation layer).** T-1: "Aut(F̄<sub>p</sub>)<sup>×</sup>/Aut(F<sub>p</sub>)^" → "**Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>)**" (both occurrences of the display in §4 and wherever it is echoed). T-2: "intro p. 5" → "intro p. 6" for "this process does not give more points" (both occurrences). T-3: move "= (ZĀ)<sup>G</sup>" outside the quotation marks or bracket it as "[= (ZĀ)<sup>G</sup>]". T-4: "§14 pp. 89–100" → "§14 pp. 89–101". T-5: replace the §10 "Session-local artifact" bullet by "[D25] is on disk at `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`; the promotion is done."

---

## 11. VERDICT BLOCK

**VERDICT: PASS-WITH-REPAIRS.**
**FATAL 0 · MAJOR 3 · MINOR 15.**

| # | sev | location | finding | repair |
|---|---|---|---|---|
| A-1 | **MAJOR** | §4, Lemma A statement | Hypothesis "κ an algebraically closed field of characteristic p" is wrong: κ<sup>×</sup> is torsion only for κ ≅ F̄<sub>p</sub>, and the conclusion "P = [·]∘τ" does not typecheck otherwise. | R-A1 |
| A-2 | **MAJOR** | §4, Lemma A (⇐) | The converse's justification ("W(k) ⊆ o", "first ghost coordinates", "V F = p") is not valid under the note's own hypotheses (**m** ⊋ p·o, no section k → o constructed) and leans on an unread standard fact. Statement is TRUE. | R-A2 (self-contained proof supplied) |
| H-1 | **MAJOR** | §7 Road 2 | "the integrand is constant (all orbits in Γ<sub>p</sub> have length log p)" does not establish constancy of an orbital weight. Conclusion is recoverable by homogeneity. | R-H1 |
| A-3 | MINOR | §2 | Setup attributed to §14 p. 89; the algebraically-closed hypotheses are §15 pp. 105–106. | R-A3 |
| A-4 | MINOR | §4 Consequence 2 | "is the Theorem-C cut E(a₀)" — the transported condition is not admissible; it selects the same base class. | R-A4 |
| B-1 | MINOR | §6 close | The inference "Deninger presumably meant the transport reading" is unsupported: the threshold class is nonempty over char 0 and non-N-invariant, matching p. 29 exactly. | R-B1 |
| B-2 | MINOR | §6, Lemma B | Justification cites "κ(x)<sup>×</sup> is torsion"; the operative fact is that 2̄ ∈ F<sub>p</sub><sup>×</sup> is torsion, which extends the lemma to the whole char-p locus. | R-B2 |
| C-1 | MINOR | §5, Lemma C | "infinite transcendence degree" is unnecessary. | R-C1 |
| C-2 | MINOR | §5, Lemma C | Last clause of the derivation is garbled. | R-C2 |
| D-1 | MINOR | §5, Lemma D | Missing scope statement: σ is not continuous; Lemma D must not be chained with closure statements (Theorem A). | R-D1 |
| D-2 | MINOR | §5, Lemma D(ii) | ⊗Q-dimension conditions are on kernels, not images; the printed one-liner attaches them to the wrong side. | R-D2 |
| D-3 | MINOR | §5–§6 | "stable" collides with [x-03] p. 29's technical term, under which E<sub>max</sub> is *not* stable. | R-D3 |
| P-1 | MINOR | §5, Prop. 1 proof | Cites p. 33 (C<sub>x₀</sub>, Q<sup>>0</sup>-orbits) where p. 38 states the suspension version directly. | R-P1 |
| T-1 | MINOR | §4 | The displayed identity for B<sub>p</sub> is false as transcribed; source reads Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>). | R-T1 |
| T-2 | MINOR | §2, §6 | "does not give more points" is on p. 6, not p. 5. | R-T2 |
| T-3 | MINOR | §7 Road 1 | Unbracketed interpolation inside a verbatim [D25] quotation. | R-T3 |
| T-4 | MINOR | §1 | §14 page range should be 89–101. | R-T4 |
| T-5 | MINOR | §10 | [D25] promotion already done; bookkeeping bullet stale. | R-T5 |

Non-defect additions recommended: **R-P2** (Corollary 1′, the sharpest form of D1), **R-N1** (the prior obstruction in §3), **R-H2** (why Haar is canonical although the coordinates are not).

### What is now established at referee grade, and its precise scope

**Established.** (1) **Lemma A**, for κ ≅ F̄<sub>p</sub>, k algebraically closed of characteristic p, o a rank-1 valuation ring with residue field k: the mod-p-additive multiplicative maps κ → o are exactly the prime-to-p Teichmüller lifts of the field embeddings κ ↪ k, with |p| the sharp constant. Both directions are re-derived here in full and the converse now has a proof that uses nothing but integer binomial coefficients and the ultrametric inequality; independently, the statement is confirmed against [x-03] Thm 15.6(1)'s closed-point fibre Y<sup>⋄</sup><sub>s</sub> = Hom(κ, k) (p. 114), read verbatim. Consequently mod-p additivity cuts the Ẑ<sup>×</sup><sub>(p)</sub>-torsor of coefficient identifications down to a p<sup>Ẑ</sup>-torsor, and the residue is exactly B<sub>p</sub> = coker(Aut(F̄<sub>p</sub>) ↪ Aut(F̄<sub>p</sub><sup>×</sup>)) — the packet base, in Deninger's own display on p. 33. (2) **Lemma B**, in the strengthened form B′: at every positive-characteristic point of any arithmetic X₀, and for every character whatever, the pair r = s = 1 forces archimedean additivity defect ≥ 1; so a uniform archimedean threshold ε < 1 selects a class with no periodic points at all, and the I-adic extension mechanism of [x-03] (172) has no archimedean counterpart. (3) **Lemma C**: Aut(C) ↠ Aut(µ(C)) = Ẑ<sup>×</sup> for every algebraically closed C of characteristic 0, with choice used exactly three times and the realizing automorphisms necessarily wild. (4) **Lemma D**: the post-composition action of Aut(C) commutes with G, with every F<sub>ν</sub>, with the Q<sup>>0</sup>-action and with the flow; it preserves each of E<sub>tors</sub>, E<sub>max</sub>, E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub> biconditionally — (Image) for E<sub>max</sub>, the note's own press point, being the easiest case rather than the hardest — and acts on the packet coordinates by (a, ν) ↦ (u<sub>σ</sub>a, ν), i.e. by translation on B<sub>p</sub>. (5) **Proposition 1**: no Aut(C)-stable, flow-invariant subset of an Aut(C)-stable admissible system contains exactly one periodic orbit over a prime; it contains one in every base class, hence uncountably many. Every input — the (38)/(39) coordinates, the fibration whose fibres are the orbits, the uncountability of B<sub>p</sub> — was re-derived here from the primary text, not imported. The proposition is **sharp**: dropping the Aut(C)-stability of E is exactly what the Theorem-C cuts E(a₀) do, and they satisfy the negated conclusion.

**Scope, stated precisely.** These results are about **X₀ = Spec Z with C-valued points in Deninger's [x-03] framework**, and about **set-level, flow-equivariant** structure only. They do **not** use, and must not be read as using, any topology: the Aut(C)-action is not continuous (finding D-1), so nothing here composes with the 9.3 adjudication's Theorem A, with compactness, or with closure. Proposition 1 constrains **selections that are Aut(C)-stable**; the passage from "canonical" to "Aut(C)-stable" is a definability schema, flagged as such in the note and left flagged here — the theorem-grade content is Corollary 1′ (R-P2), that every Aut(C)-stable admissible class carries full packets. Lemma B rules out the **uniform-threshold** archimedean reading only; averaged, asymptotic and comparative defect-profile conditions are untouched, as the note correctly says, and I add that no candidate for those exists in any source read here. Lemma A is a statement about the **closed-point stratum** of the local theory; it says nothing about the generic stratum Y<sup>⋄</sup><sub>η</sub>, where the Fargues–Fontaine content lives. Nothing in this report bears on the ledger's substrate defects W1/W6/W12, on positivity or Hodge-type clauses (the note's own Z2 quarantine), or on whether any trace formula exists — Road 2's count is now correctly justified as a formal count and remains formal, with DQ-M unchanged. Finally, **the trichotomy D1–D3 stands**: D1 on Proposition 1 (verified, sharp), D2 on Lemma B (verified, strengthened), D3 on Lemma A plus the transport analysis (verified, with the precision of R-A4). After the three MAJOR repairs are applied the note's §0 verdict is, in my judgment, correct as stated and correctly scoped.

---

## 12. Sources — every page read this session

**On-disk primary sources.** Extraction with `pdftotext -layout` (poppler 26.08.0); one display additionally read as a rendered image (`pdftoppm -r 220`), per corpus-routing caveat 1 (no third-party OCR).

* **[x-03]** Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400v4 — `fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf`. Printed page = PDF page (verified on pp. 33, 40, 116). Pages read: **5, 6** (intro: minimal-E remark; "does not give more points"; "the answer is simple, Y<sup>⋄</sup> consists of…"; "the process of completion … was necessary"); **25, 26** (X̌(C) as pairs (x, P̌<sup>×</sup>), (28)–(29), Def. 3.6, Prop. 3.7, Cor. 3.8); **27** (Def. 4.1, (Tors), (Image), Prop. 4.2, (30)–(31)); **28** (Lemma 4.3, conditions before Cor. 4.4, Cor. 4.4, E<sub>tors</sub>/E<sub>max</sub>); **29** ((E<sub>f</sub>, E<sub>fg</sub>, E<sub>fd</sub>, E<sub>fd0</sub>; the inclusion chain; the "additive mod p … not N-invariant" Remark; the *stable*-class definition and the exception for E<sub>max</sub>; functoriality); **30** (Prop. 4.5 proof, Lemma 4.6); **31** (§5 setup, hypothesis on C, choice of ι, (32), (33), C<sub>x₀</sub>); **32** ((34), (35), the (Tors)/finite-cyclic-kernel identification, (36), (37)); **33** ((38), (39), **the fibration display, read by page render**, (40)–(46)); **34** (Prop. 5.1, **Thm 5.2**, (47), (48)); **37** (Remark 5.4, Thm 5.5); **38** (§6: the suspension, φ<sup>t</sup>, Γ<sub>x₀</sub>, **"all R<sup>>0</sup>-orbits … are circles … Γ<sub>x₀</sub> fibres over Ẑ<sup>×</sup><sub>(p)</sub>/p<sup>Ẑ</sup> … with fibres the R<sup>>0</sup>-orbits"**); **39** (**Thm 6.1**, the packet statement, the X<sup>•</sup>-description remark, the Arakelov-compactification discussion); **40** (§7 opening: **the pointwise-convergence topology**; Lemma 7.1; the S4 question with both alternatives); **89** (§14 setup, N₀ = p<sup>Z</sup>, Def. 14.1); **90** (Def. 14.1 diagram, (163), Def. 14.2); **91** (continuity discussion, Prop. 14.3); **93** (Fontaine (170)–(171), A<sub>inf</sub>(X), the [CD14] presentation); **94** (**Def. 14.5**, (172)–(174), **Prop. 14.7**); **95** (proof of 14.7 with the ultrametric estimate and the (175)-diagram second proof); **98** (Prop. 14.11, (181)); **99** (**Def. 14.12 = (183)**, (184)–(185), **the "I do not know how to transport" Remark**); **100** (**Prop. 14.13**, **Prop. 14.14**, (186)–(191)); **101** (proof of 14.14, (192)–(194)); **104** (**Remark 14.17**, §15 opening, Lubin–Tate setup, (197)); **105** (tilting review, (198)–(200), the "From now on let o be…" hypothesis sentence); **106** (**k algebraically closed; k ⊆ o<sup>♭</sup>**; H<sub>κ₀</sub>(o<sup>♭</sup>), (201)–(203)); **113** (the (η,s) and (s,s) strata, "the ring homomorphisms P̂<sup>♭</sup><sub>y</sub> : κ ↪ k ⊂ o<sup>♭</sup>", (219)–(220), **Thm 15.6(1)**); **114** (**Thm 15.6(2)–(6)**, (221)–(226), the closing Remark); **115** (proof of 15.6(6), **Prop. 15.7**, (227)–(228)); **116** (**Prop. 15.8** and its proof).
* **[x-06]** Deninger, *Primes, knots and periodic orbits*, arXiv:2301.11643 — `fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf`. Pages read: **10** (W<sub>rat</sub>(X)(S), the Teichmüller map, (11)); **11** (**Thm 4.1**, the suspension X₀ and φ<sup>t</sup>, the "too many periodic orbits / we can only impose an admissible condition E" paragraph, **Thm 4.2**); **12** (Thm 4.2 continued — **orbit length log N x₀, the fibre space over Aut(F̄<sub>p</sub><sup>×</sup>)/Aut(F̄<sub>p</sub>) with fibres the compact orbits**, "all of which have length log N x₀ i.e. log p"; Thm 4.3; the infinite-dimensionality paragraph; X<sup>•</sup>(C)<sub>in</sub>); **13** (**Thm 4.4** and the non-homeomorphism remark; Kucharczyk–Scholze; the Steinberg-relations sentence).
* **[D25]** Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329v1 — `fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf`. Pages read: **2–3** (introduction, the "stronger descent conditions" sentence, verbatim).
* **[r3s-08]** Morishita, arXiv:2508.15971 — `fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf`. Text extracted; **not consulted for any claim in this report**.

**Program-internal documents read.** `results/c3-r/probe-9.3-adjudication.md` (in full); `results/c3-r/probe-9.4-note.md` (in full, 136 lines); `results/corpus-routing.md` standing caveats 1–20.

**Recalled-and-unused, flagged [RU] (carries no weight, and is not used anywhere in this report's own arguments).** The Witt-vector identity V W(A) = p W(A) for perfect A of characteristic p, invoked only to *describe* what the note's converse argument was reaching for; the repair R-A2 replaces it with an argument that reads nothing off-disk.

— end of referee report O —
