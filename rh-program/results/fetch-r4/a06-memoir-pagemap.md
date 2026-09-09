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

