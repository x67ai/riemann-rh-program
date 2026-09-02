# Port notes: Gomila/Aristotle rectangle argument principle → `Zeta23.W1.ArgPrinciple.{Rect,General}`

**Date:** 2026-09-02 (Session 14, D1 v1.1 port agent; D-R3, first deliverable component 1).
**Status:** PORT COMPLETE — both modules build clean (no errors, no warnings) on the program's
toolchain; all 45 declarations depend on `[propext, Classical.choice, Quot.sound]` only; zero
statement-level differences from the originals. Nothing has been copied into the program root's
`lean/` directory yet (this file and `../../../NOTICE` are the only program-root writes).
**Standing order 5:** every block below is pasted from the commands as run today.

**What this is and is not.** This port makes the branch's theorems available on the program's
toolchain. It does NOT discharge H-AP: the theorems are for ENTIRE functions (`Differentiable ℂ H`),
in the branch's own `Rect`/`rectIntegral`/`windingRect` vocabulary; the six gaps G1–G6 of
`../gomila-lean-branch-scout.md` §3.2 remain except G6 (toolchain drift), which this file closes.
Honest vocabulary after the bridge lands: "kernel-checked modulo the displayed hypothesis H-ENCL";
never "fully machine-checked".

## 0. Source, target, provenance

**Source:** `~/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle/RequestProject/
{ArgumentPrinciple,ArgumentPrincipleGeneral}.lean`, branch `lean/certificate-and-argument-principle`
@ `ea09b2f6aa7afe60706b67c87b202126f3149e8c` of github.com/judegomila/dbn-lambda-01787854-candidate-audit
(MIT, Copyright (c) 2026 Jude Gomila; generated with Harmonic Aristotle). SHA-256 of the sources as
ported: `b1162a0cc3b46c3559e928d04cf1a3c37b4fad6ca1323b65a41ea9948fbe605b` (ArgumentPrinciple.lean,
444 lines) and `ee3822428e40b210d14c47b044bbbde011d0b72a4cfa2bad0fb2811a04113e82`
(ArgumentPrincipleGeneral.lean, 215 lines) — identical to the hashes in
`../gomila-lean-branch-verify.md` §1.2. Verified today to build on Lean v4.28.0 + Mathlib `8f9d9cff`
with standard axioms only (same file, §3).

**Target:** APFS clone `~/rh-lean-work/zeta-23-v11` of the program's hot tree
`~/rh-lean-work/zeta-23-lean-main` (`cp -c -R`, 12:56:10 → 12:56:27 IST, 17 s; `.lake` 9.4G shared
by clonefile, no extra disk). Toolchain `leanprover/lean4:v4.33.0-rc2` (`lean --version`: "Lean
(version 4.33.0-rc2, arm64-apple-darwin24.6.0, commit d8b18978322de05a8f3dba51ef03cf5461676c17,
Release)"; Lake 5.0.0-src+d8b1897). Mathlib rev per `lake-manifest.json` =
`51e6992efd06126df61a496bebf8f49482a4e129`; `git rev-parse HEAD` in `.lake/packages/mathlib` agrees.
The hot tree was not touched (no build, no edit; `pgrep -fl "lake build"` showed no other lake
process at each of my builds). `pmset -g therm` before each heavy step: "No CPU power status has
been recorded" (no `CPU_Speed_Limit` line — no throttling recorded).

**Known hash discrepancy — reported, not resolved.** `lean/README.md` lines 25 and 52 give Mathlib
`51e6992e…`, agreeing with the manifest. `results/d1-m1/AUDIT-F.md` line 151 records "Mathlib
`123d1576…`". That short hash is the manifest's **`plausible`** package rev
(`123d15766ba49356c02ebad2a4462dfe12d79899`), which is the first `packages[]` entry of
`lake-manifest.json`; the Mathlib entry is `51e6992…`. So AUDIT-F read the wrong manifest line; the
tree's Mathlib was `51e6992` throughout. Fix belongs to the next AUDIT-F touch, not to this port.

**New files (in the clone only):**

| ported module | file | from | lines |
|---|---|---|---|
| `Zeta23.W1.ArgPrinciple.Rect` | `~/rh-lean-work/zeta-23-v11/Zeta23/W1/ArgPrinciple/Rect.lean` | `RequestProject/ArgumentPrinciple.lean` | 492 (orig. 444) |
| `Zeta23.W1.ArgPrinciple.General` | `~/rh-lean-work/zeta-23-v11/Zeta23/W1/ArgPrinciple/General.lean` | `RequestProject/ArgumentPrincipleGeneral.lean` | 249 (orig. 215) |

SHA-256 of the ported files: Rect.lean
`ac58463f888254ab71a04f8da2498909498405829f86e245ff167112261736d8`, General.lean
`1ce77fe4ead6e5cfc45f0ef5318cb6a5d40443bc32308df73bc8fe0cac4e49cc`. Both carry the program's
Apache-2.0 header (the one used by `Zeta23/W1/Soundness.lean`, "This file contains no code from
that library") followed by the required notice block ("Portions ported from the Lean development
in github.com/judegomila/dbn-lambda-01787854-candidate-audit (branch
lean/certificate-and-argument-principle, commit ea09b2f), Copyright (c) 2026 Jude Gomila, MIT
License, generated with Harmonic Aristotle; ported and adapted here.") and a port-record comment.
The MIT text was added to the program root's `NOTICE` (created today — it did not exist — with a
dated 2026-09-02 section; `LICENSE` untouched, and the program root has no LICENSE file to touch).
Namespace `ArgumentPrinciple` → `Zeta23.W1.ArgPrinciple`; the `open` lines are the originals.

The ported files were assembled mechanically (Python) from the originals: header + port comment +
import list prepended, the original `import` lines dropped, `namespace`/`end` renamed, the module
docstring's cross-reference `` `RequestProject.ArgumentPrinciple` `` → `` `Zeta23.W1.ArgPrinciple.Rect` ``;
then only the proof-level edits of §4 were made by hand. The complete `diff -u` against the
originals is in §8.

## 1. Imports (whole-Mathlib import replaced; no `import Mathlib`)

`Rect.lean`:

    import Mathlib.Analysis.Complex.CauchyIntegral
    import Mathlib.Analysis.Calculus.LogDeriv
    import Mathlib.Analysis.Calculus.FDeriv.Analytic
    import Mathlib.Analysis.Complex.RealDeriv
    import Mathlib.Analysis.SpecialFunctions.Log.Deriv
    import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
    import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus

What each supplies: `CauchyIntegral` — `Complex.integral_boundary_rect_eq_zero_of_differentiableOn`
(line 295), `Differentiable.analyticAt` (line 649), and transitively `Complex.reProdIm` (`×ℂ`),
interval integrals, `Set.uIcc`; `LogDeriv` — `logDeriv`, `logDeriv_apply/_mul/_div/_prod/_fun_pow`;
`FDeriv.Analytic` — `AnalyticAt.deriv`; `RealDeriv` — `HasDerivAt.ofReal_comp`; `Log.Deriv` —
`Real.hasDerivAt_log`; `ArctanDeriv` — `Real.hasDerivAt_arctan` (and `Arctan`:
`Real.arctan_inv_of_pos/_neg`, `Real.arctan_neg`); `FundThmCalculus` —
`intervalIntegral.integral_eq_sub_of_hasDerivAt` (line 1148; `integral_comp_sub_right` is in
`IntervalIntegral.Basic`, transitively imported).

`General.lean`:

    import Mathlib.Analysis.Analytic.Order
    import Mathlib.Analysis.Analytic.IsolatedZeros
    import Mathlib.Algebra.BigOperators.Finprod
    import Mathlib.Topology.Compactness.Compact
    import Zeta23.W1.ArgPrinciple.Rect

`Order` — `analyticOrderAt`, `analyticOrderNatAt` (line 61), `analyticOrderAt_eq_top` (75),
`AnalyticAt.analyticOrderAt_ne_top` (113), `AnalyticAt.analyticOrderAt_eq_zero` (133),
`analyticOrderAt_id` (185), `analyticOrderAt_mul` (497); `IsolatedZeros` —
`AnalyticOnNhd.eqOn_zero_of_preconnected_of_frequently_eq_zero` (214); `Finprod` — `∑ᶠ`,
`finsum_mem_coe_finset`; `Compactness.Compact` — `Set.Infinite.exists_accPt_of_subset_isCompact`
(925); `accPt_iff_frequently_nhdsNE` (`Topology/ClusterPt.lean` 217) comes transitively. Some of
these modules are also reachable transitively through `Rect`; they are listed explicitly because
this Mathlib uses the module system (`module` / `public import`; e.g. `LogDeriv.lean` imports
`IsolatedZeros` **non**-publicly), so nothing is relied on that is not imported by name.

No tactic module needed importing: `field_simp`, `linear_combination`, `positivity`, `fun_prop`,
`filter_upwards`, `push_cast`, `norm_num`, `linarith`, `exact_mod_cast`, `push` all arrived through
the analysis modules' public imports (the first build reported no unknown identifier or tactic).

## 2. Name table original → ported

Every original `ArgumentPrinciple.X` is `Zeta23.W1.ArgPrinciple.X`, same `X`, same declaration
kind, same order in the file. The 45 names (4 defs + 30 lemmas/theorems in Rect, 11 in General):

| # | original (`ArgumentPrinciple.`) | ported (`Zeta23.W1.ArgPrinciple.`) | kind | module |
|---|---|---|---|---|
| 1 | `Rect` | `Rect` | def | Rect |
| 2 | `rectIntegral` | `rectIntegral` | noncomputable def | Rect |
| 3 | `windingRect` | `windingRect` | noncomputable def | Rect |
| 4 | `RectFrontier` | `RectFrontier` | def | Rect |
| 5 | `mem_Rect` | `mem_Rect` | lemma | Rect |
| 6 | `RectFrontier_subset_Rect` | `RectFrontier_subset_Rect` | lemma | Rect |
| 7 | `mem_RectFrontier_bot` | `mem_RectFrontier_bot` | lemma | Rect |
| 8 | `mem_RectFrontier_top` | `mem_RectFrontier_top` | lemma | Rect |
| 9 | `mem_RectFrontier_right` | `mem_RectFrontier_right` | lemma | Rect |
| 10 | `mem_RectFrontier_left` | `mem_RectFrontier_left` | lemma | Rect |
| 11 | `continuousOn_edge_bot` | `continuousOn_edge_bot` | lemma | Rect |
| 12 | `continuousOn_edge_top` | `continuousOn_edge_top` | lemma | Rect |
| 13 | `continuousOn_edge_right` | `continuousOn_edge_right` | lemma | Rect |
| 14 | `continuousOn_edge_left` | `continuousOn_edge_left` | lemma | Rect |
| 15 | `rectIntegral_congr` | `rectIntegral_congr` | lemma | Rect |
| 16 | `rectIntegral_add` | `rectIntegral_add` | lemma | Rect |
| 17 | `rectIntegral_sub` | `rectIntegral_sub` | lemma | Rect |
| 18 | `rectIntegral_const_mul` | `rectIntegral_const_mul` | lemma | Rect |
| 19 | `rectIntegral_sum` | `rectIntegral_sum` | lemma | Rect |
| 20 | `rectIntegral_eq_zero_of_differentiableOn` | `rectIntegral_eq_zero_of_differentiableOn` | lemma | Rect |
| 21 | `arctan_add_arctan_inv_of_pos` | `arctan_add_arctan_inv_of_pos` | lemma | Rect |
| 22 | `arctan_add_arctan_inv_of_neg` | `arctan_add_arctan_inv_of_neg` | lemma | Rect |
| 23 | `ofReal_add_const_mul_I_ne_zero` | `ofReal_add_const_mul_I_ne_zero` | lemma | Rect |
| 24 | `hasDerivAt_edge_antiderivative` | `hasDerivAt_edge_antiderivative` | lemma | Rect |
| 25 | `integral_inv_ofReal_add_const_mul_I` | `integral_inv_ofReal_add_const_mul_I` | lemma | Rect |
| 26 | `integral_inv_const_add_ofReal_mul_I` | `integral_inv_const_add_ofReal_mul_I` | lemma | Rect |
| 27 | `arctan_rect_sum` | `arctan_rect_sum` | lemma | Rect |
| 28 | `rectIntegral_inv_sub` | `rectIntegral_inv_sub` | theorem | Rect |
| 29 | `continuousOn_logDeriv` | `continuousOn_logDeriv` | lemma | Rect |
| 30 | `rectIntegral_logDeriv_eq_zero` | `rectIntegral_logDeriv_eq_zero` | lemma | Rect |
| 31 | `sub_ne_zero_of_mem_RectFrontier` | `sub_ne_zero_of_mem_RectFrontier` | lemma | Rect |
| 32 | `windingRect_prod_mul` | `windingRect_prod_mul` | theorem | Rect |
| 33 | `windingRect_factored` | `windingRect_factored` | theorem | Rect |
| 34 | `windingRect_factored_div` | `windingRect_factored_div` | theorem | Rect |
| 35 | `analyticOrderAt_ne_top` | `analyticOrderAt_ne_top` | lemma | General |
| 36 | `exists_factor_pow_sub` | `exists_factor_pow_sub` | lemma | General |
| 37 | `exists_factor_prod` | `exists_factor_prod` | lemma | General |
| 38 | `isCompact_Rect` | `isCompact_Rect` | lemma | General |
| 39 | `finite_zeros_of_isCompact` | `finite_zeros_of_isCompact` | lemma | General |
| 40 | `finite_zeros_Rect` | `finite_zeros_Rect` | lemma | General |
| 41 | `mem_RectFrontier_left_corner` | `mem_RectFrontier_left_corner` | lemma | General |
| 42 | `mem_Ioo_of_zero_mem_Rect` | `mem_Ioo_of_zero_mem_Rect` | lemma | General |
| 43 | `windingRect_eq_sum_analyticOrder` | `windingRect_eq_sum_analyticOrder` | theorem | General |
| 44 | `windingRect_eq_finsum_analyticOrder` | `windingRect_eq_finsum_analyticOrder` | theorem | General |
| 45 | `windingRect_id_eq_one` | `windingRect_id_eq_one` | theorem | General |

## 3. Statement-level differences: NONE

Checked mechanically: for each of the 45 declarations, the text from the `theorem`/`lemma`/`def`
keyword to the first `:=` was extracted from the original and the ported file and compared as
strings (script run 13:03 IST; output verbatim):

    == ArgumentPrinciple.lean (34 decls) vs Rect.lean (34 decls)
    == ArgumentPrincipleGeneral.lean (11 decls) vs General.lean (11 decls)
    TOTAL decls compared: 45; statement differences: 0

(The `names:` lines of that output are the table above.) The `open` / `open scoped` lines are the
originals, so notation (`[[a, b]]`, `×ℂ`, `π`, `∑ᶠ`) resolves as in the source. The only things
placed in front of a statement are two `set_option linter.unusedVariables false in` lines (§4,
item 7), which change no statement.

## 4. Mathlib API drift hit (8f9d9cff, 2026-02-16 → 51e6992, 2026-08-03) and every proof-level edit

First build (13:00:04 IST, `lake build Zeta23.W1.ArgPrinciple.Rect`, 8.8 s): 4 errors, 2
deprecation warnings, 6 unused-variable warnings; all in `Rect.lean`. `General.lean` first build
(13:02:29): 0 errors, 1 deprecation warning. Everything below is the complete list of changes
inside proofs; nothing else in any proof was touched.

1. **`continuousOn_finset_sum` → `continuousOn_finsetSum`** (two sites: `rectIntegral_sum`,
   `windingRect_prod_mul`). Deprecated alias since 2026-04-08 (`Mathlib/Topology/Algebra/
   Monoid.lean` 964: `@[deprecated (since := "2026-04-08")] alias continuousOn_finset_sum :=
   continuousOn_finsetSum`); the old name still elaborates with a warning; replaced to keep the
   build warning-free.
2. **`push_neg` → `push Not`** (one site: `mem_Ioo_of_zero_mem_Rect` in General). Build warning:
   "`push_neg` has been deprecated. Prefer using `push Not` instead."
3. **`hasDerivAt_edge_antiderivative`, sub-proof `h1`:** `convert h using 1; field_simp` failed
   ("`field_simp` made no progress"): the new `convert` leaves the function-side congruence goal
   open first instead of closing it. Replaced by `refine h.congr_deriv ?_; field_simp`
   (`HasDerivAt.congr_deriv`; `refine` unifies the `Function.comp` form at default transparency).
4. **Same lemma, sub-proof `h2`:** `convert h using 1; ring` failed the same way ("`ring_nf` made
   no progress"); replaced by `refine h.congr_deriv ?_; ring`.
5. **Same lemma, final step:** `convert h3 using 1; exact key.symm` failed with "Type mismatch …
   expected to have type `addCommGroup = instNormedAddCommGroup.toAddCommGroup`" — `convert` now
   exposes an instance-equality goal first. Replaced by `rw [← key]; exact h3` (rewrite the goal's
   derivative with `key` and close by the term).
6. **`continuousOn_logDeriv`:** `simpa [logDeriv_apply] using h` failed (simp no longer rewrites
   the *unapplied* `logDeriv F` in `ContinuousOn (logDeriv F) _`). Replaced by `exact h`: `logDeriv
   f = deriv f / f` (`LogDeriv.lean` 34) and `logDeriv_apply` is `rfl`, so the two `ContinuousOn`
   statements are definitionally equal.
7. **Unused-variable linter** (`hre`, `him`, `hm` in `windingRect_factored` and
   `windingRect_factored_div` — the original build on v4.28.0 emitted the same six warnings;
   `../gomila-lean-branch-verify.md` §3.2). The hypotheses are part of the requested statement and
   unused by design (the original docstring says so). Kept byte-for-byte; silenced with
   `set_option linter.unusedVariables false in` placed before each theorem's docstring, with a
   comment. No statement change.

**Drift the scout expected that did NOT occur.** Scout §3.2 G6 listed `finsum_mem_coe_finset` as
"absent" from the program's Mathlib. It is present: it is generated by `@[to_additive]` from
`finprod_mem_coe_finset` (`Mathlib/Algebra/BigOperators/Finprod.lean` 537–538), so a plain grep
for the additive name finds nothing. `windingRect_eq_finsum_analyticOrder` compiles unchanged.
Every other Mathlib name the scout spot-checked resolved as-is: `Finset.induction_on` still takes
`| insert i s hi ih`, `logDeriv_prod`/`logDeriv_fun_pow` have the same implicit-argument shape,
`Set.Infinite.exists_accPt_of_subset_isCompact`, `AnalyticAt.analyticOrderAt_ne_top`,
`analyticOrderAt_mul`, `HasDerivAt.ofReal_comp`, `integral_eq_sub_of_hasDerivAt`,
`integral_comp_sub_right` unchanged.

**Whole-Mathlib import:** not needed (reported for the record: none).

## 5. Build log and times (all in `~/rh-lean-work/zeta-23-v11`, `lake build <module>`; logs in its `scratch/`)

| step | time (IST) | wall | result | log |
|---|---|---|---|---|
| APFS clone of the hot tree | 12:56:10–12:56:27 | 17 s | ok | — |
| build Rect, attempt 1 (verbatim proofs) | 13:00:04–13:00:15 | 11.0 s (lean 8.8 s) | 4 errors | `scratch/build-rect-1.log` |
| build Rect, attempt 2 (proof fixes; `set_option` misplaced) | 13:02:05–13:02:08 | 3 s | 2 parse errors (mine) | `scratch/build-rect-2.log` |
| build Rect, attempt 3 | 13:02:17–13:02:21 | 4 s (lean 2.1 s) | clean | `scratch/build-rect-3.log` |
| build General, attempt 1 | 13:02:29–13:02:31 | 2 s (lean 1.5 s) | clean, 1 deprecation warning | `scratch/build-general-1.log` |
| build both after `push Not` | 13:02:44–13:02:46 | 2 s | clean | `scratch/build-both-final.log` |
| `lake env lean scratch/v11-print-axioms.lean` | 13:03:02–13:03:04 | 1.8 s | 45 lines | `scratch/v11-print-axioms.log` |
| **clean rebuild of both** (their oleans/ir deleted first) | 13:03:27–13:03:31 | **4.38 s real** (Rect 1.9 s, General 1.5 s) | clean | `scratch/build-both-clean-timed.log` |

Final clean-rebuild log, verbatim:

    ✔ [2726/2727] Built Zeta23.W1.ArgPrinciple.Rect (1.9s)
    ✔ [2727/2727] Built Zeta23.W1.ArgPrinciple.General (1.5s)
    Build completed successfully (2727 jobs).
    real 4.38
    user 4.99
    sys 2.52

(The 2725 upstream jobs are Mathlib/Zeta23 oleans already present in the cloned `.lake`; only the
two new modules were compiled. Compare 25 s + 2.9 s for the originals on v4.28.0 with `import
Mathlib`, dominated by loading the whole library.)

Escape-hatch grep on the ported files
(`grep -n -E "sorry|admit|native_decide|axiom |unsafe|opaque|implemented_by|extern|decide"
Zeta23/W1/ArgPrinciple/*.lean`): no matches, `exit=1`. No new axioms, no `decide +kernel`.

## 6. `#print axioms` — all 45 declarations (verbatim, `scratch/v11-print-axioms.log`, 13:03:04 IST)

    'Zeta23.W1.ArgPrinciple.Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.RectFrontier' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.RectFrontier_subset_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_RectFrontier_bot' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_RectFrontier_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_RectFrontier_right' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_RectFrontier_left' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.continuousOn_edge_bot' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.continuousOn_edge_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.continuousOn_edge_right' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.continuousOn_edge_left' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_congr' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_add' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_const_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_eq_zero_of_differentiableOn' depends on axioms: [propext,
     Classical.choice,
     Quot.sound]
    'Zeta23.W1.ArgPrinciple.arctan_add_arctan_inv_of_pos' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.arctan_add_arctan_inv_of_neg' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.ofReal_add_const_mul_I_ne_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.hasDerivAt_edge_antiderivative' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.integral_inv_ofReal_add_const_mul_I' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.integral_inv_const_add_ofReal_mul_I' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.arctan_rect_sum' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_inv_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.continuousOn_logDeriv' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.rectIntegral_logDeriv_eq_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.sub_ne_zero_of_mem_RectFrontier' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_prod_mul' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_factored' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_factored_div' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.analyticOrderAt_ne_top' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.exists_factor_pow_sub' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.exists_factor_prod' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.isCompact_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.finite_zeros_of_isCompact' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.finite_zeros_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_RectFrontier_left_corner' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.mem_Ioo_of_zero_mem_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_eq_sum_analyticOrder' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_eq_finsum_analyticOrder' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.W1.ArgPrinciple.windingRect_id_eq_one' depends on axioms: [propext, Classical.choice, Quot.sound]

The scratch file (`~/rh-lean-work/zeta-23-v11/scratch/v11-print-axioms.lean`, not a Lake target)
imports both modules and holds one `#print axioms` line per declaration, generated by grepping
`^(theorem|lemma|def|noncomputable def)` from the ported files, so the 45 lines are the complete
inventory.

## 7. What is next (not done here, by instruction)

* Copy `Rect.lean`, `General.lean` into the program root's `lean/Zeta23/W1/ArgPrinciple/` and
  into the hot tree once its current build is finished; add nothing to `Zeta23.lean`'s root import
  unless the W1 files are wired there (they are built by targeted `lake build`).
* The bridge to H-AP (scout §3.2 G1–G5, §5 step 3): generalize the four entire-only lemmas
  (`continuousOn_logDeriv`, `rectIntegral_logDeriv_eq_zero`, `analyticOrderAt_ne_top`,
  `finite_zeros_of_isCompact`, plus `exists_factor_pow_sub`/`exists_factor_prod`) from
  `Differentiable ℂ H` to `DifferentiableOn ℂ H U` with `U` open and preconnected, or use an
  entire surrogate for ζ; the vocabulary bridge `Rect`/`RectFrontier` ↔ `rectClosed`/`rectBdry`,
  `rectIntegral (logDeriv f)` ↔ the four `logDerivSegIntegral`s (via `logDerivSegIntegral_affine`);
  the degenerate case σ₁ = σ₂; the two counting consequences from `analyticOrderNatAt`.


## 8. Complete `diff -u` original → ported (verbatim)

### 8.1 `ArgumentPrinciple.lean` → `Rect.lean`

```diff
--- gomila-ap/repo/lean/aristotle/argument_principle/RequestProject/ArgumentPrinciple.lean	2026-09-02 08:03:35
+++ zeta-23-v11/Zeta23/W1/ArgPrinciple/Rect.lean	2026-09-02 13:02:17
@@ -1,4 +1,44 @@
-import Mathlib
+/-
+Copyright (c) 2026 Kunal Tyagi. All rights reserved.
+Released under Apache 2.0 license as described in the file LICENSE.
+SPDX-License-Identifier: Apache-2.0
+
+This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
+Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
+canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
+no code from that library.
+
+Portions ported from the Lean development in
+github.com/judegomila/dbn-lambda-01787854-candidate-audit (branch
+lean/certificate-and-argument-principle, commit ea09b2f), Copyright (c) 2026 Jude Gomila,
+MIT License, generated with Harmonic Aristotle; ported and adapted here.
+The MIT license text is reproduced in the program's NOTICE file.
+-/
+/-
+Zeta23/W1/ArgPrinciple/Rect.lean — the RECTANGLE-INTEGRAL machinery of the ported argument
+principle (D1 milestone v1.1, D-R3): the closed rectangle `Rect`, its boundary `RectFrontier`,
+the four-edge boundary integral `rectIntegral` in the edge convention of Mathlib's
+`Complex.integral_boundary_rect_eq_zero_of_differentiableOn`, the winding number
+`windingRect`, the rectangle residue integral `rectIntegral_inv_sub`
+(∮ (ζ − a)⁻¹ dζ = 2πi for `a` in the open interior — the piece Mathlib lacks), and the
+factored argument principle `windingRect_prod_mul` / `windingRect_factored` /
+`windingRect_factored_div` for ENTIRE cofactors.
+
+Port record (2026-09-02): source file `RequestProject/ArgumentPrinciple.lean` of the branch
+named in the header, built there on Lean v4.28.0 + Mathlib 8f9d9cff; ported to the program's
+Lean v4.33.0-rc2 + the Mathlib revision pinned in lake-manifest.json.  Every theorem and lemma
+STATEMENT is byte-for-byte the original (namespace aside); the whole-Mathlib import was replaced
+by the specific modules below; proof-level changes are listed in
+rh-program/results/d1-m1/v11/port-notes.md.  Nothing here mentions ζ: the bridge from these
+statements to D1's `RectArgPrinciple riemannZeta` (Soundness.lean, H-AP) is separate work.
+-/
+import Mathlib.Analysis.Complex.CauchyIntegral
+import Mathlib.Analysis.Calculus.LogDeriv
+import Mathlib.Analysis.Calculus.FDeriv.Analytic
+import Mathlib.Analysis.Complex.RealDeriv
+import Mathlib.Analysis.SpecialFunctions.Log.Deriv
+import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
+import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
 
 /-!
 # The argument principle on rectangles, factored form
@@ -15,7 +55,7 @@
 open Set Complex intervalIntegral MeasureTheory
 open scoped Real BigOperators Interval
 
-namespace ArgumentPrinciple
+namespace Zeta23.W1.ArgPrinciple
 
 /-! ## Definitions -/
 
@@ -134,7 +174,7 @@
       have hFs : ∀ j ∈ s, ContinuousOn (F j) (RectFrontier z w) := fun j hj =>
         hF j (Finset.mem_insert_of_mem hj)
       have hsum : ContinuousOn (fun c => ∑ j ∈ s, F j c) (RectFrontier z w) :=
-        continuousOn_finset_sum _ hFs
+        continuousOn_finsetSum _ hFs
       simp only [Finset.sum_insert hi]
       rw [rectIntegral_add hFi hsum, ih hFs]
 
@@ -183,19 +223,22 @@
     have hq : HasDerivAt (fun t : ℝ => t ^ 2 + α ^ 2) (2 * x) x := by
       simpa using (hasDerivAt_pow 2 x).add_const (α ^ 2)
     have h := ((Real.hasDerivAt_log (ne_of_gt hpos)).comp x hq).const_mul (1 / 2 : ℝ)
-    convert h using 1
+    -- port: `convert h using 1; field_simp` no longer closes the function-side goal first
+    refine h.congr_deriv ?_
     field_simp
   have h2 : HasDerivAt (fun t : ℝ => Real.arctan (t / α)) ((1 / α) / (1 + (x / α) ^ 2)) x := by
     have hq : HasDerivAt (fun t : ℝ => t / α) (1 / α) x := by
       simpa [div_eq_mul_inv] using (hasDerivAt_id x).mul_const α⁻¹
     have h := (Real.hasDerivAt_arctan (x / α)).comp x hq
-    convert h using 1
+    -- port: as for `h1`
+    refine h.congr_deriv ?_
     ring
   have hsimp : (1 / α) / (1 + (x / α) ^ 2) = α / (x ^ 2 + α ^ 2) := by field_simp; ring
   have h3 := h1.ofReal_comp.sub (h2.ofReal_comp.const_mul I)
   rw [hsimp] at h3
-  convert h3 using 1
-  exact key.symm
+  -- port: `convert h3 using 1` now exposes an instance-equality goal first; rewrite instead
+  rw [← key]
+  exact h3
 
 /-- The antiderivative computation for the horizontal edges. -/
 lemma integral_inv_ofReal_add_const_mul_I (α u v : ℝ) (hα : α ≠ 0) :
@@ -314,7 +357,8 @@
   have hdF : Differentiable ℂ (deriv F) := fun x => ((hF.analyticAt x).deriv).differentiableAt
   have h : ContinuousOn (fun c => deriv F c / F c) (RectFrontier z w) :=
     hdF.continuous.continuousOn.div hF.continuous.continuousOn fun c hc => hF0 c hc.1
-  simpa [logDeriv_apply] using h
+  -- port: `simpa [logDeriv_apply]` no longer unfolds the unapplied `logDeriv F`; it is `rfl`
+  exact h
 
 /-- **Cauchy–Goursat** for the logarithmic derivative of an entire nonvanishing function. -/
 lemma rectIntegral_logDeriv_eq_zero {z w : ℂ} {F : ℂ → ℂ} (hF : Differentiable ℂ F)
@@ -375,7 +419,7 @@
       ContinuousOn (fun c => (m j : ℂ) * (c - a j)⁻¹) (RectFrontier z w) := fun j hj =>
     continuousOn_const.mul (ContinuousOn.inv₀ (by fun_prop) fun c hc => hsub c hc j hj)
   have hcontSum : ContinuousOn (fun c => ∑ j ∈ s, (m j : ℂ) * (c - a j)⁻¹) (RectFrontier z w) :=
-    continuousOn_finset_sum _ hcontTerm
+    continuousOn_finsetSum _ hcontTerm
   rw [windingRect, rectIntegral_congr hlog, rectIntegral_add hcontSum hVcont, hVint, add_zero,
     rectIntegral_sum hcontTerm]
   have hterm : ∀ j ∈ s,
@@ -387,6 +431,8 @@
   have hpi : (π : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
   field_simp
 
+-- port: `hre`, `him`, `hm` are unused by design (see the docstring); silence the linter only.
+set_option linter.unusedVariables false in
 /-- **Factored argument principle on a rectangle.**  If `U` is entire and nonvanishing on the
 closed rectangle `Rect z w`, the points `a j` lie in the open interior of the rectangle, and
 `H ζ = (∏ j, (ζ - a j) ^ m j) * U ζ`, then `H` is nonvanishing on the boundary of the rectangle
@@ -411,6 +457,8 @@
     windingRect_prod_mul (continuousOn_logDeriv hU hU0) (rectIntegral_logDeriv_eq_zero hU hU0)
       hUne (fun c _ => hU.differentiableAt) ha'⟩
 
+-- port: as for `windingRect_factored`.
+set_option linter.unusedVariables false in
 /-- **Consumer shape.**  Under the hypotheses of `windingRect_factored`, dividing `H` by any
 entire `B` that is nonvanishing on the closed rectangle does not change the winding number:
 `W (H / B; z, w) = ∑ j, m j`. -/
@@ -441,4 +489,4 @@
   rw [hfun]
   exact windingRect_prod_mul hVcont hVint hVne hVdiff fun j _ => ha j
 
-end ArgumentPrinciple
+end Zeta23.W1.ArgPrinciple
```

### 8.2 `ArgumentPrincipleGeneral.lean` → `General.lean`

```diff
--- gomila-ap/repo/lean/aristotle/argument_principle/RequestProject/ArgumentPrincipleGeneral.lean	2026-09-02 08:03:35
+++ zeta-23-v11/Zeta23/W1/ArgPrinciple/General.lean	2026-09-02 13:02:44
@@ -1,10 +1,44 @@
-import Mathlib
-import RequestProject.ArgumentPrinciple
+/-
+Copyright (c) 2026 Kunal Tyagi. All rights reserved.
+Released under Apache 2.0 license as described in the file LICENSE.
+SPDX-License-Identifier: Apache-2.0
 
+This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
+Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
+canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
+no code from that library.
+
+Portions ported from the Lean development in
+github.com/judegomila/dbn-lambda-01787854-candidate-audit (branch
+lean/certificate-and-argument-principle, commit ea09b2f), Copyright (c) 2026 Jude Gomila,
+MIT License, generated with Harmonic Aristotle; ported and adapted here.
+The MIT license text is reproduced in the program's NOTICE file.
+-/
+/-
+Zeta23/W1/ArgPrinciple/General.lean — the GENERAL argument principle on rectangles for entire
+functions (D1 milestone v1.1, D-R3), on top of Rect.lean: factoring the zeros of an entire
+function out of a finite set (`exists_factor_pow_sub`, `exists_factor_prod`), finiteness of the
+zero set in a compact set (`finite_zeros_of_isCompact`, `finite_zeros_Rect`), and the counting
+theorems `windingRect_eq_sum_analyticOrder` (winding number = sum of the vanishing orders
+`analyticOrderNatAt` over the zeros in the rectangle) and `windingRect_eq_finsum_analyticOrder`,
+with the sanity check `windingRect_id_eq_one`.
+
+Port record (2026-09-02): source file `RequestProject/ArgumentPrincipleGeneral.lean` of the
+branch named in the header; same port conventions as Rect.lean (statements byte-for-byte,
+imports narrowed, proof-level changes in rh-program/results/d1-m1/v11/port-notes.md).  The
+function class here is ENTIRE (`Differentiable ℂ H`); generalizing to `DifferentiableOn` on an
+open preconnected set containing the rectangle (gap G1 of the scout) is not done in this file.
+-/
+import Mathlib.Analysis.Analytic.Order
+import Mathlib.Analysis.Analytic.IsolatedZeros
+import Mathlib.Algebra.BigOperators.Finprod
+import Mathlib.Topology.Compactness.Compact
+import Zeta23.W1.ArgPrinciple.Rect
+
 /-!
 # The general argument principle on rectangles
 
-Building on the factored argument principle of `RequestProject.ArgumentPrinciple`, this file
+Building on the factored argument principle of `Zeta23.W1.ArgPrinciple.Rect`, this file
 proves the argument principle for an arbitrary entire function `H` that is nonvanishing on the
 boundary of the rectangle: the winding number `windingRect H z w` counts the zeros of `H` inside
 the rectangle with multiplicity.
@@ -13,7 +47,7 @@
 open Set Complex Filter Topology MeasureTheory
 open scoped Real BigOperators Interval
 
-namespace ArgumentPrinciple
+namespace Zeta23.W1.ArgPrinciple
 
 /-! ## Factoring out the zeros of an entire function -/
 
@@ -146,7 +180,7 @@
     p.re ∈ Ioo z.re w.re ∧ p.im ∈ Ioo z.im w.im := by
   have hnf : p ∉ RectFrontier z w := fun h => hbd p h hp0
   have h4 : ¬(p.re = z.re ∨ p.re = w.re ∨ p.im = z.im ∨ p.im = w.im) := fun h => hnf ⟨hp, h⟩
-  push_neg at h4
+  push Not at h4  -- port: `push_neg` is deprecated in favor of `push Not`
   obtain ⟨h1, h2, h3, h4⟩ := h4
   have hre' : p.re ∈ Icc z.re w.re := by
     rw [← Set.uIcc_of_le hre.le]; exact hp.1
@@ -212,4 +246,4 @@
   rw [windingRect_eq_sum_analyticOrder hre him differentiable_id hbd ({0} : Finset ℂ) hS]
   simp [analyticOrderNatAt, analyticOrderAt_id]
 
-end ArgumentPrinciple
+end Zeta23.W1.ArgPrinciple
```
