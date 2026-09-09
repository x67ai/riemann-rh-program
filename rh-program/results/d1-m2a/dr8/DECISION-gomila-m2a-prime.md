# The Gomila M2a′ decision (Session 20, queue item 2c)

**Written 2026-09-10 by pricing agent 2c (Claude Fable 5.1).** Brief: `results/d1-m2a/dr8/BRIEF.md` §2c. This file is a PRICING and a DECISION, not an implementation: no producer ran, no Lean was edited, no build was launched, no network. Authorities read: `results/d1-m2a/SPEC.md` §3.6, §5 (Lemma T, §5.4), §7.6, §11; `results/d1-m2a/RUN-REPORT.md` §4, §5, §6 (item 8 and the dated notes); `results/d1-m0/gomila-screen.md` (§2, §4 steps 2 and 5, §7, §9); `results/d1-m2a/INSTANCE-REPORT.md` §3.4, §5; `results/d1-m2a/lane-a/{PLAN.md §2.3–§4, EMIT-NOTES.md §6, plan_rows.py}`; the Lane B timing records `results/d1-m2a/{row2-summary.md, mp-leg-notes.md, arb-row2-chain-stats.txt, arb-leg-notes.md, kernel-time.log}` and `results/d1-m2a/gomila/checker-ref-spot-{arb,mp}.txt`; `results/d1-m2a/packaging/FIDELITY.md`; `lean/Zeta23/DBN/{Defs,Instance02}.lean` (the shapes `ZeroVerification`, `Polymath15Bridge'`, `row2_ray_mp`, `hH1_row2`, `row2_bound_le_point2`); the siblings `dr8/PRICING-fDH.md`, `dr8/PRICING-M3-ledger.md`; `KICKSTART.md` items 5 (thermal) and 10; `STATUS.md` (Session-20 queue); `directions/D1-certified-refutation-arm.md` (D-R2, "Current frontier", the Session-20 pricing decisions). Four float64 probes of the UNTRUSTED planning model `lane-a/plan_rows.py` were run in the scratchpad at Gomila's tuple (≈ 25 s in all, one process; Appendix A verbatim) — the same probe grade as 2a's and 2b's; NOT a certificate, NOT a producer run. Exact arithmetic (Python `fractions`) for every rational in §2. U.S. English.

Status line: §0 one-paragraph answer — DONE; §1 re-pricing — DONE; §2 what it buys — DONE; §3 cost against 10(d), the honest alternative — DONE; §4 DECISION — DONE; §5 refutation-shaped close — DONE; Appendix A (probes verbatim) — DONE; Appendix B (owed record corrections, for the orchestrator) — DONE.

## 0. One-paragraph answer

**Decision: NO now; GO later on a named trigger (§4).** The re-pricing overturns the premise M2a′ was carried on ("≈ 1 h Arb / 10 h mp + the tail decision, at near-zero Lean cost", RUN-REPORT §6 item 8). Lane B is as cheap as advertised — D1's own adaptive chain on Gomila's box costs ≈ 35–40 min (mp) and ≈ 4 min (Arb), two heavy jobs; even a prism-for-prism transcript at their 883 seams is ≈ 8 h (mp) / ≈ 20 min (Arb) (§1.1). **Lane A is the block, and it is not a matter of hours:** at Gomila's tuple (t₀ = 129/800, y₀ ≈ 0.18727) D1's v1.0 window floor — the Euler-2 mollified bound of P-9 that Lane A's two legs implement, modeled by `plan_rows.py`, which reproduces the certified row-2 floors to 4–5 digits — is NEGATIVE on the windows N ∈ [690 988, ≈ 2.0·10⁶] at y near y₀ (−0.40 at N_start; positive only from N ≈ 2.02·10⁶, i.e. x ≈ 5·10¹³, sixteen times beyond Platt–Trudgian's height), and the least y₀ the floor certifies at any H1-licensed X and this t₀ is ≈ 0.286, which gives t₀ + y₀²/2 ≈ 0.202 > 0.2 (§1.2). The crude Lemma T tail closes only at N₁ ≈ 2.3·10⁷, not the "7–9·10⁶" of SPEC §11 (§1.3). So M2a′ at Gomila's tuple needs a NEW floor lemma (Polymath15's finer mollifier, or Gomila's own "Native Triangle" bound — unrefereed), implemented on both legs and audited — 2–3 agent-sessions with an uncertain outcome — before any producer hour is worth spending; and if that lemma turns out to need singleton-N rows as Gomila's did (3.1·10⁶ of them), the mp leg alone is ≈ 4 months at the measured 13.5 s/row. What a finished M2a′ would buy is real but bounded: the program's OWN ray-form certificate of Λ ≤ 17879/100000 at their X, modulo H1 (Platt–Trudgian at 3 000 000 092 913.5, margin 175 239 886.5 — the precise Theorem-1 figure is load-bearing), H2 (D1's enclosures, plus the new floor lemma as a displayed H2-A′) and H3 — not a verification of Gomila's chain, not a record, and citable only as the program's own unrefereed candidate (§2). Against KICKSTART 10(d) and the sponsor's lean-budget rule this is the wrong purchase today: it pulls two to three sessions plus a heavy-job slot from lanes with signal, changes no belief (29/29 barrier prisms already agree; a full pass is the expected outcome), creates no zoo entry and no new theorem shape (§3). The honest alternative costs nothing: the claim stays "unrefereed, screen-open, not a record" (screen §7 caveats 1–5), and the record gains one instrument fact — the v1.0 floor does not reach their tuple — which also corrects SPEC §11's tail figure (Appendix B). A by-product of the probe, for a separate brief if the orchestrator wants a program-own sub-0.2 instance later: at t₀ ≈ 0.175 the v1.0 instrument's floor certifies y₀ ≈ 0.204, i.e. a program-own row at ≈ 0.1957 in ray form with no new lemma (§3.3) — same candidate-not-record status, priced there, not decided here.

## 1. Re-pricing with the Session-19 numbers

### 1.1 Lane B — the barrier on Gomila's box [X, X+1] × [1809/10⁴, 1], t₀ = 129/800, both legs

Measured bases, named by file:

| record | leg | measurement |
|---|---|---|
| `results/d1-m2a/row2-summary.md` (last lines), `mp-leg-notes.md` line 104 | mp, row 2 | "prisms: 39; total rows: 7176; wall: 1233 s (20.6 min); mean 31.6 s/prism" — "26–36 s per prism (rising slowly with t as the Taylor orders in t grow)"; stored moments "421 s per series" × 2 (`mp-leg-notes.md` line 15, `RUN-REPORT.md` §5) |
| `results/d1-m2a/arb-row2-chain-stats.txt`, `arb-leg-notes.md` §1 | Arb, row 2 | 72 prisms, 10 771 rows (64–289 per prism), "total producer seconds 144"; moment cache 61.4 s |
| `results/d1-m2a/INSTANCE-REPORT.md` §5.2, `gomila/checker-ref-spot-{arb,mp}.txt` | both, Gomila's box at 29 of their seams (N = 690 988) | Arb "29 prisms, 104 s incl. a 67 s moment computation" → 1.28 s/prism net; mp "922 s after 2 × 451 s of moment computation" → 31.8 s/prism; rows per prism: mp 182 (all 29), Arb 64–180 (mean 107) (counted this session from the spot files) |
| `results/d1-m2a/kernel-time.log` | Lean | monolithic `decide +kernel` on both row-2 literals (17 947 rows): 28.18 s real → 1.57 ms/row; per-module builds 137 s (mp, 41 modules) / 237 s (Arb, 74 modules), `RUN-REPORT.md` §5 |

Two variants, priced separately because they buy different things:

| variant | what it is | mp leg | Arb leg | rows (mp / Arb) | heavy jobs | wall (legs in parallel) |
|---|---|---|---|---|---|---|
| **B-883** — prism-for-prism at Gomila's 883 seams (`gomila/gomila-chain-manifest.json`) | the transcript that would let the screen's step 3 say "checker accepts D1's transcript at their seams" | 883 × 31.8 s ≈ 28 100 s + 902 s moments ≈ **8.1 h** | 883 × 1.28 s ≈ 1 130 s + 67 s ≈ **20 min** | ≈ 161 000 / ≈ 94 000 | 2 (half the cap of 4, KICKSTART item 5) | ≈ 8.1 h, mp-bound |
| **B-own** — D1's own adaptive seam chain on their box (C-B13 needs only a chain from 0 to t₀; D1's D-bounds are 3–50× tighter than their box-uniform D_t, INSTANCE-REPORT §5.2, so D1 needs ≈ 40–80 prisms as at row 2, not 883) | the transcript an M2a′ THEOREM needs | ≈ 40 prisms × ≈ 32 s + 902 s moments ≈ **35–40 min** | ≈ 75 prisms × ≈ 1.5 s + 67 s ≈ **3–4 min** | ≈ 7 300 / ≈ 11 000 | 2 | ≈ 40 min |

Scaling notes, stated not glossed: Gomila's N = 690 988 is 9.5 % above row 2's 630 783, so per-evaluation cost is ≈ 10 % higher than row 2's (already inside the spot-run figures, which were measured on their box); t₀ = 0.16125 < 0.186 means a slightly shorter chain; the prism count of B-own is a projection from row 2 (39 mp / 72 Arb), not a measurement — a factor 2 either way changes nothing below. The 29-prism spot sample has every one of the ten thinnest prisms; D1's own gate passed at their prism length on all 29 with both legs, so B-883 is expected to pass prism-for-prism — which is exactly why its information value is low (§3.1).

### 1.2 Lane A at Gomila's tuple — the block

**The Session-19 instrument.** Lane A rows are width-independent: PLAN.md §3.1 — "mp (prec 288, N_c 10 000, m 2 000, 8 pieces): 13 rows, 12 010 windows, 177.8 s, 13.3–13.8 s per row — width-independent: 13.3 s (1 window), 13.5 s (1 000), 13.7 s (10 000)"; "Arb (prec 320 …): 6.2 s, 0.5 s per row — width-independent likewise"; "Per row: mp ≈ 260 rows/h, Arb ≈ 7 000 rows/h. Because a row's cost does not depend on its width (M-8: every G is a 10 000-term head plus 4 000 integrand evaluations, whatever N₊), 'windows per hour' is a property of the partition". The tail row (PLAN §3.2): Arb 12.3 s, mp 415.2 s, of which `--direct` (the optional full-sum validation over N₁ terms) is all but 1 s. Lean (EMIT-NOTES §6): `lake build …Asym_mp` 3.18 s, `…Asym_arb` 2.53 s, `decide +kernel` on the literals "2.02 ms / 4.1 ms", root build 15.83 s. So IF the floor lemma reached their tuple, Lane A at Gomila's row would be ≈ 5 rows + tail ≈ **1.5 min + 31 min (`--direct` at N₁ ≈ 2.3·10⁷, scaled ×4.5 from 415 s at 5.14·10⁶) on mp, ≈ 3 s + 1 min on Arb**, one module per leg, kernel milliseconds. That is the pricing the brief expected. It does not apply, for the following reason.

**The floor is negative at their tuple.** `lane-a/plan_rows.py` is the float64 planning model of the certified floor (derivation M: P15 Lemma 10.1 with the Euler-2 mollifier, uniform over a sub-box N ∈ [N₋, N₊] × y ∈ [ya, yb]); PLAN §3.0 records that it "agree[s] with the model to 4–5 digits" on all 13 certified pricing rows (e.g. singleton N₀, piece [y₀, 0.18]: model 0.02756, certified 0.027556). This session the model was re-run unchanged except for the four constants (`T0 = 0.16125; Y0 = 0.187272; YA = 0.8231039; N0 = 690988`; the row-2 value 0.02756 re-reproduced first as a sanity check — Appendix A, probe 2). Findings, all float64 and UNTRUSTED, but at the precision the row-2 comparison licenses:

* At the bottom of the y-range (a 2.8·10⁻⁵-wide sliver at y₀″ = 0.187272), the floor T is **−0.399 at N = 690 988, −0.242 at 10⁶, −0.0035 at 2·10⁶, +0.219 at 5·10⁶**; at y ≈ 0.3 it is +0.039 at N_start; at the top (y ≈ 0.823) +0.54. For comparison the same sliver at row 2's tuple gives +0.028 at N₀ (certified 0.027556). The crude Step-1 triangle inequality (SPEC §5.4 step 1, no mollifier) gives 2 − A − B = **−1.53** at N_start (row 2: −0.70).
* The least y at which the floor exceeds a working E-ceiling (2.5·10⁻⁷) on the singleton window N = 690 988 is **y ≈ 0.2856**, and the same at N = 691 008 — the largest N_start any H1-licensed X allows, since X ≤ 2 × 3 000 175 332 800 gives N(X) ≤ 691 008. So with the v1.0 floor the smallest certifiable y₀ at t₀ = 129/800 gives **t₀ + y₀²/2 ≈ 0.2020 > 0.2**: no sub-record bound at this t₀ is reachable with the instrument as built, at any X Platt–Trudgian licenses.
* Why: the floor is 1 − Σ (mollified moduli) with σ ≥ (1 + y)/2 + (t₀/2) log N; at t₀ = 0.16125 the (t₀/2) log N term is 1.08 against 1.24 at row 2 (t₀ = 0.186), and b_n = exp((t₀/4) log² n) shrinks less than n^{−σ} gains; the deficit is 0.4 at the corner, not a rounding.
* What this says about Gomila's finite lane — nothing contradictory, and something clarifying. Their sealed floors are per-N singletons with a worst floor T_min = 791 366/10¹² ≈ 7.9·10⁻⁷ against E_max ≈ 2.33·10⁻⁷ (screen §4 step 1). A true floor of order 10⁻⁶ at the worst window is exactly consistent with a coarse uniform bound at −0.4: their "Native Triangle lemma" (`NATIVE_BINDING.md`) plus the Dini y-transfer (thinnest slack in their chain, 1.39·10⁻⁶, screen §4 step 5) is a much sharper device than P-9's, and it is precisely the unrefereed analytic content their own referee record lists for human sign-off (screen §5). In absolute terms hypothesis (ii) at their tuple is within 10⁻⁶ of failing by their own floor; the screen's "not knife-edge" (about the ratio E_max/T_min ≈ 0.295) should be read with that absolute figure beside it.

**Consequence for the pricing.** Lane A at Gomila's tuple is not a rerun of the Session-19 producers; it requires one of:

| route | what it needs | price | outcome |
|---|---|---|---|
| A-1: a sharper D1 floor lemma | derive (SPEC-style, from P15's quoted inequalities: Lemma 10.1 with the E_{t,5}-type mollifier of (98) p54, or Lemma 8.2-type bounds per fine y-piece), implement on both legs (`p9_mp.py`, `p9_arb.py` successors), self-tests, cross-check rule, Opus audit, SPEC v1.2 contract change (§5.4 says a different lemma is "out of this contract's scope") | 2–3 agent-sessions (the Euler-2 floor took a planner + review + build + audit stream over Sessions 17–19), producer time unknown | UNCERTAIN: the true worst floor is ≈ 10⁻⁶ by their data, so any uniform-in-N bound over a wide window range is likely to fail; if singleton-N rows are needed (as Gomila found: 3 149 013 of them), the width-independent row cost turns into ≈ 3.1·10⁶ × 13.5 s ≈ **4.2·10⁷ s ≈ 16 weeks on the mp leg** (one process; 4 weeks at the 4-job cap) and ≈ 3.1·10⁶ × 0.5 s ≈ 18 days on Arb — and the Lean literal is then SPEC §7.6's 3 000-module case |
| A-2: adopt Gomila's floor as prose | display "their finite lane holds" as an extra hypothesis H2-A′ (unrefereed; SPEC §11's tail-row wording, applied to the windows) | zero compute | the theorem's label acquires a hypothesis the program neither checked nor can check (their rows are not exposed as enclosures either; only floors), which is the thing the screen exists to avoid — rejected on the same ground as adopting `TAIL_LEMMA.md` |
| A-3: convert their 3 149 013 finite rows | `AsymRow ⟨N, N, T, E⟩` at K = 10¹² (SPEC §11 row 6, "direct") | a script; Lean: 3 149 013 rows ÷ 1 000 per chunk ≈ 3 150 modules × 3–4 s ≈ 3 h build, kernel ≈ 1.57 ms/row ≈ 80 min | converts their NUMBERS into D1's format, but H2-A's semantics ("T is a floor of |f_{t₀}| on the window") would rest on their lemma — the same displayed H2-A′ as A-2 with 3 000 modules attached; buys nothing over A-2 |

None of the three is "their finite lane extended by D1's own producer" (the brief's phrasing): D1's producer cannot extend a lane whose floor it cannot reproduce at the windows they already cover.

### 1.3 The tail decision (SPEC §11, last row)

Recomputed with the model's `tail()` at their tuple (Appendix A, probes 1, 3, 4): S(N₁) = Q₁ + Q₂ + Q₃ + Q₄ + E₁ = 2.516 at 5.14·10⁶, 2.321 at 8·10⁶, 2.032 at 2·10⁷, 1.979 at 2.5·10⁷; the least N₁ with S < 1.997 (the row-2 rule) is **N₁ ≈ 2.31·10⁷** (x_{N₁} ≈ 6.7·10¹⁵; side conditions (S1)–(S4) true with room: u₁ = 16.96 against 2a/t = 5.04 and 2a″/t = 7.36). SPEC §11's "N₁ then ≈ 7–9·10⁶ by the crude method" is wrong by 3×: the crude 2 − A − B is still −0.21 at 8·10⁶ (Appendix A, probe 1); the SPEC figure was carried over from row 2 without recomputation (Appendix B, correction 1). Decision on the tail, as the brief asks: **recompute Lemma T at their parameters (N₁ ≈ 2.3·10⁷), adopt nothing of theirs** — Lemma T's cost is unchanged (the certified tail row is a 10⁴-term head plus integrand evaluations; only the optional `--direct` validation scales with N₁: ≈ 31 min mp, ≈ 1 min Arb). The tail is NOT the block; the windows below it are (§1.2). Adopting `TAIL_LEMMA.md` as prose stays rejected (unrefereed, a different lemma, SPEC §5.4/§11).

### 1.4 Lean and packaging cost (the "near-zero" part, priced honestly)

The theorem shape is a twin of `row2_ray_{mp,arb}` (`Instance02.lean` lines 192–221): a `gomilaRect := ⟨6000000185827, 1, 6000000185828, 1, 1809, 10000, 1, 1⟩` (already type-checked in the Session-14 scratch `gomila/gomila-scratch-arb.lean`), `hH1_row3` (a `norm_num` twin of `hH1_row2` at σ₀ = 148409/250000, T₀ = 6000000185827/2 — a half-integer real, which `ZeroVerification (σ₀ T₀ : ℝ)` accepts as it stands), `row3_bound_le : 129/800 + (23409/125000)^2/2 ≤ 17879/100000` (`norm_num`; exact value 5587043781/31250000000 = 0.178785400992), two ray theorems, two corollaries: ≈ 80 lines of hand-written Lean, standard axioms expected. The choice y₀″ := 23409/125000 (Gomila's own upper bracket of the irrational y₀ = √(87677/2500000)) keeps every constant rational: `Polymath15Bridge'` quantifies over any real y₀, a larger y₀ weakens H1 (larger σ₀) and (ii′)/(iii′) (smaller regions) and costs 10⁻⁹ in the bound. The generated part is where the cost is: B-own ≈ 115 prism modules (row 2's 137 s + 237 s builds, one `lake` at a time), B-883 ≈ 1 766 modules ≈ 1.7 h serial build plus a 6.7-minute monolithic kernel check on ≈ 255 000 rows; Lane A one module per leg (or ≈ 3 150 under A-3). Packaging per 10(j) (FIDELITY.md is the ledger a second row inherits): a second trusted literal copy under `ChallengeDeps.DBN` (row 2's is 20 157 lines / 227 defs for 17 947 rows; B-883 would be ≈ 290 000 lines and the Comparator run, at 9.6 GB peak RSS for the 406 MB export today, is a RAM risk on 24 GB — B-own stays at row-2 scale), (I) ×2 and (K) ×4 new challenge statements, FIDELITY items (a) (the y-band, now yA − √(271/400) = 8231039/10⁷ − 0.82310388… ≈ 1.8·10⁻⁸), (h) (H1 at margin 175 239 886.5), a new item for y₀″ > y₀, a new item for the floor lemma of route A-1 (or the H2-A′ of A-2), the Opus checker rerun from a clean clone, the Comparator rerun: **≈ 1 builder session + 1 Opus checker session + a 30-minute Comparator run**, in addition to whatever route §1.2 takes. "Near-zero Lean cost" is true of the theorem text and false of the shipping standard.

### 1.5 Thermal, under KICKSTART item 5 (≤ 4 heavy jobs; one `lake` at a time)

B-own: 2 heavy jobs for ≈ 40 min, then one `lake` for ≈ 7 min. B-883: 2 heavy jobs for ≈ 8 h (mp-bound), then one `lake` for ≈ 1.7 h. Route A-1 with singleton rows: 4 heavy jobs for ≈ 4 weeks (mp) — outside anything this program has scheduled locally. Nothing here needs the 4-job cap except the singleton case, which is the case that should not be run.

### 1.6 The re-priced bottom line (one table)

| component | RUN-REPORT §6 item 8 said | re-priced (this file) |
|---|---|---|
| Lane B, D1's own transcript of their row | ≈ 1 h Arb / 10 h mp | B-883: ≈ 20 min Arb / ≈ 8.1 h mp; B-own: ≈ 4 min Arb / ≈ 40 min mp |
| Lane A, finite windows | "their finite lane converts directly" (SPEC §11) | v1.0 floor NEGATIVE on N ≤ 2·10⁶ near y₀ → new lemma (2–3 sessions, uncertain) or their lemma displayed unrefereed; possibly 3.1·10⁶ singleton rows (weeks) |
| Lane A, tail | "N₁ ≈ 7–9·10⁶ by the crude method" | N₁ ≈ 2.3·10⁷ (float model); cost unchanged (rows width-independent; `--direct` ≈ 31 min mp) |
| Lean + packaging | "near-zero Lean cost" | ≈ 80 lines of theorem text; ≈ 1.5 sessions of build/packaging/checker/Comparator |
| total | a day of producers | not achievable with the v1.0 instrument; with a new floor lemma 3–5 sessions plus producer time between 1 h and 4 weeks depending on whether uniform-in-N floors exist at their tuple |

## 2. What a finished M2a′ would buy — precisely

### 2.1 The theorem (proposed Lean shape, ≤ 10 lines; twin of `row2_ray_mp`, `Instance02.lean` line 192; names provisional, shape binding)

    theorem gomila_ray_mp
        (hH1   : ZeroVerification (148409 / 250000) (6000000185827 / 2))
        (hEncl : BarrierEnclOK (fun t z => Ht t z / Bt t z) gomilaBarrierMP)
        (hAsym : AsymEnclOK (fun z => Ht (129 / 800) z / Bt (129 / 800) z) gomilaAsymMP)
        (hTail : TailOK (fun z => Ht (129 / 800) z / Bt (129 / 800) z) gomilaAsymMP)
        (hH3   : Polymath15Bridge' ∧ HtEntire) :
        ∀ t : ℝ, 129 / 800 + (23409 / 125000) ^ 2 / 2 ≤ t → ∀ z : ℂ, Ht t z = 0 → z.im = 0
    -- corollary `lambda_le_point17879`: ∀ t, 17879/100000 ≤ t → …   (129/800 + (23409/125000)²/2 = 5587043781/31250000000 ≤ 17879/100000, norm_num)

with `gomilaBarrierMP`/`gomilaAsymMP` D1's OWN literals (B-own + a Lane A produced under whichever route §1.2 takes; under route A-1 `hAsym`'s semantics rest on the new floor lemma, displayed in SPEC v1.2 exactly as H2-A is displayed today; under A-2/A-3 an additional displayed H2-A′ "Gomila's window floors are floors" appears in the binder list and in the label). Modulo the same H1/H2/H3 shape as row 2 — the H2 conjunction gains a member only on routes A-2/A-3.

### 2.2 H1 at their X — discharged by Platt–Trudgian Theorem 1, with the precise figure only

`gomila-screen.md` §2: "Consumed verification height: X/2 = 3,000,000,092,913.5 against Platt–Trudgian Theorem 1's precise height 3,000,175,332,800; exact surplus 350479773/2 = 175,239,886.5." §4 step 5: "every checked inequality carries certified nonzero slack: height surplus 175,239,886.5; …". §4 step 2 rider: "the licensing works only because PT's precise Theorem-1 height is cited. With the abstract's round '3×10¹²', X/2 would exceed it by 92,913.5 and hypothesis (i) would fail." The direction file ("Current frontier", the Session-7 paragraph): "consumed height X/2 sits 1.75e8 BELOW Platt–Trudgian's precise rigorous 3,000,175,332,800". Recomputed exactly this session: 3 000 175 332 800 − 6 000 000 185 827/2 = 350 479 773/2 = **175 239 886.5**, relative 5.84·10⁻⁵ of the height; 3·10¹² − X/2 = −185 827/2 = −92 913.5. Row 2's margin for comparison (SPEC §3.6): 500 175 235 371, relative 16.7 %. So H1 at their X IS discharged by PT Theorem 1 as `ZeroVerification (148409/250000) (6000000185827/2)` — σ₀ = (1 + 23409/125000)/2 exactly, larger than their (1 + y₀)/2 by 4.5·10⁻⁸ and therefore a weaker hypothesis than theirs — with a margin 2 900× thinner than row 2's and with the exact PT figure load-bearing in the prose discharge (FIDELITY (h) would carry both numbers). Nothing in Lean checks the height; the margin is "arithmetic on the record, not in Lean", as (h) says of row 2.

### 2.3 The sentence that could be printed (all of it, and nothing more)

> "At (t₀, y₀″, X) = (129/800, 23409/125000, 6 000 000 185 827) — a tuple below the record row, taken from an unrefereed 2026 claim (Gomila; screen-open, `results/d1-m0/gomila-screen.md`) — the program's two independent producers certified hypotheses (ii) and (iii) of Polymath15 Theorem 1.2 on the program's own transcripts, kernel-checked by the M2a checkers; hence, in ray form and kernel-checked modulo H1 (Platt–Trudgian Theorem 1 at height 3 000 000 092 913.5, precise figure 3 000 175 332 800 required; margin 175 239 886.5), H2 (the program's producer-certified enclosures: H2-B, H2-A [under the v1.2 floor lemma / or: and H2-A′, Gomila's window floors, unrefereed], H-TAIL) and H3 (Theorem 1.2 in bridge form and the entirety of H_t), every H_t with t ≥ 17879/100000 has only real zeros. This is a statement about the program's own certificates. It is not a verification of the claimant's chain, whose analytic lemmas remain unrefereed; it is not a refereed result; it is not a record. The bracket of record remains 0 ≤ Λ ≤ 0.2."

And, only if B-883 is run in addition: "D1's transcript at the claimant's 883 seams is accepted by `checkBarrier` prism for prism; the claimant's own per-prism enclosures remain unexposed, so the screen's step 3 stays non-executable on the claimant's certificate."

### 2.4 The sentences that could NOT be printed, whatever is run

1. "Λ ≤ 0.1787854" or "Λ ≤ 0.17879" as a bound in force, or with the word "record" (screen §7 caveats 2–3; the program is not a promotion authority — D-R2).
2. "Gomila's proof/certificate is verified", "passes D1's checker", or "screen-pass" — their per-prism rows are not sealed (INSTANCE-REPORT §5.3 (d)); a full D1 transcript at their seams is D1's certificate, not theirs; the taxonomy's "checker accepts" cannot be met on rows that do not exist.
3. "The program has improved the de Bruijn–Newman upper bound" — the analytic content of H2 (SPEC §4.4–§4.5, §5.4 and any v1.2 floor lemma) is the program's own unrefereed derivation; the certificate has exactly the standing of Gomila's: computer-assisted, self-published, unrefereed.
4. "Λ ≤ 0.1787854 holds modulo H1, H2, H3" at THEIR y₀ — the instance is at y₀″ = 23409/125000 > y₀ (rational glue), bound 5587043781/31250000000 = 0.178785400992; the printed number is 17879/100000 or the exact rational, never 0.1787854.
5. "Fully machine-checked" (SPEC §3.7, binding everywhere).
6. "Independent confirmation of Gomila's finite lane" — under routes A-2/A-3 the finite lane is adopted, not confirmed; under A-1 it is replaced by a different lemma at different windows.

## 3. Cost against KICKSTART 10(d) and the sponsor's lean-budget rule; the honest alternative

### 3.1 What it pulls, and from what

10(d): "A result graded above threshold (a new zoo Group-IV barrier, a lemma surviving two blind referees, or a Lean-checked statement) pulls the NEXT session's full agent budget into its follow-ups". Session 20's budget is already pulled by the Session-19 Lean-checked Lane A result: item 1 (packaging) is done, item 2 (this pricing) is running, item 3 (`results/c3-r/s20/BRIEF.md`) is next, and the orchestrator has scheduled D-R8 (2 sessions) with the M3 seed bundled after item 3. M2a′ honestly priced is 3–5 agent-sessions (floor-lemma derivation + review, two producer implementations + audit, builder, Opus checker, Comparator) plus a heavy-job slot for between 1 h and 4 weeks, with an uncertain analytic outcome at the first step. That is more than D-R8 and the M3 seed together, and it would be taken from the lanes that currently carry the program's signal (the C3-r/Q-S4 line and the zoo). The sponsor's rule — "we must be really smart about directions to pursue" — asks what belief the purchase changes: none. The barrier sample already agrees 29/29 with both legs on the thinnest prisms; a full B-883 pass is the expected outcome (near-certain positive, the mirror image of the M3 ledger's near-certain negative, and worth as little); Lane A's outcome would be a fact about D1's floor lemma, not about ζ or Λ. No zoo entry can come of it (a certificate is not a barrier), no new theorem shape (the ray theorem exists), no refereed standing (§2.4 item 3). Under 10(d) it is not a trigger and must not be scheduled as a follow-up of the Lane A result: a second literal for the same theorem is instrument demonstration, exactly as the orchestrator classified D-R8 and the M3 seed — but at ten times their price and with a research-grade unknown in the middle.

### 3.2 The honest alternative: screen-open, cite nothing

Cost zero. The claim keeps the fixed vocabulary of screen §7: "unrefereed claim, screen-open (this file)", never a bound in force; caveats 1–5 verbatim wherever it is mentioned; the bracket of record 0 ≤ Λ ≤ 0.2 (Rodgers–Tao; Platt–Trudgian Corollary 2). The screening service's first customer stays at the honest terminal state the taxonomy allows on sealed summaries — step 3 non-executable in its row half, step 4 PASS on the sample — and the record gains what this pricing found: the v1.0 Lane A floor does not reach their tuple, which (i) explains from D1's side why their finite lane needed a sharper, unrefereed lemma and 3.1·10⁶ singleton rows, (ii) corrects SPEC §11's tail figure, and (iii) fixes the per-tuple reach of the instrument as built (Appendix B lists the dated notes the orchestrator should append). Nothing is lost that a trigger in §4 would not recover at lower cost later.

### 3.3 A by-product, for a separate brief only (not decided here)

The same probe (Appendix A, probe 4) shows the v1.0 instrument — no new lemma — certifies, at N_start = 690 988 (the largest window index any H1-licensed X allows), least floors-positive y₀ of 0.2612 / 0.2310 / 0.2035 / 0.1789 / 0.1534 at t₀ = 0.165 / 0.170 / 0.175 / 0.180 / 0.186, i.e. program-own tuples with t₀ + y₀²/2 ≈ 0.1991 / 0.1967 / **0.1957** / 0.1960 / 0.1978, tails closing at N₁ ≈ 6.4–7.8·10⁶ (Lane A ≈ 10 min as at row 2), the barrier unprobed (D-R2 anticipated exactly this: "same-height barrier space is not exhausted … a fresh row is not so constrained"). Such a row would be the program's own sub-record candidate on the v1.0 instrument at row-2 cost (≈ 1 h of producers, ≈ 1.5 sessions of Lean/packaging) — with the same candidate-not-record status as §2.4 item 3, and therefore the same 10(d) answer unless a write-up of the instrument needs a second instance (§4, trigger T4). It is recorded here so that "M2a′ at Gomila's tuple" is not mistaken for "a second instance of any kind": the instrument can do the latter cheaply; it cannot do the former.

## 4. DECISION

**NO now. GO later, on the earliest of four named triggers; the choice of variant depends on which fires.**

* **T1 — the claimant exposes per-segment enclosures for the 883 prisms and per-window floor certificates in a checkable (enclosure, not floor-only) form.** Then step 3 of the screen is a mechanical conversion (`gomila/convert_gomila_log.py` extended; minutes) and `checkBarrier` runs on THEIR barrier certificate; Lane A still needs the floor semantics (A-1 or a displayed H2-A′). Variant: conversion + B-own cross-check; the screen can then reach its taxonomy's "checker accepts" on the barrier half.
* **T2 — human sign-off or a refereed publication of the claimant's chain (in particular `NATIVE_BINDING.md`, the Dini y-transfer and `TAIL_LEMMA.md`).** Then the record moves to ≤ 0.1787854 on the literature, and the M2a instance SHOULD follow the record: adopt their floor lemma as refereed analytic input (a displayed, cited H2-A′, as PT Theorem 1 is displayed for H1), implement its finite computation on both D1 legs (2–3 sessions, singleton rows priced in §1.2 route A-1), run B-own. This is the trigger that makes M2a′ worth its price.
* **T3 — M2b lands (H3 discharged).** A program-own sub-record certificate then becomes an object of a new kind (modulo H2 only), and the floor-lemma work is part of that brief, not of this one.
* **T4 — the M2a instrument write-up needs a second instance to show generality.** Use §3.3's program-own row on the v1.0 instrument (t₀ ≈ 0.175, y₀ ≈ 0.204; separately priced), not Gomila's tuple: same demonstration, no new lemma, row-2 cost.

Until one fires: enact nothing; the orchestrator appends the dated corrections of Appendix B; the claim stays "unrefereed, screen-open, not a record".

## 5. Refutation-shaped close (KICKSTART 10(c))

1. **M2a′ with the v1.0 Lane A producer cannot yield an accepted asymptotic transcript at Gomila's tuple**, because the Euler-2 mollified floor (derivation M, `plan_rows.py` at 4–5-digit agreement with the certified legs) is negative on the windows N ∈ [690 988, ≈ 2.0·10⁶] at y near y₀ ≈ 0.187 (−0.40 at N_start), and C-A3 requires E < T.
2. **No X licensed by H1 repairs this at t₀ = 129/800**, because X ≤ 2 × 3 000 175 332 800 forces N_start ≤ 691 008, where the least certifiable y₀ is ≈ 0.286 and t₀ + y₀²/2 ≈ 0.202 > 0.2: the v1.0 instrument cannot certify any sub-record bound at this t₀.
3. **The tail is not the obstacle**: Lemma T closes at N₁ ≈ 2.3·10⁷ at their tuple (not 7–9·10⁶), at unchanged row cost because Lane A rows are width-independent (13.3–13.8 s mp, 0.5 s Arb per row); adopting `TAIL_LEMMA.md` stays rejected.
4. **Lane B is cheap on both legs**: B-own ≈ 40 min mp / ≈ 4 min Arb; B-883 ≈ 8.1 h mp / ≈ 20 min Arb; two heavy jobs; the sample (29 prisms incl. the ten thinnest, 8 198 pairs, 0 disjoint) makes a full pass the expected outcome, so a full run buys little information.
5. **No D1 computation can yield screen-pass for Gomila's certificate**, because the taxonomy's "checker accepts" is about the claimant's rows, which are not sealed; a D1 transcript at their seams is D1's certificate.
6. **A finished M2a′ cannot yield a record or an improvement of the de Bruijn–Newman bound**, because H2's analytic content (SPEC §4.4–§4.5, §5.4, any v1.2 floor lemma, or a displayed H2-A′) is unrefereed; its standing equals the claimant's: candidate, never a record.
7. **A finished M2a′ cannot yield a verification of Gomila's chain**, because it replaces their lemmas (A-1) or displays them (A-2/A-3); it never checks them.
8. **H1 at their X holds** — `ZeroVerification (148409/250000) (6000000185827/2)` is discharged by Platt–Trudgian Theorem 1 with margin 175 239 886.5 — and holds only with the precise height: the round 3·10¹² fails by 92 913.5.
9. **The Lean theorem is ≈ 80 lines and near-zero risk, but the shipping standard is not near-zero**: ≈ 1.5 sessions (builder, Opus checker, Comparator; B-883's literal is a RAM risk at 24 GB), on top of the route §1.2 takes.
10. **Under 10(d) M2a′ is not a trigger and pulls 3–5 sessions plus 1 h–4 weeks of heavy jobs from lanes with signal for no change of belief, no zoo entry and no new theorem shape**; the sponsor's lean-budget rule forbids it now.
11. **The honest alternative holds at zero cost**: screen-open, cite nothing, caveats 1–5 verbatim, bracket of record 0 ≤ Λ ≤ 0.2 — plus the instrument fact and the two record corrections of Appendix B.
12. **GO-later holds on T1–T4** (§4); T2 is the trigger that makes M2a′ worth its price, and T4 is served better by a program-own row on the v1.0 instrument (t₀ ≈ 0.175, y₀ ≈ 0.204, bound ≈ 0.1957 in ray form; separately priced) than by Gomila's tuple.

## Appendix B — owed record corrections (for the orchestrator; this agent edits nothing but this file)

1. `results/d1-m2a/SPEC.md` §11, tail row: "N₁ then ≈ 7–9·10⁶ by the crude method" → dated note: float model gives N₁ ≈ 2.3·10⁷ (this file §1.3, Appendix A probes 1, 3, 4); and the finite-lane row's "direct" status should carry the note that D1's v1.0 floor is negative on their windows N ≤ 2·10⁶ near y₀ (§1.2) — the conversion is direct, the semantics are not D1's.
2. `results/d1-m2a/RUN-REPORT.md` §4 and §6 item 8 ("≈ 1 h Arb / 10 h mp … at near-zero Lean cost"): dated note pointing to §1.6 of this file.
3. `results/d1-m0/gomila-screen.md` §9: dated addendum — Lane A of the claim is not reproducible with the v1.0 D1 floor (the instrument fact), the absolute thinness of their finite lane (T_min ≈ 7.9·10⁻⁷) beside the ratio figure of §4 step 5, and the tail figure.
4. `directions/D1-certified-refutation-arm.md` "PRICING DECISIONS, Session 20" (2c): this decision, the four triggers, and §3.3's program-own row as a named, unpriced option.

## Appendix A — the probes, verbatim (scratchpad; float64 planning model `lane-a/plan_rows.py` with four constants changed by `sed`; NOT a certificate, NOT a producer run)

The only edit to the model: `T0 = 0.186; Y0 = 0.16733; YA = 0.7924646; N0 = 630783` → `T0 = 0.16125; Y0 = 0.187272; YA = 0.8231039; N0 = 690988` (probe 4 sets the constants per t₀ at run time and rebuilds the arrays). Probe 2 first re-runs the UNMODIFIED model at row 2 and reproduces PLAN.md §3.0's 0.02756.


### Probe 1 — `probe_gomila_tail.py`

```
# PROBE (float64, UNTRUSTED, NOT A CERTIFICATE): plan_rows.py's Lemma-T / floor / defect model at Gomila's tuple
# t0 = 129/800, y0'' = 23409/125000 = 0.187272 (rational upper bracket of y0), yA = 8231039/10^7, N_start = 690988.
import time, math
import plan_rows_gomila as P
t=time.time()
P.ARR = P.Arrays(2*12_000_000)
print("arrays", round(time.time()-t,1), "s")
for N in (690988, 1_500_000, 3_000_000, 5_141_000, 6_000_000, 8_000_000):
    c = P.crude(N, P.Y0); print(f"crude  N={N:9d}  2-A-B={c[0]:+.4f}  A={c[1]:.4f} B={c[2]:.4f}")
for N1 in (5_141_000, 6_000_000, 7_000_000, 7_500_000, 8_000_000, 8_500_000, 9_000_000, 10_000_000, 11_000_000, 12_000_000):
    S, parts, side = P.tail(N1)
    print(f"tail   N1={N1:9d}  S={S:.5f}  Q1={parts['Q1']:.4f} Q2={parts['Q2']:.4f} Q3={parts['Q3']:.5f} Q4={parts['Q4']:.5f} E1={parts['E1']:.2e}  sides={all(side.values())}  u1={parts['u1']:.3f} 2a/t={2*parts['a']/P.T0:.2f} 2a2/t={2*parts['a2']/P.T0:.2f}")
# bisect the least N1 with S < 2 - 0.003 (the row-2 rule)
lo, hi = 5_000_000, 12_000_000
while hi - lo > 1000:
    mid = (lo+hi)//2
    S,_,_ = P.tail(mid)
    if S < 2 - 0.003: hi = mid
    else: lo = mid
print("least N1 (S < 1.997), to 1000:", hi)
# window floors from N_start on the row-2-style pieces (y from y0'')
ys=[0.187272,0.2,0.23,0.27,0.32,0.4,0.55,0.8231039]
for (Nlo,Nhi) in ((690988,690988),(690988,800000),(800001,1_600_000),(1_600_001,hi-1)):
    Tmin=min(P.floor_sub(Nlo,Nhi,ys[i],ys[i+1]) for i in range(len(ys)-1))
    E=P.defect(Nlo,Nhi,ys[0],ys[-1])[0]
    print(f"row [{Nlo},{Nhi}]  T_model={Tmin:.5f}  E_model={E:.3e}  E/T={E/Tmin:.2e}")
print("total", round(time.time()-t,1), "s")
```

Output (`probe_gomila_tail.log`):

```
arrays 0.2 s
crude  N=   690988  2-A-B=-1.5298  A=2.9274 B=0.6024
crude  N=  1500000  2-A-B=-0.9582  A=2.5515 B=0.4067
crude  N=  3000000  2-A-B=-0.5833  A=2.2968 B=0.2865
crude  N=  5141000  2-A-B=-0.3609  A=2.1411 B=0.2198
crude  N=  6000000  2-A-B=-0.3063  A=2.1021 B=0.2041
crude  N=  8000000  2-A-B=-0.2138  A=2.0355 B=0.1783
tail   N1=  5141000  S=2.51643  Q1=2.1411 Q2=0.2234 Q3=0.07519 Q4=0.07671 E1=6.85e-09  sides=True  u1=15.453 2a/t=5.04 2a2/t=7.36
tail   N1=  6000000  S=2.44290  Q1=2.1021 Q2=0.2075 Q3=0.06598 Q4=0.06731 E1=5.15e-09  sides=True  u1=15.607 2a/t=5.04 2a2/t=7.36
tail   N1=  7000000  S=2.37517  Q1=2.0655 Q2=0.1929 Q3=0.05780 Q4=0.05897 E1=3.87e-09  sides=True  u1=15.761 2a/t=5.04 2a2/t=7.36
tail   N1=  7500000  S=2.34656  Q1=2.0498 Q2=0.1867 Q3=0.05445 Q4=0.05555 E1=3.40e-09  sides=True  u1=15.830 2a/t=5.04 2a2/t=7.36
tail   N1=  8000000  S=2.32069  Q1=2.0355 Q2=0.1812 Q3=0.05147 Q4=0.05251 E1=3.01e-09  sides=True  u1=15.895 2a/t=5.04 2a2/t=7.36
tail   N1=  8500000  S=2.29717  Q1=2.0224 Q2=0.1762 Q3=0.04880 Q4=0.04979 E1=2.69e-09  sides=True  u1=15.956 2a/t=5.04 2a2/t=7.36
tail   N1=  9000000  S=2.27565  Q1=2.0103 Q2=0.1717 Q3=0.04640 Q4=0.04734 E1=2.41e-09  sides=True  u1=16.013 2a/t=5.04 2a2/t=7.36
tail   N1= 10000000  S=2.23759  Q1=1.9886 Q2=0.1636 Q3=0.04225 Q4=0.04310 E1=1.98e-09  sides=True  u1=16.118 2a/t=5.04 2a2/t=7.36
tail   N1= 11000000  S=2.20488  Q1=1.9698 Q2=0.1568 Q3=0.03879 Q4=0.03957 E1=1.65e-09  sides=True  u1=16.213 2a/t=5.04 2a2/t=7.36
tail   N1= 12000000  S=2.17636  Q1=1.9531 Q2=0.1508 Q3=0.03585 Q4=0.03658 E1=1.40e-09  sides=True  u1=16.300 2a/t=5.04 2a2/t=7.36
least N1 (S < 1.997), to 1000: 12000000
row [690988,690988]  T_model=-0.40033  E_model=2.335e-07  E/T=-5.83e-07
row [690988,800000]  T_model=-0.43244  E_model=2.335e-07  E/T=-5.40e-07
row [800001,1600000]  T_model=-0.49660  E_model=1.825e-07  E/T=-3.67e-07
row [1600001,11999999]  T_model=-0.53334  E_model=5.548e-08  E/T=-1.04e-07
total 7.6 s
```

### Probe 2 — `probe2.py`

```
import time, math, sys
import plan_rows_row2 as R
import plan_rows_gomila as G
t=time.time()
R.ARR = R.Arrays(2*700000)
print("ROW-2 SANITY: floor_sub(630783,630783,0.16733,0.18) =", round(R.floor_sub(630783,630783,0.16733,0.18),5), " (PLAN.md: model 0.02756, certified 0.027556)")
S,_,_ = R.tail.__globals__['tail'](5141000) if False else (None,None,None)
G.ARR = G.Arrays(2*20_000_000)
print("arrays", round(time.time()-t,1),"s")
# singleton windows, fine y-pieces at the bottom, at Gomila's tuple
for N in (690988, 1_000_000, 2_000_000, 5_000_000, 10_000_000, 20_000_000):
    Tb = G.floor_sub(N,N,0.187272,0.1873)          # bottom sliver, width 2.8e-5
    Tm = G.floor_sub(N,N,0.3,0.3001)
    Tt = G.floor_sub(N,N,0.8230,0.8231039)
    T,parts = G.floor_sub(N,N,0.187272,0.1873,want_parts=True)
    print(f"singleton N={N:9d}: T(bottom sliver)={Tb:+.5f}  T(y~0.3)={Tm:+.5f}  T(top)={Tt:+.5f}   sigma={parts['sigma']:.4f} LA={parts['LA']:.4f} UC={parts['UC']:.4f} beta={parts['beta']:.4f}")
# the same at row 2 for scale (y0 sliver)
R.ARR = R.Arrays(2*5_200_000)
for N in (630783, 2_000_000, 5_140_999):
    print(f"row2 singleton N={N}: T(bottom sliver [0.16733,0.16736])={R.floor_sub(N,N,0.16733,0.16736):+.5f}")
# what y0 would be needed at t0=0.16125 for a positive Euler-2 floor at N=690988 (diagnostic only)
for y in (0.2,0.25,0.3,0.35,0.4):
    print(f"diagnostic: t0=0.16125, singleton N=690988, y-sliver at {y}: T={G.floor_sub(690988,690988,y,y+0.0001):+.5f}")
print("total", round(time.time()-t,1),"s")
```

Output (`probe2.log`):

```
ROW-2 SANITY: floor_sub(630783,630783,0.16733,0.18) = 0.02756  (PLAN.md: model 0.02756, certified 0.027556)
arrays 0.4 s
singleton N=   690988: T(bottom sliver)=-0.39916  T(y~0.3)=+0.03922  T(top)=+0.54087   sigma=1.6777 LA=-0.0570 UC=0.4694 beta=0.3187
singleton N=  1000000: T(bottom sliver)=-0.24158  T(y~0.3)=+0.13247  T(top)=+0.56107   sigma=1.7075 LA=0.0715 UC=0.3885 beta=0.3122
singleton N=  2000000: T(bottom sliver)=-0.00353  T(y~0.3)=+0.27270  T(top)=+0.59430   sigma=1.7634 LA=0.2671 UC=0.2717 beta=0.3003
singleton N=  5000000: T(bottom sliver)=+0.21869  T(y~0.3)=+0.40435  T(top)=+0.63103   sigma=1.8373 LA=0.4521 UC=0.1710 beta=0.2853
singleton N= 10000000: T(bottom sliver)=+0.33551  T(y~0.3)=+0.47514  T(top)=+0.65474   sigma=1.8932 LA=0.5506 UC=0.1230 beta=0.2745
singleton N= 20000000: T(bottom sliver)=+0.42158  T(y~0.3)=+0.52904  T(top)=+0.67578   sigma=1.9490 LA=0.6238 UC=0.0909 beta=0.2641
row2 singleton N=630783: T(bottom sliver [0.16733,0.16736])=+0.02837
row2 singleton N=2000000: T(bottom sliver [0.16733,0.16736])=+0.29142
row2 singleton N=5140999: T(bottom sliver [0.16733,0.16736])=+0.42414
diagnostic: t0=0.16125, singleton N=690988, y-sliver at 0.2: T=-0.33036
diagnostic: t0=0.16125, singleton N=690988, y-sliver at 0.25: T=-0.11428
diagnostic: t0=0.16125, singleton N=690988, y-sliver at 0.3: T=+0.03922
diagnostic: t0=0.16125, singleton N=690988, y-sliver at 0.35: T=+0.15167
diagnostic: t0=0.16125, singleton N=690988, y-sliver at 0.4: T=+0.23650
total 9.7 s
```

### Probe 3 — `probe3.py`

```
import time, math
import plan_rows_gomila as G
t=time.time()
G.ARR = G.Arrays(40_000_000)
for N1 in (15_000_000, 20_000_000, 25_000_000, 30_000_000, 35_000_000, 40_000_000):
    S, p, side = G.tail(N1)
    print(f"tail N1={N1:9d} S={S:.5f} Q1={p['Q1']:.4f} Q2={p['Q2']:.4f} Q3={p['Q3']:.5f} Q4={p['Q4']:.5f} sides={all(side.values())}")
print("total", round(time.time()-t,1),"s")
```

Output (`probe3.log`):

```
tail N1= 15000000 S=2.10865 Q1=1.9128 Q2=0.1368 Q3=0.02922 Q4=0.02981 sides=True
tail N1= 20000000 S=2.03166 Q1=1.8654 Q2=0.1212 Q3=0.02231 Q4=0.02276 sides=True
tail N1= 25000000 S=1.97886 Q1=1.8317 Q2=0.1107 Q3=0.01802 Q4=0.01838 sides=True
tail N1= 30000000 S=1.93961 Q1=1.8061 Q2=0.1030 Q3=0.01509 Q4=0.01539 sides=True
tail N1= 35000000 S=1.90888 Q1=1.7856 Q2=0.0971 Q3=0.01295 Q4=0.01322 sides=True
tail N1= 40000000 S=1.88391 Q1=1.7686 Q2=0.0924 Q3=0.01134 Q4=0.01157 sides=True
total 1.2 s
```

### Probe 4 — `probe4.py`

```
# PROBE 4 (float64 planning model, UNTRUSTED, NOT A CERTIFICATE)
import math, time
import plan_rows_gomila as G
t=time.time()
def setup(t0, y0, yA, nmax):
    G.T0=t0; G.B2=math.exp(t0/4*G.LOG2**2); G.Y0=y0; G.YA=yA; G.ARR=G.Arrays(nmax)
def ymin_positive(N, lo=0.15, hi=0.6, tol=1e-4):
    # least y (bisection) with floor_sub(N,N,y,y+1e-4) > 2.5e-7 (a working E ceiling)
    while hi-lo>tol:
        m=(lo+hi)/2
        if G.floor_sub(N,N,m,m+1e-4) > 2.5e-7: hi=m
        else: lo=m
    return hi
# (1) Gomila's t0: y-threshold at N_start = 690988, and at the PT-height ceiling N = 691008
setup(0.16125, 0.187272, 0.8231039, 2*700_000)
for N in (690988, 691008):
    y=ymin_positive(N); print(f"t0=0.16125 N={N}: least certifiable y0 (v1.0 Euler-2 floor) = {y:.4f} -> bound t0+y0^2/2 = {0.16125+y*y/2:.5f}")
# (2) tail crossing at Gomila's tuple to 1e5
setup(0.16125, 0.187272, 0.8231039, 26_000_000)
lo,hi=20_000_000,26_000_000
while hi-lo>100_000:
    m=(lo+hi)//2; S,_,_=G.tail(m)
    if S<1.997: hi=m
    else: lo=m
S,p,side=G.tail(hi); print(f"Gomila tuple: least N1 (S<1.997) to 1e5 = {hi}  S={S:.5f} sides={all(side.values())}  x_N1 = {G.xN(hi):.3e}")
# (3) program-own rows at intermediate t0 (N_start = 690988, the PT-height ceiling): least y0, bound, and the tail's N1
for t0 in (0.165, 0.170, 0.175, 0.180, 0.186):
    setup(t0, 0.2, 0.8231039, 2*700_000)
    y=ymin_positive(690988); b=t0+y*y/2
    yA=math.sqrt(1-2*t0)+1e-7
    setup(t0, y, yA, 26_000_000)
    lo,hi=2_000_000,26_000_000
    while hi-lo>100_000:
        m=(lo+hi)//2; S,_,_=G.tail(m)
        if S<1.997: hi=m
        else: lo=m
    print(f"t0={t0:.3f}: least y0={y:.4f}  bound={b:.5f}  ({'<0.2' if b<0.2 else '>=0.2'})   tail N1~{hi}")
print("total", round(time.time()-t,1),"s")
```

Output (`probe4.log`):

```
t0=0.16125 N=690988: least certifiable y0 (v1.0 Euler-2 floor) = 0.2856 -> bound t0+y0^2/2 = 0.20204
t0=0.16125 N=691008: least certifiable y0 (v1.0 Euler-2 floor) = 0.2856 -> bound t0+y0^2/2 = 0.20204
Gomila tuple: least N1 (S<1.997) to 1e5 = 23093750  S=1.99699 sides=True  x_N1 = 6.702e+15
t0=0.165: least y0=0.2612  bound=0.19912  (<0.2)   tail N1~7812500
t0=0.170: least y0=0.2310  bound=0.19667  (<0.2)   tail N1~7156250
t0=0.175: least y0=0.2035  bound=0.19571  (<0.2)   tail N1~6781250
t0=0.180: least y0=0.1789  bound=0.19601  (<0.2)   tail N1~6500000
t0=0.186: least y0=0.1534  bound=0.19777  (<0.2)   tail N1~6406250
total 6.7 s
```
