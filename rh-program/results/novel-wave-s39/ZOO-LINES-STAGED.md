# ZOO LINES STAGED — wave 3 (Session-40 units), for the Session-41 zoo stream (BARRIER-ZOO.md NOT touched)

Consolidation agent (Opus 5.5), 2026-10-01, Session 41. Brief: `DIGEST-BRIEF.md` (Deliverable 2). Format of
`results/novel-wave-s37/ZOO-LINES-STAGED.md`: staged text in the zoo's own format (riders as `- **[RIDER <date>, Session <n> (<source>) —
<headline>.]**`), the zoo's status vocabulary (BARRIER-ZOO.md line 7: `formalized-in-Lean`, `computationally-verified`,
`literature-verified`, `sweep-certified`, `program-adjudicated`, `recalled-unverified`). Every quotation carries its file and line; line
numbers are those of the post-read files on disk at 16:57 IST (SHA-256 prefixes in `SHARED.md` block 11). Paths are repository-relative.
`<ENTRY-DATE>` marks the one field the zoo stream fills. The orchestrator decides wording and inserts; nothing here is inserted.
Companion: `insights-digest.md` (this folder) §B B3–B4, §F.1 (b), (f) and (a).

## Zoo state at staging (read 2026-10-01 17:24 IST)

`BARRIER-ZOO.md`: 788 lines, SHA-256 `0a0a832d10cae4e61fae9befda358519e74181e7961a948b5c1c1a84a7df7587`; **64 entries — I: 11, II: 5,
III: 21, IV: 22, V: 5** (the Session-40 paragraph, line 43: "11 + 5 + 21 + 22 + 5 = 64"). I.2 occupies lines 82–93: STATEMENT 84 …
STATUS 88, riders 89 (the (α, β) frontier, Session 38), 90 (`conj-O-s38`), 91 (`dz-half-s39`), 92 (the S5 withdrawal, `u-offsurgery-s39`
+ `s5-multiplicity-s40`), 93 (thresholds and obstructions, Session 38); 94 is blank, 95 is `### I.3`. The unit cross-reference rows
end at line 758 (`| unit \`fejer-form-s39\` …`), 759 blank.
What is already in the zoo from the four Session-40 units (not restaged): rider 92 carries s5m's n_K certificate and says "The unit's
structure theorems T1–T4 (multiplicity, freeness and surgery for ℕ-supported systems) are [single-check; read owed]" (line 92) and
names "`local-greedy-s40` Lemma 4.1" (line 92); no line yet carries Theorem 1.6, S8, T2–T3 as dual-read, or S7^{≤2}'s K-theorem.

## Insertion map (enter bottom-up, so every line number below stays valid)

| order | block | insert after the text of | kind | entry count after it |
|---|---|---|---|---|
| 1 | (iv) cross-reference rows | line 758, the row "\| unit \`fejer-form-s39\` …" | 4 table rows | 64 |
| 2 | (i) I.2 rider — Theorem 1.6 and its use | line 93, I.2's last rider (thresholds and obstructions) | rider | 64 |
| 3 | (iii) I.2 rider — S7^{≤2}, the capped prime-local system | line 92, the S5 withdrawal rider | rider | 64 |
| 4 | (ii) I.2 rider — T1–T3 of `s5-multiplicity-s40`, dual-read | line 92 (so it lands above (iii)) | rider | 64 |
| 5 | C (entry-count paragraph, optional) | line 43, the Session-40 paragraph, one blank line before | paragraph | **64 — unchanged** |

Final order inside I.2: 92 (S5 withdrawal) → (ii) → (iii) → 93 (thresholds) → (i). Count arithmetic: no entry is added; 11 + 5 + 21 +
22 + 5 = 64.
Why these homes. All three are model-world facts about Beurling systems on or near ℕ, the subject of I.2 ("The Beurling counterexample
factory"). (ii) completes rider 92, which defers T1–T4 to a read now done; it goes directly under it. (iii) is the capped counterpart of
the S5 candidate whose withdrawal rider 92 records, and rider 92 already names Lemma 4.1. (i) belongs after the thresholds rider (93):
Theorem 1.6 is RELATIVE in that rider's sense — it says nothing about (ℙ, ℕ), whose count undershoots — and it reorganizes the
refutation side of Conjecture U stated in rider 89. None is a Group-IV kill ("each extracted from a kill", zoo line 428): (i) is a
theorem with a conditional refutation route, (ii) a structure theorem, (iii) a conditional candidate.

---

## Block (i) — RIDER on I.2, Theorem 1.6 and its use (insert per the map, row 2; no count change)

- **[RIDER <ENTRY-DATE>, Session 41 (unit `free-greedy-s40/theory`: `results/free-greedy-s40/theory/NOTE.md` §0, §1.6–§1.7, §3.0; `read-F.md` AGREES-WITH-CORRECTIONS (Theorem 1.6 re-derived in Session 40, the whole NOTE in Session 41), `read-O.md` AGREES-WITH-CORRECTIONS, F1–F3 and 13 minor, 27 pairs applied; entered at the Session-41 zoo stream) — one-sided integer regularity forces a real zero, so Conjecture U on never-undershooting systems reduces to ONE integer bound; for the free greedy system S8 that bound, Lemma B_ρ, is NOT proved.]** *Theorem 1.6* (NOTE lines 103–106): "Let P be any discrete Beurling system … ρ ∈ (0, 1), E(u) := N(u) − ρ(u − 1) − 1, and suppose (A) E(u) ≥ −c for all u ≥ 1, some c ∈ [0, 1); (B) E(u) = O(u^θ) for some θ < 1 (no constant needed). Then for θ < σ < 1 … ζ_P(σ) ≥ 1 − c − ρ/(1 − σ). If σ₀ := 1 − ρ/(1 − c) > θ, then ζ_P has a real zero σ* ∈ (σ₀, 1) … P is an [α, β]-system with α ≥ σ* and β ≤ θ." Its proof uses neither discreteness nor positivity of the prime measure (`read-O.md` A1, l. 372–374; Remark 1.6′, NOTE line 161, in the form R(u) := N(u) − ρu ≥ r₀ > 0, θ < r₀/(r₀ + ρ)); the continuous template dN = δ₁ + ρdx (Diamond 1970 p. 24) is its equality case, zero exactly 1 − ρ (`read-F.md` l. 9); and "ℕ escapes only because ⌊u⌋ − u ≤ 0" (NOTE lines 13–14) — ℕ "has ζ < 0 on (0, 1) and no real zero" (line 139). *Use* (the candidate S8(ρ), `results/free-greedy-s40/CHARTER.md` §1: a g-prime is placed whenever the deficit reaches ½, so E > −½ by construction): Corollary 1.7 (line 115), "(ii) If ρ ≤ ¼ and θ ≤ ½ − ρ: α > 1 − 2ρ ≥ max{½, 2θ} ≥ max{½, 2β}, so Conjecture U is false"; the Dichotomy (line 208), "For each ρ < ¼: either Conjecture U fails, or β(S8(ρ)) > ½ − ρ", certified by finite real-axis evaluations (Cor. 1.7(iii)) as β(S8(π/16)) > 0.395 and β(S8(π/32)) > 0.445 if U holds (lines 209–210). The data: sup E ≈ 0.05·log²x (π/16) and 0.03·log²x (π/32) to 10¹¹ (`results/free-greedy-s40/compute/NOTE.md` line 30; two producers to 10¹⁰, the Session-41 reader's generator proving the event ordering there). *Not proved:* **Lemma B_ρ** (theory NOTE line 25), "for one ρ < ¼, the integer error of S8(ρ) is O(x^θ) for some θ ≤ ½ − ρ"; "Not even E = o(x) is proved" (`results/lemmaB-s41/CHARTER.md` §1). Its two-sided sieve form is FALSE (`read-O.md` F1 and A3: square-root cancellation in the Legendre remainder would force ψ_P ~ 2e^{−γ}x through Diamond–Zhang Thm 5.10; the remainder carries the bias (1 − 2e^{−γ} + o(1))u/log u). KILLS / RETURNS: any brief refuting Conjecture U through S8 or another never-undershooting rule by two-sided cancellation in the Legendre remainder (false); any brief deriving B_ρ from a zero-density bootstrap — such estimates give g-prime gaps x^{1−1/A+ε}, at best x^{½} (`read-F.md` l. 31–32, the orchestrator's pricing, single-check), while B_ρ has the strength of gaps x^θ, θ < ½ − ρ (Prop. 2.1). TEST: (1) is the proposed system never-undershooting (E ≥ −c)? Then α ≥ 1 − ρ/(1 − c) costs only a qualitative (B), and the brief's whole burden is the integer bound; (2) evaluate the brief's integer bound on ℕ (ρ = 1, E = −{x}): a bound that would force a real zero there is false. Status: program-adjudicated — dual-model (writer Opus 5.5, Session 40; readers Fable 5.1 and Opus 5.5, Sessions 40–41); novelty "new as a statement on a printed core: Bateman–Grosswald 1964 p. 367; Phragmén" (`read-F.md` l. 35; `read-O.md` l. 221–224 — the positivity-plus-pole mechanism is printed for Epstein zeta, the last step is Phragmén's, as in Révész IMRN 2023); Lemma B_ρ OPEN, the subject of `results/lemmaB-s41/` (seven units, Session 41). **BINDS:** B2 (refutations of Conjecture U), C2.

---
