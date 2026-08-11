export const meta = {
  name: 'rh-design',
  description: 'Two-track design fan-out: 8 independent research-program designers for novel RH methods',
  phases: [
    { title: 'Design', detail: '4 Track-A (advance machinery) + 4 Track-B (new machinery) designers' },
  ],
}

const SCRATCH = '/private/tmp/claude-501/-Users-jaytyagi-Documents-Work-2026-Math-riemann-anthropic/e8c24f5f-4faf-41e1-962d-7ba16dbd457a/scratchpad'
const LEAN = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/zeta-23-lean-main'

const SCHEMA = {
  type: 'object', additionalProperties: false,
  required: ['title', 'thesis', 'mechanism', 'novelty', 'evades_obstructions', 'first_theorem', 'milestones', 'lean_hook', 'numerics', 'payoff', 'failure_modes', 'confidence'],
  properties: {
    title: { type: 'string' },
    thesis: { type: 'string', description: 'one-sentence claim of the approach' },
    mechanism: { type: 'string', description: 'the mathematical mechanism in full technical detail: objects, formulas, why it should work' },
    novelty: { type: 'string', description: 'exactly what is new relative to the literature; cite specific papers it goes beyond' },
    evades_obstructions: {
      type: 'array',
      items: { type: 'object', additionalProperties: false, required: ['obstruction', 'how'], properties: { obstruction: { type: 'string' }, how: { type: 'string' } } },
      description: 'for each relevant known no-go (DH/Epstein filter, AH, bandwidth-one ceiling, lemmaR_tight, dimension cap, kappa>=2/sqrt3, Bombieri small-support, Bombieri-Garrett 94%, parity, Conrey-Li, Lambda>=0), how the approach evades it or why it is out of scope',
    },
    first_theorem: { type: 'string', description: 'the single well-posed first theorem to attempt: precise statement, current status of the needed inputs, sketch of attack' },
    milestones: { type: 'array', items: { type: 'string' }, description: 'ordered ladder of 3-6 milestones from first theorem toward the horizon goal' },
    lean_hook: { type: 'string', description: 'which Zeta23 components to reuse/extend, and what the first formalizable statement would be' },
    numerics: { type: 'string', description: 'a concrete numerical experiment runnable now (Wolfram/Python scale) that would provide evidence for or against the mechanism' },
    payoff: { type: 'string', description: 'what improves if each milestone lands: constants, statements, or refutation channels' },
    failure_modes: { type: 'array', items: { type: 'string' } },
    confidence: { type: 'number', description: 'probability in [0,1] that first_theorem is provable within ~2 years by a strong group' },
  },
}

const COMMON = `You are a research mathematician designing a NOVEL attack direction related to the Riemann Hypothesis, as part of a structured research program that builds on the 2026 "two-thirds" theorem and its Lean formalization (repo: ${LEAN}).

MANDATORY BACKGROUND (read all three first):
1. ${SCRATCH}/full-map.md — six-agent technical map of the paper + Lean repo (method, exact constants, formalized no-go theorems, extension hooks).
2. ${SCRATCH}/literature.md — verified state of the art on 12 fronts as of Aug 2026, including all known obstruction/no-go results.
3. Raw sources available for grep/Read as needed: ${SCRATCH}/full_p*.txt (the 35-page paper, one file per page), ${SCRATCH}/condensed_p*.txt, ${SCRATCH}/tx_*.txt (the 95-page discovery-transcript volume, one file per page), and the Lean sources under ${LEAN}.

HARD DESIGN CONSTRAINTS (your proposal MUST address these explicitly in evades_obstructions):
- DH/Epstein filter: Davenport-Heilbronn and Epstein zeta (class number > 1) satisfy functional equation + explicit formula + L2 mean values yet violate RH. Any route claiming to reach FULL RH must consume an input these objects violate (Euler product at every prime / multiplicativity beyond L2-means / Ramanujan). A route that only improves proportions need not pass this filter but must say so honestly.
- Alternative Hypothesis: bandwidth-1 pair-correlation data cannot even distinguish GUE from half-integer spacing worlds.
- Formalized ceilings in the repo: bandwidth-one certificate ceiling 0.6818287; lemmaR_tight (two-moment rank-trace certificate exhausted); dimension cap d = lambda*N (nothing below lambda=1/2, 100% only at lambda=1 within rank arguments); kappa(lambda) = 1/lambda + lambda/3 >= 2/sqrt(3), so trace+Frobenius certificates cap at 0.8453 at ANY bandwidth.
- Literature no-gos: Bombieri small-support Weil positivity is unconditional (so small cones prove nothing); Bombieri-Garrett ~94% pseudo-Laplacian spectral cap; parity problem for sieve-only routes; Conrey-Li counterexamples to de Branges positivity conditions; Rodgers-Tao Lambda >= 0 (no sub-critical margin); Radziwill mollifier limitations.
- Campaign residue: ~30 refuted routes in the transcript; per-pair quadratic integrality pricing is FALSE (G1-G4); the Pontryagin negative-index counting route is structurally empty; "every attempted route's first substantive step was Weil positivity in disguise" — if yours is too, say exactly what NEW leverage you add.

QUALITY BAR: Be a designer, not a surveyor. Commit to ONE mechanism and develop it in depth with formulas and precise statements. The first_theorem must be genuinely well-posed (a statement a referee could evaluate), not a restatement of a famous conjecture. Prefer theorems whose INPUTS are already proven or provably within reach. It is acceptable — encouraged — for the horizon goal to be partial (better proportions, new equivalences, refutation channels) as long as the direction is novel and the first step is real. Do not fabricate literature; if you rely on a recalled result, flag it for verification. Return via StructuredOutput.`

const designers = [
  {
    label: 'A1:break-bandwidth',
    prompt: `${COMMON}

TRACK A — ADVANCE THE EXISTING MACHINERY.
YOUR BRIEF: Break the lambda = 1 bandwidth wall at its exact formalized location: the off-diagonal bilinear prime form O1 = sum_{n != m <= X} Lambda(n)Lambda(m)/sqrt(nm) * kernel(log n - log m), currently BOUNDED in absolute value by Montgomery-Vaughan (lemma chain O1_bound -> prop_PP -> tr2 in PrimeSideB) with zero cancellation used. Design the partial-evaluation program: which technology (dispersion, Kuznetsov/Deshouillers-Iwaniec spectral theory of Kloosterman sums, Guth-Maynard large-value estimates, averaged/almost-all-h Hardy-Littlewood a la Montgomery-Soundararajan, Goldston-type lower bounds on F(alpha) beyond alpha=1, additive-divisor asymptotics) gives the first NEW unconditional information at effective support 1 + delta or a nontrivial lower/upper bound on the form factor at the band edge? Include the HL*(4,lambda) fourth-moment route (payoff 13/18 = 0.7222) and the "edge-constraint LP" idea (constrain the form factor AT alpha = 1 and re-run the ceiling LP to price the theorem before proving it). Quantify the payoff curve (support 1.043 -> 70%, 1.265 -> 80%).`,
  },
  {
    label: 'A2:richer-functionals',
    prompt: `${COMMON}

TRACK A — ADVANCE THE EXISTING MACHINERY.
YOUR BRIEF: Exhaust bandwidth one with RICHER FUNCTIONALS that escape the formalized certificate format. The ceiling covers only certificates linear in the pair form factor with C^1 weights, valid configuration-by-configuration. Design the strongest escape: candidates include (i) closing the 0.6725 -> 0.6818 gap by optimizing (c0, r) against the 256-law (well-posed finite LP); (ii) weighted inertia / depth pricing — bound the eigenvalue MAGNITUDES of hyperbolic pair-blocks (an off-line pair at depth y contributes ~ X^{|y|}), turning depth blindness into a penalty, possibly via an unconditional upper bound on lambda_max(G-hat); (iii) commutator traces tr[P,Q]^2, multi-window matrix moment problems, traces against shifted grids; (iv) third/higher-correlation rows in the ceiling LP — compute the exact value of a triple-correlation upgrade BEFORE proving it; (v) non-configurationwise (average-validity) certificates. Use the tightness theorem lemmaR_tight as the map of what is exhausted: your functional must consume an invariant OUTSIDE {tr, Frobenius norm, n_+, integer atoms}. State which new prime-side asymptotic each functional needs and whether it exists at bandwidth <= 1 (e.g. mixed moments tr(P Q^2) via von Neumann-type inequalities).`,
  },
  {
    label: 'A3:families-derivatives',
    prompt: `${COMMON}

TRACK A — ADVANCE THE EXISTING MACHINERY.
YOUR BRIEF: Averaging and iteration escapes. Three coupled sub-directions; pick the strongest as first_theorem but design all three: (i) FAMILY AVERAGING: tr and Frobenius commute with averaging; orthogonality of characters restores effective bandwidth Lambda* = 1 for {chi mod q}: 2/3 on the line on average over the family with T as small as a power of log q. The named missing piece is a Gevrey-class taper making the Prop 4.2 tail work at tiny T — assess and design it. Extend to GL(2) families (individuals give literally nothing: c = 6/13 < 1/2). (ii) DERIVATIVE ESCALATION: the xi' transfer is formalized (0.86864 simple-on-line unconditional). Iterate to xi^(k) (Farmer-Gonek: proportions -> 1 as k -> infinity conditionally); design the unconditional per-derivative transfer and determine what the k -> infinity limit yields unconditionally (does it give "for every eps, proportion 1-eps of zeros of xi^(k(eps)) on line" and what does that imply for zeta zeros via zeros-of-derivative <-> zeros interlacing/Wu-style bootstraps?). Solve the xi'-analogue of the Montgomery-Taylor variational problem (the quartic window is ad hoc). (iii) HYBRID/UNIFORMITY: q <= T^theta giving H(1/(1+theta)) uniformly, and q-uniform Theorem E. Say precisely which sub-direction could yield a statement ABOUT ZETA ITSELF that is stronger than 2/3 (e.g. via Deuring-Heilbronn-type repulsion from family results).`,
  },
  {
    label: 'A4:lindelof-lock',
    prompt: `${COMMON}

TRACK A — ADVANCE THE EXISTING MACHINERY.
YOUR BRIEF: The Lindelof lock. The campaign identified but never attacked: an a-priori bound lambda_max(G-tilde/l1) = O(1) — equivalently bounds for P_X(tau) = sum_{n <= X} Lambda(n) n^{-1/2 - i*tau} on windows of length ~ 1/log T — would (a) unlock the third moment tr R^3 as a usable constraint for lambda < 2/3, (b) permit orthonormalization of the Gabor frame (converting inertia counts into genuine eigenvalue counts), and (c) price deep off-line pairs via operator-norm penalties. This is a SHORT-WINDOW MEAN VALUE problem about Dirichlet polynomials — exactly the territory of Guth-Maynard large-value estimates (arXiv:2405.20552) and the Tao-Trudgian-Yang ANTEDB exponent machinery. Design the bridge: what is the weakest short-window/large-value statement with a nontrivial payoff in the certificate, is it within reach of current large-value technology, and what does the full chain yield? Work out the actual exponents: what does Guth-Maynard's large-value theorem give for the measure of tau where |P_X(tau)| > V on windows of length 1/L, and where is the gap to what is needed? Also design the fallback: partial lambda_max bounds (e.g. lambda_max << L^eps or << X^eps) and their quantitative payoffs through the k_c machinery.`,
  },
  {
    label: 'B1:mult-positivity',
    prompt: `${COMMON}

TRACK B — WHOLLY NEW MACHINERY.
YOUR BRIEF: Multiplicativity-sensitive positivity — take the DH/Epstein filter as the DESIGN PRINCIPLE: build the positivity statement that FAILS for Davenport-Heilbronn but is provable for zeta on growing supports, i.e. inject the Euler product where the current method provably cannot see it. Resources to weigh: Connes-Consani archimedean Weil positivity (prolate/Sonin, arXiv:2006.13771) and the semilocal program; the campaign's empirical e^{-4piX} positivity-margin law with mechanism located in prolate spheroidal eigenvalue leakage (certified on supp [1/3,3] with primes 2,3,5,7 — transcript pages tx_005-015 region); mollification/amplification INSIDE the evaluation vectors v_z of the Gram matrix (arithmetic weights in the vectors rather than the scalar taper — the block machinery only needs sigma-equivariance); Suzuki arXiv:2301.00421 (Weil-form Hilbert space = de Branges space under RH). Design the concrete new object (e.g. a mollified/amplified Weil form W_M(f,f) with explicit Euler-product-derived weights), its explicit-formula expansion, what positivity on support [1/3+eps, 3-eps] -> growing windows requires, and the first provable instance. Be explicit about why Bombieri's small-support no-go and the "Weil positivity in disguise" pattern do not empty your addition: what NEW leverage does the multiplicative structure give beyond the L2 data?`,
  },
  {
    label: 'B2:refutation-program',
    prompt: `${COMMON}

TRACK B — WHOLLY NEW MACHINERY.
YOUR BRIEF: The refutation program — the strongest honest design for FINDING a counterexample or proving one cannot hide. Channels to design (choose the sharpest as first_theorem): (i) Lambda > 0 channel: RH <=> Lambda = 0 and Lambda >= 0 is known (Rodgers-Tao); a certified strictly positive lower bound on Lambda would DISPROVE RH. Design the search for the extremal structures (Lehmer-pair-like configurations under backward heat flow; Csordas-Smith-Varga lineage; what would a certified Lambda >= 10^{-N} computation require and is it feasible?); (ii) statistics channel: what statistic computable at accessible heights (T <= 10^13 rigorous, 10^22-10^36 sampled) would distinguish "RH true" from "RH fails at carrier-wave heights ~ 10^1000+" (Farmer arXiv:2211.11671 says none known — find the loophole or prove a small no-go); (iii) structure channel: given the NEW unconditional 2/3-simple + 5/6-distinct + form-factor theorems, what must an off-line zero's neighborhood look like? Derive constraints (repulsion, multiplicity, clustering with its mirror) that any counterexample must satisfy — a "wanted poster". Also assess: does the Alternative Hypothesis world (half-integer spacings) survive the new 2/3 theorem, and what is the cheapest additional statistic that would kill AH? Be rigorous about what current technology can certify; no wishful numerics.`,
  },
  {
    label: 'B3:arithmetic-debranges',
    prompt: `${COMMON}

TRACK B — WHOLLY NEW MACHINERY.
YOUR BRIEF: Arithmetic de Branges / multiplicity-visible compressions. The Weil form's signature counts DISTINCT off-line zeros (multiplicity invisible — proven in the transcript's Part I); the de Branges kernel K_a for E_a(z) = xi(a - iz) has EXACTLY kappa_a negative squares = N(beta > a) WITH multiplicity. The campaign recorded but never developed the "delta-tilt": d/da log|xi(a+it)/xi(1-a+it)| at a = 1/2 identified with 2*pi*nu_X (the explicit-formula density) — see transcript pages around tx_048. The blocker: K_a compressions are computable only from xi on vertical lines (Riemann-Siegel), not from primes. Design the program to make K_a (or a deformation K_{1/2+delta}) PRIME-COMPUTABLE: an unconditional identity linking compressions of the tilted kernel to prime sums, e.g. via the explicit formula for xi'/xi (already formalized in Zeta23/XiPrime!) or a two-parameter family interpolating between the Weil form (a = 1/2) and genuinely tilted kernels. Then the repo's inertia machinery applies WITH multiplicity sensitivity — the exact invariant the current certificate provably lacks (lemmaR_tight: on-line double = off-line pair). Address Conrey-Li (which killed de Branges' own positivity conditions — why is your use of K_a different?), and Suzuki arXiv:2301.00421 as the nearest neighbor. First theorem should be the unconditional identity or its simplest compressed instance.`,
  },
  {
    label: 'B4:zero-dynamics',
    prompt: `${COMMON}

TRACK B — WHOLLY NEW MACHINERY.
YOUR BRIEF: Zero dynamics — couple the brand-new unconditional statistics to the de Bruijn-Newman heat flow. The 2/3-simple, 5/6-distinct, and unconditional complex-zero form-factor theorems are ONE DAY OLD; nobody has fed them into the H_t flow (zeros of H_t; Lambda = infimum of t with all zeros real... normalized so RH <=> Lambda <= 0 with Lambda >= 0 known). Design the synthesis: (i) Polymath15's upper bound Lambda <= 0.2 used effective zero statistics + barrier computations; do the new theorems (esp. simplicity: repulsion of 2/3 of zeros, and the form factor for COMPLEX zeros) improve the effective inputs enough to push below 0.2? Work out where simplicity enters the Polymath15 pipeline. (ii) Conversely: under the flow, off-line zero pairs of H_0 = xi collide onto the real axis in finite time related to their depth; the certified on-line proportion at ALL heights constrains the flow's zero-attraction dynamics — design a "dynamical rank-trace certificate": apply the Zeta23 machinery to H_t for t < 0 (backward flow, where zeros move OFF the line in conjugate pairs with computable velocity) and ask what proportion statements for H_t, t in [-c, 0], imply at t = 0. The explicit formula for H_t exists (Polymath15); the Gram/inertia machinery is instantiation-agnostic (ZeroBlockData needs only reflection symmetry + local finiteness + log-density). (iii) The equivalence "RH <=> the two-thirds-type certificate value equals its GUE prediction for H_t uniformly in t"? Find the sharpest true statement in this family. Flag every input that is conjectural.`,
  },
]

phase('Design')
const results = await parallel(designers.map(d => () =>
  agent(d.prompt, { label: d.label, phase: 'Design', schema: SCHEMA })
))

const out = {}
designers.forEach((d, i) => { out[d.label] = results[i] })
return out