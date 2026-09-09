export const meta = {
  name: 'd1-lane-a-3d-s19',
  description: 'D1 M2a Lane A phase 3(d): emit the two literals into Lean, kernel-check, replace hLaneA, print axioms, F-5 bookkeeping; then an independent Opus audit',
  phases: [
    { title: 'Emit', detail: 'Fable emitter: literals, back-parse, kernel check, replacement, axioms, bookkeeping' },
    { title: 'Audit', detail: 'Opus independent checker from a clean build' },
  ],
}
const ROOT = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const LA = `${ROOT}/results/d1-m2a/lane-a`
const LEAN = '/Users/jaytyagi/rh-lean-work/zeta-23-lean-main'
const COMMON = `Repository "${ROOT}" (path has spaces — quote it everywhere). Lean tree "${LEAN}". Read "${LA}/BRIEF-3d.md" first and follow it exactly, then the authorities it lists in order. Thermal policy: one lake build at a time, no producers, check pgrep before anything heavy. Write every deliverable to disk under "${LA}/" as you go; return only a verdict, paths, and a summary of at most 8000 characters.`
const OUT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['DONE', 'BLOCKED', 'CLEAN', 'FIX-FIRST'] },
    paths: { type: 'string', maxLength: 2000 },
    summary: { type: 'string', maxLength: 8000 },
  },
  required: ['verdict', 'paths', 'summary'],
}
phase('Emit')
const emit = await agent(`${COMMON}\n\nYou are the EMITTER (Job 1 of the brief).`, { label: 'emit', phase: 'Emit', schema: OUT, effort: 'max' })
log(`emit → ${emit ? emit.verdict : 'null'}`)
if (!emit || emit.verdict !== 'DONE') return { emit }
phase('Audit')
const audit = await agent(`${COMMON}\n\nYou are the AUDITOR (Job 2 of the brief; second model, independent checker). Emitter summary for context:\n---\n${emit.summary}\n---`, { label: 'audit', phase: 'Audit', schema: OUT, model: 'opus', effort: 'max' })
log(`audit → ${audit ? audit.verdict : 'null'}`)
let emit2 = null
if (audit && audit.verdict === 'FIX-FIRST') {
  emit2 = await agent(`${COMMON}\n\nYou are the EMITTER again. The auditor returned FIX-FIRST; its report is "${LA}/AUDIT-3d.md" (summary: ${audit.summary.slice(0, 4000)}). Apply every fix you verify to be right (say why for any you reject), rebuild, re-print axioms, update EMIT-NOTES.md with a dated block.`, { label: 'emit-fix', phase: 'Audit', schema: OUT, effort: 'max' })
  log(`emit-fix → ${emit2 ? emit2.verdict : 'null'}`)
}
return { emit: emit.verdict, audit: audit && audit.verdict, fix: emit2 && emit2.verdict }
