export const meta = {
  name: 'rh-a4-design-verify',
  description: 'Re-run the A4:lindelof-lock designer (lost at session pause), then its killer + referee critics',
  phases: [
    { title: 'Design', detail: 'A4:lindelof-lock designer (single agent)' },
    { title: 'Verify', detail: 'duplicated killers + referee on the A4 proposal (Session-4 protocol: load-bearing directions get two independent killers)' },
  ],
}

const PROG = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/rh-program'
const LEAN = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['title', 'thesis', 'mechanism', 'novelty', 'evades_obstructions', 'first_theorem', 'milestones', 'lean_hook', 'numerics', 'payoff', 'failure_modes', 'confidence'],
  properties: {
    title: { type: 'string', maxLength: 200 },
    thesis: { type: 'string', maxLength: 800, description: 'one-sentence claim of the approach' },
    mechanism: { type: 'string', maxLength: 18000, description: 'the mathematical mechanism in dense technical prose: objects, formulas, why it should work — state results, do not transcribe derivations' },
    novelty: { type: 'string', maxLength: 6000, description: 'exactly what is new relative to the literature; cite specific papers it goes beyond' },
    evades_obstructions: {
      type: 'array',
      items: { type: 'object', additionalProperties: false, required: ['obstruction', 'how'], properties: { obstruction: { type: 'string' }, how: { type: 'string' } } },
      description: 'for each relevant known no-go (DH/Epstein filter, AH, bandwidth-one ceiling, lemmaR_tight, dimension cap, kappa>=2/sqrt3, Bombieri small-support, Bombieri-Garrett 94%, parity, Conrey-Li, Lambda>=0), how the approach evades it or why it is out of scope',
    },
    first_theorem: { type: 'string', maxLength: 12000, description: 'the single well-posed first theorem to attempt: precise statement, current status of the needed inputs, sketch of attack' },
    milestones: { type: 'array', items: { type: 'string', maxLength: 1500 }, description: 'ordered ladder of 3-6 milestones from first theorem toward the horizon goal' },
    lean_hook: { type: 'string', maxLength: 4000, description: 'which Zeta23 components to reuse/extend, and what the first formalizable statement would be' },
    numerics: { type: 'string', maxLength: 5000, description: 'a concrete numerical experiment runnable now (Wolfram/Python scale) that would provide evidence for or against the mechanism' },
    payoff: { type: 'string', maxLength: 5000, description: 'what improves if each milestone lands: constants, statements, or refutation channels' },
    failure_modes: { type: 'array', items: { type: 'string', maxLength: 1500 } },
    confidence: { type: 'number', description: 'probability in [0,1] that first_theorem is provable within ~2 years by a strong group' },
  },
}

const COMMON = `You are a research mathematician designing a NOVEL attack direction related to the Riemann Hypothesis, as part of a structured research program that builds on the 2026 "two-thirds" theorem and its Lean formalization (repo: ${LEAN}).

MANDATORY BACKGROUND (read all three first):
1. ${PROG}/results/full-map.md — six-agent technical map of the paper + Lean repo (method, exact constants, formalized no-go theorems, extension hooks).
2. ${PROG}/results/literature.md — verified state of the art on 12 fronts as of Aug 2026, including all known obstruction/no-go results.
3. Raw sources available for grep/Read as needed: ${PROG}/sources-extracted/full_p*.txt (the 35-page paper, one file per page), ${PROG}/sources-extracted/condensed_p*.txt, ${PROG}/sources-extracted/tx_*.txt (the 95-page discovery-transcript volume, one file per page), and the Lean sources under ${LEAN}.
4. ${PROG}/sources-extracted/v5_p01.txt .. v5_p17.txt — v5 of the parent paper (2026-08-11; THE PRIMARY CITATION for the parent paper from now on; assessment: ${PROG}/results/paper-v5-assessment-2026-08-14.md). Load-bearing for this brief: SS7.2(e) states tr G-tilde^k is evaluable exactly in the Rudnick-Sarnak range X^k <= T^{2-eps} (the short-window frontier, now paper-official), and SS7.3 gives a CONDITIONAL cubic-weight certificate omega(m) = m/2 + (1/18)(2m^2 - m^3) + (4/9)*1_{m=1}, tight at m=1,2,3 (Schur-Horn), whose unconditional input is exactly what this direction must supply.

HARD DESIGN CONSTRAINTS (your proposal MUST address these explicitly in evades_obstructions):
- DH/Epstein filter: Davenport-Heilbronn and Epstein zeta (class number > 1) satisfy functional equation + explicit formula + L2 mean values yet violate RH. Any route claiming to reach FULL RH must consume an input these objects violate (Euler product at every prime / multiplicativity beyond L2-means / Ramanujan). A route that only improves proportions need not pass this filter but must say so honestly.
- Alternative Hypothesis: bandwidth-1 pair-correlation data cannot even distinguish GUE from half-integer spacing worlds.
- Formalized ceilings in the repo: bandwidth-one certificate ceiling 0.6818287; lemmaR_tight (two-moment rank-trace certificate exhausted); dimension cap d = lambda*N (nothing below lambda=1/2, 100% only at lambda=1 within rank arguments); kappa(lambda) = 1/lambda + lambda/3 >= 2/sqrt(3), so trace+Frobenius certificates cap at 0.8453 at ANY bandwidth.
- Literature no-gos: Bombieri small-support Weil positivity is unconditional (so small cones prove nothing); Bombieri-Garrett ~94% pseudo-Laplacian spectral cap; parity problem for sieve-only routes; Conrey-Li counterexamples to de Branges positivity conditions; Rodgers-Tao Lambda >= 0 (no sub-critical margin); Radziwill mollifier limitations.
- Campaign residue: ~30 refuted routes in the transcript; per-pair quadratic integrality pricing is FALSE (G1-G4); the Pontryagin negative-index counting route is structurally empty; "every attempted route's first substantive step was Weil positivity in disguise" — if yours is too, say exactly what NEW leverage you add.

QUALITY BAR: Be a designer, not a surveyor. Commit to ONE mechanism and develop it in depth with formulas and precise statements. The first_theorem must be genuinely well-posed (a statement a referee could evaluate), not a restatement of a famous conjecture. Prefer theorems whose INPUTS are already proven or provably within reach. It is acceptable — encouraged — for the horizon goal to be partial (better proportions, new equivalences, refutation channels) as long as the direction is novel and the first step is real. Do not fabricate literature; if you rely on a recalled result, flag it for verification. Return via StructuredOutput.

HARD OUTPUT BUDGET (previous designer attempts DIED exceeding the 64k output-token response ceiling — this is why you are being re-run): your ENTIRE StructuredOutput must total under 50,000 characters, and the schema enforces per-field maxLength caps. Write the densest technical prose you can: state the exponents and inequalities you derive and the method that yields them, but do NOT transcribe long derivations, tables, or exploratory dead ends into the output — derive in your head/scratch, report conclusions with enough detail for a referee to re-derive. If forced to choose, spend your budget on mechanism and first_theorem.`

const A4_BRIEF = `${COMMON}

TRACK A — ADVANCE THE EXISTING MACHINERY.
YOUR BRIEF: The Lindelof lock. The campaign identified but never attacked: an a-priori bound lambda_max(G-tilde/l1) = O(1) — equivalently bounds for P_X(tau) = sum_{n <= X} Lambda(n) n^{-1/2 - i*tau} on windows of length ~ 1/log T — would (a) unlock the third moment tr R^3 as a usable constraint for lambda < 2/3, (b) permit orthonormalization of the Gabor frame (converting inertia counts into genuine eigenvalue counts), and (c) price deep off-line pairs via operator-norm penalties. This is a SHORT-WINDOW MEAN VALUE problem about Dirichlet polynomials — exactly the territory of Guth-Maynard large-value estimates (arXiv:2405.20552) and the Tao-Trudgian-Yang ANTEDB exponent machinery. Design the bridge: what is the weakest short-window/large-value statement with a nontrivial payoff in the certificate, is it within reach of current large-value technology, and what does the full chain yield? Work out the actual exponents: what does Guth-Maynard's large-value theorem give for the measure of tau where |P_X(tau)| > V on windows of length 1/L, and where is the gap to what is needed? Also design the fallback: partial lambda_max bounds (e.g. lambda_max << L^eps or << X^eps) and their quantitative payoffs through the k_c machinery.

MANDATORY V5 FOLD-IN (2026-08-14 update to this brief): the parent paper's v5 (background item 4) makes your target paper-official. Cite and design against v5 SS7.2(e) (exact evaluation of tr G-tilde^k in the Rudnick-Sarnak range X^k <= T^{2-eps}) and SS7.3 (the conditional cubic-weight certificate omega(m)): present the Lindelof-lock chain as the SUPPLY LINE for the SS7.3 template's unconditional input — the paper has already built the certificate that consumes what you are asked to prove.

CAUTIONARY — REFUTED SIBLING (do not rebuild on its claims): proposal A2 (richer functionals) was adjudicated REFUTED with both fatals computationally verified (${PROG}/results/adjudication-A2.json; ${PROG}/directions/A2-richer-functionals.md). Specifically: (i) the "mixed-window corner" does NOT exist — cross-window kernels are transforms of window PRODUCTS (support min(lambda_i, lambda_j), verified numerically to ~1e-11 across two parameter sets); equal windows at 2/3 (the parent paper's own boundary) is the true optimum; (ii) the rank_trace_cubic identity is FALSE by exact counterexample (violation ~mu^3 vs quadratic remainder). A2's salvage items will be folded into THIS direction at merge time (the merged cubic-certificate direction per the completeness critic), so avoid its errors and do not re-derive its refuted identities.`

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
    repairs: { type: 'string', description: 'how to salvage/strengthen the proposal given the findings; empty if none needed or none possible' },
    literature_flags: { type: 'array', items: { type: 'string' }, description: 'recalled results the proposal relies on that need verification, or citations it gets wrong' },
  },
}

const CTX = `Background you MUST read first:
1. The proposal under review — its FULL TEXT is embedded at the end of this prompt (it has no directions/ file yet).
2. ${PROG}/results/map-hooks.txt — limitations + hooks of the zeta-2/3 method (condensed technical map).
3. ${PROG}/results/literature.md — Aug-2026 state of the art + all known no-go results.
Optional deeper sources: ${PROG}/results/full-map.md, ${PROG}/sources-extracted/ (paper pages full_p*.txt, transcript pages tx_*.txt), Lean sources under ${LEAN}.

THE OBSTRUCTION CANON (any proposal claiming a route to full RH must survive ALL of these; proportion-only routes must be honest about scope):
- DH/Epstein filter (RH-false lookalikes satisfying FE + explicit formula + L2 means — the route must consume an input they violate, e.g. Lambda(n) >= 0 / Euler product / Ramanujan).
- o(N)-blindness of density/proportion/moment methods; PCC alone already gives 100% simple-on-line WITHOUT giving RH.
- Formalized: bandwidth-one ceiling 0.6818287; lemmaR_tight; dimension cap d = lambda*N; kappa(lambda) >= 2/sqrt(3) so two-moment certificates cap at 0.845 at ANY bandwidth.
- Alternative Hypothesis world; Bombieri small-support Weil positivity (unconditional, hence empty); Bombieri-Garrett ~94% spectral cap; parity problem; Conrey-Li vs de Branges positivity conditions; Rodgers-Tao Lambda >= 0; Radziwill mollifier limitations; theta = 4/7 mollifier-length barrier.
- Campaign residue: per-pair quadratic integrality pricing FALSE; Pontryagin negative-index counting route structurally empty; visibility/interference wall for compressed detection of off-line zeros; "every refuted route's first substantive step was Weil positivity in disguise".`

const killerPrompt = (proposalJson) => `You are the KILLER — a maximally skeptical expert in analytic number theory whose job is to REFUTE a proposed RH research direction. Proposal: A4:lindelof-lock (full text embedded below).

${CTX}

Attack with every weapon:
(1) NO-GO COLLISION: does the proposal, examined carefully, actually collide with one of the canon obstructions despite its evasion claims? Check each evasion argument for real content vs hand-waving.
(2) BARRIER ZOO: construct (at least in sketch) an RH-false or otherwise pathological model world (Davenport-Heilbronn combination, Epstein class number 2, Beurling system with planted zeros, the 256-periodic adversarial law, the Alternative Hypothesis law, a fake Weil polynomial world) that satisfies ALL the inputs the proposal's route consumes. If you can, the route cannot prove what it claims — identify the exact overclaim.
(3) HIDDEN HARDNESS: is the first_theorem, or a lemma it silently needs, a known-hard problem in disguise (Lindelof, density hypothesis, HL prime-pair correlations, unbounded-support form factor, positivity at criticality)? Trace the dependency chain. For THIS proposal especially: is the short-window large-value bound it needs secretly equivalent to Lindelof itself?
(4) MECHANISM AUDIT: check the actual formulas/claims for mathematical errors — normalizations, growth rates, convergence, whether the claimed identity/inequality can hold, whether the numerics claimed would actually probe the mechanism.
Default to skepticism, but be honest: if an evasion argument is genuinely sound, say so — a false kill is as costly as a missed one. Findings must carry full technical arguments, not vibes. If the proposal claims only proportion progress or instrument-building (not full RH), judge it on THAT claim. Verdict 'refuted' requires at least one fatal finding you can defend. Return via StructuredOutput with lens='killer', proposal='A4:lindelof-lock'.

=== THE PROPOSAL (verbatim StructuredOutput of the designer) ===
${proposalJson}`

const refereePrompt = (proposalJson) => `You are the REFEREE — an expert evaluating a proposed RH research direction for novelty and tractability. Proposal: A4:lindelof-lock (full text embedded below).

${CTX}

Evaluate:
(1) NOVELTY AUDIT vs ${PROG}/results/literature.md and your knowledge: is the core mechanism actually new? Who is closest (name the papers)? Is it a known refuted/abandoned idea resurfacing? Would an expert in the relevant subfield say "we tried that in 19XX because..."? Distinguish: new object / new combination of known objects / repackaging.
(2) FIRST-THEOREM QUALITY: is it genuinely well-posed (statement a referee could evaluate)? Are its claimed inputs REALLY proven (check against literature.md; flag every recalled-from-memory citation)? Is the proof sketch plausible step by step? Estimate honestly: could a strong group prove it in ~2 years? Compare the designer's confidence number to yours.
(3) MILESTONE LADDER: are the milestones ordered by real dependency? Where is the first genuinely hard step ("the miracle")? Is the payoff claimed for each milestone correctly computed (check any constants against the map)?
(4) VALUE: if the first theorem lands but the horizon goal never does, is the theorem worth having on its own (new instrument, new equivalence, priced conjecture)? Score accordingly.
Findings must carry full technical arguments. Return via StructuredOutput with lens='referee', proposal='A4:lindelof-lock'.

=== THE PROPOSAL (verbatim StructuredOutput of the designer) ===
${proposalJson}`

phase('Design')
// effort pinned below the session's ultracode inherit: extended thinking counts toward the same
// 64k per-response output cap that killed attempts 4 and 5 before the JSON was even emitted.
const design = await agent(A4_BRIEF + '\n\nDELIVERY CONSTRAINT: produce the StructuredOutput call directly — do NOT write the design as a long plain-text message first and then re-emit it as JSON; every response you send must stay well under the output ceiling.', { label: 'A4:lindelof-lock', phase: 'Design', schema: SCHEMA, effort: 'high' })
if (!design) return { design: null, kill: null, kill2: null, ref: null, error: 'designer returned null' }
log('A4 design landed: ' + design.title)

phase('Verify')
// Session-4 process learning (binding): killer verdicts on load-bearing directions are DUPLICATED —
// two independent killers, neither sees the other's verdict. A2's reversal after a passed run-1
// verdict is the precedent.
const proposalJson = JSON.stringify(design, null, 2)
const [kill, kill2, ref] = await parallel([
  () => agent(killerPrompt(proposalJson), { label: 'kill:A4:lindelof-lock', phase: 'Verify', schema: VERDICT }),
  () => agent(killerPrompt(proposalJson) + '\n\n(NOTE: you are the SECOND of two independent killers run under the program\'s duplicate-killer protocol for load-bearing directions. You cannot see the other killer\'s output. Attack fresh — re-derive the central identities yourself rather than auditing around them.)', { label: 'kill2:A4:lindelof-lock', phase: 'Verify', schema: VERDICT }),
  () => agent(refereePrompt(proposalJson), { label: 'ref:A4:lindelof-lock', phase: 'Verify', schema: VERDICT }),
])

return { design, kill, kill2, ref }
