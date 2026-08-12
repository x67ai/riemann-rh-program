export const meta = {
  name: 'rh-grossmann-sweep2',
  description: 'Grossmann sweep wave 2: the 11 unswept corners named by the wave-1 synthesizer; closure synthesizer merges both waves',
  phases: [
    { title: 'Sweep2', detail: 'one scout per unswept corner' },
    { title: 'Close', detail: 'merge with wave 1, closure verdict' },
  ],
}

const PROG = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/rh-program'

const SPEC = `THE S1-S5 SPECIFICATION (what any RH-deciding machinery must satisfy; distilled from formalized obstructions):
- S1 Euler-product sensitivity: consume an input Davenport-Heilbronn/Epstein (class no.>1) VIOLATE (multiplicativity at every prime beyond L2-means; Lambda(n) >= 0 pointwise; Ramanujan; "sits in the functorial tower"). DH/Epstein satisfy FE + explicit formula + L2 mean values yet violate RH, so any full-RH route must consume such an input — ideally at the AXIOM level, not the estimate level.
- S2 o(N)-sensitivity: must see a SINGLE off-line zero; all density/proportion methods are structurally blind to o(N) exceptions (PCC alone already gives 100% on-line without RH).
- S3 Multiplicity-visibility: on-line double vs off-line pair must be distinguishable (the Weil-form signature is not).
- S4 A new positivity GENERATOR, not a bigger Weil-positivity cone (Weil positivity is EQUIVALENT to RH, so assuming any reparametrization of it is circular; the campaign post-mortem: "every refuted route's first substantive step was Weil positivity in disguise"). Sanctioned generator classes: algebraic (Hodge index/ampleness), analytic (reflection positivity/complete monotonicity/Lee-Yang), combinatorial (Lorentzian polynomials), probabilistic (determinantal/negative association).
- S5 Survive the named no-gos: Alternative Hypothesis world; Bombieri small-support Weil positivity (unconditional hence empty); Bombieri-Garrett ~94% pseudo-Laplacian spectral cap; parity problem; Conrey-Li vs de Branges positivity; Rodgers-Tao Lambda >= 0 (RH iff Lambda=0); bandwidth-one ceiling 0.6818287 and two-moment cap 0.8453 (formalized in Lean); mollifier limits.
- S6 (NEW, wave-1 amendment from the comparative-anatomy scout): finite-rank/tower rationality + a doubled object — every historically successful RH proof ran positivity on the SQUARE of the underlying object with a finite-dimensional (or tower-rational) trace calculus.`

const BRANCHES = [
  ['pretentious-multiplicative', 'Pretentious multiplicative number theory',
   'Granville-Soundararajan pretentious distance, Halasz theory, Koukoulopoulos treatise. The major post-2000 analytic school that reproves PNT/zero-free regions WITHOUT zeros. Verdict needed: does pretentious distance D(f,g) define a positivity/rigidity structure that sees zero LOCATION (not just mean values), and is there any pretentious statement equivalent to or stronger than a zero-free region that DH-lookalikes violate? Where does the school itself say its methods stop?'],
  ['harper-multiplicative-chaos', 'Random multiplicative functions & multiplicative chaos',
   'Harper better-than-squareroot cancellation, low moments of random multiplicative functions and character sums, critical multiplicative chaos (Soundararajan-Zaman? verify), Gaussian multiplicative chaos links to zeta maxima (FHK). A multiplicativity-NATIVE probabilistic technology distinct from Gowers and DPP. Is there any deterministic-certificate form, or a quenched->deterministic transfer, that could touch the actual zeta? Who has tried?'],
  ['riemann-hilbert-painleve', 'Riemann-Hilbert methods, integrable systems, Painleve',
   'Deift-Its school: EXACT non-asymptotic Fredholm determinant identities (sine kernel, Tracy-Widom, Painleve V), isomonodromy. Unlike CUE asymptotics these are exact identities — S2-relevant in principle. Is there any exact integrable structure connected to zeta itself (not its statistics) — e.g. Its-style RH problems for zeta, Fokas work on the Lindelof hypothesis (verify what his program actually proves!), lattice models whose partition function is xi?'],
  ['tomita-takesaki-entropy', 'Tomita-Takesaki modular theory & operator-algebraic entropy',
   'Modular flows, Araki relative entropy, QNEC, Longo entropy bounds. Relative-entropy monotonicity is a PROVEN positivity generator class absent from the S4 grid. The Bost-Connes system has KMS structure with spontaneous symmetry breaking at beta=1. Is there a modular-theoretic positivity statement about the BC system (or the adele class space) that constrains zeros? Has anyone (Longo, Lechner, van Suijlekom?) tried entropy methods on arithmetic systems?'],
  ['weyl-group-mds', 'Weyl-group multiple Dirichlet series',
   'Bump-Friedberg-Goldfeld, Diaconu, Chinta-Gunnells: multiple Dirichlet series with continuation via Weyl-group symmetry — a structural (non-estimate) continuation mechanism. Does the MDS functional-equation group generate constraints on zero location for the diagonal zeta factors? Any MDS-native positivity? Where has the school taken this relative to moments (Diaconu-Goldfeld-Hoffstein) and what died?'],
  ['beyond-endoscopy-ngo', 'Beyond endoscopy, Braverman-Kazhdan, Ngo program',
   'Trace-formula geometrization of functoriality: Langlands beyond-endoscopy, Braverman-Kazhdan-Ngo gamma-sheaves/rho-Poisson summation, Ali Altug elimination of the trivial representation. Expected closure: functoriality machinery has no zero-location content — but VERIFY: the beyond-endoscopy stable trace formula manipulations involve exactly the L-function poles/residues, and Altug-Arthur weighted orbital analysis touches zeta directly. Where exactly does zero-location content fail to appear?'],
  ['lapidus-complex-dimensions', 'Lapidus complex dimensions & fractal strings',
   'Lapidus-van Frankenhuijsen complex dimensions, the Lapidus-Maier inverse-spectral RH criterion (one can hear the RH?), fractal membranes/Lapidus quantized number theory (verify his 2015+ "fractal cohomology" claims). Cheap closure check: what precisely is proven, is the inverse-spectral equivalence just a restatement (Weil positivity in disguise?), and did the fractal-cohomology program produce any theorem about zeta zeros.'],
  ['decoupling-structural-ceiling', 'Decoupling & efficient congruencing: structural ceiling audit',
   'Bourgain-Demeter-Guth decoupling, Wooley efficient congruencing, Guth-Maynard 2024 and the ANTEDB exponent database. This is A4\'s supply line — but the sweep question is STRUCTURAL: is there a decoupling-native ceiling theorem (analogous to the bandwidth ceiling) delimiting what ANY decoupling-type input can give for zero-density/zero-location? Is Lindelof itself the natural boundary of the technology, and is THAT statement provable? What do Guth-Maynard themselves name as the wall?'],
  ['prismatic-f-gauges', 'Prismatic cohomology & F-gauges over Z',
   'Bhatt-Lurie-Drinfeld prismatization, F-gauges, the stacky approach to p-adic cohomology; Drinfeld "Shimurian" analogues. The newest candidate substrate for "cohomology of Spec Z" DISTINCT from condensed/Clausen-Scholze. Watch-grade questions: do F-gauges glue over all p into anything with an archimedean component; is there any statement about zeta or L-functions in the BLD circle (e.g. via syntomic regulators); do the authors say anything about Weil-cohomology-over-Z obstructions (Deninger arXiv:2204.02714 no-go) applying to their stacks?'],
  ['relative-langlands-bzsv', 'Relative Langlands duality (Ben-Zvi--Sakellaridis--Venkatesh)',
   'The BZSV period <-> L-function duality: hyperspherical varieties, quantization, the systematic structural home of Waldspurger/Ichino-Ikeda central-value nonnegativity. Wave-1 automorphic scout used those nonnegativity theorems pointwise; the sweep question: does BZSV upgrade central-value positivity to a FAMILY/interior positivity principle (periods as |.|^2 throughout a region?), and is there any BZSV-native statement DH-lookalikes violate at the axiom level?'],
  ['arithmetic-dynamics-equidistribution', 'Arithmetic dynamics & adelic equidistribution of small points',
   'Yuan equidistribution, adelic line bundles (Yuan-Zhang book 2021+), Szpiro-Ullmo-Zhang, arithmetic Yau-Zariski? positivity of adelic metrics as a technology. Adjacent to but distinct from wave-1 arakelov coverage: equidistribution theorems are POSITIVITY-DRIVEN (arithmetic ampleness) and quantitative. Is there a route from adelic equidistribution/height positivity to constraints on zeta zeros (e.g. via heights of special cycles, Faltings heights in families), and has anyone attempted it?'],
]

const REPORT = {
  type: 'object', additionalProperties: false,
  required: ['branch', 'verdict', 'confidence', 'fit', 'key_objects', 'prior_attacks', 'live_entry_points', 'first_interface', 'access_failures', 'verified_online', 'recalled_unverified'],
  properties: {
    branch: { type: 'string' },
    verdict: { type: 'string', enum: ['grossmann-candidate', 'instrument', 'dead-end', 'needs-deeper-look'] },
    confidence: { type: 'number', description: '0-1 confidence in the verdict' },
    fit: { type: 'object', additionalProperties: false, required: ['S1', 'S2', 'S3', 'S4', 'S5', 'S6'], properties: {
      S1: { type: 'string' }, S2: { type: 'string' }, S3: { type: 'string' }, S4: { type: 'string' }, S5: { type: 'string' }, S6: { type: 'string' },
    }, description: 'per-spec-item: score 0-5 + one-line justification' },
    key_objects: { type: 'array', items: { type: 'string' } },
    prior_attacks: { type: 'array', items: { type: 'string' }, description: 'every serious RH attack from this branch: who, when, citation, EXACTLY where it died (or why still alive)' },
    live_entry_points: { type: 'array', items: { type: 'string' }, description: 'current live interfaces with citations (2024-2026 verified where possible)' },
    first_interface: { type: 'string', description: 'the sharpest referee-evaluable theorem statement that would connect this branch to zeta under the spec' },
    access_failures: { type: 'array', items: { type: 'string' }, description: 'papers/resources you could NOT access — the sponsor will fetch these manually' },
    verified_online: { type: 'array', items: { type: 'string' } },
    recalled_unverified: { type: 'array', items: { type: 'string' } },
  },
}

const scoutPrompt = (name, brief) => `You are a research scout in a Riemann Hypothesis research program executing WAVE 2 of the GROSSMANN SWEEP (sponsor standing order: exhaustively check whether an EXISTING branch of mathematics already contains the machinery an RH proof needs, before the program builds a new branch from scratch). Wave 1 covered 24 branches and concluded "no Grossmann — the generator exists but the geometry does not"; your branch was flagged as an UNSWEPT CORNER and the sweep cannot close without it.

YOUR BRANCH: ${name}.
BRIEF: ${brief}

READ FIRST (local files):
1. ${PROG}/STATUS.md — program dashboard: spec, hard constraints, sponsor standing orders (BINDING, esp. order 5: no unverified claims presented as verified).
2. ${PROG}/results/grossmann-sweep.json — wave-1 reports + synthesis (read the synthesis and any neighboring branch reports; do not duplicate their coverage — your job is what they MISSED).
3. ${PROG}/results/literature.md — Aug-2026 state of the art.

${SPEC}

TASK:
(1) Map the branch's candidate machinery against the spec (S1-S6).
(2) PRIOR ART — MANDATORY AND ONLINE: every serious RH attack from this branch — who, when, exact citation, precisely where it died (or why alive). Use WebSearch and WebFetch (load via ToolSearch if not yet available) on arXiv and journals; verify the 2024-2026 state. Strictly separate VERIFIED-online from RECALLED-unverified claims.
(3) ACCESS FAILURES: record every unreachable resource in access_failures — the sponsor fetches these manually. NEVER substitute memory for an inaccessible source.
(4) Score fit S1-S6 (0-5 each, one-line justification).
(5) VERDICT: 'grossmann-candidate' | 'instrument' | 'dead-end' | 'needs-deeper-look' (when torn, prefer needs-deeper-look with the missing datum named).
(6) first_interface: the sharpest CONCRETE, referee-evaluable theorem statement connecting this branch to zeta under the spec.

The DH/Epstein filter is always the first test: does the branch's proposed input distinguish zeta from RH-false lookalikes at the AXIOM level? Return via StructuredOutput.`

const CLOSE = {
  type: 'object', additionalProperties: false,
  required: ['wave2_summary', 'revised_shortlist', 'needs_sponsor_fetch', 'still_unswept', 'closure_verdict'],
  properties: {
    wave2_summary: { type: 'array', items: { type: 'string' }, description: 'one line per wave-2 branch: verdict + the decisive datum' },
    revised_shortlist: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['branch', 'why', 'next_action'], properties: {
      branch: { type: 'string' }, why: { type: 'string' }, next_action: { type: 'string' } } }, description: 'the FINAL sweep shortlist merging both waves, ranked' },
    needs_sponsor_fetch: { type: 'array', items: { type: 'string' }, description: 'NEW access failures from wave 2 (do not repeat wave-1 items)' },
    still_unswept: { type: 'array', items: { type: 'string' }, description: 'anything STILL uncovered after both waves, or empty with justification' },
    closure_verdict: { type: 'string', description: 'does wave 2 change the wave-1 verdict (no Grossmann, proceed de novo)? Final closure statement for the sweep phase. 150-300 words' },
  },
}

phase('Sweep2')
const reports = await parallel(BRANCHES.map(([key, name, brief]) => () =>
  agent(scoutPrompt(name, brief), { label: `sweep2:${key}`, phase: 'Sweep2', schema: REPORT, effort: 'high' })
))
const ok = reports.filter(Boolean)
log(`Wave 2 complete: ${ok.length}/${BRANCHES.length} scouts returned`)

phase('Close')
const closure = await agent(`You are the CLOSURE SYNTHESIZER of the Grossmann sweep (wave 2) in an RH research program. Read ${PROG}/results/grossmann-sweep.json (wave-1 reports + synthesis, including its verdict "no Grossmann — the generator exists but the geometry does not" and its shortlist). The ${BRANCHES.length} wave-2 scout reports (the corners wave 1 missed) are appended. Produce: the wave-2 summary; the FINAL merged shortlist for the whole sweep (does any wave-2 branch join or displace the wave-1 top 5?); NEW sponsor-fetch items only; anything STILL unswept (be adversarial, then justify closure); and the closure verdict — does wave 2 change "no Grossmann, proceed de novo"? Return via StructuredOutput.

WAVE-2 SCOUT REPORTS:
${JSON.stringify(ok)}`, { label: 'closure', phase: 'Close', schema: CLOSE })

return { reports: ok, closure, dropped: BRANCHES.length - ok.length }
