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

