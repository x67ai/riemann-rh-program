export const meta = {
  name: 'rh-design-supplement',
  description: 'Two additional new-field designer agents: requirements-first field construction, and rigidity/conservation-law framework',
  phases: [
    { title: 'Design', detail: '2 Track-C new-field designers' },
  ],
}

const SCRATCH = '/private/tmp/claude-501/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/scratchpad'
const PROG = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/rh-program'
const LEAN = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['title', 'thesis', 'mechanism', 'novelty', 'evades_obstructions', 'first_theorem', 'milestones', 'lean_hook', 'numerics', 'payoff', 'failure_modes', 'confidence'],
  properties: {
    title: { type: 'string' },
    thesis: { type: 'string', description: 'one-sentence claim of the approach' },
    mechanism: { type: 'string', description: 'the mathematical mechanism in full technical detail: objects, axioms, formulas, why it should work' },
    novelty: { type: 'string', description: 'exactly what is new relative to the literature; cite specific papers it goes beyond' },
    evades_obstructions: {
      type: 'array',
      items: { type: 'object', additionalProperties: false, required: ['obstruction', 'how'], properties: { obstruction: { type: 'string' }, how: { type: 'string' } } },
    },
    first_theorem: { type: 'string', description: 'the single well-posed first theorem to attempt: precise statement, status of needed inputs, sketch of attack' },
    milestones: { type: 'array', items: { type: 'string' } },
    lean_hook: { type: 'string' },
    numerics: { type: 'string', description: 'a concrete numerical experiment runnable now that would provide evidence for or against the mechanism' },
    payoff: { type: 'string' },
    failure_modes: { type: 'array', items: { type: 'string' } },
    confidence: { type: 'number' },
  },
}

const COMMON = `You are a research mathematician designing GENUINELY NEW MACHINERY — potentially the seed of a new mathematical field — for attacking the Riemann Hypothesis. This is part of a structured program building on the 2026 "two-thirds" theorem and its Lean formalization (${LEAN}). The sponsor's explicit position: existing machinery has provable limitations (that is why RH stands); they want field-construction, not extension of known programs.

MANDATORY BACKGROUND (read first):
1. ${PROG}/results/full-map.md — technical map of the paper + Lean repo (method, constants, formalized no-go theorems, hooks).
2. ${PROG}/results/literature.md — Aug-2026 state of the art on 12 fronts + all known obstructions + campaign residue.
3. Grep-able raw sources: ${PROG}/sources-extracted/full_p*.txt (35-page paper), condensed_p*.txt, tx_*.txt (95-page discovery transcript). Also ${SCRATCH} has the same files. Lean sources under ${LEAN}.

THE SPECIFICATION your new machinery must satisfy (this is the distillation of every known obstruction — treat it as the axioms of the design problem):
(S1) Euler-product sensitivity: it must consume an input that Davenport-Heilbronn and Epstein zeta functions (RH-false lookalikes satisfying functional equation + explicit formula + L2 mean values) VIOLATE — multiplicativity at every prime beyond L2-means, or Ramanujan-type bounds.
(S2) o(N)-sensitivity: it must be able to see a SINGLE off-line zero, not just a positive proportion — all density/proportion methods (including the full conjectural moment ladder) are structurally blind to o(N) exceptions.
(S3) Multiplicity-visibility: the Weil form's signature counts distinct off-line zeros only; an on-line double is indistinguishable from an off-line pair in the existing certificate (lemmaR_tight).
(S4) A positivity source that is NOT just "test Weil positivity on a bigger cone": Bombieri proved small-support Weil positivity unconditionally (proves nothing); the campaign found every refuted route's first substantive step was Weil positivity in disguise. If your route IS ultimately Weil positivity, it must add a genuinely new positivity GENERATOR (algebraic: Hodge-index/ampleness/intersection theory; analytic: reflection positivity, complete monotonicity, operator monotone functions; combinatorial: hyperbolicity/log-concavity/Lorentzian polynomials; probabilistic: negative association/determinantal structure) with an argument for why that generator can be verified for zeta.
(S5) It must not be killed by: the Alternative Hypothesis world, Bombieri-Garrett's ~94% spectral cap, the parity problem, Conrey-Li's counterexamples to de Branges positivity, Rodgers-Tao Lambda >= 0 (no sub-critical margin), or the formalized bandwidth/two-moment ceilings. Address each relevant one explicitly.

QUALITY BAR: Commit to ONE design and develop it in depth: the new objects, their axioms, the master inequality or master identity the field is organized around, and the shortest path to a first genuinely well-posed theorem (a statement a referee could evaluate, whose inputs are proven or provably within reach — NOT a restatement of a famous conjecture). New-field proposals are allowed to have long horizons, but the first theorem must be real and near. Do not fabricate literature; flag recalled results for verification. Return via StructuredOutput.`

const designers = [
  {
    label: 'C1:requirements-first-field',
    prompt: `${COMMON}

YOUR BRIEF — REQUIREMENTS-FIRST FIELD CONSTRUCTION. Work BACKWARDS from the specification (S1)-(S5): design the minimal mathematical universe in which an RH-deciding inequality could live, then identify the shortest bridge from existing mathematics to that universe. Candidate skeletons to evaluate honestly and then CHOOSE ONE (or a hybrid, or something not listed):
(a) Arithmetic intersection theory completed: Connes-Consani have Riemann-Roch for Spec Z (CRAS 2024), a Jacobian (JNCG 2026), and the absolute curve (arXiv:2606.06604) — write down what the HODGE INDEX theorem would have to SAY there, in checkable terms: what is the surface playing the role of C x C, what is a correspondence (Frobenius has no obvious analogue — the scaling flow plays it), what replaces intersection numbers (Weil form values?), and precisely which finite verifiable statement would be the analogue of "deg(Z.Z') <= ..." — then find the first instance provable today.
(b) Reflection positivity: an Osterwalder-Schrader-type axiom system on the adele class space / the multiplicative group, in which zeta's completed functional equation is the reflection and the Euler product furnishes a Markov/transfer-operator structure; RP would give positivity of the reflected form. What is the transfer operator whose spectral radius statement IS RH, and is there a Perron-Frobenius-type route to its positivity that uses every prime (S1)?
(c) Lorentzian/log-concavity technology (Branden-Huh lineage): is there a family of polynomials attached to zeta (e.g. Jensen polynomials — note Griffin-Ono-Rolen-Zagier proved hyperbolicity for all shifts in the DERIVATIVE aspect, a density-type result blind to (S2) — or Turan-type expressions, or the LawN256-style LP duals) whose Lorentzian property would be RH-complete, with a combinatorial/algebraic proof strategy that goes through an exchange property rather than analysis?
Pick the skeleton with the best (specification-fit x first-theorem-nearness) product and BUILD: axioms, master inequality, first theorem. State exactly where the Euler product enters (S1) and why a single off-line zero breaks the master inequality (S2).`,
  },
  {
    label: 'C2:rigidity-conservation',
    prompt: `${COMMON}

YOUR BRIEF — RIGIDITY AND CONSERVATION LAWS: a framework whose native sensitivity is to SINGLE defects, not proportions — attacking (S2) head-on, where every existing method fails. Raw material to forge into a field:
(i) NUMBER RIGIDITY of point processes (Ghosh-Peres): the sine-kernel process is number-rigid — the configuration outside any bounded window determines the count inside it almost surely. The zeta zero process is conjecturally sine-kernel; the explicit formula provides EXACT deterministic sum rules (one per test function) linking zeros to primes. Design the deterministic analogue: an "arithmetic rigidity" theory in which the explicit-formula sum rules form a conservation-law system, and ask what a single off-line pair COSTS across the whole system simultaneously (it perturbs every sum rule coherently: f-hat evaluated at a complex point gamma with |Im gamma| = depth, growing like e^{L|Im gamma|} with bandwidth — the one place where an off-line zero is EXPONENTIALLY visible rather than invisible). The transcript's Part I visibility analysis (tx_016, tx_031-035, tx_047-053) found per-window compressions cannot see it configuration-free — but a GLOBAL, multi-window, exact-identity system was never tried: design the conserved quantities, the a-priori bounds on them from the prime side (this is where (S1) enters: the prime side of the sum rules IS the Euler product data), and the master rigidity statement "any configuration satisfying ALL sum rules with prime side equal to zeta's is on-line".
(ii) The obstruction to fear: Davenport-Heilbronn satisfies ITS OWN explicit formula with off-line zeros — so the conserved system must use positivity/structure of zeta's prime side that DH's coefficient sequence lacks (DH coefficients are not multiplicative / not nonnegative on prime powers; Lambda(n) >= 0 is itself a powerful constraint DH violates! Weil positivity never uses Lambda >= 0 pointwise — the L2 theory can't see signs). Investigate: is POINTWISE NONNEGATIVITY of the prime-side measure (Lambda(n) >= 0, i.e. a POSITIVE measure on the multiplicative side, making nu_X a signed measure with known positive part) the cheap, overlooked (S1) input? What does the cone of test functions with f-hat >= 0 AND f >= 0 (both-sided positivity, the Boas-Kac/Cohn-Elkies cone from sphere packing, already used by Carneiro-Milinovich-Ramos arXiv:2310.01913 under RH) yield UNCONDITIONALLY against the explicit formula when combined with Lambda >= 0? Design the strongest unconditional statement in this cone and whether it can break (S2)'s proportion barrier via infinite systems of inequalities rather than single certificates.
Choose the sharpest formulation and BUILD: conserved quantities, the master statement, the first well-posed theorem (e.g. a quantitative single-defect visibility theorem under an explicit density hypothesis, improving on the transcript's impossibility heuristic).`,
  },
]

phase('Design')
const results = await parallel(designers.map(d => () =>
  agent(d.prompt, { label: d.label, phase: 'Design', schema: SCHEMA })
))

const out = {}
designers.forEach((d, i) => { out[d.label] = results[i] })
return out