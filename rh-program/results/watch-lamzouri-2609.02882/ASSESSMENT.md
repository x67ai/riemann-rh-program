# Assessment — Lamzouri arXiv:2609.02882 and AxiomMath/ZetaZeros (Session 15, 2026-09-03, FYI only)

**[DUAL-MODEL CHECK 2026-09-05, Session 16 — Opus 5 re-derivation (`results/watch-lamzouri-2609.02882/dual-check-O.md`, script `dual-check-O-K2ieps.py`, 40-digit mpmath) plus the orchestrator's (Fable 5.1) independent mpmath re-check of the corrected normalization, run wf_f21601d3-1f1.]** AGREES-WITH-CORRECTIONS. The classification below stands and is no longer single-check. Corrections, binding over the text below: §3's certificate pair is (c₀, r) = (2 − Q(0), −2Q restricted to [0,1]), Q = η²∗η² (the pair written below, c₀ = 2 and r = −Q, has value 1.839 and is not a certificate of the claimed value); the II.4 per-direction step uses three inequalities on three ranges, and the slacks that carry the double-versus-pair comparison are the first-range (α_j − 2)² and the third-range α_j² + 2|α_j|; all numbers in the §2 table are confirmed at 40 digits; the A4/riders sentence is confirmed with the precision that A4 cites BGSTB24 Theorem 1 first and never forms the kernel sum Lemma 3.2 converts. Full record: `dual-check-O.md`.

**Verdict in five lines.** Useful, modestly, as a record and instrument item. It opens no new route to the Riemann hypothesis and changes none of the program's constants or no-go results. On a first reading the new proof sits inside the same two-moment, bandwidth-one certificate class that the barrier zoo's II.1 and II.4 and the A4 no-go paper already cover, so the program's record is unaffected; that reading is single-check and is labeled so below. Nothing needs doing now. Three cheap items go on the queue for whenever the program resumes (dual-model check of the single-check line, a fetch pass for three references, the optional Comparator pattern for our own Lean artifacts).

**Scope of this session.** The sponsor asked only whether these two objects have something useful for us. No verification workflow was run and Lamzouri's proof was not audited; the orchestrator read the paper and the repository, did two one-line computations, and built the Lean repository once. A planned eight-agent stream was dropped at the sponsor's word.

## 1. What the two objects are

| Object | Pin |
|---|---|
| Y. Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line* | arXiv:2609.02882v1 [math.NT], 2 Sep 2026; 14 pp.; text at `sources-extracted/lamzouri-2609.02882v1.txt` |
| github.com/AxiomMath/ZetaZeros (Axiom Math; author Kenny Lau) | commit `4bcaf70`; Lean v4.34.0-rc2, Mathlib v4.34.0-rc2; 32 modules, 7,245 lines; Apache-2.0 |

Lamzouri reproves the Alpöge–Furman (Claude) theorem: simple-and-on-the-line proportion at least C₀ = 3/2 − (1/√2)cot(1/√2) = 0.6725007…, distinct proportion at least (C₀+1)/2 = 0.8362503…. Same constants, different route: no matrix, no rank–trace inequality. The Lean repository formalizes his proof; its zeta theorems take the Riemann–von Mangoldt formula and the Baluyot–Goldston–Suriajaya–Turnage-Butterbaugh (BGSTB24) unconditional pair-correlation lemma as **assumed hypotheses** (Props), and prove his key proposition unconditionally. Our own build: clean, standard axioms only (`lean-build-record.md`).

## 2. What the proof does, in the program's language

Proposition 2.1 of the paper is zeta-free. For any finite multiset Z of complex numbers closed under conjugation (multiplicities m_z) and any real even η ∈ L² with support in (−λ, λ) and η̂²(0) = 1, with K = η̂² (the transform of η²):

    #{simple real points of Z}  ≥  2 Σ_z m_z  −  Σ_{z,s} m_z m_s K(z − s)²,
    #{distinct points of Z}     ≥  (3/2) Σ_z m_z  −  (1/2) Σ_{z,s} m_z m_s K(z − s)².

Mechanism: with f_z(u) = η(u)e^{−2πiuz} and F(u,v) = Σ_z m_z f_z(u) f_z(v), the pair sum is Σ K(z−s)² = ‖F‖² in L²((−λ,λ)²) (his (2.10)). Gram–Schmidt on the nested spans U ⊂ V ⊂ W of the f_x (real x), g_z, h_z gives real diagonal coefficients α_j = ⟨F, ψ_j ⊗ ψ_j⟩ with Σ_j α_j = Σ_z m_z (his (2.21), a trace) and Bessel ‖F‖² ≥ Σ_j α_j² (his (2.14), the diagonal part of a Hilbert–Schmidt norm). Then a² + 1 ≥ 2a on the V∖U range, a² + 4 ≥ 4a on the U range (where multiplicity ≥ 2 and conjugate pairs live, giving Σ_{j ≤ D_U} α_j ≥ 2D_U), and α_j ≤ 0 on W∖V. Section 3 feeds it BGSTB24 Lemma 5 after removing that lemma's weight 4/(4 − (ρ−ρ′)²) by the device r_{δ,T} = Q_δ − Q_δ″/(4 log² T) (his Lemma 3.2), Q = η² ∗ η². His Remark 3.4: the constant C_MT = 1.3274992… is optimal for the method (Carneiro–Chandee–Littmann–Milinovich 2017, Cor. 14). His own words: both proofs "reduce the relevant information to the estimation of a certain quadratic form over the zeros … variants of a second-moment argument … the same Montgomery–Taylor extremal problem".

**Invariants consumed:** a trace (Σ α_j), a Hilbert–Schmidt norm (‖F‖²), integrality of multiplicities and the conjugate-pair count (the U-range bookkeeping). **Where information is discarded:** the off-diagonal components ⟨F, ψ_j ⊗ ψ_ℓ⟩, j ≠ ℓ (Bessel), and the slack of a² + 1 ≥ 2a. That is exactly the data class {tr, ‖·‖²_F, n₊, integer atoms} of zoo entry II.4; the Bessel slack is the Frobenius-minus-diagonal gap already inside ‖·‖²_F, not a new invariant.

**On-line double versus off-line pair inside Proposition 2.1** (orchestrator's computation; K(2iε) = ∫ η(u)² cosh(4πεu) du ≥ 1 since η² is even with integral 1):

| Configuration | Σ m_z | Σ m_z m_s K(z−s)² | right-hand side of (2.4) |
|---|---|---|---|
| double at real x (m = 2) | 2 | 4 | 0 |
| pair x ± iε, both simple | 2 | 2 + 2K(2iε)² | 2 − 2K(2iε)² ≤ 0 |
| pair, ε → 0 | 2 | → 4 | → 0 |

Numeric check with the Montgomery–Taylor η² = f₀ (mpmath, 30 digits): K(2iε)² = 1.00122 at ε = 0.01, 1.1286 at ε = 0.1, 11.93 at ε = 0.5. The certificate reads the multiset only through the two numbers (Σ1, ΣK²), which coincide in the limit; for ε > 0 the pair is charged *more*, the wrong direction for any separation. This is lemmaR_tight's "charge 4" degeneracy (zoo II.4) in Hilbert-space form.

## 3. Relation to the program's ceilings and the A4 no-go — single-check

- **II.1 (bandwidth-one certificate ceiling 0.6818287).** (2.4) holds for every finite conjugation-invariant multiset, so it is a certificate valid configuration-by-configuration, with c₀ = 2 and r = −(η² ∗ η²) supported in [−1, 1]. The ceiling binds it. Lamzouri's admissible r form a subclass (minus autoconvolutions of nonnegative normalized functions of support ≤ 1/2), which is why the route lands at 2 − C_MT = 0.6725 rather than 0.6818; that subclass-versus-class gap is the one the closed A2 direction studied and A4 absorbed. Status: **single-check** (orchestrator's re-derivation from the paper text and full-map.md's Theorem-B description; not yet re-derived by a second model).
- **II.4 (lemmaR_tight).** Present verbatim (table above). Status: **single-check**, but the computation is one line and is reproduced in the zoo's dated note.
- **A4 no-go paper (frozen, Zenodo 10.5281/zenodo.22171688).** Nothing in it becomes wrong: its description of AF's argument as the matrix/rank–trace framework remains a correct description of AF's proof, and its subject (whether a cubic row at a second bandwidth breaks the two-moment degeneracy) is untouched by a second proof that consumes the same two moments. A future revision or the prospectus should carry one sentence noting the matrix-free proof and that the certificate class contains it, after the dual-model check. A4's near-CUE section consumes BGSTB24 in its depth-weighted form under its riders 1–3 (main.tex, "The licensing theorem, and its three riders", ≈ lines 1799–1854), so Lamzouri's weight-removal device is not needed there (orchestrator's reading of those lines, not re-derived).
- **DH filter (I.1) and S1–S5.** A proportion route, exempt; every input (functional equation, explicit formula, mean values via BGSTB24, L² Bessel positivity) is satisfied by Davenport–Heilbronn. The positivity used is L² second-moment positivity, the class the zoo's IV.1 audit files under Weil positivity in disguise; no new S4 generator.

## 4. What is useful (ranked)

1. **[record] A one-page, zeta-free statement of the two-moment certificate class, now formalized.** Proposition 2.1 is the cleanest formal statement of "a certificate valid configuration-by-configuration" the program has seen, and ZetaZeros proves it unconditionally in Lean. Use: cite it in zoo II.4 as the Hilbert-space form (done, dated); adopt it as the canonical formal statement if the zoo's formalization queue is ever worked. Cost now: zero. Porting cost later: real (Lean v4.34.0-rc2 module syntax `module` / `public import` / `@[expose]` versus our v4.33.0-rc2 tree).
2. **[instrument] The Comparator / challenge pattern.** A statement-only `Challenge` file with `sorry`, a `Solution` that discharges it, an axiom whitelist, and an independent re-check by `leanprover/comparator`. This is a better external-facing format for our own kernel-checked artifacts (GridParseval, the W1 instances, BarrierCert) than the current `#print axioms` logs. Cost: an afternoon when the Lean stream next ships something.
3. **[instrument] The weight-removal device** (Lemma 3.2: Q − Q″/(4 log² T) turns BGSTB24's weighted sum into the unweighted K² sum by two applications of the lemma). Not needed by A4 (§3), but the right tool if any future instrument needs the unweighted pair sum from the unconditional theorem.
4. **[watch] References.** Lamzouri's bibliography against our corpus index and fetch ledgers (keyword search only): present or cited — BGSTB 2024 and 2025 (2501.14545), Goldston–Suriajaya 2511.20059 and 2603.28104, GLSS 2503.15449, Chirre–Gonçalves–de Laat 2020, CCLM 2017, Farmer 1995, Bui–Heath-Brown 2013; **no hit** — Aryan 2022 (JNT 233, the unconditional Fejér-kernel pair correlation), Ki–Lee 2012 (70% distinct), Conrey–Ghosh–Gonek 1998. Fetch only if a direction needs them.
5. **[watch] ZetaZeros as a second reference formalization** of zero counting (multiplicity via `analyticOrderNatAt`, counts via `finsum`/`ncard`, pair sums as finsums with the BGSTB weight as a definition). Reusable vocabulary for our D1 Lean work; statement faithfulness not audited.

## 5. What is not useful, plainly

No new route toward RH. No new positivity generator. No change to any proportion constant (0.6725 / 0.8362 are the Alpöge–Furman numbers). No bearing on Track B/C. No effect on the frozen papers' correctness. The Lean repository's zeta theorems are conditional on two assumed Props, so it is not a stronger formal artifact than Zeta23, only a different one.

## 6. Record actions taken this session

- Dated single-check notes in BARRIER-ZOO.md II.1 and II.4; a dated note at the end of `directions/A4-lindelof-lock.md`; a dated line in `results/arxiv/README.md`; a STATUS hard-constraint line and the Session-15+ queue lines below; this directory (`README.md`, `lean-build-record.md`, `ASSESSMENT.md`); paper text in `sources-extracted/`; the PDF gitignored.

## 7. Queue lines for a future session (all cheap; none urgent)

- [record] Dual-model check (standing order 7) of the Session-15 single-check line "Lamzouri's certificate is inside the II.1/II.4 class" before it appears in prospectus v5 or any external document: one Opus 5 re-derivation from `sources-extracted/lamzouri-2609.02882v1.txt` §2 and full-map.md's Theorem-B description; then relabel the three dated notes.
- [instrument] Adopt the Comparator/challenge pattern for the next Lean artifact the program ships.
- [watch] Fetch Aryan 2022, Ki–Lee 2012, Conrey–Ghosh–Gonek 1998 only if a direction needs them; keep BGSTB 2025 and the Goldston–Suriajaya mechanism papers on the existing watch list (closest published relatives of the S2 / o(N)-sensitivity question).

## 8. Provenance

Orchestrator (Fable 5.1) only: full read of the paper text and of ZetaZeros's README, Challenge/Basic.lean, Solution/Basic.lean, Defs.lean, Main.lean and lakefile; greps of the program's record; one mpmath computation (§2 table); one Lean build (`lean-build-record.md`). No subagents. Labeled single-check throughout.
