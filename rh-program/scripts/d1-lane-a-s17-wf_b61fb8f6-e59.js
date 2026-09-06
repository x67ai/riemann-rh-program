export const meta = {
  name: 'd1-lane-a-s17',
  description: 'D1 M2a Lane A: plan + price the P-9/P-10 producers, Opus plan review, then (on GO) build the Lean checker and launch the producers detached',
  phases: [
    { title: 'Plan', detail: 'Fable planner: statement shapes, measured pricing, GO/NO-GO' },
    { title: 'Review', detail: 'Opus review of the plan' },
    { title: 'Build', detail: 'Lean checker (Asym.lean) and detached producer launch' },
  ],
}

const ROOT = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const LA = `${ROOT}/results/d1-m2a/lane-a`
const LEAN = '/Users/jaytyagi/rh-lean-work/zeta-23-lean-main'

const COMMON = `Repository "${ROOT}" (path has spaces — quote it everywhere). Read "${LA}/BRIEF.md" first and follow it exactly, then the authorities it lists, in order. Lean tree: "${LEAN}". Thermal policy is binding (≤ 4 heavy jobs; lake build -j2; check pgrep before starting anything heavy). Write every deliverable to disk under "${LA}/" as you go, in chunks; return only a verdict, paths, and a ≤ 8000-character summary.`

const OUT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['GO', 'NO-GO', 'DONE', 'BLOCKED', 'APPROVED', 'REVISE'] },
    paths: { type: 'string', maxLength: 2000 },
    summary: { type: 'string', maxLength: 8000 },
  },
  required: ['verdict', 'paths', 'summary'],
}

phase('Plan')
const plan = await agent(`${COMMON}

You are the PLANNER ("price first, batch, never shrink"). Write "${LA}/PLAN.md" with these sections, each complete before you start the next:
1. **Statements.** From SPEC §5, §7.4, §8.3 and GLUE-NOTES: the exact \`hLaneA\` statement now displayed (quote from Instance02.lean); the \`AsymData\` structure and the checks C-A1…C-A6 of \`checkAsym\`; the statement of \`cert_of_checkAsym\` (the soundness theorem) and of L-A1 (N(X+1) ≥ N_start from a rational π bound) and L-A2 (windowIdx monotone); the proof plan of \`cert_of_checkAsym\` per SPEC §5.6, with every Mathlib name it needs verified to exist in the pinned Mathlib (grep the .lake/packages/mathlib tree; list name → file). State precisely how \`cert_of_checkAsym\` on the literal yields (ii′) in the form \`hLaneA\` consumes it, so the replacement in \`lambda_le_point2\` is a one-line substitution.
2. **Producers.** What P-9 (window rows: mollified triangle-inequality floor T uniform on the window × y-range, Theorem 1.3 defect E at the worst corner) and P-10 (tail row: Q₁…Q₄, E₁ upper bounds with directed rounding, (S1)–(S4)) compute per window, with the formulas cited to SPEC line numbers; the window count N₁ and its derivation (SPEC C-A5; the "N₁ ≈ 6–8·10⁶ with the crude Lemma T" figure in STATUS — recompute it, and say whether a sharper admissible Lemma T in SPEC reduces it; never shrink the spec's requirement). The literal's size in Lean (bytes, and whether \`decide +kernel\` on it is feasible — compare with Lane B's 883-prism literal and RUN-REPORT §5's measured costs; if infeasible as one literal, the SPEC's batching/aggregation provision, cited).
3. **Pricing, measured.** Write the two producers as scripts under "${LA}/" (\`p9_mp.py\`, \`p9_arb.py\` or a single script with two legs, reusing ft_mp.py conventions; Arb via python-flint or the existing arb-cache toolchain — check what Lane B used in arb-leg-notes.md and reuse it), with batch checkpointing (\`batches/batch_<k>.json\`), a \`--resume\` switch, and \`STATUS.json\` updates per batch. Run a small batch (e.g. 200 windows spread across the range, plus the tail row) on both legs, cross-check per row, and record windows/hour per leg, memory, and the projected wall-clock for N₁ under the thermal cap. Record the exact command lines.
4. **GO/NO-GO.** GO if the projection is ≤ 48 h of wall-clock under the cap and the literal is kernel-checkable (possibly batched); otherwise NO-GO with the cheapest admissible alternative from the SPEC (e.g. the tail decision of §11, or a coarser-but-admissible T). Do NOT launch the full run; do NOT edit the Lean tree. Return GO or NO-GO.`, { label: 'plan', phase: 'Plan', schema: OUT, effort: 'max' })
log(`plan → ${plan ? plan.verdict : 'null'}`)
if (!plan || plan.verdict === 'BLOCKED') return { plan }

phase('Review')
const review = await agent(`${COMMON}

You are the REVIEWER (second model). Read "${LA}/PLAN.md" in full, then check every claim in its §1 against SPEC §5/§7.4/§8.3 and GLUE-NOTES and against the Lean tree (open Instance02.lean and Defs.lean; verify each Mathlib name the plan lists actually exists at the pinned revision); re-derive the window count in §2 from SPEC C-A5; re-run ONE small batch (≤ 50 windows) with the planner's scripts to confirm the measured rate and the cross-check; check the GO/NO-GO arithmetic. The statement shapes are trust-critical: any mismatch between \`cert_of_checkAsym\`'s conclusion and what \`lambda_le_point2\` consumes as \`hLaneA\` is a REVISE. Write "${LA}/PLAN-REVIEW.md" (table: claim / verified how / OK or FIX with the fix). Planner summary for context:
---
${plan.summary}
---
Return APPROVED (possibly with non-blocking notes) or REVISE (with the exact list).`, { label: 'review', phase: 'Review', schema: OUT, model: 'opus', effort: 'max' })
log(`review → ${review ? review.verdict : 'null'}`)

let plan2 = plan
if (review && review.verdict === 'REVISE') {
  plan2 = await agent(`${COMMON}

You are the PLANNER again. The reviewer returned REVISE; its report is "${LA}/PLAN-REVIEW.md" (summary: ${review.summary.slice(0, 4000)}). Apply every fix you verify to be right (say why for any you reject), update PLAN.md in place with a dated revision block, and re-state GO/NO-GO.`, { label: 'plan-rev', phase: 'Review', schema: OUT, effort: 'max' })
  log(`plan revision → ${plan2 ? plan2.verdict : 'null'}`)
}
if (!plan2 || plan2.verdict !== 'GO') return { plan: plan2, review }

phase('Build')
const build = await agent(`${COMMON}

You are the BUILDER. PLAN.md is GO and reviewed (PLAN-REVIEW.md). Two jobs, sequential:
(A) Lean: create "${LEAN}/Zeta23/DBN/Asym.lean" with \`AsymData\`, \`checkAsym\` (C-A1…C-A6), \`cert_of_checkAsym\`, L-A1, L-A2 exactly as PLAN.md §1 specifies (no sorry; if a proof does not close within your budget, leave the theorem OUT and record it in "${LA}/BUILD-NOTES.md" as owed — never a sorry, never an axiom). Add the import to the DBN module list only. \`lake build -j2 Zeta23.DBN.Asym\`, then \`#print axioms\` on every new theorem into "${LA}/asym-axioms.log". Do NOT touch Instance02.lean yet (the replacement waits for the literal).
(B) Producers: launch the full P-9/P-10 run exactly with the command lines in PLAN.md §3, DETACHED (nohup, setsid, output under "${LA}/batches/", log "${LA}/producers.log", "${LA}/STATUS.json" updated per batch with {phase, windows_done, windows_total, started, updated, eta_hours, errors}), respecting the thermal cap (count your lake build as heavy while it runs). Verify after 2–3 minutes that batches are landing and STATUS.json updates; record PIDs and the resume command in BUILD-NOTES.md. Return DONE with paths, or BLOCKED.`, { label: 'build', phase: 'Build', schema: OUT, effort: 'max' })
log(`build → ${build ? build.verdict : 'null'}`)
return { plan: plan2 && plan2.verdict, review: review && review.verdict, build }