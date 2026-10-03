# INTEGRITY-DIFF — v2 of the Haglund-counterexample paper, and the letter (second-model check)

Status: IN PROGRESS. Verdict line will be written at the top of Part A when the checks are done.

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
