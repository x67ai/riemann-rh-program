# CLUSTER SEED-3 — transcendence-machinery cites for `results/c3-r/seed-no-go-note.md`

Verification pass for the arXiv citation execution, run 2026-08-27. Every field below was checked
against a primary source this session. Where the agent report (`results/arxiv/novelty-check.md`)
and a primary source disagree, the primary source wins and the disagreement is flagged
**[DISAGREEMENT]**.

**Headline: one of the four items is materially wrong.** MUST 10(b) — the claim that Waldschmidt's
AWS Lecture 5 Conjectures 5.34 and 5.35 are "the printed statement of Bertrand's weak
four-exponentials conjecture and of 4EC" — is **REFUTED**. Conjectures 5.34 and 5.35 in that
document are D. Bertrand's two conjectures on the *modular function* `J(q)` (algebraic
(in)dependence of `J(q_i), DJ(q_i), D²J(q_i)`, and the modular-polynomial statement). Neither is a
four-exponentials statement. In that same document the Four Exponentials Conjecture is
**Conjecture 5.11** and the Strong Four Exponentials Conjecture is **Conjecture 5.8**; the *weak*
four-exponentials conjecture does not appear in it at all. Do not execute MUST 10(b) as written.

Working files (scratchpad, this session), directory
`/private/tmp/claude-501/.../7e2b6f90-.../scratchpad/seed3/`:
`mahler.json, roy.json, diaz.json, zb_roy.json, zb_bsdgp.json, zb_odp.json, mmj.json,
diaz2007.pdf/.txt, diazp7-07.png, diazp8-08.png, wald_abs.html, wald_odp.pdf/.txt,
mmj_pub.pdf/.txt, aws5.pdf/.txt, aws5slides.pdf/.txt, bourbaki824.pdf/.txt, bk5-05.png,
diaz1997.pdf/.txt`

**On-disk corpus first, as instructed.** None of the four sources in this cluster is in
`fetched/`, `fetched-r2/`, `fetched-r3/` or `sources-extracted/`:

```
find <rh-program> -iname "*diaz*" -o -iname "*waldschmidt*" -o -iname "*mahler*" \
     -o -iname "*barre*" -o -iname "*roy*" -o -iname "*sirieix*"     # zero hits
```

Everything below therefore came off the network, each call in a retry loop.

---

# ITEM 1 (MUST 5) — Barré-Sirieix, Diaz, Gramain, Philibert 1996

## 1.1 What the report claimed

> K. Barre-Sirieix, G. Diaz, F. Gramain and G. Philibert, "Une preuve de la conjecture de
> Mahler-Manin", Invent. Math. 124 (1996), no. 1-3, 1-9.

plus the content claim that this "gives `j(E_p)` transcendental, hence `End(E_p) = Z`,
unconditionally and with more information than Gelfond–Schneider yields here."

## 1.2 Commands run

```
curl -sS --max-time 40 "https://api.crossref.org/works?query.bibliographic=Une+preuve+de+la+conjecture+de+Mahler-Manin&rows=5&select=DOI,title,author,container-title,volume,issue,page,published,type" -o mahler.json
curl -sS --max-time 40 "https://api.zbmath.org/v1/document/_search?search_string=Une%20preuve%20de%20la%20conjecture%20de%20Mahler-Manin&results_per_page=3" -o zb_bsdgp.json
curl -sSL --max-time 40 -A "Mozilla/5.0" "https://link.springer.com/article/10.1007/s002220050044" -o springer.html   # 3036 bytes = block page; WebFetch got a 303 to idp.springer.com (paywall)
curl -sSL --max-time 60 -A "Mozilla/5.0" "http://www.numdam.org/item/SB_1996-1997__39__105_0.pdf" -o bourbaki824.pdf  # OK
pdftoppm -r 160 -png -f 5 -l 5 bourbaki824.pdf bk5     # printed p. 108, read as an image
```

## 1.3 Raw evidence — bibliographic

Crossref (`mahler.json`, first hit), verbatim JSON:

```json
{
 "issue": "1-3",
 "DOI": "10.1007/s002220050044",
 "type": "journal-article",
 "page": "1-9",
 "title": ["Une preuve de la conjecture de Mahler-Manin"],
 "volume": "124",
 "author": [
  {"given": "Katia",    "family": "Barré-Sirieix"},
  {"given": "Guy",      "family": "Diaz"},
  {"given": "François", "family": "Gramain"},
  {"given": "Georges",  "family": "Philibert"}
 ],
 "container-title": ["Inventiones Mathematicae"],
 "published": {"date-parts": [[1996, 1, 18]]}
}
```

zbMATH Open (`zb_bsdgp.json`), independently:

```
TITLE: A proof of the Mahler-Manin conjecture
 AUT: ['Barré-Sirieix, Katia', 'Diaz, Guy', 'Gramain, François', 'Philibert, Georges']
 SRC: Invent. Math. 124, No. 1-3, 1-9 (1996).
 LNK: doi 10.1007/s002220050044
 MSC: ['11J91', '11G40']
```

**Every field the report gave checks out**, in two independent databases. Note the *accents*:
**Barré-Sirieix** (not "Barre-Sirieix") and **François**; the executing session should carry them.

## 1.4 Raw evidence — the theorem

Springer is paywalled and the arXiv has no copy (1996 Inventiones), so the paper's own page 1 could
not be read. Two independent authoritative accounts of the statement were read instead, and they
agree exactly.

**(a) Séminaire Bourbaki exp. 824 — Waldschmidt's report devoted to this very theorem.** Fetched
from Numdam; front matter reads

```
Astérisque
MICHEL WALDSCHMIDT
Sur la nature arithmétique des valeurs de fonctions modulaires
Astérisque, tome 245 (1997), Séminaire Bourbaki, exp. no 824, p. 105-140
Séminaire BOURBAKI                     Novembre 1996
49ème année, 1996-97, n° 824
```

Printed page **108**, §1.2 "Le théorème stéphanois sur `J`", read from the rendered page image
(`bk5-05.png`) because the OCR text layer drops inequality signs:

> Le théorème suivant [1] répond à une question posée d'abord par Mahler (dans le cas complexe
> [6], [43]), puis par Manin ([7], §4.12, qui s'intéresse surtout au cas p-adique).
>
> **Théorème 2.** – *Soit α ∈ C un nombre algébrique vérifiant 0 < |α| < 1. Alors le nombre J(α)
> est transcendant.*

Reference `[1]` in that exposé is the Barré-Sirieix–Diaz–Gramain–Philibert paper (the introduction,
p. 105, names them: *"a été résolue en 1995 par une équipe stéphanoise : Barré-Sirieix, Diaz,
Gramain et Philibert"* — "stéphanoise" = of Saint-Étienne, hence "le théorème stéphanois").

The same exposé fixes the normalization of `J` on p. 105, §1.1:

> Comme `j(τ + 1) = j(τ)`, il existe une fonction `J`, analytique dans le disque unité pointé
> `{z ∈ C, 0 < |z| < 1}`, telle que `J(e^{2iπτ}) = j(τ)`.

**(b) zbMATH Open review** of the paper itself (independent of Waldschmidt):

> This paper answers the question of the transcendence values for the Fourier expansion at infinity
> of the modular invariant `j` at algebraic points. More precisely, `j(q)` is proved to be
> transcendental over the field of rationals (respectively over the field of `p`-adic rationals)
> for any non-zero algebraic point `q` of the unit disk of the complex plane (respectively of the
> completion of the field of `p`-adic rationals). This result conjectured by Mahler in the complex
> case and by Manin in the `p`-adic case has numerous applications in the theory of elliptic curves
> and `p`-adic `L` functions.

So the theorem, in the complex case, is exactly as the task stated it:

> **For `q` algebraic with `0 < |q| < 1`, `J(q)` is transcendental**, where `J` is the modular
> invariant as a function of the nome, `j(τ) = J(e^{2πiτ})`.

**Hypotheses, exactly:** `q ∈ C`, `q` algebraic over `Q`, `0 < |q| < 1`. Nothing else. In
particular no hypothesis on `τ`.

**Provenance flag (trap (b) of the brief).** The theorem statement above is verified from a
Bourbaki exposé and a zbMATH review, **not from the BSDGP paper's own page 1**, which is behind
Springer's paywall on this machine. Both witnesses are of very high quality and agree verbatim,
but the citation string below should be regarded as bibliographically primary-verified (Crossref +
zbMATH) and content-verified at one remove.

## 1.5 Does the theorem apply to `E_p`? — the reasoning, stated in full

The seed note (`results/c3-r/seed-no-go-note.md` §1.2) defines

```
E_p = C^× / p^Z ,   a rectangular torus with lattice Λ_p = Z ⊕ Z·τ_p ,  τ_p = i·log p /(2π).
```

**Step 1 — the nome is `1/p`, and it is algebraic.** The Tate uniformization is
`C^×/q^Z ≅ C/(Z + Zτ)` with `q = e^{2πiτ}`, and the standard convention takes `|q| < 1`. As a
*subgroup* of `C^×`, `p^Z = (p^{-1})^Z`, so `E_p = C^×/q^Z` with `q = 1/p`. This is consistent with
the note's own `τ_p`: `e^{2πiτ_p} = e^{2πi · i log p/(2π)} = e^{-log p} = 1/p`. And `1/p` is
**rational**, hence algebraic, with `0 < |1/p| = 1/p < 1` for every prime `p ≥ 2`.

**Step 2 — the hypotheses are literally satisfied.** BSDGP asks only that `q` be algebraic with
`0 < |q| < 1`. Take `q = 1/p`. Both conditions hold, with no adjustment and no gap. Therefore

```
j(E_p) = j(τ_p) = J(e^{2πiτ_p}) = J(1/p)   is transcendental.
```

*Presentational caveat, not a mathematical one:* writing `E_p = C^×/p^Z` invites the reading
`q = p`, for which `|q| > 1` and the hypothesis fails as stated. The note should say `q = p^{-1}`
explicitly (or note `p^Z = (p^{-1})^Z`) when it invokes the theorem, so that no referee has to
supply the step.

**Step 3 — transcendence of `j` gives `End(E_p) = Z`.** For a complex elliptic curve `E = C/Λ`,
`End(E)` is either `Z` or an order in an imaginary quadratic field. In the second (CM) case `τ` is
imaginary quadratic and `j(τ)` is an algebraic integer — classical CM theory; equivalently, by
Schneider's 1937 theorem (quoted in the same Bourbaki exposé, p. 105: *"Les nombres quadratiques
imaginaires sont les seuls nombres complexes tels que τ et j(τ) soient simultanément algébriques"*),
which is the theorem the note's §7 route also lives next to. Since `j(E_p)` is transcendental, it
is in particular not algebraic, so `E_p` is not CM, so `End(E_p) = Z`. **Unconditional.**

**Step 4 — is it "more information than Gelfond–Schneider yields here"? Yes, strictly.** The
note's §7 Proposition uses Gelfond–Schneider to prove `(log p)² ∉ 4π²·Q`, i.e. `τ_p² ∉ Q`, i.e.
`τ_p` is not imaginary quadratic, hence no CM, hence `End(E_p) = Z`. BSDGP gives the strictly
stronger conclusion `j(E_p) ∉ Q̄` (transcendental), from which `τ_p` not imaginary quadratic
follows a fortiori. So:

* the report's content claim is **CONFIRMED** as stated;
* but the honest framing for the note is that BSDGP is a **strengthening**, not a repair. The §7
  Gelfond–Schneider argument already suffices for `End(E_p) = Z` and is more elementary and
  self-contained. BSDGP should be cited for the extra fact (`j(E_p)` transcendental) and as the
  unconditional heavy artillery, not presented as though `End(E_p) = Z` needed it.

**No gap found.** The hypotheses apply literally once `q = p^{-1}` is written down.

## 1.6 Verdict and citation

**CONFIRMED.**

Ready to paste:

```
K. Barré-Sirieix, G. Diaz, F. Gramain and G. Philibert, *Une preuve de la conjecture de
Mahler-Manin*, Invent. Math. **124** (1996), no. 1-3, 1-9; doi:10.1007/s002220050044.
```

Supporting cite, if the note wants the statement in a readable place (recommended, since Springer
is paywalled and this is open access on Numdam):

```
M. Waldschmidt, *Sur la nature arithmétique des valeurs de fonctions modulaires*, Séminaire
Bourbaki 1996/97, exp. no. 824, Astérisque **245** (1997), 105-140 (Théorème 2, p. 108).
```

---

# ITEM 2 (MUST 9)(a) — D. Roy 1992

## 2.1 What the report claimed

> D. Roy, "Matrices whose coefficients are linear forms in logarithms", J. Number Theory 41 (1992),
> 22-47. *** REPORT SAYS NOT FETCHED, known via Diaz. ***

## 2.2 Commands run

```
curl -sS --max-time 40 "https://api.crossref.org/works?query.bibliographic=Matrices+whose+coefficients+are+linear+forms+in+logarithms+Roy&rows=5&select=DOI,title,author,container-title,volume,issue,page,published,type" -o roy.json
curl -sS --max-time 40 "https://api.zbmath.org/v1/document/_search?search_string=Matrices%20whose%20coefficients%20are%20linear%20forms%20in%20logarithms%20Roy&results_per_page=3" -o zb_roy.json
```

## 2.3 Raw evidence

Crossref, first hit:

```
10.1016/0022-314x(92)90081-y | ['Matrices whose coefficients are linear forms in logarithms']
 | ['Journal of Number Theory'] | v 41 | p 22-47 | [[1992, 5]] | ['Roy']
```

zbMATH Open:

```
TITLE: Matrices whose coefficients are linear forms in logarithms
 AUT: ['Roy, Damien']
 SRC: J. Number Theory 41, No. 1, 22-47 (1992).
 LNK: doi 10.1016/0022-314X(92)90081-Y
```

zbMATH review (verbatim, whitespace normalized):

> Denote by `L` the `Q`-vector space of complex numbers `ℓ` such that `e^ℓ` is an algebraic number,
> and by `𝓛` the vector space generated by `1` and `L` over the field `Q̄` of algebraic numbers.
> The elements of `L` are the logarithms of non-zero algebraic numbers, while the elements of `𝓛`
> are the linear forms in logarithms of algebraic numbers: `β₀ + β₁ log α₁ + ⋯ + βₙ log αₙ`. **One
> result of this paper is a lower bound for the rank of a matrix whose entries are in `𝓛`.** The
> simplest case is as follows: a `2×3` matrix with entries in `𝓛` whose columns are `Q̄`-linearly
> independent, and whose rows are `Q̄`-linearly independent, has rank 2 (the six exponentials
> theorem deals with a `2×3` matrix with entries in `L`). The proof relies on the theorem of the
> linear subgroup, which is sharpened by the author […] He deduces improvements of earlier results
> due to M. Emsalem […] and M. Laurent […] on the conjectures of Leopoldt and Jaulent concerning
> the `p`-adic rank of `S`-units in a number field.

Cross-check from **inside Diaz 2007** (p. 379, read directly, see Item 2(b) below), which is the
route the report said it knew this by:

> Le principal outil de ce paragraphe est un résultat de D.Roy obtenu en 1992, le théorème fort des
> six exponentielles (voir **[Roy 1992], corollary 2** ; [Wa 2000], corollary 11.16 ; [Wa 2004],
> theorem 2.1).

The two agree: **Roy 1992 is where the strong six exponentials theorem lives.**

**Caution, and the reason the report's "known via Diaz" flag mattered:** Waldschmidt's *Open
Diophantine Problems* bibliography contains a *different* 1992 Roy paper — `[Ro 1992] = D. Roy,
"Simultaneous approximation in number fields", Invent. Math. 109 No. 3 (1992), 547-556`. That is
**not** this paper. Anyone chasing "[Ro 1992]" in ODP will land on the wrong article. The JNT paper
appears in ODP's bibliography as the entry beginning *"Roy, D. – Matrices dont les coefficients sont
des formes linéaires"* (the Séminaire de Théorie des Nombres announcement), which is a companion
note, not the JNT article.

## 2.4 Verdict and citation

**CORRECTED** (nothing the report gave was wrong; the issue number was missing and is added).
Title, journal, volume, page range, year and author all confirmed in two independent databases.

One sentence on what it proves: *it gives a lower bound for the rank of a matrix whose entries are
linear forms in logarithms of algebraic numbers with algebraic coefficients — in particular the
**strong six exponentials theorem**: a `2×3` matrix with entries in `𝓛̃` whose two rows and three
columns are each `Q̄`-linearly independent has rank 2 — proved via a sharpened linear subgroup
theorem, with applications to the Leopoldt and Jaulent conjectures.*

Ready to paste:

```
D. Roy, *Matrices whose coefficients are linear forms in logarithms*, J. Number Theory **41**
(1992), no. 1, 22-47; doi:10.1016/0022-314X(92)90081-Y.
```

(zbMATH id Zbl 0763.11030, if the note carries Zbl numbers — it currently does not.)

---

# ITEM 2 (MUST 9)(b) — G. Diaz 2007, JTNB

## 3.1 What the report claimed

> G. Diaz, "Produits et quotients de combinaisons lineaires de logarithmes de nombres algebriques:
> conjectures et resultats partiels", J. Theor. Nombres Bordeaux 19 (2007), no. 2, 373-391;
> doi:10.5802/jtnb.592.

Content claim, to be checked verbatim:

> "Diaz 2007 Corollaire 1(1) needs `(λ₀, λ₂, λ̄₂)` to be `Q̄`-free, which fails for `λ₂ = log q`
> real."

## 3.2 Commands run

```
curl -sS  --max-time 40 "https://api.crossref.org/works/10.5802/jtnb.592" -o diaz.json
curl -sSL --max-time 60 -A "Mozilla/5.0" "https://jtnb.centre-mersenne.org/article/JTNB_2007__19_2_373_0.pdf" -o diaz2007.pdf   # 526640 bytes, 20 pp.
pdftotext diaz2007.pdf diaz2007.txt
pdftoppm -r 150 -png -f 7 -l 8 diaz2007.pdf diazp     # printed pp. 378-379, read as images
```

The PDF is the **full 20-page article**, open access from Centre Mersenne (the successor to
cedram/Numdam for JTNB). It was read, not skimmed.

## 3.3 Raw evidence — bibliographic

Crossref (`diaz.json`):

```
DOI : 10.5802/jtnb.592
title : ['Produits et quotients de combinaisons linéaires de logarithmes de nombres algébriques : conjectures et résultats partiels']
author : [{'given': 'Guy', 'family': 'Diaz'}]
container-title : ['Journal de théorie des nombres de Bordeaux']
volume : 19 ; issue : 2 ; page : 373-391
published : {'date-parts': [[2008, 12, 2]]}
```

The article's **own cover page**, read from the PDF (this is the primary, and it settles the year
that Crossref's deposit date muddies):

```
Guy DIAZ
Produits et quotients de combinaisons linéaires de logarithmes de nombres
algébriques : conjectures et résultats partiels
Tome 19, no 2 (2007), p. 373-391.
<http://jtnb.cedram.org/item?id=JTNB_2007__19_2_373_0>
© Université Bordeaux 1, 2007, tous droits réservés.
...
Journal de Théorie des Nombres
de Bordeaux 19 (2007), 373-391
```

**[Minor DISAGREEMENT — with Crossref, not with the report.]** Crossref's `published` /`issued`
date is **2008-12-02**. That is the Centre Mersenne deposit/online date, not the issue date. The
article's own cover page says **Tome 19, no 2 (2007)** and the running header says **19 (2007),
373-391**. The report's "19 (2007), no. 2" is **right**; do not "fix" it to 2008.

Manuscript received date, from p. 373 footnote: `Manuscrit reçu le 31 octobre 2005.`

Abstract, verbatim from p. 373:

> **Résumé.** Ce texte montre qu'en combinant le théorème fort des six exponentielles de D.Roy et
> la conjugaison complexe, on peut obtenir un certain nombre de cas particuliers de la conjecture
> forte des quatre exponentielles.
>
> **Abstract.** In this paper, it is shown that the strong six exponentials theorem due to D.Roy
> and complex conjugation give partial results for the strong four exponentials conjecture.

## 3.4 Raw evidence — Corollaire 1, quoted in full

**Notation first** (p. 375, §1.1), because the corollary is unreadable without it:

> On notera `Q̄` le corps des nombres algébriques (ie la clôture algébrique de `Q` dans `C`) et `L`
> le `Q`-espace vectoriel des logarithmes de nombres algébriques :
> `L := {ℓ ∈ C ; exp(ℓ) ∈ Q̄}`.
> Ce n'est pas vraiment sur `L` que l'on va travailler, mais plutôt sur `𝓛̃` le `Q̄`-espace
> vectoriel engendré dans `C` par `1` et `L` :
> `𝓛̃ := {α₀ + α₁ℓ₁ + … + αₙℓₙ ; n ∈ N, (α₀,…,αₙ) ∈ Q̄^{n+1}, (ℓ₁,…,ℓₙ) ∈ Lⁿ}`.
> **Notons que `L` et `𝓛̃` sont stables par conjugaison complexe.**

So `𝓛̃` is exactly Waldschmidt's `𝓛̃` — linear forms in logarithms of algebraic numbers with
algebraic coefficients, including the constants. "`Q̄`-libre" means `Q̄`-linearly independent.

**Corollaire 1 (PQ), printed page 379**, read from the rendered page image `diazp8-08.png` (the
overbars denoting complex conjugation are TeX rules and are invisible to `pdftotext`; the image was
read specifically to recover them):

> **Corollaire 1 (PQ).**
>
> **1)** *Soient `λ₀, λ₁, λ₂ ∈ 𝓛̃`. On suppose que la famille `(λ₀, λ₂, λ̄₂)` est `Q̄`-libre et que
> `λ₁/λ₀ ∈ (R ∪ iR)\Q̄`. Alors :*
> `λ₁λ₂/λ₀ ∉ 𝓛̃`.
>
> **2)** *Soient `λ₁, λ₂ ∈ 𝓛̃` tels que `(λ₁, λ₂, λ₁λ₂)` est `Q̄`-libre. Alors :*
> `{λ₁λ₂, λ₁/λ₂} ⊄ 𝓛̃`.
>
> **3)** *Soient `λ₁, λ₂ ∈ 𝓛̃` tels que `λ₂ ≠ 0` et tel que `(1, λ₁, 1/λ₂)` est `Q̄`-libre. Alors :*
> `{λ₁λ₂, 1/λ₂} ⊄ 𝓛̃`. *En particulier pour tout `λ ∈ 𝓛̃\Q̄` on a : `{λ², 1/λ} ⊄ 𝓛̃`.*
>
> **4)** *Soient `λ₀, λ₁ ∈ 𝓛̃` tels que `(λ₀², λ₁, λ₀λ₁)` est `Q̄`-libre. Alors :*
> `{λ₁/λ₀, λ₁/λ₀²} ⊄ 𝓛̃`. *En particulier pour tout `λ ∈ 𝓛̃\Q̄` on a : `{1/λ, 1/λ²} ⊄ 𝓛̃`.*

That the second entry of the triple in part 1 carries a conjugation bar is confirmed three ways:
(i) directly in the rendered image; (ii) the same bar is visible in the image of the facing page
378, in the line *"c) Soit `λ ∈ 𝓛̃` avec `(λ, λ̄)` `Q̄`-libre ; alors `|λ| ∉ 𝓛̃`"*; (iii) logically —
`(λ₀, λ₂, λ₂)` with a repeated entry is `Q̄`-dependent for every input, which would make the
corollary vacuous.

The corollary's engine, **Théorème 3, printed page 379** (`= Roy 1992, corollary 2`), also read from
the image:

> **Théorème 3 (théorème fort des six exponentielles).** *Les trois assertions suivantes sont
> équivalentes et sont vraies.*
> **1) Version 1.** *Soient `x₁, x₂` (resp. `y₁, y₂, y₃`) des nombres complexes `Q̄`-linéairement
> indépendants. Alors on a : `{x₁y₁, x₁y₂, x₁y₃, x₂y₁, x₂y₂, x₂y₃} ⊄ 𝓛̃`.*
> **2) Version 2.** *Soit `M` une matrice `2×3` à coefficients dans `𝓛̃`, dont les 2 lignes sont
> `Q̄`-linéairement indépendantes et dont les 3 colonnes sont `Q̄`-linéairement indépendantes. Alors
> `M` est de rang 2.*
> **3) Version 3.** *Soit `(λ₀, λ₁, λ₂, λ₃) ∈ 𝓛̃⁴` tel que les familles `(λ₀, λ₁)` et
> `(λ₀, λ₂, λ₃)` sont `Q̄`-libres ; alors : `{λ₁λ₂/λ₀, λ₁λ₃/λ₀} ⊄ 𝓛̃`.*

## 3.5 The content claim, adjudicated

**Hypotheses of Corollaire 1(1), exactly:**

* `λ₀, λ₁, λ₂ ∈ 𝓛̃`;
* `(λ₀, λ₂, λ̄₂)` is `Q̄`-linearly independent ("`Q̄`-libre");
* `λ₁/λ₀ ∈ (R ∪ iR) \ Q̄`, i.e. the ratio is real or purely imaginary, and not algebraic.

**Conclusion:** `λ₁λ₂/λ₀ ∉ 𝓛̃`.

**Why one would want it in the seed note.** The note's open rider (T1) is: for distinct primes
`p ≠ q`, is `log p · log q ∈ 4π²·Q` possible? Set `λ₀ = 2πi`, `λ₁ = log p`, `λ₂ = log q`. All three
are in `𝓛̃` (indeed in `L`). Then `λ₁λ₂/λ₀ = log p·log q/(2πi)`, and if `log p·log q = 4π²·u/v`
this equals `-2πi·(u/v)`, which **is** in `𝓛̃`. So Corollaire 1(1), if applicable, would refute
(T1) unconditionally — which would be a very big deal.

**It is not applicable.** `λ₂ = log q` is a **real** number, so `λ̄₂ = λ₂`, so the family
`(λ₀, λ₂, λ̄₂) = (2πi, log q, log q)` is `Q̄`-linearly **dependent** (the relation
`0·λ₀ + 1·λ₂ - 1·λ̄₂ = 0` is nontrivial). The freeness hypothesis fails.

**The report's reading is CONFIRMED, verbatim and exactly.**

**And it is robust — worth recording, because a referee will try the permutations.** Every
assignment of `{2πi, log p, log q}` to `(λ₀, λ₁, λ₂)` fails the same hypothesis, because in each
case `λ₂` is either real (a `log` of a prime) or purely imaginary (`2πi`), and in both cases
`λ̄₂ = ±λ₂`:

| `λ₀` | `λ₁` | `λ₂` | `λ̄₂` | `(λ₀, λ₂, λ̄₂)` |
|---|---|---|---|---|
| `2πi` | `log p` | `log q` | `log q` | dependent (`λ₂ - λ̄₂ = 0`) |
| `2πi` | `log q` | `log p` | `log p` | dependent |
| `log p` | `2πi` | `log q` | `log q` | dependent |
| `log p` | `log q` | `2πi` | `-2πi` | dependent (`λ₂ + λ̄₂ = 0`) |
| `log q` | `log p` | `2πi` | `-2πi` | dependent |
| `log q` | `2πi` | `log p` | `log p` | dependent |

The `λ₂` slot in Corollaire 1(1) is precisely where Diaz's method **needs** complex conjugation to
supply a genuinely new third direction (that is what the abstract advertises: *"le théorème fort
des six exponentielles de D.Roy **et la conjugaison complexe**"*). A `λ₂` lying on the real or the
imaginary axis contributes nothing under conjugation, and the corollary is silent. That is exactly
why (T1) survives Diaz 2007, and the note is right to leave it open.

**Second-order check — do parts 2, 3, 4 rescue it?** No. Part 2 needs `(λ₁, λ₂, λ₁λ₂)` `Q̄`-free
and concludes only that one of `{λ₁λ₂, λ₁/λ₂}` is outside `𝓛̃` — a disjunction, not what (T1)
needs. Parts 3 and 4 concern `1/λ₂` and `λ₁/λ₀²`, not the product-over-`2πi` shape. Théorème 3
Version 3 (strong six exponentials) likewise yields only the disjunction `{λ₁λ₂/λ₀, λ₁λ₃/λ₀} ⊄ 𝓛̃`,
which needs a *third* independent logarithm and delivers "at least one of two" — this is the same
wall the note's §7 already describes ("the proven six-exponentials theorem being blocked from
reaching it by this note's own Theorem 2").

## 3.6 Verdict and citation

**CONFIRMED.**

Ready to paste:

```
G. Diaz, *Produits et quotients de combinaisons linéaires de logarithmes de nombres algébriques :
conjectures et résultats partiels*, J. Théor. Nombres Bordeaux **19** (2007), no. 2, 373-391;
doi:10.5802/jtnb.592.
```

Suggested accompanying sentence for the note, which the verification supports word for word:

> Diaz's Corollaire 1(1) [Di07, p. 379] deduces `λ₁λ₂/λ₀ ∉ 𝓛̃` from the strong six-exponentials
> theorem, but it requires the family `(λ₀, λ₂, λ̄₂)` to be `Q̄`-linearly independent. In the
> situation of (T1) the slot `λ₂` is a real logarithm `log q` (or the purely imaginary `2πi`), so
> `λ̄₂ = ±λ₂` and the family is dependent for every assignment; complex conjugation supplies no new
> direction and the corollary does not apply.

---

# ITEM 3 (MUST 10)(a) — Waldschmidt, *Open Diophantine Problems*, Conjecture 3.7

## 4.1 What the report claimed

> M. Waldschmidt, "Open Diophantine Problems", Moscow Math. J. 4 (2004), 245-305; arXiv:math/0312440,
> Conjecture 3.7. […] confirm it is the matrix form of the four-exponentials conjecture (a 2x2
> matrix of logarithms of algebraic numbers with rank conditions).

## 4.2 Commands run

```
curl -sSL --max-time 60 "https://arxiv.org/abs/math/0312440" -o wald_abs.html
curl -sSL --max-time 90 "https://arxiv.org/pdf/math/0312440"  -o wald_odp.pdf     # 58 pp., v2
curl -sS  --max-time 40 "https://api.crossref.org/works?query.bibliographic=Open+Diophantine+Problems+Waldschmidt+Moscow&rows=4&..." -o mmj.json
curl -sS  --max-time 40 "https://api.zbmath.org/v1/document/_search?search_string=Open%20Diophantine%20Problems%20Waldschmidt&results_per_page=3" -o zb_odp.json
curl -sSL --max-time 60 -A "Mozilla/5.0" "https://www.ams.org/journals/hosted/journals/mmj/vol4-1-2004/waldschmidt.pdf" -o mmj_pub.pdf   # the PUBLISHED version, open access on ams.org
pdftotext mmj_pub.pdf mmj_pub.txt ; pdftotext -f 25 -l 25 mmj_pub.pdf -
```

## 4.3 Raw evidence — bibliographic

arXiv abs page `<meta>` block:

```
citation_title  = "Open Diophantine Problems"
citation_author = "Waldschmidt, Michel"
citation_date   = "2003/12/24"     citation_online_date = "2004/01/24"
citation_arxiv_id = "math/0312440"
Comments: 58 pages. to appear in the Moscow Mathematical Journal vo. 4 N.1 (2004) dedicated to Pierre Cartier
```

The arXiv record carries **no `journal-ref` field**, so the arXiv alone does not settle
volume/issue/pages. Crossref does:

```
10.17323/1609-4514-2004-4-1-245-305 | ['Open Diophantine Problems']
 | ['Moscow Mathematical Journal'] | v 4 | n 1 | p 245-305 | [[2004]] | ['Waldschmidt']
```

zbMATH, independently: `Mosc. Math. J. 4, No. 1, 245-305 (2004).`

And the **published article's own first page** (AMS-hosted PDF, open access):

```
MOSCOW MATHEMATICAL JOURNAL
Volume 4, Number 1, January–March 2004, Pages 245–305

OPEN DIOPHANTINE PROBLEMS
MICHEL WALDSCHMIDT
Dédié à un jeune septuagénaire, Pierre Cartier, qui m'a beaucoup appris
```

Three independent sources plus the article itself. The report's fields are **all correct**; the
issue number (no. 1) and the DOI are additions.

## 4.4 Raw evidence — Conjecture 3.7, verbatim

From the **published** PDF, printed page **269** (running head "OPEN DIOPHANTINE PROBLEMS"):

> Finally, a special case of Conjecture 3.6 is the well known Four Exponentials Conjecture due to
> Schneider ([Schn, Chap. V, end of §4, Problem 1]), S. Lang ([La1, Chap. II, §1], [La2, p. 638])
> and K. Ramachandra ([R, II, §4]).
>
> **Conjecture 3.7 (Four Exponentials Conjecture).** *Let `x₁, x₂` be two `Q`-linearly independent
> complex numbers and `y₁, y₂` also be two `Q`-linearly independent complex numbers. Then at least
> one of the four numbers*
>
>     exp(x_i y_j)        (i = 1, 2,  j = 1, 2)
>
> *is transcendental.*

Immediately following it, on the same page (quoted from the arXiv v2 text, which renders the
display that `pdftotext` drops from the AMS file — the wording is identical in both):

> The four exponentials Conjecture can be stated as follows: consider a `2 × 2` matrix whose
> entries are logarithms of algebraic numbers:
>
>     M = ( log α₁₁   log α₁₂
>           log α₂₁   log α₂₂ ) ;
>
> assume that the two rows of this matrix are linearly independent over `Q` (in `C²`), and also
> that the two columns are linearly independent over `Q`; then the rank of this matrix is 2.
>
> We refer to [W 2000b] for a detailed discussion of this topic, including the notion of structural
> rank of a matrix and the result, due to D. Roy, that Conjecture 3.3 is equivalent to a conjecture
> on the rank of matrices whose entries are logarithms of algebraic numbers.

## 4.5 Adjudication

* The **numbered** Conjecture 3.7 is the Four Exponentials Conjecture in its **exponentials form**
  (`exp(x_i y_j)`, at least one transcendental), *not* in matrix form.
* The **matrix form the report describes** — a `2×2` matrix of logarithms of algebraic numbers,
  rows `Q`-independent, columns `Q`-independent, conclusion rank 2 — is stated in the **unnumbered
  paragraph immediately after** Conjecture 3.7, on the same printed page 269.

So the report's substance is right and its pointer is very slightly off: it is not accurate to say
"Conjecture 3.7 *is* the matrix form"; the accurate statement is "Conjecture 3.7 is the Four
Exponentials Conjecture, restated in matrix form immediately below it." Any citation the note makes
should read **"[Wal04, Conjecture 3.7 and the matrix restatement following it, p. 269]"** so a
referee checking the numbered item finds what the note says is there.

For completeness, since the note's §7 uses the four-exponentials machinery: the neighbouring
numbered items on pp. 268-269 are Conjecture 3.4 (Strong Four Exponentials), 3.5 (Strong Five
Exponentials), 3.6 (Roy's `4×4` skew-symmetric matrix conjecture), 3.7 (Four Exponentials). The
note's `[4EC]` bibliography entry can point at 3.7.

An independent corroboration of the matrix form, from the Bourbaki exposé read for Item 1
(Astérisque 245, p. 108), if a second citation is wanted:

> **Conjecture des quatre exponentielles.** – *On considère une matrice
> `( log α₁  log α₂ ; log α₃  log α₄ )` dont les coefficients sont des logarithmes de nombres
> algébriques. Si les deux lignes sont linéairement indépendantes sur `Q`, et si les deux colonnes
> sont aussi linéairement indépendantes sur `Q`, alors le déterminant ne s'annule pas.*

## 4.6 Verdict and citation

**CORRECTED** — bibliographic fields all confirmed (issue and DOI added); the content claim is
right in substance but the numbered conjecture is the exponentials form, with the matrix form in
the sentence following. Cite both together.

Ready to paste:

```
M. Waldschmidt, *Open Diophantine Problems*, Mosc. Math. J. **4** (2004), no. 1, 245-305;
doi:10.17323/1609-4514-2004-4-1-245-305; arXiv:math/0312440. (Conjecture 3.7 and the matrix
restatement immediately following it, p. 269.)
```

---

# ITEM 3 (MUST 10)(b) — Waldschmidt, AWS Lecture 5 — **REFUTED**

## 5.1 What the report claimed

> "AWS Lecture 5: Conjectures and open problems" (Arizona Winter School), Conjectures 5.34 and
> 5.35. […] The report says 5.34/5.35 are the printed statement of Bertrand's weak
> four-exponentials conjecture and of 4EC. Confirm which is which.

## 5.2 Commands run

```
WebSearch: Waldschmidt "Arizona Winter School" lecture "Conjectures and open problems" 5.34 5.35
curl -sSL --max-time 60 -A "Mozilla/5.0" "https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf" -o aws5.pdf   # 31 pp.
curl -sSL --max-time 60 -A "Mozilla/5.0" "https://swc-math.github.io/aws/2008/08WaldschmidtSlides5.pdf" -o aws5slides.pdf
pdftotext aws5.pdf aws5.txt ; grep -n "Conjecture 5.3[0-9]" aws5.txt
WebFetch https://swc-math.github.io/aws/2008/index.html
```

## 5.3 The document, identified exactly

Front matter of `AWSLecture5.pdf`, verbatim from page 1:

```
The University of Arizona
The Southwest Center for Arithmetic Geometry
2008 Arizona Winter School, March 15-19, 2008 Special Functions and Transcendence
http://swc.math.arizona.edu/aws/08/index.html
Updated: February 26, 2008

An introduction to
irrationality and transcendence methods.
Michel Waldschmidt

Lecture 5

5   Conjectures and open problems

We already met a number of open problems in these notes, in particular in § 1.1.1. We collect
further conjectures in this field, but this is only a very partial list of questions which deserve
to be investigated further. Part of this section if from [W 2004], especially § 3.
```

("[W 2004]" is *Open Diophantine Problems* — Item 3(a) — which is why the two documents share
almost all their conjecture text under different numbering.)

The AWS 2008 school page (`https://swc-math.github.io/aws/2008/index.html`, fetched) confirms:
school title **"Arizona Winter School 2008: Special Functions and Transcendence"**, dates
**March 15-19, 2008**, Waldschmidt's course **"An introduction to irrationality and transcendence
methods"**, and it links the lecture notes at `.../AWSLecture1.pdf` … `AWSLecture5.pdf` on
Waldschmidt's own page (the old `math.jussieu.fr/~miw/` host now redirects to
`webusers.imj-prg.fr/~michel.waldschmidt/`).

Exact title / year / URL:

* **Title:** *An introduction to irrationality and transcendence methods*, Lecture 5, §5
  "Conjectures and open problems" — 2008 Arizona Winter School, "Special Functions and
  Transcendence", March 15-19, 2008 (notes dated 26 February 2008).
* **URL:** `https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf`
  (slides, separately: `https://swc-math.github.io/aws/2008/08WaldschmidtSlides5.pdf`)

## 5.4 Conjectures 5.34 and 5.35, quoted verbatim

From `AWSLecture5.pdf`, printed page **118** (the page marker "118" sits immediately above 5.34 in
the text layer):

> Further related open problems are proposed by G. Diaz in [Di 1997] and [Di 2000], in connection
> with conjectures due to D. Bertrand on the values of the modular function `J(q)`, where
> `j(τ) = J(e^{2iπτ})` (see [Bert 1997b] as well as [NeP 2001] Chap. 1, § 4 and Chap. 2, § 4).
>
> **Conjecture 5.34 (Bertrand).** *Let `q₁, …, qₙ` be non-zero algebraic numbers in the unit open
> disc such that the `3n` numbers*
>
>     J(q_i),  DJ(q_i),  D²J(q_i)        (i = 1, …, n)
>
> *are algebraically dependent over `Q`. Then there exist two indices `i ≠ j` (`1 ≤ i ≤ n`,
> `1 ≤ j ≤ n`) such that `q_i` and `q_j` are multiplicatively dependent.*
>
> **Conjecture 5.35 (Bertrand).** *Let `q₁` and `q₂` be two non-zero algebraic numbers in the unit
> open disc. Suppose that there is an irreducible element `P ∈ Q̄[X, Y]` such that*
>
>     P( J(q₁), J(q₂) ) = 0.
>
> *Then there exist a constant `c` and a positive integer `s` such that `P = cΦ_s`, where `Φ_s` is
> the modular polynomial of level `s`. Moreover `q₁` and `q₂` are multiplicatively dependent.*

## 5.5 **[DISAGREEMENT — the report is materially wrong]**

Neither 5.34 nor 5.35 is a four-exponentials statement of any kind. Both are **D. Bertrand's
conjectures on the modular function `J`.** They are the AWS-numbered twins of Conjectures **3.24**
and **3.25** of *Open Diophantine Problems* (verified: the text is word-for-word identical in
`wald_odp.txt` lines 2313-2325, in the paragraph likewise introduced by "conjectures due to
D. Bertrand on the values of the modular function `J(q)`").

Where the four-exponentials material actually is **in the same document**
(`grep -n "Conjecture 5.[0-9]*" aws5.txt`, with the statements read):

| number | what it is |
|---|---|
| **Conjecture 5.8** | **Strong Four Exponentials Conjecture** |
| Conjecture 5.10 | Roy — `4 × 4` skew-symmetric matrix with entries in `L`, rank ≤ 2 |
| **Conjecture 5.11** | **Four Exponentials Conjecture** (introduced by "Finally a special case of Conjecture 5.10 is the well known Four Exponentials Conjecture") |
| Conjectures 5.34, 5.35 | Bertrand, on values of the modular function `J` |

And the **weak** four-exponentials conjecture is **not in AWS Lecture 5 at all**:
`grep -n -i "weak four" aws5.txt wald_odp.txt diaz2007.txt` returns **zero hits** in all three
documents. The AWS slides (`08WaldschmidtSlides5.pdf`) mention only "The Strong Four Exponentials
Conjecture" (two hits) and Bertrand nowhere.

## 5.6 What the executing session should do instead

**Do NOT execute MUST 10(b) as written.** Two replacement options, both verified this session:

**(i) If the note wants a printed statement of the four-exponentials conjecture in the AWS notes,**
the correct pointers are Conjecture **5.11** (4EC) and Conjecture **5.8** (strong 4EC) — and both
are redundant with Item 3(a), which is a *published, DOI'd* source and is strictly better for an
arXiv bibliography. Recommendation: drop the AWS citation entirely and cite only [Wal04].

**(ii) If the note wants "Bertrand's weak four-exponentials conjecture" in print** — which is what
the seed note's own dated priority-correction block (head of `seed-no-go-note.md`, item 2) says
(T1) is — the AWS notes do not contain it, and the correct primary is the one that block already
names. Verified this session from the open-access Centre Mersenne PDF of that paper
(`JTNB_1997__9_1_229_0.pdf`, read; printed **p. 231**, §1):

> Le cas particulier de (C4E) que vise D. Bertrand ([2], §5) est le suivant.
>
> **(C4E faible)** *Soient `α₁, α₂` des nombres réels algébriques positifs différents de 1. Alors
> `π²` et `(log α₁)(log α₂)` sont `Q`-linéairement indépendants (`log` désigne ici le logarithme
> népérien).*
>
> On obtient la même conjecture en remplaçant la conclusion de (C4E faible) par
> `(log α₁)·(log α₂) ≠ π²`. Pour faire le lien avec (C4E) il suffit de prendre `x₁ = 1`,
> `x₂ = log α₁`, `y₁ = 2iπ`, `y₂ = log α₂`.

with `[2]` in that paper's bibliography reading, verbatim:

> [2]  D. Bertrand, *Theta functions and transcendence*, Madras Number Theory Symposium 1996,
> The Ramanujan J. Math. (à paraître).

(Published as: D. Bertrand, *Theta functions and transcendence*, International Symposium on Number
Theory (Madras, 1996), Ramanujan J. **1** (1997), no. 4, 339-350 — this bibliographic form is taken
from Waldschmidt's AWS Lecture 5 bibliography, p. 131, and is **not independently verified against
Crossref/zbMATH in this pass**; it is outside this cluster's MUST list. Verify before printing.)

Note this is a direct hit on the seed note's (T1): (C4E faible) says `π²` and `(log α₁)(log α₂)`
are `Q`-linearly independent for positive real algebraic `α_i ≠ 1`. With `α₁ = p`, `α₂ = q` that is
exactly `log p · log q ∉ π²·Q = 4π²·Q`. The note's §7 is right that (T1) is an instance of a
four-exponentials-type conjecture, and the sharp statement is Bertrand's weak form, not 4EC itself.

## 5.7 Verdict and citation

**REFUTED.** The action must not be executed as written.

If, after the note is reframed, an AWS citation is still wanted, this is the correct string
(fields verified against the document's own title page and the AWS 2008 school page):

```
M. Waldschmidt, *An introduction to irrationality and transcendence methods*, Lecture 5:
"Conjectures and open problems", 2008 Arizona Winter School ("Special Functions and
Transcendence"), Tucson, March 15-19, 2008; notes dated 26 February 2008, available at
https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/AWSLecture5.pdf
(Four Exponentials Conjecture = Conjecture 5.11; Strong Four Exponentials Conjecture =
Conjecture 5.8. Conjectures 5.34 and 5.35 are D. Bertrand's conjectures on the modular
function J and are NOT four-exponentials statements.)
```

And, for the weak form, verified this session:

```
G. Diaz, *La conjecture des quatre exponentielles et les conjectures de D. Bertrand sur la
fonction modulaire*, J. Théor. Nombres Bordeaux **9** (1997), no. 1, 229-245.
((C4E faible), p. 231, attributed to D. Bertrand, Madras, January 1996.)
```

---

# Summary table

| item | report's claim | verdict | what changed |
|---|---|---|---|
| MUST 5 — BSDGP 1996 | Invent. Math. 124 (1996), 1-3, 1-9; gives `j(E_p)` transcendental hence `End(E_p)=Z` | **CONFIRMED** | accents restored (Barré-Sirieix, François); DOI added; theorem statement and its applicability to `q = p^{-1}` verified and written out |
| MUST 9(a) — Roy 1992 | JNT 41 (1992), 22-47, not fetched | **CORRECTED** | issue no. 1 and DOI added; content verified (strong six exponentials = corollary 2); warning recorded that ODP's "[Ro 1992]" is a *different* Roy 1992 paper |
| MUST 9(b) — Diaz 2007 | JTNB 19 (2007) no. 2, 373-391; Cor. 1(1) freeness fails for real `λ₂` | **CONFIRMED** | nothing wrong; Corollaire 1 quoted in full from the article; Crossref's 2008 date identified as a deposit date and rejected in favor of the cover page's 2007 |
| MUST 10(a) — Waldschmidt ODP Conj. 3.7 | MMJ 4 (2004), 245-305; Conj. 3.7 is the matrix form of 4EC | **CORRECTED** | issue no. 1 + DOI added; Conj. 3.7 is the *exponentials* form, matrix form is the unnumbered restatement below it on p. 269 — cite both |
| MUST 10(b) — AWS Lecture 5, Conj. 5.34/5.35 | 5.34/5.35 = weak 4EC and 4EC | **REFUTED** | 5.34/5.35 are Bertrand's *modular* conjectures. 4EC = Conj. 5.11, strong 4EC = Conj. 5.8, weak 4EC absent from the document. Replacement citations supplied |
