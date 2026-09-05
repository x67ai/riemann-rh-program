# alkl23-note.tex, revision record

**Date:** 2026-09-05 (Session 16, direction C3-r). **Repairer:** Fable 5.1 (independent of the writer and of the reader).
**Input:** the second-model read `results/c3-r/s14/alkl23-note-read-O.md` (Opus 5), verdict PASS-WITH-REPAIRS, nine repairs R1-R9
(R1, R2 required; R3-R6 recommended; R7-R9 optional). **Baseline:** `alkl23-note.tex` as committed at git HEAD before this pass
(the writer's version, 3 pages).
**Method:** each FIND string was asserted to occur exactly once before replacement (script, all ten matches unique); every
theorem number, equation number, page and quoted phrase that a repair introduces was read by me in the PUBLISHED PDF
(`novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`, via `pdftotext -layout` with page tags,
and a 250-dpi render of p. 56 for the boldface); each mathematical statement a repair introduces was re-derived by me
(section 3 below). No claim below rests on recall.

## 1. Repairs, one line each

| # | Status | What changed | What I verified in the published PDF / by re-derivation |
|---|---|---|---|
| R1a | APPLIED | witness (d): declared `\dim L=n''`; cover index renamed `f_j` -> `f_i`, `(j\ge2)` -> `(i\ge2)`, and `(i\ge2)` added inside the replacement family | p. 19: "L is a regular submanifold of M of codimension n' and dimension n''", x' = first n' coordinates, x'' = the rest, L_0 = {x' = 0}; p. 22: the partition of unity of (4.10) is written {h, f_j} subordinate to {M\L, U_j}. Renaming the cover index to i inside the note removes the collision with the sequence index j of u_j; the replacement family (1-rho)h, rho+(1-rho)f_1, (1-rho)f_i (i>=2) sums to 1 and is subordinate to the same cover. |
| R1b | APPLIED | "f_ju_j=0 (j>=2)" -> "f_iu_j=0 (i>=2)" | consequence of R1a; for large j, supp u_j lies in the neighborhood of p_0 where h = f_i = 0 (i>=2). |
| R2 | APPLIED | "J^m(M,L) \cong A^m(M) by (7.26)" -> "J^m(M,L) \cong A^m(\boldsymbol M) by (7.26), where \boldsymbol M is the manifold with boundary obtained by cutting M along L" | p. 56 (250-dpi render): (7.26) is pi_* : A(**M**) -> J(M,L) with a BOLD M, and "We also get spaces J^(s)(M,L) and J^m(M,L) corresponding to A^(s)(**M**) and A^m(**M**) via (7.26)"; p. 50: "Let **M** be the smooth manifold with boundary defined by 'cutting' M along L". The text layer drops the boldface, which is why the render was needed. |
| R3 | APPLIED | lower bound now reads "for any compact K meeting {g != 0}, ||a_j||_{K,0,0,\bar m'} >= c sup_K |g| > 0" | from the note's own display, ||a_j||_{K,0,0,\bar m'} = sup_K|g| Phi_{0,\bar m'}(j) >= c sup_K|g|, which is > 0 exactly when K meets {g != 0}. |
| R4 | APPLIED | p. 18 bundle sentence: now implicates only Prop. 3.2 and Cors. 3.4 and 3.6, "(the extensions of Prop. 3.3 and Cor. 3.5 are unaffected)" | p. 18: "We can similarly define the norms (3.4) and (3.5) on S^m(E), and Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting." Prop. 3.3 (p. 17: for m < m', the (3.5) seminorms of order m' vanish on S^m) is true, as is its bundle version: |d a| |xi|^{|beta|-m'} = (|d a| |xi|^{|beta|-m}) |xi|^{m-m'} -> 0. Cor. 3.5 (density, p. 17) is true and is re-proved directly in the note's section 4, by a local argument that extends to bundles. |
| R5 | APPLIED | "there are N in N, a finite set Gamma of indices, and C,R_0>0" -> "there are a finite set Gamma of multi-indices and constants C,R_0>0" | N does not occur in display (1); in the proof it is the Taylor order, absorbed into Gamma. |
| R6 | APPLIED | footnote: `\emph{Use of AI.}` -> `\textbf{Use of AI.}`; "made the technical and editorial decisions" -> "adjudicated the technical and editorial decisions" | `results/arxiv/README.md` (settled record) and `results/arxiv/m0-axiom/main.tex`, `results/arxiv/m1-noncirc/main.tex` use `\textbf` and "adjudicated". Correction to the reader's rationale, for the record: `results/arxiv/a4-no-go/main.tex` and `results/arxiv/seed-no-go/main.tex` still carry the older `\emph` / "made the technical and editorial decisions" wording, so "all four title pages" was inaccurate; the note follows the README wording as the brief directs. The em-dashes of the canonical wording stay replaced by parentheses, and the program/repository clause stays omitted. |
| R7 | APPLIED | "... J(M,L), K(M,L), whose steps are Fr\'echet spaces, are acyclic," | p. 5: "If the steps X_k are Fréchet spaces, the above properties of (X_k) depend only on the LF-space X [39, Chapter 6, p. 111] ... In this case, X is acyclic if and only if it is boundedly/compactly/sequentially retractive [39, Proposition 6.4]. As a consequence, acyclic LF-spaces are complete and regular [39, Corollary 6.5]." The note already invoked these consequences, so the hypothesis was implicit; the paper asserts it (p. 22: I^m(M,L) "becomes a Fréchet space"; p. 38: A(M) is "the same LF-space" for both filtrations), and I re-derived it (section 3.1 below), making it a third independent check after `w3-adjudication.md` section 5.2 and `alkl23-note-read-O.md` section 2.10. |
| R8 | APPLIED (kept, see section 2) | one sentence after the direct proof of Cor. 3.5: "The conclusion of Remark 3.8 (p. 18) likewise follows from (c) directly, without the sequential retractivity of S^infty(U x R^l), which is what its printed argument uses." | p. 18, Remark 3.8: "Despite of Corollary 3.4, the following argument shows that the second inclusion of (3.3) is not a TVS-embedding ... However a_m not-> 0 in S^infty(U x R^l); otherwise, since S^infty(U x R^l) is sequentially retractive (Corollary 3.6), all a_m would lie in some step S^{m_0}(U x R^l), a contradiction." p. 16, (3.3): C_cv^infty ⊂ S^{-infty}, S^infty ⊂ C^infty; the "second inclusion" is S^infty ⊂ C^infty. Re-derivation in section 3.2. Memoir arXiv:2402.06671v1, printed p. 15 (section 2.1.8): "The following properties hold [ÁLKL23, Corollaries 3.4-3.6 and Remark 3.8]: ... however the second inclusion of (2.1.27) is not a TVS-embedding". |
| R9 | APPLIED | "(6.41) with P=1 (the topology of A^m(M) is the projective one over all P in Diff_b(M), p. 38)" | p. 38: A^m(M) = {u in C^{-infty}(M) : Diff_b(M) u ⊂ x^m L^infty(M)} "with the projective topology given by the maps P : A^m(M) -> x^m L^infty(M) (P in Diff_b(M))", and (6.41) ||u||_{k,m} = ||P_k u||_{x^m L^infty} = sup_{M°} x^{-m}|P_k u| for a countable C^infty(M)-spanning set {P_j} of Diff_b(M). 1 in Diff_b^0(M) = C^infty(M), so sup x^{-m}|u| is a continuous seminorm of A^m(M). |

**Declined:** none.

## 2. Page budget and the one layout change

With all nine repairs and the original `margin=0.8in`, the build ran to 4 pages: the whole bibliography (heading plus three
items, eight lines) moved to p. 4. I tested the alternatives in a scratch directory before touching the note (each compiled
twice; "p4 lines" = nonblank text lines on the spilled page, page number included):

| variant | pages | p4 lines |
|---|---|---|
| all nine, margin 0.8in (as instructed to try first) | 4 | 9 |
| drop R8, margin 0.8in (the brief's first fallback) | 4 | 6 |
| all nine, margin 0.75in | 4 | 3 |
| drop R8, margin 0.75in | 4 | 3 |
| all nine, margin 0.75in, footnotesize bibliography | 4 | 2 |
| all nine, margin 0.75in, compact "References" heading | 4 | 3 |
| all nine, hmargin 0.8in, vmargin 0.6in | 4 | 3 |
| all nine, margin 0.72in | 3 | - |
| all nine, hmargin 0.75in, vmargin 0.65in | 3 | - |
| all nine, hmargin 0.75in, vmargin 0.6in | 3 | - |
| all nine, margin 0.7in | 3 | - |

Dropping R8 alone does not restore 3 pages (it would have taken dropping most of the repairs), so a layout change was needed
in any case. I therefore kept R8 (the memoir cites Remark 3.8 next to Cors. 3.4-3.6, so the clause is useful to the
authors) and made the smallest content-neutral change that fits: `\usepackage[margin=0.8in]{geometry}` ->
`\usepackage[hmargin=0.75in,vmargin=0.65in]{geometry}`. Nothing else in the layout or the text was touched.

**Final build** (`pdflatex` twice, TeX Live 2026): 3 pages, 0 overfull boxes, 0 underfull boxes, no LaTeX warnings beyond
the usual hyperref/microtype notices. Page 3 ends with the bibliography, with a few lines of slack below it (checked on a render of the page). All nine
repairs were confirmed present in the PDF text layer (`pdftotext`). No em-dash (`---` or U+2014) anywhere in the source;
U.S. English throughout (the direct quotation "Despite of" does not occur in the note; "Fr\'echet" is a proper name).
Build products `.aux`, `.log`, `.out` were removed after the checks, as in the writer's pass.

## 3. Re-derivations behind the repairs that add a mathematical statement

### 3.1 The steps are Fréchet spaces (for R7)

*I^m(M,L), M compact.* By p. 22 the topology is the initial one of the injective map (4.10), u -> (hu, (a_j)_j), into
C^infty(M\L) ⊕ ⊕_j S^{\bar m}(N*L_j; N*L_j); each a_j vanishes for x'' outside the compact x''-projection of supp f_j.
The target is a countable product of Fréchet spaces, so I^m is metrizable; completeness: let (u_k) be Cauchy, so
hu_k -> v in C^infty(M\L) with supp v ⊂ supp h (a compact subset of M\L), and a_{j,k} -> a_j in S^{\bar m}. By Prop. 4.3
(p. 21, first map, continuous S^{\bar m} -> I^(s)(U_j, L_j) for s < -\bar m - n'/2) and Prop. 4.1 (I^(s) Fréchet),
f_ju_k -> w_j in I^(s)(U_j,L_j) ⊂ C^{-infty}(U_j), with supp w_j ⊂ supp f_j, so w_j extends by zero to M. Put
u := v + sum_j w_j. Then u_k = hu_k + sum_j f_ju_k -> u in C^{-infty}(M); multiplication by h and by f_j is continuous on
C^{-infty}(M), so hu = v and f_ju = w_j, whose partial Fourier transform (4.8), extended to compactly supported
distributions in x' with x'' as a parameter, is the C^infty-limit of the a_{j,k}, namely a_j in S^{\bar m}. So u lies in
I^m(M,L) with (4.10)-image (v,(a_j)), and u_k -> u in I^m. Hence I^m(M,L) is Fréchet. (Agrees with `w3-adjudication.md`
section 5.2.)

*A^m(M), M compact with boundary.* By p. 38 the topology is the projective one of the maps P : A^m(M) -> x^m L^infty(M),
P in Diff_b(M); a countable spanning set suffices ((6.41)), so A^m is metrizable. x^m L^infty(M) is a Banach space
(isometric to L^infty via multiplication by x^m) continuously included in C^{-infty}(M) = (Ċ^infty(M;Ω))' (p. 32, Sect. 6.3, the unnumbered display defining supported and extendible distributions):
for phi in Ċ^infty(M;Ω), |<x^m f, phi>| <= ||f||_infty ||x^m phi||_{L^1}, and phi -> x^m phi is continuous on Ċ^infty
because sup|x^{-N} phi| is a continuous seminorm there for every N (Taylor expansion at the boundary). Completeness: if
(u_k) is Cauchy then Pu_k -> v_P in x^m L^infty for every P; put u := v_1 in x^m L^infty ⊂ C^{-infty}(M). Each P in
Diff_b(M) ⊂ Diff(M) acts continuously on C^{-infty}(M) (transpose of P^t on Ċ^infty(M;Ω)), so Pu_k -> Pu in C^{-infty}(M),
while Pu_k -> v_P in x^m L^infty ⊂ C^{-infty}(M); the limit is unique, so Pu = v_P in x^m L^infty for all P, i.e.
u in A^m(M) and u_k -> u in A^m(M). Hence A^m(M) is Fréchet.

*The rest.* Ȧ^m(M) = I^m_M(M̆, ∂M) ((6.47)), 𝒦^m(M) = I^m_{∂M}(M̆, ∂M) (p. 41) and K^m(M,L) (p. 58) are the subspaces of
elements supported in a fixed closed set; "supp u ⊂ F" is a closed condition in C^{-infty}, into which the ambient Fréchet
space is continuously included, so these are closed subspaces, hence Fréchet. J^m(M,L) corresponds to A^m(**M**) via the
TVS-isomorphism (7.26) (p. 56), hence is Fréchet. So all six LF-spaces named in the sentence have Fréchet steps, and the
p. 5 consequences (Prop. 6.4, Cor. 6.5 of [Wen03]) apply as the note uses them.

### 3.2 The conclusion of Remark 3.8 from witness (c) (for R8)

The conclusion of Remark 3.8 is that the inclusion S^infty(U x R^l) ⊂ C^infty(U x R^l), the second inclusion of (3.3),
is not a TVS-embedding. Witness (c) of the note gives c_j = e^j theta(xi - j e_1) in S^{-infty} ⊂ S^infty with c_j -> 0 in
C^infty and c_j not-> 0 in S^infty (a 0-neighborhood W of S^infty containing no c_j is exhibited, with no property of
S^infty assumed). If the inclusion were a TVS-embedding, the C^infty-null sequence (c_j) would be S^infty-null. So the
conclusion holds, for every open U and every l >= 1, and neither Cor. 3.6 nor any retractivity of S^infty is used. The
printed argument of Remark 3.8 instead invokes "S^infty(U x R^l) is sequentially retractive (Corollary 3.6)", which is
unavailable for non-compact U by witness (f).

### 3.3 Statements read in the published PDF this pass

Read by me, with page: Wengenroth criterion as quoted (p. 4); the Fréchet-steps hypothesis, Prop. 6.4 and Cor. 6.5 as quoted,
and the compact-spectrum remark (p. 5); (3.3), (3.4) (p. 16); "Hence S'^m(U x R^l) is complete", Prop. 3.3, Cor. 3.4,
Cor. 3.5 (p. 17); Cor. 3.6, Remark 3.7, Remark 3.8, the bundle sentence (p. 18); the adapted-chart convention n', n'' (p. 19);
(4.7), (4.8), Prop. 4.3 (p. 21); (4.9), (4.10), (4.11), "which becomes a Fréchet space" (p. 22); the definition of A^m(M) and
its projective topology, (6.38)-(6.40), (6.41) (p. 38); (6.42), (6.43), Prop. 6.12, Prop. 6.13 (p. 39); the definition of extendible distributions (p. 32, Sect. 6.3); the definition of
**M** by cutting (p. 50); (7.26), (7.27), (7.28), Cors. 7.11-7.14 (p. 56); Cor. 7.15 (p. 57); memoir section 2.1.8
(printed p. 15). Of the published statements the note quotes or cites, 24 were read by me this pass; the ones the repairs do
not touch (Cor. 4.5, Cor. 6.14, Cor. 6.21, Cor. 6.27, Prop. 6.29, Claim 6.46, Cor. 7.22, Prop. 7.26, Cor. 7.31, Prop. 8.8,
the primed identity at the top of p. 17) were verified by the reader (read-O section 1) and their text in the note is unchanged.

## 4. Not done here (for the orchestrator)

* The correction to the program record named in `alkl23-note-read-O.md` section 4 (the `w3-adjudication.md` section 0 /
  `novelty/adjudication.md` C6(ii) sentence claiming S^m_K -> S^{m'}_K are compact operators) is outside this pass; the note's
  parenthetical is right and was left as it is.
* Two arXiv title pages (`a4-no-go`, `seed-no-go`) still carry the older AI-use wording; not touched.
