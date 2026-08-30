# Work order — make the two outgoing papers standalone

**Opened 2026-08-27** after the sponsor read page 1 of the A4 PDF and asked, correctly, why the
project's internal narration was in a finished paper, and why the abstract's first sentence
referred to "the parent paper" as though the reader knew which one.

He is right, and the earlier "externalization pass" (commit `afd2cdd`) did not fix it. That pass
was cosmetic: it renamed session numbers to dates and rewrote the evidence list, and left the
apparatus standing. **The test to apply to every line: would a reader who has never heard of this
program understand it, and can they check it?** If not, it is either cut or rewritten.

## Done in this session

**A4** (44 pp → 41 pp)

* **Deleted both `datedrev` changelog blocks from page 1.** They narrated a revision history — "the
  interval hardening found the earlier ratio to be a grid artifact", "an independent novelty
  re-check was run before circulation" — which is version-control information, not scholarship.
  Verified before cutting that the substantive re-scoping is stated independently in the body
  (§4.3, §7, §8; the constant `0.98465` appears at four separate places), so nothing was lost.
* **Deleted the `Program: / Date: / Evidence discipline:` front block** — "RH program, direction
  A4 (merged A2+A4 cubic-certificate direction)", "this paper is that gate's absorption branch".
* **Deleted the 144-line `Revision record (2026-08-26)` section**, a referee-repair changelog
  (R1-M1, R2-m7, …). On arXiv, revision history is the v1/v2 mechanism, not a section.
* **Rewrote the abstract's first sentence.** Was: *"The parent paper's unconditional two-thirds
  theorem rests on a two-moment certificate…"*. Now names Alpöge and Furman, states their theorem,
  and cites `[P]` — in the first sentence, where the reader needs it.
* Removed four bibliography pointers into the excluded PDF corpus (`fetched/w-09` and friends).

**Seed no-go** (21 pp, unchanged)

* `Route A` / `Route C` / `M2b` / `N2` → named mathematically ("the characteristic-one square of
  Connes and Consani", "Deninger's foliated-dynamical route").
* "What dies / what does not die" → "What the no-go rules out / What it leaves untouched".
* Provenance remark trimmed of the program narration (the prior-art gate's search-phrasing counts,
  the barrier-taxonomy entry number, the "companion program note" pointer); the two genuine
  limitations it recorded — Akatsuka read via Tanaka, quotations checked against full texts — are
  kept, because those are scholarly caveats rather than internal process.
* "this note" → "this paper"; "the commissioned calculus" → "the required calculus".

Its abstract was already fine: it opens by naming Connes and Consani.

## The A4 body pass — DONE 2026-08-27

Executed in three commits: `e8c9ff5` (the pass), `2db51b4` (the fixes its audit
found), `6938d57` (source rewrap, cosmetic).

**The counts.** `grep -ci "the gate\|adjudicat\|supplementary material\|direction A4\|deliverable"`
went **64 → 2**, and both survivors are justified line by line: the `\thanks`
footnote's use-of-AI disclosure ("the author ... adjudicated its decisions"), and
the real repository path `results/adjudication-A4.json` in the availability list.

**What was done, by class.**

* **`the gate` (40 → 0 in prose).** Judged per occurrence into the three senses
  the work order identified. Most became "the decision program", "the decision
  LP", "the computation", "the row system", or a property of the paper itself
  ("the primary geometry", "the admissible pair class") with a section pointer so
  the reader can check it. The 20 remaining string matches are all inside the
  path `results/a4-m2-gate/`, which is a real directory.
* **`adjudicat*` (15 → 1).** Where the sentence carried mathematics, the
  mathematics is stated directly. Where it was a repair label naming a real fix
  (`Theorem 1(ii)-repaired`, `R4: θ < 1 strict`, `repair R6`), the label was
  retired at *all* its sites together and replaced by the fact.
* **`supplementary material` (5 → 0).** Decided as Option B: the three companion
  documents are named and given their repository paths, matching the availability
  list. The pair-channel item now says plainly that Theorems 4.6 and 4.7 are
  proved there and only their proof architecture is given here.
* **`the program` (7 → 0), `direction A4` (2 → 0), `deliverable` (2 → 0).**

**The completeness sweep the work order asked for** found, and retired, a whole
tier the enumeration missed: Tier-1/Tier-2/Tier-A (13 sites, including the
surviving superscript `P^{T2}`), the milestone labels M2/M4/M5, R1–R7 in the
body, "the campaign", "this session", "shipped", "quarantined", "the audit's
finding N", "the direction file", session date stamps inside theorem statements,
JSON keys quoted as row names, and an unused `\newtheorem*{datedrev}`.

**§1.1–§1.3 were re-read cold** and the first two pages now refer to nothing the
reader cannot open. Gaps the de-internalization exposed were closed at the same
time: `P_base`/`P_full` are defined where the question is posed rather than 300
lines later; "bite" and "absorption" are glossed at first use (both were used
unglossed nine times downstream and in the abstract); so are "garnish", the
capacity fuzz row, `δ₀'`, `ε₃`, `Γ`, `B₁/B₂/B₃`, `p(c)`, `Sgen`, `ν_joint`,
`Φ₀`, "admissible", and the stop rule; and the baseline rows are numbered
(R-1)–(R-4) so the (R-5)–(R-9) sequence is no longer a fossil with a gap.

**`abstract.txt` is now generated from the TeX abstract, never hand-edited.** It
had been missed entirely and still carried "Direction A4 proposed" and "the
gate's R5 depth family" — the one artifact arXiv shows before the paper itself.

**Verification.** Sixteen agents across two workflows: six to propose the edits
per class and six to adversarially verify them, then four independent audit
lenses over the result (lost caveats, cold readability, fresh completeness sweep,
mathematical integrity). The integrity lens diffed every numeric literal, every
inline and display math span and all 35 theorem-family blocks between the before
and after files: **no mathematics changed.** Every scholarly caveat survives,
reworded rather than cut — the eight break attempts, flag F4's unproven bridge,
the (O1)–(O5) residue, the three [BGSTB24] riders, the pricing-is-heuristic
caveat, the audit's binding wording bar, and the "only fully clean-stop runs"
note. `bash results/arxiv/check-submittable.sh` prints ALL CHECKS PASSED, 41 pp.

## The seed no-go — swept again, and finished (commit `c29b5a5`)

The A4 sweep showed the work order's term list was not exhaustive, so the same
lens was run over the seed paper. It was far cleaner, and its `(R1)`–`(R3)` are
genuine — the paper's own names for the three requirements of the Weil-positivity
calculus, defined in §2. Twelve real hits remained and are fixed: **"the
commissioned calculus" was still in the abstract**, the priority note opened with
"an independent novelty check … run before circulation", the prior-art retraction
was phrased as a verdict with halves, the construction was "born and killed
inside the program", Provenance named "direction ``C3: geometric substrate''" and
"an independent adjudicator", and four "the note" self-references survived. Every
integrity claim in that section is untouched: the duplicate-blind protocol, the
independent re-derivation, the referee pass that found a fatal defect cutting in
the paper's own disfavor, and the two recorded limitations of the literature
search.

**Both `abstract.txt` files are now generated from their papers' TeX abstracts.**
A4's still said "Direction A4 proposed" and "the gate's R5 depth family"; the
seed's still said "commissioned". That file is what arXiv renders on the listing
page — the one artifact a reader sees before the paper.

## Closed 2026-08-28, after the sponsor asked for both open items

**Every bibliography entry in both papers is now actually cited.** 8 of A4's 16
and 10 of the seed paper's 34 were not, several carrying annotations stating
where they were cited. In every case the annotation was right and the citation
was simply missing, so each was added at the place it belonged. Two of them earn
their keep on their own: Cohn–de Laat–Salmon, because in the sphere-packing
analog the three-point bound *does* improve on the two-point bound, which makes
this paper's zero a substantive negative rather than a foregone one; and
Karlin–Studden, because cubic blindness is the exact form of the classical fact
that an odd moment cannot improve a one-sided bound in a Chebyshev system. A4's
citation style is also unified — the hard-coded `[P]`, `[BHB13]`, `[LR20]` and
seven `[BGSTB24]` are now `\cite`, so the bibliography is machine-checkable. The
one hard-coded `[RS96]` left alone sits inside the verbatim quotation from the
parent paper.

**The four companion documents have had the same pass as the papers** (223
edits, four proposers and four adversarial verifiers). What the verifiers caught
by going and checking rather than reasoning is the part worth recording: the
formalization record's claim that the Lean files were "byte-identical" to the
build tree was false (they differ in the relicensing header); its axiom block
listed nine theorems under a sentence promising twelve, and a verifier ran Lean
to produce the three missing lines rather than inferring them; its reproduction
recipe began by entering a private local directory; its file sizes described a
tree that is not public. A proposed edit asserting that a repository-wide search
for "Magma" returns nothing was dropped because a verifier ran the search and it
returns four files. No pointer into `fetched*/` survives in any of the four —
those directories are deliberately not redistributed, so every one of them was
dead for a reader.

**One broken pointer found while preparing the PDFs**: the seed paper named its
two numerical-check files with no path while its availability statement declares
paths relative to `rh-program/`. They are at `results/c3-r/`. Every other file
pointer in both papers was checked against `git ls-files` and resolves.

**The post drafts were rewritten.** They had been in markdown blockquotes, so
copying one brought a `>` on every line — against the standing rule that
anything handed over to be copied goes in a fenced block. And they were written
in AI register: rhetorical question then answer, em-dash antitheses, fragments
used for drama. Rewritten as plain declarative sentences, re-measured, and all
six now fit 280 characters *with* a link rather than without one.

## Left for the sponsor


1. **The ~40 `\texttt{}` script pointers in the body.** Untouched, as the work
   order said: this is the sponsor's call, not the program's.
2. **Nine bibliography entries are never cited in the body** (LR21, Mon73, Hej94,
   CGG98, KLS07, KLS11, CdLS22, KS66 and one more), several carrying annotations
   that state where they are cited. Citation style is also mixed — `\cite{}` in
   some places, hard-coded `[P]`, `[RS96]`, `[BGSTB24]` in others. Both are
   tidy-ups a referee would notice; neither is a de-internalization question.
3. **`θ` carries three unrelated meanings** (the ladder parameter in "θ < 1
   strict", grid positions θ_i, and the bandwidth offset). Fixing it means
   renaming a variable throughout, which is a mathematics edit, not a wording one.
4. ~~The companion documents were full of internal narration.~~ **Done above.**
   The original note read: ("Program: RH program, direction A4", "standing order 5",
   "AUDIT finding MINOR-4", pointers into `sources-extracted/` and `fetched-r3/`).
   The paper now cites them by repository path, which is honest. But if they are
   ever to ship as arXiv ancillary files — and `pair-channel.md` carries proofs
   the paper defers to — they need the same pass this paper just had.

---


## Second pass, 2026-08-30 --- the sponsor read the posted PDFs

He asked why the A4 paper says "the parent paper [P]" instead of citing Alpoge and Furman the way
papers cite papers; why both papers still carry the program's internal process; why the Tate paper
leans so hard on Winkelmann; and why either paper labors the point that a negative result is
negative. **The standard he set: the papers must be standalone and read the way published papers
read.** The first pass had removed the vocabulary; this one removed the apparatus.

**Method.** Both papers were cut into disjoint line ranges (ten for A4, seven for the seed), each
rewritten by its own agent against a shared work order and a pinned decisions file, each rewrite
adversarially verified, then reassembled and gated: every math span, numeric literal and theorem
body diffed against the pre-pass baseline. Each finished paper then went through five independent
audit lenses (cold reader, scholarly-loss, cross-range consistency, LaTeX, scope), every finding
adversarially verified before it was allowed to become an edit.

**A4** (41 pp, unchanged). `[P]` is now `[AF26]`; "the parent"/"the parent's" is gone from all ~50
sites in favor of naming Alpoge and Furman or citing `\cite[\S5]{AF26}`. "Repaired" (11x) and
"as-written" (9x) were relational adjectives whose referent the paper never showed -- the two forms
of the spectral-tail theorem are now stated once in the paper's own voice and named descriptively
thereafter. `P_cal` (used once, defined nowhere) restated. `MD(lambda, delta)` defined, and its
second argument renamed to `eta` to stop it colliding with the pair depth. The two defensive
subsections merged into one that states the scope without protesting. The bibliography's audit
trail (which PDF was opened, which databases were searched) removed, every bibliographic fact kept.
~60 ALL-CAPS emphasis words and the bold in running prose removed. Provenance is a one-sentence
method note plus the availability list, each artifact described by its contents rather than its
role in the program's governance.

**Seed** (21 pp -> 19 pp). The front-matter priority block, the block-quoted attribution note, the
"Novelty statement" and the "Withdrawn" paragraph are all gone; Winkelmann is credited in exactly
three places, plainly, plus the two places his Conjecture 1 and Lemma 7 carry mathematics. The
paper had been quoting "the proposal" as though it were a published document -- including
``the correspondence calculus itself or nothing.'', a quotation with no source anywhere, because
the paper puts the proposal forward itself. Removed, along with "the designer" and "the answer
key". The bibliography's arXiv-metadata forensics and "The paper has six sections; there is no
\S7" removed. The prior-art list said "Eight adjacent traditions" over nine items. "E. Bombieri
(2000)" was cited with no entry; it now carries a full reference. Section 0 stopped repeating the
abstract and became Section 1.

**Two mathematical corrections, made on the sponsor's instruction to fix the mathematics too.**

1. *The Cauchy--Schwarz step in the fractional-marks proposition.* The paper asserted
   `abar(d)^2 <= (1 + abar(2d))/2` and attributed it to `abar((x+y)/2)^2 <= abar(x)abar(y)` at
   `(0, 2d)`. That application yields only `abar(d)^2 <= abar(2d)`, which is strictly weaker: at
   `N = 64, d = 1` the asserted bound is 23.61 against 46.21. **The asserted bound is nonetheless
   true**, by Cauchy--Schwarz on the weights `u_j` (which sum to 1) together with
   `cosh^2 t = (1 + cosh 2t)/2`; verified numerically to machine precision. Only the justification
   changed -- the displayed conclusion and everything downstream stand.
2. *A notation collision on the paper's headline symbol.* `delta_0` denoted both the marginal value
   `P_full - P_base` (about 30 uses) and the Dirac mass in Montgomery's form factor, twenty lines
   apart, while bare `delta` is the pair depth. The Dirac mass is now `delta_D`, glossed at use.

**What was deliberately NOT done.** Both papers' scope lenses wanted a sentence added saying the
paper claims nothing about the Riemann hypothesis. The sponsor's instruction was the opposite --
readers are mathematically literate and neither paper ever made such a claim -- so it was excluded.
The "not held" / "paywalled and not read" notes on Bertrand, Schneider and Rosen--Shnidman were
kept: those are scholarly caveats about what was verified at first hand, not process narration.

**A caution for whoever runs this next.** The fix agents faithfully applied audit-proposed wording
that was mathematically wrong -- one edit rewrote "both earlier estimates are superseded" as "it
improves on the two-term dyadic bound `2 sqrt(C eps)`", which is false, since the sharp constant is
`2 sqrt 2 > 2` and so that estimate was never a valid upper bound. The verify pass caught it. Do
not skip the verify pass on the fixes, only on the findings.

---

## Original work order (retained for the record)

## Remaining — the A4 body pass

Counts as of this commit, in `a4-no-go/main.tex`:

| Term | Count | What to do |
|---|---|---|
| `the gate` | 40 | **Judgment per occurrence.** It means three different things: (i) the decision linear program itself, (ii) the pre-registered specification, (iii) the whole decision episode. Render (i) "the decision program", (ii) "the pre-registered specification", (iii) "the computation". Do **not** sed it — the paper defines the object properly in §1.3 and §2, so most occurrences only need the noun swapped. |
| `adjudicat*` | 15 | Attribute the *mathematics* directly and drop the process. "The adjudication ordered seven repairs" → state what the repairs were, or cut. Where it is genuinely a provenance claim, it belongs in the Provenance section, not the body. |
| `supplementary material` | 5 | Points at three companion documents: `theorems.md`, `pair-channel.md`, `data-tables.md`. **Decide once:** either inline what the paper actually relies on, or cite them as repository artifacts with their paths, as the availability section already does. The present half-way form — an italic phrase with no locator — tells the reader nothing. |
| `the program` | 7 | Usually removable. |
| `direction A4` | 2 | Remove; the paper is about a question, not a direction. |
| `deliverable` | 2 | Remove. |

Then: re-read §1.1–§1.3 end to end as a stranger would. That is where the paper still frames
itself as an internal answer to an internal question, and it is the part a referee reads first.

Also check both papers for: `\texttt{}` references to scripts in the body (~40 in A4). These are
defensible — the paper's headline is an exact equality with a hand-checkable witness, and the
repository is public so they resolve — but they are worth thinning to one pointer per section if a
more conventional look is wanted. **Sponsor's call, not the program's.**

## Acceptance test

1. `grep -ci "the gate\|adjudicat\|supplementary material\|direction A4\|deliverable" a4-no-go/main.tex`
   returns a number you can justify line by line.
2. Read the first two pages aloud. Nothing in them refers to a document the reader cannot open.
3. `bash results/arxiv/check-submittable.sh` still prints ALL CHECKS PASSED.
