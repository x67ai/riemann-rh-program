# a06-memoir-pagemap — Round-4 ingest report (Session 18, 2026-09-09)

**Agent:** a06-memoir-pagemap. **List item:** 9 (P3). **Flagged at:** `results/c3-r/referee-s14/novelty-adjudication.md` Cov-3 (and N4b); `results/c3-r/s16/novelty/adjudication.md` §4 item 5.

**Files:**
- `fetched-r4/r4-09-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-LNM2387-2026-PUBLISHED.pdf` — the published memoir (this ingest).
- `fetched-r3/r3s-17-…-arxiv-2402.06671v1-SESSION8-FETCH.pdf` — arXiv v1 (the program's working text).
- `fetched-r3/r3s-39-…-arxiv-2402.06671v2-SESSION16-FETCH.pdf` — arXiv v2.

Sections are appended as they are finished; a section that is absent was not reached.

## §1. Identity verification

**File:** `fetched-r4/r4-09-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-LNM2387-2026-PUBLISHED.pdf` — 8,785,829 bytes, 233 PDF pages, PDF 1.7, producer "Adobe PDF Library 10.0.1", created 2026-03-24, modified 2026-03-26, tagged, not encrypted. Page size 439 × 666 pt (Springer LNM trim).

**What it is (read from the file itself, PDF pp. 1–5, 8–10, and the chapter-opening footers):**
- Series page (PDF p. 1): "Lecture Notes in Mathematics 2387 / Jesús A. Álvarez López / Yuri A. Kordyukov / Eric Leichtnam / A Trace Formula for Foliated Flows".
- Title page (PDF p. 4): authors and title, Springer logo. Copyright page (PDF p. 5): "ISSN 0075-8434  ISSN 1617-9692 (electronic) / Lecture Notes in Mathematics / ISBN 978-3-032-15412-5  ISBN 978-3-032-15413-2 (eBook) / https://doi.org/10.1007/978-3-032-15413-2 / Mathematics Subject Classification: 58J32, 57R30, 58A14, 35K05, 57R30, 35S05 / … © The Editor(s) (if applicable) and The Author(s), under exclusive license to Springer Nature Switzerland AG 2026 / … This Springer imprint is published by the registered company Springer Nature Switzerland AG / The registered company address is: Gewerbestrasse 11, 6330 Cham, Switzerland". Author affiliations (PDF p. 5): Álvarez López — Dept of Math & CITMAga, Univ. of Santiago de Compostela; Kordyukov — Institute of Mathematics, Ufa Federal Research Centre of RAS; Leichtnam — IMJ-PRG, Paris.
- Front matter: Foreword by Christopher Deninger (pp. v–vi), Abstract (p. vii), Declarations (p. ix), Contents (p. xi). Chapters 1–7 pp. 1–216, References pp. 217–221, Index pp. 223–231, LNM editorial policy pp. [232–233 of the PDF, unnumbered].
- Every chapter-opening page carries the Springer footer "© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026 / J. A. Álvarez López et al., *A Trace Formula for Foliated Flows*, Lecture Notes in Mathematics 2387, https://doi.org/10.1007/978-3-032-15413-2_N" (N = chapter number).

**Is the text final?** Yes — this is the typeset Springer edition (LNM house style: unnumbered-looking "1.3.1 Ingredients of the Trace Formula" headings, right-hand equation labels, "Sect." cross-references, Springer copyright footers, an Index). No "uncorrected proof" or "author accepted manuscript" marking anywhere; the copyright page carries the final ISBN/DOI. The file matches list item 9's citation EXACTLY (authors, title, LNM 2387, Springer 2026); the adjudication's ISBN pair and DOI (s14 referee §4 item 3) are confirmed on the copyright page.

**Text layer:** present and clean for prose. Formula-critical caveat: the text layer emits a stray period after almost every math fragment ("(M, F).", "φ .", "H.-orbits") and drops some Greek/Fraktur glyphs (κ, ε, ℓ, Σ, Ξ render as blanks: "= p̄ ∈ R×" for "κ = κ_p̄ ∈ R^×"). Prose searches work; formulas must be read from the page image. All formula-bearing quotations below were vision-checked (see §3.4).

**PDF page ↔ printed folio (published file).** Not a single offset — the PDF omits the blank verso before four chapter openings, so the offset shrinks by one at each of them:

| PDF pages | printed | rule |
|---|---|---|
| 1–10 | front matter: 1 series half-title, 2 LNM board, 3 series description, 4 title, 5 copyright, 6–7 Foreword (v–vi), 8 Abstract (vii), 9 Declarations (ix), 10 Contents (xi); pp. viii and x blank, omitted | — |
| 11–21 | 1–11 (Ch. 1) | printed = PDF − 10 |
| 22–108 | 13–99 (Ch. 2; p. 12 blank, omitted) | printed = PDF − 9 |
| 109–165 | 101–157 (Ch. 3–4; p. 100 omitted; p. 134→135 contiguous) | printed = PDF − 8 |
| 166–196 | 159–189 (Ch. 5–6; p. 158 omitted) | printed = PDF − 7 |
| 197–227 | 191–221 (Ch. 7 + References; p. 190 omitted) | printed = PDF − 6 |
| 228–231 | 223–226 … (Index; p. 222 omitted) | printed = PDF − 5 |
| 232–233 | LNM editorial policy, unnumbered | — |

Verified on the running heads of every page (script over `pdftotext` per page; the 222 numbered pages all obey the table).

**The two arXiv files (for the concordance).** `fetched-r3/r3s-17-…-arxiv-2402.06671v1-SESSION8-FETCH.pdf` (stamp "arXiv:2402.06671v1 [math.GT] 7 Feb 2024") and `fetched-r3/r3s-39-…-arxiv-2402.06671v2-SESSION16-FETCH.pdf` (stamp "arXiv:2402.06671v2 [math.GT] 13 Feb 2024"): 176 PDF pages each, AMS Memoirs style, printed = PDF − 6 uniformly (PDF 7 = printed 1 … PDF 173 = printed 167 = Index; blank versos are kept). **v1 and v2 have identical pagination, identical section/theorem/equation numbering, and identical wording apart from 20 diff hunks, all editorial** (listed in §3.5). Every "arXiv p. N" in the program's record is therefore the same page in v1 and v2, as the record already states.

## §2. What the program asked for (quoted from the flagged passages)

`results/c3-r/referee-s14/novelty-adjudication.md`, Cov-3 row: "ALKL, *A Trace Formula for Foliated Flows*, Springer LNM 2026, Introduction | UNDETERMINED | UNDETERMINED | **UNDETERMINED** (book page, chapter page, chapter PDF and front-matter PDF all behind the Springer login wall this session). Bears only on N4b's 'no published foliated formula' clause. | SPONSOR FETCH". Its §4 item 3: "Needed only to confirm that the published book, like arXiv:2402.06671v1/v2, still assumes simple closed orbits (N4b)."

`results/c3-r/s16/novelty/adjudication.md` §4 item 5: "**J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *A Trace Formula for Foliated Flows*, Lecture Notes in Math. 2387, Springer 2026** — the published memoir. All page numbers above are to **arXiv:2402.06671v1** and must be re-located before publication. Value: **LOW–MEDIUM** (standing, S14 Cov-3)."

`FETCH-LIST-ROUND4.md` item 9: "Every memoir page number in the record is to the arXiv version and must be re-located before any publication."

So two questions: (a) does the print still assume simple closed orbits (N4b)? (b) where does every memoir locator in the record land in the print?

## §3. The answer from the source

### §3.1 N4b — does the print still assume simple closed orbits? YES.

The source says (published text, page numbers are printed folios):

- **Abstract, p. vii:** "Let F be a transversely oriented foliation of codimension one on a closed manifold M, and let φ = {φ^t} be a foliated flow on (M, F). Assume the closed orbits of φ are simple and its preserved leaves are transversely simple. In this case, there are finitely many preserved leaves, which are compact."
- **§1.1, p. 1:** "Assume M is closed, codim F = 1, the closed orbits are simple, the preserved leaves are transversely simple, and φ is transverse to the non-preserved leaves. With these conditions, C. Deninger has conjectured that the supertrace of φ^* on H̄^•(F) makes sense as a distribution L_dis(φ) on R (its Lefschetz distribution), and it has an expression involving infinitesimal data from the preserved leaves and closed orbits (a dynamical Lefschetz trace formula)."
- **§1.3.1, p. 4** (vision-checked): "For every closed orbit c of φ, let ℓ(c) denote its smallest positive period. The condition on c to be simple means that id − φ_*^{kℓ(c)} : T_pF → T_pF is an isomorphism for any p ∈ c and k ∈ Z^×, whose determinant is independent of p, and its sign is denoted by ε_c(k). The integers ℓ(c) and ε_c(k) will be also ingredients of the trace formula."
- **§4.1.1, p. 136** (vision-checked): "The flow φ is called simple if all of its fixed points and closed orbits are simple. If moreover M is closed, then Fix(φ) is finite, and C_I(φ) are finite for all compact I ⊂ R. Therefore P(φ) is a discrete subset of R." (Immediately above, same page: "For every simple closed orbit c, there are neighborhoods, V of c in M and I of ℓ(c) in R, such that c is the only closed orbit in V whose first positive period is in I, and moreover that V ∩ Fix(φ) = ∅.")
- **Theorem 1.3.10, p. 11** (vision-checked): "Assume dim F is even. We can choose η and g on M^0 such that, using the preserved leaves L and the closed orbits c, we have  L_dis(φ) = Σ_L χ(L) W_L + ^bχ_{|ω^1|}(F^1) δ_0 + Σ_c ℓ(c) Σ_{k∈Z^×} ε_c(k) δ_{kℓ(c)}." Preceded on the same page by: "By Theorems 1.3.8 and 1.3.9, the trace formula conjectured by Deninger is satisfied:".

Plain-English reading: the published book keeps exactly the hypotheses of the arXiv versions — closed orbits simple (hence isolated, countably many, discrete period set), preserved leaves finitely many and compact — and its trace formula is a sum over isolated closed orbits weighted by ε_c(k) δ_{kℓ(c)}. Nothing in print admits a continuum of periodic orbits or a transverse measure on such a continuum. **The N4b premise ("every foliated-flow trace formula assumes simple closed orbits") stands for the print; Cov-3 can be closed as DETERMINED — confirmed.** I infer nothing beyond this; the book contains no remark about non-simple closed orbits or packets (a full-text search for "packet", "non-simple closed", "continuum of" returns nothing relevant).

### §3.2 Concordance: arXiv v1 = arXiv v2 → published

**Numbering is preserved in full.** Every section, subsection and sub-subsection number, every theorem-like item number (Theorem/Proposition/Corollary/Lemma/Remark/Example/Notation/Claim, numbered N.N.N within sections) and every displayed-equation label (N.N.N) of arXiv v1 exists with the same number and the same title/statement in the print; the print adds none and drops none (checked mechanically: 240 headings, 148 theorem-like items, 472 equation labels; the three v1-only "items" my scan produced — "Proposition 3.2.1", "Proposition 4.6.1", "Theorem 5.2.1" — are line-initial cross-references to other papers, not memoir items). **Only the page numbers change.** Chapter ranges in print: 1 pp. 1–11; 2 pp. 13–99; 3 pp. 101–133; 4 pp. 135–157; 5 pp. 159–176; 6 pp. 177–189; 7 pp. 191–216; References 217–221; Index 223–231.

**Sections the program cites** (arXiv printed page, identical in v1 and v2 → published printed page / PDF page):

| § | arXiv p. | print p. | PDF | title (print) |
|---|---|---|---|---|
| 1.1 | 1 | 1 | 11 | Deninger's Program |
| 1.2 | 2 | 2 | 12 | Case with No Preserved Leaves |
| 1.3 / 1.3.1 | 2 | 3 | 13 | General Case / Ingredients of the Trace Formula |
| 1.3.2 | 4 | 4 | 14 | Conormal and Dual-Conormal Leafwise Currents |
| 1.3.3 / 1.3.4 | 5 | 6 | 16 | Witten's Perturbed Complexes / Leafwise … |
| 1.3.5 | 5 | 7 | 17 | Main Results Leading to the Trace Formula |
| 1.3.6 | 7 | 9 | 19 | The Lefschetz Distribution |
| 1.4 | 8 | 11 | 21 | Short Guide |
| 2.1 / 2.1.1 | 9 | 13 | 22 | Section Spaces … / Topological Vector Spaces |
| 2.1.2 | 10 | 14 | 23 | Smooth Functions on Open Subsets of R^n |
| 2.1.4 | 11 | 15 | 24 | Smooth and Distributional Sections |
| 2.1.8 | 15 | 21 | 30 | Symbols |
| 2.1.13 | 19 | 26 | 35 | Topological Complexes |
| 2.2 | 20 | 28 | 37 | Conormal Distributions |
| 2.2.1 | 21 | 28 | 37 | Differential Operators Tangent to a Submanifold |
| 2.2.2 | 21 | 29 | 38 | Conormal Distributions when M Is Compact |
| 2.2.3 | 22 | 30 | 39 | Filtration of I(M,L) by the Symbol Order … |
| 2.2.4 | 23 | 31 | 40 | I(M,L) for Non-compact M |
| 2.2.9 | 25 | 34 | 43 | Push-Forward of Conormal Distributions |
| 2.3 | 25 | 35 | 44 | Dual-Conormal Distributions |
| 2.4.1 / 2.4.3 | 27 / 28 | 38 / 39 | 47 / 48 | Basic Notation / Uniform Spaces |
| 2.5.10 | 38 | 52 | 61 | Filtration of A(M) by Bounds |
| 2.5.15 | 39 | 54 | 63 | Partial Extension Maps |
| 2.6.1 | 48 | 66 | 75 | Cutting Along a Submanifold |
| 2.6.3 | 50 | 69 | 78 | The Spaces C^{±∞}(M,L) |
| 2.6.7 | 52 | 72 | 81 | The Space J(M,L) |
| 2.6.9 | 53 | 73 | 82 | I(M,L) vs Ȧ(M) and J(M,L) |
| 2.6.12 | 55 | 75 | 84 | The Conormal Sequence |
| 2.6.13 / 2.6.14 | 55 | 76 | 85 | Action of Diff(M) on … / Pull-Back Maps on … |
| 2.6.16 | 56 | 77 | 86 | Case where L Is Not Transversely Orientable |
| 2.7.1 | 56 | 78 | 87 | The Spaces K′(M,L) and J′(M,L) |
| 2.7.2 | 57 | 79 | 88 | Description of J′(M,L) |
| 2.7.4 / 2.7.5 | 58 | 80 | 89 | Dual-Conormal Sequence / Action of Diff(M) on … |
| 2.9.11 | 71 | 98 | 107 | Local Lefschetz Trace Formula for the Witten's … |
| 3.1 | 73 | 101 | 109 | Foliations |
| 3.1.4 | 75 | 104 | 112 | Holonomy Groupoid |
| 3.2.1 | 82 | 112 | 120 | The Leafwise Complex |
| 4.1 / 4.1.1 | 99 | 135 | 143 | Simple Foliated Flows / Simple Flows |
| 4.1.2 | 100 | 136 (runs to 137) | 144–145 | Transversely Simple Foliated Flows |
| 4.2.2 | 102 | 139 | 147 | Transversely Simple Flows on Suspension Foliations |
| 4.3.2 / 4.3.3 | 112 | 152 | 160 | Collar Neighborhoods of Every ∂M_l / Globalization |
| 4.3.4 | 114 (runs to 115) | 154 (runs to 155) | 162–163 | The Components of M^1 |
| 5.1 | 117 | 159 | 166 | Conormal Sequence of Leafwise Currents |
| 5.2.1 | 119 | 161 (runs to 162) | 168–169 | Injectivity of ĵ^* |
| 5.5 | 120 | 164 | 171 | Short Exact Sequence of Conormal Reduced Cohomology |
| 5.5.3 / 5.5.4 | 122 | 166 | 173 | The Equality ker R̄^* = im ῑ^* / Injectivity of ῑ^* |
| 5.6 | 123 | 167 | 174 | Computations in the Case of a Suspension Foliation |
| 6.1 | 131 | 177 | 184 | Dual-Conormal Sequence of Leafwise Differential Forms |
| 6.2 / 6.3 / 6.4 | 132 / 134 / 135 | 179 / 181 / 182 | 186 / 188 / 189 | Projective Limits … / Description of H^•K′(F) / Description of H̄^•J′(F) |
| 6.5 | 135 | 183 | 190 | Short Exact Sequence of Dual-Conormal Reduced Cohomology |
| 7.1 | 141 | 191 | 197 | Operators on a Suspension Foliation |
| 7.2 | 147 | 199 | 205 | Operators on the Components M^1_l |
| 7.3 | 153 | 207 | 213 | The Limit of ^bStr(P_u) as u ↓ 0 |
| 7.4 | 158 | 213 | 219 | The Limit of ^bStr(P_{μ,u}) as u ↑ +∞ and μ → ±∞ |

**Theorem-like items the program cites:**

| item | arXiv p. | print p. | PDF |
|---|---|---|---|
| Theorem 1.3.1 | 5 | 7 | 17 |
| Theorems 1.3.2, 1.3.3, 1.3.4 | 6 | 7 | 17 |
| Theorems 1.3.5–1.3.8 | 6 | 8 | 18 |
| Theorem 1.3.9 | 7 | 8 | 18 |
| Theorem 1.3.10 (the trace formula) | 8 | 11 | 21 |
| Proposition 2.1.1 / Remark 2.1.2 | 19 | 27 | 36 |
| Proposition 2.5.1 (proof "pp. 39–40" → print pp. 54–55) | 39 | 54 | 63 |
| Remarks 2.5.2–2.5.4, Proposition 2.5.5 | 40–41 | 55–56 | 64–65 |
| Corollary 2.6.4 | 55 | 76 | 85 |
| Proposition 2.9.6 | 71 | 99 | 108 |
| Remark 3.1.6 | 82 | 112 | 120 |
| Remark 4.1.1 | 101 | 138 | 146 |
| Proposition 4.3.1 | 114 | 154 | 162 |
| Remark 4.3.2 | 114 | 155 | 163 |
| Remark 5.2.1 | 119 | 162 | 169 |
| Remarks 5.5.3, 5.5.4 | 122 | 166 | 173 |
| Remark 6.1.1 | 131 | 177 | 184 |
| Remarks 6.5.1, 6.5.2 | 137 | 185 | 192 |
| Theorem 7.3.1 | 153 | 208 | 214 |
| Proposition 7.3.2 (proof "pp. 155–156" → print pp. 209–211) | 154 | 208 | 214 |
| Remark 7.3.3 | 158 | 213 | 219 |

(Not memoir items, though they sit next to memoir citations in the record: "Prop. 3.1.8", "Thm. 3.2.1", "Cor. 3.1.5" are Wengenroth [Wen03]; "Prop. 6.1.1" is [Mel96]; "Lemma 6.5.1/6.5.2", "Thm 6.3" are the program's own note; all two-level numbers such as "Cor. 4.5, Cor. 6.12, Prop. 8.8" are [ÁLKL23]/JPDOA.)

**Equation labels the program cites** (label unchanged; arXiv p. → print p.): (1.2.1)–(1.2.4) 2 → 2; (1.3.1), (1.3.2) 4 → 5; (1.3.3), (1.3.4) 5 → 6; (2.1.2) 10 → 14; (2.1.27) 15 → 21; (2.2.3) 21 → 29; (2.2.7) 22 → 31; (2.5.16) 35 → 48; (2.5.32) 37 → 51; (2.5.37) 38 → 52; (2.5.45), (2.5.46) 40 → 55; (2.6.1) 48 → 67; (2.6.2) 49 → 67; (2.6.6) 50 → 68; (2.6.13) 51 → 70; (2.6.38), (2.6.40) 54 → 75; (2.6.41) 55 → 75; (2.7.8) 58 → 80; (4.1.1) 100 → 137; (4.3.2) 115 → 155; (5.1.5) 118 → 161; (7.3.6) 155 → 210. (Note: equation labels move from the left margin in the arXiv AMS style to the right margin in print.)

**Where numbering changed:** nowhere. The only presentational changes are "Section 2.1.8" → "Sect. 2.1.8" in cross-references, "Chapter" → "Chap.", and the bibliography keys [ÁLKL23] → [ÁLKL24] (now the JPDOA article) and [Den22] → [Den26] (now Indag. Math. 37 (2026) 25–136); see §3.4.

### §3.3 Page-offset rule, with anchors

There is no constant offset. Published page ≈ **1.35 × arXiv page** (least-squares fit over 162 anchored pages: print = 1.3497·arXiv + 0.74, max residual 2.5 pages; the rounded rule "1.35 × arXiv" is within ±1 page on 125 of 162 pages and never off by more than 3). Per chapter the additive offset runs: Ch. 1 +0…+3; Ch. 2 +4 (p. 9) … +28 (p. 72); Ch. 3 +28…+36; Ch. 4 +36…+41; Ch. 5 +42…+47; Ch. 6 +46…+50; Ch. 7 +50…+57. **Use the table, not the rule, for anything that will be printed.**

Twelve anchors (arXiv printed page → print printed page), each checked on the running heads of both files and by the item's own text: §2.1.8 Symbols 15 → 21; §2.5.10 38 → 52; §2.6.7 52 → 72; Theorem 1.3.10 8 → 11; Prop. 2.5.1 39 → 54; §3.1 opening 73 → 101; §4.1.1 99 → 135; §4.1.2 100 → 136; §4.3.4 "Γ_l has finite rank" 114 → 154; Remark 4.3.2 / "t₀ = h_l(γ₀)" 115 → 155; §5.2.1 119 → 161; §5.5.3–5.5.4 122 → 166. Bonus anchors: (4.1.1) 100 → 137; Theorem 7.3.1 153 → 208; References 161 → 217; Index 167 → 223.

**Full page map** (arXiv printed page → print printed page where the arXiv page's opening text lands; each arXiv page spreads over ~1.35 print pages, so content near the foot of an arXiv page may sit on the next print page): 1→1 2→2 3→3 4→4 5→5 6→7 7→8 8→10 9→13 10→14 11→15 12→17 13→18 14→19 15→20 16→22 17→23 18→25 19→26 20→27 21→28 22→30 23→31 24→32 25→34 26→35 27→37 28→39 29→40 30→41 31→42 32→44 33→45 34→46 35→47 36→49 37→50 38→52 39→53 40→55 41→56 42→57 43→59 44→60 45→62 46→63 47→64 48→66 49→67 50→68 51→70 52→71 53→73 54→74 55→76 56→77 57→79 58→80 59→81 60→82 61→84 62→85 63→87 64→88 65→90 66→91 67→93 68→94 69→96 70→97 71→98 72→99 73→101 74→102 75→103 76→105 77→106 78→107 79→108 80→109 81→110 82→112 83→113 84→115 85→116 86→118 87→119 88→121 89→122 90→123 91→125 92→126 93→127 94→129 95→130 96→131 97→133 98→134 99→135 100→136 101→137 102→138 103→140 104→141 105→143 106→144 107→145 108→146 109→148 110→149 111→150 112→151 113→153 114→154 115→155 116→156 117→159 118→160 119→161 120→163 121→164 122→166 123→167 124→169 125→170 126→172 127→174 128→174 129→175 130→- 131→177 132→178 133→179 134→181 135→182 136→184 137→185 138→186 139→189 140→- 141→191 142→192 143→193 144→195 145→196 146→197 147→199 148→200 149→202 150→204 151→204 152→205 153→207 154→208 155→209 156→210 157→212 158→213 159→215 160→216 161→217 162→218 163→219 164→220 165→221 166→221 (arXiv 166 = last bibliography page, mapped by hand; arXiv 130 and 140 are blank versos; arXiv 128 and 150–151 share a print page because the print reflows there).

### §3.4 Wording of the statements the program quotes — arXiv vs print

Every memoir quotation in the record (169 quoted strings were pulled from results/, directions/ and BARRIER-ZOO.md; the 30 or so that are memoir text were located in both files by their prose words, and the formula-bearing ones were read from the page images of printed pp. 4, 11, 136, 154, 155) is **verbatim identical in print**, with these exceptions:

1. **§1.3.1, arXiv p. 3–4 → print p. 4.** arXiv: "…whose determinant is independent of p, and its sign denoted by ǫ_c(k)." Print: "…whose determinant is independent of p, and its sign **is** denoted by ε_c(k)." (One inserted word; the record's quotation "and its sign denoted by ε_c(k)" is the arXiv wording.)
2. **§4.1.2, arXiv p. 100 → print p. 136.** arXiv: "Consider the notation of Sections 3.1.2, 3.1.3 and 3.1.7, using the notation…" Print: "Consider the notation of Sects. 3.1.2 and 3.1.3, 3.1.7, using the notation…" (copy-editing artifact; no content change). The sentences the program relies on — "Moreover φ is transverse to the leaves on M^1. So there is a canonical isomorphism Nφ ≅ TF on M^1", "the leaves preserved by φ correspond to the H-orbits preserved by φ̄, which indeed form Fix(φ̄) because the H-orbits are totally disconnected", "Suppose φ is transversely simple unless otherwise stated. Then M^0 is a finite union of compact leaves because every fixed point of φ̄ is isolated" — are word-for-word the same on print pp. 136–137 (vision-checked).
3. **§4.3.4, arXiv pp. 114–115 → print pp. 154–155** (vision-checked): "The Fedida's description of F^1_l is given by a regular covering π_l : M̃^1_l → M^1_l with group of deck transformations Γ_l, a holonomy monomorphism h_l : Γ_l → R and a developing map D_l : M̃^1_l → R (Sects. 3.1.9 and 3.1.11). Note that Γ_l has finite rank because M^1_l ≡ M̊_l and M_l is compact." (p. 154); "Remark 4.3.2 In Proposition 4.3.1, the projection L_l → Γ_l\L_l may not be a covering map, and therefore (M^1_l, F^1_l) may not be given by a suspension. According to its proof, a point y ∈ L_l is fixed by some γ ∈ Γ_l \ {e} just when R × {y} projects to a closed orbit of ξ^t in M^1_l whose group of periods contains h_l(γ)." (p. 155); "Let c be a closed orbit of φ_l with period t_0, and let p = [x, y] ∈ c and p̃ = (x, y) ∈ M̃^1_l ≡ R × L_l. Then k = t_0/ℓ(c) ∈ Z and there is a unique γ_0 ∈ Γ_l such that φ̃_l^{t_0}(p̃) = γ_0 · p̃. Using (4.3.2) and Proposition 4.3.1 (iii), it easily follows that t_0 = h_l(γ_0) and φ̃_l^{t_0}(y) = γ_0 · y; i.e., y is a fixed point of the diffeomorphism T_{γ_0}^{-1} φ̃^{t_0}_{l,x} of L_l." (p. 155). Identical to arXiv apart from "Sections" → "Sects."; the s16 N-G quotations are exact.
4. **§2.1.8 (print p. 21), §2.5.10 (p. 52), §2.6.7 (p. 72)** — the three restatements of the [ÁLKL23] coincidence/retractivity assertions that the S14 note tracks — are printed **unchanged** (prose located on those pages; "The following properties hold [ÁLKL24, Corollaries 3.4–3.6 and Remark 3.8]" p. 21; "the topologies of A(M) and …" p. 52; "the topologies of J(M,L) and …" p. 73 — the §2.6.7 restatement sits on the page after the heading). Only the bracket key changed ([ÁLKL23] → [ÁLKL24]). So the note's sentence "the restatements … are presumably in print there" (`results/c3-r/s14/alkl23-derivations.tex` line 278) can be upgraded to "are in print at pp. 21, 52, 73".
5. **Abstract:** v1 lacks, v2 and print add the closing sentence; v2 "…about ten years ago by the three authors." → print "…about 10 years ago by the three authors." v1/v2 "the main one being the b-trace" (v1) / "the main one is the b-trace" (v2 = print).
6. **§1.1 citation string, p. 2:** arXiv "[DS02, Müm06, Kop06, Lei08, Kop11, Lei14, KP15, Kim17, Den22, Den23]" → print "[…, Kim17, Den26, Den23]", with [Den26] = "C. Deninger, Dynamical systems for arithmetic schemes, Indag. Math. (N.S.) 37 (2026), no. 1, 25–136" (arXiv had [Den22] = arXiv:1807.06400, 2022) and [ÁLKL24] = "The topology of the space of conormal distributions. J. Pseudo-Differ. Oper. Appl. 15–47, 1–68 (2024)" (sic — the article number 47 is typeset as a page range; arXiv had [ÁLKL23] = arXiv:2304.00798). The record's remark that "the authors' memoir cites the arXiv version" of [ÁLKL23] is true of the arXiv memoir only; the print cites the journal version.

Nothing else in the quoted set differs. I did **not** diff the whole book word by word (the print's text layer inserts a stray period after every math fragment, which defeats a mechanical diff); the check covers the quoted statements plus the section/theorem/equation inventories.

### §3.5 arXiv v1 → v2 (for the record: 20 diff hunks, all editorial)

Title stamp; Abstract (see §3.4 item 5) and "Received by the editor February 13, 2024" → "February 14, 2024"; "If moreover, Y is" → "If moreover Y is"; "(l and l′ being the ranks…)" → "are the ranks"; "L being a regular submanifold" → "and L were a regular submanifold"; four occurrences of "the second/first one being …" → "is …"; §3.1.2 "After considering a possible refinement" → "After considering a refinement if necessary"; "partial TF-connection" → "TF-partial connection"; "(3.2.2) induces decomposition" → "induces a decomposition"; "Like in Section 3.2.2, any choice" → "for any choice"; "Suppse" → "Suppose"; "If moreover, H is a submersion" → "If moreover H"; "on a normal foliated chart" → "on a foliated chart"; two layout-only hunks. No statement, number or page moves; the program's "v1 = v2 for every page cited" is correct.

### §3.6 Citation line and corrected bibliography entry

The file prints no "cite this book as" line; what it prints on every chapter-opening page is Springer's running citation: **"J. A. Álvarez López et al., *A Trace Formula for Foliated Flows*, Lecture Notes in Mathematics 2387, https://doi.org/10.1007/978-3-032-15413-2_N"** (N = chapter), with the copyright line "© The Author(s), under exclusive license to Springer Nature Switzerland AG 2026". Springer's standard book-citation form built from the copyright page (this form is Springer's house convention, not text in the file): "Álvarez López, J.A., Kordyukov, Y.A., Leichtnam, E.: A Trace Formula for Foliated Flows. Lecture Notes in Mathematics, vol. 2387. Springer, Cham (2026). https://doi.org/10.1007/978-3-032-15413-2".

Entry the program should use (replaces [ALKL24m] in `results/c3-r/s14/alkl23-derivations.tex` line 286 and the "[ÁLKL24" / "[ÁLKL26" keys elsewhere):

    J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *A Trace Formula for Foliated Flows*,
    Lecture Notes in Mathematics, vol. 2387, Springer Nature Switzerland, Cham, 2026,
    xi+231 pp. ISBN 978-3-032-15412-5; eBook ISBN 978-3-032-15413-2.
    https://doi.org/10.1007/978-3-032-15413-2. arXiv:2402.06671 (v1 7 Feb 2024, v2 13 Feb 2024).
    Section, theorem and equation numbers are the same in the arXiv versions and in print;
    page numbers cited as "arXiv p." are to the arXiv versions (identical in v1 and v2) and are
    re-located to the print by the concordance in results/fetch-r4/a06-memoir-pagemap.md §3.2–3.3.

Chapter-level DOIs, if a chapter is cited: 10.1007/978-3-032-15413-2_1 … _7. The existing [ALKL24m] entry's content is correct as far as it goes (LNM 2387, Springer, Cham, 2026, DOI); it lacks the ISBNs and page count, and its "Sections are cited by number; the page numbers given are those of the arXiv version" clause should now point at this concordance.

## §4. Other things in the source a future session should know exist

- Foreword by Christopher Deninger, pp. v–vi: "The work in this lecture note is an impressive extension of classical analysis to obtain for the first time non-transversal index theorems in a situation where both fixed points and also infinitely many periodic orbits are present." and "Speculatively, there is the fascinating possibility of a deeper relation between global analysis on certain spaces and number theory, where the explicit formulas would actually become a non-transversal index theorem in the sense of the authors." — Deninger's own printed framing of the memoir's reach; not in the arXiv versions.
- §1.1 p. 2, unchanged from arXiv: "It became clear that more generality is needed to draw arithmetic consequences (perhaps foliated flows on possibly singular foliated spaces of arithmetic nature)." — already quoted in the record (Q100/Q101), now citable to the print.
- References pp. 217–221 cite Candel–Conlon *Foliations I* [CC00] and *II* [CC03], Camacho–Lins Neto [CLN85], Hector–Hirsch (as [Hec72, Hec78] papers, not the book), Melrose [Mel93, Mel96], Komatsu [Kom67, "Theorem 6′"], Wengenroth as [Wen03] — the same authorities the program is fetching this round; the print's [Kom67, Theorem 6′] citation at p. 14 (§2.1.1) is the anchor for list item 10.
- Index pp. 223–231 exists in print (arXiv also has one, pp. 167–170); "simple" entries point at pp. 135–137.
- MSC line on the copyright page repeats 57R30 twice ("58J32, 57R30, 58A14, 35K05, 57R30, 35S05") — typographic, but copy it as printed if it is ever quoted.
- No acknowledgments section, no note added in proof, no erratum, no list of changes from the arXiv version anywhere in the file.

## §5. Caveats for corpus-routing.md

- r4-09: the text layer appends a stray "." after most math fragments and blanks Greek/Fraktur glyphs (κ, ε, ℓ, Σ, Ξ, 𝔛); prose grep works, formulas do not — render the page (pdftoppm -r 110) and read it.
- r4-09: PDF page ≠ printed page + constant; the blank verso before Chapters 2, 5, 7 and the Index is omitted, so printed = PDF − 10 (Ch. 1), − 9 (Ch. 2), − 8 (Ch. 3–4), − 7 (Ch. 5–6), − 6 (Ch. 7, References), − 5 (Index). Use the running head, never arithmetic.
- r4-09 vs r3s-17/r3s-39: all numbering (sections, theorem-like items, equations) is identical across arXiv v1, v2 and print; only pages differ (print ≈ 1.35 × arXiv). Cite by number and give the print page from the §3.2 tables.
- r3s-17 / r3s-39: printed = PDF − 6 throughout; v1 and v2 are page-identical and differ only in 20 editorial hunks (§3.5).
- Bibliography keys differ: arXiv [ÁLKL23] (arXiv:2304.00798) = print [ÁLKL24] (JPDOA 15:47); arXiv [Den22] (arXiv:1807.06400) = print [Den26] (Indag. Math. 37). Do not read a "[ÁLKL24, …]" citation inside the print as a self-citation of the memoir.

*Report complete. Scratch artifacts (per-page text dumps, concordance TSVs, page map, page renders) are in the session scratchpad and are reproducible from the three PDFs with pdftotext/pdftoppm.*

**Status: COMPLETE** (all five deliverables written; nothing outstanding). Not committed by this agent — the auto-commit watchdog / coordinator commits `results/fetch-r4/`.
