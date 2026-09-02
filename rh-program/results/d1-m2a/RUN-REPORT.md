# M2a RUN-REPORT — what M2a IS after Session 14, in trust vocabulary

**Date:** 2026-09-03 (Session 14, D1 M2a; final-audit agent; companion to `AUDIT.md`, verdict REPAIRED-CLEAN, 0 fatals).
**One sentence:** Lane B of the Polymath15-row-2 barrier certificate (Theorem 1.2's hypothesis (iii) in its simplified
box form) is **kernel-checked modulo the displayed hypotheses H2-B and `hHol` (producers untrusted)** from two independent
untrusted producers; the theorem "Λ ≤ 0.2 in ray form" is **not proved** and nothing about Λ changes — **0 ≤ Λ ≤ 0.2**
(Rodgers–Tao; Platt–Trudgian Corollary 2, exact height 3 000 175 332 800) remains the bracket of record. Never "fully
machine-checked". Never "Λ < 0.2".

## 1. What exists (files, and their trust tier)

| object | file(s) | tier |
|---|---|---|
| the contract | `SPEC.md` v1.0 + §14 errata (2026-09-03), `barrier-schema.json` | normative (shape + semantics); the errata change no check or hypothesis |
| the Lean checker + soundness (Lane B) | `lean/Zeta23/DBN/BarrierCert.lean` (1 092 lines) | **Lean-proved**: `cert_of_checkBarrier`, `cert_of_checkBarrier_xy`, the rectangle argument principle on a general rectangle (`rectArgPrincipleGen`), the half-plane FTC lemma, log-derivative additivity — axioms `propext, Classical.choice, Quot.sound` only |
| the instance (both legs) | `lean/Zeta23/DBN/Instance02.lean` + `Instance02/` (115 modules, 23 965 lines) | **kernel-checked integer facts** (`decide +kernel`): 111 per-prism `checkPrism … = true`, 2 chain facts, 2 monolithic `checkBarrier … = true`; the four instantiated theorems `row2_barrier_{mp,arb}[_xy]` are generic in G |
| the producers | `producer_arb.py` (Arb/FLINT), `ft_mp.py` + `producer_mp.py` (mpmath-ball) | UNTRUSTED by design; each with a derivation record (D-A1…D-A18, D-F1…D-F9) and validation runs; independently audited (`AUDIT.md` §1–§2) |
| the transcripts | `transcripts/row2/` (mp: 39 prisms, 7 176 rows, K = 10²⁴, A = 10¹²), `transcripts/row2-arb/` (Arb: 72 prisms, 10 771 rows, K = 10¹², A = 10⁶) | producer output; accepted by three checkers (`barrier_ref_checker.py`, `checker_ref.py`, the kernel) |
| the cross-checks | `crosscheck_instance02.py` runs at all 111 seams of both chains (37 172 overlapping pairs, 0 disjoint); the audit's direct evaluation (36 fresh points, 12 argument rows, 0 failures) | producer-side evidence for H2-B (not a proof) |
| the Gomila conversion | `gomila/` (exact replay of the sealed 883-prism log; kernel-checked seam chain; 29-prism two-leg spot sample) | screen evidence only; NOT a record |
| the audit | `AUDIT.md`, `audit/` | this session's adversarial pass |

## 2. Exactly what is displayed, and exactly what the kernel checks

**Displayed (assumed, named, never hidden), for the Lane-B theorems as they stand:**

* **H2-B** = `BarrierEnclOK G row2Barrier{MP,ARB}` — per prism: some f holomorphic on an open U ⊇ R is enclosed by the
  seam rows (`W1.RowEnclOK`, verbatim), ‖G τ − f‖ ≤ E/K on ∂R, and ‖G t − G τ‖ ≤ D/K on ∂R for t in the prism. This is
  where the producers' interval arithmetic AND Polymath15's Theorem 1.3 (through E) enter. For the instance
  G t z = H_t(z)/B_t(z).
* **`hHol`** — G t is holomorphic on an open neighborhood of R for every t ∈ [0, t₀] (for the instance: from the
  entirety of H_t and B_t ≠ 0 near R — neither is in the trusted layer yet).

**Not yet displayed because the theorem that would consume them does not exist:** H1 (`ZeroVerification
(116733/200000) 2500000097429`, discharged by PT Theorem 1 with margin 500 175 235 371), H2-A and H-TAIL (Lane A), H3
(`Polymath15Bridge' ∧ HtEntire`).

**Kernel-checked (integer facts on literals, `decide +kernel`, no `native_decide`):** C-B0…C-B13 for every prism and both
chains — 17 947 rows; the audit re-checked 11 corruptions (all rejected) and printed axioms on all 119 Instance02
declarations (`audit/instance02-axioms-all.log`).

**Lean-proved (theorems, standard axioms):** everything in `BarrierCert.lean` — no Rouché, no homotopy, no zero-continuity
in t; the time step is the fixed-t argument principle applied twice plus one FTC lemma on a segment.

## 3. What the Λ ≤ 0.2 instance establishes today, and what it does not

**Establishes** (modulo H2-B for the transcript and `hHol` for G = H_t/B_t): for every t ∈ [0, 93/500] and every
z ∈ [X, X+1] × [16733/100000, 1], X = 5 000 000 194 858: **H_t(z) ≠ 0** — Polymath15 Theorem 1.2's hypothesis (iii) in the
simplified box form of p3, from two independent transcripts that agree cell-wise at every seam of both chains. The E
rows are ≥ the paper's pointwise majorant at every corner tested (slack ≤ 5·10⁻¹¹); the value and argument rows
contain independent direct evaluations at every fresh point tested.

**Does not establish:** Λ ≤ 0.2, or any statement about Λ. Missing: (ii′) — the final-time asymptotic lane (no
producer has run it; `checkAsym`/`cert_of_checkAsym` not written; Lemma T's constants not certified); the bridge
`Polymath15Bridge'` and `HtEntire` in the trusted layer (`Defs.lean` v1.1 — BLOCKING, and `Polymath15Bridge` v1.0 as it
stands is not instantiable, SPEC §3.2); L-B3 (B_t holomorphic and nonvanishing near R); the glue theorem
`lambda_le_point2`. Also not established: Theorem 1.3 itself (M2b), the entirety of the Lean `Ht` (M2b), Theorem 1.3 at
t = 0 (a recorded limit argument inside H2-B; the audit re-derived it, M2b should prove it).

**The record is unchanged:** 0 ≤ Λ ≤ 0.2. PT's Corollary 2 rests on Polymath15 Table 1 row 2 (barrier verified
numerically by the paper; asymptotic hypothesis argued from the N₀ lower bound and the §8.3/§8.5 method — SPEC §5.5);
M2a's Lane B is an independent, kernel-checked re-verification of the barrier half of that row, nothing more.

## 4. The Gomila claim (steps 3–4 of `results/d1-m0/gomila-screen.md`): status

**screen-open.** Step 3: the sealed log converts exactly in its chain half (883 seams from exactly 0, kernel-checked
`checkBarrierChain`; every printed gate margin replays exactly; their gate is C-B12 with the mesh term in the floor;
audit re-replay: 0 discrepancies) and is NON-EXECUTABLE in its row half (no per-segment enclosures are sealed). Step 4:
29 prisms (the ten thinnest + 19 evenly spaced) produced by BOTH D1 legs on Gomila's box at Gomila's seams — 8 198
overlapping pairs, 0 disjoint; 0 contradictions against their printed scalars; D1's own enclosures would certify each at
their prism length. Not screen-pass (no rows to accept; 854 prisms unsampled; their Lane A and all-N tail lemma not
converted). **Not a record. M2a′ candidate at most.** Completing it costs ≈ 1 h (Arb) / ≈ 10 h (mp) of producer time for
a full 883-prism D1 transcript of their row plus the tail decision — and yields nothing about Λ until the same missing
pieces as §3 exist for row 2.

## 5. The cost curve (measured, this session)

| stage | measured | per unit |
|---|---|---|
| mp producer, row 2 (N₀ = 630 783) | 1 233 s wall for 39 prisms × 184 rows (+ 2 × 421 s moments, once) | ≈ 32 s/prism, 0.17 s/row; 45 ms per box evaluation |
| Arb producer, row 2 | 144 s for 72 prisms (64–289 rows) (+ 61 s moments, once) | ≈ 2 s/prism; 0.3 ms per evaluation |
| cross-check re-runs | Arb at 39 mp seams 104 s; mp at 72 Arb seams 2 338 s | 2.7 s / 32 s per prism |
| JSON → Lean emission + back-parse | seconds | — |
| Lean per-prism module build (serial, one `lake`) | 137 s (mp, 41 modules) / 237 s (Arb, 74 modules) clean | 2.9–3.9 s per module, import-dominated; kernel ≈ 5 ms/row inside |
| monolithic `decide +kernel` on both literals | 28.2 s for 17 947 rows | 1.57 ms/row wall (≈ 1.4 net of imports) |
| audit direct evaluation (independent, 256 bits) | 1.6 s per boundary point | 630 783 terms per sum |
| Gomila spot sample (29 prisms, N = 690 988) | Arb 104 s (incl. 67 s moments); mp 922 s + 902 s moments | full 883-prism row: ≈ 1 h Arb / ≈ 10 h mp |

The SPEC §7.6 "serial hours" projection was for 5·10⁶ rows; the actual instance is 280× smaller. Lane A's cost is the open
question: with the crude Lemma T, N₁ ≈ 6–8·10⁶ windows must be covered by rows (SPEC §5.4); a mollified tail would
shrink it but is a different lemma (out of the v1.0 contract).

## 6. Next steps, in order (the exact cut line and what lies beyond it)

1. **`Defs.lean` v1.1 — BLOCKING** (trusted layer; ~40 lines + a dated deviation record in the file header and in the
   design note §7): replace `Polymath15Bridge` by `Polymath15Bridge'` (SPEC §3.3; the v1.0 canopy hypothesis is not
   dischargeable by any finite certificate, SPEC D-3.2), add `alpha`, `M0`, `Mt`, `Bt` (SPEC §3.4) and `HtEntire` (§3.5).
2. **L-B3** (`Bt` differentiable and nonvanishing on an open neighborhood of the instance rectangle; ≤ 100 lines
   expected; fallback = display it, label amended).
3. **Lane A**, both producers (SPEC P-9/P-10: the mollified window floor T uniform in N ∈ [N₋, N₊] and y ∈ [y₀, yA]; the
   Theorem 1.3 defect E at the window's worst corner; Lemma T's Q₁…Q₄, E₁ with (S1)–(S4) verified), then `checkAsym` +
   `cert_of_checkAsym` + L-A1/L-A2 in Lean, then the asymptotic transcript kernel-checked and cross-checked per row.
4. **`lambda_le_point2`** in `Instance02.lean` (the glue L-G is already type-checked in `lean-shapes-scratch.lean`): from
   H1 (exact), Lane A's (ii′), `row2_barrier_*_xy` at H = Ht, B = Bt as (iii′), and `hH3.1`; finish with
   t₀ + y₀²/2 ≤ 1/5. Only then may a public sentence read "Λ ≤ 0.2 in ray form, kernel-checked modulo H1, H2, H3".
5. **Packaging (design-note item (f))**: comparator config, the `PrintAxioms` audit folded into `lean/README.md`, a
   v1.1 of `SPEC.md`/schema that folds in §14 (per-lane trust label; (14) with the overline; the n² exponent).
6. **The argument principle is already discharged for this milestone** (`rectArgPrincipleGen` is a theorem; no H-AP
   analogue is displayed anywhere in Lane B) — there is no "v1.1 argument principle" item left for M2a; the W1 v1.1
   discharge carried over.
7. **M2b (horizon, NOT scheduled):** prove `Polymath15Bridge'` (Theorem 1.2), `HtEntire`, Theorem 1.3 with its t = 0
   limit, and define f_t in Lean so that H2-B's existential f becomes the concrete approximant — this is what turns
   "modulo H2, H3" into "modulo H2's producer arithmetic only".
8. **Gomila M2a′ decision** after step 4 exists for row 2: a full 883-prism D1 transcript of their row (≈ 1 h Arb / 10 h mp)
   + the tail decision (SPEC §11) — at near-zero Lean cost, as a second row literal for the same theorem.

**Cut line, stated plainly:** everything in steps 1–4 is absent from the working tree at 2026-09-03 02:15 IST. Item (e) of
the design note's work breakdown is PARTIAL (Lane B complete twice and kernel-checked twice; Lane A and the glue not
started); item (f) is not started. No program Lean file was changed by the audit.
