# CIRCULATION-PREP — register for the arXiv-preparation work

Task: novelty re-check + arXiv-submittable PDFs for the four circulation-ready documents, at the
sponsor's request (2026-08-27). **Each step below is standalone**: it names its status, inputs,
and acceptance test, so a fresh session (any model) can pick up at any step boundary. Update the
STATUS line of a step when you finish it, and commit per unit. Program setup and working loop:
`KICKSTART.md`; live register `STATUS.md` (Session-9 queue); history `LOG.md`.

## The four documents

All refereed, zero fatal findings, prior-art gates passed. Paths relative to `rh-program/`.

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

**STATUS: DONE (2026-08-27).** Verdict PASS-WITH-REPAIRS, zero fatals; 3 majors (mis-rounded
`+17.47` sliver lower bound — true minimum +17.4663, now quoted `>= +17.46` everywhere incl. the
report's own edit list; unrevised B(ii) proof-sketch tail; stale Section 8.2 "was not run") +
8 minors, ALL executed. Full record: `results/a4-no-go/referee-revision.md`. The A4 package is
wording-final. Adversarial wording check of the revised package: every revised sentence in
`paper.md`/`pair-channel.md` must (a) match the certificates in
`verify/o1_crowding_interval_out.json` + `verify/n128_rerun_out.json` + `o1-n128-report.md`
(numbers, inequality directions, rounding direction), (b) claim nothing on w in (0.98, 1] beyond
attacks + backstop, (c) keep Theorem/Section cross-references consistent (Theorem 4.7, B(i)/B(ii),
Sections 4.2–4.3, 8.3, 9, 10). Also verify the dated-revision blocks read correctly against the
report. Record the pass as `results/a4-no-go/referee-revision.md` (verdict + any repairs applied).

## STEP 2 — independent novelty check (all four documents)

**STATUS: DONE (2026-08-27).** Deliverable on disk: `results/arxiv/novelty-check.md` (97 KB;
workflow `wf_b791f90e-5da`, 4 document sweeps + 4 adversarial refutation agents + 1 synthesizer,
1.79 M subagent tokens). **Verdicts:** A4 **NOVEL-WITH-CITATIONS**; m0 **NOVEL-WITH-CITATIONS**;
m1 **ANTICIPATED-BY** (standard mathematics — the note says so itself and is right); seed no-go
**ANTICIPATED-BY on the rigidity, no-go survives**.

**The headline finding, independently verified this session against the primary sources (not taken
on the agents' word):** *Theorems 1, 2 and 3 of the seed no-go are Winkelmann's, from 2002* —
J. Winkelmann, *On elliptic curves in SL₂(ℂ)/Γ, Schanuel's conjecture and geodesic lengths*,
arXiv:math/0204195 (v1 15 Apr 2002; v3 8 Apr 2003), Nagoya Math. J. **176** (2004), 159–180. His
proof of Theorem 2 derives `4π²/(log λ_i log λ_j) ∈ Q` as the isogeny criterion for
`E_λ = ℂ*/λ^ℤ` by the same real/imaginary separation, divides two such relations to force
`log λ_i/log λ_k ∈ Q`, runs the argument on three curves, and concludes *"for each of these curves
there is at most one other curve in this family to which it is isogenous"*. With `λ = p` that is
the note's Theorems 1–3. Two further verified corrections: **(T1) is Bertrand's weak
four-exponentials conjecture** (Madras 1996; verbatim in Diaz, JTNB 1997), not "unrecorded" as §9
claims; and the **per-prime elliptic-analogue lineage is July 2015** (Connes–Consani, *The Scaling
Site*, arXiv:1507.05818, abstract read), not January 2025 — off by 9½ years. A dated
priority-correction block now heads `results/c3-r/seed-no-go-note.md`, and `prior-art-r7a.md`'s
"and no one has" sentence is formally **withdrawn** with the reason its sweeps missed it
(prime-indexed phrasing vs Winkelmann's eigenvalue/geodesic-length phrasing).

**Two agent errors in the report itself, both caught and adjudicated — do NOT execute them:**
(i) its request to drop "and the Fargues–Fontaine curve" from `[CC26]` is **false** (the arXiv API
truncates that title at the TeX macro; the on-disk full-text extraction is authoritative);
(ii) its claim that "there is no §7.5 in the parent" is **false** — item (e) *is* inside §7.5
"Limits of the method" of the 35-page parent version, and moved to §7.2(e) only in the 17-page v5.
Both pointers are correct and are now explicitly disambiguated in `paper.md`'s `[P]` entry.

**REMAINING WORK — the citation execution, ~40 MUST + ~19 SHOULD actions across the four
documents, is the next session's first task.** It is specified file-by-file, with the exact
insertion points, in `results/arxiv/novelty-check.md` §§A–D. Executing it means editing each source
`.md` **and** mirroring into the matching `results/arxiv/*/main.tex`, then rebuilding and re-running
`results/arxiv/check-submittable.sh`. The seed note additionally needs its **framing rewritten** so
Theorems 1–3 are presented as Winkelmann's, transported — not as new.

Original brief follows.

Start from the homework on disk: `results/c3-r/prior-art-r7a.md` (extended
R7(a) gate, verdict NOVEL-WITH-CITATIONS, 7 obligations — covers the three C3-r notes) and the
A4 prior-art gate recorded in `LOG.md` Session 7. Verify independently with a fresh literature
sweep (arXiv, MathSciNet-visible metadata, Semantic Scholar) per document: does any prior work
anticipate the main claim? Network note: arxiv.org/github.com were once unreachable directly and
fetched via a GCS mirror; retry loops per `~/.claude/CLAUDE.md`. Deliverable:
`results/arxiv/novelty-check.md` — per document: verdict (novel / novel-with-citations /
anticipated-by), citations to add, and the searches run.

## STEP 3 — LaTeX conversion + arXiv-submittable PDFs

**STATUS: DONE (2026-08-27).** All four packages built and passing
`results/arxiv/check-submittable.sh`: **a4-no-go 41 pp**, **m0-axiom 10 pp**, **m1-noncirc 8 pp**,
**seed-no-go 17 pp**. Each directory holds `main.tex`, `main.pdf` and `abstract.txt` (title +
abstract as plain text for arXiv's metadata form); `results/arxiv/README.md` is the submission
guide (build/check commands, what arXiv's upload form asks for, suggested categories and MSC 2020
classes, and the flag that m1 claims zero novelty in its own abstract so its natural framing is as
a companion to the seed note). `results/arxiv/check-submittable.sh` rebuilds from clean and fails
on a TeX error, an undefined reference or citation, a `??` reaching the PDF text, an overfull box
over 20 pt, `\write18`, a missing title/author/abstract, or a British spelling.

**A4 conversion (workflow `wf_50c80dfa-1b1`).** Adversarial fidelity audit verdict **FAITHFUL** —
mechanical numeric-multiset diff against `paper.md` with zero unexplained differences; all 26
numbered statements at exactly the source numbers; all 8 tables; inequality census exact. Five
typographic minors, four applied. **Then five substantive repairs** from the novelty gate and the
formalization audit were applied to `paper.md` and mirrored into `main.tex`: Section 10 rewritten,
the `[P]` parent citation replaced (arXiv:2608.13637, Alpöge–Furman) with the version pin, the
parent's item (e) quoted and distinguished in §1.2, the Lagarias–Rodgers clause in §1.5, and the
bibliography grown from 2 entries to 13.

**Bibliography check of the three C3-r notes — DONE**, see the block below: 33 entries audited,
five substantive errors (four converter-manufactured, one inherited from the prior-art gate) and
15 completeness/staleness fixes, all applied and rebuilt.

**FORMALIZATION AUDIT — new, and it changed the A4 paper.** `results/a4-no-go/formalization-status.md`
records it. Twelve theorems across `Zeta23/PairCeiling/{GridParseval,GridWitness,GridCorner}.lean`
machine-check the paper's Lemma 3.8, Theorem 3.9, the 4128/33 witness for every vacancy position,
the "alive" half of Proposition 3.10, Lemma 4.2, and Theorem 4.3 pointwise + law-form + with exact
attainment. Rebuilt this session: *Build completed successfully (2081 jobs)*, Lean 4.33.0-rc2 /
Mathlib `51e6992`. `#print axioms` on all twelve returns `[propext, Classical.choice, Quot.sound]`
— no `sorryAx`, no `Lean.ofReduceBool`. Whole-tree scan with comments stripped: **zero** real
`sorry`/`admit` across 34 `.lean` files. Section 10 had been titled "Formalization plan" and listed
four of these as queue items; it is now retitled and states the true position, with an honest list
of what is *not* formalized. **No Magma anywhere in this program.**
`results/FORMALIZATION-ROADMAP.md` costs the remaining work and answers the sponsor's "can't we
formalize all this?" — verified against the pinned Mathlib: Gelfond–Schneider, Baker and
six-exponentials are absent; Riemann–Roch, intersection theory and algebraic surfaces are absent;
matrix inertia is absent. A4's headline is reachable end-to-end at tier-1+2 effort; the three C3-r
notes are blocked on Mathlib coverage, not effort.

TeX Live 2026 is installed and verified working:
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

## STEP 4 — execute the citation actions (opened 2026-08-27)

**STATUS: DONE (2026-08-27, Session 11).** All four documents executed and committed, one commit
per document, plus an adjudication sweep. Rebuilt from clean: **a4-no-go 44 pp, m0-axiom 14 pp,
m1-noncirc 13 pp, seed-no-go 21 pp — ALL CHECKS PASSED.** The `a4-no-go` package was also missing
its `abstract.txt` (the other three had one); created.

**The verification discipline below was followed literally, and it was worth it.** A workflow of
18 primary-source verification agents plus an adjudicator checked every MUST and SHOULD action
before it touched a file: 92 items, 2.67 M subagent tokens, evidence written one file per cluster
to `results/arxiv/citation-verification/` with `ADJUDICATION.md` settling the cross-cluster
disagreements. **Twenty-one of the report's actions did not survive**, and each is now recorded in
a dated block inside the paper it would have touched so that a later session cannot reintroduce
it. The most dangerous four, because a sentence was to be written on their strength:

* **Ito–Ito–Koshikawa Remark 1.3 is not "the published non-circularity audit"** — it says the
  opposite, that they *did not attempt* to avoid the Weil conjecture. (That is a *stronger*
  precedent for m1 and is now quoted as what it is.)
* **Ancona makes no independence or non-circularity claim anywhere**, and his §1 does not publish
  m1's §9 "verbatim". `grep circular` returns zero.
* **The seed note's "first appears in January 2025" lineage** is off by nine years and five months
  — and the correction needed a correction of its own: the July-2015 object is `C_p = R*₊/p^Z`, a
  **real** circle in characteristic one, while the **complex** Tate curve is June 2026. Both halves
  are now stated.
* **The two Connes–Consani Riemann–Roch papers do not supply `h⁰_θ`** — they explicitly call the
  log-theta number virtual, "for the obvious reason that it outputs real numbers rather than
  integers". m0's §7 is softened, but the M4-level input genuinely does survive as unsupplied.

Also caught and not executed: an **invented Milne quotation** ("avoid the Weil conjecture" — the
string "avoid" occurs zero times in his paper); **Kleiman's Remark 3.10** pointing at the wrong
remark (4.5 is the dependency-ledger one); **Montgomery–Vaughan §1.2** (it is §1.3); a **"§7"
citation to a paper with six sections** (Winkelmann); **Waldschmidt's AWS Conjectures 5.34/5.35**
described as four-exponentials statements (they are Bertrand's *modular* conjectures on `J`); and
**Chirre–Gonçalves–de Laat's inequality (7)** called "the published convex-programming form" (it is
elementary integer arithmetic, credited there to an argument of Ghosh, and at the *third*
integrality level where A4's Lemma 4.2 is at the *second*). Two report claims that were already
adjudicated in Session 10 were re-confirmed against the primary sources a second time: the parent's
item (e) really is in §7.5 of the 35-page version, and "and the Fargues–Fontaine curve" really is
part of the `[CC26]` title — though the *mechanism* recorded for the latter ("the API truncates at
a TeX macro") was itself wrong and is now corrected in place: the clause is absent from every arXiv
metadata surface and from zbMATH, and survives only on the typeset title page and in arXiv's HTML.

**Two withdrawals now stand in `prior-art-r7a.md`**, both dated: the "and no one has" sentence
(Session 10) and the January-2025 lineage clause (this session). `BARRIER-ZOO.md` I.1 no longer
attributes the word "monoid" to Blomer and Leung — a case-insensitive count in both arXiv versions
of their paper is zero, and their theorem is for GL(3) while Davenport–Heilbronn is degree 2, so
they do not exclude it; what they supply is the *shape* of the exclusion.

**What remains for the sponsor:** Session-9 item 5, the circulation decision itself. Nothing in
this step touched a theorem, a proof, a number or a verdict in any of the four papers.

Original brief follows.

`results/arxiv/novelty-check.md` §§A–D specify, per document, ~40 MUST and ~19 SHOULD citation
actions plus 13 textual repairs, each with its insertion point. Working loop, per document:

1. Apply the MUST items to the source `.md` (the source of truth), then the SHOULD items.
2. Mirror every change into the matching `results/arxiv/<paper>/main.tex` — do **not** re-convert.
3. Rebuild: `export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"` then two `pdflatex` passes.
4. `bash results/arxiv/check-submittable.sh results/arxiv/<paper>` must print ALL CHECKS PASSED.
5. Commit per document.

**VERIFY EACH ACTION BEFORE EXECUTING IT — this is not a checklist to apply blind.** Session 10 independently checked roughly six of the report's claims against primary sources and **two were wrong**: it asked for the `[CC26]` title to be truncated (the arXiv API truncates that title at the TeX macro — the on-disk full-text extraction is authoritative, and executing the "fix" would replace a correct citation with a wrong one), and it asserted "there is no §7.5 in the parent" (item (e) *is* inside §7.5 of the 35-page parent version; it moved to §7.2(e) only in the 17-page v5). Neither is a criticism of the report — it also found the Winkelmann anticipation, which is real and which the 2026-08-26 gate missed entirely. It means the error rate is high enough that **every MUST action must be confirmed against a primary source before it touches a file**: the arXiv API or abs page, Crossref, zbMATH, or the on-disk corpus in `fetched*/` and `sources-extracted/`. Where the report and a primary source disagree, the primary source wins and the disagreement gets a dated note so it cannot be reintroduced.

**The seed no-go needs more than citations.** Its framing must be rewritten so Theorems 1–3 are
presented as Winkelmann's rigidity transported to the June-2026 Connes–Consani Tate curves, with
the note's own contribution located where it actually is — Theorem 4 (Néron–Severi collapse),
Theorem 5 (prime-blind diagonal residue, unconditional via Gelfond–Schneider), Theorem 6, and the
no-go conclusion. §9's "(T1) appears to be unrecorded" must go, and the §1.2/§9 lineage must move
from January 2025 to July 2015. The dated block at the head of the note states all of this; the
body has not yet been rewritten to match.

**A4's remaining textual repairs** are the three named in `novelty-check.md` §A; note that its
first two — the Haran/Thas citation and the parent-paper `[P]` entry — are already **done**.

## STEP 5 — the circulation recommendation (NEW, 2026-08-27)

**STATUS: RECOMMENDATION MADE. The act itself is still the sponsor's** — posting is outward-facing,
permanent, and goes out under his name, so nothing has been submitted and nothing will be without
his say-so. Full reasoning in `results/arxiv/README.md`, top section.

**The sponsor's question, in his words:** *"it's pointless if the paper carries nothing novel and
doesn't contribute to the field, right?"*

**He is right about two of the four and wrong about the other two, and the reason is that "novel"
is the wrong sorting criterion here.** All four documents are negative results. A negative result
earns publication when it **stops someone else wasting time**, not when it is new — Gonçalves–de
Laat–Leijenhorst publish exactly such a negative (the remark after their (6)), and so does
Deninger's whole "there is no 'Weil-'cohomology" paper. Applying that test:

| Document | Would anyone otherwise have tried this? | Call |
|---|---|---|
| A4 no-go | **Yes** — the parent's own §7.5(e) raises the question and leaves the two-bandwidth case open; and GdLL's 3-level row *does* pay for their target, so "nothing here" is substantive | **POST** |
| Seed no-go | **Yes, and urgently** — the CC Tate curves are two months old and products are the obvious first move | **POST** |
| m0 axiom note | **No** — nobody proposed this axiom class in print; the note kills a proposal made inside this program | **KEEP INTERNAL** |
| m1 non-circularity | **No** — it is textbook, and Milne §1 publishes it end to end; the note says so itself | **KEEP INTERNAL** |

**Why A4 survives the test cleanly.** Exact result (δ₀ = 0, not "small"), explicit hand-checkable
witness, twelve machine-checked theorems with a clean axiom footprint, a published third-party
comparandum it reconciles with rather than ignores, and a question the literature actually asks.
Small audience; real audience.

**Why the seed note survives it, and what it is.** Its content is an assembly of known facts —
Winkelmann 2002, the well-known NS decomposition, the classical `(Γ_m·Γ_n) = (m−n)²` profile,
Gelfond–Schneider 1934 — applied to a June-2026 object and yielding a clean zero. That makes it a
**note**, not a research paper, and it should go out as one. Its value is timeliness plus correct
attribution, and after step 4 the attribution is right.

**Why the other two stay in, and what would change that.** Neither is worthless; both are
premature. `m0-axiom` becomes postable the day someone proposes such an axiom class in print — it
is then a short, sharp reply. `m1-noncirc` is a real audit trail that the seed note and the program
both consume, and it belongs in the repository as supplementary material, cited by filename exactly
as the A4 companions are. On arXiv the first would read as an answer with no question and the
second as a homework exercise a moderator would query. The earlier README advice to post
`m1-noncirc` "as a companion to seed-no-go" is withdrawn.

**Cost of being wrong in each direction.** Posting all four risks the two weak ones dragging the two
good ones down — a reader who opens `m1-noncirc` first and finds "zero novelty is claimed" will
discount the other three. Posting only two risks nothing except that two internal documents stay
internal, which is what they were written to be. The asymmetry is why the recommendation is two,
not four.

**If the sponsor decides otherwise, no work is required:** all four packages are built and pass
`check-submittable.sh`, and the suggested categories and MSC classes for all four are in
`results/arxiv/README.md`.

## STEP 6 — pre-posting blockers (opened and mostly closed, 2026-08-27)

Answering the sponsor's "can they be published?" turned up one real blocker beyond the citation
work, and raised two questions that were his to settle. Status:

1. **The A4 paper's evidence base was unreachable — FIXED.** Its Provenance section cited thirteen
   file paths inside a repository that returned HTTP 404, and its body referred to "Session 8",
   "this session" and "the binding adjudication, survives-with-repairs 5.5" as if those were
   citable authorities. Thirty edits to `results/arxiv/a4-no-go/main.tex`: the internal vocabulary
   is now *defined* before use, every session reference is a date or neutral phrasing, and the
   evidence list is a proper "Data and code availability" statement. The seed note was already
   externalized and gained the matching statement. **The source `.md` files are unchanged** — they
   are the internal record, where the internal words are the right ones.
2. **Repository visibility — CLOSED by the sponsor.** The repo is public and is to stay public
   (verified: HTTP 200, `private: false`). Both outgoing papers cite it.
3. **Authorship and AI disclosure — CLOSED by the sponsor.** Author is **Kunal Tyagi**, email
   `hello.jay.tyagi@gmail.com`, and Claude is disclosed openly and *specifically* in a title-page
   footnote on all four papers — what it did, that it is a tool and not an author, and that the
   author is responsible. See `results/arxiv/README.md` for the exact wording and for a plain
   statement of what opening the repository publishes.
4. **arXiv endorsement — OPEN, and only the sponsor can clear it.** A first-time `math.NT`
   submitter needs an endorsement from an established author. This is a hard gate and nothing in
   the repository removes it.

**A distinction that was blurred earlier and should not be again:** *posting to arXiv* (a preprint
server, no peer review) and *journal publication* (peer review) are different bars. The
recommendation in STEP 5 is for arXiv. For a journal, neither paper is ready as it stands: the A4
paper builds on a parent that is itself weeks old and unrefereed and is long for a negative result,
and the seed note — with the attribution now correct — is a short note whose content is an assembly
of known results applied to a new object, which a referee may reasonably call a remark rather than a
paper. Post first; treat journal submission as a later, separate decision.

## Housekeeping

Per `~/.claude/CLAUDE.md`: `caffeinate` + push watchdog at session top; commit small and often;
push with a retry loop. When all steps are DONE: mark Session-9 queue items 1b + 2 done in
STATUS.md, add a LOG.md entry, and leave the circulation decision itself to the sponsor
(Session-9 item 5).
