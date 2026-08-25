export const meta = {
  name: 'rh-a4-m2gate',
  description: 'A4 action one: the corrected M2 decision-gate LP (adjudication repair R5) — formulate, implement, adversarially audit',
  phases: [
    { title: 'Formulate', detail: 'precise LP spec per R5: clustered null, marks to W, depth-parametrized pairs, garnish fuzz row' },
    { title: 'Implement', detail: 'build + run the gate LP at N=64/128 with W-scaling and null-model Monte Carlo' },
    { title: 'Audit', detail: 'independent adversarial audit: try to break the gate result' },
  ],
}

const PROG = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/anthropic/rh-program'
const LEAN = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'
const OUT = `${PROG}/results/a4-m2-gate`

const COMMON = `You are working on the RH research program's direction A4 (the merged cubic-certificate direction, adjudicated survives-with-repairs 5.5). The task is A4's ACTION ONE: the corrected M2 decision-gate LP, exactly as mandated by binding adjudication repair R5. This gate decides whether the cubic-row mechanism gets any further investment: it must be run BEFORE the R2 bridge work, and EITHER branch is a deliverable (bite -> direction live; absorption -> a publishable sharpened no-go "the bandwidth-one ceiling is robust under Rudnick-Sarnak-range cubic augmentation with capacity control").

MANDATORY BACKGROUND (read in this order; do not skip):
1. ${PROG}/directions/A4-lindelof-lock.md — the ENTIRE file: mechanism Steps 1-5, Theorem 1, all three Phase-4 verdicts, the BINDING adjudication section with repairs R1-R7, and the merge-guidance section. R5 (the gate spec) and R7 (the fallback row system, now PRIMARY) are your contract.
2. ${PROG}/results/adjudication-A4.json — the 12 computations; especially the garnish/squeeze LP computation (killer-1 fatal overruled at mechanism level: bounded heights blocked by Frobenius/pair cost Delta/h, divergent heights by ladder cap C_led/h, max absorbable cubic = O(sqrt(eps*C_led)) N), the sprinkling adversary at theta >= 1 (m = loglogT, n = eps N/m^2, eps = 1/sqrt(loglogT)), and the c_3(lambda') decomposition (density term + F(alpha) band term + absolute constant 2.3158; total Fourier support (k-1)lambda' = 1 + o(1)).
3. ${PROG}/results/full-map.md — sections on Lemma R / rank_trace_mult_k / lemmaR_tight, Prop 4.1 block structure (pair eigenvalues generically ASYMMETRIC per tx_082: m*L^2*a*(1 +/- A)), and the ENTIRE lean:ceiling section (the PairCeiling LP formalization: form factor S, discrepancy D, certificate (c0, r), validity, the 256-law).
4. ${PROG}/sources-extracted/v5_p*.txt — v5 SS7.2 (the ceiling + SS7.2(e) RS-range cubic trace) and SS7.3 (the conditional cubic-weight certificate omega(m) = m/2 + (2m^2 - m^3)/18 + (4/9)1_{m=1}, tight at m = 1,2,3 by Schur-Horn; the sine moments m_k(1) = 1, 4/3, 2, 13/4 line in SS7.5(f)(g)).
5. ${PROG}/sources-extracted/tx_081.txt and tx_082.txt — the transcript's support arithmetic ((k-1)lambda for the k-th trace) and the Prop 4.1 pair-block spectrum.
6. ${LEAN}/Zeta23/PairCeiling/ — Defs.lean, Stability.lean, NearCUE.lean, LawN256.lean (the exact-rational LP architecture the gate extends).
BINDING PROGRAM RULES: standing order 5 — every load-bearing number re-derived or computed, never recalled; flag anything you could not verify. Thermal policy: at most 4 concurrent heavy local compute processes (this is a shared MacBook, M5 10-core; batch, don't shrink). Write ALL durable outputs to ${OUT}/ (create it), never to /tmp.

THE GATE, AS THE ADJUDICATION FIXED IT (R5 verbatim contract, expanded):
(1) NULL MODEL: a CLUSTERED sine-process null — at lambda' = 1/2+ the window width is TWO mean gaps, so average window occupancy 2; the null's budget moments m_2(lambda'), m_3(lambda') must include the O(1) cluster cross-term background from ordinary nearby simple zeros (referee major-2), Monte-Carlo-sampled from the sine process (CUE eigenangles are an acceptable sampler at n = 512-2048 with enough realizations; justify convergence), NOT from isolated-block idealizations.
(2) ADVERSARY CLASS: mark/cluster alphabet up to a slowly divergent W (run W-scaling, e.g. W in {3, 4, 6, 8}, and report the trend — the sprinkling adversary lives at m ~ loglogT, so W-stability is the whole question); depth-parametrized off-line pair family u in [0, 1/L'] with the TRUE Prop-4.1 block spectrum (asymmetric eigenvalues, block continuity: at u -> 0 the pair's spectrum tends to (+2, -0) and its cubic charge to +8, mimicking a double — the gate MUST include these shallow pairs); adversarial 3-point positional freedom subject only to point-process realizability (state precisely which realizability constraints you impose and why they are necessary AND sufficient for the LP's honesty — this is the hardest design decision; an unrealizable adversary kills the gate's meaning in one direction, an over-constrained one in the other).
(3) ROW SYSTEM (the R7 fallback system, PRIMARY): density row tr = N(1+o(1)); Frobenius row tr^2 = kappa(lambda')N with the split Sum_+ + Sum_-; the signed cubic row tr^3 = c_3(lambda')N with c_3's honest content (bandwidth-one pair data + absolute constant — R6); the all-V count ladder n(V) <= C_led N V^{-4} for ALL V >= C_abs with explicit constants (NOT a scalar tail row at divergent V0 — that is R1's vacuity); n_- <= p; power-mean; Hoelder row with o(N) correction; and the GARNISH-CAPACITY FUZZ ROW of order sqrt(eps*C_led) N derived from the repaired ladder (re-derive the adjudicator's squeeze computation to fix the constant).
(4) DECISION CRITERION: the gate BITES iff the LP (joint with the lambda = 1 counting side, i.e. the N_d-relevant rows of the parent certificate) certifies N_d >= 5/6 + delta_0 with delta_0 > 0 stable under W-scaling and null-model error bars — equivalently the N_d-extremal configuration (2/3 simple + 1/6 doubles) is cut off by the cubic row against ALL admissible adversaries. ABSORPTION means: an admissible adversary family (positions/depths/clusters) satisfies every row while keeping N_d = 5/6 + o(1). Report delta_0 (or the absorbing family) with error bars; a result within error bars of 0 is 'gate inconclusive at this scale' — say so rather than forcing a verdict.
PRIOR EXPECTATIONS TO TEST AGAINST (not to assume): the referee priced P(bite) <= 50%; the designer's own admission is that at lambda = 1 the sine budget exactly matches the extremal demand (2 = 2) and any gain must come from the window-optimized margin (2m_2 - m_3) surviving at reduced bandwidth; the adjudicator proved garnish-type (spectral-escape) absorption is CAPPED, so absorption, if it happens, must come from position/interference freedom (shallow pairs + cluster cross-terms). Verify the recalled sine moments m_2, m_3 by your own computation before using them.`

phase('Formulate')
const spec = await agent(`${COMMON}

YOUR ROLE: THE FORMULATOR. Produce the complete, precise mathematical specification of the gate LP — every object, row, constant, discretization, and the exact decision criterion — and the implementation plan. Derive, do not hand-wave: (a) re-derive the garnish-capacity constant sqrt(eps*C_led) from the adjudication's squeeze argument with your own eps/C_led bookkeeping; (b) re-derive kappa(lambda') and the c_3(lambda') decomposition at the operating point (theta < 1 strict) far enough to fix what the LP's budget column actually is at finite N; (c) fix the pair-family parametrization (depth grid in u, the asymmetric block spectrum per tx_082) and the cluster alphabet; (d) state the point-process realizability constraints you impose (with justification for necessity and sufficiency at the LP's level of abstraction); (e) fix N (start 64, confirm at 128 if cheap), W-grid, sampler, realization counts, error-bar methodology; (f) specify the lambda = 1 side rows you keep so N_d is actually pinned by the joint system (use the PairCeiling architecture as the template; say exactly what changes).
WRITE the full spec as ${OUT}/SPEC.md (create the directory; dense, referee-evaluable, with all derivations either inline or delegated to a short appendix). Then return via StructuredOutput a faithful SUMMARY of what you fixed (the implementer works from SPEC.md; the summary is for the program record).`,
  { label: 'formulate:m2gate', phase: 'Formulate', schema: {
    type: 'object', additionalProperties: false,
    required: ['spec_path', 'row_system', 'null_model', 'adversary_class', 'realizability', 'garnish_constant', 'decision_criterion', 'discretization', 'open_risks'],
    properties: {
      spec_path: { type: 'string' },
      row_system: { type: 'string', maxLength: 4000, description: 'the LP rows with constants as fixed' },
      null_model: { type: 'string', maxLength: 2500 },
      adversary_class: { type: 'string', maxLength: 2500 },
      realizability: { type: 'string', maxLength: 2500, description: 'exactly which point-process realizability constraints are imposed and why' },
      garnish_constant: { type: 'string', maxLength: 1500, description: 're-derived fuzz-row constant and bookkeeping' },
      decision_criterion: { type: 'string', maxLength: 1500 },
      discretization: { type: 'string', maxLength: 1500, description: 'N, W-grid, u-grid, sampler, realizations, error bars' },
      open_risks: { type: 'array', items: { type: 'string', maxLength: 800 } },
    } } })
if (!spec) return { error: 'formulator died', spec: null }
log('SPEC fixed: ' + spec.spec_path)

phase('Implement')
const impl = await agent(`${COMMON}

YOUR ROLE: THE IMPLEMENTER. The formulator's binding spec is at ${OUT}/SPEC.md — read it in full and implement it faithfully. Where the spec is silent or you must deviate, record the deviation and its reason in your output AND in a DEVIATIONS section of the run report. Build the code under ${OUT}/ (python3; numpy/scipy/mpmath available; keep any single heavy sweep to <= 4 concurrent processes). Steps: (1) null-model Monte Carlo (budget moments with error bars; convergence evidence); (2) adversary/configuration classes exactly per spec (marks to W, depth-u pairs with the true block spectra, cluster geometry freedom); (3) the LP assembly and solve (scipy linprog or exact-rational where the spec demands it; document solver tolerances); (4) W-scaling runs and the N=128 confirmation if the spec kept it; (5) write ${OUT}/RUN-REPORT.md (methods, numbers, error bars, plots optional) and ${OUT}/gate-result.json (machine-readable: delta_0 estimates per W, absorbing family if found, verdict field 'bite'|'absorb'|'inconclusive' with error bars). Sanity gates before you trust output: reproduce the known sine moments at bandwidth 1 (m_2 = 4/3, m_3 = 2 — verify by your own sampler; if your sampler disagrees, STOP and debug rather than proceeding); confirm the doubles-vs-tight-pair cubic charges (+8 vs 0) and the shallow-pair continuity (+8 limit) emerge from your block builder. Return a summary via StructuredOutput.`,
  { label: 'implement:m2gate', phase: 'Implement', schema: {
    type: 'object', additionalProperties: false,
    required: ['status', 'files', 'sanity_checks', 'headline', 'gate_result', 'deviations', 'caveats'],
    properties: {
      status: { type: 'string', enum: ['complete', 'partial', 'blocked'] },
      files: { type: 'array', items: { type: 'string' } },
      sanity_checks: { type: 'string', maxLength: 2000, description: 'sine moments reproduction, block-charge checks, solver validation' },
      headline: { type: 'string', maxLength: 2500, description: 'the numbers: budgets, demands, delta_0 per W, trends' },
      gate_result: { type: 'string', enum: ['bite', 'absorb', 'inconclusive'] },
      deviations: { type: 'array', items: { type: 'string', maxLength: 600 } },
      caveats: { type: 'array', items: { type: 'string', maxLength: 600 } },
    } } })
if (!impl) return { spec, error: 'implementer died', impl: null }
log(`Implementation ${impl.status}; preliminary gate: ${impl.gate_result}`)

phase('Audit')
const audit = await agent(`${COMMON}

YOUR ROLE: THE ADVERSARIAL AUDITOR (independent; you did not write the spec or the code). On disk: ${OUT}/SPEC.md, the implementation, ${OUT}/RUN-REPORT.md, ${OUT}/gate-result.json. Your job: try to BREAK the result before the program trusts it.
(1) SPEC-vs-R5 conformance: does SPEC.md actually implement all four R5 components (clustered null, marks to divergent W, depth-parametrized pairs with TRUE block spectra, garnish fuzz row, realizability-only positional freedom)? Any silent narrowing of the adversary class is exactly the failure mode R5 exists to prevent (a 'bite' from a narrowed adversary is an artifact — the marks-{1,2} precedent).
(2) CODE-vs-SPEC conformance: read the code; re-run at least the null-model moments and one full LP cell yourself (fresh seed); check solver tolerances and that error bars are honest.
(3) BREAK ATTEMPTS: construct absorption candidates the implementation may have excluded — shallow-pair ladders at multiple depths, mixed cluster geometries, boundary-of-realizability configurations, the sprinkling family adapted to finite N — and evaluate the row system on them directly (the code's builders should let you; else write your own). If any admissible configuration beats the reported delta_0, the gate result flips.
(4) STABILITY: is the verdict stable under W, N, seed, and null-model error bars? A delta_0 within 2 sigma of 0 is 'inconclusive', whatever gate-result.json says.
Write ${OUT}/AUDIT.md with your full findings. Return StructuredOutput: your independent verdict on the gate and on the deliverable's publishability (either branch: if 'absorb' holds up, is the no-go write-up supported? if 'bite', is delta_0 real?).`,
  { label: 'audit:m2gate', phase: 'Audit', schema: {
    type: 'object', additionalProperties: false,
    required: ['conformance_r5', 'conformance_code', 'break_attempts', 'gate_verdict_final', 'delta0_assessment', 'findings', 'recommendation'],
    properties: {
      conformance_r5: { type: 'string', maxLength: 2000 },
      conformance_code: { type: 'string', maxLength: 2000 },
      break_attempts: { type: 'string', maxLength: 3000, description: 'what you tried, what happened' },
      gate_verdict_final: { type: 'string', enum: ['bite', 'absorb', 'inconclusive', 'implementation-unsound'] },
      delta0_assessment: { type: 'string', maxLength: 1500 },
      findings: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['severity', 'claim'], properties: {
        severity: { type: 'string', enum: ['fatal', 'major', 'minor'] },
        claim: { type: 'string', maxLength: 1200 },
      } } },
      recommendation: { type: 'string', maxLength: 1500, description: 'next action for the A4 direction given the audited result' },
    } } })

return { spec, impl, audit }
