# alkl23-note REVISION 2 (Session 16, 2026-09-06) - repair pass after rechecks F and O

Repairer: Fable 5.1. Inputs: `alkl23-note-recheck-F.md`, `alkl23-note-recheck-O.md`, the merged list E1-E10 from the orchestrator, the binding record `w3-adjudication.md` (Sections 3.4 and 3.8). Sources opened for verification: the published PDF (text layer, pages split by form feed; pp. 18, 56, 59 rendered at 150 dpi), arXiv v1 (on disk), arXiv v2 and v3 and memoir v2 (downloaded this pass into `fetched-r3/` as r3s-37, r3s-38, r3s-39; text layers extracted with `pdftotext -layout`), memoir v1 (on disk). Live re-checks run on 2026-09-06: arxiv.org/abs/2304.00798 (v1 3 Apr 2023, v2 29 Jul 2023, v3 1 Jun 2024, no v4), arxiv.org/abs/2402.06671 (v1 7 Feb 2024, v2 13 Feb 2024), api.crossref.org record of 10.1007/s11868-024-00617-y (`relation` empty, no `update-to`, no `updated-by`, is-referenced-by-count 0), api.semanticscholar.org (citationCount 0), api.zbmath.org document 7901419 (journal article, links to DOI and arXiv only, no corrigendum entry, no review text). Unpaywall NOT re-run (its API requires an e-mail parameter). Build: TeX Live 2026 pdflatex twice; 3 pages; 0 overfull, 0 underfull; .aux/.log/.out removed. Not committed.

Result: 3 pages, zero overfull/underfull. All ten items applied; two applied in a narrower form than proposed, with the reason given (E1 wording; E4's 'copies' clause). Nothing declined outright. No content cut; page budget met by tightening the margins (0.75/0.65 in to 0.6/0.5 in) and setting the bibliography in \footnotesize.

## Items

**E1 (ERROR, both rereads) - APPLIED, narrower wording.** Verification: word-level diff of the normalized pdftotext of sections 3-4 (from the heading '3. Symbols' to '5. Dual-conormal distributions', running heads stripped): v2 vs v3 = 0 differences; v1 vs v2 = 45 opcodes, all of them in: the U = R^0 notation sentence before Prop. 3.1; Remark 3.7 ('Proposition 6.8' -> '6.10'); section 4.2.2 ('Frechet space' -> 'LCHS' for I_c^(infty)); Sect. 4.3.3 ('Corollary 4.7 can be extended with' -> 'has extensions for'); sections 4.6-4.8 (equations (4.21)-(4.24) -> (4.20)-(4.22), cross-references into section 2 shifted by one, section 4.8 partly rewritten); plus running-head noise. Every item the note cites from sections 3-4 was extracted from v1, v2, v3 and the published text and compared: Prop. 3.2 with its full proof (including 'since ||phi(a)||' = ||a||' < infty' and 'Hence S'^m is complete'), Prop. 3.3, Cor. 3.4, Cor. 3.5, Cor. 3.6 with its proof, Remark 3.8, the p. 18 bundle sentence, Cor. 4.5 with its proof, Cor. 4.7, (3.1), (3.4), (3.5), (4.8), (4.9), (4.10): identical wording in all three arXiv versions and in the published text. The cited sections 6-8 items (Props. 6.10, 6.12, 6.29, 7.26, 8.8; Cors. 6.14, 6.15, 6.16, 6.21, 6.22, 6.27, 6.28, 6.39, 7.13, 7.14, 7.15, 7.17, 7.22, 7.23, 7.31; Remarks 6.17, 6.41; Claim 6.46; (6.41)-(6.43), (6.47), (6.49), (7.26), (7.27)) carry the published numbers in v2 and in v3. Because Sect. 4.3.3, which (f) cites, WAS reworded between v1 and v2 (same content), the new sentence is restricted to 'every proposition, corollary, remark and equation cited here from sections 3-4' rather than 'every statement'.
  OLD: `arXiv:2304.00798v3 has the same numbering, and \S\S3--4 are unchanged in all arXiv versions)`
  NEW: `arXiv:2304.00798v2 and v3 carry the same numbering, and every proposition, corollary, remark and equation cited here from \S\S3--4 has the same number and wording in all three arXiv versions)`

**E2 (ERROR F1 / SHOULD-FIX O2, O F8, O F12c) - APPLIED.** Chart convention checked on published p. 19 (x = (x', x''): U -> U' x U'', L cap U = {x' = 0}). 'meeting L' added so that 0 in U'. supp u_j written with 'subset' (the support of g(x'') psi_*(j x') is contained in {|x'| <= 1/j} x supp g). p_0 and x(p_0) = 0 dropped. eta_0 != 0 added. Index letter f_i kept throughout; the A^m partition of unity in section 4 renamed lambda_i for uniformity. Cross-check against w3-adjudication.md section 3.4: the binding record takes N a neighborhood of a point p_0 and g in C_c^infty(U''), which carries the same gap; the repaired choice (N a neighborhood of the compact set x^{-1}({0} x supp g)) closes it and leaves the rest of the record's derivation unchanged. Re-derivation after the edit: a_j(x'',xi) = j^{n'+m'bar} g(x'') j^{-n'} psi_*hat(xi/j) = j^{m'bar} g psi_*hat(xi/j); d^alpha_{x''} d^beta_xi a_j = j^{m'bar-|beta|} d^alpha g (d^beta psi_*hat)(xi/j); with xi = j eta, (1+|xi|)^{|beta|-m1bar} = j^{|beta|-m1bar}(1/j+|eta|)^{|beta|-m1bar}, giving the displayed identity (the suprema over x'' in K and eta factor). Phi_{beta,m1bar}(j) <= C_beta for m1bar <= 2N_0 (|beta| >= m1bar: weight <= (1+|eta|)^{|beta|-m1bar}, Schwartz decay; |beta| < m1bar: weight <= |eta|^{|beta|-m1bar}, |d^beta psi_*hat| <= C|eta|^{2N_0-|beta|} near 0, product <= C|eta|^{2N_0-m1bar} <= C on |eta| <= 1, weight <= 1 for |eta| >= 1); with m1bar = m''bar <= 2N_0: ||a_j||_{K,alpha,beta,m''bar} <= C j^{m'bar-m''bar} -> 0; the (4.10)-image of u_j is (0,(a_j,0,...)) because supp u_j subset N, so u_j -> 0 in I^{m''}. Lower bound: Phi_{0,m'bar}(j) >= |psi_*hat(eta_0)| (1/j+|eta_0|)^{-m'bar} >= |psi_*hat(eta_0)| min{(1+|eta_0|)^{-m'bar}, |eta_0|^{-m'bar}} = c > 0 for eta_0 != 0 (such eta_0 exists: psi_*hat = (-|eta|^2)^{N_0} psi-hat is a nonzero real-analytic function), so ||a_j||_{K,0,0,m'bar} >= c sup_K |g| > 0 and u_j does not tend to 0 in I^{m'}. Both displayed estimates re-derived and unchanged.
  OLD: `Let $M$ be compact, $\operatorname{codim}L=n'\ge1$, $\dim L=n''$, $m<m'<m''$, and $\bar m,\bar m',\bar m''$ as in (4.9). Take $p_0\in L$, a chart $(U_1,x=(x',x''))$ adapted to $L$ with $x(p_0)=0$, and the partition of unity $\{h,f_i\}$ of (4.10) with $f_1=1$ and $h=f_i=0$ ($i\ge2$) near $p_0$ (replace any $\{h,f_i\}$ by $\{(1-\rho)h,\ \rho+(1-\rho)f_1,\ (1-\rho)f_i\ (i\ge2)\}$, $\rho\in C_c^\infty(U_1)$, $\rho=1$ near $p_0$; by the closed graph theorem the Fr\'echet topology of $I^m(M,L)$ is independent of these choices anyway). Let $g\in C_c^\infty(\R^{n''})$, $g\not\equiv0$; $\psi\in C_c^\infty(\{|x'|<1\})$, $\psi\not\equiv0$;`
  NEW: `Let $M$ be compact, $L\ne\emptyset$, $\operatorname{codim}L=n'\ge1$, $\dim L=n''$, $m<m'<m''$, and $\bar m,\bar m',\bar m''$ as in (4.9). Take a chart $(U_1,x=(x',x''))$ adapted to $L$ and meeting $L$, $x\colon U_1\to U'\times U''$ (p.~19), $g\in C_c^\infty(U'')$, $g\not\equiv0$, and the partition of unity $\{h,f_i\}$ of (4.10) with $f_1=1$ and $h=f_i=0$ ($i\ge2$) on a neighborhood $N$ of the compact set $x^{-1}(\{0\}\times\supp g)\subset L$ (replace any $\{h,f_i\}$ by $\{(1-\rho)h,\ \rho+(1-\rho)f_1,\ (1-\rho)f_i\ (i\ge2)\}$, $\rho\in C_c^\infty(U_1)$, $\rho=1$ on $N$; by the closed graph theorem the Fr\'echet topology of $I^m(M,L)$ is independent of these choices anyway). Let $\psi\in C_c^\infty(\{|x'|<1\})$, $\psi\not\equiv0$;`
  OLD: `u_j(x',x'')=j^{\,n'+\bar m'}\,g(x'')\,\psi_*(jx')\in C^\infty(M)\subset I^{m}(M,L).
\]
For large $j$, $hu_j=0$ and $f_iu_j=0$ ($i\ge2$), and by (4.8) the symbol of $f_1u_j=u_j$ is`
  NEW: `u_j(x',x'')=j^{\,n'+\bar m'}\,g(x'')\,\psi_*(jx').
\]
For $j$ large, $\supp u_j\subset x^{-1}(\{|x'|\le1/j\}\times\supp g)\subset N$, so $u_j\in C_c^\infty(U_1)\subset C^\infty(M)\subset I^{m}(M,L)$, $hu_j=0$ and $f_iu_j=0$ ($i\ge2$), and by (4.8) the symbol of $f_1u_j=u_j$ is`
  OLD: `for any $\eta_0$ with $\hat\psi_*(\eta_0)\ne0$`
  NEW: `for any $\eta_0\ne0$ with $\hat\psi_*(\eta_0)\ne0$`
  OLD: `$u\mapsto((\lambda_ju)_j,\mu u)$ into collar models and $C^\infty(\Mo)$, for a partition of unity $\{\lambda_j,\mu\}$`
  NEW: `$u\mapsto((\lambda_iu)_i,\mu u)$ into collar models and $C^\infty(\Mo)$, for a partition of unity $\{\lambda_i,\mu\}$`
  OLD: `whose symbols vanish outside the compact base projections of the $f_j$`
  NEW: `whose symbols vanish outside the compact base projections of the $f_i$`

**E3 (SHOULD-FIX, both) - APPLIED** (section 2 bundle clause, 'and every l >= 1', 'L != emptyset', and the last sentence of section 2).
  OLD: `the acyclicity and bounded-retractivity clauses of Cor.~3.6 (p.~18) for every non-compact $U$, together with the part of the sentence on p.~18 that extends Prop.~3.2 and Cors.~3.4 and~3.6 to symbols on a vector bundle (the extensions of Prop.~3.3 and Cor.~3.5 are unaffected); Cor.~4.5 (p.~23), for every compact $(M,L)$ with $\operatorname{codim}L\ge1$;`
  NEW: `the acyclicity and bounded-retractivity clauses of Cor.~3.6 (p.~18) for every non-compact $U$ and every $l\ge1$, together with the part of the sentence on p.~18 that extends Prop.~3.2 and Cor.~3.4 to symbols on a vector bundle, and its extension of Cor.~3.6 when the base manifold is non-compact (the extensions of Prop.~3.3 and Cor.~3.5 are unaffected, and the extension of Cor.~3.6 over a compact base is true, \S4); Cor.~4.5 (p.~23), for every compact $(M,L)$ with $L\ne\emptyset$ and $\operatorname{codim}L\ge1$;`
  OLD: `The witnesses below are constant in the base variable up to a fixed cut-off, so they also refute every parametrized or bundle version.`
  NEW: `The witnesses (a)--(e) below are constant in the base variable up to a fixed cut-off, so they also refute every parametrized or bundle version; (f) is inherently non-local.`

**E4 (SHOULD-FIX, both) - APPLIED, without the 'copies' clause.** Published p. 18 read: the semi-Montel step is 'Since S^infty is boundedly retractive, B is contained and bounded in some S^m, and the topologies of S^infty and S^m coincide on B. By Corollary 3.4, it follows that B is a complete bounded subspace of C^infty(U x R^l)'. The note now says that what the step needs is the bounded-set statement, and that it is TRUE (for m' > m, S^{m'}- and C^infty-convergence agree on bounded subsets of S^m), consistent with w3-adjudication.md section 3.8 (O Lemma 6.5.2, CONFIRMED). The draft clause 'the step and its copies in Cors. 4.7, 6.16, 6.22, 6.28, 7.15 and 7.23 go through' was NOT written: the printed proof of Cor. 4.7 (p. 23, read) obtains semi-Montel from the closed TVS-embedding (4.13) into a product of Montel spaces, and Cors. 6.22, 6.28, 7.23 follow it ('closed subspace of the Montel space I(M-breve, dM)'), so they are not copies of the bounded-set step; the note's first section-4 paragraph already covers all six Montel clauses by its own route. Density clause: verified in the published PDF - Prop. 6.10 (p. 37: C_c^infty(M-ring) dense in x^m L^infty(M) with the x^{m'} L^infty topology, direct measure-theoretic proof, no coincidence statement), Cor. 6.15 (p. 39), Remark 6.17 (p. 39: 'Proposition 6.10 provides an alternative direct proof of Corollary 6.15'), Cor. 6.39 (p. 47), Remark 6.41 (p. 47: 'Corollary 6.39 is stronger than Corollary 6.15'), Cor. 7.14 (p. 56), Cor. 7.17 (p. 57), and p. 57: 'The analog of Remark 6.17 makes sense for J(M,L)', 'The analog of Remark 6.41 makes sense for J(M,L)'. The proof chain behind Cor. 6.39 (Cor. 6.38 <- Cor. 6.37, Prop. 6.36, (6.1); Prop. 6.36 <- (6.52), (6.53), Prop. 2.5, Cor. 6.35) was scanned and contains no coincidence statement. Because Remark 6.41 attributes Cor. 6.15 to Cor. 6.39 rather than to Prop. 6.10, the sentence names both routes and both remarks with their p. 57 analogues.
  OLD: `Two printed arguments use a coincidence statement for more than the word ``acyclic''.`
  NEW: `Several printed arguments use a coincidence statement for more than the word ``acyclic''. The semi-Montel step of the printed proof of Cor.~3.6 (p.~18) applies Cor.~3.4 to a bounded subset $B$ of some $S^m$; what it needs is the bounded-set statement, which is true: for $m'>m$, $S^{m'}$- and $C^\infty$-convergence agree on bounded subsets of $S^m(U\times\R^l)$, so, with $m'>m$ in place of $m$ and bounded retractivity in hand, the step goes through.`
  OLD: `Cor.~7.13 is not needed there.`
  NEW: `Cor.~7.13 is not needed there. The density Cors.~6.15 and 7.14, whose printed proofs are modeled on Cor.~3.5's, follow instead from Prop.~6.10 and its $J$-analogue, or from Cors.~6.39 and 7.17 (Remarks~6.17 and 6.41 and their analogues on p.~57).`

**E5 (SHOULD-FIX F5) - APPLIED.** Verified in memoir v1 AND v2: section 2.5.10 (pdf p. 44 = printed p. 38 in both; running head '38  2. ANALYTIC TOOLS'): 'The following is true [ALKL23, Corollaries 6.14-6.16 and 6.39 and Remark 6.41]: the topologies of A(M) and C^infty(M-ring) coincide on every A^m(M) ...'; section 2.6.7 (its heading on pdf p. 58 = printed 52, the sentence on pdf p. 59 = printed p. 53; running head '2.6. CONORMAL SEQUENCE  53'): '... and the topologies of J(M,L) and C^infty(M\L) coincide on every J^m(M,L)'. Sentence added at the end of (e) (folded into the E7 edit below).

**E6 (SHOULD-FIX, both) - APPLIED.** Memoir v2 (arXiv 13 Feb 2024, 176 pp.) checked: section 2.1.8 on pdf p. 21 = printed p. 15 (running head '2.1. SECTION SPACES AND OPERATORS ON MANIFOLDS  15'); section 5.2.1 'is compactly retractive (Section 2.2.2)' on pdf p. 125 = printed 119; sections 5.5.3-5.5.4 on pdf p. 128 = printed 122; identical pages in v1.
  OLD: `arXiv:2402.06671 (v1, 7 February 2024).`
  NEW: `arXiv:2402.06671 (v2, 13 February 2024; the pages cited are the same in v1).`

**E7 (SHOULD-FIX F7) - APPLIED.** Published p. 56 rendered: (7.27) reads 'Diff(M,L) u subset x^m L^infty(M)' with BOLD x and BOLD M; p. 56 also: 'Extend |x| to a function x [bold] on M that is positive and smooth on M\L. Its lift pi^* x is a boundary defining function of M [bold], also denoted by x [bold].' Bold M is now introduced in (e) and the section-4 clause shortened to a back-reference.
  OLD: `Since $J^m(M,L)$ is given by (7.27) with $\Diff(M,L)$ and $x^mL^\infty(M)$, the same $u_j$ and $v_j$, placed in $\{\tfrac12<jx<2\}\subset M\setminus L$, refute both assertions of Cor.~7.13.`
  NEW: `Since $J^m(M,L)$ is given by (7.27) with $\Diff(M,L)$ and $\boldsymbol x^mL^\infty(\boldsymbol M)$, $\boldsymbol M$ the manifold with boundary obtained by cutting $M$ along $L$ and $\boldsymbol x$ extending $|x|$ (p.~56), the same $u_j$ and $v_j$, placed in $\{\tfrac12<jx<2\}\subset M\setminus L$, refute both assertions of Cor.~7.13. (\cite{ALKL24m} restates these second assertions at \S2.5.10, p.~38, and \S2.6.7, p.~53.)`
  OLD: `and $J^m(M,L)\cong A^m(\boldsymbol M)$ by (7.26), where $\boldsymbol M$ is the manifold with boundary obtained by cutting $M$ along $L$.`
  NEW: `and $J^m(M,L)\cong A^m(\boldsymbol M)$ by (7.26).`

**E8 (SHOULD-FIX O3 / F8) - APPLIED.**
  OLD: `$g\in C_c^\infty$ in $y$ with $g(y_0)=1$, $m'<m$, and $u_j=j^{-m'}\chi(jx)g(y)$`
  NEW: `$g\in C_c^\infty$ in $y$ with $g(y_0)=1$, $m'\in\R$, and $u_j=j^{-m'}\chi(jx)g(y)$`

**E9 (SHOULD-FIX O4) - APPLIED.**
  OLD: `Let $U\subset\R^n$ be open and nonempty, $n\ge1$.`
  NEW: `Let $U\subset\R^n$ be open and nonempty, $n\ge1$, and let $l\ge1$.`

**E10 (NITs) - ALL APPLIED.** Prop. 7.26 verified on published p. 59: '(7.36) bigoplus_{m>=0} C^1_m -> K(M,L), where C^1_m = C^infty(L; Omega^{-1} NL)', 'Proposition 7.26 The map (7.36) is a TVS-isomorphism, which induces TVS-isomorphisms (7.37)'; so the finite-sum statement is about K(M,L), and membership in K^m(M,L) is the degree condition v_k = 0 for k > m-bar (a polynomial symbol of exact degree k lies in S^{m-bar} iff k <= m-bar). Section 5: the four checks re-run today are named as such; Unpaywall kept at September 3. \vspace after \maketitle set to -2em (the budget allows it after the margin change).
  OLD: `($u_j=0$ on $\{x<1/2j\}$)`
  NEW: `($u_j=0$ on $\{x<1/(2j)\}$)`
  OLD: `\sup x^k|u|<\tfrac12\inf_ie^ii^{-k}\}`
  NEW: `\sup x^k|u|<\tfrac12\inf_{i\ge1}e^ii^{-k}\}`
  OLD: `$b_j=\sum_{i\le j}c_i\,\theta(\xi-iRe_1)$`
  NEW: `$b_j=\sum_{1\le i\le j}c_i\,\theta(\xi-iRe_1)$`
  OLD: `$\|a-\chi(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}$ by the Leibniz rule`
  NEW: `$\|a-\rho(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}$ with the $\rho$ of (f), by the Leibniz rule`
  OLD: `to finite products with constant spectra, and to subspaces`
  NEW: `to finite products of spectra each satisfying it, and to subspaces`
  OLD: `by Prop.~7.26 every element of $K^m(M,L)$ is a finite sum of Dirac layers $\partial_x^k\delta_L\otimes v_k$ with $k\le\bar m$, whose local symbols are polynomials in $\xi$ of degree $\le\bar m$, and on polynomial symbols`
  NEW: `by Prop.~7.26 every element of $K(M,L)$ is a finite sum of Dirac layers $\partial_x^k\delta_L\otimes v_k$, whose local symbols are polynomials in $\xi$ with the $v_k$ as coefficients, so it lies in $K^m(M,L)$ iff $v_k=0$ for $k>\bar m$; on polynomial symbols`
  OLD: `As of September 3, 2026 the author found no erratum: arXiv lists versions v1 to v3 only; the Crossref record of the DOI carries no correction; zbMATH 7901419 carries no review or corrigendum; Semantic Scholar lists no citing work; Unpaywall lists no correction DOI.`
  NEW: `As of September 6, 2026 the author found no erratum: arXiv lists versions v1 to v3 only, the Crossref record of the DOI carries no correction, zbMATH 7901419 carries no review or corrigendum, and Semantic Scholar lists no citing work (all four re-checked on that date); Unpaywall listed no correction DOI on September 3, 2026.`
  OLD: `\maketitle
\vspace{-2.5em}`
  NEW: `\maketitle
\vspace{-2em}`

**Further edits (not in the merged list).**
- Note date advanced to the revision date, so that it is not earlier than the section-5 date.
  OLD: `\date{\vspace{-1ex}\normalsize September 5, 2026}`
  NEW: `\date{\vspace{-1ex}\normalsize September 6, 2026}`
- Layout only, to keep 3 pages with no content cut: margins and bibliography size.
  OLD: `\usepackage[hmargin=0.75in,vmargin=0.65in]{geometry}`
  NEW: `\usepackage[hmargin=0.6in,vmargin=0.5in]{geometry}`
  OLD: `\vspace{-0.5em}
\begin{thebibliography}{9}\setlength{\itemsep}{0pt}\small`
  NEW: `\vspace{-1em}
\begin{thebibliography}{9}\setlength{\itemsep}{0pt}\footnotesize`

## Final consistency read
- Partition-of-unity index: f_i in (d) and section 4; lambda_i, mu in section 4; no f_j / lambda_j left (grep).
- Cut-offs: theta (a)-(c); psi, psi_*, rho (d); chi (e); chi_j, rho, rho_R (f); rho of (f) reused in section 4 for Cor. 3.5; no undefined chi in section 4 (grep).
- Bold M and bold x: introduced in (e) with (7.27), reused in section 4 with (7.26); calligraphic K for K(M) as in the paper.
- p_0 no longer occurs. m' in (e) is free (m' in R), used at m' = m and m' < m.
- Dates: title September 6, 2026; section 5 'As of September 6, 2026' with the four re-run checks, Unpaywall dated September 3, 2026.
- Build: 3 pages, 0 overfull, 0 underfull, no LaTeX warnings; renders of all three pages read.

## For the program record (not the note)
- `novelty/adjudication.md` section 2 C6 / A2-02 and `w3-adjudication.md` R2 say the sections 6-7 renumbering entered at v3 and that sections 3-4 are unchanged across versions; the evidence above says v2 (29 Jul 2023) already carries the published numbering (v2 = v3 in sections 3-4 word for word, and the sections 6-8 items above), and sections 3-4 were lightly edited between v1 and v2. Suggest a dated correction there.
- Files: `fetched-r3/r3s-37-...2304.00798v2-SESSION16-FETCH.pdf`, `r3s-38-...2304.00798v3-...pdf`, `r3s-39-...2402.06671v2-...pdf` (local-only directory). Scratch: text layers, diffs (`sec34.py`, `wd.py`), renders and trial builds in the session scratchpad.
