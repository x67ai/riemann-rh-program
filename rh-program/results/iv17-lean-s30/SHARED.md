# G8 / IV.17 — SHARED log (builder Fable 5.1, then checker Opus 5); Session 30, 2026-09-29

Brief `BRIEF.md` SHA-256 `9aabf0dbfb74e602941c490a2a3d417e825f33cfad11e537e5c3ff45ee2ffd70`. Every block dated by `date`.

## [builder] Tue Sep 29 00:50:30 IST 2026 — deliverable 1 landed: `TYPING-NOTE.md` (+ the probe `typing-probe.lean`)
Both Zeta23 files read in full. The mark type enters the Parseval algebra only through the cast `(m k : K)`, used as an opaque ring
element; the ℂ step uses one cast lemma (`map_intCast`). Probe through the built clone: rational marks do NOT cast into a general
`CommRing` (need `Field`); `map_ratCast`, `Complex.ofReal_ratCast`, `Rat.cast_intCast` exist; `decide +kernel` closes the three
ℚ facts on `ZMod 65` (mass 64, Σm² = 256/3, N_d = 48) in one 8.53 s file. Decision: Parseval stated once for a general coefficient
vector `dftVec` over the integer file's `[CommRing K] [IsDomain K]`, with `dftMark` (ℤ) and `dftMarkQ` (ℚ, `[Field K]`) as `rfl`
instances. Stop lines (i) and (ii) do not fire. Note: the ℚ kernel facts depend on all three standard axioms (not `[propext, Quot.sound]`).
SHA-256 TYPING-NOTE.md = fd3b5464000352689645b0a73f36a48970b526bb3aa18ba87df8a2d71e37fb7d.
Next: `Zeta23/PairCeiling/GridParsevalRat.lean`, built alone.
