# `rh-program/lean` — this program's own Lean 4 files

Eight files, ~2,970 lines. They are **additions to the `Zeta23` library**, not a standalone
project, and they are the only Lean files in this repository.

| File | Lines | What it carries |
|---|---|---|
| `Zeta23/PairCeiling/GridParseval.lean` | 578 | The grid-Parseval decoupling identity — the algebraic core of the A4 absorption result (Lemma 3.8 and Theorem 3.9 of the A4 paper) |
| `Zeta23/PairCeiling/GridWitness.lean` | 397 | The 4128/33 witness, for every vacancy position |
| `Zeta23/PairCeiling/GridCorner.lean` | 258 | The corner theorem: Lemma 4.2 and Theorem 4.3, pointwise, in law form, and with exact attainment |
| `Zeta23/W1/Soundness.lean` | 1257 | W1 checker soundness |
| `Zeta23/W1/{Checker,Examples,Format}.lean` | 370 | The W1 checker, its examples and its output format |
| `Zeta23/DBN/Defs.lean` | 112 | De Bruijn–Newman definitions |

`#print axioms` on all twelve machine-checked theorems reports only Lean's three standard
axioms — `propext`, `Classical.choice`, `Quot.sound`. No `sorryAx`, no `Lean.ofReduceBool`, and
no real `sorry` or `admit` anywhere in the development.

## What these build against, and why it is not here

They extend **Zeta23**, the Lean 4 formalization released as the companion artifact to
*More than two thirds of the zeros of the Riemann zeta function lie on the critical line*
(arXiv:2608.13637).

> Zeta23 is **Copyright 2026 Anthropic, PBC**, released under the **Apache License 2.0**.
> Its canonical home is <https://github.com/anthropics/zeta-23-lean>.

That library was kept locally during the program **for reference**, and an earlier state of this
repository redistributed a copy of it. It has been removed: it is Anthropic's work, it is already
published at the address above, and there is no reason for a second copy to live here. Apache 2.0
permits redistribution — nothing improper was done — but a dependency is better cited than copied.

## Building

```sh
git clone https://github.com/anthropics/zeta-23-lean
cd zeta-23-lean
# copy this directory's Zeta23/ subtree over the checkout, preserving paths:
cp -R /path/to/this/repo/rh-program/lean/Zeta23/. Zeta23/
lake exe cache get && lake build
```

Toolchain, as pinned by upstream and used for the recorded build: Lean `v4.33.0-rc2`, Mathlib
commit `51e6992efd06126df61a496bebf8f49482a4e129`. The recorded result is
*Build completed successfully (2081 jobs)*. The full formalization record — the environment, the
theorem-by-theorem map to the A4 paper's numbering, the `#print axioms` output, and the
reproduction recipe — is `rh-program/results/a4-no-go/formalization-status.md`.

## Licensing (settled 2026-08-27)

These eight files are **Copyright 2026 Kunal Tyagi**, released under the **Apache License 2.0**
(see the repository's [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE)).

They previously carried `Copyright (c) 2026 Anthropic, PBC` — copied from the surrounding library's
header convention when they were written inside it, and pointing at a `LICENSE` file that is no
longer in this repository. That attribution was wrong: these are this program's own work, not part
of Anthropic's Zeta23 release. Each header now says so explicitly, and records that the file
contains no code from Zeta23 but imports it. Apache-2.0 is kept rather than swapped for something
else, so that there is no compatibility question with the library these files extend or with
mathlib, both of which are Apache-2.0.

Verified before relicensing: none of the eight carries an upstream-derivation notice, and none
sits under `Zeta23/FromPNTPlus/`, which is where Zeta23's own NOTICE records its derived files.
They are original.
