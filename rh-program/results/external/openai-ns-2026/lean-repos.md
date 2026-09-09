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

