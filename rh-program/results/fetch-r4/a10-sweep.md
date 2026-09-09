# a10-sweep — mechanical sweep of `fetched-r4/` (Session 18, 2026-09-09)

**Agent:** a10-sweep. **Method:** the Session-4.5 / Round-2 mechanical sweep re-run over every PDF under `fetched-r4/` (24 files, including `duplicates-of-r3/` and `not-on-list/`), with pypdf 6.16.2 and poppler (`pdfinfo`, `pdftotext`, `pdffonts`, `pdfimages`, `pdftoppm`): magic bytes; pypdf and pdfinfo page counts; PDF metadata; font count; text-layer health from nine sampled pages per file (three each at the start, middle and end: characters per page, alphabetic fraction, hit rate against `/usr/share/dict/words`, counts of Cyrillic / private-use / U+FFFD / `(cid:` glyphs), an intact-common-word test (the, and, class, compact, foliation, leaf, leaves, group, space, theorem, proof; feuille, feuilletage, groupe, espace, lemme, compacte) and a dropped-letter test (`lass`, `ompact`, `oliation`, `eaf`, `heorem`, `rst`/`nite` for lost fi-ligatures); SHA-256; size; first readable printed folio and the PDF-page ↔ printed-page offset, by text where a text layer exists and otherwise by rendering pages with `pdftoppm` and reading them myself; filename author token vs the file's first pages and metadata; page count vs the printed range in the filename; born-digital vs scan (image objects per page). **Zero third-party OCR.** Raw data, one record per file with all sample statistics: `results/fetch-r4/sweep-2026-09-09.json`.

The dictionary hit rate is an English dictionary, so it under-reads French texts (r4-02, r4-07); every 'garbled' verdict below was re-checked by reading the extracted text, and the French-only cases were reclassified. The r4-13b file was swept under its NEW name (renamed WRONG-FILE by another agent mid-session); r4-15b was renamed `…-SECOND-EDITION-CUP2006.pdf` by another agent after this sweep read it — same bytes, SHA-256 unchanged.

## 0. Headline findings

1. **24/24 files are valid PDFs** (magic bytes OK, pypdf opens all, pypdf and pdfinfo page counts agree on every file, no pypdf errors). Total 337,720,125 bytes (322 MiB): 21 files at the top level, 2 in `duplicates-of-r3/`, 1 in `not-on-list/`.
2. **One identity FAILURE: `r4-13b`.** The file is Proc. AMS **Vol. 30, No. 4 (December 1971)** — the issue cover plus the *Index to Volumes 21–30* (April 1969–December 1971), printed pp. 613–796, offset +612. Hájek's *Parallelizability revisited* (vol. 27, pp. 77–84, issue no. 1, January 1971) is **absent**; the only occurrence of Hájek in the 184 pages is the author-index entry "Hájek, Otomar — 1 Parallelizability revisted, 27 (1971), 77-85" (the index prints 77–85; the list says 77–84 — a one-page discrepancy the re-fetch should settle). Already renamed `r4-13b-WRONG-FILE-…-HAJEK-ABSENT.pdf`. Item 13's Hájek half is NOT delivered.
3. **Three citation/filename mismatches, none affecting identity of the mathematics:** (a) `r4-14` masthead prints **Math. Nachr. 186 (1997), 149–162** — the list's "185" is wrong, the filename is right; (b) `r4-15b` is the **second edition** (title page "Second Edition", Cambridge University Press; copyright page "© Mathematical Sciences Research Institute 2006", cambridge.org/9780521613057) — it matches the list's citation exactly, and the original filename's "FIRST-EDITION-1988" was wrong (since corrected to `…-SECOND-EDITION-CUP2006.pdf` by another agent); (c) `r4-15c` is the Vieweg **1986 second edition** of Hector–Hirsch Part A (copyright page: 1st edition 1981, 2nd edition 1986), the list cites 1981 — edition caveat only (Part B's preface says its second edition changed nothing beyond minor corrections; Part A's own preface was not checked for the equivalent sentence).
4. **Three files add nothing:** `r4-07` is byte-identical (SHA-256) to `fetched-r3/r3s-35`; `r4-08` is byte-identical to the Session-16 Wayback author copy in `results/c3-r/s16/qs4prime/`; the two `duplicates-of-r3/` files are byte-identical to r3s-32 and r3s-34. Items 7 and 8 (journal pagination of the Ghys and Leichtnam author copies) remain undelivered.
5. **Five image-only files must be read by vision** (no text layer at all): `r4-04`, `r4-06a`, `r4-11`, `r4-15a`, `r4-15a2`. Their folio offsets were established by rendering (below). **Three book scans drop blank versos**, so their PDF→folio offset drifts through the book (`r4-06a` −9→−1, `r4-15a` −8→+4, `r4-15a2` −8→+6) — for those three, **never compute a page by arithmetic; render the estimate, read the folio, adjust.** The published memoir `r4-09` does the same at every chapter opener (table in §2).
6. **Text layers that must not be quoted from** (search only, verify by vision): `r4-02` (JSTOR OCR loses inter-word spaces and accents and reads § as ?), `r4-15b` (born-digital, but the text layer DROPS fi/fl ligatures — "finite" comes out "nite", "first" as "rst" — and remaps math glyphs, so a text search for any word containing fi/fl will miss), `r4-14`, `r4-16b`, `r4-x1`, `r4-13a` (publisher OCR with letter substitutions), `r4-15c`/`r4-15c2` (CVISION OCR of a typewritten original: prose fine, math garbage). No Cyrillic or private-use glyphs anywhere; no `(cid:` residue; no U+FFFD.
7. **Git: `fetched-r4/` IS in `.gitignore` — but 19 of its PDFs are already TRACKED and PUSHED.** The repository's top level is `…/Math/riemann` (not `rh-program`); `riemann/.gitignore` line 9 reads `rh-program/fetched-r4/`, added in commit 2e28924 at 16:18:30 today. One minute earlier, the auto-commit watchdog's commit **b77e474 (16:17:35, "19 file(s) written by running agents")** added the 19 top-level PDFs then present to the index (10,764 insertions; the four later-arriving files — `duplicates-of-r3/`, `not-on-list/`, `r4-15a`, `r4-15a2` — show `!!` ignored). Both commits are on `origin/main` (github.com/x67ai/riemann-rh-program). `git status --porcelain` shows nothing under `fetched-r4/` precisely because the files are tracked and unchanged, not because they are ignored. **Copyrighted third-party PDFs are therefore in the public remote's history.** Fix (orchestrator's call, not done by this agent): `git rm -r --cached rh-program/fetched-r4 && git commit` removes them from the tree going forward; purging them from history needs a rewrite (`git filter-repo --path rh-program/fetched-r4 --invert-paths`) and a force-push, which is irreversible and is the sponsor's decision. The 19 tracked files are listed in `sweep-2026-09-09.json` → `summary.git`.

## 1. Per-file records (identity, pages, offset, text health)

Producer/creator from the PDF metadata; "scan+OCR" means one image object per page with a publisher-embedded text layer; offsets give printed folio as a function of PDF page.

### r4-01+12 — `r4-01+12-walczak-conlon-langevin-foliations-geometry-dynamics-warsaw2000-WS2002-VOLUME.pdf`
- **Size / pages / SHA-256:** 18,711,442 B; 462 pp (pdfinfo agrees); `595f451a1bc2a7e86677dd7803b9b9d765495b6eb7799583f32ce4c740e44b7d`
- **Metadata:** title='—'; author='—'; producer='iText 2.1.7 by 1T3XT'; creator='pdfsam-console (Ver. 2.3.0e)'; created="D:20100704030519+01'00'"
- **Source kind / fonts:** scan+OCR; 10 fonts
- **Text health:** clean (OCR layer). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.75, 3:1.0, 230:0.787, 231:0.815, 232:0.748, 460:0.565, 461:0.569, 462:0.0; damaged-form hits 0; fi-ligature intact/broken 9/0
- **Offset:** folio = pdf - 9, constant pdf 12..461 (folio 3..452); pdf 1-3 cover art, pdf 4 title page, pdf 5 copyright (WS 2002), TOC pdf 6-9
- **Identity:** OK (editors Walczak, Conlon, Langevin, Tsuboi on pdf 4)
- **Note:** Alvarez Lopez-Kordyukov 'Distributional Betti numbers' folio 159 = pdf 168; Cantwell-Conlon 'Endsets of exceptional leaves; a theorem of G. Duminy' folio 225 = pdf 234 (TOC text layer misreads 'Endests'/'Dummy')

### r4-02 — `r4-02-ghys-1995-topologie-des-feuilles-generiques-annals-141-387-422.pdf`
- **Size / pages / SHA-256:** 2,548,023 B; 37 pp (pdfinfo agrees); `28f4924cc1ad6f6f3dd8150477eb457d6a2ec41db0976a9ca0e7ae0665f10110`
- **Metadata:** title='Topologie des Feuilles Generiques'; author='—'; producer='iText 2.1.5 (by lowagie.com)'; creator='—'; created="D:20100513174600-04'00'"
- **Source kind / fonts:** scan+OCR; 6 fonts
- **Text health:** garbled (JSTOR OCR: inter-word spaces lost, accents stripped, section sign read as '?') - searchable, NOT quotable. Sample dictionary hit rates (page:rate): 1:0.618, 2:0.261, 3:0.202, 17:0.207, 18:0.201, 19:0.233, 35:0.242, 36:0.181, 37:0.381; damaged-form hits 6; fi-ligature intact/broken 2/0
- **Page count vs filename range 387–422:** expected 36 printed pages, file has 37 (delta +1 = one JSTOR/NUMDAM cover page)
- **Offset:** folio = pdf + 385 (pdf 2 = 387 ... pdf 37 = 422); pdf 1 = JSTOR cover
- **Identity:** OK - cover: Annals of Mathematics (2) 141 no. 2 (Mar. 1995) 387-422, JSTOR 2118526; exact match

### r4-03 — `r4-03-kopei-2011-foliated-arakelov-abh-hamburg-81-141-189.pdf`
- **Size / pages / SHA-256:** 1,448,680 B; 49 pp (pdfinfo agrees); `b5457ee10d80b53c595d3243dbef3a16b1d2fa05285e2376333aec9839fbff8f`
- **Metadata:** title='—'; author='—'; producer='Acrobat Distiller 9.4.5 (Windows)'; creator='VTeX PDF Tools'; created="D:20110922155704+03'00'"
- **Source kind / fonts:** born-digital (Springer); 18 fonts
- **Text health:** clean. Sample dictionary hit rates (page:rate): 1:0.588, 2:0.784, 3:0.885, 23:0.847, 24:0.912, 25:0.917, 47:0.85, 48:0.621, 49:0.615; damaged-form hits 0; fi-ligature intact/broken 8/0
- **Page count vs filename range 141–189:** expected 49 printed pages, file has 49 (delta +0)
- **Offset:** folio = pdf + 140 (pdf 1 = 141 ... pdf 49 = 189)
- **Identity:** OK - masthead Abh. Math. Semin. Univ. Hambg. (2011) 81:141-189, DOI 10.1007/s12188-011-0061-4; exact match

### r4-04 — `r4-04-contemp-math-387-2005-VOLUME-leichtnam-invitation-pp201-236.pdf`
- **Size / pages / SHA-256:** 41,718,775 B; 298 pp (pdfinfo agrees); `b6c9045687931b750c4c6074d074086ea159f753123f72fca558d4f02c3d342a`
- **Metadata:** title='—'; author='—'; producer='libtiff / tiff2pdf - 20201219'; creator='—'; created='D:20260909083352'
- **Source kind / fonts:** scan, no text layer; 0 fonts
- **Text health:** image-only (tiff2pdf scan, created 2026-09-09). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.0, 3:0.0, 148:0.0, 149:0.0, 150:0.0, 296:0.0, 297:0.0, 298:0.0; damaged-form hits 0; fi-ligature intact/broken 0/0
- **Offset:** Leichtnam article: folio = pdf - 19 (pdf 220 = 201 title page, pdf 255 = 236 references; pdf 211 = 192 Katz-Lescop); front: pdf 1 cover, 3 frontispiece, 5 copyright, 8 preface, 9 IMCP, 10-11 participants, 12 program; pdf 298 back cover
- **Identity:** OK by vision (pdf 220: 'An Invitation to Deninger's Work on Arithmetic Zeta Functions', Eric Leichtnam, Contemp. Math. 387, 2005, (c) 2005 E. Leichtnam)
- **Note:** READ VISUALLY

### r4-06a — `r4-06a-farber-2004-topology-of-closed-one-forms-SMM108.pdf`
- **Size / pages / SHA-256:** 21,829,240 B; 247 pp (pdfinfo agrees); `50b3a767bf76ad009eb885fe8b05b1024ebd849440bdad010b41d23cd856d326`
- **Metadata:** title='Topology of Closed One-Forms - M. Farber (AMS, 2003) WW.djvu'; author='John'; producer='Acrobat Distiller 10.0.1 (Windows)'; creator='PScript5.dll Version 5.2.2'; created="D:20110611135133-04'00'"
- **Source kind / fonts:** scan, no text layer; 0 fonts
- **Text health:** image-only (DjVu-derived scan, 2011). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.0, 3:0.0, 122:0.0, 123:0.0, 124:0.0, 245:0.0, 246:0.0, 247:0.0; damaged-form hits 0; fi-ligature intact/broken 0/0
- **Offset:** pdf 10 = folio 1 (offset -9), drifting to -1 by the end because blank versos were dropped: pdf 30=21, 60=52, 120=114, 180=176, 245=244, 246=245, 247=246 (last index page; book complete). Sec. 2.1 (folio 35 per Contents on pdf 3) is about pdf 43-44 - locate by vision
- **Identity:** OK by vision (pdf 1 title page: Topology of Closed One-Forms, Michael Farber, SMM 108, AMS)
- **Note:** READ VISUALLY; metadata title says 'AMS, 2003' - copyright year not checked (list says 2004)

### r4-07 — `r4-07-ghys-1999-laminations-par-surfaces-de-riemann-AUTHOR-COPY-again.pdf`
- **Size / pages / SHA-256:** 382,413 B; 50 pp (pdfinfo agrees); `777a0927c056523b96616207eece95305f4f0fb154569ec89767bd21f6193bcb`
- **Metadata:** title='lamination'; author='ghys'; producer='Acrobat Distiller 4.05 for Macintosh'; creator='Texturesª: AdobePS 8.6 (219)'; created='D:20010424144855'
- **Source kind / fonts:** born-digital; 21 fonts
- **Text health:** clean (French, TeX/Textures 2001). Sample dictionary hit rates (page:rate): 1:0.319, 2:0.25, 3:0.355, 24:0.291, 25:0.287, 26:0.273, 48:0.489, 49:0.549, 50:0.552; damaged-form hits 0; fi-ligature intact/broken 2/0
- **Offset:** folio = pdf (1..50) - author's own pagination, NOT the SMF 49-95 pagination
- **Identity:** OK - but SHA-256 identical to r3s-35 already on disk; adds nothing to item 7

### r4-08 — `r4-08-leichtnam-2008-analogy-arithmetic-geometry-foliated-spaces-RMA-copy-UNVERIFIED-edition.pdf`
- **Size / pages / SHA-256:** 291,460 B; 21 pp (pdfinfo agrees); `7fd56a359ae7832ec7974aedec504931f3dc4ae9eb1990249e42cb195f475e01`
- **Metadata:** title='—'; author='—'; producer='pdfeTeX-1.30.4'; creator='TeX'; created="D:20081127113433+01'00'"
- **Source kind / fonts:** born-digital (pdfeTeX 2008); 24 fonts
- **Text health:** clean. Sample dictionary hit rates (page:rate): 1:0.698, 2:0.8, 3:0.785, 9:0.884, 10:0.791, 11:0.8, 19:0.84, 20:0.573, 21:0.481; damaged-form hits 0; fi-ligature intact/broken 4/0
- **Page count vs filename range 163–188:** expected 26 printed pages, file has 21 (delta -5 = author copy, not the journal typesetting)
- **Offset:** folio = pdf (1..21) - author copy; journal 163-188 (26 pp) not derivable
- **Identity:** OK - SHA-256 identical to the s16 Wayback author copy (results/c3-r/s16/qs4prime/); adds nothing to item 8

### r4-09 — `r4-09-alvarez-lopez-kordyukov-leichtnam-trace-formula-foliated-flows-LNM2387-2026-PUBLISHED.pdf`
- **Size / pages / SHA-256:** 8,785,829 B; 233 pp (pdfinfo agrees); `1f4ef3ae43d5084edbe483b840a070297853334d8294b65b3a29a0efd19ce047`
- **Metadata:** title='A Trace Formula for FoliatedFlows'; author='—'; producer='Adobe PDF Library 10.0.1'; creator='—'; created="D:20260324210803+05'30'"
- **Source kind / fonts:** born-digital (Springer, Adobe PDF Library, 2026-03); 108 fonts
- **Text health:** clean. Sample dictionary hit rates (page:rate): 1:0.467, 2:0.492, 3:0.739, 115:0.799, 116:0.72, 117:0.822, 231:0.632, 232:0.782, 233:0.672; damaged-form hits 0; fi-ligature intact/broken 2/0
- **Offset:** front matter pdf 1-10 (pdf 4 title page); body offset steps by one at each chapter opener because the blank verso before each chapter is omitted - see report table
- **Identity:** OK (title page pdf 4: Alvarez Lopez, Kordyukov, Leichtnam; chapter DOIs 10.1007/978-3-032-15413-2_n)

### r4-10 — `r4-10-komatsu-1967-projective-injective-limits-jmsj-19-366-383.pdf`
- **Size / pages / SHA-256:** 2,220,066 B; 18 pp (pdfinfo agrees); `8141d7f8388e8b822974c0514a9ac89e1a195614dae39085b6ff0ae82976e17a`
- **Metadata:** title='—'; author='—'; producer='pdfTeX-1.40.3'; creator='LaTeX with hyperref package'; created="D:20091120135758+09'00'"
- **Source kind / fonts:** scan+OCR (Project Euclid); 2 fonts
- **Text health:** clean (OCR layer). Sample dictionary hit rates (page:rate): 1:0.643, 2:0.798, 3:0.835, 8:0.848, 9:0.792, 10:0.874, 16:0.799, 17:0.763, 18:0.496; damaged-form hits 0; fi-ligature intact/broken 1/0
- **Page count vs filename range 366–383:** expected 18 printed pages, file has 18 (delta +0)
- **Offset:** folio = pdf + 365 (pdf 1 = 366 ... pdf 18 = 383)
- **Identity:** OK - masthead J. Math. Soc. Japan Vol. 19 No. 3 1967, Komatsu; exact match

### r4-11 — `r4-11-wengenroth-1996-acyclic-inductive-spectra-studia-120-247-258-SCAN.pdf`
- **Size / pages / SHA-256:** 644,567 B; 7 pp (pdfinfo agrees); `121a3292e0e9c71cf964f48239a91c6c1577cdd53e73571c807e7c5f67c66011`
- **Metadata:** title='Acyclic inductive spectra of FrÃ©chet spaces'; author='J. WENGENROTH'; producer='FPDF 1.53'; creator='ICM'; created='D:20051111095600'
- **Source kind / fonts:** scan, no text layer; 0 fonts
- **Text health:** image-only (ICM/EuDML 2-up scan). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.0, 3:0.0, 4:0.0, 5:0.0, 6:0.0, 7:0.0; damaged-form hits 0; fi-ligature intact/broken 0/0
- **Page count vs filename range 247–258:** expected 12 printed pages, file has 7 (delta -5 — 2-up scan, see offset)
- **Offset:** two printed pages per PDF page: pdf p = printed 2p+244 (left) and 2p+245 (right); pdf 1 = 246|247 ... pdf 7 = 258|259; article 247-258 complete
- **Identity:** OK by vision (pdf 1 right: STUDIA MATHEMATICA 120 (3) (1996), 'Acyclic inductive spectra of Frechet spaces', JOCHEN WENGENROTH (Trier)); exact match
- **Note:** READ VISUALLY

### r4-13a — `r4-13a-antosiewicz-dugundji-1961-parallelizable-flows-annals-73-543-555.pdf`
- **Size / pages / SHA-256:** 1,083,737 B; 14 pp (pdfinfo agrees); `3e583360a7ea3ebbc0d46c60b3391d84814bc5988c23dff9c22c830752e9d8b0`
- **Metadata:** title="Parallelizable Flows and Lyapunov's Second Method"; author='—'; producer='Atypon Systems, Inc.'; creator='PDFplus'; created="D:20100510235515-04'00'"
- **Source kind / fonts:** scan+OCR; 7 fonts
- **Text health:** clean-ish (JSTOR OCR layer, usable). Sample dictionary hit rates (page:rate): 1:0.627, 2:0.566, 3:0.644, 6:0.778, 7:0.596, 8:0.789, 12:0.738, 13:0.826, 14:0.482; damaged-form hits 0; fi-ligature intact/broken 3/0
- **Page count vs filename range 543–555:** expected 13 printed pages, file has 14 (delta +1 = one JSTOR/NUMDAM cover page)
- **Offset:** folio = pdf + 541 (pdf 2 = 543 ... pdf 14 = 555); pdf 1 = JSTOR cover
- **Identity:** OK - cover: Annals (2) 73 no. 3 (May 1961) 543-555, authors listed 'J. Dugundji and H. A. Antosiewicz'; exact match

### r4-13b — `r4-13b-WRONG-FILE-proc-ams-30-4-dec-1971-cover-plus-index-vols-21-30-HAJEK-ABSENT.pdf`
- **Size / pages / SHA-256:** 37,858,548 B; 184 pp (pdfinfo agrees); `e1596efdb097fc872974c94fbc1b6f9ee9dffe030a3bc306dcc27945ac9b41e7`
- **Metadata:** title='—'; author='—'; producer='iTextSharp 4.1.6 by 1T3XT'; creator='—'; created="D:20100330151317+05'30'"
- **Source kind / fonts:** scan+OCR; 1 fonts
- **Text health:** clean (OCR layer). Sample dictionary hit rates (page:rate): 1:0.634, 2:0.801, 3:0.882, 91:0.672, 92:0.703, 93:0.669, 182:0.833, 183:0.725, 184:0.766; damaged-form hits 0; fi-ligature intact/broken 3/0
- **Offset:** folio = pdf + 612 (pdf 3 = 615 ... pdf 184 = 796); pdf 1-2 = issue cover/masthead
- **Identity:** FAIL - file is Proc. AMS Vol. 30 No. 4 (Dec. 1971): cover + INDEX TO VOLUMES 21-30, pp. 613-796. Hajek's paper is ABSENT; the only occurrence is the index entry 'Hajek, Otomar - 1 Parallelizability revisted, 27 (1971), 77-85' (index gives 77-85, list says 77-84)
- **Note:** already renamed WRONG-FILE by another agent; re-fetch Proc. AMS 27 no. 1 (Jan. 1971)

### r4-14 — `r4-14-mangino-1997-LF-spaces-tensor-products-math-nachr-185-149-162.pdf`
- **Size / pages / SHA-256:** 670,585 B; 14 pp (pdfinfo agrees); `6769919ca9ba0e68b6385e013f656f567dac46b3f643487ff1ff903fbdc25274`
- **Metadata:** title='(LF) - Spaces and Tensor Products'; author='—'; producer='PDFlib PLOP 2.0.0p6 (SunOS)/Acrobat 4.0 Import Plug-in for Windows'; creator='Acrobat 5.0 Paper Capture Plug-in for Windows'; created="D:20071211081601+05'30'"
- **Source kind / fonts:** scan+OCR; 10 fonts
- **Text health:** partial garble (Acrobat Paper Capture OCR: 'MANQINO', 'Fkeived'; math unreliable). Sample dictionary hit rates (page:rate): 1:0.661, 2:0.748, 3:0.772, 6:0.693, 7:0.82, 8:0.738, 12:0.714, 13:0.718, 14:0.48; damaged-form hits 0; fi-ligature intact/broken 3/0
- **Page count vs filename range 149–162:** expected 14 printed pages, file has 14 (delta +0)
- **Offset:** folio = pdf + 148 (pdf 1 = 149 ... pdf 14 = 162)
- **Identity:** OK - masthead prints 'Math. Nachr. 186 (1997), 149-162' -> the list's '185' is WRONG (filename is right)

### r4-15a — `r4-15a-candel-conlon-foliations-I-GSM23.pdf`
- **Size / pages / SHA-256:** 78,239,348 B; 398 pp (pdfinfo agrees); `2a1122a79e0aa02566dd97949860087eec1d9c14a53a89e40e82b0e0ce3d96ca`
- **Metadata:** title='—'; author='—'; producer='Foxit PhantomPDF Printer Version 6.0.3.0513'; creator='—'; created="D:20131020184853+03'00'"
- **Source kind / fonts:** scan, no text layer; 0 fonts
- **Text health:** image-only (Foxit print of a scan, 2013). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.0, 3:0.0, 198:0.0, 199:0.0, 200:0.0, 396:0.0, 397:0.0, 398:0.0; damaged-form hits 0; fi-ligature intact/broken 0/0
- **Offset:** pdf 1 title page (GSM 23), pdf 3 dedication, pdf 9 = xiv; body offset drifts -8 -> +4 (blank versos dropped): pdf 40=32, 80=73, 120=114, 160=158, 200=198, 240=241, 280=281, 320=322, 360=363, 390=393, 398=402 (last index page; body complete; part of the xiv front matter absent)
- **Identity:** OK by vision (pdf 1: Foliations I, Alberto Candel, Lawrence Conlon, GSM 23, AMS)
- **Note:** READ VISUALLY; locate folios by rendering, never by arithmetic

### r4-15a2 — `r4-15a2-candel-conlon-foliations-II-GSM60-BONUS.pdf`
- **Size / pages / SHA-256:** 100,535,749 B; 539 pp (pdfinfo agrees); `da2d9174d62e49b86556b1778d1f2293b0aa26130e9020a98febdc8286f7de14`
- **Metadata:** title='—'; author='—'; producer='Foxit PhantomPDF Printer Version 6.0.3.0513'; creator='—'; created="D:20131013203213+03'00'"
- **Source kind / fonts:** scan, no text layer; 0 fonts
- **Text health:** image-only (Foxit print of a scan, 2013). Sample dictionary hit rates (page:rate): 1:0.0, 2:0.0, 3:0.0, 268:0.0, 269:0.0, 270:0.0, 537:0.0, 538:0.0, 539:0.0; damaged-form hits 0; fi-ligature intact/broken 0/0
- **Offset:** pdf 1 title page (GSM 60), pdf 9 = xii, pdf 10 = xiii; body offset drifts -8 -> +6: pdf 60=52, 120=113, 240=237, 300=301, 360=363, 420=423, 480=485, 520=525, 535=541, 539=545 (last index page; body complete)
- **Identity:** OK by vision (pdf 1: Foliations II, Candel, Conlon, GSM 60, AMS)
- **Note:** READ VISUALLY; locate folios by rendering

### r4-15b — `r4-15b-moore-schochet-global-analysis-foliated-spaces-MSRI9-SECOND-EDITION-CUP2006.pdf` (swept under its original name `…-MSRI9-FIRST-EDITION-1988.pdf`; renamed by another agent mid-session; bytes unchanged)
- **Size / pages / SHA-256:** 1,440,658 B; 309 pp (pdfinfo agrees); `ede7758a0edeb8c52882a15cf43ce01b991ed15d38b74a9df24cbac2515748ad`
- **Metadata:** title='Global Analysis on Foliated Spaces, Second Edition'; author='Calvin C.Moore and Claude L.Schochet'; producer='dvipdfm 0.13.2c, Copyright © 1998, by Mark A. Wicks'; creator=' TeX output 2005.10.21:0957'; created="D:20051021095800-08'00'"
- **Source kind / fonts:** born-digital (dvipdfm, TeX output 2005-10-21; CUP eBook boilerplate); 30 fonts
- **Text health:** born-digital but text layer DROPS fi/fl ligatures ('finite'->'nite' 15x in 7 pages, 'first'->'rst') and remaps math glyphs (C*_r(G) -> 'Cr .G/ Š'); prose search on ligature words fails - quote by vision. Sample dictionary hit rates (page:rate): 1:0.0, 2:1.0, 3:0.836, 153:0.8, 154:0.799, 155:0.78, 307:0.674, 308:0.772, 309:0.672; damaged-form hits 0; fi-ligature intact/broken 0/7
- **Offset:** folio = pdf - 16, constant pdf 17..309 (folio 1..293); pdf 5 series half-title, 6 MSRI series list, 7 title page, 8 copyright
- **Identity:** OK - SECOND EDITION: title page pdf 7 'Global Analysis on Foliated Spaces, Second Edition, Calvin C. Moore, Claude L. Schochet, Cambridge University Press'; pdf 8 '(c) Mathematical Sciences Research Institute 2006', cambridge.org/9780521613057. Matches the list's citation; the original filename 'FIRST-EDITION-1988' was wrong and has since been corrected to '...-SECOND-EDITION-CUP2006.pdf' by another agent

### r4-15c — `r4-15c-hector-hirsch-geometry-of-foliations-part-A-1986-2nd-ed.pdf`
- **Size / pages / SHA-256:** 5,106,290 B; 246 pp (pdfinfo agrees); `5b799c6805f3b5611638ba21964bcdebba07afb4dc6bb453b3037d920229e75f`
- **Metadata:** title='—'; author='—'; producer='CVISION Technologies'; creator='PdfCompressor 3.1.34'; created="D:20120405002051+08'00'"
- **Source kind / fonts:** scan+OCR; 1061 fonts
- **Text health:** partial (CVISION OCR of a typewritten original: prose good, math garbage, 'Proof' -> 'PILoo6'). Sample dictionary hit rates (page:rate): 1:0.556, 2:0.681, 3:0.44, 122:0.815, 123:0.778, 124:0.701, 244:0.4, 245:0.596, 246:0.171; damaged-form hits 0; fi-ligature intact/broken 3/0
- **Offset:** folio = pdf - 11, pdf 13..234 (folio 2..223), folios printed as '- n -'; folio 224 absent = blank verso (223 ends the text, Literature starts on recto 225 = pdf 235); pdf 4 copyright, 5-6 preface
- **Identity:** OK - pdf 4: Hector/Hirsch, Introduction to the geometry of foliations, Pt. A, 2nd ed. 1986, Vieweg (1st ed. 1981), ISBN 978-3-528-18501-5. List cites the 1981 first edition: EDITION CAVEAT (Part B's preface says the 2nd ed. changed only minor corrections; Part A's own preface not checked)

### r4-15c2 — `r4-15c2-hector-hirsch-geometry-of-foliations-part-B-BONUS.pdf`
- **Size / pages / SHA-256:** 4,718,389 B; 308 pp (pdfinfo agrees); `fff20675f957d162b01744b2f19f7595248241cfb00a24f5c6e8a200136c8449`
- **Metadata:** title='978-3-528-18568-8_Book_PrintPDF.pdf'; author='ebernarte'; producer='CVISION Technologies'; creator='PdfCompressor 3.1.34'; created="D:20120510223647+08'00'"
- **Source kind / fonts:** scan+OCR; 996 fonts
- **Text health:** partial (same OCR quality as Part A). Sample dictionary hit rates (page:rate): 1:0.556, 2:0.553, 3:0.474, 153:0.675, 154:0.732, 155:0.883, 306:0.598, 307:0.786, 308:0.559; damaged-form hits 0; fi-ligature intact/broken 1/0
- **Offset:** folio = pdf - 10, pdf 12..307 (folio 2..297); pdf 4 copyright, 5-6 preface (Bonn, April 1987)
- **Identity:** OK - Pt. B, 2nd ed. 1987 (1st ed. 1983), Vieweg, ISBN 978-3-528-18568-8 (bonus, not on the list)

### r4-16a — `r4-16a-sullivan-1976-cycles-dynamical-study-foliated-manifolds-invent-36-225-255.pdf`
- **Size / pages / SHA-256:** 1,705,201 B; 31 pp (pdfinfo agrees); `11afa11df9bbba2406face707cf1b793c8a2728cb392c1cdf2332ec488ef3717`
- **Metadata:** title='Cycles for the dynamical study of foliated manifolds and complex manifolds'; author='—'; producer='PageGenie PDFGenerator'; creator='009124008.TIF'; created='Tue Feb 22 20:57:21 2005'
- **Source kind / fonts:** scan+OCR (PageGenie from TIFF); 130 fonts
- **Text health:** clean (OCR layer, good). Sample dictionary hit rates (page:rate): 1:0.747, 2:0.737, 3:0.754, 14:0.875, 15:0.882, 16:0.846, 29:0.778, 30:0.643, 31:0.667; damaged-form hits 1; fi-ligature intact/broken 3/0
- **Page count vs filename range 225–255:** expected 31 printed pages, file has 31 (delta +0)
- **Offset:** folio = pdf + 224 (pdf 1 = 225 ... pdf 31 = 255)
- **Identity:** OK - masthead Inventiones math. 36, 225-255 (1976); exact match

### r4-16b — `r4-16b-plante-1975-foliations-measure-preserving-holonomy-annals-102-327-361.pdf`
- **Size / pages / SHA-256:** 2,745,214 B; 36 pp (pdfinfo agrees); `2f92e8c1171170284248d0c9575659af0004f8184d1415640801f7545f4839dc`
- **Metadata:** title='Foliations With Measure Preserving Holonomy'; author='—'; producer='iText 2.1.5 (by lowagie.com)'; creator='—'; created="D:20100523025516-04'00'"
- **Source kind / fonts:** scan+OCR; 6 fonts
- **Text health:** partial (JSTOR OCR: spaces lost in places, refs run together). Sample dictionary hit rates (page:rate): 1:0.626, 2:0.545, 3:0.569, 17:0.695, 18:0.649, 19:0.602, 34:0.631, 35:0.5, 36:0.409; damaged-form hits 0; fi-ligature intact/broken 1/0
- **Page count vs filename range 327–361:** expected 35 printed pages, file has 36 (delta +1 = one JSTOR/NUMDAM cover page)
- **Offset:** folio = pdf + 325 (pdf 2 = 327 ... pdf 36 = 361); pdf 1 = JSTOR cover
- **Identity:** OK - cover: Annals (2) 102 no. 2 (Sep. 1975) 327-361, J. F. Plante; exact match

### r4-x1 — `r4-x1-edwards-millett-sullivan-1977-foliations-all-leaves-compact-topology-16-13-32-BONUS.pdf`
- **Size / pages / SHA-256:** 1,632,393 B; 20 pp (pdfinfo agrees); `9d7ca37be3ff77966bb335fa89dfe2a3170d0edae689237589667ef2e17afa36`
- **Metadata:** title='PII: 0040-9383(77)90028-3'; author='—'; producer='Acrobat 3.0 Import Plug-in\x00'; creator='捁潲慢⁴⸳‰慃瑰牵\u2065汐杵椭n'; created='D:20020715173509'
- **Source kind / fonts:** scan+OCR; 118 fonts
- **Text health:** partial (Acrobat Capture OCR: 'MILLETr', 'KEr~Ern', '[oliated' - names and math unreliable). Sample dictionary hit rates (page:rate): 1:0.86, 2:0.896, 3:0.84, 9:0.846, 10:0.833, 11:0.86, 18:0.877, 19:0.877, 20:0.63; damaged-form hits 0; fi-ligature intact/broken 16/0
- **Page count vs filename range 13–32:** expected 20 printed pages, file has 20 (delta +0)
- **Offset:** folio = pdf + 12 (pdf 1 = 13 ... pdf 20 = 32)
- **Identity:** OK - masthead Topology Vol. 16, pp. 13-32, Pergamon 1977; Edwards, Millett, Sullivan (Millett only by vision-quality reading of 'MILLETr'); exact match

### DUP-cantwell — `duplicates-of-r3/cantwell-conlon-1981-AIF-31-113-135-DUP-of-r3s-32.pdf`
- **Size / pages / SHA-256:** 1,819,405 B; 24 pp (pdfinfo agrees); `ae217300f425d8acf315dc2da0f374aa4b97ff58b98cc01608424debbdd29f9e`
- **Metadata:** title='Tischler fibrations of open foliated sets'; author='John Cantwell Lawrence Conlon'; producer='pdfTeX-1.40.16'; creator='NUMDAM'; created="D:20260116154722+01'00'"
- **Source kind / fonts:** scan+OCR; 12 fonts
- **Text health:** clean (NUMDAM OCR layer). Sample dictionary hit rates (page:rate): 1:0.195, 2:0.759, 3:0.812, 11:0.881, 12:0.913, 13:0.858, 22:0.852, 23:0.84, 24:0.585; damaged-form hits 0; fi-ligature intact/broken 3/0
- **Page count vs filename range 113–135:** expected 23 printed pages, file has 24 (delta +1 = one JSTOR/NUMDAM cover page)
- **Offset:** folio = pdf + 111 (pdf 2 = 113 ... pdf 24 = 135); pdf 1 NUMDAM cover
- **Identity:** SHA-256 identical to fetched-r3/r3s-32; AIF 31 no. 2 (1981) 113-135
- **Note:** ignore

### DUP-epstein — `duplicates-of-r3/epstein-1976-AIF-26-265-282-DUP-of-r3s-34.pdf`
- **Size / pages / SHA-256:** 1,459,009 B; 19 pp (pdfinfo agrees); `600bb91031dfb06094d0f6cb139b95c332b81628efa336f5bc578d6ef77a32cf`
- **Metadata:** title='Foliations with all leaves compact'; author='D. B. A. Epstein'; producer='pdfTeX-1.40.16'; creator='NUMDAM'; created="D:20241104122247+01'00'"
- **Source kind / fonts:** scan+OCR; 11 fonts
- **Text health:** clean (NUMDAM OCR layer). Sample dictionary hit rates (page:rate): 1:0.226, 2:0.779, 3:0.833, 8:0.869, 9:0.868, 10:0.862, 17:0.84, 18:0.628, 19:0.667; damaged-form hits 2; fi-ligature intact/broken 8/0
- **Page count vs filename range 265–282:** expected 18 printed pages, file has 19 (delta +1 = one JSTOR/NUMDAM cover page)
- **Offset:** folio = pdf + 263 (pdf 2 = 265 ... pdf 19 = 282); pdf 1 NUMDAM cover
- **Identity:** SHA-256 identical to fetched-r3/r3s-34; AIF 26 no. 1 (1976) 265-282
- **Note:** ignore

### NOT-blinovsky — `not-on-list/blinovsky-arxiv-1703.03827v16-math.GM-NOT-REQUESTED.pdf`
- **Size / pages / SHA-256:** 125,104 B; 12 pp (pdfinfo agrees); `ad4dd7072ba8ec03c79ab116e31cf4dfbe37e92a4a2a6474fada0254f09444f6`
- **Metadata:** title='Proof of Riemann hypothesis'; author='Vladimir Blinovsky'; producer='pikepdf 8.15.1'; creator='arXiv GenPDF (tex2pdf:8def8d8)'; created="D:20260811015635+00'00'"
- **Source kind / fonts:** born-digital (arXiv); 27 fonts
- **Text health:** clean. Sample dictionary hit rates (page:rate): 1:0.822, 2:0.773, 3:0.898, 5:0.816, 6:0.818, 7:0.846, 10:0.385, 11:0.821, 12:0.582; damaged-form hits 0; fi-ligature intact/broken 2/0
- **Offset:** folio = pdf
- **Identity:** not requested; arXiv 1703.03827v16 (math.GM), Blinovsky, 'Proof of Riemann hypothesis'
- **Note:** ignore

## 2. `r4-09` (LNM 2387) PDF-page ↔ folio table

Front matter pdf 1–10 (pdf 4 title page, pdf 5 addresses/copyright, pdf 9 declarations, pdf 10 contents); the blank verso before each chapter opener is omitted from the PDF, so the offset steps by +1 at each chapter; Springer LNM back matter at pdf 232–233. Each chapter carries DOI 10.1007/978-3-032-15413-2_n.

| PDF pages | Content | folio = pdf + | folios |
|---|---|---|---|
| 11–21 | Ch. 1 Introduction | −10 | 1–11 |
| 22–108 | Ch. 2 Analytic Tools | −9 | 13–99 |
| 109–142 | Ch. 3 Foliation Tools | −8 | 101–134 |
| 143–165 | Ch. 4 Foliations with Simple Foliated Flows | −8 | 135–157 |
| 166–183 | Ch. 5 Conormal Leafwise Reduced … | −7 | 159–176 |
| 184–196 | Ch. 6 Dual-Conormal Leafwise Reduced … | −7 | 177–189 |
| 197–222 | Ch. 7 Contribution from M¹ | −6 | 191–216 |
| 223–227 | References | −6 | 217–221 |
| 228–231 | Index | −5 | 223–226 |

(Chapter-opener folios are inferred from the neighbors — the opener page itself carries no running head; a06's memoir page map should confirm the two openers it relies on by vision.)

## 3. Housekeeping checks

- `.gitignore`: **present, but see §0 item 7** — the ignore line post-dates the commit that tracked 19 of the files. `git status --porcelain | grep fetched-r4` → 0 lines. `git status --ignored` lists only the 4 untracked items as ignored.
- File count 24; total 337,720,125 bytes (322 MiB). Largest: r4-15a2 (98 MB), r4-15a (76 MB), r4-04 (41 MB), r4-13b (37 MB), r4-06a (21 MB), r4-01+12 (18 MB).
- Tools: pypdf 6.16.2 (already installed), poppler 25.x from Homebrew. No OCR engine invoked.

## Summary

Paste-ready for `FETCH-RESPONSE-ROUND4.md`. Offset column: printed folio as a function of PDF page.

| id | title (short) | pages | text health | offset | identity OK? |
|---|---|---|---|---|---|
| r4-01+12 | Walczak–Conlon–Langevin–Tsuboi (eds), *Foliations: Geometry and Dynamics* (Warsaw 2000), WS 2002 — volume | 462 | scan+OCR, clean | pdf − 9 (whole body); ÁL–K art. folio 159 = pdf 168; Cantwell–Conlon art. folio 225 = pdf 234 | YES |
| r4-02 | Ghys, *Topologie des feuilles génériques*, Ann. Math. 141 (1995) 387–422 | 37 (JSTOR cover + 36) | JSTOR OCR — garbled; quote by vision | pdf + 385 | YES (exact) |
| r4-03 | Kopei, Abh. Hamburg 81 (2011) 141–189 | 49 | born-digital, clean | pdf + 140 | YES (exact) |
| r4-04 | Contemp. Math. 387 (2005) — volume; Leichtnam pp. 201–236 | 298 | IMAGE-ONLY | Leichtnam: pdf − 19 (pdf 220–255) | YES (vision) |
| r4-06a | Farber, *Topology of Closed One-Forms*, SMM 108 | 247 | IMAGE-ONLY | pdf 10 = 1, drifting −9→−1 (blank versos dropped); §2.1 ≈ pdf 43–44 | YES (vision) |
| r4-07 | Ghys 1999 — author copy | 50 | born-digital, clean | folio = pdf (author pagination) | YES — byte-identical to r3s-35; item 7 still open |
| r4-08 | Leichtnam RMA 2008 — author copy | 21 | born-digital, clean | folio = pdf (author pagination) | YES — byte-identical to s16 Wayback copy; item 8 still open |
| r4-09 | ÁLKL, *A Trace Formula for Foliated Flows*, LNM 2387 (2026) | 233 | born-digital, clean | per chapter, −10 → −5 (table §2) | YES |
| r4-10 | Komatsu, JMSJ 19 (1967) 366–383 | 18 | scan+OCR, clean | pdf + 365 | YES (exact) |
| r4-11 | Wengenroth, Studia 120 (1996) 247–258 | 7 (2-up) | IMAGE-ONLY | pdf p = printed 2p+244 ∣ 2p+245 | YES (vision, exact) |
| r4-13a | Antosiewicz–Dugundji, Ann. Math. 73 (1961) 543–555 | 14 (cover + 13) | JSTOR OCR, usable | pdf + 541 | YES (exact) |
| r4-13b | **WRONG FILE** — Proc. AMS 30 no. 4 (Dec 1971): cover + Index vols 21–30, pp. 613–796 | 184 | scan+OCR, clean | pdf + 612 | **NO — Hájek absent** |
| r4-14 | Mangino, Math. Nachr. **186** (1997) 149–162 | 14 | OCR, partial garble | pdf + 148 | YES (list's "185" wrong) |
| r4-15a | Candel–Conlon, *Foliations I*, GSM 23 | 398 | IMAGE-ONLY | pdf 9 = xiv; drifts −8→+4; pdf 398 = 402 | YES (vision) |
| r4-15a2 | Candel–Conlon, *Foliations II*, GSM 60 (bonus) | 539 | IMAGE-ONLY | pdf 9 = xii; drifts −8→+6; pdf 539 = 545 | YES (vision) |
| r4-15b | Moore–Schochet, *Global Analysis on Foliated Spaces*, **2nd ed.**, MSRI 9, CUP © 2006 | 309 | born-digital; fi/fl dropped in text layer — quote by vision | pdf − 16 (pdf 17 = 1) | YES (original filename "FIRST-EDITION-1988" wrong; since corrected) |
| r4-15c | Hector–Hirsch, Part A, Vieweg **2nd ed. 1986** | 246 | OCR, partial (math garbage) | pdf − 11; folio 224 absent (blank verso) | YES (list cites 1981 1st ed.) |
| r4-15c2 | Hector–Hirsch, Part B, Vieweg 2nd ed. 1987 (bonus) | 308 | OCR, partial | pdf − 10 | YES |
| r4-16a | Sullivan, Invent. 36 (1976) 225–255 | 31 | scan+OCR, clean | pdf + 224 | YES (exact) |
| r4-16b | Plante, Ann. Math. 102 (1975) 327–361 | 36 (cover + 35) | JSTOR OCR, partial | pdf + 325 | YES (exact) |
| r4-x1 | Edwards–Millett–Sullivan, Topology 16 (1977) 13–32 (bonus) | 20 | OCR, partial ("MILLETr") | pdf + 12 | YES (exact) |
| dup r3s-32 | Cantwell–Conlon, AIF 31 (1981) 113–135 | 24 | NUMDAM OCR, clean | pdf + 111 | = r3s-32 (SHA) |
| dup r3s-34 | Epstein, AIF 26 (1976) 265–282 | 19 | NUMDAM OCR, clean | pdf + 263 | = r3s-34 (SHA) |
| not-on-list | Blinovsky, arXiv 1703.03827v16 (math.GM) | 12 | born-digital | — | ignore |

**Read visually (no usable text layer):** r4-04 (CM 387, all 298 pp), r4-06a (Farber), r4-11 (Wengenroth, 2-up), r4-15a (Candel–Conlon I), r4-15a2 (Candel–Conlon II).

**Text layer present but garbled — search with it, quote only by vision:** r4-02 (Ghys 1995, JSTOR), r4-15b (Moore–Schochet: fi/fl ligatures dropped, math remapped), r4-14 (Mangino), r4-15c and r4-15c2 (Hector–Hirsch, math), r4-16b (Plante, JSTOR), r4-x1 (Edwards–Millett–Sullivan), r4-13a (JSTOR, mild).

**Mismatches to carry into the response:** r4-13b wrong issue (identity fail; Hájek not delivered; index says pp. 77–85); r4-14 volume 186 not 185; r4-15b original filename edition wrong (file is the correct 2nd ed.; filename since corrected); r4-15c 2nd ed. 1986 vs cited 1981; r4-07 and r4-08 duplicate files already on disk (items 7, 8 still open); 19 fetched-r4 PDFs tracked and pushed in git (§0 item 7).

**Status: COMPLETE** (2026-09-09; raw data `sweep-2026-09-09.json`, 24 records).
