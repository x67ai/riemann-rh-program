# Cluster SEED-5 — citation verification for `results/c3-r/seed-no-go-note.md`

Verifier: independent subagent, session of 2026-08-27.
Discipline: every field checked against a primary source (arXiv abs page / PDF first page, Crossref,
zbMATH Open, or the article's own text on disk). The agent-written report
(`results/arxiv/novelty-check.md`) was treated as an *allegation*, never as evidence.

Scratch directory for all downloads and extractions:
`/private/tmp/claude-501/-Users-jaytyagi-.../scratchpad/seed5/`

---

## ITEM 1 (SHOULD 11) — Rosen & Shnidman, arXiv:1402.2233

### 1.1 What the report claimed

* arXiv id `1402.2233`, 2014.
* Title "Neron-Severi groups of product abelian surfaces"; authors J. Rosen and A. Shnidman.
* That the paper is "the precise modern reference for Theorem 4's decomposition", i.e. for
  `NS(E_p x E_q) = Z xi_1 + Z xi_2 + Hom(E_p, E_q)`.

### 1.2 Commands run

```
curl -sSL --max-time 40 "https://arxiv.org/abs/1402.2233"        -o rs_abs.html
curl -sSL --max-time 60 "https://arxiv.org/pdf/1402.2233v2"      -o rs.pdf ; pdftotext rs.pdf rs.txt
curl -sS  --max-time 40 "https://api.crossref.org/works?query.bibliographic=N%C3%A9ron-Severi+groups+of+product+abelian+surfaces+Rosen+Shnidman&rows=5&..."
curl -sS  --max-time 40 "https://api.zbmath.org/v1/document/_search?search_string=Neron-Severi%20groups%20of%20product%20abelian%20surfaces&results_per_page=5"
curl -sS  --max-time 40 "https://api.zbmath.org/v1/document/_search?search_string=au%3AShnidman%20au%3ARosen&results_per_page=10"
```

(The arXiv **API** `id_list=1402.2233` returned a zero-byte body on three separate attempts this
session; the **abs page** and the **PDF** both returned cleanly. Recorded here because the same
API flakiness has bitten this program before.)

### 1.3 Raw evidence

arXiv abs page metadata (`rs_abs.html`):

```
<meta name="citation_title"    content="N\'eron-Severi groups of product abelian surfaces" />
<meta name="citation_author"   content="Rosen, Julian" />
<meta name="citation_author"   content="Shnidman, Ariel" />
<meta name="citation_date"     content="2014/02/10" />
<meta name="citation_arxiv_id" content="1402.2233" />
subjects : Algebraic Geometry (math.AG) ; Number Theory (math.NT)
Submission history: [v1] Mon, 10 Feb 2014 18:41:51 UTC (32 KB)
                    [v2] Sun, 12 Oct 2014 19:04:14 UTC (34 KB)
```

There is **no** `jref` (journal-ref) and no `doi` table cell on the abs page; the only DOI present is
the arXiv datacite DOI `10.48550/arXiv.1402.2233`.

Note the **inverse of trap (a)**: here the arXiv metadata carries the *raw TeX*
(`N\'eron-Severi`). The PDF's own title page prints the accented form:

```
NÉRON-SEVERI GROUPS OF PRODUCT ABELIAN SURFACES
                    JULIAN ROSEN AND ARIEL SHNIDMAN
              arXiv:1402.2233v2 [math.AG] 12 Oct 2014
```

Publication status. Crossref bibliographic search returns no matching work (top five hits are
Selder 1987, Geisser 2026, Kuroda 2015, Pirola 1989, Shramov 2020 — none is this paper). zbMATH is
explicit:

```
1405.11082      | Extensions of CM elliptic curves and orbit counting on the projective line
                | ['Rosen, Julian', 'Shnidman, Ariel'] | Res. Number Theory 3, Paper No. 9, 13 p. (2017).
arXiv:1402.2233 | Néron-Severi groups of product abelian surfaces
                | ['Julian Rosen', 'Ariel Shnidman'] | Preprint, arXiv:1402.2233 [math.AG] (2014)
```

So as of 2026-08-27 it is **still a preprint**. There is no journal-ref to add.

### 1.4 The content claim — the numbered statement

Read from the PDF (`rs.txt`), Section 2 "Preliminaries on abelian surfaces", printed **p. 5**:

> The following result, describing the group NS(A) for a product surface, is well-known.
>
> **Proposition 2.3.** *If A = E × E′ is a product of elliptic curves, then the map*
>
>     Z ⊕ Hom(E, E′) ⊕ Z → NS(A)
>     (a, λ, b) ↦ (a − 1)h + Γ_λ + (b − deg(λ))v,
>
> *is an isomorphism of groups. Here, Γ_λ ⊂ E × E′ is the graph of λ : E → E′.*

The hypothesis in force from the head of §2 is: "Let A be an abelian surface over an algebraically
closed field k of characteristic 0"; and `h`, `v` are defined there as "the classes of φ(E × {0})
and φ({0} × E′) in NS(A) … the horizontal and vertical axes".

The bare additive form the seed note uses is restated verbatim in §4, printed **p. 8**:

> "Thus Hom(E, E′) is simply Zλ. Then NS(A) ≅ Zh ⊕ Zv ⊕ Hom(E, E′), with h and v the horizontal
> and vertical classes as before."

(and again at printed p. 15 for the CM case: "≅ NS(E₁) ⊕ Hom(E₁, E₂) ⊕ NS(E₂)").

**Verdict on the content claim: CONFIRMED, with one correction of emphasis.** Proposition 2.3 *is*
exactly the seed note's Theorem 4 decomposition, for a product of two elliptic curves, stated for
an arbitrary product (no isogeny or non-CM hypothesis is imposed on Prop. 2.3 itself). Dictionary:
the note's `ξ₁ = [{0}×E′]` is Rosen–Shnidman's `v`, and the note's `ξ₂ = [E×{0}]` is their `h`.
The correction: Rosen–Shnidman **do not claim the result** — they preface it with "is well-known".
So the note must cite it as a convenient precise modern reference, **not** as the source of the
decomposition. Wording such as "see e.g. [RS, Prop. 2.3]" is accurate; "due to [RS]" would not be.

Small consistency point worth recording: the note's own proof produces `Hom(E, Ê′)` and then uses
the canonical principal polarization `E′ ≅ Ê′`; Rosen–Shnidman state it directly with `Hom(E, E′)`.
Same group, same statement.

### 1.5 Ready-to-paste citation

    J. Rosen and A. Shnidman, *Néron-Severi groups of product abelian surfaces*,
    arXiv:1402.2233 (2014); see Proposition 2.3.

House-style long form if the executing session prefers full first names:

    Julian Rosen and Ariel Shnidman, *Néron-Severi groups of product abelian surfaces*,
    preprint (2014), arXiv:1402.2233 [math.AG]; Proposition 2.3.

**Do not** add a journal reference: zbMATH records it as a preprint and Crossref has no record.

---

## ITEM 1b — Birkenhake–Lange, the comparison citation

### 1.6 What the report / note claimed

Task text to check: "C. Birkenhake and H. Lange, *Complex Abelian Varieties*, 2nd ed.,
Grundlehren der mathematischen Wissenschaften 302, Springer, 2004"; and: identify the
chapter/section carrying `NS(A × B) = NS(A) + NS(B) + Hom(A, B̂)`.

The note itself cites at chapter level: `[BL, Ch. 5; self-contained proof below]` (§5, Theorem 4),
`[BL], Ch. 2 for the Poincaré bundle, seesaw, and rigidity; Ch. 5 for the endomorphism context`,
and in the bibliography `C. Birkenhake, H. Lange, *Complex Abelian Varieties*, Springer, Ch. 2 and
Ch. 5. (Citation at chapter level per the adjudicated record …)`.

### 1.7 Commands run

```
curl -sS "https://api.crossref.org/works/10.1007%2F978-3-662-06307-1"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=Birkenhake%20Lange%20Complex%20abelian%20varieties&results_per_page=6"
curl -sS "https://api.zbmath.org/v1/document/2120946"
for n in 1..7: curl -sS "https://api.crossref.org/works/10.1007%2F978-3-662-06307-1_$n"
WebFetch https://link.springer.com/book/10.1007/978-3-662-06307-1        (303 -> idp.springer.com auth wall)
WebFetch https://link.springer.com/chapter/10.1007/978-3-662-06307-1_4   (303 -> idp.springer.com auth wall)
```

### 1.8 Raw evidence

Crossref (`10.1007/978-3-662-06307-1`):

```
title: ['Complex Abelian Varieties']  container-title: ['Grundlehren der mathematischen Wissenschaften']
publisher: Springer Berlin Heidelberg   issued: {'date-parts': [[2004]]}   type: book
ISBN: ['9783642058073', '9783662063071']  ISSN: ['0072-7830']
author: [('Christina','Birkenhake'), ('Herbert','Lange')]
```

zbMATH record **Zbl 1056.14063** (id 2120946):

```
title:  {'title': 'Complex abelian varieties', 'addition': '2nd augmented ed.'}
year:   2004
series: Grundlehren der Mathematischen Wissenschaften, volume '302', year 2004
book:   Berlin: Springer, ISBN 3-540-20488-1 (hbk)
source: "Grundlehren der Mathematischen Wissenschaften 302. Berlin: Springer
         (ISBN 3-540-20488-1/hbk). xii, 635~p. (2004)."
```

zbMATH also carries the **first** edition separately:

```
108485 | Complex abelian varieties | ['Lange, Herbert', 'Birkenhake, Christina'] | 1992
       | Grundlehren der Mathematischen Wissenschaften 302 | Berlin: Springer-Verlag, ISBN 3-540-54747-9
```

— note the author order is **reversed** in the 1992 edition (Lange, Birkenhake). Rosen–Shnidman's
own bibliography cites the **1992** edition: "[BL] Ch. Birkenhake, H. Lange, Complex abelian
varieties, Springer-Verlag, Grundlehren 302 (1992)." Both editions are Grundlehren **302**.

Chapter DOIs via Crossref (the series offset is +2 because *Introduction* and *Notation* are
front matter with their own DOIs):

```
_1 Introduction                     pp.   1-4
_2 Notation                         p.    5
_3 Complex Tori                     pp.   7-22    (= Chapter 1)
_4 Line Bundles on Complex Tori     pp.  23-44    (= Chapter 2)
_5 Cohomology of Line Bundles       pp.  45-68    (= Chapter 3)
_6 Abelian Varieties                pp.  69-112   (= Chapter 4)
_7 Endomorphisms of Abelian Varieties pp. 113-144 (= Chapter 5)
```

### 1.9 Verdict

Bibliographic fields: **CONFIRMED** (2nd augmented ed., Grundlehren der mathematischen
Wissenschaften **302**, Springer, Berlin, **2004**, xii+635 pp., ISBN 3-540-20488-1,
DOI 10.1007/978-3-662-06307-1, authors Christina Birkenhake and Herbert Lange).

Chapter identification: **CONFIRMED** that BL Ch. 2 = "Line Bundles on Complex Tori" (pp. 23-44)
and BL Ch. 5 = "Endomorphisms of Abelian Varieties" (pp. 113-144) — both consistent with what the
note draws from them (Poincaré bundle / seesaw / rigidity; the endomorphism context).

Section carrying the product decomposition: **NOT LOCATED — UNVERIFIED.** No copy of the book is
in the on-disk corpus, Springer's book and chapter pages redirect (HTTP 303) to
`idp.springer.com` authentication, and no free primary source read this session states a numbered
BL result for `NS(X₁ × X₂) ≅ NS(X₁) ⊕ NS(X₂) ⊕ Hom(X₁, X̂₂)`. Search hits that *appeared* to give
one were secondary summaries and are refused as evidence under trap (b).

**Recommendation to the executing session:** leave the BL citation at chapter level exactly as the
note already has it (the note explicitly re-proves everything it consumes, so nothing load-bearing
rests on a page number), and let **Rosen–Shnidman Prop. 2.3** carry the precise pointer. Do not
invent a BL section number.

### 1.10 Ready-to-paste citation

    C. Birkenhake and H. Lange, *Complex Abelian Varieties*, 2nd augmented ed.,
    Grundlehren der mathematischen Wissenschaften **302**, Springer, Berlin, 2004;
    doi:10.1007/978-3-662-06307-1.

---

## ITEM 2 (SHOULD 12) — the two Nesterenko items

### 2(a) Nesterenko 1996, Mat. Sb. / Sb. Math.

Commands:

```
curl -sS "https://api.crossref.org/works?query.bibliographic=Nesterenko+Modular+functions+and+transcendence+questions+Sbornik+Mathematics+1996&rows=6&..."
curl -sS "https://api.crossref.org/works/10.1070%2Fsm1996v187n09abeh000158"
curl -sS "https://api.crossref.org/works/10.4213%2Fsm158"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=Nesterenko%20Modular%20functions%20and%20transcendence%20questions&results_per_page=3"
curl -sSL "https://iopscience.iop.org/article/10.1070/SM1996v187n09ABEH000158"
```

Crossref, Russian original (`10.4213/sm158`):

```
title:  ['Модулярные функции и вопросы трансцендентности', 'Modular functions and transcendence questions']
container-title: ['Математический сборник', 'Matematicheskii Sbornik']
volume 187   issue 9   page 65-96   issued 1996   ISSN 0368-8666
author: [('Юрий Валентинович','Нестеренко'), ('Yuri Valentinovich','Nesterenko')]
```

Crossref, English translation (`10.1070/sm1996v187n09abeh000158`):

```
title: ['Modular functions and transcendence questions']
container-title: ['Sbornik: Mathematics']
volume 187   issue 9   page 1319-1348   issued 1996-10-31   ISSN 1064-5616, 1468-4802
author: [('Yu V','Nesterenko')]
```

IOP page metadata corroborates: `citation_journal_abbrev: Sb. Math.`, `citation_volume: 187`,
`citation_issue: 9`, `citation_firstpage: 1319`, `citation_doi: 10.1070/SM1996v187n09ABEH000158`,
`citation_author_institution: M.V. Lomonosov Moscow State University`.

**Verdict: CONFIRMED.** Every field the report gave (volume 187, no. 9, Mat. Sb. 65-96,
Sb. Math. 1319-1348, 1996) checks out, and both DOIs are now on record.

#### What Nesterenko 1996 proves

The full text is paywalled; it was **not read in the original**. Two curated reviews plus the
publisher abstract were used, and they agree.

zbMATH review of the paper itself (**Zbl 0898.11031**, verbatim excerpt):

> "Let P, Q, R denote the normalized Eisenstein series of weights 2, 4, 6, respectively,
> J := 1728Q³/(Q³ − R²) the elliptic modular function. Then for each q = exp(2πiτ) ∈ ℂ,
> 0 < |q| < 1, at least three of the numbers q, P(q), Q(q), R(q) are algebraically independent
> over ℚ (Theorem 1). … and, in particular, the algebraic independence of the elements
> {π, e^π, Γ(1/4)}, {π, e^{π√3}, Γ(1/3)}, {π, e^{π√D}} for any D ∈ ℕ (Corollaries 5 and 6)."

Independently corroborated by the zbMATH review of LNM 1752 (**Zbl 0966.11032**):

> "Prenant prétexte de la preuve par Yu. Nesterenko (1996) de l'indépendance algébrique de π, e^π
> et Γ(1/4) (plus généralement de valeurs prises par les séries d'Eisenstein E₂(τ), E₄(τ), E₆(τ)
> et l'exponentielle e^{2iπτ}) …"

and by the publisher's own abstract (IOP), which is thinner:

> "We prove results on the transcendence degree of a field generated by numbers connected with the
> modular function … In particular, we show that [j(τ)] and [j′(τ)] are algebraically independent
> and we prove Bertrand's conjecture on algebraic independence over [ℚ] of the values at algebraic
> points of a modular function and its derivatives."

**One sentence for the note.** Nesterenko's Theorem 1 states that for every q with 0 < |q| < 1 at
least three of the four numbers q, E₂(q), E₄(q), E₆(q) (Ramanujan's P, Q, R — the normalized
Eisenstein series of weights 2, 4, 6) are algebraically independent over ℚ; specializing to the CM
point q = e^{−2π} yields the algebraic independence of the triple **π, e^π, Γ(1/4)** (and likewise
π, e^{π√3}, Γ(1/3)).

**Caveat, stated plainly:** the triple is `{π, e^π, Γ(1/4)}` as the report says — but this is
verified from two signed zbMATH reviews and the publisher abstract, **not** from the paper's own
text, which is behind a paywall. Do not upgrade this to "read in the original".

Ready-to-paste:

    Yu. V. Nesterenko, *Modular functions and transcendence questions*, Mat. Sb. **187** (1996),
    no. 9, 65-96; doi:10.4213/sm158; English transl., Sb. Math. **187** (1996), no. 9, 1319-1348;
    doi:10.1070/SM1996v187n09ABEH000158.

### 2(b) Nesterenko & Philippon (eds.), LNM 1752 — the report's flagged item

The report flagged this **NOT INDEPENDENTLY VERIFIED**. It is now verified, twice.

Crossref (`10.1007/b76882`):

```
type: book   title: ['Introduction to Algebraic Independence Theory']
container-title: ['Lecture Notes in Mathematics']   issued: [[2001]]
editor: [('Yuri V.','Nesterenko'), ('Patrice','Philippon')]
ISBN: ['9783540414964', '9783540445500']
```

(Chapter DOIs under this book use the alternate prefix `10.1007/3-540-44550-1_*`, e.g.
`10.1007/3-540-44550-1_4` = "Some remarks on proofs of algebraic independence".)

zbMATH (**Zbl 0966.11032**):

```
title:  "Introduction to algebraic independence theory. With contributions from F. Amoroso,
         D. Bertrand, W. D. Brownawell, G. Diaz, M. Laurent, Yu. V. Nesterenko, K. Nishioka,
         P. Philippon, G. Rémond, D. Roy, M. Waldschmidt"
source: "Lecture Notes in Mathematics. 1752. Berlin: Springer. xiii, 256 p. (2001)."
```

The zbMATH review also lists the contents, confirming Nesterenko's own Chapter 3, "Algebraic
independence for values of Ramanujan functions" (pp. 27-46) — the natural pointer if the note wants
a textbook account of the 1996 theorem rather than the original paper.

**Verdict: CONFIRMED.** LNM number **1752**, year **2001**, editors **Yu. V. Nesterenko and
P. Philippon**, Springer, xiii+256 pp., DOI **10.1007/b76882**.

Ready-to-paste:

    Yu. V. Nesterenko and P. Philippon (eds.), *Introduction to Algebraic Independence Theory*,
    Lecture Notes in Math. **1752**, Springer, Berlin, 2001; doi:10.1007/b76882.

If the note wants the chapter pointer instead:

    Yu. V. Nesterenko, *Algebraic independence for values of Ramanujan functions*, in
    Yu. V. Nesterenko and P. Philippon (eds.), *Introduction to Algebraic Independence Theory*,
    Lecture Notes in Math. **1752**, Springer, Berlin, 2001, 27-46; doi:10.1007/3-540-44550-1_3.

  — the pp. 27-46 range is from the zbMATH contents listing; the chapter DOI suffix `_3` is
  inferred from the Crossref chapter-DOI pattern for this book and was **not** individually
  resolved, so either resolve it before use or drop the chapter DOI.

---

## ITEM 3 (SHOULD 14) — Alaoglu & Erdős 1944. The report did NOT read it. I did.

### 3.1 Commands

```
curl -sS  "https://api.crossref.org/works/10.1090%2FS0002-9947-1944-0011087-2"
curl -sSL "https://www.ams.org/journals/tran/1944-056-00/S0002-9947-1944-0011087-2/S0002-9947-1944-0011087-2.pdf" -o ae.pdf
pdftotext ae.pdf ae.txt
grep -n -i "rational|transcend|two primes|distinct primes|simultaneous" ae.txt
```

### 3.2 Bibliographic evidence

Crossref:

```
title: ['On highly composite and similar numbers']
container-title: ['Transactions of the American Mathematical Society']
volume 56   page 448-469   issued 1944   ISSN 0002-9947, 1088-6850
author: [('L.','Alaoglu'), ('P.','Erdös')]
DOI: 10.1090/s0002-9947-1944-0011087-2
```

The AMS PDF's own first page confirms authors and title, and carries the footnote
"Presented to the Society, April 29, 1944; received by the editors February 14, 1944."
Extracted page markers run continuously **448 … 469**.

Orthography note: the printed article sets the name as "P. ERDÖS" (umlaut) and Crossref echoes
"Erdös". Modern house style is **Erdős** (double acute). Use Erdős.

### 3.3 The content claim — FOUND, and it is exactly the two-prime question

**Passage 1, printed p. 449** (Introduction), verbatim from the extracted text:

> "In the theory of colossally abundant numbers the most interesting question is whether the
> quotient of two consecutive colossally abundant numbers is a prime or not. This question leads
> to the following problem in Diophantine analysis. *If p and q are different primes, is it true
> that p^x and q^x are both rational only if x is an integer?*"

(the italics are the original's; the OCR renders the leading "If" as "7/", an artifact of the
scanned italic ligature — the sentence is otherwise character-for-character as quoted.)

**Passage 2, printed p. 455** (§3, immediately after Theorem 10), verbatim:

> "Since log{(q^{1+ε} − 1)/(q^ε − 1)}/log q is a continuous function of ε, k_q(ε) will increase by
> steps of at most 1, and this will occur when log{(q^{1+ε} − 1)/(q^ε − 1)}/log q is an integer.
> But this makes q^ε rational. It is very likely that q^x and p^x can not be rational at the same
> time except if x is an integer. This would show that the quotient of two consecutive colossally
> abundant numbers is a prime. At present we can not show this. Professor Siegel has communicated
> to us the result that q^x, r^x and s^x can not be simultaneously rational except if x is an
> integer. Hence the quotient of two consecutive colossally abundant numbers is either a prime or
> the product of two distinct primes."

### 3.4 Verdict

**CONFIRMED, and stronger than the report claimed.** The paper does not merely contain "a germ" of
the two-distinct-primes question — it *states it twice, explicitly, as an open problem in
Diophantine analysis*, and it records the exact split that the seed note's §7 open question (T1)
lives on:

* **two primes** (p^x, q^x simultaneously rational ⟹ x ∈ ℤ) — Alaoglu–Erdős could not prove it;
  this is the four-exponentials-conjecture-strength statement;
* **three primes** (q^x, r^x, s^x simultaneously rational ⟹ x ∈ ℤ) — communicated to them by
  **Siegel**, i.e. the six-exponentials-strength statement, which is a theorem.

That is precisely the four-vs-six exponentials dichotomy, in 1944. This is a better citation than
the report realized, and it should be cited to **both** pages, not just to the introduction.

Also worth recording for accuracy: Alaoglu–Erdős phrase the question multiplicatively
(`p^x, q^x ∈ ℚ`), **not** as "is log p / log q rational". The two are equivalent
(p^x, q^x ∈ ℚ with x irrational forces log p / log q ∈ ℚ), but if the note paraphrases, it should
paraphrase honestly, e.g. "in the equivalent form: if p ≠ q are primes, can p^x and q^x both be
rational for a non-integer x?"

### 3.5 Ready-to-paste citation

    L. Alaoglu and P. Erdős, *On highly composite and similar numbers*, Trans. Amer. Math. Soc.
    **56** (1944), 448-469; doi:10.1090/S0002-9947-1944-0011087-2. The two-prime question is
    stated at p. 449 ("If p and q are different primes, is it true that p^x and q^x are both
    rational only if x is an integer?") and again at p. 455, where Siegel's three-prime result is
    recorded.

---

## ITEM 4 — Haran 1991 and Thas (already applied to the note; fields re-checked)

### 4.1 Haran — bibliographic

Commands:

```
pdfinfo   "…/fetched-r3/haran1991.pdf"
pdftotext "…/fetched-r3/haran1991.pdf" haran.txt
curl -sS "https://api.crossref.org/works/10.1017%2FCBO9780511526053.010"
curl -sS "https://api.crossref.org/works/10.1017%2FCBO9780511526053"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=Haran%20Index%20theory%20potential%20theory%20Riemann%20hypothesis&results_per_page=4"
```

Crossref, the chapter:

```
title: ['Index theory, potential theory, and the Riemann hypothesis']
container-title: ['L-Functions and Arithmetic']   page: 257-270   issued: 1991-02-22
author: [('Shai','Haran')]   publisher: Cambridge University Press
ISBN: ['9780521386197','9780511526053']   type: book-chapter
```

Crossref, the volume (`10.1017/CBO9780511526053`):

```
title: ['L-Functions and Arithmetic']  issued: 1991-02-22  publisher: Cambridge University Press
editor: [('J.','Coates'), ('M. J.','Taylor')]   ISBN: ['9780521386197','9780511526053']
```

zbMATH (**Zbl 0744.11042**):

```
Index theory, potential theory, and the Riemann hypothesis | Haran, Shai
\(L\)-functions and arithmetic, Proc. Symp., Durham/UK 1989,
Lond. Math. Soc. Lect. Note Ser. 153, 257-270 (1991).
```

The on-disk PDF itself carries the Cambridge Core stamp on every page:
`Cambridge Books Online © https://doi.org/10.1017/CBO9780511526053.010, Cambridge University Press`.

**Verified:** title, author, volume title, editors J. Coates and M. J. Taylor, series **London
Math. Soc. Lecture Note Ser. 153**, CUP, **1991**, pages **257-270**, DOI
**10.1017/CBO9780511526053.010**, **Zbl 0744.11042**, symposium at **Durham 1989**.

**MR1110396 — NOT INDEPENDENTLY VERIFIED.** MathSciNet is behind Cloudflare/JS
(`mathscinet.ams.org/mathscinet-mref` returned a Cloudflare challenge page; the relay station
`?mr=1110396` returned an empty shell). A web-search summary of the MathSciNet relay-station page
did report MR1110396 = this exact chapter, but that is a search-engine rendering, not the database,
and under trap (b) it is not being laundered as primary. **Options:** keep MR1110396 with an
internal note that it is unverified this session, or drop the MR and keep Zbl 0744.11042 + the DOI,
both of which are verified. My recommendation is the latter — nothing is lost.

### 4.2 Haran — the p. 259 content, quoted from the on-disk PDF

The extracted text places the printed page number **259** at line 90 of `haran.txt`, and the next
marker **260** at line 133; the three quoted sentences fall between them, i.e. all three are on
printed **p. 259**. Verbatim (OCR artifacts noted in brackets):

> "It will not be an exaggeration to say that the greatest mystery of arithmetic is the simple
> fact that Z ⊗ Z = Z, or equivalently, that from the point of view of algebraic geometry,
> spec Z × spec Z = spec Z, i.e., the surface reduces to the diagonal!"

> "Nevertheless, for functions f, g : R⁺ → R smooth and compactly supported, to be thought of as
> representing 'Frobenius divisors' on the non-existing surface, we can define their intersection
> number: ⟨f, g⟩ = W(f * g*), and again, associating with such a function, f, a real number
> h⁰(f) ≥ 0 satisfying the above three properties will lead to the solution of the Riemann
> hypothesis."

> "Ergo our main point is: a two dimensional Riemann-Roch for spec Z may very well exist!"

[The FineReader OCR renders `f` as `/` and `g` as `#` in the pairing line, printing
`(/, #) = W(f * #*)`; the surrounding sentence names the functions f and g explicitly, so the
pairing is unambiguously `⟨f, g⟩ = W(f * g*)`. The `h⁰(f) ≥ 0` is OCR'd `h°(f) > 0`; the
"three properties" referred to are Riemann-Roch inequality, Monotoneness and Ampleness, listed on
p. 257-258.]

**Verdict: CONFIRMED.** p. 259 carries the pairing `⟨f, g⟩ := W(f * g*)` and the two other
sentences the note quotes, exactly as the note's bibliography entry says. The note's rendering of
the third quote as "a two dimensional Riemann-Roch for spec(Z) may very well exist!" adds
parentheses around Z that Haran does not print ("spec Z"); trivial, but if the note claims
verbatim quotation it should print `spec Z`.

Two further checks the note asserts, spot-confirmed against `haran.txt`: the Frobenius
correspondences `A_n = {(x, x^{p^n})}` with `A_0 = Diag` on `C × C` for a **single** curve over a
**single** finite field F_p do appear (p. 257), and the surrounding text is existence-optimistic
throughout — no obstruction or no-go claim anywhere.

Ready-to-paste:

    S. Haran, *Index theory, potential theory, and the Riemann hypothesis*, in *L-functions and
    Arithmetic* (Durham, 1989), J. Coates and M. J. Taylor (eds.), London Math. Soc. Lecture Note
    Ser. **153**, Cambridge Univ. Press, Cambridge, 1991, 257-270;
    doi:10.1017/CBO9780511526053.010; Zbl 0744.11042. The passage relied on is p. 259.

    [MR1110396 is reported by secondary listings but was not independently verified this session;
     omit it or mark it accordingly.]

### 4.3 Thas

arXiv abs page (`https://arxiv.org/abs/1507.06480`):

```
citation_title  : A taste of Weil theory in characteristic one
citation_author : Thas, Koen
citation_date   : 2015/07/23
Submission history: [v1] Thu, 23 Jul 2015 12:58:31 UTC (204 KB)
subjects        : Algebraic Geometry (math.AG)
```

No journal-ref on the abs page. The published version is on Crossref
(`10.4171/157-1/8`):

```
title: ['A taste of Weil theory in characteristic one']
container-title: ['Absolute Arithmetic and $\mathbb F_1$-Geometry']
page: 365-386   issued: 2016-07-25   author: [('Koen','Thas')]
publisher: EMS Press   ISBN: ['9783037191576','9783037196571']   type: book-chapter
```

**Verdict: CONFIRMED.** Author **Koen Thas** (single author), arXiv:1507.06480 v1 dated
**23 July 2015**, published as pp. **365-386** of *Absolute Arithmetic and F₁-Geometry*,
EMS, 2016, DOI **10.4171/157-1/8**. This matches the note's dated correction of 2026-08-27 (which
had already fixed the earlier misattribution of 1507.06480 to Haran). Nothing further to change.

One field the note gives that I did **not** verify from a primary source: the volume's editor
("K. Thas (ed.)") and its place of publication ("Zürich"). Crossref lists EMS Press as publisher
and gives no editor for the chapter record. Both are almost certainly right, but they are
uncorroborated here; the safe form drops "Zürich" and keeps the DOI.

Ready-to-paste:

    K. Thas, *A taste of Weil theory in characteristic one*, in *Absolute Arithmetic and
    F₁-Geometry*, EMS Press, 2016, 365-386; doi:10.4171/157-1/8; arXiv:1507.06480.

---

## Summary of disagreements with the report

| # | Report said | Primary source says |
|---|---|---|
| 1 | Rosen-Shnidman is "the precise modern reference for Theorem 4's decomposition" | True — Prop. 2.3, p. 5 — **but** RS themselves preface it "is well-known", so cite as "see e.g.", never "due to". Also: still an unpublished preprint (zbMATH: "Preprint, arXiv:1402.2233 [math.AG] (2014)"), so add no journal-ref. |
| 1b | (task) identify the BL section carrying NS(A×B) | **Not located.** Springer is auth-walled and no copy is on disk. Keep the note's chapter-level citation; BL Ch. 2 = "Line Bundles on Complex Tori", Ch. 5 = "Endomorphisms of Abelian Varieties" are confirmed. |
| 2b | LNM 1752 flagged NOT INDEPENDENTLY VERIFIED | Now verified twice (Crossref 10.1007/b76882; Zbl 0966.11032). LNM **1752**, 2001, eds. Nesterenko and Philippon, xiii+256 pp. |
| 3 | Alaoglu-Erdős "contains the 1944 germ", not read | Understated. The two-prime question is stated **explicitly, twice** (pp. 449 and 455), and p. 455 also records **Siegel's** three-prime theorem — the exact four-vs-six-exponentials split. |
| 4 | MR1110396 | Could not be verified from MathSciNet (Cloudflare/JS wall). Zbl 0744.11042 and doi:10.1017/CBO9780511526053.010 are verified; prefer those. |
