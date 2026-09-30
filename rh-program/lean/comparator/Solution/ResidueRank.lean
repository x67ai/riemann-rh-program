/-
Copyright (c) 2026 Kunal Tyagi. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
SPDX-License-Identifier: Apache-2.0

This file is an addition to the Zeta23 library and is not part of it. Zeta23 is
Copyright 2026 Anthropic, PBC, released under the Apache License 2.0, and its
canonical home is https://github.com/anthropics/zeta-23-lean. This file contains
no code from that library and imports nothing from it: its imports are this unit's modules
Zeta23/ResidueRank/Pair.lean and Zeta23/ResidueRank/GenusBound.lean, which import only Mathlib (and LogPrimes.lean).
-/
/-
comparator/Solution/ResidueRank.lean — the UNTRUSTED comparator solution module for the topic `ResidueRank` (Theorem R's arithmetic
core; unit brief rh-program/results/theoremR-lean-s36/UNIT-BRIEF.md): the eight statements of Challenge/ResidueRank.lean,
byte-identical, PROVED by delegating to Zeta23/ResidueRank/LogPrimes.lean (items 1–3), Zeta23/ResidueRank/Pair.lean (4–6) and
Zeta23/ResidueRank/GenusBound.lean (7–8).  The statements mention Mathlib's vocabulary only, so each proof is the program theorem
of the same name applied to the same arguments; every displayed hypothesis is passed on (the program side does not use item 3's
positivity nor item 6's κ > 0 — PREDERIVATION-ERRATA E1, E4).  This module never imports the challenge.  Nothing in this file is
part of the trusted base: comparator re-checks that each theorem below has exactly the statement of its Challenge namesake and uses
only the permitted axioms.
-/
import Zeta23.ResidueRank.Pair
import Zeta23.ResidueRank.GenusBound

namespace ResidueRank

/-- (1) H3.3(b): the logarithms of the rational primes are linearly independent over ℚ. -/
theorem log_primes_linearIndependent :
    LinearIndependent ℚ (fun p : Nat.Primes => Real.log ((p : ℕ) : ℝ)) :=
  Zeta23.ResidueRank.log_primes_linearIndependent

/-- (2) Theorem R, arithmetic core: if every prime `p` divides a positive integer `N p`, the ℚ-span of the
real numbers `log (N p)` is not finitely generated. -/
theorem span_log_not_finite (N : Nat.Primes → ℕ) (hpos : ∀ p, 0 < N p)
    (hdvd : ∀ p : Nat.Primes, (p : ℕ) ∣ N p) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun p : Nat.Primes => Real.log ((N p : ℕ) : ℝ))) :=
  Zeta23.ResidueRank.span_log_not_finite N hpos hdvd

/-- (3) The converse bound: logarithms of positive integers whose prime factors lie in a finite set `S`
span a ℚ-space of dimension at most `#S`. -/
theorem rank_span_log_le {ι : Type} (S : Finset ℕ) (N : ι → ℕ) (hpos : ∀ i, 0 < N i)
    (hsupp : ∀ i p, p.Prime → p ∣ N i → p ∈ S) :
    Module.rank ℚ (Submodule.span ℚ (Set.range fun i => Real.log ((N i : ℕ) : ℝ)))
      ≤ (S.card : Cardinal) :=
  Zeta23.ResidueRank.rank_span_log_le S N hpos hsupp

/-- (4) Lemma F(a): under A9's real-valued fiber sums, each fiber holds finitely many prime powers. -/
theorem lemmaF_finite_fiber {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n)))
    (n : ℕ) (hn : 2 ≤ n) :
    {m : ℕ | IsPrimePow m ∧ cls m = cls n}.Finite :=
  Zeta23.ResidueRank.lemmaF_finite_fiber cls v κ hA9 n hn

/-- (5) Lemma F(b): if the class map is multiplicative into a monoid, every prime has infinite order. -/
theorem lemmaF_infinite_order {E : Type} [Monoid E] (φ : ℕ → E)
    (hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b) (v : E → ℝ) (κ : ℝ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ φ m = φ n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (φ n)))
    (p : ℕ) (hp : p.Prime) (a k : ℕ) (ha : 1 ≤ a) (hk : 1 ≤ k) :
    φ (p ^ a) ≠ φ (p ^ (a + k)) :=
  Zeta23.ResidueRank.lemmaF_infinite_order φ hmul v κ hA9 p hp a k ha hk

/-- (6) Theorem R on the abstract pair: A5 (the weights are von Mangoldt's Λ) and A9 (every fiber sum is
`κ` times a real number `v`, one fixed `κ > 0`) force the ℚ-span of the diagonal row to be
infinite-dimensional. -/
theorem theoremR {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ) (hκ : 0 < κ)
    (hA9 : ∀ n : ℕ, 2 ≤ n →
      HasSum (fun m : {m : ℕ // 2 ≤ m ∧ cls m = cls n} => ArithmeticFunction.vonMangoldt (m : ℕ))
        (κ * v (cls n))) :
    ¬ Module.Finite ℚ
      (Submodule.span ℚ (Set.range fun n : {n : ℕ // 2 ≤ n} => v (cls (n : ℕ)))) :=
  Zeta23.ResidueRank.theoremR cls v κ hκ hA9

/-- (7) The real-algebra core of Theorem S: the two Castelnuovo–Severi inequalities at `p` and `p²`
bound `L = log p / κ` in terms of `g` alone. -/
theorem theoremS_bound (g x L : ℝ) (hg : 0 ≤ g)
    (h1 : (1 + x - L) ^ 2 ≤ 4 * g ^ 2 * x)
    (h2 : (1 + x ^ 2 - L) ^ 2 ≤ 4 * g ^ 2 * x ^ 2) :
    L ≤ (1 + 2 * g) * (1 + (1 + Real.sqrt (1 + 8 * g)) / 2) :=
  Zeta23.ResidueRank.theoremS_bound g x L hg h1 h2

/-- (8) Theorem S: no real `g ≥ 0` satisfies the two inequalities at every prime. -/
theorem theoremS (κ g : ℝ) (hκ : 0 < κ) (hg : 0 ≤ g) (d : ℕ → ℝ)
    (h1 : ∀ p : ℕ, p.Prime → (1 + d p - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p)
    (h2 : ∀ p : ℕ, p.Prime →
      (1 + d p ^ 2 - Real.log (p : ℝ) / κ) ^ 2 ≤ 4 * g ^ 2 * d p ^ 2) : False :=
  Zeta23.ResidueRank.theoremS κ g hκ hg d h1 h2

end ResidueRank
