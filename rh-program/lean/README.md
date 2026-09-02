# `rh-program/lean` — this program's own Lean 4 files

9 files, ~6,280 lines (3,265 of them the data literals of `W1/Instances.lean`, added
2026-09-02). They are **additions to the `Zeta23` library**, not a standalone project, and
they are the only Lean files in this repository.

| File | Lines | What it carries |
|---|---|---|
| `Zeta23/PairCeiling/GridParseval.lean` | 583 | The grid-Parseval decoupling identity — the algebraic core of the A4 absorption result (Lemma 3.8 and Theorem 3.9 of the A4 paper) |
| `Zeta23/PairCeiling/GridWitness.lean` | 402 | The 4128/33 witness, for every vacancy position |
| `Zeta23/PairCeiling/GridCorner.lean` | 263 | The corner theorem: Lemma 4.2 and Theorem 4.3, pointwise, in law form, and with exact attainment |
| `Zeta23/W1/Soundness.lean` | 1257 | W1 checker soundness |
| `Zeta23/W1/{Checker,Examples,Format}.lean` | 370 | The W1 checker, its examples and its output format |
| `Zeta23/W1/Instances.lean` | 3265 | The ten M1 v1 acceptance transcripts and the two positive controls as kernel-checked checker instances (`checkW1Floor … = true` ×10, `checkW1 … = false` ×2 by `decide +kernel`); mechanically emitted by `results/d1-m1/emit_lean.py` and back-parse-verified against the JSON; needs `set_option maxRecDepth 100000` (written by the emitter) for the 983/1294-row literals — added at the reconciled audit of 2026-09-02, `results/d1-m1/AUDIT.md` |
| `Zeta23/DBN/Defs.lean` | 112 | De Bruijn–Newman definitions |

`#print axioms` on all twelve machine-checked theorems reports only Lean's three standard
axioms — `propext`, `Classical.choice`, `Quot.sound`. No `sorryAx`, no `Lean.ofReduceBool`, and
no real `sorry` or `admit` anywhere in the development. The twelve `_check` theorems of
`W1/Instances.lean` report `[propext]` (the ten `checkW1Floor` instances) or no axioms at all
(the two rejections) — they are integer facts about literals; the ζ conclusion for the eight ζ
transcripts is `cert_of_checkW1` modulo the displayed hypotheses H-ENCL and H-AP, and the two
f_DH instances carry no theorem about f_DH (D-R8). Build record for `Instances.lean`:
`lake build Zeta23.W1.Instances` — *Build completed successfully (656 jobs)*, 13.9 s, Lean
`v4.33.0-rc2`, Mathlib `51e6992e` (`results/d1-m1/recon_lean_instances.log`).

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

These nine files are **Copyright 2026 Kunal Tyagi**, released under the **Apache License 2.0**
(see the repository's [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE)).
(`W1/Instances.lean`, added 2026-09-02, was written under this header from the start; the
relicensing record below concerns the original eight.)

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
