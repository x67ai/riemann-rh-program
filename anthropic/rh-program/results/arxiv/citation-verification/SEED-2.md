# CLUSTER SEED-2 — the four-exponentials lineage for `results/c3-r/seed-no-go-note.md`

Verification date: 2026-08-27. Verifier: citation-verification subagent, session 11.
Discipline: every field checked against a primary source. The agent-written report
(`results/arxiv/novelty-check.md`) was treated as an untrusted claim list throughout.

**Headline.** The report's central claim is **CONFIRMED, from the primary source, verbatim, with a
page number.** The seed note's §9 sentence — *"The question (T1) appears to be unrecorded in the
literature in this form and is stated here as open"* — is **false**. (T1) is printed as a displayed,
labeled conjecture on **p. 231 of Diaz, JTNB 9 (1997)**, under the label **(C4E faible)**, and the
sentence immediately after it is the note's own four-exponentials reduction, with the same
substitution the note performs in its §7.

Three secondary findings, all of which change what should be written:

1. **The English name "Bertrand's weak four-exponentials conjecture" is the report's coinage, not a
   term of art.** Diaz's label is `(C4E faible)`; Waldschmidt never uses "weak four exponentials" in
   *Open Diophantine Problems*, in *AWS Lecture 5*, or in *LIL* (all three grepped). The statement is
   real and is Bertrand's; the *name* is not standard and should not be presented as one.
2. **The report's MUST-10 claim that Waldschmidt's AWS Lecture 5 Conjectures 5.34/5.35 are "the
   printed statement of Bertrand's conjecture" is half right and, as used in MUST-3, misleading.**
   5.34 and 5.35 are Bertrand's two *modular* conjectures on `J` (Diaz's (CDB) family). Neither is
   the weak four-exponentials statement, and neither mentions "§5". AWS Lecture 5 therefore does
   **not** corroborate the §5 attribution; Diaz does.
3. **A much better secondary source than the report used exists for the Schneider/Lang/Ramachandra
   lineage, and it vindicates the report's Lang and Ramachandra references exactly.** Waldschmidt,
   *Linear Independence of Logarithms of Algebraic Numbers* (LIL), Ch. 1, p. 1-8/1-9, names
   Bourbaki 305 **and** Topology 5 (1966) 363-370 **and** Acta Arith. 14 (1968) 65-88 in one
   sentence and closes with "They both formulated the four exponentials conjecture explicitly."
   Waldschmidt's *own* attribution line in ODP/AWS5 instead names Lang's **book** (`[La 1966]`
   Chap. II §1 = *Introduction to Transcendental Numbers*, Addison-Wesley 1966) and `[La 1971]`
   p. 638. Both should be carried.

---

## ITEM 1 (report MUST 2) — G. Diaz, JTNB 9 (1997), 229–245

### What the report claimed

> **G. Diaz, "La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la
> fonction modulaire", J. Théor. Nombres Bordeaux 9 (1997), no. 1, 229–245** — states (T1)
> verbatim as (C4E faible), gives the note's own four-exponentials reduction in the next sentence,
> and proves (C0) ⟺ (C6). Propositions 1 and 3(1) are unconditional partial results the note
> should report.

and, in the body of the report:

> It is D. Bertrand's **weak four-exponentials conjecture**, stated verbatim in Diaz (JTNB 1997)
> §I: *"(C4E faible) Soient a₁, a₂ des nombres réels algébriques positifs différents de 1. Alors π²
> et (log a₁)(log a₂) sont ℚ-linéairement indépendants"* … Diaz's Théorème 1 proves the equivalence
> of (C0) (isogeny of two algebraic-parameter Tate curves implies multiplicative dependence) with
> (C6) (the log-product vs π² statement), and his Propositions 1 and 3(1) give unconditional partial
> results about the (T1) scenario the note does not know about.

### Commands run

```
curl -sS -L "http://www.numdam.org/item/JTNB_1997__9_1_229_0/"          -> numdam-item.html
curl -sS -L "https://www.numdam.org/item/JTNB_1997__9_1_229_0.pdf"      -> diaz1997-numdam.pdf  (1,557,849 bytes, 18 pp.)
pdfinfo diaz1997-numdam.pdf
pdftotext -layout diaz1997-numdam.pdf diaz-layout.txt
pdftotext         diaz1997-numdam.pdf diaz-raw.txt
pdftoppm -r 200 -png -f {2,3,4,5,14,15} -l {…} diaz1997-numdam.pdf      # pages 229, 230, 231, 232, 241, 242
curl -sS -L "https://jtnb.centre-mersenne.org/item/JTNB_1997__9_1_229_0/"
```

The Numdam PDF is a **scan with an OCR'd text layer** and the OCR silently drops math-font tokens —
`π²` vanished out of (C6), `x₂ = (log α₁)/2iπ` came out as `X2 (log`, and `alors` was eaten in
Proposition 1. **Every load-bearing quotation below was therefore re-read off a 200 dpi page
rendering, not off pdftotext.** This matters: a pdftotext-only reading of this paper would have
produced a garbled (C6) and could easily have been mistaken for a different statement.

Local copy retained at
`results/arxiv/citation-verification/assets/diaz-1997-jtnb9-quatre-exponentielles-numdam.pdf`.

### Raw evidence — bibliographic

Numdam item page, `<meta>` block, verbatim:

```
<meta name="citation_title" content="La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la fonction modulaire">
<meta name="citation_author" content="Diaz, Guy">
<meta name="citation_publication_date" content="1997">
<meta name="citation_journal_title" content="Journal de théorie des nombres de Bordeaux">
<meta name="citation_issn" content="2118-8572">
<meta name="citation_volume" content="9">
<meta name="citation_language" content="fr">
<meta name="citation_issue" content="1">
<meta name="citation_firstpage" content="229">
<meta name="citation_lastpage" content="245">
```

The article's own running head, p. 229 (read off the page image): `Journal de Théorie des Nombres
de Bordeaux 9 (1997), 229–245`. Author line: `par Guy DIAZ`. Footer: `Manuscrit reçu le 24 février
1997`. Affiliation on p. 245: `Université de Saint-Etienne, Equipe de Théorie des Nombres`.

**Verdict on the bibliographic fields: every one of the report's fields is correct** — author,
title, journal, volume 9, issue no. 1, year 1997, pages 229–245.

### Raw evidence — (a) the statement labeled (C4E faible)

Verbatim, **p. 231**, top of page (read off the page rendering; italics in the original):

> **(C4E faible)** *Soient α₁, α₂ des nombres réels algébriques positifs différents de 1. Alors π²
> et (log α₁)(log α₂) sont ℚ-linéairement indépendants* (log *désigne ici le logarithme népérien*).

Its introduction, last line of **p. 230**:

> Le cas particulier de (C4E) que vise D. Bertrand ([2], §5) est le suivant.

and, at the head of that section, **p. 230**:

> **I - Conjecture des quatre exponentielles, conjecture de D. Bertrand.**
> La conjecture des quatre exponentielles (notée (C4E) ici) a plusieurs formulations équivalentes.
> En voici une (voir [9], §1.2 pour une autre version).
> **(C4E)** *Si (x₁, x₂) et (y₁, y₂) sont deux familles de nombres complexes ℚ-linéairement
> indépendants, alors parmi les quatre exponentielles e^{x_i y_j}, 1 ≤ i, j ≤ 2, il y a au moins un
> nombre transcendant.*

**Answers to the questions asked.**

* Is it literally "the weak four-exponentials conjecture"? **The label is `(C4E faible)` — "weak
  (C4E)". Diaz does not call it a "conjecture faible des quatre exponentielles" in words; he calls
  it *"le cas particulier de (C4E) que vise D. Bertrand"*.** The English phrase the report uses is a
  faithful translation of the label, but it is **not** a term of art (see the negative greps under
  ITEM 2).
* Does it say what the report says it says? **Yes, exactly**, with one sharpening the report did not
  make: the hypothesis is *real* algebraic, *positive*, *≠ 1* — which primes satisfy — and the
  conclusion is ℚ-linear independence of π² and the log-product, i.e. `(log α₁)(log α₂) ∉ π²·ℚ`.
  Since `4π²ℚ = π²ℚ`, the seed note's (T1) `log p · log q ∉ 4π²ℚ` is **literally the α₁ = p,
  α₂ = q instance of (C4E faible)** — not an analogue of it, not adjacent to it, the same sentence.

### Raw evidence — (b) the sentence immediately after, giving the 4EC reduction

Verbatim, **p. 231**, the paragraph directly below (C4E faible):

> On obtient la même conjecture en remplaçant la conclusion de (C4E faible) par
> (log α₁).(log α₂) ≠ π². Pour faire le lien avec (C4E) il suffit de prendre
> x₁ = 1, x₂ = (log α₁)/2iπ, y₁ = 2iπ, y₂ = log α₂.

This is the seed note's §7 argument, transposed. The note takes `x₁ = 2πi, x₂ = log p, y₁ = 1,
y₂ = log q/(2πi)`; Diaz takes `x₁ = 1, x₂ = (log α₁)/2iπ, y₁ = 2iπ, y₂ = log α₂`. Same matrix, rows
and columns exchanged. The four exponentials are `1, α₂, α₁, exp((log α₁)(log α₂)/2iπ)` in both.
**The note's "(4EC ⟹ ¬(T1))" paragraph is Diaz's two-line remark of 1997.**

### Raw evidence — (c) Théorème 1 and (C0) ⟺ (C6)

Verbatim, **p. 231–232**:

> **THÉORÉME 1.**
> *Les énoncés (C0) à (C6) sont équivalents.*
>
> **(C0)** *Si q₁ et q₂ sont deux éléments de D\* algébriques et vérifiant φ_n(J(q₁), J(q₂)) = 0
> pour au moins un entier n ≥ 1, alors q₁ et q₂ sont multiplicativement dépendants.*
>
> …
>
> **(C6)** *Soient α₁ et α₂ des nombres algébriques non nuls, et de module différent de 1. On fixe
> une détermination log α₁, log α₂ de leurs logarithmes. Alors (log α₁)(log α₂) et π² sont
> ℚ-linéairement indépendants.*

Notation fixed on p. 230: `D` is the open unit disc, `D* = D \ {0}`, `j` the modular invariant and
`J` its Fourier expansion at infinity (so `j(τ) = J(e^{2iπτ})`), and *"Le n-ième polynôme modulaire
est noté φ_n(X, Y), avec la convention φ₁(X, Y) = X − Y."*

So:

* **(C0)** — literally: for algebraic `q₁, q₂` in the punctured unit disc, if the `j`-invariants of
  the corresponding Tate curves satisfy the level-`n` modular polynomial for some `n ≥ 1` (i.e. the
  curves are `n`-isogenous), then `q₁, q₂` are multiplicatively dependent. **The report's gloss
  ("isogeny of two algebraic-parameter Tate curves implies multiplicative dependence") is
  accurate.**
* **(C6)** — the log-product-versus-π² statement, over *all* nonzero algebraic numbers of modulus
  ≠ 1, with an arbitrary determination of the logarithms. This is (C4E faible) with the reality and
  positivity hypotheses dropped.
* **(C0) ⟺ (C6) — CONFIRMED**, as part of the seven-way equivalence of Théorème 1.

Théorème 2, **p. 235–236**, closes the ladder:

> **THÉORÈME 2.**
> (a) (C4E) implique (C0), (C1), …, (C6).
> (b) (CDB) implique (C0), (C1), …, (C6).
> (c) (C0), …, (C6) impliquent chacune [(C4E faible)].
> …
> (c) (C6) implique (C4E faible) : c'est trivial !

**Adjudication note carried forward.** The prior session's own adjudication (novelty-check.md,
item 4) already warned that Diaz proves an equivalence of *universally quantified conjectures*, not
an unconditional pairwise criterion. That warning is **correct and I confirm it**: nothing in
Théorème 1 is unconditional. Diaz anticipates (T1) as a *statement*; Winkelmann anticipates the
note's Theorems 1–3 as *theorems*. Do not let the seed note's rewrite blur the two.

### Raw evidence — (d) Proposition 1 and Proposition 3(1)

Verbatim, **p. 241**, immediately preceded by Diaz's own signpost:

> ∘ En direction de (C6) et de (C4E faible) on a le résultat suivant.
>
> **PROPOSITION 1.** *Soient α₁, α₂ des nombres algébriques non nuls et non racines de l'unité. On
> fixe une détermination log α₁, log α₂ de leurs logarithmes. Si (log α₁)(log α₂) et π² sont
> ℚ-linéairement dépendants alors log α₁ et log α₂ (ainsi que log α₁ et 2iπ) sont algébriquement
> indépendants.*
>
> *Démonstration.* On se ramène au cas (log α₁)(log α₂) = −4π² ; on applique le lemme 6-(A.1) avec
> x₁ = 1, x₂ = (log α₁)/2iπ, y₁ = 2iπ, y₂ = log α₂. On en déduit que ℚ̄(2iπ, log α₁, log α₂) a un
> degré de transcendance supérieur ou égal à 2 ; la relation initiale dit que ce corps est
> ℚ̄(2iπ, log α₁) et qu'il a même degré de transcendance que ℚ̄(log α₁, log α₂), ce qui donne le
> résultat.

**Exactly what Proposition 1 gives, stated plainly:** it is an *unconditional* theorem about the
(T1) scenario. **If** the coincidence held — i.e. if `log p · log q ∈ π²ℚ` — **then** `log p` and
`log q` would be *algebraically independent* over ℚ̄, and so would `log p` and `2iπ`. In other
words, a (T1) coincidence cannot be cheap: it would force a strong algebraic-independence statement
that nobody can currently prove but that is at least consistent. Two operational consequences for
the seed note:

* the note's §7 sentence that "no proven theorem currently excludes it" stays true, but the note
  should stop implying nothing is known — Proposition 1 is a proven constraint *on the coincidence*;
* the note's Schanuel paragraph (which derives the same algebraic independence *from* Schanuel) is
  strictly weaker than Proposition 1 in this respect, since Proposition 1 needs no conjecture.
  Note also the normalization: Diaz reduces to `(log α₁)(log α₂) = −4π²`, which is where the note's
  `4π²` (rather than `π²`) naturally comes from.

Verbatim, **p. 242**, preceded by *"∘ Dans le même ordre d'idée, en direction de (C4) on a le
résultat suivant."*:

> **PROPOSITION 3.** *Soit τ ∈ H.*
> *(1) Si exp(2iπτ) est algébrique alors Im(τ) est transcendant et Re(τ) est transcendant ou
> rationnel.*
> *(2) Si exp(2iπ/τ) est algébrique alors Im(τ)/|τ|² est transcendant et Re(τ)/|τ|² est
> transcendant ou rationnel.*
> *(3) si exp(2iπτ) et exp(2iπ/τ) sont algébriques alors* (3-1) … (3-5) …
>
> *Démonstration.* ∘ (1) Je note τ = x + iy (x, y ∈ ℝ). Puisque exp(2iπτ) est algébrique, sa partie
> réelle et sa partie imaginaire le sont aussi : (cos 2πx).e^{−2πy}, (sin 2πx).e^{−2πy} ∈ ℚ̄. En
> faisant la somme des carrés cela dit aussi que e^{−2πy} est algébrique. Et e^{2iπx} =
> e^{2iπτ}.e^{2πy} est donc algébrique. Le théorème de Gel'fond-Schneider dit alors que x est
> transcendant ou rationnel, et que iy est transcendant.

**Correction to the report on Proposition 3(1).** The report files Prop. 3(1) alongside Prop. 1 as
an "unconditional partial result toward (T1)". **Diaz files it under (C4), not under (C6)/(C4E
faible)** — his own signpost sentence says so. (C4) is equivalent to (C6) by Théorème 1, so it is
in the same family, but the report's placement is not what the paper says and a referee reading the
paper will notice. What Prop. 3(1) actually gives the note is different and useful: applying it to
`q = 1/p = exp(2iπτ)` with `τ = i·(log p)/2π` yields `Im(τ) = (log p)/2π` **transcendental**,
unconditionally, by a five-line Gel'fond–Schneider argument. That is the note's `y_p`-transcendence
fact, already in print in 1997.

### Raw evidence — (e) Diaz's attributions and his bibliography entry [2]

**Four-exponentials conjecture.** First sentence of the paper, **p. 229**:

> **0 - Introduction.**
> La conjecture des quatre exponentielles (premier problème de Schneider, 1957, voir [7] p.139) est
> un des grands problèmes de la transcendance depuis quarante ans (au moins). L'attaque frontale par
> la méthode classique de Gel'fond-Schneider n'a rien donné, jusqu'ici.

**So Diaz attributes 4EC to Schneider 1957, "premier problème" — first problem — citing the French
edition, p. 139. He does NOT name Lang or Ramachandra for the conjecture.** He names them for the
*six*-exponentials theorem, **p. 231**:

> **Note.** En direction de (C4E), on ne dispose actuellement que de peu de résultats : le théorème
> des six exponentielles (dû à C. Siegel, S. Lang et K. Ramachandra : voir [13], §1-4), le théorème
> des cinq exponentielles (dû à M. Waldschmidt, voir [12], corollaire 2-2), le théorème fort des six
> exponentielles de D. Roy (voir [5], corollaire 2-2) qui contient les deux résultats précédents, et
> un résultat de D. Roy et M. Waldschmidt (voir [6], théorème 2).

**Weak version / Bertrand.** **p. 229**:

> Lors d'une conférence à Madras en janvier 1996, D. Bertrand a proposé différentes conjectures,
> liées à la fonction modulaire J ; une réponse positive à ces conjectures permettrait d'obtenir un
> cas particulier des quatre exponentielles, ce qui serait déjà une belle avancée.

and **p. 231**:

> D. Bertrand propose dans [2], §5, plusieurs conjectures pour la fonction modulaire J, liées entre
> elles (avec ses notations la conjecture 1 est plus forte que la conjecture 2(ii), elle même plus
> forte que la conjecture 2(i)). Je m'intéresse ici à la seconde, sous la forme suivante (notée
> (CDB) par la suite).
>
> **(CDB)** *Si q₁, q₂ sont deux éléments de D\* algébriques et multiplicativement indépendants
> alors J(q₁) et J(q₂) sont algébriquement indépendants.*
>
> Je ne connais pas de lien direct entre (C4E) et (CDB). Par contre ces deux conjectures contiennent
> (C4E faible). Cette implication, établie dans [2], §5, sera raffinée au théorème 2 ci-dessous.

Note that **(CDB) is Diaz's label** for Bertrand's second conjecture, not Bertrand's own; the report
speaks of "the algebraic-independence conjecture (CDB)" without saying whose notation that is.

**Bibliography, p. 244–245, verbatim, the two entries asked for:**

```
[2]   D. Bertrand, Theta functions and transcendence, Madras Number Theory Sympo-
      sium 1996, The Ramanujan J. Math. (à paraître).

[7]   Th. Schneider, Introduction aux nombres transcendants, Gauthier-Villars (1959).
```

Two things to record. **[2] is a "to appear" entry** — Diaz's manuscript was received 24 February
1997 and Bertrand's paper appeared in the December 1997 issue, so Diaz never saw page numbers.
**[7] is the French translation only**; Diaz cites the German original nowhere, and gives no
chapter or section, only "premier problème … p. 139".

Also worth knowing for the seed note's `[BSDGP]` citation (a different cluster, but the error is in
this same bibliography): **[1] reads `K. Barré, G. Diaz, F. Gramain, G. Philibert, Une preuve de la
conjecture de Malher-Manin, Invent.Math. 124 (1996), 1-9`** — Diaz's own bibliography drops the
"-Sirieix" from Barré-Sirieix and misspells "Mahler" as "Malher". **Do not copy fields from this
bibliography.**

### Verdict — ITEM 1

**CONFIRMED.** Every bibliographic field is correct. Every content claim is correct and has now been
read verbatim off the page: (C4E faible) on p. 231 is the seed note's (T1); the four-exponentials
reduction is the next sentence; Théorème 1 gives (C0) ⟺ (C6); Propositions 1 (p. 241) and 3 (p. 242)
exist and say what is claimed. Two refinements the executing session must apply:

* **Proposition 3(1) is filed by Diaz under (C4), not under (C4E faible).** Say "his Proposition 1
  (toward (C6) and (C4E faible)) and Proposition 3(1) (toward (C4), equivalent to (C6) by his
  Théorème 1)".
* **Do not write "weak four-exponentials conjecture" as if it were a standard name.** Write
  "Diaz's (C4E faible) — the special case of the four-exponentials conjecture that D. Bertrand aims
  at".

### Ready-to-paste citation

    G. Diaz, *La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la
    fonction modulaire*, J. Théor. Nombres Bordeaux **9** (1997), no. 1, 229-245;
    <http://www.numdam.org/item?id=JTNB_1997__9_1_229_0>.

(JTNB volumes of that era carry no DOI on Numdam; the Numdam item id is the stable handle. Zbl
0873.11049 was **not** verified this session and is deliberately omitted.)

Suggested sentence for the seed note's §9, replacing the "unrecorded" claim:

    (T1) is not new. It is the alpha_1 = p, alpha_2 = q case of the statement Diaz prints as
    (C4E faible) -- "Soient alpha_1, alpha_2 des nombres reels algebriques positifs differents
    de 1. Alors pi^2 et (log alpha_1)(log alpha_2) sont Q-lineairement independants" -- the
    special case of the four-exponentials conjecture aimed at by D. Bertrand [Diaz 1997, p. 231,
    citing Bertrand, Ramanujan J. 1 (1997), Sect. 5]. The reduction to the four-exponentials
    conjecture given in Sect. 7 above is the sentence that immediately follows it there. Diaz's
    Theoreme 1 places it in a seven-way equivalence with, among others, the statement (C0) that
    two Tate curves with algebraic parameters related by a modular polynomial have
    multiplicatively dependent parameters; and his Proposition 1 (p. 241) is an unconditional
    constraint on the coincidence: if (log alpha_1)(log alpha_2) and pi^2 were Q-linearly
    dependent, then log alpha_1 and log alpha_2 -- and log alpha_1 and 2i pi -- would be
    algebraically independent.

---

## ITEM 2 (report MUST 3) — D. Bertrand, Ramanujan J. 1 (1997), no. 4, 339–350, §5

### What the report claimed

> **D. Bertrand, "Theta functions and transcendence", Madras Number Theory Symposium, January
> 1996; Ramanujan J. 1 (1997), no. 4, 339–350, §5** — the origin of the weak four-exponentials
> conjecture and of the algebraic-independence conjecture (CDB). *(Paywalled; content and the §5
> attribution read via Diaz 1997 §I and its bibliography entry [2], and via Waldschmidt's AWS
> Lecture 5 Conjectures 5.34/5.35. Reference not independently verified from the source.)*

### Commands run

```
curl -sS "https://api.crossref.org/works?query.bibliographic=Theta+functions+and+transcendence+Bertrand+Ramanujan+Journal&rows=5&select=…"
curl -sS "https://api.crossref.org/works/10.1023/A:1009749608672"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=au%3ABertrand%20%26%20ti%3A%22Theta%20functions%20and%20transcendence%22&results_per_page=3"
curl -sS "https://api.zbmath.org/v1/document/1185660"                       # full record incl. review text
curl -sS -L "https://zbmath.org/?q=an%3A0916.11043"                          # Cloudflare challenge, unusable
curl -sS -L "https://link.springer.com/article/10.1023/A:1009749608672"      # 3038 bytes, bot wall
WebFetch link.springer.com/article/10.1023/A:1009749608672                    # 303 -> idp.springer.com auth
curl -sS "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1023/A:1009749608672?fields=…"  # abstract elided
curl -sS "https://api.crossref.org/journals/1382-4090/works?filter=from-pub-date:1997-01-01,until-pub-date:1998-01-01&rows=40"
curl -sS -L "https://webusers.imj-prg.fr/~daniel.bertrand/"                   # author page, no publication list
curl -sS -L "https://webusers.imj-prg.fr/~daniel.bertrand/recherche/…"        # 404
```

### Raw evidence — bibliographic (this part is now fully verified)

**Crossref, DOI record**, verbatim fields:

```
DOI     : "10.1023/a:1009749608672"
title   : ["Theta Functions and Transcendence"]
container-title : ["The Ramanujan Journal"]
volume  : "1"
issue   : "4"
page    : "339-350"
published-print : {"date-parts": [[1997, 12]]}
author  : [{"given": "Daniel", "family": "Bertrand", "sequence": "first"}]
ISSN    : ["1382-4090", "1572-9303"]
type    : "journal-article"
```

**zbMATH Open**, document 1185660 / **Zbl 0916.11043**:

```
title   : "Theta functions and transcendence"
authors : ['Bertrand, Daniel']
source  : "Ramanujan J. 1, No. 4, 339-350 (1997)."
series  : The Ramanujan Journal, vol 1, issue 4, 1997, Springer US, New York, NY
links   : doi 10.1023/A:1009749608672
msc     : 11J91 (Transcendence theory of other special functions), 11F03
```

**Crossref issue listing, Ramanujan J. vol. 1 no. 4 (1997)** — an "Editorial" by Alladi at p. 331
opens the issue, then: Kim–Kim–Raghavan 333–337; **Bertrand 339–350**; Mignotte–Roy 351–356;
Amoroso 357–362; Kanemitsu–Yoshimoto 363–378; Roy–Waldschmidt 379–430; Gordon–McIntosh 431–448.
Consistent with a number-theory-symposium special issue.

**Waldschmidt's bibliography** (*Open Diophantine Problems*, arXiv:math/0312440, and identically in
*AWS Lecture 5*), verbatim:

> Bertrand, D. – Theta functions and transcendence. International Symposium on Number Theory
> (Madras, 1996). Ramanujan J. 1 N° 4 (1997), 339–350.

**All bibliographic fields the report gave are CONFIRMED**: volume 1, 1997, issue 4, pages 339–350,
title "Theta functions and transcendence". The conference name in print is **"International
Symposium on Number Theory (Madras, 1996)"** (Waldschmidt) or **"Madras Number Theory Symposium
1996"** (Diaz's own bibliography); **"January 1996"** comes from Diaz's prose (*"Lors d'une
conférence à Madras en janvier 1996"*, p. 229), not from a bibliography entry.

### Raw evidence — §5 content

I could not read the paper. Springer is behind an IdP redirect, Semantic Scholar reports the
abstract "elided by the publisher", zbMATH's web front end serves a Cloudflare challenge, and
Bertrand's IMJ-PRG page (last updated 18/01/2015) carries no publication list. No arXiv version
exists (the paper predates his arXiv activity). **Three independent-ish secondary readings:**

**(i) zbMATH review, Zbl 0916.11043 — signed "Guy Diaz (Saint Etienne)".** Closing sentences,
verbatim:

> Le dernier paragraphe est consacré à deux conjectures portant sur l'invariant modulaire \(J\); la
> seconde contient un cas particulier de la célèbre ``conjecture des quatre exponentielles''. Cet
> article a un prolongement dans le texte de *D. Bertrand* [\(\Theta(\tau, z)\) and transcendence,
> in Introduction to algebraic independence theory, Yu. Nesterenko and P. Philippon (eds.), Lect.
> Notes Math. 1752, 1--11 (2001; Zbl 0966.11032)].

This says the **last section** carries **two** conjectures on `J`, the **second** of which contains
a special case of the four-exponentials conjecture. That is exactly Diaz's §I description. **But the
reviewer is Diaz himself.** It is a second document by the same author, not a second author. Label
it as such and do not present it as independent corroboration.

**(ii) Diaz 1997, §I, p. 231** (primary for *Diaz's* claim, secondary for Bertrand's): cites
"[2], §5" **twice** — once for "D. Bertrand propose dans [2], §5, plusieurs conjectures pour la
fonction modulaire J", once for "Cette implication, établie dans [2], §5". Quoted in full under
ITEM 1(e).

**(iii) Waldschmidt, *Open Diophantine Problems* / *AWS Lecture 5*.** These are the report's cited
support for MUST 3, and **they do not support what the report says they support.** Verbatim, AWS
Lecture 5, p. 118 (identically ODP §3):

> Further related open problems are proposed by G. Diaz in [Di 1997] and [Di 2000], in connection
> with conjectures due to D. Bertrand on the values of the modular function J(q), where
> j(τ) = J(e^{2iπτ}) (see [Bert 1997b] as well as [NeP 2001] Chap. 1, § 4 and Chap. 2, § 4).
>
> **Conjecture 5.34 (Bertrand).** Let q₁, …, q_n be non-zero algebraic numbers in the unit open disc
> such that the 3n numbers J(q_i), DJ(q_i), D²J(q_i) (i = 1, …, n) are algebraically dependent over
> Q̄. Then there exist two indices i ≠ j (1 ≤ i ≤ n, 1 ≤ j ≤ n) such that q_i and q_j are
> multiplicatively dependent.
>
> **Conjecture 5.35 (Bertrand).** Let q₁ and q₂ be two non-zero algebraic numbers in the unit open
> disc. Suppose that there is an irreducible element P ∈ Q̄[X, Y] such that P(J(q₁), J(q₂)) = 0.
> Then there exist a constant c and a positive integer s such that P = cΦ_s, where Φ_s is the modular
> polynomial of level s. Moreover q₁ and q₂ are multiplicatively dependent.

Two consequences. **First, this is real, independent, printed corroboration that Bertrand has two
named modular conjectures**, and 5.35 is recognizably the same object as Diaz's remark inside the
proof of Théorème 2(b) — *"D. Bertrand conjecture que pour q₁, q₂ ∈ D\* ∩ ℚ̄ les seules relations
de dépendance algébrique irréductibles possibles entre J(q₁) et J(q₂) sont de la forme Φ_s = 0, à
constante multiplicative près (voir conjecture 2 de [2])"*. Waldschmidt cites `[Bert 1997b]` = the
Ramanujan J. paper. **Second, neither 5.34 nor 5.35 is the weak four-exponentials statement, and
neither mentions "§5".** Waldschmidt never writes "weak four exponentials": grepped, zero hits, in
*Open Diophantine Problems* (58 pp.), *AWS Lecture 5*, and *LIL*. **The report's parenthetical —
that the §5 attribution was "read via … Waldschmidt's AWS Lecture 5 Conjectures 5.34/5.35" — is
wrong.** AWS 5 supplies Bertrand's modular conjectures; the "§5" locator comes from Diaz alone.

### Verdict — ITEM 2

**PARTIALLY_VERIFIED.** Every bibliographic field is now **independently confirmed** from two
primary-grade records (Crossref DOI record and zbMATH Open), so the report's "not independently
verified" hedge on the *reference* can be dropped. The **§5 content claim remains UNVERIFIED from
the source**: I did not read Bertrand's paper, and the best evidence is a zbMATH review written by
Diaz plus Diaz's own article. The report's naming of AWS Lecture 5 as support for the §5 attribution
is **REFUTED** and must not be repeated.

### Ready-to-paste citation

    D. Bertrand, *Theta functions and transcendence*, International Symposium on Number Theory
    (Madras, 1996), Ramanujan J. **1** (1997), no. 4, 339-350; doi:10.1023/A:1009749608672;
    Zbl 0916.11043.

Recommended accompanying wording (the honest form — it says whose word the §5 locator is on):

    ... the special case of the four-exponentials conjecture aimed at by D. Bertrand [Bertrand,
    Ramanujan J. 1 (1997), Sect. 5, as reported by Diaz, JTNB 9 (1997), 231]. Bertrand's two
    conjectures on the modular function J from that section are stated as Conjectures 5.34 and
    5.35 in Waldschmidt, Open Diophantine Problems, Moscow Math. J. 4 (2004), 245-305.

Do **not** write "January 1996" in the reference itself unless the seed note also cites Diaz for it;
the printed conference designation is "International Symposium on Number Theory (Madras, 1996)".

---

## ITEM 3 (report MUST 4) — Schneider 1957 / Lang / Ramachandra

### What the report claimed

> **Th. Schneider, *Einführung in die transzendenten Zahlen*, Springer, 1957, Ch. V §4, Problem 1
> (French ed.: *Introduction aux nombres transcendants*, Gauthier-Villars, 1959, p. 139)** — the
> four-exponentials conjecture, with the later explicit formulations by S. Lang (Sém. Bourbaki 305,
> 1965/66; Topology 5 (1966), 363–370) and K. Ramachandra (Acta Arith. 14 (1968), 65–88).
> *(Not held; attribution verified twice via Diaz 1997 §0 and Waldschmidt LIL Ch. 1.)*

### Commands run

```
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=au%3ASchneider%20%26%20ti%3A%22Einf%C3%BChrung%20in%20die%20transzendenten%20Zahlen%22&results_per_page=5"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=ti%3A%22Introduction%20aux%20nombres%20transcendants%22&results_per_page=5"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=au%3ALang%20%26%20py%3A1966%20%26%20so%3ATopology&results_per_page=5"
curl -sS "https://api.zbmath.org/v1/document/_search?search_string=au%3ARamachandra%20%26%20py%3A1968%20%26%20so%3A%22Acta%20Arith%22&results_per_page=5"
curl -sS -L "http://www.numdam.org/volume/SB_1964-1966__9_/"
curl -sS -L "http://www.numdam.org/item/SB_1964-1966__9__391_0/"   # Gramain, exp. 304
curl -sS -L "http://www.numdam.org/item/SB_1964-1966__9__407_0/"   # Lang,    exp. 305
curl -sS -L "http://www.numdam.org/item/SB_1964-1966__9__415_0/"   # Tate,    exp. 306
curl -sS -L "https://www.numdam.org/item/SB_1964-1966__9__407_0.pdf" -> lang-bourbaki305.pdf
curl -sS -L "https://arxiv.org/pdf/math/0312440"                      -> Waldschmidt, Open Diophantine Problems
curl -sS -L "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf"
curl -sS -L "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LIL.pdf"
curl -sS -L "https://www.sciencedirect.com/science/article/pii/0040938366900280"  # Elsevier bot wall, unusable
```

### 3a. Schneider, German original

**zbMATH Zbl 0077.04703**, verbatim:

```
title   : Einführung in die transzendenten Zahlen
authors : ['Schneider, Theodor']
year    : 1957
series  : Grundlehren der Mathematischen Wissenschaften, volume 81, ISSN 0072-7830
source  : "Die Grundlehren der Mathematischen Wissenschaften. Band 81.
           Berlin-Göttingen-Heidelberg: Springer-Verlag. 150 p. DM 24,20 (1957)."
```

**The question asked — is the series "Grundlehren der mathematischen Wissenschaften 81"? — is
CONFIRMED: Band 81, 150 pages, Springer-Verlag, Berlin–Göttingen–Heidelberg, 1957.** The report
omitted the series and volume; they should be added.

Waldschmidt's own bibliography entry (ODP, secondary but printed), verbatim:

> Schneider, Th. – Einführung in die transzendenten Zahlen. Springer-Verlag,
> Berlin-Göttingen-Heidelberg, 1957. Introduction aux nombres transcendants. Traduit de l'allemand
> par P. Eymard. Gauthier-Villars, Paris 1959.

### 3b. Schneider, French translation

**zbMATH Zbl 0098.26304**, verbatim:

```
title   : Introduction aux nombres transcendants. Traduit par P. Eymard
authors : ['Schneider, T.']
year    : 1959
source  : "Paris: Gauthier-Villars. viii, 151 p. (1959)."
```

**Publisher, city, year CONFIRMED**; the translator is **P. Eymard**, which the report omits. Diaz's
page citation is p. 139 (Diaz 1997, p. 229: *"premier problème de Schneider, 1957, voir [7] p.139"*)
and the book runs to 151 pages, so p. 139 falls in the closing problem list, as it should.
**I could not open the book; the page number rests on Diaz.**

### 3c. "Ch. V §4, Problem 1" — the locator the report gives

Two independent Waldschmidt texts give it, verbatim.

*Open Diophantine Problems* (arXiv:math/0312440), §3, immediately before Conjecture 3.7:

> Finally a special case of Conjecture 3.6 is the well known Four Exponentials Conjecture due to
> Schneider [Schn 1957] Chap. V, end of §4, Problem 1; S. Lang [La 1966] Chap. II, §1; [La 1971]
> p. 638 and K. Ramachandra [R 1968 II] §4.

*AWS Lecture 5*, p. 107–108, the same sentence with an internal cross-reference added:

> Finally a special case of Conjecture 5.10 is the well known Four Exponentials Conjecture (see
> 2.48) due to Schneider ([Schn 1957] Chap. V, end of § 4, Problem 1), S. Lang ([La 1966] Chap. II,
> § 1; [La 1971] p. 638) and K. Ramachandra ([R 1968 II], § 4).

*LIL* (Linear Independence of Logarithms of Algebraic Numbers), Ch. 1, p. 1-9:

> The four exponentials conjecture is equivalent to the first of the eight problems at the end of
> Schneider's book [S].

**"Chap. V, end of §4, Problem 1" is CONFIRMED as Waldschmidt's locator, stated twice, and LIL
independently confirms it is the *first* of the closing problems.** All three are **secondary** —
I did not open Schneider's book — and must be labeled as such. Note the small sharpening: it is
"end of §4", and LIL says there are **eight** such problems.

**A note the report does not carry and the seed note should.** Waldschmidt's Lang locator is the
**book** — `[La 1966]` = *Lang, S. – Introduction to transcendental numbers. Addison-Wesley
Publishing Co., Reading, Mass.-London-Don Mills, Ont. 1966. Collected Papers, vol. I, Springer
(2000), 396–506*, Chap. II §1 — plus `[La 1971]` = *Lang, S. – Transcendental numbers and
Diophantine approximations. Bull. Amer. Math. Soc. 77 (1971), 635–677*, p. 638. **Not** the Bourbaki
exposé and **not** the Topology paper. The report picked a different pair of Lang references; both
pairs are defensible, and the reason the report's pair is defensible is 3e below.

### 3d. Lang, Séminaire Bourbaki exposé 305

**A near-miss worth recording.** The Numdam *volume* listing page interleaves exposé numbers and
titles in an order that reads, on a naive scrape, as though **exposé 305 were Tate's Birch–
Swinnerton-Dyer talk** and Lang's transcendence talk were 304. It is not. Fetching the three item
pages individually settles it. **Numdam item page `SB_1964-1966__9__407_0`**, verbatim:

> Séminaire Bourbaki | no. 9 | Exposé no. 305 | Suivant
> **Nombres transcendants**
> Lang, Serge
> Séminaire Bourbaki : années 1964/65 1965/66, exposés 277-312,
> Séminaire Bourbaki, no. 9 (1966), **Exposé no. 305, 8 p.**
> `@incollection{SB_1964-1966__9__407_0, author = {Lang, Serge}, title = {Nombres transcendants}, …`

Its neighbors, for the record: `…__391_0` = **Exposé no. 304**, Gramain, *L'invariance topologique
des classes de Pontrjagin rationnelles*, 16 p.; `…__415_0` = **Exposé no. 306**, Tate, *On the
conjectures of Birch and Swinnerton-Dyer and a geometric analog*, 26 p.

The PDF's own cover page, verbatim:

> S ÉMINAIRE N. B OURBAKI / S ERGE L ANG / **Nombres transcendants** / Séminaire N. Bourbaki, 1966,
> exp. no 305, **p. 407-414**

and its first page header:

> Séminaire BOURBAKI / **18e année, 1965/66, n° 305** / **Février 1966.** /
> NOMBRES TRANSCENDANTS / par Serge LANG

**CONFIRMED: exposé number 305, volume 9 covering 1964/65 and 1965/66, exposés 277–312, delivered
February 1966, pages 407–414, title "Nombres transcendants".** The report gave "Sém. Bourbaki 305,
1965/66" with no title and no pages; both are now available.

**Content.** Théorème 1 of the exposé is the six-exponentials theorem (the 3 × 2 case). Its
Corollaire 3, verbatim, is the Alaoglu–Erdős application: *"De tous les nombres 2^s, 3^s, 5^s, …, au
plus deux sont algébriques."* The four-exponentials conjecture appears not as a labeled conjecture
but as a wish, verbatim:

> On voudrait bien réduire d'une unité le nombre 3 dans le Théorème 1, mais il semble que cela soit
> nettement plus profond.

**So Bourbaki 305 poses the four-exponentials problem but does not display it as a numbered
conjecture.** Calling it a "later explicit formulation", as the report does, is defensible only
because Waldschmidt says so (3e); on the page itself it is one sentence of wishing.

### 3e. Lang, Topology 5 (1966), 363–370, and Ramachandra, Acta Arith. 14 (1968)

**zbMATH Zbl 0168.19002**, verbatim:

```
title   : Algebraic values of meromorphic functions. II
authors : ['Lang, Serge']
source  : "Topology 5, 363-370 (1966)."
links   : doi 10.1016/0040-9383(66)90028-0
```

**The title the report omitted is "Algebraic values of meromorphic functions. II"**; volume, year,
pages and DOI are CONFIRMED. I could **not** read the paper — ScienceDirect served an 832 KB bot
wall with no metadata — so **the content claim (that it formulates 4EC explicitly) is verified only
through Waldschmidt**, quoted below.

**zbMATH Zbl 0176.33101**, verbatim:

```
title   : Contributions to the theory of transcendental numbers. I, II
authors : ['Ramachandra, K.']
source  : "Acta Arith. 14, 65-72 (1968); 14, 73-88 (1968)."
links   : doi 10.4064/aa-14-1-65-72 ; eudml.org/doc/204849
```

**CORRECTION to the report.** The report writes "K. Ramachandra (Acta Arith. 14 (1968), 65–88)" as
though it were one paper. It is **two**: part I at 65–72 and part II at 73–88, both Acta Arith. 14
(1968). Waldschmidt's own bibliography uses the combined form — *"Ramachandra, K. – Contributions
to the theory of transcendental numbers. I, II. Acta Arith. 14 (1967/68), 65-72 and 73–88."* — and
his 4EC attribution line points specifically at **`[R 1968 II] §4`**, i.e. part II. If the seed note
wants to cite the four-exponentials formulation, it should cite **part II, 73–88, §4**.

**The sentence that vindicates the report's Lang/Ramachandra pair.** Waldschmidt, *LIL*, Ch. 1,
p. 1-9, verbatim:

> The six exponentials theorem can be deduced from a very general (and complicated) result of
> Schneider (Ein Satz über ganzwertige Funktionen als Prinzip für Transzendenzbeweise, Math. Ann.
> 121 (1949), 131–140). The four exponentials conjecture is equivalent to the first of the eight
> problems at the end of Schneider's book [S]. An explicit statement of the six exponentials
> conjecture, together with a proof, has been published independently and at about the same time by
> S. Lang and K. Ramachandra:
> – S. Lang, Nombres transcendants, Sém. Bourbaki 18ème année (1965/66), N° 305; Algebraic values of
> meromorphic functions, 2, Topology 5 (1966), 363–370; see also [L] Chap.2.
> – K. Ramachandra, Contributions to the theory of transcendental numbers, Acta Arith. 14 (1968),
> 65–88; see also [R] Chap.2.
> **They both formulated the four exponentials conjecture explicitly.**

(The words "six exponentials conjecture" there are a slip for "theorem"; the theorem is what is
proved and the conjecture is what is formulated, as the closing sentence makes explicit.) **This is
where the report's MUST-4 lineage comes from, and on this evidence its Lang and Ramachandra
references are CORRECT** — both the Bourbaki exposé and the Topology paper, and Acta Arith. 14
(1968) 65–88.

**Bonus, and directly relevant to the seed note's framing.** LIL Ch. 1, p. 1-8, verbatim:

> The six exponentials theorem occurs for the first time in a paper by L. Alaoglu and P. Erdős : On
> highly composite and similar numbers, Trans. Amer. Math. Soc. 56 (1944), 448–469; when these
> authors try to prove Ramanujan's assertion that the quotient of two consecutive superior highly
> composite numbers is a prime, they need to know that if x is a real number such that p₁^x and p₂^x
> are both rational numbers, with p₁ and p₂ distinct prime numbers, then x is an integer; however
> this statement (special case of the four exponentials conjecture) is yet unproved; they quote
> Siegel and claim that x indeed is an integer if one assumes p_i^x to be rational for three
> distinct primes p_i; this is just a special case of the six exponentials theorem.

The report's claim that "the two-distinct-primes germ is Alaoglu–Erdős 1944" is **CONFIRMED via
Waldschmidt (secondary, quoted above; the Alaoglu–Erdős paper itself was not opened)**. The seed
note is welcome to it: the "two distinct primes vs. three distinct primes" structure that the note
rediscovers in its §7 (six exponentials blocked, four exponentials needed) is the 1944 obstruction,
described in exactly those terms.

### Verdict — ITEM 3

**CORRECTED.** All five sub-references check out with three fixes and three additions:

| field | report | primary source | action |
|---|---|---|---|
| Schneider German, series | not given | Grundlehren der Math. Wiss. **81**, 150 pp. (Zbl 0077.04703) | **add** |
| Schneider German, cities | "Springer, 1957" | Springer-Verlag, Berlin-Göttingen-Heidelberg, 1957 | add |
| Schneider French, translator | not given | **traduit par P. Eymard**, viii+151 pp. (Zbl 0098.26304) | **add** |
| Schneider French, publisher/year/page | Gauthier-Villars, 1959, p. 139 | Paris: Gauthier-Villars, 1959; p. 139 per Diaz only | confirmed / book not opened |
| "Ch. V §4, Problem 1" | asserted | Waldschmidt ODP + AWS5, verbatim, twice; LIL "first of the eight problems" | confirmed, **secondary** |
| Lang Bourbaki 305 | number + year | **exp. 305, "Nombres transcendants", 1965/66, Feb. 1966, pp. 407-414** | **add title/pages** |
| Lang Topology 5 | no title | **"Algebraic values of meromorphic functions. II"**, doi:10.1016/0040-9383(66)90028-0 | **add title/DOI** |
| Ramachandra | "Acta Arith. 14 (1968), 65-88" | **two papers: I, 65-72; II, 73-88**; 4EC is in **II, §4** | **CORRECT** |

### Ready-to-paste citations

    Th. Schneider, *Einfuhrung in die transzendenten Zahlen*, Grundlehren der mathematischen
    Wissenschaften **81**, Springer-Verlag, Berlin-Gottingen-Heidelberg, 1957, 150 pp.;
    Ch. V, end of Sect. 4, Problem 1. French translation: *Introduction aux nombres
    transcendants*, traduit par P. Eymard, Gauthier-Villars, Paris, 1959, viii+151 pp., p. 139.
    (Chapter and problem locator per M. Waldschmidt, *Open Diophantine Problems*, Moscow Math.
    J. **4** (2004), 245-305, Sect. 3 -- book not consulted directly.)

    S. Lang, *Nombres transcendants*, Seminaire Bourbaki, 18e annee (1965/66), exp. no. 305,
    Feb. 1966, pp. 407-414; <http://www.numdam.org/item?id=SB_1964-1966__9__407_0>.

    S. Lang, *Algebraic values of meromorphic functions. II*, Topology **5** (1966), 363-370;
    doi:10.1016/0040-9383(66)90028-0. (Not read directly; its explicit formulation of the
    four-exponentials conjecture is reported by M. Waldschmidt, *Linear Independence of
    Logarithms of Algebraic Numbers*, Ch. 1.)

    K. Ramachandra, *Contributions to the theory of transcendental numbers. I, II*, Acta Arith.
    **14** (1968), 65-72 and 73-88; doi:10.4064/aa-14-1-65-72; the four-exponentials conjecture
    is formulated in part II, Sect. 4.

Optionally, and worth it, for the umbrella statement of the lineage:

    M. Waldschmidt, *Open Diophantine Problems*, Mosc. Math. J. **4** (2004), no. 1, 245-305;
    arXiv:math/0312440, Conjecture 3.7 and the attribution sentence preceding it.

(Waldschmidt's own Lang locator is the book -- S. Lang, *Introduction to Transcendental Numbers*,
Addison-Wesley, Reading, Mass., 1966, Ch. II Sect. 1, and *Transcendental numbers and Diophantine
approximations*, Bull. Amer. Math. Soc. **77** (1971), 635-677, at p. 638. Carry these alongside
Bourbaki 305 and Topology 5, or instead of them if the seed note wants one Lang reference only.)

---

## Sources that could not be reached, and what was substituted

* **D. Bertrand, Ramanujan J. 1 (1997), 339–350** — Springer IdP redirect; Semantic Scholar reports
  the abstract elided by the publisher; zbMATH's web UI is behind Cloudflare; the author's page has
  no publication list. Substituted: Crossref + zbMATH Open records (bibliography, fully sufficient)
  and, for §5, the zbMATH review **written by Diaz** plus Diaz's article, plus Waldschmidt's
  Conjectures 5.34/5.35 for the existence and shape of Bertrand's two modular conjectures.
* **Th. Schneider, *Einführung in die transzendenten Zahlen*, 1957** — not held anywhere reachable.
  Substituted: zbMATH catalog records for both editions (series, volume, pagination, translator) and
  Waldschmidt's locator, quoted twice, labeled secondary.
* **S. Lang, Topology 5 (1966)** — Elsevier bot wall. Substituted: zbMATH record (title, pages, DOI)
  and Waldschmidt LIL for the content claim, labeled secondary.
* **zbMATH web front end** — Cloudflare interstitial on every request. The **API** (`api.zbmath.org`)
  works without a challenge and returns full review text; use it, not the site.
* **MathSciNet** — no access, as in prior sessions. zbMATH Open covered every needed record.

## Method notes for the executing session

1. **The Numdam Diaz PDF's OCR layer is not trustworthy for mathematics.** `pdftotext` silently ate
   `π²` from (C6), the `/2iπ` from the reduction, and `alors` from Proposition 1. Render the page
   (`pdftoppm -r 200 -png`) and read the image before quoting anything from this paper.
2. **Numdam volume-listing pages interleave exposé numbers and titles misleadingly.** A scrape of
   the Bourbaki vol. 9 listing appears to make Lang exposé 304 and Tate exposé 305. Fetch the
   individual `/item/…` pages — they carry the exposé number unambiguously in the breadcrumb and in
   the BibTeX block.
3. **A zbMATH review signed by the same person who wrote the citing article is not independent
   evidence.** Zbl 0916.11043's review of Bertrand is by Guy Diaz. Useful, but label it.
4. Local copies retained under `results/arxiv/citation-verification/assets/`:
   `diaz-1997-jtnb9-quatre-exponentielles-numdam.pdf`,
   `lang-1966-seminaire-bourbaki-305-nombres-transcendants-numdam.pdf`.
