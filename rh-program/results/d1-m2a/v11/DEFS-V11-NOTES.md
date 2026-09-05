# Defs.lean v1.1 — build notes (Session 16, 2026-09-06, D1/M2a, builder agent Fable 5.1)

STATUS: IN PROGRESS (this file is written as the work happens; a line reading "STATUS: DONE" at the
bottom means STEP 1 finished and built).

## What is being changed (RUN-REPORT §6 item 1; SPEC §3.2–3.5)

File: `~/rh-lean-work/zeta-23-lean-main/Zeta23/DBN/Defs.lean` (v1.0 of 2026-08-26 → v1.1).

1. `Polymath15Bridge` (merged canopy form) REMOVED — not kept under the old name (SPEC §3.3: "do not keep
   both"). Reason: its second hypothesis quantifies (ii) over all t ∈ [0, t₀] and all x ≥ X; at t = 0 that is
   RH in the strip Re s ≥ (1 + y₀)/2 at every height ≥ X/2 (SPEC derivation D-3.2) — not dischargeable by any
   finite certificate, so `lambda_le_point2` was unprovable from any transcript.
2. `Polymath15Bridge'` ADDED, exactly as SPEC §3.3 prints it: (ii′) at the final time t₀ only, on
   x ≥ X + 1, y ≥ y₀, y² ≤ 1 − 2t₀; (iii′) on the simplified box X ≤ x ≤ X + 1, y₀ ≤ y ≤ 1, 0 ≤ t ≤ t₀.
   Justification D-H3 (SPEC §3.3): implied by P15 Theorem 1.2 with the p3 simplified barrier region.
3. `alpha`, `M0`, `Mt`, `Bt` ADDED (SPEC §3.4; P15 eqs. (9), (6), (10), (11)) with the shapes of
   `lean-shapes-scratch.lean` §A verbatim.
4. `HtEntire` ADDED (SPEC §3.5): `∀ t : ℝ, Differentiable ℂ (Ht t)`.
5. `open Complex (I)` added so that the source reads exactly as SPEC §3.3–3.4 print it (`I`, not
   `Complex.I`); elaborated term unchanged.

Dated deviation record placed in the file header (format: design note §7).

## Build 1: `lake build Zeta23.DBN.Defs` (2026-09-06)

    ✔ [3140/3140] Built Zeta23.DBN.Defs (11s)
    Build completed successfully (3140 jobs).

Zero warnings, zero errors.

## `#print` of every new declaration (scratch `defs-print.lean` via `lake env lean`, verbatim)

    def Zeta23.DBN.alpha : ℂ → ℂ :=
    fun s => 1 / (2 * s) + 1 / (s - 1) + 1 / 2 * Complex.log (s / (2 * ↑Real.pi))
    def Zeta23.DBN.M0 : ℂ → ℂ :=
    fun s =>
      1 / 8 * (s * (s - 1) / 2) * ↑Real.pi ^ (-s / 2) * ↑√(2 * Real.pi) *
        Complex.exp ((s / 2 - 1 / 2) * Complex.log (s / 2) - s / 2)
    def Zeta23.DBN.Mt : ℝ → ℂ → ℂ :=
    fun t s => Complex.exp (↑t / 4 * alpha s ^ 2) * M0 s
    def Zeta23.DBN.Bt : ℝ → ℂ → ℂ :=
    fun t z => Mt t ((1 - Complex.I * z) / 2)
    def Zeta23.DBN.HtEntire : Prop :=
    ∀ (t : ℝ), Differentiable ℂ (Ht t)
    def Zeta23.DBN.Polymath15Bridge' : Prop :=
    ∀ (t₀ X y₀ : ℝ),
      0 < t₀ →
        0 < X →
          0 < y₀ →
            y₀ ≤ 1 →
              ZeroVerification ((1 + y₀) / 2) (X / 2) →
                (∀ (x y : ℝ), X + 1 ≤ x → y₀ ≤ y → y ^ 2 ≤ 1 - 2 * t₀ → Ht t₀ (↑x + ↑y * Complex.I) ≠ 0) →
                  (∀ (x y : ℝ),
                      X ≤ x → x ≤ X + 1 → y₀ ≤ y → y ≤ 1 → ∀ (t : ℝ), 0 ≤ t → t ≤ t₀ → Ht t (↑x + ↑y * Complex.I) ≠ 0) →
                    ∀ (t : ℝ), t₀ + y₀ ^ 2 / 2 ≤ t → ∀ (z : ℂ), Ht t z = 0 → z.im = 0
    'Zeta23.DBN.Polymath15Bridge'' depends on axioms: [propext, Classical.choice, Quot.sound]
    'Zeta23.DBN.Bt' depends on axioms: [propext, Classical.choice, Quot.sound]
    /private/tmp/claude-501/-Users-jaytyagi-Library-Mobile-Documents-com-apple-CloudDocs-Documents-Work-2026-Math-riemann/59ecbf7d-661c-4ac8-b521-c036ba5a0218/scratchpad/defs-print.lean:11:8: error(lean.unknownIdentifier): Unknown identifier `Zeta23.DBN.Polymath15Bridge`

The last line (the `Unknown identifier` error for `Zeta23.DBN.Polymath15Bridge`) is the intended confirmation
that the v1.0 Prop no longer exists under the old name.

Check against SPEC §3.3–3.5 and `lean-shapes-scratch.lean` §A: the six shapes are character-for-character the
scratch's §A text (only the namespace differs: `Zeta23.DBN` here, `Zeta23.DBN.M2aScratch` there); the
elaborated `Polymath15Bridge'` matches the SPEC §3.3 display with `I` = `Complex.I` and the two real-to-complex
coercions on x, y — the same coercions v1.0's `Polymath15Bridge` carried (SPEC §3.1).

Axioms of the definitions: `propext`, `Classical.choice`, `Quot.sound` (no theorems in this file, by design).

## Build 2: `lake build Zeta23.DBN.BarrierCert Zeta23.DBN.Instance02` against Defs v1.1 (2026-09-06)

Every module downstream of Defs rebuilt (BarrierCert, Instance02/Rect, the 39 mp prism modules, the 72 Arb
prism modules, both `_Barrier` assemblies, Instance02): 116 `Built` lines, zero errors, zero warnings, no
`sorry`.  NO adaptation was needed in BarrierCert.lean or Instance02.lean: the old name `Polymath15Bridge`
occurred there only inside docstrings/comments (BarrierCert.lean lines 56 and 1065; Instance02.lean header),
never in code.  Log tail (verbatim):

    ✔ [3258/3262] Built Zeta23.DBN.Instance02.mp_0002 (4.4s)
    ✔ [3259/3262] Built Zeta23.DBN.Instance02.mp_0000 (2.9s)
    ✔ [3260/3262] Built Zeta23.DBN.Instance02.arb_Barrier (3.4s)
    ✔ [3261/3262] Built Zeta23.DBN.Instance02.mp_Barrier (1.5s)
    ✔ [3262/3262] Built Zeta23.DBN.Instance02 (1.5s)
    Build completed successfully (3262 jobs).
    lake build Zeta23.DBN.BarrierCert Zeta23.DBN.Instance02  309.01s user 163.76s system 773% cpu 1:01.12 total
    exit=0

Wall time 1:01 (773 % CPU, the per-prism `decide +kernel` modules in parallel).

STATUS: DONE (STEP 1).  Program-tree copy of Defs.lean happens in STEP 4 (rsync of the DBN directory).
