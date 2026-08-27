# CIRCULATION-PREP — brief for the arXiv-preparation session

Written 2026-08-27 at the sponsor's request (novelty re-check + arXiv-submittable PDFs for the
circulation-ready documents). This file is the task spec; the program's setup and working loop are
in `KICKSTART.md`, the live register is `STATUS.md` (Session-9 queue), history in `LOG.md`.

## The four circulation-ready documents

All four are refereed with zero fatal findings and passed their prior-art gates. Paths are
relative to `anthropic/rh-program/`.

1. **A4 no-go paper** — *"The two-moment certificate is robust under Rudnick–Sarnak-range cubic
   augmentation with capacity control"* — `results/a4-no-go/paper.md` (~123KB), with companions
   `theorems.md`, `pair-channel.md`, `data-tables.md`. Dual-refereed (`referee-1.md`,
   `referee-2.md`, zero fatals); prior-art clean (Session-7 LOG entry).
   **GATE: apply the dated revision BEFORE any external use** — see below.
2. **C3-r m0 axiom note** — *"The polarized-Frobenius axiom class: an S1 axiom statement with
   DH/Epstein witnesses (not a theorem)"* — `results/c3-r/m0-axiom-note.md`. Refereed
   (`referee-m0.md`), pass-with-repairs, zero fatals, all repairs executed. Ready as-is.
3. **C3-r m1 non-circularity note** — *"Castelnuovo–Severi/Hodge index on a surface from
   Riemann–Roch + ampleness: the non-circularity re-derivation"* —
   `results/c3-r/m1-noncircularity.md`. Refereed (`referee-m1.md`), zero fatals, repairs
   executed (incl. Nakai–Moishezon addition IN7). Ready as-is.
4. **C3-r seed no-go note** — *"Products of the per-prime Tate curves of absolute geometry carry
   no correspondence calculus for the Weil explicit formula"* (barrier-zoo IV.10, publishable
   form) — `results/c3-r/seed-no-go-note.md`. Refereed (`referee-seed-no-go.md`), repaired and
   STRENGTHENED: End(E_p) = Z for every prime p unconditionally via Gelfond–Schneider; one open
   rider (T1, refuted under 4EC). Ready as-is.

## Order of work

**Step 1 — finish the A4 dated revision (Session-9 queue items 1a + 2; verified still owed
2026-08-27: `paper.md` still states the 0.9775 constant at lines 48/392/623 and nowhere mentions
0.98018; `o1-n128-report.md` still has 26 unfilled `{{C1_*}}` template slots).**
(a) Fill the `{{C1_*}}` slots in `results/a4-no-go/o1-n128-report.md` from
`results/a4-no-go/verify/o1_crowding_interval_out.json`.
(b) Apply the report's quoted replacement sentences to `pair-channel.md`, `theorems.md`, and
`paper.md`. The corrected content of Theorem B(ii)'s "w ≤ 1 mod one certified constant" clause:
certified C* < 1 on w ≤ 0.98018 (17-box interval partition); certified FAILURE of the ledger
route on w ∈ (0.98, 1] (crossing d* ∈ (0.156, 0.158) certified); (MI) itself numerically
unrefuted at the sliver (margin +17.5); N = 128 all-identities-hold. This is a
strengthening-by-honesty; record it as a dated revision and referee-check the wording.

**Step 2 — independent novelty check of all four documents.** Start from the homework on disk:
`results/c3-r/prior-art-r7a.md` (extended R7(a) gate, verdict NOVEL-WITH-CITATIONS, 7 obligations
— covers the three C3-r notes) and the A4 prior-art gate recorded in `LOG.md` Session 7. Verify
independently (fresh literature sweep), do not merely re-read the files. Note: at Session-7
launch, arxiv.org and github.com were unreachable directly and were fetched via a GCS mirror —
have retry loops ready (network rules in `~/.claude/CLAUDE.md`).

**Step 3 — LaTeX conversion and arXiv-submittable PDFs, one per document.** No TeX is installed
on this machine (decision was deferred until a venue existed — that constraint is now lifted by
the sponsor's request): install BasicTeX (`brew install --cask basictex`, then `tlmgr` packages
as needed) or MacTeX if disk allows. Keep the LaTeX sources in a new `results/arxiv/` directory,
one subdirectory per paper, and commit sources + PDFs. arXiv wants the .tex (+ .bbl) as the
submission unit — the PDF is for the sponsor's review.

## Not circulation-ready — do NOT include

`results/c3-r/m2c-feasibility-ledger.md` (OPEN-WITH-LEDGER), `probe-9.3-a.md`, `probe-9.3-b.md`,
`probe-9.4-note.md`, `s2-feasibility-note.md` (referee debts owed — Session-9 queue item 3), and
everything under `results/d1-*`/Lean (infrastructure, not papers).

## Housekeeping

Per `~/.claude/CLAUDE.md`: start `caffeinate` at the top of the session; commit small and often;
push to origin with a retry loop. U.S. English throughout, including in the LaTeX. Log the work
as a LOG.md entry and update STATUS.md (this task partially discharges Session-9 queue items 1a,
2, and prepares item 5 — the circulation decision itself stays the sponsor's).
