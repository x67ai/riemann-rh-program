# alkl23-note recheck F (Fable 5.1), Session 16, 2026-09-06

Adversarial re-read of `results/c3-r/s14/alkl23-note.tex` / `alkl23-note.pdf` (3 pp., mtime 2026-09-05 22:47, the post-repair version), by a reader who had not seen the note, its derivations, the first read, or the revision record before this pass. Sources opened (nothing on trust): the PUBLISHED PDF `novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf` (text layer per page; pp. 16, 17, 48, 49, 56 also rendered at 130 dpi); arXiv v1 (on disk), v2 and v3 (downloaded this pass to the scratchpad, 55 pp. each); the memoir arXiv:2402.06671 v1 (on disk) and v2 (downloaded this pass, 176 pp.); `novelty/adjudication.md` §2 C6; arxiv.org, api.crossref.org and api.semanticscholar.org live. Previous readers' materials (`alkl23-note-read-O.md`, `alkl23-note-REVISION.md`, `alkl23-note-derivations.md`) were opened only after the derivations and the citation checks below were finished.

## 0. Count and verdict

**Errors: 2** (ERROR severity), plus 5 SHOULD-FIX and 7 NIT. Neither error changes a mathematical conclusion; both are one-clause repairs. (E1) Witness (d) omits the hypothesis that ties the support of g to the region where the partition of unity has been normalized: as written ("ρ = 1 near p_0", "g ∈ C_c^∞(R^{n''})") the sentences "u_j ∈ C^∞(M)" and "For large j, hu_j = 0 and f_i u_j = 0" are not guaranteed; the same gap sits in the derivations file and was not caught by the first read. (E2) The parenthetical "§§3–4 are unchanged in all arXiv versions" is false: §§3–4 changed between v1 and v2 (Remark 3.7's cross-reference, the wording of Sect. 4.3.3, §§4.6–4.8 rewritten with equations (4.21)–(4.24) collapsed to (4.21)–(4.22), cross-references into §2 shifted); what is true is that the statement and equation numbers the note cites from §§3–4 are the same in every version, and that v2 = v3 = published in §§3–4. Everything else checked out: every theorem/corollary/proposition/claim number, every page, every equation label and every quotation matches the published PDF; v3 carries the published numbering for every cited statement (so does v2, see §4); the memoir sentences are exact (printed pages, same in v1 and v2); the erratum facts of §5 are still true on 2026-09-06; witnesses (a), (b), (c), (e), (f), the proof-failure diagnosis, inequality (1), and the Claim 6.46 / Prop. 8.8 / Cor. 3.5 / Remark 3.8 / Cor. 6.27–7.22 repairs all re-derive; the build is clean (0 overfull/underfull, no warnings), U.S. English, no em-dashes, courteous. Verdict: PASS after E1 and E2 are applied; the SHOULD-FIX items (memoir v2 in the bibliography; the memoir's two further restatements of the false statements; the "two printed arguments" count; the Cor. 3.6 bundle qualifier; the bold-face quotation of (7.27)) should be applied before sending.

## 1. Findings

Locations refer to the .tex; "PDF p." is the note's page.

**F1 — ERROR — Witness (d), PDF p. 2, the two sentences "Take p_0 ∈ L, ... h = f_i = 0 (i ≥ 2) near p_0 (... ρ = 1 near p_0 ...)" and "Let g ∈ C_c^∞(R^{n''}), g ≢ 0".**
What is wrong: nothing constrains supp g. supp u_j = x^{-1}({|x'| ≤ 1/j} × supp g) shrinks to x^{-1}({0} × supp g), a compact subset of L ∩ U_1 that is not contained in a neighborhood of p_0 unless supp g is small. So (i) "u_j ∈ C^∞(M)" needs {0} × supp g ⊂ x(U_1) (with g ∈ C_c^∞(R^{n''}) the chart image need not contain it, and then u_j is not a function on M), and (ii) "For large j, hu_j = 0 and f_i u_j = 0 (i ≥ 2)" needs h = f_i = 0 on a neighborhood of x^{-1}({0} × supp g), not merely near p_0. If (ii) fails, the (4.10)-image of u_j has other nonzero components and the displayed computation no longer proves u_j → 0 in I^{m''}(M, L).
Evidence: published p. 19 (adapted chart x = (x', x''): U → U' × U'' with U' ⊂ R^{n'}, U'' ⊂ R^{n''} open, L_0 = {x' = 0}); p. 22 ((4.10) is u ↦ (hu, (a_j)) and all components enter the topology). `alkl23-note-derivations.md` §5 has the same gap ("ρ = 1 on a neighborhood N of p_0", "g ∈ C_c^∞(U'')", then "supp u_j ⊂ {|x'| ≤ 1/j} × supp g ⊂ N for j ≥ j_0", which does not follow); `alkl23-note-read-O.md` §2.4 repeats it.
Exact fix (one clause, mathematics unchanged): replace
  "Take p_0 ∈ L, a chart (U_1, x=(x',x'')) adapted to L with x(p_0)=0, and the partition of unity {h,f_i} of (4.10) with f_1=1 and h=f_i=0 (i≥2) near p_0 (replace any {h,f_i} by {(1−ρ)h, ρ+(1−ρ)f_1, (1−ρ)f_i (i≥2)}, ρ∈C_c^∞(U_1), ρ=1 near p_0; ...). Let g ∈ C_c^∞(R^{n''}), g≢0;"
by
  "Take a chart (U_1, x=(x',x'')): U_1 → U'×U'' adapted to L (p. 19), g ∈ C_c^∞(U''), g≢0, and the partition of unity {h,f_i} of (4.10) with f_1=1 and h=f_i=0 (i≥2) on a neighborhood N of the compact set x^{-1}({0}×supp g) ⊂ L (replace any {h,f_i} by {(1−ρ)h, ρ+(1−ρ)f_1, (1−ρ)f_i (i≥2)}, ρ∈C_c^∞(U_1), ρ=1 on N; ...);"
and after the display of u_j write "For j large, supp u_j = x^{-1}({|x'|≤1/j}×supp g) ⊂ N, so u_j ∈ C_c^∞(U_1) ⊂ C^∞(M) ⊂ I^m(M,L), hu_j = 0 and f_iu_j = 0 (i≥2), and by (4.8) ...". (p_0 is then not needed; "x(p_0)=0" can go.)

**F2 — ERROR — §1, PDF p. 1, "arXiv:2304.00798v3 has the same numbering, and §§3–4 are unchanged in all arXiv versions".**
What is wrong: the second clause is false. Word-level diff of §§3–4 (from the heading "3. Symbols" to "5. Dual-conormal distributions"), pdftotext of v1 / v2 / v3 / published: v1 → v2 has 26 substantive differences (Remark 3.7: "like in Proposition 6.8" → "6.10"; §3 intro sentence on U = R^0 reworded; §4.2.2 "Fréchet space I_c^(∞)" → "LCHS"; Sect. 4.3.3 "Corollary 4.7 can be extended with" → "has extensions for"; §§4.6–4.7 rewritten: v1's (4.21) and (4.24) ("continuous extensions") removed, so v1 (4.22), (4.23) become (4.21), (4.22); §4.8 rewritten (the sentence "In this case, we have m̄ = m in (4.9), and the symbol of any A ∈ Ψ^m ... multiplicative and compatible with transposition" is new); cross-references (2.7)–(2.21) shifted by one). v2 → v3: no differences in §§3–4. v3 → published: layout noise only. The first clause is true (all cited statement numbers checked in v3, table in §2), and in fact already true of v2.
Evidence: scratchpad diffs `wdiff2.py v1.txt alkl-v2.txt` (26 flagged), `alkl-v2.txt alkl-v3.txt` (0), `alkl-v3.txt published` (layout only); v1 p. 15 line "Remark 3.7. Another proof of Corollary 3.5 could be given like in Proposition 6.8" vs published p. 18 "Proposition 6.10".
Exact fix: replace "arXiv:2304.00798v3 has the same numbering, and §§3–4 are unchanged in all arXiv versions" by "arXiv:2304.00798v3 has the same numbering, and the statements and equations of §§3–4 cited here carry the same numbers in every arXiv version". (Do not write "v2 and v3 have the same numbering" unless wanted; it is true, see §4.)

**F3 — SHOULD-FIX — Bibliography [2], PDF p. 3: "arXiv:2402.06671 (v1, 7 February 2024)".**
What is wrong: arXiv lists a v2 (Tue, 13 Feb 2024, 176 pages). A courtesy note should cite the current version. Checked in v2 this pass: §2.1.8 is still printed p. 15 (pdf 21), §5.2.1 still p. 119 (pdf 125), §§5.5.3–5.5.4 still p. 122 (pdf 128), the three "compactly retractive" sentences and the I(F) definition are verbatim the same, and the two further restatements of F5 are on the same pages (38, 53).
Exact fix: "arXiv:2402.06671 (v2, 13 February 2024; the pages cited are the same in v1)".

**F4 — SHOULD-FIX — §4, PDF p. 3, "Two printed arguments use a coincidence statement for more than the word 'acyclic'."**
What is wrong: undercount. The semi-Montel step of the printed proof of Cor. 3.6 (p. 18: "the topologies of S^∞ and S^m coincide on B. By Corollary 3.4, it follows that B is a complete bounded subspace of C^∞(U×R^l)") uses Cor. 3.4 to identify the S^m-topology on a bounded set B with the C^∞-topology, and that identification is false even on bounded sets: a_N(ξ) = θ((ξ−Ne_1)/N) (r < 1) is bounded in S^0, a_N → 0 in C^∞, and ‖a_N‖_{0,0,0} = θ(0) = 1. The proofs of Cors. 4.7, 6.16, 6.22, 6.28, 7.15, 7.23 say "like in Corollary 3.6". The note does handle this (the parenthetical on relatively compact images, and "and then of their Montel clauses"), so only the sentence is inaccurate; but the authors will read that sentence as a claim of completeness.
Exact fix: "Besides the semi-Montel step of the printed proof of Cor. 3.6 (which invokes Cor. 3.4 to pass to the C^∞-topology on a bounded set, and which the parenthetical above replaces), two printed arguments use a coincidence statement for more than the word 'acyclic'." Optionally add the classical true statement the authors are likely to reply with: "What is true is the bounded-set version: on a bounded subset of S^m(U×R^l) the topology of S^{m'}, m' > m, is the C^∞-topology; this also repairs the semi-Montel step once acyclicity is known."

**F5 — SHOULD-FIX — (f), PDF p. 2, "and to [2, §2.1.8, p. 15], which restates Cors. 3.4–3.6 for arbitrary open U ⊂ R^n" and §4's memoir sentence.**
What is wrong: incomplete. The memoir also restates the second assertion of Cor. 6.14 in §2.5.10 (printed p. 38, pdf 44): "The following is true [ÁLKL23, Corollaries 6.14–6.16 and 6.39 and Remark 6.41]: the topologies of A(M) and C^∞(M̊) coincide on every A^m(M) ..."; and the second assertion of Cor. 7.13 in §2.6.7 (printed p. 53, pdf 59): "... and the topologies of J(M,L) and C^∞(M\L) coincide on every J^m(M,L)". Both are refuted by witness (e). Same pages in memoir v1 and v2. (No other "coincide" restatement exists in the memoir; the only uses of retractivity are the three the note lists, verified by grep of the whole text.)
Exact fix: at the end of (e) add "([2] restates the second assertions of Cor. 6.14 and Cor. 7.13 in §2.5.10, p. 38, and §2.6.7, p. 53.)" or fold into the §4 memoir sentence: "In the memoir [2], §2.5.10 (p. 38) and §2.6.7 (p. 53) restate Cor. 6.14 and Cor. 7.13; the uses of compact retractivity ..."

**F6 — SHOULD-FIX — §2, PDF p. 1, "the acyclicity and bounded-retractivity clauses of Cor. 3.6 (p. 18) for every non-compact U, together with the part of the sentence on p. 18 that extends Prop. 3.2 and Cors. 3.4 and 3.6 to symbols on a vector bundle".**
What is wrong: for Cor. 3.6 the bundle extension fails only over a non-compact base (the note's own §4 proves acyclicity over a compact base, and (f) says "bundles over a non-compact manifold"); the §2 sentence lets "for every non-compact U" be read as attaching only to the first item, so the Cor. 3.6 bundle extension reads as false for every base. Overclaim by ambiguity.
Exact fix: "... extends Prop. 3.2 and Cors. 3.4 and 3.6 to symbols on a vector bundle (Cor. 3.6 again only over a non-compact base; the extensions of Prop. 3.3 and Cor. 3.5 are unaffected)".

**F7 — SHOULD-FIX (quotation accuracy) — (e), PDF p. 2, "Since J^m(M,L) is given by (7.27) with Diff(M,L) and x^m L^∞(M)".**
What is wrong: (7.27) reads Diff(M,L) u ⊂ 𝒙^m L^∞(𝑴) with bold x and bold M (p. 56, rendered: "Its lift π*x is a boundary defining function of 𝑴, also denoted by 𝒙"); the note prints a plain M, and introduces bold M only later (§4). Not a mathematical error (the collar description is the same), but a misquotation of the symbol.
Exact fix: "with Diff(M,L) and $\boldsymbol x^mL^\infty(\boldsymbol M)$, $\boldsymbol M$ the manifold with boundary obtained by cutting $M$ along $L$ (p. 56)"; then in §4 shorten "where $\boldsymbol M$ is the manifold ..." to a back-reference or leave it.

**F8 — NIT — (e), PDF p. 2: "m' < m, and u_j = j^{-m'}χ(jx)g(y)" then "So (with m' = m) u_j → 0 ...".** m' = m contradicts the fixed m' < m. Fix: "m' ≤ m" in the setup.

**F9 — NIT — (e), PDF p. 2: "(u_j = 0 on {x < 1/2j})".** Ambiguous; fix "{x < 1/(2j)}".

**F10 — NIT — §2 last sentence, PDF p. 1: "The witnesses below are constant in the base variable up to a fixed cut-off, so they also refute every parametrized or bundle version."** Witness (f) is not (χ_j moves with j; it is intrinsically about a non-compact base). Fix: "The witnesses in (a)–(e) are constant ...".

**F11 — NIT — §4, PDF p. 3: "to finite products with constant spectra".** Ambiguous (the (4.10) product has one constant factor and non-constant symbol factors). Fix: "to finite products of spectra satisfying it (a constant spectrum does trivially)".

**F12 — NIT — §4, PDF p. 3: "by Prop. 7.26 every element of K^m(M,L) is a finite sum of Dirac layers ∂_x^kδ_L ⊗ v_k with k ≤ m̄".** Prop. 7.26 gives the finite sum for K(M,L); the bound k ≤ m̄ is a consequence of the symbol order (a polynomial symbol of exact degree k lies in S^{m̄} iff k ≤ m̄). Fix: "by Prop. 7.26 every element of K(M,L) is a finite sum of Dirac layers ∂_x^kδ_L ⊗ v_k, and it lies in K^m(M,L) iff v_k = 0 for k > m̄, since its local symbols are polynomials in ξ of degree ≤ m̄;".

**F13 — NIT — §5, "As of September 3, 2026".** Re-checked 2026-09-06: arXiv abs page lists v1/v2/v3 only; Crossref record relation {} and no update-to/updated-by, is-referenced-by-count 0; Semantic Scholar citationCount 0. Update the date to the sending date if re-checked then. (zbMATH and Unpaywall not re-checked, see §4.)

**F14 — NIT — layout, PDF p. 1.** The date line and "1. Purpose." abut with no vertical space (\vspace{-2.5em} after \maketitle); -2em would separate them at the cost of one line. Optional.

Checked and found correct (no finding): the title and bibliographic data of [1] (JPDOA 15 (2024) art. 47, 68 pp., DOI, v3 = 1 June 2024) and [3]; every citation in §2 (table below); the quotations from pp. 17 and 48–49 (primes and the unprimed exponent m confirmed on renders); the diagnosis of the proof failure of Prop. 3.2; witnesses (a), (b), (c), (e), (f) (see §3); inequality (1) and its use of the p. 4 criterion; the relatively-compact-image / not-compact-operator parenthetical; the Fréchet-steps hypothesis; the Claim 6.46 repair including the m' < m remark (source prints "For any m' > m, let E_{m'}: A^m(M) → ..." on p. 48, which with (6.38) is the wrong direction); Prop. 8.8 via Cor. 7.31 (p. 60); Cor. 3.5 directly; Remark 3.8 from (c); Cor. 6.27 / 7.22 via polynomial symbols and (6.49); the memoir sentences (§2.1.8 p. 15; §5.1 closed M; I(F) := I(M,M^0;ΛF); §5.2.1 p. 119; §§5.5.3–5.5.4 p. 122); the §5 facts against `novelty/adjudication.md` §2 C6 and live; the AI-use footnote wording; U.S. spelling; no em-dash in source or PDF; no program-internal jargon; "false" used only where a witness is given; the build (scratch rebuild text-identical to the shipped PDF; log free of Overfull/Underfull/Warning lines); the author name "Kunal Tyagi" matches the program's other arXiv title pages.

## 2. Citation table (published PDF page = printed journal page)

| Cited in the note | Found at | Check |
|---|---|---|
| Prop. 3.2 (p. 16) | p. 16, statement + proof start | OK |
| proof of Prop. 3.2: "‖φ(a)‖'_{K,α,β,m} = ‖a‖'_{K,α,β,m} < ∞" at the top of p. 17 | p. 17, line 2, primes present (render) | OK |
| "Hence S'^m(U×R^l) is complete" (p. 17) | p. 17, unaccented S'^m (render) | OK |
| Prop. 3.3 (unaffected) | p. 17 | OK |
| Cor. 3.4, both assertions (p. 17) | p. 17 | OK |
| Cor. 3.5 (p. 17) | p. 17 (proof continues p. 18) | OK |
| Cor. 3.6 (p. 18), proof "Corollary 3.4 gives the property of being acyclic" | p. 18 | OK |
| Remark 3.8 (p. 18), "sequentially retractive (Corollary 3.6)" | p. 18 | OK |
| p. 18 bundle sentence "Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended" | p. 18 | OK |
| (3.1), (3.4), (3.5) | pp. 15, 16, 16 | OK ((3.1) with (1+|ξ|)^{m-|β|}; (3.5) with |ξ|^{m-|β|}) |
| (4.8) | p. 21 | OK |
| (4.9), (4.10) | p. 22 | OK |
| Cor. 4.5 (p. 23), proof "Use Corollary 3.4 and the TVS-embeddings (4.10)" | p. 23 | OK |
| Cor. 4.7 (p. 23) | p. 23 | OK |
| Sect. 4.3.3, p. 23, "except acyclicity in the case of I(M,L)" | p. 23 | OK |
| p. 38: A^m(M) projective topology over P ∈ Diff_b(M); (6.41) | p. 38 | OK |
| (6.42), (6.43); Prop. 6.12; Cor. 6.14 both assertions (p. 39) | p. 39 | OK |
| Cor. 6.16 (p. 39) | p. 39 | OK |
| Cor. 6.21 (p. 40), "consequence of Corollary 4.5 applied to (M̆,∂M)"; Cor. 6.22 | p. 40 | OK |
| (6.47) Ȧ^m(M) = I^m_M(M̆,∂M) closed subspaces | p. 40 | OK |
| Cor. 6.27 (p. 41), "formally the same proofs, using Corollaries 6.21, 6.22 and 6.26"; Cor. 6.28; (6.49); 𝒦^m closed in Ȧ^m (p. 41) | p. 41 | OK |
| (6.33) | p. 36 | OK |
| Prop. 6.29, domain A^m(M) | p. 42 | OK |
| Claim 6.46 (pp. 48–49) and the quoted sentence | pp. 48–49 (sentence straddles the break) | OK |
| Cor. 7.13 both assertions (p. 56); (7.26); (7.27) | p. 56 | OK ((7.27) has bold x, bold M: F7) |
| Cor. 7.15 (p. 57) | p. 57 | OK |
| K^m(M,L) closed in I^m(M,L) (p. 58); Cor. 7.22 (p. 58) "consequences of ... Corollaries 6.26 to 6.28"; Cor. 7.23 | p. 58 | OK |
| Prop. 7.26 | p. 59 (proof to p. 60) | OK |
| Cor. 7.31 | p. 60 | OK |
| Prop. 8.8 (p. 64), lead-in "using Proposition 7.29 and Corollaries 7.13, 7.15 and 7.31" | p. 64 | OK |
| Wengenroth Thm. 6.1 "quoted on p. 4"; Prop. 6.4, Cor. 6.5 and the compact-spectrum remark "on p. 5" | pp. 4, 5 | OK |
| [1] 68 pp.; arXiv v3 1 June 2024 | published p. 68 = last; arXiv abs page | OK |
| v3 "has the same numbering" | v3 text: Props. 3.2, 3.3, 6.12, 6.13, 6.29, 7.26, 7.29, 8.8; Cors. 3.4–3.6, 4.5, 4.7, 6.14, 6.16, 6.21, 6.22, 6.27, 6.28, 7.13, 7.15, 7.22, 7.23, 7.31; Claim 6.46; Remarks 3.7, 3.8; eqs. (3.1)–(3.5), (4.8)–(4.10), (6.33), (6.41)–(6.43), (6.47), (6.49), (7.26), (7.27) all as published | OK |
| "§§3–4 unchanged in all arXiv versions" | v1 ≠ v2 in §§3–4 | MISMATCH (F2) |
| [2] §2.1.8, p. 15 | memoir v1 and v2, printed p. 15 = pdf 21 | OK |
| [2] §5.2.1, p. 119; §§5.5.3–5.5.4, p. 122; closed M; I(F) = I(M,M^0;ΛF) | printed 119 = pdf 125; 122 = pdf 128; §5.1 p. 123; identical in v2 | OK |
| [2] "(v1, 7 February 2024)" | v2 of 13 Feb 2024 exists | SHOULD-FIX (F3) |
| §5 facts (2026-09-03) | adjudication §2 C6 A2-03 and live 2026-09-06 | OK |

## 3. Witness re-derivations (own notation, brief)

(a) g_N = θ(ξ−Ne_1) ∈ S^{-∞}. (3.4) over Q ⊂ K×B̄(0,ρ): supp g_N ⊂ {|ξ| > N−r}, zero for N > ρ+r. (3.5): compact ξ-support, limsup = 0. (3.1) with η = ξ−Ne_1: sup_{|η|≤r} |∂^βθ(η)|(1+|η+Ne_1|)^{|β|−m} ≥ (inf of the weight)(sup|∂^βθ|) = (1+N−r)^{|β|−m} sup|∂^βθ| → ∞ for |β| > m; such β exist in every order (a compactly supported nonzero θ is no polynomial). Refutes Prop. 3.2; with |β| > m' refutes the first assertion of Cor. 3.4. Correct.

(b) c_i = (1+iR)^{m+1}, b_j = Σ_{i≤j} c_iθ(ξ−iRe_1), R > 2r. b_j − b_i supported in |ξ| ≥ (i+1)R−r: all (3.5) seminorms 0, (3.4) seminorms over a fixed Q zero for i large; Cauchy in S'^m. C^∞-limit b with |b(x,iRe_1)|(1+iR)^{−m} = 1+iR → ∞, so b ∉ S^m; a limit in S'^m would equal b in C^∞. Extended seminorm of the class a: lim ‖b_j‖' = 0; ‖φ(a)‖' = ‖b‖'_{K,0,0,m} = sup_x limsup |b|/|ξ|^m ≥ limsup_i (1+iR)^{m+1}/(iR)^m = ∞. So the identity at the top of p. 17 fails exactly there. Correct.

(c) c_j = e^jθ(ξ−je_1); K = {x_0}; ε_k = ½ inf_j e^j(1+j)^{−k} > 0; W_k = {‖a‖_{K,0,0,k} < ε_k}; W = acx(∪W_k) is a 0-nbhd of ind_k S^k. For w ∈ W_k: |w(x_0,je_1)| ≤ ‖w‖_{K,0,0,k}(1+j)^k < ε_k(1+j)^k ≤ e^j/2. So c_j = Σλ_iw_i with Σ|λ_i| ≤ 1 gives e^j < e^j/2. Correct; no regularity used.

(d) a_j(x'',ξ) = j^{m̄'}g(x'')ψ̂_*(ξ/j) (partial Fourier transform, ψ_*(j·) scales by j^{−n'}); with ξ = jη, (1+|ξ|)^{|β|−m̄_1} = j^{|β|−m̄_1}(1/j+|η|)^{|β|−m̄_1}, giving the displayed formula. Φ_{β,m̄_1} ≤ C for m̄_1 ≤ 2N_0 (Schwartz decay when |β| ≥ m̄_1; when |β| < m̄_1 ≤ 2N_0 use |∂^βψ̂_*(η)| ≤ C|η|^{2N_0−|β|} near 0, so the product is ≤ C|η|^{2N_0−m̄_1} ≤ C on |η| ≤ 1). Φ_{0,m̄'}(j) ≥ |ψ̂_*(η_0)| min{(1+|η_0|)^{−m̄'}, |η_0|^{−m̄'}} > 0. Hence u_j → 0 in I^{m''}, u_j ↛ 0 in I^{m'}. Correct once the support hypothesis of F1 is added (the partition-of-unity replacement family sums to 1 and is subordinate to the same cover; closed-graph independence of the topology holds). Transfer to (M̆,∂M) with supp ψ ⊂ (½,1): u_j ∈ C_c^∞(M̊) ⊂ I^m_M(M̆,∂M); refutes Cor. 6.21. Correct.

(e) u_j = j^{−m'}χ(jx)g(y), supp ⊂ {1/(2j) < x < 2/j}. (6.42) zero for j large; (6.43) zero for every j; sup x^{−m'}|u_j| ≥ (1/j)^{−m'}j^{−m'}·1 = 1 with P = 1 ∈ Diff_b. Refutes Prop. 6.12 (m' = m) and the first assertion of Cor. 6.14 (m' < m). v_j = e^jχ(jx)g(y), W_k = {u ∈ A^{−k}: sup x^k|u| < ½ inf_i e^i i^{−k}}; at (1/j,y_0): |w(1/j,y_0)| < ε_k j^k ≤ e^j/2; same contradiction; refutes the second assertion. J^m(M,L) has the same local description (7.27) with Diff(M,L) ∋ 1 and weight 𝒙^m near L; supports in {½ < jx < 2} ⊂ M\L; refutes Cor. 7.13. Correct.

(f) b_j = χ_j(x)(1+|ξ|²)^{j/2} ∈ S^j \ S^m (m < j). Given an absolutely convex 0-nbhd W of S^∞ and basic W_k ⊂ W ∩ S^k: for j with supp χ_j ∩ K_1 = ∅ (local finiteness), b_jρ_R ∈ S^{−∞} ⊂ S^1 vanishes on K_1×R^l so 2b_jρ_R ∈ W_1; b_j(1−ρ_R) ∈ S^{j+1} is supported in |ξ| ≥ R and Leibniz gives its S^{j+1}-seminorms ≤ C_j/R, so 2b_j(1−ρ_R) ∈ W_{j+1} for R large; b_j = ½(2b_jρ_R) + ½(2b_j(1−ρ_R)) ∈ W; finitely many remaining b_j are absorbed. Bounded, in no step: not regular, hence not boundedly retractive and (Cor. 6.5 as quoted p. 5) not acyclic. Correct; the memoir §2.1.8 restatement is false for non-compact U.

(1) For |γ| = k: Taylor/Landau–Kolmogorov on a box of side h gives |∂^ka| ≲ h^{−k} sup|a| + h^{n−k} sup|∂^na|. With sup|a| ≤ N_m(a;0)(1+|ξ|)^m (global because a vanishes off K), h = (1+|ξ|)^{1−c} in ξ (or (1+|ξ|)^{−c} in x), kc = (m'−m)/2 and n with (n−k)c ≥ m''−m': first term ≤ N_m(a;0)(1+|ξ|)^{−(m'−m)/2} ≤ R^{−(m'−m)/2}N_m(a;0) on 1+|ξ| > R, second ≤ max_Γ N_{m''}; on 1+|ξ| ≤ R, N_{m'} ≤ R^{m''−m'}N_{m''}. R_0 from h ≤ (1+|ξ|)/2. Hence (1). On V = {N_m(·;0) < 1}, applied to a−a_0 ∈ 2V, the S^{m'}- and S^{m''}-topologies coincide: the p. 4 criterion with k' = k+1 and all k'' ≥ k'. Correct. Bounded sets have relatively compact image (Arzelà–Ascoli + tail (1+|ξ|)^{m−m'}); a 0-nbhd does not (a_λ = ελ^{−k_0} sin(λx_1)θ_1(x)θ(ξ)), so not compact operators. Correct.

Repairs: Claim 6.46 — A bounded in some A^m (regularity); on A the A(M)-, A^{m'}- and A^m-topologies coincide (bounded retractivity, m' < m); W ∩ A open in A for the A(M)-topology gives V with V ∩ A ⊂ W; then A ∩ V = R(E_{m'}(A∩V)) ⊂ R(B ∩ U). Correct; the printed "m' > m" is indeed the wrong direction for E_{m'} on A ⊂ A^m. Prop. 8.8 identical with Cor. 7.31 (p. 60). Cor. 3.5: (1−χ(ξ/R))a has S^{m'}-seminorms ≤ CR^{m−m'} by Leibniz (each term ≤ C(1+|ξ|)^{m−m'+|β''|}R^{−|β''|} on R ≤ |ξ| ≤ cR, or (1+|ξ|)^{m−m'} on |ξ| ≥ R); x-cut-off exact on compacts. Correct. Remark 3.8 from (c). Correct. Cor. 6.27 / 7.22: ∂^β_ξ a(x'',0) = β! v_β(x'') shows the coefficient C^∞-topology ≤ every S^{m̄_1}-topology, and |ξ|^{k−β}(1+|ξ|)^{β−m̄_1} ≤ 1 for k ≤ k_0 ≤ m̄_1 shows the converse; so all S^{m̄_1} with m̄_1 ≥ k_0 agree on polynomial symbols of degree ≤ k_0, and m̄', m̄'' > m̄ ≥ deg. Correct; (6.49) transfers to 𝒦^m(M).

## 4. What I could not check, and one aside for the program record

- zbMATH an:7901419 (HTTP 403 to the fetcher) and Unpaywall (API requires an e-mail parameter; not sent): the §5 claims about them rest on `novelty/adjudication.md` §2 C6 (2026-09-03) only. MathSciNet closed to the program.
- The full proof of (1) with constants, and the b-collar analog: mechanism and exponents re-derived; the detailed Taylor bookkeeping in `alkl23-note-derivations.md` §9 was not line-audited.
- The vector-bundle versions I(M,L;E), J(F) = J(M,M^0;ΛF) of the memoir: the note's "covered by the above" assumes the scalar argument localizes to bundle coefficients; plausible (finite products locally), not written out anywhere.
- Aside (program record, not the note): arXiv **v2 (29 Jul 2023) already carries the published numbering** of §§6–7 (v2 lines: Prop. 6.12, Cor. 6.14, Cor. 6.21, Cor. 6.27, Prop. 6.29, Claim 6.46, Cor. 7.13, Cor. 7.22, Prop. 7.26, Cor. 7.31, Prop. 8.8, all as published; Remark 3.7 cites "Proposition 6.10"). `novelty/adjudication.md` §2 C6 and `w3-adjudication.md` say the renumbering entered at v3; that should read v2. The note's sentence about v3 remains true.
- Not re-verified: that the sponsor wishes to sign as "Kunal Tyagi" (consistent with `results/arxiv/*/main.tex`).

Files: this report; scratch build and page renders in the session scratchpad (`build/`, `img/`, `alkl-v2.txt`, `alkl-v3.txt`, `memoir-v2.txt`, `wdiff2.py`).
