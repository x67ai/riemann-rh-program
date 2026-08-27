# CIRCULATION-PREP — register for the arXiv-preparation work

Task: novelty re-check + arXiv-submittable PDFs for the four circulation-ready documents, at the
sponsor's request (2026-08-27). **Each step below is standalone**: it names its status, inputs,
and acceptance test, so a fresh session (any model) can pick up at any step boundary. Update the
STATUS line of a step when you finish it, and commit per unit. Program setup and working loop:
`KICKSTART.md`; live register `STATUS.md` (Session-9 queue); history `LOG.md`.

## The four documents

All refereed, zero fatal findings, prior-art gates passed. Paths relative to `anthropic/rh-program/`.

| # | Document | Path | Referee record |
|---|---|---|---|
| 1 | A4 no-go paper — "The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control" | `results/a4-no-go/paper.md` (+ `theorems.md`, `pair-channel.md`, `data-tables.md` companions) | `referee-1.md`, `referee-2.md` |
| 2 | C3-r m0 axiom note — "The polarized-Frobenius axiom class" | `results/c3-r/m0-axiom-note.md` | `referee-m0.md` |
| 3 | C3-r m1 non-circularity note — "Castelnuovo–Severi/Hodge index from RR + ampleness" | `results/c3-r/m1-noncircularity.md` | `referee-m1.md` |
| 4 | C3-r seed no-go note — "Products of the per-prime Tate curves carry no correspondence calculus" (zoo IV.10) | `results/c3-r/seed-no-go-note.md` | `referee-seed-no-go.md` |

## STEP 1a — fill the O1/N128 report template slots

**STATUS: DONE (2026-08-27).** All 39 `{{...}}` occurrences in `results/a4-no-go/o1-n128-report.md`
filled from `verify/o1_crowding_interval_out.json` with direction-safe rounding (upper bounds up,
lower bounds down): C* = 0.9846470880 (short 0.98465), margin 0.0153529; binding box
(31/200, 39/250] = (0.155, 0.156] equal-depth corner; Sgen2 lower bounds 1.001823 / 1.014053 /
1.015279 at d = 0.158/0.159/0.1591 (short L159 = 1.01405); C13 <= 0.304542 (short 0.30455),
2C13 = 0.60910, Phi0 >= 0.643710 (short 0.64371), S13 <= 0.704577 (short 0.70458); elapsed 3209 s.
Acceptance: `grep -c '{{' o1-n128-report.md` returns 0. VERIFIED.

## STEP 1b — apply the dated revision to the paper package

**STATUS: DONE (2026-08-27).** The complete 16-edit quote→replacement list of
`o1-n128-report.md` section 5 applied: 9 edits + 1 append in `pair-channel.md`, 6 edits + 1
residue-list insertion in `paper.md`, 1 edit in `directions/A4-lindelof-lock.md` (its wording
uses Unicode ≤ — matched in situ). Every "current" string matched its file exactly once before
replacement (dry-run verified). Dated-revision blocks added at the top of `paper.md` and
`pair-channel.md`. Three leftovers beyond the report's list fixed: the paper.md line-743 referee
changelog entry annotated (history kept, pointer added); two stale Phi_0 = 0.6665 floats in
pair-channel.md (Section 6 comparison + Section 10 key-constants line) replaced with
0.6675 float / 0.64371 certified. `theorems.md` untouched (per the report: atom-only model
theorem, Remark 2.6 caveat stands); referee reports and `data-tables.md` untouched (dated
records). Acceptance: no `w <= 1 modulo`-style claim outside historical/annotated context;
remaining `0.9775` mentions only as the historical grid value. VERIFIED (sweep clean).

## STEP 1c — referee-check the revision wording

**STATUS: IN PROGRESS (2026-08-27, workflow wf_029660e9-d56, 2 referee agents; if this session
died mid-run, treat as TODO and re-run).** Adversarial wording check of the revised package: every revised sentence in
`paper.md`/`pair-channel.md` must (a) match the certificates in
`verify/o1_crowding_interval_out.json` + `verify/n128_rerun_out.json` + `o1-n128-report.md`
(numbers, inequality directions, rounding direction), (b) claim nothing on w in (0.98, 1] beyond
attacks + backstop, (c) keep Theorem/Section cross-references consistent (Theorem 4.7, B(i)/B(ii),
Sections 4.2–4.3, 8.3, 9, 10). Also verify the dated-revision blocks read correctly against the
report. Record the pass as `results/a4-no-go/referee-revision.md` (verdict + any repairs applied).

## STEP 2 — independent novelty check (all four documents)

**STATUS: IN PROGRESS (2026-08-27, workflow wf_4501be8c-d24, 4 hunters + 1 reference verifier;
if this session died mid-run, treat as TODO and re-run).** Start from the homework on disk: `results/c3-r/prior-art-r7a.md` (extended
R7(a) gate, verdict NOVEL-WITH-CITATIONS, 7 obligations — covers the three C3-r notes) and the
A4 prior-art gate recorded in `LOG.md` Session 7. Verify independently with a fresh literature
sweep (arXiv, MathSciNet-visible metadata, Semantic Scholar) per document: does any prior work
anticipate the main claim? Network note: arxiv.org/github.com were once unreachable directly and
fetched via a GCS mirror; retry loops per `~/.claude/CLAUDE.md`. Deliverable:
`results/arxiv/novelty-check.md` — per document: verdict (novel / novel-with-citations /
anticipated-by), citations to add, and the searches run.

## STEP 3 — LaTeX conversion + arXiv-submittable PDFs

**STATUS: IN PROGRESS for the three C3-r notes (2026-08-27, workflow wf_6fb7779d-f10, one
converter per note, output under results/arxiv/); the A4 paper conversion WAITS for step 1c's
verdict, then runs with the same rules. If this session died mid-run: check results/arxiv/ for
committed main.tex/main.pdf per note; anything missing is TODO.** TeX Live 2026 is installed and verified working:
`export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"` (pdflatex 1.40.29; `tlmgr`
available; the "no TeX on this machine" notes in STATUS.md/LOG.md are stale — install nothing).
One subdirectory per paper under `results/arxiv/` (`a4-no-go/`, `m0-axiom/`, `m1-noncirc/`,
`seed-no-go/`), each self-contained: `main.tex` (+ `refs.bib` if used), compiled PDF committed
alongside. Source of truth is the markdown; convert faithfully (amsart or article + amsmath/
amssymb/amsthm; theorem environments; ASCII math in the sources becomes proper LaTeX). The A4
paper converts `paper.md` ONLY (the companions stay internal; where the paper cites them, cite
as supplementary material with the repo filename). Include the dated-revision note as a titlepage
footnote or frontmatter remark. U.S. English throughout. Acceptance per paper: pdflatex runs
clean (no undefined references, no overfull-box storms), PDF opens, statement numbers match the
markdown.

## Not circulation-ready — do NOT include

`results/c3-r/m2c-feasibility-ledger.md` (OPEN-WITH-LEDGER), `probe-9.3-a.md`, `probe-9.3-b.md`,
`probe-9.4-note.md`, `s2-feasibility-note.md` (referee debts owed — Session-9 queue item 3), and
everything under `results/d1-*`/Lean (infrastructure, not papers).

## Housekeeping

Per `~/.claude/CLAUDE.md`: `caffeinate` + push watchdog at session top; commit small and often;
push with a retry loop. When all steps are DONE: mark Session-9 queue items 1b + 2 done in
STATUS.md, add a LOG.md entry, and leave the circulation decision itself to the sponsor
(Session-9 item 5).
