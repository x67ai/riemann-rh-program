# G8 — FIDELITY ledger for the Comparator topic `IntegralityGap` (barrier-zoo IV.17, the fractional-mark integrality barrier); builder Fable 5.1, Session 30, 2026-09-29

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (v)). Brief: `results/iv17-lean-s30/BRIEF.md` §2 item 3. The record
the statements are read against: zoo IV.17 STATEMENT (the master inequality "(MI) F1(c) ≥ 3M(c) − 2N_d(c)"; "(MI) is FALSE for
fractional marks, at the baseline itself: mass N of mark-4/3 atoms on the (N+1)-site grid … has F1 = (3/4)N·(16/9) = (4/3)N,
budget-tight, and N_d = (3/4)N < (5/6)N, while (MI) would demand F1 ≥ 3N − (3/2)N = (3/2)N"; "Integrality is consumed through exactly
two devices … the per-zero slack (m − 1)(m − 2) ≥ 0 … and the mark-1 floor m² ≥ m"), its EXECUTABLE TEST (1) and (3), `theorems.md`
Lemma 2.2 (the two integrality levels) and Theorem 2.3, `paper.md` §2.4 and §4.2, and formalization-queue item 10 ("N = 64: 48 atoms of
mark 4/3 on distinct grid sites; F1 = Σ m² = 256/3 = (4/3)·64, N_d = 48, 3M − 2N_d = 96 > 256/3").

**First paragraph, binding (10(c)).** Nothing about ζ or RH follows from anything below. The theorems are statements about mark
vectors on a finite cyclic grid and one quadratic form on them (the bandwidth-one Frobenius row); no zero, no zero configuration, no
explicit formula, no law, and no property of ζ appears in any statement. The label the unit earns (BRIEF §1(6)), verbatim: "IV.17's
master inequality is a Comparator-checked theorem over integer marks and a Comparator-checked FALSEHOOD over rational marks on the same
Frobenius row (the mark-4/3 instance kernel-checked), over Mathlib alone, no displayed hypothesis, axioms
propext/Classical.choice/Quot.sound, replayed by nanoda". The pair channel stays unformalized, and the label says so.

## 1. What IS covered — each claim is a theorem in `lean/comparator/Challenge/IntegralityGap.lean` (proved in `Solution/IntegralityGap.lean` by delegation to `Zeta23/PairCeiling/{GridCorner, GridParsevalRat, GridGap}.lean`)

| record's claim | theorem | exact content |
|---|---|---|
| grid Parseval "stated with RATIONAL marks" (item 10; paper Thm 3.9 = theorems.md Thm 1.2, F1 = Σm²) | `trace_sq_grid_rat` | ∀ n, ∀ m : ZMod (2n+1) → ℚ: Σ_{j₁,j₂ ∈ [−n,n]} (1/(2n+1))² · normSq (c_{j₁+j₂}) = Σ_k (m k : ℝ)², c = `dftMarkQ (zetaM (2n+1)) m` |
| the row as a named quantity, rational marks | `gridRowQ_eq` | `gridRowQ n m = ((Σ_k (m k)² : ℚ) : ℝ)` |
| the row as a named quantity, integer marks (GridCorner's Theorem 1.2 equality) | `gridRow_eq` | `gridRow n m = ((Σ_k (m k)² : ℤ) : ℝ)` |
| "on the same Frobenius row" — the integer row IS the rational row of the cast marks | `gridRow_eq_gridRowQ` | `gridRow n m = gridRowQ n (fun k => (m k : ℚ))` |
| the instance, "N = 64: 48 atoms of mark 4/3 on distinct grid sites" — mass 64 | `fracMark_mass` | `Σ_k fracMark k = 64` (`decide +kernel`) |
| "F1 = Σ m² = 256/3 = (4/3)·64" | `fracMark_sq` | `Σ_k (fracMark k)² = 256/3` (`decide +kernel`) |
| "N_d = 48" | `fracMark_Nd` | `#{k : ZMod 65 ∣ fracMark k ≠ 0} = 48` (`decide +kernel`) |
| "budget-tight": F1 = (4/3)N at ε = 0 | `fracMark_row` | `gridRowQ 32 fracMark = 4/3 · 64 · (1 + 0)` |
| "(MI) is FALSE for fractional marks" (STATEMENT; TEST (1): a relaxation "must FAIL to certify F1 ≥ 3M − 2N_d") | `mi_fails_rational` | `¬ ∀ m : ZMod 65 → ℚ, (∀ k, 0 ≤ m k) → 3·Σm − Σm² ≤ 2·#{k ∣ m k ≠ 0}` — "3M − 2N_d = 96 > 256/3" |
| "N_d = (3/4)N < (5/6)N" — the 5/6 baseline is false for fractional marks on the grid at ε = 0 | `corner_fails_rational` | `(∀ k, 0 ≤ fracMark k) ∧ Σ fracMark = 64 ∧ gridRowQ 32 fracMark ≤ 4/3·64·(1+0) ∧ (48 : ℝ) < 64·(5/6 − 2/3·0)` — every hypothesis of `grid_corner_pointwise` at N = 64, ε = 0 and the negation of its first conclusion |
| the same as a negated universal (Theorem 2.3's first conclusion with ℚ for ℤ) | `corner_bound_fails_rational` | `¬ ∀ m : ZMod 65 → ℚ, 0 ≤ m → Σm = 64 → gridRowQ 32 m ≤ 4/3·64·(1+0) → 64·(5/6 − 2/3·0) ≤ N_d` |
| "(MI) F1 ≥ 3M − 2N_d" over integer marks (theorems.md Lemma 2.2(a)) | `mi_holds_integer` | `∀ M [NeZero M] (m : ZMod M → ℤ), (∀ k, 0 ≤ m k) → 3·Σm − Σm² ≤ 2·#{k ∣ m k ≠ 0}` — `two_mul_distinct_ge` re-exported |
| "the per-zero slack (m − 1)(m − 2) ≥ 0" — the line where integrality is consumed (TEST (3)) | `per_atom_slack` | `∀ m : ℤ, 0 ≤ (m − 1)·(m − 2)` |
| … and it is an integer fact | `per_atom_slack_fails_rational` | `¬ ∀ q : ℚ, 0 ≤ q → 0 ≤ (q − 1)·(q − 2)` (witness 4/3: −2/9) |
| "the mark-1 floor m² ≥ m" (the second device of TEST (3)) | `per_atom_floor` | `∀ m : ℤ, m ≤ m²` |
| … and it is an integer fact | `per_atom_floor_fails_rational` | `¬ ∀ q : ℚ, 0 ≤ q → q ≤ q²` (witness 1/2) |

All sixteen: no displayed hypothesis; axioms `[propext, Classical.choice, Quot.sound]` (`print-axioms.log`); statement identity
challenge/solution 16/16 (`statement-identity.log`); the Comparator run with nanoda PASS (`comparator.log`).

## 2. What is NOT covered — stated nowhere in Lean

* **Laws.** IV.17's corner is a statement about LAWS (probability mixtures of columns) with E[F1] ≤ (4/3)N(1 + ε); the negation here is
  POINTWISE (one column). The law form of the negation follows at once (a one-column law), and the integer law form is already
  `grid_corner_law` (GridCorner.lean); neither a rational law form nor its negation is stated.
* **The pair channel.** Paper Prop. 4.5 = `pair-channel.md` Prop. 3.1 (F1 − S2 = 2μ²ā(2d)² − 4μ(ā(d)² − 1), NEGATIVE for small real μ;
  the numeric anchor (d, μ) = (0.25, 0.05), F1 − S2 = −3.520·10⁻²) and the integer-mark safety chain — "paper-certificate grade, or
  Lean only with interval arithmetic on ā" (item 10). Nothing about pairs, depths, or ā appears in any statement. TEST (2) is untouched.
* **Other budgets.** Only the bandwidth-one grid row (λ = 1, symmetric band {−n, …, n}, uniform weights (1/(2n+1))²). Nothing about the
  two-sided band, the λ' = 1/2 cubic block, the cubic row, the half-band F' of GridWitness.lean, or any other row.
* **Off the grid.** Marks live on the (2n+1)-site uniform grid (`ZMod (2n+1)`); the atom-only class at arbitrary positions (Lemma 2.1,
  F1 ≥ Σm² off the grid) is not formalized, as GridCorner.lean's header records.
* **Theorem 2.3 over ℚ in any positive form; the second corner (n₁ ≥ N(2/3 − (4/3)ε)) over ℚ** — not stated (its integer form is
  `mark_one_count_ge` / `grid_corner_pointwise`).
* **ζ, RH, any zero, any explicit formula.**

## 3. Where the formal statements differ from the prose (the yaml row (v), item by item)

* **(v1) The row's normalization.** "F1" is the literal SPEC-1.4 double sum with uniform weights (1/(2n+1))² on the symmetric band —
  `gridRow`/`gridRowQ`, a real number, the same normalization as GridParseval's `trace_sq_grid`. The prose's F1 is this row.
* **(v2) `ZMod 65` for "the (N+1)-site grid".** N = 64, M = 2n + 1 = 65 with n = 32; the instance is at that one size, not for
  every N (the zoo's "mass N of mark-4/3 atoms on the (N+1)-site grid" is a family; the record's numbers are at N = 64). The zoo's
  numbers are stated verbatim; no smaller instance was needed (stop line (ii) did not fire; `decide +kernel` closed the three ℚ
  facts on `ZMod 65` in under two seconds inside the module build).
* **(v3) The instance at ε = 0.** F1 = (4/3)·64 exactly (`fracMark_row`), so the budget hypothesis holds at ε = 0 with equality; the
  corner negation is the ε = 0 case of `grid_corner_pointwise`'s first conclusion with ℚ for ℤ. The record's "N_d = (3/4)N < (5/6)N"
  is the same fact (48 < 160/3).
* **(v4) The form of (MI).** `mi_fails_rational` negates (MI) as `3·Σm − Σm² ≤ 2·N_d` (the statement of `two_mul_distinct_ge` with ℚ
  for ℤ, N_d = #{k | m k ≠ 0}), not as "F1 ≥ 3M − 2N_d"; on the grid the two coincide by `gridRowQ_eq`, and
  `corner_bound_fails_rational` states the row form (with `gridRowQ` in the hypothesis).
* **(v5) Nonnegative marks, no floor.** The negation quantifies over nonnegative rational marks (empty sites are m = 0); the record's
  integer atoms have m ≥ 1, and the fractional relaxation is exactly the removal of that floor. `mi_holds_integer` likewise takes
  0 ≤ m, as GridParseval's `two_mul_distinct_ge` does.
* **(v6) `per_atom_slack` for EVERY integer.** Stated for all m : ℤ (the product of two consecutive integers is nonnegative), not only
  m ≥ 1 as Lemma 2.2(a) — stronger, and it is the line the proof of `two_mul_distinct_ge` consumes (`nlinarith [(m − 1)(m − 2) ≥ 0]`
  at 2 ≤ m; the cases m = 0, 1 are direct). `mi_holds_integer` is a re-export of `two_mul_distinct_ge`, not a re-proof through
  `per_atom_slack`; the two theorems are separately named, as the brief asks, and the proof text of `two_mul_distinct_ge` is where a
  reader sees the slack consumed.
* **(v7) General-coefficient Parseval.** The algebra is proved once for `dftVec : ZMod M → K` over the integer file's `[CommRing K]
  [IsDomain K]`; rational marks need `[Field F]` for the cast ℚ → F (item 10's typing fact, TYPING-NOTE.md) and are the instance
  `v = (m · : F)` by `rfl`. Stronger than the brief's clause (1) ("rational marks"); the brief's alternative "a cast lemma m ↦ (m : ℚ)"
  was not used — the instance's marks are genuinely rational.
* **(v8) The axioms of the `decide +kernel` facts.** They print all three standard axioms (`Classical.choice` enters through Mathlib's
  `Rat`/`Finset` instances), not the `[propext, Quot.sound]` the brief anticipated from GridCorner's record; GridCorner's own
  `attainMark_mass`/`attainMark_sq` print the same three at this toolchain (`print-axioms.log`, last two lines). Within the permitted
  set and within the label.
* **Naming.** The brief's names are kept verbatim (`trace_sq_grid_rat`, `gridRowQ_eq`, `fracMark`, `mi_fails_rational`,
  `corner_fails_rational`, `mi_holds_integer`, `per_atom_slack`); added: `gridRow_eq`, `gridRow_eq_gridRowQ`, `fracMark_row`,
  `corner_bound_fails_rational`, `per_atom_slack_fails_rational`, `per_atom_floor`, `per_atom_floor_fails_rational`; `dftMarkQ` is the
  brief's name; the general `dftVec` is new.

## 4. Character-for-character claims for the checker to `diff`

`IntegralityGap.chi`, `dftMark`, `zetaM` against `Zeta23/PairCeiling/GridParseval.lean` (`chi`, `dftMark`, `zetaM`);
`IntegralityGap.gridRow` against `GridCorner.lean` (`gridRow`); `IntegralityGap.dftMarkQ`, `gridRowQ` against
`GridParsevalRat.lean` (`dftMarkQ`, `gridRowQ`); `IntegralityGap.fracMark` against `GridGap.lean` (`fracMark`). The delegations in
`Solution/IntegralityGap.lean` typecheck only because these are definitionally equal after unfolding — the Solution's clean build
(0 errors) is itself the check, and the Comparator's statement comparison confirms the challenge side.

**[CORRECTION 01:22 IST 2026-09-29, Session 30 — from CHECK-O F1/F2 (Opus 5, clean clone `~/rh-lean-work/checker-clone-s30b`), re-derived by the orchestrator at the file; the Lean files are NOT edited (the D5 precedent: a comment change would alter the hash and oblige a fresh comparator run for no change in content).]** (F1) `GridGap.lean` lines 40–42 say "the five column-data facts … are kernel-checked (`decide +kernel`)": exactly THREE facts are `decide +kernel` (`fracMark_mass`, `fracMark_sq`, `fracMark_Nd`); `fracMark_nonneg` is `norm_num`, and `fracMark_row` is rational Parseval (`gridRowQ_eq`) plus `fracMark_sq` — the row contains `Complex.exp` and no decision procedure could decide it. The same slip is in the `results/a4-no-go/formalization-status.md` addendum ("row = (4/3)·64 — kernel-checked by `decide +kernel`"): the first three are kernel-checked, the row is by rational Parseval; a dated correction line stands beneath that addendum. (F2) `GridGap.lean` line 93, the docstring of `mi_holds_integer`, says "Its proof consumes integrality at exactly `per_atom_slack`": the proof is `two_mul_distinct_ge m hm`, whose module is upstream of `GridGap` and carries an inline copy of the slack step (`nlinarith [mul_nonneg (… m k − 1) (… m k − 2)]`); the content is exactly `per_atom_slack` summed over occupied sites (2 − (3m − m²) = (m − 1)(m − 2)), and the checker proved the dependency in content (`check-O/` probes `checker_mi_of_slack`: (MI) for every nonnegative rational mark vector whose marks satisfy (m − 1)(m − 2) ≥ 0; `checker_mi_integer_via_slack`: the integer (MI) with `per_atom_slack` as its only integrality input) — only the wording "the proof term uses the constant" is false. Neither item touches a statement, a proof, an axiom, the comparator result or the label. Optional later hygiene (not owed): add `mi_of_slack` to `GridGap` and restate the re-export through it (Solution side only; rebuild + one comparator run).
