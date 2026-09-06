# verify3-O.md — fresh-reader check of the Session 17 repair of `alkl23-note.tex` and of the new `alkl23-derivations.tex`

Reader: fresh reader (second model, Opus 5), 2026-09-06. Inputs read: `xcheck-s17/repair3-log.md`;
`git diff 26f306c HEAD -- results/c3-r/s14/alkl23-note.tex` (the whole repair diff: 8 changed lines,
73 of 81 unchanged; the working tree matches HEAD for the `.tex`); `xcheck-s17/adjudication.md`
§Recommendation items 1–11 and the companion list C1–C9; `novelty/ALKL-2024-published.txt` plus
renders of published pp. 39 and 56 from the CC-BY PDF; the memoir PDFs v1 and v2 in `fetched-r3/`;
the rebuilt `alkl23-note.pdf` (4 pp.) and `alkl23-derivations.pdf` (11 pp.), read as text and as
200–500 dpi renders.

**Verdict: FIX-FIRST — one fix, and it is in the companion, not in the note.**
The note is clean: every one of items 1–11 is applied faithfully (item 1 in its companion-attached
variant), every number, page and quoted phrase in a changed line checks out against the published
text or a live query re-run today, and every glyph-sensitive symbol renders correctly. The single
fix is a constant in `alkl23-derivations.tex` §9.6 that holds only for non-negative orders.

---

## A. Every changed line of `alkl23-note.tex`, checked three ways

(i) = against the adjudication's replacement text; (ii) = against the published paper / live record;
(iii) = as rendered in the rebuilt PDF (200–500 dpi crops read for the glyph-sensitive spots).

| Line | Item | Change | (i) adjudication | (ii) fact check | (iii) render | Verdict |
|---|---|---|---|---|---|---|
| 29 | 1 | §1 last sentence: appended "; the proofs of the estimate \eqref{interp} and of the assembly in \S4 are written out in full in the accompanying derivations." | Verbatim, and the **companion-attached** variant (not the "available on request" variant) — correct, since the companion is being attached | no page/number claims | p. 1: "…stands once this is done; the proofs of the estimate (1) and of the assembly in §4 are written out in full in the accompanying derivations." `\eqref` resolves to **(1)** | **OK** |
| 47 | 2 | §3(d): "$\rho\in C_c^\infty(U_1)$, $0\le\rho\le1$, $\rho=1$ on $N$" | Verbatim | no page claims; makes $\{\tilde h,\tilde f_i\}$ a partition of unity in the nonnegative sense, as N4 requires | p. 2: "ρ ∈ C_c^∞(U_1), 0 ≤ ρ ≤ 1, ρ = 1 on N" | **OK** |
| 58 | 3 | §3(e): "(p.~56)" → "(pp.~50, 56)" | Verbatim | p. 50 (line "Let **M** be the smooth manifold with boundary defined by 'cutting' M along L", §7.1, between the p. 50 and p. 51 markers) and p. 56 (the (7.26)/(7.27) block and the $\boldsymbol x$ sentence) — both re-read | p. 2: "…obtained by cutting M along L (pp. 50, 56)" | **OK** |
| 58 | 3 | §3(e): inserted "(both lie in $C_c^\infty(M\setminus L)$, hence in every $J^{m_1}(M,L)$, since $Pu$ is then compactly supported where $\boldsymbol x$ is bounded below)" | Wording verbatim; placed **before** the comma rather than after it (logged deviation; punctuation only, and it reads correctly) | Correct as mathematics and correctly avoids the (7.28) route, which C3 shows is false for $m_1>0$; published (7.27) and the $\boldsymbol x$ sentence re-read on p. 56 | 500 dpi crop of p. 2: "…since $Pu$ is then compactly supported where **𝒙** is bounded below" — **bold 𝒙**, correct; the neighbouring "$\boldsymbol x^mL^\infty(M)$", "$\boldsymbol x$ the extension", "boundary **𝑴**" all bold, "cutting *M* along *L*" ordinary | **OK** |
| 58 | 11 | §3(e): "at \S2.5.10, p.~38, and \S2.6.7, p.~53" → "at \S2.5.10 and \S2.6.7, arXiv pp.~38, 53" | Comma form instead of the adjudication's "(arXiv pp.~38, 53)" (logged deviation, to avoid nesting parentheses inside an existing parenthetical); the instruction "write arXiv p. before each memoir page number" is met | Verified in the memoir PDF (printed page = PDF page − 6): printed p. 38 carries §2.5.10 and "the topologies of A(M) and C^∞(M̊) coincide on every A^m(M)"; printed p. 53 carries "the topologies of J(M,L) and C^∞(M∖L) coincide on every J^m(M,L)" (§2.6.7, whose header is on p. 52). Same headers on the same printed pages in v1 and v2 | p. 2: "([2] restates these second assertions at §2.5.10 and §2.6.7, arXiv pp. 38, 53.)" | **OK** |
| 60 | 11 | §3(f): "\cite[\S2.1.8, p.~15]" → "\cite[\S2.1.8, arXiv p.~15]" | Verbatim | Memoir printed p. 15, §2.1.8: "For any open U ⊂ R^n …" and "The following properties hold [ÁLKL23, Corollaries 3.4–3.6 and Remark 3.8]: The topologies of S^∞(U×R^l) and C^∞(U×R^l) coincide on S^m(U×R^l) … and S^∞(U×R^l) is an acyclic Montel space" — the whole restatement is on p. 15 | p. 2: "[2, §2.1.8, arXiv p. 15]" | **OK** |
| 60 | 4 | §3(f): parenthetical → "(Sect.~4.3.3, p.~23, excepts acyclicity in the case of $I(M,L)$ when $M$ is non-compact, while still claiming it for $\bigcup_mI^m(M,L)$ and $I_c(M,L)$; the symbol statements of \S3 make no exception of any kind.)" | Verbatim | Published p. 23, §4.3.3: "Corollary 4.7 has extensions for ⋃_m I^m(M,L) and I_{·/c}(M,L), except acyclicity in the case of I(M,L)." The paper's "·/c" convention (fixed two sentences earlier, "I^{−∞}_{·/c}(M,L) = ⋃_m I^m_{·/c}(M,L)") means arbitrary **and** compact support, so what survives the exception is exactly ⋃_m I^m and I_c — the note's reading | p. 2, reads correctly with the ⋃ operator | **OK** |
| 67 | 5 | §4: "$\sim(1+|\xi|)^{-c}$" → "$(1+|\xi|)^{-c}$" and the constants sentence ($c$, $N$, $\Gamma$, $R_0$, $C$ and the two exponent identities) | Verbatim except two logged additions: "(for $\gamma\ne0$; for $\gamma=0$ the bound is elementary, with $\Gamma=\{0\}$, $C=1$, $R_0=1$)" and "($d=\dim U$; …)" | Both additions are right. γ = 0: $N_{m'}(a;0)\le R^{m''-m'}N_{m''}(a;0)+R^{m-m'}N_m(a;0)$ and $R^{m-m'}\le R^{-(m'-m)/2}$ for $R\ge1$, so (1) holds with Γ = {0}, C = 1, R_0 = 1. Recomputed both exponent identities: $c|\gamma|+m-m'=(m'-m)/2-(m'-m)=-(m'-m)/2$; and $-c(N|S|-|\gamma|)+m''-m'\le-c(N-|\gamma|)+m''-m'<0$ from $N>|\gamma|+(m''-m')/c$ | p. 3, 500 dpi: primes ($m''-m'$, $m'$), $N\chi_S$, $R_0=\max\{1,(2N\sqrt l)^{1/c}\}$ with $\sqrt l$ (ell), all correct | **OK** |
| 67 | 5 | §4: inserted the ε–δ parenthetical after "…$0$-neighborhood $\{N_m(\cdot\,;0)<1\}$ of $S^m_K$" | Verbatim | Matches companion §9.5 exactly (choose R for the first term, then δ for the second; absolute convexity closes it) | p. 3, reads correctly | **OK** |
| 67 | 6 | §4: "whose steps are Fr\'echet spaces" → "… (for $I^m(M,L)$ by p.~22; for $A^m(M)$, hence $J^m(M,L)$, by Cor.~6.38 with Remark~6.41, or directly: … countable family (6.41) … $x^mL^\infty(M)\subset C^{-\infty}(M)$, p.~37 …)" | Verbatim | p. 22: "I^m(M,L), which becomes a Fréchet space [25, Sections 6.2 and 6.10]" ✓. p. 46: "Corollary 6.38 A^m(M) ≡ x^m H_b^∞(M) ≡ x^{m+1/2}H^∞(M̊)" ✓; p. 47: "Remark 6.41 … independent of g. So they hold true without the assumptions (A) and (B)" ✓. p. 38: "Let {P_j | j ∈ N_0} be a countable C^∞(M)-spanning set of Diff_b(M). The topology of A^m(M) can be described by the semi-norms ‖·‖_{k,m} … (6.41)" ✓. p. 37: "there is a continuous inclusion x^m L^∞(M) ⊂ C^{−∞}(M)" ✓ | p. 3, reads correctly | **OK** |
| 67 | 9 | §4: appended to "…and then of their Montel clauses": "(the printed Montel step of Cor.~4.7 also cites Cor.~3.6 over the non-compact base $L_j$; the compactly based models avoid this as well)" | Verbatim (optional clause, taken) | Published p. 23, proof of Cor. 4.7: "Then I(M,L) is semi-Montel because C^∞(M∖L) and S^∞(N*L_j; ΩN*L_j) are Montel spaces (Corollary 3.6)"; $L_j = L\cap U_j$ is fixed on p. 22, an open (hence in general non-compact) subset of L | p. 3, ends the sentence with "…avoid this as well)." | **OK** |
| 69 | 7 | §4: "is bounded in some $A^m(M)$, on which the topologies…" → "…, and on that hull the topologies…" | Verbatim | Removes the reading that witness (e) refutes; the intended antecedent (the hull) is now explicit | p. 3: "…is bounded in some A^m(M), and on that hull the topologies of A(M), A^{m′}(M) and A^m(M) coincide…" | **OK** |
| 69 | 9 | §4: "Cor.~3.5 follows directly" → "…directly (as Remark~3.7, p.~18, anticipates)" | Verbatim (optional clause, taken) | p. 18: "Remark 3.7 Another proof of Corollary 3.5 could be given like in Proposition 6.10." (between the p. 18 and p. 19 markers) | p. 3, reads correctly | **OK** |
| 69 | 8 | §4: "Cor.~6.27 is the case $(\Mb,\partial M)$ via (6.49)." → "…$(\Mb,\partial M)$: by (6.47), $\mathcal K^m(M)=\dot A^m_{\partial M}(M)=I^m_{\partial M}(\Mb,\partial M)=K^m(\Mb,\partial M)$ with the same subspace topologies." | Verbatim | (6.47) on p. 40: "Ȧ^m(M) = I^m_M(M̆,∂M) ⊂ I^m(M̆,∂M) (m ∈ R), which are closed subspaces"; §6.13 on p. 40: "K^{(s)}(M) = Ȧ^{(s)}_{∂M}(M), K^m(M) = Ȧ^m_{∂M}(M), K(M) = Ȧ_{∂M}(M)"; §7.10 on p. 58: "K^m(M,L) = I^m_L(M,L) … closed subspaces". Applying §7.10 to (M̆,∂M) gives the last equality; restricting (6.47) to supports in ∂M gives the middle one. (6.49), p. 41, is indeed printed as a consequence of Cor. 6.20 | 500 dpi crop of p. 3: **𝒦**^m(M) calligraphic, **Ȧ**^m_{∂M}(M) dotted, **M̆** breve in both "(M̆, ∂M)", final $K^m$ ordinary — all correct | **OK** |
| 69 | 11 | §4: "\S5.2.1, p.~119; \S\S5.5.3--5.5.4, p.~122" → "arXiv p.~119 … arXiv p.~122" | Verbatim | Memoir printed p. 119: "5.2.1. Injectivity of ĵ_*"; printed p. 122: "5.5.3. The equality ker R̄_* = im ῑ_*" ("density of C_c^∞(M^1;ΛF) in J(F) (Section 2.6.7)") and "5.5.4. Injectivity of ῑ_*" ("Since I(F) is compactly retractive"). Identical printed pages in v1 and v2 | p. 3–4, reads correctly | **OK** |
| 72 | 10 + 11 | §5 rewritten: Crossmark clause, Zbl number, the three DOI indexes, Google Scholar, the "presumably now in print" clause, "accompany this note" | Item 10 verbatim; the item-11 clause placed in §5 (permitted: "add to §2 or §5"); "accompany this note" is the attached-companion option | **All re-run live today.** arXiv 2304.00798: abs page lists v1, v2, v3 only; `/abs/2304.00798v4` → HTTP 404, v3 → 200. Crossref 10.1007/s11868-024-00617-y: `update-to` null, `relation {}`, `is-referenced-by-count` 0. Crossmark dialog: contains "Document is current". zbMATH API document 7901419: `identifier` 1564.46031, one editorial contribution of type "summary", no review, no corrigendum. OpenAlex W4399476425: `cited_by_count` 0. Semantic Scholar DOI record: `citationCount` 0. Google Scholar: "Cited by 3", and the cites page lists exactly three — the authors' own preprint copy, "Analytic Tools" (in *A Trace Formula for Foliated Flows*, 2026, Springer = ch. 2), and Gilsdorf's 2026 book; none a correction | 300 dpi crop of p. 4: quotation marks around "Document is current" render as curly ``…'' correctly; "Zbl 1564.46031", "OpenAlex", "Chapter 2 of [2]" all correct | **OK** |
| 77 | 11 | Bibliography [ALKL24m] → LNM 2387 entry with the book DOI, plus the citation-convention sentence | Verbatim | Crossref 10.1007/978-3-032-15413-2: type book, "A Trace Formula for Foliated Flows", container "Lecture Notes in Mathematics", publisher Springer Nature Switzerland, location Cham, issued 2026, created 2026-05-03, ISBNs 9783032154125/9783032154132; chapter `_2` = "Analytic Tools", pp. 13–99. Springer book page (via the idp cookie bounce): **"Lecture Notes in Mathematics (LNM, volume 2387)"**, Springer Cham, © 2026 — the volume number Crossref does not carry. arXiv API 2402.06671: latest v2, `updated` 2024-02-13 ("v2, 13 February 2024"); abs page lists v1, v2 only; no journal-ref | p. 4: "*A Trace Formula for Foliated Flows*, Lecture Notes in Mathematics, vol. 2387, Springer, Cham (2026), https://doi.org/10.1007/978-3-032-15413-2; arXiv:2402.06671 (v2, 13 February 2024). Sections are cited by number; the page numbers given are those of the arXiv version, the same in v1 and v2." | **OK** |

Build: `pdflatex` twice, exit 0, 0 errors, 0 Overfull/Underfull boxes, 0 LaTeX warnings, no "??", 4 pages.
Dates: `\date` and §5 both read September 6, 2026 (today) — correct, unchanged.

### Two cosmetic observations on the note (not fixes, no action needed)
1. §4 now defines `$d=\dim U$` while §3(f) writes `$U\subset\R^n$` for the same object; two names for one
   dimension. The adjudication's replacement text uses $d$, and $d$ had to be defined, so this is the
   right trade; "$d=\dim U$" could equally read "$d=n=\dim U$".
2. The note writes ordinary $A$, $J$, $I$ where the paper prints script $\mathcal A$, $\mathcal J$,
   $\mathcal I$ (but keeps $\mathcal K$). This is pre-existing, consistent throughout, and unambiguous.

---

## B. `alkl23-derivations.pdf` (new, 11 pp.) — read end to end

Build: `pdflatex` twice, exit 0, 0 errors, 0 Overfull/Underfull boxes, 0 undefined references or
citations, no "??".

**Conversion from the `.md`.** §§0–12 present in the same order and with the same content; every
formula I checked is a faithful LaTeX rendering of the Unicode original (Lemmas A and B, Prop. 9.4
and its two exponent lines, §9.5's (M*) argument and transfer rules, §9.6's b-model, §9.7's five
bullets, §§10.1–10.4). The `.tex` adds material the `.md` lacks (the γ = 0 instance in 9.4, the
written-out b-model inequality in 9.6, the extra §0 rows) and drops nothing.

**Internal apparatus removed** ✓ — no program/status header (replaced by a two-sentence intro naming
the note and the citation conventions), no "(adjudication)" tags, no §13, and §12 is now the public
record paragraph rather than a pointer to an internal file. A grep for `adjudication|brief|Deviations|
internal|xcheck|Session|LOG|STATUS` over the rendered text returns nothing.

**C1–C9, each checked in the rendered PDF:**

- **C1** ✓ §5: "ρ = 1 on a neighborhood N of the compact set x^{−1}({0} × supp g) ⊂ L (with g as below)" — the point p_0 is gone.
- **C2** ✓ §5: "pick η_0 ≠ 0 with ψ̂_*(η_0) ≠ 0 (exists: ψ̂_* is entire and ≢ 0, so its zero set has empty interior)". Correct: ψ_* = Δ^{N_0}ψ is compactly supported and ≢ 0 (a compactly supported polyharmonic function is 0), so ψ̂_* is entire and ≢ 0.
- **C3** ✓ §6: the false chain through J^{(∞)} is gone. (7.28) is now used only for the ambient membership C^∞(M) ⊂ C^{−∞}(M,L), and J^{m_1} membership comes from the direct bound. Checked against published (7.28) on p. 56.
- **C4** ✓ §7 item 5: the divergent family is replaced by the dilated annular bump a_j = ψ(x) j^{m′} φ(ξ/j), φ ∈ C_c^∞({½<|η|<2}), φ(e_1) = 1. Recomputed: ∂_x^α∂_ξ^β a_j is supported where 1+|ξ| ≍ j, so every S^{m″}-seminorm is ≲ j^{m′−|β|}·j^{|β|−m″} = j^{m′−m″} → 0, while ‖a_j‖_{K′,0,0,m′} ≥ j^{m′}(1+j)^{−m′} = (j/(1+j))^{m′} → 1. Correct.
- **C5** ✓ §9.5: "choose R ≥ max_i R_{0,i}", with Γ = ⋃_i Γ_i.
- **C6** ✓ §9.6: "with (k, k′, k″) in the roles of (m, m′, m″), i.e. with c := (k′−k)/(2|γ|) > 0 and N > |γ| + (k″−k′)/c (not with m = −k etc. substituted literally, which would give c < 0)", and the b-model inequality is written out. Both b-model exponents recompute (see below). **One defect here — see §C.**
- **C7** ✓ §9.7: the Fréchet fill for A^m(M) is present in both forms (Cor. 6.38 + Remark 6.41, with the non-circularity note; and the direct Cauchy-sequence argument through x^mL^∞(M) ⊂ C^{−∞}(M), p. 37), transferred to J^m by (7.26) and to the three closed subspaces; the O4 narrowing is stated ("The models S^m_K and B^m_K need no such statement: the transfer rule uses only (M*) of the target spectrum"); and "take K with int K ≠ ∅, since S^m_K = {0} otherwise, and θ_1 ∈ C_c^∞(int K)" is in the non-compactness remark.
- **C8** ✓ §10.1 renders "Let E_{m′}: A^{m′}(M) → Ȧ^{(s)}(M) … (RE_{m′} = 1 on A^{m′})" with m′ < m, and repeats the correction explicitly; §10.2 repeats it for J^{m′} ⊃ J^m.
- **C9** ✓ §0 table: (6.43) is written "lim_{ϵ↓0} sup_{{0<x<ϵ}} |x^{−m}P_k u|" — I rendered published p. 39 at 300 dpi and the printed form is exactly that; (7.26) is written "π_*: A(**M**) → J(M,L)" with the subscript star and bold **M** — published p. 56 rendered at 300 dpi shows bold **π**_*: 𝒜(**M**) → J(M,L). (The companion uses an ordinary π and an ordinary A where the paper prints bold π and script 𝒜; same convention as the note, and the star and the bold M — the two things C9 named — are right.)

**The mathematics of §9, recomputed from the rendered text:**

- **Lemma A (9.2)** ✓. Taylor at t with y_i = f^{(i)}(t)h^i/i! and |r_k| ≤ (Nh)^N‖f^{(N)}‖/N!; the Vandermonde matrix (k^i)_{0≤k,i≤N−1} has distinct nodes 0,…,N−1 and an inverse depending only on N; |f^{(j)}(t)| = j!h^{−j}|y_j| then gives the stated bound. The j = N caveat is stated.
- **Lemma B (9.3)** ✓. The induction splits Lemma A's two terms into the 1 ∉ S and 1 ∈ S families, and ∂_1^N∂^{γ̃}F = ∂^{γ̃}(∂_1^N F) makes the second application legitimate. The hypothesis γ_i ≤ N is what Lemma A needs.
- **Prop. 9.4, S = ∅ exponent** ✓. ∏_i h_i^{−γ_i} = w^{c|α|}w^{−(1−c)|β|}; times sup_Q|a| ≤ 2^{|m|}w^m N_m(a;0) and the weight w^{|β|−m′}: c|α| − (1−c)|β| + m + |β| − m′ = c|α| + c|β| + m − m′ = c|γ| + m − m′, and c|γ| = (m′−m)/2, so the exponent is **−(m′−m)/2**. Matches.
- **Prop. 9.4, S ≠ ∅ exponent** ✓. The four products give −cN|S_x| + c|α_S| + N|S_ξ| − cN|S_ξ| − |β_S| + c|β_S| + c|α_{S^c}| − |β_{S^c}| + c|β_{S^c}|; adding the sup factor w^{m″−N|S_ξ|} and the weight w^{|β|−m′}, the |S_ξ| and |β| terms cancel and the total is −cN|S| + c|γ| + m″ − m′ = **−c(N|S|−|γ|) + m″ − m′**, which is ≤ −c(N−|γ|) + m″ − m′ < 0 exactly because N > |γ| + (m″−m′)/c. Matches.
- **The box geometry** ✓. √l N w^{1−c} ≤ w/2 ⟺ 2N√l ≤ w^c, which is what R_0 = max{1,(2N√l)^{1/c}} buys; hence 1+|ξ′| ∈ [w/2, 3w/2] on Q and the constants 2^{|m|}, 2^{|m″|+Nl} are correct with the absolute values as written.
- **γ = 0 (9.4)** ✓, and it is the same statement as the note's new parenthetical: splitting at w = R gives N_{m′}(a;0) ≤ R^{m″−m′}N_{m″}(a;0) + R^{m−m′}N_m(a;0), and m − m′ < −(m′−m)/2, so Γ = {0}, C = 1, R_0 = 1.
- **§9.5** ✓. (M*) ⇒ coincidence on V uses only that V and W_0 are absolutely convex, which they are; k′ = k+1 in Wengenroth's Thm 6.1 as quoted on p. 4.
- **§9.6 b-model exponents** ✓ as identities: S = ∅ gives c|γ| + k − k′ = −(k′−k)/2 and S ≠ ∅ gives −c(N|S|−|γ|) + k″ − k′ < 0, and the w ≤ R regime gives R^{k″−k′}. The chain B^{−k}_K ⊂ B^{−k′}_K ⊂ B^{−k″}_K is right for k < k′ < k″, since B^m ⊂ B^{m′} for m′ < m. **But see §C.**
- **§9.7 and §10** ✓. The assembly, the Montel argument, the "not compact operators" witness (a_λ = ελ^{−k_0}sin(λx_1)θ_1(x)θ(ξ), with N_{m′}(a_λ;(α_0,0)) ≳ ελ for α_0 = (k_0+1)e_1), the Claim 6.46 and Prop. 8.8 repairs with the corrected index, the direct Cor. 3.5 proof, and the polynomial-symbol argument for Cors. 6.27/7.22 all check out.

**Page anchors in §0 spot-checked against the published text** (page marker arithmetic on
`ALKL-2024-published.txt`): p. 4 criterion, pp. 4–5 Prop. 6.4/Cor. 6.5, p. 5 compact spectra,
(3.1) p. 15, (3.4)/(3.5) p. 16, Prop. 3.2 p. 16, Prop. 3.3 / Cors. 3.4, 3.5 p. 17, Cor. 3.6,
Remarks 3.7 and 3.8, bundle extension p. 18, adapted chart p. 19, Prop. 4.3 p. 21, §4.3.2 cover
sentence and "becomes a Fréchet space" p. 22, Cors. 4.5, 4.6, 4.7 and §4.3.3 p. 23, Diff_b p. 35,
(6.33) p. 36, x^mL^∞ p. 37, A^m/(6.38)/(6.40)/(6.41) p. 38, (6.42)/(6.43)/Prop. 6.12/Cors. 6.14,
6.16 p. 39, (6.47)/Cor. 6.21/Cor. 6.22/§6.13 p. 40, Cor. 6.27/Cor. 6.28/(6.49) p. 41, Prop. 6.29
p. 42, Cor. 6.38 p. 46 and Remark 6.41 p. 47, Claim 6.46 p. 48, cutting p. 50, (7.26)–(7.28)/
Cor. 7.13 p. 56, Cor. 7.15 p. 57, K^m(M,L)/Cor. 7.22 p. 58, Prop. 7.26 p. 59, Cor. 7.31 p. 60,
Prop. 8.8 p. 64, refs [18] p. 67 and [39] p. 68. **All correct.** The three memoir rows
(§2.1.8 arXiv p. 15; §§2.5.10, 2.6.7 arXiv pp. 38, 53; §5.2.1 arXiv p. 119, §§5.5.3–5.5.4 arXiv
p. 122) and §11's extra anchor (§2.2.2, arXiv p. 21, "I(M,L) is barreled, ultrabornological,
webbed, acyclic and a Montel space … [ÁLKL23, Corollaries 4.2 and 4.7]") were checked in the
memoir PDF and are correct; I(F) = I(M,M^0;ΛF) is fixed on arXiv p. 117 as §11 says.

**Glyph checks in the rendered companion:** bold **𝒙** and bold **𝑴** throughout the §0 (7.26)/(7.27)
and "cutting" rows and throughout §6; breve **M̆** and dotted **Ȧ** in §5 and §9.7; primes
(m̄′, m̄″, k′, k″, m′, m″) everywhere I checked; √l, N χ_S, |S_ξ|, ∂^{Nχ_S} all correct;
the numbered display (1) resolves.

### One cosmetic observation on the companion (no action needed)
The AI-use footnote is copied from the note and still says "The mathematics in **this note**…".
In a document titled "Derivations accompanying …" that reads slightly oddly, though a reader
receiving both will not be misled.

---

## C. The one fix

**FIX 1 — `results/c3-r/s14/alkl23-derivations.tex`, §9.6 (line 252): the two b-model constants
`e^k` and `e^{k''}` are valid only for non-negative orders.**

On the box Q the base variable satisfies w′ := e^{ϱ′} ∈ [w, ew], and N^b_{−k}(v;γ) = sup w′^{−k}|∂^γ v|,
so |v| ≤ (w′)^k N^b_{−k}(v;0). For k ≥ 0 that is ≤ e^k w^k N^b_{−k}(v;0), as printed; but for k < 0
one has (w′)^k ≤ w^k while e^k w^k < w^k, so the printed inequality is **false** — and k can be
negative, because the orders are written as −k > −k′ > −k″ with k, k′, k″ real (k < 0 is the case
m = −k > 0 of the A^m filtration, which the criterion has to cover). The same applies to k″. The
conclusion is unaffected — C is allowed to depend on the orders, and §9.4 already writes its
analogous constants correctly as 2^{|m|} and 2^{|m″|+Nl} — but the displayed step should be right.

old (exact string, occurs once):

    $\sup_Q|v|\le e^kw^kN^b_{-k}(v;0)$, $\sup_Q|\partial^{N\chi_S}v|\le e^{k''}w^{k''}N^b_{-k''}(v;N\chi_S)$

new:

    $\sup_Q|v|\le e^{|k|}w^kN^b_{-k}(v;0)$, $\sup_Q|\partial^{N\chi_S}v|\le e^{|k''|}w^{k''}N^b_{-k''}(v;N\chi_S)$

(The old string occurs exactly once in the file; each of its two fragments `e^kw^k` and
`e^{k''}w^{k''}` also occurs exactly once, so the edit is unambiguous either way.)

After the edit, rebuild `alkl23-derivations.pdf` with `pdflatex` twice and confirm §9.6 reads
"e^{|k|}" and "e^{|k''|}". (The internal `.md` at §9.6 does not carry these two constants at all,
so it needs no matching change; if the dated-tag convention is being kept, a note that the two
b-model constants were added in the `.tex` with absolute values would be consistent.)

Nothing in `alkl23-note.tex` needs changing: the note may go as it stands once the companion is
rebuilt.
