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
