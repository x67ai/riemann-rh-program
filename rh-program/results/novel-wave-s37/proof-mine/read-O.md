# read-O — Opus reader on M2 `proof-mine` (dual-model check, standing orders 5, 7, 11)

Reader: Opus 5.5 (independent of the orchestrator's read; not waited for). Date: 2026-10-01.
Object read: `NOTE.md` (40 535 bytes, 322 lines, CLOSE T, writer Opus 5.5, 2026-09-30), charter §"Seed M2", `SHARED.md` blocks 0–8.
My scripts and logs: `verify-O/` (independent route: no import from `verify/`).

**VERDICT LINE:** (pending — filled when §1–§5 have landed)

Section status: §1 pending · §2 pending · §3 pending · §4 pending · §5 pending · §6 pending · §7 pending

## §1 The 14 rows at the page

Method: each cited passage opened in `sources/` (text layer; page images rendered with `pdftoppm` into `verify-O/*.png` for
Bombieri pp. 234–240 and Deligne pp. 283–285, 298, 301, where the text layer drops the formulas). Page numbers are the printed ones.

| row | source file : line (printed page) | the step named as the line | status |
|---|---|---|---|
| R1 Hasse (D) | `sutherland-18783-hasse-lecture8.txt` : 33–75 (pp. 1–2) | "noting that deg(r − π_E s) ≥ 0 … the discriminant t² − 4q cannot be positive" (l. 68–73) | VERIFIED |
| R2 Weil–Rosati (D) | `milne-…txt` : 1205–1221 (p. 21, Thm 1.27), 1241–1271 (p. 22, Cor 1.29, Thm 1.30), 1282 (p. 23), 294–327 (p. 5) | Thm 1.27, Tr(αα†) = (2g/(D^g))(D^{g−1}·α⁻¹D) > 0 "by dimension theory" | VERIFIED |
| R3 Weil 1941/48a (A) | `milne-…txt` : 358–375 (p. 6), 610–701 (pp. 11–12; σ(D∘D′) = def(D) l. 637–644; Φ l. 669–697; Thm 10 p. 54 l. 700) | effective representative + Φ = det(φ_i(D_j(P))), σ(D∘D′) ≥ 2g d₁(D) | VERIFIED (sketch assumes d₂(D) = g ≥ 2, l. 654; g = 1 is CCM (2.40)) |
| R4 Mattuck–Tate–Grothendieck (A) | `milne-…txt` : 462–600 (pp. 8–10), 744–750 (p. 13) | Thm 1.2 / Cor 1.3 (index 1); Thm 1.5, Cor 1.6, Ex. 1.7, "abs((Δ·Γ_π) − q − 1) ≤ 2gq^{1/2}" (l. 597) | VERIFIED |
| R5 Stepanov / Schmidt (C) | `bombieri-…txt` : 76–81, image p. 234 | quoted sentence only; proofs not read | UNVERIFIED (as the NOTE says; no verdict carried) |
| R6 Bombieri 1973 (C) | images pp. 236 (Thm 1, (5), (i)–(v)), 238–239 ((7), parameters), 239 (§III, ω₁ = q, ω₂ = 1), 240 ((8)–(10)) | §III: separable t, Galois C′ → P¹, twisted counts ν₁(C′, η), (8) + (9) ⇒ (10) | VERIFIED |
| R7 Deligne Weil I (B) | `deligne-…txt` + images: Thm (3.2) p. 284 (not 283), Lemmes 3.3–3.6 p. 284, (3.7) and the Rankin step "abs(α) ≤ q_x^{β/2 + 1/2k}" p. 285, Lemme (7.1) p. 298, (7.2) p. 300, (7.3) p. 301 | (7.1) at X = C × C via (7.3); family form (3.2) | VERIFIED |
| R8 Laumon / Weil II (B) | `laumon-…txt` : 142 (p. 133), 3227 (Thm 4.1.3, p. 204), 3260 (4.2.1.3, p. 205), 3305–3325 (Cor 4.3.1.1, Prop 4.3.2.1, p. 206) | (4.3.2.1) "une fonction méromorphe non constante f : X → D", then Fourier + purity | VERIFIED |
| R9 Kedlaya (B) | `kedlaya-…txt` : 17–21 (abstract), 82 (p. 2, Dwork = rationality), 204–207 (p. 5), 280–281 (p. 7) | R8 transcribed; Rankin squaring on a curve | VERIFIED |
| R10 Davenport–Hasse / Weil 1949 (C) | `milne-…txt` : 1305–1340 (p. 23) | Gauss-sum expression of the counts (at the page); the positivity step abs(g(χ))² = q ⇒ RH is NOT on p. 23 | PARTIAL: route VERIFIED, positivity step recalled (NOTE labels it) |
| R11 automorphic (—) | `milne-…pdf` PDF pp. 49, 51, 58 (checked by `pdftotext`) | not a proof of RH: consumers of RH | VERIFIED as a negative row; it is NOT one of the "12 proofs" (see F3) |
| R12 CCM (A) | `ccm-…txt` : 430–508 (pp. 9–11; (2.35) l. 433, effectivity l. 434, (2.40) l. 473), 530–556 (p. 12 dictionary), 1287–1291 (p. 29, Prop 6.2) | R3's positivity via Riemann–Roch on C | VERIFIED |
| R13 Hrushovski (A) | `hrushovski-…txt` : 156 (printed p. 4), 508–509 (printed p. 11), 6457–6464 (printed p. 115) | Ex. 11.4, Weil's positivity β | VERIFIED in content; pages cited as 3, 10, 114 are each ONE LOW (F1) |
| R14 named-not-read | — | Manin, Igusa, Quigley, Roquette, Kani, Weil II 1980, Stark, Stöhr–Voloch | UNVERIFIED (as labeled) |

**Tally.** Positivity step at the page: R1–R4, R6–R9, R12, R13 (10 rows). Route at the page, positivity step recalled: R10.
Negative row: R11. Not read: R5, R14. Three of the ten are not independent proofs: R9 = R8 transcribed (Kedlaya's abstract),
R12 = R3 restated (CCM p. 9), R13 = R3 for curves (Hrushovski p. 11). Independent proofs verified at the page: **7** (R1, R2, R3, R4, R6, R7, R8).
