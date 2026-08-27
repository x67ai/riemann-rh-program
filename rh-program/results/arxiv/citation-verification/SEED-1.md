# CLUSTER SEED-1 — Winkelmann, Nagoya Math. J. 176 (2004)

Verification pass for the arXiv citation execution. Every field below was checked against a
primary source this session (2026-08-27). Where the agent report and a primary source disagree,
the primary source wins and the disagreement is flagged with **[DISAGREEMENT]**.

Working files (scratchpad, this session):
`.../scratchpad/wink/{abs.html, v3.pdf, v3.txt, v3p.txt, v1.pdf, v1.txt, cr.json, cr2.json, zb.json, doi.html}`

---

## 1. Bibliographic verification

### 1.1 Commands run

```
curl -sSL --max-time 40 -A "Mozilla/5.0 (research citation check)" \
  "https://arxiv.org/abs/math/0204195" -o abs.html          # 39217 bytes, OK

curl -sS --max-time 40 \
  "http://export.arxiv.org/api/query?search_query=all:math/0204195&max_results=5" \
  -o wink_api.xml                                            # EMPTY -- API does not serve this
                                                             # old-style id; abs page used instead

curl -sS --max-time 40 \
  "https://api.zbmath.org/v1/document/_search?search_string=Winkelmann%20elliptic%20curves%20Schanuel%20geodesic%20lengths&results_per_page=3" \
  -o zb.json                                                 # 1 hit, zbMATH id 2211522

curl -sS --max-time 40 "https://api.crossref.org/works/10.1017/S0027763000009016" -o cr.json
curl -sS --max-time 40 "https://api.crossref.org/works?query.bibliographic=Winkelmann+elliptic+curves+Schanuel+geodesic+lengths+Nagoya&rows=2" -o cr2.json

curl -sSL --max-time 45 -A "Mozilla/5.0 ... Chrome/120 ..." \
  "https://doi.org/10.1017/S0027763000009016" -o doi.html    # resolves to Cambridge Core; 780697 bytes
                                                             # (first attempt timed out; second succeeded)

curl -sSL --max-time 60 "https://arxiv.org/pdf/math/0204195v3" -o v3.pdf   # 247003 bytes, 20 pp.
curl -sSL --max-time 60 "https://arxiv.org/pdf/math/0204195v1" -o v1.pdf   # 17 pp.
pdftotext v3.pdf v3p.txt ; pdftotext v1.pdf v1.txt
```

Project Euclid was tried (`https://projecteuclid.org/journals/nagoya-mathematical-journal/volume-176/issue-none`)
and returned a 1159-byte stub — blocked. Not needed: the DOI resolves to **Cambridge University
Press**, which is the current host of Nagoya Math. J., and the publisher page carries full
`citation_*` metadata.

### 1.2 Raw evidence

**arXiv abs page** (`https://arxiv.org/abs/math/0204195`), parsed:

```
[Submitted on 15 Apr 2002 (v1), last revised 8 Apr 2003 (this version, v3)]
Title: On Elliptic Curves in SL_2(C)/Γ, Schanuel's conjecture and geodesic lengths
Authors: Joerg Winkelmann (Univ. of Nancy I, France)
Comments: 20 pages; LaTeX; lemma 2 corrected, some minor improvements in presentation
Subjects: Algebraic Geometry (math.AG); Differential Geometry (math.DG); Number Theory (math.NT)
MSC classes: 22E40; 32M10; 32J17; 53C22
Cite as: arXiv:math/0204195 [math.AG]
https://doi.org/10.48550/arXiv.math/0204195

Submission history
From: Joerg Winkelmann [view email]
[v1] Mon, 15 Apr 2002 13:46:34 UTC (13 KB)
[v2] Wed,  6 Nov 2002 10:06:23 UTC (13 KB)
[v3] Tue,  8 Apr 2003 14:43:05 UTC (15 KB)
```

There is **no `journal-ref` field on the arXiv abs page** — the arXiv record was never updated
with the Nagoya publication. So the journal data had to come from Crossref / zbMATH / the
publisher, and it does.

**zbMATH Open, id 2211522** (`zb.json`):

```json
"title": "On elliptic curves in \\(\\mathrm{SL}_2(\\mathbb C)/\\Gamma\\), Schanuel's conjecture and geodesic lengths"
"authors": ["Winkelmann, Jörg"]
"source": "Nagoya Math. J. 176, 159-180 (2004)."
"series": {"short_title":"Nagoya Math. J.", "title":"Nagoya Mathematical Journal",
           "volume":"176", "year":"2004", "issue": null,
           "issn":[{"number":"0027-7630","type":"print"},{"number":"2152-6842","type":"electronic"}],
           "publisher":"Cambridge University Press, Cambridge"}
"pages": "159-180"
"links": [{"type":"doi","identifier":"10.1017/S0027763000009016"},
          {"type":"arxiv","identifier":"math/0204195"}]
```

**Crossref** (`cr.json`, DOI lookup):

```
DOI = "10.1017/s0027763000009016"
type = "journal-article"
title = ["On Elliptic Curves in SL<sub>2</sub>(ℂ)/Γ.., Schanuel’s Conjecture and Geodesic Lengths"]
container-title = ["Nagoya Mathematical Journal"]
volume = "176"   issue = null   page = "159-180"
published-print = {"date-parts": [[2004]]}
author = [{"given":"Jörg","family":"Winkelmann","sequence":"first"}]
publisher = "Cambridge University Press (CUP)"
ISSN = ["0027-7630","2152-6842"]
```

**Publisher page** (DOI resolution -> Cambridge Core), `<meta>` tags:

```
citation_journal_title  = Nagoya Mathematical Journal
citation_publisher      = Cambridge University Press
citation_title          = On Elliptic Curves in SL2(ℂ)/Γ.., Schanuel’s Conjecture and Geodesic Lengths
citation_author         = Jörg Winkelmann
citation_publication_date = 2004/01
citation_online_date    = 2016/01/22
citation_volume         = 176
citation_firstpage      = 159
citation_lastpage       = 180
citation_doi            = 10.1017/S0027763000009016
citation_issn           = 0027-7630 / 2152-6842
citation_keywords       = 22E40; 32M10; 32J17; 53C22
```

**The PDF's own first page** (`pdftotext v3.pdf`, page 1):

```
arXiv:math/0204195v3 [math.AG] 8 Apr 2003

ON ELLIPTIC CURVES IN SL2 (C)/Γ, SCHANUEL’S
CONJECTURE AND GEODESIC LENGTHS
JÖRG WINKELMANN
```

and page 20 (the address block):

```
Jörg Winkelmann, Institut Elie Cartan (Mathématiques), Université Henri
Poincaré Nancy 1, B.P. 239,, F-54506 Vandœuvre-les-Nancy Cedex,, France
E-mail address: jwinkel@member.ams.org
```

### 1.3 Verdicts, field by field

| Field | Report claimed | Primary source says | Verdict |
|---|---|---|---|
| Author | J. Winkelmann | **Jörg Winkelmann** (PDF title block, PDF address block, Crossref `given:"Jörg"`, zbMATH `Winkelmann, Jörg`, Cambridge `citation_author`) | CONFIRMED, spelled with o-umlaut. arXiv's metadata field ASCII-izes it to "Joerg"; **he prints it "Jörg"** — use the umlaut. |
| Title | "On elliptic curves in SL_2(C)/Gamma, Schanuel's conjecture and geodesic lengths" | Same, modulo case. arXiv abs page: "On Elliptic Curves in SL_2(C)/Γ, Schanuel's conjecture and geodesic lengths". zbMATH: all-lowercase-after-first. PDF runs it in small caps. | CONFIRMED. See the ".." trap below. |
| Journal | Nagoya Math. J. | Nagoya Mathematical Journal (zbMATH short title "Nagoya Math. J.") | CONFIRMED |
| Volume | 176 | 176 (all three) | CONFIRMED |
| Issue | (none claimed) | `issue: null` in Crossref and zbMATH — the volume is unnumbered by issue | CONFIRMED (omit issue) |
| Year | 2004 | 2004 (Crossref `published-print`, Cambridge `2004/01`, zbMATH) | CONFIRMED |
| Pages | 159-180 | 159-180 (Crossref, zbMATH, Cambridge firstpage/lastpage) | CONFIRMED |
| DOI | "if any" | **10.1017/S0027763000009016** | CONFIRMED (Cambridge, not Project Euclid) |
| arXiv id | math/0204195 | math/0204195 [math.AG] | CONFIRMED |
| Versions | v1 15 Apr 2002, v3 8 Apr 2003 | v1 Mon 15 Apr 2002 13:46:34 UTC; **v2 Wed 6 Nov 2002 10:06:23 UTC**; v3 Tue 8 Apr 2003 14:43:05 UTC | CONFIRMED, and there is a **v2** the report did not mention (Nov 2002). Not a defect, but the version list is v1/v2/v3. |

**TITLE TRAP — do not copy Crossref or Cambridge verbatim.** Both Crossref and the Cambridge Core
page render the title as `... SL2(ℂ)/Γ.., Schanuel's Conjecture ...` — with a spurious `..`
after the Gamma. That is a publisher-side typesetting artifact in their metadata (almost certainly
a mangled `$\Gamma$` macro), not part of the title. zbMATH and the paper's own title page have no
such dots. **Use the arXiv/zbMATH/PDF form.** This is the same class of trap as (a) in the brief,
running the other way: here the *publisher* metadata is corrupt and arXiv is clean.

### 1.4 READY-TO-PASTE CITATION (house style)

```
J. Winkelmann, *On elliptic curves in SL_2(C)/Gamma, Schanuel's conjecture and geodesic
lengths*, Nagoya Math. J. **176** (2004), 159-180; doi:10.1017/S0027763000009016;
arXiv:math/0204195 (v1 15 Apr 2002, v3 8 Apr 2003).
```

With the umlaut and the TeX the paper actually uses:

```
J. Winkelmann, *On elliptic curves in $\mathrm{SL}_2(\mathbb{C})/\Gamma$, Schanuel's
conjecture and geodesic lengths*, Nagoya Math.\ J.\ \textbf{176} (2004), 159--180;
doi:10.1017/S0027763000009016; arXiv:math/0204195 (v1 15 Apr 2002, v3 8 Apr 2003).
```

If the note wants the author's full given name: `J\"org Winkelmann`.

For the priority sentence, cite the preprint date explicitly, because the journal year (2004) is
two years later than the date that matters:

```
arXiv:math/0204195v1, 15 April 2002; published as Nagoya Math. J. 176 (2004), 159-180.
```

---

## 2. Content verification — the quote set

All quotes below are from `pdftotext` of **arXiv:math/0204195v3** (20 pp.). Page numbers are the
paper's own printed page numbers, which for v3 coincide with the PDF page index. Where v1 differs,
that is recorded in section 5. Unicode has been kept as `pdftotext` produced it; `⟨ ⟩` is written
for the source's angle brackets.

### 2(a) The setup — E_lambda = C*/lambda^Z = C/<2 pi i, log lambda>

**[PARTIAL DISAGREEMENT — the report compresses three separate statements into one hypothesis.]**
Winkelmann never writes a single displayed definition "E_lambda = C*/lambda^Z = C/⟨2 pi i, log
lambda⟩ for real algebraic lambda > 1". The three ingredients occur in three places:

*(i) The construction, p. 2 (§1, Introduction):*

> "If γ ∈ Γ is a semisimple element of infinite order, then the centralizer C = {g ∈ SL2 (C) :
> gγ = γg} is isomorphic to C∗ as a complex Lie group and C ∩ Γ is a discrete subgroup
> containing γ and therefore commensurable with {γ^k : k ∈ Z}. The quotient of C∗ by an infinite
> discrete subgroup is necessarily compact. Hence for every semisimple element γ ∈ Γ of infinite
> order we obtain an elliptic curve E ⊂ X = SL2 (C)/Γ which arises as orbit of the centralizer C.
> Moreover, this elliptic curve E ≃ C/(C ∩ Γ) is isogenous to C/⟨γ⟩ and therefore isogenous to
> C∗/⟨λ⟩ where λ and λ^{-1} are the eigenvalues of the matrix γ ∈ SL2 (C)."

*(ii) The `C*/alpha^Z` normal form and the algebraicity + |alpha|>1 hypothesis, p. 13 (§3.2,
Conjecture 1):*

> "Let α1 , α2 ∈ C be algebraic numbers with |αi | > 1. Let Ei be the quotient manifold
> C∗/{αi^k : k ∈ Z}."

*(iii) The lattice presentation and the "real, larger than 1" hypothesis, p. 16 (proof of thm. 2):*

> "let λi , λj and λk be pairwise multiplicatively independent real numbers larger than 1 such
> that the three elliptic curves Ei , Ej and Ek are all isogenous. Note that Ei = C/⟨2πi, log λi⟩
> and similarily for Ej and Ek ."

Also p. 13, immediately after Conjecture 1, the exponential dictionary:

> "Note that C/⟨1, τ⟩ ≃ C∗/⟨e^{2πiτ}⟩ for τ ∈ H+."

**Verdict: CONFIRMED in substance, with the caveat that "real algebraic λ > 1" is a composite of
Conjecture 1's "algebraic, |α| > 1" and Theorem 2's proof's "real, larger than 1"**, and that in
Theorem 2 algebraicity is not assumed — it is *derived* elsewhere (p. 15, Prop. 4: "Γ is conjugate
to a subgroup of SL2 (k) for some number field k (see [5], Thm. 7.67), hence all the numbers λi
are algebraic numbers"). A rewrite that attributes to Winkelmann the exact phrase "real algebraic
λ > 1 as a standing hypothesis" would be overstating; attribute the ingredients as above.

### 2(b) Lemma 7 — the isogeny / Q-linear-relation lemma

p. 13 (§3.1, Isogeny criteria). Verbatim:

> **Lemma 7.** Let Λ, Γ be lattices in C, and Λ_Q = Λ ⊗ Q, Γ_Q = Γ ⊗ Q. Consider the natural map
> Φ : Λ_Q ⊗_Q Γ_Q → C induced by the inclusion maps Γ ↪ C, Λ ↪ C.
> Then C/Λ and C/Γ are isogenous **iff** dim_Q ker Φ > 0.
>
> *Proof.* We may assume Γ = ⟨1, τ⟩_Z , Λ = ⟨1, σ⟩_Z . The kernel ker Φ is positive-dimensional
> iff there is a linear relation
>
>     a + bτ + cσ + dτσ = 0
>
> with (a, b, c, d) ∈ Q^4 \ {(0,0,0,0)}. Using σ, τ ∈ H+, one verifies that
> −(a b ; c d) ∈ GL_2^+(Q). Thus σ = −(a + bτ)/(c + dτ) = −(a b ; c d)(τ), i.e. dim ker Φ > 0
> iff τ and σ are contained in the same GL_2^+(Q)-orbit.  □

**Verdict: CONFIRMED.** Note carefully — **Lemma 7 is itself stated as an "iff"**. This matters
for item 3 below.

The companion lemma, also p. 13, which the note may want:

> **Lemma 8.** For a lattice ⟨α, β⟩_Z = Λ ⊂ C let K_Λ denote the subfield of C given by
> K_Λ = Q(α/β). Then K_Λ depends only on Λ and not of the choice of the basis (α, β). Let Λ and
> Λ̃ be lattices in C. If trdeg K_Λ/Q > 0, then C/Λ and C/Λ̃ are isogenous elliptic curves if and
> only if K_Λ = K_Λ̃ .

### 2(c) Theorems 1, 2 and 3, in full

**Theorem 1** — p. 3 (§2.1):

> **Theorem 1.** Let Γ be a subgroup of SL2 (C) which is dense in the algebraic Zariski topology.
> Then there exists infinitely many pairwise multiplicatively independent complex numbers λ which
> occur as eigenvalues for elements of Γ.

with the definition it depends on, same page:

> **Definition.** Two non-zero elements x, y in a field k are called *multiplicatively dependent*
> if there exists a pair (p, q) ∈ Z × Z \ {(0, 0)} such that x^q = y^p. They are called
> *multiplicatively independent* if they are not multiplicatively dependent.

**Theorem 2** — p. 16 (§4.1, "The case where Γ ∩ SL2 (R) is Zariski dense"):

> **Theorem 2.** Let Γ be a discrete subgroup of SL2 (C) and assume that Γ ∩ SL2 (R) is
> Zariski-dense in SL2 .
> Then there exists infinitely many isogeny classes of elliptic curves embedded in
> X = SL2 (C)/Γ.

**[DISAGREEMENT with the way the cluster brief describes it.]** The brief and the abstract speak
of the case "Γ ∩ SL_2(R) **cocompact** in SL_2(R)". The theorem as stated assumes only
**Zariski-dense**, which is weaker. Cocompactness enters only in §5 (Prop. 5, Cor. 3), where he
constructs a Γ for which the intersection is cocompact. Quote the theorem as *Zariski-dense*.

**Theorem 3** — p. 19 (§6):

> **Theorem 3.** Let M be a compact real hyperbolic manifold of dimension two or three and Λ its
> geodesic length spectrum.
> Then Λ contains infinitely many pairwise Q-linearly independent elements.

Adjacent, p. 19, and worth having:

> **Proposition 6.** Assume that M is a compact real hyperbolic 3-manifold. Then there exist
> infinitely many closed geodesics on M such that their complex lengths are pairwise Q-linearly
> independent.
>
> **Corollary 4.** Let Γ be a Zariski-dense subgroup in SL2 (C). Then there exist two elements
> γ1 , γ2 ∈ Γ with respective eigenvalues λ1 , λ2 ∈ R such that the numbers | log λ1 |, | log λ2 |
> generate a dense subgroup of the additive group (R, +).

### 2(d) THE KEY PASSAGE — proof of Theorem 2, p. 16, quoted whole

This is the passage that anticipates Theorems 1-3 of `results/c3-r/seed-no-go-note.md`. Verbatim,
arXiv:math/0204195v3, **page 16**, from the start of the proof to its end:

> *Proof.* By thm. 1 there are infinitely many pairwise multiplicatively independent complex
> numbers λi occuring as eigenvalues for elements γ ∈ Γ ∩ SL2 (R). None of these λi is a root of
> unity.
>
> If λ is an eigenvalue for a matrix SL2 (R), then either λ is real or |λ| = 1. If λ is an
> eigenvalue for an element of a discrete subgroup of SL2 (R) with |λ| = 1, then λ must be a root
> of unity.
>
> Since none of the λi is a root of unity, it follows that all the numbers λi are real.
>
> Thus there are infinitely many elliptic curves Ei in X = SL2 (C)/Γ which are isogenous to
> C∗/⟨λi⟩ where the numbers λi are all real and pairwise multiplicatively independent.
>
> We claim that at most two of these Ei can be isogenous. Assume the converse, i.e., let λi , λj
> and λk be pairwise multiplicatively independent real numbers larger than 1 such that the three
> elliptic curves Ei , Ej and Ek are all isogenous.
>
> **Note that Ei = C/⟨2πi, log λi⟩ and similarily for Ej and Ek . Isogeny of Ei and Ej implies
> that there is a Q-linear relation between 4π², log λi log λj , 2πi log λi and 2πi log λj (see
> lemma 7). Now 4π² ∈ R and log λi log λj ∈ R, while 2πi log λi and 2πi log λj are Q-linearly
> independent elements of iR. Therefore a Q-linear relation can only exists if**
>
> **4π²/(log λi log λj ) ∈ Q.**
>
> **Similarily the existence of an isogeny of between Ej and Ek implies**
>
> **4π²/(log λj log λk ) ∈ Q.**
>
> **Combined, this yields (log λi log λj )/(log λj log λk ) = log λi / log λk ∈ Q which
> contradicts the assumption of λi and λk being multiplicatively independent.**
>
> This proves the claim.
>
> **Thus we obtain an infinite family of elliptic curves in SL2 (C)/Γ such that for each of these
> curves there is at most one other curve in this family to which it is isogenous.** It follows
> that there are infinitely many isogeny classes.  □

(Bold added here only to mark the load-bearing sentences; there is no emphasis in the original.
"Similarily", "of between", "can only exists", "occuring" are Winkelmann's own spellings — quote
them as-is or mark with [sic].)

**Verdict: CONFIRMED, both target strings verbatim.** Both
`4π²/(log λi log λj) ∈ Q` and `for each of these curves there is at most one other curve in this
family to which it is isogenous` appear exactly as the report says, on **page 16 of v3**.
See §5 for the v1 wording of the second string, which differs.

### 2(e) Conjecture 1 — full statement, and does it imply the (T1) non-coincidence?

p. 13 (§3.2, Conjectures). Verbatim:

> **Conjecture 1.** Let α1 , α2 ∈ C be algebraic numbers with |αi | > 1. Let Ei be the quotient
> manifold C∗/{αi^k : k ∈ Z}.
> Then E1 and E2 are isogenous **if and only if** α1 , α2 are multiplicatively dependent (in the
> sense of def. 2.1).

And the equivalent reformulation he gives, p. 14:

> **Conjecture 2.** Let B+(Q) = {(a b ; 0 a^{-1}) : a ∈ Q+ , b ∈ Q} and let σ, τ ∈ H+ be
> contained in the same GL_2^+(Q)-orbit. Assume that both e^{2πiσ} and e^{2πiτ} are algebraic.
> Then σ and τ are already contained in the same B+(Q)-orbit.

**The check the brief asked for.** The report calls Conjecture 1 "the note's (T1)-refuting
statement", i.e. the statement whose truth would rule out `log p log q ∈ 4π² Q`.
**That is CORRECT, but only via Lemma 7, and the deduction should be spelled out rather than
attributed to Winkelmann as a stated result.** Precisely:

- Apply Conjecture 1 with α1 = p, α2 = q, distinct rational primes. Both are algebraic with
  |α| > 1, so the hypotheses hold. p and q are multiplicatively independent (p^b = q^a forces
  a = b = 0 by unique factorization). Hence Conjecture 1 gives: **E_p and E_q are not isogenous.**
- Now run Lemma 7 in the *converse* direction. With τ_i = log λi/(2πi) one has
  τ_i τ_j = −(log λi log λj)/(4π²). If 4π²/(log p log q) = r ∈ Q^× then τ_p τ_q = −1/r ∈ Q, so
  (a, b, c, d) = (1/r, 0, 0, 1) is a nonzero rational quadruple with a + bτ + cσ + dτσ = 0, so
  dim_Q ker Φ > 0, so by Lemma 7 E_p and E_q **would be** isogenous.
- Contrapositive: Conjecture 1 ⟹ E_p not isogenous to E_q ⟹ 4π²/(log p log q) ∉ Q, i.e.
  log p · log q ∉ 4π² Q. That is exactly (T1).

**So: yes, Conjecture 1 implies the (T1) non-coincidence — but Winkelmann never writes (T1), never
writes the 4π² criterion in the direction needed, and never mentions primes.** The bridge is one
line off his own Lemma 7's "iff". A rewrite may say "Winkelmann's Conjecture 1 implies (T1)" only
if it also says how — the implication is not in his text.

### 2(f) The Schanuel argument — **[DISAGREEMENT: there is no §7]**

**The paper has SIX sections, not seven.** Verified by grepping the section headers out of the
extracted text:

```
$ grep -n "^[0-9]\+\. " v3.txt
13:1. Introduction
86:2. Multiplicatively independent eigenvalues
659:3. Equivalence of elliptic curves
789:4. Elliptic Curves in SL2 (C)/Γ
876:5. Existence of Γ for which Γ ∩ SL2 (R) is cocompact in SL2 (R)
936:6. Geodesic length spectra for hyperbolic manifolds
```

**The Schanuel argument is Proposition 3 in §3.2, page 14.** Any citation of the form
"Winkelmann §7" is wrong and must be corrected to **§3.2, Prop. 3 (p. 14)**.

Verbatim, p. 14:

> **Proposition 3.** Conjecture 1 holds, if Schanuels conjecture is true.
>
> Schanuels Conjecture is the far-reaching conjecture from transcendental number theory which
> encompasses many important conjecture in this area. It states the following:
>
> **Schanuel's Conjecture.** If x1 , . . . , xn are Q-linearly independent complex numbers, then
> the transcendence degree of Q(x1 , . . . , xn , e^{x1} , . . . , e^{xn}) over Q is at least n.
>
> Now we prove the proposition.
>
> *Proof.* Indeed, let x1 = 2πi, x2 = log α1 , x3 = log α2 . Schanuels conjecture then implies
> that either
> (1) dim_Q ⟨2πi, log α1 , log α2⟩ ≤ 2, or
> (2) 2πi, log α1 , log α2 are all three algebraically independent.
> Since ℜ log αi = log |αi | > 0 (recall that we assumed |αi | > 1) for i = 1, 2, in the first
> case there exist integers n, m ∈ Z \ {0} such that α1^n = α2^m , i.e. α1 and α2 are
> multiplicatively dependent.
> In the second case we can conclude that log α1/2πi and log α2/2πi are both transcendental and
> Q(log α1/2πi) ≠ Q(log α2/2πi). Hence C∗/⟨α1⟩ is not isogenous to C∗/⟨α2⟩ in this case.
> Thus we have shown that either α1 and α2 are multiplicatively dependent, or C∗/⟨α1⟩ must be
> isogenous to C∗/⟨α2⟩.  □
>
> **Remark.** Actually we do not use Schanuels conjecture in its full strength, but only a
> special case of it. However, even the special statement we need is not yet proven.

Two things to flag for anyone pasting from this:
1. **The last sentence of the proof contains a typo in the published/v3 text**: "or C∗/⟨α1⟩ must
   be isogenous to C∗/⟨α2⟩" should read "must **not** be isogenous", as the body of the proof and
   the Remark make plain. v1's version of the proof (see §5) does not carry that sentence and is
   therefore cleaner. If quoting, quote the two numbered cases and stop, or add [sic].
2. He writes "Schanuels" without the apostrophe in the running text but "Schanuel's Conjecture"
   in the displayed statement. Both are his.

The Schanuel chain's consequences, p. 15-16:

> **Proposition 4.** If conjecture 1 holds, then for every discrete cocompact subgroup
> Γ ⊂ SL2 (C) there exist infinitely many isogeny classes of elliptic curves embedded in
> X = SL2 (C)/Γ.
>
> **Corollary 2.** If Schanuel's conjecture holds, then for every discrete cocompact subgroup
> Γ ⊂ SL2 (C) there exists infinitely many isogeny classes of elliptic curves embedded in
> X = SL2 (C)/Γ.

---

## 3. CRITICAL FOR THE REWRITE — what he does and does not give

This is the item that decides whether the seed note's claim of added value is exactly right.

### 3.1 Does he state the criterion in "iff" form?

**NO — not for the 4π² criterion.** In the proof of Theorem 2 he states and uses **one direction
only**:

> "Isogeny of Ei and Ej implies that there is a Q-linear relation between 4π², log λi log λj,
> 2πi log λi and 2πi log λj (see lemma 7). ... Therefore a Q-linear relation can only exists if
> 4π²/(log λi log λj ) ∈ Q."

That is `Hom(E_i, E_j) ≠ 0  ⟹  4π²/(log λi log λj) ∈ Q`. He never writes the converse, and never
states an equivalence in these terms anywhere in the paper.

**BUT** — and the rewrite must not miss this — **his Lemma 7 *is* an equivalence**
("C/Λ and C/Γ are isogenous **iff** dim_Q ker Φ > 0"), and the converse of the 4π² statement is a
one-line consequence of it, by the same real/imaginary bookkeeping he already performs: if
4π²/(log λi log λj) = r ∈ Q^× then (a, b, c, d) = (1/r, 0, 0, 1) is a nonzero rational relation
a + bτ_i + cτ_j + dτ_iτ_j = 0 with τ_i = log λi/(2πi), hence dim_Q ker Φ > 0, hence isogenous.

**Practical wording for the note.** Do **not** write "Winkelmann proves the equivalence". Do
**not** write "Winkelmann proves only one direction and the converse is new" either — the converse
is immediate from his own Lemma 7 and cannot be claimed as an addition. The accurate wording is:

> Winkelmann [W, proof of Thm. 2, p. 16] derives the necessity of
> 4π²/(log λ_i log λ_j) ∈ Q for isogeny of C*/λ_i^Z and C*/λ_j^Z with λ real; the sufficiency is
> immediate from his Lemma 7, which is stated as an equivalence, though he does not remark on it.

### 3.2 Does he compute the rank of Hom, or the isogeny degree?

**NO. Neither. Verified by exhaustive grep of the full extracted text of v3:**

```
$ grep -n "Hom" v3p.txt          # (no matches)
$ grep -ni "rank" v3p.txt        # (no matches)
$ grep -ni "isogeny degree\|degree of the isogeny\|degree of isogeny" v3p.txt   # (no matches)
```

The word "Hom" does not occur in the paper. The word "rank" does not occur. Every occurrence of
"degree" in the paper is a **field extension degree** (`deg K(λ)/K ≤ 2`, `deg(L(w)/L) ≤ 2`,
Dirichlet's unit theorem, `d0 = deg(L0/Q)`) or the transcendence degree in Schanuel's statement —
none is the degree of an isogeny.

The closest he comes to a quantitative statement is `dim_Q ker Φ > 0` in Lemma 7, which is a
*positivity* assertion, not a computation. He never evaluates dim_Q ker Φ, never identifies
Hom(E_i, E_j) as a group, and never produces a minimal isogeny.

**So the seed note's claim to "sharpen his result to the exact Hom group and isogeny degree" is
defensible — narrowly.** Calibrate it as follows so it is exactly right and not overstated:

- **NOT new:** the statement of Theorems 1-3 of the note; the criterion
  `Hom ≠ 0 ⟹ 4π²/(log λ_i log λ_j) ∈ Q`; the real/imaginary separation that proves it; the
  division of two such relations to force `log λ_i/log λ_k ∈ Q`; the three-curve run; the
  "at most one other curve in this family" conclusion. **All of this is Winkelmann 2002.**
- **NOT new, though he does not say it:** the converse direction, hence the full equivalence.
  It is one line from his Lemma 7 and must be attributed to him, not claimed.
- **Genuinely not in Winkelmann:** the identification of the group Hom(E_i, E_j) itself and its
  rank; the degree of the minimal isogeny; the specialization λ = p to primes and the
  reformulation of the whole thing as a statement about `log p log q`.
- The honest framing is therefore *"we make explicit, in the prime-indexed case, the Hom group
  and isogeny degree behind a criterion due to Winkelmann"* — an explication, not a sharpening of
  a theorem. A claim of priority over Theorems 1-3 is not available.

---

## 4. Does he ever take lambda = a prime, or index the family by primes?

**NO.** Verified exhaustively:

```
$ grep -ni "prime" v3p.txt
899:F3 = Q[i, √2] and p = 5. We observe that the prime ideal (5) splits in
900:F2 : 5 = (2 + i)(2 − i). Now (2 + i) is prime in Z[i] and both residue
903:consequence the prime ideals (5) and (2 + i) (and similarily for (2 − i))
```

Three hits, **all three in §5 (p. 17), all three about prime ideals in the arithmetic construction
of Γ**, none about eigenvalues or elliptic-curve parameters. The full context, p. 17:

> "Let F1 = Q[√2], F2 = Q[i], F3 = Q[i, √2] and p = 5. We observe that the prime ideal (5) splits
> in F2 : 5 = (2 + i)(2 − i). ... It follows that 5 is not contained in the image of the norm for
> either the field extension Q[i, √2]/Q[i] or the field extension Q[√2]/Q.
> Thus we may use the above construction with (K, L, λ) = (Q[i], Q[i, √2], 5) resp.
> = (Q, Q[√2], 5) ..."

**NOTATION TRAP, and it is a real one for anyone skimming the paper.** In §5 Winkelmann reuses the
letter **λ** for the norm-form parameter of a quaternion algebra (`t² = λ`, `λ ∉ N_{L/K}(L*)`),
and sets it to `5`. That is **not** the λ of §§2-4 (an eigenvalue of an element of Γ / a parameter
of an elliptic curve). Reading `(K, L, λ) = (Q[i], Q[i,√2], 5)` as "he takes λ = the prime 5" would
be a misreading. He does not. Nowhere in the paper is a prime used as an eigenvalue or as the
`C*/λ^Z` parameter, and nowhere is the family of curves indexed by primes.

**Consequence for the note's framing:** the prime-indexed presentation *is* the note's own, and it
is exactly why the program's earlier prior-art sweeps missed Winkelmann (his phrasing is
"eigenvalue" and "geodesic length", not "prime"). That is worth saying in the dated priority note —
it explains the miss without excusing it.

---

## 5. v1 vs v3 — the 2002 priority date

**The Theorem 2 argument is present in v1 (15 April 2002), essentially verbatim.** Retrieved
`https://arxiv.org/pdf/math/0204195v1` (17 pp.); the passage is on **v1 pages 12-13**.

**Theorem 2, v1 p. 12** — identical statement:

> **Theorem 2.** Let Γ be a discrete subgroup of SL2 (C) and assume that Γ ∩ SL2 (R) is
> Zariski-dense in SL2 .
> Then there exists infinitely many isogeny classes of elliptic curves embedded in
> X = SL2 (C)/Γ.

**Proof, v1 pp. 12-13** — verbatim, with the two divergences from v3 marked:

> *Proof.* By thm. 1 there are infinitely many pairwise multiplicatively independent complex
> numbers of absolute value different from one occuring as eigenvalues for elements
> γ ∈ Γ ∩ SL2 (R).
>
> A complex number λ with |λ| ≠ 1 which occurs as an eigenvalue for a matrix γ ∈ SL2 (R) is
> necessarily real.
>
> Thus there are infinitely many elliptic curves Ei in X = SL2 (C)/Γ which are isogenous to
> C∗/⟨λi⟩ where the numbers λi are all real and pairwise multiplicatively independent.
>
> We claim that at most two of these Ei can be isogenous. Assume the converse, i.e., let λi , λj
> and λk be pairwise multiplicatively independent real numbers larger than 1 such that the three
> elliptic curves Ei , Ej and Ek are all isogenous.
>
> **Note that Ei = C/⟨2πi, log λi⟩ and similarily for Ej and Ek . Isogeny of Ei and Ej implies
> that there is a Q-linear relation between 4π², log λi log λj , 2πi log λi and 2πi log λj (see
> lemma 4). Now 4π² ∈ R and log λi log λj ∈ R, while 2πi log λi and 2πi log λj are Q-linearly
> independent elements of iR. Therefore a Q-linear relation can only exists if
> 4π²/(log λi log λj ) ∈ Q.**
>
> **Similarily isogeny of Ej and Ek implies 4π²/(log λj log λk ) ∈ Q.**
>
> **Combined, this yields (log λi log λj )/(log λj log λk ) = log λi / log λk ∈ Q which
> contradicts the assumption of λi and λk being multiplicatively independent.**
>
> This proves the claim. **Thus we obtain infinitely many elliptic curves among which at most two
> can be isogenous.** It follows that there are infinitely many isogeny classes.  □

### Divergences v1 -> v3, and what they mean for quoting

1. **Lemma numbering.** The isogeny lemma is **lemma 4 in v1** and **lemma 7 in v3** (v3 inserted
   lemmas in §2.3; the abs page's comment "lemma 2 corrected" refers to §2.3's Lemma 2). Verified:
   `grep -n "Lemma 4" v1.txt` -> v1 line 498, statement identical word-for-word to v3's Lemma 7
   ("Let Λ, Γ be lattices in C ... Then C/Λ and C/Γ are isogenous iff dim_Q ker Φ > 0.").
   **A citation of "Lemma 7" is a v3/published citation. Cite "lemma 4 (v1) = lemma 7 (v3)" if the
   sentence is about the 2002 priority.**
2. **The conclusion sentence differs.** v1 ends "Thus we obtain infinitely many elliptic curves
   among which at most two can be isogenous." v3 ends "Thus we obtain an infinite family of
   elliptic curves in SL2 (C)/Γ such that for each of these curves there is at most one other
   curve in this family to which it is isogenous."
   **So the exact string the report quotes — "for each of these curves there is at most one other
   curve in this family to which it is isogenous" — is v3 (8 Apr 2003) wording, NOT v1.** The
   mathematical content is the same and is in v1; the sentence is not. If the note quotes that
   sentence it must cite v3 / the published paper, not v1. If it needs a 2002-dated quote, use
   "at most two can be isogenous" from v1, or quote the 4π² sentences, which *are* verbatim in v1.
3. **Theorem 1 is slightly weaker in v1**, carrying an extra clause: v1 reads "infinitely many
   pairwise multiplicatively independent complex numbers λ **with |λ| ≠ 1** which occur as
   eigenvalues"; v3 drops the `|λ| ≠ 1`. Theorem 3 is **word-for-word identical** in v1 (v1 p. 16)
   and v3 (p. 19).
4. **The Conjecture is unnumbered in v1** (both conjectures are simply "Conjecture"; v1 refers to
   the first as "conj. 3.2" by subsection). Its text is word-for-word the v3 Conjecture 1
   ("Let α1 , α2 ∈ C be algebraic numbers with |αi| > 1 ... if and only if α1 , α2 are
   multiplicatively dependent"), on v1 p. 10. The Schanuel proposition is **Proposition 2 in v1**
   (= Proposition 3 in v3), and v1's proof is the cleaner one — it lacks v3's mis-negated closing
   sentence.

### Priority verdict

**The 4π² isogeny criterion, its real/imaginary-separation proof, the division of two relations to
force log λ_i/log λ_k ∈ Q, the three-curve argument and the "at most two isogenous" conclusion are
all present in arXiv:math/0204195v1, dated 15 April 2002.** The prior session's finding is
CONFIRMED and the priority date is **15 April 2002** (preprint), with publication in
**Nagoya Math. J. 176 (2004), 159-180**. Cite the preprint date when the sentence is about
priority; cite the journal when the sentence is a plain reference.

---

## 6. Summary of disagreements with the agent report

| # | Report said | Primary source says | Severity |
|---|---|---|---|
| 1 | "his §7 Schanuel argument" | The paper has **6 sections**. The Schanuel argument is **§3.2, Proposition 3, p. 14**. | Must fix — a §7 citation would be uncheckable. |
| 2 | Theorem 2 is the "Γ ∩ SL_2(R) cocompact" case | Theorem 2 assumes only **Zariski-dense**; cocompactness is §5 (Prop. 5, Cor. 3). | Must fix if the note states the hypothesis. |
| 3 | "for each of these curves there is at most one other..." used as the 2002 quote | That sentence is **v3 (2003)**; v1 says "at most two can be isogenous". Content is 2002; wording is 2003. | Must fix if the quote is dated. |
| 4 | Setup "E_λ = C*/λ^Z = C/⟨2πi, log λ⟩ for real algebraic λ > 1" | Composite of three separate places; algebraicity is *derived*, not assumed, in Thm. 2's setting. | Minor — do not present as a single hypothesis. |
| 5 | Version list "v1 2002 / v3 2003" | There is also a **v2, 6 Nov 2002**. | Cosmetic. |
| 6 | (implied) Winkelmann gives the isogeny criterion | He gives **one direction only** (necessity). Sufficiency follows from his Lemma 7 but is not stated. | Must be phrased precisely — see §3.1. |
| 7 | (implied) the note sharpens him "to the exact Hom group and isogeny degree" | He has **no** Hom groups, **no** ranks, **no** isogeny degrees anywhere (grep: zero hits). The claim of *addition* is fair; a claim of priority over Thms. 1-3 is not. | See §3.2 for the calibrated wording. |
| 8 | Title, from Crossref/Cambridge | Both carry a spurious `Γ..`. Use the arXiv/zbMATH/PDF form. | Must fix if pasted from Crossref. |
| 9 | Author "J. Winkelmann" | He prints **Jörg** (umlaut); arXiv's metadata ASCII-izes to "Joerg". | Minor. |

Nothing in the report's core finding was refuted. The core finding — that the seed no-go note's
Theorems 1-3 are Winkelmann's, from 15 April 2002 — is **CONFIRMED against the primary source, in
both v1 and v3**.
