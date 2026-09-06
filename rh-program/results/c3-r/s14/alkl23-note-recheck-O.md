# ADVERSARIAL RE-CHECK of `alkl23-note.tex` / `alkl23-note.pdf`

**Date:** 2026-09-06 (Session 16, direction C3-r). **Rechecker:** O (Opus 5), independent third pass —
I had not seen the note, the writer's file, the reader's file (`alkl23-note-read-O.md`), the repairer's
file (`alkl23-note-REVISION.md`) or `w3-adjudication.md` before doing my own pass. Those four were opened
only at the end, to check that nothing they flagged was left unfixed (§4 of this file).

**What I opened, with what tool.**
`alkl23-note.tex` (source) and `alkl23-note.pdf` (`pdftotext -layout`, plus 150-dpi `pdftoppm` renders of all
three pages). Published paper `novelty/ALKL-2024-topology-conormal-distributions-PUBLISHED-JPDOA-15-47.pdf`
via `novelty/ALKL-2024-published.txt` (form-feed page split; PDF page N = printed page N) and 170-dpi renders
of pp. 17 and 58 where primes, calligraphic K and boldface M matter. arXiv v1
`fetched-r3/r3s-18-…-2304.00798v1-SESSION8-FETCH.pdf`. arXiv **v2** downloaded fresh this pass
(`arxiv.org/pdf/2304.00798v2`, 55 pp.) — no earlier pass in this program had opened it. Memoir v1
`fetched-r3/r3s-17-…-2402.06671v1-SESSION8-FETCH.pdf` and memoir **v2** downloaded fresh
(`arxiv.org/pdf/2402.06671v2`, 176 pp.). Live re-checks: `arxiv.org/abs/2304.00798`,
`arxiv.org/abs/2402.06671`, `api.crossref.org/works/10.1007/s11868-024-00617-y`. Rebuild:
`pdflatex` twice, TeX Live 2026, in a scratch copy.

---

## 0. Count and verdict

**Errors found: 12** — 1 ERROR, 4 SHOULD-FIX, 7 NIT.

The mathematics is sound. I re-derived witnesses (a)–(f), the displayed inequality (1), and every repair of
§4 (Claim 6.46, Prop. 8.8, Cor. 3.5, Remark 3.8, Cors. 6.27/7.22) from scratch in my own notation, and found
no false step, no wrong sign and no wrong exponent. Every witness refutes exactly the statement it is aimed
at, in the exact form that statement has in the published paper (I checked the primes on Cors. 4.5, 6.14,
6.21, 7.13, 7.22 against the v1/v2 text layers and a render of p. 58, because the published text layer drops
them). All 34 statement numbers, equation numbers and page numbers the note cites are right; all three
verbatim quotations are exact, including the paper's own notation `S'^m`; the note's diagnosis of the printed
proof of Prop. 3.2 — that the identity `‖φ(a)‖' = ‖a‖'` at the top of p. 17 is the broken step — is accurate,
and its observation that Claim 6.46 needs `m' < m` rather than the printed `m' > m` is a genuine, correctly
stated slip in the paper. The memoir sentences check out in **both** memoir versions. The closing paragraph's
five factual claims all still hold today (I re-checked arXiv and Crossref live: still v1–v3, still no
correction). The build is warning-free: 0 overfull, 0 underfull, 3 pages, no em-dashes, U.S. English
throughout. The one ERROR is a factual claim about the arXiv version history that is simply false — §§3–4
*were* edited between v1 and v2 — and the renumbering the note attributes to v3 entered at v2. It costs no
mathematics but it is exactly the kind of claim the three addressees can check in thirty seconds. Of the four
SHOULD-FIX items, two are missing hypotheses inside witnesses ((d): `supp g` must be small and inside the
chart; (f): `l ≥ 1`), one is a self-contradiction in the setup of (e) (`m' < m` declared, then `m' = m` used),
and one is an overstatement in §2 about the bundle extension of Cor. 3.6. None of them changes a conclusion;
all four are one-line fixes. **Recommendation: fix the ERROR and the four SHOULD-FIX items, then send.**

---

## 1. Findings

### F1 — ERROR — §1, the parenthetical about the arXiv versions

**Where.** `alkl23-note.tex` line 29 / PDF p. 1, §1: *"(cited by its published numbering and pages;
arXiv:2304.00798v3 has the same numbering, and §§3--4 are unchanged in all arXiv versions)"*.

**What is wrong.** Two things.

1. *"§§3–4 are unchanged in all arXiv versions" is false.* §§3–4 were edited between v1 (3 Apr 2023) and
   v2 (29 Jul 2023). A diff of the `pdftotext -layout` output of v1 and v2 over the whole of §§3–4 (headers
   and page numbers stripped) gives, among others:
   * §3, Remark 3.7: v1 *"could be given like in **Proposition 6.8**"* → v2/v3/published *"like in
     **Proposition 6.10**"*.
   * §3, the paragraph before Prop. 3.1: v1 *"The notation S^m(R^l), S^{±∞}(R^l), etc. is used when U = R^0
     = {0}"* → v2 *"When U = R^0 = {0}, the notation S^m(R^l), S^{±∞}(R^l) and S^{(m)}(R^l) is used, and …"*
     (this is the sentence printed on p. 16 of the published paper).
   * §4.2.2: v1 *"We also have the **Fréchet space** I_c^{(∞)}(M,L) = ∩_s I_c^{(s)}(M,L)"* → v2 *"We also
     have the **LCHS** I_c^{(∞)}(M,L) = …"*. That is a change of a mathematical assertion, not typography.
   * §4.3.3: v1 *"Corollary 4.7 can be extended with"* → v2 *"Corollary 4.7 has extensions for"*.
   * §§4.6–4.7: v1's equations **(4.21)–(4.24)** become v2's **(4.20)–(4.22)**, with the surrounding text
     rewritten ("If φ is a local diffeomorphism, then (4.20) is compatible with the Sobolev and symbol order
     filtrations…"). So even the *equation* numbering of §4 differs between v1 and v2.
   * §4.8 (pseudodifferential operators) is substantially rewritten.
2. *The v3 attribution is off by one version.* v2 already carries the published numbering. In v2 I read
   `Proposition 6.12` (semi-norms (6.42) and (6.43)), `Corollary 6.14`, `Corollary 6.21`, `Corollary 6.27`,
   `Corollary 7.13`, `Corollary 7.15`, `Corollary 7.22`, `Corollary 7.23`, and the equation labels
   (6.41)/(6.42)/(6.43) — i.e. everything the note cites in §§6–7. (It is v1 that is out of step: v1 has
   Prop. 6.10 = semi-norms, Cor. 6.12, Cor. 6.19, Cor. 6.25, Cor. 7.11, Cor. 7.20, and (6.41)/(6.42).) Saying
   only "v3 has the same numbering" is true but leaves the impression that v2 does not, which is wrong.

**Evidence.** arXiv abstract page (fetched 2026-09-06): v1 3 Apr 2023, v2 29 Jul 2023, v3 1 Jun 2024, no v4.
`arxiv.org/pdf/2304.00798v2` downloaded this pass; v1 on disk; published PDF on disk. The v1↔v2 §§3–4 diff and
the v2 statement list are reproducible from the two text layers. (This also corrects
`novelty/adjudication.md` §2 C6 and item A2-02, which state that "the renumbering entered at **v3**"; v2 was
never opened there. That is a program-record item, not a defect of the note — see §4 below.)

**Why it matters.** Nothing mathematical: every statement, equation and page the note actually cites in §§3–4
is verbatim identical in v1, v2, v3 and the published paper (I checked Prop. 3.2 with its full proof, Prop. 3.3,
Cors. 3.4, 3.5, 3.6, Remark 3.8, the bundle paragraph, (3.1)–(3.5), (4.7)–(4.13), Cors. 4.5, 4.7 and Sect.
4.3.3). But the three addressees wrote the paper and know its version history; a checkable claim about it that
is false is the worst possible first impression for a note whose whole authority is that it checked everything.

**Exact fix.** Replace

    (cited by its published numbering and pages; arXiv:2304.00798v3 has the same numbering, and \S\S3--4 are unchanged in all arXiv versions)

by

    (cited by its published numbering and pages; arXiv:2304.00798v2 and v3 already carry that numbering, and every statement, equation and page cited below from \S\S3--4 is unchanged in all three arXiv versions)

---

### F2 — SHOULD-FIX — witness (d): `g` needs a support hypothesis, twice over

**Where.** `alkl23-note.tex` line 47 / PDF p. 2, witness (d): *"Let $g\in C_c^\infty(\R^{n''})$,
$g\not\equiv0$"*, and line 51: *"For large $j$, $hu_j=0$ and $f_iu_j=0$ ($i\ge2$)"*.

**What is wrong.** `u_j(x',x'') = j^{n'+m̄'} g(x'') ψ_*(jx')` is supported in
`{|x'| < 1/j} × supp g`. The support shrinks **only in `x'`**; in `x''` it is the fixed set `supp g`. Two
consequences:

* `u_j` is not a function on `M` at all unless `supp g ⊂ U''` (the `x''`-range of the chart `U_1`). The note
  writes `g ∈ C_c^∞(R^{n''})`, which does not say that. (The earlier reader's derivation wrote
  `g ∈ C_c^∞(U'')`; the note is weaker than the derivation behind it.)
* More seriously, *"for large `j`, `hu_j = 0` and `f_iu_j = 0` (`i ≥ 2`)" is false as stated.* Those functions
  vanish only on a neighborhood of `p_0`, i.e. on `{ρ = 1}` for the cut-off `ρ ∈ C_c^∞(U_1)` the note itself
  introduces. For `hu_j = 0` one needs `{0} × supp g ⊂ {ρ = 1}`, and no shrinking in `j` supplies that,
  because `supp g` does not move. With a `g` whose support is larger than the `x''`-slice of `{ρ = 1}`,
  `hu_j ≠ 0` for every `j`, and the two-term computation of the (4.10)-image of `u_j` collapses.

**Evidence.** Published p. 22, (4.10) and the partition of unity `{h, f_j}` subordinate to `{M\L, U_j}`;
published p. 19 for the adapted chart `x = (x', x'')`, `x' ∈ U' ⊂ R^{n'}`, `x'' ∈ U'' ⊂ R^{n''}`,
`L_0 = {x' = 0}`. The note's own replacement family `{(1-ρ)h, ρ+(1-ρ)f_1, (1-ρ)f_i}` equals `{0, 1, 0, …}`
exactly on `{ρ = 1}`, which is a *fixed* neighborhood of `p_0`.

**Why the conclusion is nevertheless safe.** Choose `δ > 0` with `ρ = 1` on `{|x'| < δ} × {|x''| < δ}` and
require `supp g ⊂ {|x''| < δ}`; then `supp u_j ⊂ {ρ = 1}` for `j > 1/δ` and everything the note says goes
through unchanged (I re-derived the symbol, the seminorms, both limits, and the transfer to Cor. 6.21 under
this hypothesis — §3 below).

**Exact fix.** Replace

    Let $g\in C_c^\infty(\R^{n''})$, $g\not\equiv0$;

by

    Let $g\in C_c^\infty(U'')$, $g\not\equiv0$, with $\{0\}\times\supp g$ inside $\{\rho=1\}$;

(and, if `U''` is not introduced by name, "`with supp g inside the x''-slice of {ρ=1}`").

---

### F3 — SHOULD-FIX — witness (e): the setup declares `m' < m` and the argument then uses `m' = m`

**Where.** `alkl23-note.tex` line 58 / PDF p. 2, witness (e): *"…$g\in C_c^\infty$ in $y$ with $g(y_0)=1$,
**$m'<m$**, and $u_j=j^{-m'}\chi(jx)g(y)$"*, then eleven lines later *"So (**with $m'=m$**) $u_j\to0$ in the
topology of (6.42) and (6.43) on $A^m(M)$ but not in $A^m(M)$"*.

**What is wrong.** A flat self-contradiction on the page. The family `u_j = j^{-m'}χ(jx)g(y)` depends on a
real parameter `m'` and nothing in the computation needs `m' < m`: the seminorm bound
`sup_{M̊} x^{-m'}|u_j| ≥ 1` holds for every `m' ∈ R`. The note then legitimately uses the family twice, once
with `m' = m` (to refute Prop. 6.12) and once with `m' < m` (to refute the first assertion of Cor. 6.14). It
is the *declaration* `m' < m` in the setup that is wrong, not either use.

**Evidence.** Published p. 39, Prop. 6.12 ("The semi-norms (6.42) and (6.43) together describe the topology of
`A^m(M)`" — one order `m`, so the refuting family must live at `m' = m`) and Cor. 6.14 (v1 Cor. 6.12,
v2/v3/published Cor. 6.14: "If `m' < m`, then the topologies of `A^{m'}(M)` and `C^∞(M̊)` coincide on
`A^m(M)`" — two orders, so `m' < m`). Both readings are needed; both are correct; only the shared preamble is
over-restrictive.

**Exact fix.** Replace `$m'<m$, and $u_j=j^{-m'}\chi(jx)g(y)$` by `$m'\in\R$, and $u_j=j^{-m'}\chi(jx)g(y)$`.

---

### F4 — SHOULD-FIX — witness (f) and the §2 clause on Cor. 3.6 omit `l ≥ 1`

**Where.** `alkl23-note.tex` line 60 / PDF p. 2, witness (f): *"Let $U\subset\R^n$ be open and nonempty,
$n\ge1$"*; and line 32 / PDF p. 1, §2: *"the acyclicity and bounded-retractivity clauses of Cor.~3.6 (p.~18)
for every non-compact $U$"*.

**What is wrong.** The paper's `l` runs over `N_0` ("The canonical coordinates of `R^n × R^l` (`n, l ∈ N_0`)",
published p. 15), so `l = 0` is inside the scope of Cor. 3.6. For `l = 0` every seminorm (3.1) reduces to
`sup_K |∂^α a|` — the weight `(1+|ξ|)^{m-|β|}` is `1` — so `S^m(U × R^0) = C^∞(U)` **for every `m`**,
`S^∞(U × R^0) = C^∞(U)` is a Fréchet space, and Cor. 3.6 is true (a constant spectrum is acyclic; `C^∞(U)` is
Montel). The witness of (f) degenerates at the same point: `b_j(x,ξ) = χ_j(x)(1+|ξ|²)^{j/2} = χ_j(x)` lies in
every `S^m`, so "`b_j ∈ S^j \ S^m (m < j)`" fails and `{b_j}` *is* contained in a step. Witness (a) states
"every `l ≥ 1`" correctly; (f) and the §2 clause do not.

**Evidence.** Published p. 15 (definition of (3.1) and of `S^m(U × R^l)`, `n, l ∈ N_0`), p. 16 (`S^∞`), p. 18
(Cor. 3.6, stated for `S^∞(U × R^l)` with no restriction on `l`).

**Exact fix.** In (f), replace `Let $U\subset\R^n$ be open and nonempty, $n\ge1$.` by
`Let $U\subset\R^n$ be open and nonempty, $n\ge1$, and let $l\ge1$.` In §2, replace
`for every non-compact $U$` by `for every non-compact $U$ and every $l\ge1$`.

---

### F5 — SHOULD-FIX — §2 overstates the failure of the p. 18 bundle sentence for Cor. 3.6

**Where.** `alkl23-note.tex` line 32 / PDF p. 1, §2: *"…together with the part of the sentence on p.~18 that
extends Prop.~3.2 and Cors.~3.4 and~3.6 to symbols on a vector bundle (the extensions of Prop.~3.3 and
Cor.~3.5 are unaffected)"*.

**What is wrong.** As written, the bundle extension of **Cor. 3.6** is declared false without qualification.
It is not. The note's own §3(f) restricts the claim correctly — *"The same applies to the extension on p. 18
for bundles over a **non-compact** manifold"* — and the note's own §4 **proves** the bundle version of the
Cor. 3.6 acyclicity clause over a *compact* base (that is precisely what "Cor. 3.6 (compact base, e.g.
`S^∞(R^l)`)" in the last sentence of the first §4 paragraph is doing). The extensions of Prop. 3.2 and
Cor. 3.4, by contrast, *are* false over any base, compact or not, since witness (a) is local and lives in one
trivializing chart. So the clause needs splitting, exactly as §2 already splits `Cor. 3.6` from `Prop. 3.2`
and `Cor. 3.4` in the `U` case.

**Evidence.** Published p. 18: *"We can similarly define the norms (3.4) and (3.5) on `S^m(E)`, and
Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting."* Note §3(f),
last-but-one sentence. Note §4, first paragraph, last sentence.

**Exact fix.** Replace

    together with the part of the sentence on p.~18 that extends Prop.~3.2 and Cors.~3.4 and~3.6 to symbols on a vector bundle (the extensions of Prop.~3.3 and Cor.~3.5 are unaffected)

by

    together with the part of the sentence on p.~18 that extends Prop.~3.2 and Cor.~3.4 to symbols on a vector bundle, and its extension of Cor.~3.6 when the base manifold is non-compact (the extensions of Prop.~3.3 and Cor.~3.5 are unaffected, and the extension of Cor.~3.6 over a compact base is true --- \S4)

---

### F6 — SHOULD-FIX — §4: "Two printed arguments" undercounts, on the evidence of the same paragraph

**Where.** `alkl23-note.tex` line 69 / PDF p. 3, second paragraph of §4, first sentence: *"Two printed
arguments use a coincidence statement for more than the word ``acyclic''."*

**What is wrong.** The very paragraph that opens with "Two" then repairs **four**: Claim 6.46, Prop. 8.8,
Cor. 3.5 (*"follows directly"* — its printed proof on p. 17 is *"The first assertion is given by
Corollary 3.4 and the density of `C_c^∞(U × R^l)` in `C^∞(U × R^l)`"*, i.e. a use of the false Cor. 3.4 for
more than acyclicity), and Remark 3.8 (*"without the sequential retractivity of `S^∞(U × R^l)`, which is what
its printed argument uses"*). Two further printed arguments of the same kind are not mentioned at all:
**Cor. 6.15** and **Cor. 7.14**, the density statements, whose proofs are the analogues of Cor. 3.5's — p. 39,
*"The proofs of the following results are similar to the proofs of Propositions 3.2 and 3.3, Corollaries 3.4
to 3.6, using (6.33)"*, which covers Cor. 6.15, and p. 56, *"Moreover the following analogs of Proposition 6.6
and Corollaries 6.7 and 6.14 to 6.16 hold true"*, which covers Cor. 7.14. Both survive by the paper's own
alternative routes (Remark 6.17 / Prop. 6.10 for Cor. 6.15; Cor. 7.17 for Cor. 7.14), so the omission costs
the note nothing mathematically — but a reader who checks will find the count wrong and the two density
corollaries unaccounted for.

**Evidence.** Published pp. 17 (Cor. 3.5's proof), 18 (Remark 3.8), 39 (Cor. 6.15, Remark 6.17), 47
(Cor. 6.39, Remark 6.41), 48–49 (Claim 6.46), 56 (Cor. 7.14), 57 (Cor. 7.17), 64 (Prop. 8.8).

**Exact fix.** Replace `Two printed arguments use a coincidence statement for more than the word ``acyclic''.`
by

    Several printed arguments use a coincidence statement for more than the word ``acyclic''.

and, after `Cor.~7.13 is not needed there.`, insert

    (The density Cors.~6.15 and 7.14, whose proofs are the analogues of Cor.~3.5's, follow instead from Prop.~6.10 and Cor.~7.17, as Remarks~6.17 and 6.41 already note.)

---

### F7 — NIT — §4: `\chi` is undefined here and collides with the `\chi` of witness (e)

**Where.** `alkl23-note.tex` line 69 / PDF p. 3: *"Cor.~3.5 follows directly: for $a\in S^m$ and $m<m'$,
$\|a-\chi(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}$"*.

**What is wrong.** `χ` is never introduced in §4; the reader must guess "a cut-off equal to 1 near 0". The
same letter was fixed in witness (e) as `χ ∈ C_c^∞((1/2,2))` with `χ(1) = 1` — a cut-off that is *zero* near
0, so the guess is actively contradicted by the note's own earlier usage. The note already has a suitable
symbol: `ρ ∈ C_c^∞`, `ρ = 1` near 0, introduced in (f).

**Exact fix.** Replace `$\|a-\chi(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}$` by
`$\|a-\rho(\xi/R)a\|_{K,\alpha,\beta,m'}\le CR^{m-m'}$ with the $\rho$ of (f)`.

---

### F8 — NIT — witness (d): `η_0 ≠ 0` is needed for the displayed lower bound

**Where.** `alkl23-note.tex` line 56 / PDF p. 2: *"$\Phi_{0,\bar m'}(j)\ge|\hat\psi_*(\eta_0)|
\min\{(1+|\eta_0|)^{-\bar m'},|\eta_0|^{-\bar m'}\}=c>0$ for any $\eta_0$ with $\hat\psi_*(\eta_0)\ne0$"*.

**What is wrong.** The expression `|η_0|^{-m̄'}` is undefined at `η_0 = 0` when `m̄' > 0` and is `+∞`-valued in
the wrong direction otherwise. When `N_0 ≥ 1` the point `η_0 = 0` is excluded automatically
(`ψ̂_*(η) = (-|η|²)^{N_0} ψ̂(η)` vanishes there), but `N_0 = 0` is allowed by the note's own hypothesis
("`N_0 ∈ N_0` with `2N_0 ≥ m̄''`", satisfied by `N_0 = 0` whenever `m̄'' ≤ 0`), and then `ψ̂_*(0) = ∫ψ` may well
be non-zero.

**Exact fix.** Replace `for any $\eta_0$ with $\hat\psi_*(\eta_0)\ne0$` by
`for any $\eta_0\ne0$ with $\hat\psi_*(\eta_0)\ne0$`.

---

### F9 — NIT — unstated index ranges in (b), (c) and (e)

**Where.** (b): `$b_j=\sum_{i\le j}c_i\theta(\xi-iRe_1)$` (lower limit of `i` never given); (e):
`$\tfrac12\inf_ie^ii^{-k}$` (range of `i` never given, and the expression is `0` if `i = 0` is admitted, since
`e^0·0^{-k}` is undefined / the infimum over `i ≥ 0` of `e^i i^{-k}` is not positive).

**What is wrong.** In (c) the corresponding quantity is correctly written `$\varepsilon_k=\tfrac12\inf_{j\ge1}
e^j(1+j)^{-k}$` — bounded below by a positive number because `e^j(1+j)^{-k} → ∞` and every term is positive.
In (e) the same device is written `$\inf_i e^i i^{-k}$`, which needs `i ≥ 1` to be defined and positive. In
(b) the sum's lower limit is immaterial to the conclusion but should be visible.

**Exact fix.** In (e) write `$\tfrac12\inf_{i\ge1}e^ii^{-k}$`; in (b) write `$b_j=\sum_{1\le i\le j}c_i
\theta(\xi-iRe_1)$` (or `$\sum_{i=1}^{j}$`).

---

### F10 — NIT — §2: the "constant in the base variable" sentence is untrue of witness (f)

**Where.** `alkl23-note.tex` line 32 / PDF p. 1, last sentence of §2: *"The witnesses below are constant in
the base variable up to a fixed cut-off, so they also refute every parametrized or bundle version."*

**What is wrong.** True of (a), (b), (c) (literally constant in `x`) and of (d), (e) (a fixed bump `g` in the
base variable). **False of (f)**, whose witness is `b_j(x,ξ) = χ_j(x)(1+|ξ|²)^{j/2}` with a cut-off `χ_j` that
*moves with `j`* — and must, since the whole point of (f) is that the supports escape every compact subset of
`U`. The sentence's conclusion for (f) is separately and correctly made at the end of (f) ("The same applies
to the extension on p. 18 for bundles over a non-compact manifold").

**Exact fix.** Replace `The witnesses below are constant in the base variable up to a fixed cut-off` by
`The witnesses (a)--(e) below are constant in the base variable up to a fixed cut-off`.

---

### F11 — NIT — §2: `codim L ≥ 1` should also say `L ≠ ∅`

**Where.** `alkl23-note.tex` line 32 / PDF p. 1: *"Cor.~4.5 (p.~23), for every compact $(M,L)$ with
$\operatorname{codim}L\ge1$"*.

**What is wrong.** Witness (d) begins "Take `p_0 ∈ L`". For `L = ∅` one has `I(M,∅) = C^∞(M)` and Cor. 4.5 is
vacuously true, so the universal claim needs `L ≠ ∅`. (`codim ∅` is conventionally undefined, so this is a
pedantic point, but the note is making a universal falsity claim.)

**Exact fix.** `for every compact $(M,L)$ with $L\ne\emptyset$ and $\operatorname{codim}L\ge1$`.

---

### F12 — NIT — reference [2] cites a superseded arXiv version; and two presentation points

**(a) Memoir version.** `arXiv:2402.06671` has **two** versions: v1 (7 Feb 2024) and v2 (13 Feb 2024). The
note cites v1. I downloaded v2 and checked all three citations: §2.1.8 is on printed p. 15 (PDF p. 21) with
the same text, including *"The following properties hold [ÁLKL23, Corollaries 3.4–3.6 and Remark 3.8]"*;
§5.2.1 is on printed p. 119 (PDF p. 125); §§5.5.3–5.5.4 are both on printed p. 122 (PDF p. 128);
`I(F) = I_Λ^•(F) := I(M, M^0; ΛF)` is unchanged. So **nothing breaks** — but citing the superseded version
without saying so is a small blemish in a note whose §1 makes a point of version hygiene.
*Fix:* `arXiv:2402.06671 (v2, 13 February 2024; the pages cited are the same in v1)`.

**(b) Date of the erratum search.** §5 opens *"As of September 3, 2026"* in a note dated **September 5, 2026**.
I re-ran the two decisive checks live on 2026-09-06: `arxiv.org/abs/2304.00798` still lists v1, v2, v3 only,
and the Crossref record of `10.1007/s11868-024-00617-y` still has an empty `relation` with no `update-to` /
`updated-by`. The sentence is therefore still true; only the date is stale.
*Fix:* update to the note's own date on the day it is sent.

**(c) Mixed reference styles.** The note writes `Sect. 4.3.3, p. 23` for a subsection of [1] but
`[2, §2.1.8, p. 15]` for a subsection of [2], while `§2`–`§5` refer to the note's own sections. Harmless;
worth one pass for uniformity if the note is re-edited for any of the above.

---

## 2. Citation table

Every number and page the note cites, against the **published** PDF (`ALKL-2024-published.txt`, PDF page N =
printed page N; primes and accents confirmed on a 170-dpi render where the text layer drops them, and against
the v1/v2 text layers, which keep them).

| # | The note cites | Where I found it | Verdict |
|---|---|---|---|
| 1 | Prop. 3.2, p. 16 | statement on p. 16 (proof runs to p. 17): "The semi-norms (3.4) and (3.5) together describe the topology of `S^m(U×R^l)`" | **OK** |
| 2 | Cor. 3.4, both assertions, p. 17 | p. 17: "For `m<m'`, the topologies of `S^{m'}(U×R^l)` and `C^∞(U×R^l)` coincide on `S^m(U×R^l)`. Therefore the topologies of `S^∞…` and `C^∞…` coincide on `S^m…`" | **OK** |
| 3 | Cor. 3.6, p. 18 | p. 18: "`S^∞(U×R^l)` is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive" | **OK** |
| 4 | the p. 18 sentence extending Prop. 3.2, Prop. 3.3, Cors. 3.4–3.6 to bundles | p. 18: "We can similarly define the norms (3.4) and (3.5) on `S^m(E)`, and Propositions 3.2 and 3.3 and Corollaries 3.4 to 3.6 can be directly extended to this setting." | **OK** (scope overstated — F5) |
| 5 | Prop. 3.3 and Cor. 3.5 "unaffected" | Prop. 3.3 p. 17 (true; I re-derived it), Cor. 3.5 p. 17 (true; §4 of the note re-proves it) | **OK** |
| 6 | Cor. 4.5, p. 23 | p. 23: "For `m < m', m''`, the topologies of `I^{m'}(M,L)` and `I^{m''}(M,L)` coincide on `I^m(M,L)`" (primes confirmed in v1 line 1071 and v2 line 1040); proof "Use Corollary 3.4 and the TVS-embeddings (4.10)" | **OK** |
| 7 | Prop. 6.12, p. 39 | p. 39: "The semi-norms (6.42) and (6.43) together describe the topology of `A^m(M)`" | **OK** |
| 8 | Cor. 6.14, both assertions, p. 39 | p. 39: "If `m' < m`, then the topologies of `A^{m'}(M)` and `C^∞(M̊)` coincide on `A^m(M)`. Therefore the topologies of `A(M)` and `C^∞(M̊)` coincide on `A^m(M)`" | **OK** |
| 9 | Cor. 6.21, p. 40 | p. 40: "For `m < m', m''`, the topologies of `Ȧ^{m'}(M)` and `Ȧ^{m''}(M)` coincide on `Ȧ^m(M)`"; preceded by "The following is a consequence of Corollary 4.5 applied to `(M̆, ∂M)`" | **OK** |
| 10 | Cor. 7.13, both assertions, p. 56 | p. 56: "If `m' < m`, then the topologies of `J^{m'}(M,L)` and `C^∞(M\L)` coincide on `J^m(M,L)`. Therefore the topologies of `J(M,L)` and `C^∞(M\L)` coincide on `J^m(M,L)`" | **OK** |
| 11 | Cor. 6.27, p. 41 | p. 41: "For `m < m', m''`, the topologies of `𝒦^{m'}(M)` and `𝒦^{m''}(M)` coincide on `𝒦^m(M)`"; preceded by "the following analogs of Corollaries 6.21 and 6.22 hold true with formally the same proofs, using Corollaries 6.21, 6.22 and 6.26" | **OK** (and the note's "printed proofs pass through Cor. 6.21" is exact) |
| 12 | Cor. 7.22, p. 58 | p. 58 (render): "For `m < m', m''`, the topologies of `K^{m'}(M,L)` and `K^{m''}(M,L)` coincide on `K^m(M,L)`"; preceded by "Thus we get the following consequences of Propositions 6.24 and 6.25 and Corollaries 6.26 to 6.28" | **OK** |
| 13 | seminorms (3.1) | p. 15, display (3.1) | **OK** |
| 14 | seminorms (3.4) `‖·‖_{Q,C^k}` | p. 16, display (3.4), "continuous semi-norms … on `S^∞(U×R^l)`" | **OK** |
| 15 | seminorms (3.5) `‖·‖'_{K,α,β,m}` | p. 16, display (3.5), "consider also the continuous semi-norms … on `S^m(U×R^l)`" | **OK** ("every (3.4) and (3.5) seminorm is continuous on `S^m`" is the paper's own word) |
| 16 | quotation: "Hence `S'^m(U×R^l)` is complete" (p. 17) | p. 17, render: verbatim, and `S'^m` is the **paper's own** notation (`S'^m` metrizable, `Ŝ'^m` its completion) | **OK — verbatim** |
| 17 | quotation: "`‖φ(a)‖'_{K,α,β,m} = ‖a‖'_{K,α,β,m} < ∞`" at the **top** of p. 17 | p. 17, render, second line of the page: "since `‖φ(a)‖'_{K,α,β,m} = ‖a‖'_{K,α,β,m} < ∞`, there are `C, R > 0` so that…" | **OK — verbatim, and "top of p. 17" is literally right** |
| 18 | (4.8) (partial Fourier transform giving the symbol) | p. 21, (4.8) `C_c^∞(U) → C^∞(N^*U'')`, `a(x'',ξ) = ∫ e^{-i⟨x',ξ⟩} u(x',x'') dx'` | **OK** |
| 19 | (4.9) `m̄ = m + n/4 − n'/2` | p. 22, display (4.9) | **OK** |
| 20 | (4.10) and its partition of unity `{h, f_j}` | p. 22: "{h, f_j} … subordinated to the open covering {M\L, U_j}", and (4.10) "the following map is required to be a TVS-embedding" | **OK** (index renamed to `f_i` in (d) deliberately) |
| 21 | `n' = codim L`, `n'' = dim L` | p. 19: "`L` is a regular submanifold of `M` of codimension `n'` and dimension `n''`", `x = (x', x'')`, `L_0 = {x' = 0}` | **OK** |
| 22 | (6.47) `Ȧ^m(M) = I^m_M(M̆, ∂M)` | p. 40, display (6.47), "which are closed subspaces" | **OK** |
| 23 | (6.41) with `P = 1`; "the topology of `A^m(M)` is the projective one over all `P ∈ Diff_b(M)`, p. 38" | p. 38: "with the projective topology given by the maps `P : A^m(M) → x^m L^∞(M)` (`P ∈ Diff_b(M)`)", and (6.41) `‖u‖_{k,m} = sup_{M̊} x^{-m}|P_k u|` | **OK** |
| 24 | (6.42), (6.43) | p. 39, displays (6.42) `sup_K |P_k u|` and (6.43) `lim_{ε↓0} sup_{0<x<ε} x^{-m}|P_k u|` | **OK** |
| 25 | (7.27) with `Diff(M,L)` and `x^m L^∞(M)` | p. 56, second line of (7.27): `J^m(M,L) = { u ∈ C^{-∞}(M,L) | Diff(M,L) u ⊂ x^m L^∞(M) }` | **OK** |
| 26 | (7.26), `J^m(M,L) ≅ A^m(**M**)`, `**M**` = `M` cut along `L` | p. 56 (render): `π^* : A(**M**) →≅ J(M,L)` in **boldface M**, and "We also get spaces `J^{(s)}(M,L)` and `J^m(M,L)` … corresponding to `A^{(s)}(**M**)` and `A^m(**M**)` via (7.26)"; p. 50: "Let `**M**` be the smooth manifold with boundary defined by 'cutting' `M` along `L`" | **OK** (the note's `\boldsymbol M` matches the paper's own glyph) |
| 27 | `Ȧ^m(M)`, `𝒦^m(M)`, `K^m(M,L)` closed subspaces of `I^m(M̆,∂M)`, `Ȧ^m(M)`, `I^m(M,L)` — "(6.47), pp. 41, 58" | (6.47) p. 40 for `Ȧ^m`; p. 41 "These are closed subspaces of `Ȧ^{(s)}(M)`, `Ȧ^m(M)` and `Ȧ(M)`"; p. 58 "These are closed subspaces of `I^{(s)}(M,L)`, `I_L^m(M,L)` and `I(M,L)`" | **OK** — note the paper's own p. 58 misprint `I_L^m` for `I^m`; the note states the intended fact and is right not to belabor it |
| 28 | (6.33) and the local form of `Diff_b(M)` | p. 56 quotes (6.33) as giving `J(M,L) ⊂ C^∞(M\L)`; p. 38 uses (6.33) for `sup_{M̊}` in (6.41) — i.e. (6.33) is the inclusion `A(M) ⊂ C^∞(M̊)` | **OK** |
| 29 | (6.49), "Cor. 6.27 is the case `(M̆, ∂M)`" | p. 41, (6.49) `𝒦(M) ≡ I_{∂M}(M̆,∂M)`, "which restricts to identities between the spaces defining the Sobolev and symbol order filtrations" — and `K(M̃,L̃) := I_{L̃}(M̃,L̃)` on p. 58 | **OK** |
| 30 | Prop. 7.26 (Dirac-layer description of `K(M,L)`) | p. 59, Prop. 7.26: (7.36) `⊕_{m≥0} C^1_m →≅ K(M,L)`, `C^1_m = C^∞(L; Ω^{-1}NL)`, with (7.37) for `K^{(s)}` | **OK** |
| 31 | Prop. 6.29 (`E_m : A^m(M) → Ȧ^{(s)}(M)`) | p. 42, Prop. 6.29 | **OK** — and the note's parenthetical "domain is `A^{m'}(M) ⊃ A^m(M)`, so `m' < m` rather than `m' > m` is the index needed" is **right**: (6.38) p. 38 gives `A^m ⊂ A^{m'}` for `m' < m`, so the printed "For any `m' > m`" on p. 48 cannot feed `E_{m'}` with `A ⊂ A^m` |
| 32 | Claim 6.46, pp. 48–49, and the quoted sentence | Claim 6.46 stated p. 48, proof pp. 48–49; the sentence spans the page break: p. 48 ends "By Corollary 6.14," and p. 49 begins "there is some 0-neighborhood `V ⊂ A(M)` such that `V ∩ A^m(M) = W ∩ A^m(M)`" | **OK — verbatim; "pp. 48–49" is the right span** |
| 33 | Prop. 8.8, p. 64; repaired with Cor. 7.31; Cor. 7.13 "not needed there" | p. 64, Prop. 8.8, preceded by "The following analog of Proposition 6.45 holds true with formally the same proof, using Proposition 7.29 and Corollaries 7.13, 7.15 and 7.31"; Cor. 7.31 (partial extension maps for `J`) p. 61 | **OK** — the paper does invoke Cor. 7.13 there, and the note's claim is that the repaired argument does not need it, which is right |
| 34 | Cor. 3.6 "(compact base, e.g. `S^∞(R^l)`)", 4.7, 6.16, 6.22, 6.28, 7.15, 7.23 | Cor. 4.7 p. 23; Cor. 6.16 p. 39; Cor. 6.22 p. 40; Cor. 6.28 p. 41; Cor. 7.15 p. 57; Cor. 7.23 p. 58 — each "is an acyclic Montel space, and therefore complete, boundedly retractive and reflexive" | **OK** |
| 35 | Remark 3.8, p. 18, and "its printed argument uses sequential retractivity" | p. 18, Remark 3.8: "…since `S^∞(U×R^l)` is sequentially retractive (Corollary 3.6), all `a_m` would lie in some step `S^{m_0}(U×R^l)`, a contradiction" | **OK — the description of the printed argument is exact** |
| 36 | Wengenroth criterion "quoted on p. 4" ([3, Thm. 6.1]) | p. 4: "the condition of being acyclic can be described as follows [39, Theorem 6.1]: for all `k`, there is some `k' ≥ k` such that, for all `k'' ≥ k'`, the topologies of `X_{k'}` and `X_{k''}` coincide on some 0-neighborhood of `X_k`" | **OK** |
| 37 | [3, Cor. 6.5] "as quoted on p. 5"; the pp. 4–5 consequences; the p. 5 compact-spectrum remark | p. 5: "acyclic LF-spaces are complete and regular [39, Corollary 6.5]"; "If the steps `X_k` are Fréchet spaces … `X` is acyclic if and only if it is boundedly/compactly/sequentially retractive [39, Proposition 6.4]"; "It is said that `(X_k)` is compact if the inclusion maps are compact operators. In this case, `(X_k)` is clearly acyclic … [18, Theorem 6']" | **OK** — and p. 4's definition of *regular* / *boundedly retractive* supports (f)'s "not regular, hence not boundedly retractive … not acyclic" |
| 38 | "Sect. 4.3.3, p. 23, excepts acyclicity for non-compact `M`" | p. 23, Sect. 4.3.3, last sentence: "Corollary 4.7 has extensions for `∪_m I^m(M,L)` and `I_{·/c}(M,L)`, except acyclicity in the case of `I(M,L)`" | **OK** |
| 39 | [2, §2.1.8, p. 15] "restates Cors. 3.4–3.6 for arbitrary open `U ⊂ R^n`" | memoir v1 **and** v2, printed p. 15 (PDF p. 21), §2.1.8: "For any open `U ⊂ R^n` and `l ∈ N_0` …" then "The following properties hold [ÁLKL23, **Corollaries 3.4–3.6 and Remark 3.8**]: The topologies of `S^∞(U×R^l)` and `C^∞(U×R^l)` coincide on `S^m(U×R^l)`, however the second inclusion of (2.1.27) is not a TVS-embedding; `C_c^∞(U×R^l)` is dense in `S^∞(U×R^l)`; and `S^∞(U×R^l)` is an acyclic Montel space, and therefore complete, boundedly/compactly/sequentially retractive and reflexive." | **OK** (the memoir also restates Remark 3.8, which the note handles separately in §4) |
| 40 | [2] `I(F) = I(M, M^0; ΛF)`; §5.2.1 p. 119; §§5.5.3–5.5.4 p. 122; "concern a closed `M`" | memoir v1 and v2: "`I(F) = I_Λ^•(F) := I(M, M^0; ΛF)`" (Ch. 5 opening); §5.2.1 printed p. 119 "because `I(F)` is compactly retractive (Section 2.2.2)"; §5.5.3 printed p. 122 "Using that `J(F)` is compactly retractive (Section 2.6.7)"; §5.5.4 printed p. 122 "Since `I(F)` is compactly retractive"; Ch. 5 opening: "Let `F` be a transversely orientable smooth foliation of codimension one on a **closed** manifold `M`". These are the **only** three uses of compact retractivity in the memoir (`grep`: lines 6933, 7109, 7129, plus the Ch. 2 definition and the index) | **OK** |
| 41 | §5: arXiv v1–v3 only, no v4 | `arxiv.org/abs/2304.00798`, fetched 2026-09-06: v1 3 Apr 2023, v2 29 Jul 2023, v3 1 Jun 2024. No v4 | **OK, still true today** |
| 42 | §5: Crossref record carries no correction | `api.crossref.org/works/10.1007/s11868-024-00617-y`, fetched 2026-09-06: `relation` empty, no `update-to`, no `updated-by` | **OK, still true today** |
| 43 | §5: zbMATH 7901419 no review or corrigendum; Semantic Scholar no citing work; Unpaywall no correction DOI | `novelty/adjudication.md` §2 C6 and item A2-03 (2026-09-03): "zbMATH 7901419 no corrigendum … Semantic Scholar 0 citers, Unpaywall no correction DOI, zbMATH reviewer null" | **OK** (not independently re-fetched this pass — §4 below) |
| 44 | Bibliography [1]: JPDOA 15 (2024), art. 47, 68 pp., DOI 10.1007/s11868-024-00617-y; arXiv v3, 1 June 2024 | published p. 1 header "J. Pseudo-Differ. Oper. Appl. (2024) 15:47", DOI on p. 1, running head "Page N of 68"; arXiv abstract page: v3 = 1 Jun 2024 | **OK** |
| 45 | Bibliography [2]: arXiv:2402.06671 (v1, 7 February 2024) | arXiv abstract page: v1 = 7 Feb 2024 | **OK but superseded** (v2 = 13 Feb 2024 — F12a) |
| 46 | Bibliography [3]: Wengenroth, *Derived Functors in Functional Analysis*, LNM 1810, Springer, Berlin (2003) | published bibliography, ref. **[39]**: "Wengenroth, J.: Derived Functors in Functional Analysis. Lecture Notes in Mathematics, vol. 1810. Springer, Berlin (2003)" | **OK — identical** |
| 47 | Notation `𝒦` (calligraphic) for `K(M)` vs `K` for `K(M,L)` | published p. 58 (render): (7.32) `𝒦(**M**) ≡ K(M,L) ⊕ K(M,L)`, and "`𝒦^{(s)}(**M**)` and `𝒦^m(**M**)`" | **OK — the note follows the paper's own convention** |
| 48 | Version claim: "arXiv v3 has the same numbering; §§3–4 unchanged in all arXiv versions" | v2 also has the published numbering; §§3–4 **were** edited between v1 and v2 | **MISMATCH — F1** |

**Statement numbers, spot-checked in arXiv v1 as the brief requires (three or more).** Prop. 3.2 (v1 line 785,
statement *and* full proof word-for-word identical to published p. 16–17, including "since
`‖φ(a)‖'_{K,α,β,m} = ‖a‖'_{K,α,β,m} < ∞`" and "Hence `S'^m(U×R^l)` is complete"); Cor. 3.4 (v1 line 820,
identical); Cor. 4.5 (v1 line 1071, identical, primes visible). Also checked and identical: Prop. 3.3,
Cor. 3.5, Cor. 3.6 with its proof, Remark 3.8, the bundle paragraph, Cor. 4.7. The §6–§7 numbers do **not**
carry over to v1 (v1 Cor. 6.12 = published 6.14, v1 Cor. 6.19 = published 6.21, v1 Cor. 7.11 = published 7.13,
v1 Cor. 7.20 = published 7.22, v1 (6.41)/(6.42) = published (6.42)/(6.43)) — which is exactly why the note
restricts its "unchanged" claim to §§3–4, and exactly why that restricted claim must also be stated correctly
(F1).

---

## 3. My re-derivations, in brief

Throughout, `‖a‖_{K,α,β,m} = sup_{x∈K, ξ} |∂_x^α ∂_ξ^β a(x,ξ)| (1+|ξ|)^{|β|-m}` (3.1) and
`‖a‖'_{K,α,β,m} = sup_{x∈K} limsup_{|ξ|→∞} |∂_x^α ∂_ξ^β a| / |ξ|^{m-|β|}` (3.5). I worked each item without
looking at the note's justification first, then compared.

**(a) — CORRECT.** `g_N(x,ξ) = θ(ξ − Ne_1)`, `θ ∈ C_c^∞(R^l)`, `θ(0)=1`, `supp θ ⊂ B(0,r)`. Compact `ξ`-support
gives `g_N ∈ S^{-∞}` and kills every (3.5) seminorm for every `N`. Any compact `Q ⊂ U × R^l` sits in
`K × B̄(0,ρ)`; `supp g_N ⊂ {|ξ| > N − r}`, so `‖g_N‖_{Q,C^k} = 0` once `N > ρ + r` — hence `g_N → 0` in the
(3.4)+(3.5) topology and in `C^∞`. For the lower bound, substitute `η = ξ − Ne_1`:
`‖g_N‖_{K,0,β,m} = sup_{|η|≤r} |∂^βθ(η)| (1+|η+Ne_1|)^{|β|-m}`. When `|β| > m` the exponent is positive and
`|η+Ne_1| ≥ N − r`, so the sup is `≥ (1+N−r)^{|β|−m} sup|∂^βθ| → ∞`. Such `β` exist in every order because a
nonzero compactly supported function is not a polynomial. So `(g_N)` is unbounded in `S^m`, a fortiori not
convergent there: the (3.4)+(3.5) topology is strictly coarser (Prop. 3.2 false), and with `|β| > m'` the same
family is in `S^m`, `→ 0` in `C^∞`, `↛ 0` in `S^{m'}` (first assertion of Cor. 3.4 false). Needs `l ≥ 1`,
which the note states here. **No error.**

**(b) — CORRECT, and the diagnosis of the printed proof is exact.** `R > 2r`, `c_i = (1+iR)^{m+1}`,
`b_j = Σ_{i≤j} c_i θ(ξ − iRe_1)`; the balls `B(iRe_1, r)` are disjoint since `R > 2r`. For `i < j`,
`b_j − b_i` is supported in `{|ξ| ≥ (i+1)R − r}`, so all its (3.5) seminorms vanish and its (3.4) seminorms
over a fixed `Q` vanish once `(i+1)R − r` exceeds the `ξ`-radius of `Q`: `(b_j)` is Cauchy in `S'^m`. Its
`C^∞`-limit `b = Σ_i c_i θ(ξ − iRe_1)` satisfies `|b(x,iRe_1)| (1+iR)^{-m} = (1+iR)^{m+1-m} = 1+iR → ∞`, so
`‖b‖_{K,0,0,m} = ∞`, `b ∉ S^m`. Since the (3.4) seminorms alone generate the `C^∞` topology, any `S'^m`-limit
of `(b_j)` would be its `C^∞`-limit `b`; so `(b_j)` has no limit and `S'^m` is not complete — which is exactly
what p. 17 asserts ("Hence `S'^m(U×R^l)` is complete"). For the class `a` of `(b_j)` in the completion,
`‖a‖'_{K,0,0,m} = lim_j ‖b_j‖'_{K,0,0,m} = 0` (continuous extension of a defining seminorm) while
`φ(a) = b` has `‖b‖'_{K,0,0,m} = limsup |b|/|ξ|^m = ∞` along `ξ = iRe_1`. So the identity
`‖φ(a)‖'_{K,α,β,m} = ‖a‖'_{K,α,β,m}` used at the top of p. 17 fails on this very `a`, which is precisely the
note's claim. **No error.**

**(c) — CORRECT.** `c_j = e^j θ(ξ − je_1) ∈ S^{-∞}`, `c_j → 0` in `C^∞`. With `K = {x_0}`,
`ε_k = ½ inf_{j≥1} e^j(1+j)^{-k} > 0` (each term positive, and `e^j(1+j)^{-k} → ∞`),
`W_k = {a ∈ S^k : ‖a‖_{K,0,0,k} < ε_k}`. The absolutely convex hull `W` of `∪_k W_k` contains each `W_k`, so
`W ∩ S^k` is a 0-neighborhood of `S^k` for every `k`, and an absolutely convex set with that property is a
0-neighborhood of the inductive limit. If `c_j = Σ_i λ_i w_i` with `Σ|λ_i| ≤ 1`, `w_i ∈ W_{k_i}`, then
`|w_i(x_0, je_1)| < ε_{k_i}(1+j)^{k_i} ≤ ½ e^j` by the definition of `ε_k`, whence
`e^j = |c_j(x_0,je_1)| < ½ e^j`. So `c_j ∉ W`, `c_j ↛ 0` in `S^∞`, and the topologies of `S^∞` and `C^∞`
differ on every `S^m` (second assertion of Cor. 3.4 false). No property of `S^∞` is used — the note's
parenthetical is right, and this is what makes (c) usable to repair Remark 3.8. **No error.**

**(d) — CORRECT once `supp g` is constrained (F2).** With `m̄ = m + n/4 − n'/2` and
`u_j = j^{n'+m̄'} g(x'') ψ_*(jx')`, (4.8) and `x' = z/j` give
`a_j(x'',ξ) = j^{n'+m̄'} g(x'') · j^{-n'} ψ̂_*(ξ/j) = j^{m̄'} g(x'') ψ̂_*(ξ/j)` — the `j^{n'}` in the prefactor is
exactly the Jacobian, so the note's exponent is right. Then
`∂_{x''}^α ∂_ξ^β a_j = j^{m̄'-|β|} ∂^α g · (∂^β ψ̂_*)(ξ/j)`, and with `ξ = jη`,
`1+|ξ| = j(1/j + |η|)`, so
`‖a_j‖_{K,α,β,m̄_1} = j^{m̄'-m̄_1} sup_K|∂^α g| · Φ_{β,m̄_1}(j)` with
`Φ_{β,m̄_1}(j) = sup_η |∂^β ψ̂_*(η)| (1/j+|η|)^{|β|-m̄_1}` — the note's display, verified term by term.
`ψ̂_*(η) = (−|η|²)^{N_0} ψ̂(η)` (correct for `â(ξ) = ∫ e^{-i⟨x,ξ⟩}a`), Schwartz, vanishing to order `2N_0` at
`0`, so `∂^β ψ̂_*` vanishes to order `2N_0 − |β|`. For `m̄_1 ≤ 2N_0`: if `|β| ≥ m̄_1` the exponent is `≥ 0` and
`(1/j+|η|)^{|β|-m̄_1} ≤ (1+|η|)^{|β|-m̄_1}`, tamed by Schwartz decay; if `|β| < m̄_1` the exponent is `< 0`, so
`(1/j+|η|)^{|β|-m̄_1} ≤ |η|^{|β|-m̄_1}` and `|∂^βψ̂_*(η)| ≤ C|η|^{2N_0-|β|}` near `0` gives
`≤ C|η|^{2N_0-m̄_1} ≤ C`. Hence `Φ_{β,m̄_1} ≤ C_β` and `‖a_j‖_{K,α,β,m̄''} ≤ C j^{m̄'-m̄''} → 0`:
`u_j → 0` in `I^{m''}(M,L)`. Conversely `Φ_{0,m̄'}(j) ≥ |ψ̂_*(η_0)| (1/j+|η_0|)^{-m̄'} ≥ c > 0` for a fixed
`η_0 ≠ 0` with `ψ̂_*(η_0) ≠ 0` (F8), so `‖a_j‖_{K,0,0,m̄'} = sup_K|g| · Φ_{0,m̄'}(j) ≥ c sup_K|g| > 0` for any
compact `K` meeting `{g ≠ 0}`: `u_j ↛ 0` in `I^{m'}(M,L)`. Since `u_j ∈ C^∞(M) ⊂ I^m(M,L)` (a smooth function's
partial Fourier transform in `x'` is Schwartz in `ξ`, so its symbol is in `S^{-∞}`), Cor. 4.5 fails. The only
gap is the one recorded in F2: for the (4.10)-image to reduce to `(0, a_j, 0, …)` one needs
`supp u_j ⊂ {ρ = 1}` for large `j`, and since `supp u_j ⊂ {|x'| < 1/j} × supp g` does not shrink in `x''`,
`supp g` must be small. The transfer to Cor. 6.21 (`supp ψ ⊂ (½,1)` in the collar of `(M̆, ∂M)`, `n' = 1`) is
correct: `ψ_* = Δ^{N_0}ψ` has the same support as `ψ`, so `u_j` is supported in `{1/(2j) < x < 1/j}`, i.e. in
`C_c^∞(M̊) ⊂ Ȧ^m(M) = I^m_M(M̆, ∂M)`. **No error beyond F2 and F8.**

**(e) — CORRECT once the parameter is freed (F3).** Filtration direction first: (6.38) gives
`A^m(M) ⊂ A^{m'}(M)` for `m' < m` (smaller index = bigger space), the reverse of the symbol convention, and
Cor. 6.14 is stated accordingly. With `u_j = j^{-m'}χ(jx)g(y)`, `χ ∈ C_c^∞((½,2))`, `χ(1)=1`, `g(y_0)=1`:
`supp u_j ⊂ {1/(2j) < x < 2/j}`, so `u_j ∈ C_c^∞(M̊) ⊂ A^{m_1}(M)` for every `m_1`; every (6.42) seminorm
(sup over a compact `K ⊂ M̊`, where `x ≥ x_K > 0`) vanishes for large `j`; every (6.43) seminorm
(`lim_{ε↓0} sup_{0<x<ε}`) vanishes identically since `u_j = 0` on `{x < 1/(2j)}`; and (6.41) with `P = 1`
gives `sup_{M̊} x^{-m'}|u_j| ≥ (1/j)^{-m'} j^{-m'} χ(1) g(y_0) = 1`. Taking `m' = m` refutes Prop. 6.12;
taking `m' < m` refutes the first assertion of Cor. 6.14. Nothing in the computation needs `m' < m`, which is
why declaring it in the setup is the error (F3). For the second assertion, `v_j = e^j χ(jx)g(y)` and
`W_k = {u ∈ A^{-k}(M) : sup x^k|u| < ½ inf_{i≥1} e^i i^{-k}}` (note `A(M) = ∪_k A^{-k}(M)` — the union runs
downwards, correctly written in the note): evaluation at `(1/j, y_0)` gives `x^k|v_j| = j^{-k}e^j` and the
same convexity contradiction as (c). The transfer to Cor. 7.13 is right: by (7.27) `J^m(M,L)` is defined by
`Diff(M,L) u ⊂ x^m L^∞(M)` with the same projective topology, `x` is the extension of `|x|` positive and
smooth on `M\L` (p. 56), and the families sit in `{½ < jx < 2} ⊂ M\L`. **No error beyond F3.**

**(f) — CORRECT once `l ≥ 1` is added (F4).** `b_j = χ_j(x)(1+|ξ|²)^{j/2} ∈ S^j`, and `b_j ∉ S^m` for `m < j`
because `‖b_j‖_{K,0,0,m} = ∞` for any compact `K` meeting `{χ_j ≠ 0}`. Given an absolutely convex
0-neighborhood `W` of `S^∞`, pick basic `W_k ⊂ W ∩ S^k`. Local finiteness of `{B̄(x_j,r_j)}` and `K_1` compact
give `supp χ_j ∩ K_1 = ∅` for all large `j`. Split `b_j = b_jρ_R + b_j(1−ρ_R)`. First piece: compact
`ξ`-support, so in `S^{-∞} ⊂ S^1`, and it vanishes on `K_1 × R^l`, so all its `K_1`-seminorms are `0` and
`2b_jρ_R ∈ W_1`. Second piece: supported in `{|ξ| ≳ R}`; I checked the `O(1/R)` claim by Leibniz — the
`β' = 0` term contributes `(1+|ξ|)^{m-m'}`-style gain `(1+|ξ|)^{-1} ≤ (cR)^{-1}` at level `S^{j+1}`, and each
`β' ≠ 0` term contributes `R^{-|β'|}(1+|ξ|)^{|β'|-1} ≲ R^{-1}` because `|ξ| ≍ R` on `supp ∂^{β'}ρ_R`. So
`2b_j(1−ρ_R) ∈ W_{j+1}` for `R` large, and `b_j = ½(2b_jρ_R) + ½(2b_j(1−ρ_R)) ∈ W` by absolute convexity.
The finitely many remaining `b_j` are absorbed because `W` is absorbing. So `{b_j}` is bounded but in no step:
the spectrum is not regular, hence (p. 4's definition) not boundedly retractive and (p. 5's Cor. 6.5,
contrapositive) not acyclic. **No error beyond F4.**

**Inequality (1) — CORRECT, and I get the same box scaling.** Split `sup` at `1+|ξ| = R`. Low frequencies:
`|∂^α∂^βa|(1+|ξ|)^{|β|-m'} = [|∂^α∂^βa|(1+|ξ|)^{|β|-m''}](1+|ξ|)^{m''-m'} ≤ R^{m''-m'} N_{m''}(a;γ)` since
`m'' > m'` — that is the second term, with `γ' = γ`. High frequencies: put `t = 1+|ξ_0| > R` and take the box
`|x − x_0| ≤ h_x = t^{-c}`, `|ξ − ξ_0| ≤ h_ξ = t^{1-c}` (the note's scaling exactly), on which `1+|ξ| ≍ t` and
which stays in `U` for `t` large because `dist(K, ∂U) > 0`. Rescaling to the unit cube and applying the
Landau–Kolmogorov/Taylor inequality `‖∂^γ f‖_∞ ≤ C(‖f‖_∞ + max_{|δ|=D}‖∂^δ f‖_∞)` for `D > d = |γ|`:
`|∂^α∂^β a| ≤ C h_x^{-|α|}h_ξ^{-|β|}[ t^m N_m(a;0) + max_{|δ|=D} h_x^{|α'|}h_ξ^{|β'|} t^{m''-|β'|} N_{m''}(a;δ) ]`.
With `h_x^{-|α|}h_ξ^{-|β|} = t^{cd-|β|}` and `h_x^{|α'|}h_ξ^{|β'|}t^{-|β'|} = t^{-cD}`, multiplying by
`(1+|ξ|)^{|β|-m'} ≍ t^{|β|-m'}` gives
`N_{m'}` contribution `≤ C[ t^{cd+m-m'} N_m(a;0) + t^{cd+m''-m'-cD} max_δ N_{m''}(a;δ) ]`.
Choose `c ≤ (m'-m)/(2d)` so the first exponent is `≤ −(m'−m)/2`, hence `≤ R^{-(m'-m)/2}` for `t > R`; choose
`D ≥ d + (m''-m')/c` so the second exponent is `≤ 0`, hence `≤ 1 ≤ R^{m''-m'}`. That is (1), with
`Γ = {γ} ∪ {δ : |δ| = D}` finite and `C, R_0` depending only on `γ, m, m', m''`. Because `S^m_K`'s elements
vanish for `x ∉ K`, `N_m(a;0)` is a *global* supremum — the note's remark, and precisely the property that
(f) destroys. Applying (1) on `{N_m(·;0) < 1}` (absolutely convex, so differences of its elements lie in
`2·` it): given `ε`, take `R` with `2CR^{-(m'-m)/2} < ε/2` and then `max_Γ N_{m''} < ε/(4CR^{m''-m'})`; the
`S^{m'}_K`- and `S^{m''}_K`-topologies therefore agree on that 0-neighborhood, which is Wengenroth's
Thm. 6.1 as quoted on p. 4. **No error.**

**Claim 6.46 repair — CORRECT, including the index observation.** `A ⊂ A(M)` bounded; by bounded retractivity
(now available from the repaired Cor. 6.16) its absolutely convex hull `D` is bounded and contained in some
`A^m(M)`, with the `A(M)`- and `A^m(M)`-topologies agreeing on `D`; `A^{m'}(M)` sits between them for `m' < m`,
so its topology agrees too. Given a 0-neighborhood `W ⊂ A^{m'}(M)`, `W ∩ D` is a relative neighborhood of
`0 ∈ D` (`0 ∈ D` because `D` is absolutely convex — this is why the hull is taken), so there is a
0-neighborhood `V ⊂ A(M)` with `V ∩ D ⊂ W`, a fortiori `V ∩ A ⊂ W`. Then `E_{m'}(A ∩ V) ⊂ E_{m'}(W) ⊂ U`
and `⊂ E_{m'}(A) = B`, so `A ∩ V = R(E_{m'}(A∩V)) ⊂ R(B ∩ U)`, which is Claim 6.46. And the index really does
have to be `m' < m`: Prop. 6.29 gives `E_{m'}` on `A^{m'}(M)`, and (6.38) makes `A^{m'} ⊇ A^m` exactly when
`m' < m`, so the printed "For any `m' > m`" leaves `E_{m'}(A)` undefined. (It also matches Cor. 6.14's own
hypothesis `m' < m`, which the printed proof invokes two lines later.) **No error.**

**Prop. 8.8, Cor. 3.5, Remark 3.8, Cors. 6.27/7.22 — CORRECT.**
*Prop. 8.8:* p. 64 routes it through the analogue of Prop. 6.45, i.e. of Claim 6.46, with Cor. 7.31 supplying
the partial extension maps; the same substitution works and Cor. 7.13 drops out. *Cor. 3.5:* with a cut-off
`ρ = 1` near `0`, Leibniz gives `‖a − ρ(ξ/R)a‖_{K,α,β,m'} ≤ C R^{m-m'}` (the `β' = 0` term because
`(1+|ξ|)^{m-m'} ≤ (cR)^{m-m'}` on `{|ξ| ≳ R}`, the `β' ≠ 0` terms because `|ξ| ≍ R` there), and multiplying by
a `ψ ∈ C_c^∞(U)` equal to `1` on the finitely many compacts of the given 0-neighborhood changes none of those
seminorms — density in the `S^{m'}` topology, with no use of Cor. 3.4. *Remark 3.8:* its conclusion is that
`S^∞ ⊂ C^∞` is not a TVS-embedding; (c) exhibits a `C^∞`-null sequence in `S^{-∞} ⊂ S^∞` that is not
`S^∞`-null, which is that conclusion, and (c) uses no retractivity — whereas the printed argument uses
sequential retractivity from Cor. 3.6, as the note says. *Cors. 6.27/7.22:* by Prop. 7.26 every `u ∈ K(M,L)`
is a finite sum `Σ_k ∂_x^k δ_L^{v_k}`, `v_k ∈ C^∞(L; Ω^{-1}NL)`, with local symbol `Σ_k c_k v_k(y) ξ^k`, a
polynomial of degree `≤ k_0`; and `h u = 0` since `h` is supported in `M\L` and `u` in `L`, so the (4.10)
topology on `K^m(M,L)` is purely the symbol topology. On polynomials of degree `≤ k_0`,
`‖a‖_{K,α,β,m̄_1} ≤ C max_k ‖v_k‖_{C^{|α|}(K)}` whenever `m̄_1 ≥ k_0` (each `(1+|ξ|)^{k-m̄_1} ≤ 1`), and
conversely `v_k = (1/k!)∂_ξ^k a|_{ξ=0}` gives `|∂_y^α v_k| ≤ C‖a‖_{K,α,k,m̄_1}` — so every such topology is the
`C^∞`-topology of the coefficients, independent of `m̄_1`, and both corollaries hold. Membership `u ∈ K^m`
forces `k ≤ m̄` (a degree-`k` polynomial symbol lies in `S^{m̄}` iff `k ≤ m̄`), consistent with (4.12) and
(7.34). `Cor. 6.27` is the case `(M̆, ∂M)` by (6.49). **No error.**

**Assembly (the rest of §4) — CORRECT.** The criterion passes to subspaces (`Y_k = Y ∩ X_k`: intersect the
0-neighborhood), to finite products including constant factors, and hence to initial topologies of one fixed
injective map (a subspace of the product); `I^m(M,L)` is the initial topology of (4.10), whose symbol
components have compact base support, `A^m(M)` the initial topology of `u ↦ ((λ_j u)_j, μu)` (with `μu` in the
constant factor `C^∞(M̊)`, on whose support `x` is bounded away from `0`, so the `A^m`-seminorms there are
`C^∞` seminorms), `Ȧ^m`, `𝒦^m`, `K^m` closed subspaces, `J^m ≅ A^m(**M**)`. The collar version of (1) is the
symbol version transported by `x = e^{-ϱ}`, under which `b`-derivatives `x∂_x = −∂_ϱ` correspond to
`(1+|ξ|)∂_ξ` and the box `t^{-c} × t^{1-c}` becomes a box of side `e^{-cϱ}` in `(ϱ, y)`; I redid the estimate
in that variable and it goes through unchanged (paper's own Example 6.11 confirms `A^{-m}(S^l_+) ≅ S^m(R^l)`).
`S^m_K → S^{m'}_K` maps bounded sets to relatively compact sets (Arzelà–Ascoli plus the tail
`(1+|ξ|)^{m-m'}`) but is not a compact operator (no 0-neighborhood of a non-normable Fréchet space is
bounded), exactly as the note's parenthetical says. **No error.**

---

## 4. Typography, English and tone; and the earlier passes

**Build.** Rebuilt in a scratch copy with TeX Live 2026 (`pdflatex` twice): **3 pages**, and the log contains
**no** `Overfull`, `Underfull`, `Warning`, `Missing` or `undefined` line at all. Page count and layout match
the committed `alkl23-note.pdf` byte-for-byte in page count. I read 150-dpi renders of all three pages.

**Renders.** No broken symbols: `\mathring M`, `\breve M`, `\boldsymbol M`, `\varrho`, `\eqref{interp}`, the
`\|\cdot\|'` primes, `\ind`, `\Diff_b`, `\Delta^{N_0}`, `\hat\psi_*` and the accented `\'Alvarez L\'opez` all
set correctly. Display (1) is numbered and referenced correctly ("By (1), the …"). No orphaned heading: §4's
run-in heading sits at the foot of p. 2 with two lines under it, §5's on p. 3 with its whole paragraph. The
footnote sits on p. 1 under the rule, with the `\thanks` marker on the author. The three-item bibliography
fits on p. 3 with slack below. Nothing scrolls off the measure.
*One cosmetic point (part of F12c):* the `\vspace{-2.5em}` after `\maketitle` leaves the date line and
"**1. Purpose.**" flush against one another with no air; two or three points of `\medskip` would read better
and the page still holds.

**English and tone.** U.S. spelling throughout (`neighborhood`, `seminorms`, `parametrized`, `nonzero`; a
targeted scan for `-ise/-isation/-our/centre/behaviour/neighbourhood/labelled/modelling/towards/whilst/
programme/grey/maths` returns only "likewise"). **No em-dashes** (`---` or U+2014): none in the source.
Tone is courteous and non-triumphal: "offered to the authors as a courtesy", "The author would be glad to
learn whether the authors agree, and thanks them for a paper the author has found very useful". No
program-internal jargon anywhere (no "C3-r", no "witness class", no "session"). The word *false* is used only
where a counterexample is exhibited; where only a proof fails the note says so and says which step ("their
printed proofs pass through Cor. 6.21", "the printed derivations of the other clauses of Cor. 3.6 pass through
these properties", "which is what its printed argument uses"). Cors. 6.27 and 7.22 are explicitly declared
**true**. I found **no overclaim**: the note never says the paper's main results fail, and §1's "The main
package … stands once this is done" is supported by §4. The author name "Kunal Tyagi" matches the program's
other arXiv title pages (`results/arxiv/*/main.tex`), so it is not a slip.

**Earlier passes — nothing left unfixed.** `alkl23-note-REVISION.md` records nine repairs R1–R9 from
`alkl23-note-read-O.md`, all APPLIED, none declined; I confirmed each is present in the current source
(R1 `f_i` indexing and `\dim L = n''`; R2 `\boldsymbol M`; R3 "for any compact `K` meeting `{g ≠ 0}`";
R4 the p. 18 split; R5 the dropped `N`; R6 `\textbf{Use of AI.}` / "adjudicated"; R7 "whose steps are Fréchet
spaces"; R8 the Remark 3.8 clause; R9 the "`P = 1`" justification). **None of my twelve findings duplicates
one of theirs.** Two of mine bear on their work: F2 sharpens R1 (the repairer's rationale states "for large
`j`, supp `u_j` lies in the neighborhood of `p_0` where `h = f_i = 0`", which needs the `supp g` hypothesis
that neither the note nor R1 supplies, and the note's `g ∈ C_c^∞(R^{n''})` is *weaker* than the
`g ∈ C_c^∞(U'')` used in the reader's own derivation); F1 corrects a claim neither earlier pass tested,
because neither opened arXiv v2.

**One program-record item (not a defect of the note).** `novelty/adjudication.md` §2 C6 and item A2-02 state
that the §§6–7 renumbering "entered at **v3**" and that "§§3–4 [are] unchanged in all three" (v1, v3,
published). Both are wrong on the evidence above: it entered at **v2** (29 Jul 2023), and §§3–4 were edited
between v1 and v2. The note inherited the second of these. That record should carry a dated correction, and
any downstream "(v1) = (v3 = published)" mapping should read "(v1) = (v2 = v3 = published)". (The separate
dated correction already at the end of `novelty/adjudication.md` — that `S^m_K → S^{m'}_K` are *not* compact
operators — is right, and the note's parenthetical states the corrected form.)

---

## 5. What I could not check

1. **zbMATH 7901419, Semantic Scholar and Unpaywall were not re-fetched by me this pass.** I re-verified the
   two claims that carry the weight (arXiv version list; Crossref `relation`) live on 2026-09-06 and both
   still hold. The other three rest on `novelty/adjudication.md` §2 C6 / A2-03 (2026-09-03, two models).
   MathSciNet was closed then and I did not try it. If the note is sent after any delay, re-run all five.
2. **arXiv v3 of 2304.00798 was not downloaded by me.** I established that v2 already carries the published
   numbering and that the published PDF does; the v3 = published identity rests on `novelty/adjudication.md`
   item A2-02, which downloaded v3 and compared statement numbers. My F1 fix is worded so that it is true on
   either reading.
3. **Memoir §§2.2.2, 2.5.36 and 2.6.7** (the internal cross-references behind "`I(F)` is compactly retractive
   (Section 2.2.2)" and "`J(F)` … (Section 2.6.7)") were not opened. I verified the three *uses* and the
   closedness of `M`, which is what the note asserts; I did not verify that those two subsections derive
   compact retractivity from [1] rather than from something else. If they cite a different source, the note's
   "are covered by the above" would need a word.
4. **Wengenroth's book itself** was not opened; Thm. 6.1, Prop. 6.4 and Cor. 6.5 were checked only as [1]
   quotes them on pp. 4–5, which is all the note claims ("as quoted on p. 5", "quoted on p. 4", "quoted on
   pp. 4–5").
5. **`Diff_b(M)` locality and (6.33)** — I took the paper's local description of `Diff_b` and the inclusion
   `A(M) ⊂ C^∞(M̊)` from its own statements (pp. 38, 56) rather than re-deriving them; the note's §4 sentence
   on the initial topology of `A^m(M)` is a summary of a derivation held off-page ("Full derivations … are
   available on request"), and I checked it is *true*, not that the note's one-line justification is
   self-contained.
6. **Prop. 4.3's continuity constants** (p. 21) were not re-derived; witness (d) uses only (4.8) directly, so
   nothing in this note depends on them.
