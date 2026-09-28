# G8 / IV.17 — the Lean typing check of formalization-queue item 10 (deliverable 1; BUILDER, Fable 5.1; Session 30)

Written BEFORE any theorem of the unit. Brief: `results/iv17-lean-s30/BRIEF.md` (SHA-256
`9aabf0dbfb74e602941c490a2a3d417e825f33cfad11e537e5c3ff45ee2ffd70`, recomputed at the start). Item 10 asks: "the counterexample needs the
grid-Parseval identity stated with RATIONAL marks (it is linear algebra, so the extension is mechanical — check the Lean typing of marks
before commissioning)". Checked here against the two files on disk, `lean/Zeta23/PairCeiling/GridParseval.lean` (583 lines) and
`GridCorner.lean` (263 lines), read in full, and by a scratch probe run through the built clone (`typing-probe.lean` in this directory,
`lake env lean`, Lean v4.33.0-rc2 / Mathlib 51e6992e, 8.53 s wall for the whole file including the import).

## 1. Where the mark type enters the existing proofs

`dftMark (ζ : K) (m : ZMod M → ℤ) (r : ZMod M) : K := ∑ k, (m k : K) * chi ζ (r * k)` with `[CommRing K]`. The integer marks enter
ONLY through the cast `(m k : K)`, and every algebraic theorem — `sum_dftMark_mul_neg` (Parseval), `flat_band_trace_sq` (Lemma 1.1),
`sum_band`, `sum_band_pair` — treats `(m k : K)` as an opaque ring element: the proofs use `Finset.sum_mul_sum`, `Finset.sum_comm`,
`sum_chi_mul` (character orthogonality), `Finset.sum_ite_eq'`, and `ring`. No property of ℤ is used (no `omega`, no `Int` lemma, no
cast lemma) in Sections 1–3 of the file. The ℂ specialization (Section 4) uses ONE fact about the marks: `dftMark_neg` rewrites
`conj (m k : ℂ) = (m k : ℂ)` by `map_intCast` — integers are fixed by complex conjugation — and then `Complex.mul_conj` gives
`c_r · c_{−r} = |c_r|²`. `grid_parseval_decoupling` and `trace_sq_grid` then move the identity to ℝ by `exact_mod_cast` (the casts
`((m k : ℤ) : ℂ) = (((m k : ℤ) : ℝ) : ℂ)`, `Int.cast` norm_cast lemmas). `gridRow`/`gridRow_eq` (GridCorner Section 2) only wrap
`trace_sq_grid` and push the cast of `Σ m²` from ℤ to ℝ.

Where ℤ IS used: `two_mul_distinct_ge` (the master inequality) and `mark_one_count_ge` (Lemma 2.2(b)) — the per-atom case split
`m k = 0 ∨ m k = 1 ∨ 2 ≤ m k` by `omega`, and `nlinarith [(m − 1)(m − 2) ≥ 0]`. THAT is the integrality, and it is exactly the line the
unit must isolate (`per_atom_slack`) and exhibit as false over ℚ.

## 2. What generalizes to ℚ verbatim, and what does not

* `(m k : K)` for `m : ZMod M → ℚ` does NOT typecheck over `[CommRing K]` (probe (a): "Type mismatch … has type ℚ … expected K"):
  `Rat.cast` needs `[RatCast K]`, supplied by `DivisionRing`. It DOES typecheck over `[Field K]` (probe (a′)). So the rational
  generalization cannot be "the same statements with ℚ in place of ℤ over a general commutative domain"; the coefficient ring must be a
  field, and ℂ is one. **Decision:** the Parseval algebra is stated once for a GENERAL coefficient vector `v : ZMod M → K` over the same
  `[CommRing K] [IsDomain K]` as the integer file (`dftVec`, `sum_dftVec_mul_neg`, `flat_band_trace_sq_vec`) — the proofs of the
  integer file transfer word for word with `v k` in place of `(m k : K)` — and BOTH `dftMark ζ m = dftVec ζ (fun k => (m k : K))`
  (ℤ marks, any commutative domain) and `dftMarkQ ζ m = dftVec ζ (fun k => (m k : K))` (ℚ marks, `[Field K]`) are its instances by
  `rfl`. This is stronger than the brief's clause (1) asks (rational marks) and is the honest shape of "it is linear algebra".
* The ℂ specialization transfers with ONE lemma exchanged: `map_intCast` → `map_ratCast` (probe (b): `map_ratCast` exists for ring
  homs between division rings; `starRingEnd ℂ` qualifies; the `example` typechecks). Rationals are fixed by conjugation, so
  `c_{−r} = conj c_r` and `c_r c_{−r} = |c_r|²` hold for rational marks exactly as for integer marks. Moving to ℝ:
  `Complex.ofReal_ratCast` (probe (b)) replaces `Complex.ofReal_intCast` in the `exact_mod_cast` step.
* `gridRowQ` and `gridRowQ_eq` are `gridRow`/`gridRow_eq` with `ℚ` for `ℤ` and `Rat.cast` for `Int.cast`.
* A cast lemma `m ↦ (m : ℚ)` is NOT enough and is not what is built: the marks of the instance are genuinely rational (`4/3`). The
  compatibility `dftMark ζ m = dftMarkQ ζ (fun k => (m k : ℚ))` (by `Rat.cast_intCast`, probe (b)) is recorded as a theorem so that the
  integer theory is visibly the restriction of the rational one, but nothing in the unit rests on it.
* `two_mul_distinct_ge` / `mark_one_count_ge` do NOT generalize — by design: over ℚ the per-atom slack `(m − 1)(m − 2) ≥ 0` is false
  at `m = 4/3` (value `−2/9`), and the unit's theorem `mi_fails_rational` is the statement that the master inequality fails.

**Stop line (i) does NOT fire:** no new idea is needed; the generalization is the same proof with a general coefficient vector, plus
two cast-lemma substitutions. No H-row hypothesis will be displayed.

## 3. Kernel evaluation over ℚ on `ZMod 65` (stop line (ii))

Probe (c): with `fracMarkProbe k := if k.val < 48 then 4/3 else 0`, the three facts `Σ = 64`, `Σ (·)² = 256/3`, `#{k | ≠ 0} = 48` all
close by `decide +kernel` (no `native_decide`, no `norm_num` fallback needed); the whole probe file, including the import of
`Zeta23.PairCeiling.GridCorner`, took 8.53 s wall (`/usr/bin/time`). `Rat` arithmetic reduces in the kernel because `Nat.gcd`, `Nat.div`,
`Nat.mod` are kernel-accelerated and `Rat`'s `DecidableEq` is the derived structural one. **Stop line (ii) does NOT fire.** The probe's
`#print axioms` prints `[propext, Classical.choice, Quot.sound]` for all three — the three standard axioms (the brief's "`[propext,
Quot.sound]` or fewer" ceiling is NOT met here; `Classical.choice` enters through Mathlib's `Rat`/`Finset` instances; it is within the
Comparator's permitted set and within the label). Recorded as a fidelity note, not a defect.

## 4. Consequences for the module layout (clause (5))

`Zeta23/PairCeiling/GridParsevalRat.lean` (imports `GridCorner`): `dftVec`, the two general theorems, `dftMarkQ`, `dftMark_eq_dftVec`,
`dftMarkQ_eq_dftVec`, `dftMark_eq_dftMarkQ`, the ℂ lemmas `dftMarkQ_neg`, `dftMarkQ_mul_neg_eq_normSq`, `grid_parseval_decoupling_rat`,
`trace_sq_grid_rat`, `gridRowQ`, `gridRowQ_eq`. `Zeta23/PairCeiling/GridGap.lean` (imports `GridParsevalRat`): `per_atom_slack`,
`per_atom_floor`, `per_atom_slack_fails_rational`, `fracMark` and its four kernel facts, `fracMark_row`, `mi_holds_integer`,
`mi_fails_rational`, `corner_fails_rational`. The Comparator's trusted layer `ChallengeDeps/IntegralityGap.lean` re-declares, over
Mathlib only, `chi`, `dftMark`, `dftMarkQ`, `zetaM`, `gridRow`, `gridRowQ`, `fracMark` character for character (namespace
`IntegralityGap`), so that the Solution's delegation to the Zeta23 modules typechecks by definitional unfolding (the SeparationG1
precedent).
