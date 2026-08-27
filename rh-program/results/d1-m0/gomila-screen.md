# Gomila claim screen — first live run of the D1 claim-screening service

**Date:** 2026-08-26 (Session 7; claim-screening officer agent).
**Protocol:** `results/d1-m0/m2a-m2b-design.md` §3(b) — 5 required disclosures, 5 checker steps, outcome taxonomy screen-pass / screen-fail / non-evaluable. Executed as written, to the extent executable this session (see step 3/4 findings).
**Binding framing** (D1 direction file, D-R2 clause): this claim is a **prior-art item** AND the **screening service's first customer**. It is **NOT a record** and must **never be cited as one**. The bracket of record remains **0 ≤ Λ ≤ 0.2** (Rodgers–Tao + Platt–Trudgian Cor. 2). A screen-pass would make it a candidate second target for the M2a formal instance (M2a′), nothing more — "screen-pass is a statement about certificates, not a promotion authority."
**Verification discipline (standing order 5):** every load-bearing number below was either recomputed exactly this session (exact rational arithmetic, transcript below) or read from the claim's primary artifacts at a pinned commit, cross-checked against the program's on-disk primary PDFs (`fetched/p3-22a4` Polymath15 arXiv:1904.12438v2; `fetched/p3-22a1` Platt–Trudgian). No recalled claims.

---

## 1. Claim identity (located this session, network live)

* **Claimant / claim:** Jude Gomila, 2026 (unrefereed): **Λ ≤ 893927/5000000 = 0.1787854**, presented as a computer-assisted **unconditional** proof ("no unproved conjecture anywhere in the chain"), self-labeled "**not yet peer reviewed**" throughout.
* **Announcement page:** `https://www.judegomila.com/posts/riemann-lambda-0.1787854` ("Let's Solve Riemann" — twelve-chapter interactive exposition; fetched this session).
* **Audit repository:** `https://github.com/judegomila/dbn-lambda-01787854-candidate-audit`
  * HEAD at screen time: commit **`a74738deb6d5e0f76887cb36901da08b68dca705`** (2026-08-21T21:26:54Z), tree `babfa77e570dae893df0a57c2b4b9627bfa22304`, 640 tree entries, ~84 MB. All artifacts below were read at this pinned commit.
  * Sealed adversarial-review commit (v3, per the in-repo referee report): `2e9976c4becbf97e31c56fe75fce07cdff5dd4ea`; release-paper program links pinned to `6222740e`; Romik program-promotion commit `f4d2d03ebc6342b3bce4e0c0b695b82f2e213f1a`.
  * Repo created 2026-07-24; description: "…fail-closed interval certificates, replayable from source. Not yet peer reviewed."
* **Upstream provenance:** the claimant's own prior campaign, version-locked at Zenodo DOI `10.5281/zenodo.21175533` (2026-07-03; 196 MB certificate archive, SHA-256 recorded in `UPSTREAM.md`). The evaluator is a **reimplementation** (own C producers under `barrier/src/` and `src/`, own Python/Arb verifiers), **not a fork of the Polymath15 dbn repository**.
* **Method (one line):** a Lane-A row in the design note's sense — Polymath15 Theorem 1.2 instantiated at a new (t₀, y₀, X) consuming the existing Platt–Trudgian height; barrier + finite-window + analytic-tail certificates in FLINT/Arb ball arithmetic (256/512-bit), fail-closed checkers, SHA-256-sealed transcripts.

**File inventory (top level, from the pinned tree):** `certificates/` 15 gzip shards, ~24.6 MB (the 3,149,013 finite rows in four auxiliary-prime legs); `barrier/` ~1.4 MB (4 C producers, 20-digit coefficient matrix `storedsum_nolemma_6000000185827_dig_20.txt` 230 KB, sealed 883-prism logs for Linux/FLINT-3.0.1 and macOS/FLINT-3.6.0); `verifiers/` 23 fail-closed programs (Python + 3 standalone Arb C checkers); `logs/` 17 sealed transcripts; `provenance/` 10 lemma/audit notes; `independent/` 5 reimplementation programs (authored by Dan Romik, promoted under seal); `vendor/` 256 entries (version-locked upstream subset); `lean/` 73 entries (incl. `lean/aristotle/` — seven Lean 4 lemma-layer projects added 2026-08-21, post-referee); `dan-reworking/` 118 MB (Romik's unsealed manuscript rework); primary paper `gomila_dbn_lambda_01787854_release.pdf` (2026-08-20); `SHA256SUMS` 443 entries; `verify.sh`, `Dockerfile`, hash-pinned `requirements.txt`, replay scripts.

**Integrity spot-check this session:** 16/16 files downloaded for this screen match `SHA256SUMS` at HEAD (SEAL OK: PROOF_NOTE, CANDIDATE_PARAMETERS, README, BARRIER_CERTIFICATE, TAIL_LEMMA, WINDOW_FREEZE_THEOREM, DERIVATIVE_BOX_LEMMA, ERROR_CONSTANT_WELD, PROVENANCE, ENVIRONMENT.txt, UPSTREAM, EXTERNAL_REFEREE_REPORT_2026-07-28, MAXIMUM_CHECKS, OPEN_REVIEW_QUESTIONS, verify.sh, independent/README).

---

## 2. What is actually claimed (from the sealed primary artifacts)

Exact row (`PROOF_NOTE.md` §1, `CANDIDATE_PARAMETERS.md`):

* **X = 6,000,000,185,827** (barrier abscissa; barrier box [X, X+1]);
* **t₀ = 129/800 = 0.16125** exactly;
* **y₀² = 87677/2,500,000 = 0.0350708** exactly (y₀ = positive square root; certified bracket 1872719/10⁷ < y₀ < 23409/125000);
* conclusion **Λ ≤ t₀ + y₀²/2 = 893927/5,000,000 = 0.1787854** via Polymath15 Theorem 1.2 (arXiv:1904.12438v2), instantiated in its exact **curved** form (not the simplified box): (i) ζ zero-free for (1+y₀)/2 ≤ σ ≤ 1, 0 ≤ T ≤ X/2; (ii) H_{t₀} ≠ 0 for x ≥ X+√(1−y₀²), y₀ ≤ y ≤ √(1−2t₀); (iii) H_t ≠ 0 on the curved barrier for 0 ≤ t ≤ t₀.
* **Consumed verification height:** X/2 = 3,000,000,092,913.5 against Platt–Trudgian Theorem 1's **precise** height 3,000,175,332,800; exact surplus 350479773/2 = 175,239,886.5. The T = 0 endpoint is closed classically (η(σ) > 0, ζ(σ) < 0 on (0,1), pole at s = 1).
* **Evidence architecture:** (iii) = 883 consecutive closed t-prisms from exactly t = 0, cyclic boundary mesh, per-prism winding-0 certificates, whole-prism D_t (t-interpolation) bounds, strict fail-closed gate M_i > D_z/(2(num−1)) + D_t·Δt + 0.00125; (ii)-finite = 3,149,013 window rows N = 690,988…3,840,000 with stored floors; (ii)-tail = an all-N contraction theorem (`TAIL_LEMMA.md`) checked by a standalone Arb program at the split point N★ = 3,840,000, overlapping the finite lane on the full window W_{3840000}; arithmetic = FLINT/Arb balls at 256 and 512 bits, coefficients restored as balls with a separately-carried Taylor tail < 1.96×10⁻²², final assembly in exact rationals.

---

## 3. Disclosure inventory (the 5 required disclosures)

| # | Required disclosure | Finding |
|---|---|---|
| 1 | Exact tuple (t₀, y₀, X) with the arithmetic claim as exact rationals | **PRESENT.** All parameters exact rationals/integers; the bound is an exact rational identity (§4 step 1). |
| 2 | Consumed height X/2 ≤ 3,000,175,332,800 with citation to PT Theorem 1 | **PRESENT.** X/2 = 3,000,000,092,913.5, cited to PT's precise Theorem-1 figure (not the round 3×10¹²), surplus stated to the half-integer. |
| 3 | Barrier transcripts: mesh, t-slices, ball enclosures convertible to (lo,hi) integers at a scale, winding-0 per slice, t-interpolation bound | **PRESENT.** 883 prisms, sealed printed-enclosure logs (two toolchains), per-prism winding gates strictly inside (−¼,¼), whole-prism D_t re-evaluation (not left-endpoint sampling), coefficient matrix + Taylor-tail provenance. Printed decimal balls are convertible to the `BarrierCertData` integer-pair convention in principle; no format obstruction identified. |
| 4 | Asymptotic-region evidence: checkable finite computation + citable analytic tail, split point stated | **PRESENT** (with a flag). Finite lane = 3,149,013 rows in 15 sealed shards; tail = `TAIL_LEMMA.md` + standalone Arb checker; split point N★ = 3,840,000 stated with an overlap window. Flag: the tail is a **new lemma in the package**, not Polymath15 Thm 1.5 (§5). |
| 5 | Software identity: versions, rerun scripts, evaluator provenance | **PRESENT.** Pinned container (image sha256 `bedf7303…`), FLINT 3.0.1 (Linux) + 3.6.0 (macOS), mpmath 1.4.1, hash-pinned requirements, full replay scripts (`verify.sh`, barrier/tail/prop410/full-sweep), Zenodo-locked upstream; evaluator = own reimplementation, not a Polymath15-dbn fork. |

**All five disclosures PRESENT.** The design note's prior expectation ("non-evaluable at first contact") is refuted — this is, by a wide margin, the predicted market's best-dressed customer.

---

## 4. Checker steps (executed in order; protocol says stop at first failure — none occurred)

**Step 1 — Arithmetic (exact rational cross-multiplication). PASS, recomputed this session:**
* t₀ + y₀²/2 = 129/800 + 87677/5,000,000 = **893927/5,000,000 = 0.1787854 exactly** (terminating decimal; equality, not ≤).
* Height conversion X/2 = 3,000,000,092,913.5; T_PT − X/2 = **350479773/2 = 175,239,886.5 > 0** exactly.
* Theorem 1.2 preconditions: 0 < t₀ < ½; 0 < y₀² < 1 − 2t₀ = 271/400; y₀ ≤ 1. All hold exactly.
* Canopy identity y₀² + 2t₀ = 893927/2,500,000 < 1 exactly.
* Certified brackets verified by integer squares: (1872719/10⁷)² < y₀² < (23409/125000)²; (8231038/10⁷)² < 271/400 ≤ (8231039/10⁷)².
* Barrier floor containment: y₀² − (1809/10⁴)² = **234599/10⁸ > 0** exactly (so the certified box [X,X+1]×[0.1809,1] contains the curved region, whose y-floor is ≥ y₀ > 0.18727).
* Finite margin: 791366/10¹² − 233494905212337849/10²⁴ = 557871094787662151/10²⁴ ≥ 0.000000557871094787 (claimed figure is the safe truncation). PASS.

**Step 2 — Coverage: hypothesis (i)'s (σ,T) region ⊆ PT Theorem 1's verified region. PASS:**
* Verified against the program's on-disk PT PDF (`p3-22a1`, Theorem 1: "The Riemann hypothesis is true up to height 3 000 175 332 800"): the region σ ∈ [(1+y₀)/2, 1] ⊂ (½, 1], T ∈ [0, 3,000,000,092,913.5] ⊂ [0, 3,000,175,332,800]. The claim leans **only** on the rigorous Platt–Trudgian height — **not** on Gourdon 10¹³ (which is not rigorous and appears nowhere in the chain).
* Transcription fidelity: Gomila's PROOF_NOTE §2 (2.1)–(2.4) matches Polymath15 Theorem 1.2 **verbatim** (re-read this session from the on-disk `p3-22a4`, including the curved hypothesis-(iii) region and the conclusion Λ ≤ t₀ + ½y₀²). The x = 2T normalization matches eq. (1) (H₀(z) = ⅛ξ(½ + iz/2)).
* **Rider (thinnest external hook, flagged by the claim's own referee record and endorsed here):** the licensing works only because PT's precise Theorem-1 height is cited. With the abstract's round "3×10¹²", X/2 would exceed it by 92,913.5 and hypothesis (i) would fail. Gomila cites the precise figure; any D1 write-up must too.

**Step 3 — Format conversion + run `checkBarrier`. NOT EXECUTABLE THIS SESSION (D1-side): PENDING.**
The D1 checker this step invokes does not exist yet — `BarrierCert.lean`/`checkBarrier` are M2a items (a)–(b), sequenced after M1 v1, and the toolchain has not landed. What was done instead, within protocol intent: full artifact inventory (§1); the claim's own fail-closed chain inspected at the descriptive level (54-check strict parsers, fail-closed gates, seal 443 entries, `verify.sh` assembly with the Dini log-auditor wired in after the referee's coverage finding); seal spot-verified 16/16 on this session's downloads; formats confirmed convertible to `BarrierCertData` in principle. **The conversion + kernel-checked run is exactly the M2a′ work item if screening proceeds.**

**Step 4 — Two-producer spot check (Arb + mpmath-ball, D1's own runs). NOT EXECUTABLE THIS SESSION (D1-side): PENDING.**
D1's two producer legs are priced but unbuilt (D-R3 mpmath ball core; the f_t evaluator layer ~3–4 wk Arb / ~2 wk mpmath, priced in the design note §4). Claimant-side replication on record (not a substitute for D1's own): two genuinely different toolchains for the barrier (FLINT 3.0.1 vs 3.6.0, radii differ), 256/512-bit precision cross-checks, Python-interval corroboration (honestly labeled same-backend where it is), and an in-repo referee addendum recording a fresh-from-source recompute of all three heavy lanes (7,688 coefficients, 883 prisms, all 3,149,013 rows matched line-for-line in the pinned container). **Cheap independent spot-recomputes done this session (all agree):** the window-index bracket x_{690988} < X + √(1−y₀²) < x_{690989} reproduced with margins 5,377,393.99 and 11,989,041.17 against the claimed >5.37×10⁶ and >1.19×10⁷ (mpmath, 60 dps); the exact identities of step 1; the finite-margin subtraction.

**Step 5 — Sensitivity: nonzero margin everywhere. PASS (with one thin-margin note and one display nit):**
* The red-flag condition (sum exactly = 0.1787854 AND zero slack in enclosures) is NOT triggered: the sum is exactly the claimed rational **by construction** (the bound is defined as the tuple's value — no rounding was needed), and every checked inequality carries certified nonzero slack: height surplus 175,239,886.5; finite margin ≥ 5.5787×10⁻⁷ (E_max/T_min ≈ 0.295 — not knife-edge); barrier error 3.565×10⁻⁴ vs allowance 1.25×10⁻³ (3.5×); minimum prism margin ≥ 0.5198; tail post-error margin > 1.735×10⁻⁴ (contraction D < 0.999721, and ≈ 0.9605 with the redundant padding removed per the referee record).
* **Thinnest inequality in the chain (note, not a failure):** the Dini y-transfer worst ratio ≤ 0.99999860767275095 — slack ≈ 1.39×10⁻⁶ — certified at 180 and 256 bits with 17-digit agreement, and now gated in the sealed assembly; it is also the top human-sign-off item (§5).
* **Display nit (not a gate):** the three displayed tail roundings are not mutually derivable at the last digit (flow-lower − error-upper = 0.0001735209373332 from the displayed figures vs the stated post-error margin > 0.0001735209373337); consistent with independently-rounded ball summaries, recorded for completeness.

---

## 5. New-argument flag (protocol: flag, do not adjudicate)

The claim is **not a pure Polymath15 Table-row rerun**. The framework (Theorem 1.2 criterion, Theorem 1.3 effective approximation) is the published one, but the discharge of hypotheses (ii) and (iii) runs through **new, unrefereed analytic lemmas in the package**: `NATIVE_BINDING.md` (Triangle-floor-to-|f_t| conversion), `ERROR_CONSTANT_WELD.md` (conservative 10.50 constant from Prop. 6.6(vi), avoiding the paper's displayed 10.44), `WINDOW_FREEZE_THEOREM.md` (per-window x-freeze), `TAIL_LEMMA.md` (all-N tail contraction — used **instead of** Polymath15 Thm 1.5), `DERIVATIVE_BOX_LEMMA.md` (uniform D_z, D_t), and the Dini y-transfer (`provenance/TRIANGLE_Y_DINI_THEOREM.independent.md`). Per protocol these are flagged, not adjudicated here.

The claim's own sealed review record (`EXTERNAL_REFEREE_REPORT_2026-07-28.md` — a four-agent adversarial AI panel, **not** human peer review, plus a recompute addendum) found no fatal defect, fixed one gating gap (the Dini check was not consumed by the sealed assembly; now wired in), and states the **residual to acceptance = human-mathematician sign-off on three prose-only analytic steps**: (a) B_t ≠ 0 on the closed barrier rectangle; (b) the t>0 → t=0 dominated-convergence extension of Thm 1.3/Lemma 8.4; (c) the Dini y-transfer derivation — plus the precise-PT-height citation discipline. A post-referee `lean/aristotle/` layer (added 2026-08-21, seven Lean 4 projects claiming kernel-verified formalizations of the lemma layer) exists at HEAD but has **not** been audited by this screen and carries no weight in it. Independent human involvement on record: Dan Romik (write access; authored the sealed `independent/` recomputation programs; unsealed manuscript rework under `dan-reworking/`).

---

## 6. VERDICT

**Interim: screen-open — disclosure-complete; checker steps 1, 2, 5 PASS; steps 3–4 pending on D1-side infrastructure. Not screen-pass, not screen-fail, not non-evaluable.**

Reason chain:
1. **Not non-evaluable:** all five required disclosures are present at a pinned commit with a verified seal — the taxonomy's non-evaluable criteria (disclosures absent / environment unreproducible / unverified height consumed) all fail to apply. In particular the claim consumes only the rigorous PT height with exact surplus.
2. **Not screen-fail:** every checker step executed this session passed; no producer disagreement is on record anywhere (claimant-side or in this session's spot-recomputes); no gate failure was found.
3. **Not (yet) screen-pass:** the taxonomy requires "checker accepts, spot-check agrees" — i.e., steps 3 and 4 run by D1's own checker and D1's own two producers. Those artifacts (M1 v1 checker / `BarrierCert` conversion; the Arb and mpmath-ball f_t producer legs) are priced but not yet built. The block is **ours, not the claimant's** — issuing non-evaluable would misassign it, and issuing screen-pass would overclaim.

**What completes the screen (all D1-side; the claimant owes nothing further for evaluability):** (a) M1 v1 checker + `BarrierCertData` conversion of the 883-prism and finite/tail transcripts, then the kernel (or verified-extraction) `checkBarrier` run — this is exactly the M2a′ inventory already in the design-note milestone table; (b) the two-producer spot check per protocol (≥1% of mesh cells + every cell with margin below 2× median) once the D-R3 mpmath ball core and the f_t evaluator layers exist. Re-screen at that point from this file's §1 pinned identity; if HEAD has moved, re-pin and re-verify the seal.

**Consequence meanwhile:** the claim stands as the **strongest known Lane-A prior-art item** — it confirms the design note's Lane-A analysis concretely (same 3×10¹² height, new row, materially better numerics claimed via a curved-barrier instantiation and new error welds) — and remains the natural M2a′ second target **if** the screen completes to pass.

---

## 7. Binding caveats (fixed vocabulary; repeat wherever this claim is mentioned)

1. **Unrefereed.** The claim is a self-published, computer-assisted proof candidate; its own repository says "not yet peer reviewed" and its own review record is an AI adversarial audit, not human peer review. Three analytic steps await human sign-off by its own account.
2. **NOT a record.** The bracket of record remains **0 ≤ Λ ≤ 0.2** (Rodgers–Tao; Platt–Trudgian Corollary 2). Nothing in this screen changes that.
3. **Never cite as a record.** In any D1/program document this item is cited only as "unrefereed claim, screen-open (this file)" — never as a bound in force.
4. **A future screen-pass is not a promotion.** Per the protocol: screen-pass would make the row a candidate second instantiation target for M2a (M2a′) at near-zero marginal Lean cost, and a statement about its certificates — not refereed standing, not kernel-checked standing, not "the record."
5. **Precise-height discipline.** Any statement of hypothesis (i) must cite PT's exact 3,000,175,332,800 — the round "3×10¹²" breaks the licensing (§4 step 2 rider).

---

## 8. Session verification ledger

**Recomputed exactly this session (Python `fractions`, integer cross-multiplication):** the Λ sum; the height conversion and surplus; the Theorem 1.2 preconditions; the canopy identity; the y₀ and √(1−2t₀) brackets; the barrier floor margin; the finite T_min − E_max margin. **Recomputed independently at 60 dps (mpmath):** the window-index bracket x_{690988} < x★ < x_{690989} and both stated margins. **Read from primary sources this session:** Polymath15 Theorem 1.2 full curved statement (on-disk `p3-22a4`); PT Theorem 1 exact height (on-disk `p3-22a1`); the claim's sealed PROOF_NOTE, CANDIDATE_PARAMETERS, README, referee report + addendum, OPEN_REVIEW_QUESTIONS, UPSTREAM, independent/README (all seal-verified 16/16 against `SHA256SUMS` at commit `a74738d`). **Not verified this session (recorded as unaudited):** the heavy certificate contents themselves (the 15 finite shards, the 883-prism logs' arithmetic, the Arb C programs' proof-to-code maps), the `lean/aristotle` layer, the release PDF's prose, the Zenodo archive. Those are precisely the objects steps 3–4 and the M2a′ conversion exist to check.
