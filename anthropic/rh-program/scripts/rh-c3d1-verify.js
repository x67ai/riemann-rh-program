export const meta = {
  name: 'rh-c3d1-verify',
  description: 'Phase-4 adversarial cycles for the two Phase-5 commissions: C3 geometric-substrate and D1 certified-refutation-arm (duplicated killers + referee each)',
  phases: [
    { title: 'Verify C3', detail: 'two independent killers + referee on directions/C3-geometric-substrate.md' },
    { title: 'Verify D1', detail: 'two independent killers + referee on directions/D1-certified-refutation-arm.md' },
  ],
}

const PROG = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/anthropic/rh-program'
const LEAN = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'

const VERDICT = {
  type: 'object', additionalProperties: false,
  required: ['proposal', 'lens', 'verdict', 'score', 'findings', 'repairs', 'literature_flags'],
  properties: {
    proposal: { type: 'string' },
    lens: { type: 'string', enum: ['killer', 'referee'] },
    verdict: { type: 'string', enum: ['survives', 'survives-with-repairs', 'refuted'] },
    score: { type: 'number', description: '0-10 overall promise AFTER accounting for findings: soundness x novelty x tractability x payoff' },
    findings: {
      type: 'array',
      items: { type: 'object', additionalProperties: false, required: ['severity', 'claim', 'argument'], properties: {
        severity: { type: 'string', enum: ['fatal', 'major', 'minor'] },
        claim: { type: 'string' },
        argument: { type: 'string', description: 'the full technical argument, checkable by a referee' },
      } },
    },
    repairs: { type: 'string', description: 'how to salvage/strengthen the commission given the findings; empty if none needed or none possible' },
    literature_flags: { type: 'array', items: { type: 'string' }, description: 'recalled results the brief relies on that need verification, citations it gets wrong, or prior art it missed' },
  },
}

const CTX = `You are a Phase-4 critic in a structured RH research program built on the 2026 "two-thirds" theorem and its Lean formalization (${LEAN}). The object under review is a PHASE-5 COMMISSIONING BRIEF (a full direction file on disk), not a designer StructuredOutput: it was written by a synthesis agent from verified program sources, it cites its evidence discipline inline, and it has had NO adversarial pass yet. Your verdict decides whether it may rank above "commissioned" grade and receive design effort.

MANDATORY BACKGROUND (read in this order):
1. The direction file under review (path in your role section below) — read it IN FULL, every section.
2. ${PROG}/BARRIER-ZOO.md — the program's executable falsification suite (45 barriers, 5 groups). Section 0 is the ordered brief-time protocol; you are its Phase-4 enforcement. Run the protocol against the brief.
3. ${PROG}/results/map-hooks.txt — condensed limitations + hooks of the zeta-2/3 method.
4. ${PROG}/results/literature.md — Aug-2026 verified state of the art + no-gos.
5. ${PROG}/results/corpus-routing.md — header caveats before you cite any corpus file.
Optional deeper sources: ${PROG}/results/full-map.md; ${PROG}/results/grossmann-sweep.json and grossmann-sweep2.json (the sweep harvests the brief builds on); ${PROG}/results/decisive-tests/ (ccm-dh-filter.json, arxiv-2606-body-read.json); ${PROG}/results/adjudication-*.json (the program's five binding adjudications — precedents for what kills and what survives); ${PROG}/sources-extracted/ (paper pages full_p*.txt, v5_p*.txt, transcript tx_*.txt); the Lean tree under ${LEAN}; the local corpus folders ${PROG}/fetched/, fetched-r2/, fetched-r3/ (PDF corpus; corpus-routing.md maps ids to files).

BINDING PROGRAM RULES FOR CRITICS:
- Standing order 5 (no decisive action on fabrications): agents hallucinate; recalled citations and "known" theorems may be invented. Any load-bearing claim you ATTACK or DEFEND must be independently verified — by direct computation (you have Bash/python; mpmath/sympy available), by re-derivation, or against the tier-1 source (WebFetch/WebSearch; arXiv is free). If a needed source is paywalled/unreachable, SAY SO in literature_flags — never substitute memory.
- Standing order 1 (prior-art gate): novelty claims are checked ONLINE, not from memory.
- Re-derive, don't audit around: any "survives" verdict is only as good as the deepest identity you actually re-derived yourself (the A2 reversal is the precedent: run-1 critics audited around a false identity and passed it; a fresh killer re-derived it and killed the direction).
- The brief's own [RU] (recalled-unverified) tags are attack surface: an evasion or milestone resting on an [RU] claim is unsupported until verified. You may VERIFY an [RU] item yourself (that is a finding too — say what you verified and how).
- Scope honesty cuts both ways: judge the brief on what it CLAIMS (instrument / refutation channel / proof substrate), not on what it does not claim. A false kill is as costly as a missed one.
- OUTPUT BUDGET: your entire StructuredOutput must stay under 50,000 characters. Dense technical prose; findings carry full arguments, not vibes.`

const killC3 = `${CTX}

YOU ARE A KILLER (maximally skeptical) on **C3:geometric-substrate** — ${PROG}/directions/C3-geometric-substrate.md.

The brief commissions the de-novo construction of an "arithmetic square with a correspondence calculus" (Connes-Consani x Deninger joint via the Morishita bridge; Yuan-Zhang adelic Hodge index as positivity engine; a novel Tate-curve E_p x E_q assembly seed), with first deliverable Lemma B: DH/Epstein admit no polarized Frobenius system.

ATTACK SURFACE THE BRIEF ITSELF NAMES FOR YOU (its Verification-verdicts section) — hit all four, then go beyond:
(a) **Lemma B step 1 / risk R8**: can "degrees against the two fibers reproduce the counting data of D(s)" be formalized WITHOUT smuggling in the Euler product (which would make Lemma B a definition, not a theorem)? Try to construct the circularity explicitly: write the candidate definition and show it either presupposes multiplicative structure or fails to pin D(s).
(b) **The Z5 bilinearity gate on the E_p x E_q seed**: is a (p,q)-graded family of products structurally condemned to bilinear-in-primes data (= L2/bandwidth data in geometric dress)? Where do the archimedean and pole terms of the explicit formula live? Attempt to PASS or FAIL the gate yourself on paper — a killer who fails the gate before the program spends the week has earned a fatal.
(c) **M3 base-vs-fiber crossing**: every existing arithmetic Hodge index theorem has Spec Z as the BASE. Check whether the brief's M3 statement (Yuan-Zhang extended to proper adelic-curve bases in the Chen-Moriwaki sense) actually CROSSES the mismatch or merely relabels it. If you can show the extension is either (i) already known/trivial or (ii) secretly equivalent to constructing the substrate itself, that is a finding.
(d) **Every [RU] tag in the file** (R6 lists them): the function-field non-circularity fact (Mattuck-Tate/Grothendieck: Castelnuovo-Severi from RR + ampleness, no RH input), the Connes-1999 equivalence scope, the seed's novelty claim. Verify or refute what you can online/by re-derivation.
FURTHER WEAPONS: (e) Model-world battery at the AXIOM level: does DH or an Epstein h>1 form, or a Beurling/DMV world (BARRIER-ZOO I.2), instantiate the polarized-Frobenius axioms? (Λ_P >= 0 + full Euler product HOLD in Beurling worlds — does Lemma B's axiom set exclude them, and if not, is the S1 anchor weaker than claimed?) (f) Is any step Weil positivity in disguise (zoo IV.1) despite the Z2 guards? (g) Vacuity adversary Z6: is the axiom class provably empty even FOR zeta (i.e. does some verified no-go — Deninger 2204.02714, Serre's argument — already forbid a zeta instantiation of the axioms as stated)? If you can prove the axioms unsatisfiable for zeta, the whole commission collapses to a no-go note. (h) The DH witness arithmetic: re-verify Λ_DH(6) and Λ_DH(12) yourself from the DH coefficient definition (a_n = (1, κ, −κ, −1, 0) mod 5, κ = 0.2840790438…) — the builders in ${PROG}/results/ccm-dh-test/ exist but re-derive independently.
Verdict 'refuted' requires at least one fatal finding you can defend before an adjudicator who WILL re-compute your mathematics. Return via StructuredOutput with lens='killer', proposal='C3:geometric-substrate'.`

const killD1 = `${CTX}

YOU ARE A KILLER (maximally skeptical) on **D1:certified-refutation-arm** — ${PROG}/directions/D1-certified-refutation-arm.md.

The brief commissions Track D: certified refutation — machine-checked witness formats (W1 argument-principle box, W2 KKT partial sums, W3 Weil-form negativity, W4 Robin), a formal Λ-bracket, and a wanted-poster-guided certified search; first deliverable = Certified Refutation Interface v1 with a DH live-fire test.

ATTACK SURFACE THE BRIEF ITSELF NAMES FOR YOU (its Current-frontier section) — hit all four, then go beyond:
(a) **Re-derive the reduction "Λ > t₀ ⟺ H_{t₀} has a non-real zero"** from the definition of the de Bruijn-Newman constant (the brief flags this as the scout's own derivation, [RU]). Is it exactly right? (Mind the subtlety: Λ is defined via H_t all of whose zeros are real for t >= Λ; check both directions and edge cases — what exactly does Λ > t₀ give at t = t₀ itself?) A wrong reduction poisons M5 and the W1-on-H_t format.
(b) **Mathlib coverage check**: does Mathlib (2025-26 state) ship a usable rectangle argument principle / winding-number zero count for holomorphic functions? Check the actual Mathlib source/docs online (leanprover-community). The brief's v1 mitigation (ship the analytic step as a displayed hypothesis) — is that honest engineering or does it hollow out the deliverable (a checker whose soundness theorem assumes the mathematics it exists to certify)?
(c) **The KKT W2 row** (arXiv:2408.03938): the brief admits abstract-verification only. READ THE BODY (free on arXiv). Do Kerr-Klurman-Thorner's theorems actually yield a machine-checkable GRH-disproof witness format — exact thresholds, family scope, uniformity? Or is the implication conditional/asymptotic in a way that breaks the witness format?
(d) **Prior-art re-sweep** (standing order 1, online): rigorous verification height (is 3*10^12 Platt-Trudgian still the record in Aug 2026?), any Λ-bracket improvement beyond [0, 0.22], any competing certified/formalized zeta-zero verification (Lean/Coq/Isabelle — e.g. any formalization of zero-free regions or zero counts), any new counterexample-search program. Each hit reprioritizes or kills a milestone.
FURTHER WEAPONS: (e) W3 soundness: is "certified W(f,f) < 0 for one explicit f ⟹ ¬RH" exactly Weil's criterion in the correct normalization and test class (check which side needs the FULL class vs one function; a one-function witness is only valid if positivity-for-all is equivalent to RH in the normalization used — verify against the literature/corpus). (f) W4: verify the Robin statement scope (n > 5040, σ(n) < e^γ n log log n ⟺ RH) including the equivalence direction the witness needs. (g) The honesty section's pricing: are the claimed RH-true payoffs real (e.g. does a formal Λ-bracket instance actually differ from Polymath15's published computation in any checkable way)? (h) Detector discipline: the conductor-Fuchs anomaly detector inherits the CCM experiment's calibration — check the brief does not smuggle verdict-grade weight into pointer-grade statistics anywhere. (i) The Dobner S1-emptiness claim (Acta Arith 201 / arXiv:2005.05142): verify the theorem statement online — does it really cover the class claimed ("extended Selberg class from FE alone")? (j) Compute policy realism: months-scale certified searches on ONE MacBook (KICKSTart local-only policy) — is any milestone's compute budget fantasy? Price M0 and M1 honestly.
Verdict 'refuted' requires at least one fatal finding you can defend before an adjudicator who WILL re-compute your mathematics. Return via StructuredOutput with lens='killer', proposal='D1:certified-refutation-arm'.`

const refC3 = `${CTX}

YOU ARE THE REFEREE (novelty + tractability + value) on **C3:geometric-substrate** — ${PROG}/directions/C3-geometric-substrate.md.

Evaluate:
(1) NOVELTY AUDIT (online, standing order 1): (i) the E_p x E_q Tate-curve assembly seed — has ANYONE proposed products of per-prime Tate curves / per-prime elliptic fibers as arithmetic-surface surrogates (search: Connes-Consani orbit, Haran, van der Geer-Schoof, Manin F1 lineage, Smirnov)? The brief's R7 demands exactly this search — run it. (ii) "Hodge index over adelic curves": has the Chen-Moriwaki school (2023-2026) already published partial results that would make M3 known? (iii) The polarized-Frobenius-system axiomatization and Lemma B — closest existing work?
(2) FIRST-DELIVERABLE QUALITY: is Lemma B genuinely referee-evaluable as specified (proof obligations 1-4)? Are steps 2-3 really "formal monoid algebra + one Yuan-Zhang input" or is hardness hidden? Is the Epstein witness (N1) correctly specified (class-number-2 form x^2+5y^2, D=-20; support off prime powers / negative Λ_Q)? Sanity-check the mathematical claim that Epstein zetas of h>1 lack Euler products and would violate the Λ_D >= 0 + prime-power-support conclusion.
(3) MILESTONE LADDER: is M0 -> M1 -> M2{a,b,c} -> M3 -> M4 ordered by real dependency? Where is the miracle? Is the kill-criterion (M2 fails on all three sub-routes while M0 stands -> documented no-go) actually executable, or will the direction zombie on forever? Compare against the 8-year CC stall base rate the brief itself concedes (R1).
(4) VALUE decomposition: price M0, M1, M2c, M3 as STANDALONE outputs (publishable? instrument-grade? usable by sibling directions?) under the modal outcome that M4 never happens. The brief claims every rung is independently publishable — audit that claim rung by rung.
(5) The brief's evidence discipline: spot-check 3-5 of its [V:...] tags against the named sources on disk (the two sweep JSONs, the decisive-test files) — does the cited source actually say what the brief says it says? (The program has been burned by paraphrase drift; the arxiv-2606 body-read exists because of exactly this.)
Estimate honestly whether a strong group lands M0+M1 in one session-scale effort as claimed. Return via StructuredOutput with lens='referee', proposal='C3:geometric-substrate'.`

const refD1 = `${CTX}

YOU ARE THE REFEREE (novelty + tractability + value) on **D1:certified-refutation-arm** — ${PROG}/directions/D1-certified-refutation-arm.md.

Evaluate:
(1) NOVELTY AUDIT (online, standing order 1): (i) certified/formal verification of zeta zero-counts or RH-partial results — what exists (Isabelle/HOL prime number theorem line, ARB certified zeta work, any Lean analytic number theory in progress)? Is the claimed gap ("no certified zeta-zero formalization, no counterexample-search program") real as of Aug 2026? (ii) The witness-format idea (DRAT-analog transcripts for analytic computations) — closest prior art? (iii) Is anyone already formalizing de Bruijn-Newman / Polymath15?
(2) FIRST-DELIVERABLE QUALITY: the Certified Refutation Interface v1 — audit its three components against the ACTUAL Lean repo (${LEAN}: comparator/, Zeta23/PairCeiling/NumericCert.lean, RowCert.lean, WeilEF/). Are the claimed reuse points real (do those files exist and do what the brief says)? Is the "~100 lines of trusted statements" estimate credible? Is the DH live-fire test well-posed (the checker is zeta-specific but the test runs on DH — is the claimed resolution of that tension coherent)?
(3) MILESTONE LADDER: M0 (detector calibration, weeks) -> M1 (interface, months) -> M2 (formal Λ-bracket) -> M3 (targeted search) -> M4/M5. Real dependencies? Which milestones survive contact with the local-compute-only policy? Where is the first step that is actually a research problem in disguise (the brief flags Bober-Hiary rigorization — anything else)?
(4) VALUE under RH-true (the honest frame the brief itself adopts): audit the honesty section's pricing item by item. Is the insurance-policy argument for witness formats sound program economics or sunk-cost dressing? Is the exclusion-ledger value real given verification already stands at 3*10^12?
(5) DIVISION OF LABOR: the B2-owns-theory / D1-owns-execution split — check ${PROG}/directions/B2-refutation-program.md (if present; else B2 content in results/design-proposals.json + verdicts) for actual overlap or orphaned dependencies (does B2 M6's depth->Λ bridge exist yet? what happens to M5 if it never lands?).
(6) Spot-check 3-5 [program-verified] anchors in the Numerics section against their sources (corpus-routing caveat 9 for the Λ bracket; Stopple; Platt-Trudgian).
Estimate honestly: could this program, on one MacBook plus Lean, land M0 and M1 within its horizon? Return via StructuredOutput with lens='referee', proposal='D1:certified-refutation-arm'.`

const dupNote = `

(NOTE: you are the SECOND of two independent killers run under the program's duplicate-killer protocol for load-bearing directions. You cannot see the other killer's output. Attack fresh — re-derive the central claims yourself rather than auditing around them. The A2 precedent: the second killer found a fatal derivation error the first had missed, and the direction fell.)`

const [c3k1, c3k2, c3r, d1k1, d1k2, d1r] = await parallel([
  () => agent(killC3, { label: 'kill:C3', phase: 'Verify C3', schema: VERDICT }),
  () => agent(killC3 + dupNote, { label: 'kill2:C3', phase: 'Verify C3', schema: VERDICT }),
  () => agent(refC3, { label: 'ref:C3', phase: 'Verify C3', schema: VERDICT }),
  () => agent(killD1, { label: 'kill:D1', phase: 'Verify D1', schema: VERDICT }),
  () => agent(killD1 + dupNote, { label: 'kill2:D1', phase: 'Verify D1', schema: VERDICT }),
  () => agent(refD1, { label: 'ref:D1', phase: 'Verify D1', schema: VERDICT }),
])

return { c3: { kill: c3k1, kill2: c3k2, ref: c3r }, d1: { kill: d1k1, kill2: d1k2, ref: d1r } }
