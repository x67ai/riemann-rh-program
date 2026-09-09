# Round-4 ingest report — agent a13-hajek

Session 18, 2026-09-09. Ingest-only; no verdict changes; nothing in the record edited.

## Files

- ITEM 13b: `fetched-r4/r4-13b-hajek-1971-parallelizability-revisited-proc-ams-27-77-84.pdf` — O. Hájek, *Parallelizability revisited*, Proc. AMS 27 (1971) 77–84 (JSTOR scan).
- Companion (item 13a, Dugundji–Antosiewicz 1961) was done in `results/fetch-r4/a07-parallelizable-sullivan-plante.md` §1 13a, §3 item 13; this report reconciles with it in §3(d).
- Also on disk, ignore: `fetched-r4/r4-13b-WRONG-FILE-proc-ams-30-4-dec-1971-cover-plus-index-vols-21-30-HAJEK-ABSENT.pdf` (the mis-delivery a07 documented; renamed by the sponsor).

(Sections appended below as each is finished.)

## §1 Identity verification

### 13b — `fetched-r4/r4-13b-hajek-1971-parallelizability-revisited-proc-ams-27-77-84.pdf`
- **What it is:** Otomar Hájek, *Parallelizability revisited*, Proceedings of the American Mathematical Society, **Volume 27, Number 1, January 1971**, pp. 77–84. JSTOR scan (cover sheet: "Vol. 27, No. 1 (Jan., 1971), pp. 77-84", Stable URL jstor.org/stable/2037265, accessed 08-03-2015). Running head on PDF p. 2 (verified by vision): "PROCEEDINGS OF THE AMERICAN MATHEMATICAL SOCIETY, Volume 27, Number 1, January 1971"; title "PARALLELIZABILITY REVISITED¹", byline "OTOMAR HÁJEK"; footer "Received by the editors March 13, 1970. AMS 1969 subject classifications. Primary 3465; Secondary 5482, 5440." Affiliation (p. 84): Case Western Reserve University, Cleveland, Ohio 44106. NSF grants GP-8961, GP-12261.
- **Page count / offset:** 9 PDF pages = 1 JSTOR cover + 8 article pages. **Printed page = PDF page + 75** (PDF 2 = 77, PDF 9 = 84). Last article page is **84** (PDF 9: references 2–12 and the address; nothing follows). So the AMS 10-volume index's "77–85" (see a07 §1 13b, verified there on the wrong-file delivery) is a misprint; the article itself, the JSTOR cover, and Crossref (a07) all say **77–84**. The list's citation is EXACT: volume 27, 1971, pp. 77–84. No edition caveats (journal article, one version).
- **Text layer:** present (iText-produced JSTOR OCR); prose is clean, math is garbled (π rendered "ir"/"7r", ∈ as "E"/"C", subscripts lost, ∅ as "0", "Tichonov" and "Lindelöf" mangled). Every statement quoted in §3 was verified by vision on rendered pages (130 dpi, PDF pp. 2–8 = printed 77–83); p. 84 (references) read from the text layer and checked by eye where cited.
- **Match with the list:** matches EXACTLY. Note the sponsor's earlier mis-delivery (the Proc. AMS 30(4) index volume, documented in a07 §1 13b) is now on disk as `r4-13b-WRONG-FILE-…-HAJEK-ABSENT.pdf`; ignore it.

## §2 What the program asked for

Verbatim from `results/c3-r/s14/novelty/adjudication.md` §4 item 4 (line 143): "**H. A. Antosiewicz, J. Dugundji, Ann. of Math. 73 (1961) 543–555; O. Hájek, Proc. AMS 27 (1971) 77–84** — the exact "time function / section" wording of the parallelizability theorem. AMS PDF → HTML. Bears on the C3 citation sentence only."

The citation sentence (`results/c3-r/s14/novelty/sweep-O.md` C3, lines 189–193): "A positive function W with W∘φ^t = e^t·W is the exponential of a **time function** f = log W satisfying f(φ^t x) = t + f(x). The existence of such a function is the classical characterization of a *parallelizable* flow, and parallelizable ⟺ dispersive ⟺ **all limit sets empty** ⟺ no nonempty compact invariant set. This is a 65-year-old body of theory that the program's notes nowhere cite." The adjudication's own caveat (line 61): "Antosiewicz–Dugundji … and Hájek, *Parallelizability revisited*, Proc. AMS 27 (1971) 77–84, were **not** opened … their exact "time function" wording carries no weight here." What was applied to the record (R5; `s14/qstar-adjudication.md` §4 NOVELTY block, line 105): "The device — a positive function conjugating the flow to translation, whose existence forbids compact invariant sets — is the classical parallelizable/dispersive framework … (Ann. of Math. 73, 543–555; Hájek, Proc. AMS 27 (1971); Bhatia–Szegő 1970 — named, not opened). That framework assumes locally compact state spaces and a globally wandering flow".

a07 (§3 item 13) answered the Dugundji–Antosiewicz half: "time function" occurs nowhere in the 1961 paper; its datum is a section S with the crossing time t_s continuous (Definition 1, Theorem 1, p. 544, any metric space); the additivity identity is never written; parallelizable ⟺ dispersive is Theorem 3 (p. 548, locally compact separable metric); the "limit sets empty / compact invariant set" clauses are not in the paper. This report does the Hájek half and gives the combined verdict in §3(d).

## §3 The answer from the source — Hájek 1971

Notation: Hájek writes the flow as xπt (x ∈ X, t ∈ R¹); C_x = orbit, K_x = orbit closure, L_x = limit set, D_x = prolongation, J_x = prolongational limit set; e: X → X/C the orbit-space quotient. All quotations below verified by vision.

### (a) Statement of purpose, and what is new relative to Dugundji–Antosiewicz [4]

**Abstract (p. 77):** "A classical theorem (Antosiewicz and Dugundji) states that a dynamical system on a locally compact separable metric space is parallelizable if and only if it is dispersive. In this paper it is shown that separability may be omitted, and, under a further condition, local compactness weakened to local Lindelöfness. The crucial step consists in a purely topological characterization of complete instability."

**§1 Introduction (p. 77), first two paragraphs:** "The well-known Antosiewicz-Dugundji theorem on parallelizability ([4, Theorem 3]; also see [8, first theorem in 2.4]) reads thus: a dynamical system on a locally compact separable metric space is parallelizable if and only if it is dispersive. The aim of the present paper is to obtain a more general theorem of the same type; one of its corollaries shows that separability may be omitted entirely. It is also shown how local compactness may be replaced by local Lindelöfness, thereby obtaining one of the few theorems in dynamical system theory which apply, e.g., to separable normed linear spaces.
Our principal results are corollaries to Theorem 7. §1 is introductory, §3 has the function of an appendix. The question of parallelizability is first reduced to the purely topological problem of finding cross-sections for fiber bundles (Theorem 6 and Lemma 5). An application of known results then yields Theorem 7. (The method just described is not novel: one may recognize the proof of Theorem 3 in [4] as a special case of the construction of cross-sections for fiber bundles [11, 12.2]; an improvement of the latter has led to a generalization of the former.)"

Reference [4] (p. 84) is printed as "J. Dugundji and H. A. Antosiewicz, Parallelizable flows and Lyapunov's second method, Ann. of Math. (2) 73 (1961), 543–555. MR 23 #A395." — i.e., Hájek himself uses the order "Antosiewicz–Dugundji" in prose and "Dugundji and Antosiewicz" in the bibliography. [8] = Nemyckiĭ, Uspehi Mat. Nauk 4 (1949); [11] = Steenrod, *The topology of fibre bundles*; [7] = Markus, *Parallel dynamical systems*, Topology 8 (1969) 47–57; [12] = Ura, Math. Systems Theory 3 (1969) 1–16; [1] = Bhatia–Hájek, *Theory of dynamical systems* I, IV (1969 technical notes); [5] = Hájek, *Dynamical systems in the plane* (1968).

### (b) Definitions, verbatim (p. 78 unless noted)

**Setting (pp. 77–78):** "If π is a dynamical system on a topological space X, then the value of π at (x, t) ∈ X × R¹ is written as xπt (thus the axioms are that π: X × R¹ → X is continuous, xπ0 = x, (xπt)πs = xπ(t+s)); similarly for MπT where M ⊂ X, T ⊂ R¹. A subset M ⊂ X is called invariant iff MπR¹ = M." — The base class is an **arbitrary topological space**; hypotheses (Hausdorff, Tichonov, regular, locally compact, metrizable) are added theorem by theorem.

**Limit sets:** "Given a point x ∈ X, we define C_x = xπR¹ (the trajectory or orbit, through x), K_x = C̄_x (orbit-closure); next we define L_x, D_x, J_x (limit set, prolongation, prolongational limit set) as follows: y ∈ L_x iff xπt_i → y for some |t_i| → ∞; y ∈ D_x iff x_iπt_i → y for some x_i → x, t_i ∈ R¹; y ∈ J_x iff x_iπt_i → y for some x_i → x, |t_i| → ∞." Display (1): C_x ⊂ K_x ⊂ D_x, L_x ⊂ J_x, with K_x ⊃ L_x and D_x ⊃ J_x (vertical ∪ signs); "and, if X is Hausdorff, K_x = C_x ∪ L_x, D_x = C_x ∪ J_x."

**Poisson unstable / divergent / wandering / dispersive:** "A point x ∈ X is called Poisson unstable, divergent, wandering, dispersive iff, respectively, x ∉ L_x, L_x = ∅, x ∉ J_x, J_x = ∅. Iff this holds for all points x ∈ X, then the entire system is termed Poisson unstable, divergent, completely unstable (= almost dispersive in [10]), dispersive, respectively. Obvious relations between these concepts follow from (1)."

**Parallelizable, and the section formulation:** "A dynamical system π on X is called parallelizable iff there is a homeomorphism between X and a space of the form Y × R¹, such that, whenever x maps into (y, s), also xπt maps into (y, s+t) for all t. Or equivalently [4], there exists a global section S for π: a subset S ⊂ X such that, for every x ∈ X, there is xπθ ∈ S for a unique θ ∈ R¹, and the mapping x ↦ θ is continuous (then we may take Y = S)."

**Orbit space:** "The set of equivalence classes modulo C will standardly be endowed with the quotient topology, denoted by X/C, and called the orbit space (of π). The canonical quotient map X → X/C will consistently be denoted by e: X → X/C". **1. Lemma.** "e: X → X/C is a continuous open surjection."

**Regularity property (p. 79, §2):** "DEFINITION. A dynamical system has the regularity property iff every invariant neighborhood of any point contains a closed invariant neighborhood of the point."

**Local section (p. 80, Lemma 4, used without a separate definition; the proof refers to "the Whitney-Bebutov theorem (existence of local sections)" and to [5, VI, 2.12]).** **Cross-section (p. 81):** "Recall that a cross-section to a quotient map f: X → Y is the range of a continuous map s: Y → X such that f ∘ s is the identity map of Y."

### (b′) The theorems, verbatim

**2. Lemma (p. 79).** "Let π be a system on a regular phase space X. Then 1. π has the regularity property iff the orbit space X/C is regular. 2. If π is parallelizable, then it has the regularity property."

**3. Lemma (p. 80).** "Let X be Hausdorff. If π is completely unstable with the regularity property, then it is dispersive, and X/C is Hausdorff. If X is locally compact, then, conversely, dispersiveness implies the regularity property; in non-locally-compact X, it need not." (Proof, p. 80, contains the remark: "in dispersive systems, VπR¹ is closed whenever V is compact (actually this is necessary and sufficient for dispersiveness).")

**4. Lemma (p. 80).** "In a Tichonov phase space, a point x is wandering (i.e., x ∉ J_x) if and only if there exists a local section S containing x such that SπR¹ is open and on it the system is parallelizable (or dispersive)." Proof: "That for wandering points x such a local section exists is Lemma 3 in [4] (also see [12, Theorem 3]), in case the phase space is locally compact and metrizable. For our situation use the generalization of the Whitney-Bebutov theorem (existence of local sections) applying to Tichonov spaces [5, VI, 2.12]. Then on SπR¹ our system reduces to the parallel system over S × R¹."

**5. Lemma (p. 80).** "Let π be a system on a space X. Every global section for π is a cross-section to the quotient map e: X → X/C; if π is completely unstable and X Hausdorff, the two concepts coincide." Proof (p. 81), the passage where the crossing-time map appears: "Since π is completely unstable and hence nonperiodic, there exists a mapping θ: X → R¹ such that θ(x) is the unique element in R¹ with xπθ(x) ∈ S. It remains to show that θ is continuous, i.e., that x_iπt_i ∈ S ∋ xπt, x_i → x imply t_i → t. … Let t′ be any accumulation point of the t_i. Then t′ = ∞ is excluded by complete instability and x_i → x, x_iπt_i → xπt ∈ C_x; and for finite t′, closedness of S yields t′ = t. Thus indeed t_i → t."

**6. Theorem (p. 81).** "For a system π on a Tichonov space X, the following conditions are mutually equivalent: 1. π is completely unstable. 2. e: X → X/C is the projection of a fiber bundle with fiber R¹." (Remark before the proof: "Part of the proof parallels that of Theorem 3 in [7]. However, there are so many points of difference (differentiability and special phase spaces in [7]) that it seemed advisable to give our proof at length.")

**7. Theorem (pp. 81–82) — the basic theorem.** "Let π be a dynamical system on a Tichonov space X, and assume that (*) X/C is paracompact. Then π is parallelizable if and only if it is completely unstable." Proof (p. 82): "Since parallelizable systems are completely unstable, we need only prove one implication. Let π be completely unstable. According to Theorem 6, e: X → X/C is the projection of a fiber bundle with R¹ as fiber. From the assumptions, both X and X/C are regular, so that π has the regularity property (Lemma 2). If [sic] follows easily that X/C is a T₁ space, and hence a Hausdorff space. Thus we have a fiber bundle with base space paracompact Hausdorff, and fiber R¹, an absolute retract for normal spaces. According to [11] (p. 218, referring to [6]), there exists a cross-section to e; from Lemma 5, this is then a global section for π, and so π is parallelizable."

**8. Corollary (p. 82).** "If π is a dynamical system on a Hausdorff paracompact locally Lindelöf space, then π is parallelizable if and only if it is completely unstable and has the regularity property."

**9. Corollary (p. 82).** "If π is a dynamical system on a Hausdorff paracompact locally compact space, then π is parallelizable if and only if it is dispersive." Proof: "Lemma 3 reduces this to Corollary 8; local compactness implies local Lindelöfness."

**10. Corollary (p. 82).** "If π is a system on a metrizable locally separable space, then π is parallelizable if and only if it is completely unstable and has the regularity property."

**11. Corollary (p. 82).** "On a space X with metric ρ, let π be a system which is Liapunov stable in the sense that, for every ε > 0, there exists δ > 0 with ρ(xπt, yπt) < ε whenever ρ(x, y) < δ. Then π is parallelizable if and only if it is Poisson unstable." (Proof: "For Liapunov stable systems we have L_x = J_x, so that Poisson instability is equivalent to complete instability. The assertion now follows from Theorem 7, since X/C is metrizable.")

**§3 (p. 83):** 12. Proposition (regular locally compact ⟹ paracompact iff direct sum of regular locally compact σ-compact spaces); 13. Proposition (regular locally Lindelöf ⟹ paracompact iff direct sum of regular Lindelöf spaces); 14. Corollary ("Let p: X → Y be the projection of a bundle space, and assume that X is paracompact and locally Lindelöf, Y is regular, the fiber F is connected. Then Y is paracompact."); and a CONJECTURE ("Let p: X → Y be the projection of a fiber bundle with R¹ as fiber (or merely a Lindelöf fiber), and assume that Y is regular. If X is paracompact then so is Y.").

**Which class of spaces.** The definition of parallelizable and its global-section equivalent: any topological space (p. 78; the equivalence is credited to [4]). Theorem 6 and Theorem 7: Tichonov (completely regular Hausdorff) X, plus (*) X/C paracompact for Theorem 7. Corollary 8: Hausdorff paracompact locally Lindelöf. Corollary 9: Hausdorff paracompact locally compact — **no metric, no separability**. Corollary 10: metrizable locally separable. Corollary 11: metric, Liapunov stable. None of Hájek's statements is on an arbitrary metric space without further hypotheses, and none is on a non-Hausdorff space.

### (c) Does "time function" or f(φ^t x) = t + f(x) occur anywhere in Hájek?

**No.** "time function" (and "time-function") occurs nowhere in the text layer (0 hits) and nowhere on the rendered pages 77–84. The only real-valued crossing-time map in the paper is the **unnamed** θ: X → R¹ of p. 78 ("the mapping x ↦ θ is continuous") and p. 81 (Lemma 5 proof: "θ(x) is the unique element in R¹ with xπθ(x) ∈ S"). Hájek never writes any additivity identity for θ. (I infer, not the paper: with his convention xπθ(x) ∈ S, θ satisfies θ(xπt) = θ(x) − t — the **opposite sign** to the record's f(φ^t x) = f(x) + t; Dugundji–Antosiewicz's t_s, with f(p, −t_s(p)) ∈ S, has t_s(f(p,t)) = t_s(p) + t. Neither paper states either identity.) The parallelizability characterizations Hájek proves are (i) via the **orbit space being an R¹-fiber bundle** (Theorem 6), (ii) via a **cross-section / global section** (Lemma 5, Theorem 7's proof), (iii) via **complete instability** = every point wandering, x ∉ J_x (Theorem 7, Cor. 8, 10), (iv) via **dispersiveness** J_x = ∅ (Cor. 9), (v) via **Poisson instability** under Liapunov stability (Cor. 11). "Section" occurs in exactly the sense of p. 78 (global section) and p. 80 (local section, cross-section).

### (d) Verdict on the Session-14 citation sentence, both halves combined

**Is the sentence attributable to "Antosiewicz–Dugundji 1961; Hájek 1971"?** Clause by clause:

1. *"a time function f = log W satisfying f(φ^t x) = t + f(x) … The existence of such a function is the classical characterization of a parallelizable flow."* — **Not the wording of either paper.** "Time function" appears in neither (a07 for 1961; §3(c) above for 1971), and neither writes the additivity identity. What both papers state is the **global section with continuous crossing time**: Dugundji–Antosiewicz Definition 1 + Theorem 1 (p. 544, any metric space); Hájek p. 78 restates it as the definition-equivalent form on any topological space, crediting [4]. The record's clause is a correct **one-line restatement** of that (S = f^{−1}(0), θ = −f; continuity of f is the whole content, as a07 notes), and is fairly called "classical", but it must be presented as the program's paraphrase, attributed to **Dugundji–Antosiewicz 1961, Thm 1** (with Hájek 1971 p. 78 as the later textbook-style formulation), never as a quotation.

2. *"parallelizable ⟺ dispersive"* — **Accurate, with the right hypotheses and the right paper for each:** locally compact separable metric — Dugundji–Antosiewicz Thm 3 (p. 548); Hausdorff paracompact locally compact, no metric or separability — **Hájek Cor. 9 (p. 82)**. Without local compactness it is **false** in general: Hájek's Bebutov example (p. 79) is a dispersive, non-parallelizable flow on a completely metrizable σ-compact space. So the qstar block's "That framework assumes locally compact state spaces" is correct for this equivalence; what Hájek adds is that the parallelizable ⟺ **completely unstable** form survives on locally Lindelöf spaces when the regularity property holds (Thm 7, Cor. 8, 10). "Globally wandering flow" in the qstar block is exactly Hájek's "completely unstable" (every x ∉ J_x), which is the hypothesis of his Theorem 7.

3. *"⟺ all limit sets empty ⟺ no nonempty compact invariant set"* — **In neither paper, and Hájek's own vocabulary warns against it.** Hájek calls "all limit sets empty" (L_x = ∅ ∀x) **divergent**, distinguishes it from **completely unstable** (x ∉ J_x ∀x) and **dispersive** (J_x = ∅ ∀x), and states (p. 78, display (1); p. 80 Lemma 3 proof) only the one-way implications dispersive ⟹ completely unstable ⟹ divergent. He nowhere asserts that divergent implies dispersive or parallelizable. a07 attributed this clause to Akin–Auslander Thm 6.3(b)(iv) "Ωφ = ∅"; whether Akin–Auslander's Ω is the ω-limit relation (Hájek's L) or the prolongational one (Hájek's J) should be checked before the clause is kept — if it is the L-version, the chain is unsupported by any of the three sources named in the record. The "no nonempty compact invariant set" clause is not in Hájek at all.

4. *Author order.* The bibliographic order is **Dugundji–Antosiewicz** (a07 §1 13a, from the 1961 byline; confirmed by Hájek's reference [4], p. 84). The prose order "Antosiewicz–Dugundji theorem" is **Hájek's own usage** (abstract and p. 77 line 1), so the record's "Antosiewicz–Dugundji" is defensible as the name of the theorem, but citations of the paper itself should read Dugundji–Antosiewicz.

**Corrected wording (proposed; reconciles with a07's proposal, which it extends by one clause and one attribution).** For the C3 sentence in `sweep-O.md` and the qstar §4 NOVELTY block:

"A continuous real function f additive along orbits, f(φ^t x) = f(x) + t, is the same datum as a global section S = f^{−1}(0) with continuous crossing time; its existence is equivalent to parallelizability (Dugundji–Antosiewicz, Ann. of Math. 73 (1961), Def. 1 and Thm 1, p. 544, any metric space; restated on any topological space by Hájek, Proc. AMS 27 (1971), p. 78). Parallelizable ⟺ dispersive on locally compact separable metric spaces (Dugundji–Antosiewicz Thm 3, p. 548), and on Hausdorff paracompact locally compact spaces without separability (Hájek Cor. 9, p. 82); parallelizable ⟺ completely unstable (every point wandering) whenever the orbit space is paracompact (Hájek Thm 7, pp. 81–82). Neither paper uses the phrase 'time function' or writes the additivity identity, and neither states the equivalence with 'all limit sets empty' or 'no nonempty compact invariant set' — Hájek explicitly separates 'divergent' (all L_x = ∅) from 'dispersive' (all J_x = ∅) and gives only the one-way implications. Local compactness cannot be dropped from the dispersive form: Hájek's Bebutov example (p. 79) is dispersive, completely metrizable, σ-compact and not parallelizable. The program's log W is additive but only lower semicontinuous, so it is a parallelizing datum only in the weakened sense that it still forbids compact invariant sets."

**Attribution table:**
| Statement | Paper, theorem, page |
|---|---|
| parallelizable ⟺ global section with continuous crossing time (metric X) | Dugundji–Antosiewicz 1961, Def. 1, Thm 1, p. 544 |
| same, stated as the definition on any topological space, credited to [4] | Hájek 1971, p. 78 |
| wandering point ⟺ open parallelizable tube through it | Dugundji–Antosiewicz Lemma 3, p. 545 (locally compact metric); Hájek Lemma 4, p. 80 (Tichonov) |
| parallelizable ⟺ dispersive, locally compact separable metric | Dugundji–Antosiewicz Thm 3, p. 548 |
| parallelizable ⟺ dispersive, Hausdorff paracompact locally compact | Hájek Cor. 9, p. 82 |
| parallelizable ⟺ completely unstable, Tichonov X with X/C paracompact | Hájek Thm 7, pp. 81–82 |
| completely unstable ⟺ e: X → X/C is an R¹-bundle (Tichonov) | Hájek Thm 6, p. 81 |
| "time function", f(φ^t x) = t + f(x), "all limit sets empty", "no compact invariant set" | **neither paper** |

**Plain-English reading.** Hájek's paper is the 1961 theorem with the metric and separability hypotheses stripped away and the proof recast as a fiber-bundle cross-section problem: a flow with no recurrence at all ("completely unstable") makes the orbit space the base of a line bundle, and a line bundle over a paracompact Hausdorff base has a section, which is exactly a parallelization. The program's sentence names the right theory and the right pair of papers, but the "time function" phrasing is the program's, the "limit sets empty / compact invariant set" links come from elsewhere, and Hájek's counterexample shows the local-compactness caveat the record already carries is essential. **Nothing here changes a verdict**: C3/C4 stay PARTIAL on the same anchor (ingest-only; not applied to the record).

## §4 Other content a future session should know exists

- p. 79, EXAMPLE (Bebutov, via Nemyckiĭ [8, 2.4]): a dispersive, non-parallelizable flow on a metrizable σ-compact, completely metrizable (G_δ in R²) space with Hausdorff Lindelöf orbit space; "The Antosiewicz-Dugundji theorem traces this to absence of local compactness of X"; Theorem 7 traces it to X/C not being regular. Disproves Nemyckiĭ's conjecture [8, 2.5, 4] that dispersive + separable complete metric ⟹ parallelizable.
- p. 79, Lemma 2 and the remarks after it: locally compact X with Hausdorff X/C (equivalently C_x = D_x for all x; cf. Markus [7, Thm 2]) has the regularity property; so does any system uniformly stable relative to a uniformity.
- p. 80, Lemma 3 proof: "in dispersive systems, VπR¹ is closed whenever V is compact (actually this is necessary and sufficient for dispersiveness)" — a closed-saturation criterion for dispersiveness.
- p. 81, Theorem 6: complete instability ⟺ the orbit-space quotient is an R¹-fiber bundle (Tichonov spaces); compare Markus [7, Thm 3] (differentiable case).
- p. 82, Cor. 11: Liapunov-stable systems are parallelizable iff Poisson unstable; the proof (pp. 82–83) builds an invariant metric d (Bhatia–Hájek [1, IV, 2.8]) and the induced metric inf{d(xπt, yπs)} on X/C.
- p. 83, Props. 12–13 (paracompactness of regular locally compact / locally Lindelöf spaces as direct sums), Cor. 14, and the open CONJECTURE (paracompact total space of an R¹-bundle over a regular base ⟹ paracompact base).
- p. 84, reference list: Bhatia–Hájek 1969 technical notes [1]; Markus 1969 [7]; Nemyckiĭ 1949 [8]; Nemyckiĭ–Stepanov [9]; Seibert 1966 [10] ("almost dispersive" = completely unstable); Ura 1969 [12].
- Relevance to the program's setting (I infer): every theorem of Hájek assumes at least Hausdorff (Tichonov) phase space; the record's note that the framework does not reach the non-T₀ space X₀ is confirmed from the 1971 paper too.

## §5 Caveats for `corpus-routing.md`

- `r4-13b-hajek-…pdf`: text layer garbles all symbols (π→"ir", ∈→"E"/"C", ∅→"0", subscripts dropped, diacritics lost — "HAJEK", "Lindelof", "Tichonov"); quote theorems only after vision on the rendered page. Printed = PDF + 75.
- `r4-13b-hajek-…pdf`: the AMS 10-volume index (Proc. AMS 30(4), the mis-delivered file) prints "77–85"; the article ends on p. 84 — cite 77–84.
- `r4-13b-WRONG-FILE-proc-ams-30-4-…-HAJEK-ABSENT.pdf`: not the article; contains only index entries. Ignore; documented in a07 §1 13b.
- Hájek's vocabulary: "divergent" (L_x = ∅), "completely unstable" (= Seibert's "almost dispersive"; x ∉ J_x), "dispersive" (J_x = ∅), "Poisson unstable" (x ∉ L_x) are four different conditions — do not translate any of them as "all limit sets empty" without saying which limit set. "Tichonov" = completely regular Hausdorff.
- Author order: the 1961 paper's byline and Hájek's reference [4] read Dugundji–Antosiewicz; Hájek's prose says "Antosiewicz-Dugundji theorem". Use the former for the bibliographic citation, the latter only as the theorem's name.

## §6 Not done
- Nothing outstanding for item 13b. The record was not edited (ingest-only). The Akin–Auslander Ω check (§3(d) clause 3) is a one-line lookup for whoever next opens arXiv:1004.0323.
