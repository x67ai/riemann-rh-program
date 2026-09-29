# H5 — the attack on the orchestrator's pre-derivation of BRIEF.md §0 (builder, Fable 5.1; Session 32, 2026-09-29)

Brief: `results/h5-c2-lean-s32/BRIEF.md`, SHA-256 `1a2e8a3acb4c6ba0623a9cf91ac515952490d49767717dd4b09af45f5c4e49ab` (recomputed Tue Sep 29 06:30:41 IST 2026).
Method: every step (P1)–(P6) of §0's single-model pre-derivation re-derived by hand against the trusted definitions of
`lean/comparator/ChallengeDeps/WeilContainment.lean` (`primeSide`, `tiltedPrimeSide`; unchanged) and against Mathlib at 51e6992e as it
sits in `~/rh-lean-work/checker-clone-s21/.lake/packages/mathlib` (`Mathlib/Analysis/Calculus/BumpFunction/Basic.lean`: `structure
ContDiffBump` line 70, `ContDiffBump.neg` 132, `one_of_mem_closedBall` 137, `tsupport_eq` 157, `zero_of_le_dist` 163, `contDiff` 203 —
re-read at the line this session; the four the brief names are present with the signatures it states, so stop line (i) does NOT fire).
Mathlib conventions inherited by the formal statement: `tsum` of a non-summable family is 0; `Real.log 0 = Real.log 1 = 0`;
`vonMangoldt 0 = vonMangoldt 1 = 0`; `Real.sqrt 0 = 0`; `Real.rpow` on the cast `(n : ℝ)`; `tsupport g = closure (Function.support g)`.
"No error found" entries name the check that was run.

**Verdict up front.** The pre-derivation is correct in substance and the statement's SHAPE is unchanged — stop line (iv) does NOT
fire. One genuine gap (E1: the case split as written does not cover L = log 2, where the interior set is empty and (P3)'s "finite
nonempty set" is false), repaired inside the proof by splitting on the interior set instead of on L. One unused hypothesis (E2: the
evenness of g is never used — kept as displayed, because the brief fixes the statement). One design simplification adopted in Lean
(E3: one bump times an even Lagrange interpolant replaces the δ-separated family of bumps; the witness is still an interpolant at
±log n, so the label's clause stays exact). Four checks with no error (E4–E7).

## (P1) L < log 2 ⟹ k := 0 — no error found

Check: for n ≥ 2, `Real.log n ≥ Real.log 2 > L`, so `Real.log n ∉ Set.Icc (-L) L`, hence `Real.log n ∉ tsupport g` and `g (Real.log n) = 0`
(`image_eq_zero_of_notMem_tsupport`). The cutoff sum over `Finset.range (⌊Real.exp L⌋₊ + 1)` has ⌊e^L⌋₊ ≤ 1 (e^L < 2), so it ranges over
n ∈ {0, 1} at most, where Λ = 0. So `tiltedPrimeSide a g = 0`. `k = 0` is even, `ContDiff ℝ 2` (`contDiff_const`), `tsupport 0 = ∅`
(`Function.support` of the zero function is empty, closure of ∅ is ∅), and `primeSide 0 = ∑' n, (…) * (0 + 0) = 0`. Correct.

## (P2) the interior set I and the edge — one gap (E1), one precision note (E4)

**E1 (gap — the case L = log 2).** (P1) treats L < log 2 and (P2) "otherwise", i.e. L ≥ log 2. At L = log 2 exactly, N = ⌊e^{log 2}⌋₊ = 2
and I = {n : 2 ≤ n ≤ 2, log n < log 2} = ∅. Then (P3)'s "δ … smaller than L − max_{n∈I} log n (a positive minimum over a finite
NONEMPTY set)" is false: I is empty, there is no max and no δ, and (P4)'s sum over I is the empty sum — which is in fact the right
witness (k = 0: the n = 2 term of the cutoff sum is Λ(2)·2^{−a}·g(log 2) = 0 because g(L) = 0 by continuity, exactly (P2)'s own edge
argument). So the conclusion is TRUE at L = log 2 but the argument as written does not reach it. Repair (what the Lean proof does):
split on `I = ∅` versus `I.Nonempty` (with I := the n in `Finset.range (N + 1)` with 2 ≤ n and log n < L), not on L < log 2. In the
empty case k := 0 works for every L (every term of the cutoff sum vanishes: n ≤ 1 by Λ = 0, n ≥ 2 by L ≤ log n and the closed-set
argument of E4); in the nonempty case the construction goes through. The theorem's statement is unaffected (stop line (iv) does not
fire); the brief's (P1) is subsumed by the empty case.

**E4 (precision, no error).** (P2)'s "g(L) = 0, because g = 0 on (L, ∞) (tsupport ⊆ Icc) and g is continuous at L" is correct. The
mechanism the Lean proof uses, stated so the checker can re-derive it: `{u | g u = 0}` is closed (`isClosed_eq hg continuous_const`),
contains `Set.Ioi L` (a point u > L is outside `Set.Icc (-L) L`, hence outside `tsupport g`), hence contains `closure (Set.Ioi L) =
Set.Ici L` (`closure_Ioi`). So g u = 0 for EVERY u ≥ L, not only at u = L. The remark "at most one n with log n = L, and only when
e^L ∈ ℕ" is true but not needed: for n ∈ `Finset.range (N + 1)` with n ∉ I one has n ≤ 1 (Λ(n) = 0) or L ≤ log n (g(log n) = 0 by the
closed-set argument); no equality case is ever distinguished. Also correct: N ≥ 2 when L ≥ log 2 (e^L ≥ 2 ⟹ ⌊e^L⌋₊ ≥ 2), and for n > N,
`Real.exp L < n` (`Nat.lt_of_floor_lt`) gives L < log n (`Real.lt_log_iff_exp_lt`), so g(log n) = 0 — the cutoff step is the D5 proof
of `weilContainment_cutoff`, re-proved locally in the solution modules (a solution imports Mathlib and `ChallengeDeps` only; it may not
import the challenge, and D5's solution module is not imported either, so each topic stays self-contained as D5's did).

## (P3) the points ±log n, their distinctness, and δ — no error found (E5)

**E5 (check).** "log is injective on ℕ" is false on ℕ (`Real.log 0 = Real.log 1 = 0`) but the sentence is applied to n ∈ I ⊆ {n ≥ 2},
where it is true (`Real.log_injOn_pos`). log n ≥ log 2 > 0 > −log 2 ≥ −log m: correct, so the 2|I| points are pairwise distinct. All in
(−L, L): log n < L by the definition of I. δ > 0 exists when I ≠ ∅ (E1). One clause the pre-derivation does not spell out but needs
in (P4): the MIRRORED bump centered at −log n must vanish at the unmirrored points log m, which requires δ < log n + log m; this
follows from the δ clause "smaller than half the minimum distance between any two of the points", because the pair {log n, −log n} is
among them, at distance 2 log n ≥ 2 log 2, so δ < log 2 ≤ (log n + log m)/2. No error.

## (P4)–(P5) the witness — correct as written; a simpler witness is built (E3)

Check of (P4): `ContDiffBump (Real.log n)` with `rIn = δ/2 < rOut = δ` is a legal structure (`0 < rIn < rOut`); the instance
`HasContDiffBump ℝ` is `hasContDiffBump_of_innerProductSpace` (`Mathlib/Analysis/Calculus/BumpFunction/InnerProduct.lean` line 57);
`one_of_mem_closedBall` gives φ_n(log n) = 1; every other bump vanishes at log n because the distance exceeds rOut = δ
(`zero_of_le_dist`); k(log m) = c_m and k(−log m) = c_m. Check of (P5): each summand `u ↦ φ_n u + φ_n (−u)` is even and `ContDiff ℝ n`
for every n (`ContDiffBump.contDiff`, `ContDiff.comp` with `contDiff_neg`, `ContDiff.add`); a finite sum of C^∞ functions is C^∞
(`ContDiff.sum`); tsupport of a finite sum ⊆ union of the tsupports ⊆ Icc (−L) L by δ < L − max log I. Correct.

**E3 (design; no error in the pre-derivation, but the Lean proof takes a shorter route).** The δ bookkeeping of (P3)–(P4) — a
uniform separation radius, one bump per interior point, the mirrored copies, and the three disjointness facts — is unnecessary. Let
M := max I (so log M = max_{n∈I} log n, with 0 < log 2 ≤ log M < L) and take ONE bump φ : `ContDiffBump (0 : ℝ)` with rIn = log M and
rOut = L. Then φ = 1 on `closedBall 0 (log M) = Icc (−log M) (log M)`, which contains ±log n for every n ∈ I; φ(±log n) = 0 for every
n ≥ 2 with n ∉ I, because then L ≤ log n = |±log n| = dist (±log n) 0 = rOut (`zero_of_le_dist`); φ is even (`ContDiffBump.neg`);
`tsupport φ = closedBall 0 L = Icc (−L) L` (`tsupport_eq`, `Real.closedBall_eq_Icc`). For the values, interpolate in the EVEN
variable x = u²: the nodes x_n := (log n)², n ∈ I, are pairwise distinct (log n ≥ 0 on I, and `pow_left_inj₀` on [0, ∞) followed by
`Real.log_injOn_pos`), so Mathlib's `Lagrange.interpolate I v r` (`Mathlib/LinearAlgebra/Lagrange.lean` line 299; `eval_interpolate_at_node`
line 319) with v n := ((log n)² : ℂ) and r n := c_n = (1/2)·n^{1/2−a}·g(log n) gives a polynomial P over ℂ with P(x_n) = c_n on I.
The witness is k(u) := P(u²)·φ(u). It is even by construction ((−u)² = u², φ(−u) = φ(u)); it is C^∞, hence `ContDiff ℝ 2` (a polynomial
is C^∞ over ℂ by induction on the polynomial, restricted to ℝ scalars, composed with u ↦ (u² : ℂ); times `Complex.ofRealCLM ∘ φ`);
`tsupport k ⊆ tsupport φ` (`tsupport_mul_subset_right`); k(±log n) = P((log n)²)·1 = c_n for n ∈ I and k(±log n) = 0 for n ∉ I, n ≥ 2.
So k interpolates the prescribed values at ±log n exactly as (P4)'s k does — the label's clause "the C² witness is an interpolant at
±log n, not the tilted test" describes it word for word — with none of the separation estimates. At rung 1 (L = log 3, I = {2}) the
polynomial is the constant c_2 and k = c_2·φ with rIn = log 2, rOut = log 3.

## (P6) the prime side of the witness — no error found (E6)

**E6 (check).** For n ∈ I: (Λ(n)/√n)·(k(log n) + k(−log n)) = (Λ(n)/√n)·2c_n = Λ(n)·n^{−1/2}·n^{1/2−a}·g(log n) = Λ(n)·n^{−a}·g(log n):
`Real.sqrt_eq_rpow`, `Real.rpow_neg`, `Real.rpow_add` on (n : ℝ) > 0 — the D5 computation `h3` of `Solution/WeilContainment.lean`,
valid for every n ≥ 1, so for n ≥ 2 in particular. For n ∉ I: n ≤ 1 gives Λ(n) = 0 (`ArithmeticFunction.map_zero`,
`vonMangoldt_apply_one`); n ≥ 2 with n ∉ I gives L ≤ log n (either n > N, whence L < log n, or n ≤ N with ¬(log n < L)), so both
k(log n) and k(−log n) vanish (E3) and the summand is 0. The tsum has support inside I ⊆ `Finset.range (N + 1)`, so `tsum_eq_sum`
turns it into the finite sum over I, and `Finset.sum_subset` (I ⊆ range (N + 1), the non-I terms vanish by (P2)/E4) identifies it
with the cutoff sum, i.e. with `tiltedPrimeSide a g`. Correct. The pre-derivation's "the support stays ≤ max log I + δ < L" is the
δ-design's version of the same fact; in the E3 design the vanishing at n ∉ I is `zero_of_le_dist` directly.

## The statement itself — two notes (E2, E7)

**E2 (unused hypothesis, no error).** Neither the pre-derivation nor the proof ever uses `∀ u, g (-u) = g u`: `tiltedPrimeSide a g`
reads g only at the points log n ≥ 0, and the witness's evenness comes from its construction, not from g's. So the theorem is true
for every CONTINUOUS g with `tsupport g ⊆ Set.Icc (-L) L`, even or not. Decision: the evenness hypothesis is KEPT as displayed. The
brief fixes the statement verbatim and says the displayed hypotheses are exactly the three; the record's family (cos-transforms of
windows) is even, and an unused hypothesis is a redundancy, not a divergence (D5's E4 dropped a redundant `0 ≤ L` because that brief
listed statements to be shaped; this brief prescribes the statement). Recorded in FIDELITY.md as a "differs from the prose" row so
that no reader takes evenness of g to be load-bearing. No stronger variant is added (footprint).

**E7 (check).** The statement type-checks as written at 51e6992e: `ContDiff ℝ 2 k` has smoothness index in `WithTop ℕ∞` (the numeral
2 elaborates there); `ContDiffBump.contDiff : ContDiff ℝ n f` is stated for `n : ℕ∞` coerced, so the witness's C² property is obtained
from its C^∞ property by `ContDiff.of_le` (or by instantiating n). `primeSide k = tiltedPrimeSide a g` is an equation in ℂ between
two `tsum`s over ℕ; both are finite sums for the data at hand (E6), so no summability question arises. Nothing in the statement
mentions `EF_lit`, Zeta23, ζ, a zero, or the zero side; the theorem is a statement about prime-side VALUES.

## Rung 1 (L = log 3) — no error found

Check: N = ⌊e^{log 3}⌋₊ = ⌊(3 : ℝ)⌋₊ = 3 (`Real.exp_log`, `Nat.floor_ofNat`); I = {2} (log 2 < log 3; log 3 < log 3 is false, so n = 3 is
the edge, where g(log 3) = 0 by E4); the general proof instantiated at L = log 3 is the rung-1 proof (as D5's rung 1 instantiated
its general computation at a = 1). The brief's reading — "n = 2 is interior, n = 3 sits at the edge" — is correct.

## Summary of what changed against §0

Nothing in the two statements. In the proof: the case split is on I = ∅ (E1), and the witness is P(u²)·φ(u) with one bump (E3)
rather than the δ-separated sum. Recorded also in BUILD-NOTES "Statement decisions" and in FIDELITY.md.
