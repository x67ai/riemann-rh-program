# H5 — CHECK-O: the Opus 5 clean-clone check of the Comparator topics `WeilContainmentC2One` and `WeilContainmentC2` (Session 32; BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5, opened Tue Sep 29 06:53:02 IST 2026. Brief `BRIEF.md` SHA-256 `1a2e8a3acb4c6ba0623a9cf91ac515952490d49767717dd4b09af45f5c4e49ab` (recomputed; §7).
Clean clone: `~/rh-lean-work/checker-clone-s32-h5` — a NEW directory, `git clone https://github.com/anthropics/zeta-23-lean`,
`git checkout v1.0` (HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`), overlay of `rh-program/lean/` by the `lean/README.md` "Building"
recipe (`Zeta23/.`, `comparator/.`, `Zeta23.lean`). The builder's tree `~/rh-lean-work/checker-clone-s21` was not used for any build or
run. Logs of this check: `results/h5-c2-lean-s32/check-O/`. This checker edited no file outside `results/h5-c2-lean-s32/` and committed nothing.

(Written incrementally; the verdict section is filled at the close.)

## 1. Clone, cache, builds (`check-O/clone.log`, `check-O/cache-get.log`, `check-O/build-c2one.log`, `check-O/build-c2.log`)

* Clone at v1.0: HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`; `lean-toolchain` = `leanprover/lean4:v4.33.0-rc2`; manifest Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`
  (the checked-out `.lake/packages/mathlib` HEAD equals it). Overlay: `OVERLAY-OK`.
* `lake exe cache get`: "Decompressed 8489 already-cached file(s)", "Completed successfully", exit 0. Mathlib was never compiled from source.
* `lake build Solution.WeilContainmentC2One`: *Build completed successfully (8698 jobs)*, exit 0; the only modules built were
  `ChallengeDeps.WeilContainment` (6.3s) and `Solution.WeilContainmentC2One` (3.3s); 0 lines containing "warning" or "error".
* `lake build Solution.WeilContainmentC2` (after the first, one at a time): *Build completed successfully (8698 jobs)*, exit 0; only
  `Solution.WeilContainmentC2` (3.3s) built; 0 warnings, 0 errors. The builder's figures (8698 jobs each, 0/0) are reproduced.

## 2. #print axioms (`check-O/print-axioms.log`, `check-O/probe_h5.log`)

    'weilContainment_c2_interpolant_log3' depends on axioms: [propext, Classical.choice, Quot.sound]
    'weilContainment_c2_interpolant' depends on axioms: [propext, Classical.choice, Quot.sound]

No `sorryAx`, no `Lean.ofReduceBool`. The configs name one theorem each, so these are every theorem name. The probe
`check-O/probe_h5.lean` (run in the clone) adds: both helper theorems `WeilContainmentC2{,One}.Proof.interpolant` on the same three
axioms; `#check` of `interpolant` shows NO evenness hypothesis (the kernel's confirmation of ERRATA E2 / FIDELITY (D2));
`#print weilContainment_c2_interpolant_log3` shows the body `fun a g x hc hs => WeilContainmentC2One.Proof.interpolant a (Real.log 3) g hc hs`
(the evenness argument is bound and discarded); the brief's rung-1 spelling `∃ k,` (no ascription) is accepted as the type of the shipped
theorem (elaborates to the same term); and the witness is in the class `EF_lit` quantifies over (`ContDiff ℝ 2 k ∧ HasCompactSupport k`,
by `IsCompact.of_isClosed_subset isCompact_Icc (isClosed_tsupport k)`), which is what the headers' "a member of the class Zeta23's
`EF_lit` quantifies over" requires (`EF_lit` read at `Zeta23/ExplicitFormula.lean` line 81 in the clone: `∀ k : ℝ → ℂ, ContDiff ℝ 2 k →
HasCompactSupport k → …`; its prime term, lines 70–73, is `primeSide`'s body character for character).
