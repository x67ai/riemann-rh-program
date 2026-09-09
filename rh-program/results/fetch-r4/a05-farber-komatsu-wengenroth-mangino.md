# Round-4 ingest report — agent a05-farber-komatsu-wengenroth-mangino (Session 18, 2026-09-09)

**Scope:** ingest-only, per `results/fetch-r4/BRIEF.md`. Four list items:

| Item | File | Source as listed | Flagged at |
|---|---|---|---|
| 6a (P2) | `fetched-r4/r4-06a-farber-2004-topology-of-closed-one-forms-SMM108.pdf` (IMAGE-ONLY, 247 pp.) | M. Farber, *Topology of Closed One-Forms*, Math. Surveys and Monographs 108, AMS 2004, §2.1 | `results/c3-r/s16/novelty/adjudication.md` §4 item 4 |
| 10 (P3) | `fetched-r4/r4-10-komatsu-1967-projective-injective-limits-jmsj-19-366-383.pdf` (text layer) | H. Komatsu, J. Math. Soc. Japan 19 (1967) 366–383, Thm 6′ | `results/c3-r/s14/novelty/adjudication.md` §4 item 2 |
| 11 (P3) | `fetched-r4/r4-11-wengenroth-1996-acyclic-inductive-spectra-studia-120-247-258-SCAN.pdf` (IMAGE-ONLY 2-up scan, 7 pp.) | J. Wengenroth, *Acyclic inductive spectra of Fréchet spaces*, Studia Math. 120 (1996) 247–258 | `results/c3-r/s14/novelty/adjudication.md` §4 item 3 |
| 14 (P3) | `fetched-r4/r4-14-mangino-1997-LF-spaces-tensor-products-math-nachr-186-149-162.pdf` (text layer, garbled in places) | E. M. Mangino, *(LF)-spaces and tensor products*, Math. Nachr. **185** (1997) 149–162 per list; file header says **186** | `results/c3-r/s14/novelty/adjudication.md` §4 item 5 |

**Method:** image-only files read by vision from `pdftoppm -r 110` renders; text-layer files located with `pdftotext`, and every formula-bearing quotation checked against a page render. Calegari, *Foliations and the Geometry of 3-Manifolds* (OUP 2007), the companion citation for item 6a, is NOT on disk (still missing; see item 6a §3). Sections are appended as finished.

---

## ITEM 6a (P2) — Farber, *Topology of Closed One-Forms*, §2.1

### §1 Identity verification

- **File:** `fetched-r4/r4-06a-farber-2004-topology-of-closed-one-forms-SMM108.pdf`, 247 PDF pages, letter size, **image-only** (no text layer; PDF metadata title "Topology of Closed One-Forms - M. Farber (AMS, 2003) WW.djvu" — a DjVu-to-PDF conversion of a scan). Read by vision from `pdftoppm -r 110` renders.
- **What it is (from the copyright page, PDF 2):** Michael Farber, *Topology of closed one-forms*, Mathematical Surveys and Monographs, ISSN 0076-5376, v. 108, ISBN 0-8218-3531-9; "© 2004 by the author"; LC data "QA614.7.F37 2003", control number 2003062825; 2000 MSC Primary 58E05, 57R70, Secondary 57R30. The "2003" in the file's metadata title is the LC cataloguing year; the imprint is **2004**, so the list's citation (SMM 108, AMS 2004) is EXACT. Front matter: Contents (PDF 3–4 = printed v–vi), Preface (PDF 5 = printed vii).
- **PDF ↔ printed offset (two regimes — a blank page is missing from the scan):** PDF 33 = printed 24 and PDF 34 = printed 25 (offset **+9**); PDF 43 = printed 35 (Chapter 2 opening) and PDF 44–46 = printed 36–38 (offset **+8**). The verso p. 34 preceding the Chapter 2 opening was evidently dropped when the scan was made. PDF 246–247 = printed 245–246 (Index; offset +1 at the end, so further blanks are missing later in the book — anyone citing a page past p. 38 must re-verify the offset locally). Bibliography ends at printed 244 = PDF 245.
- **Contents (PDF 3, verbatim for Chapter 2):** "Chapter 2. The Novikov Inequalities 35 / 2.1. Closed 1-forms 35 / 2.2. Geometry of Novikov theory 38 / 2.3. The Novikov inequalities 45". So **§2.1 = printed pp. 35–38 = PDF 43–46**, read in full.
- **Companion citation NOT on disk:** D. Calegari, *Foliations and the Geometry of 3-Manifolds*, Oxford Math. Monographs, OUP 2007, §9.3 — still missing (only a draft PDF with different section numbering was ever seen, per the s16 adjudication §4 item 4). Nothing below rests on it.

### §2 What the program asked for

`results/c3-r/s16/novelty/adjudication.md` §4 item 4: "**M. Farber, *Topology of Closed One-Forms*, Math. Surveys and Monographs 108, AMS 2004, §2.1**, and **D. Calegari, *Foliations and the Geometry of 3-Manifolds*, Oxford Math. Monographs, OUP 2007, §9.3** — the two sources **KMNT themselves cite** ("[7, 9.3], [19, 2.1]", published p. 331) for the rank-one/fibration characterization of a period group. … Value: **MEDIUM** for N-D/N-G — a textbook rank statement for period groups would sharpen the credit line but cannot cover B1′'s open, non-compact-leaf case."

Context (same file, §1 N-D and the zoo IV.13 block): the "length-group kill" rests on the rank of the period group Λ_S = im([ω_S] : H₁(M₀; Z) → R); KMNT's Prop. 2.10 is the printed rank-one dichotomy, and the question is what its two cited textbook sources actually state.

### §3 The answer from the sources

**3.1 How KMNT cite Farber and Calegari** (`fetched-r3/r3s-36-kmnt-2021-mjm-14-323-348-PUBLISHED-SWEEP-F-FETCH.pdf`, text layer; PDF 9 = printed **331**; PDF 7 = printed 329):

> "We note that the class of FDS³'s of bundle foliation over S¹ is characterized by the period group. Although this may be known (cp. [7, 9.3], [19, 2.1]), we give a proof in the following, for the sake of readers.
> **Proposition 2.10.** Let S be an FDS³. If S is of type I or of type III-1, then the period group Λ_S = Z. Conversely, if the Λ_S has rank one (namely, Λ_S ≃ Z) and M₀ is connected, then S is of type I or of type III-1." (printed p. 331)

The converse half of their proof (p. 331): "suppose that S = (M, F, φ) is an FDS³ with M₀ being connected and Λ_S = λZ for some λ ∈ R^× so that [ω_S](H₁(M₀; Z)) = λZ. Fix a base point p₀ ∈ M₀, and define the map ϖ : M₀ → S¹ by ϖ(p) := exp((2πi/λ)∫_γ ω_S), where γ is a path from p₀ to p. Then we see easily that λϖ*(dθ) = ω_S. By Definition 1.10 of ω_S, ϖ is a fibration and F consists of fibers of ϖ." — this is, step for step, Farber's proof of Lemma 2.1 below (the map exp(2πi∫ω)), plus the nonvanishing of ω_S (Definition 1.10 makes ω_S a closed 1-form with ker ω_S = TF, so ϖ is a submersion) to turn the map into a fibration.

Definition of the period group (printed p. 329): "**Definition 1.10.** Let S = (M, F, φ) be an FDS³. We call the smooth closed 1-form in Lemma 1.9 the canonical 1-form of S and denote it by ω_S. The de Rham cohomology class of ω_S defines the period homomorphism [ω_S] : H₁(M₀; Z) → R; [ℓ] ↦ ∫_ℓ ω_S, and the period group of S is defined by the image of [ω_S], which we denote by Λ_S."

Bibliography entries (KMNT p. 346–347): "[7] D. Calegari, Foliations and the geometry of 3-manifolds, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2007. MR2327361" and "[19] M. Farber, Topology of closed one-forms, Mathematical Surveys and Monographs, 108, American Mathematical Society, Providence, RI, 2004. MR2034601". So "[19, 2.1]" = Farber §2.1 (there is no "Theorem 2.1" reference intended beyond what §2.1 contains; §2.1 has exactly one lemma, Lemma 2.1, and one corollary, Cor. 2.2).

**3.2 Farber §2.1 "Closed 1-forms", verbatim** (printed 35–38 = PDF 43–46; read by vision):

Opening (p. 35): "Here we recall the standard background material concerning closed 1-forms. Later in Chapter 10 (see §10.2) we will study a more general notion of a closed 1-form defined on general topological spaces. **Basic notions.** Let M be a closed smooth manifold. A *1-form* ω on M is a smooth section of the cotangent bundle T*M → M. … A 1-form ω is called *closed* if dω = 0, where d is the exterior derivative."

p. 36, last two paragraphs of "Examples": "Examples of closed 1-forms on manifolds can be obtained as follows. Let f : M → S¹ be a smooth map. The pullback ω = f*(dθ) is a closed 1-form on M. The zeros of ω are nondegenerate if and only if f has only Morse critical points. Varying the circle-valued map f : M → S¹, we obtain a variety of induced closed 1-forms ω = f*(dθ). Below we characterize the closed 1-forms which can be obtained in this way. / A closed 1-form on a closed manifold may have no zeros. This cannot happen with a function, since any function necessarily has a minimum and a maximum, which yield at least two critical points."

p. 37, first paragraph: "Closed 1-forms without zeros appear systematically in the following situation. Consider a closed manifold F and a diffeomorphism h : F → F. Let M be *the mapping torus* of h, i.e., the factor-space of F × [0, 1], in which any point (x, 0) is identified with (h(x), 1). M has naturally a smooth manifold structure and there is a projection p : M → S¹, where p(x, t) = t. Here we understand the circle as the interval [0, 1] with identified end points. The map p is a smooth fibration. The pullback ω = p*(dθ) is a closed 1-form on M having no zeros."

p. 37, "**Periods and rank.** One of the important features of a closed 1-form is its de Rham cohomology class ξ = [ω] ∈ H¹(M; R). It vanishes ξ = 0 if and only ω is exact, i.e., ω = df, where f : M → R is a smooth function. / Given a 1-form ω and a smooth path γ : [0, 1] → M, the line integral ∫_γ ω ∈ R is well defined. By the Stokes Theorem, the condition that ω is closed is equivalent to the property that the integral ∫_γ ω remains unchanged under any continuous homotopy of the path γ with fixed end points. Therefore, a closed 1-form defines a homomorphism from the fundamental group π₁(M, x₀) to R. It acts as follows: [γ] ↦ ∫_γ ω, [γ] ∈ π₁(M, x₀). Here R is viewed as the additive group of real numbers. Since R is abelian, it factors uniquely through the Hurewicz homomorphism h : π₁(M, x₀) → H₁(M). The obtained homomorphism
(2.1)  Per_ξ : H₁(M) → R
is *the homomorphism of periods* of ω. It depends only on the cohomology class ξ = [ω] ∈ H¹(M; R). Because of the isomorphism H¹(M; R) ≃ Hom(H₁(M); R), the homomorphism of periods Per_ξ determines entirely the cohomology class ξ and any group homomorphism H₁(M) → R can be realized as the homomorphism of periods of a closed 1-form."

p. 37: "**LEMMA 2.1.** *A closed 1-form ω on a smooth manifold M can be represented as ω = f*(dθ) where f : M → S¹ is a smooth map, if and only if the de Rham cohomology class ξ = [ω] ∈ H¹(M; R) of ω is integral, i.e., ξ ∈ H¹(M; Z).*
PROOF. Let f : M → S¹ be a smooth map to the circle and let ω = f*(dθ) be the induced closed 1-form. Then the number ∫_γ ω = ∫_γ f*(dθ) = ∫_{f_*(γ)} dθ ∈ Z is an integer since it coincides with the degree of the loop f_*(γ) on the circle. This shows that the homomorphism of periods of any closed 1-form ω = f*(dθ) takes integral values, i.e., its cohomology class belongs to H¹(M; Z). / Conversely, suppose that ω is a closed 1-form with all integral periods. Let us fix a base point x₀ ∈ M and define the following map f : M → S¹, f(x) = exp(2πi · ∫_{x₀}^{x} ω). f is well defined since the indeterminacy in the choice of the path connecting the base point x₀ with x results in adding an integer to the integral ∫_{x₀}^{x} ω which then has no effect on f. It is clear that ω = f*(dθ) as required. □"

p. 38 (the rank paragraph, in full): "The image of the period homomorphism Per_ξ is a finitely generated free abelian subgroup of R. The *rank* of a cohomology class ξ ∈ H¹(M; R) is the rank of the image of Per_ξ; compare Definition 1.43. We denote the rank of ξ as rk(ξ). It is bounded above by the first Betti number of M, rk(ξ) ≤ rk H₁(M). If the homology classes of closed curves γ₁, …, γ_m in M form a free basis of H₁(M)/Tor, then rk(ξ) equals the maximal cardinality of a subset of the periods ⟨ξ, [γ₁]⟩, …, ⟨ξ, [γ_m]⟩ which is linearly independent over Q. The rank of ξ equals zero if and only if ξ = 0. / Classes of rank 1 are real multiples of integral cohomology classes ξ = λξ₀, where ξ₀ ∈ H¹(M; Z) and λ ∈ R*. Indeed, if the image of Per_ξ is a cyclic subgroup of R, then all periods are integral multiples of a minimal period λ ∈ R. Hence the class λ⁻¹ξ has all integral periods and belongs to H¹(M; Z). / The subgroup H¹(M; Z) ⊂ H¹(M; R) of integral classes is a *lattice* in the vector space H¹(M; R), i.e., it is a finitely generated free abelian subgroup with its rank equal to the dimension of H¹(M; R). The set of rank 1 classes can be viewed as the union of all the straight lines in H¹(M; R) passing through the origin and points of the integral lattice. Since the union of these lines is dense, we conclude: / **COROLLARY 2.2.** *The set of rank 1 classes is dense in H¹(M; R).*"

Cross-referenced definition (printed p. 25 = PDF 34, §1.6, for a finite CW complex X): "**DEFINITION 1.43.** The rank of a cohomology class ξ ∈ H¹(X; R) is defined as rk(ξ) = rk(H₁(X)) − rk(ker(ξ)). / In other words, rk(ξ) is the maximal number of rationally independent periods ⟨ξ, z⟩ ∈ R, where z ∈ H₁(X). / Any nonzero class ξ ∈ im[H¹(X; Q) → H¹(X; R)] has rank 1. Therefore the set of rank 1 classes is dense in H¹(X; R)." (Here rk(ker ξ) is the rank of the kernel of ξ : H₁(X) → R as an abelian group.)

**3.3 Plain-English reading.**

*The source says:* (a) the period group of a closed 1-form on a closed manifold is a finitely generated free abelian subgroup of R (because it is the image of H₁(M), finitely generated) and its rank is the maximal number of Q-independent periods — this is exactly the "rank" the program's IV.13 uses, and it is printed with the bound rk(ξ) ≤ b₁(M) (p. 38); (b) rank one ⟺ ξ = λξ₀ with ξ₀ integral (p. 38, proved in two lines); (c) integral ⟺ ω = f*(dθ) for a smooth circle-valued map f, with the explicit map f = exp(2πi∫ω) (Lemma 2.1, p. 37); (d) the mapping-torus example shows a fibration over S¹ yields a nowhere-zero closed 1-form p*(dθ) (p. 37).

*The source does NOT say:* the converse Tischler-type statement "a nowhere-vanishing closed 1-form of rank one is (a multiple of) the pullback of dθ under a **fibration** M → S¹" is not stated as a theorem in §2.1. It is one sentence away: by (b)+(c), λ⁻¹ω = f*(dθ); if ω has no zeros then f is a submersion, and a submersion of a closed manifold onto S¹ is a fibration (Ehresmann). Farber leaves that sentence unsaid; his §2.1 is about closed 1-forms with zeros (Novikov theory), and the book cites neither Tischler (Topology 9 (1970)) nor Cantwell–Conlon — its bibliography (PDF 236–245 checked at the T entries: [Ta] Takens, [Tam] Tamura, [Ta1–3] Taimanov, [Thom1–2]) has no Tischler entry, and the index (printed 245–246) has no entry for "Tischler", "fibration" or "period group" (it has "Homomorphism of periods, 37" and "Rank of a cohomology class, 25").

*I infer:* KMNT's "cp. [19, 2.1]" points at exactly the two printed facts (b) and (c) (their proof of Prop. 2.10 reproduces Farber's exp(2πi∫ω) construction verbatim); the fibration conclusion is KMNT's own added step, which is why they write "Although this may be known … we give a proof … for the sake of readers." For the program's credit line (N-D/N-G, zoo IV.13): Farber §2.1 supplies a clean textbook citation for **"the period group of a closed 1-form on a closed manifold is a finitely generated free abelian group of rank ≤ b₁(M), and rank one means a real multiple of an integral class"** (Farber 2004, p. 38, with Definition 1.43 p. 25 and Lemma 2.1 p. 37) — a statement for **closed** manifolds only, as the adjudication anticipated: it does not touch the open, non-compact-leaf case of B1′, and it does not mention foliations, flows, or length spectra at all. Nothing in Farber §2.1 contradicts anything on the program's record. Calegari §9.3 remains unread (not on disk).

### §4 Other things in the source worth knowing

- §10.2 (per p. 35) generalizes closed 1-forms to arbitrary topological spaces (Čech class; index p. 163–165); Chapter 10 also has "Asymptotic cycle of a flow, 199", "Lyapunov 1-form of a flow, 198", "Chain recurrent set R_ξ, 201" (index) — Schwartzman asymptotic cycles [Sch] Ann. Math. 66 (1957) and [Sch1] PNAS 48 (1962) are in the bibliography (p. 243–244). Possibly relevant to the program's transverse-measure / asymptotic-cycle vocabulary; not read.
- Theorem 1.44 (p. 25): for rk(ξ) > 1 there is a sequence of rational classes ξ_n → ξ vanishing on ker ξ with the same Novikov numbers — the density-of-rank-one-classes principle (Cor. 2.2, p. 38) in Novikov-number form.
- "Singular foliation, 125", "Transitive closed 1-form, 132", "Calabi Theorem, 132" (index) — Chapter on intrinsically harmonic forms; not read.

### §5 Caveats for `corpus-routing.md`

- `r4-06a`: image-only DjVu scan; the printed-page offset is **not constant** (+9 through p. 25, +8 at pp. 35–38, +1 by the index) because blank versos were dropped — locate every page by rendering, never by arithmetic.
- `r4-06a`: KMNT's "[19, 2.1]" is a **section** reference (§2.1, pp. 35–38), not "Lemma 2.1"; both exist.
- Calegari 2007 §9.3 is still not on disk; the draft PDF seen in s16 has different section numbers.

