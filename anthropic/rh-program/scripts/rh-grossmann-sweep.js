export const meta = {
  name: 'rh-grossmann-sweep',
  description: 'Grossmann sweep: fit 24 existing branches of mathematics against the S1-S5 spec before building a new branch from scratch (sponsor standing order 6)',
  phases: [
    { title: 'Sweep', detail: 'one scout per branch, online-verified' },
    { title: 'Synthesize', detail: 'ranked shortlist + unswept-corner check' },
  ],
}

const PROG = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic/rh-program'

const SPEC = `THE S1-S5 SPECIFICATION (what any RH-deciding machinery must satisfy; distilled from formalized obstructions):
- S1 Euler-product sensitivity: consume an input Davenport-Heilbronn/Epstein (class no.>1) VIOLATE (multiplicativity at every prime beyond L2-means; Lambda(n) >= 0 pointwise; Ramanujan; "sits in the functorial tower"). DH/Epstein satisfy FE + explicit formula + L2 mean values yet violate RH, so any full-RH route must consume such an input — ideally at the AXIOM level, not the estimate level.
- S2 o(N)-sensitivity: must see a SINGLE off-line zero; all density/proportion methods are structurally blind to o(N) exceptions (PCC alone already gives 100% on-line without RH).
- S3 Multiplicity-visibility: on-line double vs off-line pair must be distinguishable (the Weil-form signature is not).
- S4 A new positivity GENERATOR, not a bigger Weil-positivity cone (Weil positivity is EQUIVALENT to RH, so assuming any reparametrization of it is circular; the campaign post-mortem: "every refuted route's first substantive step was Weil positivity in disguise"). Sanctioned generator classes: algebraic (Hodge index/ampleness), analytic (reflection positivity/complete monotonicity/Lee-Yang), combinatorial (Lorentzian polynomials), probabilistic (determinantal/negative association).
- S5 Survive the named no-gos: Alternative Hypothesis world; Bombieri small-support Weil positivity (unconditional hence empty); Bombieri-Garrett ~94% pseudo-Laplacian spectral cap; parity problem; Conrey-Li vs de Branges positivity; Rodgers-Tao Lambda >= 0 (RH iff Lambda=0); bandwidth-one ceiling 0.6818287 and two-moment cap 0.8453 (formalized in Lean); mollifier limits.`

// [key, display name, brief]
const BRANCHES = [
  ['arakelov-hodge-index', 'Arakelov / arithmetic intersection theory & Hodge index over Spec Z',
   'The ONLY mechanism that ever proved an RH (Weil via Castelnuovo, Deligne via weights) is intersection-theoretic positivity. Map the current distance to a workable "surface" Spec Z x Spec Z with intersection pairing + index theorem: Gillet-Soule arithmetic Hodge index, Bost slopes/theta-invariants, and the ACTIVE Connes-Consani absolute-geometry line (Riemann-Roch for Spec Z-bar, CRAS 2024; the Jacobian of Spec Z, JNCG 2026; arXiv:2606.06604). Identify the exact missing ingredient(s) and whether any is a theorem-shaped target rather than a philosophy.'],
  ['f1-lambda-rings', 'F1-geometry: Lambda-rings, blueprints, arithmetic site',
   'Borger Lambda-ring F1, Soule varieties, Lorscheid blueprints, Connes-Consani arithmetic/scaling sites. Does ANY F1 formalism yet produce a cohomology with a Lefschetz fixed-point formula for a Frobenius-at-the-archimedean-place? Where does each formalism provably stall?'],
  ['ncg-trace-formula', 'Noncommutative geometry: adele class space, prolate operators',
   'Connes trace-formula equivalence of RH, adele class space, the semilocal prolate wave operator (arXiv:2310.18423), Connes-Consani zeta-cycles and their 2026 survey; Bost-Connes systems. Locate EXACTLY where the positivity gap sits today, what the prolate spectral results actually prove, and whether the campaign residue (e^{-4piX} margin law, prolate eigenvalue leakage mechanism) matches their published quantities.'],
  ['automorphic-functoriality', 'Automorphic forms / functoriality positivity',
   'Rankin-Selberg nonnegativity (-L\'/L(s, pi x pi-tilde) has nonnegative Dirichlet coefficients) is a PROVEN S1-grade positivity generator; DH/Epstein have no automorphic origin, so "zeta sits in the functorial tower" passes the DH filter at the AXIOM level. Known uses: zero-free regions, Luo-Rudnick-Sarnak, Sarnak-Thorner? Can functoriality power a positivity forcing the LINE (not just regions)? What is the strongest known "functoriality => zero-location" statement?'],
  ['additive-combinatorics', 'Additive combinatorics: Gowers uniformity of the primes',
   'Green-Tao-Ziegler U^k-uniformity of W-tricked Lambda, Matomaki-Radziwill short intervals, Tao-Teravainen Chowla/Sarnak progress — proven, unconditional, DH-violating inputs. Could U^3-type control substitute for Hardy-Littlewood prime-pair input at the program\'s named wall (the O1_bound -> prop_PP -> tr2 lemma chain; triple-correlation supply lines)? Has anyone connected Gowers norms to zero statistics? Check 2024-2026 literature.'],
  ['determinantal-rigidity', 'Determinantal point processes, negative association, rigidity',
   'Ghosh-Peres number rigidity, Lyons DPP theory, negative association, hyperuniformity/stealth. The sine process is determinantal and zeros are conjecturally sine-distributed. Is there a DETERMINISTIC certificate form of determinantal/negative-association structure applicable to a fixed (non-random) zero set unconditionally? Who has tried?'],
  ['fourier-duality-crystalline', 'Fourier optimization, interpolation, crystalline measures',
   'Cohn-Elkies duality, Viazovska magic functions, Radchenko-Viazovska interpolation, crystalline measures / Fourier quasicrystals (Kurasov-Sarnak 2020-2023, Olevskii-Ulanovskii, Meyer). The explicit formula says (zeros, prime powers) is a crystalline summation pair. Do the recent uniqueness/rigidity theorems for crystalline measures and Fourier interpolation bases constrain OFF-line configurations? Check the Bondarenko-Radchenko-Seip and Carneiro-school 2023-2026 work.'],
  ['debranges-canonical-systems', 'de Branges spaces & Krein canonical systems',
   'Post-Conrey-Li state: which de Branges-type positivity routes remain viable? Krein canonical systems realizing xi (does an explicit Hamiltonian exist? Suzuki arXiv:2301.00421 and successors; Lagarias program; Kaltenback-Woracek indefinite Hermite-Biehler/Pontryagin theory). Note this program already refuted two tilted/jet instantiations (B1, C1 — read their direction files) — what remains OUTSIDE what those refutations covered?'],
  ['reflection-positivity-qft', 'Reflection positivity & constructive QFT',
   'Osterwalder-Schrader, chessboard estimates, lattice RP, Neeb-Olafsson RP on symmetric spaces. This program REFUTED one instantiation (C1: tilted RP — read directions/C1-requirements-first-field.md first). The sweep question is broader: does ANY RP setup exist whose transfer operator is genuinely arithmetic (prime-indexed) with a PROVEN spectral statement? Any physics-side construction with zeta as partition function where RP is established?'],
  ['transfer-operators-dynamics', 'Transfer operators & thermodynamic formalism',
   'Mayer transfer operator (Gauss map <-> Selberg zeta for PSL(2,Z)), Lewis-Zagier period functions, Ruelle zeta, Dolgopyat-type estimates, Pollicott-Sharp. Dynamical RH-analogues are THEOREMS in hyperbolic settings. What structural ingredient makes them provable, and what is the state of the search for a dynamical system whose Ruelle/Fredholm determinant IS Riemann zeta?'],
  ['deninger-weil-etale', 'Deninger cohomological program & Weil-etale cohomology',
   'Deninger foliated dynamical systems / regularized determinants program (30 years on — current state? his 2020s papers), Lichtenbaum Weil-etale cohomology, arithmetic topology. Also Kucharczyk-Scholze (realizing Galois groups via topology) as a possible modern foothold. What is proven vs programmatic; sharpest partial result.'],
  ['berry-keating-xp', 'Hilbert-Polya operator constructions: xp and successors',
   'Berry-Keating xp, Connes absorption spectrum, Sierra models, Bender-Brody-Muller, Knauf. HARD CONSTRAINT to apply: Bombieri-Garrett ~94% pseudo-Laplacian cap (arXiv:2002.07929) and the fact that self-adjointness-with-zeros-as-spectrum is essentially equivalent to RH (the positivity must COME from somewhere). Verdict question: does anything in this genre have an arithmetic self-adjointness MECHANISM, or is it all spectral bookkeeping?'],
  ['random-matrix-moments', 'Random matrix theory beyond pair correlation',
   'Keating-Snaith moments, CFKRS recipes, ratios conjectures, Fyodorov-Hiary-Keating maxima, recent moment theorems (2024-2026: check progress on 2k-th moments, Soundararajan-Harper upper bounds). Honest question: is RMT structurally capable of being more than an instrument (conjecture-generator/calibrator), given AH-consistency of bandwidth-1 data? Is there ANY route from universality to a forcing statement?'],
  ['lorentzian-log-concavity', 'Lorentzian polynomials & log-concavity technology',
   'Branden-Huh Lorentzian polynomials, Hodge theory in combinatorics (Huh school), hyperbolic/stable polynomials, Borcea-Branden stability preservers, GORZ Jensen-polynomial hyperbolicity (proven for xi in bounded degree ranges). C1\'s design assessed this skeleton as S1-fail (consumes only archimedean moment data that DH lookalikes share) — VERIFY that assessment independently, and check whether any coupling of a multiplicative input into the Lorentzian framework has been attempted.'],
  ['free-probability-operators', 'Free probability & operator algebras',
   'Voiculescu free probability, subfactors, Haagerup\'s unpublished RH work (check what exists), free convolution models of zero statistics, Connes embedding aftermath. Weak prior — but sweep honestly: any published interface between freeness/operator-algebraic positivity and L-function zeros?'],
  ['p-adic-iwasawa', 'p-adic L-functions & Iwasawa theory',
   'Main conjectures (Mazur-Wiles, Skinner-Urban), p-adic zero distribution, trivial zeros. Precise question: does ANY p-adic structure constrain ARCHIMEDEAN zero location (via periods, integrality, p-adic interpolation of critical values)? Document the disconnect precisely if dead — that delimitation is itself valuable.'],
  ['motives-periods', 'Motives, periods, special values',
   'Beilinson conjectures, mixed motives, motivic Galois groups, Kontsevich-Zagier periods. Is there any concrete mechanism connecting motivic structure to zero LOCATION (not special values), or is this genre purely programmatic for RH? Check Deninger-adjacent motivic proposals and anything 2024-2026.'],
  ['condensed-analytic-stacks', 'Condensed mathematics & analytic stacks over Z',
   'Clausen-Scholze condensed/liquid theory and analytic stacks; their program of analytic geometry over Z (Fargues-Fontaine-style at the archimedean place); Clausen-Scholze statements about zeta meromorphic continuation via six-functor formalism (2024-2026 lectures/notes — find and verify what is actually claimed/proven). Is a Weil cohomology over Z with a Hodge-index-analogue positivity within THIS formalism\'s stated reach? What do the authors themselves name as the obstruction?'],
  ['model-theory-ominimality', 'Model theory, o-minimality, decidability',
   'Pila-Wilkie/Andre-Oort methods, Zilber pseudoexponentiation (Zilber\'s claims touching Schanuel/zeta?), continuous logic. Any leverage on zero location? Likely dead-end — but document exactly why (what would o-minimality need to see zeros, and why zeta\'s growth defeats it).'],
  ['selberg-ihara-worked-examples', 'Comparative anatomy of the TRUE RH cases',
   'The cases where RH-analogues are THEOREMS: function fields (Weil/Deligne), Selberg zetas (trace formula => spectral => analogue), Ihara/graph zetas (Ramanujan graphs), Dwork. Extract the EXACT structural-ingredient list each true case has that Riemann zeta lacks (cohomology? compactness? trace formula with both sides geometric? positivity source?). Output a spec-completion: which ingredients are jointly sufficient in every known true case — this sharpens S1-S5 or adds an S6.'],
  ['beurling-axiom-calibration', 'Beurling generalized primes: the negative space',
   'Diamond-Montgomery-Vorhauer barriers, Hilberdink, Zhang Wen-Bin?, recent Beurling literature (Broucke-Debruyne-Vindas 2020s). Which axiom sets provably FAIL to force RH (counterexample systems exist)? Output the sharpest known delimitation "these axioms admit RH-false systems" — the calibration every new-branch proposal must clear, and the exact axiom-gap between Beurling worlds and zeta.'],
  ['certified-computation-sat', 'Certified computation as proof machinery + the Lambda>0 disproof channel',
   'Polymath15 pipeline (Lambda <= 0.2 — check for post-2020 improvements), Platt-Trudgian height verification (3*10^12 — current record?), interval/ball arithmetic proof infrastructure, SAT/LP/SDP certificates in mathematics (flag algebras, Marijn Heule-style). Design question: what would a SERIOUS certified counterexample-search program look like (Rodgers-Tao: certified Lambda>0 would DISPROVE RH; Farmer arXiv:2211.11671 notes no serious search program exists) — feasibility, cost, where to look (Lehmer pairs near-degeneracies).'],
  ['arithmetic-que-microlocal', 'Arithmetic quantum ergodicity & microlocal methods',
   'Lindenstrauss AQUE/entropy methods, Anantharaman entropy bounds, Soundararajan QUE for Eisenstein series?, microlocal positivity (sharp Garding as a positivity generator?). Any transfer mechanism from eigenfunction equidistribution technology to zero-location for zeta? Verify the Eisenstein QUE <-> zeta-zeros connections (Luo-Sarnak, Jakobson) and their actual strength.'],
  ['lee-yang-stat-mech', 'Lee-Yang theory & statistical-mechanics zero theorems',
   'The Lee-Yang circle theorem is a PROVEN structural mechanism forcing all zeros of a partition function onto a critical circle/line — exactly the shape of statement RH needs. Map: Lee-Yang/Ruelle extensions, Newman\'s Lee-Yang work and its connection to de Bruijn-Newman, realizations of xi as a Lee-Yang-class partition function (Knauf spin chains, number-theoretic gases, Julia/Bost-Connes), and the total-positivity/Polya frequency function angle. Where exactly does the known Lee-Yang machinery fail to apply to xi, and is that gap theorem-shaped?'],
  ['hyperuniformity-coulomb', 'Coulomb gases, hyperuniformity, universality of log-gases',
   'Zeros as a 1D log-gas at inverse temperature beta=2: DLR equations for sine-beta (Dereudre et al), rigidity/hyperuniformity of Coulomb systems (Serfaty school 2020s), universality. Is there an unconditional bridge from log-gas rigidity theorems to constraints on the actual (deterministic) zero set? Who has tried to make "zeros are a Gibbs state" precise, and what broke?'],
]

const REPORT = {
  type: 'object', additionalProperties: false,
  required: ['branch', 'verdict', 'confidence', 'fit', 'key_objects', 'prior_attacks', 'live_entry_points', 'first_interface', 'access_failures', 'verified_online', 'recalled_unverified'],
  properties: {
    branch: { type: 'string' },
    verdict: { type: 'string', enum: ['grossmann-candidate', 'instrument', 'dead-end', 'needs-deeper-look'] },
    confidence: { type: 'number', description: '0-1 confidence in the verdict' },
    fit: { type: 'object', additionalProperties: false, required: ['S1', 'S2', 'S3', 'S4', 'S5'], properties: {
      S1: { type: 'string' }, S2: { type: 'string' }, S3: { type: 'string' }, S4: { type: 'string' }, S5: { type: 'string' },
    }, description: 'per-spec-item: score 0-5 + one-line justification' },
    key_objects: { type: 'array', items: { type: 'string' }, description: 'the branch objects/theorems that could serve the spec' },
    prior_attacks: { type: 'array', items: { type: 'string' }, description: 'every serious RH attack from this branch: who, when, citation, EXACTLY where it died (or why still alive)' },
    live_entry_points: { type: 'array', items: { type: 'string' }, description: 'current live interfaces with citations (2024-2026 verified where possible)' },
    first_interface: { type: 'string', description: 'the sharpest referee-evaluable theorem statement that would connect this branch to zeta under the spec' },
    access_failures: { type: 'array', items: { type: 'string' }, description: 'papers/resources you could NOT access (botwall/paywall/dead link) — the sponsor will fetch these manually' },
    verified_online: { type: 'array', items: { type: 'string' }, description: 'load-bearing claims you verified against tier-1 online sources this run' },
    recalled_unverified: { type: 'array', items: { type: 'string' }, description: 'load-bearing claims recalled from memory you could NOT verify online — these are NOT to be trusted until checked' },
  },
}

const scoutPrompt = (name, brief) => `You are a research scout in a Riemann Hypothesis research program executing the GROSSMANN SWEEP (sponsor standing order: exhaustively check whether an EXISTING branch of mathematics already contains the machinery an RH proof needs, before the program builds a new branch from scratch — Einstein found Riemannian geometry ready-made via Grossmann; we must not grind while the answer sits published).

YOUR BRANCH: ${name}.
BRIEF: ${brief}

READ FIRST (local files):
1. ${PROG}/STATUS.md — the program dashboard: S1-S5 spec, hard constraints, sponsor standing orders (BINDING, esp. order 5: no unverified claims presented as verified).
2. ${PROG}/results/literature.md — Aug-2026 state of the art on 12 fronts.
3. ${PROG}/results/completeness-critic.json — known portfolio gaps.
(Optionally: results/full-map.md for the base machinery; directions/ files if your brief names one.)

${SPEC}

TASK:
(1) Map the branch's candidate machinery against the spec: what objects/theorems could serve as positivity generator, spectral interpretation, or arithmetic input.
(2) PRIOR ART — MANDATORY AND ONLINE: every serious RH attack from this branch — who, when, exact citation, and precisely where it died (or why it is still alive). Use WebSearch and WebFetch (load them via ToolSearch if not yet available) on arXiv and journals; verify the 2024-2026 state of the art — do not rely on memory for anything load-bearing. In your report, strictly separate VERIFIED-online claims from RECALLED-unverified ones.
(3) ACCESS FAILURES: if a paper/resource is unreachable (botwall, paywall, dead link), record it in access_failures with enough detail for the sponsor to fetch it manually. NEVER silently substitute memory for an inaccessible source.
(4) Score fit S1-S5 (0-5 each with a one-line justification).
(5) VERDICT: 'grossmann-candidate' (machinery substantially exists and fits the spec — the program should build the interface NOW), 'instrument' (useful input to existing directions, not a proof engine), 'dead-end' (provably or historically exhausted — state exactly why), 'needs-deeper-look' (could not determine — state exactly what is missing, e.g. an inaccessible source).
(6) first_interface: the sharpest CONCRETE, referee-evaluable theorem statement that would connect this branch to zeta under the spec.

Honesty calibration: a false 'grossmann-candidate' costs a design cycle; a false 'dead-end' could miss the answer — when genuinely torn, prefer 'needs-deeper-look' with the missing datum named. The DH/Epstein filter is always the first test: does the branch's proposed input distinguish zeta from RH-false lookalikes at the AXIOM level? Return via StructuredOutput.`

const SYNTH = {
  type: 'object', additionalProperties: false,
  required: ['shortlist', 'instruments', 'dead_ends', 'needs_sponsor_fetch', 'unswept_corners', 'sweep_verdict'],
  properties: {
    shortlist: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['branch', 'why', 'next_action'], properties: {
      branch: { type: 'string' }, why: { type: 'string' }, next_action: { type: 'string' } } }, description: 'grossmann-candidates ranked: strongest spec-fit first' },
    instruments: { type: 'array', items: { type: 'string' }, description: 'branch -> which existing direction it feeds' },
    dead_ends: { type: 'array', items: { type: 'string' }, description: 'branch -> one-line reason (for the no-go library)' },
    needs_sponsor_fetch: { type: 'array', items: { type: 'string' }, description: 'ALL access_failures aggregated across scouts, deduped, with why each matters' },
    unswept_corners: { type: 'array', items: { type: 'string' }, description: 'branches of mathematics NOT covered by the 24 scouts that plausibly deserve a scout — the sweep is only done when this list is empty or justified' },
    sweep_verdict: { type: 'string', description: 'the decisive summary: does an existing branch fit (Grossmann found), or does the program proceed to de novo construction (Weil mode)? 200-400 words' },
  },
}

phase('Sweep')
const reports = await parallel(BRANCHES.map(([key, name, brief]) => () =>
  agent(scoutPrompt(name, brief), { label: `sweep:${key}`, phase: 'Sweep', schema: REPORT, effort: 'high' })
))
const ok = reports.filter(Boolean)
log(`Sweep complete: ${ok.length}/${BRANCHES.length} scouts returned (${BRANCHES.length - ok.length} dropped)`)

phase('Synthesize')
const synthesis = await agent(`You are the SYNTHESIZER of the Grossmann sweep in an RH research program. ${BRANCHES.length} scouts each fitted one existing branch of mathematics against the S1-S5 spec below. Their full reports are appended. Read ${PROG}/STATUS.md (sponsor standing orders + spec) and ${PROG}/results/completeness-critic.json first.

${SPEC}

Produce: (1) the ranked SHORTLIST of grossmann-candidates (strongest spec-fit first — judge on the actual S1-S5 scores and the concreteness of the first_interface, not scout enthusiasm; demote any candidate whose case rests on recalled_unverified claims); (2) instruments mapped to the existing directions they feed (survivors: A3, B2, B3, B4, C2, A2/A4 pending); (3) dead-ends with reasons (for the program's no-go library); (4) needs_sponsor_fetch: aggregate and dedupe ALL access_failures, with why each matters; (5) unswept_corners: what parts of mathematics did the 24-branch grid MISS that plausibly deserve a scout (be adversarial — the sponsor's order is EVERY corner); (6) the sweep verdict: is there a Grossmann (existing machinery to build on now), or does the program proceed to de novo construction — and if de novo, which sweep findings become its raw material. Return via StructuredOutput.

SCOUT REPORTS:
${JSON.stringify(ok)}`, { label: 'synthesize', phase: 'Synthesize', schema: SYNTH })

return { reports: ok, synthesis, dropped: BRANCHES.length - ok.length }
