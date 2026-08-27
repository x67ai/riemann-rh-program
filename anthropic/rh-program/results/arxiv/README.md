# `results/arxiv/` — the submission packages

**Written 2026-08-27** as part of CIRCULATION-PREP step 3. One self-contained directory per paper.
Nothing here is submitted; **whether, where and when to circulate is the sponsor's decision**
(STATUS.md Session-9 queue item 5). This directory only makes the decision cheap to act on.

## What is here

| Directory | Paper | Source of truth | Pages |
|---|---|---|---|
| `a4-no-go/` | The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control | `results/a4-no-go/paper.md` | see the directory |
| `m0-axiom/` | The polarized-Frobenius axiom class | `results/c3-r/m0-axiom-note.md` | 14 |
| `m1-noncirc/` | Castelnuovo–Severi/Hodge index from Riemann–Roch and ampleness | `results/c3-r/m1-noncircularity.md` | 13 |
| `seed-no-go/` | Products of the per-prime Tate curves carry no correspondence calculus | `results/c3-r/seed-no-go-note.md` | 21 |

(Page counts as of the 2026-08-27 citation pass; `a4-no-go` is 44 pp. All four grew when the citations, prior-art sections and reference lists were added.)

Each directory holds `main.tex` (the submission), `main.pdf` (the compiled paper), `abstract.txt`
(title + abstract as plain text, for pasting into arXiv's metadata form), and the build products
`main.aux` / `main.log` / `main.out`, which are **not** part of a submission tarball.

**The markdown is the source of truth.** If a paper needs changing, change the `.md` first and
re-derive; never let the `.tex` drift into being a second original.

## Building

TeX Live 2026 is installed on this machine and needs nothing added:

```
export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"
cd results/arxiv/<paper> && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex
```

Two passes: the second resolves cross-references. There is no `.bib` — every paper carries a
hand-written `thebibliography`, so there is no BibTeX/biber step and no `.bbl` to ship.

## Checking

```
bash results/arxiv/check-submittable.sh              # all papers
bash results/arxiv/check-submittable.sh results/arxiv/seed-no-go
```

It rebuilds each paper from a clean state and fails on: a TeX error, an undefined reference or
citation, a `??` reaching the PDF text, an overfull box wider than 20 pt, `\write18`, a missing
title/author/abstract, or a British spelling. It also lists the files that must be kept out of the
submission tarball. **All three C3-r notes pass.**

## Submitting (what arXiv asks for, and the answer for these papers)

Upload `main.tex` alone — a single `.tex` file with no figures, no `.bib`, no `\input`. arXiv's
AutoTeX runs `pdflatex` and will produce the same PDF; do **not** upload the PDF, and do not
upload `main.aux`/`main.log`/`main.out`.

| Field | What to enter |
|---|---|
| Title / Abstract | Paste from the paper's `abstract.txt` (line 1 is the title, the rest is the abstract). Inline `$…$` is accepted in arXiv abstracts. |
| Authors | Jay Tyagi |
| Comments | Page count, and — where it applies — a pointer to the companion material, e.g. "Companion notes are cited as supplementary material and are not part of this submission." |
| License | The sponsor's choice. arXiv's default (`arXiv.org perpetual, non-exclusive license`) is the least restrictive to the author. |
| Journal-ref / DOI / Report-no | Leave blank. |

### Suggested categories and MSC classes

**These are suggestions for the sponsor to confirm, not verified facts.** arXiv moderators
re-classify freely, and a wrong primary category delays announcement rather than preventing it.

| Paper | Primary | Cross-list | MSC 2020 (suggested) |
|---|---|---|---|
| `a4-no-go` | math.NT | math.OC | 11M26 (zeros of ζ and L), 11M50 (relations with random matrices), 90C05 (linear programming) |
| `m0-axiom` | math.NT | math.AG | 11M41 (other Dirichlet series and zeta functions), 11N80 (generalized primes), 14G40 (Arakelov theory) |
| `m1-noncirc` | math.AG | math.NT | 14C17 (intersection theory), 14J99 (surfaces), 11G20 (curves over finite/local fields) |
| `seed-no-go` | math.NT | math.AG | 11M26, 14K02 (isogenies), 11J81 (transcendence) |

`m1-noncirc` is the one to think about before posting: **it claims zero novelty in its own
abstract** ("Every statement is graduate-textbook algebraic geometry") and its value is the audit
trail. That is an honest and useful thing to have on record, but it is not the usual shape of an
arXiv posting, and a moderator may query it. Posting it as a companion to `seed-no-go`, which
consumes it, is the framing that makes sense of it.

## The novelty record

`results/arxiv/novelty-check.md` is the independent prior-art check for all four papers (step 2).
The earlier, deeper gate for the C3-r notes is `results/c3-r/prior-art-r7a.md` — read its dated
2026-08-27 corrections, which repair a misattribution the gate itself introduced.

## Bibliography provenance

Every bibliography entry in the three C3-r notes was independently re-verified on 2026-08-27
against the arXiv API, Crossref, zbMATH, NUMDAM, mathnet.ru and the on-disk PDF corpus. Five
substantive errors were found and fixed; the full record, including what was checked and found
*correct*, is in `CIRCULATION-PREP.md` under "Bibliography check". Two of those corrections are
also standing caveats — `results/corpus-routing.md` caveats 17 and 18 — because the wrong data had
propagated into program files beyond these papers.

**The citation pass (2026-08-27, CIRCULATION-PREP step 4).** Every MUST and SHOULD action in
`novelty-check.md` §§A–D was confirmed against a primary source **before** it was allowed to touch
a file — the report's own error rate made that non-negotiable. The evidence is on disk, one file
per source cluster, in `results/arxiv/citation-verification/`, with
`ADJUDICATION.md` settling the cross-cluster disagreements. **Twenty-one of the report's actions
did not survive and were not executed**; each is recorded in a dated block inside the paper it
would have touched, so that a later session cannot reintroduce it. The four that would have done
real damage, because a sentence was to be written on their strength: Ito–Ito–Koshikawa's Remark 1.3
says the *opposite* of "a clean non-circularity audit"; Ancona makes no independence claim at all;
the seed note's "January 2025" lineage is off by nine years and five months; and the two
Connes–Consani Riemann–Roch papers do **not** supply the θ-effectivity input, since they
explicitly call the log-theta number virtual. Also caught: an invented Milne quotation ("avoid the
Weil conjecture" — the string "avoid" occurs zero times in his paper), a Kleiman remark number
pointing at the wrong remark, a Montgomery–Vaughan section number off by one, and a "§7" citation
to a paper with six sections.

**What that pass cost the papers, honestly.** The seed no-go's Theorems 1–3 are now presented as
Winkelmann's (2002), transported — in its abstract, in a priority note directly under the abstract,
in a banner at the head of §3, and in its novelty statement. `prior-art-r7a.md` carries two dated
withdrawals. Nothing else changed: no theorem, proof, number or verdict in any of the four papers
was affected.
