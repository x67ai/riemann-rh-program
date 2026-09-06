# repair3-log.md — Session 17 repair of `alkl23-note.tex` and creation of the sendable companion `alkl23-derivations.tex`

Repairer: Session 17 repair agent (Fable 5.1). Started: Sun Sep  6 14:49:04 IST 2026.
Inputs: `adjudication.md` (§Recommendation items 1–11, companion list C1–C9, §A/§B/§C reasons), `alkl23-note.tex`, `alkl23-note-derivations.md`, the twelve referee reports, `novelty/ALKL-2024-published.txt`.
Rule applied: every fact changed is checked against the published text or a live web query before the edit is made; no report quotation is trusted unopened.

## Task 1 — read adjudication.md in full and the note in full
- 2026-09-06 14:49 IST: Read adjudication.md in full (all sections: verdict table rows 1–22, §A N1–N6, §B N7–N12, §C C1–C10, §D D1–D7, §E O1–O9, §Recommendation items 1–11 and the companion list, §Summary). Read alkl23-note.tex in full (80 lines; §§1–5, bibliography). Read alkl23-note-derivations.md in full (222 lines, §§0–13).

## Verification of every fact touched by items 1–11 (done before editing; 2026-09-06 14:50–15:05 IST)
Published text (`novelty/ALKL-2024-published.txt`, page markers "Page k of 68"; pp. 39 and 56 also rendered from the PDF at 200 dpi):
- p. 18: "Remark 3.7 Another proof of Corollary 3.5 could be given like in Proposition 6.10." — item 9 confirmed.
- p. 22: "I^m(M,L), which becomes a Fréchet space [25, Sections 6.2 and 6.10]" — item 6 confirmed.
- p. 23: "Corollary 4.7 has extensions for ⋃_m I^m(M,L) and I_{·/c}(M,L), except acyclicity in the case of I(M,L)." — item 4 confirmed. Proof of Cor. 4.7: "I(M,L) is semi-Montel because C^∞(M\L) and S^∞(N*L_j; ΩN*L_j) are Montel spaces (Corollary 3.6)", with L_j = L ∩ U_j (p. 22) — item 9's second clause confirmed.
- p. 37: "there is a continuous inclusion x^m L^∞(M) ⊂ C^{−∞}(M)" — item 6 confirmed.
- p. 38: A^m(M) with "the projective topology given by the maps P: A^m(M) → x^m L^∞(M) (P ∈ Diff_b(M))"; "Let {P_j | j ∈ N_0} be a countable C^∞(M)-spanning set of Diff_b(M). The topology of A^m(M) can be described by the semi-norms ‖·‖_{k,m} (k ∈ N_0) given by (6.41)" — item 6 (countable family) confirmed.
- p. 40: (6.47) "Ȧ^m(M) = I^m_M(M̆,∂M) ⊂ I^m(M̆,∂M) (m ∈ R), which are closed subspaces"; §6.13 "K^m(M) = Ȧ^m_{∂M}(M)" — item 8 confirmed. p. 41: "closed subspaces of Ȧ^{(s)}(M), Ȧ^m(M) and Ȧ(M), respectively"; p. 58: "K^m(M,L) = I^m_L(M,L) ... closed subspaces" — item 8's chain K^m(M) = Ȧ^m_{∂M}(M) = I^m_{∂M}(M̆,∂M) = K^m(M̆,∂M) with subspace topologies confirmed.
- p. 46: "Corollary 6.38 A^m(M) ≡ x^m H_b^∞(M) ≡ x^{m+1/2} H^∞(M̊) (m ∈ R)"; p. 47: "Remark 6.41 Corollary 6.39 and the first identities of Corollaries 6.38 and 6.40 are independent of g. So they hold true without the assumptions (A) and (B)." — item 6 confirmed.
- p. 50: "Let 𝑴 be the smooth manifold with boundary defined by 'cutting' M along L" — item 3's "(pp. 50, 56)" confirmed. p. 56: (7.26) π_*: A(𝑴) → J(M,L); "Extend |x| to a function 𝒙 on M that is positive and smooth on M\L. Its lift π^*𝒙 is a boundary defining function of 𝑴"; (7.27) J^m(M,L) = {u ∈ C^{−∞}(M,L) | Diff(M,L)u ⊂ 𝒙^m L^∞(M)} — item 3's inserted clause confirmed.
Live record (all re-run by this agent on 2026-09-06, ~14:50–15:05 IST; raw responses kept in the session scratchpad `live/`):
- arXiv API for 2304.00798: latest v3 (2024-06-01); abs page lists v1, v2, v3; https://arxiv.org/abs/2304.00798v4 → HTTP 404. "v1 to v3 only" confirmed.
- Crossref works/10.1007/s11868-024-00617-y: update-to None, relation {}, is-referenced-by-count 0; reverse filter `updates:` → total-results 0. "carries no correction" and "Crossref ... no citing work" confirmed.
- Crossmark dialog (crossmark.crossref.org/dialog/?doi=...): the page contains "Document is current" (the JSON endpoint returns an empty body; the dialog HTML was used). Confirmed.
- zbMATH API document/7901419: identifier 1564.46031; editorial_contributions = one entry of type "summary" (text unavailable for license reasons), no review, no corrigendum; document_type journal article. "zbMATH 7901419 (Zbl 1564.46031) carries no review or corrigendum" confirmed.
- OpenAlex W4399476425: cited_by_count 0. Semantic Scholar DOI record: citationCount 0, citations []. "DOI-based citation indexes ... list no citing work" confirmed.
- Google Scholar (curl, no captcha): result "Topology of the space of conormal distributions" shows "Cited by 3"; the cites page lists exactly three: (i) "A trace formula for foliated flows", Álvarez López–Kordyukov–Leichtnam (ecommons.udayton.edu copy); (ii) "Analytic Tools", same authors, in *A Trace Formula for Foliated Flows*, 2026, Springer; (iii) T. E. Gilsdorf, *Locally Convex Spaces: Banach Space Theory, Mathematical Physics, and Distribution Theory Applications*, 2026 (book). None is a correction. "Google Scholar lists three, among them Chapter 2 of [ALKL24m]" confirmed.
- Crossref works/10.1007/978-3-032-15413-2: type book, "A Trace Formula for Foliated Flows", container Lecture Notes in Mathematics, publisher Springer Nature Switzerland, location Cham, issued 2026, created 2026-05-03, ISBN 9783032154125 / 9783032154132; chapter _2 "Analytic Tools" pp. 13–99 (its reference 2_CR11 is the paper); chapter _5 "Conormal Leafwise Reduced Cohomology" pp. 159–176. Crossref carries no series volume number.
- Springer book page (WebFetch through the idp.springer.com cookie bounce; curl is blocked by a Cloudflare challenge): "Lecture Notes in Mathematics (LNM, volume 2387)", Springer Cham, © 2026, eBook 03 May 2026, softcover 05 May 2026, ISBN 978-3-032-15413-2 (eBook) / 978-3-032-15412-5 (softcover), XI + 228 pp.; Analytic Tools pp. 13–99; Conormal Leafwise Reduced Cohomology pp. 159–176. "vol. 2387, Springer, Cham (2026)" confirmed.
- arXiv API for 2402.06671: v2 (2024-02-13), abs page lists v1, v2; no journal-ref field. Confirmed.
- Memoir pagination (pdftotext of the repo copies of v1 and v2, `fetched-r3/r3s-17-…v1` and `r3s-39-…v2`, plus a fresh download of v2 whose text is byte-identical to the repo copy): the note's memoir page numbers are the PRINTED arXiv page numbers (front matter shifts the PDF index by 6). §2.1.8 with the Cor. 3.4–3.6 restatement on printed p. 15; "2.5.10. Filtration of A(M) by bounds" and "the topologies of A(M) and C^∞(M̊) coincide on every A^m(M)" on printed p. 38; §2.6.7 header on printed p. 52 and "the topologies of J(M,L) and C^∞(M\L) coincide on every J^m(M,L)" on printed p. 53; "5.2.1. Injectivity ... compactly retractive (Section 2.2.2)" on printed p. 119; "5.5.3 ... J(F) is compactly retractive (Section 2.6.7)" and "5.5.4 ... Since I(F) is compactly retractive" on printed p. 122. Identical in v1 and v2. "the same in v1 and v2" confirmed; the "arXiv p." relabeling is correct as printed page numbers.
- Dates: today is 2026-09-06; the \date line and §5's "As of September 6, 2026" already carry today's date, so neither is changed.

### Task 2 — edits applied to alkl23-note.tex (each old string asserted present exactly once, grep -cF and str.count, before the edit)
- E1 (item 1, companion attached): line 29; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E2 (item 2): line 47; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3a (item 3, pages): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3b (item 3, J-membership clause): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E3c (item 11, memoir pages in (e)): line 58; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E4 (item 4): line 60; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E4b (item 11, memoir page in (f)): line 60; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E5a (item 5, constants): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E5b (item 5, epsilon-delta step): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E6 (item 6, Frechet fill): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E7 (item 7, Claim 6.46 clause): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E8 (item 8, Cor. 6.27 via (6.47)): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9a (item 9, Remark 3.7): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9b (item 9, Montel clause of Cor. 4.7): line 67; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E9c (item 11, memoir pages in section 4): line 69; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E10 (item 10 + item 11 clause, section 5): line 72; grep -cF of the old string = 1 (exactly once) before the edit; applied.
- E11 (item 11, bibliography): line 77; grep -cF of the old string = 1 (exactly once) before the edit; applied.

### Task 2 — every changed line of alkl23-note.tex against the pre-repair commit 26f306c (the auto-commit watchdog had already folded the edits into HEAD, so the diff is taken against 26f306c; fragments shown as [OLD] -> [NEW]; full unified diff in `xcheck-s17/repair3-note.diff`)
- line 29:
    insert after '...nces) stands once this is done': [] -> [; the proofs of the estimate \eqref{interp} and of the assembly in \S4 are written out in full in the accompanying derivations]
- line 47:
    insert after '..., $\rho\in C_c^\infty(U_1)$, $': [] -> [0\le\rho\le1$, $]
- line 58:
    insert after '...ed by cutting $M$ along $L$ (p': [] -> [p]
    insert after '... by cutting $M$ along $L$ (p.~': [] -> [50, ]
    insert after '...12<jx<2\}\subset M\setminus L$': [] -> [ (both lie in $C_c^\infty(M\setminus L)$, hence in every $J^{m_1}(M,L)$, since $Pu$ is then compactly supported where $\boldsymbol x$ is bounded below)]
    delete after '... second assertions at \S2.5.10': [, p.~38,] -> []
    insert after '...\S2.5.10, p.~38, and \S2.6.7, ': [] -> [arXiv p]
    insert after '....5.10, p.~38, and \S2.6.7, p.~': [] -> [38, ]
- line 60:
    insert after '...nifold, and to \cite[\S2.1.8, ': [] -> [arXiv ]
    insert after '....3, p.~23, excepts acyclicity ': [] -> [in the case o]
    replace after '...3, p.~23, excepts acyclicity f': [or] -> [ $I(M,L)$ when $M$ is]
    insert after '...pts acyclicity for non-compact': [] -> [, while still claiming it for]
    insert after '...s acyclicity for non-compact $': [] -> [\bigcup_mI^m(]
    insert after '... acyclicity for non-compact $M': [] -> [,L)$ and $I_c(M,L)]
    delete after '...ct $M$; the symbol statements ': [d] -> []
    insert after '... $M$; the symbol statements do': [] -> [f \S3 make]
    insert after '...$; the symbol statements do no': [] -> [ excep]
    insert after '...; the symbol statements do not': [] -> [ion of any kind]
- line 67:
    delete after '...gorov type) on boxes of side $': [\sim] -> []
    insert after '...$\xi$ in the region $1+|\xi|>R': [] -> [$, with $c=(m'-m)/(2|\gamma|)$ (for $\gamma\ne0$; for $\gamma=0$ the bound is elementary, with $\Gamma=\{0\}$, $C=1$, $R_0=1$), an integer $N>|\gamma|+(m''-m')/c$, $\Gamma=\{\gamma\}\cup\{N\chi_S:\emptyset\ne S\subset\{1,\dots,d+l\}\}$ ($d=\dim U$; $N\chi_S$ equal to $N$ on $S$ and $0$ elsewhere), $R_0=\max\{1,(2N\sqrt l)^{1/c}\}$, and $C$ depending only on $m,m',m'',\gamma,d,l$: the term of the Taylor bound without derivatives carries the exponent $c|\gamma|+m-m'=-(m'-m)/2$ of $1+|\xi|$, and each other term the exponent $-c(N|S|-|\gamma|)+m''-m'<0]
    insert after '...N_m(\cdot\,;0)<1\}$ of $S^m_K$': [] -> [ (given $\varepsilon$ and finitely many $\gamma_i$, choose $R$ with $CR^{-(m'-m)/2}<\varepsilon/2$ and then $\delta$ with $CR^{m''-m'}\delta<\varepsilon/2$; the neighborhood being absolutely convex, the resulting inclusion of neighborhoods gives coincidence of the two topologies on it)]
    insert after '...ose steps are Fr\'echet spaces': [] -> [ (for $I^m(M,L)$ by p.~22; for $A^m(M)$, hence $J^m(M,L)$, by Cor.~6.38 with Remark~6.41, or directly: the topology is given by the countable family (6.41), and a Cauchy sequence converges in $x^mL^\infty(M)\subset C^{-\infty}(M)$, p.~37, for $P=1$ and then for every $P$; the remaining three are closed subspaces)]
    insert after '...d then of their Montel clauses': [] -> [ (the printed Montel step of Cor]
    insert after '... then of their Montel clauses.': [] -> [~4.7 also cites Cor.~3.6 over the non-compact base $L_j$; the compactly based models avoid this as well).]
- line 69:
    insert after '... is bounded in some $A^m(M)$, ': [] -> [and ]
    replace after '... bounded in some $A^m(M)$, on ': [w] -> [t]
    replace after '...ounded in some $A^m(M)$, on wh': [ic] -> [at ]
    insert after '...ded in some $A^m(M)$, on which': [] -> [ull]
    insert after '...57). Cor.~3.5 follows directly': [] -> [ (as Remark~3.7, p.~18, anticipates)]
    insert after '...is the case $(\Mb,\partial M)$': [] -> [:]
    replace after '...s the case $(\Mb,\partial M)$ ': [via] -> [by]
    replace after '...se $(\Mb,\partial M)$ via (6.4': [9] -> [7]
    insert after '... $(\Mb,\partial M)$ via (6.49)': [] -> [, $\mathcal K^m(M)=\dot A^m_{\partial M}(M)=I^m_{\partial M}(\Mb,\partial M)=K^m(\Mb,\partial M)$ with the same subspace topologies]
    insert after '...and $J(\mathcal F)$ (\S5.2.1, ': [] -> [arXiv ]
    insert after '...2.1, p.~119; \S\S5.5.3--5.5.4,': [] -> [ arXiv]
- line 72:
    insert after '... the DOI carries no correction': [] -> [ and the publisher's Crossmark record reads ``Document is current'']
    insert after '...the DOI carries no correction,': [] -> [ and]
    insert after '... no correction, zbMATH 7901419': [] -> [ (Zbl 1564.46031)]
    insert after '...rries no review or corrigendum': [] -> [. The DOI-based citation indexes (Crossref]
    replace after '...ies no review or corrigendum, ': [a] -> [Ope]
    replace after '...s no review or corrigendum, an': [d] -> [Alex,]
    insert after '...rigendum, and Semantic Scholar': [] -> [)]
    delete after '...dum, and Semantic Scholar list': [s] -> []
    insert after '...c Scholar lists no citing work': [] -> [;]
    replace after '... Scholar lists no citing work ': [(a] -> [Goog]
    replace after '...holar lists no citing work (al': [l] -> [e]
    replace after '...lar lists no citing work (all ': [four re-] -> [S]
    delete after '...no citing work (all four re-ch': [ecked ] -> []
    replace after '...ng work (all four re-checked o': [n th] -> [l]
    replace after '...rk (all four re-checked on tha': [t date); Unpaywall] -> [r]
    insert after '... on that date); Unpaywall list': [] -> [s thr]
    replace after '...on that date); Unpaywall liste': [d] -> [e, among them Chapter~2 of \cite{ALKL24m},]
    insert after '...hat date); Unpaywall listed no': [] -> [ne of them a]
    insert after '...Unpaywall listed no correction': [] -> [;]
    replace after '...npaywall listed no correction ': [DOI] -> [the restatements]
    insert after '...all listed no correction DOI o': [] -> [f the affected sentences noted i]
    insert after '...l listed no correction DOI on ': [] -> [\]
    insert after '... listed no correction DOI on S': [] -> [3 ar]
    insert after '...listed no correction DOI on Se': [] -> [ presumably now in print in that cha]
    delete after '...ted no correction DOI on Septe': [mbe] -> []
    delete after '...no correction DOI on September': [ 3, 2026] -> []
    replace after '...f \eqref{interp}, and of \S4 a': [r] -> [ccompany this not]
    delete after '...\eqref{interp}, and of \S4 are': [ available on request] -> []
- line 77:
    insert after '....~A. Kordyukov, E. Leichtnam, ': [] -> [\emph{]
    replace after '...A. Kordyukov, E. Leichtnam, A ': [t] -> [T]
    replace after '...dyukov, E. Leichtnam, A trace ': [f] -> [F]
    replace after '...eichtnam, A trace formula for ': [f] -> [F]
    replace after '... A trace formula for foliated ': [f] -> [F]
    insert after '...ace formula for foliated flows': [] -> [}]
    insert after '...ce formula for foliated flows,': [] -> [ Lecture Notes in Mathematics, vol.~2387, Springer, Cham (2026), \url{https://doi.org/10.1007/978-3-032-15413-2};]
    insert after '...02.06671 (v2, 13 February 2024': [] -> [). Sections are cited by number]
    insert after '...v2, 13 February 2024; the page': [] -> [ number]
    replace after '..., 13 February 2024; the pages ': [c] -> [g]
    replace after '...13 February 2024; the pages ci': [t] -> [v]
    replace after '... February 2024; the pages cite': [d] -> [n]
    insert after '...uary 2024; the pages cited are': [] -> [ those of the arXiv version,]
    replace after '...pages cited are the same in v1': [)] -> [ and v2]
- changed lines: [29, 47, 58, 60, 67, 69, 72, 77]; unchanged: 73 of 81.

### Task 3 — C1–C9 applied to the internal companion alkl23-note-derivations.md (dated tags; internal apparatus kept there)
- header note: line 3; old string present exactly once; applied with a dated tag.
- C9a (6.43): line 32; old string present exactly once; applied with a dated tag.
- C9b (7.26): line 37; old string present exactly once; applied with a dated tag.
- C1 (§5 neighborhood N): line 91; old string present exactly once; applied with a dated tag.
- C2 (§5 η_0): line 105; old string present exactly once; applied with a dated tag.
- C3 (§6 J-membership): line 127; old string present exactly once; applied with a dated tag.
- C4 (§7 item 5): line 142; old string present exactly once; applied with a dated tag.
- C5 (§9.5 R_0 per γ_i): line 183; old string present exactly once; applied with a dated tag.
- C6 (§9.6 roles of k, k′, k″): line 188; old string present exactly once; applied with a dated tag.
- C7 (§9.7 Fréchet fill): line 194; old string present exactly once; applied with a dated tag.
- C7b (§9.7 int K ≠ ∅): line 196; old string present exactly once; applied with a dated tag.
- C8 (§10.2 index m′ < m): line 204; old string present exactly once; applied with a dated tag.
- N8 alignment note (§10.4): line 210; old string present exactly once; applied with a dated tag.

### Task 3 — sendable companion created: `results/c3-r/s14/alkl23-derivations.tex` / `.pdf` (2026-09-06 15:05–15:15 IST)
Source: `alkl23-note-derivations.md` converted by hand from Unicode math to LaTeX, section by section (§§0–12), with the same preamble, author line, AI-use footnote and date as the note, plus `longtable`/`array` for the §0 table and five macros (`\MB` bold M, `\xb` bold x, `\dist`, `\interior`, `\Mstar`). Title as instructed. Bibliography labels [P], [M], [W] (the .md's conventions), the [M] entry being the note's new LNM 2387 entry.
Changes relative to the .md (all C1–C9 as ruled in adjudication §C, the reasons re-derived here before applying):
- C1 (§5): ρ = 1 on a neighborhood N of the compact set x^{−1}({0} × supp g) ⊂ L (was: of p_0); 0 ≤ ρ ≤ 1 added (matches the note's item 2).
- C2 (§5): "pick η_0 ≠ 0 with ψ̂_*(η_0) ≠ 0 (exists: ψ̂_* is entire and ≢ 0, so its zero set has empty interior)" (was: "η_0 ≠ 0 automatically", false for N_0 = 0).
- C3 (§6): the chain C^∞(M) ⊂ J^{(∞)}(M,L) ⊂ J^{m_1}(M,L) removed; membership via C^∞(M) ⊂ C^{−∞}(M,L) by (7.28) plus the direct bound (Pu_j compactly supported away from L, where 𝒙 is bounded below).
- C4 (§7 item 5): the family (1+j)^{m′}ψ(x)θ(ξ−je_1) replaced by the dilated annular bump a_j = ψ(x) j^{m′} φ(ξ/j), φ ∈ C_c^∞({½<|η|<2}), φ(e_1) = 1; re-derived: every S^{m″}-seminorm ≤ C j^{m′−m″} → 0, ‖a_j‖_{K′,0,0,m′} ≥ (j/(1+j))^{m′} → 1, a_j ∈ V for all j.
- C5 (§9.5): R ≥ max_i R_{0,i}, with C_i, R_{0,i}, Γ_i the constants of 9.4 for γ_i.
- C6 (§9.6): the roles stated explicitly: orders −k > −k′ > −k″ (k < k′ < k″), w = e^ϱ, (k,k′,k″) in the roles of (m,m′,m″), c = (k′−k)/(2|γ|) > 0, N > |γ| + (k″−k′)/c; both exponents and the w ≤ R regime recomputed; the resulting b-model inequality written out.
- C7 (§9.7): the Fréchet fill of N1 added for A^m(M) (Cor. 6.38 + Remark 6.41, or the direct Cauchy-sequence argument via x^mL^∞(M) ⊂ C^{−∞}(M), p. 37) and its transfer to J^m ≅ A^m(𝑴) and the three closed subspaces; the transfer rule noted to need only (M*) of the target; "int K ≠ ∅, since S^m_K = {0} otherwise, θ_1 ∈ C_c^∞(int K)" added to the non-compactness remark.
- C8 (§10.2): E_{m′} with m′ < m stated explicitly (domain J^{m′} ⊃ J^m), "not m′ > m".
- C9 (§0 table): (6.43) written as lim_{ε↓0} sup_{0<x<ε} (rendered p. 39 checked); (7.26) written π_*: A(𝑴) → J(M,L) (rendered p. 56 checked: bold π, subscript star, bold M).
Internal apparatus removed: the program/status header (replaced by a two-sentence intro naming the note and the citation conventions); the "(adjudication)" mentions (§3's second-gap parenthetical now reads without attribution; §6 "as the adjudication also notes" dropped; §9.7's closing sentence about "the brief" and "the W3 adjudication" dropped); §0's numbering paragraph keeps the cross-version numbers but not the internal file names and line numbers; §12's sourcing line replaced by the note's §5 public-record paragraph (same sentences as the note's new §5, record part); §13 "Deviations from the brief" deleted.
Additions beyond C1–C9 (all verified against the published text or the memoir text before insertion): §0 rows for Remark 3.7 (p. 18), the p. 22 cover sentence with L_j = L ∩ U_j and "becomes a Fréchet space", the Cor. 4.7 Montel-step quotation (p. 23), x^mL^∞(M) ⊂ C^{−∞}(M) (p. 37), the countable spanning set sentence (p. 38), §6.13's K^m(M) = Ȧ^m_{∂M}(M) (p. 40), Cor. 6.38 / Remark 6.41 (pp. 46–47), "cutting M along L" (p. 50), and the [M] §2.5.10 / §2.6.7 restatements (arXiv pp. 38, 53); §9.4 states the γ = 0 case as an instance of (1) with Γ = {0}, C = 1, R_0 = 1 (matching the note's new parenthetical); §9.7's Montel item carries N11's half-clause; §10.3 mentions Remark 3.7 (N10); §10.4 uses the (6.47) chain 𝒦^m(M) = Ȧ^m_{∂M}(M) = I^m_{∂M}(M̆,∂M) = K^m(M̆,∂M) as the note now does (N8), with (6.49) noted as not used; §11 records the LNM 2387 publication. Not added: N12's non-injectivity example (optional, not requested).
The internal .md keeps its apparatus and received C1–C9 with dated "[corrected 2026-09-06 per xcheck-s17 …]" tags (13 replacements, each old string present exactly once), plus a header line pointing to the .tex and an N8 alignment note in §10.4.

### Task 4 — builds (pdflatex twice each, TeX Live 2026)
- `alkl23-note.pdf`: exit 0 on both passes; 0 errors; 0 Overfull/Underfull boxes; 4 pages (was 3). pdftotext confirms the changed passages: "accompanying derivations" (§1), "0 ≤ ρ ≤ 1" (d), "(pp. 50, 56)", "(both lie in C_c^∞(M\L), hence in every J^{m_1}(M,L), since Pu is then compactly supported where x is bounded below)", "arXiv pp. 38, 53", "[2, §2.1.8, arXiv p. 15]", the §4.3.3 parenthetical, the §4 constants line with c, N, Γ, R_0, C and the two exponents, the ε–δ parenthetical, the Fréchet fill, "and on that hull", "(as Remark 3.7, p. 18, anticipates)", "by (6.47), 𝒦^m(M) = … = K^m(M̆,∂M) with the same subspace topologies", "(the printed Montel step of Cor. 4.7 also cites Cor. 3.6 over the non-compact base L_j …)", "arXiv p. 119 … arXiv p. 122", the new §5 ("Document is current", "Zbl 1564.46031", "OpenAlex", "Google Scholar lists three, among them Chapter 2 of [2]", "presumably now in print in that chapter", "accompany this note"), and the [2] entry ("vol. 2387, Springer, Cham (2026)"). Pages 2–4 rendered at 130 dpi and read: bold 𝒙 and bold 𝑴 in (e), breve M̆ in the (6.47) chain, primes m′, m″ throughout, \eqref rendered as "(1)".
- `alkl23-derivations.pdf`: exit 0 on both passes; 0 errors; 0 Overfull/Underfull boxes; 0 "??"; no undefined references or citations; 11 pages. pdftotext confirms C1–C9 in place (compact-set neighborhood, "empty interior", "dilated annular bumps", "max_i R_{0,i}", the (k,k′,k″) roles sentence, "Their steps are Fréchet spaces", "int K ≠ ∅", "not m′ > m", (6.43) with lim, (7.26)); pages 1, 7, 8, 9, 11 rendered at 110 dpi and read (table, witness (f), Lemmas A/B and (1), assembly, public record and references).

### Task 5 — page counts, companion changes, deviations from the adjudication's wording
- Page counts: note 4 pp.; companion 11 pp.
- Every changed line of the note: lines 29, 47, 58, 60, 67, 69, 72, 77 (listed fragment by fragment above; full diff in `repair3-note.diff`, taken against 26f306c because the auto-commit watchdog had already committed the edited file).
- Companion changes: listed under Task 3.
- Deviations from the adjudication's replacement text, and why:
  1. Item 3's inserted parenthesis is placed before the comma ("… ⊂ M∖L (both lie …), refute both assertions") rather than literally after it, which would have read ", (both …) refute". Punctuation only.
  2. Item 11, witness (e): "at §2.5.10 and §2.6.7, arXiv pp. 38, 53" (comma form) instead of "(arXiv pp. 38, 53)", because the sentence is already parenthetical and the literal form would nest parentheses; the instruction "write arXiv p. before each memoir page number" is met. (f) and §4 use the adjudication's forms verbatim.
  3. Item 5: two clarifications inserted in the constants sentence, both checked: "(for γ ≠ 0; for γ = 0 the bound is elementary, with Γ = {0}, C = 1, R_0 = 1)", because c = (m′−m)/(2|γ|) is undefined at γ = 0 while (1) is asserted for every γ (the γ = 0 case: N_{m′}(a;0) ≤ R^{m″−m′}N_{m″}(a;0) + R^{m−m′}N_m(a;0), and R^{m−m′} ≤ R^{−(m′−m)/2} for R ≥ 1); and "(d = dim U; …)" because d was undefined in the note (its base dimension is otherwise written n). Everything else in item 5 verbatim.
  4. Item 11's "one clause in §2 or §5": placed in §5 as "; the restatements of the affected sentences noted in §3 are presumably now in print in that chapter." Item 10's second sentence otherwise verbatim; "accompany this note" chosen (companion attached).
  5. Item 1: companion-attached variant, verbatim. Items 2, 4, 6, 7, 8, 9 (both optional clauses), 11 (bibliography and the two other relabelings): verbatim.
- Dates: \date and §5 already read September 6, 2026 (today); unchanged.
- Nothing committed by this agent; the auto-commit watchdog committed the note at 15:00 IST (75c1148) and the .tex/.pdf files at 15:10 IST (711dbfd); the .md and this log await the next auto-commit.
