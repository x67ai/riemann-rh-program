# Discharge notes: H-AP proved — `Zeta23.W1.ArgPrincipleBridge` and `cert_of_checkW1_ap`

**Date:** 2026-09-02 (Session 14, D1 v1.1 discharge agent; D-R3, first deliverable component 1).
**Status:** DISCHARGED. `RectArgPrinciple f` (Soundness.lean's H-AP, in its consequence form)
is a THEOREM for every `f : ℂ → ℂ` (`rectArgPrinciple_of_local`), hence for `riemannZeta`
(`rectArgPrinciple_riemannZeta`), and the W1 checker soundness theorem is restated without it
(`cert_of_checkW1_ap`).  The module builds clean (no errors, no warnings) on the program's
toolchain; all 18 new declarations depend on `[propext, Classical.choice, Quot.sound]` only; no
`sorry`/`admit`/`native_decide`/`decide`/new axiom.  Nothing has been copied into the program
root's `lean/` yet (this file and `../../../NOTICE` are the only program-root writes).
**Standing order 5:** every block below is pasted from the commands as run today.

**HONEST LABEL from here on (binding).**  An accepted ζ transcript is
"kernel-checked modulo the displayed hypothesis H-ENCL (producers untrusted)".
Never "fully machine-checked": H-ENCL (`W1EnclOK riemannZeta d`, FORMAT.md §8.1) is where the
untrusted producers' interval arithmetic enters the trusted statement, and it stays displayed.
The v1 statement remains ζ-SPECIFIC (D-R8): `cert_of_checkW1_ap` mentions `riemannZeta` only.

## 0. Where things are

| item | path |
|---|---|
| the module | `~/rh-lean-work/zeta-23-v11/Zeta23/W1/ArgPrincipleBridge.lean` (459 lines, 18 declarations; SHA-256 `b8392aad5f3438458038bdf4c9b71a660cab2ddd1d63f9a5e7a05771cf503a0e`) |
| its imports | `Mathlib.Analysis.Analytic.Order`, `Mathlib.Analysis.Complex.CauchyIntegral`, `Zeta23.W1.ArgPrinciple.General` (→ `.Rect`), `Zeta23.W1.Soundness` |
| toolchain | Lean `v4.33.0-rc2` (commit d8b18978), Mathlib `51e6992efd06126df61a496bebf8f49482a4e129` (lake-manifest.json; the README/AUDIT-F short-hash discrepancy is recorded in `port-notes.md` §0 — not resolved here) |
| build logs | `~/rh-lean-work/zeta-23-v11/scratch/build-bridge-{1,2,3,4,clean-timed}.log` |
| axioms | `scratch/v11-bridge-axioms.{lean,log}` |
| smoke test | `scratch/v11-bridge-smoke.{lean,log}` (not a Lake target; run with `lake env lean`) |
| attribution | header = program Apache-2.0 block + the required Gomila/MIT/Aristotle notice block; `NOTICE` got a dated addendum section naming this file |

The hot tree `~/rh-lean-work/zeta-23-lean-main` was not touched (no build, no edit; `pgrep -fl
"lake build"` showed no other lake process at each build).  `pmset -g therm` before the builds:
"No CPU power status has been recorded" (no throttling).

## 1. The statement

`#check` output, verbatim (`scratch/v11-bridge-axioms.log`):

    Zeta23.W1.cert_of_checkW1_ap : ∀ (d : Zeta23.W1.W1Data),
      Zeta23.W1.checkW1 d = true →
        Zeta23.W1.W1EnclOK riemannZeta d →
          (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ Zeta23.W1.T1 d < ρ.im ∧ ρ.im < Zeta23.W1.T2 d) ∧
            (d.m = 0 → ∀ s ∈ Zeta23.W1.W1Rect d, riemannZeta s ≠ 0)
    Zeta23.W1.rectArgPrinciple_of_local : ∀ (f : ℂ → ℂ), Zeta23.W1.RectArgPrinciple f

As written in the module:

    theorem cert_of_checkW1_ap (d : W1Data) (hc : checkW1 d = true)
        (hEncl : W1EnclOK riemannZeta d) :
        (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
            ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
        ∧ (d.m = 0 → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0) :=
      cert_of_checkW1 d hc hEncl rectArgPrinciple_riemannZeta

Same conclusion as `cert_of_checkW1` (Soundness.lean line 928), same hypotheses minus
`hAP : RectArgPrinciple riemannZeta`, which is now the theorem `rectArgPrinciple_riemannZeta :=
rectArgPrinciple_of_local riemannZeta`.  `Soundness.lean` is imported, not modified; the `hAP`
argument of `cert_of_checkW1` is simply fed the proof.  `RectArgPrinciple` is exactly the Prop of
Soundness.lean lines 173–182 (the consequence form: ∃ Z : ℕ with (i) the winding identity
`2πZ = Σ` of the four directed edge increments, (ii) `Z = 0 →` no zero in the open rectangle,
(iii) `1 ≤ Z →` a zero in the open rectangle), quantified over `½ < σ₁ ≤ σ₂ < 1`, `t₁ < t₂`, any
open `U ⊇ rectClosed`, `DifferentiableOn ℂ f U`, and boundary nonvanishing.

## 2. Route taken: (B), and why (A) was not needed

The task offered (A) an entire surrogate `H(s) = (s − 1)·ζ(s)` or (B) generalizing the ported
theorem from `Differentiable ℂ H` to `DifferentiableOn ℂ H U`.  **Route B**, for one decisive
reason: H-AP as declared in Soundness.lean universally quantifies the open set `U` and takes
`DifferentiableOn ℂ f U` as a hypothesis.  So H-AP is a statement about functions analytic on a
neighborhood of the closed rectangle, with no ζ in it, and it is true for EVERY `f`.  Once the
ported argument principle is available in that generality, `RectArgPrinciple f` follows for all
`f`, and no fact about ζ is consumed anywhere in the module (`differentiableAt_riemannZeta` is
used only inside `cert_of_checkW1`, already, to produce the `DifferentiableOn` input for
`U = {s | s.re < 1}`).  Route A would have needed Mathlib's `riemannZeta_residue_one` plus a
removable-singularity argument (Mathlib's `riemannZeta` is defined by `Function.update` at 0 only,
so `(s − 1)·ζ(s)` as a term is not continuous at 1 and would need its own `update`), plus the
outside-the-rectangle variant of `rectIntegral_inv_sub`, plus a zero/order comparison between
`H` and ζ — all strictly more work than route B, whose proofs are the port's with local edits.

The generalization was mechanical, as the port-notes §7 and the scout's G1 route (a) predicted:
the port uses entireness in exactly the places the scout listed, and each use becomes
`hH.analyticAt (hU.mem_nhds _)` (Mathlib's `DifferentiableOn.analyticAt`), or an identity-theorem
step on a preconnected set.  One simplification over the scout's plan: the scout expected to need
`U` preconnected (the consumer's `U = {Re s < 1}` is convex).  Not needed — the identity theorem
is applied on the closed rectangle `Rect z w` itself (preconnected, `isPreconnected_Rect`), where
`H` is `AnalyticOnNhd` because `Rect z w ⊆ U` with `U` open; and Mathlib's
`AnalyticOnNhd.analyticOrderAt_ne_top_of_isPreconnected` transports finite order from the
nonvanishing corner `z` to every point of the rectangle without any hand-rolled identity-theorem
argument.  So `RectArgPrinciple f` holds for arbitrary open `U`, which is what the Prop demands.

## 3. Module structure and the scout's gap list G1–G6

`ArgPrincipleBridge.lean`, namespace `Zeta23.W1` (§1 inside `Zeta23.W1.ArgPrinciple`, next to
the ported names):

| § | declaration | what it is | closes |
|---|---|---|---|
| 1 | `ArgPrinciple.isPreconnected_Rect` | `Rect z w` is preconnected (image of `[[·,·]] ×ˢ [[·,·]]` under `(x,y) ↦ x + yI`; the set identity is the port's `isCompact_Rect` one) | G1 |
| 1 | `ArgPrinciple.analyticOrderAt_ne_top_of_analyticOnNhd` | finite order at every point of a preconnected `K` where `H` is `AnalyticOnNhd` and not identically zero — replaces the port's `analyticOrderAt_ne_top` (entire, via `isPreconnected_univ`) | G1 |
| 1 | `ArgPrinciple.exists_factor_pow_sub_on` | the port's `exists_factor_pow_sub` with `Differentiable ℂ H` → `DifferentiableOn ℂ H U`, `U` open, `p ∈ U`; cofactor `DifferentiableOn ℂ G U`; factorization for all `ζ` | G1 |
| 1 | `ArgPrinciple.exists_factor_prod_on` | the port's `exists_factor_prod`, with `S ⊆ K ⊆ U`, `K` preconnected, `H` not identically zero on `K` | G1 |
| 1 | `ArgPrinciple.finite_zeros_of_isCompact_on` | the port's `finite_zeros_of_isCompact` for `K ⊆ U` compact preconnected | G1 |
| 1 | `ArgPrinciple.finite_zeros_Rect_on` | the port's `finite_zeros_Rect`, local | G1 |
| 1 | `ArgPrinciple.continuousOn_logDeriv_on` | the port's `continuousOn_logDeriv`, local (`AnalyticOnNhd.deriv` on `Rect z w`) | G1 |
| 1 | `ArgPrinciple.rectIntegral_logDeriv_eq_zero_on` | the port's Cauchy–Goursat step for `F′/F`, local | G1 |
| 1 | `ArgPrinciple.windingRect_eq_sum_analyticOrder_on` | **the local argument principle**: the port's `windingRect_eq_sum_analyticOrder` with `Differentiable ℂ H` → `IsOpen U`, `Rect z w ⊆ U`, `DifferentiableOn ℂ H U` | G1 |
| 2 | `cpt_eq` | `cpt x y = x + y·I` | G3 |
| 2 | `Rect_cpt` | `Rect (cpt s₁ t₁) (cpt s₂ t₂) = rectClosed s₁ s₂ t₁ t₂` for `s₁ ≤ s₂`, `t₁ ≤ t₂` | G3 |
| 2 | `RectFrontier_cpt` | `RectFrontier (cpt s₁ t₁) (cpt s₂ t₂) = rectBdry s₁ s₂ t₁ t₂` for `s₁ ≤ s₂`, `t₁ ≤ t₂` | G3 |
| 2 | `logDerivSegIntegral_horiz` | `logDerivSegIntegral f (cpt u T) (cpt v T) = ∫ x in u..v, logDeriv f (x + T·I)` — unconditional (junk-safe) | G2 |
| 2 | `logDerivSegIntegral_vert` | `logDerivSegIntegral f (cpt S u) (cpt S v) = I * ∫ y in u..v, logDeriv f (S + y·I)` — unconditional | G2 |
| 2 | `edge_sum_eq_rectIntegral` | bottom + right + top + left (the §4 traversal) `= rectIntegral (logDeriv f) (cpt s₁ t₁) (cpt s₂ t₂)` — unconditional | G2 |
| 3 | `rectArgPrinciple_of_local` | `∀ f, RectArgPrinciple f` | G2–G5 |
| 3 | `rectArgPrinciple_riemannZeta` | `RectArgPrinciple riemannZeta` | — |
| 3 | `cert_of_checkW1_ap` | soundness without H-AP | — |

G6 (toolchain drift) was closed by the port (port-notes §4).  All six gaps of
`../gomila-lean-branch-scout.md` §3.2 are now closed.

**How `rectArgPrinciple_of_local` goes.**  Given `s₁ ≤ s₂`, split on `s₁ < s₂` vs `s₁ = s₂`.

*Nondegenerate.*  `z := cpt s₁ t₁`, `w := cpt s₂ t₂`; `Rect_cpt`/`RectFrontier_cpt` transport
`rectClosed ⊆ U` and boundary nonvanishing into the port's vocabulary; `S :=
(finite_zeros_Rect_on …).toFinset` is the finite zero set of `f` in the closed rectangle;
`Z := ∑ p ∈ S, analyticOrderNatAt f p`.
  (i) `windingRect_eq_sum_analyticOrder_on` gives `(2πI)⁻¹ · rectIntegral (logDeriv f) z w = Z`
  (as complex numbers, `Nat.cast_sum` via `push_cast`); `inv_mul_eq_iff_eq_mul₀` turns it into
  `rectIntegral … = 2πI·Z`; `edge_sum_eq_rectIntegral` identifies the four
  `logDerivSegIntegral`s' sum with `rectIntegral`; imaginary parts (`Complex.add_im`,
  `Complex.mul_I_im`, `Complex.ofReal_re`) give `2πZ = Σ argIncrement`.  As the scout noted (G2),
  the port's identity is strictly stronger (real part 0) — nothing is lost.
  (ii) `Z = 0`: a zero `s` in the open rectangle lies in the closed one, so `s ∈ S`;
  `Finset.sum_eq_zero_iff` gives `analyticOrderNatAt f s = 0`, i.e. (`ENat.toNat_eq_zero`)
  `analyticOrderAt f s = 0 ∨ = ⊤`; the first contradicts `f s = 0` by
  `AnalyticAt.analyticOrderAt_eq_zero`, the second contradicts
  `analyticOrderAt_ne_top_of_analyticOnNhd` on the preconnected rectangle (the `⊤` case is
  exactly the "toNat hiding ⊤" trap the scout flagged in G5).
  (iii) `1 ≤ Z`: `Finset.nonempty_of_sum_ne_zero` gives `p ∈ S`; the port's
  `mem_Ioo_of_zero_mem_Rect` puts it in the open rectangle.

*Degenerate `s₁ = s₂`* (clause C2b allows it; the checker's `hs12le` is non-strict): `Z := 0`.
  (i) bottom and top are one-point segments (`w − z = 0`, integrand times 0:
  `simp [logDerivSegIntegral]`); left is the reverse of right — both are
  `logDerivSegIntegral_vert` instances, and `intervalIntegral.integral_symm t₁ t₂` makes them
  negatives — so the four increments sum to `0 = 2π·0`.  No integrability is needed: the
  vertical-edge lemma is a change of variables valid for the Bochner integral including the junk
  case (this is why the §2 lemmas are stated unconditionally).
  (ii) `rectOpen s₁ s₁ t₁ t₂` is empty (`s₁ < s.re < s₁`).  (iii) `1 ≤ 0` is false.

The hypotheses `½ < s₁` and `s₂ < 1` of `RectArgPrinciple` are unused (named `_hhalf`, `_hs2`):
the theorem holds for every rectangle.  They stay in the Prop because the Prop's text is pinned by
FORMAT.md §8.2 and consumed verbatim by `cert_of_checkW1`.

## 4. Every Mathlib result consumed (by name)

Names as they resolve in Mathlib `51e6992`; the module where each lives is given for the
non-obvious ones.

*Analyticity and orders* (`Mathlib/Analysis/Complex/CauchyIntegral.lean`,
`Mathlib/Analysis/Analytic/{Order,IsolatedZeros}.lean`):
`DifferentiableOn.analyticAt` (open-set differentiability ⇒ analytic at interior points — the
one fact that makes route B work), `DifferentiableOn.analyticOnNhd`, `AnalyticOnNhd.mono`,
`AnalyticOnNhd.deriv`, `AnalyticOnNhd.continuousOn`,
`AnalyticOnNhd.analyticOrderAt_ne_top_of_isPreconnected` (Order.lean 627),
`AnalyticOnNhd.eqOn_zero_of_preconnected_of_frequently_eq_zero` (IsolatedZeros.lean 214),
`AnalyticAt.analyticOrderAt_eq_zero` (Order.lean 133), `AnalyticAt.analyticOrderAt_ne_top`
(Order.lean 113), `analyticOrderAt_mul` (Order.lean 497), `analyticOrderNatAt` (Order.lean 61,
`= (analyticOrderAt f z₀).toNat`), `ENat.toNat_eq_zero`, `ENat.zero_ne_top`.

*Topology* (`Mathlib/Topology/…`): `isPreconnected_uIcc`, `IsPreconnected.prod`,
`IsPreconnected.image`, `Set.Infinite.exists_accPt_of_subset_isCompact`,
`accPt_iff_frequently_nhdsNE`, `Set.not_finite`, `IsOpen.mem_nhds`, `isOpen_ne`,
`Filter.EventuallyEq.self_of_nhds`, `DifferentiableAt.congr_of_eventuallyEq`,
`DifferentiableAt.div`, `DifferentiableOn.differentiableAt`, `ContinuousOn.div`,
`ContinuousOn.mono`.

*Complex numbers and sets*: `Complex.mem_reProdIm` (`Data/Complex/Basic.lean` 116),
`Complex.ext`, `Complex.real_smul`, `Complex.add_im`, `Complex.neg_im`, `Complex.zero_im`,
`Complex.mul_I_im`, `Complex.ofReal_re`, `Complex.ofReal_ne_zero`, `Complex.I_ne_zero`,
`Real.pi_ne_zero`, `Set.uIcc_of_le`, `Set.mem_Icc`, `Set.mem_sdiff`, `Set.mem_ofPred_eq`
(this Mathlib's set-builder membership lemma, as Soundness.lean already uses), `Set.mem_image`,
`Set.mem_prod`.

*Interval integrals* (`Mathlib/MeasureTheory/Integral/IntervalIntegral/Basic.lean`):
`intervalIntegral.integral_const_mul`, `intervalIntegral.integral_symm`, and — through
Soundness.lean's `smul_comp_integral` — `intervalIntegral.integral_smul` and
`intervalIntegral.smul_integral_comp_mul_add` (the unconditional change of variables; the direct
`rw` with Mathlib's `smul_integral_comp_add_mul` failed on a `•`-instance mismatch, see §6,
so the module applies Soundness.lean's already-elaborated lemma as a term instead).
`Complex.integral_boundary_rect_eq_zero_of_differentiableOn` enters through the port's
`rectIntegral_eq_zero_of_differentiableOn`.

*Finite sums and sets*: `Finset.induction_on`, `Finset.prod_insert`, `Finset.mem_insert`,
`Finset.sum_eq_zero_iff`, `Finset.nonempty_of_sum_ne_zero`, `Nat.cast_sum` (via `push_cast`),
`Set.Finite.toFinset`, `Set.Finite.mem_toFinset`, `inv_mul_eq_iff_eq_mul₀`, `logDeriv_apply`.

*From the port* (`Zeta23.W1.ArgPrinciple.{Rect,General}`): `Rect`, `RectFrontier`,
`rectIntegral`, `windingRect`, `RectFrontier_subset_Rect`, `mem_RectFrontier_left_corner`,
`isCompact_Rect`, `mem_Ioo_of_zero_mem_Rect`, `rectIntegral_eq_zero_of_differentiableOn`, and the
load-bearing `windingRect_prod_mul` (the residue computation `rectIntegral_inv_sub` and the
`logDeriv_mul/_prod/_fun_pow` algebra sit inside it, unchanged).

*From Soundness.lean*: `RectArgPrinciple`, `rectClosed`, `rectOpen`, `rectBdry`, `cpt`,
`cpt_re`, `cpt_im`, `segPt`, `segPt_mk_horiz`, `segPt_mk_vert`, `logDerivSegIntegral`,
`argIncrement`, `smul_comp_integral`, `cert_of_checkW1`, `W1EnclOK`, `W1Rect`, `T1`, `T2`,
`checkW1`.

Nothing about ζ: `differentiableAt_riemannZeta` and `riemannZeta_residue_one` are NOT used by the
module (the former is used by `cert_of_checkW1` itself, unchanged).

## 5. Build log and times (all in `~/rh-lean-work/zeta-23-v11`, `lake build Zeta23.W1.ArgPrincipleBridge`)

| step | time (IST) | wall | result | log |
|---|---|---|---|---|
| attempt 1 | 13:18:09–13:18:11 | 2.68 s | 2 errors (both `rw [… smul_integral_comp_add_mul]` in the two edge lemmas: "Did not find an occurrence of the pattern `?c • ∫ … ?f (?d + ?c * x)`"), 2 warnings (`Set.mem_diff` deprecated; unused simp arg) — everything else, §1 and §3 included, elaborated | `scratch/build-bridge-1.log` |
| attempt 2 (edge lemmas via `rw [smul_comp_integral]`) | 13:19:07–13:19:10 | 2.44 s | same 2 errors (pattern `∫ s in 0..1, ?c • ?F (?c * s + ?d)` not found — the `•` instance in the goal differs syntactically from the lemma's) | `scratch/build-bridge-2.log` |
| attempt 3 (edge lemmas apply `smul_comp_integral` as a term, as `logDerivSegIntegral_affine` does) | 13:19:41–13:19:44 | 2.67 s | **clean**; 2 style-linter warnings (`<;>` where `;` suffices) | `scratch/build-bridge-3.log` |
| attempt 4 (linter fixes) | 13:20:22–13:20:25 | 2.56 s | **clean, no warnings**; module 1.6 s | `scratch/build-bridge-4.log` |
| `lake env lean scratch/v11-bridge-axioms.lean` | 13:20:27 (log mtime) | ~2 s | 18 axiom lines + 2 `#check` | `scratch/v11-bridge-axioms.log` |
| `lake build Zeta23.W1.Examples` (for the smoke test) | 13:20:27 (log mtime) | cached | "Build completed successfully (656 jobs)" | `scratch/build-examples.log` |
| `lake env lean scratch/v11-bridge-smoke.lean` | first run 13:20, rerun 13:21:01 (log mtime) | ~2 s | 3 axiom lines | `scratch/v11-bridge-smoke.log` |
| **clean rebuild** (`.lake/build/{lib/lean,ir}/Zeta23/W1/ArgPrincipleBridge.*` deleted first) | 13:20:57–13:21:00 | **2.56 s real** (module 1.6 s) | clean | `scratch/build-bridge-clean-timed.log` |

Clean-rebuild log, verbatim:

```
✔ [3145/3145] Built Zeta23.W1.ArgPrincipleBridge (1.6s)
Build completed successfully (3145 jobs).
lake build Zeta23.W1.ArgPrincipleBridge  2.50s user 1.76s system 166% cpu 2.560 total
```

(3145 jobs vs the port's 2727: the bridge pulls in `Zeta23.W1.Soundness` and its Checker/Zeta23
upstream, all already built in the cloned `.lake`; only the bridge module was compiled.)

Escape-hatch grep (`grep -n -E "sorry|admit|native_decide|axiom |unsafe|opaque|implemented_by|extern|decide" Zeta23/W1/ArgPrincipleBridge.lean`): no matches, `exit=1`.
No `decide +kernel` anywhere in the module (the smoke test's `1 ≤ exampleRefutation.m` is
closed by `le_rfl`; the only kernel-`decide` in the chain is the Examples file's own
`exampleRefutation_accepted`, which is where the W1 files already use it).

## 6. `#print axioms` — all 18 declarations (verbatim, `scratch/v11-bridge-axioms.log`)

```
'Zeta23.W1.ArgPrinciple.isPreconnected_Rect' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.analyticOrderAt_ne_top_of_analyticOnNhd' depends on axioms: [propext,
 Classical.choice,
 Quot.sound]
'Zeta23.W1.ArgPrinciple.exists_factor_pow_sub_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.exists_factor_prod_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.finite_zeros_of_isCompact_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.finite_zeros_Rect_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.continuousOn_logDeriv_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.rectIntegral_logDeriv_eq_zero_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.ArgPrinciple.windingRect_eq_sum_analyticOrder_on' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.cpt_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.Rect_cpt' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.RectFrontier_cpt' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.logDerivSegIntegral_horiz' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.logDerivSegIntegral_vert' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.edge_sum_eq_rectIntegral' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.rectArgPrinciple_of_local' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.rectArgPrinciple_riemannZeta' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.cert_of_checkW1_ap' depends on axioms: [propext, Classical.choice, Quot.sound]
Zeta23.W1.cert_of_checkW1_ap : ∀ (d : Zeta23.W1.W1Data),
  Zeta23.W1.checkW1 d = true →
    Zeta23.W1.W1EnclOK riemannZeta d →
      (1 ≤ d.m → ∃ ρ, riemannZeta ρ = 0 ∧ 1 / 2 < ρ.re ∧ ρ.re < 1 ∧ Zeta23.W1.T1 d < ρ.im ∧ ρ.im < Zeta23.W1.T2 d) ∧
        (d.m = 0 → ∀ s ∈ Zeta23.W1.W1Rect d, riemannZeta s ≠ 0)
Zeta23.W1.rectArgPrinciple_of_local : ∀ (f : ℂ → ℂ), Zeta23.W1.RectArgPrinciple f
```

Together with port-notes §6 (the 45 ported declarations) and `cert_of_checkW1` itself
(`'Zeta23.W1.cert_of_checkW1' depends on axioms: [propext, Classical.choice, Quot.sound]`,
checked today in `scratch/v11-bridge-check.lean`), the whole chain
`checkW1 d = true` + H-ENCL ⟹ conclusion is on the three standard axioms.

**Proof-level friction worth recording (for the next person who touches this Mathlib).**
Mathlib's `intervalIntegral.smul_integral_comp_add_mul`/`smul_integral_comp_mul_add` could not be
applied by `rw`: the `ℝ`-on-`ℂ` `•` in a goal written with `(v - u) • …` elaborates to a
syntactically different `SMul` instance from the lemma's `NormedSpace ℝ E` path, and `rw`'s
keyed matching does not see through it.  Soundness.lean hit the same thing (its
`logDerivSegIntegral_affine` applies `smul_comp_integral` with `exact`); the bridge does likewise
(`have key := smul_comp_integral …; rw [hb] at key; exact key`).  Everything else in the port's
proofs transferred verbatim.

## 7. Smoke test: the FORMAT.md §11 examples through `cert_of_checkW1_ap`

`scratch/v11-bridge-smoke.lean` (not a Lake target), verbatim:

```lean
import Zeta23.W1.ArgPrincipleBridge
import Zeta23.W1.Examples
namespace Zeta23.W1
/-- smoke test: the §11 refutation example through `cert_of_checkW1_ap`; H-ENCL stays displayed
(never certified for this ARTIFICIAL data), H-AP is gone. -/
theorem exampleRefutation_cert_ap (hEncl : W1EnclOK riemannZeta exampleRefutation) :
    (1 ≤ exampleRefutation.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 exampleRefutation < ρ.im ∧ ρ.im < T2 exampleRefutation)
    ∧ (exampleRefutation.m = 0 → ∀ s ∈ W1Rect exampleRefutation, riemannZeta s ≠ 0) :=
  cert_of_checkW1_ap exampleRefutation exampleRefutation_accepted hEncl
/-- the same for the exclusion twin. -/
theorem exampleExclusion_cert_ap (hEncl : W1EnclOK riemannZeta exampleExclusion) :
    (1 ≤ exampleExclusion.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 exampleExclusion < ρ.im ∧ ρ.im < T2 exampleExclusion)
    ∧ (exampleExclusion.m = 0 → ∀ s ∈ W1Rect exampleExclusion, riemannZeta s ≠ 0) :=
  cert_of_checkW1_ap exampleExclusion exampleExclusion_accepted hEncl
/-- and the m = 1 witness extracted: a zero of ζ in the open rectangle, modulo H-ENCL only. -/
theorem exampleRefutation_zero_ap (hEncl : W1EnclOK riemannZeta exampleRefutation) :
    ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 exampleRefutation < ρ.im ∧ ρ.im < T2 exampleRefutation :=
  (exampleRefutation_cert_ap hEncl).1 le_rfl
#print axioms exampleRefutation_cert_ap
#print axioms exampleExclusion_cert_ap
#print axioms exampleRefutation_zero_ap
end Zeta23.W1
```

Output, verbatim (`scratch/v11-bridge-smoke.log`):

```
'Zeta23.W1.exampleRefutation_cert_ap' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.exampleExclusion_cert_ap' depends on axioms: [propext, Classical.choice, Quot.sound]
'Zeta23.W1.exampleRefutation_zero_ap' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Honesty label as in Examples.lean: the numbers are ARTIFICIAL, no producer certified H-ENCL for
them, and these three theorems assert nothing about ζ — they show that an accepted transcript
plus an H-ENCL certificate now yields the conclusion with no other hypothesis, on the standard
axioms, through the identical Examples pattern.

## 8. What remains displayed — and what does not

* **H-ENCL stays.** `W1EnclOK riemannZeta d` is the single remaining displayed hypothesis of
  `cert_of_checkW1_ap`.  It is the trust boundary by design (FORMAT.md §8.1; D1 direction
  "Trust boundary honesty").  Nothing here touches it.
* **H-AP is gone.**  `RectArgPrinciple riemannZeta` is a theorem (`rectArgPrinciple_riemannZeta`)
  on the standard axioms; the Prop `RectArgPrinciple` is kept in Soundness.lean as the interface
  `cert_of_checkW1` consumes.  Soundness.lean's header still describes H-AP as "v1's displayed
  analytic debt" and gives the two-hypothesis label — that text, FORMAT.md §8.2/§9 (the
  `zeta` label line 507 "kernel-checked modulo displayed hypotheses H-ENCL and H-AP"), and the
  README are now out of date and belong to the next documentation touch (not this agent's files).
* **Consequence form vs full §8.2.**  `cert_of_checkW1` consumes only the consequence form
  (Soundness.lean's dated 2026-08-26 formulation note); the multiplicity-counting statement that
  FORMAT.md §7.1 deferred to v1.1 is ALSO now formalized —
  `ArgPrinciple.windingRect_eq_sum_analyticOrder_on` is exactly "winding number = number of zeros
  in the rectangle with multiplicity" for a function analytic on a neighborhood of the rectangle
  — and `rectArgPrinciple_of_local` instantiates `Z` as that multiplicity count.  So the
  discharge is of the full §8.2 content, not only of the weaker Prop.
* **Unused hypotheses.** `½ < σ₁` and `σ₂ < 1` are not needed by the proof (the pole of ζ never
  enters: differentiability on `U` is a hypothesis of the Prop).  They remain in the Prop's text
  because FORMAT.md pins it.
* **Still not formalized (unchanged by this work, per Soundness.lean's header):** D2/D3 (branch
  lifting, the C7 clamp's justification) — the chain does not use them; f_DH-in-Lean (D-R8: the
  statement is ζ-specific).
* **Deliberately NOT done here (by instruction):** no copy into the program root's `lean/` or
  the hot tree; no edit to Soundness.lean, FORMAT.md, README, AUDIT-F; no rewrite of the
  two-hypothesis label anywhere except this file's and the module's own text.

## 9. Statements of the 18 declarations (keyword to `:=`, extracted mechanically from the module)

```lean
lemma isPreconnected_Rect (z w : ℂ) : IsPreconnected (Rect z w)

lemma analyticOrderAt_ne_top_of_analyticOnNhd {H : ℂ → ℂ} {K : Set ℂ} (hK : IsPreconnected K)
    (hH : AnalyticOnNhd ℂ H K) (hne : ∃ x ∈ K, H x ≠ 0) {p : ℂ} (hp : p ∈ K) :
    analyticOrderAt H p ≠ ⊤

lemma exists_factor_pow_sub_on {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hH : DifferentiableOn ℂ H U) {p : ℂ} (hp : p ∈ U) (htop : analyticOrderAt H p ≠ ⊤) :
    ∃ G : ℂ → ℂ, DifferentiableOn ℂ G U ∧ G p ≠ 0 ∧
      ∀ ζ, H ζ = (ζ - p) ^ (analyticOrderNatAt H p) * G ζ

lemma exists_factor_prod_on {U K : Set ℂ} (hU : IsOpen U) (hKU : K ⊆ U)
    (hK : IsPreconnected K) (S : Finset ℂ) (hSK : ∀ p ∈ S, p ∈ K)
    {H : ℂ → ℂ} (hH : DifferentiableOn ℂ H U) (hne : ∃ x ∈ K, H x ≠ 0) :
    ∃ G : ℂ → ℂ, DifferentiableOn ℂ G U ∧ (∀ p ∈ S, G p ≠ 0) ∧
      ∀ ζ, H ζ = (∏ p ∈ S, (ζ - p) ^ (analyticOrderNatAt H p)) * G ζ

lemma finite_zeros_of_isCompact_on {H : ℂ → ℂ} {U K : Set ℂ} (hU : IsOpen U) (hKU : K ⊆ U)
    (hK : IsCompact K) (hKc : IsPreconnected K) (hH : DifferentiableOn ℂ H U)
    (hne : ∃ x ∈ K, H x ≠ 0) : {p | p ∈ K ∧ H p = 0}.Finite

lemma finite_zeros_Rect_on {z w : ℂ} {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hH : DifferentiableOn ℂ H U) (hne : ∃ x ∈ Rect z w, H x ≠ 0) :
    {p | p ∈ Rect z w ∧ H p = 0}.Finite

lemma continuousOn_logDeriv_on {z w : ℂ} {F : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hF : DifferentiableOn ℂ F U) (hF0 : ∀ c ∈ Rect z w, F c ≠ 0) :
    ContinuousOn (logDeriv F) (RectFrontier z w)

lemma rectIntegral_logDeriv_eq_zero_on {z w : ℂ} {F : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U)
    (hRU : Rect z w ⊆ U) (hF : DifferentiableOn ℂ F U) (hF0 : ∀ c ∈ Rect z w, F c ≠ 0) :
    rectIntegral (logDeriv F) z w = 0

theorem windingRect_eq_sum_analyticOrder_on {z w : ℂ} (hre : z.re < w.re) (him : z.im < w.im)
    {H : ℂ → ℂ} {U : Set ℂ} (hU : IsOpen U) (hRU : Rect z w ⊆ U) (hH : DifferentiableOn ℂ H U)
    (hbd : ∀ c ∈ RectFrontier z w, H c ≠ 0)
    (S : Finset ℂ) (hS : ∀ p, p ∈ S ↔ (p ∈ Rect z w ∧ H p = 0)) :
    windingRect H z w = ∑ p ∈ S, (analyticOrderNatAt H p : ℂ)

lemma cpt_eq (x y : ℝ) : cpt x y = (x : ℂ) + (y : ℂ) * I

lemma Rect_cpt {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ ≤ t₂) :
    Rect (cpt s₁ t₁) (cpt s₂ t₂) = rectClosed s₁ s₂ t₁ t₂

lemma RectFrontier_cpt {s₁ s₂ t₁ t₂ : ℝ} (hs : s₁ ≤ s₂) (ht : t₁ ≤ t₂) :
    RectFrontier (cpt s₁ t₁) (cpt s₂ t₂) = rectBdry s₁ s₂ t₁ t₂

lemma logDerivSegIntegral_horiz (f : ℂ → ℂ) (u v T : ℝ) :
    logDerivSegIntegral f (cpt u T) (cpt v T)
      = ∫ x in u..v, logDeriv f ((x : ℂ) + (T : ℂ) * I)

lemma logDerivSegIntegral_vert (f : ℂ → ℂ) (S u v : ℝ) :
    logDerivSegIntegral f (cpt S u) (cpt S v)
      = I * ∫ y in u..v, logDeriv f ((S : ℂ) + (y : ℂ) * I)

lemma edge_sum_eq_rectIntegral (f : ℂ → ℂ) (s₁ s₂ t₁ t₂ : ℝ) :
    logDerivSegIntegral f (cpt s₁ t₁) (cpt s₂ t₁) + logDerivSegIntegral f (cpt s₂ t₁) (cpt s₂ t₂)
      + logDerivSegIntegral f (cpt s₂ t₂) (cpt s₁ t₂)
      + logDerivSegIntegral f (cpt s₁ t₂) (cpt s₁ t₁)
    = rectIntegral (logDeriv f) (cpt s₁ t₁) (cpt s₂ t₂)

theorem rectArgPrinciple_of_local (f : ℂ → ℂ) : RectArgPrinciple f

theorem rectArgPrinciple_riemannZeta : RectArgPrinciple riemannZeta

theorem cert_of_checkW1_ap (d : W1Data) (hc : checkW1 d = true)
    (hEncl : W1EnclOK riemannZeta d) :
    (1 ≤ d.m → ∃ ρ : ℂ, riemannZeta ρ = 0 ∧ 1/2 < ρ.re ∧ ρ.re < 1
        ∧ T1 d < ρ.im ∧ ρ.im < T2 d)
    ∧ (d.m = 0 → ∀ s ∈ W1Rect d, riemannZeta s ≠ 0)
```

## 10. What is next

1. Copy `Zeta23/W1/ArgPrinciple/{Rect,General}.lean` and `Zeta23/W1/ArgPrincipleBridge.lean`
   into the program root's `lean/Zeta23/W1/` and into the hot tree once its current build has
   finished; `lake build Zeta23.W1.ArgPrincipleBridge` there and re-run
   `scratch/v11-bridge-axioms.lean` (expect the same 18 lines).
2. Documentation sweep for the new label: Soundness.lean header (trust model paragraph and the
   "WHAT IS PROVED HERE" list), FORMAT.md §8.2 ("discharged by v1.1" → discharged, with the
   theorem name), §9 label line, `lean/README.md`, D1 direction file (D-R3 success criterion:
   "fully kernel-checked after v1.1" must be replaced by "kernel-checked modulo the displayed
   hypothesis H-ENCL" — the producers are still untrusted), STATUS/LOG.  Also fix the AUDIT-F
   Mathlib short-hash slip recorded in port-notes §0.
3. Optionally promote the smoke-test theorems into `Zeta23/W1/Examples.lean` (or a new
   `ExamplesAP.lean`) as the kernel-checked "acceptance ⇒ conclusion modulo H-ENCL" witnesses.
4. Decide whether to tighten `RectArgPrinciple`'s unused `½ < σ₁`, `σ₂ < 1` — a FORMAT.md text
   change, so it is a documentation decision, not a Lean one.
