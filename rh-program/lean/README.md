# Lean files of the cubic-augmentation paper

Three Lean 4 files. They carry the twelve machine-checked theorems of Section 10 of *The
two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity
control* (source: `rh-program/results/arxiv/a4-no-go/main.tex`).

| File | Lines | What it carries |
|---|---|---|
| `Zeta23/PairCeiling/GridParseval.lean` | 583 | The grid Parseval identity: Lemma 3.8 and Theorem 3.9 of the paper |
| `Zeta23/PairCeiling/GridWitness.lean` | 402 | The witness at N = 64: F1 = 64 and F′ = 4128/33 for every vacancy position; Proposition 3.10 in witness form |
| `Zeta23/PairCeiling/GridCorner.lean` | 263 | Lemma 4.2 and Theorem 4.3 on the grid: pointwise, in law form, and with exact attainment |

`#print axioms` on each of the twelve theorems returns `[propext, Classical.choice, Quot.sound]`.
The map from theorem names to the paper's numbering, the axiom output, the environment and the
steps to reproduce the check are in `rh-program/results/a4-no-go/formalization-status.md`.

## Building

The files are additions to the Zeta23 library (<https://github.com/anthropics/zeta-23-lean>;
Copyright 2026 Anthropic, PBC; Apache License 2.0) and build inside a checkout of it:

```sh
git clone https://github.com/anthropics/zeta-23-lean
cd zeta-23-lean
# copy this directory's Zeta23/ subtree over the checkout, preserving paths:
cp -R /path/to/riemann-rh-program/rh-program/lean/Zeta23/. Zeta23/
lake exe cache get
lake build Zeta23.PairCeiling.GridParseval Zeta23.PairCeiling.GridWitness Zeta23.PairCeiling.GridCorner
```

Toolchain, as pinned by Zeta23 and used for the recorded build: Lean `v4.33.0-rc2`, Mathlib
commit `51e6992efd06126df61a496bebf8f49482a4e129`. Recorded result: *Build completed
successfully (2081 jobs)*.

## License

Copyright 2026 Kunal Tyagi. Apache License 2.0; see [`LICENSE`](../../LICENSE) and
[`NOTICE`](../../NOTICE). The files import Zeta23 and contain no code from it.
