# Adversarial audit — D1 v1.1 (D-R3): the ported argument principle and the discharge of H-AP

**Date:** 2026-09-02 (Session 14, D1 adversarial Lean audit agent; standing order 5 — a different
model from the porting and discharging agents, nothing taken on their word). **Inputs read in
full first:** `results/d1-m1/gomila-lean-branch-scout.md`, `results/d1-m1/gomila-lean-branch-verify.md`,
`results/d1-m1/v11/port-notes.md` (targeted), `results/d1-m1/v11/discharge-notes.md` (targeted),
`lean/Zeta23/W1/Soundness.lean`, `lean/Zeta23/W1/Checker.lean`, `results/d1-m1/FORMAT.md` §8,
`directions/D1-certified-refutation-arm.md`. **Tree audited:**
`~/rh-lean-work/zeta-23-v11` (Lean `v4.33.0-rc2`, Mathlib
`51e6992efd06126df61a496bebf8f49482a4e129` per `lake-manifest.json`). **Not touched:**
`~/rh-lean-work/zeta-23-lean-main`. One `lake` process at a time; `pmset -g therm` printed no
`CPU_Speed_Limit` line at every check.

## VERDICT: **CLEAN**

No repair was needed and none was applied. Everything the port and discharge reports claim was
re-derived here from the files and from fresh builds, plus three checks the builders did not run
(elaborated-statement equality against the original toolchain, an independent smoke test, and a
concrete non-vacuity/orientation witness). Five observations are recorded in §7; none of them
changes the verdict, and none is a defect in the Lean.

Honest label after this audit, binding and verbatim: an accepted ζ transcript is
**"kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)"**. Never "fully
machine-checked" — H-ENCL survives, and it is where the untrusted producers enter.

---

## 1. Statement diff: every ported declaration against the original source

Source of truth: the clone at `~/rh-lean-work/gomila-ap/repo`, `git rev-parse HEAD` =
`ea09b2f6aa7afe60706b67c87b202126f3149e8c` (the commit named in the attribution). File hashes
re-taken today and matching the verify report byte for byte:

    b1162a0cc3b46c3559e928d04cf1a3c37b4fad6ca1323b65a41ea9948fbe605b  RequestProject/ArgumentPrinciple.lean
    ee3822428e40b210d14c47b044bbbde011d0b72a4cfa2bad0fb2811a04113e82  RequestProject/ArgumentPrincipleGeneral.lean

Ported files as audited:

    ac58463f888254ab71a04f8da2498909498405829f86e245ff167112261736d8  Zeta23/W1/ArgPrinciple/Rect.lean      (492 lines)
    1ce77fe4ead6e5cfc45f0ef5318cb6a5d40443bc32308df73bc8fe0cac4e49cc  Zeta23/W1/ArgPrinciple/General.lean   (249 lines)
    b8392aad5f3438458038bdf4c9b71a660cab2ddd1d63f9a5e7a05771cf503a0e  Zeta23/W1/ArgPrincipleBridge.lean     (459 lines)

### 1.1 Text-level: 45 of 45 statements identical

A mechanical extractor (`theorem`/`lemma`/`def`/`abbrev`, from the keyword to the first top-level
`:=`, paren/bracket-depth aware) was run over both source files and both ported files. It found
**34 declarations in `ArgumentPrinciple.lean` / `Rect.lean` and 11 in
`ArgumentPrincipleGeneral.lean` / `General.lean` — 45 in total, in the same order with the same
names — and `diff` on the two extracted streams is empty in both cases.** So every statement is
byte-for-byte the original, including binder implicitness, hypothesis order and docstring-free
signature text. The declaration counts also reconcile with the upstream commit's arithmetic
(4 theorems + 26 lemmas + 4 defs; 3 theorems + 8 lemmas).

`open` lines are identical in both files (`Set Complex intervalIntegral MeasureTheory` /
`Set Complex Filter Topology MeasureTheory`, plus `scoped Real BigOperators Interval`); the only
namespace change is `ArgumentPrinciple` → `Zeta23.W1.ArgPrinciple`.

### 1.2 Elaborated-statement equality across the two toolchains (a check the port did not run)

Text equality is not meaning equality: the port narrows `import Mathlib` to 7 + 4 specific
modules and moves from Lean `v4.28.0` / Mathlib `8f9d9cff` to `v4.33.0-rc2` / `51e6992`, either
of which could in principle change how a name resolves. So all 45 declarations were
`#check @…`-printed with `pp.fullNames true` **in both trees** — `lake env lean` in
`~/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle` and in
`~/rh-lean-work/zeta-23-v11` — and the two outputs compared after the single substitution
`Zeta23.W1.ArgPrinciple.` → `ArgumentPrinciple.` and whitespace normalization:

    src decls 45   port decls 45
    only in src: []      only in port: []
    DIFFERING: 0

**All 45 elaborated types are identical.** Raw outputs:
`v11/audit/elaborated-statements-source.txt`, `v11/audit/elaborated-statements-port.txt`.

### 1.3 The complete source→port diff (independently regenerated)

`v11/audit/audit-source-to-port.diff` is this audit's own unified diff of the two source files
against the two ported files after undoing the namespace rename. It contains **nothing but**:
the Apache-2.0 + MIT/Aristotle header block, the file-purpose comment, the import replacement,
one docstring cross-reference (`RequestProject.ArgumentPrinciple` → `Zeta23.W1.ArgPrinciple.Rect`),
and eight proof-level edits:

| Site | Edit |
|---|---|
| `continuousOn_logDeriv`, `windingRect_prod_mul` | `continuousOn_finset_sum` → `continuousOn_finsetSum` (deprecated upstream 2026-04-08) |
| `hasDerivAt_edge_antiderivative` (h1, h2) | `convert h using 1` → `refine h.congr_deriv ?_` |
| `hasDerivAt_edge_antiderivative` (h3) | `convert h3 using 1; exact key.symm` → `rw [← key]; exact h3` |
| `integral_inv_ofReal_add_const_mul_I` | `simpa [logDeriv_apply] using h` → `exact h` |
| `finite_zeros_of_isCompact` | `push_neg at h4` → `push Not at h4` |
| `windingRect_factored`, `windingRect_factored_div` | `set_option linter.unusedVariables false in` prefixed (observation O1) |

Every one is inside a proof or a `set_option … in` prefix. **No statement, hypothesis, binder or
conclusion is touched anywhere.** This matches the port report's own list.

---

## 2. `ArgPrincipleBridge.lean`, read line by line

### 2.1 Is H-AP proved in exactly the form `Soundness.lean` declares?

`Soundness.lean` is **unmodified**: `diff -rq` of the v11 tree's `Zeta23/W1` against both the hot
tree `~/rh-lean-work/zeta-23-lean-main/Zeta23/W1` and the program's `lean/Zeta23/W1` reports the
two new paths as the *only* difference; `Soundness.lean`, `Checker.lean`, `Examples.lean`,
`Format.lean`, `Instances.lean` are identical in all three. `grep -rn "def RectArgPrinciple"`
over the whole v11 tree returns exactly one hit, `Soundness.lean:173`. There is no shadowing
definition.

`#print Zeta23.W1.RectArgPrinciple` in the built environment reproduces Soundness's body exactly
(∀ s₁ s₂ t₁ t₂, 1/2 < s₁ → s₁ ≤ s₂ → s₂ < 1 → t₁ < t₂ → ∀ U, IsOpen U → rectClosed ⊆ U →
DifferentiableOn ℂ f U → boundary nonvanishing → ∃ Z with the winding identity and the two
counting consequences). And:

    Zeta23.W1.rectArgPrinciple_of_local : ∀ (f : ℂ → ℂ), Zeta23.W1.RectArgPrinciple f
    Zeta23.W1.rectArgPrinciple_riemannZeta : Zeta23.W1.RectArgPrinciple riemannZeta

So H-AP is proved **for every `f`, with no side condition of any kind** — the `Prop` itself
carries `DifferentiableOn ℂ f U` as a hypothesis, so no analytic input about ζ is consumed
anywhere in the file (the scout's route-(b) entire surrogate `(s−1)ζ(s)` was not needed, and no
ζ fact appears in `ArgPrincipleBridge.lean` other than the one-line instantiation).

### 2.2 Exactly the rectangles the checker admits?

`Checker.lean` line 27, clause **C2**: `q₁ < 2p₁; p₁q₂ ≤ p₂q₁; p₂ < q₂; a₁b₂ < a₂b₁`, i.e.
**½ < σ₁ ≤ σ₂ < 1 (non-strict in the middle) and T₁ < T₂ (strict)**. `cert_of_checkW1` converts
these with `ratVal_lt_of_cross`/`ratVal_le_of_cross` and feeds `hs12le : sigma1 d ≤ sigma2 d`.
`RectArgPrinciple` quantifies over precisely `1/2 < s₁ → s₁ ≤ s₂ → s₂ < 1 → t₁ < t₂`, and
`rectArgPrinciple_of_local` opens with `intro s₁ s₂ t₁ t₂ _hhalf hs12 _hs2 ht12 U hU hRU hf hbd`
— the same binders, in the same order, with `_hhalf` and `_hs2` **unused** (the proof is stronger
than required: it never uses ½ < σ₁ or σ₂ < 1).

The degenerate rectangle **σ₁ = σ₂ is handled**, not excluded: `rcases hs12.lt_or_eq with hs | hs`
splits, and the equality branch supplies `Z = 0` with
(i) the four increments summing to 0 — the two horizontal edges are point segments
(`w − z = 0`, so the integrand is identically 0 and `logDerivSegIntegral = 0` unconditionally),
and the two vertical edges are reverses of each other (`logDerivSegIntegral_vert` +
`intervalIntegral.integral_symm`);
(ii) vacuous, since `rectOpen s₁ s₁ t₁ t₂` is empty (`lt_trans hs.1 hs.2.1` gives `s₁ < s₁`);
(iii) vacuous by `omega` from `1 ≤ 0`.
This closes the scout's gap **G4** without tightening C2b, so `FORMAT.md`'s displayed hypothesis
text is unchanged.

### 2.3 No added hypothesis anywhere

* **Strictness:** none added — see §2.2.
* **Nonvanishing:** the only nonvanishing input is `hbd : ∀ s ∈ rectBdry …, f s ≠ 0`, which is
  already a hypothesis of `RectArgPrinciple`. Nothing is required in the interior. The `hne`
  ("`f` not identically zero on the rectangle") that the generalized identity-theorem lemmas need
  is **derived**, not assumed: `⟨cpt s₁ t₁, hzR, hbd' _ (mem_RectFrontier_left_corner _ _)⟩` — the
  lower-left corner is on the frontier, so `hbd` gives it.
* **Integrability:** none assumed. The two change-of-variables lemmas
  `logDerivSegIntegral_horiz` and `logDerivSegIntegral_vert` and the four-edge identity
  `edge_sum_eq_rectIntegral` are stated with **no hypotheses at all** (junk-value safe); they rest
  on `Soundness.lean`'s `smul_comp_integral`, itself hypothesis-free
  (`intervalIntegral.smul_integral_comp_mul_add`). Integrability on the path actually used is a
  *consequence* of the Cauchy machinery, never an input — §2.5 exhibits a witness proving the
  increments are not the junk value.
* **Connectivity:** `U` is required only to be open. The identity theorem is applied on the closed
  rectangle, which the new `isPreconnected_Rect` proves preconnected; `U` itself need not be. This
  is strictly weaker than the scout's route-(a) sketch (which assumed `U` preconnected) and so
  cannot over-assume.

### 2.4 Orientation and sign — the anti-cheat point of §8.2

Checked by hand against the definitions, because a sign error here is exactly what the displayed
statement exists to prevent.

`rectIntegral g z w` (ported verbatim) `= ∫_{z.re}^{w.re} g(x + i z.im) − ∫_{z.re}^{w.re} g(x + i w.im)
+ i∫_{z.im}^{w.im} g(w.re + iy) − i∫_{z.im}^{w.im} g(z.re + iy)` — Mathlib's positively-oriented
boundary convention. With `z := cpt s₁ t₁` (lower-left) and `w := cpt s₂ t₂` (upper-right),
expanding the four `logDerivSegIntegral`s of the §4 traversal by
`logDerivSegIntegral_horiz`/`_vert` and `intervalIntegral.integral_symm` gives term-by-term
exactly those four integrals, in the same signs — which is what `edge_sum_eq_rectIntegral` proves
and what I re-derived independently. `windingRect H z w = (2πi)⁻¹ · rectIntegral (logDeriv H) z w`
and `windingRect_eq_sum_analyticOrder(_on)` equates it to `∑ analyticOrderNatAt ≥ 0`. The port's
own kernel-checked sanity theorem `windingRect_id_eq_one : windingRect id (−1−i) (1+i) = 1`
confirms the sign for the same corner assignment. So bottom → right → top → left is the
counterclockwise traversal and the winding is **+Z**, not −Z.

### 2.5 Non-vacuity and non-junk: an independent witness (this audit's own)

`v11/audit/AuditWitness.lean`, compiled today against the built tree, proves from
`rectArgPrinciple_of_local` alone, for `f = (· − c)` with `c = 13/20 + (21/2)i` and the
checker-admissible rectangle `[3/5, 7/10] × [10, 11]` (½ < 3/5 ≤ 7/10 < 1, 10 < 11), `U = univ`:

    theorem auditWitness : ∃ Z : ℕ, 1 ≤ Z ∧ 2 * Real.pi * Z = (the four §4 argIncrements summed)

`'Zeta23.W1.auditWitness' depends on axioms: [propext, Classical.choice, Quot.sound]`. Because
`Z ≥ 1`, the right-hand side is `2πZ > 0`. So on the path H-AP actually takes, the four
`argIncrement`s are **not** the Lean junk value, the winding of a counterclockwise traversal
around one interior zero is **positive**, and the discharged hypothesis is not vacuously true.
This is the strongest of the checks here and it was not run by the builders.

### 2.6 `cert_of_checkW1_ap` versus `cert_of_checkW1`

Verbatim `#check` output from the built environment (`v11/audit/audit-print-axioms.log`):

    Zeta23.W1.cert_of_checkW1_ap : ∀ (d : Zeta23.W1.W1Data),
      Zeta23.W1.checkW1 d = true →
        Zeta23.W1.W1EnclOK riemannZeta d →
          (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ Zeta23.W1.T1 d < ρ.im ∧ ρ.im < Zeta23.W1.T2 d) ∧
            (d.m = 0 → ∀ s ∈ Zeta23.W1.W1Rect d, riemannZeta s ≠ 0)
    Zeta23.W1.cert_of_checkW1 : ∀ (d : Zeta23.W1.W1Data),
      Zeta23.W1.checkW1 d = true →
        Zeta23.W1.W1EnclOK riemannZeta d →
          Zeta23.W1.RectArgPrinciple riemannZeta →
            (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ Zeta23.W1.T1 d < ρ.im ∧ ρ.im < Zeta23.W1.T2 d) ∧
              (d.m = 0 → ∀ s ∈ Zeta23.W1.W1Rect d, riemannZeta s ≠ 0)

**Same conclusion, character for character. Strictly fewer displayed hypotheses: `hAP` is gone and
nothing replaced it.** The proof is the one-liner
`cert_of_checkW1 d hc hEncl rectArgPrinciple_riemannZeta`, so the conclusion cannot have drifted.

Independent smoke test (`v11/audit/AuditSmoke.lean`, this audit's own, compiled today): applying
`cert_of_checkW1_ap` to `exampleRefutation` with `exampleRefutation_accepted` (a `decide +kernel`
fact already in `Examples.lean`) and to `exampleExclusion` yields the ζ conclusions from
**H-ENCL alone**, on `[propext, Classical.choice, Quot.sound]`. The theorem therefore has content
on a transcript the checker really accepts.

---

## 3. Build, reproduced here

    export PATH="$HOME/.elan/bin:$PATH"
    rm -rf .lake/build/lib/lean/Zeta23/W1/ArgPrinciple .lake/build/lib/lean/Zeta23/W1/ArgPrincipleBridge.*
    lake build Zeta23.W1.ArgPrincipleBridge

    ✔ [3143/3145] Built Zeta23.W1.ArgPrinciple.Rect (1.9s)
    ✔ [3144/3145] Built Zeta23.W1.ArgPrinciple.General (1.5s)
    ✔ [3145/3145] Built Zeta23.W1.ArgPrincipleBridge (1.7s)
    Build completed successfully (3145 jobs).

6 s wall from deleted oleans (upstream cached), exit 0, **no warnings and no errors**. Toolchain
`leanprover/lean4:v4.33.0-rc2`; Mathlib `51e6992efd06126df61a496bebf8f49482a4e129` per
`lake-manifest.json` and `.lake/packages/mathlib` HEAD.

## 4. `#print axioms` — all 63 new declarations plus their consumers

Full log: `v11/audit/audit-print-axioms.log`. Every one of

* the **18** declarations of `ArgPrincipleBridge.lean` (`isPreconnected_Rect`,
  `analyticOrderAt_ne_top_of_analyticOnNhd`, `exists_factor_pow_sub_on`, `exists_factor_prod_on`,
  `finite_zeros_of_isCompact_on`, `finite_zeros_Rect_on`, `continuousOn_logDeriv_on`,
  `rectIntegral_logDeriv_eq_zero_on`, `windingRect_eq_sum_analyticOrder_on`, `cpt_eq`, `Rect_cpt`,
  `RectFrontier_cpt`, `logDerivSegIntegral_horiz`, `logDerivSegIntegral_vert`,
  `edge_sum_eq_rectIntegral`, `rectArgPrinciple_of_local`, `rectArgPrinciple_riemannZeta`,
  `cert_of_checkW1_ap`),
* the **45** ported declarations (4 defs + 41 theorems/lemmas),
* and, for context, `cert_of_checkW1`, `RectArgPrinciple`, `W1EnclOK`,

reports exactly

    depends on axioms: [propext, Classical.choice, Quot.sound]

(`checkW1` reports "does not depend on any axioms"). **No `sorryAx`, no `Lean.ofReduceBool`, no
`Lean.trustCompiler`, no new axiom of any kind.** In particular
`'Zeta23.W1.cert_of_checkW1_ap' depends on axioms: [propext, Classical.choice, Quot.sound]`, and
so do this audit's own `auditSmoke_refutation`, `auditSmoke_exclusion` and `auditWitness`.

## 5. Escape-hatch grep

    grep -n -E "sorry|admit|native_decide|axiom|unsafe|opaque|implemented_by|extern|decide|@\[csimp\]|partial " \
      Zeta23/W1/ArgPrinciple/Rect.lean Zeta23/W1/ArgPrinciple/General.lean Zeta23/W1/ArgPrincipleBridge.lean
    → no output, exit 1

Not one match, comments included; `decide` does not occur as a substring, which also rules out
`native_decide` and `decide +kernel` in the new files. A second grep for `@[`, `attribute`,
`instance`, `local`, `scoped`, `macro`, `notation`, `syntax`, `elab` also returns nothing (exit 1):
the new files register no attribute, instance, notation or macro, so they cannot perturb the
elaboration of any existing module.

## 6. Attribution, headers and NOTICE

* **Headers.** All three new files carry the program's Apache-2.0 block (Copyright (c) 2026 Kunal
  Tyagi, SPDX-License-Identifier: Apache-2.0, plus the "addition to the Zeta23 library / Zeta23 is
  Copyright 2026 Anthropic, PBC" paragraph) **and** the required notice, verbatim in content:
  "Portions ported from the Lean development in
  github.com/judegomila/dbn-lambda-01787854-candidate-audit (branch
  lean/certificate-and-argument-principle, commit ea09b2f), Copyright (c) 2026 Jude Gomila, MIT
  License, generated with Harmonic Aristotle; ported and adapted here." (line-wrapped, followed by
  "The MIT license text is reproduced in the program's NOTICE file.").
* **Commit hash.** `ea09b2f` is correct: `git rev-parse HEAD` in the clone is
  `ea09b2f6aa7afe60706b67c87b202126f3149e8c`, the head recorded by both the scout and the verify
  agent.
* **NOTICE.** `rh-program/NOTICE` carries a dated section "2026-09-02 — Rectangle argument
  principle (Lean), ported from the Gomila audit repository" and a dated addendum
  "2026-09-02 (addendum) — H-AP discharge module adapting the ported argument principle", both
  appended, with the older text untouched. `LICENSE` was not modified.
* **MIT text verbatim — byte-checked.** The block reproduced in NOTICE was extracted
  programmatically and `diff`ed against lines 1–21 of the source repository's `LICENSE`: **no
  difference**. NOTICE's claimed hash of that file,
  `cf3cef645439d98d6a4e153699e52842adcf294e5074225770d46044e8cf77f4`, matches `shasum -a 256
  LICENSE` in the clone. The "Scope" trailer is correctly described as continuing beyond the
  quoted block rather than being silently dropped.

## 7. Observations (recorded; none blocks the verdict)

* **O1 — linter suppression on two upstream theorems.** `Rect.lean` prefixes
  `windingRect_factored` and `windingRect_factored_div` with
  `set_option linter.unusedVariables false in`, silencing the six warnings the upstream build
  emitted (`hre`, `him`, `hm` unused). The statements are unchanged, unused hypotheses only make a
  theorem weaker-to-apply and never unsound, and neither theorem is on the path to
  `cert_of_checkW1_ap` (the bridge uses `windingRect_prod_mul`). Documented in port-notes §4.
  Recorded, not a defect — but a future re-port should not silently inherit the suppression.
* **O2 — the new modules are not in the library root.** `Zeta23.lean` does not import
  `Zeta23.W1.ArgPrinciple.Rect/General` or `Zeta23.W1.ArgPrincipleBridge`, so a bare `lake build`
  (default target `Zeta23`) does not compile them; they need
  `lake build Zeta23.W1.ArgPrincipleBridge`. This is the existing convention for W1 additions
  (`W1/Instances.lean`, `W1/AuditO*.lean` are likewise absent from `Zeta23.lean`), so nothing was
  changed — but the build command belongs in the README, and it is now there.
* **O3 — FORMAT.md §8.2's older success-criterion wording is now inaccurate.** It reads
  "converts into a kernel-checked disproof modulo the two displayed hypotheses; fully
  kernel-checked after v1.1". With H-AP discharged, H-ENCL remains, so "fully kernel-checked" is
  wrong. Per the task the older text is not rewritten; a dated paragraph appended to §8 records
  the discharge and supersedes that phrase.
* **O4 — Mathlib short-hash discrepancy: diagnosed and confirmed, not resolved here.**
  `results/d1-m1/AUDIT-F.md` line 151 records Mathlib `123d1576…`. Independently verified today:
  `123d15766ba49356c02ebad2a4462dfe12d79899` is the **`plausible`** package revision, the first
  entry of `lake-manifest.json`; the `mathlib` entry is
  `51e6992efd06126df61a496bebf8f49482a4e129`, agreeing with `lean/README.md` and with
  `git rev-parse HEAD` in `.lake/packages/mathlib`. AUDIT-F read the wrong manifest line. The fix
  belongs to the next AUDIT-F touch.
* **O5 — provenance of the ported mathematics.** The 45 ported declarations are
  machine-generated (Harmonic Aristotle) and were, before this program touched them, an
  unverified third-party development. They are now: rebuilt on the program's pinned toolchain,
  axiom-audited declaration by declaration, statement-diffed at both text and elaborated-type
  level against the original, and — decisively — the only thing that matters downstream is
  `RectArgPrinciple riemannZeta`, which the Lean kernel has checked. Faithfulness-to-intent
  worries about *their* definitions do not propagate, because the D1 statement being discharged is
  `Soundness.lean`'s own, written before the branch was known.

## 8. What this does and does not establish

**Establishes.** `Zeta23.W1.RectArgPrinciple riemannZeta` is a theorem of the program's Lean
development on the three standard axioms, for exactly the rectangles clause C2 admits (σ₁ = σ₂
included) and with no hypothesis beyond those the `Prop` already displays; and
`Zeta23.W1.cert_of_checkW1_ap` re-proves W1 checker soundness with the same conclusion and one
displayed hypothesis fewer. D-R3's v1.1 obligation for H-AP is met.

**Does not establish.** H-ENCL is untouched and remains the single displayed hypothesis: the
untrusted producers' interval arithmetic still enters the trusted statement there, and FORMAT.md
§8.1's "what the checker cannot see" note (mis-scaled `K`/`A`, rotated rows, negated boxes ⇒ a
false H-ENCL and a vacuous conclusion) stands unchanged. The correct public sentence remains
"kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)".

## 9. Files copied into the program after this verdict

`Zeta23/W1/ArgPrinciple/Rect.lean`, `Zeta23/W1/ArgPrinciple/General.lean` and
`Zeta23/W1/ArgPrincipleBridge.lean` were copied from `~/rh-lean-work/zeta-23-v11` into
`rh-program/lean/Zeta23/W1/` preserving paths (hashes as in §1). `rh-program/lean/README.md` was
updated (table rows, the axiom sentence, a v1.1 paragraph with the MIT attribution and the build
command) and a dated paragraph was appended to `results/d1-m1/FORMAT.md` §8. No file in
`~/rh-lean-work/zeta-23-lean-main` was read-modified or written; the orchestrator merges there.
Audit artifacts: `results/d1-m1/v11/audit/`.
