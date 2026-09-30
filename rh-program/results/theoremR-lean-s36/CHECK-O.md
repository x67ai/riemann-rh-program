# THEOREM R's ARITHMETIC CORE — CHECK-O, the Opus 5.5 clean-clone check of the Comparator topic `ResidueRank` (Session 36; UNIT-BRIEF §3; KICKSTART 10(f), 10(j))

Checker: Opus 5.5, started Wed Sep 30 17:47 IST 2026 (machine clock). Contract: `results/theoremR-lean-s36/UNIT-BRIEF.md` §3 (SHA-256
`60b131b3353f944b101bca54609cd07f591fad4c20618fab5387b6a03d42068e`, recomputed, equal to the value BUILD-NOTES quotes); typing probe
`typing-probe.lean` `881e024a9184e9e4aab0976e42a31f1d8f8f5f01b3cec10c773a00f236601a81` (equal to BUILD-NOTES'). Sources read for the
mathematics: `results/beta-shapes-s35/NOTE.md` §1.1, §2.0, §2.3 (SHA-256 `49eb8e12…`), `results/beta-shapes-s35/read-O.md` §2.2, §2.5
(`1614bcbb…`). Precedent for the procedure: `results/h4-pair-lean-s33/CHECK-O.md` and its `check-O/` scripts. The builder's tree
`~/rh-lean-work/checker-clone-s33-h4` was never used for a build or a run here. Every log below is under
`results/theoremR-lean-s36/check-O/`. Nothing committed; no Lean file, yaml, README or builder file edited.

(Verdict and the numbered findings: §11, written last.)

## 1. Clean clone, overlay, cache (`check-O/clone.sh`, `clone.log`, `overlay.sh`, `overlay.log`, `cache-get.log`)

`git clone https://github.com/anthropics/zeta-23-lean ~/rh-lean-work/checker-clone-s36-residue` (a NEW directory — the script refuses
an existing one; retry loop), `git checkout v1.0` → HEAD `3635e74826a4c1fcece7d1cd2b6fa75e43a00510` ("Merge pull request #3 from
anthropics/xiprime-pairceiling", the same commit as the Session-33 checker's v1.0); `lean-toolchain` `leanprover/lean4:v4.33.0-rc2`;
manifest Mathlib `rev` = `inputRev` = `51e6992efd06126df61a496bebf8f49482a4e129`. `lake exe cache get` (17:48–17:50 IST): "Decompressed
8489 already-cached file(s) … Completed successfully in 10489 ms"; the checked-out `.lake/packages/mathlib` HEAD is `51e6992e…`. Mathlib
was never compiled from source.

**Overlay — exactly the seven unit files, nothing else** (`overlay.sh`: `cp` then `cmp` against `rh-program/lean/`, each OK): the program
modules `Zeta23/ResidueRank/{LogPrimes,Pair,GenusBound}.lean` and the topic files `comparator/{Challenge,Solution,PrintAxioms}/ResidueRank.lean`,
`comparator/config-residue-rank.json`. None pre-existed in v1.0. `git status --short` after the overlay: five `??` entries (the new
directory `Zeta23/ResidueRank/` and the four topic files) and nothing modified. The import closure needs nothing more: `LogPrimes` and
`GenusBound` import `Mathlib` only, `Pair` imports `Zeta23.ResidueRank.LogPrimes`, the challenge `Mathlib`, the solution `Pair` +
`GenusBound`, the print-axioms file `Solution.ResidueRank`. The root `Zeta23.lean` was not touched (the unit adds no root import;
BUILD-NOTES §1 says why), so the modules are built by name.

## 2. Cold builds, one `lake` at a time (`check-O/build.sh`, `build-{logprimes,pair,genusbound,solution,challenge}.log`)

Each build started only after the previous `lake` exited (the script logs `pgrep -x lake` = 0 before each start).

| build (sequential) | result | module line | wall / max RSS |
|---|---|---|---|
| `lake build Zeta23.ResidueRank.LogPrimes` (17:50:40) | *Build completed successfully (8697 jobs)*, rc 0, 0 errors, 0 warnings | `Built Zeta23.ResidueRank.LogPrimes (6.3s)` | 9.36 s / 5.88 GB |
| `lake build Zeta23.ResidueRank.Pair` (17:51:04) | 8698 jobs, rc 0, 0 warnings | `Built Zeta23.ResidueRank.Pair (3.4s)` | 5.65 s / 5.87 GB |
| `lake build Zeta23.ResidueRank.GenusBound` (17:51:10) | 8697 jobs, rc 0, 0 warnings | `Built Zeta23.ResidueRank.GenusBound (7.7s)` | 9.95 s / 5.90 GB |
| `lake build Solution.ResidueRank` (17:51:25) | 8700 jobs, rc 0, 0 warnings | `Built Solution.ResidueRank (3.3s)` | 5.54 s / 5.85 GB |
| `lake build Challenge.ResidueRank` (17:51:31) | 8697 jobs, rc 0, **exactly 8 warnings, each "declaration uses `sorry`"**, at lines 51, 57, 65, 72, 81, 93, 103, 110 — the eight `theorem` lines | `Built Challenge.ResidueRank (3.3s)` | 5.64 s / 5.85 GB |

The job counts equal BUILD-NOTES §5's expectation (8697 / 8698 / 8697 / 8700). (The max RSS is Mathlib's oleans mapped by `lake`, as in
every prior record.) One procedural slip of this checker, repaired: the first call of `build.sh` passed a RELATIVE log path, so
`build-logprimes.log` was written into the clone's root; it was moved into `check-O/` at once (no other effect; `git status` of the clone
is otherwise the overlay's).

## 3. `#print axioms` for every name (`check-O/print-axioms.log`, `program-axioms-checker.lean`, `sorry-control.{lean,log}`)

* `lake env lean comparator/PrintAxioms/ResidueRank.lean` in the clean clone (17:51:59), rc 0 — the eight topic names:

| name | axioms |
|---|---|
| `ResidueRank.log_primes_linearIndependent` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.span_log_not_finite` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.rank_span_log_le` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.lemmaF_finite_fiber` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.lemmaF_infinite_order` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremR` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremS_bound` | `[propext, Classical.choice, Quot.sound]` |
| `ResidueRank.theoremS` | `[propext, Classical.choice, Quot.sound]` |

* The checker's own probe, GENERATED from every `def`/`theorem` line of the three program modules (27 names: `LogPrimes` 2 defs + 14
  theorems, `Pair` 8, `GenusBound` 3 — the same 27 the builder's `program-axioms.lean` lists, so the builder's "all 27 program-side
  declarations" is the whole of the three files): 27 lines, each `[propext, Classical.choice, Quot.sound]`, rc 0.
* `sorryAx`: 0 hits; `Lean.ofReduceBool` / `Lean.trustCompiler`: 0 hits.
* **Negative control** (`sorry-control.lean`): the same `#print axioms` on the CHALLENGE module prints `[propext, sorryAx,
  Classical.choice, Quot.sound]` for three of its names — the probe does detect a `sorry` when one is present.
* **Result: clean.** Every topic name and every program declaration uses exactly the three standard axioms.

## 4. Statement identity (`check-O/identity_checker.py`, `statement-identity.log`; `brief-elab-check2.{lean,log}`)

The checker's own script (extraction: the docstring above `theorem <name>` plus the text from `theorem <name>` to the first `:=`; the
builder's `tools/statement_identity_s36.py` was neither run nor read):
* [A] challenge = solution, byte for byte (docstring + statement), 8/8, in the clean clone AND in `rh-program/lean` (and the two copies
  of each file are `cmp`-identical, [F] 7/7).
* [B] challenge = typing probe `results/theoremR-lean-s36/typing-probe.lean`, byte for byte, 8/8.
* [C] the challenge from the LINE `import Mathlib` to EOF = the probe from its `import Mathlib` line to EOF: 3536 bytes, identical; the
  challenge and the probe each have exactly one import line, `import Mathlib`. (First run of the script: [C] FAILED because it located
  "import Mathlib" by substring and hit the phrase "From `import Mathlib` to the end" in the challenge's header comment — a bug of the
  checker's script, kept as `statement-identity-run1-buggy.log`; the line-anchored re-run passes.)
* [D] against UNIT-BRIEF §0: items 1, 2, 3, 7, 8 are printed in the brief as full backticked statements, and each equals the challenge
  statement after whitespace normalization, character for character. Items 4–6 are printed as prose with backticked fragments; every
  fragment occurs verbatim in the statement except `hA9 : ∀ n, 2 ≤ n → …` (challenge: `∀ n : ℕ, 2 ≤ n → …`) and item 5's `hmul : ∀ a
  b, φ (a * b) = …` (challenge: `∀ a b : ℕ, …`), plus the prose substitution "`cls := φ`". To settle whether those ascriptions change
  anything, `brief-elab-check2.lean` elaborates the brief's LITERAL fragments, assembled into theorem statements, and compares the
  resulting types with the challenge constants: `lemmaF_finite_fiber`, `lemmaF_infinite_order`, `theoremR` — alpha-equal `true`,
  `isDefEq` `true`, all three. (A first form, `brief-elab-check.lean`, elaborated them as `def … : Prop` and found item 6 unequal; the
  cause, located in `brief-elab-diff.log`, is that Lean's `def` elaborator abstracts the `CharZero ℝ` proof inside the `Module ℚ ℝ`
  instance into an auxiliary lemma `brief6._proof_1`, while a theorem statement keeps the proof term inline — an artifact of that probe,
  not of the statement.) So the brief's §0 text, the probe and the challenge denote the same eight terms.
* [E] config: `theorem_names` = `ResidueRank.` + the challenge's names in file order; `permitted_axioms` = `propext`, `Quot.sound`,
  `Classical.choice`; `enable_nanoda: true`; modules `Challenge.ResidueRank` / `Solution.ResidueRank`; no other key.
* RESULT: PASS.

## 5. Trust greps (`check-O/trust_greps_checker.py`, `trust-greps.log`)

The checker's own scan of the seven shipped files in the clean clone (word-bounded; each hit classified CODE or COMMENT with a
nesting-aware comment mask), 28 words — the brief's seven (`axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`, `opaque`,
`sorry`) plus `admit`, `ofReduceBool`, `decide`, `set_option`, `macro`, `elab`, `syntax`, `partial`, `attribute`, `instance`, `private`,
`noncomputable`, `Challenge`, `sorryAx`, `trustCompiler`, `run_cmd`, `run_meta`, `#eval` and others. Hits IN CODE: the 8 deliberate
challenge `sorry`s (lines 53, 61, 69, 78, 88, 99, 107, 114); the two `noncomputable def`s of `LogPrimes.lean` (`logP`, `expVec` —
`noncomputable` only withholds compiled code, it adds no axiom: both print the three standard axioms, §3); and the config's
`"challenge_module": "Challenge.ResidueRank"` field. Nothing else: no `axiom`, `native_decide`, `unsafe`, `implemented_by`, `extern`,
`opaque`, `decide`, `set_option`, attribute, macro or instance anywhere in code. The raw `grep -n -w` with comments INCLUDED: `axiom` 2
hits (both in the print-axioms file's header comment: "quick axiom audit", "no other axiom"), `sorry` 9 (the 8 plus the challenge
header's "The `sorry`s below are deliberate"), the other five words 0. Declaration keywords in code: `LogPrimes` 2 `def` + 14
`theorem`, `Pair` 8, `GenusBound` 3, challenge 8, solution 8, print-axioms none. **Imports: the solution imports
`Zeta23.ResidueRank.Pair` and `Zeta23.ResidueRank.GenusBound` only; no file imports `Challenge.*`; the program modules import `Mathlib`
and `LogPrimes` only.** Clean.

## 6. Comparator run with nanoda from the clean clone (`check-O/run-clone.sh`, `cleanup.sh`, `prerun-cleanup.log`, `comparator-run.log`)

Runner: the builder's `tools/run.sh` with exactly two lines changed (the comment line 2 and the `cd` target → the clean clone; the `diff`
is in this session's transcript and reproducible: `diff tools/run.sh check-O/run-clone.sh`). Pre-run cleanup (the builder's
`prerun-cleanup.sh`, same two-line adaptation) removed the 16 comparator-layer artifacts of `Challenge/ResidueRank` and
`Solution/ResidueRank` under `.lake/build/{lib/lean,ir}`, "remaining: 0" (the program modules stay built — the untrusted side either
way); there is no ChallengeDeps module for this topic. Heavy processes (> 50 % CPU) before the start: none.

| comparator output (17:56:19–17:56:57 IST) | nanoda | Lean kernel | exit | wall / max RSS |
|---|---|---|---|---|
| `Built Challenge.ResidueRank (5.3s)` (the 8 deliberate `sorry` warnings), export of the 8 names + the 29 fixed targets from both modules, `Built Solution.ResidueRank (3.3s)`, `Your solution is okay!` | `Running nanoda kernel on solution` / `Nanoda kernel accepts the solution` | `Running Lean default kernel on solution.` / `Lean default kernel accepts the solution` | **0** | 37.53 s / 5.85 GB |

Tool SHA-256s printed in the log — comparator `fe1222e25fc3…`, lean4export `de4ffedf1412…`, nanoda_bin `d6c87133b59c…`, fake-landrun
`167507c89d8b…` — each occurs once in `results/d1-m2a/packaging/COMPARATOR-RUN.md` §1. Toolchain in the log `v4.33.0-rc2` (commit
d8b18978), Mathlib `51e6992e…`. NOT sandboxed (the fake-landrun shim prints "THIS IS NOT REAL LANDRUN" for each of the five steps), as in
every prior macOS record (COMPARATOR-RUN.md §2); the solution file was read here in full (§5, §7) and imports nothing trusted-side.
What the run establishes: each solution theorem's statement coincides constant for constant with its challenge namesake (all constants
are Mathlib's), the proofs use no axiom outside the three, nanoda re-checked the solution export, and Lean's kernel replayed it.
**PASS, reproduced from the clean clone.**

## 7. The eight challenge statements read as mathematics (against NOTE §1.1, §2.0, §2.3 and read-O §2.2, §2.5)

Witness probes, kernel-checked in the clean clone (never shipped): `check-O/witnesses.lean` → `witnesses.log` (rc 0, no warning — so no
`sorry`), `check-O/lemmaF-b-positive.lean` → `lemmaF-b-positive.log` (`#print axioms`: the three standard axioms). Numbers:
`check-O/rederive.py` → `rederive.log` (sympy for the exact identities; 3.4 s). The builder's `tools/errata_numbers.py` was not read.

**(1) `log_primes_linearIndependent`** — `LinearIndependent ℚ (fun p : Nat.Primes => Real.log ((p : ℕ) : ℝ))`. NOTE H3.3(b), read at
the line: if Σ c_ℓ log ℓ = 0 with finitely many rational c_ℓ ≠ 0, multiply by a common denominator to get integers m_ℓ with Π ℓ^{m_ℓ} = 1
(a positive rational, log injective on (0, ∞)); the ℓ-adic valuation of the left side is m_ℓ, so every m_ℓ = 0. Indexing by `Nat.Primes`
builds in that distinct primes give distinct numbers (linear independence of a family includes injectivity). No hypothesis. Not in
Mathlib at the pin: the grep over the clone's Mathlib for files naming `LinearIndependent`/`linearIndependent`/`LinearIndepOn` together
with `Real.log` or `Nat.Primes` returns exactly `NumberField/Units/Regulator.lean` and `NumberField/CanonicalEmbedding/NormLeOne.lean`
(`check-O/pin-facts.log`) — the builder's grep reproduced. **Faithful; true.**

**(2) `span_log_not_finite`** — for N : Nat.Primes → ℕ with 0 < N p and p ∣ N p for every p, the ℚ-span of {log N p} is not
`Module.Finite`. Hand proof (the NOTE's proof of Theorem R, arithmetic part): every log N p lies in V = ⊕_ℓ ℚ log ℓ (direct by (1));
finitely many generators of the span have coordinates on a finite set S of primes, so every element of the span has support in S; a prime
q ∉ S (Euclid) has log N q with q-coordinate v_q(N q) ≥ 1 because q ∣ N q and N q ≠ 0 — a contradiction. For a ℚ-vector space,
`Module.Finite` (finitely generated) is finite-dimensional, so the negation is dim_ℚ = ∞. Both hypotheses are necessary with Mathlib's
`Real.log 0 = 0`: N ≡ 0 (every p divides 0) and N ≡ 1 give the span ⊥, which is finite — both counterexamples kernel-checked
(`witnesses.lean`, the two `¬ ∀ N, …` examples). Hypotheses satisfiable (N p = p). **Faithful to the label's second clause; true.**

**(3) `rank_span_log_le`** — for N : ι → ℕ with 0 < N i and every prime factor of every N i in a finite S ⊂ ℕ, `Module.rank ℚ (span ℚ
{log N i}) ≤ #S`. Hand proof: log N i = Σ_{q ∣ N i} v_q(N i) log q ∈ span{log q : q ∈ S}, a span of at most #S vectors. (S may contain
non-primes; the bound is then weaker and still true.) It is read-O §2.5's converse "dim_Q G ≤ |char(B)|" in arithmetic form, S playing
char(B) finite, without the κ⁻¹ scaling (FIDELITY §2 says so). `hpos` is removable (E4, below). Satisfiable (S = {2, 3}, N i = 6^i).
**Faithful; true.**

**(4) `lemmaF_finite_fiber`** — with `cls : ℕ → ι`, `v : ι → ℝ`, `κ : ℝ` and hA9: for every n ≥ 2 the family m ↦ Λ(m) over the subtype
{m : ℕ // 2 ≤ m ∧ cls m = cls n} has (unconditional) sum κ · v(cls n); conclusion: {m | IsPrimePow m ∧ cls m = cls n} is finite for
n ≥ 2. Hand proof = NOTE Lemma F(a), first clause: a summable family of nonnegative reals has only finitely many terms ≥ log 2 (the
terms tend to 0 along the cofinite filter), and every prime power m in the fiber has m ≥ 2 (so it lies in the subtype) and Λ(m) =
log(minFac m) ≥ log 2. `IsPrimePow m` is m = p^k with p prime and k ≥ 1, i.e. the NOTE's F_D = {p^k : k ≥ 1, φ_{p^k} = ψ_D} with
D = cls n. The NOTE's "for every D in the image of c" loses nothing by n ≥ 2: a D reached only by Γ_1 has an empty prime-power fiber.
Satisfiable (cls = id, κ = 1, v = Λ — kernel-checked). **Faithful; true.**

**(5) `lemmaF_infinite_order`** — for φ : ℕ → E into a monoid with `hmul : ∀ a b : ℕ, φ (a * b) = φ a * φ b` and hA9 (cls := φ):
φ(p^a) ≠ φ(p^{a+k}) for p prime, a ≥ 1, k ≥ 1. Hand proof = NOTE Lemma F(b): if φ(p^a) = φ(p^{a+k}), then by induction φ(p^{a+jk}) =
φ(p^{a+(j−1)k}) · φ(p^k) = φ(p^a) · φ(p^k) = φ(p^{a+k}) = φ(p^a) for every j ≥ 0, so the fiber of φ(p^a) holds the infinitely many prime
powers p^{a+jk}, against (4). By `hmul`, φ(p^a) = φ(p)^a for a ≥ 1, so the statement says the positive powers of φ(p) are pairwise
distinct — the NOTE's "φ_p has infinite order". **One precision the ledger does not carry (finding F1):** `hmul` ranges over ALL
a, b : ℕ, the index 0 included, whereas the NOTE's φ is a monoid map on M = ℕ≥1 (NOTE §1.1: "φ: M → E, n ↦ φ_n"). At 0, `hmul` demands
φ 0 = φ 0 · φ b = φ a · φ 0 for all a, b — a real constraint: for φ into a group with φ 2 ≠ 1 it fails (`lemmaF-b-positive.lean`, the
closing `example`), and End_β(B) need not contain a two-sided absorbing element. So the Lean hypothesis is weaker than A7 at 1 (no
φ(1) = 1) and stronger at 0, not "weaker" outright as FIDELITY (r6), yaml (aa1) and PREDERIVATION-ERRATA §1(5) say. The mathematics is
unaffected: the topic's statement implies Lemma F(b) for any φ₀ multiplicative on the POSITIVE integers only — adjoin a zero, E :=
`WithZero E₀`, φ 0 := 0, φ n := φ₀ n (n ≥ 1), v extended by 0; the fibers over m, n ≥ 2 are unchanged. This corollary is kernel-checked
from the Solution's proved theorem as `lemmaF_b_on_positive` (`lemmaF-b-positive.log`: `[propext, Classical.choice, Quot.sound]`). The
Lean proof itself uses `hmul` only at positive arguments. Satisfiable (E = (ℕ, ·), φ = id, v = Λ, κ = 1 — kernel-checked).
**Faithful up to the WithZero reduction (checked); true; F1 is a prose precision, no statement changes.**

**(6) `theoremR`** — with `cls`, `v`, `κ`, `hκ : 0 < κ` and hA9 as in (4): ¬ `Module.Finite ℚ` (span ℚ {v(cls n) : n ≥ 2}). This is the
question the brief asks first; the answer is below, then the three-sentence summary in §11.
* *Against the NOTE.* T3's hypotheses at B = Spec Z: H3.1 (A5 over Z: deg(Γ_1 ∩ Γ_n) = Λ(n), n ≥ 2) — built in as the weights
  `vonMangoldt`; H3.2 (A7, A9, A11: "for each D = c(Γ_n), n ≥ 2, L(D) = κ (Δ · D)_Y ∈ R, with one fixed κ > 0") — hA9 with one κ and
  `hκ`; the NOTE's L(D) is "Σ_{n ≥ 2 : φ_n = ψ} Λ(n)" (§1.1), the Lean fiber is {m ≥ 2 : cls m = cls n} — the same index set, with
  non-prime-powers contributing Λ = 0 in both; the NOTE's "D = c(Γ_1) = Δ included when some c(Γ_n), n ≠ 1, equals it" is automatic
  (fibers are indexed by m ≥ 2, whatever their image). H3.3 (Euclid; unique factorization) is not assumed — it is proved inside
  (statements 1–2 and `Infinite Nat.Primes`). H3.4's negation is the conclusion: G = ℚ-span{(Δ · c(Γ_n))_Y : n ≥ 2} = span ℚ (range
  (n : {n // 2 ≤ n}) ↦ v (cls n)), and ¬ `Module.Finite` is dim_ℚ G = ∞. So the Lean statement is T3 in the form "H3.1 ∧ H3.2 ⟹ dim G = ∞"
  — the arithmetic content of "(D3) is empty at B = Spec Z"; the passage from a triple (β, Y, c) to the abstract pair (cls, v) is the
  NOTE's reading and is not in Lean (FIDELITY §2).
* *What is dropped, and why that is sound.* A6, A8, A10, A13, A7's graph structure (c(Γ_n) = Γ_{φ_n} and φ_{mn} = φ_m ∘ φ_n), and A11
  beyond "the diagonal row is real" are absent: `cls` is an arbitrary map and `v` an arbitrary real function. The NOTE's converse
  paragraph says exactly this is admissible — "The proof reads only the fibers of c on components: A7's graph structure is not used (it
  enters Lemma F(b)–(c), not Theorem R)" — and read-O §2.5 lists what the proof uses: "A5 …, A9 with real values and one fixed κ > 0,
  Euclid, unique factorization". Dropping hypotheses makes the Lean theorem more general than T3, never weaker.
* *The proof re-derived.* Lemma F(a) at each prime p: the fiber of cls p has finitely many prime powers and κ · v(cls p) = log N_p with
  N_p = Π_{p'^k in the fiber} p' (the program lemma `fiber_sum_eq_log`: the HasSum collapses to the finite sum over prime powers, each
  contributing log(minFac)); p itself is in its own fiber, so p ∣ N_p and N_p > 0. The ℚ-linear map x ↦ κx sends the diagonal-row span
  onto a subspace containing span{log N_p}; if the former were finite-dimensional, so would be the latter, against (2). For κ = 0 the
  same lines run (the hypotheses are then contradictory, below); no sign of κ is used.
* *Vacuity.* Not vacuous: cls = id, v = Λ/κ satisfies hA9 for every κ ≠ 0 (singleton fibers) — kernel-checked for κ = 1 (the displayed
  case) and κ = −1 (`witnesses.lean`). κ = 0 makes hA9 contradictory at n = 2 (the fiber sum is ≥ Λ(2) = log 2 > 0 = 0 · v) —
  kernel-checked with `le_hasSum`. The conclusion is not a Lean artifact: for N ≡ 1 the analogous span IS finite (item 2's
  counterexample), so `¬ Module.Finite` is a real claim here.
* *One κ is essential* (read-O M1): with κ allowed to depend on n, cls = id, v ≡ 1, κ_n = Λ(n) satisfies the per-n equations and the span
  is ℚ·1. The Lean statement fixes one κ before the ∀ n of hA9. Correct.
* *What it is not:* the general-base Theorem R ("for any base B … if dim_Q G < ∞ then char(B) is finite") — Λ_B, closed points and
  residue fields do not appear; FIDELITY §2 says so. **Verdict: a faithful rendering of NOTE T3 (= Theorem R at B = Spec Z) on the
  abstract pair; true; `hκ` unused; not vacuous.**

**(7) `theoremS_bound`** — g ≥ 0, (1 + x − L)² ≤ 4g²x, (1 + x² − L)² ≤ 4g²x² ⟹ L ≤ (1 + 2g)(1 + r), r := (1 + √(1 + 8g))/2. Re-derived
by hand, independently of the orchestrator's sketch:
* g > 0: h1's right side must be ≥ 0, so x ≥ 0; put s = √x. h1 ⟺ |1 + x − L| ≤ 2gs, so L ≤ 1 + s² + 2gs; h2 ⟺ |1 + x² − L| ≤ 2gx, so
  L ≥ 1 + x² − 2gx. Hence x² − x − 2gx − 2gs ≤ 0, i.e. s⁴ − s² − 2gs² − 2gs ≤ 0, and s⁴ − s² − 2gs² − 2gs = s(s + 1)(s² − s − 2g)
  (sympy, [S1]). For s > 0 this gives s² − s − 2g ≤ 0, i.e. s ≤ r (r the positive root of t² − t − 2g; r ≥ 1); for s = 0, s ≤ r
  trivially. As t ↦ 1 + t² + 2gt increases on t ≥ 0, L ≤ 1 + s² + 2gs ≤ 1 + r² + 2gr, and with r² = r + 2g this is 1 + r + 2g + 2gr =
  (1 + 2g)(1 + r).
* g = 0 (the boundary): h1 and h2 force L = 1 + x and L = 1 + x², so x = x², x ∈ {0, 1}, L ∈ {1, 2}; the bound at g = 0 is
  1 · (1 + (1 + 1)/2) = 2. True, with equality at x = 1, L = 2.
* x < 0: infeasible for g > 0 (h1's right side < 0) and for g = 0 (x ∈ {0, 1}); the random search of [S2] (400 000 draws, x ∈ [−5, 30],
  seed 20260930) finds 11 425 feasible triples, none with x < 0, none above the bound.
* Equality: at x = r², L = 1 + r² + 2gr both h1 and h2 hold with equality (h1: 1 + x − L = −2gr, square 4g²r² = 4g²x; h2: 1 + x² − L =
  r⁴ − r² − 2gr = r(r³ − r − 2g) = r · 2gr = 2gx, using r³ = r² + 2gr = r + 2g + 2gr), and L equals the bound — so the bound is
  attained for every g ≥ 0 and cannot be lowered (E7 confirmed; sympy [S1] gives both slacks = 0 identically; the x-scan of [S2]
  reproduces max L = bound to 4·10⁻¹⁶ at x = r² for g ∈ {0, 0.01, 0.1, 0.5, 1, 2, 5, 10}; kernel-checked at g = 1: x = 4, L = 9).
* `hg` is necessary with Mathlib's `Real.sqrt` (negative ↦ 0): g = −1, x = L = 1 satisfy h1 and h2 (1 ≤ 4 twice) while the bound is
  (1 − 2)(1 + 1/2) = −3/2 — kernel-checked (`witnesses.lean`, first example).
**True; the real algebra only; faithful to the brief's item 7.**

**(8) `theoremS`** — κ > 0, g ≥ 0, d : ℕ → ℝ with both inequalities at L = log p / κ for every prime p ⟹ False. By (7), log p / κ ≤
B(g) for every prime, false for any prime p > exp(κB) (there are infinitely many). First such primes ([S4]): κ = 1, g = 1: B = 9,
e⁹ = 8103.08, p = 8111 (the builder's [N3] reproduced); κ = log 2, g = 1: p = 521; κ = 1, g = 0: p = 11. `hκ` is necessary in the form
κ ≠ 0 (Lean's x / 0 = 0: d ≡ 1, g = 1 satisfy (2)² ≤ 4 twice at every prime — kernel-checked). For κ < 0 the hypotheses are
contradictory at every large prime, but "by h1 alone" (PREDERIVATION-ERRATA §1(8), an aside marked "not needed") holds only for g > 0:
with M = log p/|κ| > g² − 1, h1 fails at x < 0 (right side negative), at x = 0 ((1 + M)² > 0) and at x > 0 ((1 + x + M)² ≥ 4(1 + M)x >
4g²x); at g = 0, h1 is MET by x = d p = −1 − M, and it is h2 that fails ((1 + (1 + M)² + M)² > 0) — finding F3, a one-clause precision.
`hg` is removable (E5: g enters h1, h2 only as g²). The hypotheses are jointly contradictory by design — that is the theorem's content,
not a vacuity defect. **True; faithful to the brief's item 8.**

**Items 7–8 and geometry.** The challenge header says: "(7) `theoremS_bound`, (8) `theoremS` — two REAL-ALGEBRA statements, SCOPED: true
on their face as statements about real numbers. Their reading as a statement about the diagonal of a target surface belongs to the
Session-36 unit under read (rh-program/results/d4-infty-s36/) and is NOT claimed here", and its NOT list ends "the geometric reading of
(7)–(8)". **The header makes no geometric claim.** The two docstrings (probe text, which the brief binds character for character) NAME
the source of the inequalities — "(7) The real-algebra core of Theorem S: the two Castelnuovo–Severi inequalities at `p` and `p²` …",
"(8) Theorem S: …" — a name, not an assertion that any surface exists (observation O1, no fix possible without changing the probe).

## 8. FIDELITY.md and PREDERIVATION-ERRATA re-derived, sentence by sentence

**Quotations** (`check-O/quote_check.py` → `quote-check.log`): every double-quoted fragment of 25+ characters in FIDELITY.md,
PREDERIVATION-ERRATA.md, BUILD-NOTES.md, the challenge header and yaml row (aa), split at ellipses, searched verbatim in NOTE.md,
read-O.md, UNIT-BRIEF.md and the probe: 34 fragments, 30 found; the other 4 are a README section title, a Lean error message, and two
paraphrases of the brief set in quotation marks inside PREDERIVATION-ERRATA ("delegate if Mathlib has it"; "verified numerically in
pre_check.py [P1]") — observation O3. (A first run mis-paired quotes around every short quotation; `quote-check-run1-mispaired.log`.)

**FIDELITY.md.**
* Opening paragraph (10(c)): true — no zeta function, zero or explicit formula occurs in any statement; the NOTE quotation ("T3 is a
  SHAPE theorem, RH-blind; it is not a falsification channel for RH") is verbatim. The label is reproduced verbatim (§9).
* §1 table: each "exact content" cell is the Lean statement read at the line (rows 1–8 checked against §7); each record quotation is
  verbatim. "All eight: no displayed hypothesis beyond the statements' own binders — exactly the list printed in UNIT-BRIEF §0": true
  (§4 [D] and `brief-elab-check2.log`). Axioms for the 8 names and "all 27 program-side declarations": true, and here 27 IS the whole of
  the three files (§3). Statement identity, comparator PASS: reproduced (§4, §6).
* §1 "Which displayed hypotheses the proofs use": `hpos` of item 3 unused (the program theorem is the corollary of
  `rank_span_log_le_of_supp`, read at the line) — true; `hκ` of item 6 unused — true (`theoremR := theoremR_of_A9 …`, read at the line;
  the argument re-derived in §7(6)); "for κ = 0 the hypotheses are contradictory at n = 2, for κ < 0 they are satisfiable and the
  conclusion holds" — true, both kernel-checked (§7(6)); the used-but-removable list (item 4's 2 ≤ n, item 5's 1 ≤ a, item 8's 0 ≤ g) —
  true, each program-side theorem read at the line and printing the three axioms; the used-and-necessary list (item 2's `hpos`, `hdvd`;
  item 7's `hg`; item 8's `hκ` as κ ≠ 0) — true, all four counterexamples kernel-checked (`witnesses.lean`).
* §2 (NOT covered): every bullet true — A6–A8, A7's graphs, A10, A13 appear nowhere; no statement quantifies over targets; the
  general-base Theorem R is absent (no Λ_B, residue field or char(B)); Lemma F(a)'s second clause is the program lemma
  `fiber_sum_eq_log` (read at the line: κ · v(cls n) = log Π minFac over the fiber's prime powers — the NOTE's N_D = Π_{p^k ∈ F_D} p, as
  minFac(p^k) = p) and Lemma F(c) is not stated; the κ-scaling of the converse is not stated; rung 1, T1, T2, Prop. 2.2.1, Cor. 3.1–3.2,
  routes (a)/(b) are not stated; "the bound of item 7 is attained" — true (§7(7)). The sentence "The staged zoo entry built on the NOTE is
  therefore not, as a whole, a Lean statement" is correct and is the opposite of the first forbidden phrasing.
* §3 (r1)–(r11): (r1) true (the NOTE's converse-paragraph quotation verbatim); (r2) true; (r3) true (`vonMangoldt_apply` at
  VonMangoldt.lean l. 73: `Λ n = if IsPrimePow n then Real.log (minFac n) else 0`, `pin-facts.log`); (r4) true; (r5) true; **(r6)
  incomplete — finding F1** (§7(5): `hmul` is demanded at the index 0 too, so the hypothesis is not simply "weaker"; the statement still
  implies the NOTE's Lemma F(b), kernel-checked); (r7) true; (r8) true (and each of the three totalizations is exercised by a
  kernel-checked counterexample); (r9)–(r11) true. "Fidelity divergences in the brief's sense (a hypothesis beyond the statements' own):
  NONE" — true: `hmul` is the brief's own binder (§4 [D]: the brief's `∀ a b, …` elaborates to the challenge's `∀ a b : ℕ, …`).
* §4 (items 7–8 scoped): true (§7(7)–(8)); the challenge header, yaml rows and README section assert no geometric reading.

**PREDERIVATION-ERRATA.**
* §1 (1)–(8): true as stated, with two exceptions: §1(5)'s "a weaker hypothesis, so a stronger theorem" (F1) and §1(8)'s aside "by h1
  alone" (F3: false at g = 0, where h2 is needed; the aside is marked "not needed" and carries no load). §1(1)'s Mathlib grep reproduced
  (`pin-facts.log`); §1(2)'s two counterexamples, §1(7)'s g = −1 counterexample and §1(8)'s κ = 0 counterexample kernel-checked;
  §1(6)'s non-vacuity witness (cls = id, v = Λ/κ) kernel-checked for κ = ±1.
* **E1** (the brief's parenthetical wrong for κ < 0; `hκ` unused): CONFIRMED. κ = 0: contradictory at n = 2 (kernel-checked with
  `le_hasSum`); κ < 0: satisfiable (kernel-checked at κ = −1) and the conclusion holds (the span of {Λ(n)/κ} is κ⁻¹ times the span of
  {log p}); the proof is uniform in κ (§7(6)).
* **E2** (item 4 needs no 2 ≤ n): CONFIRMED by hand — for n < 2 the set is empty or equals the fiber of any of its members m₀ ≥ 2 — and
  as the program theorem `lemmaF_finite_fiber_all` (three axioms).
* **E3** (item 5 needs no 1 ≤ a): CONFIRMED — if φ(1) = φ(p^k) then φ(p^k) = φ(1 · p^k) = φ(1)φ(p^k) = φ(p^k)φ(p^k) = φ(p^{2k}), the case
  a = k (uses `hmul` at positive arguments only); `lemmaF_infinite_order_all` (three axioms).
* **E4** (item 3's positivity removable): CONFIRMED, both routes — an N i = 0 contributes Real.log 0 = 0 (the program proof), and
  independently `hsupp` would put every prime into the finite S (the errata's §2 argument).
* **E5** (item 8's 0 ≤ g removable): CONFIRMED — h1, h2 see g only through g²; `theoremS_abs` applies item 8 at |g|.
* **E6** ([P1] samples x ≥ 0 only): CONFIRMED at the line — `results/d4-infty-s36/prederivation/pre_check.py` line 15:
  `xs = np.linspace(0, (r**2)*1.5 + 2, 400001)`.
* **E7** (every step of item 7; the bound attained at x = r², L = 1 + r² + 2gr): CONFIRMED by hand and exactly (§7(7), [S1], [S2]).
* **E8** (names at the pin): CONFIRMED in the clone's Mathlib (`pin-facts.log`): `vonMangoldt_apply` l. 73, `vonMangoldt_nonneg` l. 80,
  `vonMangoldt_apply_pow` l. 86, `vonMangoldt_apply_prime` l. 89, `vonMangoldt_eq_zero_iff` l. 99; `Nat.infinite_setOf_prime` a deprecated
  alias (since 2026-07-09) of `infinite_setOfPred_prime` (Data/Nat/PrimeFin.lean l. 30); `Infinite.exists_notMem_finset`
  (Data/Fintype/EquivFin.lean l. 450).
* **E9** (no ChallengeDeps module): CONFIRMED — the challenge imports Mathlib only and the comparator run needed nothing else (§6).
* **E10** (the unused-variable linter fires at the pin): consistent with this check (`brief-elab-check.log` shows the linter on unused
  binders); the Solution's zero-warning build confirms it passes every hypothesis on.
* **Necessity counterexamples**: item 2 (N ≡ 0; N ≡ 1), item 7 (g = −1, x = L = 1), item 8 (κ = 0, d ≡ 1, g = 1) — CONFIRMED by hand,
  numerically ([S3]) and in the kernel (`witnesses.lean`).
* **BUILD-NOTES.** Every number re-read against its log; one stale line reference (F2): "lines 103–156 of `LogPrimes.lean`" is the
  rung-1 file's numbering (SHARED.md 17:27:58 says so, with the rung-1 hash 9a76d131…); in the shipped file item 1 and its helpers are
  lines 104–157 (`pin-facts.log`). The 54-line count is right.

## 9. The label, the forbidden phrasings, 10(g) (`check-O/forbidden_label_lint.py`, `forbidden-label-lint.log`)

The label and the forbidden phrasings were READ from UNIT-BRIEF §1(3) by the script (not typed), and searched over the seven unit files
of `rh-program/lean`, the whole `lean/formalization.yaml` and `lean/README.md`, and every file of `results/theoremR-lean-s36/` outside
`check-O/` (comments and docstrings included):
* **The label, verbatim** (whitespace-normalized, markdown bold ignored): once each in BUILD-NOTES.md, FIDELITY.md,
  `lean/formalization.yaml` (the `main_results` description) and `lean/README.md` (the ResidueRank section), and in the brief itself.
  **Earned**: every clause is a checked fact — (1) ↔ "the logarithms of the primes are ℚ-linearly independent"; (2) ↔ "a family of
  positive integers N_p with p | N_p has logarithms spanning an infinite-dimensional ℚ-space"; (3) ↔ "the converse rank bound"; (4)–(5)
  ↔ "Lemma F" (the brief's items 4–5 = F(a)'s finiteness clause and F(b); observation O2); (6) ↔ "Theorem R on the abstract pair (von
  Mangoldt weights, real fiber sums, one κ)"; "over Mathlib alone" (no ChallengeDeps; the challenge imports Mathlib, the solution only
  the program modules, which import only Mathlib); "no displayed hypothesis" (§4 [D], FIDELITY §3); "the three standard axioms" (§3);
  "replayed by nanoda" (§6, reproduced from the clean clone). The "only if everything lands" condition holds.
* **Forbidden phrasings: 0 hits in every file of the unit, the yaml and the README**; the only hits are in UNIT-BRIEF.md, which states
  the rule. Every line of the unit's files that mentions RH, ζ or zeros was printed and read: each is a disclaimer ("nothing about ζ's
  zeros or RH follows", "What is NOT claimed: anything about ζ's zeros or RH"), an item in a NOT-covered list, or the Lean induction case
  name `zero`; README l. 669 is the parent paper's title in an older section. **No sentence connects the topic to RH or to the zeros.**
* 10(g): the four banned phrases — 0 hits outside the brief (which quotes the rule). U.S. spelling: 0 British forms in prose (the hits
  are identifiers such as `grid_corner_pointwise` and the builder's lint word lists).

## 10. Hashes and the yaml (`check-O/hash-recompute.log`, `check-O/yaml-validation.log`)

* Every one of the 33 SHA-256s in `hashes.txt` recomputed with `shasum -a 256 -c`: **33 OK, 0 FAILED**. `hashes.txt` itself =
  `2badc8cfa545c73b…`, the value SHARED.md's final builder block quotes; BUILD-NOTES.md `f882e480…` and FIDELITY.md `b25f4f45…` equal
  their SHARED.md values; the clean-clone copies of the seven Lean/config files have the listed hashes. Files of the folder not in
  `hashes.txt`: exactly the declared exclusions (`hashes.txt`, `SHARED.md`) and the two inputs (`UNIT-BRIEF.md`, `typing-probe.lean`,
  whose hashes the header quotes and which equal their recomputed values). SHARED.md at the time of this check (before this checker's
  block): `195a06bf…`.
* `validate_yaml_sigma_strong.py` re-run from `rh-program` on `formalization.yaml` `2aad986e…`: schemas identical upstream, **VALIDATION
  errors: 0, undeclared names: 0, RESULT: PASS**. (A first attempt wrapped the call in GNU `timeout`, which macOS lacks — five "command
  not found", nothing run; logged.)
* This checker's own files: `check-O/hashes-checker.txt` (SHA-256 of every file under `check-O/`, written last); this file's hash is in
  the checker's SHARED.md block. `check-O/self-lint.log`: the same lint run over this checker's files — forbidden phrasings 0, banned
  phrases 0 (the lint script stores the banned phrases reversed and prints neither list, so no log repeats them).

## 11. Verdict, findings, observations

(Every OLD: string below occurs exactly once in its file, line breaks read as spaces — checked by `check-O/old_strings_check.py`,
`old-strings-check.log`.)

**Verdict: FIX-FIRST — prose only (F1–F3). The eight Lean statements, the proofs, every cold build on the fresh v1.0 clone, the axioms,
statement identity, the trust greps and the comparator run with nanoda are CLEAN; the label of UNIT-BRIEF §1(3) is earned verbatim; no
forbidden phrasing appears anywhere.** None of the three findings touches a theorem, a trusted file or the label; F1 is the one with
content (a fidelity sentence that states the direction of a hypothesis change incompletely); F2 and F3 are one-clause accuracy fixes.
The orchestrator may apply them without a new comparator run (no Lean file changes).

**Statement 6 (`theoremR`) in three sentences.** Under the brief's abstraction — c on components as an arbitrary map `cls`, the diagonal
row as an arbitrary real function `v`, A5 as von Mangoldt weights, A9 as one unconditional `HasSum` per fiber over m ≥ 2 with ONE κ —
`theoremR` states exactly NOTE T3's conclusion dim_ℚ G = ∞ at B = Spec Z from H3.1–H3.2, with H3.3 (Euclid, unique factorization)
proved inside rather than assumed; it drops A6–A8, A7's graph structure and the rest of A11, which the NOTE's converse paragraph and
read-O §2.5 say Theorem R does not use, so it is if anything more general than T3. Its hypotheses are satisfiable (cls = id, v = Λ/κ, any
κ ≠ 0; kernel-checked at κ = 1 and κ = −1), so it is not vacuous; κ = 0 makes them contradictory at n = 2, and the displayed κ > 0 is
unused by the proof (E1 confirmed), while the one κ is essential (with κ depending on the fiber, v ≡ 1 would pass). It is the
B = Spec Z instance only — not the general-base Theorem R ("if dim_Q G < ∞ then char(B) is finite") — which FIDELITY §2 records correctly.

**F1 (fidelity ledger: statement 5's `hmul` at the index 0).** FIDELITY (r6), yaml (aa1), PREDERIVATION-ERRATA §1(5) and one clause of
BUILD-NOTES §4 describe the Lean hypothesis of Lemma F(b) as weaker than A7 (no φ(1) = 1). It is weaker at 1 but STRONGER at 0: `hmul :
∀ a b : ℕ, …` also demands φ 0 = φ 0 · φ b = φ a · φ 0, which the NOTE's φ on M = ℕ≥1 does not supply and which a nontrivial φ into a group
cannot meet (kernel-checked example). The theorem is unaffected in substance: it implies Lemma F(b) for any φ multiplicative on the
positive integers, through `WithZero E` (kernel-checked, `check-O/lemmaF-b-positive.lean`, three axioms). No Lean file changes.
OLD: weaker hypothesis); by `hmul`, φ(p^a) = φ(p)^a for a ≥ 1, so the statement is the NOTE's "pairwise distinct".
NEW: weaker hypothesis at 1) — but `hmul` is demanded at the index 0 too (φ 0 = φ 0 · φ b = φ a · φ 0), where the NOTE's φ on ℕ≥1 is not defined and which a nontrivial φ into a group cannot meet; the statement still implies the NOTE's Lemma F(b) for every φ multiplicative on the positive integers, through `WithZero E` with 0 ↦ 0 (CHECK-O §7(5), kernel-checked in `check-O/lemmaF-b-positive.lean`); by `hmul`, φ(p^a) = φ(p)^a for a ≥ 1, so the statement is the NOTE's "pairwise distinct".
OLD: and Lemma F(b) keeps only multiplicativity, without φ(1) = 1.
NEW: and Lemma F(b) keeps only multiplicativity, without φ(1) = 1 but over all of ℕ (index 0 included — a demand the NOTE's φ on ℕ≥1 does not carry; the statement implies the NOTE's Lemma F(b) through WithZero E, results/theoremR-lean-s36/CHECK-O.md §7(5)).
OLD: φ(p^a) and needs neither φ(p^a) = φ(p)^a nor φ(1) = 1 (A7's φ_1 = id is not used — a weaker hypothesis, so a stronger theorem).
NEW: φ(p^a) and needs neither φ(p^a) = φ(p)^a nor φ(1) = 1 (A7's φ_1 = id is not used — weaker there; but `hmul` ranges over all a, b : ℕ, the index 0 included, which the NOTE's φ on ℕ≥1 does not supply — stronger there; the statement implies the NOTE's Lemma F(b) through `WithZero E`, CHECK-O §7(5)).
OLD: Lemma F(b) on φ(p^a) without φ(1) = 1;
NEW: Lemma F(b) on φ(p^a) without φ(1) = 1 but with `hmul` over all of ℕ, index 0 included (CHECK-O F1);

**F2 (a stale line reference).** BUILD-NOTES "Stop lines" paragraph: item 1 and its two valuation helpers are lines 104–157 of the
shipped `LogPrimes.lean`; "103–156" is the rung-1 file's numbering (SHARED.md 17:27:58, rung-1 hash 9a76d131…). (SHARED.md's own
"lines 103–156" is a dated log line about the rung-1 file; leave it.)
OLD: (lines 103–156 of `LogPrimes.lean`;
NEW: (lines 104–157 of the shipped `LogPrimes.lean`, 103–156 of the rung-1 file;

**F3 (an aside, one clause).** PREDERIVATION-ERRATA §1(8): for κ < 0 and g = 0, h1 alone is satisfiable (d p = log p/κ − 1) and h2 is
what fails; "by h1 alone" holds for g > 0 only (§7(8)). Carries no load ("not needed").
OLD: (For κ < 0 the hypotheses are also contradictory, by h1 alone at a large prime — not needed.)
NEW: (For κ < 0 the hypotheses are also contradictory at every large prime — by h1 alone when g > 0; when g = 0, h1 is met by d p = log p/κ − 1 and it is h2 that fails — not needed.)

**Observations (no fix required of this unit).**
* **O1 — docstrings of items 7–8.** The probe's docstrings (bound character for character) name the source of the inequalities: "the two
  Castelnuovo–Severi inequalities at `p` and `p²`", "Theorem S". A name, not a claim; the challenge header's SCOPED paragraph and its NOT
  list ("the geometric reading of (7)–(8)") govern. If the orchestrator wants the trusted text free of the geometric name, that is a
  probe change and a new comparator run — not recommended for this unit.
* **O2 — what "Lemma F" covers.** The label's "Lemma F" is the brief's items 4–5: F(a)'s finiteness clause and F(b). F(a)'s second clause
  (L(D) = log N_D) is kernel-checked only as the program lemma `fiber_sum_eq_log` inside the Solution's proof of `theoremR` (so the
  comparator's kernel replay covered it as a dependency, but it is not a compared statement), and F(c) is not stated; FIDELITY §2 says
  both. A zoo or STATUS line that wants precision can write "Lemma F (a: finiteness; b)".
* **O3 — two paraphrases in quotation marks** in PREDERIVATION-ERRATA ("delegate if Mathlib has it" for the brief's "the solution
  delegates to it"; "verified numerically in pre_check.py [P1]" for "Verified numerically in `results/d4-infty-s36/prederivation/
  pre_check.py` [P1]"). Harmless.
* **O4 — sandbox.** The comparator runs (builder's and this one) are NOT sandboxed (macOS; fake-landrun shim), as in every prior macOS
  record; the solution was read in full here and imports no trusted-side module. A Linux re-run under Landlock (COMPARATOR-RUN.md §2's
  Session-32 note) would add the sandbox.
* **O5 — independence.** Read before the checks: the brief, BUILD-NOTES, SHARED.md, hashes.txt, the builder's `tools/run.sh` and
  `tools/prerun-cleanup.sh` (to adapt them, two lines each), and the builder's `program-axioms.lean` (to compare name lists). Read only
  after this file's §1–§6 were written: FIDELITY.md, PREDERIVATION-ERRATA.md, the yaml rows and the README section. Never run or read:
  `tools/statement_identity_s36.py`, `tools/trust_greps_s36.py`, `tools/errata_numbers.py` and its log, `tools/lint_10g.py`. Every script
  and probe under `check-O/` is this checker's own.
* **O6 — this checker's own slips, all repaired and logged:** a relative log path (the first build log landed in the clone's root; moved);
  a substring bug in the identity script's [C] (`statement-identity-run1-buggy.log`); a probe artifact of `def`-elaboration in the brief
  comparison (`brief-elab-diff.log`; the theorem-form re-check is clean); quote mis-pairing in the first quote check
  (`quote-check-run1-mispaired.log`); GNU `timeout` absent on macOS (yaml validation re-run without it); two tactic steps in the witness
  probes needed a second and third run (logged in `witnesses.log` / `lemmaF-b-positive.log` headers).

**OVERALL.** Mathematics and machine checks: CLEAN — a fresh v1.0 clone (HEAD 3635e74), Mathlib 51e6992e from the cache, the seven unit
files overlaid and nothing else; cold builds one at a time (8697 / 8698 / 8697 / 8700 / 8697 jobs; 0 warnings except the challenge's 8
deliberate `sorry`s); `#print axioms` on the 8 topic names and all 27 program declarations = `[propext, Classical.choice, Quot.sound]`,
with a `sorryAx` negative control; statement identity 8/8 (challenge = solution = probe, the brief's §0 text elaborating to the same
terms); trust greps clean; the comparator with nanoda exit 0 ("Nanoda kernel accepts the solution", "Your solution is okay!", 37.5 s);
every statement read against the NOTE and found true and faithful, statement 6 a faithful rendering of T3 at B = Spec Z and not
vacuous; item 7's bound re-derived by hand, attained, g = 0 included; E1–E10 and the necessity counterexamples confirmed (the four
counterexamples and three non-vacuity witnesses kernel-checked); 33/33 hashes; yaml validation PASS. Ledger: FIX-FIRST on F1–F3 (prose).
Nothing about ζ's zeros or RH follows from anything here.
