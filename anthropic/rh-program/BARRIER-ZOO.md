# BARRIER ZOO — the executable falsification suite (applied at BRIEF time)

**Mandate.** Completeness-critic recommendation 4 (2026-08-13, `results/completeness-critic.json`, as recorded in STATUS.md Phase 4): *"institutionalize the barrier zoo as an executable falsification suite applied at BRIEF time — A1/B1/C1 all died post-design-cost to model checks."* This file is that institution. Every future design brief, direction proposal, and Grossmann-style candidate MUST be run through the protocol below BEFORE design cost is spent. The zoo also serves Phase-4 critics as their standard obstruction battery and the D1 certified-refutation arm as its model-world library.

**Created:** 2026-08-19 (Session 5, Phase-5 commissioning). **Compiled from:** STATUS.md (hard constraints, S1–S6 spec), `results/literature.md`, `results/grossmann-sweep.json` + `grossmann-sweep2.json` + `grossmann-sweep2-partial.json`, `results/decisive-tests/ccm-dh-filter.json`, `results/adjudication-{A1,B1,C1,A2,A4}.json`, `results/full-map.md`, `results/corpus-routing.md`. Nothing here is from memory alone; recalled-unverified items are flagged inline.

**Status vocabulary** (per entry): `formalized-in-Lean` (machine-checked in `zeta-23-lean-main`), `computationally-verified` (program numerics under standing order 5), `literature-verified` (statement checked against the tier-1 source / on-disk corpus file), `sweep-certified` (Grossmann-sweep scout verdict, source-pinned), `program-adjudicated` (binding adjudication verdict with computations), `recalled-unverified` (flagged; may not bear decisive weight — standing order 5).

**Scope vocabulary**: `BINDS: full-RH` (proportion/instrument routes exempt but must declare the exemption), `BINDS: all routes` (including proportion work), `BINDS: certificate-class` (routes inside the parent paper's Gram/rank-trace paradigm), `CALIBRATION` (not a kill — a quantitative baseline any claim must beat or explain).

---

## 0. BRIEF-TIME PROTOCOL (the ordered checklist)

A designer submits a brief; a critic (or the designer, pre-submission) runs this checklist IN ORDER. Total cost is hours, not weeks — every test below is either a table lookup, a short computation, or an audit of the brief's own axiom list.

1. **Scope declaration.** The brief states which of {full-RH proof, proportion improvement, instrument, refutation channel} it is. This fixes which barriers bind. A brief that will not declare is returned unread.
2. **Model-world battery** (Group I). For EVERY input/axiom the brief consumes, instantiate the relevant RH-false or adversarial worlds — Davenport–Heilbronn + Epstein at the AXIOM level (I.1), Beurling/Axiom-A worlds (I.2), the AH world and the 256-periodic law (I.3), the graph-zeta ensemble world (I.4), the random multiplicative model (I.5) — and ask: *does the RH-false world satisfy every input?* If yes, the route cannot decide RH (full-RH scope) or must re-derive its claimed edge (proportion scope).
3. **Ceiling arithmetic** (Group II). If the brief is certificate-class: compute the claimed constant against the formalized ceilings; name the invariant beyond {tr, ‖·‖²_F, block structure, n₊} it consumes and where its price is proven; locate its arithmetic input relative to the `O1_bound → prop_PP → tr2` wall.
4. **Structural no-go screen** (Group III). Match the route's mechanism signature (spectral/self-adjoint, positivity-cone, density, sieve, mollifier, modular/entropy, period/FE-group, distance-metric, large-values, cohomological substrate) against the no-go table; each match demands an explicit evasion clause.
5. **Disguise audits** (Group IV). Run the four program-proven audits: (a) Weil-positivity-in-disguise containment (IV.1); (b) hard-input smuggling — is any "second-order/technical" step secretly averaged Hardy–Littlewood, PCC α>1, or a Lindelöf-strength λ_max bound (IV.3, IV.4, IV.6)?; (c) if any cubic/odd-moment row appears: the garnish-absorption and per-block-cubic audits (IV.6, IV.7); (d) if any tilted/reparametrized explicit formula appears: the ghost audit (IV.2).
6. **Visibility pricing** (IV.9). Compute the support/height/truncation at which a SINGLE off-line zero becomes visible to the brief's detector, and verify the brief's numerics and first milestones live in the visible regime (not in an A1-style "deceptive dip" or a CCM-style sub-threshold range).
7. **Process gates** (Group V). Prior-art gate (online, not from memory); every load-bearing recalled claim flagged; evasion arguments themselves verified per standing order 5.

**THE RULE (binding):** a brief that hits any barrier without an explicit, written evasion argument — naming the consumed input the model world violates, or the new invariant with its proven price, or the quantitative reason the ceiling/no-go does not apply — is **RETURNED before design cost**. An evasion argument resting on a recalled-unverified claim is not an evasion argument (standing order 5). A "pass" on this suite is necessary, never sufficient: A4 passed brief-time screens and still needed 7 mandatory repairs — the suite catches structural deaths, not analytic gaps.

**Precedent for the rule:** A1, B1, C1 each consumed a full design cycle and died in Phase 4 to checks in this file (IV.3; IV.4; IV.1+IV.2+I.2 respectively). A2 died to checks now institutionalized as IV.5+IV.6. Every one of those kills was available at brief time for hours of work.

---

## GROUP I — MODEL-WORLD BARRIERS (instantiate the world, run the proposal)

### I.1 The Davenport–Heilbronn / Epstein filter

- **STATEMENT.** The Davenport–Heilbronn function (coefficients a_n = (1, κ, −κ, −1, 0) mod 5, κ = 0.2840790438… by Gauss-sum surd; a = 3/4, conductor 5, entire) and Epstein zeta functions of class-number > 1 binary quadratic forms satisfy: a functional equation, the explicit formula, L² mean-value bounds, and Riemann-von-Mangoldt-type counting — yet violate RH. DH's off-line zero is re-verified at ρ = 0.808517182456637 + 85.699348485377592i (Newton residual 7.6e-41). What DH *lacks*, at the AXIOM level: an intact Euler product (support of Λ_DH off prime powers: Λ_DH(6) = +1.9364, **Λ_DH(12) = −0.7629 < 0 — the one-line witness**), Λ(n) ≥ 0 pointwise, Hecke multiplicativity, Rankin–Selberg-square nonnegativity, membership in any Braverman–Kazhdan/Ngô monoid family (Blomer–Leung converse mechanism, Adv. Math. 471 (2026) 110716 — the sharpest formal home; Epstein rider: E(s,Q) with h(D)>1 is a single-point evaluation of a torus-period orbit that admits no Euler factorization off the full orbit average, per the BZSV scout's Part-B lemma target).
- **KILLS.** Any full-RH route whose entire input list is DH-satisfiable — i.e. FE + EF + L²-means + counting + self-adjointness + spectral realization. Program casualties: the campaign's ~30 routes (transcript residue); B1's M4 (real but redundant separation); the Lapidus school (III.13, axiom-level failure); every "phenomena-level" DH filter (see the CCM case study below).
- **THE CCM CASE STUDY (why the test must run at the AXIOM level).** The decisive pre-design test (`results/decisive-tests/ccm-dh-filter.json`, 2026-08-19, confidence 0.85): the Connes–Consani–Moscovici zeta-spectral-triples mechanism (arXiv:2511.22755) is **arithmetic-blind as probed** — DH passes CCM's "missing step (a)" at every probed truncation (simple even ground state, positive form, D″ spectrum reproducing DH's own genuine low zeros to 1.05e-5, margin collapsing on the same prolate/Fuchs law). At finite truncation ALL Weil-form phenomena are conductor-universal; a DH filter applied to *phenomena* (spectra, margins, ground states) certifies nothing. The filter must ask which *axiom* fails for DH — and for CCM the only failing step is the unproven convergence conjecture itself (= Weil positivity at all supports, by their own Hurwitz argument).
- **EXECUTABLE TEST.** (a) List every input the proposal consumes. (b) For each, evaluate it on DH and on an Epstein h(D)>1 form — by direct computation where numeric (builders exist in `results/ccm-dh-test/`: weilform.py + finisher_weilext.py implement DH, χ₄, χ₅, ζ coefficient systems end-to-end), by axiom audit where structural. (c) PASS (for a full-RH brief) = at least one consumed input **provably fails** for DH/Epstein at the axiom level, with the failure named (e.g. "consumes Λ(n) ≥ 0; Λ_DH(12) < 0"). Phenomena-level separation claims must additionally pass I.6 (conductor-law controls). Proportion briefs: exempt, but must state the exemption and inherit III.1.
- **SOURCE.** STATUS.md hard constraints; `results/decisive-tests/ccm-dh-filter.json`; `results/ccm-dh-test/`; grossmann-sweep2-partial (beyond-endoscopy scout, Blomer–Leung pin); grossmann-sweep2 (relative-langlands-bzsv scout, Epstein rider).
- **STATUS.** computationally-verified (DH construction, witness values, off-line zero, CCM run — standing-order-5 re-verified). **BINDS: full-RH.**

### I.2 The Beurling counterexample factory (DMV / BDR / Broucke school)

- **STATEMENT.** Beurling generalized number systems have a full Euler product, multiplicativity at every prime, and Λ_P(n) ≥ 0 pointwise automatically — yet violate RH maximally. The factory: (a) **DMV** (Diamond–Montgomery–Vorhauer, Math. Ann. 334 (2006) 1–36 = `fetched/p1-02`): N(x) = ρx + O(x^θ), θ < 1, with zeros filling the de la Vallée Poussin boundary — the classical zero-free region is OPTIMAL within Euler-product + integer-density axioms; (b) **[α,β]-systems** (Broucke–Debruyne–Révész, arXiv:2309.01567): populated unconditionally for all α ∈ [0,1), β ∈ [1/2,1); hard wall max{α,β} ≥ 1/2; β < 1/2 only under RH ("RH = Z is the extremal [1/2,0]-system"); (c) **prescribed-zero-contour factory** (Broucke, arXiv:2507.13780): plant zeros ON any prescribed contour with none to the right; (d) **discretization machine** (Broucke–Vindas, arXiv:2102.08478): converts any continuous counterexample into a genuine *discrete* number system PRESERVING Λ_P ≥ 0; (e) **RH-insensitivity detector**: Riemann–von Mangoldt and Carlson density hold for ALL Axiom-A systems (Révész, Broucke pins in sweep report) — hence *any lemma provable from Axiom A alone provably cannot decide RH*; (f) **Λ ≥ 0-insufficiency corollary** (re-derived, elementary): "Λ(n) ≥ 0 pointwise + Euler product + N(x) = ρx + O(x^{1/2+ε})" still admits zeros arbitrarily close to Re s = 1. This factory is the published, systematic form of the Zeta23 campaign's ad-hoc zoo ("Beurling systems with planted zeros, fake Weil polynomials").
- **KILLS.** Any route consuming only {Euler product, multiplicativity, pointwise positivity, integer-density regularity} — including "Λ(n) ≥ 0 as the S1 input" ALONE (relevant to C2's claimed input). Program casualty: C1's M4 margin-propagation (killed by DMV: the OS+CM axiom system as drafted holds in DMV worlds — adjudication-C1 mandatory repair 5).
- **EXECUTABLE TEST.** (a) Does every axiom of the brief hold in a DMV world (or a discretized planted-zero system built by (c)+(d))? If yes and the claimed conclusion exceeds de-la-Vallée-Poussin strength → dead. (b) Is any load-bearing lemma provable from Axiom A alone? Then it is RH-insensitive — it may support infrastructure, never the deciding step. (c) For refutation-channel calibration: use the factory to build the adversarial world the detector must distinguish. Note the closing bracket: adding FE + Euler product + Ramanujan at degree 1 collapses the class to actual L-functions (Kaczorowski–Perelli, see I.7) — the gap between (a)-death and I.7-rigidity is exactly where a sufficient axiom set must sit.
- **SOURCE.** grossmann-sweep.json (beurling-axiom-calibration scout, verdict instrument 0.87 — the S5 = 5/5 engine); corpus `p1-02`, `z-01–z-03`, `z-18`, `t-11b–t-19a`, `t-50`, `w-18a–g` + erratum `r-11a` (JNT 269 (2025) 460–464).
- **STATUS.** literature-verified (arXiv/Crossref pins in the sweep report; DMV on disk). **BINDS: full-RH** (clause (b) binds all routes: it detects insensitive lemmas anywhere).

### I.3 The Alternative Hypothesis world + the 256-periodic adversarial law

- **STATEMENT.** Two adversaries for pair-correlation-based claims. (a) **AH (arithmetic form):** the Alternative Hypothesis — zero gaps at half-integer multiples of the mean spacing, maximally GUE-violating — is consistent with ALL bandwidth-1 pair-correlation data (Goldston–Lee–Schettler–Suriajaya II, arXiv:2507.06823 = corpus y-22). Framing correction (Round-1 ingest, STATUS carry-forward flag ii): AH obstructs *distinguishing GUE*, not the PCC ⇒ 100% conclusion. (b) **256-periodic law (formalized form):** an explicit finitely-supported probability law over 256-periodic marked configurations (marks m ∈ {1,2}, rational weights/positions, exact-rational LP) whose grid form factor is within τ = 3·10⁻⁴⁰ of the CUE value j/256 for 0 < j < 256, edge discrepancy |D(1)| ≤ 0.82395317, simple fraction exactly p₀ = 0.68182868746… — the kernel-checked witness of the bandwidth-one ceiling (II.1).
- **KILLS.** (i) Any claim that bandwidth-≤1 data certify a simple-on-line proportion > 0.6818287 + 2.5431316·10⁻⁶·(|r′(1)| + ∫|r″|); (ii) any claim to *distinguish GUE* or to rule out a GUE-violating universe from bandwidth-1 data; (iii) multiplicity-separation claims at depth → 0 (the law's marks-{1,2} configurations realize lemmaR_tight's degeneracy). Program casualty: A4's AH-evasion bullet — the claimed "combined Fourier support 3λ′ ≈ 3/2" is false; the third trace's true total support is (k−1)λ′ = 1 + 2θ·loglogT/logT (adjudication-A4 R6, computed) — struck.
- **EXECUTABLE TEST.** (a) Certificate-class briefs: evaluate the certificate against the 256-law (re-solve the LP with the brief's rows added; the law and enclosures are in `zeta-23-lean-main/Zeta23/PairCeiling/`, EnclOK sha256-pinned). A "ceiling break" is only evidence if the added rows are backed by proven transport/validity lemmas AND the null model is adversarial enough (A4 R5 lesson: marks-{1,2} + CUE sampling is NOT a decisive gate — the decision LP needs a clustered sine-process null, depth-parametrized pairs u ∈ [0, 1/L′], marks up to a divergent W, and a garnish-capacity fuzz row). (b) Any brief claiming arithmetic content beyond bandwidth 1: compute the actual total Fourier support of its data (tx_081 rule: (k−1)λ for the k-th trace, k odd) — not the naive sum of window widths.
- **SOURCE.** literature.md front 3 + no-go 11; corpus y-21/y-22 (+Suriajaya credit caveat); full-map.md (PairCeiling, NearCUE law); adjudication-A4.json (computations c, R5, R6).
- **STATUS.** formalized-in-Lean (256 law + stability bound, modulo EnclOK interval-arithmetic enclosures); literature-verified (AH). **BINDS: certificate-class and any pair-correlation-only claim; clause (ii) binds all routes.**

### I.4 The graph-zeta ensemble world (Ihara / Ramanujan calibration)

- **STATEMENT.** Ihara zetas of finite regular graphs satisfy finiteness + rationality + functional equation + a trace formula — all four — for EVERY finite regular graph, yet the RH-analogue (Ramanujan property) FAILS generically: only ~69% of random d-regular graphs are Ramanujan (Huang–McKenzie–Yau, arXiv:2412.20263, verified by the sweep scout). LPS graphs are Ramanujan only via Deligne — i.e. via imported arithmetic. Companion fact from the same comparative anatomy: Selberg zetas have full self-adjoint spectral realizations yet generic surfaces have genuine off-line (real) exceptional zeros; the congruence-quotient RH-analogue (Selberg eigenvalue conjecture) is STILL OPEN — self-adjointness alone provably confines zeros only to "line ∪ real segment".
- **KILLS.** (i) "FE + rationality + trace formula + spectral realization suffice" claims — the toy world where RH is *decidable per-object* refutes them; (ii) ensemble/density arguments as RH mechanisms even in decidable worlds (the ~69% cap is the ensemble ceiling's cleanest exhibit); (iii) bare Hilbert–Pólya claims (self-adjointness ⇒ line ∪ real segment, no further — this is the structural reading of the Bombieri–Garrett cap, III.3).
- **EXECUTABLE TEST.** Transplant the brief's mechanism to graph zetas: does it "prove" Ramanujan for all finite regular graphs? If yes, it is wrong (~31% counterexamples exist). If it needs LPS-style arithmetic input to work on graphs, the brief must name the zeta-side analog of that input and show DH lacks it (back to I.1).
- **SOURCE.** grossmann-sweep.json (selberg-ihara-worked-examples scout — the S6 comparative-anatomy report; HMY pin verified).
- **STATUS.** sweep-certified + literature-verified (HMY). **BINDS: full-RH** (clause (ii) binds proportion claims that advertise "100%").

### I.5 The random multiplicative model (Wintner–Harper quenched-transfer barrier)

- **STATEMENT.** In the random multiplicative model, RH holds almost surely (Wintner 1944 — recalled-standard, canonical exhibit in the sweep report) while nothing follows for μ; and the model *provably miscalibrates* at RH-relevant scales: its now-settled a.s. fluctuation scale √x·(loglog x)^{1/4} (Harper IMRN 2023 lower bound + Durkan–Pearce-Crump arXiv:2607.29429 upper, July 2026) disagrees with the Gonek–Ng conjectured √x·(logloglog x)^{5/4} for the true M(x) — the i.i.d.-on-primes model fails exactly at the scale where zero-correlation information lives. (The scale disagreement's zeta side is conjectural; the model-side scale is a theorem.)
- **KILLS.** Quenched → deterministic transfer: any route deriving RH-grade conclusions for ζ from distributional/almost-sure/family-averaged statements in a random model (GMC limits, moment asymptotics, a.s. bounds). A single off-line zero is a measure-zero event, invisible to every such statement (Saksman–Webb's GMC limit for actual ζ on random windows is UNCONDITIONAL — hence zero RH content).
- **EXECUTABLE TEST.** (a) Is the brief's input a distributional/a.s./averaged statement? Then demand the deterministic bridge lemma explicitly, and check it against the (loglog x)^{1/4}-vs-(logloglog x)^{5/4} mismatch. (b) Does the input hold verbatim in the random model? Then by Wintner it cannot decide RH. Alive exception (the honest interface): Harper-conditioning transplanted to fixed short windows of length 1/log T — the Lindelöf-lock supply line for A4 (arXiv:1703.06654, arXiv:2301.04390 = fetched-r3) — which makes no single-zero claim.
- **SOURCE.** grossmann-sweep2.json (harper-multiplicative-chaos scout, instrument 0.85).
- **STATUS.** sweep-certified; literature-verified except the Gonek–Ng target (conjectural) and Wintner (recalled-standard). **BINDS: full-RH.**

### I.6 The conductor law c = 4π/q (Weil-form margin calibration — NEW, program-discovered)

- **STATEMENT.** The ground-eigenvalue collapse rate of truncated Weil quadratic forms obeys the conductor law **c = 4π/q**: fitted rates over μ = λ² ladders give c_ζ = 12.596 (4π, +0.2%), c_χ₄ = 2.991 (4π/4, −4.8%), c_χ₅ = 2.669 and c_DH = 2.604 (both → 4π/5; the RH-false DH and the RH-true SAME-CONDUCTOR χ₅ agree to 2.4%). The RH-true baseline is the conductor-rescaled Fuchs prolate-leakage law ε ~ poly·e^{−4πμ/q} (Fuchs 1964 = `fetched/p1-04`, pp. 317–330; prefactor reproduced to 0.7% of CCM's (2¹⁴/3)√2·π⁵). The spectacular ζ-vs-DH gap (1e-38 vs 1e-6 at λ=3) that read as an arithmetic signal was a q=1-vs-q=5 effect.
- **KILLS.** "Separator-via-rate" and "separator-via-margin" readings: any claim that a Weil-form/spectral-truncation phenomenon (margin size, collapse rate, low-zero matching accuracy) is arithmetic-sensitive, made without conductor-matched RH-true controls. Program casualty: the Session-4 collapse-rate reading of the CCM experiment (refuted by the χ₅ control).
- **EXECUTABLE TEST.** Any brief exhibiting a numerical positivity/margin/spectral phenomenon as evidence of S1 content must: (a) run at least one RH-true Euler-intact control at the SAME conductor and gamma-shape as its RH-false test object; (b) show a departure from the conductor-Fuchs baseline ε ~ poly·e^{−4πμ/q} at accessible depth. No departure ⇒ the phenomenon measures archimedean data, not arithmetic. Positive use (B2 channel): an anomalously LARGE Weil-form minimum against the conductor baseline at growing support is a computable signature of a nearby off-line zero.
- **SOURCE.** `results/decisive-tests/ccm-dh-filter.json` (headline 3, alternatives 3+5); `results/ccm-dh-test/finisher_fits.json`; `fetched/p1-04`.
- **STATUS.** computationally-verified (four systems, 10–14 support points each; standing-order-5 re-verified, rebuilds ≤ 1e-15). **CALIBRATION** (binds any brief using Weil-form numerics as evidence).

### I.7 Degree-one rigidity (the calibration bracket any new axiom set must clear)

- **STATEMENT.** Selberg class degree 1 = ζ + shifted Dirichlet L-functions only, and there are no elements of degree 1 < d < 2 (Kaczorowski–Perelli, Acta Math. 182 (1999) 207–241; Ann. of Math. 173 (2011) 1397–1441; corpus Selberg-class cluster `u-26a`, `u-22a`, `u-32b`, `u-35b` — read the orientation survey u-35b first). FE + Euler product + Ramanujan at degree one collapses the axiom class to actual L-functions — the closing bracket to the Beurling factory's opening bracket (I.2): below these axioms, counterexamples are mass-produced; at them, rigidity.
- **KILLS.** Nothing by itself — it is the two-sided CALIBRATION the sweep ordered for every de-novo axiom set: a proposed axiom system for "the class RH is provable for" must (a) fail in Beurling worlds (I.2) and (b) reproduce degree-one rigidity (or explicitly contain it). An axiom set passing (a) but not (b) is too weak to know what its own objects are; one failing (a) proves nothing.
- **EXECUTABLE TEST.** For any Track-C/de-novo brief: derive (or cite as target) the degree-one classification within the proposed axioms; exhibit the axiom that DMV worlds violate. Both clauses in writing before design cost.
- **SOURCE.** grossmann-sweep.json (beurling scout, key object 9; sweep verdict "calibration theorems: Beurling degree-one rigidity"); corpus routing (Track-C table).
- **STATUS.** literature-verified (corpus on disk). **CALIBRATION** (binds Track-C/de-novo axiom sets).

---

## GROUP II — FORMALIZED CEILINGS (machine-checked in `zeta-23-lean-main`; exact constants)

### II.1 The bandwidth-one certificate ceiling 0.6818287

- **STATEMENT.** EVERY bandwidth-one certificate (c₀, r), r ∈ C¹[0,1] reading only form-factor data on [0,1] and valid configuration-by-configuration, certifies a simple-zero proportion ≤ **0.6818287** + 2.5431316·10⁻⁶·(|r′(1)| + ∫|r″|) — proven against the 256-periodic near-CUE law (I.3b). The parent paper's 0.6725 sits ~0.009 below its own method-class ceiling. Payoff table (paper Remark 1.1): pair-correlation support ≈ 1.043 → 70%, 1.265 → 80%, 1.70 → 90%. Explicitly OUTSIDE scope: certificates using constraints the 256-law violates but ζ satisfies — e.g. F(α) ≥ 0 for |α| > 1 (Chirre–Gonçalves–de Laat under RH reach **0.6792**, GRH **0.6845**; corpus `w-08` — inequalities NON-STRICT), or average (non-configurationwise) validity.
- **KILLS.** Any brief claiming > 0.6818… from bandwidth-1 configurationwise data. Prior-art rider: the honest open gap for RH-conditional work is 0.6792 → 0.6818287 = 0.0026 (w-08 pre-empted A2's novelty claim).
- **EXECUTABLE TEST.** State the brief's data class (bandwidth, validity mode). If bandwidth ≤ 1 + configurationwise: the claimed constant must be ≤ the ceiling, or the brief must name which out-of-scope constraint it consumes and where that constraint is proven (F-positivity beyond [−1,1] is RH/GRH-conditional). LP re-solve against the 256-law available as a direct check.
- **SOURCE.** `Zeta23/PairCeiling/` (EnclOK sha256-pinned); full-map.md §formalized-obstruction; v5 §7.2 (in-paper ceiling).
- **STATUS.** formalized-in-Lean. **BINDS: certificate-class (all scopes).**

### II.2 The two-moment cap: κ(λ) = 1/λ + λ/3 ≥ 2/√3 ⇒ ≤ 0.8453 at ANY bandwidth

- **STATEMENT.** The trace+Frobenius certificate constant is 2 − κ(λ) with κ(λ) = 1/λ + λ/3; by AM–GM κ ≥ 2/√3 ≈ 1.1547 > 1 for ALL λ > 0, so two-moment certificates cap at 2 − 2/√3 ≈ **0.84530** (attained at λ = √3), verified numerically (STATUS verified-numerics table). The λ/3 form-factor term is contributed by the zeros themselves (near-CUE randomness), not by technique deficiency — arbitrary-length mean-value theorems cannot help.
- **KILLS.** "Proportion 1 via better mean values" inside the two-moment class: even granting full Hardy–Littlewood at every bandwidth, {tr, ‖·‖²_F} certificates never reach RH-strength. Forces every RH-complete certificate route to add functionals beyond the two moments — and then IV.6/IV.7 bind.
- **EXECUTABLE TEST.** If the brief's functional list is {tr, ‖·‖²_F} (+ rank/inertia): its ceiling is 0.8453 regardless of arithmetic input claims. Any higher claim must name the third functional and its unconditional price.
- **SOURCE.** Lean `kfun`/FinalMult.lean; full-map.md lines 311–315; STATUS hard constraints.
- **STATUS.** formalized-in-Lean + computationally-verified. **BINDS: certificate-class (all scopes).**

### II.3 The dimension cap d = λN

- **STATEMENT.** The Gabor test space at critical sampling has d = λ·N(T,2T)(1+o(1)) atoms; rank P and n₊ ≤ d, so no certificate of this kind certifies more than λN on-line points — 100% requires λ = 1 exactly; λ ≤ 1/2 certifies nothing (which voids the "many moments available at kλ < 2, λ small" escape). Paper Prop. 7.4.
- **KILLS.** Small-bandwidth escape routes ("use λ < 1/2 where k = 4,5,… moments are unconditional"); any resource plan whose bandwidth and claimed proportion violate proportion ≤ λ.
- **EXECUTABLE TEST.** One-line arithmetic: claimed proportion vs stated λ.
- **SOURCE.** Lean (Prop 7.4 formalization); full-map.md line 184.
- **STATUS.** formalized-in-Lean. **BINDS: certificate-class (all scopes).**

### II.4 lemmaR_tight — the two-moment degeneracy (double ≡ deep pair)

- **STATEMENT.** On configurations of orthonormal on-line atoms (integer m_j ≤ c) plus b pair-blocks of eigenvalue c: 2c·tr(P+Q) − ‖P+Q‖²_F = Σ_j k_c(m_j) + c²b EXACTLY (k_c(p) = c² − ((c−p)₊)²) — the rank-trace certificate is saturated, and at c = 2 an on-line DOUBLE zero (k₂(2) = 4) is indistinguishable from an off-line pair at depth → 0 (charge 4). `Zeta23/ZeroSide/TightMult.lean` (lemmaR_tight, lines 93–122). Tightness is relative to the invariant list {tr, ‖·‖²_F, atom norms ≤ 1, n₊} — an invitation to add invariants (λ_max, cubic traces, windowed/shifted traces), each of which is priced elsewhere in this zoo (IV.6, IV.7, II.5).
- **KILLS.** "Better linear algebra on the same two moments" (any claimed improvement without a new invariant is provably false); multiplicity-visibility claims (S3) made from Weil-form two-moment data.
- **PROGRAM BOOKKEEPING (2026-08-19, binding):** lemmaR_tight is NOT yet broken by anything currently provable. It breaks only if A4's M2-corrected gate shows the budget cuts the doubles corner (adversely indicated, ≤ 50%) AND the R2 V-dependent bridge lands (~0.8 provable). Any brief claiming to break it must engage both.
- **EXECUTABLE TEST.** Does the brief separate on-line doubles from off-line pairs? Then name the invariant beyond the list, its unconditional price, and run IV.6/IV.7 on it. Depth-continuity check (A4 computation h): shallow pair blocks have eigenvalues → (+2, −0) with cubic charge → +8 (= the double's) — any separation claim must be depth-uniform or priced over the depth family u ∈ [0, 1/L′].
- **SOURCE.** Lean TightMult.lean; full-map.md; adjudication-A4.json (merge_guidance, computation h).
- **STATUS.** formalized-in-Lean. **BINDS: certificate-class; the S3 clause binds all full-RH routes.**

### II.5 The wall's street address: O1_bound → prop_PP → tr2, and the Rudnick–Sarnak range

- **STATEMENT.** The entire bandwidth-1 restriction enters the formalization through ONE lemma chain (PrimeSideB): off-diagonal prime pairs in tr G̃² are bounded via Montgomery–Vaughan in ABSOLUTE VALUE — zero cancellation used. λ > 1 requires Hardy–Littlewood-strength prime-pair correlations (Montgomery's F(α), |α| > 1). Higher moments tr R^k are diagonal-dominated only in the Rudnick–Sarnak range kλ < 2; k = 3 admissible for λ < 2/3 but odd moments provably cannot improve a count on [0,∞) without a λ_max bound = Lindelöf-strength control of Σ_{n≤X} Λ(n)n^{−1/2−iτ} on windows of length 1/L (the "Lindelöf lock" — the A4 direction's target); k = 4 needs λ < 1/2, where II.3 kills everything.
- **KILLS.** Nothing by itself; it LOCATES where any proportion progress must pay. Vague "improve the off-diagonal treatment" briefs are returned with this address: the improvement is averaged-HL (see IV.3 for what claiming it cheaply looks like).
- **EXECUTABLE TEST.** Every certificate-class brief must state which of the three entry points it pays at (cancellation in O1_bound; a λ_max/short-window bound; a new invariant per II.4) and cite the unconditional input. GRH-conditional super-bandwidth data exists (corpus w-19: F(α) ≥ 3/2 − |α| − ε on 1 ≤ |α| ≤ 3/2 − 2ε under GRH for Dirichlet L) — usable only in explicitly conditional briefs.
- **SOURCE.** full-map.md (bandwidth analysis); STATUS hard constraints; corpus w-19.
- **STATUS.** formalized-in-Lean (the chain); literature-verified (RS range, w-19). **BINDS: certificate-class.**

---

## GROUP III — STRUCTURAL NO-GOS (literature- and sweep-certified; match by mechanism signature)

### III.1 o(N)-blindness of density methods (PCC ⇒ 100% without RH)

- **STATEMENT.** Pair correlation ALONE, without RH, already implies 100% of zeros simple and on the line (Goldston–Lee–Schettler–Suriajaya, arXiv:2503.15449 = corpus y-21). Hence the marginal value of ALL bandwidth → ∞ pair data is exactly "100% but not RH": o(N) exceptional zeros are structurally invisible to every density-type statement. The parent paper's own disclaimer (§7.5, HL*(k₀,λ) program): "RH itself is out of reach of the mechanism."
- **KILLS.** Any density/proportion/moment route CLAIMING full RH (spec S2). Also deflates "just push the proportion" pitches: the asymptote is known and it is not RH.
- **EXECUTABLE TEST.** Add o(N) adversarial off-line zeros to the brief's model configuration; if every consumed input is unchanged to o(1), the route is o(N)-blind — full-RH claims die, proportion claims survive with the exemption declared.
- **SOURCE.** literature.md front 3; STATUS findings log 2026-08-11; corpus y-21/y-23.
- **STATUS.** literature-verified. **BINDS: full-RH.**

### III.2 Bombieri small-support (small cones prove nothing)

- **STATEMENT.** Weil-positivity is UNCONDITIONAL for test functions of small support, and genuine negativity appears once support reaches (1/p, p) (Bombieri, Lincei 2000; the deepest single analysis of the Weil form incl. the archimedean obstruction is on disk as `fetched-r2/u-23a`). Small-support cones can never certify RH; the campaign's own certified-margin work (e^{−4πX} law on supp [1/3,3], primes 2,3,5,7) lives entirely in this regime — and I.6 now shows such margins are conductor-universal anyway.
- **KILLS.** "Positivity verified on small support" as evidence of an RH mechanism; extrapolation of small-support certificates.
- **EXECUTABLE TEST.** Compute the support at which the brief's positivity claim is tested vs the support at which its target statement requires positivity; if the tested regime is inside the unconditional zone, the evidence is content-free. Cross-run I.6's conductor controls on any numeric margin.
- **SOURCE.** literature.md front 5; corpus u-23a, u-19a (Bombieri–Lagarias Li bridge).
- **STATUS.** literature-verified. **BINDS: full-RH** (and any evidence claim from small-support numerics).

### III.3 Bombieri–Garrett ~94% spectral cap

- **STATEMENT.** Pseudo-Laplacian (Friedrichs-extension) discrete spectra can contain at most ~94% of the zeros — forced by pair correlation + ζ(1+it) growth (Bombieri–Garrett, arXiv:2002.07929). Structural reading from I.4: self-adjointness confines to "line ∪ real segment," never further, absent functorial input. The arithmetic-QUE corner's spectral route IS this cap (sweep dead-end III.19); BZSV's only line-targeting relative (pseudo-Laplacian perturbation by period distributions) is exactly this capped route (III.12).
- **KILLS.** All-zeros spectral-embedding routes via exotic self-adjoint extensions / pseudo-Laplacians.
- **EXECUTABLE TEST.** Does the brief embed zeros into the discrete spectrum of a self-adjoint (pseudo-)Laplacian-type operator? Then it caps at ~94% — full-RH claims die; the brief must show its operator class evades the hypothesis (and then I.1: does DH admit the same construction?).
- **SOURCE.** literature.md fronts 5/11; grossmann-sweep.json (arithmetic-que dead-end); grossmann-sweep2.json (bzsv scout S5).
- **STATUS.** literature-verified. **BINDS: full-RH.**

### III.4 The parity problem

- **STATEMENT.** Sieve-only methods are blocked from RH-strength conclusions (Selberg 1949; Tao 2007 — recalled-standard pins; M(x) ≪ x^{1/2+ε} ⟺ RH). Pretentious-school self-assessment (Granville, verbatim per sweep scout): multiplicative-function arithmetic alone is "unlikely to rule out" even Siegel zeros — if it cannot reach the Siegel zero it cannot reach RH.
- **KILLS.** Routes whose arithmetic input is entirely sieve-type (linear forms in Λ with sieve-weight positivity); Möbius-cancellation claims from sieve axioms.
- **EXECUTABLE TEST.** Check whether the brief's arithmetic inputs distinguish Λ from its parity-flipped counterfeit (the classical Liouville-dressing); if not, the route caps at parity strength. (This is the A1 lesson's cousin: a sieve upper bound consumed where signed cancellation is needed — IV.3.)
- **SOURCE.** literature.md no-go 11; grossmann-sweep2.json (pretentious scout S5).
- **STATUS.** literature-verified (mechanism); pins recalled-standard. **BINDS: full-RH.**

### III.5 Conrey–Li (de Branges positivity fails)

- **STATEMENT.** The positivity conditions de Branges' approach requires FAIL numerically (Conrey–Li, IMRN 2000, arXiv:math/9812166 = corpus `p1-06`). Program-verified reading cautions: Conrey–Li operate at E(z) = ξ(1−iz), i.e. the a = 1 coordinate, NOT a = 1/2 (C1's lines 29/39 were inverted on exactly this — corpus response §4 replacement text is mandatory); F(W) is not a space of entire functions as sometimes paraphrased; and the ξ-normalization trap (Lagarias defines ξ WITH the ½ factor, Conrey–Li without — the factor-of-4 discrepancy source, routing caveat 12). Suzuki's unconditional complement (corpus p2-B1x, Thms 1.4/1.5): no compression, no Gram matrix, no certificate from the Weil-distribution space.
- **KILLS.** Unmodified de Branges-positivity routes; any brief citing "de Branges space positivity" without engaging the numerical counterexamples and the a-coordinate distinction. (B3 survives precisely because K_a kernels are multiplicity-visible and it engages this barrier explicitly.)
- **EXECUTABLE TEST.** Locate the brief's claimed positivity in the (a, normalization) coordinates; check it against Conrey–Li's counterexamples in the correct coordinate; verify any "essentially due to de Branges" attribution against `w-04/w-05a/w-05b` (vision pipeline, caveat 4 — the fidelity check still carries a standing risk flag).
- **SOURCE.** literature.md front 7; corpus p1-06, p2-B1x, w-05b; routing caveats 4/12.
- **STATUS.** literature-verified (counterexamples on disk). **BINDS: full-RH routes through HB/de-Branges positivity.**

### III.6 Rodgers–Tao Λ ≥ 0 (no margin below criticality)

- **STATEMENT.** The de Bruijn–Newman constant satisfies Λ ≥ 0 (Rodgers–Tao, arXiv:1801.05914; corpus p3-22a3); RH ⟺ Λ = 0. Standing program bracket **[corrected 2026-08-26, Session 6]: 0 ≤ Λ ≤ 0.2** — Λ ≤ 0.2 is Platt–Trudgian Bull. LMS 53 (2021) **Corollary 2** (p3-22a1 §3.4: Polymath15 Table 1 row 2 at H > 2.51·10¹² + their verified H = 3·10¹²; PDF text verified three ways in Session 6). The previous "[0, 0.22]; the 0.2 line is NOT the standing record" wording was a propagated Round-2 verification error, now superseded (see routing caveat 9). Still binding: the STRICT "Λ < 0.2" remains unproven — never write it; Λ < 0.19 would need H > 10¹³ (PT). "RH, if true, is barely true": zero margin for smoothing/heat-flow shortcuts. Corollary channel: a certified Λ > 0 would DISPROVE RH — the only channel that could literally decide RH (negatively) within the horizon (D1 arm).
- **KILLS.** Heat-flow/smoothing arguments that would, if valid, prove Λ < 0; any mechanism giving RH "with room to spare" in the flow variable.
- **EXECUTABLE TEST.** Apply the brief's deformation mechanism at t slightly negative (backward flow): if it would prove zeros stay on the line there too, it contradicts Λ ≥ 0 and is false. Check all Λ-adjacent claims against the standing bracket.
- **SOURCE.** literature.md front 4; corpus p3-22a3/a4/a5, t-60b (dBN kernel certified NOT PF₅); routing caveat 9.
- **STATUS.** literature-verified. **BINDS: all routes touching the dBN flow; the disproof channel is B2/D1 property.**

### III.7 Mollifier limits (Radziwiłł; θ = 4/7)

- **STATEMENT.** Intrinsic ceiling for Levinson–Conrey with one-piece arbitrary-length mollifiers (Radziwiłł, arXiv:1207.6583); separately the θ = 4/7 mollifier-length barrier (Conrey via Deshouillers–Iwaniec). Program-verified sharpening for weighted Gram certificates in IV.4 (B1's kill).
- **KILLS.** "Longer/cleverer mollifier ⇒ proportion 1" briefs; mollifier-length claims past 4/7 without new bilinear technology.
- **EXECUTABLE TEST.** Extract the brief's mollifier length exponent and gain claim; compare against Radziwiłł's bound and the 4/7 wall; if the brief reweights a Weil-form certificate, run IV.4's fourth-moment divergence check.
- **SOURCE.** literature.md no-go 11; corpus y-26 (Conrey–Farmer short mollifiers — the 2025 state of the art works *regardless of mollifier length*, i.e. around, not through, this wall).
- **STATUS.** literature-verified. **BINDS: certificate/mollifier-class (all scopes).**

### III.8 Gesteau–Liu modular no-go (no arithmetic half-sided modular inclusion)

- **STATEMENT.** The arithmetic thermal system ("Riemannium"/primon gas, spectral support {log p}) admits NO half-sided modular inclusion at ANY temperature — discrete spectral support kills it; the needed "modular chaos" (L¹-decay of thermal two-point functions of prime modes) is conclusion-grade input (Gesteau–Liu, arXiv:2408.12642, Prop 2.9/2.11, verified from PDF by the sweep scout). Reinforced by vN-level erasure: for β ∈ (0,1] the BC-system KMS factor is the unique injective III₁ factor (Connes–Haagerup), so EVERY modular invariant of the arithmetic system coincides with any sufficiently mixing counterfeit — the DH filter fails at exactly the layer where modular machinery operates; type III factors have no trace, so no S6 finite-rank calculus can exist inside the framework. The cooled/distilled spectral realization carries zero RH content (Meyer 2005; unconditional form on disk as `u-33b` — text layer drops "c", never text-search).
- **KILLS.** Modular/relative-entropy positivity routes (Tomita–Takesaki, Araki/QNEC, Borchers–Wiesbrock positive-generator constructions) as RH engines — the one genuinely new S4 class wave 1 had flagged, now certified dead (tomita-takesaki-entropy dead-end 0.72). Only escape: derive modular chaos from an interaction consuming multiplicativity at every prime AND exhibit the axiom that fails for a DH counterfeit flow — burden stated in the scout's interface clause, currently discharged by no one.
- **EXECUTABLE TEST.** Does the brief's positivity generator live at the von Neumann/modular layer? Then: (a) cite what evades Prop 2.9/2.11 for discrete spectral support; (b) show which modular invariant survives injective-III₁ uniqueness; (c) run I.1 on the claimed interaction. Absent all three, returned.
- **SOURCE.** grossmann-sweep2.json (tomita-takesaki-entropy scout, dead-end certificate).
- **STATUS.** sweep-certified + literature-verified (GL PDF read). **BINDS: full-RH.**

### III.9 Pretentious D-continuity / Halász floor

- **STATEMENT.** The Granville–Soundararajan pretentious metric has total diameter ~√(2 loglog x); the school's own formalized floor (GS book draft Ex. 2.3.1 + p.74, verbatim per sweep scout): distance data cannot improve error terms beyond (loglog x)/log x — all zero-location content from D-data is confined to the classical de la Vallée Poussin edge. Power cancellation is NOT D-continuous (Jung–Lemke Oliver, MPCPS 154 (2013) 481–498: f₁, f₂ with D(f₁,f₂;x) = o(1) yet x^{1−δ} vs x/(log x)^A partial sums). The 3-4-1 inequality is Fejér-square positivity — the identical 1899 generator behind classical zero-free regions, edge-capped for 125 years.
- **KILLS.** Multiplicative-distance routes to interior zero-free regions or RH; "pretentious classification ⇒ zero repulsion" briefs. RH, Lindelöf, and every interior zero-free region are provably NOT pretentious-metric-continuous properties. Survives only: the refutation direction (Kerr–Klurman–Thorner, arXiv:2408.03938 — certified large partial sums ⇒ off-line low-lying zero; a B2 instrument).
- **EXECUTABLE TEST.** Is the brief's arithmetic input expressible as a D-metric-continuous functional on {f multiplicative, |f| ≤ 1}? Then it caps at dlVP strength. The brief must exhibit the power-scale rigidification axiom beyond D-data it consumes (and run I.2 on it).
- **SOURCE.** grossmann-sweep2.json (pretentious-multiplicative scout — the branch-closing no-go is stated there as a formalizable theorem target, "cheapest, already a book exercise").
- **STATUS.** sweep-certified + literature-verified (GS book/JLO pins). **BINDS: full-RH and interior-region claims.**

### III.10 ANTEDB DH-blindness ceiling (large-value calculus)

- **STATEMENT.** The entire large-value/exponent-pair/decoupling calculus (Bourgain–Demeter–Guth, Wooley, Guth–Maynard arXiv:2405.20552, Tao–Trudgian–Yang ANTEDB arXiv:2501.16779) is stated for ARBITRARY ℓ∞-bounded coefficients on frequencies {log n} — every axiom holds VERBATIM for the DH series (coefficient-blind at the axiom level; even GM's zeta-specific additive-energy gain is DH-invariant). Its own TERMINAL conjecture (Montgomery large values) yields only the Density Hypothesis (Guth survey arXiv:2503.07410 §3.4); the σ ≤ 3/4 decoupling-only case is already capped unconditionally by Guth's almost-counterexample (§5.5). Sup of zero-location output over the LP-closure of the full axiom set + its terminal conjectures = Density Hypothesis + Vinogradov–Korobov-shape regions. Both parts are ANTEDB-executable/formalizable (the sweep's "DH-blindness ceiling theorem" deliverable).
- **KILLS.** "Push Guth–Maynard/decoupling harder toward RH" briefs; any claim that large-value technology can exclude even one off-line zero. (It remains THE supply line for A4's tail bounds — instrument, not engine.)
- **EXECUTABLE TEST.** If the brief's inputs are large-value/mean-value estimates for Dirichlet polynomials with unstructured coefficients: its terminal payoff is density-class; full-RH claims returned. Where feasible, check the claimed estimate against the ANTEDB LP-closure (expdb) — if the claim beats the closure, it is either new arithmetic input (name it, run I.1) or an error.
- **SOURCE.** grossmann-sweep2-partial.json (decoupling-structural-ceiling scout, instrument 0.87).
- **STATUS.** sweep-certified + literature-verified. **BINDS: full-RH; CALIBRATION for proportion briefs (ANTEDB closure = the known-axiom optimum).**

### III.11 Sawin–Whitehead FE-group classification + DGG natural boundaries (MDS agnosticism)

- **STATEMENT.** In Weyl-group multiple Dirichlet series, zeta's zeros enter ONLY as locations of polar divisors (scattering denominators) — the continuation mechanism is valid wherever the zeros happen to be, hence zero-position-AGNOSTIC; moving a DH-surrogate zero through the scattering data changes nothing the machinery proves. The axiomatic ceiling map is the school's own 112pp classification (Sawin–Whitehead, arXiv:2507.08662); the naive moment-MDS class has proven NATURAL BOUNDARIES (Diaconu–Garrett–Goldfeld, Progr. Math. 300, 2012 — DGH Compositio 139 on the ROUND-3 sponsor list); coefficient positivity (Waldspurger squares L(1/2,χ_d) ≥ 0) feeds Landau's theorem only at REAL points of the w-line, provably unable to reach complex scattering divisors. Even total success of the moment program tops out at Lindelöf.
- **KILLS.** FE-group/MDS-based zero-location claims; "period/moment positivity in families ⇒ RH" via double Dirichlet series. Contrast fact for S6: the same school's function-field triumph (BDPW arXiv:2302.07664, all-moment CFKRS) runs SOLELY on Deligne purity — corroborating "the generator exists but the geometry does not."
- **EXECUTABLE TEST.** For any families/moments/MDS brief: (i) identify where the diagonal factor's zeros enter (polar loci only?); (ii) run the DH-surrogate move — if the machinery's conclusions are invariant, it is S2 = 0; (iii) trace every positivity input to the real-point reach of Landau.
- **SOURCE.** grossmann-sweep2.json (weyl-group-mds scout, instrument 0.85 — the three-part calibration theorem is stated there as a formalizable deliverable).
- **STATUS.** sweep-certified + literature-verified. **BINDS: full-RH.**

### III.12 BZSV discrete-point lock (period positivity flows FROM RH)

- **STATEMENT.** In relative-Langlands duality (Ben-Zvi–Sakellaridis–Venkatesh), L-values enter ONLY at the discrete set of half-integer shifts of the center attached to the G_gr-grading (BZSV eq. 14.3) — no continuous s-parameter, no interior reach. And the numerical conjecture's L-value nonnegativity is justified BY the Riemann hypothesis (BZSV p.292, fn.115, read verbatim by the scout): period positivity flows FROM RH into the framework — circular as an RH engine. Number-field/archimedean theory explicitly unbuilt (Rmk 1.1.3). Companion cap: the only line-targeting relative is the Bombieri–Garrett-capped pseudo-Laplacian route (III.3).
- **KILLS.** "Hyperspherical period positivity / Waldspurger–Ichino–Ikeda nonnegativity aggregated over families ⇒ zero-location" briefs — no aggregation over pairs/representations/twists yields sign statements at any interior point off the discrete set, nor excludes a single off-line zero.
- **EXECUTABLE TEST.** For any period-positivity brief: (i) list the s-points its positivity statements actually concern (half-integer center shifts only?); (ii) trace the sign input — if it descends from purity/GRH, the route is circular; (iii) the S1 rider that DOES survive: the Epstein no-Euler-factorization lemma (I.1 rider) — a brief may consume that as an axiom, never the period positivity as an engine.
- **SOURCE.** grossmann-sweep2.json (relative-langlands-bzsv scout, instrument 0.82; discrete-point ceiling theorem stated as formalizable deliverable).
- **STATUS.** sweep-certified + literature-verified (fn.115/14.3 read directly). **BINDS: full-RH.**

### III.13 Lapidus equivalence-level death certificate

- **STATEMENT.** Everything proven in the complex-dimensions/spectral-operator program is EQUIVALENCE-level (RH ⟺ quasi-invertibility of a_c for all c ≠ 1/2; RH ⟺ (ISP)_D for D ≠ 1/2) — the campaign-post-mortem class. The school's own statement that its criteria extend to "essentially all" GRH-class functions = axiom-level DH-filter failure (the machinery mirrors ANY zero set). The one non-circular target — coercivity inequality (64) (Phil. Trans. R. Soc. A 373 (2015) 20140240) derived from an operator-valued Euler product with DH-discrimination — was announced 2014–15 and never produced; as stated, (64) is RH reparametrized. Midfractal c = 1/2 excluded by construction.
- **KILLS.** Fractal-string/complex-dimension/quantized-number-theory routes absent a genuinely new generator; "inverse spectral problem ⇒ RH" briefs (the sensitivity is a restatement of the zero set — no independent detector).
- **EXECUTABLE TEST.** For any equivalence-heavy brief (this school or otherwise): identify the one implication that is NOT a reparametrization and check whether it consumes an input DH violates (it will be the unproven one). If every proven statement is an equivalence, the brief is an instrument at best.
- **SOURCE.** grossmann-sweep2.json (lapidus-complex-dimensions scout, dead-end 0.85 — "the cheap certificate wave 1 predicted"); corpus r-10, t-53, r-27b/r-28b/t-29b.
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.14 Deninger's own no-go: no real-coefficient Weil cohomology

- **STATEMENT.** There is no Weil cohomology theory with real coefficients for arithmetic schemes of the kind naive transfers require (Deninger, arXiv:2204.02714 = `fetched/x-04`) — the in-house bound on shortcuts to a cohomological RH proof; any candidate cohomology must evade this at the design stage. Companion state-of-the-art: both model-world halves of Deninger's program are now theorems (ALKL trace formula arXiv:2402.06671; regularized determinants arXiv:2410.20758) but no cohomology exists on the arithmetic object.
- **KILLS.** "Just build H¹ with real coefficients and run Hodge theory" briefs; substrate proposals that never engage the coefficient obstruction.
- **EXECUTABLE TEST.** Any cohomological-substrate brief must state its coefficient ring/structure and show the x-04 obstruction does not apply (or how it is dodged — e.g. condensed/analytic coefficients, characteristic-one, etc.), in writing, before design.
- **SOURCE.** grossmann-sweep.json (deninger-weil-etale scout; sweep verdict); corpus x-04.
- **STATUS.** literature-verified (on disk). **BINDS: Track-C cohomological substrates.**

### III.15 The Fisher-zero wall (statistical mechanics acts in the wrong variable)

- **STATEMENT.** Every proven positivity in statistical mechanics/QFT (ferromagnetic/GKS, Lee–Yang, KMS/OS reflection positivity) acts in the FIELD/fugacity/state variable, while zeta's zeros are TEMPERATURE-plane (Fisher) zeros — for which no Lee–Yang-type theorem exists. Knauf's Ramanujan-graph reduction is relocated RH-strength input with no generator (spin-chain certificates reach only Re s > 3/2 — corpus p2-15/p2-16/p3-30a).
- **KILLS.** "Zeta as partition function + reflection/Lee–Yang positivity ⇒ RH" briefs, unless the brief exhibits a temperature-variable positivity theorem (none exists) or a change of variables moving zeros into the field plane WITH the positivity intact (the dark-horse exception on file: the ferromagnetic realization of the dBN kernel via Newman's class-L closure — the lee-yang feasibility brief — which is precisely an attempt to satisfy this test, not evade it).
- **EXECUTABLE TEST.** Name the variable in which the brief's positivity theorem acts vs the variable in which zeta's zeros live. Mismatch without a proven bridge = returned.
- **SOURCE.** grossmann-sweep.json (reflection-positivity-qft dead-end 0.70; lee-yang-stat-mech instrument 0.72); corpus p1-03b, p2-17, r-05a/r-06a/r-23a.
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.16 Lorentzian/log-concavity arithmetic-blindness

- **STATEMENT.** Hyperbolicity/log-concavity technology is arithmetic-blind at the axiom level: its results hold for RH-false extended-Selberg members and for Poisson random functions (sweep scout: Chasse T² information dispersal; Farmer's X₁₀ counterexample); arXiv contains literally zero papers coupling Lorentzian polynomials to RH (totalResults = 0 at sweep time). Adjacent certified negative: the dBN kernel is certified NOT PF₅ (Michalowski, corpus t-60b — interval-arithmetic 5×5 Toeplitz minor).
- **KILLS.** Jensen–Pólya/Turán-inequality escalation briefs ("prove hyperbolicity of all Jensen polynomials ⇒ RH" as a *mechanism* claim); Lorentzian-polynomial dressings without a multiplicative bridge. Resurrection bar (recorded by the scout): a multiplicative-Lorentzian bridge with prime-side coefficients — no candidate exists.
- **EXECUTABLE TEST.** Does the brief's hyperbolicity input hold for an RH-false extended-Selberg member / Poisson random function? (It will.) Then the input is S1-empty; returned unless the bridge is exhibited.
- **SOURCE.** grossmann-sweep.json (lorentzian-log-concavity dead-end 0.82); corpus z-08–z-14, t-60b cluster.
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.17 p-adic transversality (interpolation-locus pinning)

- **STATEMENT.** The p-adic and archimedean topologies on the s-line are transverse away from the interpolation integers: every existing transfer mechanism (trivial-zero L-invariants, p-converse theorems) is pinned to the interpolation locus and cannot reach generic 1/2 + it. Kedlaya's p-adic Weil II runs on Frobenius weight theory with no archimedean analog. Wave-2 confirmation: the entire prismatic/F-gauge school has NO archimedean component (zero hits for zeta/archimedean/Deninger in Bhatt's notes; Gurney's generic fiber Frobenius-free).
- **KILLS.** Iwasawa-theoretic/p-adic-L routes to archimedean zero location; "prismatic cohomology will supply the substrate" briefs without an archimedean construction.
- **EXECUTABLE TEST.** Mark on the s-line the set of points the brief's p-adic mechanism actually constrains; if it is the interpolation locus (± trivial-zero points), the route cannot see 1/2 + it. Watch-item exception (not an engine): the prismatic Stage-1 question — do the {φ_p} extend over the generic point.
- **SOURCE.** grossmann-sweep.json (p-adic-iwasawa dead-end 0.80); grossmann-sweep2.json (prismatic-f-gauges scout).
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.18 o-minimal anti-tameness

- **STATEMENT.** Zeta on the strip is provably anti-tame: an infinite discrete zero set kills o-minimal definability, and Voronin universality (exact statement on disk, corpus p3-29c) kills bounded-complexity definable families; the branch contains no positivity notion of any kind.
- **KILLS.** Model-theory/tameness/point-counting (Pila–Wilkie-style) routes to RH.
- **EXECUTABLE TEST.** If the brief requires ζ (or its zero set) to be definable in a tame structure: returned, with the anti-tameness theorem (the sweep's branch-closing deliverable) as the certificate.
- **SOURCE.** grossmann-sweep.json (model-theory-ominimality dead-end 0.85); corpus p3-29c.
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.19 Arithmetic-QUE closure (dynamical equivalences without a handle)

- **STATEMENT.** Every RH-equivalence the QUE/microlocal corner owns (Zagier horocycle rate, Lax–Phillips causality) is the explicit formula in dynamical clothing with no independent handle; the unconditional exponent has been stuck at the spectral 1/2 for 45+ years and is proven optimal for rough observables; the spectral corner IS Bombieri–Garrett (III.3); equidistribution provably encodes only near-1-line zero data (Pan–Young, per scout).
- **KILLS.** Horocycle/equidistribution-rate and causality-criterion routes presented as new mechanisms.
- **EXECUTABLE TEST.** Ask what the dynamical statement adds beyond a reparametrized EF; check the observable class against the rough-observable optimality; run III.3 on any spectral variant. Dead-end certificate quotes on disk (corpus p3-24, p3-26a/b, p3-27 [Cyrillic], p3-28a/b).
- **SOURCE.** grossmann-sweep.json (arithmetic-que-microlocal dead-end 0.72).
- **STATUS.** sweep-certified. **BINDS: full-RH.**

### III.20 The S6 doubled-object rule (comparative anatomy of every TRUE RH)

- **STATEMENT.** In every fully-proven RH case, BOTH hold: **(A)** a finite-rank/trace-class determinantal realization overdetermined by an infinite counting tower (Frobenius tower rationality), AND **(B)** an external positivity generator applied to a SQUARED/DOUBLED object (Hodge index/Castelnuovo on C×C; even-tensor-power coefficient positivity) whose output is a CLOSED condition pinning eigenvalues exactly. Each alone is refuted within the anatomy: Selberg has (B)-shape without (A)'s tower → real off-line exceptions persist; generic Ihara has (A) without (B)'s arithmetic input → RH false (I.4). The generator NEVER acts on the zeta's own explicit formula — Weil positivity over Z is the diagonal shadow of the missing Hodge-index inequality: assuming it is assuming the conclusion. Deligne's squeeze additionally needs RATIONALITY (finitely many eigenvalues of fixed weight) — the exact coordinate with no archimedean analog, where the transfer dies. Wave-2 independent corroborations: BDPW (function-field all-moments from purity alone), BZSV (finite fixed-point calculus on doubled objects, function fields only, Rmk 1.1.6/1.1.3), Yuan–Zhang (proven char-0 positivity, substrate-blind — III.21).
- **KILLS.** De-novo designs missing either (A) or (B); positivity claims acting directly on the explicit formula (= diagonal-shadow circularity); "self-adjointness + trace formula suffices" (that is (B)-shape without (A), the Selberg failure mode).
- **EXECUTABLE TEST.** S6 conformance audit for every Track-C brief: exhibit the doubled object, the external generator, the closed output condition, and the tower/rationality structure — four named items. A brief with the generator acting on the un-doubled EF is returned as Weil-positivity-in-disguise (IV.1).
- **SOURCE.** grossmann-sweep.json (selberg-ihara scout, "THE SPEC-COMPLETION (proposed S6)"; sweep verdict — the S6 amendment is binding spec); grossmann-sweep2.json closure (three corroborations).
- **STATUS.** sweep-certified. **BINDS: Track-C/de-novo designs (spec-level).**

### III.21 Substrate-blindness of positivity calculi (the Yuan–Zhang dress test)

- **STATEMENT.** A positivity calculus whose axioms consume only the product formula is substrate-blind: Yuan–Zhang arithmetic Hodge index/bigness (Annals Studies 223, 2026) is the best-developed PROVEN, RH-independent char-0 positivity calculus (demonstrably not Weil positivity in disguise) — yet Chen–Moriwaki adelic curves show its axioms are satisfiable by DH-dressed data (S1 fails at the axiom level). The positivity ENGINE being real does not make the SUBSTRATE arithmetic. Provable-today companion lemma (shortlist-#1 first deliverable): DH/Epstein admit no polarized Frobenius system (Ψ_p∘Ψ_q = Ψ_pq forces the Λ(n) ≥ 0 Euler structure DH lacks).
- **KILLS.** "We found a proven positivity theorem, RH follows once we apply it" briefs that never check whether the theorem's axioms can be instantiated by RH-false data.
- **EXECUTABLE TEST.** Dress the brief's substrate axioms with DH data (adelic-curve style): if they instantiate, the calculus needs an S1 anchor axiom ADDED (e.g. the polarized-Frobenius lemma) — demand it in the brief.
- **SOURCE.** grossmann-sweep2.json (arithmetic-dynamics-equidistribution scout, instrument 0.82); Chen–Moriwaki in fetched-r3.
- **STATUS.** sweep-certified. **BINDS: Track-C substrates; generalizes I.1 to axiom systems.**

---

## GROUP IV — PROGRAM-DISCOVERED BARRIERS (adjudication-certified; each extracted from a kill)

### IV.1 The "Weil positivity in disguise" containment audit

- **STATEMENT.** Campaign post-mortem (95-page transcript): "every attempted route's first substantive step turned out to be Weil positivity or an equivalent in disguise" — and the Grossmann sweep confirmed this HELD across all 35 branches. The C1 adjudication converted it into a proof technique: C1's entire (a,w)-family of prime-computable tilted-EF observables was identified with classical Weil tests (1/2)ŵ(u)e^{−(a−1/2)|u|} on the same band via bounded-below multipliers — the family spans exactly bandwidth-log X Weil-EF data; multi-a constraints follow from single-band data by analytic continuation (information-free). "No new data coordinate."
- **KILLS.** Any route whose prime-facing data class is a reparametrized/reweighted/tilted restriction of the Weil-EF data at some bandwidth while claiming a new generator or new data (S4-trap). Casualties: C1 fatal 2 (verified); B1's W(b*f, b*g) (a reweighted restriction of the same cone); most of the campaign's ~30.
- **EXECUTABLE TEST.** Write the proposal's prime-computable observables explicitly; attempt to express each as (classical Weil test at bandwidth log X) × (multiplier bounded above and below on the band). Success of the expression = the route has no new data coordinate; its "generator" must then be audited as a cone-restriction (and small-support positivity is unconditional — III.2). Also check for the analytic-continuation leak: families parametrized by an auxiliary variable (tilt level, weight, flow time) whose members are mutually determined by continuation carry ONE band of information, not many.
- **SOURCE.** literature.md campaign residue; adjudication-C1.json (fatal 2, multiplier argument "airtight", independently verified); grossmann-sweep.json sweep_verdict.
- **STATUS.** program-adjudicated (computationally verified in C1). **BINDS: all routes.**

### IV.2 The tilted-EF cosh ghost (level-shifted explicit formulas are false below zero depth)

- **STATEMENT.** A "tilted" explicit formula at level a is FALSE as an identity once a lies below any in-window zero depth β₀: the correction is a ghost term 2m_ρ∫₀^{log X} ŵ(u)cosh((β₀−a)u)cos(γ₀u + phase)du with oscillatory envelope ~X^{β₀−a} — exponentially large in the cutoff, NOT an O(1) sign-definite constant (the C1 referee's contrary repair was verified WRONG). Ghost-free validity at level a is EQUIVALENT to quasi-RH(a) in the window; detecting the ghost needs X ~ T^c — the canon's visibility wall reinstated exactly.
- **KILLS.** LP/box certificates built on level-tilted EF identities assumed ghost-free (C1's M3); any depth-parametrized EF family whose identities silently assume the conclusion at that depth.
- **EXECUTABLE TEST.** For every EF-variant identity in a brief: test it numerically in a planted-zero world (I.2c factory: put a zero at β₀ > a inside the window) and measure the discrepancy against the X^{β₀−a} envelope. An identity that only holds zero-free is a hypothesis, not a tool — the brief must carry the ghost term explicitly or gate the identity behind quasi-RH(a).
- **SOURCE.** adjudication-C1.json (fatal 1, independently verified incl. the referee's error); mandatory repair 1 (the correct ghost formula, to be propagated verbatim).
- **STATUS.** program-adjudicated (computationally verified). **BINDS: all routes using EF variants.**

### IV.3 The sieve-envelope barrier (mean-zero kernels; averaged-HL smuggling)

- **STATEMENT.** A termwise absolute-value sieve sandwich 0 ≤ C_X(h) ≤ C_s·S(h)·X applied to a MEAN-ZERO resonant kernel has an X-sized envelope: a nonnegative mean-zero kernel would be identically zero, so the positive-part mass is bounded below (~half the absolute mass), and the sieve-consistent adversary saturates it — the envelope evaluates to ~C_s·X = C_s·T^{1+η}, not any "second-order in η" size. Converting a per-h sieve cap into a per-α cap silently requires the inter-h SIGNED cancellation (C(h) tracking S(h)X) — i.e. averaged Hardy–Littlewood at window H ~ T^η, below the Mikawa X^{1/3} threshold. Companion trap: the "deceptive dip" — A1's toy numerics (T ≤ 10⁶) lived where the divergent term is 1–6% of main (env/main = 0.057 at T = 4000, minimum ~0.004 near 10¹², divergent thereafter), so the designed kill-switch could not fire.
- **KILLS.** Briefs claiming unconditional control of signed prime-pair kernels from sieve upper bounds ("the price is second-order"); refutation channels calibrated inside the dip. Casualty: A1 (refuted 2, killer fatal upheld; the claimed achievable point 14.6 also failed its own corrected gate C_eff ≤ 13.33).
- **EXECUTABLE TEST.** For every sieve-bounded error term: (a) check whether the bounded kernel is mean-zero (then the envelope is its ABSOLUTE mass — compute it); (b) ask whether the claimed bound, if provable, would constitute averaged-HL/PCC-α>1 at some window (then it is M5 smuggled into M1 — reprice as conditional); (c) extend any calibration numerics past the dip (compute where the divergent term overtakes, and test there).
- **SOURCE.** adjudication-A1.json (fatal + secondary findings, adjudicator re-derived scaling and reproduced the dip numerically).
- **STATUS.** program-adjudicated (computationally verified). **BINDS: all routes.**

### IV.4 The mollifier-weight no-gain barrier (weighted Gram certificates)

- **STATEMENT.** For μ-mollifier weights in Weil-Gram certificates the fourth-moment ratio diverges like (θ·log T)² (sign-coherence/4^ω(n) mechanism — found independently by killer and referee), so the certificate tends to −1: vacuous. The honest repair (bounded-variance weights) gains only O(θ²), strictly dominated by window-widening's O(θ) throughout the regime; and past total polynomial length T the binding off-diagonal is Λ×Λ on BOTH long variables — genuine HL/PCC-α>1 prime-pair correlations, NOT the divisor-type shifted convolutions that Deshouillers–Iwaniec/BCHB/BCR technology evaluates (coefficient-type mismatch).
- **KILLS.** "Multiplicativity-sensitive reweighting of the Weil cone beats the constants" briefs. Casualty: B1 (refuted 2). Open question it leaves (B1 repair 6): a Weil-form analog whose atoms carry ζ′(ρ)-type mass (CGG-style damping) rather than reweighted flat mass — any successor must target that, not reweighting.
- **EXECUTABLE TEST.** For any weighted-certificate brief: (a) compute the fourth-moment ratio of the proposed weight class (the (log M)² divergence check is a short computation); (b) compare the claimed weight gain O(θ^k) against the window-widening gain at matched support; (c) classify the coefficients on every off-diagonal variable past length T — Λ-type means HL input, declare it conjectural and LP-price it (B1 repair 2).
- **SOURCE.** adjudication-B1.json (findings 1, 3 upheld; overruled finding 2 documents the O(θ²) resonator subtlety — quote it, don't rediscover it).
- **STATUS.** program-adjudicated. **BINDS: certificate-class.**

### IV.5 The cross-window product law (no mixed-window corner)

- **STATEMENT.** In tr(G_aG_bG_c) each shared grid index pairs adjacent DIFFERENT windows: cross-window kernels are Fourier transforms of window PRODUCTS with supports min(λ_i, λ_j) — verified numerically to ~1e-11 relative with two independent parameter sets (the proposal's per-window kernel was off by 57% and a factor ~350 respectively; FFT energy outside the min-band: 1.3e-26). Total accessible support under a₊b₊c ≤ 1.98 is maximized ONLY at equal windows (0.66, 0.66, 0.66) — the parent paper's own kλ < 2 boundary. The mixed-window corner does not exist.
- **KILLS.** Any brief claiming access to per-window simplex support {|ξ_w| ≤ λ_w} in multi-window trace expressions; "one factor at pair-bandwidth ~1" escape stories. Casualty: A2 fatal 1.
- **EXECUTABLE TEST.** For every multi-window trace in a brief: derive the cross-kernel as a product transform and compute its support (the adjudicator's numeric check is reproducible in minutes); reject any support accounting exceeding min-window pairing. A4 is certified free of this re-import (adjudication-A4 a2_reimport_check) — use that check's method as the template.
- **SOURCE.** adjudication-A2.json (fatal 1, verification block).
- **STATUS.** program-adjudicated (computationally verified). **BINDS: certificate-class.**

### IV.6 No unconditional per-block cubic inequality (rank_trace_cubic is false)

- **STATEMENT.** The proposed cubic analog of Lemma R is FALSE within its stated hypothesis class: hyperbolic difference-of-rank-one blocks B_i = μ(e_ie_i† − ww†) (eigenvalues {+μ, −μ}, n₊ = 1, tr = 0 exactly) with admissible ψ(m) = −m³ violate the inequality by ~μ³ against a remainder budget that is quadratic with ZERO trace-asymmetry currency (violation 1.17e5 at μ = 10, 1.197e8 at μ = 100 — exact construction, verified by direct eigenvalue/trace computation). Negative-eigenvalue escape is not covered by "mass escaping to large eigenvalues hurts the adversary."
- **KILLS.** Any revived cubic/odd-degree certificate stated as an unconditional per-block inequality. The ONLY visible routes around the odd-degree sign problem: (a) a λ_max(Q)-type hypothesis (= the Lindelöf lock, to be proven not assumed); (b) vector-geometry (u–w coupling) hypotheses WITH a proof they instantiate at zeta; (c) even-degree sign-definite currencies (tr(G_aG_bG_bG_a) = ‖G_bG_a‖²_F ≥ 0) LP-priced first. Casualty: A2 fatal 2; standing caution written into the A4 merge (cubic Lemma R must be engineered with the ladder and explicit o(N) budgets, "never as an unconditional per-block cubic inequality — that road is A2's fatal 2").
- **EXECUTABLE TEST.** Run the hyperbolic-block family at height μ → ∞ against any proposed odd-degree row: cubic gain ~μ³ vs the brief's stated quadratic costs. If the brief's budget does not price it, returned.
- **SOURCE.** adjudication-A2.json (fatal 2 + repairs 2); adjudication-A4.json (a2_reimport_check).
- **STATUS.** program-adjudicated (computationally verified, exact counterexample). **BINDS: certificate-class.**

### IV.7 The garnish-absorption barrier (divergent-cutoff scalar Schatten rows) — NEW, Session 5

- **STATEMENT.** A scalar Schatten-tail row with a DIVERGENT cutoff (Σ_{|λ|≥V₀}|λ|³ = o(N), V₀ → ∞, count bound stated only for V ≥ V₀) is **unconditionally absorbable**: a cluster garnish at height h₀ = V₀/2 gains the full doubles-vs-pairs cubic swing (4/3·N) at vanishing cost in every other row (trace +Δ/h₀², Frobenius +Δ/h₀, tail row 0, count row 0) — against such a row system the separation δ₀ = 0. **The complement (equally binding):** consuming the ALL-V count ladder n(V) ≤ C_led·N·V⁻⁴ for EVERY V ≥ C (absolute constant) plus the already-consumed o(N)-precision second-moment/pair equalities SQUEEZES the entire garnish/sprinkling adversary class to max absorbable cubic mass O(√(ε·C_led))·N = o(N) — divergent heights die on the ladder cap C_led/h, bounded heights on the Frobenius/pair cost Δ/h (LP-verified across C_led ∈ {1, 60, 1000}; analytic optimum 2√(εC_led) at h* = √(C_led/ε)); ANY O(1) ladder constant defeats the adversary — sharp constants are not required. Riders (same adjudication, all computed): θ ≥ 1 is certificate-vacuous (ladder constant (loglog T)², sprinkling m = loglog T neutralizes the cubic row at vanishing cost — operating points must be θ < 1 STRICT); the third trace's support is (k−1)λ′ = 1 + o(1), not 3λ′; the genuinely cubic prime resonance is the absolute constant Σ_p (log p)³/(p−1)² = 2.3158 contributing o(N) — near-critical cubic traces are a NONLINEAR READING OF PAIR DATA, not new correlation information.
- **KILLS.** Any brief consuming a spectral-tail row with a divergent cutoff and no all-V ladder (the row is vacuous — provable today as a PairCeiling-library no-go: "scalar divergent-cutoff cubic rows are unconditionally absorbed"); any θ ≥ 1 operating point for ladder-based rows; any "cubic trace = triple-correlation input" framing.
- **EXECUTABLE TEST.** For every spectral-tail/capacity row in a brief: (a) is the count/ladder bound stated for ALL V ≥ C or only above a divergent V₀? If the latter — run the garnish at h₀ = V₀/2 (five-line audit) and return the brief; (b) if all-V — check the squeeze arithmetic O(√(εC_led)) covers the brief's claimed swing; (c) recompute the row's actual Fourier support by the (k−1)λ rule; (d) any adversary analysis must include position/interference freedom, not only spectral escape (the squeeze's own stated limitation).
- **SOURCE.** adjudication-A4.json (killer-1 fatal layer 1 VERIFIED / layer 2 OVERRULED; computations d, e, f, i, j; repairs R1, R4, R6).
- **STATUS.** program-adjudicated (12 computations, LP-verified). **BINDS: certificate-class (any Schatten/tail/capacity row anywhere).**

### IV.8 Campaign residue: integrality pricing FALSE; Pontryagin counting empty

- **STATEMENT.** Two structural negatives from the Zeta23 campaign, held ever since: (a) per-pair quadratic "integrality pricing" is FALSE (G1–G4 experiments) — the (m−1)(m−2) spectral level is destroyed by interactions even under RH+GUE; only the mass-linear rank-trace inequality survives; (b) the negative-index (Pontryagin) route to COUNTING off-line zeros is structurally empty — visibility needs dim V ≳ N(T) (the counting functional cannot be localized). Related C1-adjudication datum: κ_a finiteness is OPEN for every a ∈ (1/2, 1), DH has κ = ∞ in σ > 1, and B3-vs-C1 CONTRADICT at a = 1/2 (carry-forward flag ii) — no Pontryagin-index layer currently has a nontrivial instance.
- **KILLS.** Briefs pricing multiplicity/integrality per-pair at quadratic level; off-line-zero COUNTING claims via negative squares/indices without dim V ~ N(T) resources; any κ_a-dependent milestone not gated behind κ_a < ∞ as an open hypothesis.
- **EXECUTABLE TEST.** (a) Any per-pair quadratic pricing claim: run the campaign's interaction configurations (transcript G1–G4; residue described in literature.md) — the level collapses; (b) any index-counting claim: compute the dimension the detector needs against N(T); (c) any κ_a use: exhibit the finiteness proof or the explicit gate.
- **SOURCE.** literature.md campaign residue; adjudication-C1.json (major 3); STATUS carry-forward flag (ii).
- **STATUS.** literature-verified (transcript) + program-adjudicated (κ_a). **BINDS: all routes.**

### IV.9 Visibility pricing (the cross-cutting detection-threshold barrier — program-synthesized)

- **STATEMENT.** Synthesized from four independent kills, one pattern: every mechanism has a computable threshold (support, height, cutoff, truncation) below which a single off-line zero — or the mechanism's own failure — is INVISIBLE, and every dead brief's evidence lived below its threshold. Exhibits: CCM/DH — off-line zero at t = 85.7 needs spectral resolution μ ≳ 120 vs probed μ ≤ 14.44 (CCM's own ≤ 17); C1 — ghost detection needs X ~ T^c; A1 — the deceptive dip (env/main minimum ~0.004 near 10¹², toy numerics at T ≤ 10⁶); parent method — resolution 1/L governs when off-line zeros are spectrally visible at all (annihilation threshold ε ≳ 0.2·2π/L).
- **KILLS.** Numerical "evidence" gathered below the mechanism's own visibility threshold; kill-switches/decision gates calibrated in the invisible regime (they pass while the route is dead — A1's M0); S2 claims with unpriced thresholds.
- **EXECUTABLE TEST.** Every brief with a detection claim or a numerical gate must include a computed visibility threshold (what support/height/precision makes one off-line zero, or one failure mode, visible to THIS detector) and demonstrate its experiments/milestones operate above it. No threshold computation = returned.
- **SOURCE.** `results/decisive-tests/ccm-dh-filter.json` (interpretation, μ ≳ 120); adjudication-C1.json (fatal 1); adjudication-A1.json (finding 5); full-map.md (Part-I visibility analysis).
- **STATUS.** program-adjudicated components; the synthesis is a program rule (this file). **BINDS: all routes.**

---

## GROUP V — PROCESS BARRIERS (how briefs die for non-mathematical reasons)

### V.1 The brief-time rule (this suite's own application law)

- **STATEMENT.** A1, B1, C1 all died POST-design-cost to model checks executable at brief time; A2 died to a trace-index audit and one exact counterexample, both brief-time-executable. The suite exists to move those deaths before the spend.
- **TEST.** No design work is commissioned until the protocol (§0) is on file with, for every barrier hit, an explicit evasion argument. The critic's checklist output (barrier-by-barrier: pass / evaded-with-argument / HIT) is attached to the brief and versioned with it.
- **SOURCE.** completeness-critic.json rec 4 (via STATUS Phase 4); adjudications A1/B1/C1/A2.
- **STATUS.** program rule (binding, this file). **BINDS: all briefs.**

### V.2 The prior-art gate (novelty is checked online, not recalled)

- **STATEMENT.** Standing order 1. Program casualties of skipped/late prior art: A2's novelty claim 5 punctured by Lagarias–Rodgers (corpus w-09, "on the title alone"); the 0.6725→0.6818 "gap" pre-shrunk by Chirre–Gonçalves–de Laat 0.6792 (w-08); B3's 70.37% record competitors (w-10/w-11). Novelty checks are not optional and not from memory; paywalled/unreachable sources are reported to the sponsor, never skipped silently.
- **TEST.** Every brief carries a prior-art section with tier-1 pins checked THIS session (arXiv/zbMATH/corpus); the routing index (`results/corpus-routing.md`) is consulted for on-disk pre-emptions; MathSciNet is permanently closed — use zbMATH (routing caveat 13).
- **SOURCE.** STATUS standing order 1; corpus-routing.md; STATUS carry-forward flag (i).
- **STATUS.** sponsor standing order. **BINDS: all briefs.**

### V.3 Verification standards (recall is not evidence; single verdicts have variance)

- **STATEMENT.** Standing order 5: no decisive action on unverified recalled claims — load-bearing mathematics is re-derived or computed, contested claims adjudicated by computation (this caught A2's F1/F2 "decisively and cheaply, ~5 min of numerics"). Session-4 process learning: single-run critic verdicts have real variance — run-2's fresh killer flipped A2 from swr-consensus to refuted; run-1's referee had computed the SHADOW of the error (0.74) inside the false formula without recognizing it. Consequently: (a) killer verdicts on load-bearing directions are DUPLICATED (two independent killers); (b) a "survives" verdict is only as good as the deepest identity actually re-derived — critics re-derive the central identity, never audit around it; (c) adjudicators verify computationally.
- **TEST.** Brief-time barrier evasion arguments are held to the same standard: an evasion resting on a recalled theorem is flagged and verified before the brief proceeds; every numeric barrier check in this file cites its reproducible computation path.
- **SOURCE.** STATUS standing order 5 + findings log 2026-08-13; adjudication-A2.json (adjudication_type).
- **STATUS.** sponsor standing order + program protocol. **BINDS: all briefs and all critics.**

---

## Cross-reference: program casualties → barriers that killed them

| Casualty | Verdict | Killing barriers |
|---|---|---|
| A1 break-bandwidth | REFUTED (2) | IV.3 (sieve envelope / HL smuggling), IV.9 (numerics dip) |
| B1 mult-positivity | REFUTED (2) | IV.4 (mollifier no-gain, Λ×Λ mismatch), IV.1 (reweighted cone) |
| C1 requirements-first-field | REFUTED (2.5) | IV.2 (cosh ghost), IV.1 (containment), I.2 (DMV), IV.8 (κ_a) |
| A2 richer-functionals | REFUTED (3) | IV.5 (window products), IV.6 (per-block cubic) |
| A4 lindelof-lock (as drafted) | SWR (5.5) — repaired | IV.7 (garnish; forced R1/R4/R5), I.3 (AH bullet struck, R6) |
| CCM/ncg shortlist #3 | reclassified INSTRUMENT | I.1 axiom-level (phenomena filter defeated), I.6 (conductor law) |
| tomita-takesaki-entropy | DEAD-END 0.72 | III.8 |
| lapidus-complex-dimensions | DEAD-END 0.85 | III.13, I.1 |
| reflection-positivity-qft | DEAD-END 0.70 | III.15 |
| lorentzian-log-concavity | DEAD-END 0.82 | III.16 |
| p-adic-iwasawa | DEAD-END 0.80 | III.17 |
| model-theory-ominimality | DEAD-END 0.85 | III.18 |
| arithmetic-que-microlocal | DEAD-END 0.72 | III.19, III.3 |
| campaign ~30 routes | refuted (transcript) | IV.1, I.1, IV.8 |

## Formalization queue (barriers worth turning into Lean/paper certificates, per the sweep)

1. Pretentious D-continuity/Halász-floor no-go (III.9) — cheapest; "already a book exercise."
2. ANTEDB DH-blindness two-part theorem (III.10) — finite audit + LP-closure supremum; expdb-executable.
3. Sawin–Whitehead/DGG MDS agnosticism calibration (III.11).
4. BZSV discrete-point ceiling (III.12).
5. "Scalar divergent-cutoff cubic rows are unconditionally absorbed" (IV.7) — provable today; extends the PairCeiling library; publish with its positive complement (the all-V-ladder squeeze).
6. DH/Epstein "no polarized Frobenius system" lemma (III.21 rider) — shortlist #1's first deliverable.
7. Monoid-form DH-exclusion via Blomer–Leung (I.1 rider) — the S1 axiom in its sharpest formal home.

*(File discipline: this suite is versioned with the program. Add a new entry the session any barrier is discovered — an adjudicated kill without a zoo entry is an unfinished adjudication. Do not delete entries; supersede them with a dated note, as STATUS does.)*
