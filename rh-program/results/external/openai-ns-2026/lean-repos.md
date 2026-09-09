# Lean repos: OpenAI NavierStokesAndEuler and Alpöge–Buckmaster fluid_lean

Agent `lean-repos`, 2026-09-09. Both repositories were cloned into the session scratchpad (not into the project) and inspected on disk. Lean toolchain present locally: elan 4.2.4. Neither full project was built (see §Build estimate). Quoted text is verbatim from the repositories at the commits recorded below.

## 1. openai/NavierStokesAndEuler

### 1(a) README, verbatim

```markdown
# Finite time blowup for Navier–Stokes and Euler equations

This repository contains Lean 4 formalizations of the results presented in
“Finite time blowup for Navier–Stokes” and
“Finite time blowup for the Euler equation” by OpenAI.

## Navier Stokes

For every positive viscosity, we prove two results:

- **Whole space $\mathbb{R}^3$:** There exist smooth initial data and forcing for
  which no global smooth solution with uniformly bounded kinetic energy exists.
- **Periodic torus $\mathbb{R}^3/\mathbb{Z}^3$:** There exist smooth periodic
  initial data and forcing for which no global smooth solution exists.

These are alternatives [**(C)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes solutions on ℝ³”
and [**(D)**](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf#page=2) “Breakdown of Navier–Stokes Solutions on ℝ³/ℤ³”
in the Clay Mathematics Institute’s [official problem description](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)
of the [Navier–Stokes existence and smoothness](https://www.claymath.org/millennium/navier-stokes-equation/)
[Millennium Prize Problem](https://www.claymath.org/millennium-problems/).

## Euler

We construct smooth, compactly supported, divergence-free initial velocity on
$\mathbb{R}^3$ whose solution to the unforced incompressible Euler equations
develops a singularity in finite time. The velocity’s $C^1$ norm becomes unbounded
near that time, and the time integral of the vorticity’s $L^\infty$ norm diverges.

## Building the formalizations

The project uses Lean 4.34.0-rc2, Mathlib, and Lake. With
[elan](https://github.com/leanprover/elan) installed, fetch the mathlib cache and build the formalizations with:

```sh
lake exe cache get
lake build
```

## Independent proof checking

For instructions on checking the formalizations with Comparator, see the
[ComparatorChallenges README](ComparatorChallenges/README.md).
```

### 1(a′) Build configuration (lean-toolchain, lakefile.toml, verbatim)

```
leanprover/lean4:v4.34.0-rc2

name = "NavierStokesAndEuler"
version = "0.1.0"
defaultTargets = ["NavierStokes", "Euler", "ComparatorChallenges"]

[[require]]
name = "mathlib"
scope = "leanprover-community"
git = "https://github.com/leanprover-community/mathlib4.git"
rev = "v4.34.0-rc2"

[[require]]
name = "Comparator"
scope = "leanprover"
git = "https://github.com/leanprover/comparator.git"
rev = "v4.34.0-rc2"

[[lean_lib]]
name = "NavierStokes"
globs = ["NavierStokes", "NavierStokes.+"]

[[lean_lib]]
name = "Euler"
leanOptions = { autoImplicit = false, warningAsError = true }
globs = ["Euler", "Euler.+"]

[[lean_lib]]
name = "ComparatorChallenges"
globs = ["ComparatorChallenges.+"]
```

The manifest pins Mathlib at `85e3a25e006c35636f0e53b0e9296caca2685bc0` (tag v4.34.0-rc2) and Comparator at `19e111e2141cf333c7daff0f64c5f24acc91dd2e` (tag v4.34.0-rc2); Comparator pulls in `lean4export` (leanprover, master). The `Euler` library is compiled with `autoImplicit = false, warningAsError = true`; the `NavierStokes` library sets neither.

### 1(d-ii) formalization.yaml, verbatim

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/mathlib-initiative/formalization.yaml/main/schema/formalization.schema.json

# formalization.yaml (v0.4): repo-root metadata for formalization projects.
version: "v0.4"

project:
  name: "NavierStokesAndEuler"
  description: >-
    This project formalizes finite-time blowup in Lean 4 for the three-dimensional
    incompressible Navier–Stokes equations with smooth forcing, for every positive
    viscosity, on Euclidean space and the periodic torus. It also formalizes
    unforced Euler blowup.
  authors:
    - "OpenAI"
  license: "Apache-2.0"

sources:
  - title: "Finite time blowup for Navier–Stokes"
    authors:
      - "OpenAI"
    type: "article"
    location: "Main theorem and periodic finite-time blowup corollary"
    relationship: "formalizes"
  - title: "Finite time blowup for the Euler equation"
    authors:
      - "OpenAI"
    type: "article"
    location: "Main theorem"
    relationship: "formalizes"

related_formalizations:
  - id: "https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Millenium/NavierStokes.lean"
    relationship: "builds-on"
    note: >-
      The Formal Conjectures Navier–Stokes formalization supplies the independent
      Comparator reference statements and definitions for alternatives (C) and (D).

classification:
  arxiv:
    - "math.AP"
  msc2020:
    - "35Q30"
    - "35Q31"

status:
  scope: "Full formalization of main results."
  sorry_count: 0
  sorry_in_definitions: 0
  main_results:
    - description: >-
        (C) Non-existence of global smooth solutions with uniformly bounded kinetic
        energy on Euclidean space.
      declaration: "NavierStokes.Comparator.navier_stokes_breakdown_R3"
      file: "NavierStokes/ComparatorSolution.lean"
      sorry_count: 0
      axioms:
        - "propext"
        - "Classical.choice"
        - "Quot.sound"
      comparator_config: "ComparatorChallenges/NavierStokes.json"
    - description: "(D) Non-existence of global smooth periodic solutions"
      declaration: "NavierStokes.Comparator.navier_stokes_breakdown_periodic"
      file: "NavierStokes/ComparatorSolution.lean"
      sorry_count: 0
      axioms:
        - "propext"
        - "Classical.choice"
        - "Quot.sound"
      comparator_config: "ComparatorChallenges/NavierStokes.json"
    - description: >-
        Non-existence of global smooth unforced Euler solutions with uniformly
        bounded kinetic energy on Euclidean space.
      declaration: "Euler.euler_breakdown_R3"
      file: "Euler/Solution.lean"
      sorry_count: 0
      axioms:
        - "propext"
        - "Classical.choice"
        - "Quot.sound"
      comparator_config: "ComparatorChallenges/Euler.json"
    - description: >-
        Compact smooth initial data for unforced Euler with a positive finite
        maximal lifespan in the all-order Sobolev solution class, an infinite
        C1 norm limsup, and an infinite time integral of the vorticity norm.
      declaration: "Euler.exists_compact_smooth_euler_singularity"
      file: "Euler/Solution.lean"
      sorry_count: 0
      axioms:
        - "propext"
        - "Classical.choice"
        - "Quot.sound"
      comparator_config: "ComparatorChallenges/Euler.json"

automation:
  methods:
    - method: "agent"
      models:
        - "GPT-6 Astra"
      framework: "Codex"

review:
  status: "self-assessed"

alignment:
  namespaces:
    - "NavierStokes.Comparator"
    - "Euler"
  statements:
    - source: "Theorem 1.1 (Navier–Stokes on ℝ³)"
      lean: "NavierStokes.Comparator.navier_stokes_breakdown_R3"
      module: "NavierStokes.ComparatorSolution"
      status: "proved"
    - source: "Corollary 10.6 (Navier–Stokes on ℝ³/ℤ³)"
      lean: "NavierStokes.Comparator.navier_stokes_breakdown_periodic"
      module: "NavierStokes.ComparatorSolution"
      status: "proved"
    - source: "Theorem 1.1 (Euler)"
      lean: "Euler.euler_breakdown_R3"
      module: "Euler.Solution"
      status: "proved"
    - source: "Theorem 1.1 (Euler), alternate version"
      lean: "Euler.exists_compact_smooth_euler_singularity"
      module: "Euler.Solution"
      status: "proved"

acknowledgements: >-
  Thank you very much to the authors of Lean 4 and mathlib, as well as Formal
  Conjectures, Lake, Comparator, lean4export, nanoda, and related tools.
```

### 1(b) Size and history

Measured on the clone at commit `8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538` (2026-09-08 06:57:25 -0400).

| Quantity | Value |
|---|---|
| `.lean` files (excluding `.lake/`) | 2,486 |
| Total lines of Lean | 616,276 (32.4 MB of source) |
| `NavierStokes/` | 643 files, 392,455 lines (one subdirectory, `NavierStokes/R3/`) |
| `Euler/` | 1,839 files, 211,579 lines (flat, no subdirectories) |
| `ComparatorChallenges/` | 5 files: README.md, NavierStokes.lean, NavierStokes.json, Euler.lean, Euler.json |
| File-size distribution | <100 lines: 1,014 files; 100–300: 1,046; 300–600: 167; 600–1,000: 138; ≥1,000: 121 |

Largest files by line count:

```
   20755  Euler/EulerProof.lean
    9849  NavierStokes/CorrectionStep.lean
    5573  NavierStokes/CorrectionInitializationNoOptions.lean
    5562  NavierStokes/CorrectionInitialization.lean
    3004  NavierStokes/VariableGaugeMean.lean
    2854  NavierStokes/InitialPhysicalData.lean
    2807  NavierStokes/BaseResidual.lean
    2679  NavierStokes/NominalProfile.lean
    2602  NavierStokes/ParticularWaveBounds.lean
    2253  NavierStokes/TransitionRamp.lean
    2180  NavierStokes/OutgoingEntranceCone.lean
    2146  NavierStokes/ActualSignedPhysicalData.lean
    2065  NavierStokes/PrimaryPulseBounds.lean
    2037  NavierStokes/MeanRankUpdate.lean
    2031  NavierStokes/ActivationContinuation.lean
```

**Commit history: exactly one commit.** `git log` shows a single commit, `8937a8f`, dated 2026-09-08 06:57:25 -0400, author Boris Alexeev `<balexeev@openai.com>`, commit message `.` (a single period). No tags, one branch (`main`). So the public history carries no information about how the 616k lines were produced — no incremental development, no review trail, no per-file authorship. The development happened elsewhere (presumably in an internal repository or agent workspace) and was squashed into a single drop. For comparison, Mathlib itself is roughly 1.7M lines; this drop is over a third of Mathlib's size, delivered in one commit. The only attribution to a process is `formalization.yaml`'s `automation.methods: agent / GPT-6 Astra / Codex` and its `review.status: self-assessed`.

For scale: `Euler/` has 1,839 files averaging 115 lines, with one 20,755-line file (`EulerProof.lean`) sitting on top; `NavierStokes/` has 643 files averaging 610 lines. The two subprojects were clearly produced by different runs or different regimes (the Euler library also compiles under `autoImplicit = false, warningAsError = true`, the Navier–Stokes library does not).

### 1(e) `ComparatorChallenges/` — independent proof checking

**What Comparator is.** [Comparator](https://github.com/leanprover/comparator) is a tool from the Lean FRO (pinned here at tag `v4.34.0-rc2`). Its purpose is to check that a *solution* module proves exactly the theorems stated in an independent *challenge* module: it exports both environments with `lean4export`, compares the theorem *types* (statements) declaration-for-declaration, re-checks the solution's proof terms with an independent external kernel (`nanoda`, a Rust re-implementation of the Lean type checker), and verifies that the proof uses only a permitted axiom list. The sandbox `landrun` is used to isolate the run. The point is to defeat the standard attacks on a "0 sorries" claim: redefining the statement in the solution, smuggling in an axiom, exploiting a Lean kernel bug, or using `native_decide`/`implemented_by` to trust compiled code.

**How the challenge is set up.** Each of the two JSON files names a *challenge module* (a standalone file importing only Mathlib, with the theorems stated and their proofs given as `sorry`), a *solution module* (inside the project), a list of theorem names that must match, `enable_nanoda: true`, and a permitted axiom list of exactly `propext`, `Quot.sound`, `Classical.choice` — the three standard axioms of Lean's `Classical` core. Verbatim:

```json
{
  "challenge_module": "ComparatorChallenges.NavierStokes",
  "solution_module": "NavierStokes.ComparatorSolution",
  "enable_nanoda": true,
  "theorem_names": [
    "NavierStokes.Comparator.navier_stokes_breakdown_R3",
    "NavierStokes.Comparator.navier_stokes_breakdown_periodic"
  ],
  "permitted_axioms": [
    "propext",
    "Quot.sound",
    "Classical.choice"
  ]
}

{
  "challenge_module": "ComparatorChallenges.Euler",
  "solution_module": "Euler.Solution",
  "enable_nanoda": true,
  "theorem_names": [
    "Euler.euler_breakdown_R3",
    "Euler.exists_compact_smooth_euler_singularity"
  ],
  "permitted_axioms": [
    "propext",
    "Quot.sound",
    "Classical.choice"
  ]
}
```

**The challenge README, verbatim:**

```markdown
# [Comparator](https://github.com/leanprover/comparator) challenges

Install `landrun`, `lean4export`, and `nanoda_bin`, and make them available on `PATH`. Then, from the repository root:

```sh
lake exe cache get
lake exe comparator ComparatorChallenges/NavierStokes.json
lake exe comparator ComparatorChallenges/Euler.json
```

Thank you to the [Formal Conjectures](https://google-deepmind.github.io/formal-conjectures/) authors for their [Lean formalization of the Navier–Stokes problem statement](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/Millenium/NavierStokes.lean), which we adapted for these Comparator challenges.
```

**Provenance of the challenge statements.** Both challenge files carry the Formal Conjectures (Google DeepMind) copyright header and state that they were adapted from `FormalConjectures/Millenium/NavierStokes.lean` — the NS one at pinned upstream commit `8bf45ed70d48b2b2a501de9c00b26bfa38c573ee`. The Navier–Stokes challenge says "The upstream definitions, helper proofs, and breakdown alternatives (C) and (D) are retained, including their intentional `sorry` challenge placeholders … Neither the proof root nor the submission imports this reference." That last clause matters: the solution cannot cheat by importing and reusing the challenge's definitions; the definitions are duplicated independently on both sides and Comparator checks that the two *types* agree up to the export. The Euler challenge, by contrast, is *not* an upstream Formal Conjectures statement — it is OpenAI's own specialization ("the whole-space breakdown alternative specialized to zero viscosity and zero external force") plus a second, much more elaborate theorem (`exists_compact_smooth_euler_singularity`) whose solution class (`EulerSobolevExistenceAndSmoothnessR3On`, `SobolevSmoothOn`, `toL2`) was written by OpenAI. So for Euler the "independent" statement is independent of the *proof* but not of the *authors*; there is no third-party statement of the Euler theorem to compare against.

**What I could and could not verify locally.** I did not run Comparator (it needs `landrun`, `lean4export`, `nanoda_bin` on PATH and a full build of the 616k-line project; see §Build estimate). What I did verify is below in §1(d): the axiom-relevant greps over the entire source, and that the solution files' theorem statements are textually identical to the challenge files' statements.

### 1(c) The main theorem statements, verbatim, and what they say

The four exported theorems live in two thin "solution" files whose only job is to restate the challenge theorems under the reference names and discharge them from the bulk of the development.

**(C) and (D), `NavierStokes/ComparatorSolution.lean` lines 15–27** (the file is 32 lines; lines 31–32 are `#print axioms` for both theorems):

```lean
/-- (C) Breakdown of Navier–Stokes solutions on ℝ³. -/
theorem navier_stokes_breakdown_R3 (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionDecay u₀ ∧ ForceConditionDecay f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p) := by
  exact ComparatorBridge.navier_stokes_breakdown_R3 nu hnu

/-- (D) Breakdown of Navier–Stokes solutions on ℝ³/ℤ³. -/
theorem navier_stokes_breakdown_periodic (nu : ℝ) (hnu : nu > 0) :
    ∃ (u₀ : ℝ³ → ℝ³) (f : ℝ³ → ℝ → ℝ³),
    InitialVelocityConditionPeriodic u₀ ∧ ForceConditionPeriodic f ∧
    ¬ (∃ v p, NavierStokesExistenceAndSmoothnessPeriodic nu u₀ f v p) := by
  exact ComparatorBridge.navier_stokes_breakdown_periodic nu hnu
```

The structures these mention are defined identically in `ComparatorChallenges/NavierStokes.lean` (the trusted reference, lines 36–270) and `NavierStokes/ComparatorDefinitions.lean` (the solution-side copy; `diff -w` between the two shows only the header comment and the two theorem placeholders differ). The key ones, verbatim from the reference:

```lean
structure NavierStokesExistenceAndSmoothness
    (nu : ℝ) (u₀ : ℝ^n → ℝ^n) (f : ℝ^n → ℝ → ℝ^n)
    (v : ℝ^n → ℝ → ℝ^n) (p : ℝ^n → ℝ → ℝ) : Prop where
  navier_stokes : ∀ x, ∀ t ≥ 0,
    derivWithin (v x ·) (Set.Ici 0) t + fderiv ℝ (v · t) x (v x t) =
      nu • Δ (v · t) x - gradient (p · t) x + f x t
  div_free : ∀ x, ∀ t ≥ 0, ∇⬝ (v · t) x = 0
  initial_condition : ∀ x, v x 0 = u₀ x
  velocity_smooth : ContDiffOn ℝ ∞ (↿v) (Set.univ ×ˢ Set.Ici 0)
  pressure_smooth : ContDiffOn ℝ ∞ (↿p) (Set.univ ×ˢ Set.Ici 0)

structure NavierStokesExistenceAndSmoothnessRn ... extends NavierStokesExistenceAndSmoothness nu u₀ f v p where
  integrable : ∀ t ≥ 0, MemLp (‖v · t‖) 2
  globally_bounded_energy : ∃ E, ∀ t ≥ 0, (∫ x : ℝ^n, ‖v x t‖ ^ 2) < E

structure NavierStokesExistenceAndSmoothnessPeriodic ... extends NavierStokesExistenceAndSmoothness nu u₀ f v p where
  isOnePeriodic_velocity : ∀ t ≥ 0, IsOnePeriodic (v · t)
  isOnePeriodic_pressure : ∀ t ≥ 0, IsOnePeriodic (p · t)
```

and the data conditions `InitialVelocityConditionDecay` (smooth, divergence-free, every derivative decays faster than any polynomial: `∀ m K, ∃ C, ∀ x, ‖iteratedFDeriv ℝ m u₀ x‖ ≤ C / (1 + ‖x‖) ^ K`), `ForceConditionDecay` (smooth on ℝ³ × [0,∞) with the analogous joint space-time decay `C / (1 + ‖x‖ + t) ^ K`), and the periodic versions (1-periodic in each coordinate, force decaying in time only).

**Plain-English reading.**

* *Which Clay alternatives.* Exactly (C) and (D) of Fefferman's official statement, in the Formal Conjectures encoding: for every viscosity ν > 0 there exist smooth initial data u₀ and a smooth forcing f satisfying Fefferman's decay/periodicity hypotheses such that **no** pair (v, p) exists that is C^∞ on ℝ³ × [0,∞), solves the equation pointwise, has the right initial data, and (for (C)) has uniformly bounded kinetic energy, or (for (D)) is 1-periodic in space (pressure too, per the Clay errata). The theorems are *statements of non-existence*: `¬ (∃ v p, …)`. There is no blowup time in the exported statement.
* *Equation form.* Classical pointwise solutions. `derivWithin (v x ·) (Set.Ici 0) t` is the one-sided time derivative on [0,∞); the nonlinearity is `fderiv ℝ (v · t) x (v x t)`, i.e. (v·∇)v as the spatial Fréchet derivative applied to v; `Δ` is Mathlib's Laplacian notation; the pressure enters as `gradient (p · t) x`. Everything is Frechet-differentiable-everywhere smooth; no weak, mild, or Leray–Hopf notion appears in the statement. Function spaces: C^∞ jointly in (x, t) on ℝ³ × [0,∞) (`ContDiffOn ℝ ∞ (↿v) (univ ×ˢ Ici 0)`), L² in space at each time (`MemLp (‖v · t‖) 2`), plus the uniform energy bound.
* *The force is part of the statement and is essential.* The theorems quantify existentially over f, exactly as Clay's (C)/(D) allow. In the proof the initial datum is chosen to be **identically zero** (`refine ⟨fun _ => 0, toComparator (rescaledForce ν f), …⟩` in `ComparatorR3Theorem.lean` and `ComparatorTheorem.lean`): the entire blowup is driven by the forcing. Viscosity is normalized to one internally and the general ν is obtained by the time-and-amplitude rescaling `rescaledForce ν f = fun z => ν ^ 2 • f (ν * z.1, z.2)` (`ComparatorBridge.lean` lines 61–65), so the constructed force for viscosity ν is ν² f(νt, x); the space variable is not rescaled (it cannot be on the unit torus). The constructed force has compact support in time (`CompactFutureTimeSupport`, `ProblemStatement.lean` line 89) — it is switched off after a finite time — and, for (C), compact support in space as well (`R3CompactCandidate`).
* *How "¬∃" is actually proved: a candidate with unbounded speed at t = 1, plus uniqueness.* The internal object is `ProblemStatement.CandidateProperties u p f` (`NavierStokes/ProblemStatement.lean` lines 101–117): a viscosity-one velocity/pressure/force triple, smooth on the pre-singular domain [0,1) × ℝ³, 1-periodic, zero initial velocity, solving `navierStokesResidual u p t x = f (t, x)` for 0 < t < 1, with `speed_unbounded : SpeedUnboundedAtOne u`, where
  ```lean
  def SpeedUnboundedAtOne (u : VelocityField) : Prop :=
    ∀ M : ℝ, 0 < M → ∀ δ : ℝ, 0 < δ →
      ∃ t : ℝ, ∃ x : Space, t ∈ Ioo 0 1 ∧ 1 - δ < t ∧ M < ‖u (t, x)‖
  ```
  So the blowup is *encoded as a blowup time* (t = 1, in the ν = 1 normalization) inside the proof, and then converted to the Clay-style non-existence by a uniqueness argument: `MaximalLifespan.candidate_excludes_global_solution` (`MaximalLifespan.lean` line 237, "An actual `CandidateProperties` witness has maximal classical lifespan one. The proof uses the proved periodic uniqueness theorem and a compactness bound for a continuous periodic field across time one") for (D), and `compact_candidate_excludes_global_solution` in `R3FiniteEnergyComparison.lean` (line 37) for (C), which uses a whole-space finite-energy uniqueness theorem (`R3/WholeSpaceUniqueness.lean`, proved through Fourier/heat-kernel/Riesz-transform pressure recovery — see 1(f)). In words: any hypothetical global smooth solution with the same data would agree with the candidate on [0,1) by uniqueness; the candidate's speed is unbounded as t → 1⁻; but a global smooth periodic (resp. finite-energy) solution is bounded on the compact slab [0,1] × torus (resp. controlled by the energy bound); contradiction.
* *The candidate itself.* The existential `candidateStatement` (`ProblemStatement.lean` line 120, still labeled "OPEN target" in a module doc written before it was proved) is discharged by `ActualCandidateAssembly.selected_candidate` (`ActualCandidateAssembly.lean` line 1183, a 1,187-line file importing fifteen "Actual…" modules). The construction vocabulary in the module docs — "correction cycles", "primary pulse", "outgoing entrance cone", "five-row mean update", "transition ramp", "wave covariance", "slow Borel base" — describes an iterated forced construction on the torus; the module docs consistently disclaim anything not proved in that file ("No cone inequality is assumed here", "does not assert arbitrary-power alias decay", "No solution or energy estimate is assumed").

**Euler, `Euler/Solution.lean` lines 33–38 and 43–69** (75-line file; lines 73 and 75 are `#print axioms`):

```lean
theorem euler_breakdown_R3 :
    ∃ u₀ : ℝ³ → ℝ³, InitialVelocityConditionDecay u₀ ∧
      ¬ (∃ v p, EulerExistenceAndSmoothnessR3 u₀ v p) := by
  exact ⟨initialDatum.field,
    initialVelocityConditionDecay_of_compact initialDatum.field initialDatum.smooth
      initialDatum_compact initialDatum_divergence, initialDatum_no_global_solution⟩

theorem exists_compact_smooth_euler_singularity :
    ∃ (u₀ : ℝ³ → ℝ³) (Tstar : ℝ) (v : ℝ³ → ℝ → ℝ³) (p : ℝ³ → ℝ → ℝ),
      InitialVelocityConditionDecay u₀ ∧ HasCompactSupport u₀ ∧ u₀ ≠ 0 ∧
      0 < Tstar ∧ Tstar ≤ 1 ∧
      EulerSobolevExistenceAndSmoothnessR3On (Ico 0 Tstar) u₀ v p ∧
      (∃ E : ℝ, ∀ t ∈ Ico (0 : ℝ) Tstar, (∫ x : ℝ³, ‖v x t‖ ^ 2) < E) ∧
      (∀ T : ℝ, 0 < T →
        ((∃ w q, EulerSobolevExistenceAndSmoothnessR3On (Icc 0 T) u₀ w q) ↔ T < Tstar)) ∧
      (∀ T ∈ Ioo 0 Tstar,
        (⨆ t ∈ Icc (0 : ℝ) T, velocityC1Norm (v · t)) < ⊤ ∧
        (∫⁻ t in Ico (0 : ℝ) T, vorticityNorm (v · t)) < ⊤) ∧
      Filter.limsup (fun t : ℝ => velocityC1Norm (v · t)) (𝓝[<] Tstar) = ⊤ ∧
      (∫⁻ t in Ico (0 : ℝ) Tstar, vorticityNorm (v · t)) = ⊤ ∧
      ¬ (∃ w q, EulerExistenceAndSmoothnessR3 u₀ w q) := by
  refine ⟨initialDatum.field, lifespan.duration, maximalVelocityExtension lifespan,
    maximalPressureExtension lifespan, ?_, initialDatum_compact, initialDatum_nonzero,
    lifespan.duration_pos, lifespan_le_one, maximal_sobolevSolution lifespan,
    maximalVelocityExtension_bounded_energy lifespan, ?_, ?_,
    maximalVelocityExtension_c1_limsup lifespan,
    maximalVelocityExtension_vorticity_integral lifespan, initialDatum_no_global_solution⟩
  ...
```

*Plain-English reading.* `euler_breakdown_R3` is the Clay (C) template with ν = 0 and f = 0: there is a smooth, divergence-free, rapidly decaying (in fact compactly supported) u₀ such that no global classical solution of unforced Euler with uniformly bounded energy exists. **Unlike the Navier–Stokes theorems, no force is involved**, and the datum is nonzero. The second theorem is the quantitative singularity: a maximal lifespan T* ∈ (0, 1]; a solution on [0, T*) in an "all-order Sobolev" class (`SobolevSmoothOn`: every spatial derivative tensor is in L² and depends continuously on time in L², with the Euler equation holding with a strong L²-time-derivative witness — see the challenge file lines 108–160); solutions on closed intervals [0, T] exist *exactly* for T < T* (this is the maximality clause, an if-and-only-if); the C¹ norm and ∫‖ω‖_∞ are finite on every [0, T] with T < T* and the limsup of the C¹ norm and the full vorticity integral are infinite at T* (Beale–Kato–Majda-type blowup; the proof file `CompactVorticityContradiction.lean` says "The contradiction uses the proved Beale--Kato--Majda integral criterion", and `Euler/OrdinaryEulerBKM.lean` exists). Here "no global smooth solution" is stated both as a blowup time (T*) and as `¬∃`. The suprema are ℝ≥0∞-valued so "unbounded" is literally `= ⊤`.

### 1(d) Trust audit

Greps over every `.lean` file outside `.lake/` (2,486 files, 616k lines). Results:

| Pattern | Count | Where |
|---|---|---|
| `sorry` | 5 | All in `ComparatorChallenges/` — one in a comment, four are the intentional placeholders (`NavierStokes.lean:277,284`, `Euler.lean:88,184`). **Zero in `NavierStokes/` and `Euler/`.** |
| `axiom` (as declaration, `^axiom`) | 0 | The word occurs 4 times, all in prose comments ("not an axiom or a proved theorem", "not postulated as an inverse axiom", "`Quot.sound` occur in its axiom dependencies"). |
| `native_decide` | 0 | — |
| `decide` | 201 | All `by decide` on tiny closed goals (`(2 : ℕ) ≠ 0`, `1 ≤ 2`, `Fin` inequalities); kernel-checked, harmless. No `decide +kernel` on large literals. |
| `unsafe`, `implemented_by`, `@[extern`, `partial def`, `opaque` (decl), `@[csimp]` | 0 | `opaque` appears once in a comment. |
| `set_option maxHeartbeats` | 5 | Values 3200000 (×3), 1800000, 1000000. No other `set_option` at all. |
| `Classical.choice` / `Classical.choose` | 150 / 128 | In defs and proofs (noncomputable choices, `#print axioms` expectations); Comparator permits `Classical.choice`. No statement-level dependence beyond the standard three axioms is claimed. |
| `#print axioms` | 4 | End of the two solution files (statements will print at build time). |
| `#eval`/`#check`/`#guard` | 0 | — |
| `noncomputable` | 8,285 | Everything analytic is noncomputable, as expected. |
| `admit`, `sorryAx`, `ofReduceBool`, `lcProof`, `trustCompiler` | 0 | — |

**Independence of the statement from the proof.** The solution modules never import the challenge module (`ComparatorSolution.lean` line 8: "The adapters import `ComparatorDefinitions`, never the challenge module"; `Euler/Solution.lean` line 11: "Its definitions come from `SolutionDefinitions`, never from the reference module"). I confirmed by `diff -w` that `NavierStokes/ComparatorDefinitions.lean` equals the challenge file minus the two theorems, and `Euler/SolutionDefinitions.lean` equals the Euler challenge minus its two theorems and the connecting prose. One detail worth noting: `Euler/Solution.lean` line 41 sets `attribute [local instance] CompletePartialOrder.toSupSet` "to match the reference's elaboration of ENNReal suprema independently of import order" — a reminder that "same statement text" and "same elaborated term" are different things, and Comparator checks the latter.

**What `formalization.yaml` declares** (full text in §1(d-ii) above): schema v0.4 of the mathlib-initiative `formalization.yaml`; author "OpenAI"; two source "articles" by OpenAI (no arXiv ids, no venue); `related_formalizations: builds-on` the DeepMind Formal Conjectures NS statement; MSC 35Q30/35Q31; `sorry_count: 0` for the four main results, each with axioms `[propext, Classical.choice, Quot.sound]` and a Comparator config; **`automation.methods: agent`, models `GPT-6 Astra`, framework `Codex`**; **`review.status: self-assessed`**; an `alignment` block mapping "Theorem 1.1 (Navier–Stokes on ℝ³)", "Corollary 10.6 (Navier–Stokes on ℝ³/ℤ³)", "Theorem 1.1 (Euler)" and "Theorem 1.1 (Euler), alternate version" to the four Lean names. So the yaml is explicit that (i) the code was produced by an agent swarm, (ii) nobody outside OpenAI has reviewed it, and (iii) the claim of correctness rests on the Comparator run plus the standard-axiom printout.

**What I verified locally** (Lean toolchain `v4.34.0-rc2` was already installed; Mathlib cache for the pinned revision fetched into the scratch clone in ~11 s after a first 7.8 GB download):

* `lake build ComparatorChallenges` — both challenge modules elaborate against Mathlib only, 25 s each, with exactly the four expected `declaration uses 'sorry'` warnings (`NavierStokes.lean:273:8`, `:280:8`; `Euler.lean:85:8`, `:170:8`).
* `lake build NavierStokes.ComparatorDefinitions Euler.SolutionDefinitions NavierStokes.ProblemStatement` — 7.5 s, no warnings. So the solution-side statement layer compiles as written.
* Two small-closure proof modules (`NavierStokes.R3.WeakFourierUniqueness`, closure 8 modules / 1,689 lines; `NavierStokes.WeightedODEJets`, 8 modules / 2,959 lines) built cleanly in 10 s and 14 s wall, ~1.5–3.5 s per module. See §4 for the extrapolation; a full build was not attempted.

I did **not** run Comparator (needs `landrun`, `lean4export`, `nanoda_bin`, and the full build). The trust chain therefore stands as: OpenAI's self-assessment + the source-level greps above + local elaboration of the statement layer.

### 1(f) Structure of the proof

**Layering.** Two flat libraries, `NavierStokes` (643 modules, 580 of them in the import closure of the exported theorems) and `Euler` (1,839 modules, 1,829 in the closure), with `import` depth 59 (NS) and 97 (Euler). 63 `NavierStokes` modules (24,702 lines) and 10 `Euler` modules are shipped but unreachable from the exported theorems — many are named `…NoOptions` or `…Investigation` (`CorrectionInitializationNoOptions`, 5,573 lines, a near-duplicate of `CorrectionInitialization`; `LpCylinderCoefficientTimeInvestigation`), and a whole abandoned first attempt at the R³ pressure theory lives at top level as `NavierStokes/R3PressureKernel.lean`, `R3RieszKernel.lean`, `R3WeakPressure.lean`, … (37 unused `R3*` files) while the live version is in the subdirectory `NavierStokes/R3/` (92 files). That is a swarm signature: parallel attempts were left in the tree rather than pruned.

The NS development, read from the module docs and file names, is organized as:

1. *Statement layer* — `ProblemStatement.lean` (Space = `EuclideanSpace ℝ (Fin 3)`, SpaceTime = ℝ × Space, the differential operators as explicit `fderiv` expressions, `CandidateProperties`, `SpeedUnboundedAtOne`); `ComparatorDefinitions.lean`; the bridges `ComparatorBridge.lean` (operator translations `divergence_eq`, `gradient_eq`, `laplacian_eq`, `temporalDerivative_eq`, viscosity rescaling), `ComparatorTheorem.lean` (D), `ComparatorR3Theorem.lean` (C), `ComparatorSolution.lean`.
2. *Construction of the periodic candidate* — the "Actual…" family: `ActualCandidateAssembly` ← `ActualCandidateConstruction`, `InitialPhysicalData`, `ActualPhysicalStageBounds`, `GermCandidateAssembly`, `ActualValidBandWaves`, `ActualMeanExterior`, …; the iteration machinery `CorrectionStep` (9,849 lines, "Exact field bookkeeping for one correction cycle"), `CorrectionInitialization`, `ActualCycleParameters`, `MeanRankUpdate` ("the physical five-row mean update"), `VariableGaugeMean`, `TransitionRamp`, `OutgoingEntranceCone`, `ActivationContinuation`, `NominalProfile`, `ParticularWaveBounds` ("Volterra solution"), `PrimaryPulseBounds`, `BaseResidual` ("locally finite series in `SlowBorelBase`").
3. *Analysis inputs* — ODE/propagator files (`TangentODE`, `ParametricODE`, `ViscousPropagator`, `SmoothPathFamily`, `WeightedODEJets`, `MovingFrameODE`), heat kernel files (`HeatTailEdit`, `ParametricHeatTail`), Fourier aliasing on the torus (`FourierAlias`, `TorusAverages`, `PhaseEstimates`), weighted classes (`WeightedClasses`, `WeightedSobolev`, `WeightedInterpolation`), harmonic/axis analysis (`HarmonicFields`, `AxisHolomorphicJoint`, `NaturalAxisBridge`).
4. *Uniqueness and lifespan* — `PeriodicIntegration`, `PeriodicUniqueness`, `MaximalLifespan` (292 lines) for the torus; for ℝ³ the subdirectory `R3/` (heat kernel Fourier representation `HeatKernelFourier`, `RieszHeatRepresentation`, `RieszL2Bounds`, `SchwartzParseval`, `PressureRecovery`, `LocalizedDifferenceEnergy`, `ComparisonGronwall`, `WholeSpaceUniqueness`, `WeakFourierUniqueness`) and `R3CompactCandidate`, `R3FiniteEnergyComparison`.

The Euler library is organized around a "packet induction" (`EulerPacketInduction` namespace; `Packet*` ≈ 200 files, `Mean*`, `Transverse*`, `TimeH1*`, `TimeLp*`, `Sobolev*`, `Gevrey*`, `Hilbert*`) and closes with `EulerFiniteLifespan`, `OrdinaryEulerBKM`, `OrdinaryMaximalVorticityIntegral`, `CompactVorticityContradiction`, `ComparatorMaximalSolution`, `ComparatorSingularityNorms`. Its single giant file `EulerProof.lean` (20,755 lines, 983 theorems) is, despite the name, "Explicit numerical estimates for the factorial majorants used in the proposed Euler construction. These lemmas prove combinatorial implications; they do not assert the analytic estimates" — i.e. a library of binomial/factorial inequalities (`le_choose_of_interior`, `sum_inv_choose_le_three`, `majorant_convolution`, …), which explains why it is imported by 32 other modules.

**Mathlib areas used** (identifier counts over `NavierStokes/` + `Euler/`): `ContDiff`/`ContDiffOn` 14.7k + 4.8k, `iteratedFDeriv` 5.9k, `fderiv` 5.2k, `deriv`/`HasDerivAt` 15.8k + 2.1k, `MeasureTheory` 1.4k, `integral` 4.9k, `MemLp` 1.0k, `Lp` 7.7k, `Fourier` 1.4k (torus aliasing in NS, the R³ heat-kernel/Riesz uniqueness), `SchwartzMap` 150, `Convolution` 1.2k, `Laplacian` 1.4k, `Gronwall` 47, `Lipschitz` 170, `Polynomial` 1.8k, `Complex` 3.1k (NS only — the "axis holomorphic" files), `Matrix` 1.4k, `Sobolev` 6.3k (a project-defined word: `SobolevSpace`, `SobolevWord`, `SobolevEdge`, `ordinarySobolev` — Mathlib has no Sobolev spaces, so the Euler project builds its own all-order L² jet class), `ENNReal`/`NNReal` 1.6k. There is no use of Mathlib's ODE existence theory (`ODE`/`gronwall` 0 hits as Mathlib names) — the ODE/Volterra solutions are built in-house as explicit integrals. Imports are granular (`import Mathlib.Analysis.Calculus.…`, 838 distinct imports in NS, 2,018 in Euler); only 10 Euler files `import Mathlib` wholesale.

**Numerics.** The NS/Euler development contains essentially **no interval arithmetic and no external computation**. Large numeric literals (298 occurrences of ≥5-digit numerals, the common ones being 10⁵, 10⁶, 2·10⁵, 3·10⁷, 4·10⁸, 10⁹) are *generous slack constants in inequalities*, e.g. `def neighborStabilityConstant : ℝ := 1000000000*exp 6` (`Euler/PacketNeighborControlled.lean:154`) and `|V t-Z t|+|U t+Z₁ t| ≤ 400000000*e*Θ^29*(1+lam)*F t`. They are discharged by `norm_num` (4,574 uses), `positivity` (3,560), `nlinarith`/`linarith` (2,496/5,208), `field_simp`, `ring`, and `exp_le_exp`/`Real.add_one_le_exp` (187/15) — never by a certified numerical table. Nothing is admitted by an axiom; no lemma is "assumed" — the module docs go out of their way to say what is *not* assumed ("is not assumed" ×15, "does not assert" ×14, "not asserted" ×6, "not silently included as proved consequences").

**Tactic profile** (NS / Euler): `simp` 9,965 / 4,076 (`simp only` 6,113 / 2,273), `rw [` 15.6k / 7.4k, `exact` 16.7k / 7.1k, `simpa` 4.5k / 2.5k, `refine` 3.0k / 0.5k, `calc` 1.5k / 0.8k, `linarith` 3.9k / 1.3k, `nlinarith` 1.4k / 1.1k, `norm_num` 3.1k / 1.5k, `positivity` 1.8k / 1.8k, `ring` 4.0k / 1.2k, `omega` 713 / 1,958, `field_simp` 867 / 255, `gcongr` 111 / 226, `fun_prop` 98 / 60, `continuity` 86 / 115, `measurability` 10 / 3, `convert` 599 / 280, `by_contra` 498 / 51, `linear_combination` 48 / 11; **`aesop` 0, `polyrith` 0, `grind` 0, `exact?`/`apply?` 0, `interval_cases` 0/1, `decide +kernel` 0**. Declarations: 26,073 + 11,228 `theorem`s (only 29 `lemma`s in total — the swarm writes `theorem`), 7,232 + 3,287 `def`s, 497 + 130 `structure`s. Average 15.5 (NS) and 18.8 (Euler) lines per theorem; the longest single proof I found in the two largest files is 125–144 lines. Documentation: 7,108 + 4,975 docstrings, 1,498 + 1,886 module-doc blocks, and **only 24 line comments (`--`) in 616k lines** — every explanation is a docstring or a module doc, none is an inline remark, which is an unmistakable machine signature (a human leaves `-- TODO`, `-- see paper (3.4)`; the swarm was evidently instructed to document declarations and forbidden from leaving loose comments).

## 2. tristanbuckmaster/fluid_lean (Alpöge–Buckmaster; Lean code written by Claude)

**Correction to the brief.** The repository does not contain a porous-medium project. It holds three Lake projects — `affinecore/` (forced 2D inviscid Boussinesq, gradient blowup with bounded temperature, from explicit odd data), `boussinesq-blowup/` (forced 2D inviscid Boussinesq, every buoyancy κ > 0), and `euler-blowup/` (forced 3D incompressible Euler, obtained from the planar Boussinesq mechanism through an axisymmetric "ring" lift) — and no README at the top level. The most important single fact about it, stated in every README and every `formalization.yaml`: *"all Lean code in this directory, the trusted statement file `Challenge.lean` included, was written by Claude (Anthropic) under the direction of Levent Alpöge, who wrote no Lean by hand"*. The NOTICE files carry "Copyright 2026 Anthropic, PBC". So the contrast the brief asked for — human-led versus swarm-produced — is really *Claude under one mathematician's direction, with a Comparator-style trusted statement file the mathematician reads* versus *a Codex/GPT-6 swarm with self-assessed review*. Both codebases are machine-written.

### 2(a) READMEs, verbatim (the three project READMEs; there is no root README)

```markdown
# Finite-time gradient blow-up for the forced two-dimensional inviscid Boussinesq system — Lean 4 formalisation

This repository contains a Lean 4 / Mathlib proof of the theorem stated below. The proof is complete: no file other
than the trusted statement file [`Challenge.lean`](Challenge.lean) contains a `sorry` (that file states the theorem with a
placeholder proof, as the comparator tool's standard Challenge/Solution layout requires), and the proof rests on no axiom beyond Lean's standard
three (`propext`, `Classical.choice`, `Quot.sound`). `Challenge.lean` is the only file a reader must trust;
[comparator](https://github.com/leanprover/comparator) is configured (`comparator.json`) to check the proof against it.

> Research artifact. Not maintained; issues are welcome, pull requests are not accepted.

## The theorem

Write ℝ² with coordinates (x₁, x₂), the direction of x₂ being the direction of gravity. The two-dimensional inviscid
Boussinesq system with buoyancy constant 1 and forcing (f_θ, f_u) for a temperature θ, a velocity u and a pressure p is
∂ₜθ + (u·∇)θ = f_θ, ∂ₜu + (u·∇)u + ∇p = θ e₂ + f_u, div u = 0.

**Theorem.** For every real A₀ ≥ 1 and every radial smooth compactly supported cut-off χ₀ : ℝ² → ℝ equal to 1 on the
open ball of radius 2 about the origin, there exist a finite time T > 0, forcing terms f_θ, f_u and a classical solution
(θ, u, p) of finite energy on [0, T) × ℝ² of the Boussinesq system with buoyancy constant 1, with the following properties, every time t
below ranging over the half-open interval [0, T). θ(t), u(t) and the forces are odd under x ↦ −x; the initial temperature
is θ(0, x) = −(A₀/N₀) sin(N₀ x₂) χ₀(x) with N₀ = ⌈(√A₀)/2⌉ and the initial velocity is zero, both initial data compactly supported; the forces are C^∞ on
[0, T) × ℝ² with every mixed space–time derivative bounded there (derivatives taken within [0, T) × ℝ², hence one-sided
at t = 0); one fixed ball contains the supports of θ(t), of the vorticity curl u(t) and of both forces for every t; u(t) is
the Biot–Savart velocity of its vorticity through the logarithmic kernel, and the pressure vanishes at the origin; the
temperature stays bounded on [0, T) × ℝ² while the supremum norm of its gradient tends to +∞ as t ↑ T, and the supremum
norm of the vorticity has limes superior +∞ as t ↑ T; and on every [0, T′] with 0 < T′ < T the pair (θ, u) belongs to the
finite-energy Lipschitz class defined with these forces (momentum equation in weak, pressure-free form) and is the only
member of that class with its initial values.

In words: for explicit odd initial temperature data and zero initial velocity there are a finite time T and a smooth,
compactly supported forcing with every derivative bounded up to T which together produce a classical solution of the
forced planar Boussinesq system whose temperature stays bounded while its gradient blows up at time T, the solution being
unique in the natural strong class on every shorter interval. The precise content is the proposition
`AffineCore.External.Theorem1` defined in `Challenge.lean`, phrased over the library module `AffineCore/Statement/External.lean`'s
own copies of seven library definitions (the logarithmic kernel and potential, the Biot–Savart velocity and the datum),
identical in text to the originals and placed in one file because the comparator compares auxiliary-lemma names, which
Lean assigns per file; the library also proves an internal form of the theorem carrying
the staircase of stage times and amplitudes, of which the statement above is a corollary.

## Building and checking

Toolchain: `leanprover/lean4:v4.32.2`. Mathlib is pinned in `lake-manifest.json` (commit
`81a5d257c8e410db227a6665ed08f64fea08e997`, Mathlib's tag `v4.32.0`) together with its own dependencies. Do not run `lake update`.

```
lake build                               # Mathlib publishes no prebuilt objects for Lean 4.32.2, so Mathlib is compiled
                                         # from source, then the vendored planar library, then this project
lake env lean scripts/PrintAxioms.lean   # prints the axioms of the main theorem
```

Expected: no errors; exactly one `declaration uses 'sorry'` warning, from `Challenge.lean` (the placeholder statement
file), and none from `AffineCore/`, `vendor/` or `Solution.lean`; every line of the axiom printout reads
`[propext, Classical.choice, Quot.sound]`. The build is large (about 1,100 modules in this project plus the vendored planar library); with Mathlib's
objects already built, this project's 1,113 modules compiled in about nine minutes on a 32-core machine once Mathlib and the vendored library had been built, and the
stock toolchain `leanchecker` replayed all modules in the main theorem's closure in about thirty-five minutes; Mathlib
itself must first be compiled from source for this toolchain (plan for a machine with on the order of 100 GB of memory and
a few hours at two dozen parallel jobs rather than a laptop).

`Challenge.lean` states the theorem using Mathlib only; `Solution.lean` proves that statement from the library's main
theorem; `comparator.json` is the configuration for [comparator](https://github.com/leanprover/comparator), which
type-checks the statement file independently, checks that the solution inhabits exactly that statement, restricts axioms
to the standard three, and replays the proof.

## Layout

- `AffineCore/` — the construction (a protocol of planted temperature layers and its cascade) and its analysis: the
  statement layer `AffineCore/Statement/`, the framework and construction libraries, the leaf contracts
  `AffineCore/Leaves/`, and one closed proof unit per leaf under `AffineCore/Proofs/`, assembled into the main theorem in
  `AffineCore/Proofs/R01/`. The modules shipped here are exactly those that `Solution.lean`
  transitively imports (1,113 of them); the development tree in which the proof was written is larger.
- `vendor/ChainPlanar/` — supporting modules from a planar fluid-mechanics library built by the same project on top of
  Mathlib (plane vector calculus, the logarithmic Newton potential and Biot–Savart law, a Calderón–Zygmund core with
  Bogovskiĭ-type right inverses, elliptic regularity lemmas, smooth compactly supported forcing and the finite-energy
  Lipschitz uniqueness class, transport and ODE toolkits, and that library's statement objects as definitions), included
  byte for byte as a build arrangement; only the modules this proof imports are shipped (each with its own proofs); the proof of that library's main theorem is not.
- `Challenge.lean`, `Solution.lean`, `comparator.json` — statement, solution bridge, comparator configuration
  (the comparator tool's standard Challenge/Solution layout); `scripts/PrintAxioms.lean` prints the axioms.

Authorship: all Lean code in this directory, the trusted statement file `Challenge.lean` included, was written by
Claude (Anthropic) under the direction of Levent Alpöge, who wrote no Lean by hand. `Challenge.lean` has not yet been read against the
theorem stated above by the responsible maintainer; `formalization.yaml` (`automation`, `review`) records the same
account and will be updated after that read.

## Licence

Apache License 2.0; see `LICENSE` and `NOTICE`.

```

```markdown
# Finite-time blow-up for the planar inviscid Boussinesq equations with smooth force — Lean 4 formalisation

This repository contains a Lean 4 / Mathlib proof of the theorem stated below. The proof is complete: no file other
than the trusted statement file [`Challenge.lean`](Challenge.lean) contains a `sorry` (that file states the theorem with a
placeholder proof, as the comparator / Palomar template requires), and the proof rests on no axiom beyond Lean's standard
three (`propext`, `Classical.choice`, `Quot.sound`). `Challenge.lean` is the only file a reader must trust;
[comparator](https://github.com/leanprover/comparator) checks the proof against it.

> Research artifact. Not maintained; issues are welcome, pull requests are not accepted.

## The theorem

**Theorem.** For every κ > 0 there exist T > 0, maps θ, p, f_θ : ℝ × ℝ² → ℝ and u, f_u : ℝ × ℝ² → ℝ² with the
following properties, every time t below ranging over the half-open interval [0, T). θ, u and p are C^∞ on
[0, T) × ℝ², u(t, ·) is divergence-free, u(t, ·) and θ(t, ·) are square-integrable, and the two equations
∂ₜθ + u·∇θ = f_θ and ∂ₜu + (u·∇)u + ∇p = κ θ e₂ + f_u hold at every point (the time derivative is taken within
[0, ∞), hence one-sided at t = 0); at every t the pair (θ(t, ·), u(t, ·)) is odd under x ↦ −x, that is
θ(t, −x) = −θ(t, x) and u(t, −x) = −u(t, x), and the forcing pair (f_θ(t, ·), f_u(t, ·)) is odd in the same sense;
θ(0, ·) and u(0, ·) have compact support; f_θ and every component of f_u are C^∞ on [0, T) × ℝ² with every mixed
space–time derivative bounded there, and vanish outside a fixed ball; there is a function g with g(t) → +∞ as t ↑ T
such that at every t the gradient of θ satisfies ‖∇θ(t, x)‖ ≥ g(t) at some point x — in particular
‖∇θ(t, ·)‖_∞ → ∞; θ itself stays bounded, in the sense that there is a single M with |θ(t, x)| ≤ M at every t and
every x; for every M there are times t arbitrarily close to T — frequently as t ↑ T — at which the vorticity
ω = ∂₁u₂ − ∂₂u₁ satisfies |ω(t, x)| ≥ M at some point x, so that ‖ω(t, ·)‖_∞ is unbounded near T in the limsup
sense; and for every T′ with 0 < T′ < T, the pair (θ, u) belongs on [0, T′] to the finite-energy Lipschitz class
for κ and the forces (f_θ, f_u) (pairs (θ, u) locally Lipschitz on [0, T′] × ℝ² with
sup_t (‖θ(t)‖_{L²} + ‖u(t)‖_{L²}) < ∞ and sup_t (‖∇θ(t)‖_{L^∞} + ‖∇u(t)‖_{L^∞}) < ∞, with u divergence-free almost
everywhere at every time, satisfying the transport equation for θ almost everywhere on [0, T′] × ℝ² and the momentum
equation with buoyancy κ θ e₂ and force f_u in weak, pressure-free form) and every member (θ′, u′) of that class with
the same initial temperature and velocity coincides with (θ, u) on [0, T′].

In words: for each buoyancy constant κ > 0 there exist a time T > 0, smooth compactly supported finite-energy
initial data odd under x ↦ −x, and smooth forces vanishing outside a fixed ball with every derivative bounded up to
time T, which together produce a classical solution of the planar inviscid Boussinesq system on [0, T) × ℝ² that is
unique in the natural strong class on every shorter interval, whose temperature remains bounded while its gradient
becomes unbounded as t ↑ T, and whose vorticity is unbounded along a sequence of times approaching T.

## Building and checking

Toolchain: `leanprover/lean4:v4.32.2`. Mathlib is pinned in `lake-manifest.json` (commit
`81a5d257c8e410db227a6665ed08f64fea08e997`) together with its own dependencies. Do not run `lake update`.

```
lake build                               # Mathlib publishes no prebuilt objects for Lean 4.32.2 (= 4.32.0 plus two kernel
                                         # soundness fixes), so Mathlib is compiled from source, then this project
lake env lean scripts/PrintAxioms.lean   # prints the axioms of the main theorem and of the library theorem it is derived from
```

Expected: no errors; exactly one `declaration uses 'sorry'` warning, from `Challenge.lean` (the placeholder statement
file), and none from `BoussinesqBlowup/`, `vendor/` or `Solution.lean`; every line of the axiom printout reads
`[propext, Classical.choice, Quot.sound]`. The build is large (about 1,500 modules); plan for a machine with on the
order of 150 GB of memory and a couple of hours at three dozen parallel jobs rather than a laptop.

`Challenge.lean` states the theorem using Mathlib only; `Solution.lean` proves that statement from the library's main
theorem `BoussinesqBlowup.Num.Cert.theorem01`; `comparator.json` is the configuration for
[comparator](https://github.com/leanprover/comparator), which type-checks the statement file independently, checks that
the solution inhabits exactly that statement, restricts axioms to the standard three, and replays the proof.

## Layout

- `BoussinesqBlowup/` — the construction and its analysis (1,413 modules), and under `BoussinesqBlowup/Num/Cert/`
  some 1,200 machine-generated interval-arithmetic certificate modules, each an inequality between explicit rationals
  decided by the kernel; the fixed-point arithmetic they use is itself proved sound in Lean.
- `vendor/cm24-r2/` — a self-contained supporting library (kernel estimates, transport, uniqueness; 35 modules and a
  root import file `Cm24.lean`) built by this project on top of Mathlib and included as a build arrangement.
- `Challenge.lean`, `Solution.lean`, `comparator.json` — statement, solution bridge, comparator configuration
  (Palomar template layout); `scripts/PrintAxioms.lean` prints the axioms.

Authorship: all Lean code in this directory, the trusted statement file `Challenge.lean` included, was written by
Claude (Anthropic) under the direction of Levent Alpöge, who wrote no Lean by hand and is to read `Challenge.lean` against
the theorem stated above before release. `formalization.yaml` (`automation`, `review`) records the same account.

## Licence

Apache License 2.0; see `LICENSE` and `NOTICE`.

```

```markdown
# Finite-time blow-up for the three-dimensional incompressible Euler equations with smooth force — Lean 4 formalisation

This repository contains a Lean 4 / Mathlib proof of the theorem stated below. The proof is complete: no file other
than the trusted statement file [`Challenge.lean`](Challenge.lean) contains a `sorry` (that file states the theorem with a
placeholder proof, as the comparator / Palomar template requires), and the proof rests on no axiom beyond Lean's standard
three (`propext`, `Classical.choice`, `Quot.sound`). `Challenge.lean` is the only file a reader must trust;
[comparator](https://github.com/leanprover/comparator) checks the proof against it.

> Research artifact. Not maintained; issues are welcome, pull requests are not accepted.

## The theorem

**Theorem.** There exist T > 0, maps u, f : ℝ × ℝ³ → ℝ³ and p : ℝ × ℝ³ → ℝ with the following properties,
every time t below ranging over the half-open interval [0, T). u and p are C^∞ on [0, T) × ℝ³, u(t, ·) is
divergence-free and square-integrable, and ∂ₜu + (u·∇)u + ∇p = f holds at every point (the time derivative is
taken within [0, ∞), hence one-sided at t = 0); u(0, ·) has compact support; every component of f is C^∞ on
[0, T) × ℝ³ with every mixed space–time derivative bounded there, and f vanishes outside a fixed ball; there is a
function g with g(t) → +∞ as t ↑ T such that at every t the vorticity ω = curl u satisfies ‖ω(t, x)‖ ≥ g(t) at some
point x — in particular ‖ω(t, ·)‖_∞ → ∞; for every M there exist T′ ∈ [0, T) and an integrable function h ≥ 0 on
[0, T′] such that at every s ∈ [0, T′] one has h(s) ≤ ‖ω(s, x)‖ at some point x, and ∫₀^{T′} h ≥ M — in particular
∫₀^T ‖ω(t, ·)‖_∞ dt = +∞; and for every T′ with 0 < T′ < T, u belongs on [0, T′] to the finite-energy Lipschitz
class (velocity fields locally Lipschitz on [0, T′] × ℝ³ with sup_t (‖u(t)‖_{L²} + ‖∇u(t)‖_{L^∞}) < ∞, divergence-free
almost everywhere, solving the momentum equation with force f in weak, pressure-free form) and every member of that
class with the same initial velocity coincides with u on [0, T′].

In words: there exist a time T > 0, smooth compactly supported finite-energy initial data, and a smooth force vanishing
outside a fixed ball with every derivative bounded up to time T, which together produce a classical solution of the
incompressible Euler equations on [0, T) × ℝ³ that is unique in the natural strong class on every shorter interval and
whose vorticity becomes unbounded as t ↑ T.

## Building and checking

Toolchain: `leanprover/lean4:v4.32.2`. Mathlib is pinned in `lake-manifest.json` (commit
`81a5d257c8e410db227a6665ed08f64fea08e997`) together with its own dependencies. Do not run `lake update`.

```
lake build                               # Mathlib publishes no prebuilt objects for Lean 4.32.2 (= 4.32.0 plus two kernel
                                         # soundness fixes), so Mathlib is compiled from source, then this project
lake env lean scripts/PrintAxioms.lean   # prints the axioms of the main theorem
```

Expected: no errors; exactly one `declaration uses 'sorry'` warning, from `Challenge.lean` (the placeholder statement
file), and none from `EulerBlowup/`, `vendor/` or `Solution.lean`; every line of the axiom printout reads
`[propext, Classical.choice, Quot.sound]`. The build is large (about 1,100 modules); plan for a machine with on the
order of 100 GB of memory and a few hours at two dozen parallel jobs rather than a laptop.

`Challenge.lean` states the theorem using Mathlib only; `Solution.lean` proves that statement from the library's main
theorem; `comparator.json` is the configuration for [comparator](https://github.com/leanprover/comparator), which
type-checks the statement file independently, checks that the solution inhabits exactly that statement, restricts
axioms to the standard three, and replays the proof.

## Layout

- `EulerBlowup/` — the construction and its analysis, and under `EulerBlowup/Num/` interval-arithmetic certificates,
  each an inequality between explicit rationals decided by the kernel; the fixed-point arithmetic they use is itself
  proved sound in Lean.
- `vendor/cm24-r2/` — a self-contained supporting library (kernel estimates, transport, uniqueness) built by this
  project on top of Mathlib and included as a build arrangement.
- `Challenge.lean`, `Solution.lean`, `comparator.json` — statement, solution bridge, comparator configuration
  (Palomar template layout); `scripts/PrintAxioms.lean` prints the axioms.

Authorship: all Lean code in this directory, the trusted statement file `Challenge.lean` included, was written by
Claude (Anthropic) under the direction of Levent Alpöge, who wrote no Lean by hand and read `Challenge.lean` against the
theorem stated above. `formalization.yaml` (`automation`, `review`) records the same account.

## Licence

Apache License 2.0; see `LICENSE` and `NOTICE`.

```

### 2(b) Size and history

Measured on the clone at the single commit `d012468` (2026-09-08), author `tristanbuckmaster <108429921+tristanbuckmaster@users.noreply.github.com>`, message "Add affinecore, boussinesq-blowup, and euler-blowup Lean projects". **One commit, one branch, no tags** — exactly like the OpenAI repository, and dated the same day. The development history ("the development tree in which the proof was written is larger", affinecore README) is not public.

| Project | `.lean` files | Lines | Vendored library | Toolchain / Mathlib |
|---|---|---|---|---|
| `affinecore/` | 1,117 | 298,129 | `vendor/ChainPlanar` (64 files, 53,975 lines, itself vendoring `cm24-r2`) | `leanprover/lean4:v4.32.2`, Mathlib `81a5d257…` (tag v4.32.0) |
| `boussinesq-blowup/` | 1,417 | 448,170 | `vendor/cm24-r2` (36 files, 36,547 lines) | same |
| `euler-blowup/` | 1,078 | 938,281 | `vendor/cm24-r2` (identical copy) | same |
| **Total** | **3,748** | **1,811,649** | | |

Largest files: `euler-blowup/EulerBlowup/Ring/S4r/TimeRates.lean` **101,042 lines** (1,780 theorems; longest single proof 908 lines), `Ring/S7r/LayerRows.lean` 66,278, `Ring/S6r/TheoremH.lean` 53,963, `Ring/S6r/BaseRun.lean` 39,547, `Ring/S7r/TimeRegularity.lean` 34,120, `Ring/S4r/Stage.lean` 32,177, `Ring/S7r/FanRing.lean` 28,463, `Ring/S4r/Recipe.lean` 26,275, `S7/TimeRegularity.lean` 22,267 (in both Euler and Boussinesq trees), `S6/TheoremH.lean` 21,024 (both). Average file size 870 lines in `euler-blowup`, 316 in `boussinesq-blowup`, 267 in `affinecore` — versus 610 (NS) and 115 (Euler) in the OpenAI repository.

**The Euler tree is the Boussinesq tree plus a 3D layer.** `diff -rq` shows the two planar skeletons (`S0`–`S7`, `D`, `E`, `L`, `Lit`, `Kit`, `Num`) share 998 file paths that differ *only by the namespace rename* (`sed s/EulerBlowup/BoussinesqBlowup/` makes `S7/TimeRegularity.lean` identical); the 184 files only in Boussinesq are extra numerical certificates (`Num/Cert/SB0…SB7`). On top of that, `euler-blowup/EulerBlowup/Ring/` (59 files, **541,216 lines**) and `Ring3D/` (12 files, 12,848 lines) carry the axisymmetric 3D Euler construction. Section-coded directory names (`S2`, `S31`, `S32a`, `S32b`, `S33`, `S4` in `Cm24`; `S0`–`S7` and `S4r`, `S6r`, `S7r` in the projects; leaves `R01`–`R09`; `L320.lean` = Lemma 3.20) show the Lean tree mirrors a manuscript's section structure — the manuscripts are "in preparation (2026)" with titles "to be determined" (formalization.yaml `sources`).

### 2(c) Main theorem statements, verbatim

Each project has a Mathlib-only `Challenge.lean` (trusted) and a `Solution.lean` (bridge). The `Challenge.lean` statements:

**`euler-blowup/Challenge.lean` lines 56–67:**

```lean
theorem euler_smooth_force_blowup :
    ∃ (T : ℝ) (_ : 0 < T) (u f : ℝ → R3 → R3) (p : ℝ → R3 → ℝ),
      ClassicalEuler T u f p ∧
      HasCompactSupport (u 0) ∧
      (∀ i : Fin 3, SmoothForce T (fun z => (f z.1 z.2) i)) ∧
      (∃ g : ℝ → ℝ, Tendsto g (𝓝[<] T) atTop ∧ ∀ τ ∈ Ico 0 T, ∃ x, ‖curl3 (u τ) x‖ ≥ g τ) ∧
      (∀ M : ℝ, ∃ T' ∈ Ico 0 T, ∃ g : ℝ → ℝ, (∀ τ ∈ Icc 0 T', 0 ≤ g τ ∧ ∃ x, ‖curl3 (u τ) x‖ ≥ g τ) ∧
          IntervalIntegrable g volume 0 T' ∧ ∫ τ in (0 : ℝ)..T', g τ ≥ M) ∧
      (∀ T' < T, 0 < T' → InLipschitzClass3 T' u f) ∧
      (∀ T' < T, 0 < T' → ∀ u', InLipschitzClass3 T' u' f → u' 0 = u 0 →
          ∀ t ∈ Icc 0 T', u' t = u t) := by
  sorry
```

with the defining structures (same file, lines 9–52):

```lean
structure SmoothForce {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (T : ℝ) (F : ℝ × E → ℝ) : Prop where
  smooth : ContDiffOn ℝ ∞ F (Ico 0 T ×ˢ univ)
  support : ∃ Rball : ℝ, ∀ t ∈ Ico 0 T, ∀ x : E, Rball < ‖x‖ → F (t, x) = 0
  bounded : ∀ k : ℕ, ∃ M : ℝ, ∀ z ∈ Ico 0 T ×ˢ (univ : Set E),
    ‖iteratedFDerivWithin ℝ k F (Ico 0 T ×ˢ univ) z‖ ≤ M

abbrev R3 := EuclideanSpace ℝ (Fin 3)

def e3 (i : Fin 3) : R3 := EuclideanSpace.single i (1 : ℝ)

def pd3 (i : Fin 3) (g : R3 → ℝ) (x : R3) : ℝ := fderiv ℝ g x (e3 i)

def pdt3 (g : ℝ → R3 → ℝ) (t : ℝ) (x : R3) : ℝ := derivWithin (fun τ => g τ x) (Ici 0) t

def div3 (u : R3 → R3) (x : R3) : ℝ := ∑ i, pd3 i (fun y => (u y) i) x

def advect3 (u : R3 → R3) (g : R3 → ℝ) (x : R3) : ℝ := ∑ i, (u x) i * pd3 i g x

def curl3 (u : R3 → R3) (x : R3) : R3 :=
  (pd3 1 (fun y => (u y) 2) x - pd3 2 (fun y => (u y) 1) x) • e3 0 +
  (pd3 2 (fun y => (u y) 0) x - pd3 0 (fun y => (u y) 2) x) • e3 1 +
  (pd3 0 (fun y => (u y) 1) x - pd3 1 (fun y => (u y) 0) x) • e3 2

structure ClassicalEuler (T : ℝ) (u f : ℝ → R3 → R3) (p : ℝ → R3 → ℝ) : Prop where
  smoothu : ContDiffOn ℝ ∞ (fun z : ℝ × R3 => u z.1 z.2) (Ico 0 T ×ˢ univ)
  smoothp : ContDiffOn ℝ ∞ (fun z : ℝ × R3 => p z.1 z.2) (Ico 0 T ×ˢ univ)
  divFree : ∀ t ∈ Ico 0 T, ∀ x, div3 (u t) x = 0
  finiteEnergy : ∀ t ∈ Ico 0 T, MemLp (u t) 2 volume
  equ : ∀ t ∈ Ico 0 T, ∀ x, ∀ i : Fin 3,
    pdt3 (fun τ y => (u τ y) i) t x + advect3 (u t) (fun y => (u t y) i) x + pd3 i (p t) x
      = (f t x) i

structure InLipschitzClass3 (T' : ℝ) (u f : ℝ → R3 → R3) : Prop where
  lip : LocallyLipschitzOn (Icc 0 T' ×ˢ univ) (fun z : ℝ × R3 => u z.1 z.2)
  energyGrad : ∃ M, ∀ t ∈ Icc 0 T', MemLp (u t) 2 volume ∧
    (eLpNorm (u t) 2 volume).toReal ≤ M ∧ ∀ x, ‖fderiv ℝ (u t) x‖ ≤ M
  divFree : ∀ t ∈ Icc 0 T', ∀ᵐ x ∂(volume : Measure R3), div3 (u t) x = 0
  solvesWeak : ∀ φ : ℝ × R3 → R3, ContDiff ℝ ∞ φ → HasCompactSupport φ →
    tsupport φ ⊆ Ioo 0 T' ×ˢ univ → (∀ z : ℝ × R3, div3 (fun y => φ (z.1, y)) z.2 = 0) →
    ∫ z : ℝ × R3, ∑ i : Fin 3,
      ( (u z.1 z.2) i * deriv (fun τ => (φ (τ, z.2)) i) z.1
        + ∑ j : Fin 3, (u z.1 z.2) i * (u z.1 z.2) j * pd3 j (fun y => (φ (z.1, y)) i) z.2
        + (f z.1 z.2) i * (φ z) i ) = 0
```

**`boussinesq-blowup/Challenge.lean` lines 67–80:**

```lean
theorem boussinesq_smooth_force_blowup :
    ∀ κ : ℝ, 0 < κ →
    ∃ (T : ℝ) (_ : 0 < T) (θ p fθ : ℝ → R2 → ℝ) (u fu : ℝ → R2 → R2),
      ClassicalBoussinesq κ T θ p u fu fθ ∧
      (∀ t ∈ Ico 0 T, InClassP (θ t) (u t)) ∧ (∀ t ∈ Ico 0 T, InClassP (fθ t) (fu t)) ∧
      HasCompactSupport (θ 0) ∧ HasCompactSupport (u 0) ∧
      SmoothForce T (fun z => fθ z.1 z.2) ∧ (∀ i : Fin 2, SmoothForce T (fun z => (fu z.1 z.2) i)) ∧
      (∃ g : ℝ → ℝ, Tendsto g (𝓝[<] T) atTop ∧ ∀ τ ∈ Ico 0 T, ∃ x, gradSize (θ τ) x ≥ g τ) ∧
      (∃ M : ℝ, ∀ τ ∈ Ico 0 T, ∀ x, |θ τ x| ≤ M) ∧
      (∀ M : ℝ, ∃ᶠ τ in 𝓝[<] T, ∃ x, |curl2 (u τ) x| ≥ M) ∧
      (∀ T' < T, 0 < T' → InLipschitzClass κ T' θ u fθ fu) ∧
      (∀ T' < T, 0 < T' → ∀ θ' u', InLipschitzClass κ T' θ' u' fθ fu →
          θ' 0 = θ 0 → u' 0 = u 0 → ∀ t ∈ Icc 0 T', θ' t = θ t ∧ u' t = u t) := by
  sorry
```

with `ClassicalBoussinesq` and `InLipschitzClass` (lines 37–66):

```lean
structure ClassicalBoussinesq (κ T : ℝ) (θ p : ℝ → R2 → ℝ) (u fu : ℝ → R2 → R2)
    (fθ : ℝ → R2 → ℝ) : Prop where
  smoothθ : ContDiffOn ℝ ∞ (fun z : ℝ × R2 => θ z.1 z.2) (Ico 0 T ×ˢ univ)
  smoothu : ContDiffOn ℝ ∞ (fun z : ℝ × R2 => u z.1 z.2) (Ico 0 T ×ˢ univ)
  smoothp : ContDiffOn ℝ ∞ (fun z : ℝ × R2 => p z.1 z.2) (Ico 0 T ×ˢ univ)
  divFree : ∀ t ∈ Ico 0 T, ∀ x, div2 (u t) x = 0
  finiteEnergy : ∀ t ∈ Ico 0 T, MemLp (u t) 2 volume ∧ MemLp (θ t) 2 volume
  eqθ : ∀ t ∈ Ico 0 T, ∀ x, pdt θ t x + advect (u t) (θ t) x = fθ t x
  equ : ∀ t ∈ Ico 0 T, ∀ x, ∀ i : Fin 2,
    pdt (fun τ y => (u τ y) i) t x + advect (u t) (fun y => (u t y) i) x + pd i (p t) x
      = κ * θ t x * (if i = 1 then 1 else 0) + (fu t x) i

structure InLipschitzClass (κ T' : ℝ) (θ : ℝ → R2 → ℝ) (u : ℝ → R2 → R2)
    (fθ : ℝ → R2 → ℝ) (fu : ℝ → R2 → R2) : Prop where
  lip : LocallyLipschitzOn (Icc 0 T' ×ˢ univ) (fun z : ℝ × R2 => (θ z.1 z.2, u z.1 z.2))
  energy : ∃ M, ∀ t ∈ Icc 0 T', MemLp (u t) 2 volume ∧ MemLp (θ t) 2 volume ∧
    (eLpNorm (u t) 2 volume).toReal ≤ M ∧ (eLpNorm (θ t) 2 volume).toReal ≤ M
  gradBounded : ∃ M, ∀ t ∈ Icc 0 T', ∀ x, ‖fderiv ℝ (θ t) x‖ ≤ M ∧ ‖fderiv ℝ (u t) x‖ ≤ M
  divFree : ∀ t ∈ Icc 0 T', ∀ᵐ x ∂(volume : Measure R2), div2 (u t) x = 0
  solvesθAE : ∀ᵐ z : ℝ × R2 ∂(volume.restrict (Icc 0 T' ×ˢ univ)),
    pdt θ z.1 z.2 + advect (u z.1) (θ z.1) z.2 = fθ z.1 z.2
  solvesuWeak : ∀ φ : ℝ × R2 → R2, ContDiff ℝ ∞ φ → HasCompactSupport φ →
    tsupport φ ⊆ Ioo 0 T' ×ˢ univ → (∀ z : ℝ × R2, div2 (fun y => φ (z.1, y)) z.2 = 0) →
    ∫ z : ℝ × R2, ∑ i : Fin 2,
      ( (u z.1 z.2) i * deriv (fun τ => (φ (τ, z.2)) i) z.1
        + ∑ j : Fin 2, (u z.1 z.2) i * (u z.1 z.2) j * pd j (fun y => (φ (z.1, y)) i) z.2
        + (κ * θ z.1 z.2 * (if i = 1 then 1 else 0) + (fu z.1 z.2) i) * (φ z) i ) = 0
end BoussinesqBlowup

open BoussinesqBlowup in
```

**`affinecore/Challenge.lean` lines 270–271** (`theorem forced_boussinesq_affine_core_blowup : AffineCore.External.Theorem1 := by sorry`), where the proposition is defined at lines 232–269 of the same file:

```lean
def Theorem1 : Prop :=
  ∀ A₀ : ℝ, 1 ≤ A₀ → ∀ χ₀ : R2 → ℝ, IsRadialCutoff χ₀ →
  ∃ (T : ℝ) (_ : 0 < T) (θ p fθ : ℝ → R2 → ℝ) (u fu : ℝ → R2 → R2),
    ClassicalBoussinesq 1 T θ p u fu fθ ∧ (∀ t ∈ Ico 0 T, InClassP (θ t) (u t)) ∧
    (∀ t ∈ Ico 0 T, InClassP (fθ t) (fu t)) ∧
    (∀ T' < T, 0 < T' → InLipschitzClass 1 T' θ u fθ fu) ∧
    HasCompactSupport (θ 0) ∧ HasCompactSupport (u 0) ∧
    θ 0 = thetaIn A₀ χ₀ ∧ u 0 = uIn ∧
    SmoothForce T (fun z => fθ z.1 z.2) ∧ (∀ i : Fin 2, SmoothForce T (fun z => (fu z.1 z.2) i)) ∧
    (∃ R : ℝ, ∀ t ∈ Ico 0 T, ∀ x : R2, R < ‖x‖ →
        θ t x = 0 ∧ curl2 (u t) x = 0 ∧ fθ t x = 0 ∧ fu t x = 0) ∧
    (∀ t ∈ Ico 0 T, Differentiable ℝ (newtonPotential (curl2 (u t))) ∧
        ∀ x : R2, u t x = biotSavart (curl2 (u t)) x) ∧
    (∀ t ∈ Ico 0 T, p t 0 = 0) ∧
    (∀ M : ℝ, ∀ᶠ τ in 𝓝[<] T, ∃ x, gradSize (θ τ) x ≥ M) ∧
    (∃ M, ∀ τ ∈ Ico 0 T, ∀ x, |θ τ x| ≤ M) ∧
    (∀ M : ℝ, ∃ᶠ τ in 𝓝[<] T, ∃ x, |curl2 (u τ) x| ≥ M) ∧
    (∀ T' < T, 0 < T' → ∀ θ' u', InLipschitzClass 1 T' θ' u' fθ fu →
        θ' 0 = θ 0 → u' 0 = u 0 → ∀ t ∈ Icc 0 T', θ' t = θ t ∧ u' t = u t)

end AffineCore.External

/-- Finite-time gradient blow-up with bounded temperature for the forced two-dimensional inviscid
Boussinesq system, from explicit data. For every real A₀ ≥ 1 and every radial smooth compactly
supported cut-off χ₀ equal to 1 on the open ball of radius 2 about the origin, there exist a
finite time T > 0, forcing terms f_θ, f_u and a classical solution (θ, u, p) on [0, T) of the
Boussinesq system with buoyancy constant 1 such that: θ(t), u(t) and the forces are odd under
x ↦ −x at every time t ∈ [0, T); the initial temperature is −(A₀/N₀) sin(N₀ x₂) χ₀(x) with
N₀ = ⌈(√A₀)/2⌉ and the initial velocity is zero; the forces are smooth on [0, T) × ℝ² with
derivatives bounded order by order; one fixed ball contains the supports of θ(t), of the
vorticity curl u(t) and of both forces for every t ∈ [0, T); u(t) is the Biot–Savart velocity
of its vorticity through the logarithmic kernel; the pressure vanishes at the origin; the
temperature stays bounded on [0, T) × ℝ² while the supremum norm of its gradient tends to +∞ as
t ↑ T, and the supremum norm of the vorticity has limes superior +∞ as t ↑ T; and on every
[0, T'] with 0 < T' < T the pair (θ, u) belongs to the finite-energy Lipschitz class defined
with these forces (momentum equation in weak, pressure-free form) and is the only member of
that class with its initial values. The precise content of the theorem is the proposition
AffineCore.Theorem1_External. -/
```

**Plain-English reading, and how it differs from OpenAI's Euler theorem.**

* *Not a Clay alternative.* None of the three is stated against the Formal Conjectures / Clay template. They are the authors' own theorems about *forced* Euler and *forced* Boussinesq, in their own definitional layer (`ClassicalEuler`, `SmoothForce`, `InLipschitzClass3`, …). The 3D Euler theorem says: there exist T > 0, a force f and a classical solution (u, p) on [0, T) × ℝ³, smooth, divergence-free, L², with compactly supported initial velocity, such that ‖curl u(t)‖_∞ → ∞ as t ↑ T and ∫₀^T ‖curl u‖_∞ dt = ∞, and u is the unique solution in a finite-energy Lipschitz class on every [0, T′], T′ < T. **The force is part of the conclusion and is essential** — as in OpenAI's Navier–Stokes theorems, and *unlike* OpenAI's Euler theorem, which is unforced (f = 0) and therefore addresses the genuinely open problem for Euler; the Alpöge–Buckmaster Euler statement is an (interesting, uniqueness-class-quantified) forced blowup, not the unforced one.
* *Blowup time, not ¬∃.* All three theorems exhibit a finite T and the solution up to T; there is no non-existence clause at all. Unboundedness is stated without sup-norms: "there is g(t) → +∞ with ‖ω(t, x)‖ ≥ g(t) at some x" (`fidelity.divergences` in each yaml explains this rendering), and the BKM divergence as an integrable minorant of arbitrarily large integral. The yaml states plainly "No rate of blow-up is certified."
* *Equation form.* Pointwise classical, componentwise: `pdt3 (fun τ y => (u τ y) i) t x + advect3 (u t) (fun y => (u t y) i) x + pd3 i (p t) x = (f t x) i`, with `pdt3` the one-sided time derivative (`derivWithin … (Ici 0)`), `pd3` a partial derivative as `fderiv … (e3 i)`, smoothness `ContDiffOn ℝ ∞ … (Ico 0 T ×ˢ univ)`. Time comes *before* space (`ℝ → R3 → R3`), the opposite of the Clay/Formal Conjectures convention. Uniqueness is in a weak, pressure-free formulation (`solvesWeak`, tested against smooth compactly supported divergence-free φ), i.e. a genuinely different — and stronger, in the uniqueness sense — solution notion than OpenAI's.
* *Which class of solutions.* Classical C^∞ on [0, T) × ℝ³, finite energy (`MemLp (u t) 2`), plus, for the uniqueness clause, the "finite-energy Lipschitz class" (locally Lipschitz, uniform L² and Lipschitz bounds, divergence-free a.e., weak momentum equation). No Sobolev-jet class as in OpenAI's Euler.
* *The internal, stronger form.* `Solution.lean` derives the exported theorem from `EulerBlowup.Num.Cert.theorem01prime 1 one_pos`, whose statement `Theorem01prime_Statement'` (`EulerBlowup/Ring/Statement.lean` lines 11–32) is the axisymmetric version: for every ring radius r₀ > 0, an axisymmetric solution supported in a torus-shaped ring around the circle of radius r₀ (`(cylR x - r₀)² + x₂² ≤ (r₀/4 + r₀/10⁷)²`), with angular momentum, a `Staircase T` record (`Main.lean` line 67: stage times t n ↑ T and amplitudes A n with `A (n+1) ≥ q^n * A n` eventually for every q — super-exponential growth across stages) and the blowup quantified as `‖fderiv ℝ (angMom (u τ)) x‖ ≥ S.A (S.stage τ) / 2`. So the exported "∃ g → ∞" is `g τ = S.A (S.stage τ) / 2` — a staircase of explicit stage amplitudes. This is the classic 2D Boussinesq ↔ axisymmetric 3D Euler-with-swirl correspondence made formal (`Ring/`, `Ring3D/`, `Merid.lean`, `Cyl.lean`, `Rescale.lean`).

### 2(d) Trust audit

Greps over all 3,748 files (including the duplicated vendor copies):

| Pattern | Count | Where |
|---|---|---|
| `sorry` | 4 | One in a comment; three are the intentional placeholders, one per `Challenge.lean` (`affinecore:271`, `euler-blowup:67`, `boussinesq-blowup:80`). **Zero** in the developments and vendor libraries. |
| `axiom` declarations | 0 | — |
| `native_decide` | 0 | The yaml says so explicitly: "one step evaluates interval-arithmetic certificates … inside the kernel (decide; native_decide is not used)". |
| `decide +kernel` | 8,251 | `Num/Cert/` (783 certificate files in `euler-blowup` alone) — see 2(f). |
| `by decide` | 504 (Num) / 22,820 total `decide` tokens | Mostly the checker *definitions* (`decide (0 < …)`, `decide (c = pc.len)` inside `Bool` functions) and small `Fin` facts. |
| `unsafe`, `implemented_by`, `@[extern`, `partial def`, `opaque` | 0 | — |
| `set_option maxHeartbeats` | **5,161** | Values: 400000 (×1,959), 4000000 (×1,923), 1000000 (×855), 800000 (×330), 1600000 (×58), 2000000 (×23), 3200000 (×4), 3000000 (×1), 500000, 200000. |
| `set_option maxRecDepth` | 660 | e.g. `8192` ×255 in `Num` (needed for the big literal arrays). |
| other `set_option` | 117 | `maxSynthPendingDepth` 33, `autoImplicit` 24, `linter.*` 60. |
| `Classical.choice` | 0 in source | (No explicit mention; it is of course in the axiom printout.) |
| `#print axioms` | 6 | `scripts/PrintAxioms.lean` in each project: the exported theorem and the library theorem it is derived from. |
| `#eval`/`#guard` | 0 | — |

**Comparator setup.** Each project has `comparator.json` (challenge `Challenge`, solution `Solution`, one theorem name, the three standard axioms, `enable_nanoda: true`) — the same tool and the same permitted-axiom list as OpenAI. The READMEs call it "the comparator tool's standard Challenge/Solution layout" / "Palomar template". Notably, the affinecore yaml says "the comparator run is pending" and its README that `Challenge.lean` "has not yet been read against the theorem stated above by the responsible maintainer"; the Boussinesq yaml's `review.status` is `unreviewed` ("To be confirmed at release"); only the Euler yaml is `author-verified` ("Levent Alpöge … read the challenge module `Challenge.lean` at the released revision … and confirmed it states the manuscript's blow-up theorem"). So of the three, one has the human read of the trusted statement recorded; OpenAI's is `self-assessed` for all four. Neither repository records a third-party review.

**The affinecore statement-file subtlety.** The affinecore README explains that `Challenge.lean` contains "copies of seven library definitions … identical in text to the originals and placed in one file because the comparator compares auxiliary-lemma names, which Lean assigns per file" — the same duplication-for-independence pattern as OpenAI's `ComparatorDefinitions.lean`, with the same practical wrinkle (auxiliary-declaration naming must match).

**What I verified locally.** Nothing was built: Mathlib publishes no cache for `v4.32.2` (the READMEs say Mathlib must be compiled from source and recommend "on the order of 100–150 GB of memory and a few hours at two to three dozen parallel jobs rather than a laptop"; the locally installed toolchains are 4.28.0, 4.33.0-rc2, 4.34.0-rc2). The audit is source-level only.

### 2(f) Structure of the proofs

**Layering (euler-blowup, 1,078 modules; the others are analogous).** `S0`–`S7` (planar Boussinesq sections: S2 "Dressed", S4 "Iteration"/"Force"/"Stage"/"TimeRates", S6 "TheoremH"/"BaseRun"/"Ledger", S7 "TimeRegularity"/"Readout"), `D` (TheoremR), `E`, `L` (Parity, …), `Lit/` (literature results: `CZ/CZCore`, `CZ/Bogovskii` — Calderón–Zygmund and Bogovskiĭ operators), `Kit/` (BiotSavartGlobal, ParamLinearOp, WeightCalc, MixedBounds), `Num/` (878 files: the certificate kernel `Kernel.lean`, `Check.lean`, `CheckP.lean`, `QCheck.lean`, `Expr.lean`/`ExprDeriv.lean`, `FlatStepTable*`, and `Num/Cert/` with 832 generated certificate modules), `Ring/` (the axisymmetric lift, `S4r`/`S6r`/`S7r`/`Lr`, 541k lines) and `Ring3D/` (`Cyl`, `Merid`, `Potential`, `Force`, `Rescale`, `Assembly`, `Final`), `Main.lean` (the `Staircase` record and `Theorem01_Statement`), `Ring/Statement.lean`, `Hypotheses.lean`. The vendored `Cm24` library ("kernel estimates, transport, uniqueness"; `Kernel.lean`, `Kit.lean`, `Layered.lean`, sections `S2`, `S31`, `S32a`, `S32b`, `S33`, `S4`) is the shared analytic base. affinecore instead has `Framework/{Skeleton,Ladder,Planar,Numerics,ODE,Cascade,LemmaS}`, `Statement/{Interface,TheoremA,Assembly,Protocol,Cascade,LemmaS}`, `Construction/…`, `Leaves/` ("leaf contracts") and `Proofs/R01…R09` ("one closed proof unit per leaf", assembled in `Proofs/R01/Theorem1.lean`, a 10-line file).

**Mathlib areas** (euler-blowup dev tree, identifier counts): `ContDiff`/`ContDiffOn` 22k/13k, `fderiv` 9.6k, `iteratedFDeriv` 2.1k, `HasDerivAt` 2.3k, `Real.exp` 14k, `Real.sin|cos` 8.2k (explicit trigonometric data: the initial temperature is `−(A₀/N₀) sin(N₀ x₂) χ₀(x)`), `Real.pi` 1.3k, `ENNReal` 9.6k, `MeasureTheory` 542, `integral` 3.0k, `MemLp` 266, `Lipschitz` 326, `BiotSavart` 908, `Gronwall` 113 (project-defined), `Fourier` 224, `Complex` 2.9k, `Finset` 30k, `List` 14k, `Fin` 21k, `Nat.` 12.7k, `ℚ` 1.9k, `Array` 427 — i.e. far more discrete/combinatorial bookkeeping (staircases, tables, integer certificate data) than the OpenAI code, and no Sobolev-jet machinery. Every file starts with `import Mathlib` (222 files in euler-blowup, 462 in affinecore) rather than granular imports.

**Numerics: kernel-checked interval arithmetic.** This is the sharpest structural difference from OpenAI. The Boussinesq and Euler projects rest on "some 1,200 machine-generated interval-arithmetic certificate modules, each an inequality between explicit rationals decided by the kernel; the fixed-point arithmetic they use is itself proved sound in Lean" (README). Concretely: `Num/Kernel.lean` defines a dyadic-interval type `DI` with `DI.add`, `DI.mul` (994 lines); `Num/Check.lean` an interval polynomial evaluator with soundness (`IPoly.evalI_sound`, `IPoly.encl_sound_aux_mvt`); `Num/CheckP.lean` (913 lines) a Boolean checker `pCheckPiece : PFieldData → Array DI → Array DI → PieceCert → Bool` and its soundness theorem `pCheckPiece_sound` / `pChainOK_sound` relating `= true` to real inequalities on an ODE field; and `Num/Cert/**` holds 783 files of the shape

```lean
def dpreB_B_16 : PieceCert :=
  { u0 := 662929865148936960, len := 5764607523034240,
    lo := #[[15231680609924354, 114624049788098048, …], …],
    hi := #[[19376720356890944, …], …],
    cuts := [0, 720575940379280, …, 5764607523034240] }

theorem dpreB_B_16_ok : pCheckPiece (preFieldBP hTab) dpreB_OmB dpreP dpreB_B_16 = true := by
  decide +kernel
```

(`Num/Cert/SB3/DPreBig_B_p1.lean`), 111,428 lines of such certificates in `euler-blowup` alone, each under `set_option maxHeartbeats 4000000` and `maxRecDepth 8192`. The certificate *generator* (the untrusted producer) is not in the repository; only the certificates and the Lean checker are. affinecore takes the opposite route: "every constant of the construction is a letter with a stated admissible range; the order hypotheses between the letters are shown consistent in Lean by exact rational arithmetic, and no floating-point or interval certificate is evaluated" (`Leaves/ConstsOfLetters.lean`: `def normCapG (W : LemmaSWindows) : ℝ := 4 * W.CW * W.CS * (1 + 8 * W.zetaHi)`, …).

**Tactic profile** (euler-blowup dev tree / affinecore): `rw [` 97k / 23.6k, `exact` 60k / 15k, `linarith` 34.7k / 8.6k, `simp` 26.7k / 5.7k, `positivity` 24.4k / 3.3k, `omega` 23k / 10.9k, `refine` 23k / 4.7k, `ring` 17.5k / 3.2k, `norm_num` 14.5k / 1.2k, `calc` 12k / 1.9k, `nlinarith` 7.4k / 3.1k, `gcongr` 2.6k / 0.2k, `field_simp` 2.6k / 0.8k, `push_cast` 1.3k / 50, `fun_prop` 494 / 471, `interval_cases` 69 / 7, `linear_combination` 252 / 72, `convert` 78 / 5, `continuity` 52 / 2, `measurability` 0; **`aesop` 0, `polyrith` 0, `grind` 0, `exact?` 0** in both repositories. Declarations: 27,877 / 14,291 `theorem`s (46 / 2 `lemma`s), 10,498 / 2,867 `def`s. Average 33.6 (euler-blowup) and 20.8 (affinecore) lines per theorem, with individual proofs up to 908 lines. Documentation: **zero docstrings, zero module docs, zero line comments in the entire 1.7M-line development** (`grep -rl '/--'` finds no file in `EulerBlowup/` or `AffineCore/`); the only prose is in `Challenge.lean` (docstrings on every definition, written for the human reader who must trust it), the READMEs and the yaml. Names are systematic and paper-indexed rather than descriptive: `Lnode_quantities_continuousOn_s_cyl_7_aux_fderiv`, `stageCond_at_park_aux_ratio`, `chain_closed_aux_le_of_Ico`, `dpreB_B_16_ok`, files `L320.lean`, `R05Rec.lean`, `DB3_Params.lean`.

