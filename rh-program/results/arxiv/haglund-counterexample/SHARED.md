# SHARED.md — writer's log for `results/arxiv/haglund-counterexample/`

Dated blocks, newest last. Writer: Opus 5.5 (default effort), on `WRITER-BRIEF.md`.

## 2026-10-01 00:09 IST — start

- Read `WRITER-BRIEF.md`, `results/arxiv/README.md`, `check-submittable.sh`.
- TeX: the brief says TeX is not on PATH. It is not on PATH, but a user-level TeX Live 2026 is
  already installed at `~/texlive/2026/bin/universal-darwin` (pdfTeX 1.40.29), exactly as
  `results/arxiv/README.md` "Building" records, and `check-submittable.sh` prepends that directory
  itself. Verified: amsart, amsthm, hyperref, booktabs, mathtools, microtype, lmodern present.
  No install needed; build with `export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"`.
- Next: read the template, then the source files named in the brief.

## 2026-10-01 ~00:10 IST — template, footnote, sources located

- Template read (`a4-no-go/main.tex`: article 11pt, 1in margins, amsthm, booktabs, hyperref
  hidelinks, hand-written `thebibliography` with [AF26]-style keys, "Provenance, data and code"
  section with a "Data and code availability" paragraph and repository paths).
- AI footnote: the brief binds me to the README wording ("... working under the author's direction
  inside a structured research program; the author set the program's objectives, adjudicated its
  decisions, and is responsible for the content. Claude is a tool and is not an author."). NOTE for
  the orchestrator: the two POSTED papers carry a later variant from the 2026-08-30 second pass
  ("... working under the author's direction; the author set the objectives, made the technical and
  editorial decisions, and is responsible for the content."). I use the README wording verbatim, as
  instructed, plus the template's repository sentence; switching is a one-line edit.
- `verify-F/`: there is none inside `results/haglund-cert-s37/`. The orchestrator's verify-F for
  this result is `results/novel-wave-s36/staircase/verify-F/` (haglund_direct_arb.py,
  rerun_N27.py, rerun_N27.log; cited by staircase `read-F.md` §2). That is the folder I copy.
- Sources read so far: `haglund-cert-s37/NOTE.md`; staircase `read-F.md` (F1-F5); staircase
  `NOTE.md` §0-§4, §6, §7, §10 (F1, F2, F4, F5 are already applied in the NOTE text; F3 is the
  added paragraph under Proposition E).

## 2026-10-01 ~00:12 IST — both certificates read; hashes checked

- Read `producer-A/CERT.md` (all 194 lines) and `producer-B/CERT.md` (all 171 lines).
- CERT hashes on disk match the NOTE: A `b1ecfe0a...513f`, B `c4a8ca6b...87a3`.
- Producer A: every hash in its CERT §9 (5 logs, 6 scripts) matches the files on disk.
- Producer B: every hash in its SHARED.md final block (2026-09-30 23:37) matches EXCEPT
  `logs/ladder.log`: recorded `ee71d58d...c8a1`, on disk `c8d836f7...58f5` (mtime 23:48).
  Cause: `ladder.py` writes `logs/ladder.log` itself (line 15), so the orchestrator's re-run at
  23:48 overwrote B's log. The file on disk equals `rerun-F/B-ladder-rerun.log` except for a
  trailing "exit 0" line, and every value it prints matches B's CERT §C (R1 enclosures, R2 k = 1
  at 1e-3 and 1e-8 with E and lower moduli, R3 sum/2pi in [-1.2447e-5, 1.2447e-5], R2 model
  zero). Not a defect in the result; a provenance wrinkle. Handling: the archive ships the file as
  it is, and the certificate README says so explicitly. Flagged for the referee brief.

## 2026-10-01 ~00:15 IST — Haglund text, prior art, two citations read at the page

- Haglund arXiv:0910.5228v1 text on disk read: (1), (2)-(3), (6)-(14) pp. 1-3; "monotonic zeros"
  definition, Conjecture 1, Proposition 1 and proof pp. 3-4; Remark 1 and the table p. 4; (50)-(52)
  and the sentence "Thus the coefficient of 1/x2 in ΞN(x) is positive for k ≥ 3 and negative for
  1 ≤ k < 3." p. 10. Appendix (zeros of Ξ1) begins on p. 16 (page marker "15" precedes the
  heading "7 Appendix" in the text), so Producer A's "App. p. 15" is off by one; I cite p. 16.
- Writer's observation to be checked by the referee (not on disk as a claim): Haglund's (51) omits
  the factor 4 coming from G evaluated at z/2 in (14); his (52) values are one quarter of the
  NOTE's normalization (N = 1: NOTE -0.078997 vs his -.01974938206, ratio 4.0000). Signs are
  unaffected, so the erratum on the sign stands as the NOTE states it. The paper says only that
  his normalization differs by a factor 4, so the reader is not confused by the two numbers.
- Platt-Trudgian read at the page (arXiv abs page, 2026-10-01, saved `lit/`): title "The Riemann
  hypothesis is true up to 3·10^12"; abstract: "We verify numerically, in a rigorous way using
  interval arithmetic, that the Riemann hypothesis is true up to height 3·10^12. That is, all
  zeroes β + iγ of the Riemann zeta-function with 0 < γ ≤ 3·10^12 have β = 1/2." Crossref for
  DOI 10.1112/blms.12460: Bull. London Math. Soc. 53 (2021), no. 3, 792-797.
- Conjecture 4 (k = 1) result: Zenodo answered 403 directly; read through Firecrawl (2026-10-01,
  saved `lit/zenodo-22059236*`): title "Haglund's Zero-Trajectory Conjecture for the First
  Riemann Xi Approximant", author Mayk Loide Baccaro, citation_doi 10.5281/zenodo.22059236,
  published August 22, 2026, v1.0.0, preprint. Description quoted in the paper: "The result covers
  only the first interpolation." Condition of the brief met: it is cited.

## 2026-10-01 ~00:24 IST — main.tex: front matter, Section 1, Section 2 on disk

- `main.tex` so far: preamble (template class and packages), title, author with the README
  footnote, date October 1, 2026, abstract; Section 1 (Haglund's objects and exact quotes of the
  definition, Conjecture 1, Proposition 1, Remark 1, the "no rigorous error bounds" sentence;
  Theorem 1.1; scope with the Platt-Trudgian quote; mechanism and the two corrections; companion
  family; prior work: Haglund, Ahn (title page and p. 10 quote read on disk), Baccaro (Zenodo
  record), Lagarias-Montague p. 24 (exact words re-checked on disk), Ki p. 198, LMOZ Thm 1.7;
  organization); Section 2 (Riemann's identity, the family xi_w, Lemma 2.1 relating Phi_n and g_n
  with a proof re-typed from PRIOR-ART §0's derivation, the constants c_1..c_5 from the NOTE).
- Next: Section 3 (Theorems D, D', lobe law, odd count, tail coefficient).

## 2026-10-01 ~00:32 IST — Sections 3, 4, 5 on disk

- Section 3: Theorem 3.1 (NOTE Theorem D) with proof; Corollary 3.2 (lobe law); Theorem 3.3
  (NOTE Theorem D', F1 applied: +0.291 and +0.0395) with proof; Proposition 3.4 (tail) with the
  NOTE's five values; the p. 10 erratum; Corollary 3.5 (odd count, F5 applied: Xi_N(0) >=
  0.4971 - c_1 > 0) and the table erratum (31, largest 103.3679880094135, numerical census).
- Section 4: Theorem 4.1 (NOTE Theorem A, F2 applied: written with phi~_n = 2 x NOTE's phi_n, so
  the u -> -infinity coefficient carries -2*pi(2k+3)(-pi)^k/k!, i.e. twice the NOTE's; this is the
  F2-corrected statement in consistent notation - flagged for the referee); Theorem 4.2 (NOTE
  Theorem B) with the Hamburger/Nakamura/Burnol citations and the Knopp caveat as reported by
  Nakamura; Proposition 4.3 (NOTE Proposition F) in one statement plus one paragraph, with F3's
  two-regime argument for hypothesis (ii) summarized.
- Section 5: departure law (NOTE §3 departure lobes N = 1..7), lobe-scan tally (NOTE §4.1), the
  N = 27 lobes (0.411 / 1.325), labeled as floating-point and not part of the proof.
- Test build of the partial file: no TeX errors; overfull boxes fixed in displays.

## 2026-10-01 00:36 IST — timestamps corrected; Sections 6, 7, provenance, bibliography; archive copied

- Correction: the headers of the four previous blocks carried estimated times, two of them later
  than the real clock. They are now marked "~" and set from file modification times; from here
  on every header is read from `date`.
- `main.tex` complete: Section 6 (certificate A with Lemmas 6.1-6.3 re-typed from A's CERT §3;
  certificate B's bounds from B's CERT §B; Tables 1-3; cross-checks; the verify-F values; proof of
  Theorem 1.1), Section 7 (xi_24, both certificates' numbers), Provenance with the data and code
  availability statement (zip hash still a placeholder, filled after zipping), bibliography of 17
  entries (every entry's data read on disk or at the page: Crossref for Platt-Trudgian and Arb).
- Full build: no errors, no overfull boxes; 16 pages (target was 8-12; the proofs of Theorems
  D, D', A, B, the certificate lemmas and three tables account for the length).
- `certificate/` created by copying producer-A/, producer-B/, rerun-F/ (from haglund-cert-s37),
  verify-F/ (from the staircase folder), NOVELTY-F.md: 49 files, 3.6 MB.
- Next: reproduce both certificates in a scratch copy (not in certificate/, because B's scripts
  overwrite their own logs), then README.md, SHA256SUMS, the zip and its hash.
