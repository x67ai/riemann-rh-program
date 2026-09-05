# SECOND-MODEL READ of `alkl23-note.tex` / `alkl23-note.pdf` (courtesy note to Álvarez López–Kordyukov–Leichtnam)

**Reader:** Opus 5, independent of the writer. **Date:** 2026-09-05 (Session 16, direction C3-r).
**Files read this session, in full:**
`results/c3-r/s14/alkl23-note.tex` (81 lines) and the text layer of `results/c3-r/s14/alkl23-note.pdf` (3 pp.);
the PUBLISHED paper `results/c3-r/s14/novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`
(68 pp.; my own `pdftotext -layout` extraction plus 300/600-dpi page renders of pp. 16, 17, 22, 42, 48, 49, 56 to read
accents and primes that the text layer drops);
the arXiv v1 PDF `fetched-r3/r3s-18-…-2304.00798v1-SESSION8-FETCH.pdf` (numbering cross-check);
the memoir `fetched-r3/r3s-17-…-2402.06671v1-SESSION8-FETCH.pdf` (§2.1.8 p. 15; §5.2.1 p. 119; §§5.5.3–5.5.4 p. 122);
`results/c3-r/s14/w3-adjudication.md` §0, §1, §2, §3 head, §4 (all), §5, §7 and the dated v1→v3 blocks;
`results/c3-r/s14/novelty/adjudication.md` §2 C6 and §3 R2.
**Not available in this sandbox:** a LaTeX engine, so I could not rebuild the PDF. The PDF on disk is 3 pages and its
text layer contains every late edit present in the `.tex` (checked on five distinctive strings), so `.tex` and `.pdf`
are in sync.

---

## 0. VERDICT

**PASS-WITH-REPAIRS.**

The mathematics is correct. I re-derived all six witnesses (a)–(f), the interpolation inequality (1), the assembly,
the Claim 6.46 / Prop. 8.8 / Cor. 3.5 repairs and the Cor. 6.27 / Cor. 7.22 truth argument from scratch, in my own
notation, and every one of them does what the note says it does and refutes exactly the statement it is aimed at.
Every theorem number, page number and quoted sentence in the note was opened in the PUBLISHED PDF and matches, to
the character where the note uses quotation marks. **No v1 number slipped in**: the note is in published (= arXiv v3)
numbering throughout, and I confirmed against the v1 PDF on disk that §§3–4 are unchanged and that §§6–7 are exactly
where they renumber. The "what survives" paragraph claims nothing the adjudication did not prove, and in one place
(the completeness clause of Cor. 3.6) it claims strictly *less* than the adjudication, which is the right choice.
No program jargon, no invented citation, no em-dash, U.S. English, 3 pages, courteous throughout.

The repairs in §3 are: **two required** (a real index collision in witness (d) that makes one sentence unreadable as
written; one place where the note's `A^m(M)` conflates the closed `M` with the paper's cut manifold, which the paper
prints in a different glyph), **four recommended** (precision and the AI-use footnote), **three optional**.

**One deviation from the orchestrator's brief is upheld.** The brief states that `S^m_K → S^{m'}_K` are compact
operators, so the p. 5 compact-spectrum remark applies. That is **wrong**, the writer is right to say so, and the
note's parenthetical is correct: I re-derived the counterexample (§2.7 below). The brief's sentence traces to
`w3-adjudication.md` §0 C6(ii) ("§4.8(iii) above proves the compactness of `S^m_K → S^{m′}_K`"), which mis-summarizes
its own §4.8 — §4.8(iii) proves only that *bounded sets* have relatively compact image, and §4.8(ii) says in terms
that the compact-spectrum shortcut "is unavailable already for one point". The note agrees with §4.8, not with §0.
This should be corrected in the program record (§4 below); it does not touch the note.

**One statement I could not re-verify from disk** (recorded for honesty, no repair asked): the note's §1 clause
"arXiv:2304.00798v3 has the same numbering [as the published text]". Only v1 and the published PDF are on disk. The
claim rests on the program's own dual-checked record (`novelty/adjudication.md` §2 C6, §3 R2, checked 2026-09-03).
Everything else in the note I verified myself.

---

## 1. Statement-by-statement table (published numbering; page = the page of the PUBLISHED PDF)

Legend: **✓** = the note's number, page and wording all match the published text, and the claim about it is one I
re-derived and confirmed.

| # | The note says | Published text, checked | Page | Verdict |
|---|---|---|---|---|
| 1 | Prop. 3.2 false | "Proposition 3.2 The semi-norms (3.4) and (3.5) together describe the topology of $S^m(U\times\mathbb R^l)$." | **16** | ✓ |
| 2 | The proof's identity "$\|\varphi(a)\|'_{K,\alpha,\beta,m}=\|a\|'_{K,\alpha,\beta,m}<\infty$" at the top of p. 17 | quoted verbatim; it is the 3rd body line of p. 17 (read at 200 dpi; the primes are real, the text layer renders them `\x02`) | **17** | ✓ |
| 3 | "Hence $S'^m(U\times\mathbb R^l)$ is complete" | verbatim, and the symbol is the **unaccented** $S'^m$ (the completion, three lines above on p. 16, is $\widehat{S'^m}$ — read at 200 dpi). The note quotes the right one. | **17** | ✓ |
| 4 | Cor. 3.4, both assertions, false | "Corollary 3.4 For $m<m'$, the topologies of $S^{m'}$ and $C^\infty$ coincide on $S^m$. Therefore the topologies of $S^\infty$ and $C^\infty$ coincide on $S^m$." | **17** | ✓ |
| 5 | Cor. 3.6 acyclicity + bounded retractivity false for non-compact $U$ | "Corollary 3.6 $S^\infty(U\times\mathbb R^l)$ is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive." Proof: "Corollary 3.4 gives the property of being acyclic…" | **18** | ✓ (note does **not** claim the completeness clause false — correct restraint) |
| 6 | the p. 18 sentence extending §3 to bundles | "We can similarly define the norms (3.4) and (3.5) on $S^m(E)$, and Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting." | **18** | ✓ number/page/wording; see **repair R4** (Prop. 3.3 and Cor. 3.5 do extend, and the note's phrasing sweeps them in) |
| 7 | Cor. 4.5 false for every compact $(M,L)$, $\operatorname{codim}L\ge1$ | "Corollary 4.5 For $m<m',m''$, the topologies of $I^{m'}(M,L)$ and $I^{m''}(M,L)$ coincide on $I^m(M,L)$. Proof Use Corollary 3.4 and the TVS-embeddings (4.10)." | **23** | ✓ |
| 8 | Prop. 6.12 false | "Proposition 6.12 The semi-norms (6.42) and (6.43) together describe the topology of $A^m(M)$." | **39** | ✓ |
| 9 | Cor. 6.14, both assertions, false | "Corollary 6.14 If $m'<m$, then the topologies of $A^{m'}(M)$ and $C^\infty(\mathring M)$ coincide on $A^m(M)$. Therefore the topologies of $A(M)$ and $C^\infty(\mathring M)$ coincide on $A^m(M)$." | **39** | ✓ |
| 10 | Cor. 6.21 false | "Corollary 6.21 For $m<m',m''$, the topologies of $\dot A^{m'}(M)$ and $\dot A^{m''}(M)$ coincide on $\dot A^m(M)$", preceded by "The following is a consequence of Corollary 4.5 applied to $(\breve M,\partial M)$." | **40** | ✓ |
| 11 | Cor. 7.13, both assertions, false | "Corollary 7.13 If $m'<m$, then the topologies of $J^{m'}(M,L)$ and $C^\infty(M\setminus L)$ coincide on $J^m(M,L)$. Therefore …" | **56** | ✓ |
| 12 | Cor. 6.27 true, printed proof passes through Cor. 6.21 | "Corollary 6.27 For $m<m',m''$, the topologies of $\mathcal K^{m'}(M)$ and $\mathcal K^{m''}(M)$ coincide on $\mathcal K^m(M)$", preceded by "the following analogs of Corollaries 6.21 and 6.22 hold true with formally the same proofs, using Corollaries 6.21, 6.22 and 6.26." | **41** | ✓ |
| 13 | Cor. 7.22 true, same route | "Corollary 7.22 For $m<m',m''$, the topologies of $K^{m'}(M,L)$ and $K^{m''}(M,L)$ coincide on $K^m(M,L)$", preceded by "consequences of Propositions 6.24 and 6.25 and Corollaries 6.26 to 6.28." | **58** | ✓ (so it routes through Cor. 6.27, hence 6.21, hence 4.5 — the note's chain is right) |
| 14 | Claim 6.46, and its sentence "By Corollary 6.14, there is some 0-neighborhood $V\subset A(M)$ such that $V\cap A^m(M)=W\cap A^m(M)$" | Claim 6.46 is stated on p. 48; the quoted sentence straddles pp. 48–49 and the exponent is the **unprimed** $m$ (read at 200 dpi). The note's quote is exact and its "pp. 48–49" is right. | **48–49** | ✓ |
| 15 | "$E_{m'}$ from Prop. 6.29 (whose domain is $A^{m'}(M)\supset A^m(M)$, so $m'<m$ rather than $m'>m$)" | Prop. 6.29 (p. 42): "For all $m\in\mathbb R$, there is a continuous linear partial extension map $E_m:A^m(M)\to\dot A^{(s)}(M)$…". Claim 6.46's proof (p. 48) prints "For any $m'>m$, let $E_{m'}:A^m(M)\to\dot A^{(s)}(M)$…" and then "$W\subset A^{m'}(M)$". With (6.38) ($A^m\subset A^{m'}$ for $m'<m$) the note's correction is exactly right. | **42, 48** | ✓ |
| 16 | Prop. 8.8 repaired identically with Cor. 7.31; Cor. 7.13 not needed | Prop. 8.8 (p. 64), preceded by "The following analog of Proposition 6.45 holds true with formally the same proof, using Proposition 7.29 and Corollaries 7.13, 7.15 and 7.31." Cor. 7.31 (p. 60) is the $J$-side partial extension map. | **60, 64** | ✓ |
| 17 | Cor. 3.5 | "Corollary 3.5 For $m<m'$, $C_c^\infty(U\times\mathbb R^l)$ is dense in $S^m$ with the topology of $S^{m'}$…" | **17** | ✓ |
| 18 | acyclicity clauses of Cors. 4.7, 6.16, 6.22, 6.28, 7.15, 7.23 | all six read; each says "… is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive" | **23, 39, 40, 41, 57, 58** | ✓ (this is the adjudication's list, correctly translated from v1 6.14/6.20/6.25/7.13/7.21) |
| 19 | Wengenroth's criterion "quoted on p. 4" | p. 4: "the condition of being acyclic can be described as follows [39, Theorem 6.1]: for all $k$, there is some $k'\ge k$ such that, for all $k''\ge k'$, the topologies of $X_{k'}$ and $X_{k''}$ coincide on some 0-neighborhood of $X_k$." | **4** | ✓ |
| 20 | "[Wen03, Cor. 6.5] as quoted on p. 5" | p. 5: "acyclic LF-spaces are complete and regular [39, Corollary 6.5]"; also "X is acyclic if and only if it is boundedly/compactly/sequentially retractive [39, Proposition 6.4]" | **5** | ✓ |
| 21 | "the remark on p. 5 about compact spectra" | p. 5: "It is said that $(X_k)$ is compact if the inclusion maps are compact operators. In this case, $(X_k)$ is clearly acyclic… Moreover $X$ is a complete bornological DF Montel space [18, Theorem 6′]." | **5** | ✓ (the brief said p. 4; the note's p. 5 is right) |
| 22 | reference [3] "Wengenroth, LNM 1810, Springer, Berlin (2003)" | paper's ref. [39]: "Wengenroth, J.: Derived Functors in Functional Analysis. Lecture Notes in Mathematics, vol. 1810. Springer, Berlin (2003)" | **68** | ✓ identical |
| 23 | equations (3.1), (3.4), (3.5), (4.8), (4.9), (4.10), (6.33), (6.41), (6.42), (6.43), (6.47), (6.49), (7.26), (7.27) | each opened; all as the note uses them. (4.9) is $\bar m=m+n/4-n'/2$ (read at 300 dpi); the note only uses that $\bar m$ increases with $m$, which is safe. | 15, 16, 21, 22, 36, 38, 39, 40, 41, 56 | ✓ |
| 24 | "Sect. 4.3.3, p. 23, excepts acyclicity for non-compact $M$" | p. 23: "Corollary 4.7 has extensions for $\bigcup_mI^m(M,L)$ and $I_{\cdot/c}(M,L)$, except acyclicity in the case of $I(M,L)$." | **23** | ✓ and a fair, courteous observation |
| 25 | memoir §2.1.8, p. 15, restates Cors. 3.4–3.6 for arbitrary open $U$ | memoir printed p. 15 (PDF p. 21): "The following properties hold [ÁLKL23, Corollaries 3.4–3.6 and Remark 3.8]: The topologies of $S^\infty(U\times\mathbb R^l)$ and $C^\infty(U\times\mathbb R^l)$ coincide on $S^m$ … and $S^\infty(U\times\mathbb R^l)$ is an acyclic Montel space, and therefore complete, boundedly/compactly/sequentially retractive and reflexive", with "$U\subset\mathbb R^n$ open" | **15 (memoir)** | ✓ |
| 26 | memoir consumers §5.2.1 p. 119, §§5.5.3–5.5.4 p. 122, and $I(\mathcal F)=I(M,M^0;\Lambda\mathcal F)$ | §5.2.1 sits on printed p. 119 ("because $I(\mathcal F)$ is compactly retractive (Section 2.2.2)"); §5.5.3 and §5.5.4 sit on printed p. 122 ("Using that $J(\mathcal F)$ is compactly retractive"; "Since $I(\mathcal F)$ is compactly retractive"); the definition $I(\mathcal F)=I_{\Lambda^\bullet}(\mathcal F):=I(M,M^0;\Lambda\mathcal F)$ is printed. §2.2.2 is headed "Conormal distributions when $M$ is compact". | **119, 122 (memoir)** | ✓ |
| 27 | v1/v3 numbering | v1 on disk: Props. 3.1–3.3, Cors. 3.4–3.6, Cor. 4.5 have the **same** numbers as the published text; v1's 6.10 / 6.12 / 6.19 / 6.24 / 7.11 / 7.20 / Claim 6.43 / Prop. 6.26 are the published 6.12 / 6.14 / 6.21 / 6.27 / 7.13 / 7.22 / Claim 6.46 / Prop. 6.29. The note uses **only** published numbers. | — | ✓ no leakage |

**Nothing in the note is single-check.** The one item that carried a `[novelty: single-check]` flag in
`w3-adjudication.md` — §5.1, "Cor. 6.27 and Cor. 7.22 are TRUE" — is re-derived by me from scratch in §2.8 below,
independently of the adjudicator and of the writer, so the flag is cleared for the sentence as it appears in the note.
The other single-check items of §5 (5.2 Fréchet-ness of $I^m$, 5.3 the $C(T)$ transfer, 5.4 the $A$-topology
gap-closure) do **not** appear in the note.

**"What survives" versus the adjudication (§4, §7.1(3)).** The note's §4 claims:
acyclicity of $I(M,L)$, $A(M)$, $\dot A(M)$, $\mathcal K(M)$, $J(M,L)$, $K(M,L)$ for compact $M$; the retractivities,
completeness and regularity that Wengenroth's quoted statements deliver from it; the repair of Claim 6.46 and of
Prop. 8.8 from bounded retractivity plus the partial extension maps; the direct proof of Cor. 3.5; the truth of
Cors. 6.27 and 7.22; and coverage of the memoir's pp. 119/122 consumers. That is exactly the adjudication's §7.1(3)
list, minus the two internal items (Fréchet-ness of $I^m$; the $C(T;\cdot)$ transfer). **The note claims nothing
more.** Two places where it claims *less* than the adjudication, both correctly: (i) it does not assert the
completeness clause of Cor. 3.6 is false (the adjudication does; only regularity is actually refuted by (f));
(ii) it does not assert the non-existence of the neighborhood $V$ of Claim 6.46's printed proof, it merely supplies
a working substitute.

---

## 2. My own re-derivations

Throughout, $U\subset\mathbb R^n$ open, $l\ge1$, and I write $\langle\xi\rangle:=1+|\xi|$. I use the paper's (3.1)
$\|a\|_{K,\alpha,\beta,m}=\sup_{x\in K,\xi}|\partial_x^\alpha\partial_\xi^\beta a|\langle\xi\rangle^{|\beta|-m}$,
(3.4) $\|a\|_{Q,C^k}$, (3.5) $\|a\|'_{K,\alpha,\beta,m}=\sup_{x\in K}\limsup_{|\xi|\to\infty}|\partial^\alpha_x\partial^\beta_\xi a|\,|\xi|^{|\beta|-m}$.
I fix $\theta\in C_c^\infty(\mathbb R^l)$, $\theta(0)=1$, $\operatorname{supp}\theta\subset B(0,r)$. I re-derived each
item without consulting the writer's companion file.

### 2.1 Witness (a) — Prop. 3.2 and the first assertion of Cor. 3.4

Put $g_N(x,\xi)=\theta(\xi-Ne_1)$.

*In every $S^m$.* $g_N$ is $x$-independent and compactly supported in $\xi$, so $\partial_x^\alpha g_N=0$ for
$\alpha\ne0$ and $\sup_\xi|\partial^\beta\theta(\xi-Ne_1)|\langle\xi\rangle^{|\beta|-m}<\infty$ for every $m$:
$g_N\in S^{-\infty}\subset S^m$ for all $m$.

*Null in the (3.4)+(3.5) topology.* For compact $Q\subset K\times\bar B(0,\rho)$ and $N>\rho+r$, $\operatorname{supp}g_N$
misses $Q$, so $\|g_N\|_{Q,C^k}=0$; and each (3.5) seminorm vanishes because the $\xi$-support is compact
(the $\limsup_{|\xi|\to\infty}$ is over a region where $g_N\equiv0$). Also $g_N\to0$ in $C^\infty(U\times\mathbb R^l)$,
since $g_N$ vanishes identically on any fixed compact set once $N$ is large.

*Unbounded in $S^m$.* Substituting $\eta=\xi-Ne_1$ and using $\operatorname{supp}\partial^\beta\theta\subset B(0,r)$,
$$\|g_N\|_{K,0,\beta,m}=\sup_{|\eta|\le r}|\partial^\beta\theta(\eta)|\,(1+|\eta+Ne_1|)^{|\beta|-m},$$
an equality (outside $|\eta|\le r$ the integrand is $0$). If $|\beta|>m$ the exponent is positive and
$1+|\eta+Ne_1|\ge1+N-r$, so $\|g_N\|_{K,0,\beta,m}\ge(1+N-r)^{|\beta|-m}\sup|\partial^\beta\theta|\to\infty$.
Such $\beta$ exist in every order: if $\partial^\beta\theta\equiv0$ for all $|\beta|=k$ then $\theta$ is a polynomial
of degree $<k$, impossible for a nonzero compactly supported function.

**Conclusion.** $(g_N)$ is null for (3.4)+(3.5) and unbounded in $S^m$, for every $m\in\mathbb R$, every $U$, every
$l\ge1$: **Prop. 3.2 is false**. Taking $|\beta|>m'$ instead: $g_N\in S^m$, $g_N\to0$ in $C^\infty$,
$g_N\not\to0$ in $S^{m'}$: **the first assertion of Cor. 3.4 is false**. Agrees with the note.

### 2.2 Witness (b) — where the printed proof of Prop. 3.2 breaks

Let $S'^m$ be $S^m$ with the (3.4)+(3.5) topology. Fix $R>2r$ (so the balls $B(iRe_1,r)$ are pairwise disjoint),
$c_i=(1+iR)^{m+1}$, $b_j=\sum_{i\le j}c_i\theta(\xi-iRe_1)$.

*Cauchy in $S'^m$.* For $i<j$, $b_j-b_i$ is supported in $\{|\xi|\ge(i+1)R-r\}$ and compactly in $\xi$; its (3.5)
seminorms vanish, and for a fixed compact $Q\subset K\times\bar B(0,\rho)$ its $\|\cdot\|_{Q,C^k}$ vanishes as soon as
$(i+1)R-r>\rho$.

*No limit.* The (3.4) seminorms are exactly the $C^\infty(U\times\mathbb R^l)$ seminorms, so $S'^m\hookrightarrow C^\infty$
continuously and any $S'^m$-limit would be the $C^\infty$-limit. That limit is $b=\sum_ic_i\theta(\xi-iRe_1)$
(the sum is locally finite), and $|b(x,iRe_1)|\langle iRe_1\rangle^{-m}=(1+iR)^{m+1}/(1+iR)^m=1+iR\to\infty$, so
$b\notin S^m$. Hence **$S'^m$ is not complete**, contradicting the printed "Hence $S'^m(U\times\mathbb R^l)$ is complete"
(p. 17).

*The failing identity.* Let $a$ be the class of $(b_j)$ in $\widehat{S'^m}$. Each (3.5) seminorm is continuous on
$S'^m$, so its continuous extension satisfies $\|a\|'_{K,0,0,m}=\lim_j\|b_j\|'_{K,0,0,m}=0$. But $\varphi(a)=b$
(both are the $C^\infty$-limit) and $\|b\|'_{K,0,0,m}=\limsup_{|\xi|\to\infty}|b|\,|\xi|^{-m}=\infty$ along
$\xi=iRe_1$. So $\|\varphi(a)\|'\ne\|a\|'$: the printed identity at the top of p. 17 fails on this $a$. Agrees with
the note, including its localization of the break.

### 2.3 Witness (c) — the second assertion of Cor. 3.4

$c_j=e^j\theta(\xi-je_1)\in S^{-\infty}\subset S^m$ for every $m$, and $c_j\to0$ in $C^\infty$ (each compact set is
missed for large $j$).

Fix $x_0\in U$, $K=\{x_0\}$. For $k\in\mathbb N$ set $\varepsilon_k=\frac12\inf_{j\ge1}e^j(1+j)^{-k}$, which is
$>0$ because $e^j(1+j)^{-k}\to\infty$ and is positive for each $j$. Put $W_k=\{a\in S^k:\|a\|_{K,0,0,k}<\varepsilon_k\}$,
a $0$-neighborhood of the step $S^k$, and let $W$ be the absolutely convex hull of $\bigcup_kW_k$. Then $W\cap S^k\supset W_k$
for every $k$, and an absolutely convex set meeting every step in a $0$-neighborhood is a $0$-neighborhood of the
locally convex inductive limit $S^\infty=\operatorname{ind}_kS^k$.

Suppose $c_j=\sum_i\lambda_iw_i$ (finite), $\sum_i|\lambda_i|\le1$, $w_i\in W_{k_i}$. Evaluating at $(x_0,je_1)$:
$|w_i(x_0,je_1)|\le\|w_i\|_{K,0,0,k_i}(1+j)^{k_i}<\varepsilon_{k_i}(1+j)^{k_i}\le\frac12e^j$ by the definition of
$\varepsilon_{k_i}$. Hence $e^j=|c_j(x_0,je_1)|\le\sum_i|\lambda_i|\,|w_i(x_0,je_1)|<\frac12e^j$, absurd. So
$c_j\notin W$ for every $j$ and $c_j\not\to0$ in $S^\infty$, while $c_j\to0$ in $C^\infty$ and $c_j\in S^m$ for every
$m$: **the second assertion of Cor. 3.4 is false, for every $U$ and every $m$**. No property of $S^\infty$ (in
particular no regularity, which would be circular) is used. Agrees with the note.

### 2.4 Witness (d) — Cor. 4.5, and Cor. 6.21

$M$ compact, $L$ closed regular of codimension $n'\ge1$ and dimension $n''$, $m<m'<m''$, $\bar m=m+n/4-n'/2$ (4.9)
so $\bar m<\bar m'<\bar m''$. Adapted chart $(U_1,x=(x',x''))$ at $p_0\in L$, $x(p_0)=0$.

*Normalizing the partition of unity.* Given $\{h,f_i\}$ subordinate to $\{M\setminus L,U_i\}$ and
$\rho\in C_c^\infty(U_1)$ with $\rho=1$ near $p_0$, the family $\{(1-\rho)h,\ \rho+(1-\rho)f_1,\ (1-\rho)f_i\ (i\ge2)\}$
sums to $(1-\rho)\cdot1+\rho=1$, is subordinate to the same cover, and near $p_0$ equals $\{0,1,0,\dots\}$. (And in any
case the two Fréchet topologies induced on $I^m(M,L)$ by two admissible choices are comparable by the closed graph
theorem, both being continuously included in $C^{-\infty}(M)$; so the choice is immaterial.) Both checks confirm the
note's parenthetical.

*The family.* Let $g\in C_c^\infty(U'')$, $g\not\equiv0$; $\psi\in C_c^\infty(\{|x'|<1\})$, $\psi\not\equiv0$;
$N_0\in\mathbb N_0$ with $2N_0\ge\bar m''$; $\psi_*=\Delta^{N_0}\psi$. With
$\hat f(\eta)=\int e^{-i\langle z,\eta\rangle}f(z)\,dz$ one has $\widehat{\partial_k\psi}=i\eta_k\hat\psi$, so
$\hat\psi_*(\eta)=(-|\eta|^2)^{N_0}\hat\psi(\eta)$: Schwartz, $\not\equiv0$, and $\partial^\beta\hat\psi_*$ vanishes
to order $2N_0-|\beta|$ at $0$. Put $u_j(x',x'')=j^{\,n'+\bar m'}g(x'')\psi_*(jx')\in C_c^\infty(U_1)\subset C^\infty(M)$,
supported in $\{|x'|<1/j\}\times\operatorname{supp}g$.

*Its symbol.* By (4.8), substituting $x'=z/j$,
$$a_j(x'',\xi)=\int e^{-i\langle x',\xi\rangle}u_j\,dx'=j^{\,n'+\bar m'}g(x'')\,j^{-n'}\!\int e^{-i\langle z,\xi/j\rangle}\psi_*(z)\,dz=j^{\bar m'}g(x'')\hat\psi_*(\xi/j).$$

*Its seminorms.* $\partial_{x''}^\alpha\partial_\xi^\beta a_j=j^{\bar m'-|\beta|}\partial^\alpha g\,(\partial^\beta\hat\psi_*)(\xi/j)$;
with $\xi=j\eta$ and $1+|\xi|=j(1/j+|\eta|)$,
$$\|a_j\|_{K,\alpha,\beta,\bar m_1}=j^{\,\bar m'-\bar m_1}\sup_K|\partial^\alpha g|\cdot\Phi_{\beta,\bar m_1}(j),\qquad
\Phi_{\beta,\bar m_1}(j)=\sup_\eta|\partial^\beta\hat\psi_*(\eta)|\,(1/j+|\eta|)^{|\beta|-\bar m_1}.$$
This reproduces the note's display exactly. For $\bar m_1\le2N_0$ and $j\ge1$, $\Phi_{\beta,\bar m_1}(j)\le C_\beta$:
if $|\beta|\ge\bar m_1$ use $(1/j+|\eta|)^{|\beta|-\bar m_1}\le(1+|\eta|)^{|\beta|-\bar m_1}$ and Schwartz decay; if
$|\beta|<\bar m_1$ then $(1/j+|\eta|)^{|\beta|-\bar m_1}\le|\eta|^{|\beta|-\bar m_1}$ and, since
$|\partial^\beta\hat\psi_*(\eta)|\le C|\eta|^{2N_0-|\beta|}$ near $0$ with $2N_0-|\beta|\ge\bar m_1-|\beta|$, the
product is bounded near $0$ and trivially bounded for $|\eta|\ge1$. Conversely, picking $\eta_0$ with
$\hat\psi_*(\eta_0)\ne0$ (necessarily $\eta_0\ne0$),
$\Phi_{0,\bar m'}(j)\ge|\hat\psi_*(\eta_0)|\min\{(1+|\eta_0|)^{-\bar m'},|\eta_0|^{-\bar m'}\}=:c>0$ for all $j\ge1$
(the first entry serves when $\bar m'\ge0$, the second when $\bar m'<0$).

**Conclusion.** $\|a_j\|_{K,\alpha,\beta,\bar m''}\le Cj^{\bar m'-\bar m''}\to0$, so $u_j\to0$ in $I^{m''}(M,L)$;
while for a compact $K$ meeting $\{g\ne0\}$, $\|a_j\|_{K,0,0,\bar m'}\ge c\sup_K|g|>0$, so $u_j\not\to0$ in
$I^{m'}(M,L)$. Since $u_j\in C^\infty(M)\subset I^{-\infty}(M,L)\subset I^m(M,L)$, **Cor. 4.5 is false**, for every
compact $(M,L)$ with $\operatorname{codim}L\ge1$ (for $n''=0$ take $g$ a nonzero constant). Agrees with the note.
See **repair R3**: the note writes $\sup|g|$ where $\sup_K|g|$ with $K$ meeting $\{g\ne0\}$ is meant.

*Cor. 6.21.* Take the collar chart of $(\breve M,\partial M)$ ($n'=1$, $\psi_*=\psi^{(2N_0)}$) and
$\operatorname{supp}\psi\subset(\frac12,1)$, so $\operatorname{supp}u_j\subset\{\frac1{2j}<x<\frac1j\}\subset\mathring M$
and $u_j\in C_c^\infty(\mathring M)\subset\dot A^{m}(M)=I^m_M(\breve M,\partial M)$ by (6.47). The symbol computation
is unchanged, and $\dot A^{m_1}(M)$ carries the topology induced from $I^{m_1}(\breve M,\partial M)$, so $u_j\to0$ in
$\dot A^{m''}(M)$ and $u_j\not\to0$ in $\dot A^{m'}(M)$: **Cor. 6.21 is false**. Agrees with the note.

### 2.5 Witness (e) — Prop. 6.12, Cor. 6.14, Cor. 7.13

$M$ compact with boundary, $(x,y)$ a collar chart, $\chi\in C_c^\infty((\frac12,2))$ with $\chi(1)=1$,
$g$ a bump in $y$ with $g(y_0)=1$. First recall the direction of the filtration: (6.37)–(6.38) give
$A^m(M)\subset A^{m'}(M)$ for $m'<m$, so the steps grow as $m$ decreases, and Cor. 6.14 reads "for $m'<m$ the
topologies of $A^{m'}(M)$ and $C^\infty(\mathring M)$ coincide on $A^m(M)$".

Put $u_j=j^{-m'}\chi(jx)g(y)$, supported in $\{\frac1{2j}<x<\frac2j\}$, hence in $C_c^\infty(\mathring M)$ for large
$j$, hence in $A^{m_1}(M)$ for every $m_1$ (on its support $x$ is bounded below, so $x^{-m_1}|Pu_j|$ is bounded for
every $P\in\operatorname{Diff}_b$).

* (6.42) $\|u\|_{K,k,m}=\sup_K|P_ku|$ over compact $K\subset\mathring M$: since $x\ge x_K>0$ on $K$, this vanishes for
  large $j$.
* (6.43) $\|u\|'_{k,m}=\lim_{\varepsilon\downarrow0}\sup_{\{0<x<\varepsilon\}}x^{-m}|P_ku|$: identically $0$, since
  $u_j=0$ on $\{x<\frac1{2j}\}$.
* (6.41) with $P=1$: $\sup_{\mathring M}x^{-m'}|u_j|\ge(1/j)^{-m'}\cdot j^{-m'}\chi(1)g(y_0)=1$.
* $u_j\to0$ in $C^\infty(\mathring M)$ (supports leave every compact set).

With $m'=m$ this gives a sequence null for (6.42)+(6.43) and not null in $A^m(M)$: **Prop. 6.12 is false**. With
$m'<m$ it gives $u_j\in A^m(M)$, $u_j\to0$ in $C^\infty(\mathring M)$, $u_j\not\to0$ in $A^{m'}(M)$: **the first
assertion of Cor. 6.14 is false**.

For the second assertion put $v_j=e^j\chi(jx)g(y)$ and repeat §2.3 with steps $A^{-k}(M)$ and
$W_k=\{u\in A^{-k}(M):\sup_{\mathring M}x^{k}|u|<\frac12\inf_{i\ge1}e^ii^{-k}\}$; evaluating at $(1/j,y_0)$, where
$x^{k}|v_j|=j^{-k}e^j$, gives $|w_i(1/j,y_0)|<\frac12e^j$ for $w_i\in W_{k_i}$ and hence $v_j\notin W$, while
$v_j\to0$ in $C^\infty(\mathring M)$ and $v_j\in A^{m}(M)$ for all $m$: **the second assertion of Cor. 6.14 is false**.

For Cor. 7.13, (7.27) defines $J^m(M,L)$ by $\operatorname{Diff}(M,L)u\subset x^mL^\infty$ with the analogous
topology, and $C_c^\infty(M\setminus L)\subset J^{m_1}(M,L)$ for every $m_1$. Placing the same $u_j$ and $v_j$ in
$\{\frac12<jx<2\}\subset M\setminus L$ and running the same three computations refutes **both assertions of
Cor. 7.13**. Agrees with the note.

### 2.6 Witness (f) — Cor. 3.6 for non-compact $U$

$U\subset\mathbb R^n$ open nonempty, $n\ge1$ (so $U$ is non-compact; conversely a nonempty open $U\subset\mathbb R^n$
is compact only when $n=0$, which is the case $S^\infty(\mathbb R^l)$ the note excepts). Choose $x_j\in U$ leaving
every compact subset of $U$, pairwise disjoint closed balls $\bar B(x_j,r_j)\subset U$ forming a locally finite family,
$\chi_j\in C_c^\infty(B(x_j,r_j))$ with $\chi_j(x_j)=1$, and $b_j(x,\xi)=\chi_j(x)(1+|\xi|^2)^{j/2}$. Then
$b_j\in S^j$, and $b_j\notin S^m$ for $m<j$ because $|b_j(x_j,\xi)|\langle\xi\rangle^{-m}\to\infty$.

*Boundedness in $S^\infty$.* Let $W$ be an absolutely convex $0$-neighborhood of $S^\infty$; choose in each
$W\cap S^k$ a basic $W_k=\{a\in S^k:\|a\|_{K_k,\alpha,\beta,k}<\varepsilon_k,\ (\alpha,\beta)\in F_k\}$, $F_k$ finite.
By local finiteness, $\operatorname{supp}\chi_j\cap K_1=\emptyset$ for all but finitely many $j$. For such $j$, take
$\rho\in C_c^\infty(B(0,2))$ with $\rho=1$ on $B(0,1)$ and $\rho_R(\xi)=\rho(\xi/R)$, and split
$b_j=b_j\rho_R+b_j(1-\rho_R)$.

* $b_j\rho_R\in S^{-\infty}\subset S^1$ has compact $\xi$-support and vanishes on $K_1\times\mathbb R^l$, so all its
  $\|\cdot\|_{K_1,\alpha,\beta,1}$ vanish: $2b_j\rho_R\in W_1$.
* $b_j(1-\rho_R)\in S^{j+1}$ vanishes for $|\xi|\le R$. By Leibniz, the $\beta'=0$ term of
  $\partial^\alpha\partial^\beta[b_j(1-\rho_R)]$ contributes $\le C_{j,\alpha,\beta}\langle\xi\rangle^{j-|\beta|}$ on
  $\{|\xi|\ge R\}$, i.e. $\le C\langle\xi\rangle^{-1}\le C/R$ after dividing by $\langle\xi\rangle^{j+1-|\beta|}$; a
  term with $\beta'\ne0$ carries $|\partial^{\beta'}\rho_R|\le CR^{-|\beta'|}$ on $\{R\le|\xi|\le2R\}$ and gives
  $\le CR^{-|\beta'|}(3R)^{|\beta'|-1}\le C/R$. So all $S^{j+1}$-seminorms are $O(1/R)$ and
  $2b_j(1-\rho_R)\in W_{j+1}$ for $R$ large (depending on $j$, which is fixed).
* By absolute convexity, $b_j=\frac12(2b_j\rho_R)+\frac12(2b_j(1-\rho_R))\in W$.

The finitely many remaining $b_j$ are absorbed by $W$ (a $0$-neighborhood is absorbing). So $\{b_j\}$ is bounded in
$S^\infty$ and lies in no single step: **the spectrum is not regular**, hence not boundedly retractive, and by the
quoted "acyclic LF-spaces are complete and regular [39, Cor. 6.5]" (p. 5) **not acyclic**. The printed derivations of
Cor. 3.6's remaining clauses run through acyclicity and bounded retractivity, so they break as well; the note says
exactly this and no more. Agrees with the note. The same construction, in a chart with a base cut-off, applies to the
p. 18 bundle extension over a non-compact base and to the memoir's §2.1.8.

### 2.7 The interpolation inequality (1), and the compact-operator question

*Statement re-derived.* $K\subset U$ compact, $S^m_K$ = symbols vanishing for $x\notin K$ (so they extend by zero to
smooth functions on $\mathbb R^n\times\mathbb R^l$, and $N_m(a;0)$ is a **global** supremum — this is the only place
compact base support is used, and it is exactly what (f) destroys). Fix $\gamma=(\alpha,\beta)$, $|\gamma|=k\ge1$,
$m<m'<m''$. Put $\lambda=(m'-m)/(2k)$ and $N=k+\lceil(m''-m')/\lambda\rceil$.

For $\rho:=1+|\xi_0|>R\ge1$, rescale on the box $\{|x-x_0|\le1,\ |\xi-\xi_0|\le\rho/2\}$ by
$\tilde a(y,\eta)=a(x_0+y,\xi_0+\tfrac\rho2\eta)$, so that $\partial_y^{\alpha}\partial_\eta^{\beta}\tilde a=(\rho/2)^{|\beta|}\partial_x^\alpha\partial_\xi^\beta a$
and, since $1+|\xi|\in[\rho/2,3\rho/2]$ on the box,
$\sup|\tilde a|\le C\rho^{m}N_m(a;0)$ and $\sup|\partial^{\gamma'}\tilde a|\le C\rho^{m''}\max_{|\gamma'|=N}N_{m''}(a;\gamma')$
(the anisotropy makes the $\rho$-power independent of $\gamma'$). The Landau–Kolmogorov/Taylor inequality on the unit
cube, applied on sub-cubes of side $\delta\in(0,1]$, gives
$\sup|\partial^\gamma\tilde a|\le C[\delta^{N-k}\sup_{|\gamma'|=N}|\partial^{\gamma'}\tilde a|+\delta^{-k}\sup|\tilde a|]$.
Unwinding and multiplying by $\rho^{|\beta|-m'}$:
$$|\partial^\alpha_x\partial^\beta_\xi a(x_0,\xi_0)|\,\rho^{|\beta|-m'}\le C\big[\delta^{N-k}\rho^{\,m''-m'}B+\delta^{-k}\rho^{\,m-m'}A\big],$$
$A=N_m(a;0)$, $B=\max_{|\gamma'|=N}N_{m''}(a;\gamma')$. Taking $\delta=\rho^{-\lambda}$ makes the first exponent
$m''-m'-\lambda(N-k)\le0$ and the second $m-m'+\lambda k=-(m'-m)/2$, so the whole is
$\le C[B+\rho^{-(m'-m)/2}A]\le C[B+R^{-(m'-m)/2}A]$. On $\{1+|\xi|\le R\}$ one has directly
$|\partial^\gamma a|\langle\xi\rangle^{|\beta|-m'}\le R^{m''-m'}N_{m''}(a;\gamma)$. Adding the two regions gives
exactly the note's (1), with $\Gamma=\{\gamma\}\cup\{|\gamma'|=N\}$. The sub-cube has side $\delta=\rho^{-\lambda}$
in $x$ and $\delta\cdot\rho/2\sim\rho^{1-\lambda}$ in $\xi$, so the note's parenthetical description ("boxes of side
$\sim(1+|\xi|)^{-c}$ in $x$ and $(1+|\xi|)^{1-c}$ in $\xi$") is accurate, with $c=\lambda$. **(1) is true.**
The only cosmetic flaw is that the quantifier "$N\in\mathbb N$" is declared and never used (it is absorbed into
$\Gamma$) — **repair R5**.

*It gives Wengenroth's criterion.* $N_{m''}\le N_{m'}$ always, so only one direction needs work. On
$V=\{N_m(\cdot;0)<1\}$, given $\gamma$ and $\varepsilon>0$, choose $R$ with $CR^{-(m'-m)/2}<\varepsilon/2$ and then
$\delta=\varepsilon/(2CR^{m''-m'})$; the difference of two elements of $V$ has $N_m\le2$, so the same estimate
(rescaled) shows the $S^{m''}_K$- and $S^{m'}_K$-topologies agree on $V$. This is verbatim the p. 4 form of
[Wen03, Thm. 6.1]. **Confirmed.**

*The transfer principles.* (i) Subspaces: if the topologies of $X_{k'}$, $X_{k''}$ agree on a $0$-neighborhood $V$
of $X_k$, they agree on $V\cap Y_k$, a $0$-neighborhood of $Y_k$ with the induced topology. (ii) Finite products:
take $V_1\times V_2$; a constant spectrum satisfies the criterion with $V$ the whole space. (iii) Initial topology
of one fixed injection into an acyclic spectrum: this is (i) applied to the image. **All three confirmed**, which is
what the note's "the criterion passes to initial topologies of a fixed map, to finite products with constant spectra,
and to subspaces" asserts.

*Not compact operators (the writer's deviation from the brief, upheld).* A $0$-neighborhood of the Fréchet space
$S^m_K$ constrains only finitely many seminorms, say those with $|\alpha|\le k_0$. Take
$a_\lambda=\varepsilon\lambda^{-k_0}\sin(\lambda x_1)\theta_1(x)\theta(\xi)$ with $\theta_1\in C_c^\infty$ supported
in the interior of $K$. Then $\|a_\lambda\|_{K,\alpha,\beta,m}\le C\varepsilon\lambda^{|\alpha|-k_0}\le C\varepsilon$
for $|\alpha|\le k_0$, so the whole family sits in that neighborhood; but
$\|a_\lambda\|_{K,\alpha,0,m'}\ge c\varepsilon\lambda\to\infty$ for $|\alpha|=k_0+1$, so its image in $S^{m'}_K$ is
unbounded, a fortiori not relatively compact. **The inclusion is not a compact operator**, for any $m<m'$, and the
p. 5 shortcut does not apply. (An oscillation in $\xi$, $\sin(\lambda\xi_1)/\lambda^{p}$, does the same job.) The
weaker statement the note does claim — bounded sets have relatively compact image — is true: for $B$ bounded in
$S^m_K$, Arzelà–Ascoli gives a $C^\infty_{loc}$-convergent subsequence, and
$|\partial^\gamma(a_k-a)|\langle\xi\rangle^{|\beta|-m'}\le2C_\gamma\langle\xi\rangle^{m-m'}$ makes the tail uniformly
small. **Both halves of the note's parenthetical are confirmed.**

### 2.8 Cor. 6.27 and Cor. 7.22 are true (clearing the one single-check item)

By Prop. 7.26 (p. 59), (7.36) $\bigoplus_{k\ge0}C^\infty(L;\Omega^{-1}NL)\to K(M,L)$ is a TVS-isomorphism, so every
$u\in K(M,L)$ is a **finite** sum $u=\sum_k\partial_x^k\delta_L^{v_k}$. In an adapted chart with $n'=1$,
$\delta_L^{v}=v(y)\delta(x)$ and, by (4.8),
$$a(y,\xi)=\int e^{-ix\xi}v(y)\delta^{(k)}(x)\,dx=v(y)\,(i\xi)^k,$$
a polynomial of degree $k$ in $\xi$ with smooth coefficient. Such a symbol lies in $S^{\bar m}$ iff $k\le\bar m$
(the monomials are linearly independent in $\xi$), so $K^m(M,L)$ consists exactly of the sums with $k\le\bar m$.
Also $hu=0$ for $u$ supported in $L$ (the compact $\operatorname{supp}h$ lies in the open $M\setminus L$, hence misses
$L$), so on $K^m$ the (4.10)-topology is carried entirely by the symbols.

On the finite-dimensional-coefficient space $P_{k_0}=\{\sum_{k\le k_0}v_k(y)(i\xi)^k\}$ and for $\bar m_1\ge k_0$:
$|\partial_y^\alpha\partial_\xi^\beta a|\le C\langle\xi\rangle^{k_0-|\beta|}\max_k\sup_K|\partial^\alpha v_k|$, so
$\|a\|_{K,\alpha,\beta,\bar m_1}\le C\langle\xi\rangle^{k_0-\bar m_1}\max_k\sup_K|\partial^\alpha v_k|\le C\max_k\sup_K|\partial^\alpha v_k|$;
conversely $\partial_\xi^ka|_{\xi=0}=k!\,i^kv_k$ gives
$\sup_K|\partial^\alpha v_k|\le C\|a\|_{K,\alpha,(k),\bar m_1}$. So every $S^{\bar m_1}$-topology with
$\bar m_1\ge k_0$ restricts on $P_{k_0}$ to the $C^\infty$-topology of the coefficients, and in particular the
$K^{m'}$- and $K^{m''}$-topologies coincide on $K^m$ for $m<m',m''$: **Cor. 7.22 is true**. By (6.49)
$\mathcal K(M)\equiv I_{\partial M}(\breve M,\partial M)$, compatibly with the symbol filtration (p. 41), the same
argument applied to $(\breve M,\partial M)$ gives **Cor. 6.27**. This is my own third derivation of
`w3-adjudication.md` §5.1; **the single-check flag on this statement is cleared** for the form in which the note
uses it.

### 2.9 The two repairs of printed proofs, and Cor. 3.5

*Claim 6.46.* Let $A\subset A(M)$ be bounded; replace it by its absolutely convex hull (still bounded, contains $0$).
Bounded retractivity (now proved, §2.7 + the assembly) puts $A$ inside some step $A^m(M)$, boundedly, with the
$A(M)$- and $A^m(M)$-topologies agreeing on it. Fix $m'<m$, so $A^m\subset A^{m'}$ by (6.38) and $E_{m'}$ of
Prop. 6.29 is defined on $A^{m'}$; $B:=E_{m'}(A)$ is bounded in $\dot A^{(s)}$, hence in $\dot A$. Given a
$0$-neighborhood $U$ of $\dot A$, continuity gives a $0$-neighborhood $W\subset A^{m'}$ with
$E_{m'}(W)\subset U\cap\dot A^{(s)}$. Since $\tau_{A}\le\tau_{m'}\le\tau_{m}$ and the outer two agree on $A$, all
three agree on $A$, so $W\cap A$ is a $\tau_A$-neighborhood of $0$ in $A$ and there is $V$ with $V\cap A\subset W$.
Then for $a\in A\cap V$, $E_{m'}a\in B\cap U$ and $a=R(E_{m'}a)$, i.e. $A\cap V\subset R(B\cap U)$. ∎ This is exactly
the note's sentence, including its correction of the index direction. **Confirmed.** Prop. 8.8 (p. 64) is the same
lemma with $J^m(M,L)$, $I^{(s)}(M,L)$, $R=(7.31)$ and $E_m$ of Cor. 7.31; and indeed Cor. 7.13 enters Prop. 6.45's
proof only through Claim 6.46, so it is not needed. **Confirmed.**

*Cor. 3.5.* For $a\in S^m$, $m<m'$, $\chi\in C_c^\infty$ with $\chi=1$ on $B(0,1)$:
$(1-\chi(\xi/R))a$ vanishes for $|\xi|\le R$; the $\beta'=0$ Leibniz term is
$\le\|a\|_{K,\alpha,\beta,m}\langle\xi\rangle^{m-m'}\le\|a\|(1+R)^{m-m'}$ after dividing by
$\langle\xi\rangle^{m'-|\beta|}$, and a term with $\beta'\ne0$ carries $CR^{-|\beta'|}$ on $\{R\le|\xi|\le2R\}$ and is
$\le C\|a\|R^{m-m'}$. So $\|a-\chi(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}\to0$; then an $x$-cut-off equal to $1$
on $K$ costs nothing on the $K$-seminorms, and a diagonal argument over an exhaustion gives a sequence in
$C_c^\infty(U\times\mathbb R^l)$. **Confirmed** — and no coincidence statement is used.

### 2.10 The assembly, and the memoir

$I^m(M,L)$ carries by definition ("the following map is required to be a TVS-embedding", p. 22) the initial topology
of the single $m$-independent map (4.10) into $C^\infty(M\setminus L)\oplus\bigoplus_j S^{\bar m}_{K_j}$, where
$K_j$ is the compact $x''$-projection of $\operatorname{supp}f_j$ — I checked that $a_j$ does vanish off $K_j$,
because $a_j(x'',\xi)=\int e^{-i\langle x',\xi\rangle}(f_ju)\,dx'$. Combining §2.7(i)–(iii) with §2.7's criterion for
$(S^{\bar m}_{K_j})$ gives acyclicity of $I(M,L)$. For $A^m(M)$ the same $b$-collar inequality holds: in
$\varrho=-\log x$ the seminorms read $\sup e^{m_1\varrho}|D^\gamma v|$ with $D$ the $b$-derivatives, and taking
sub-boxes of side $e^{-\lambda\varrho}$ gives the analogue of (1) with $e^{\pm\varrho}$ in place of $\langle\xi\rangle$;
the localization $u\mapsto((\lambda_ju)_j,\mu u)$ is an initial-topology map (its left inverse is summation), so
§2.7(i)–(iii) apply. $\dot A^m$, $\mathcal K^m$, $K^m(M,L)$ are closed subspaces with induced topology by (6.47),
p. 41 and p. 58; $J^m(M,L)$ corresponds to $A^m$ of the cut manifold by (7.26). All steps involved are Fréchet, so
the p. 4–5 consequences apply. **Confirmed**, and this is precisely the note's paragraph.

For the memoir I read printed p. 15 (§2.1.8, the restatement for arbitrary open $U$), p. 119 (§5.2.1, "because
$I(\mathcal F)$ is compactly retractive (Section 2.2.2)") and p. 122 (§§5.5.3–5.5.4, "Using that $J(\mathcal F)$ is
compactly retractive"; "Since $I(\mathcal F)$ is compactly retractive"); §2.2.2 is headed "Conormal distributions
when $M$ is compact" and $I(\mathcal F)=I(M,M^0;\Lambda\mathcal F)$ with $M$ closed. **The note's sentence about the
memoir is accurate on all four counts** (the two page numbers, the identification of $I(\mathcal F)$, and the fact
that the consumers are covered by the compact-$M$ repair).

---

## 3. Repairs (numbered; LaTeX-ready, exact find/replace against `alkl23-note.tex`)

Apply in order. Each FIND string occurs exactly once in the file.

### R1 (REQUIRED) — witness (d): the index $j$ is used for the sequence and for the partition of unity at once

As written, "$hu_j=0$ and $f_ju_j=0$ ($j\ge2$)" is not readable: $j$ is simultaneously the sequence index of $u_j$
and the cover index of $f_j$. Rename the cover index to $i$ (two edits), and declare $n''$ while there.

**R1a — FIND:**
```
$\operatorname{codim}L=n'\ge1$, $m<m'<m''$, and $\bar m,\bar m',\bar m''$ as in (4.9). Take $p_0\in L$, a chart $(U_1,x=(x',x''))$ adapted to $L$ with $x(p_0)=0$, and the partition of unity in (4.10) with $f_1=1$ and $h=f_j=0$ ($j\ge2$) near $p_0$ (replace any $\{h,f_j\}$ by $\{(1-\rho)h,\ \rho+(1-\rho)f_1,\ (1-\rho)f_j\}$,
```
**REPLACE:**
```
$\operatorname{codim}L=n'\ge1$, $\dim L=n''$, $m<m'<m''$, and $\bar m,\bar m',\bar m''$ as in (4.9). Take $p_0\in L$, a chart $(U_1,x=(x',x''))$ adapted to $L$ with $x(p_0)=0$, and the partition of unity $\{h,f_i\}$ of (4.10) with $f_1=1$ and $h=f_i=0$ ($i\ge2$) near $p_0$ (replace any $\{h,f_i\}$ by $\{(1-\rho)h,\ \rho+(1-\rho)f_1,\ (1-\rho)f_i\ (i\ge2)\}$,
```

**R1b — FIND:**
```
For large $j$, $hu_j=0$ and $f_ju_j=0$ ($j\ge2$), and by (4.8) the symbol of $f_1u_j=u_j$ is
```
**REPLACE:**
```
For large $j$, $hu_j=0$ and $f_iu_j=0$ ($i\ge2$), and by (4.8) the symbol of $f_1u_j=u_j$ is
```

### R2 (REQUIRED) — §4: $A^m$ of the *cut* manifold, not of $M$

(7.26) reads $\pi_*:\mathcal A(\boldsymbol M)\xrightarrow{\ \cong\ }J(M,L)$, where the paper prints a **bold** $\boldsymbol M$
for the manifold with boundary obtained by cutting $M$ along $L$ (verified in a 600-dpi render of p. 56; the text layer
loses the boldface). The note's "$A^m(M)$" reads, in the surrounding sentence, as $A^m$ of the closed $M$, for which
$A^m$ is not defined.

**FIND:**
```
and $J^m(M,L)\cong A^m(M)$ by (7.26).
```
**REPLACE:**
```
and $J^m(M,L)\cong A^m(\boldsymbol M)$ by (7.26), where $\boldsymbol M$ is the manifold with boundary obtained by cutting $M$ along $L$.
```
(`\boldsymbol` is already available: `amsmath` is loaded.)

### R3 (RECOMMENDED) — witness (d): name the compact set in the lower bound

**FIND:**
```
whereas $\|a_j\|_{K,0,0,\bar m'}\ge c\sup|g|>0$, i.e.\ $u_j\not\to0$ in $I^{m'}(M,L)$.
```
**REPLACE:**
```
whereas, for any compact $K$ meeting $\{g\ne0\}$, $\|a_j\|_{K,0,0,\bar m'}\ge c\sup_K|g|>0$, i.e.\ $u_j\not\to0$ in $I^{m'}(M,L)$.
```

### R4 (RECOMMENDED) — §2: do not implicate Prop. 3.3 and Cor. 3.5 in the p. 18 sentence

The p. 18 sentence covers Props. 3.2–3.3 and Cors. 3.4–3.6 together, but the extensions of Prop. 3.3 and Cor. 3.5 are
fine; only the Prop. 3.2 / Cor. 3.4 part fails (for every base) and the Cor. 3.6 part fails (for non-compact bases).
Saying so is both more accurate and more courteous.

**FIND:**
```
together with the sentence on p.~18 extending Props.~3.2--3.3 and Cors.~3.4--3.6 to symbols on bundles over a manifold;
```
**REPLACE:**
```
together with the part of the sentence on p.~18 that extends Prop.~3.2 and Cors.~3.4 and~3.6 to symbols on a vector bundle (the extensions of Prop.~3.3 and Cor.~3.5 are unaffected);
```

### R5 (RECOMMENDED) — §4: drop the unused quantifier in (1)

$N$ is declared and never appears in the display; it is absorbed into $\Gamma$.

**FIND:**
```
there are $N\in\N$, a finite set $\Gamma$ of indices, and $C,R_0>0$ such that
```
**REPLACE:**
```
there are a finite set $\Gamma$ of multi-indices and constants $C,R_0>0$ such that
```

### R6 (RECOMMENDED) — the AI-use footnote: match the program's standard wording

The program's four arXiv title pages (`results/arxiv/*/main.tex`, and the settled record at
`results/arxiv/README.md`) use `\textbf{Use of AI.}` and "adjudicated its decisions". The note's substance is the
same; align the two visible divergences. (The em-dashes of the canonical wording are correctly replaced by
parentheses here, and the "structured research program" / repository clause is correctly omitted from a document that
must carry no program material — keep both of those choices.)

**FIND:**
```
\emph{Use of AI.} The mathematics in this note (the derivations, the computations, and the text) was produced by Claude (Anthropic) working under the author's direction; the author set the objectives, made the technical and editorial decisions, and is responsible for the content. Claude is a tool and is not an author.
```
**REPLACE:**
```
\textbf{Use of AI.} The mathematics in this note (the derivations, the computations, and the text) was produced by Claude (Anthropic) working under the author's direction; the author set the objectives, adjudicated the technical and editorial decisions, and is responsible for the content. Claude is a tool and is not an author.
```

### R7 (OPTIONAL) — §4: record the Fréchet hypothesis of the quoted consequences

The p. 4–5 statements ("acyclic iff boundedly/compactly/sequentially retractive"; "acyclic LF-spaces are complete and
regular") are quoted there under "If the steps $X_k$ are Fréchet spaces". Half a clause makes the note self-contained.

**FIND:**
```
Hence, for compact $M$, the LF-spaces $I(M,L)$, $A(M)$, $\dot A(M)$, $\mathcal K(M)$, $J(M,L)$, $K(M,L)$ are acyclic,
```
**REPLACE:**
```
Hence, for compact $M$, the LF-spaces $I(M,L)$, $A(M)$, $\dot A(M)$, $\mathcal K(M)$, $J(M,L)$, $K(M,L)$, whose steps are Fr\'echet spaces, are acyclic,
```

### R8 (OPTIONAL) — §4: one clause on Remark 3.8

Remark 3.8 (p. 18) argues from "$S^\infty$ is sequentially retractive (Corollary 3.6)", which is unavailable for
non-compact $U$; its conclusion, however, is immediate from witness (c). Worth a clause, since the memoir cites
Remark 3.8 alongside Cors. 3.4–3.6.

**FIND:**
```
by the Leibniz rule, and a cut-off in $x$ finishes.
```
**REPLACE:**
```
by the Leibniz rule, and a cut-off in $x$ finishes. The conclusion of Remark~3.8 (p.~18) likewise follows from (c) directly, without the sequential retractivity of $S^\infty(U\times\R^l)$, which is what its printed argument uses.
```

### R9 (OPTIONAL) — witness (e): justify "$P=1$" in (6.41)

(6.41) is printed with the operators $P_k$ of a spanning set; the topology of $A^m(M)$ is, by its definition on p. 38,
the projective one over all $P\in\operatorname{Diff}_b(M)$, so $P=1$ is admissible.

**FIND:**
```
But the seminorm (6.41) with $P=1$ gives
```
**REPLACE:**
```
But the seminorm (6.41) with $P=1$ (the topology of $A^m(M)$ is the projective one over all $P\in\Diff_b(M)$, p.~38) gives
```

**After applying R1–R9, rebuild with `pdflatex` twice** and confirm the note is still 3 pages with no overfull box;
R2, R4 and R8 each add roughly one line, R5 removes half a line. If page 3 would spill, R8 is the first thing to drop.

---

## 4. One correction owed to the program record (not to the note)

`w3-adjudication.md` §0 (verdict table, C6 dated block) and `novelty/adjudication.md` §2 C6(ii) both say that the
program's own Prop. 5.6 / §4.8(iii) "proves the compactness of $S^m_K\to S^{m'}_K$", and conclude that acyclicity of
the model spectra "is one printed sentence away" from the p. 5 compact-spectrum remark. That is a mis-summary of
§4.8, which says two different things: (iii) *bounded* sets have relatively compact image (true, Arzelà–Ascoli plus
the tail), and (ii) the inclusions are *not* compact operators, "already for one point" (also true — I re-derived it
in §2.7). A compact operator must map some $0$-neighborhood, not merely some bounded set, into a relatively compact
set, and a $0$-neighborhood of a Fréchet symbol space constrains only finitely many seminorms. So the p. 5 shortcut
is **not** available even for a one-point base, the Wengenroth/interpolation route is load-bearing at the manifold
level and not only after parametrization, and the C6(ii) grade "PARTIAL — one printed sentence away" rests on the
error. Recommended: amend §0 of `w3-adjudication.md` and C6(ii) of `novelty/adjudication.md` to read "§4.8(iii)
proves that bounded sets of $S^m_K$ have relatively compact image in $S^{m'}_K$; §4.8(ii) proves the inclusions are
not compact operators, so the p. 5 compact-spectrum shortcut does not apply". The note itself already states the
correct version and needs no change on this account.
