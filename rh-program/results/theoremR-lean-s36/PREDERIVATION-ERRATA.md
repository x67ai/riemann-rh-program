# THEOREM R in Lean — PREDERIVATION-ERRATA (builder Opus 5.5, Session 36, 2026-09-30; deliverable 1 of UNIT-BRIEF §2)

Brief `results/theoremR-lean-s36/UNIT-BRIEF.md` (SHA-256 `60b131b3…`), probe `typing-probe.lean` (SHA-256 `881e024a…`). Read against
`results/beta-shapes-s35/NOTE.md` §1.1, §2.0 (Lemma F), §2.3 (Theorem R, the converse paragraph, T3) and `read-O.md` §2.5. Numbers:
`tools/errata_numbers.py` → `tools/errata_numbers.log` (sympy for the exact identities, a seeded random search, 1.2 s). Nothing about ζ's
zeros or RH follows from anything below.

**Verdict.** All eight statements are TRUE as printed and are faithful renderings of what the NOTE proves (with the abstractions listed in
§1, none of which adds a hypothesis). **Stop line (i) does not fire.** One erratum against the brief's SKETCHES (E1: the parenthetical
"for κ ≤ 0 the hypothesis is contradictory at n = 2" is wrong for κ < 0), none against its STATEMENTS. Five displayed hypotheses are
logically removable (E2–E5 and item 6's `hκ`); every one is kept as displayed (the probe's text is shipped verbatim), and FIDELITY records
which proofs use them. The algebra of item 7 is right at every step, the boundary g = 0 and the region x < 0 included, and its bound is
attained (E7).

## §1 Statement by statement

**(1) `log_primes_linearIndependent`.** True (NOTE H3.3(b)). No hypotheses. Mathlib at 51e6992e does not carry it under any name: a grep of
`Mathlib/` for files mentioning both `LinearIndependent`/`linearIndependent`/`LinearIndepOn` and `Real.log`/`log p`/`Nat.Primes` returns only
`NumberField/Units/Regulator.lean` and `NumberField/CanonicalEmbedding/NormLeOne.lean` (units of number fields — unrelated); the brief's
"delegate if Mathlib has it" clause therefore does not apply. Route chosen (E11): ℚ-independence ⟸ ℤ-independence by Mathlib's
`LinearIndependent.iff_fractionRing ℤ ℚ` (the clearing of denominators, done once in Mathlib); for an integer relation Σ_{p∈s} m_p log p = 0
put x := Π_{p∈s} p^{m_p} ∈ ℚ (integer exponents, `zpow`), then log x = 0, so x = 1, and the q-adic valuation gives m_q = v_q(x) = v_q(1) = 0
(`padicValRat.zpow`, `padicValRat.self`, `padicValNat_primes`) — the NOTE's "unique factorization" in the form of `padicValRat`.

**(2) `span_log_not_finite`.** True. Both hypotheses are needed: without `hpos`, N ≡ 0 gives Real.log 0 = 0 (Mathlib's convention) at every p
and the span {0} is finite; without `hdvd`, N ≡ 1 gives the same. The brief's sketch (finitely many generators have a finite union of prime
supports; every prime lies in the support of its own N p; Euclid) is right; the Lean route uses item 1 through the coordinate map
`LinearIndependent.repr` on span{log p} (the coordinate at a prime q outside the finite union vanishes on the span and equals v_q(N q) ≥ 1 on
log N q).

**(3) `rank_span_log_le`.** True; it does not need item 1 (an upper bound only needs log N_i ∈ span{log p : p ∈ S}). `hpos` is removable (E4).
Faithful to the reader's converse "dim_Q G ≤ |char(B)|" (read-O §2.5 "Converse (reader)") in its arithmetic form: the κ⁻¹-scaling from
log N_D to (Δ · D)_Y is not part of the statement (it preserves rank for κ ≠ 0; not stated in Lean).

**(4) `lemmaF_finite_fiber`.** True. **It does not need `2 ≤ n` (E2).** Faithful to the finiteness clause of Lemma F(a); the second clause
L(D) = log N_D is not a challenge statement (it is proved on the program side as a helper of item 6). Lemma F(c) is not stated.

**(5) `lemmaF_infinite_order`.** True. `hk : 1 ≤ k`, `hp`, `hmul`, `hA9` are needed; `ha : 1 ≤ a` is removable (E3). Faithful to Lemma F(b):
by `hmul`, φ(p^a) = φ(p)^a for a ≥ 1, so the statement says the powers φ_p, φ_p², … are pairwise distinct; the Lean form is phrased on
φ(p^a) and needs neither φ(p^a) = φ(p)^a nor φ(1) = 1 (A7's φ_1 = id is not used — weaker there; but `hmul` ranges over all a, b : ℕ, the index 0 included, which the NOTE's φ on ℕ≥1 does not supply — stronger there; the statement implies the NOTE's Lemma F(b) through `WithZero E`, CHECK-O §7(5)).

**(6) `theoremR`.** True, and a faithful rendering of NOTE T3 = Theorem R at B = Spec Z (char(Spec Z) = all primes, Euclid inside). The
abstractions, none of which adds a hypothesis: (a) c on components is an arbitrary map `cls : ℕ → ι` (A7's graph structure is dropped —
the NOTE's converse paragraph: "The proof reads only the fibers of c on components: A7's graph structure is not used"); (b) the diagonal row of
A11's real pairing is an arbitrary `v : ι → ℝ`; (c) A5 is built in — the weights are `ArithmeticFunction.vonMangoldt`; (d) A9 is the `HasSum`
over the fiber {m ≥ 2 : cls m = cls n} for every n ≥ 2 (NOTE §1.1: "L(D) := Σ_{n ≥ 2 : φ_n = ψ} Λ(n)", "A9 reads: L(D) = κ (Δ · D)_Y for
every D = c(Γ_n), n ≥ 2"; Γ_1 is excluded, the index 0 has no meaning and is excluded; `HasSum` is unconditional summation, which for
nonnegative terms is ordinary convergence in any order); (e) ONE κ, as H3.2 and read-O's one-κ sentence require; (f) the conclusion
`¬ Module.Finite ℚ (span ℚ {v (cls n) : n ≥ 2})` is dim_Q G = ∞ with G the NOTE's diagonal-row span. The general-base Theorem R (any B of A2's
class, conclusion "char(B) finite") is NOT stated — it would need Λ_B and residue fields. `hκ : 0 < κ` is unused by the proof (E1).
Non-vacuity: the hypotheses are met by cls = id, v(n) = Λ(n)/κ for any κ ≠ 0 (the fiber of n is {n}; `[N2]`).

**(7) `theoremS_bound`.** True, the boundary included (E7). `hg` is needed: at g = −1, 1 + 8g < 0 and Mathlib's `Real.sqrt` of a negative
number is 0, so the bound is (1 − 2)(1 + 1/2) = −3/2, while x = 1, L = 1 satisfy h1 ((1)² ≤ 4) and h2 ((1)² ≤ 4) — a counterexample without
`hg`.

**(8) `theoremS`.** True. `hκ` is needed in the form κ ≠ 0: at κ = 0 Lean's `Real.log p / 0 = 0`, and d ≡ 1, g = 1 satisfy h1 ((2)² ≤ 4)
and h2 ((2)² ≤ 4) at every prime, so the conclusion `False` fails. (For κ < 0 the hypotheses are also contradictory at every large prime — by h1 alone when g > 0; when g = 0, h1 is met by d p = log p/κ − 1 and it is h2 that fails — not needed.) `hg` is removable (E5). First violating primes for a few (κ, g): `[N3]` (κ = 1, g = 1: bound 9, first prime 8111).

## §2 ERRATA against the brief's sketches and hints (none against a statement)

* **E1 (item 6's parenthetical — an ERROR in the sketch).** "for κ ≤ 0 the hypothesis is contradictory at n = 2" holds for κ = 0 only: the
  nonnegative sum at n = 2 contains Λ(2) = log 2 > 0 and would equal 0. For κ < 0 the hypotheses are SATISFIABLE — cls = id, v(n) = Λ(n)/κ
  (`[N2]`) — and the conclusion still holds. The proof needs no hypothesis on κ at all, not even κ ≠ 0: the ℚ-linear map x ↦ κx carries
  span_ℚ{v(cls p) : p prime} onto span_ℚ{log N_p}, so if the diagonal-row span were finite-dimensional the log-span would be too, against
  item 2 (at κ = 0 the contradiction arrives the same way). So `hκ` is kept as displayed (it is the SPEC's κ > 0) and is UNUSED; FIDELITY
  says so. The statement is unaffected.
* **E2 (item 4 — the brief's question "does statement 4 need `2 ≤ n`?": NO).** If n < 2, the set {m | IsPrimePow m ∧ cls m = cls n} is
  either empty or contains some m₀, and then m₀ ≥ 2 (`IsPrimePow.two_le`) and cls m₀ = cls n, so the set equals the fiber of m₀, to which `hA9`
  applies. `hn` is removable; kept as displayed.
* **E3 (item 5).** `ha : 1 ≤ a` is removable: if φ(1) = φ(p^k), then φ(p^k) = φ(1 · p^k) = φ(1)φ(p^k) = φ(p^k)φ(p^k) = φ(p^{2k}), which is
  the case a = k of the statement. Only k ≥ 1 is essential (k = 0 is φ(p^a) = φ(p^a)).
* **E4 (item 3).** `hpos` is removable: if N i = 0, every prime divides N i and `hsupp` would put every prime into the finite set S, against
  the infinitude of primes.
* **E5 (item 8).** `hg` is removable: h1 and h2 see g only through g², and item 7 at |g| gives the contradiction the same way.
* **E6 (brief §0 item 7, "verified numerically in pre_check.py [P1]").** [P1] samples x ≥ 0 only; the region x < 0 and the boundary g = 0 are
  covered here: x < 0 is infeasible (for g > 0, h1 has a negative right side; for g = 0, h1 and h2 force x = x², so x ∈ {0, 1}), and the
  random search of `[N1]` (400 000 draws, x ∈ [−5, 3r² + 2]) finds 143 489 feasible triples, none with x < 0, none above the bound.
* **E7 (item 7 — precision, no error).** Every step of the orchestrator's derivation re-derived: for g > 0, h1 gives x ≥ 0 and
  |1 + x − L| ≤ 2g√x; h2 gives |1 + x² − L| ≤ 2gx; so x² − x ≤ 2gx + 2g√x, i.e. with s = √x, s(s + 1)(s² − s − 2g) ≤ 0 (the factorization is
  `[N1]`'s sympy line); for s > 0 this is s² − s − 2g ≤ 0, i.e. s ≤ r := (1 + √(1 + 8g))/2 (the positive root; r² = r + 2g, `[N1]`); at s = 0 the
  bound is L ≤ 1. Then L ≤ 1 + s² + 2gs ≤ 1 + r² + 2gr = (1 + 2g)(1 + r). For g = 0: L = 1 + x = 1 + x², x ∈ {0, 1}, L ≤ 2 = the bound at
  g = 0. **The bound is attained** for every g ≥ 0, at x = r², L = 1 + r² + 2gr: both h1 and h2 hold with EQUALITY there (`[N1]`, exact), so
  [P1]'s "sup" is a maximum and the constant cannot be lowered.
* **E8 (hint names).** At 51e6992e: `ArithmeticFunction.vonMangoldt_apply` (Λ n = if IsPrimePow n then Real.log (minFac n) else 0),
  `vonMangoldt_nonneg`, `vonMangoldt_apply_pow`, `vonMangoldt_apply_prime` exist as named (`NumberTheory/ArithmeticFunction/VonMangoldt.lean`
  lines 73, 80, 86, 89); the proof also uses `vonMangoldt_eq_zero_iff` (line 99). `HasSum` takes a `SummationFilter` argument at this pin
  (the probe's `HasSum f a` is the default, unconditional one). `Nat.infinite_setOf_prime` is deprecated (2026-07-09) in favor of
  `Nat.infinite_setOfPred_prime`; the instance `Nat.Primes.infinite` is what the proofs use. `Infinite.exists_not_mem_finset` is
  `Infinite.exists_notMem_finset` at this pin.
* **E9 (the ChallengeDeps question, brief §0).** The Comparator layout does not want a `ChallengeDeps/ResidueRank.lean`: the statements use
  Mathlib's vocabulary only, the comparator needs a challenge module and a solution module and nothing else, and the probe itself imports
  Mathlib. `Challenge/ResidueRank.lean` therefore imports Mathlib directly (the probe's own import line) and no ChallengeDeps module is
  written. (Every earlier topic had one because it needed trusted definitions.)
* **E10 (the unused-variable linter).** At this pin the linter fires on an unused hypothesis in a theorem signature (checked by a scratch
  probe). The challenge and solution carry the displayed names (`hκ` etc.) and the solution passes every hypothesis to the program side, so
  neither warns; the program-side theorem whose proof does not use a displayed hypothesis names it with a leading underscore (`_hκ`) — a
  binder name in the program module only; the comparator compares the challenge against the solution, whose binders are the displayed ones.

## §3 Plan (rung order of 10(l))

1. `Zeta23/ResidueRank/LogPrimes.lean` (items 1–3): the exponent vector `expVec n : Nat.Primes →₀ ℚ` (n's factorization on the primes), its
   linear combination against log p equal to log n for n ≠ 0 (induction on primes), item 1 by the route of §1(1), item 2 by `repr`, item 3 by
   `rank_span_finset_le` + `Submodule.rank_mono`. Built alone; `rung1-print-axioms.log`.
2. `Zeta23/ResidueRank/Pair.lean` (items 4–6): item 4 by `Summable.tendsto_cofinite_zero` (finitely many terms ≥ log 2); item 5 by the
   infinite injective family j ↦ p^{a+jk} in one fiber; item 6 by N_p := Π_{m ∈ fiber, prime power} minFac m, the helper
   κ · v(cls p) = log N_p (the HasSum collapses to a finite sum), then item 2 through the ℚ-linear map x ↦ κx.
3. `Zeta23/ResidueRank/GenusBound.lean` (items 7–8): item 7 on E7's route (`nlinarith` with the hint terms), item 8 from item 7 and
   `Nat.exists_infinite_primes` at a prime above exp(κ · bound).
4. The topic, the checks, the comparator run with nanoda; then BUILD-NOTES, FIDELITY, the yaml rows, the README section, hashes.

## §4 Addendum after the build (Wed Sep 30 17:35:08 IST 2026) — the removable hypotheses, kernel-checked on the program side

Every "removable" claim of §2 is now a Lean theorem on the program side (NOT a statement of the Comparator topic, which ships the
probe's eight statements verbatim): E1 — `Zeta23.ResidueRank.theoremR_of_A9` (Theorem R with no hypothesis on κ; `theoremR` is its
corollary with the binder `_hκ`); E2 — `lemmaF_finite_fiber_all` (no `2 ≤ n`); E3 — `lemmaF_infinite_order_all` (no `1 ≤ a`);
E4 — `rank_span_log_le_of_supp` (no positivity; an N i = 0 contributes Real.log 0 = 0 — shorter than the §2 argument, which stays
true); E5 — `theoremS_abs` (no `0 ≤ g`). All with the three standard axioms (`program-axioms.log`). The necessity claims of §1
(item 2's `hpos`/`hdvd`, item 7's `hg`, item 8's `hκ`) are hand counterexamples, not Lean statements.
