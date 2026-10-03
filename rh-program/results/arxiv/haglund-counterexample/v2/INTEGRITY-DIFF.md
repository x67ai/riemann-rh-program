# INTEGRITY-DIFF — v2 of the Haglund-counterexample paper, and the letter (second-model check)

VERDICT (Part A, version 2 of the paper): CLEAN-WITH-CORRECTIONS — F1 and F2 before publishing, F3 recommended,
F6 at the next build, F4/F5 optional (details in A.3-A.5). Part B (the letter): see the section "Letter" below.

## Plan (second model, independent)
1. Read v2/VERIFY-BRIEF.md and follow it exactly.
2. A.1 Integrity diff: v2/main.tex against the published ../main.tex; classify every hunk.
3. A.2 Every new sentence about the three versions of Haglund's paper (web copy 2011-02-09,
   arXiv, journal) checked at the page against the texts on disk (paths from the brief).
4. A.3 Read the whole revised text for anything that still does not fit.
5. A.4 Look at the built PDF with pdftotext only (no rebuild, no check-submittable.sh).
6. Verdict line: CLEAN / CLEAN-WITH-CORRECTIONS / NOT CLEAN, with OLD/NEW pairs.
7. Part B "Letter": statements 1-10 judged by number only (TRUE AS WRITTEN / NEEDS A WORD /
   FALSE), each with file:line of support. Letter text is not copied into any file.
8. After each batch: dated block appended to rh-program/results/haglund-conj4/SHARED.md
   (stamps from rh-program/scripts/stamp.py only).


## Part A — version 2 of the paper

### A.1 Integrity diff (done 17:48 IST 2026-10-03)
- Own diff: `diff ../main.tex v2/main.tex` -> 14 hunks (47c47, 70,74c70,73, 175c174, 198c197,198,
  201,205c201, 207,209c203, 210a205,213, 273c276, 464,474c467,479, 495,496c500,501,
  498,499c503,505, 1036a1043,1045, 1037a1047,1048, 1089a1101,1106); 32 old lines, 49 new lines.
- It is byte-identical to the diff printed in v2/CHANGES.md (compared with `diff`: no output).
- SHA-256: ../main.tex 58ba455b…e474 (v1, published); v2/main.tex f4322378…db16.
- Every hunk falls in a span CHANGES.md lists: date line (47); abstract sentence (70-74);
  heading of §1.3 (175); §1.3 "corrects two statements"/"inconsistent"/printed conclusion
  (198, 201-209); credit paragraph (210a); §1.5 organization sentence (273); paragraph after
  Proposition tail (464-474); paragraph after Corollary odd (495-499); Acknowledgment (1036a,
  1037a); reference HagW (1089a).
- No theorem, proof, hypothesis, constant or formula of v1 is touched; the numbers that leave
  §1.3 (Haglund's 32, Haglund's printed 103.3679880094) were his, not the paper's; the paper's
  own 31 and 103.3679880094135 are kept (v2 lines 503-505).
- Record-only finding (CHANGES.md, not the paper): it says "82 changed lines"; the diff has 81
  marked lines (32 + 49).
  OLD: (82 changed lines)
  NEW: (81 changed lines: 32 removed, 49 added)

### A.2 The new sentences, at the page (17:50 IST 2026-10-03)
Texts: W = lit/haglund-rh8-penn.txt (+pdf), V = lit/haglund-0910.5228v1.txt, J = staircase/lit/
haglund-CEJM-2011-degruyter-fulltext.md (all read by me).
- v2 l.206-209 (W's table 1, 7, 15, 31, 53, 79, 113, 155, 207, 263, p. 4): W p.4 (text page 4) has
  exactly these; V p.4 and J's table have 32 at N = 4. TRUE.
- v2 l.209 quotation "approaches zero from below as $N \to \infty$", [HagW, p. 10]: W p.10, last
  sentence of the new paragraph, verbatim. TRUE.
- v2 l.210-212 "arXiv and journal versions have 32 ... 'positive for k >= 3 and negative for
  1 <= k < 3' [Hag, p. 10]; [HagW] corrects both": V p.10 verbatim ("Thus the coefficient of 1/x2
  in ΞN (x) is positive for k ≥ 3 and negative for 1 ≤ k < 3"); J has the same words (with x^-2
  for 1/x^2, outside the quoted span) and 32. W has 31 and the new sentence. TRUE of all three.
- v2 l.467 "to more digits in [HagW, (52)]": W (52) is on p.10 with 12-13 digit values. TRUE as far
  as it goes (W's digits also differ from V's from the 8th-10th significant digit; see A.3).
- v2 l.468-470 "his (51) applies his (50) at x": (50), (51) identical in V and W (only (47)'s
  x^-4 term differs, which (50) does not use). Quarter factor re-derived: (51) gives
  1/2(8X^3-30X^2+15X)e^-X, the paper 2(8X^3-30X^2+15X)e^-X. TRUE.
- v2 l.471-474 V/J conclusion vs W's "approaches zero from below": TRUE of the texts; but see A.3
  on "the later copy".
- v2 l.500-505 (W's ten entries odd; census 31 = W's entry; V and J print 32): TRUE.
- Date "February 9, 2011": W title page; server Last-Modified Wed, 09 Feb 2011 17:32:20 GMT
  (lit/haglund-rh8-penn.pdf.headers.txt); pdfinfo CreationDate Feb 9 2011. TRUE.
- Read date "(read October 3, 2026)": fetch header date Sat, 03 Oct 2026 10:41:53 GMT. TRUE.
- Address https://www2.math.upenn.edu/~jhaglund/preprints/rh8.pdf: Haglund home (www2) ->
  research.html -> href "preprints/rh8.pdf" (lit/penn-research.html l.189). TRUE.
- Title in [Hag11w] matches W's title page. SHA-256 of W = a8daaab8...88df as CHANGES.md says.
- Unchanged quotations still cited to V (pp. 2, 3, 3-4, 4): identical in W on the same pages
  (whitespace-normalized search). No conflict.

### A.3 What still does not fit (whole of v2 read once; L-lit §3 items 1-12 used as a test list)
Items 3, 6, 7, 8, 9 of L-lit §3 ((47), (53), (54), the M-curve paragraph, Hejhal) are not used
by v2 (grep). Item 11 is typography only. No sentence of v2 still calls anything a correction of
Haglund's paper ("inconsistent", "Two statements", "corrects two" all gone; the one remaining
"corrections", l.644, is the paper's P_N, Q_N). Findings:

**F1 (fix before publishing; factual).** v2 l.472 calls W "the later copy". W is dated
February 9, 2011; the journal version was published online 2011-02-18 and in print 2011-04-01
(staircase/lit/haglund-CEJM-2011-degruyter-fulltext.md: "Published Online:**2011-2-18",
"Published in Print:**2011-4-1"; received 12 July 2010, accepted 1 December 2010). The sentence
names "The arXiv and journal versions" just before, so "later" reads as later than both; by date
of publication it is not later than the journal.
OLD: $1 \le k < 3$'' \cite[p.~10]{Hag}; the later copy
NEW: $1 \le k < 3$'' \cite[p.~10]{Hag}; the author's web copy

**F2 (fix before publishing; consistency).** v2 l.1093-1094, entry [Hag09]: "Page and equation
numbers in this paper refer to this version." v2 now cites [HagW, p. 4], [HagW, p. 10] and
[HagW, (52)] (l.208, 209, 467, 474, 500), so the blanket sentence is no longer true as worded.
OLD: arXiv:0910.5228v1, 27 October 2009. Page and equation numbers in this paper
refer to this version.
NEW: arXiv:0910.5228v1, 27 October 2009. Page and equation numbers in this paper
refer to this version, except where \cite{HagW} is cited.

**F3 (recommended; residue of the correction framing, brief item 3(a)/(b)).** v2 l.475-477: "The
coefficients of Φ1, Φ2 and Φ3 nearly cancel, and ten-digit values of them cannot resolve their
sum, which is of order 10^-16, at N = 3." It now follows W's sentence, so it reads as a diagnosis
of an error W had already removed; and after "to more digits in [HagW, (52)]" (l.467) a reader may
think W's digits resolve the sum. They do not: W's printed values sum to -2.18e-15 (his
normalization), the true value is -6.96e-17 (my recomputation from (51) at 60 digits; L-lit
check_task3 has -7.0e-17); V's ten digits give +4.8e-10.
OLD: ten-digit values of them cannot resolve their sum, which is of order $10^{-16}$,
at $N = 3$.
NEW: their sum at $N = 3$, of order $10^{-16}$, is below the resolution of the printed
values of (52) in either copy.

**F4 (optional; v1 number, outside the integrity span).** v2 l.468 "(at N = 1, -.01974938206 against
-0.078997)": the paper's own value four lines up is -0.0789975 (l.462); 4 x 0.01974938206 =
0.07899752824, which rounds to 0.078998. Changing it adds a hunk to the diff; the orchestrator decides.
OLD: $-.01974938206$ against $-0.078997$),
NEW: $-.01974938206$ against $-0.0789975$),

**F5 (optional wording).** v2 l.474 "which is what Proposition tail shows for every N": W's sentence
is about N -> infinity; Prop. tail's limit -2 sum_{n>N}(8X^3-30X^2+15X)e^-X is negative for each N
and tends to 0 as the tail of a convergent series, so the claim holds, but the clause can say both.
OLD: which is what Proposition~\ref{prop:tail} shows for every $N$.
NEW: which is what Proposition~\ref{prop:tail} shows: the limit is negative for every $N$ and
tends to $0$.

### A.4 The built PDF (pdftotext and the PDF outline only; nothing rebuilt) (17:53 IST 2026-10-03)
- v2/main.pdf: 15 pp., CreationDate 2026-10-03 16:59:38 IST, SHA-256 a95e6c3f…be40.
- Every new sentence is present in the text layer (date line, abstract sentence, heading "1.4 The
  mechanism", the credit paragraph, l.467-474 paragraph, l.500-505 paragraph, Acknowledgment,
  entry [Hag11w] with the URL and "(read October 3, 2026)"). "inconsistent" and "Two statements"
  absent. No "??" in the page text.
- **F6 (fix when the PDF is next built; present in the published v1 PDF too).** The PDF outline
  (bookmarks, read with PyMuPDF get_toc) has the entry "Proof of Theorem ??" in v2 and in v1;
  v2/main.log l.415-416 "Rerun to get outlines right". v2/main.out already holds "Proof of Theorem
  1.1", so one more pdflatex pass fixes it; a run-independent fix:
  OLD: \subsection{Proof of Theorem~\ref{thm:main}}
  NEW: \subsection{Proof of Theorem~\texorpdfstring{\ref{thm:main}}{1.1}}
- v2/abstract.txt equals the abstract of v2/main.tex word for word; it states the odd count and the
  negative limit as results, as the body does (Cor. odd, Prop. tail).

### A.5 Record-only (not the paper)
- **F7.** CHANGES.md (and LOG 16:23) call the mechanism subsection "§1.3" and the organization
  paragraph "§1.5"; in the paper they are §1.4 and §1.7 (§1.3 is "Scope"). The paper itself uses
  \ref throughout and is unaffected; the brief's "Section 1.3" means §1.4.
  OLD: in the heading of §1.3, "the two corrections" in §1.5
  NEW: in the heading of §1.4, "the two corrections" in §1.7
- **F8.** CHANGES.md "82 changed lines": 81 (see A.1).

### Verdict (Part A)
**CLEAN-WITH-CORRECTIONS.** Integrity: CLEAN (diff identical to CHANGES.md, all hunks in listed
spans, no mathematics or v1 number altered). Every new statement about W, V and J is true at the page.
Before publishing: F1 ("the later copy": the journal appeared online nine days after W's date) and
F2 (the [Hag09] note on page numbers); F3 recommended; F6 at the next build; F4, F5 optional.
