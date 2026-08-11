export const meta = {
  name: 'rh-understand',
  description: 'Deep-read the zeta-2/3 paper + Lean formalization to map the method, its exact limits, and extension hooks',
  phases: [
    { title: 'Understand', detail: 'parallel readers over papers and Lean subsystems' },
  ],
}

const ROOT = '/Users/jaytyagi/Documents/Work/2026/Math/riemann/anthropic'
const LEAN = ROOT + '/zeta-23-lean-main'

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['summary', 'key_items', 'bandwidth_role', 'limitations', 'extension_hooks'],
  properties: {
    summary: { type: 'string', description: 'Dense 2-4 paragraph technical summary of what this source contains' },
    key_items: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        required: ['name', 'statement', 'where'],
        properties: {
          name: { type: 'string' },
          statement: { type: 'string', description: 'precise mathematical content, with constants' },
          where: { type: 'string', description: 'file path or page number' },
        },
      },
    },
    bandwidth_role: { type: 'string', description: 'Exactly where and how the length/bandwidth limitation of Dirichlet polynomials or test-function support enters this material; N/A if it does not' },
    limitations: { type: 'array', items: { type: 'string' }, description: 'What this method/material provably or plausibly CANNOT do, incl. any stated obstructions' },
    extension_hooks: { type: 'array', items: { type: 'string' }, description: 'Concrete places where new mathematics could plug in: a lemma that could be strengthened, a parameter that could be pushed, a structure that generalizes' },
  },
}

const COMMON = `You are a research mathematician (analytic number theory + Lean 4/Mathlib) analyzing a research artifact: a complete, sorry-free Lean 4 formalization of the paper "More than two thirds of the zeros of the Riemann zeta function lie on the critical line" (2026). Root: ${ROOT}. Lean repo: ${LEAN}. First read ${LEAN}/README.md (skim) for orientation.
Your job is NOT summary for a lay reader — it is reconnaissance for a follow-up research program whose goal is to design genuinely novel methods toward proving or refuting RH itself. So: extract exact statements, exact constants, exact hypotheses, and above all the PRESSURE POINTS — where the method saturates, why, and what structures would have to change to go further. Be precise and skeptical. Return via StructuredOutput.`

const readers = [
  {
    label: 'read:paper-method',
    prompt: `${COMMON}

Read the condensed paper ${ROOT}/zeta-two-thirds-condensed.pdf (all 5 pages) and the full paper ${ROOT}/zeta-two-thirds.pdf pages 1-18 (use the Read tool with pages parameter).
Map the METHOD end-to-end: how does the argument go from Weil's explicit formula to a Gram/overlap matrix, to the rank-trace inequality (Lemma R), to the 2/3 and Montgomery-Taylor constants? What is the certificate (c0, r)? What is the variational problem of Theorem D and its optimizer? Identify exactly which analytic input limits the test-function support/bandwidth to 1 (Montgomery-Vaughan? diagonal-only evaluation?). Record every headline constant and its formula.`,
  },
  {
    label: 'read:paper-limits',
    prompt: `${COMMON}

Read the full paper ${ROOT}/zeta-two-thirds.pdf pages 16-35 (use the Read tool with pages parameter; overlap with earlier pages is fine).
Focus on: the prime side (Gram matrix traces, Montgomery-Vaughan), the zero side (block structure, tail bounds), the assembly (§6), any remarks on OPTIMALITY, the bandwidth-one ceiling / appendix material, the xi-prime results, and anything the authors say about what would be needed to go beyond 2/3 or toward RH. Extract the exact form of the ceiling statement (0.6818... cap for bandwidth-one certificates) and precisely what class of arguments it rules out — and, crucially, what it does NOT rule out.`,
  },
  {
    label: 'read:transcript',
    prompt: `${COMMON}

The file ${ROOT}/zeta-transcript-explanation.pdf (95 pages) appears to explain the discovery process / transcript behind the result. Read pages 1-20 first to understand its structure, then selectively read the most relevant further page ranges (up to ~60 pages total, in <=20-page chunks) prioritizing: any discussion of failed approaches, dead ends, obstructions encountered, ideas considered but not pursued, and any stated next steps or open problems. These are gold for designing the follow-up program. Report what the document is, and extract every forward-looking or negative result you find.`,
  },
  {
    label: 'lean:ceiling',
    prompt: `${COMMON}

Read the Lean sources under ${LEAN}/Zeta23/PairCeiling/ (all files: Defs, Stability, NearCUE, RowCert, LawN256, CeilingLaw256, Signed - list the dir first) plus any docstrings referencing the ceiling. Also grep the repo for 'ceiling' and 'bandwidth'.
Extract: the exact formal definition of a bandwidth-one certificate; the stability inequality ceiling_stability with all hypotheses; the LawN256 construction (what is the 256-periodic near-CUE law, what does EnclOK assume, what was computed outside Lean); and the exact cap statement (0.6818287 + error terms). State precisely the logical form: FOR ALL certificates of type X valid against configuration class Y, certified proportion <= Z. What are X and Y formally? What natural strengthenings of X (higher bandwidth, different functionals, multi-linear forms) fall OUTSIDE the ceiling's scope?`,
  },
  {
    label: 'lean:certificate',
    prompt: `${COMMON}

Read ${LEAN}/Zeta23/Statement.lean, ${LEAN}/Zeta23/Defs.lean, the files under ${LEAN}/Zeta23/LinAlg/ and ${LEAN}/Zeta23/ZeroSide/ (list dirs first; prioritize the rank-trace inequality 'Lemma R', Sylvester inertia, Cauchy-Schwarz count, the multiplicity-aware zero side Mult.lean, TightMult.lean).
Extract: the formal certificate structure (what data, what inequalities); how zeros on/off the line enter as 'atoms' and 'pair-blocks'; the tightness theorem lemmaR_tight and exactly what it says about improvability; how multiplicity is handled (c=2 vs c=3). Assess: which parts of this linear-algebra layer are generic (reusable against ANY operator/quadratic-form situation, e.g. a future Hilbert-Polya-type or higher-bandwidth setup) vs specific to this argument?`,
  },
  {
    label: 'lean:analytic',
    prompt: `${COMMON}

Read (list dirs first, then prioritize): ${LEAN}/Zeta23/WeilEF/ and ${LEAN}/Zeta23/ExplicitFormula.lean (Weil explicit formula as formalized - exact statement, test function class), ${LEAN}/Zeta23/MV/ (Montgomery-Vaughan generalized Hilbert inequality - exact form), ${LEAN}/Zeta23/PrimeSideA/ and PrimeSideB/ (Gram matrix traces; where polynomial length is constrained), ${LEAN}/Zeta23/ThmD/Functional.lean (the variational problem), ${LEAN}/Zeta23/Taper.lean or Taper/, ${LEAN}/Zeta23/Poisson.lean.
Extract: the exact class of test functions the formalized explicit formula accepts; the exact MV inequality proved; where in PrimeSide the 'bandwidth <= 1' constraint bites (which lemma fails for longer polynomials and why - off-diagonal terms?); the exact variational functional of ThmD and the Montgomery-Taylor optimizer. Assess reusability of each component for OTHER approaches (Weil positivity criterion, Li coefficients, pair correlation with larger support, moments).`,
  },
]

phase('Understand')
const results = await parallel(readers.map(r => () =>
  agent(r.prompt, { label: r.label, phase: 'Understand', schema: SCHEMA })
))

const out = {}
readers.forEach((r, i) => { out[r.label] = results[i] })
return out