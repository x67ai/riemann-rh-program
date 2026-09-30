# d4-infty-s36 — SHARED (writer's dated blocks; machine clock IST)

## Block 1 — launch (Wed Sep 30 17:26 IST 2026)

Writer: Opus (Claude Opus 5.5), per `BRIEF.md` (SHA-256 3763c902…6695). Inputs hashed at launch: s35 `NOTE.md` 49eb8e12…91f1 (agrees with the brief's 49eb8e12…); SPEC f7553e52…302d; `BARRIER-ZOO.md` 8e66cdc0…dae8 (699 lines; 58 entries, IV: 19 — IV.20 staged by s35, not inserted, so the next free number is IV.21 as the brief says); C3 e000c4ba…7a; `prederivation/pre_check.py` b847e904…c9ab (read, NOT reused — `verify/numbers_check.py` is independent code). Python 3.9.6, numpy 2.0.2, sympy 1.14.0, mpmath 1.3.0. Nothing outside `results/d4-infty-s36/` is edited; nothing is committed.

Read so far: BRIEF in full; s35 NOTE §0–§6 (all, including O1–O3 insertions and the E11-candidate flag in §3.1); `read-O.md` §1–§2.10, §4–§6; SPEC §1 (A1–A14) and §2 table; zoo header and count paragraphs (Session 34: 58 entries), III.6, III.20 (STATEMENT + all riders), III.21, IV.1 (+ riders), IV.10 (+ R-b′, + E3 rider), I.2, V.1–V.5; Milne 1509.00797 extraction pp. 8–11 (printed folios 8–11).

First adversarial findings recorded before writing (to be re-checked at the line in the NOTE):
- Milne p. 10 Example 1.7 prints d₂ = 1 and d₁ = deg f for a graph (C₁ ≅ C₁ × pt); the brief uses the transposed convention (d₁(Γ_ψ) = 1, d₂ = deg ψ). Harmless (def and 𝔅 are symmetric under 1 ↔ 2) — recorded as a convention note, not an erratum.
- Theorem S's contradiction needs (H-inj₂) at ONE prime p with log p > κ(1 + 2g)(1 + r_g), not at all primes: under the Weil package c is non-injective at every prime above that bound (sharpening).
- (H-adj) is the product form of the canonical class; a canonical-class form (K_Y in the domain of the index-one form, adjunction for each graph ≅ B) gives the same kill without the product assumption (candidate Theorem S(b); to be proved in §2).
- Proposition B: the zeta whose "RH" the index theorem expresses is exp(Σ_N (L_N/κ) T^N/N) = Π_ℓ (1 − T^{deg ℓ})^{−log ℓ/(κ deg ℓ)}, NOT Π_ℓ (1 − T^{deg ℓ})^{−1} (candidate erratum).
- Proposition A: Gelfond–Schneider suffices in place of Baker (the ratios log N_{[p^k]}/log N_{[p]} are algebraic, hence rational, hence 1 by squarefreeness) — candidate simplification; both transcendence theorems to be looked for on disk.
- Partition: P₄ as worded omits (H-mult) and the fiber classes, which Theorem S uses; the "triple in no cell" example (no fiber classes) is in ¬P₄, not in no cell.
