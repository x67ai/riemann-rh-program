# THEOREM R in Lean — FIDELITY ledger for the Comparator topic `ResidueRank` (Theorem R's arithmetic core, Lemma F, Theorem R on the abstract pair, and two scoped real-algebra statements); builder Opus 5.5, Session 36, 2026-09-30

Mirrored in `lean/formalization.yaml` (`fidelity.divergences`, row (aa)). Brief: `results/theoremR-lean-s36/UNIT-BRIEF.md` §2 item 5. The
record the statements are read against: `results/beta-shapes-s35/NOTE.md` §1.1 (conventions: "L(D) := Σ_{n ≥ 2 : φ_n = ψ} Λ(n)"; "A9 reads:
L(D) = κ (Δ · D)_Y for every D = c(Γ_n), n ≥ 2"; "G := the Q-linear span in R of the set {(Δ · c(Γ_n))_Y : n ≥ 2}"), §2.0 (Lemma F: "(a) for
every D in the image of c, the fiber F_D := {p^k : k ≥ 1, φ_{p^k} = ψ_D} is finite, and L(D) = log N_D with N_D = Π_{p^k ∈ F_D} p a positive
integer; (b) for every prime p the powers φ_p, φ_p², φ_p³, … are pairwise distinct"), §2.3 (H3.3(b): "{log ℓ : ℓ prime} is Q-linearly
independent"; Theorem R: "Under H3.1, H3.2 and H3.3(b) — for any base B in A2's class — if dim_Q G < ∞ then char(B) is finite"; T3's proof:
"For B = Spec Z, char(B) is the set of all primes, infinite by H3.3(a); Theorem R gives dim_Q G = ∞"), and `read-O.md` §2.5 (the reader's
converse: "supp(log N_D) ⊆ char(B) for every D …, so dim_Q G ≤ |char(B)|").

**First paragraph, binding (10(c)).** Nothing about ζ's zeros or RH follows from anything below. Theorem R is RH-blind (NOTE §2.3 DH CHECK:
"T3 is a SHAPE theorem, RH-blind; it is not a falsification channel for RH"); the eight statements are about the logarithms of integers, the
von Mangoldt function, ℚ-spans in ℝ, a map into a monoid, and real inequalities — no zeta function, no zero, no explicit formula appears in any
statement. The label the unit earns (UNIT-BRIEF §1(3); every statement landed with no displayed hypothesis beyond its own binders), verbatim:
"Theorem R's arithmetic core Comparator-checked: the logarithms of the primes are ℚ-linearly independent, a family of positive integers N_p
with p | N_p has logarithms spanning an infinite-dimensional ℚ-space, the converse rank bound, Lemma F, and Theorem R on the abstract pair
(von Mangoldt weights, real fiber sums, one κ) — over Mathlib alone, no displayed hypothesis, the three standard axioms, replayed by nanoda".
Items 7–8 are in the topic and are not named by the label (UNIT-BRIEF §0: they are SCOPED; §4 below).

## 1. What IS covered — each claim is a theorem in `lean/comparator/Challenge/ResidueRank.lean` (namespace `ResidueRank`; proved in `Solution/ResidueRank.lean` by delegation to `Zeta23/ResidueRank/{LogPrimes,Pair,GenusBound}.lean`)

| record's claim | theorem | exact content |
|---|---|---|
| NOTE H3.3(b): {log ℓ : ℓ prime} is ℚ-linearly independent (unique factorization) | `log_primes_linearIndependent` | `LinearIndependent ℚ (fun p : Nat.Primes => Real.log ((p : ℕ) : ℝ))` — ℝ as a ℚ-module; no hypothesis |
| Theorem R's arithmetic core (NOTE §2.3 proof: finitely many generators have a finite union S of prime supports; every prime ℓ divides its own N; "Therefore char(B) ⊆ S, which is finite") | `span_log_not_finite` | ∀ N : Nat.Primes → ℕ, (∀ p, 0 < N p) → (∀ p, (p : ℕ) ∣ N p) → ¬ Module.Finite ℚ (span ℚ (range fun p => Real.log (N p))) |
| the reader's converse, "dim_Q G ≤ \|char(B)\|" (read-O §2.5), in its arithmetic form | `rank_span_log_le` | ∀ {ι : Type} (S : Finset ℕ) (N : ι → ℕ), (∀ i, 0 < N i) → (∀ i p, p.Prime → p ∣ N i → p ∈ S) → Module.rank ℚ (span ℚ (range fun i => Real.log (N i))) ≤ #S (as a cardinal) |
| Lemma F(a), finiteness clause | `lemmaF_finite_fiber` | ∀ {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ), hA9 → ∀ n, 2 ≤ n → {m : ℕ \| IsPrimePow m ∧ cls m = cls n}.Finite, where hA9 := ∀ n ≥ 2, `HasSum` (m ↦ Λ(m) over the subtype {m : ℕ // 2 ≤ m ∧ cls m = cls n}) (κ · v (cls n)) |
| Lemma F(b): the powers φ_p, φ_p², … are pairwise distinct | `lemmaF_infinite_order` | ∀ {E : Type} [Monoid E] (φ : ℕ → E), (∀ a b, φ (a·b) = φ a · φ b) → ∀ (v : E → ℝ) (κ : ℝ), hA9 (with cls := φ) → ∀ p, p.Prime → ∀ a k, 1 ≤ a → 1 ≤ k → φ (p^a) ≠ φ (p^(a+k)) |
| NOTE T3 = Theorem R at B = Spec Z: dim_Q G = ∞ | `theoremR` | ∀ {ι : Type} (cls : ℕ → ι) (v : ι → ℝ) (κ : ℝ), 0 < κ → hA9 → ¬ Module.Finite ℚ (span ℚ (range fun n : {n : ℕ // 2 ≤ n} => v (cls n))) |
| (scoped) the real-algebra core of the Session-36 Theorem S | `theoremS_bound` | ∀ g x L : ℝ, 0 ≤ g → (1 + x − L)² ≤ 4g²x → (1 + x² − L)² ≤ 4g²x² → L ≤ (1 + 2g)(1 + (1 + √(1 + 8g))/2) |
| (scoped) no g ≥ 0 at every prime | `theoremS` | ∀ κ g : ℝ, 0 < κ → 0 ≤ g → ∀ d : ℕ → ℝ, (∀ p prime, (1 + d p − log p/κ)² ≤ 4g² d p) → (∀ p prime, (1 + (d p)² − log p/κ)² ≤ 4g² (d p)²) → False |

All eight: no displayed hypothesis beyond the statements' own binders — exactly the list printed in UNIT-BRIEF §0 (stop line (iii) did not
fire); axioms `[propext, Classical.choice, Quot.sound]` for each (`print-axioms.log`) and for all 27 program-side declarations
(`program-axioms.log`; rung 1 alone `rung1-print-axioms.log`); statement identity challenge/solution 8/8 on the build tree and on
`rh-program/lean`, challenge/probe 8/8, whole text from `import Mathlib` identical to the probe, config order PASS (`statement-identity.log`);
the Comparator run with nanoda PASS, exit 0 (`comparator-run.log`).

**Which displayed hypotheses the proofs use.** Unused: item 3's `hpos` (the program theorem `rank_span_log_le` names it `_hpos` and is the
corollary of `rank_span_log_le_of_supp`, which has no positivity — an N i = 0 contributes Real.log 0 = 0); item 6's `hκ : 0 < κ` (**the
brief's question: the proof does NOT use it** — `theoremR` is the corollary, binder `_hκ`, of `theoremR_of_A9`, which has no hypothesis on κ:
the ℚ-linear map x ↦ κx carries the diagonal-row span onto a space containing span{log N_p}, so finiteness would pass to span{log N_p},
against item 2; for κ = 0 the hypotheses are contradictory at n = 2, for κ < 0 they are satisfiable and the conclusion holds —
PREDERIVATION-ERRATA E1). Used but removable (kernel-checked on the program side): item 4's `2 ≤ n` (`lemmaF_finite_fiber_all`, E2), item 5's
`1 ≤ a` (`lemmaF_infinite_order_all`, E3), item 8's `0 ≤ g` (`theoremS_abs`, E5). Used and necessary (hand counterexamples, errata §1):
item 2's `hpos` and `hdvd`, item 7's `hg`, item 8's `hκ` (in the form κ ≠ 0). The Solution passes every displayed hypothesis to the program
side, so no binder of the eight trusted statements is unused there.

## 2. What is NOT covered — stated nowhere in Lean

* **The SPEC's geometric axioms A6–A8** (the base β and the factorization Sp_B → Sp_{F₁} → Sp_β, dimension two, the canonical class,
  adjunction), **A7's graph structure** (c(Γ_n) = Γ_{φ_n} as graphs in B ×_β B; the topic sees only the map on components), **A10, A11 beyond a
  real diagonal row, A13**: none appears. The staged zoo entry built on the NOTE is therefore not, as a whole, a Lean statement: the topic is
  its arithmetic core and its abstract-pair theorem, nothing more.
* **The existence or non-existence of a target Y** — no statement quantifies over targets, surfaces, pairings or intersection numbers; `v` is
  an arbitrary real function on an arbitrary type of classes.
* **The general-base Theorem R** ("for any base B in A2's class … char(B) is finite"): not stated; Λ_B, closed points, residue fields and
  char(B) do not appear. `theoremR` is the B = Spec Z instance (T3), with Euclid inside the proof (`Infinite Nat.Primes`).
* **Lemma F(a)'s second clause** (L(D) = log N_D) is proved on the program side (`Zeta23.ResidueRank.fiber_sum_eq_log`, κ·v(cls n) =
  log Π minFac over the fiber's prime powers) and used by `theoremR`, but it is not a statement of the topic; **Lemma F(c)** is not stated.
* **The κ-scaling of the converse** (dim_Q G = dim_Q span{log N_D} for κ ≠ 0) and the converse on the pair: item 3 is the arithmetic bound only.
* **The rung-1 side** (the curve pair over F_q, where char(S) = {ℓ} and Theorem R is silent): not stated.
* **The geometric reading of items 7–8** (Castelnuovo–Severi at p and p², a finite self-intersection of the diagonal, the Session-36
  Theorem S of `results/d4-infty-s36/`, under read): not claimed; the two statements are real algebra and the Solution proves them as such.
  The bound of item 7 is attained (errata E7: x = r², L = 1 + r² + 2gr, both inequalities with equality) — a sympy fact
  (`tools/errata_numbers.log` [N1]), not a Lean statement.
* **T1, T2, Proposition 2.2.1, Corollaries 3.1–3.2, routes (a)/(b) of §2.3.5, the (D1)–(D4) partition**: not stated.
* **ζ, its zeros, RH, the DH column**: nothing.

## 3. Where the formal statements differ from the prose (none adds a hypothesis)

* **(r1) The abstract pair.** `cls : ℕ → ι` stands for n ↦ c(Γ_n) (an arbitrary map; the NOTE's c comes from A6–A7); `v : ι → ℝ` for
  D ↦ (Δ · D)_Y (an arbitrary real function; the NOTE's is A11's pairing on the diagonal row). The NOTE's own remark covers the dropped
  structure: "The proof reads only the fibers of c on components: A7's graph structure is not used (it enters Lemma F(b)–(c), not Theorem R)".
* **(r2) Indexing.** ℕ includes 0; the fibers and the span run over m, n ≥ 2 (the NOTE's n ∈ ℕ_{≥1}, n ≠ 1: Γ_1 is the diagonal, excluded as
  the NOTE's fiber sum excludes it). The fiber of `cls n` is {m ≥ 2 : cls m = cls n}, the NOTE's {n ≥ 2 : c(Γ_n) = D} with D = cls n —
  including D = Δ when some n ≥ 2 has c(Γ_n) = Δ, as the NOTE requires ("D = c(Γ_1) = Δ included when some c(Γ_n), n ≠ 1, equals it").
* **(r3) A5 built in.** The weight of Γ_1 ∩ Γ_m is `ArithmeticFunction.vonMangoldt m` (Mathlib's Λ: log (minFac m) on prime powers, 0
  elsewhere); the NOTE's "deg(Γ_1 ∩ Γ_n) = Λ(n)".
* **(r4) A9 as `HasSum`.** Unconditional summation over the subtype (Mathlib's default `SummationFilter`); for the nonnegative Λ it is
  ordinary convergence in any order, which is what the NOTE's "L(D) = κ (Δ · D)_Y ∈ R" requires. ONE κ for all fibers — the NOTE's H3.2
  and read-O's sentence "Theorem R is exactly as strong as A9's one normalization".
* **(r5) κ.** Any real κ in `lemmaF_*` (no sign needed); `theoremR` displays the SPEC's κ > 0 and does not use it (§1).
* **(r6) Lemma F(b)'s form.** Stated on φ(p^a), a ≥ 1, with `hmul` for all a, b and without φ(1) = 1 (A7's φ_1 = id is not assumed — a
  weaker hypothesis at 1) — but `hmul` is demanded at the index 0 too (φ 0 = φ 0 · φ b = φ a · φ 0), where the NOTE's φ on ℕ≥1 is not defined and which a nontrivial φ into a group cannot meet; the statement still implies the NOTE's Lemma F(b) for every φ multiplicative on the positive integers, through `WithZero E` with 0 ↦ 0 (CHECK-O §7(5), kernel-checked in `check-O/lemmaF-b-positive.lean`); by `hmul`, φ(p^a) = φ(p)^a for a ≥ 1, so the statement is the NOTE's "pairwise distinct".
* **(r7) "Infinite-dimensional" as `¬ Module.Finite ℚ ↥(span …)`**; for a ℚ-vector space, finite = finitely generated = finite-dimensional
  (the probe's docstring for item 2 says "not finitely generated"; the same statement). The rank bound as `Module.rank ℚ ↥(span …) ≤ (S.card
  : Cardinal)`.
* **(r8) Mathlib's totalizations.** `Real.log 0 = 0` (item 2 needs `hpos` because of it; item 3 does not), `Real.sqrt` of a negative number
  is 0 (item 7's `hg` excludes it), `x / 0 = 0` (item 8's `hκ` excludes it).
* **(r9) Names.** `theoremR`, `theoremS_bound`, `theoremS`, `lemmaF_*`, … in namespace `ResidueRank` (the probe's); the program side in
  `Zeta23.ResidueRank`.
* **(r10) Program-side binders.** `rank_span_log_le` and `theoremR` name their unused displayed hypothesis `_hpos`, `_hκ` (the unused-variable
  linter fires at this pin); the trusted statements and the Solution carry the displayed names — a binder name in the program module only.
* **(r11) No trusted definition layer.** No ChallengeDeps module: every constant the statements mention is Mathlib's, so the comparator's
  constant-by-constant comparison is against Mathlib itself.

**Fidelity divergences in the brief's sense (a hypothesis beyond the statements' own): NONE.**

## 4. Items 7–8, scoped

`theoremS_bound` and `theoremS` are true on their face as statements about real numbers (PREDERIVATION-ERRATA §1 (7)–(8), E7: every step of
the orchestrator's derivation re-derived, the boundary g = 0 and the region x < 0 included). Their reading as "no finite self-intersection of
the diagonal" belongs to the Session-36 unit `results/d4-infty-s36/`, which is under read; this ledger, the challenge header, the yaml row and
the README section do not assert that reading, and the label above does not mention it.
