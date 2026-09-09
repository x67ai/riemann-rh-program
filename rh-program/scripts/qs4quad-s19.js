export const meta = {
  name: 'qs4quad-s19',
  description: 'Q-S4 quad literature decision: two scouts (Fable, Opus) on clause (S) semiproperness + face (a), then a binding adjudicator',
  phases: [
    { title: 'Scouts', detail: 'Fable and Opus scouts, independent, literature only' },
    { title: 'Adjudicate', detail: 'Fable adjudicator, binding, refutation-shaped' },
  ],
}
const ROOT = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const D = `${ROOT}/results/c3-r/s19/qs4quad`
const COMMON = `Repository "${ROOT}" (path has spaces — quote it everywhere). Read "${D}/BRIEF.md" first and follow it exactly; then the digest "${ROOT}/results/c3-r/s19/insights-digest.md" sections G, I, J; then the sources it names, on disk. Nothing from memory; vision-verify garbled text layers (corpus-routing caveat 21). Standing order 6: literature decision only, no construction. Write every deliverable to disk in chunks as you go; append progress to "${ROOT}/results/c3-r/s19/SHARED.md". Return only a verdict, paths, and a summary of at most 8000 characters.`
const OUT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['PRINTED-YES', 'PRINTED-NO', 'OPEN-NAMED', 'MIXED', 'BLOCKED'] },
    paths: { type: 'string', maxLength: 2000 },
    summary: { type: 'string', maxLength: 8000 },
  },
  required: ['verdict', 'paths', 'summary'],
}
phase('Scouts')
const [F, O] = await parallel([
  () => agent(`${COMMON}\n\nYou are SCOUT F. Write "${D}/scout-F.md" per the brief's deliverable spec (sections 0–6; the refutation-shaped close is mandatory). Do not open scout-O.md.`, { label: 'scout-F', phase: 'Scouts', schema: OUT, effort: 'max' }),
  () => agent(`${COMMON}\n\nYou are SCOUT O (second model). Write "${D}/scout-O.md" per the brief's deliverable spec (sections 0–6; the refutation-shaped close is mandatory). Do not open scout-F.md.`, { label: 'scout-O', phase: 'Scouts', schema: OUT, model: 'opus', effort: 'max' }),
])
log(`scouts → F ${F ? F.verdict : 'null'} / O ${O ? O.verdict : 'null'}`)
phase('Adjudicate')
const adj = await agent(`${COMMON}\n\nYou are the ADJUDICATOR. Read "${D}/scout-F.md" and "${D}/scout-O.md" in full. Re-derive every disagreement from the cited pages yourself (open the PDFs). Write "${D}/adjudication.md" per the brief: binding verdict on clause (S) and on face (a) in the refutation shape; proposed ledger block §16-sexies; a zoo entry in the IV.13 format if a kill; the next decidable question or the named-open-problem closure. Scout summaries for context:\n--- F ---\n${F ? F.summary : 'missing'}\n--- O ---\n${O ? O.summary : 'missing'}\n---`, { label: 'adjudicate', phase: 'Adjudicate', schema: OUT, effort: 'max' })
log(`adjudication → ${adj ? adj.verdict : 'null'}`)
return { F: F && F.verdict, O: O && O.verdict, adjudication: adj }
