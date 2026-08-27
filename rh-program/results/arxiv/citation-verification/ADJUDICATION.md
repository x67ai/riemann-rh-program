# ADJUDICATION — citation-verification pass, 18 clusters

Adjudicator: independent session, 2026-08-27.
Inputs: the 18 cluster reports in this directory (`A4-1`, `A4-2`, `A4-3`, `M0-1` … `M0-5`,
`m1-1`, `M1-2` … `M1-5`, `SEED-1` … `SEED-5`), all read end to end.
Where two clusters checked the same source and disagreed, the disagreement was settled against
the primary source — re-fetched and re-read in this session where the reports did not settle it.

Standing rule applied throughout, inherited from the pass: **the primary source wins.** A cluster's
verdict line does not outrank its own quoted evidence, and an index (Crossref, zbMATH) does not
outrank a printed page.

Three sources were re-checked from scratch in this session because the clusters conflicted or
because a transcription looked corrupt:

* the Clay Mathematics Institute Bombieri PDF (fetched fresh, 11 pp., `pdfinfo` + per-page
  `pdftotext`);
* Diaz, JTNB 9 (1997), p. 231 (the on-disk asset rendered at 250 dpi and read as an image);
* the on-disk Connes–Consani "Riemann-Roch strategy" PDF title page
  (`fetched/y-06-connes-consani-2019-riemann-roch-strategy-complex-lift-scaling-site.pdf`).

---

## 1. Disagreements and how they were settled

Five sources were checked by more than one cluster. Two produced real conflicts; three produced
agreement plus complementary findings. All five are recorded, because the agreements are
load-bearing corroboration and should not be re-litigated.

### D1. Bombieri, *Problems of the Millennium: the Riemann Hypothesis* (Clay, 2000) — CONFLICT, settled for `m1-1`

| | `m1-1` (cluster M1-1) | `M1-2` (rider item) |
|---|---|---|
| page of the algebraic-index-theorem passage | **REFUTED** "pp. 9-10"; entirely on **p. 9** | "its page range ('pp. 9-10') **CONFIRMED verbatim**" |
| length of the PDF | **11 pages** (`pdfinfo`) | "10 pp." |
| printed title | "Problems of the Millennium: **the** Riemann Hypothesis" (lower-case *the*) | ready-to-paste uses "**The** Riemann Hypothesis" |

**Settled this session against the file itself.** Fetched
`https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf` (159,267 bytes; `pdfinfo`:
`Pages: 11`, `CreationDate: Wed Aug 30 17:19:01 2000`).

* `pdftotext -layout -f 9 -l 9` returns a page whose running head reads
  `PROBLEMS OF THE MILLENNIUM: THE RIEMANN HYPOTHESIS   9` and which contains, in order and in
  full: the Weil-negativity sentence; the **Algebraic Index Theorem** statement; the Severi
  paragraph, including "The proof uses the Riemann-Roch theorem on X and the finiteness of
  families of curves on X of a given degree; no other proof by algebraic methods is known up to
  now, although much later several authors independently rediscovered Severi's argument."; the
  Hodge paragraph; the Montgomery/Odlyzko/Rudnick–Sarnak paragraph; and **footnote 8** entire.
* `pdftotext -layout -f 10 -l 10` begins `10    E. BOMBIERI` / "here in the realm of conjectures
  and speculation…" and then runs into the bibliography.
* Page 1 prints `Problems of the Millennium: the Riemann Hypothesis / E. Bombieri`.

**VERDICT: `m1-1` is right on all three points.** Cite **p. 9**, never "pp. 9-10". The PDF is
**11 pages**. The printed title carries a lower-case "the". `M1-2`'s content quotations are
accurate and its own evidence is labelled "Page 9" — its verdict line is a transcription slip, not
a second reading, and it must not be used to keep "pp. 9-10" alive.

**Also settled here:** `M1-1`'s URL correction stands. `https://…/2022/06/riemann.pdf` 404s;
`https://…/2022/05/riemann.pdf` is the live file (HTTP 200, fetched twice this session).

**Bonus corroboration for M0-2.** Bombieri's own bibliography, printed on p. 10, reads
`[Den] C. Deninger, Some analogies between number theory and dynamical systems on foliated spaces,
Proc. Int. Congress Math. Berlin 1998, Vol. I, 163–…`. That is a **fourth independent witness**
(alongside the Documenta article page, zbMATH and Crossref) for the printed pagination **163-186**,
against the 23-46 electronic-offprint pagination that Deninger's own 2002 bibliography and EUDML
print. M0-2's instruction — do not "fix" 163-186 to 23-46 — is reinforced.

### D2. Diaz, JTNB 9 (1997), p. 231 — the four-exponentials reduction — CONFLICT, settled for `SEED-2`

* `SEED-2` quotes: "Pour faire le lien avec (C4E) il suffit de prendre `x₁ = 1`,
  `x₂ = (log α₁)/2iπ`, `y₁ = 2iπ`, `y₂ = log α₂`", read off a 200 dpi rendering, and warns
  explicitly that the Numdam OCR layer silently drops math tokens — naming `/2iπ` as one of them.
* `SEED-3` §5.6(ii) quotes the same sentence as "`x₁ = 1`, `x₂ = log α₁`, `y₁ = 2iπ`,
  `y₂ = log α₂`" — the `/2iπ` missing.

**Settled this session against the primary.** Rendered p. 231 of the retained asset
`assets/diaz-1997-jtnb9-quatre-exponentielles-numdam.pdf` at 250 dpi and read the image. The
printed line is:

> Pour faire le lien avec (C4E) il suffit de prendre x₁ = 1, **x₂ = (log α₁)/2iπ**, y₁ = 2iπ,
> y₂ = log α₂.

**VERDICT: `SEED-2` is correct; `SEED-3`'s transcription is OCR-corrupted and must not be pasted.**
The mathematics confirms it independently: with SEED-2's substitution the four exponentials
`exp(x_i y_j)` are `1, α₂, α₁, exp((log α₁)(log α₂)/2iπ)` — which is exactly the quadruple the
reduction needs. SEED-3's version yields `exp(2iπ · log α₁)`, which is not.

The same rendering also confirms, verbatim on p. 231, under the running head
`Conjectures modulaires de D. Bertrand    231`: the statement labelled **(C4E faible)**; the
sentence "D. Bertrand propose dans [2], §5, plusieurs conjectures pour la fonction modulaire J…";
and **(CDB)** as *Diaz's own* label for Bertrand's second conjecture. `SEED-2` is corroborated on
every point it makes about this page.

### D3. Connes–Consani, *The Riemann-Roch strategy* — three renderings across three clusters, settled

| cluster | title as proposed |
|---|---|
| `M0-5` (SHOULD 14) | "The Riemann-Roch strategy**.** Complex lift of the **s**caling **s**ite" (zbMATH, "printed form") |
| `M1-5` (MUST 3) | "The Riemann-Roch strategy**:** Complex lift of the **S**caling **S**ite" (Springer title/subtitle) |
| `SEED-4` (MUST 7) | "The Riemann-Roch strategy**:** **c**omplex lift of the **S**caling **S**ite" |

**Settled this session against the author's own title page.** `pdftotext -f 1 -l 1` of
`fetched/y-06-connes-consani-2019-riemann-roch-strategy-complex-lift-scaling-site.pdf`
(= arXiv:1805.10501v1) prints, on two lines:

```
The Riemann-Roch strategy
Complex lift of the Scaling Site
```

Springer's own Crossref record agrees on the capitalization: `title: "The Riemann–Roch strategy"`,
`subtitle: "Complex lift of the Scaling Site"`.

**VERDICT: adopt `The Riemann-Roch strategy: Complex lift of the Scaling Site`, one form in every
file.** zbMATH's lower-case "scaling site" is zbMATH's own sentence-casing — visible all over this
pass (it sentence-cases Kuna–Lebowitz–Speer, the Deninger ICM title, the Selecta title, and prints
"Lecture on zeta functions and motives" for Manin's *Lectures*) — and is not evidence about the
printed page. The colon is the correct normalization of Springer's title/subtitle split.

All three clusters agree on every other field: Springer, Cham, **2019**, pp. **53-125**,
doi:10.1007/978-3-030-29597-4_2, arXiv:1805.10501, six editors (Chamseddine, Consani, Higson,
Khalkhali, Moscovici, Yu). `SEED-4`'s extra finding stands and must be honored: **CC's own later
bibliographies date the chapter "Springer (2020)" — that is the online-first date. Print 2019.**

### D4. arXiv:1507.05818 / *The scaling site* — no field conflict; two complementary findings, both must survive

`M0-5` and `SEED-4` agree exactly: **C. R. Math. Acad. Sci. Paris 354 (2016), no. 1, 1-6;
doi:10.1016/j.crma.2015.09.027**, with the journal styling the title *The scaling site* (lower
case) and arXiv styling it *The Scaling Site*. Both also agree the report's pairing of
arXiv:1507.05818 with the *Selecta* article is wrong — 1507.05818 is the C. R. note,
arXiv:1603.03191 is the *Selecta* article. Both note Crossref alone would suggest 2015
(online-first 2015-11-03); the issue year 2016 comes from zbMATH and the publisher page.

Two findings that look like they collide and do not:

* `M0-5`: the scaling site is `[0,∞) ⋊ N^×` — the acting monoid is **N^×**, not R*₊.
* `SEED-4`: the **per-prime object** is `C_p = R*₊/p^Z`, a real circle of length log p.

These are different objects — the site's semidirect factor and the periodic orbit of the scaling
flow. Both are verified, and both must go into the note.

**Trap to record, so nobody "corrects" it:** the DOI prefix `10.1016` is Elsevier's, but Crossref
now serves the record under MathDoc/Centre Mersenne (C. R. changed publisher in 2020 and kept the
legacy prefixes). A DOI-prefix/publisher mismatch here is legitimate.

### D5. arXiv:1603.03191 / *Geometry of the scaling site* — agreement

`M0-5` and `SEED-4` agree field for field: **Selecta Math. (N.S.) 23 (2017), no. 3, 1803-1850;
doi:10.1007/s00029-017-0313-y; arXiv:1603.03191.** Both note the arXiv record carries no
journal-ref, so the preprint↔article identification rests on identical title, authors and abstract
plus Crossref and zbMATH. Nothing to settle.

### D6. Milne, arXiv:1509.00797 — agreement on fields, one provenance point settled for `M1-2`

`m1-1` and `M1-2` agree on the corrected values: **B. Segre, Ann. Mat. Pura Appl. (4) 16 (1937),
157-163** and **J. Bronowski, J. London Math. Soc. 13 (1938), 86-90**, independently confirmed by
Crossref and zbMATH and matching Milne's printed bibliography.

They differ on *where the corruption comes from*:

* `m1-1` attributes "G. Bronowski" / "1958" to a "competing transcription" (the denisevellachemla
  retranscription).
* `M1-2` read **Grothendieck's own 1958 printed bibliography** off the De Gruyter scan at 420 dpi
  and found it there: `[1] G. Bronowski, … J. London Math. Soc. 13 (1958), 86.` It also found
  Grothendieck's Segre start page (**167**) wrong; the true first page is 157.

**VERDICT: `M1-2`'s reading is primary and supersedes.** The corrected fields are the same either
way, but the executing session must not repeat `m1-1`'s stated reason: anyone who consults
Grothendieck's original expecting it to be clean will reintroduce "G. Bronowski (1958)".

**Cross-check that survives, and is worth keeping:** the report's "Milne footnote 14" pointer is
*right* for **Kani** (footnote 14 is the Castelnuovo/Kani footnote — `m1-1`, consistent with
`M1-5`'s Kani item) and *wrong* for **Segre/Bronowski**, who are in **footnote 16**.

### D7. arXiv:1810.08843 (Chirre–Gonçalves–de Laat) — agreement

`A4-2` and `A4-3` agree: Corollary 3 gives `N_d ≥ (0.8477+o(1))N` under RH and `(0.8486+o(1))N`
under GRH; the same paragraph attributes 0.8051 to Farmer–Gonek–Lee and 0.8466 to Bui–Heath-Brown.
`A4-2` supplies the DOI that `A4-3` omits: **10.1016/j.aim.2019.106926** (2019 stem, 2020 volume —
Elsevier online-first; not an error). Carry it.

### D8. Waldschmidt, AWS Lecture 5, Conjectures 5.34 / 5.35 — independent agreement, and it is the strongest refutation of the pass

`SEED-2` (working from Diaz and from ODP) and `SEED-3` (working from the AWS PDF itself) reached
the same verdict independently: 5.34 and 5.35 are **D. Bertrand's two conjectures on the modular
function J**, not four-exponentials statements. In the same document 4EC is **Conjecture 5.11** and
strong 4EC is **Conjecture 5.8**; the *weak* four-exponentials conjecture is absent from it
entirely (`grep "weak four"` returns zero hits in AWS Lecture 5, in *Open Diophantine Problems*,
and in Diaz 2007). Two agents, two routes, one answer. Treat as settled.

### D9. Bertrand, *Theta functions and transcendence* — `SEED-2` supersedes `SEED-3`'s caveat

`SEED-3` §5.6 records the bibliographic form as "taken from Waldschmidt's AWS Lecture 5
bibliography… **not** independently verified against Crossref/zbMATH in this pass". `SEED-2` did
verify it, twice: Crossref on doi:10.1023/A:1009749608672 and zbMATH Zbl 0916.11043, plus a
Crossref listing of the whole issue placing Bertrand at 339-350 between Kim–Kim–Raghavan (333-337)
and Mignotte–Roy (351-356). **Ramanujan J. 1 (1997), no. 4, 339-350 is verified; drop SEED-3's
caveat on the fields.** The §5 *content* locator remains unverified — see §3.

### D10. Alaoglu–Erdős 1944 — `SEED-5` supersedes `SEED-2`'s secondary route

`SEED-2` confirmed the two-prime germ through Waldschmidt's *LIL* (secondary). `SEED-5` downloaded
the free AMS PDF and read it: the question is stated **explicitly, twice** — p. 449 ("If p and q
are different primes, is it true that p^x and q^x are both rational only if x is an integer?") and
p. 455, where **Siegel's three-prime result** is recorded. Use `SEED-5`'s two-page pin; it is
stronger than the report or `SEED-2` realized, and it is the four-vs-six-exponentials split in
1944.

### D11. Mattuck–Tate 1958 — agreement across four clusters, with one caveat

`m1-1` (via Milne's bibliography), `M1-2` (via Grothendieck's printed `[4]`), `M1-3` (via Ancona's
`[MT58]`) and `M1-5` all give **Abh. Math. Sem. Univ. Hamburg 22 (1958), 295-299**. Three
independent *published bibliographies* agree. Note, however, that **no cluster checked it against
Crossref or zbMATH directly**. Good enough for a bibliography entry as it stands; if a DOI is
wanted, verify first rather than constructing one.

---

## 2. REFUTED items — do not execute as written

### 2A. The action, or a load-bearing field inside it, is false

1. **`SEED-3-MUST-10b` — Waldschmidt, AWS Lecture 5 (whole item REFUTED).**
   The report's claim that Conjectures 5.34/5.35 are "the printed statement of Bertrand's weak
   four-exponentials conjecture and of 4EC" is false. **Do not execute.** Replacement: for 4EC
   cite the published `SEED-3-MUST-10a` (Waldschmidt, *Open Diophantine Problems*, Mosc. Math. J.
   4 (2004), no. 1, 245-305, Conjecture 3.7) and drop the AWS cite; for the *weak* form the AWS
   notes do not contain it at all, and the correct primary is Diaz, JTNB 9 (1997), no. 1, p. 231,
   "(C4E faible)". If an AWS citation is still wanted for some other purpose, the corrected string
   in the `SEED-3` report carries the right conjecture numbers (4EC = 5.11, strong 4EC = 5.8).

2. **`CC25-arXiv-2501.06560` — the seed note's lineage sentence (whole item REFUTED).**
   "The per-prime elliptic-curve analogue first appears here, January 2025" is wrong by
   **9 years 5.7 months**. It first appears in arXiv:1507.05818v1, 21 July 2015 (= C. R. Math.
   354 (2016), no. 1, 1-6), long version *Selecta* 23 (2017), no. 3, 1803-1850; 2501.06560 itself
   cites the *Selecta* paper for it. **Do not merely delete the pointer** — replace it: this
   paper's actual contribution is a geometric generalization of class field theory, a functor from
   finite abelian extensions of Q to finite covers of X_Q, with the monodromy of the length-log p
   periodic orbits matching the Galois action of Frobenius at p.

3. **`CGdL20` — "inequality (7) is the published convex-programming form of A4's Lemma 4.2
   device".** Display (7) contains no convex or semidefinite programming; it is elementary integer
   arithmetic, `(m-2)(m-3)/m ≥ 2·1_{m=1}`, summed over zeros, and the authors credit the
   combination to "an argument of Ghosh". Their SDP is in Section 3, on the Cohn–Elkies-type
   auxiliary-function class. **Write instead:** "the same per-multiplicity integrality device, at
   the reciprocal-weighted third level" — and note that A4's Lemma 4.2(a) is the *unweighted
   second* level.

4. **`BGSTB24` — "the same authors' second-moment sequel, arXiv:2501.14545".** That paper is
   *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and
   Critical Zeros*; its own abstract treats the **horizontal** distribution of zeros under a
   narrow-vertical-box hypothesis, not second moments. **Strike "second-moment"**; keep "the same
   authors' sequel" with a neutral description, and record that it is still unpublished (v1 24 Jan
   2025, v2 21 Nov 2025).

5. **`M0-MUST-1` — Borger, arXiv:0906.3146.** The first half of the quotation ("a Λ-structure on a
   flat Z-space *is* a commuting family of Frobenius endomorphisms indexed by the primes") is
   verbatim in the paper, twice (intro p. 2; §1.1 p. 6). The second half — "with ψ_m ψ_n = ψ_mn and
   primitivity at the primes by unique factorization" — **is not printed in this paper** and must
   not be quoted against it. It is true mathematics; it is not a sentence of arXiv:0906.3146,
   which defers the general-m construction to its reference [7]. Cite §1.1 for (PF2); cite §6
   ("the Λ-ideals I_m are ordered by divisibility on m") for the composition law, or attribute the
   law elsewhere.

6. **`M0-MUST-5` — Deninger, "Weil-"cohomology impossibility.** "Its item 2.3 is a trace-reading
   axiom" is false: **2.3 is the spectral / Hilbert–Pólya axiom; the trace axiom is 2.4.** And the
   property Theorem 2.13 actually refutes is **2.12** (the Galois-equivariant order-of-vanishing
   property), not 2.3 and not 2.7. Any sentence saying Deninger rules out a real theory satisfying
   "his trace axiom" is wrong twice over. Also fix the title punctuation:
   `There is no "Weil-"cohomology theory with real coefficients for arithmetic curves` — the
   closing quotation mark sits immediately after `Weil-`, and the scare quotes are load-bearing.
   Also: the paper is now published — Ann. Sc. Norm. Super. Pisa Cl. Sci. (5) 25 (2024), no. 3,
   1717-1725; doi:10.2422/2036-2145.202204_005 — so "arXiv v2, to appear" is stale.

7. **`M0-MUST-6a` and `M0-MUST-6b` — the two Connes–Consani Riemann-Roch papers.** The brief's
   paraphrase, that these papers **supply an h⁰_θ**, and specifically the M4-level theta-effectivity
   input `h⁰_θ(D) ≥ deg D + O(1)`, is false and must not be executed. Connes and Consani prove an
   Euler-characteristic identity with an **integer-valued** dimension over the sphere spectrum, for
   Spec Z alone, and they say in their own introduction that the log-theta number as a dimension
   "remains virtual … for the obvious reason that it outputs real numbers rather than integers".
   What *is* true, and is what the report itself asked for, is that §7's flat "a substrate-level
   input no current object supplies" is overstated **as an absolute** — a Riemann-Roch theorem for
   Arakelov divisors on Spec Z-bar, with two cohomologies, integer dimensions and Serre duality,
   is in print. The DMV-violated M4 input survives. Also: the overline spans **Spec Z**, not Z —
   set `$\overline{\mathrm{Spec}\,\mathbb{Z}}$`, never `\mathrm{Spec}\,\overline{\mathbb{Z}}`.
   Also add the arXiv id the report omitted for 6b: **arXiv:2306.00456**.

8. **`M0-MUST-8` — Conrey–Li, IMRN 2000.** "The published exemplar of §6.3's over-breadth move, **on
   the same witness function χ₄**" must not be executed as written. de Branges' conditions fail for
   **ζ itself** too (the 34th zero; and Sarnak's numerics-free argument for the F(W) form, which
   moreover covers *every* Dirichlet character). Conrey–Li is therefore not an exemplar of a filter
   separating ζ from χ₄ — which is what §6.3 does. The honest parallel is the genre. Two further
   constraints: say **"de Branges' positivity conditions"** explicitly (a referee will otherwise
   read "Conrey and Li, positivity" as Li's λ_n criterion); and if a narrower parallel is wanted,
   write "including on L(s, χ₄)", not "on the same witness function χ₄".

9. **`M0-SHOULD-15b` — Montgomery–Vaughan, MNT I.** "§1.2" is wrong: §1.2 is "Analytic properties
   of Dirichlet series" (pp. 11-18). The completely-multiplicative Euler product is
   **§1.3, "Euler products and the zeta function", pp. 19-30, Theorem 1.9, p. 20**. Note also that
   MV say **"totally multiplicative"**, not "completely multiplicative"; if the note's own sentence
   uses "completely multiplicative", Apostol is the closer terminological match and should lead.

10. **`M1-MUST-1` — Milne.** "The word 'circular' returns zero hits" is **CONFIRMED** (zero hits in
    both PDFs, both extractions). "He uses **'avoid the Weil conjecture'** instead" is **false**:
    the string "avoid" occurs **zero** times in the paper, in any inflection, in either extraction
    of either PDF. Do not put that phrase in the note as a Milne quotation. Use instead Aside 1.8
    ("the proof is purely geometric and takes place over an algebraically closed field") and the
    Grothendieck sentence ("… which itself is a simple consequence of the Riemann-Roch theorem for
    surfaces"). The *framing* as a non-circularity certificate is the note's own contribution —
    which is good for the note's novelty position, and should be said that way.
    Bibliographically the entry is materially incomplete: **Volume II, ALM 35 part 2, pp. 487-565**,
    editors **Ji, Oort and Yau**, and doi:10.4310/ICCM.2016.v4.n2.a4 (which belongs to the ICCM
    *reprint*, not to the book — punctuate so a reader cannot misattach it).

11. **`M1-MUST-2` — Bombieri, CMI.** "pp. 9-10" is REFUTED — **cite p. 9** (settled in D1 against
    the file). The URL in the brief (`/2022/06/`) 404s — use `/2022/05/`. Two riders: Bombieri's
    Severi 1906 is *Sulla totalità delle curve algebriche tracciate sopra una superficie
    algebrica*, Math. Ann. 62 (1906), 194-225, a **different** 1906 paper from the Castelnuovo 1906
    that Milne cites — do not conflate them; and the printed title carries a lower-case "the".

12. **`M1-MUST-6` — Kleiman 1968.** **Remark 3.10 does not support the claim attached to it.** It is
    a characteristic-zero remark about homological versus numerical equivalence and never mentions
    RH, the zeta function, or finite fields. **Theorem 4.7 alone** carries "Hodge-type positivity is
    logically upstream of RH". The remark the note actually wants is **Remark 4.5** — Kleiman's own
    dependency ledger, "this derivation does not depend on any unproved conjectures". Replace 3.10
    with 4.5, or cite 3.10 separately for its own narrower point. Also extend the imprint: series
    **Advanced Studies in Pure Mathematics 3**, and co-publisher **Masson & Cie, Paris**; and do
    **not** write Grothendieck and Kuiper as volume editors — they are *series* editors.

13. **`M1-MUST-7` — Ito, Ito and Koshikawa.** "The published **non-circularity audit**" reverses the
    direction of the source. Remark 1.3 says the opposite: "However, we did **not** attempt to avoid
    the Weil conjecture in our proof of Theorem 1.2." Reword to: "Ito, Ito and Koshikawa flag the
    same dependency question explicitly, and answer it in the negative for their own proof." That is
    *stronger* for the note — it shows the question is recognized **and** that answering it is not
    automatic. (Good news alongside: the report's "volume/pages from search-surfaced AMS metadata
    only" caveat can be **lifted** — zbMATH confirms J. Algebraic Geom. 34 (2025), no. 2, 299-330.
    Crossref alone would not have settled it: its record has volume, issue and page all null.)

14. **`M1-MUST-8` — Ancona.** Two refutations. (i) "§1 publishes the note's §9 lineage repair
    **verbatim**" is false — nothing is quoted from one text in the other; Ancona publishes the same
    *priority record* in his own words. (ii) Ancona makes **no** statement about who first gave a
    proof independent of the Weil conjectures. He says only that the Segre/Bronowski proof is
    "algebraic … valid in any characteristic"; `grep -c -i circular` returns 0 over his full text,
    and he never writes "independent" or "does not use". **Do not attribute a non-circularity claim
    to Ancona.** Quotation trap: he writes "the **Lang–Weil estimate**", not "the Weil bound" and
    not "the Riemann hypothesis for curves" — quote it as written; silently upgrading it would be a
    real misquotation in a note about dependency bookkeeping.

15. **`Wink04` — Winkelmann.** Three refutations, all executable errors:
    * **"his §7 Schanuel argument"** — the paper has **six** sections. The Schanuel argument is
      **§3.2, Proposition 3, p. 14**. A "§7" citation is uncheckable.
    * **"Theorem 2 is the case where Γ ∩ SL₂(R) is cocompact"** — Theorem 2 assumes only
      **Zariski-dense**; cocompactness enters in §5 (Prop. 5, Cor. 3).
    * **"Winkelmann states the criterion in 'iff' form"** — he states and uses **one direction
      only** (necessity). The converse follows in one line from his **Lemma 7**, which *is* an
      equivalence, but he never remarks on it. Correct wording: "Winkelmann derives the necessity
      …; the sufficiency is immediate from his Lemma 7, which is stated as an equivalence, though he
      does not remark on it."
    Also: the author prints **Jörg** (umlaut); the title must not be pasted from Crossref or
    Cambridge Core, both of which render a spurious `Γ..` (a publisher-side TeX artifact).

16. **`SEED-3-MUST-10a` — Waldschmidt, ODP.** "Conjecture 3.7 **is** the matrix form of 4EC" is
    wrong as a pointer. Conjecture 3.7 as numbered is 4EC in **exponentials** form; the 2×2
    matrix-of-logarithms restatement is the **unnumbered paragraph immediately after it**, same
    printed page 269. Cite them together:
    "[Wal04, Conjecture 3.7 and the matrix restatement following it, p. 269]".

17. **`MUST6b-arXiv-1507.05818` — the per-prime object.** "An analogue of an elliptic curve **over
    C**, i.e. the Tate curve C*/p^Z" is false. The 2015 object is **C_p = R*₊/p^Z**, a real circle
    of circumference log p carrying a characteristic-one structure sheaf, with Jacobian
    **Z/(p-1)Z** and a **real-valued** Riemann-Roch theorem. Connes and Consani call it a "variant
    … of the classical Jacobi description C*/q^Z" — an antecedent, explicitly modeled on it, not
    equal to it. The complex Tate curve E_p = C*/p^Z enters the CC program in **June 2026**
    (arXiv:2606.06604), where C_p is identified as the connected component of its real locus and
    E_p decomposes as C_p × X̃_∞.

18. **`CC26-arXiv-2606.06604` — the title-truncation mechanism.** The conclusion is right (keep
    "and the Fargues-Fontaine curve"); the **stated reason is wrong and must be amended wherever it
    is recorded**. It is *not* that the arXiv API truncates at a TeX macro while the abs page has
    the full title: the abs-page `<h1>`, the `citation_title` meta tag, the API, the PDF's own
    metadata and zbMATH **all** carry the short form. The clause survives only on the typeset title
    page and in arXiv's HTML rendering of the LaTeX `\title{}`. Add a one-line note saying so, or
    the next person to re-check will "fix" the citation back to the short title.

19. **`MUST7-CC-RiemannRoch-Strategy` — the equivalence relation.** "The plain isogeny relation on
    elliptic curves" is wrong. It is the relation generated by isogenies of **triangular** elliptic
    curves (their Definition 6.4), and CC note explicitly that multiplication by n **fails** the
    triangular condition unless n = ±1. Say "triangular".

20. **`RS14` — Rosen–Shnidman.** Two things. The paper **has not appeared in a journal** (zbMATH:
    "Preprint, arXiv:1402.2233 [math.AG] (2014)"; Crossref: no record) — add no journal-ref. And
    Rosen and Shnidman **do not claim** Proposition 2.3: they preface it "The following result …
    is well-known." Cite it as **"see e.g. [RS, Prop. 2.3]"**, never "due to [RS]".

21. **`AE44` — Alaoglu–Erdős.** The question is **not** phrased as "is log p / log q rational". It is
    phrased multiplicatively: "If p and q are different primes, is it true that p^x and q^x are both
    rational only if x is an integer?" (p. 449). The two are equivalent; if the note paraphrases, it
    must paraphrase honestly. Also: pin **both** p. 449 and p. 455 — p. 455 records Siegel's
    three-prime result, which is the other half of the four-vs-six-exponentials split. Orthography:
    the printed article and Crossref set "Erdös"; modern house style is **Erdős**.

### 2B. Not refuted, but must not be executed in the report's words

These would put a false or overstated sentence into a paper if pasted literally.

* **`M0-MUST-2` (Geometry of the arithmetic site).** The composition law is **conditional** — it is
  `Ψ(λ)∘Ψ(λ′) = Ψ(λλ′)` when λλ′ ∉ Q and when λ, λ′ are both rational, but
  `Ψ(λ)∘Ψ(λ′) = Id_ε ∘ Ψ(λλ′)` when λ, λ′ are irrational with λλ′ ∈ Q. Do not present a clean
  semigroup law. Differentiator (a) as worded ("their index monoid is R*₊") is attackable — the
  paper also carries an N^×-indexed Frobenius family on the structure sheaf. Defensible form: the
  Frobenius **correspondences on the square**, the objects whose composition law Thm 1.2 / 7.7
  prove, are indexed by the divisible group R*₊. Also: the paper hyphenates "semi-ringed topos".
* **`M0-MUST-3` (Connes, essay).** The `D.ξ₀ + D.ξ₁ > 0` statement is item 2 of an unlabeled
  three-item list introduced as "One needs three basic facts ([62])" — say **"the second of the
  three basic facts"**, not "the numbered basic fact". "Polarized" is the note's word, not
  Connes's. The essay hyphenates "Riemann-Roch" with an ASCII hyphen. And the on-disk file is the
  **arXiv v1 preprint paginated 1-32**, so its folios are *not* the book's — pin-cite by section
  (§2.3, §4.3.1, §4.3.2) or say "arXiv:1509.05576v1, p. N".
* **`M0-MUST-4` (Diamond–Zhang).** Clean, but if the note credits the *oscillation construction*,
  Theorem 17.14 descends from **both** Zhang 2007 and Diamond–Montgomery–Vorhauer 2006 — name both.
* **`M0-MUST-7` (Deninger, ICM 1998).** The verb "**IS**" over-identifies. Deninger's setting is
  leafwise cohomology of a foliated dynamical system; the note's §3.3 is about counting data of an
  arithmetic correspondence in a Yuan–Zhang-style calculus. Same *move*, not the same statement.
  Soften to a precedence claim. "In print for 28 years" survives (1998 → 2026).
* **`M0-MUST-10a` (Banaszak–Uetake).** The equivalence is to **RH plus simplicity of all nontrivial
  zeros**, not to RH alone (2015 Thm 5.4; 2021 §1, in the authors' own words). Print the rider —
  it is sharper and more honest.
* **`M0-SHOULD-12` (Connes–Consani–Marcolli, *Fun with F₁*).** The word **"graph" appears zero
  times** in the paper. CCM work with the endomorphism σ_n on the pro-variety μ(∞) = lim Spec
  Z[Z/n], not with a graph correspondence on P¹ × P¹ — the graph packaging is the m0 note's own.
  And literal coincidence with the classical Frobenius correspondence is asserted only for
  **n = p^ℓ over a perfect field of characteristic p > 0** (Thm 6.2(b)); for general n the claim is
  the weaker §6.1 one.
* **`M0-REPAIR-BlomerLeung`.** The repair itself is confirmed ("monoid" = zero hits in **both** v1
  and v2, hyphenation-guarded) and must be executed: rewrite the m0 note's two occurrences of
  "Blomer–Leung monoid converse" to "Blomer–Leung beyond-endoscopy converse theorem". BARRIER-ZOO
  I.1 already attributes it correctly and needs no change. Separate constraint: Blomer–Leung prove
  this for **GL(3)**; Davenport–Heilbronn is degree 2. **Do not write that Blomer–Leung "exclude
  Davenport–Heilbronn."** Keep the "sharpest formal home of the *shape* of the exclusion" hedge.
* **`M1-MUST-4` (Grothendieck 1958).** Two corrections. (i) The mapping "(2.3) = (IN5)" is wrong:
  (IN5) is folded into his **(2.1)** (the passage from the Riemann-Roch *equality* to the
  *inequality* is "drop h¹ ≥ 0" plus Serre duality); his (2.3) has **no** counterpart in the note's
  (IN1)-(IN7). Correct mapping: (2.1) = (IN1)+(IN2)+(IN5); (2.2) = (IN2); (2.3) = unlisted;
  (2.4) = (IN3). (ii) "needs **no** positivity hypothesis on D whatsoever" is overstated — `D² > 0`
  *is* a positivity hypothesis, on the self-intersection. Print: "assumes only D² > 0 — no
  ampleness, no hyperplane section, no effectivity, and no sign condition on D." (iii) The optional
  "drop (IN4)+(IN7)" is well founded on the Grothendieck side but is a **re-routing, not a
  deletion**: §6 still needs m(ξ₁+ξ₂) very ample, which is the Segre-embedding fact (IN7)'s own
  gloss already names. Bill it that way.
* **`M1-MUST-5a` / `M1-MUST-5b` (Segre 1937, Bronowski 1938).** "Valid in **any characteristic**"
  must be **attributed, not asserted**: neither zbMATH review nor Milne's footnote 16 says it. The
  only primary source that does is Grothendieck, p. 208 — "valables en toute caractéristique".
  Write it as attribution. And the dating is one year short for Segre: 1937 → 1958 is 21 years,
  1937 → 1948 is 11. Use "two decades / a decade", or give the years.
* **`M1-RIDER-Severi1906 + Bombieri Clay`.** Do **not** call the Weil-free routes "multiple
  independent" while citing Bombieri: on the page being cited he says "no other proof by algebraic
  methods is known up to now, although much later several authors independently rediscovered
  Severi's argument." Safe wording: "several published Weil-free derivations, which Bombieri regards
  as rediscoveries of Severi's 1906 argument."
* **`SEED-MUST-2` (Diaz 1997).** Two constraints. Diaz files **Proposition 3(1) under (C4)**, not
  under (C6)/(C4E faible) — (C4) is equivalent to (C6) by his Théorème 1, so the family is right but
  the placement is not what the paper says. And **"weak four-exponentials conjecture" is not a term
  of art** — Diaz's label is "(C4E faible)" and he describes it only as "le cas particulier de (C4E)
  que vise D. Bertrand"; Waldschmidt never writes "weak four exponentials" (zero hits in ODP, AWS
  Lecture 5 and LIL). Also note "(CDB)" is Diaz's own notation, not Bertrand's.
* **`SEED-3-MUST-5` (Barré-Sirieix–Diaz–Gramain–Philibert).** Cite for the **strengthening**, not as
  a repair: the §7 Gelfond–Schneider argument already suffices for End(E_p) = Z and is more
  elementary. BSDGP gives the strictly stronger `j(E_p)` transcendental. And write **q = p⁻¹**
  explicitly (or note p^Z = (p⁻¹)^Z) when invoking the theorem — writing E_p = C^×/p^Z invites the
  reading q = p, for which |q| > 1 and the hypothesis fails as stated.
* **`SEED-1` `Wink04` — the added-value claim.** "We sharpen his result to the exact Hom group and
  isogeny degree" needs calibration. Not new: Theorems 1-3 of the note; the criterion
  `Hom ≠ 0 ⟹ 4π²/(log λ_i log λ_j) ∈ Q`; the real/imaginary separation; the division of two
  relations; the three-curve run; the "at most one other curve" conclusion — all Winkelmann,
  **15 April 2002** (present in v1). Not new either, though unremarked by him: the converse. Not in
  Winkelmann at all (`grep`: zero hits for "Hom", "rank", "isogeny degree"): the Hom group itself
  and its rank, the minimal-isogeny degree, and the prime-indexed specialization. Honest framing:
  "we make explicit, in the prime-indexed case, the Hom group and isogeny degree behind a criterion
  due to Winkelmann" — an explication, not a sharpening of a theorem. A claim of priority over
  Theorems 1-3 is not available. Two quoting traps: the sentence "for each of these curves there is
  at most one other curve in this family to which it is isogenous" is **v3 (2003)** wording — v1
  says "at most two can be isogenous"; and the isogeny lemma is **lemma 4 in v1 = lemma 7 in v3**.
* **`FGL-0.8051`.** The disambiguation is warranted and must be written, but: cite the **published
  2014 three-author JLMS version** (the 2008 two-author preprint arXiv:0803.0425 has 0.6544, not
  0.8051), and do not describe 0.8051 as a current record — it is superseded by 0.84665
  (Bui–Heath-Brown) and 0.8477/0.8486 (Chirre–Gonçalves–de Laat).
* **`P` (Alpöge–Furman).** No field changes. One clarity risk: "the 17-page v5" reads as an arXiv
  version number, and **there is no arXiv v3+** (exactly v1 and v2). Write "the 17-page local
  revision v5", or equivalent.

---

## 3. UNVERIFIABLE items — cite with a caveat, or drop

Nothing here is known to be wrong. Each is a claim or field that no reachable primary source
settles. The rule for all of them: **either carry the provenance in the text, or drop the item.**

1. **`SEED-MUST-3` — Bertrand, Ramanujan J. 1 (1997), §5.** The **bibliographic fields are verified**
   (D9). The **§5 content locator is not**: the paper is behind Springer's IdP, Semantic Scholar
   reports the abstract elided, zbMATH's web front end is behind Cloudflare, and Bertrand's own
   page carries no publication list. The best evidence is a zbMATH review **written by Diaz
   himself** plus Diaz's own article — not independent. **The report's stated support (Waldschmidt's
   AWS 5.34/5.35) is REFUTED and must not be repeated.** Cite as: "[Bertrand, Ramanujan J. 1 (1997),
   Sect. 5, **as reported by** Diaz, JTNB 9 (1997), 231]". Also: "January 1996" is Diaz's prose; the
   printed conference designation is "International Symposium on Number Theory (Madras, 1996)".
2. **`Ha91` — MR1110396.** MathSciNet is behind a Cloudflare/JS wall; the relay station returns an
   empty shell. A web-search *rendering* reported the number, which is not the database.
   **Recommendation: drop the MR and keep Zbl 0744.11042 plus doi:10.1017/CBO9780511526053.010,
   both verified.** Nothing is lost. (Minor: Haran prints "spec Z", not "spec(Z)" — fix if the
   quotation is claimed verbatim.)
3. **`BL04` — the numbered Birkenhake–Lange statement for NS(A × B).** Not located. No copy on disk;
   Springer's book and chapter pages return HTTP 303 to `idp.springer.com`. **Do not invent a BL
   section number.** Leave the note's deliberate chapter-level citation as is and let Rosen–Shnidman
   Prop. 2.3 carry the precise pointer. (Incidental: the 1st edition, 1992, same Grundlehren 302,
   has the author order **reversed** — Lange, Birkenhake — and that is the edition Rosen–Shnidman
   themselves cite.)
4. **`M0-SHOULD-15a` — the section number inside Apostol Ch. 11, and any theorem number.** Not
   readable from any legitimate primary source this session. **Cite the chapter** (Ch. 11,
   "Dirichlet Series and Euler Products", pp. 224-248). No theorem number has been invented; do not
   invent one.
5. **`M0-MUST-10a` — "the only prior published axiomatization of a Weil-style intersection calculus
   for zeta".** A universal negative over the published literature; no primary source can establish
   it and none was found that does. **Print the hedged form** ("the closest prior work is …"), or,
   if "the only" must stand, attach "as far as we are aware" — and that is the sponsor's call, not
   the verification's.
6. **`M0-MUST-9` — "the standard modern survey of the Davenport–Heilbronn function".** An editorial
   judgment, not a checkable field. All *bibliographic* fields are confirmed. Keep or hedge.
7. **`M0-MUST-7` — "the m0 note's §3.3 Lefschetz-tie axiom **IS** Deninger's conjecture".** See
   §2B. Deninger's conjectural dynamical trace formula is confirmed in print (§3 eq. (6), §4
   eq. (20)-(22), with his own admission that "the formula (20) does not seem to be established");
   the *identification* is not.
8. **`M1-MUST-5a` / `M1-MUST-5b` — "valid in any characteristic" as the papers' own claim.** See
   §2B. The originals were not read (Annali and JLMS both paywalled); the characteristic-freeness
   rests on Grothendieck's 1958 assessment.
9. **`M1-SHOULD-13` — Vainsencher–Voloch as "a further short published **proof**".** The three-page
   article is unreachable (De Gruyter paywall; EuDML 403; GDZ/digizeitschriften serve a JS shell;
   no author copy). Fujita's zbMATH review reports a **sharpened inequality improving Kani**, not a
   re-proof of the bare Castelnuovo–Severi bound. **Soften to "a further short published
   sharpening of the inequality, improving Kani".** All bibliographic fields are confirmed.
10. **`KS66` — "the one-sided Chebyshev–Markov–Stieltjes principle lives in Chapter IV, Section 2".**
    Sourced only from Gilboa–Peled, arXiv:1407.2467 §2; the 1966 book is in copyright and the
    Internet Archive search-inside hosts did not resolve. **Either label the pointer as
    secondary-sourced, or drop the parenthesis and cite the book as a whole** — the A4 sentence
    already works without it. All catalog fields are now verified four ways (LoC MARC, zbMATH,
    Internet Archive/Open Library, Google Books).
11. **`CGdL20` — the numbering "Corollary 3" and "(7)".** Read in arXiv:1810.08843**v2**
    (18 Nov 2019), the final arXiv version, post-acceptance. The typeset Elsevier version is
    paywalled and was not read. Very unlikely to differ; say so rather than gloss it.
12. **`Mon73` — the AMS-canonical expansion "Vol. XXIV" and the imprint "Providence, R.I."**
    `bookstore.ams.org` returned HTTP 403. The entry **as written** is fully verified by zbMATH.
    Do not add the expansion unless someone checks it.
13. **`SEED-3-MUST-5` — the BSDGP theorem statement itself.** Bibliographically primary-verified
    (Crossref + zbMATH); the *statement* was read at one remove, from Waldschmidt's Séminaire
    Bourbaki exp. 824 (Astérisque 245 (1997), p. 108, rendered as an image) and the zbMATH review,
    which agree verbatim. Springer is paywalled. Do not claim the paper's page 1 was read.
14. **`Nes96` — the content (π, e^π, Γ(1/4)).** All bibliographic fields and both DOIs are
    confirmed. The content rests on two zbMATH reviews and the publisher abstract; the paper is
    paywalled and was not read. **Do not upgrade this to "read in the original".**
15. **`NP01` — the chapter DOI suffix `_3`.** Inferred from the Crossref chapter-DOI pattern for
    that book, **not** individually resolved. Resolve it before use, or drop the chapter DOI (the
    book DOI 10.1007/b76882 and all book fields are verified twice).
16. **`SHOULD13-Morishita` — "to appear in Münster Journal of Mathematics".** An author-supplied
    arXiv **comment** only: no arXiv journal-ref, no Crossref record. Also: **single** author, and
    the paper has five versions, the latest 21 January 2026 (zbMATH indexes it under 2026), while
    the report's "August 2025" is the v1 date.
17. **`M0-SHOULD-11` — doi:10.17879/90169642993.** A Universität Münster repository DOI, **not
    Crossref-registered**, and direct resolution through doi.org was blocked by a bot-check
    interstitial. It is attested as this article's DOI by zbMATH and by HAL independently. Keep it;
    record that it was not watched to resolve end to end. There is **no arXiv id** — two searches
    return nothing; the open-access preprint is **HAL hal-02407608**. Do not manufacture an arXiv id.
18. **van der Geer–Schoof and Bost (context for `M0-MUST-6a`/`6b`).** Their journal/series fields
    come from Connes–Consani's own bibliography items [11] and [1] — a secondary source, not
    independently verified. The arXiv titles and authorship are primary.
19. **`M1-MUST-2` — the reprint's internal page.** The 2006 AMS/CMI reprint locus **pp. 107-124** is
    verified (zbMATH). The page *within* the reprint on which the index-theorem passage falls is
    **not** — the book was not obtained. Cite the passage by the CMI PDF's p. 9.
20. **`Thas15` — the volume editor and the place "Zürich".** Crossref names EMS Press as publisher
    and gives no editor on the chapter record. Both are almost certainly right and neither is
    corroborated here. The safe form drops "Zürich" and keeps the DOI.
21. **`M1-MUST-7` / `M1-MUST-8` — numbering against the published texts.** Remark 1.3 is verified in
    arXiv:2206.10086**v1** only (no v2 exists; the AMS text is paywalled). Ancona's §1 and Lemma
    7.10 are verified in arXiv:1806.03216**v3**, which post-dates Springer's online publication by
    four days and is therefore *very likely* the published text — but that is an inference, not a
    verification.
22. **Mattuck–Tate 1958.** Attested by three agreeing published bibliographies; not checked against
    an index. See D11.

---

## 4. Content claims that did not survive

These are the dangerous ones: for each, the report asked that a **sentence be written into a paper**
on the strength of the claim. Ranked roughly by how much damage the sentence would do.

1. **`M1-MUST-7` (Ito–Ito–Koshikawa) — "the published non-circularity audit."** The source says the
   **opposite** of what the note would assert on its authority. A referee who opens Remark 1.3
   catches it in one line. → Reword to "flag the question and answer it in the negative for their
   own proof".
2. **`M1-MUST-8` (Ancona) — "§1 states who first gave a proof independent of the Weil conjectures"
   (and "publishes … verbatim").** Attributes a non-circularity certification to an author who makes
   none. → Ancona certifies **priority and characteristic-independence**, nothing more.
3. **`CC25-arXiv-2501.06560` — "the per-prime elliptic-curve analogue first appears here (January
   2025)."** Off by 9 years 5.7 months; the paper itself cites the 2017 *Selecta* article for it.
   → Replace with its real contribution (the class-field-theory functor).
4. **`SEED-3-MUST-10b` — "AWS Lecture 5 Conjectures 5.34/5.35 are Bertrand's weak
   four-exponentials conjecture and 4EC."** Two independent agents refuted it. → Cite Diaz p. 231
   for the weak form and ODP Conjecture 3.7 for 4EC.
5. **`M0-MUST-6a` / `M0-MUST-6b` — "these papers supply an h⁰_θ" / the M4 effectivity input
   `h⁰_θ(D) ≥ deg D + O(1)`.** Would concede a substantive point that is not conceded by the
   sources — Connes–Consani explicitly call the log-theta number a dimension that "remains virtual".
6. **`M0-MUST-5` (Deninger) — "item 2.3 is a trace-reading axiom."** 2.3 is spectral; 2.4 is the
   trace axiom; and Theorem 2.13 refutes **2.12**. A sentence built on 2.3 is wrong twice.
7. **`M1-MUST-1` (Milne) — "he uses 'avoid the Weil conjecture' instead."** Would put an invented
   quotation in Milne's mouth. The string "avoid" is absent from the paper.
8. **`M0-MUST-8` (Conrey–Li) — "on the same witness function χ₄."** The criterion fails for ζ too,
   so the source does **not** exemplify a filter separating ζ from χ₄, which is what §6.3 does.
9. **`M1-MUST-6` (Kleiman) — "Remark 3.10 supports Hodge-type positivity upstream of RH."** Wrong
   remark; 3.10 never mentions RH, zeta, or finite fields. Use Remark 4.5.
10. **`CGdL20` — "inequality (7) is the published convex-programming form."** (7) contains no
    programming of any kind and is credited by its authors to Ghosh.
11. **`M0-MUST-1` (Borger) — "ψ_m ψ_n = ψ_mn and primitivity at the primes by unique
    factorization."** True mathematics, not a sentence of the cited paper. Do not quote it against
    arXiv:0906.3146.
12. **`Wink04` — "Theorem 2 is the cocompact case"; "his §7 Schanuel argument"; "he states the
    criterion in iff form."** Three separate uncheckable or false pointers in one item.
13. **`MUST6b-arXiv-1507.05818` — "the per-prime object is the complex Tate curve C*/p^Z."** It is
    the real circle C_p = R*₊/p^Z. This is the lineage sentence's load-bearing identification.
14. **`MUST7-CC-RiemannRoch-Strategy` — "the plain isogeny relation on elliptic curves."** It is
    isogeny of **triangular** elliptic curves, and CC say explicitly that plain multiplication by n
    breaks the triangular condition.
15. **`SEED-3-MUST-10a` — "Conjecture 3.7 is the matrix form of 4EC."** Right paper, right page,
    wrong object attached to the number.
16. **`M0-SHOULD-15b` — "MNT I §1.2 carries the completely-multiplicative Euler product."** It is
    §1.3, Theorem 1.9, p. 20.
17. **`M1-MUST-2` — "the passage sits at pp. 9-10."** Settled against the file: p. 9 alone (D1).
18. **`BGSTB24` — "the second-moment sequel."** The sequel is about horizontal distribution.
19. **`RS14` — "the paper has appeared in a journal"; "due to [RS]."** Still a preprint, and the
    authors call the result "well-known".
20. **`AE44` — "the question is phrased as 'is log p / log q rational'."** It is phrased
    multiplicatively.
21. **`CC26-arXiv-2606.06604` — "the arXiv API truncates the title while the abs page has it in
    full."** A mechanism claim recorded in a prior session's note; every arXiv metadata surface
    carries the short title. Amend the note.

---

## 5. Items requiring an inline "(not independently verified)" tag

Fields **inside a citation string** (or a pin-cite) that no primary source settled. Tag them where
they appear, rather than asserting them.

| key | field to tag | what to write |
|---|---|---|
| `SEED-MUST-4a` | Schneider, "Ch. V, end of Sect. 4, Problem 1" and French ed. p. 139 | keep, tagged "(chapter and problem locator per Waldschmidt, *Open Diophantine Problems*, Sect. 3; book not consulted directly)". Series/volume/pagination/translator **are** verified: Grundlehren 81, 150 pp.; French, trans. P. Eymard, viii+151 pp. |
| `SEED-MUST-4b` | Lang, Bourbaki 305 — "a later explicit formulation" | tag as Waldschmidt's characterization. On the page itself 4EC appears as one sentence of wishing ("On voudrait bien réduire d'une unité le nombre 3…"), not as a numbered conjecture. Exposé number, title, date and pp. 407-414 **are** verified. |
| `SEED-MUST-4c` | Lang, Topology 5 (1966), 363-370 — the 4EC formulation | tag "(not read directly; its explicit formulation of the four-exponentials conjecture is reported by Waldschmidt, *LIL*, Ch. 1)". Title, volume, pages and DOI are verified. |
| `SEED-MUST-4d` | Ramachandra — the DOI | doi:10.4064/aa-14-1-65-72 covers **part I only**. It is **two papers** (I, 65-72; II, 73-88), and the 4EC formulation is in **part II, Sect. 4**. Do not attach part I's DOI to part II, and do not construct part II's. |
| `SEED-MUST-3` | Bertrand, "§5" | "(Sect. 5 locator per Diaz, JTNB 9 (1997), 231; the paper itself was not obtained)". |
| `Ha91` | MR1110396 | **drop**. Keep Zbl 0744.11042 + the DOI. |
| `BL04` | any section number | none exists in verified form — keep the citation at chapter level. |
| `M0-SHOULD-15a` | any Apostol section or theorem number | none — cite Ch. 11, pp. 224-248 only. |
| `KS66` | "Ch. IV, Sec. 2" | tag as taken from Gilboa–Peled arXiv:1407.2467 §2, or drop the parenthesis. |
| `CGdL20` | "Corollary 3", "(7)" | tag "(numbering as in arXiv:1810.08843v2)". |
| `M1-MUST-7` | "Remark 1.3" | keep the existing self-tag "(numbering as in arXiv:2206.10086v1)". |
| `M1-MUST-8` | "§1", "Lemma 7.10" | keep "(numbering as in arXiv:1806.03216v3)" and add that v3 = the published text is an inference, not a verification. |
| `M0-SHOULD-11` | doi:10.17879/90169642993 | tag "(Universität Münster repository DOI; not Crossref-registered)". No arXiv id exists — use HAL hal-02407608 or omit. |
| `SHOULD13-Morishita` | "to appear in Münster J. Math." | tag "(author-announced on arXiv; no journal-ref, no Crossref record)". |
| `M1-SHOULD-14` | pages 275-284 | **Crossref/De Gruyter give 275-284; zbMATH gives 275-283.** Print the publisher's 275-284 and record the variance. Title is printed **"Polya"** without the accent in both arXiv and De Gruyter. |
| `M1-MUST-2` | the internal page in the 2006 AMS/CMI reprint | omit it; cite the CMI PDF p. 9. Reprint locus pp. 107-124 is verified. |
| `M1-MUST-1` | doi:10.4310/ICCM.2016.v4.n2.a4 | punctuate so the DOI attaches to the **ICCM reprint**, not the ALM book. |
| `MUST9a-Milne-LFF` | "v1.1, 14 July 2022" | tag as **Milne's own website revision number**, not an arXiv version (arXiv has v1 only, 12 Nov 2020). Do not conflate the two schemes. Also: the PDF's `hyperref` Title metadata carries a stale working title, "Consequences of the Lefschetz standard conjecture" — never let a metadata scrape substitute it. Cite as a preprint; no journal-ref, no DOI. |
| `MUST10d-YuanZhang` | paper II | must be a **second entry**, not folded into the first: still unpublished, arXiv:1304.3539 v2 (2021). And the **published** Math. Ann. paper's title carries **no roman numeral**. |
| `NP01` | chapter DOI `…_3` | inferred, unresolved — resolve or drop. |
| `Thas15` | "K. Thas (ed.)" and "Zürich" | drop both; keep EMS Press and the DOI. |
| `CC26-arXiv-2606.06604` | the title clause "and the Fargues-Fontaine curve" | keep it, with a one-line note that it is absent from **every** arXiv metadata surface and from zbMATH, and present only on the typeset title page and in arXiv's HTML rendering. |
| `Wink04` | the title | do **not** paste from Crossref or Cambridge Core (both carry a spurious `Γ..`). Use the arXiv/zbMATH/PDF form. Author prints **Jörg**. Nagoya Math. J. is hosted by **Cambridge**, not Project Euclid. |
| `M0-SHOULD-16b` | author name and title | **França** (cedilla), and "Riemann **ζ**", not "Riemann zeta". No journal publication — cite as a preprint. |
| `M0-MUST-6a` | the overline | `$\overline{\mathrm{Spec}\,\mathbb{Z}}$`, never `\mathrm{Spec}\,\overline{\mathbb{Z}}`. |
| `M0-6.1-DH1936-II` | "(second paper)" | the printed page carries **"(Second paper)"**; Crossref drops it entirely. Keep it; capitalize knowingly. |
| `M0-MUST-3` | page pins | the on-disk file is the arXiv v1 preprint paginated 1-32, not the Springer chapter (pp. 225-257). Pin by section, or say "arXiv:1509.05576v1, p. N". |
| `GdLL25` | none — but **strike two caveats** | "(Volume/issue/pages not independently verified — AMS page HTTP 403.)" and the line-212 note are both now closed by three sources. Also rename the key **GdLL24 → GdLL25** and sweep for stale `\cite{GdLL24}`. |

**Internal-consistency sweep (arXiv id ↔ paper, DOI prefix ↔ publisher, volume/year).** Every
arXiv id in the pass matches the paper named and the stated v1 date matches its YYMM prefix; every
DOI prefix matches the publisher named. Four apparent mismatches were checked and are **legitimate,
not errors** — do not "fix" any of them:

* `10.1016/j.aim.2019.106926` on a **2020** volume, and `10.1016/j.aim.2025.110716` on a **2026**
  volume — Elsevier stems the DOI with the online-first year.
* `10.1016/j.crma.2015.09.027` on a **2016** issue, and served by **Centre Mersenne** under an
  **Elsevier** prefix — C. R. changed publisher in 2020 and kept the legacy prefixes.
* `10.1090/mcom/4005` deposited 2024 on a **2025** issue — AMS online-first (this is the trap that
  produced the year error; the issue year is 2025 on the AMS's own index).
* `10.1515/crll.1958.200.208`, `…1984.352.24`, `…1988.390.114` — Crossref's legacy Crelle records
  put the **year in the `volume` field and the volume in `issue`**. The citable volumes are 200,
  352, 390. Do not "correct" them to 1958/1984/1988.

---

## 6. Everything else: clean, execute as verified

Execute these exactly as the cluster report specifies, **including the additive corrections it
lists** (issue numbers, page ranges, DOIs, arXiv ids, accents, and the caveat-strikes). No refuted
claim, no unverifiable field, and no inline tag is attached to any of them.

`KLS07` · `KLS11` · `GdLL25` · `LR20` · `LR21` · `Hej94` · `RS96` · `CGG98` · `BHB13` · `CdLS22` ·
`M0-MUST-10b` · `M0-MUST-10c` · `M0-6.1-DH1936-I` · `M0-6.1-DH1936-II` · `M0-SHOULD-13a` ·
`M0-SHOULD-13b` · `M0-SHOULD-14` · `M0-SHOULD-16a` · `M0-SHOULD-16b` · `M0-SHOULD-17` ·
`M1-MUST-3` · `M1-ADDITION-Hodge1937` · `M1-SHOULD-11` · `M1-SHOULD-12` · `MUST9b-Milne-AIM` ·
`MUST10a-Kunnemann` · `MUST10b-GilletSoule` · `MUST10c-Moriwaki` · `MUST10e-Faltings-Hriljac` ·
`CONTENT-arith-HIT-codim` · `MUST6a-CC-ScalingSite-CRAS` · `MUST6c-CC-GeomScalingSite-Selecta` ·
`MUST8-CC-Knots-Primes-AdeleClassSpace` · `SEED-3-MUST-9a` · `SEED-3-MUST-9b` · `Nes96`

(36 keys. `M0-SHOULD-14` and `M1-MUST-3` are listed here on the title form settled in **D3**;
`M0-SHOULD-13a`/`13b` and `MUST6a`/`MUST6c` on the arXiv-id repair settled in **D4**/**D5**.
`Nes96`'s *fields* are clean; its *content* claim carries the caveat in §3 item 14.)
