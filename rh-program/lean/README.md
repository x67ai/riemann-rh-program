# `rh-program/lean` — this program's own Lean 4 files

13 files, ~8,570 lines (3,265 of them the data literals of `W1/Instances.lean`, added
2026-09-02; 1,092 of them `DBN/BarrierCert.lean`, added the same day). They are **additions to the `Zeta23` library**, not a standalone project, and
they are the only Lean files in this repository.

| File | Lines | What it carries |
|---|---|---|
| `Zeta23/PairCeiling/GridParseval.lean` | 583 | The grid-Parseval decoupling identity — the algebraic core of the A4 absorption result (Lemma 3.8 and Theorem 3.9 of the A4 paper) |
| `Zeta23/PairCeiling/GridWitness.lean` | 402 | The 4128/33 witness, for every vacancy position |
| `Zeta23/PairCeiling/GridCorner.lean` | 263 | The corner theorem: Lemma 4.2 and Theorem 4.3, pointwise, in law form, and with exact attainment |
| `Zeta23/W1/Soundness.lean` | 1262 | W1 checker soundness |
| `Zeta23/W1/{Checker,Examples,Format}.lean` | 385 | The W1 checker, its examples and its output format |
| `Zeta23/W1/Instances.lean` | 3265 | The ten M1 v1 acceptance transcripts and the two positive controls as kernel-checked checker instances (`checkW1Floor … = true` ×10, `checkW1 … = false` ×2 by `decide +kernel`); mechanically emitted by `results/d1-m1/emit_lean.py` and back-parse-verified against the JSON; needs `set_option maxRecDepth 100000` (written by the emitter) for the 983/1294-row literals — added at the reconciled audit of 2026-09-02, `results/d1-m1/AUDIT.md` |
| `Zeta23/W1/ArgPrinciple/Rect.lean` | 492 | The rectangle-integral machinery of the argument principle: `Rect`, `RectFrontier`, the four-edge `rectIntegral` in Mathlib's boundary convention, `windingRect`, the rectangle residue integral `rectIntegral_inv_sub` (∮ (ζ−a)⁻¹ dζ = 2πi — the piece Mathlib lacks), and the factored forms for entire cofactors. **Ported** (see the v1.1 note below) |
| `Zeta23/W1/ArgPrinciple/General.lean` | 249 | The general argument principle on rectangles for entire functions: zero factorization, finiteness of the zero set, `windingRect_eq_sum_analyticOrder`. **Ported** |
| `Zeta23/W1/ArgPrincipleBridge.lean` | 459 | **v1.1, D-R3: H-AP discharged.** Generalizes the ported theorem from entire functions to `DifferentiableOn ℂ f U` on an open `U ⊇ R`, bridges the two rectangle/winding vocabularies, handles the degenerate rectangle σ₁ = σ₂, and proves `rectArgPrinciple_of_local : ∀ f, RectArgPrinciple f`, `rectArgPrinciple_riemannZeta`, and `cert_of_checkW1_ap` — checker soundness with H-AP removed |
| `Zeta23/DBN/Defs.lean` | 117 | De Bruijn–Newman definitions |
| `Zeta23/DBN/BarrierCert.lean` | 1092 | **M2a Lane B (added 2026-09-02).** The barrier-certificate transcript data (`PrismData`, `RectData`, `BarrierData`), the integer checker `checkBarrier` (per-prism `checkPrism` = W1's C1, C3–C9 with the strip-free C2′, m = 0, the C11 floor and the gate C-B12 (E+D)·Fd < Fn·K; global `checkBarrierChain` = C-B13), the displayed hypothesis H2-B (`BarrierEnclOK`), and the soundness theorem `cert_of_checkBarrier` — PROVED, not displayed: the rectangle argument principle on a general rectangle (`rectArgPrincipleGen`, from the v1.1 bridge), the strip-free W1 mesh chain, and the one new analytic lemma `logDerivSegIntegral_eq_log_sub` (∫ h′/h = Log h(w) − Log h(z) when Re h > 0 on the segment) with log-derivative additivity; no Rouché, no zero-continuity in t. Plus `cert_of_checkBarrier_xy`, the coordinate form `Polymath15Bridge`'s (iii) consumes. Contract: `results/d1-m2a/SPEC.md`; record: `results/d1-m2a/lean-notes.md` |

`#print axioms` on every machine-checked theorem here reports only Lean's three standard
axioms — `propext`, `Classical.choice`, `Quot.sound`. This now covers, besides the twelve
theorems recorded before, all 45 declarations of `W1/ArgPrinciple/{Rect,General}.lean` and all 18
of `W1/ArgPrincipleBridge.lean`, `cert_of_checkW1_ap` included
(`results/d1-m1/v11/audit/audit-print-axioms.log`), and all 28 theorems and lemmas of
`DBN/BarrierCert.lean`, `cert_of_checkBarrier` included (`results/d1-m2a/barriercert-axioms.log`). No `sorryAx`, no `Lean.ofReduceBool`, and
no real `sorry` or `admit` anywhere in the development. The twelve `_check` theorems of
`W1/Instances.lean` report `[propext]` (the ten `checkW1Floor` instances) or no axioms at all
(the two rejections) — they are integer facts about literals; **since 2026-09-02 the ζ conclusion
for the eight ζ transcripts is `cert_of_checkW1_ap` modulo the single displayed hypothesis
H-ENCL** (H-AP is a theorem; see the v1.1 note below), and the two f_DH instances carry no
theorem about f_DH (D-R8). Build record for `Instances.lean`: `lake build Zeta23.W1.Instances` —
*Build completed successfully (656 jobs)*, 13.9 s, Lean `v4.33.0-rc2`, Mathlib `51e6992e`
(`results/d1-m1/recon_lean_instances.log`).

## v1.1 (2026-09-02): H-AP is discharged; H-ENCL is the only displayed hypothesis left

`W1/Soundness.lean` proves W1 checker soundness (`cert_of_checkW1`) modulo two displayed
hypotheses, H-ENCL (`W1EnclOK riemannZeta d`) and H-AP (`RectArgPrinciple riemannZeta`, the
rectangle argument principle for the exact counterclockwise traversal of FORMAT.md §4).
**H-AP is now a theorem**: `Zeta23.W1.rectArgPrinciple_of_local : ∀ f : ℂ → ℂ,
RectArgPrinciple f` in `W1/ArgPrincipleBridge.lean`, with `rectArgPrinciple_riemannZeta` its ζ
instance and

    Zeta23.W1.cert_of_checkW1_ap (d : W1Data) (hc : checkW1 d = true)
        (hEncl : W1EnclOK riemannZeta d) : <the conclusion of cert_of_checkW1, unchanged>

the restatement of soundness without it. `Soundness.lean` is imported, not rewritten. How: the
ported theorem `windingRect_eq_sum_analyticOrder` is generalized from `Differentiable ℂ H`
(entire) to `DifferentiableOn ℂ H U` for an open `U` containing the closed rectangle — the
identity theorem is applied on the preconnected closed rectangle, so `U` itself need not be
connected — the two rectangle/winding vocabularies are bridged by unconditional (junk-value-safe)
change-of-variables lemmas, and the degenerate rectangle σ₁ = σ₂ that clause C2b admits is proved
directly with `Z = 0`. No ζ-specific analytic input is consumed anywhere.

Build: `lake build Zeta23.W1.ArgPrincipleBridge` — *Build completed successfully (3145 jobs)*,
6 s from deleted oleans, no warnings, Lean `v4.33.0-rc2`, Mathlib `51e6992e`. (Since 2026-09-02
evening the root `Zeta23.lean` imports every program module, `DBN/BarrierCert` and `W1/Instances`
included; `lake build Zeta23` — *Build completed successfully (9023 jobs)*.) Adversarial audit, by a different model: `results/d1-m1/v11/AUDIT.md` — verdict CLEAN.

**Honest label, binding.** An accepted ζ transcript is *"kernel-checked modulo the displayed
hypothesis H-ENCL (producers untrusted)"*. Never "fully machine-checked": H-ENCL is where the
untrusted producers' interval arithmetic enters the trusted statement, and it stays.

**Attribution for the two ported files.** `W1/ArgPrinciple/Rect.lean` and
`W1/ArgPrinciple/General.lean` are ported, statement-for-statement unchanged, from the Lean
development in `github.com/judegomila/dbn-lambda-01787854-candidate-audit` (branch
`lean/certificate-and-argument-principle`, commit `ea09b2f`), **Copyright (c) 2026 Jude Gomila,
MIT License**, generated with Harmonic Aristotle; ported and adapted here (imports narrowed,
proofs repaired for a newer Mathlib, namespace changed). `W1/ArgPrincipleBridge.lean` adapts
seven of those lemmas and carries the same notice. The MIT license text is reproduced verbatim in
the repository's [`NOTICE`](../NOTICE), in dated sections; the port record is
`results/d1-m1/v11/port-notes.md`, the discharge record `results/d1-m1/v11/discharge-notes.md`,
and the independent build/axiom verification of the source branch
`results/d1-m1/gomila-lean-branch-verify.md`.

## M2a Lane B (2026-09-02): `DBN/BarrierCert.lean`

The barrier-certificate layer of the Λ ≤ 0.2 instance, implementing `results/d1-m2a/SPEC.md`
v1.0. Honest label for an accepted barrier transcript: *"kernel-checked modulo the displayed
hypotheses H2-B (`BarrierEnclOK G d`) and `hHol` (G t holomorphic near the rectangle), producers
untrusted"*. The theorem

    Zeta23.DBN.cert_of_checkBarrier (G : ℝ → ℂ → ℂ) (d : BarrierData)
        (hchain : checkBarrierChain d = true) (hprisms : ∀ p ∈ d.prisms, checkPrism d.rect p = true)
        (hHol : ∀ t, 0 ≤ t → t ≤ t0 d → ∃ U, IsOpen U ∧ BarrierRect d ⊆ U ∧ DifferentiableOn ℂ (G t) U)
        (hEncl : BarrierEnclOK G d) :
        ∀ t, 0 ≤ t → t ≤ t0 d → ∀ z ∈ BarrierRect d, G t z ≠ 0

takes the checker facts in the split form of SPEC §7.6 (per-prism kernel facts in per-prism
modules). Build: `lake build Zeta23.DBN.BarrierCert` — *Build completed successfully (3147 jobs)*,
3.2 s from a deleted olean, no warnings (`results/d1-m2a/barriercert-build.log`). The SPEC §12
micro-example checks by `decide +kernel` against the built module, with four negative controls
(`results/d1-m2a/barriercert-example-scratch.lean`, `.log`). `Defs.lean` is unchanged (v1.0); its
v1.1 additions (`Polymath15Bridge'`, `Bt`, `HtEntire`), the asymptotic lane and `Instance02.lean`
are the next items of the Lean stream.

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

These thirteen files are **Copyright 2026 Kunal Tyagi**, released under the **Apache License 2.0**
(see the repository's [`LICENSE`](../../LICENSE) and [`NOTICE`](../../NOTICE)).
(`W1/Instances.lean`, added 2026-09-02, was written under this header from the start; so were the
three argument-principle files of the same day and `DBN/BarrierCert.lean`, which carry in addition the MIT notice for the
portions ported from the Gomila/Aristotle development — see the v1.1 section above and the dated
sections of [`NOTICE`](../../NOTICE). The relicensing record below concerns the original eight.)

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
