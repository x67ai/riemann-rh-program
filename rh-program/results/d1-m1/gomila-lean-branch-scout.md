# Scout: the Gomila `lean/certificate-and-argument-principle` branch vs. D1's H-AP

**Date:** 2026-09-02 (Session 14, D1 scouting agent; read-only — nothing built, no `lake`, no
Mathlib cache downloaded). **Trigger:** `results/watch-sweep-2026-09-02.md` §7. **Standing order
5:** every statement below about the branch is read from its files as fetched today; nothing is
from memory. Fetched copies (API JSON and raw files) were kept in the session scratchpad only;
this file is the record.

**Verdict in one line.** The branch contains a plain Lean 4 / Mathlib development (659 lines, two
files) that, IF it builds as claimed, proves the rectangle argument principle for **entire**
functions in Mathlib's `integral_boundary_rect` edge convention. It does **not** discharge D1's
H-AP (`Zeta23.W1.RectArgPrinciple riemannZeta`) directly — ζ is not entire, the winding number is
stated in a different (stronger, complex-valued) form, and D1's hypothesis admits the degenerate
rectangle σ₁ = σ₂ — but it would supply the two hard pieces v1.1 was priced for (the rectangle
residue integral ∮(ζ−a)⁻¹ dζ = 2πi and the zero-factorization/finiteness argument), leaving
bridging work of roughly one to three Lean sessions. Status: **UNVERIFIED third-party Lean
development** (AI-generated, prose-only verification record, AI referee panel); it must be rebuilt
against the pinned toolchain and audited before any use. The branch's own "hAP" is NOT ours: it is
the hypothesis `hAP : windingRect H z w = N` of the repository's own
`DeBruijnNewman.windingRect_div_eq_zeroCount` — the name coincidence is accidental.

---

## 1. What was fetched (branch head ea09b2f, 2026-08-27T23:13:46Z)

Repository: `https://github.com/judegomila/dbn-lambda-01787854-candidate-audit` (GitHub API
`repos/…`: default branch `main`, license `NOASSERTION`, `pushed_at` 2026-08-27T23:13:47Z).
Branch `lean/certificate-and-argument-principle`, head `ea09b2f6aa7afe60706b67c87b202126f3149e8c`;
tree (recursive, 657 entries, not truncated) fetched via `git/trees/ea09b2f…?recursive=1`.

Commits on the branch beyond `main` (a74738d):

* `3038be5` (Jude Gomila, 2026-08-27T23:13:46Z) — "lean/aristotle: kernel-checked e_C0
  certificate value and the rectangle argument principle". Body, verbatim: "Two further Aristotle
  projects, locally kernel-verified (61 theorems, all on the three standard axioms, no
  sorry/axiom/native_decide): - ec0_certificate: EC0.eC0_le_sharp proves the sharp Prop 4.10 budget
  bound e_C0 <= 233492848188649183/10^24 over the exact parameter boxes in-kernel — the pilot for
  moving Arb certificate values into Lean. - argument_principle: windingRect_eq_sum_analyticOrder
  proves the general argument principle on rectangles (winding = sum of vanishing orders),
  including the rectangle residue integral mathlib lacks; its factored and H/B forms match the
  base-case definitions, so the declared hAP hypothesis is now dischargeable. Reseal."
  Trailers: "Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>" and "Co-authored-by:
  Aristotle (Harmonic) <aristotle-harmonic@harmonic.fun>". Stats: +1308 / −0, 14 files (13 added,
  `lean/aristotle/README.md` modified +27).
* `ea09b2f` (same timestamp) — "Reseal for the two new lean/aristotle projects" (SHA256SUMS only).

### 1.1 File table (git blob SHA-1 from the tree; sizes in bytes)

| Path (under `lean/aristotle/`) | Size | Blob SHA-1 | Content |
|---|---|---|---|
| `README.md` | 7436 | f072f6ec… | project README (2026-08-20 record + 2026-08-27 "Additions" section) |
| `argument_principle/lean-toolchain` | 25 | 4c685fa0… | `leanprover/lean4:v4.28.0` |
| `argument_principle/lakefile.toml` | 234 | d1331e37… | see §1.2 |
| `argument_principle/lake-manifest.json` | 3109 | 57bef473… | see §1.2 |
| `argument_principle/ARISTOTLE_SUMMARY.md` | 2964 | 3aa5262e… | Aristotle's own run summary (run `fda395ce-fa2c-4214-a442-d9ff1a52f5b0`) |
| `argument_principle/RequestProject/Main.lean` | 563 | 308f9cfb… | `import Mathlib` + `set_option`s only (no declarations) |
| `argument_principle/RequestProject/ArgumentPrinciple.lean` | 23422 | edbf83fb… | 444 lines: 4 defs, 26 lemmas, 4 theorems |
| `argument_principle/RequestProject/ArgumentPrincipleGeneral.lean` | 10838 | d2741530… | 215 lines: 8 lemmas, 3 theorems |
| `ec0_certificate/lean-toolchain` | 25 | 4c685fa0… | identical to the above |
| `ec0_certificate/lakefile.toml` | 234 | d1331e37… | identical blob |
| `ec0_certificate/lake-manifest.json` | 3109 | 57bef473… | identical blob |
| `ec0_certificate/ARISTOTLE_SUMMARY.md` | 2579 | 5bba3cb1… | Aristotle's run summary (run `8316f55a-1cc3-456c-8c52-b400767e8723`) |
| `ec0_certificate/RequestProject/Main.lean` | 563 | 308f9cfb… | identical blob |
| `ec0_certificate/RequestProject/EC0Certificate.lean` | 14630 | 888a9130… | 321 lines: 8 defs, 18 lemmas, 2 theorems |

SHA-256 of the raw files as fetched today: `ArgumentPrinciple.lean`
`b1162a0cc3b46c3559e928d04cf1a3c37b4fad6ca1323b65a41ea9948fbe605b`;
`ArgumentPrincipleGeneral.lean` `ee3822428e40b210d14c47b044bbbde011d0b72a4cfa2bad0fb2811a04113e82`;
`Main.lean` `929b0bddef0b781f3fb42c7a99f252dc0bda7331f698104f7075e12ff637c52d`;
`EC0Certificate.lean` `bbf8c87db066583a2f9cabd0438607b70dc44d8465c53a90b9fae3d0a4a00d6b`.

Declaration count across the three `.lean` files: 4+26 + 3+8 + 2+18 = **61** theorems+lemmas —
this matches the commit's "61 theorems" exactly, so the count is of every `theorem`/`lemma`
declaration in both projects, not of headline results. **Nothing else is in the commit**: no build
log, no `#print axioms` output, no CI configuration. The only verification record is prose (§4).

### 1.2 Toolchain and dependency pins (both projects byte-identical)

`lean-toolchain`: `leanprover/lean4:v4.28.0`.

`lakefile.toml`, verbatim:

    name = "RequestProject"
    defaultTargets = ["RequestProject"]

    [[require]]
    name = "mathlib"
    git = "https://github.com/leanprover-community/mathlib4.git"
    rev = "v4.28.0"

    [[lean_lib]]
    name = "RequestProject"
    globs = ["RequestProject.+"]

`lake-manifest.json` (`version` 1.1.0, `name` RequestProject): mathlib
`8f9d9cff6bd728b17a24e163c9402775d9e6a365` (inputRev `v4.28.0`; that commit is dated
2026-02-16T15:28:25Z, "chore: bump toolchain to v4.28.0 (#35406)" per the mathlib4 GitHub API);
plausible `55c8532e…`, LeanSearchClient `c5d5b8fe…`, importGraph `85b59af4…`, proofwidgets
`be3b2e63…` (v0.0.87), aesop `f642a64c…`, Qq `b8f98e90…`, batteries `495c008c…`, Cli `4f10f476…`
(v4.28.0).

Every source file begins `import Mathlib` (the whole library); `ArgumentPrincipleGeneral.lean` also
imports `RequestProject.ArgumentPrinciple`. `Main.lean` sets `maxHeartbeats 8000000`,
`maxRecDepth 4000`, `synthInstance.maxHeartbeats 20000`, `autoImplicit false` — but the two
mathematics files do not import `Main.lean`, so those options do not apply to them (they run with
Lean defaults unless `lake` passes options, which the lakefile does not).

**Against the program's pin:** the D1 checker builds on `leanprover/lean4:v4.33.0-rc2` with Mathlib
`51e6992efd06126df61a496bebf8f49482a4e129` (2026-08-03; `~/rh-lean-work/zeta-23-lean-main/
lake-manifest.json` and the package's git HEAD, read today). The branch's Mathlib is ~5.5 months
older. (Side note for the parent: `results/d1-m1/AUDIT-F.md` line 151 records the Mathlib as
"123d1576…", which does not match the manifest/HEAD `51e6992…` on disk — reconcile at the next
touch; not in this scout's scope.)

### 1.3 License

Repository `LICENSE` (blob 2d908c4d…, 1423 bytes): "MIT License / Copyright (c) 2026 Jude Gomila"
followed by the standard MIT text, then a trailer: "Scope. This MIT license covers the source code
original to this repository (for example: verifiers/, scripts/, src/, barrier/src/, lean/,
research/, and paper/generate_paper.py). See LICENSE-DOCS for the documentation and data license,
and THIRD_PARTY.md plus the "License" section of README.md for third-party material and the
recorded exceptions." README "License" section: source code MIT; documentation/data/certificates
CC BY 4.0; exceptions (all rights reserved) are the authored manuscripts, `dan-reworking/`, and the
`independent/` programs by Dan Romik. `THIRD_PARTY.md` mentions neither Lean, Aristotle, Harmonic,
nor Mathlib. GitHub reports `NOASSERTION` only because of the custom scope trailer.

**Compatibility with Apache-2.0:** MIT is a permissive license and MIT-licensed code may be
incorporated into an Apache-2.0 project; the obligation is to retain the MIT copyright notice and
permission notice with any copied or adapted portion (the same pattern as the Zeta23/W1 file headers
already use for Anthropic's zeta-23). Caveat recorded, not adjudicated: the code is machine-generated
(Aristotle) and the repository asserts MIT over it as "source code original to this repository"; if
any of it is ported, keep the notice and the Aristotle co-author attribution verbatim.

---

## 2. The `argument_principle` sources, verbatim where it matters

Namespace `ArgumentPrinciple`; `open Set Complex intervalIntegral MeasureTheory`,
`open scoped Real BigOperators Interval`.

### 2.1 Definitions (`ArgumentPrinciple.lean` lines 22–38)

    /-- The closed axis-parallel rectangle with corners `z` and `w` (unordered intervals). -/
    def Rect (z w : ℂ) : Set ℂ := [[z.re, w.re]] ×ℂ [[z.im, w.im]]

    /-- The integral of `f` over the (positively oriented) boundary of the rectangle
    with corners `z` and `w`. -/
    noncomputable def rectIntegral (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
        (∫ x : ℝ in z.re..w.re, f (x + z.im * I)) - (∫ x : ℝ in z.re..w.re, f (x + w.im * I))
          + I * (∫ y : ℝ in z.im..w.im, f (w.re + y * I))
          - I * (∫ y : ℝ in z.im..w.im, f (z.re + y * I))

    /-- The winding number of `f` around the boundary of the rectangle with corners `z` and `w`. -/
    noncomputable def windingRect (f : ℂ → ℂ) (z w : ℂ) : ℂ :=
        (2 * (π : ℂ) * I)⁻¹ * rectIntegral (logDeriv f) z w

    /-- The boundary of the rectangle with corners `z` and `w`. -/
    def RectFrontier (z w : ℂ) : Set ℂ :=
        {c ∈ Rect z w | c.re = z.re ∨ c.re = w.re ∨ c.im = z.im ∨ c.im = w.im}

So the winding number is defined **via a path integral of Mathlib's `logDeriv f`** (= `deriv f / f`,
`logDeriv_apply`) along the four edges in the convention of Mathlib's
`Complex.integral_boundary_rect_eq_zero_of_differentiableOn` (bottom edge left→right at Im = z.im,
minus the top edge at Im = w.im, plus i·(right edge upward at Re = w.re), minus i·(left edge at
Re = z.re)) — i.e. the counterclockwise traversal when z.re < w.re and z.im < w.im. Not a
continuous-argument lift, not Mathlib's `circleIntegral`, not a Mathlib winding-number notion.

### 2.2 Main theorem statements (verbatim)

`ArgumentPrinciple.lean` line 259 — the residue integral the commit message refers to:

    theorem rectIntegral_inv_sub {z w a : ℂ} (h1 : z.re < a.re) (h2 : a.re < w.re)
        (h3 : z.im < a.im) (h4 : a.im < w.im) :
        rectIntegral (fun c => (c - a)⁻¹) z w = 2 * (π : ℂ) * I

(proved by explicit antiderivatives `½·log(t²+α²) − i·arctan(t/α)` on each edge and the
four-arctan identity `arctan_rect_sum`, lines 150–308).

Line 347 — the reusable core:

    theorem windingRect_prod_mul {z w : ℂ} {V : ℂ → ℂ}
        (hVcont : ContinuousOn (logDeriv V) (RectFrontier z w))
        (hVint : rectIntegral (logDeriv V) z w = 0)
        (hVne : ∀ c ∈ RectFrontier z w, V c ≠ 0)
        (hVdiff : ∀ c ∈ RectFrontier z w, DifferentiableAt ℂ V c)
        {ι : Type*} {s : Finset ι} {a : ι → ℂ} {m : ι → ℕ}
        (ha : ∀ j ∈ s, (a j).re ∈ Ioo z.re w.re ∧ (a j).im ∈ Ioo z.im w.im) :
        windingRect (fun c => (∏ j ∈ s, (c - a j) ^ (m j)) * V c) z w = ∑ j ∈ s, (m j : ℂ)

Line 398 — the factored form ("primary target" per the summary):

    theorem windingRect_factored {z w : ℂ} (hre : z.re < w.re) (him : z.im < w.im)
        {U : ℂ → ℂ} (hU : Differentiable ℂ U) (hU0 : ∀ c ∈ Rect z w, U c ≠ 0)
        {k : ℕ} (a : Fin k → ℂ) (m : Fin k → ℕ) (hm : ∀ j, 1 ≤ m j)
        (ha : ∀ j, (a j).re ∈ Ioo z.re w.re ∧ (a j).im ∈ Ioo z.im w.im) :
        (∀ c ∈ RectFrontier z w, (∏ j, (c - a j) ^ (m j)) * U c ≠ 0) ∧
          windingRect (fun c => (∏ j, (c - a j) ^ (m j)) * U c) z w = ∑ j, (m j : ℂ)

Line 417 — the `H / B` consumer form (`windingRect_factored_div`): same hypotheses plus
`{B : ℂ → ℂ} (hB : Differentiable ℂ B) (hB0 : ∀ c ∈ Rect z w, B c ≠ 0)`, concluding
`windingRect (fun c => ((∏ j, (c - a j) ^ (m j)) * U c) / B c) z w = ∑ j, (m j : ℂ)`.

`ArgumentPrincipleGeneral.lean` line 162 — **the general theorem the commit names**:

    theorem windingRect_eq_sum_analyticOrder {z w : ℂ} (hre : z.re < w.re) (him : z.im < w.im)
        {H : ℂ → ℂ} (hH : Differentiable ℂ H) (hbd : ∀ c ∈ RectFrontier z w, H c ≠ 0)
        (S : Finset ℂ) (hS : ∀ p, p ∈ S ↔ (p ∈ Rect z w ∧ H p = 0)) :
        windingRect H z w = ∑ p ∈ S, (analyticOrderNatAt H p : ℂ)

Line 184 — the self-contained form:

    theorem windingRect_eq_finsum_analyticOrder {z w : ℂ} (hre : z.re < w.re) (him : z.im < w.im)
        {H : ℂ → ℂ} (hH : Differentiable ℂ H) (hbd : ∀ c ∈ RectFrontier z w, H c ≠ 0) :
        windingRect H z w
          = ∑ᶠ p ∈ {p | p ∈ Rect z w ∧ H p = 0}, (analyticOrderNatAt H p : ℂ)

Line 199 — the sanity check: `windingRect (id : ℂ → ℂ) (-1 - I) (1 + I) = 1`.

**Read-off of the hypotheses and conclusion.** Function class: `Differentiable ℂ H` — **entire**
(differentiable on all of ℂ), not "holomorphic on an open set containing the closed rectangle".
Boundary: `H ≠ 0` on `RectFrontier z w`. Rectangle: nondegenerate, `z.re < w.re ∧ z.im < w.im`.
Conclusion: the complex-valued winding number equals the **sum of the vanishing orders
(`analyticOrderNatAt`) over the zeros of `H` in the closed rectangle** — a count with multiplicity
(the zeros lie in the open interior by `mem_Ioo_of_zero_mem_Rect`, line 144). Supporting lemmas:
`analyticOrderAt_ne_top` (identity theorem on `Set.univ`), `exists_factor_pow_sub` and
`exists_factor_prod` (factor `H = ∏ (ζ−p)^ord · G` with `G` entire and nonzero on the finite set),
`isCompact_Rect`, `finite_zeros_of_isCompact` / `finite_zeros_Rect` (accumulation-point argument on
`univ`), `continuousOn_logDeriv` and `rectIntegral_logDeriv_eq_zero` (Cauchy–Goursat for an entire
nonvanishing function, via Mathlib's rectangle Cauchy theorem).

### 2.3 Axioms / escape-hatch grep

`grep -n -i "sorry\|admit\|native_decide\|axiom\|unsafe\|opaque\|implemented_by\|extern\|decide"`
over `argument_principle/RequestProject/*.lean` and `ec0_certificate/RequestProject/*.lean`:
**no matches at all** (exit 1) — not even in comments; `decide` as a substring is absent, which
also rules out `native_decide` and `decide +kernel`. Tactics used are ordinary Mathlib tactics
(`simp`, `rw`, `ring`, `field_simp`, `linarith`, `norm_num`, `fun_prop`, `filter_upwards`,
`linear_combination`, `positivity`, `exact_mod_cast`, `push_cast`, `induction … using
Finset.induction_on`, `conv_lhs`).

**`#print axioms` output recorded in the repo: none.** The only statements are prose — the commit
body ("all on the three standard axioms, no sorry/axiom/native_decide"), `lean/aristotle/README.md`
("verified with the same record (lake build green on v4.28.0; no `sorry`/`axiom`/`native_decide`;
all 61 theorems on `[propext, Classical.choice, Quot.sound]`; statements faithfulness-checked)"),
and each `ARISTOTLE_SUMMARY.md` ("Everything builds cleanly with no `sorry` and only the standard
axioms (`propext`, `Classical.choice`, `Quot.sound`)"). No log, no transcript, no CI.

### 2.4 The `ec0_certificate` project (for the file table's sake)

`EC0Certificate.lean` (namespace `EC0`): exact reals `N0 = 690988`, `t0 = 129/800`,
`t1 = 161250001/10^9`, `y0 = √(87677/2500000)`, `ymax = √(271/400)`, `xf t = 4π(N0² − t/16)`,
`Lf t = log(N0² − t/16)`, `eC0 t y` (line 63), and

    theorem eC0_le_sharp {t y : ℝ} (ht0 : t0 ≤ t) (ht1 : t ≤ t1) (hy0 : y0 ≤ y) (hy1 : y ≤ ymax) :
        eC0 t y ≤ 233492848188649183 / 10 ^ 24

plus `eC0_le_weak` (`≤ 234 / 10 ^ 9`) and `box_nonempty` (`t0 < t1 ∧ y0 < ymax`). Rational
enclosures of log/exp/sqrt/π throughout; the summary records that Aristotle found the informal
guidance's enclosure `26.98 < L < 26.99` to be wrong (true `L = 26.8917554…`). Not relevant to
H-AP; relevant to the Gomila screen (`results/d1-m0/gomila-screen.md`) as "one Arb certificate
value re-proved in-kernel", unverified.

---

## 3. Comparison with D1's H-AP

### 3.1 What H-AP needs (`lean/Zeta23/W1/Soundness.lean` lines 168–182, verbatim)

    def RectArgPrinciple (f : ℂ → ℂ) : Prop :=
      ∀ s₁ s₂ t₁ t₂ : ℝ, 1/2 < s₁ → s₁ ≤ s₂ → s₂ < 1 → t₁ < t₂ →
      ∀ U : Set ℂ, IsOpen U → rectClosed s₁ s₂ t₁ t₂ ⊆ U → DifferentiableOn ℂ f U →
        (∀ s ∈ rectBdry s₁ s₂ t₁ t₂, f s ≠ 0) →
        ∃ Z : ℕ,
          2 * π * Z
              = argIncrement f (cpt s₁ t₁) (cpt s₂ t₁) + argIncrement f (cpt s₂ t₁) (cpt s₂ t₂)
                + argIncrement f (cpt s₂ t₂) (cpt s₁ t₂) + argIncrement f (cpt s₁ t₂) (cpt s₁ t₁)
            ∧ (Z = 0 → ∀ s ∈ rectOpen s₁ s₂ t₁ t₂, f s ≠ 0)
            ∧ (1 ≤ Z → ∃ ρ ∈ rectOpen s₁ s₂ t₁ t₂, f ρ = 0)

with `rectClosed s₁ s₂ t₁ t₂ = {s | s₁ ≤ s.re ∧ s.re ≤ s₂ ∧ t₁ ≤ s.im ∧ s.im ≤ t₂}`,
`rectOpen` the strict version, `rectBdry = rectClosed \ rectOpen`, `cpt x y = ⟨x, y⟩`,
`logDerivSegIntegral f z w = ∫ t in (0:ℝ)..1, (deriv f (segPt z w t) / f (segPt z w t)) * (w − z)`
and `argIncrement f z w = (logDerivSegIntegral f z w).im`. It is consumed once, in
`cert_of_checkW1` (line 1119): `hAP (sigma1 d) (sigma2 d) (T1 d) (T2 d) hhalf hs12le hs2lt1 hT12 _
hUopen hUsub hdiff hbnz` with `f := riemannZeta`, `U := {s : ℂ | s.re < 1}` (open; ζ is
`DifferentiableOn` there via `differentiableAt_riemannZeta`), and `hs12le : sigma1 d ≤ sigma2 d`
coming from the checker's **non-strict** clause C2b. FORMAT.md §8.2 states the full form ("the number
Z of zeros of f in R° counted with multiplicity is finite and 2π·Z = Σ_e Im ∫_e f′/f ds"); the Lean
Prop is the weaker consequence form (header note of 2026-08-26), which is what v1.1 must discharge.

### 3.2 Gap-by-gap

**G1 — function class (the substantive gap).** The branch requires `Differentiable ℂ H` (entire).
H-AP is stated for `DifferentiableOn ℂ f U` on an open `U ⊇ rectClosed`, and the consumer
instantiates `f := riemannZeta`, which has a pole at 1 and is not entire. So
`windingRect_eq_sum_analyticOrder` **cannot be applied to ζ as stated**. Entire-ness is used in
three places: `continuousOn_logDeriv` (takes `Differentiable ℂ (deriv F)` from `hF.analyticAt`),
`analyticOrderAt_ne_top` and `finite_zeros_of_isCompact` (identity theorem via
`AnalyticOnNhd ℂ H Set.univ` and `isPreconnected_univ`), and `exists_factor_pow_sub` /
`exists_factor_prod` (the cofactor `G` is built and shown differentiable on all of ℂ). Two
adaptation routes, both real work:
  (a) generalize the development from `Differentiable ℂ H` to `DifferentiableOn ℂ H U` with `U` open
  and preconnected containing `Rect z w` (the identity-theorem steps need connectedness of `U`; the
  Cauchy–Goursat step already needs only the closed rectangle; the factorization must produce a
  cofactor differentiable on `U`, which is what `AnalyticAt.analyticOrderAt_ne_top` gives locally,
  glued on `U`); the consumer's `U = {Re s < 1}` is convex, hence preconnected, so it would fit;
  (b) keep the theorem entire-only and apply it to an entire function with the same zeros in the
  region, e.g. `s ↦ (s − 1)·ζ(s)` — then `logDeriv` differs by `(s − 1)⁻¹`, whose rectangle
  integral vanishes for σ₂ < 1 by the branch's own `rectIntegral_eq_zero_of_differentiableOn`, and
  orders at zeros agree. Whether Mathlib packages `(s−1)ζ(s)` as an entire function was NOT checked
  today (only `riemannZeta_residue_one` and `differentiableAt_riemannZeta` were confirmed present by
  name in the program's Mathlib tree) — route (b)'s feasibility is [UNVERIFIED].

**G2 — form of the winding identity (bridgeable, small).** Branch: the complex identity
`rectIntegral (logDeriv H) z w = 2πi · Z` (i.e. `windingRect H z w = (Z : ℂ)`), with
`logDeriv f = deriv f / f` and the four edges parameterized by `x ↦ x + c·I` / `y ↦ c + y·I` over
Mathlib interval integrals. H-AP: `2πZ = Im Σ_edges logDerivSegIntegral f`, with each edge
parameterized affinely on `[0,1]` (`segPt z w t = z + t·(w − z)`, integrand times `(w − z)`), in the
order bottom `(σ₁,t₁)→(σ₂,t₁)`, right `→(σ₂,t₂)`, top `→(σ₁,t₂)`, left `→(σ₁,t₁)` — the same
counterclockwise traversal (the branch's `− top` and `− I·left` are exactly the reversed-direction
edges). Bridge: with `z := cpt s₁ t₁`, `w := cpt s₂ t₂`, show Σ_edges `logDerivSegIntegral f` =
`rectIntegral (logDeriv f) z w` by four affine changes of variables (Soundness.lean already has
`logDerivSegIntegral_affine`, line 726, and the `edge_sum_eq` machinery; Mathlib's
`intervalIntegral.integral_comp_mul_add`-family lemmas do the rest), then take imaginary parts of
`2πi·Z`. The branch's identity is **strictly stronger** than H-AP's clause (i) (it also gives real
part 0), so no information is lost.

**G3 — rectangle sets (bridgeable, small).** `Rect z w = [[z.re, w.re]] ×ℂ [[z.im, w.im]]`
(`uIcc`) equals `rectClosed s₁ s₂ t₁ t₂` once `s₁ ≤ s₂`, `t₁ ≤ t₂` (`Set.uIcc_of_le`,
`Complex.mem_reProdIm` — present by name in the program's Mathlib). `RectFrontier z w` equals
`rectBdry s₁ s₂ t₁ t₂` for the nondegenerate rectangle (both are "in the closed rectangle and on one
of the four bounding lines"; a short `ext` lemma). The branch's zero set is over the CLOSED
rectangle; with boundary nonvanishing it coincides with the open one, which is what H-AP's (ii)/(iii)
quantify over.

**G4 — degenerate rectangle (must be handled; small but unavoidable).** H-AP admits `s₁ = s₂`
(hypothesis `s₁ ≤ s₂`, fed by the checker's non-strict C2b). The branch requires `z.re < w.re`. For
`s₁ = s₂` one proves H-AP by hand: `rectOpen` is empty, so (ii) is vacuous and (iii) forces
`Z = 0`, i.e. the four increments sum to 0 — bottom and top are one-point "segments" (`w − z = 0`,
integrand times 0), right and left are the same vertical segment traversed oppositely and cancel
(`logDerivSegIntegral_affine` + `intervalIntegral.integral_symm`; integrability from `f ≠ 0` on the
whole closed set, which is all boundary here). Alternatively tighten H-AP to `s₁ < s₂` (C2b already
could be made strict), but that changes the displayed hypothesis text and FORMAT.md; proving the
degenerate case is the cleaner path.

**G5 — the two counting consequences (bridgeable, small).** Take `Z := ∑ p ∈ S, analyticOrderNatAt
H p : ℕ` with `S := (finite_zeros_Rect …).toFinset`. (ii) `Z = 0` → every summand is 0 → for
`p ∈ S`, `analyticOrderAt H p = 0`, which for analytic `H` means `H p ≠ 0` (Mathlib's
`analyticOrderAt_eq_zero`, present by name) — contradiction unless `S = ∅` → no zeros in `Rect`, a
fortiori in `rectOpen` (needs `analyticOrderAt_ne_top` so that `toNat` is not hiding `⊤`). (iii)
`1 ≤ Z` → some summand is nonzero → `S ≠ ∅` → a zero in `Rect`, in the open interior by
`mem_Ioo_of_zero_mem_Rect`. A few lines each on top of the branch's lemmas.

**G6 — toolchain drift (mechanical, unpriced until tried).** Branch: lean4 v4.28.0, Mathlib
`8f9d9cff` (2026-02-16). Program: lean4 v4.33.0-rc2, Mathlib `51e6992` (2026-08-03). Spot check by
recursive grep of the program's Mathlib tree for every Mathlib name the two files use: present —
`analyticOrderNatAt`, `Complex.integral_boundary_rect_eq_zero_of_differentiableOn`,
`Real.arctan_inv_of_pos`, `logDeriv_prod`, `logDeriv_fun_pow`, `accPt_iff_frequently_nhdsNE`,
`exists_accPt_of_subset_isCompact`, `AnalyticAt.analyticOrderAt_ne_top`,
`eqOn_zero_of_preconnected_of_frequently_eq_zero`, `analyticOrderAt_id`, `analyticOrderAt_mul`,
`analyticOrderAt_eq_zero`, `analyticOrderAt_eq_top`, `logDeriv_apply`, `Complex.mem_reProdIm`;
**absent** — `finsum_mem_coe_finset` (used once, in `windingRect_eq_finsum_analyticOrder`, which
the Finset-form main theorem does not depend on). So a port to the program's toolchain needs at
least one substitution and possibly signature adjustments that only a compile will reveal.

### 3.3 Verdict on the question asked

* **Directly:** no. Wrong function class for ζ (G1), different rectangle/winding vocabulary
  (G2/G3), nondegeneracy mismatch (G4), and a different toolchain (G6).
* **After adaptation:** yes, plausibly — IF it builds as claimed. G2–G5 are bridging lemmas of the
  kind Soundness.lean already contains; G1 is the one piece of genuine mathematics-in-Lean (route
  (a) generalization to an open preconnected `U`, or route (b) via an entire surrogate for ζ). What
  the branch would contribute is precisely the part D-R3 identified as missing from Mathlib: the
  rectangle residue integral `rectIntegral_inv_sub` (explicit antiderivatives + four-arctan identity,
  ~160 lines) and the factor-out-the-zeros / finiteness argument (`ArgumentPrincipleGeneral.lean`,
  ~180 lines). With those in hand, v1.1 reduces from "build the argument principle on
  `WeilEF/Contour.lean` + the divisor layer" to "generalize entire → on-`U`, and bridge".
* **Not at all** would be the answer only if the development fails to build or the `Differentiable ℂ`
  → `DifferentiableOn` generalization turned out to be blocked, which nothing read today suggests.

**Important framing for any write-up:** the branch's own claim "the declared hAP hypothesis is now
dischargeable" refers to the repository's `lean/DeBruijnNewman_BaseCase.aristotle.lean`, whose
`theorem windingRect_div_eq_zeroCount {H B : ℂ → ℂ} {z w : ℂ} {N : ℕ} (hH : Differentiable ℂ H)
(hB : Differentiable ℂ B) (hBne : ∀ ζ ∈ Rect z w, B ζ ≠ 0) (hHne : ∀ ζ ∈ RectFrontier z w, H ζ ≠ 0)
(hAP : windingRect H z w = N) : windingRect (fun ζ => H ζ / B ζ) z w = N` takes the argument
principle for an **entire** `H` as the hypothesis `hAP` (that file's header: "Since Mathlib does not
(yet) contain the argument principle, the statement … is recorded as
`DeBruijnNewman.windingRect_div_eq_zeroCount`, which takes the argument principle for `H` itself as
a hypothesis"). Its `Rect`/`rectIntegral`/`windingRect`/`RectFrontier` are textually the same
definitions as the branch's (`uIcc` vs `[[ ]]` notation; `Real.pi` vs `(π : ℂ)`), in a different
namespace — so even their own discharge is a definitional bridge, not yet done in the branch. It has
nothing to do with D1's `RectArgPrinciple`; the shared name "hAP" is a coincidence and must not be
quoted as if the branch addressed D1.

---

## 4. Provenance and trust

* **Generator.** `lean/aristotle/README.md`: "Seven Lean 4 projects generated by **Harmonic
  Aristotle** (arXiv:2510.01346, via the `aristotlelib` API, 2026-08-20) …" and, for this branch,
  "Two further Aristotle projects, verified with the same record". Each `ARISTOTLE_SUMMARY.md` is
  written in the first person by the system ("I formalized `job8_ec0_certificate.tex` …";
  "Formalized `job9_argument_principle.tex` …"; "All work is committed and pushed"). The `.tex`
  job files named as sources are not in the commit. Commit co-authors: "Claude Fable 5
  <noreply@anthropic.com>" and "Aristotle (Harmonic) <aristotle-harmonic@harmonic.fun>". So the
  Lean was produced by Harmonic's Aristotle from a task document, and the commit was assembled with
  a Claude session; no human author of the proofs is named.
* **Verification record.** Prose only (§2.3): "locally kernel-verified", "lake build green on
  v4.28.0", "#print axioms … [propext, Classical.choice, Quot.sound]", "statements
  faithfulness-checked" — by whom is not stated for the 2026-08-27 additions (the 2026-08-20 record
  says "one independent review pass" without naming it). No build log, no axioms output, no CI, no
  independent recompile is recorded anywhere in the tree.
* **Referee record of the repository.** `EXTERNAL_REFEREE_REPORT_2026-07-28.md`, line 4:
  "**Reviewer:** adversarial AI referee panel (four independent agents, one per proof leg + one
  cross-cutting), directed and synthesized by Claude (Opus 4.8), 2026-07-28." Line 7: "This is an
  AI adversarial review, **not** a substitute for human expert peer review." Line 95: "*This review
  was performed by AI agents under human direction. It is an adversarial technical audit, not human
  expert peer review …*". Line 109: "Residual to acceptance is now purely human-mathematician
  analytic sign-off". The `lean/aristotle/README.md` "Autoformalization caveat": "Proofs are
  kernel-verified; faithfulness of statements and definitions to the intended mathematics was
  checked by one independent review pass … but still warrants referee eyes".
* **Status, plainly:** an **UNVERIFIED third-party Lean development.** Nothing in it has been
  compiled, kernel-checked, or axiom-audited by this program. What this scout adds is only a human
  read of 659 lines: the code is ordinary Mathlib-style Lean, the grep for escape hatches is clean,
  the declaration count matches the "61 theorems" claim, and the main statements say what the
  summaries say they say (with the entire-function restriction the summaries do not emphasize). A
  read is not a build. Before any use: rebuild against the pinned toolchain, run `#print axioms` on
  `windingRect_eq_sum_analyticOrder`, `windingRect_factored`, `rectIntegral_inv_sub`, and audit the
  definitions against FORMAT.md §8.2 (definition faithfulness is the known failure mode of
  autoformalization — the repository's own README records two statement-level transcription defects
  found in its earlier `tail_lemma` project).
* **Screen bookkeeping.** For `results/d1-m0/gomila-screen.md`: `main` is unchanged at a74738d; the
  branch adds nothing to the Λ claim's evidence chain except an in-kernel re-proof of one Arb
  certificate value (§2.4), itself unverified.

---

## 5. Recommended next step, with cost

**Recommendation: verify-as-is first, in isolation; port only if it passes.** Do not touch the D1
tree until the branch is known to build.

1. **Verify as-is (heavy, mostly I/O; run only when the machine is idle and off the thermal cap).**
   Clone the branch shallowly into a space-free scratch directory (e.g. `~/rh-lean-work/gomila-ap/`,
   `git clone --depth 1 --branch lean/certificate-and-argument-principle …`), keep only
   `lean/aristotle/argument_principle/`, and pin the exact commit `ea09b2f`. Then `elan` fetches
   `leanprover/lean4:v4.28.0` (a second toolchain, ~1 GB), `lake exe cache get` pulls the Mathlib
   `8f9d9cff` oleans (several GB on disk; 10–30 min on a good link, hours on the sponsor's patchy
   one — the download must have a retry loop), and `lake build` compiles the three files
   (`import Mathlib` per file; ~5–15 min of CPU-heavy work on this machine). Finish with a scratch
   file `#print axioms ArgumentPrinciple.windingRect_eq_sum_analyticOrder` (and the three others
   named above) via `lake env lean`. **Estimate: 1–2 hours wall, ~30 min of it heavy CPU; disk
   ~6–8 GB for a throwaway toolchain + cache.** Record the log next to this file.
2. **If it builds: port to the program's toolchain (medium).** Copy the two files into the D1 tree
   (e.g. `Zeta23/W1/ArgPrinciple.lean`, MIT notice + Aristotle attribution in the header, imports
   narrowed from `Mathlib` to the actual modules) and compile against v4.33.0-rc2 / Mathlib
   `51e6992`; fix the known missing name `finsum_mem_coe_finset` and whatever else drifts.
   **Estimate: half a session to a session**, dominated by name/signature drift; the mathematics
   should not change.
3. **Then discharge H-AP (the real v1.1 work, re-priced).** G1 route (a) — generalize the four
   entire-only lemmas to `DifferentiableOn ℂ H U` for open preconnected `U` — plus the G2–G5 bridges
   and the G4 degenerate case, ending with `theorem rectArgPrinciple_riemannZeta :
   RectArgPrinciple riemannZeta` and the corollary `cert_of_checkW1'` with the `hAP` argument
   removed. **Estimate: 1–3 sessions of Lean work** (down from the original v1.1 pricing, which
   assumed building the residue integral and the divisor-layer counting from scratch on
   `WeilEF/Contour.lean`). Route (b) (`(s−1)ζ(s)` entire surrogate) is the fallback if (a) fights
   the identity-theorem plumbing.
4. **Do not** cite the branch, the "61 theorems", or "hAP dischargeable" in any public D1 text
   until step 1 has run and its `#print axioms` output is on disk in this directory.
