
## Scout O (Opus 5) — 2026-09-24 16:45 IST

- Report: `results/grossmann-rescout-s22/pair1-lorentzian/scout-O.md`, SHA-256 `b3b48770863ea353f265658c0783e0a3e3764cd2c3cbaced3ecfa03a0fb85269`.
- Verdict: **instrument** (confidence 0.85).
- (R-b) return: **YES-by-the-square** — the Lorentzian polynomial with von Mangoldt coefficients whose Lorentzian property is equivalent to Weil's RH for C is the volume polynomial of nef translates H₃ = Δ + g(C × pt) + g(pt × C), H₄ = Γ_{π^n} + (2g − 1)(C × pt) on C × C (nonnegative integer coefficients, M-convex support); Lorentzian at level n ⟺ |N_n − q^n − 1| ≤ 2g q^{n/2} (Milne Cor. 1.6 at (Δ, Γ_{π^n})), and over all n ⟺ RH for C; no prime-variable object with the iff avoiding C × C is exhibited (the BH Thm 2.10 dressing passes through C × C).
- Stop lines (a)–(c): none fired.
- Corrections of record offered: Z′/Z (not −Z′/Z) in the T variable (Milne M 58–59); eq. (2) at M 196; RH for C is the bound for all n (M 102), not n = 1.

## Scout F (Fable 5.1) — PAIR 1 W1-14 lorentzian-log-concavity — block appended Thu Sep 24 16:47:29 IST 2026 (append-only; written blind, nothing above this block was read)

- **Report:** `results/grossmann-rescout-s22/pair1-lorentzian/scout-F.md`, SHA-256 `c534362b69ec8cabed562b6f37b71880b3f0cc8a2db6cfac3a6dfa2341640444`.
- **Verdict:** instrument (confidence 0.88). **(R-b) return: YES-by-the-square.** The Lorentzian polynomial with von Mangoldt coefficients on the bottom rung is the volume polynomial of the four nef classes (C × pt, pt × C, Δ + (g−1)(C × pt + pt × C), Γ_π + (g−1)(C × pt + q·pt × C)) on C̄ × C̄ (Brändén–Huh Thm 4.6, `verify/bh-text.txt` 2352); its Lorentzian property is exactly |N₁ − q − 1| ≤ 2g√q (4 × 4 Gram matrix, block-diagonalized; report §2.4–§2.5, Appendix A), and over Γ_{πⁿ} exactly Weil's RH for C (Milne 100–111). No prime-variable Lorentzian object is exhibited in the two sources, `reports[14]`, or the record (§3.1, internal inventory statement). Refutation-shaped close: PRICING §1(c) line 64's YES close, verbatim in §4, plus a sharpened single-check sentence.
- **Stop lines (PRICING §4(i)):** (a) no — nonnegativity is required at lines 77–79, 85, 269–270, 312–314; (b) no — the nef translation exists with nonnegative Gram entries; (c) no — none found in the inventory. None fired.
- **New zoo rows:** IV.18 — does not bind (the certificate is an inertia condition n₊ ≤ 1, unwinding to signed first-order tests, Sector II; not a strip-positive cone element); IV.19 — kills nothing on the rung, fixes the currency over Q (clause (a) would be an evaluation with term count ≍ X(N), never a height-uniform estimate).
- **Record notes for the adjudicator:** the pricing's "−Z′/Z = Σ N_n T^{n−1}" (lines 51, 60) carries the s-form's sign; Milne line 58–59 has Z′/Z in T. The raw Gram on (C₁, C₂, Δ, Γ_π) is not itself in L²_n for g ≥ 2 (entries 2 − 2g, 2q(1 − g) < 0); the Lorentzian object is the nef-translated volume polynomial, same inertia by Sylvester.
- **refinement_compliance:** eight verdict sentences, all labeled internal (§7); no absence sentence in the verdict.
