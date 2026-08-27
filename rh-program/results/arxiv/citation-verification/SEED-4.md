# CLUSTER SEED-4 — lineage repair for `results/c3-r/seed-no-go-note.md`

Verification session, 2026-08-27. Every field below was checked against a primary source
(arXiv abs page HTML, arXiv PDF title page, Crossref REST, zbMATH Open, the Comptes Rendus
publisher page, or the on-disk full text). Where the agent report and a primary source disagree,
the primary source is recorded as authoritative and the disagreement is stated explicitly.

**Headline result.** The note's lineage sentence is wrong and the report's correction is right.
The per-prime "analogue of an elliptic curve" is Connes-Consani, **21 July 2015**
(arXiv:1507.05818v1 = the C. R. note), not January 2025. The gap is **9 years 5.7 months**.
But the report's *mechanism* claim about the [CC26] title is **wrong** (see Item 2), and the
substantive identification of the 2015 object needs a correction the report did not make:
the 2015 object is **C_p = R*_+ / p^Z**, a real circle of length log p, **not** the complex
Tate curve C*/p^Z. The June-2026 paper says so itself, in its own abstract.

---

## ITEM 1 (MUST 6) — A. Connes and C. Consani, "The Scaling Site"

### 1(a) The Comptes Rendus note

Report claimed: C. R. Math. Acad. Sci. Paris **354** (2016), 1-6.

Commands:

```
curl -s "https://api.crossref.org/works?query.bibliographic=Connes+Consani+The+Scaling+Site+Comptes+Rendus&rows=5&select=DOI,title,container-title,volume,issue,page,issued,author,type"
curl -s "https://api.crossref.org/works/10.1016/j.crma.2015.09.027"
curl -s "https://api.zbmath.org/v1/document/_search?search_string=Connes%20Consani%20scaling%20site&results_per_page=8"
curl -sL "https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2015.09.027/"
```

Crossref (`10.1016/j.crma.2015.09.027`), verbatim fields:

```
DOI = "10.1016/j.crma.2015.09.027"
type = "journal-article"
title = ["The scaling site"]
container-title = ["Comptes Rendus. Mathematique"]
volume = "354"
issue = "1"
page = "1-6"
published-online = {"date-parts": [[2015, 11, 3]]}
issued = {"date-parts": [[2015, 11, 3]]}
publisher = "MathDoc/Centre Mersenne"
AUTH = [('Alain', 'Connes'), ('Caterina', 'Consani')]
```

Crossref carries **no** `published-print`, only `published-online` = 2015-11-03. That is the
online-first date, not the issue date, so Crossref alone does not settle the year. Two further
primary sources do:

zbMATH Open, record 6579838:

```
6579838 | The scaling site | 2016
    SRC: C. R., Math., Acad. Sci. Paris 354, No. 1, 1-6 (2016).
    DOI: 10.1016/j.crma.2015.09.027
```

Publisher page (comptes-rendus.academie-sciences.fr), text extracted from the HTML:

```
Number theory/Algebraic geometry
The scaling site
[Le site des frequences]
Alain Connes 1, 2, 3 ; Caterina Consani 4
1 College de France, 3 rue d'Ulm, 75005 Paris, France  2 I.H.E.S., France
3 Ohio State University, USA  4 The Johns Hopkins University, Baltimore, MD 21218, USA
Comptes Rendus. Mathematique, Volume 354 (2016) no. 1, pp. 1-6
```

**Verdict: CONFIRMED.** Volume 354, issue 1, pp. 1-6, year **2016**, DOI 10.1016/j.crma.2015.09.027.
Exact title as published: *The scaling site* (lower-case "scaling site"), with the French
alternative title *Le site des frequences*. The arXiv PDF title page styles it "The Scaling Site";
the journal of record styles it "The scaling site". Use the journal styling.

Ready to paste:

    A. Connes and C. Consani, *The scaling site*, C. R. Math. Acad. Sci. Paris **354** (2016),
    no. 1, 1-6; doi:10.1016/j.crma.2015.09.027; arXiv:1507.05818.

### 1(b) arXiv:1507.05818 — v1 date and the load-bearing sentence

Commands:

```
curl -sL "https://arxiv.org/abs/1507.05818"     # metadata abstract (latest = v2)
curl -sL "https://arxiv.org/abs/1507.05818v1"   # metadata abstract as of v1
curl -sL "https://arxiv.org/pdf/1507.05818v1" -o 1507.05818v1.pdf ; pdftotext -f 1 -l 1 ... 
```

Submission history, from the abs page:

```
Submission history From: Alain Connes [view email]
[v1] Tue, 21 Jul 2015 13:16:02 UTC (55 KB)
[v2] Thu, 24 Sep 2015 08:25:59 UTC (56 KB)
Comments: 8 pages, minor typos and style corrected, notations clarified in v2
```

**v1 date CONFIRMED: 21 July 2015.**

The abstract, quoted verbatim from the abs page (identical on the v1 abs page and the current
abs page — I diffed them; the sentence in question is present in **v1**):

> We investigate the semi-ringed topos obtained by extension of scalars from the arithmetic site
> of our previous work, by replacing the smallest Boolean semifield by the tropical semifield of
> real numbers with the max-plus operations. The obtained site is the semi-direct product of the
> Euclidean half-line by the action of the monoid of positive integers by multiplication. Its
> points are the same as the points of the arithmetic site over the tropical semifield of real
> numbers, and coincide with the quotient of the adele class space of Q by the action of the
> maximal compact subgroup of the idele class group. The structure sheaf of the scaling topos
> endows it with a natural structure of tropical curve over the arithmetic topos. The restriction
> of this structure to the periodic orbits of the scaling flow gives, for each prime p, an
> analogue of an elliptic curve whose Jacobian is a cyclic group of order p-1. The Riemann-Roch
> formula holds and involves real valued dimensions and real degrees for divisors.

Exact-substring test of the claimed sentence against the fetched abstract returned `True`:

```
target = 'The restriction of this structure to the periodic orbits of the scaling flow gives, for
each prime p, an analogue of an elliptic curve whose Jacobian is a cyclic group of order p-1.'
EXACT SUBSTRING MATCH: True
SENT IN V1: True
```

**Verdict: CONFIRMED WORD FOR WORD**, and present already in v1 (21 July 2015).

Corroboration from the PDF's own abstract (v1 title page, `pdftotext -f 1 -l 1`), which is
slightly more specific than the arXiv metadata and is the better thing to quote in the note:

```
arXiv:1507.05818v1 [math.AG] 21 Jul 2015

The Scaling Site
Le Site des Frequences
Alain Connes a, Caterina Consani b,1
...
The restriction of this structure to the periodic orbits of the scaling flow gives, for each
prime p, an analogue Cp of an elliptic curve whose Jacobian is Z/(p-1)Z. The Riemann-Roch
formula holds on Cp and involves real valued dimensions and real degrees for divisors.
```

Note the PDF names the object **C_p** and gives the Jacobian as **Z/(p-1)Z**; the arXiv metadata
paraphrases it as "a cyclic group of order p-1".

### 1(c) "Geometry of the scaling site" — Selecta

Report claimed: Selecta Math. (N.S.) **23** (2017), 1803-1850; arXiv:1603.03191.

Crossref (`10.1007/s00029-017-0313-y`):

```
title = ["Geometry of the scaling site"]
container-title = ["Selecta Mathematica"]
short-container-title = ["Sel. Math. New Ser."]
volume = "23"   issue = "3"   page = "1803-1850"
published-print = {"date-parts": [[2017, 7]]}
published-online = {"date-parts": [[2017, 3, 1]]}
AUTH = [('Alain', 'Connes'), ('Caterina', 'Consani')]
```

zbMATH 6745643: `Sel. Math., New Ser. 23, No. 3, 1803-1850 (2017). DOI: 10.1007/s00029-017-0313-y`.

Identification of arXiv:1603.03191 with the Selecta paper: the abs page gives
title "Geometry of the scaling site", authors Connes and Consani, v1 Thu, 10 Mar 2016, 43 pages,
7 figures, and an abstract whose text is the Selecta abstract. The arXiv record carries **no**
journal-ref (I grepped the abs page: the only DOI on it is the arXiv DataCite DOI
`10.48550/arXiv.1603.03191`). Identification therefore rests on identical title + authors +
abstract + Crossref/zbMATH agreement, which is sufficient; flagged here for honesty.

**Verdict: CONFIRMED** (all fields; the issue number 3 is an addition the report omitted).

Ready to paste:

    A. Connes and C. Consani, *Geometry of the scaling site*, Selecta Math. (N.S.) **23** (2017),
    no. 3, 1803-1850; doi:10.1007/s00029-017-0313-y; arXiv:1603.03191.

### 1 — WHAT THE PER-PRIME OBJECT ACTUALLY IS (the part the rewrite turns on)

This is the substantive question and the answer is unambiguous in both papers.

**In arXiv:1507.05818 (C. R. note), section 6**, `pdftotext` of the v2 PDF:

> Let p be a prime and consider the subspace C_p of points of [0, infinity) x| N^x corresponding
> to subgroups H subset R which are abstractly isomorphic to the subgroup H_p subset Q of
> fractions with denominator a power of p.
>
> **Lemma 6.3** The map R*_+ -> C_p, lambda |-> lambda H_p induces a topological isomorphism
> eta_p : R*_+ / p^Z -> C_p. The pullback by eta_p of the structure sheaf O is the sheaf O_p on
> R*_+ / p^Z of piecewise affine, continuous convex functions, with slopes in H_p.

and

> **Theorem 6.5** The map chi : H -> H_p/(p-1)H_p vanishes on principal divisors and it induces
> an isomorphism of groups chi : J(C_p) -> Z/(p-1)Z ...
>
> **Theorem 6.7** (ii) The following Riemann-Roch formula holds
> Dim_R(H^0(D)) - Dim_R(H^0(-D)) = deg(D), for all D in Div(C_p).

**In arXiv:1603.03191 (Selecta), abstract and introduction (p. 3), and section 5
"The periodic orbits C_p", Lemma 5.1**, `pdftotext`:

> We restrict this construction to the periodic orbit of the scaling flow associated to each
> prime p and obtain a quasi-tropical structure which turns this orbit into a **variant
> C_p = R*_+ / p^Z of the classical Jacobi description C*/q^Z of an elliptic curve.**

> We find that for each prime p the corresponding **circle of length log p** is endowed with a
> quasi-tropical structure which turns this orbit into a variant C_p = R*_+ / p^Z of the classical
> Jacobi description C*/q^Z of an elliptic curve. The structure sheaf O_p of C_p is obtained by
> restriction of O to C_p and its sections are periodic functions f(p lambda) = f(lambda),
> lambda in R*_+, which are convex, piecewise affine and whose derivatives take values in the
> group H_p subset R of rational numbers with denominators a power of p.

> **Lemma 5.1.** (i) The map R*_+ -> C_p, lambda |-> lambda H_p induces the isomorphism
> eta_p : R*_+ / p^Z -> C_p.

**Connes-Consani's own later gloss**, arXiv:2401.08401, introduction p. 3:

> We refer to [6] for the structure of C_p inherited from the scaling site : **C_p = R*_+ / p^Z
> appears as an elliptic curve in characteristic one, similar to the Jacobi elliptic curve
> C*/q^Z.** The Riemann-Roch formula for C_p involves real valued dimensions.

**So, precisely:**

* The per-prime object of July 2015 is **C_p = R*_+ / p^Z**: a **real** circle of circumference
  log p, the periodic orbit of the scaling flow, carrying a characteristic-one (idempotent,
  max-plus) structure sheaf of convex piecewise-affine functions with slopes in Z[1/p].
* It is an **analogue** of an elliptic curve, in characteristic one: it has divisors, principal
  divisors, theta functions, a Jacobian J(C_p) = Z/(p-1)Z, and a Riemann-Roch theorem with
  **real-valued** dimensions. It is **not** an elliptic curve over any field.
* It is **not** C*/p^Z. Connes and Consani say explicitly that it is a *variant of*, and *similar
  to*, the classical Jacobi model C*/q^Z. The base is R*_+, not C*; the object is
  1-dimensional over R, not 2.

**The honest relationship to the June-2026 object** is stated by the June-2026 paper itself
(arXiv:2606.06604, abstract, verbatim from the abs page):

> Quotienting the archimedean orbit by the discrete Frobenius symmetries yields the complex Tate
> curve with modulus q = p^{-1}. We show that this elliptic curve canonically decomposes as the
> product of its real locus, which exactly recovers the adelic periodic orbit
> C_p = R_+^x / p^Z, and a p-independent phase space that emerges naturally as a real analogue of
> the Fargues-Fontaine curve.

and in the body (Theorem 5, and section 4.1.2 "The Tate curve E_p"):

> The Tate curve E_p = C^x / p^Z arises from quotienting the space of non-trivial local morphisms
> M_p^infty by the discrete arithmetic symmetry group p^Z ...
>
> The first factor of this decomposition is the periodic orbit C_p = R_+^x / p^Z of the adelic
> scaling site. It constitutes the connected component of the real locus of E_p and carries the
> entire dependence on the prime p. The second factor X~_infty is the (p-independent) real
> analogue of the Fargues-Fontaine-curve.

**Therefore the correct lineage sentence is:** the per-prime characteristic-one analogue of an
elliptic curve, C_p = R*_+ / p^Z, is Connes-Consani, July 2015; the **complex** Tate curve
E_p = C*/p^Z appears in the CC program in June 2026, where C_p is identified as its real locus.
The 2015 object is an antecedent of the 2026 Tate curve and its real form, not the same object.

---

## ITEM 2 — the June-2026 paper, [CC26] = arXiv:2606.06604

### The title — report's conclusion CONFIRMED, report's mechanism REFUTED

On-disk full text, first lines of
`sources-extracted/arxiv-2606.06604-absolute-geometry-specZ-fulltext.txt`:

```
On the Absolute Geometry of 

 Spec
 Z

and the Fargues-Fontaine curve
```

PDF title page (`curl -sL https://arxiv.org/pdf/2606.06604`, `pdftotext -f 1 -l 1`):

```
On the Absolute Geometry of Spec Z
and the Fargues-Fontaine curve
Alain Connes and Caterina Consani

arXiv:2606.06604v1 [math.AG] 4 Jun 2026
```

**arXiv abs page HTML** (`curl -sL https://arxiv.org/abs/2606.06604`), raw `<h1>`:

```html
<h1 class="title mathjax"><span class="descriptor">Title:</span>On the Absolute Geometry of
$\operatorname{Spec}\mathbf{Z}$</h1>
<div class="authors"><span class="descriptor">Authors:</span>...Alain Connes...Caterina Consani...
```

and the citation meta tag on the same page:

```html
<meta name="citation_title" content="On the Absolute Geometry of $\operatorname{Spec}\mathbf{Z}$" />
<meta name="citation_author" content="Connes, Alain" />
<meta name="citation_author" content="Consani, Caterina" />
<meta name="citation_date" content="2026/06/04" />
```

`grep -i fargues` on the abs page HTML returns only three hits, **all inside the abstract**
("...real analogue of the Fargues--Fontaine curve."), none in the title.

zbMATH 903065884: `On the Absolute Geometry of $\operatorname{Spec}\mathbf{Z}$ | 2026 |
Preprint, arXiv:2606.06604 [math.AG] (2026)` — same short form.

The arXiv-generated PDF **document metadata** (`pdfinfo`) also carries the short form:

```
Title:           On the Absolute Geometry of SpecZ
Author:          Alain Connes; Caterina Consani
Creator:         arXiv GenPDF (tex2pdf:a6404ea)
Pages:           30
```

**Verdict on the title: PARTIALLY_VERIFIED / CORRECTED.**

* **CONFIRMED:** the paper's own title, as typeset on its title page and as rendered in arXiv's
  HTML full text, **does** include "and the Fargues-Fontaine curve". The full title is
  *On the Absolute Geometry of Spec Z and the Fargues-Fontaine curve*.
* **REFUTED:** the prior session's stated mechanism — "the arXiv API truncates the title at the
  TeX macro, so use the abs page" — is wrong. The abs page is **not** the fix: the abs-page
  `<h1>`, the `citation_title` meta tag, the arXiv API, the PDF metadata, and zbMATH **all**
  carry the short form. The clause is missing from arXiv's *metadata record*, not merely from the
  API's rendering of it. The only sources that carry the full title are the typeset PDF title
  page and arXiv's HTML rendering of the LaTeX `\title{}`.
* Practical consequence for the citation pass: the earlier instruction "do not drop 'and the
  Fargues-Fontaine curve' from [CC26]" stands and should still be honored, but anyone who
  re-checks it against the abs page will find the short title and think the citation is wrong.
  Add a one-line note recording why.

Other fields (abs page): authors Alain Connes, Caterina Consani; `[v1] Thu, 4 Jun 2026 18:01:03 UTC
(30 KB)`; Comments: `30 pages`; **no journal-ref**; the only DOI is `10.48550/arXiv.2606.06604`.
zbMATH lists it as a preprint. **Verdict on these fields: CONFIRMED.**

Ready to paste:

    A. Connes and C. Consani, *On the absolute geometry of Spec Z and the Fargues-Fontaine curve*,
    arXiv:2606.06604 (2026).

(Note for the executing session: arXiv's own metadata title omits "and the Fargues-Fontaine
curve"; the full title is taken from the paper's title page and from arXiv's HTML full text.)

### Does it cite the Scaling Site papers for the per-prime elliptic-curve analogue?

Yes. From the on-disk full text, introduction (line 282) and again in section 5 (line 1627),
identical sentence both times:

> **In [CC3] we developed the characteristic 1 geometry of the periodic orbit $C_p$ as an
> analogue of an elliptic curve.**

Section 5 continuation:

> The identification of the absolute F_1-geometry as a universal receptacle for the closed points
> of the Fargues-Fontaine curve naturally leads to a functorial connection with the
> characteristic-1 (equivalently, idempotent) geometry of the scaling site S introduced in [CC3].

And in the introduction, before Theorem 4:

> The periodic orbit $C_p$ of the adelic geometry ([CC3, CC6]) then appears canonically as the
> quotient $E_p(\mathbf{R})/\langle \pm 1\rangle$, where the element $-1 \in W_\infty$
> geometrically exchanges the two connected components of the real locus.

Its bibliography resolves the key:

```
[CC3]  A. Connes and C. Consani, Geometry of the Scaling Site, Selecta Math. no. 3, (2017),
       1803-1850.
[CC6]  A. Connes and C. Consani, On the Jacobian of \overline{Spec Z}, arXiv:2602.15941 (2026).
```

**Verdict: CONFIRMED, with one refinement.** [CC26] cites the **Selecta** Scaling Site paper
(arXiv:1603.03191) for the per-prime elliptic-curve analogue. It does **not** cite the 2015
C. R. note / arXiv:1507.05818 at all — that paper is absent from its bibliography. So "cites the
Scaling Site papers" (plural) is loose; it cites one of them. Note also that [CC26]'s own entry
for [CC3] omits the volume number 23.

---

## ITEM 3 (MUST 7) — "The Riemann-Roch strategy: complex lift of the Scaling Site"

Report claimed: in "Advances in Noncommutative Geometry", Springer, 2019, 53-125; arXiv:1805.10501.

Crossref (`10.1007/978-3-030-29597-4_2`):

```
type = "book-chapter"
title = ["The Riemann-Roch strategy"]
subtitle = ["Complex lift of the Scaling Site"]
container-title = ["Advances in Noncommutative Geometry"]
page = "53-125"
published-print = {"date-parts": [[2019]]}
published-online = {"date-parts": [[2020, 1, 14]]}
publisher = "Springer International Publishing"
ISBN = ["9783030295967", "9783030295974"]
AUTH = [('Alain', 'Connes'), ('Caterina', 'Consani')]
```

zbMATH 7217272:

```
The Riemann-Roch strategy. Complex lift of the scaling site | 2019
SRC: Chamseddine, Ali (ed.) et al., Advances in noncommutative geometry. Based on the
noncommutative geometry conference, Shanghai, China, March 23 -- April 7, 2017. On the occasion
of Alain Connes' 70th Birthday. Cham: Springer. 53-125 (2019).
DOI: 10.1007/978-3-030-29597-4_2
```

arXiv:1805.10501 abs page: title "The Riemann-Roch strategy, Complex lift of the Scaling Site",
authors Connes and Consani, `[v1] Sat, 26 May 2018 15:53:59 UTC (736 KB)`, 67 pages, 6 figures,
no journal-ref. PDF title page (`pdftotext -f 1 -l 1`):

```
The Riemann-Roch strategy
Complex lift of the Scaling Site
arXiv:1805.10501v1 [math.NT] 26 May 2018
Alain Connes and Caterina Consani
```

**Verdict on the bibliographic fields: CONFIRMED**, with one caveat worth recording: CC's own
later bibliographies (e.g. arXiv:2401.08401 ref [7], arXiv:2501.06560 ref [CC5]) date this chapter
to **Springer (2020)**. Crossref and zbMATH both give **2019** for the print publication (2020 is
the online-first date). Use 2019; this is exactly trap (b) — do not launder CC's own bibliography.

Ready to paste:

    A. Connes and C. Consani, *The Riemann-Roch strategy: complex lift of the Scaling Site*, in
    Advances in Noncommutative Geometry (A. Chamseddine, C. Consani, N. Higson, M. Khalkhali,
    H. Moscovici and G. Yu, eds.), Springer, Cham, 2019, 53-125;
    doi:10.1007/978-3-030-29597-4_2; arXiv:1805.10501.

### CONTENT CLAIM: "moduli of triangular elliptic curves with the equivalence relation generated by isogenies"

**CONFIRMED.** It is the paper's stated main result, and it is developed in **Sections 6.4-6.6**,
with the isogeny material in **Section 6.5, "Commensurability and isogenies"**.

Abstract (PDF title page, verbatim):

> Our main result is the construction, at the adelic level, of a complex lift of the adele class
> space of the rationals. **We interpret this lift as a moduli space of elliptic curves endowed
> with a triangular structure. The equivalence relation yielding the noncommutative structure is
> generated by isogenies.** We describe the tight relation of this complex lift with the
> GL(2)-system.

Introduction (p. 4 of the arXiv PDF), verbatim:

> By using the geometric interpretation of Q-lattices up to scale in terms of elliptic curves
> endowed with pairs of elements of the Tate module, we provide in Sect. 6.4 the geometric
> interpretation of the points of C_Q in terms of elliptic curves endowed with a triangular
> structure (reflecting the parabolic structure of the Q-lattice) and modulo the equivalence
> relation generated by isogenies (Sect. 6.5). In Sect. 6.6 we prove that the natural complex
> structure of the moduli space of triangular elliptic curves is the same as the complex structure
> on C_Q defined in Sect. 5 using the right action of P(R).

The definitions themselves (p. 57, Section 6.4-6.5), verbatim:

> **Definition 6.3.** A triangular structure on an elliptic curve E is a pair (xi, eta) of elements
> of the Tate module T(E), such that xi != 0 and < xi^perp, eta > = Z.
> In the following, we shall abbreviate "elliptic curve with triangular structure" by "triangular
> elliptic curve".

> **6.5 Commensurability and isogenies.** We recall that an isogeny from an abelian variety A to
> another B is a surjective morphism with finite kernel. In this section we describe how a
> triangular structure behaves under isogenies. At the geometric level, the commensurability
> relation is obtained from the following notion of isogeny between triangular elliptic curves.
>
> **Definition 6.4.** An isogeny f : (E, xi, eta) -> (E', xi', eta') of triangular elliptic curves
> is an isogeny f : E -> E' such that T(f)(xi) = xi' and T(f)(eta) = eta'.

> The following result determines the equivalence relation generated by isogenies
>
> **Proposition 6.3.** Let (E; xi, eta) and (E'; xi', eta') be two triangular elliptic curves and
> (Lambda, phi) and (Lambda', phi') the associated parabolic Q-lattices. ... (ii) The parabolic
> Q-lattices (Lambda, phi) and (Lambda', phi') are commensurable if and only if there exist two
> isogenies f : (E, xi, eta) -> (E'', xi'', eta'') and f' : (E', xi', eta') -> (E'', xi'', eta'')
> to the same triangular elliptic curve.

Section 6.8 gives the classification:

> **6.8 Boundary cases.** Theorem 6.2 and Proposition 6.2 show that triangular elliptic curves are
> classified by the subspace Pi^0 := P^+(Z) \ {(rho, alpha) in P(Zhat) x P^+(R) | rho = [[u,v],[0,1]],
> u != 0} subset Pi^+.

Note for the seed no-go note: the equivalence relation here is generated by isogenies of
**triangular** elliptic curves (Definition 6.4), which is *not* the plain isogeny relation —
CC observe explicitly that multiplication by n fails the triangular condition unless n = +-1:

> For ordinary isogenies, one can use the dual isogeny to show that the existence of an isogeny
> E -> E' is a symmetric relation. ... In our set-up the multiplication by n gives xi' = n xi and
> eta' = n eta. This modification does not alter the orthogonal, i.e. one has xi'^perp = xi^perp.
> But one has < xi'^perp, eta' > = nZ, thus the triangular condition is not fulfilled unless
> n = +-1.

---

## ITEM 4 (MUST 8) — "Knots, Primes and the adele class space", arXiv:2401.08401

arXiv abs page:

```
Title: Knots, Primes and the adele class space
Authors: Alain Connes, Caterina Consani
Submission history: [v1] Tue, 16 Jan 2024 14:43:19 UTC (748 KB)
Comments: 9 pages
```

No journal-ref; only DOI on the page is `10.48550/arXiv.2401.08401`.
zbMATH 902401558: `Knots, Primes and the adele class space | 2024 | Preprint, arXiv:2401.08401
[math.NT] (2024)`. No Crossref journal record.

PDF title page (`pdftotext -f 1 -l 1`):

```
KNOTS, PRIMES AND THE ADELE CLASS SPACE
arXiv:2401.08401v1 [math.NT] 16 Jan 2024
Alain Connes and Caterina Consani
```

**Verdict on fields: CONFIRMED**, still a preprint as of 2026-08-27.

Ready to paste:

    A. Connes and C. Consani, *Knots, primes and the adele class space*, arXiv:2401.08401 (2024).

### CONTENT CLAIM: Gamma \ (Q_p x Q_q x R) with Gamma = {+- p^m q^n}

**CONFIRMED, verbatim.** The object is in the table of contents as **Section 3** and is defined in
the introduction (p. 3) and again at the head of Section 3 (p. 6).

Table of contents:

```
3. The semilocal space Gamma\(Qp x Qq x R). . . . . . . . . . . . .
4. The classifying space Gamma\(A_{Q,S} x EGamma) and its codimension 1 foliation. . . .
```

Introduction, verbatim:

> Given two primes p != q we consider the inverse image of the periodic orbit C_p in the semilocal
> adele class space (4) associated to the set of places S = {p, q, infinity}. **The semilocal adele
> class space is Gamma\(Q_p x Q_q x R) where Gamma := {+-p^m q^n | m, n in Z}.**
>
> **Theorem 1.2.** The inverse image of the periodic orbit C_p in the semilocal adele class space
> Gamma\(Q_p x Q_q x R) associated to S = {p, q, infinity} is the mapping torus of the canonical
> generator {Frob_p} acting by multiplication in the abelianized etale fundamental group
> pi_1^et(Spec Z[1/q])^ab of the complement of q in Spec Z.

Section 3 gives the general form and specializes:

> The group Gamma of invertible elements of O_{Q,S} is
> Gamma = GL_1(O_{Q,S}) = {+-p_1^{n_1} ... p_k^{n_k} : p_j in S \ {infinity}, n_j in Z}.   (5)
> ... We let p != q be two primes and S = {p, q, infinity}. The ring O_{Q,S} is Z[1/p, 1/q] and the
> abelianized etale fundamental group of its spectrum is pi_1^et(Spec O_{Q,S})^ab = Z*_p x Z*_q.

### Distinguishing point: knot/linking-number analogy, NOT a correspondence calculus

**CONFIRMED, on two independent grounds.**

(1) The paper frames the whole two-prime construction as the linking number of two knots:

> Our second result gives the geometry underlying the analogy with the linking number of two knots
> K, L subset S^3 in the three sphere. By definition, the linking number lk(K, L) is the monodromy
> obtained by lifting the first knot K in the maximal abelian cover (S^3 - L)^ab of the complement
> of the second knot L. ... In the analogy between knots and primes the role of the knots K, L is
> played by two distinct primes p, q, while the sphere is replaced by Spec Z and X_L := S^3 - L is
> replaced by Spec Z[1/q].

> Thus the periodic orbit C_p plays the role of the first knot, and the monodromy of its lift in
> the maximal abelian cover of the complement of q in Spec Z is the element p in Z*_q. In the
> analogy between knots and primes developed in [12, 15, 16], p in Z*_q plays the role of the
> linking number (5) of p with q.

(2) A negative check: `grep -n -i "correspondence" 2401.txt` on the full extracted text returns
**no hits at all**. Likewise `grep -i "isogen"` returns no hits. There is no correspondence
calculus, no intersection-of-correspondences, no isogeny relation anywhere in the paper. Its
downstream use is K-theory of the associated C*-algebras (Section 3) and the Baum-Connes map for
the codimension-one foliation of Gamma\(Q_p x Q_q x R x R^2) (Section 4).

---

## ITEM 5 (SHOULD 13) — M. Morishita, arXiv:2508.15971

arXiv abs page, verbatim:

```
Title: On a relation between Deninger's foliated dynamical systems and Connes-Consani's adelic spaces
Authors: Masanori Morishita
Submission history: From: Masanori Morishita [view email]
[v1] Thu, 21 Aug 2025 21:27:06 UTC (19 KB)
[v2] Sat, 30 Aug 2025 21:11:42 UTC (19 KB)
[v3] Thu, 4 Sep 2025 06:15:32 UTC (19 KB)
[v4] Fri, 19 Dec 2025 06:53:22 UTC (19 KB)
[v5] Wed, 21 Jan 2026 04:51:16 UTC (19 KB)
Comments: 26 pages. minor change (v2), corrected typos (v3), minor changes and corrected
misprints (v4); to appear in Munster Journal of Mathematics
```

Abstract, quoted verbatim from the abs page:

> We give a relation between Deninger's foliated dynamical systems associated to abelian number
> fields and Connes-Consani's adelic spaces. It fits with the analogy between knots and primes in
> arithmetic topology and lights up a geometric view of class field theory.

No journal-ref field on the abs page; only DOI is `10.48550/arXiv.2508.15971`.
Crossref search for a published version returns nothing matching.
zbMATH 902813104: `On a relation between Deninger's foliated dynamical systems and
Connes-Consani's adelic spaces | 2026 | Preprint, arXiv:2508.15971 [math.NT] (2026) |
AUTH: ['Masanori Morishita']`.

**Verdict: CONFIRMED**, with two notes the report did not carry:
* **Single author** (Masanori Morishita), not multiple.
* The report's date "August 2025" is the **v1** date and is correct, but the paper has been
  revised five times, most recently **21 January 2026**; zbMATH indexes it under **2026**.
  "to appear in Munster Journal of Mathematics" is an author-supplied arXiv comment, not an
  independently verified journal-ref; there is no Crossref record yet.

Ready to paste:

    M. Morishita, *On a relation between Deninger's foliated dynamical systems and
    Connes-Consani's adelic spaces*, arXiv:2508.15971 (2025); to appear in Munster J. Math.
    (announced by the author, not independently verified).

---

## ITEM 6 — what arXiv:2501.06560 (the note's [CC25]) actually is

arXiv abs page and PDF title page agree:

```
Knots, primes and class field theory
arXiv:2501.06560v1 [math.NT] 11 Jan 2025
Alain Connes and Caterina Consani
Comments: 30 pages
```

No journal-ref; only DOI `10.48550/arXiv.2501.06560`.

Abstract, verbatim from the abs page:

> In this paper, we present a geometric generalization of class field theory, demonstrating how
> adelic constructions, central to the spectral realization of zeros of L-functions and the
> geometric framework for explicit formulas in number theory, naturally extend the classical
> theory. This generalization transitions from the idele class group, which acts as the adelic
> analog of Galois groups, to a geometric framework associated with schemes and the ring of
> integers of global fields. This perspective provides a conceptual explanation for the role of
> the adele class space in the spectral realization of L-function zeros and identifies the idele
> class group as a generic point in this context. The sector X_Q of the adele class space
> corresponding to the Riemann zeta function gives the class field counterpart of the scaling
> topos. The main result is the construction of a functor mapping finite abelian extensions of Q
> to finite covers of X_Q, with the monodromy of periodic orbits of length log p under the scaling
> action corresponding to the Galois action of the Frobenius at the prime p.

**Does 2501.06560 originate the per-prime elliptic-curve analogue? NO.** It *recalls* it, and
cites the 2017 Selecta paper for it. From the introduction (p. 8), verbatim:

> The scaling topos serves as the topos viewpoint of the adelic space X_Q and, as shown in [CC4],
> its interpretation via an extension of scalars from the arithmetic site (see [CC3]) equips the
> scaling topos with a natural structure sheaf. The sections of this sheaf are piecewise affine,
> continuous, convex functions. A remarkable consequence of this additional structure is observed
> in the periodic orbits C_p: **each C_p, when equipped with the restriction of the scaling
> topos's structure sheaf, becomes an analogue of an elliptic curve within the framework of
> characteristic one.**

Its bibliography:

```
[CC4] A. Connes, C. Consani, Geometry of the Scaling Site. Selecta Math. (N.S.) 23 (2017),
      no. 3, 1803-1850.
[CC5] A. Connes, C. Consani, The Riemann-Roch strategy, complex lift of the Scaling Site,
      "Advances in Noncommutative Geometry, ...", Springer.
```

`grep -i "isogen"` on its full text: no hits. `grep -i "Tate"`: no hits. So it contains no isogeny
material and no Tate curve.

**Verdict: the note's lineage pointer is REFUTED.** arXiv:2501.06560 is not the origin of the
per-prime elliptic-curve analogue; it cites the 2017 Selecta paper for it, which in turn is the
long version of the July-2015 C. R. note. What 2501.06560 *does* contribute, and what the rewrite
should say it contributes, is the **geometric generalization of class field theory**: a functor
from finite abelian extensions of Q to finite covers of X_Q, under which the monodromy of the
periodic orbit of length log p corresponds to the Galois action of Frobenius at p.

Ready to paste:

    A. Connes and C. Consani, *Knots, primes and class field theory*, arXiv:2501.06560 (2025).

---

## SUMMARY OF CORRECTIONS THE EXECUTING SESSION MUST MAKE

1. **The note's "first appears ... in January 2025" is wrong.** The per-prime characteristic-one
   analogue of an elliptic curve is Connes-Consani, **21 July 2015** (arXiv:1507.05818v1 =
   C. R. Math. Acad. Sci. Paris 354 (2016), no. 1, 1-6), with the long version in Selecta Math.
   (N.S.) 23 (2017), no. 3, 1803-1850 (arXiv:1603.03191). The gap is 9 years 5.7 months.
2. **Do not say the 2015 object is C*/p^Z.** It is **C_p = R*_+ / p^Z**, a real circle of length
   log p with a characteristic-one structure sheaf, Jacobian Z/(p-1)Z, and a real-valued
   Riemann-Roch theorem. Connes and Consani themselves call it a "variant ... of the classical
   Jacobi description C*/q^Z" — i.e. an antecedent, explicitly modeled on C*/q^Z but not equal
   to it. The complex Tate curve E_p = C*/p^Z enters the CC program in **June 2026**
   (arXiv:2606.06604), where C_p is identified as the connected component of its real locus and
   E_p decomposes as C_p x X~_infty.
3. **Keep "and the Fargues-Fontaine curve" in the [CC26] title, but record why it looks wrong.**
   The clause is on the paper's title page and in arXiv's HTML full text, but is absent from
   arXiv's metadata record (abs-page `<h1>`, `citation_title` meta, API, PDF metadata, zbMATH).
   The earlier diagnosis "the API truncates it, the abs page has it" is incorrect and should be
   amended in whatever note carries it.
4. **Date the Riemann-Roch strategy chapter 2019, not 2020**, notwithstanding CC's own
   bibliographies, which say Springer (2020) — that is the online-first date.
5. **Morishita is a single author** and the paper has been revised through 21 January 2026;
   "to appear in Munster J. Math." is author-announced only.
6. **Replace, do not delete, the [CC25] pointer.** arXiv:2501.06560's actual contribution is the
   functor from finite abelian extensions of Q to finite covers of X_Q, with Frobenius monodromy
   on the length-log p periodic orbits.
