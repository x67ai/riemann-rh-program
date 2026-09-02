# Port notes: Gomila/Aristotle rectangle argument principle → `Zeta23.W1.ArgPrinciple.{Rect,General}`

**Date:** 2026-09-02 (Session 14, D1 v1.1 port agent). **Status:** IN PROGRESS — this file is
written as the work happens (RULE ONE); a section marked "(pending)" has not run yet.

**Source:** `~/rh-lean-work/gomila-ap/repo/lean/aristotle/argument_principle/RequestProject/
{ArgumentPrinciple,ArgumentPrincipleGeneral}.lean`, branch `lean/certificate-and-argument-principle`
@ `ea09b2f6aa7afe60706b67c87b202126f3149e8c` of github.com/judegomila/dbn-lambda-01787854-candidate-audit
(MIT, Copyright (c) 2026 Jude Gomila; generated with Harmonic Aristotle). SHA-256 of the sources as
ported: `b1162a0c…` / `ee382242…` (full hashes in `../gomila-lean-branch-verify.md` §1.2). Verified
today to build on Lean v4.28.0 + Mathlib `8f9d9cff` with standard axioms only (same file, §3).

**Target:** APFS clone `~/rh-lean-work/zeta-23-v11` of the program's hot tree
`~/rh-lean-work/zeta-23-lean-main` (created 12:56 IST today, `cp -c -R`, 17 s). Toolchain
`leanprover/lean4:v4.33.0-rc2`; Mathlib rev per `lake-manifest.json` =
`51e6992efd06126df61a496bebf8f49482a4e129` (the package's git HEAD agrees). Known discrepancy,
reported not resolved: the tree's README.md line "Mathlib commit `51e6992e…`" agrees with the
manifest, but `results/d1-m1/AUDIT-F.md` records "123d1576…" — that short hash is the manifest's
*plausible* rev, not Mathlib's (see the scout's side note).

New files (in the clone only; NOT copied into the program root's `lean/` yet):

* `Zeta23/W1/ArgPrinciple/Rect.lean`    ← `RequestProject/ArgumentPrinciple.lean` (444 lines)
* `Zeta23/W1/ArgPrinciple/General.lean` ← `RequestProject/ArgumentPrincipleGeneral.lean` (215 lines)

Both carry the program's Apache-2.0 header plus the required notice block (Gomila / MIT /
Aristotle). Namespace `ArgumentPrinciple` → `Zeta23.W1.ArgPrinciple`.

## 1. Imports (whole-Mathlib import replaced)

(pending — filled in once the build is clean)

## 2. Name table original → ported

(pending)

## 3. Statement-level differences

(pending — expected empty)

## 4. Mathlib API drift hit (8f9d9cff, 2026-02 → 51e6992, 2026-08)

(pending)

## 5. Build log and times

(pending)

## 6. `#print axioms`

(pending)
