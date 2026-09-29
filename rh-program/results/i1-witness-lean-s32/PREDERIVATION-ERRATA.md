# I.1 witness table — the attack on the orchestrator's pre-derivation of BRIEF.md §0 (builder, Fable 5.1; Session 32, 2026-09-29)

Brief: `results/i1-witness-lean-s32/BRIEF.md`, SHA-256 `54ad13fb0b6197d241bae84de43942d6e1e7396bc0050eb965cc503f62aa3b69` (recomputed at the start).
Method: every line of §0's single-model pre-derivation of (D2), every value the statements (E1), (E2), (D1), (D2), (D3) assert, and the
box-count definition of `epsteinB` re-derived by hand against the record — `results/c3-r/m0-axiom-note.md` §6.1–§6.2 (the DH table, the
Epstein normalization), `results/c3-m0-epstein/n1_epstein_witness.json` (`witness_i`, `witness_ii`, `all_nonzero_lambda_n_le_100`) and
`n1_epstein_witness.py` (`lam_exact`: `lam[n] = b_n·log n − Σ_{1<d<n, d|n} lam[d]·b[n/d]`, the recursion as it ran on disk). Typing facts
(E9, E11) were measured in the program tree `~/rh-lean-work/checker-clone-s21` (Lean v4.33.0-rc2, Mathlib 51e6992e) with the probes kept
under the session scratchpad; the measurements are repeated in `typing.log`. "No error found" entries name the check that was run.

**Verdict up front.** No error that changes a value; stop line (iv) does NOT fire. Every coefficient of the (D2) pre-derivation, every
a_n it uses, and every Epstein count it presupposes is correct. Two gaps of presentation, both closed inside the proofs without changing
any statement: E7 (the third clause of (E2) is not a `decide`) and E13 (the word "hence" in (E1)/(D1)/(D2) omits the primes that
divide nothing — their coefficients vanish by a lemma). Two typing notes (E8, E9), one cost note (E11).

## E1 (check, no error) — the recursion, and the d = 1 and d = n terms
The record's recursion `a_n log n = Σ_{d|n} Λ(d) a_{n/d}` with Λ(1) = 0 and a_1 = 1 has the d = 1 term Λ(1)·a_n = 0 and the d = n term
Λ(n)·a_1 = Λ(n); so `Λ(n) = a_n log n − Σ_{d|n, 1<d<n} Λ(d) a_{n/d}`, which is exactly the loop `for d in range(2, n): if n % d == 0`
of `lam_exact` in `n1_epstein_witness.py`, and exactly the brief's `lambdaVec b n p = b n · e_p(n) − Σ_{d | n, d < n} lambdaVec b d p ·
b (n / d)` once `lambdaVec b 1 = 0` is used for the d = 1 term. The formal definition sums over `Nat.properDivisors n` (the divisors
d with 1 ≤ d < n); the d = 1 summand is `lambdaVec b 1 p · b n = 0`. Correct.

## E2 (check, no error) — the DH coefficients a_n at the divisors of 12
(a₁,…,a₅) = (1, κ, −κ, −1, 0) at n ≡ 1, 2, 3, 4, 0 (mod 5) (`m0-axiom-note.md` §6.1; zoo I.1 STATEMENT). a_2 = κ, a_3 = −κ,
a_4 = −1, a_6 = a_1 = 1 (6 ≡ 1), a_12 = a_2 = κ (12 ≡ 2). All five agree with the brief's use of them. Correct.

## E3 (check, no error) — Λ_DH(2), Λ_DH(3), Λ_DH(4), Λ_DH(6)
Λ(2) = a_2 log 2 = κ log 2. Λ(3) = a_3 log 3 = −κ log 3 (the record's "cheapest witness", −0.3120927…; κ·log 3 = 0.284079·1.098612 =
0.312093 ✓). Λ(4) = a_4 log 4 − Λ(2)a_2 = −2 log 2 − κ² log 2 = −(2 + κ²) log 2 (record: −1.44223196…; (2 + 0.080701)·0.693147 =
1.442232 ✓). Λ(6) = a_6 log 6 − [Λ(2)a_3 + Λ(3)a_2] = log 6 − [−κ² log 2 − κ² log 3] = (1 + κ²) log 6 (record: +1.93635607662…;
1.080701·1.791759 = 1.936356 ✓). Correct.

## E4 (check, no error) — the n = 12 divisor sum and Λ_DH(12)
Proper divisors d > 1 of 12: 2, 3, 4, 6 with 12/d = 6, 4, 3, 2 and a_{12/d} = 1, −1, −κ, κ. The sum Σ Λ(d) a_{12/d} =
κ log 2·1 + (−κ log 3)(−1) + (−(2 + κ²) log 2)(−κ) + (1 + κ²)(log 2 + log 3)·κ; the coefficient of log 2 is κ + κ(2 + κ²) + κ(1 + κ²)
= 4κ + 2κ³, the coefficient of log 3 is κ + κ(1 + κ²) = 2κ + κ³ — the brief's two brackets, re-derived. Then Λ(12) = a_12 log 12 − sum
= κ(2 log 2 + log 3) − (4κ + 2κ³) log 2 − (2κ + κ³) log 3 = −(2κ + 2κ³) log 2 − (κ + κ³) log 3 = −κ(1 + κ²)(2 log 2 + log 3) =
−κ(1 + κ²) log 12. So `lambdaVec dhA 12 2 = −2κ(1 + κ²)` and `lambdaVec dhA 12 3 = −κ(1 + κ²)`, as the brief states. The record's
other form −κ·[κ² log 6 + (2 + κ²) log 2 + log 3] expands to −κ[(2 + 2κ²) log 2 + (1 + κ²) log 3], the same. Numeric:
0.284079·1.080701·2.484907 = 0.762877 (record −0.762877471988…) ✓. Correct.

## E5 (check, no error) — the Epstein counts at the divisors of 36 and the recursion values
r_Q(n) = #{(x, y) ∈ ℤ² : x² + 5y² = n}, b_n = r_Q(n)/2 (normalization of §6.2 and of the JSON). Enumerated by hand:
n = 1: (±1, 0), b = 1. n = 2, 3: none, b = 0. n = 4: (±2, 0), b = 1. n = 6: (±1, ±1), b = 2. n = 9: (±3, 0), (±2, ±1), b = 3.
n = 12: y = 0 gives 12, y = ±1 gives 7 — neither a square; b = 0. n = 18: 18, 13 — b = 0. n = 36: (±6, 0), (±4, ±2) (y = ±1 gives 31);
b = 3. Recursion: Λ(2) = Λ(3) = 0 (b = 0). Λ(4) = 1·(2 log 2) − Λ(2)·b_2 = 2 log 2 (JSON "4": (2)*log(2) ✓). Λ(6) = 2·(log 2 + log 3) −
[Λ(2)b_3 + Λ(3)b_2] = 2 log 2 + 2 log 3 (`witness_i` ✓; (E1)). Λ(9) = 3·2 log 3 − Λ(3)b_3 = 6 log 3 (JSON "9": (6)*log(3) ✓).
Λ(12) = 0·log 12 − [Λ(2)b_6 + Λ(3)b_4 + Λ(4)b_3 + Λ(6)b_2] = 0 − [0 + 0 + 2 log 2·0 + (2 log 2 + 2 log 3)·0] = 0 (12 is absent from
`all_nonzero_lambda_n_le_100` ✓). Λ(18) = 0 − [Λ(2)b_9 + Λ(3)b_6 + Λ(6)b_3 + Λ(9)b_2] = 0 (18 absent ✓). Λ(36) = 3·(2 log 2 + 2 log 3)
− [Λ(2)b_18 + Λ(3)b_12 + Λ(4)b_9 + Λ(6)b_6 + Λ(9)b_4 + Λ(12)b_3 + Λ(18)b_2] = (6 log 2 + 6 log 3) − [0 + 0 + 6 log 2 + (4 log 2 +
4 log 3) + 6 log 3 + 0 + 0] = −4 log 2 − 4 log 3 (`witness_ii` "(-4)*log(2) + (-4)*log(3)" ✓; (E2)). The Lean kernel agrees
(`typing.log`: `lambdaVec epsteinB 36 2 = -4`, `… 3 = -4` decided). Correct.

## E6 (check, no error) — the box |x|, |y| ≤ n is exact
x² ≤ x² + 5y² = n gives |x| ≤ √n ≤ n for n ≥ 1, and 5y² ≤ n gives |y| ≤ √(n/5) ≤ n; at n = 0 the only solution (0, 0) lies in the
box `Icc 0 0`. So `epsteinB n` IS r_Q(n)/2 for every n, with no second definition and no lemma `epsteinB_eq_count` needed; the
FIDELITY row records the box as the definition. Remark: `epsteinB 0 = 1/2` (the origin, halved) is never consumed — `lambdaVec b 0 = 0`
by definition and every `b (n / d)` in the recursion has n / d ≥ 1. Correct.

## E7 (gap of presentation, closed in the proof; no value changes) — the third clause of (E2) is not a `decide`
`∀ p, p.Prime → p ≠ 2 → p ≠ 3 → lambdaVec epsteinB 36 p = 0` quantifies over all p and is not decided in the kernel. It follows from
the lemma `¬ p ∣ n → lambdaVec b n p = 0` (strong induction: e_p(n) = 0 and every proper divisor of n is also prime to p) together with
"a prime dividing 36 = 2²·3² is 2 or 3". The brief's "kernel `decide` over ℚ" describes the first two clauses only. Same for the
non-dividing primes of (E1) (p = 5), (D1) (p = 2) and (D2) (p = 5, 7, 11) — see E13.

## E8 (typing note; no error) — `LambdaReal` needs the coefficients in ℝ
The brief writes `LambdaReal b n := Σ_{p prime, p ≤ n} lambdaVec b n p · Real.log p` for b : ℕ → R generic; a product with `Real.log p`
needs values in ℝ. Formalized as `LambdaReal (b : ℕ → ℝ) (n : ℕ)`; the Epstein statements read `LambdaReal (fun n => (epsteinB n : ℝ))`,
with the commutation lemma `lambdaVec (fun n => (b n : ℝ)) n p = ((lambdaVec b n p : ℚ) : ℝ)` proved in the solution (induction on the
fuel; `lambdaVec` is built from ring operations). The DH array is real already. Not an error in the mathematics.

## E9 (typing note; no error) — `padicValNat` reduces in the kernel
The brief takes e_p(n) := `padicValNat p n`. I expected this to be kernel-opaque (it is defined through `Nat.find`) and prepared a
fuel-structural replacement; measurement says otherwise: `padicValNat 2 36 = 2 ∧ padicValNat 3 36 = 2` by `decide +kernel` type-checks
in 0.6 ms, and the negative control `¬ (padicValNat 2 36 = 3)` is decided too (so the instance evaluates rather than degenerates). The
trusted definition therefore uses `padicValNat`, as the brief wrote. Recorded in `typing.log`.

## E10 (check, no error) — `kappa_pos`
κ = (√(10 − 2√5) − 2)/(√5 − 1). Numerator > 0 ⟺ 2 < √(10 − 2√5) ⟺ 4 < 10 − 2√5 ⟺ √5 < 3 ⟺ 5 < 9 (Mathlib at 51e6992e:
`Real.lt_sqrt : 0 ≤ x → (x < √y ↔ x ^ 2 < y)`, `Real.sqrt_lt' : 0 < y → (√x < y ↔ x < y ^ 2)` — both `#check`ed). Denominator > 0 ⟺
1 < √5 ⟺ 1 < 5. Numerically κ = (2.351141 − 2)/1.236068 = 0.284079 (record 0.28407904384…). Correct.

## E11 (cost note; no error) — the ten-minute line is not approached
The brief projected that the n = 36 `decide` might need the 10(j) split into nine box-count lemmas. Measured kernel type-checking
times (single theorem per file, `set_option profiler true`, `decide +kernel`): `epsteinB 6 = 2` 19 ms; `epsteinB 36 = 3` 0.77 s;
`lambdaVec epsteinB 6 2 = 2 ∧ lambdaVec epsteinB 6 3 = 2` 77 ms; `lambdaVec epsteinB 36 2 = -4` 3.62 s; `lambdaVec epsteinB 36 3 = -4`
3.55 s. No split; stop line (i) does not fire. (The fuel recursion re-evaluates shared divisors along different chains; at n = 36 this
costs a few seconds, not minutes.)

## E12 (check, no error) — the optional (D3) values
Λ_DH(4) = −(2 + κ²) log 2 < 0 and Λ_DH(6) = (1 + κ²) log 6 > 0 (E3; κ² ≥ 0 and log 2, log 3 > 0). Shipped, as the budget allowed.

## E13 (gap of presentation, closed in the proof; no value changes) — the word "hence"
(E1) says the two coefficients at p = 2, 3 give "hence `LambdaReal epsteinB 6 = 2·Real.log 2 + 2·Real.log 3`". `LambdaReal` sums over
the primes p ≤ 6, which include 5; the step needs `lambdaVec epsteinB 6 5 = 0`, which holds because 5 ∤ 6 (E7's lemma). Likewise (D1)
needs the p = 2 coefficient at n = 3 to vanish (2 ∤ 3), and (D2) the p = 5, 7, 11 coefficients at n = 12. In Lean each such sum is
reduced to its two (or one) surviving terms with `Finset.sum_eq_add_of_mem` (or `Finset.sum_eq_single`) and the lemma.
