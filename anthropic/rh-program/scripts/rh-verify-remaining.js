export const meta = {
  name: 'rh-verify-remaining',
  description: 'Remaining Phase-4 verdicts: 6 missing killer/referee verdicts (A2,B4,C1,C2) + completeness critic; 12/18 already harvested in results/verdicts-partial.json',
  phases: [
    { title: 'Verify', detail: '2 independent critics per proposal' },
    { title: 'Completeness', detail: 'cross-slate gap analysis' },
  ],
}

const PROG = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/rh-program'
const LEAN = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'

const MISSING = [
  ['A2:richer-functionals', 'A2-richer-functionals', ['killer']],
  ['B4:zero-dynamics', 'B4-zero-dynamics', ['killer']],
  ['C1:requirements-first-field', 'C1-requirements-first-field', ['killer', 'referee']],
  ['C2:rigidity-conservation', 'C2-rigidity-conservation', ['killer', 'referee']],
]

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
1. ${PROG}/directions/<FILE>.md — the proposal under review (full text).
2. ${PROG}/results/map-hooks.txt — limitations + hooks of the zeta-2/3 method (condensed technical map).
3. ${PROG}/results/literature.md — Aug-2026 state of the art + all known no-go results.
Optional deeper sources: ${PROG}/results/full-map.md, ${PROG}/sources-extracted/ (paper pages full_p*.txt, transcript pages tx_*.txt), Lean sources under ${LEAN}.

THE OBSTRUCTION CANON (any proposal claiming a route to full RH must survive ALL of these; proportion-only routes must be honest about scope):
- DH/Epstein filter (RH-false lookalikes satisfying FE + explicit formula + L2 means — the route must consume an input they violate, e.g. Lambda(n) >= 0 / Euler product / Ramanujan).
- o(N)-blindness of density/proportion/moment methods; PCC alone already gives 100% simple-on-line WITHOUT giving RH.
- Formalized: bandwidth-one ceiling 0.6818287; lemmaR_tight; dimension cap d = lambda*N; kappa(lambda) >= 2/sqrt(3) so two-moment certificates cap at 0.845 at ANY bandwidth.
- Alternative Hypothesis world; Bombieri small-support Weil positivity (unconditional, hence empty); Bombieri-Garrett ~94% spectral cap; parity problem; Conrey-Li vs de Branges positivity conditions; Rodgers-Tao Lambda >= 0; Radziwill mollifier limitations; theta = 4/7 mollifier-length barrier.
- Campaign residue: per-pair quadratic integrality pricing FALSE; Pontryagin negative-index counting route structurally empty; visibility/interference wall for compressed detection of off-line zeros; "every refuted route's first substantive step was Weil positivity in disguise".`

const killerPrompt = (label, file) => `You are the KILLER — a maximally skeptical expert in analytic number theory whose job is to REFUTE a proposed RH research direction. Proposal: ${label}, file ${PROG}/directions/${file}.md.

${CTX}

Attack with every weapon:
(1) NO-GO COLLISION: does the proposal, examined carefully, actually collide with one of the canon obstructions despite its evasion claims? Check each evasion argument for real content vs hand-waving.
(2) BARRIER ZOO: construct (at least in sketch) an RH-false or otherwise pathological model world (Davenport-Heilbronn combination, Epstein class number 2, Beurling system with planted zeros, the 256-periodic adversarial law, the Alternative Hypothesis law, a fake Weil polynomial world) that satisfies ALL the inputs the proposal's route consumes. If you can, the route cannot prove what it claims — identify the exact overclaim.
(3) HIDDEN HARDNESS: is the first_theorem, or a lemma it silently needs, a known-hard problem in disguise (Lindelof, density hypothesis, HL prime-pair correlations, unbounded-support form factor, positivity at criticality)? Trace the dependency chain.
(4) MECHANISM AUDIT: check the actual formulas/claims for mathematical errors — normalizations, growth rates, convergence, whether the claimed identity/inequality can hold, whether the numerics claimed would actually probe the mechanism.
Default to skepticism, but be honest: if an evasion argument is genuinely sound, say so — a false kill is as costly as a missed one. Findings must carry full technical arguments, not vibes. If the proposal claims only proportion progress or instrument-building (not full RH), judge it on THAT claim. Verdict 'refuted' requires at least one fatal finding you can defend. Return via StructuredOutput with lens='killer', proposal='${label}'.`

const refereePrompt = (label, file) => `You are the REFEREE — an expert evaluating a proposed RH research direction for novelty and tractability. Proposal: ${label}, file ${PROG}/directions/${file}.md.

${CTX}

Evaluate:
(1) NOVELTY AUDIT vs ${PROG}/results/literature.md and your knowledge: is the core mechanism actually new? Who is closest (name the papers)? Is it a known refuted/abandoned idea resurfacing? Would an expert in the relevant subfield say "we tried that in 19XX because..."? Distinguish: new object / new combination of known objects / repackaging.
(2) FIRST-THEOREM QUALITY: is it genuinely well-posed (statement a referee could evaluate)? Are its claimed inputs REALLY proven (check against literature.md; flag every recalled-from-memory citation)? Is the proof sketch plausible step by step? Estimate honestly: could a strong group prove it in ~2 years? Compare the designer's confidence number to yours.
(3) MILESTONE LADDER: are the milestones ordered by real dependency? Where is the first genuinely hard step ("the miracle")? Is the payoff claimed for each milestone correctly computed (check any constants against the map)?
(4) VALUE: if the first theorem lands but the horizon goal never does, is the theorem worth having on its own (new instrument, new equivalence, priced conjecture)? Score accordingly.
Findings must carry full technical arguments. Return via StructuredOutput with lens='referee', proposal='${label}'.`

phase('Verify')
const results = await parallel(MISSING.flatMap(([label, file, lenses]) => lenses.map(lens =>
  lens === 'killer'
    ? () => agent(killerPrompt(label, file), { label: `kill:${label}`, phase: 'Verify', schema: VERDICT })
    : () => agent(refereePrompt(label, file), { label: `ref:${label}`, phase: 'Verify', schema: VERDICT })
)))

phase('Completeness')
const COMPLETE_SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['gaps', 'redundancies', 'cross_synergies', 'portfolio_assessment'],
  properties: {
    gaps: { type: 'array', items: { type: 'string' }, description: 'attack directions or instruments MISSING from the 9-proposal slate, with why they matter' },
    redundancies: { type: 'array', items: { type: 'string' }, description: 'where proposals overlap enough to merge' },
    cross_synergies: { type: 'array', items: { type: 'string' }, description: 'combinations of two+ proposals stronger than either alone' },
    portfolio_assessment: { type: 'string', description: 'overall: does this slate honestly maximize P(decide RH | months of work)? what single change most improves it?' },
  },
}
const completeness = await agent(`You are the COMPLETENESS CRITIC for an RH research program. Read ${PROG}/STATUS.md (constraints S1-S5, sponsor directive: new-machinery priority), ${PROG}/results/design-proposals.json (9 proposals; a 10th, A4:lindelof-lock on short-window Dirichlet-polynomial bounds via Guth-Maynard technology, is still being designed — treat it as present), and skim ${PROG}/results/literature.md. Identify: what attack directions, instruments, or hedges are MISSING from the slate (modalities not covered: e.g. automorphic/GL(n) leverage, random matrix universality inputs, additive combinatorics, computational/SAT-style certificates, physics constructions...); which proposals overlap; which combinations are stronger than their parts; and the single change that most improves P(program decides RH or produces field-defining results). Judge against the sponsor directive (Track B/C priority). Return via StructuredOutput.`, { label: 'completeness', phase: 'Completeness', schema: COMPLETE_SCHEMA })

return { verdicts: results.filter(Boolean), completeness }