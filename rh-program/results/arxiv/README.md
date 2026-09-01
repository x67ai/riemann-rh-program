# `results/arxiv/` — the submission packages

**Written 2026-08-27** as part of CIRCULATION-PREP step 3; **recommendation added the same day,
after step 4.** One self-contained directory per paper. Nothing here is submitted, and nothing
should be: posting is outward-facing, permanent, and goes out under the sponsor's name, so it stays
the sponsor's act.

## RECOMMENDATION — post two, keep two (2026-08-27)

The four documents are **not** of equal standing, and treating them as one batch would be a
mistake. Three of the four are, in substantial part, standard mathematics, and two of them say so
themselves. So "is it novel?" is the wrong question to sort them by — all four are negatives, and a
negative result is worth publishing when it **stops someone else wasting time**, not when it is
new. That test separates them cleanly:

| Directory | Would anyone otherwise have tried this? | Recommendation |
|---|---|---|
| `a4-no-go/` | **Yes.** The parent paper's own §7.5(e)/§7.2(e) raises exactly this question and leaves the two-bandwidth case open. Gonçalves–de Laat–Leijenhorst's 3-level row *does* pay for their target, so "it pays nothing here" is a substantive, non-obvious negative. | **POST.** The strongest of the four by a distance. |
| `seed-no-go/` | **Yes, and urgently.** The Connes–Consani per-prime Tate curves are two months old and products are the first thing anyone will try. | **POST**, now that Theorems 1–3 are correctly attributed to Winkelmann. Timeliness is most of its value. |
| `m0-axiom/` | **No.** Nobody has proposed this axiom class in print. The note kills a proposal made inside this program. | **Do not post.** Keep as the internal record it says it is. |
| `m1-noncirc/` | **No.** It is graduate-textbook algebraic geometry, and Milne's survey §1 publishes it end to end. | **Do not post.** It claims zero novelty in its own abstract, and it is right. |

**On `a4-no-go`.** It answers a question the literature actually poses, with an exact result
(δ₀ = 0, not "small"), an explicit hand-checkable witness law, twelve machine-checked theorems with
a clean axiom footprint, and a published third-party comparandum it reconciles with rather than
ignores. The audience is small — people working on pair-correlation LP/SDP methods for the
distinct-zeros and simple-zeros problems — but it is a real audience with a real question.

**On `seed-no-go`.** Its mathematical content is an assembly: Winkelmann's rigidity (2002), the
well-known Néron–Severi decomposition for a product of elliptic curves, the classical
$(\Gamma_m \cdot \Gamma_n) = (m-n)^2$ profile, and Gelfond–Schneider (1934) — applied to a
June-2026 object, yielding a clean zero. That is a **note**, not a research paper, and it should be
posted as one. Its value is that it forecloses an obvious route on a new object before people spend
a year on it, and that it does so with the attribution scrupulously right, which it now is.

**On the two that stay in.** Neither is worthless; both are premature. `m0-axiom` becomes postable
the day someone proposes such an axiom class in print — at that point it is a short, sharp reply.
`m1-noncirc` is a genuine audit trail that the seed note and the program both consume, and it
belongs in the repository, cited as supplementary material exactly as the A4 companions are. What
neither belongs on is arXiv, where the first would read as an answer with no question and the
second as a homework exercise a moderator would query.

**If the sponsor disagrees and wants all four out**, the packages are built and pass every check;
nothing further is required. The recommendation is a judgment about audience and standing, not
about readiness.

## POSTED (recorded 2026-09-02)

Both recommended papers are public, by the sponsor's act, and are now **frozen records**:

| Paper | Where |
|---|---|
| The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control (`a4-no-go/`, 41 pp) | `https://x67.ai/cubic-augmentation-no-go.pdf`; Zenodo concept DOI **10.5281/zenodo.22171688** (v1 record DOI 10.5281/zenodo.22171689; file `cubic-augmentation-no-go.pdf`, 631.4 kB; CC BY 4.0; record date 2026-08-26) |
| Products of the per-prime Tate curves of absolute geometry carry no correspondence calculus for the Weil explicit formula (`seed-no-go/`, 19 pp) | `https://x67.ai/tate-products-no-go.pdf`; Zenodo concept DOI **10.5281/zenodo.22171136** (v1 record DOI 10.5281/zenodo.22171137; file `tate-products-no-go.pdf`, 472.8 kB; CC BY 4.0; record date 2026-08-26) |

The two DOIs the sponsor reported (10.5281/zenodo.22171688 and 10.5281/zenodo.22171136) are Zenodo
**concept DOIs** (resolve to the latest version); each currently points at a v1 record whose DOI is one
higher, as tabulated. Mapping read from the Zenodo record pages on 2026-09-02 (through a server-side
fetch; direct requests from this network were answered HTTP 403 "unusual traffic"); the file sizes
match the served PDFs in `public/` byte for byte (631,405 and 472,779 bytes). Cite the concept DOI.
Any later change to either paper is a **public revision** (a new
Zenodo version, with the change stated), never a silent edit of the `.md`/`.tex`. Neither paper is on
arXiv (endorsement gate, CIRCULATION-PREP STEP 6 item 4). `m0-axiom/` and `m1-noncirc/` remain internal.

## What is here

| Directory | Paper | Source of truth | Pages | Recommendation |
|---|---|---|---|---|
| `a4-no-go/` | The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control | `results/a4-no-go/paper.md` | 44 | **post** |
| `m0-axiom/` | The polarized-Frobenius axiom class | `results/c3-r/m0-axiom-note.md` | 14 | keep internal |
| `m1-noncirc/` | Castelnuovo–Severi/Hodge index from Riemann–Roch and ampleness | `results/c3-r/m1-noncircularity.md` | 13 | keep internal |
| `seed-no-go/` | Products of the per-prime Tate curves carry no correspondence calculus | `results/c3-r/seed-no-go-note.md` | 21 | **post** |

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
| Authors | Kunal Tyagi (`hello.jay.tyagi@gmail.com`) — set on all four title pages 2026-08-27, with the AI-use footnote below it. |
| Comments | Page count; a pointer to the companion material where it applies ("Companion notes are cited as supplementary material and are not part of this submission"); and the repository, `Code and data: https://github.com/x67ai/riemann-rh-program`. |
| License | The sponsor's choice. arXiv's default (`arXiv.org perpetual, non-exclusive license`) is the least restrictive to the author. |
| Journal-ref / DOI / Report-no | Leave blank. |

### Settled 2026-08-27 — authorship, disclosure, and the repository

Three things that were open when the packages were built are now closed, at the sponsor's
direction. They are recorded here because each is visible on the title page and a later session
must not undo them.

* **Author.** All four title pages read **Kunal Tyagi**, with `hello.jay.tyagi@gmail.com` in the
  author footnote. (They previously read "Jay Tyagi".)
* **Use of AI, disclosed openly and specifically.** The author footnote on every title page reads:
  *"The mathematics in this paper — the derivations, the computations, the verification suite, and
  the text — was produced by Claude (Anthropic) working under the author's direction inside a
  structured research program; the author set the program's objectives, adjudicated its decisions,
  and is responsible for the content. Claude is a tool and is not an author."* This is deliberately
  specific rather than a vague "AI-assisted": a reader who wants to know what the tool did is told,
  on page 1, without having to infer it. It also matches what arXiv and most journals require —
  a generative system cannot be an author, a human takes responsibility, and the use is declared.
* **The repository is public and is to stay public** (verified 2026-08-27: HTTP 200,
  `private: false`). Both outgoing papers cite it by URL in a "Data and code availability"
  statement, with a commit pin and the note that the fetched PDF corpus is deliberately not
  redistributed for copyright reasons. **Nothing in either paper depends on the corpus**; every
  external claim is cited to its published source.

**What opening the repository actually publishes**, stated plainly so it is a knowing choice: not
only the papers' evidence, but the whole program record — `LOG.md`, `STATUS.md`, `BARRIER-ZOO.md`,
every referee report and adjudication, the probe notes that carry unpaid referee debts, and the
session-by-session history of what was tried, what was wrong, and what was corrected. On balance
that is an asset rather than a liability: it is a fuller audit trail than almost any paper ships
with, and it makes the disclosure above unfalsifiable. But it does mean a reader can find the
program's mistakes, including the ones this session fixed.

**Still outstanding, and only the sponsor can do it: arXiv endorsement.** A first-time submitter to
`math.NT` needs an endorsement from an established author before anything can be posted. Nothing in
this directory removes that gate.

### Suggested categories and MSC classes

**These are suggestions for the sponsor to confirm, not verified facts.** arXiv moderators
re-classify freely, and a wrong primary category delays announcement rather than preventing it.

| Paper | Primary | Cross-list | MSC 2020 (suggested) |
|---|---|---|---|
| `a4-no-go` | math.NT | math.OC | 11M26 (zeros of ζ and L), 11M50 (relations with random matrices), 90C05 (linear programming) |
| `m0-axiom` | math.NT | math.AG | 11M41 (other Dirichlet series and zeta functions), 11N80 (generalized primes), 14G40 (Arakelov theory) |
| `m1-noncirc` | math.AG | math.NT | 14C17 (intersection theory), 14J99 (surfaces), 11G20 (curves over finite/local fields) |
| `seed-no-go` | math.NT | math.AG | 11M26, 14K02 (isogenies), 11J81 (transcendence) |

`m1-noncirc` was previously listed here as postable "as a companion to `seed-no-go`". **That advice
is withdrawn** (2026-08-27): it claims zero novelty in its own abstract ("Every statement is
graduate-textbook algebraic geometry"), the step-4 citation pass confirmed that Milne's survey §1
publishes §§3–7 of it end to end, and Bombieri's Clay problem description states the same thing
about the same theorem. The recommendation above is to keep it in the repository as supplementary
material and cite it from `seed-no-go` by filename, which is what the A4 companions already do.
The categories and classes are kept below in case the sponsor decides otherwise.

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
