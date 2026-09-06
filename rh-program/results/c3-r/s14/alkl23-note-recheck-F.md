# alkl23-note recheck F (Fable 5.1), Session 16, 2026-09-06

Status: IN PROGRESS (this file is written as the pass proceeds; if it ends abruptly the pass died mid-way).

Document under test: results/c3-r/s14/alkl23-note.tex (mtime 2026-09-05 22:47), alkl23-note.pdf (3 pp.).

## 0. Verdict

(to be written last)

## 1. Findings

(numbered as found)

## 2. Citation table

(filled as checked)

## 3. Witness re-derivations

(filled as done)

## 4. Not checked


### Progress log (written as the pass proceeds)

- 10:2x Read .tex and `pdftotext -layout` of the shipped PDF. Scratch rebuild (pdflatex x2, TeX Live 2026): text identical to the shipped PDF; log has NO Overfull/Underfull/LaTeX-warning lines.
- Published PDF: PDF page index = printed journal page ("Page N of 68"), so every "p. N" in the note maps directly. Pages 4, 5, 15-18, 20-23, 36-42, 47-49, 55-62, 64 read from the text layer.
- All statement numbers and pages cited for [1] found where the note says (table in Sec. 2 below). Quotation "By Corollary 6.14, there is some 0-neighborhood V ... = W ∩ A^m(M)" matches pp. 48-49 verbatim. Quotation "Hence S'^m(U x R^l) is complete" matches p. 17. The identity "‖φ(a)‖' = ‖a‖' < ∞" is at the top of p. 17 (text layer drops the primes; image check pending).
- Memoir 2402.06671v1 (on disk): printed p. 15 = pdf p. 21 = §2.1.8, restates [ÁLKL23, Cors. 3.4-3.6 and Remark 3.8] for "any open U ⊂ R^n" (verbatim: "S^∞(U×R^l) is an acyclic Montel space, and therefore complete, boundedly/compactly/sequentially retractive and reflexive"). §5.2.1 = printed p. 119 (pdf 125): "I(F) is compactly retractive (Section 2.2.2)". §5.5.3 = printed p. 122 (pdf 128): "J(F) is compactly retractive (Section 2.6.7)"; §5.5.4 same page: "Since I(F) is compactly retractive". §5.1 (pdf 123): "closed manifold M"; I(F) = I_{Λ•}(F) := I(M, M^0; ΛF). All memoir sentences in the note CONFIRMED (pages are printed pages; consistent).
- ONLINE recheck 2026-09-06: arxiv.org/abs/2304.00798 lists v1 (3 Apr 2023), v2 (29 Jul 2023), v3 (1 Jun 2024) only, comments "55 pages". Crossref 10.1007/s11868-024-00617-y: relation {} empty, no update-to/updated-by, is-referenced-by-count 0. Semantic Scholar arXiv:2304.00798: citationCount 0. => §5 sentences still true today.
- ONLINE: arxiv.org/abs/2402.06671 has a **v2 (13 Feb 2024)**; the note cites v1 only (FINDING, see Sec. 1).
- v1 vs published, §§3-4, word-level diff: statement numbers and equations (3.1)-(3.5), (4.8)-(4.10) unchanged, BUT text is not: Remark 3.7 cross-ref "Proposition 6.8" -> "6.10"; §4.2.2 "Fréchet space I_c^(∞)" -> "LCHS"; §4.3.3 reworded; §§4.6-4.7 equations (4.21)-(4.24) collapsed to (4.21)-(4.22); §4.8 rewritten; cross-refs into §2 shifted by one. => "§§3-4 are unchanged in all arXiv versions" is an overclaim (FINDING).
- v2 and v3 PDFs downloaded to scratchpad (55 pp. each) for the numbering check (pending below).
