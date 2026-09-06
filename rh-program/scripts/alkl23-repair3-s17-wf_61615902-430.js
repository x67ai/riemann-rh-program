export const meta = {
  name: 'alkl23-repair3-s17',
  description: 'Apply the xcheck adjudication to alkl23-note (N1–N11) and the companion (C1–C9, sendable derivations PDF), rebuild, fresh-reader check of changed lines',
  phases: [
    { title: 'Repair', detail: 'one Fable agent edits note + companion, builds both PDFs' },
    { title: 'Verify', detail: 'one Opus fresh reader checks only the changed lines' },
    { title: 'Fix', detail: 'only if the verifier says FIX-FIRST: repairer applies its list, verifier re-reads' },
  ],
}

const ROOT = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const S14 = `${ROOT}/results/c3-r/s14`
const X = `${S14}/xcheck-s17`

const COMMON = `Repository "${ROOT}" (the path has spaces — quote it everywhere). TeX: export PATH="$HOME/texlive/2026/bin/universal-darwin:$PATH"; build with pdflatex, twice. Files: the note "${S14}/alkl23-note.tex" (+ .pdf), the companion "${S14}/alkl23-note-derivations.md", the adjudication "${X}/adjudication.md" (its §Recommendation carries replacement LaTeX items 1–11 and the companion list C1–C9; its §A/§B/§C give the reasons), the twelve referee reports "${X}/{refute,verify}-*.md", the published paper text "${S14}/novelty/ALKL-2024-published.txt". Every fact you change must be checked against the published text or a live web query; do not trust a report's quote without opening the page. U.S. English. Write to disk as you go; commit nothing (watchdogs commit). Return only a one-line verdict, paths, and a summary of at most 8000 characters.`

const OUT = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['DONE', 'SEND', 'FIX-FIRST', 'BLOCKED'] },
    paths: { type: 'string', maxLength: 2000 },
    summary: { type: 'string', maxLength: 8000 },
  },
  required: ['verdict', 'paths', 'summary'],
}

const repairPrompt = `${COMMON}

You are the REPAIRER. Tasks, in order; append a dated entry per task to "${X}/repair3-log.md" as you go.
1. Read adjudication.md in full (all sections). Then read the note .tex in full.
2. Apply to the note EXACTLY the replacement text of §Recommendation items 1–11, choosing for item 1 the "companion attached" variant (the derivations will accompany the note). Item 9's optional clauses: apply both. Item 11: apply the bibliography entry AND the "arXiv p." relabeling at every memoir page citation AND the one clause in §2 or §5 that the restatements are presumably now in print in ch. 2 of the book. Update the date in the \\date line and in §5 to today if you change §5's date. Before each edit, assert the old string is present exactly once (grep -c); after all edits, diff against git HEAD and list every changed line in the log.
3. Companion: create a SENDABLE derivations document. Copy alkl23-note-derivations.md to a working file, apply C1–C9 (and C7's "int K ≠ ∅"), strip the internal apparatus (the program header line, every "(adjudication)" tag, §12's sourcing line, §13 "Deviations from the brief"; replace §12 with the same public-record paragraph as the note's §5), and convert it to LaTeX as "${S14}/alkl23-derivations.tex" with the same preamble/author/AI-use footnote as the note and the title "Derivations accompanying 'A note on the topology-coincidence statements in Topology of the space of conormal distributions'". Convert the math faithfully (the .md uses Unicode math; produce real LaTeX). Keep the §0 page-anchor table (fix C9 there) — it is useful to the authors. Build "${S14}/alkl23-derivations.pdf". Also keep the internal .md in place but apply C1–C9 to it too (dated "[corrected 2026-09-06 per xcheck-s17]" tags are fine there, not in the .tex).
4. Rebuild "${S14}/alkl23-note.pdf". Both builds must be warning-free on overfull boxes worse than 10pt and error-free; run pdftotext on both PDFs and grep the changed passages to confirm they rendered (bold x, breve M, primes, the \\eqref).
5. Record in the log: page counts, every changed line of the note, the list of companion changes, any place where you deviated from the adjudication's wording and why.
Return DONE with the paths, or BLOCKED with what blocked you.`

const verifyPrompt = (rep) => `${COMMON}

You are the FRESH READER (second model). The repairer reports:
---
${rep ? rep.summary : '(no summary — read the log)'}
---
Read "${X}/repair3-log.md", then "git -C '${ROOT}' diff HEAD~3 -- results/c3-r/s14/alkl23-note.tex" (widen the range until you see the whole repair diff; the autocommit watchdog may have committed in between — use "git log --oneline -8 -- results/c3-r/s14/alkl23-note.tex" to find the pre-repair commit and diff against it). Check ONLY the changed lines of the note, but check each one three ways: (i) against the adjudication's replacement text (was it applied faithfully, with the "companion attached" variant of item 1?), (ii) against the published paper text for every number, page and quoted phrase in the changed line, (iii) as rendered: pdftotext the new alkl23-note.pdf and read the rendered sentences — glyph-sensitive symbols (bold x, breve M, primes, the \\eqref number, ρ bounds) must be right; the last two edit rounds each introduced one glyph error. Then read alkl23-derivations.pdf END TO END once (it is new): every formula must be a faithful conversion of the .md, C1–C9 must be applied, no internal apparatus may remain, and the mathematics in §9 (Lemma A, Lemma B, Prop. 9.4, §9.5) must read correctly after conversion — recompute the two exponent identities from the rendered text. Write "${X}/verify3-O.md" with a table of every changed line (OK / FIX with the exact fix) and a section on the derivations PDF. Verdict SEND (nothing to fix) or FIX-FIRST (list the fixes, exact old → new).`

phase('Repair')
const rep = await agent(repairPrompt, { label: 'repair', phase: 'Repair', schema: OUT, effort: 'max' })
log(`repair → ${rep ? rep.verdict : 'null'}`)
if (!rep || rep.verdict === 'BLOCKED') return { repair: rep }

phase('Verify')
let ver = await agent(verifyPrompt(rep), { label: 'verify3', phase: 'Verify', schema: OUT, model: 'opus', effort: 'max' })
log(`verify3 → ${ver ? ver.verdict : 'null'}`)

let rounds = 0
while (ver && ver.verdict === 'FIX-FIRST' && rounds < 2) {
  rounds++
  phase('Fix')
  const fix = await agent(`${COMMON}

You are the REPAIRER, round ${rounds + 1}. The fresh reader's verdict was FIX-FIRST; its report is "${X}/verify3-O.md" and its summary:
---
${ver.summary}
---
Apply exactly the listed fixes (assert each old string exists once; verify each against the published text yourself before applying — if a "fix" is itself wrong, do not apply it and say why in the log). Rebuild both PDFs, pdftotext-check the fixed lines, append to "${X}/repair3-log.md". Return DONE.`, { label: `fix-${rounds}`, phase: 'Fix', schema: OUT, effort: 'max' })
  log(`fix-${rounds} → ${fix ? fix.verdict : 'null'}`)
  ver = await agent(`${COMMON}

You are the FRESH READER again (round ${rounds + 1}). Your previous report is "${X}/verify3-O.md"; the repairer's round-${rounds + 1} entry is at the end of "${X}/repair3-log.md" (summary: ${fix ? fix.summary.slice(0, 3000) : '-'}). Re-check ONLY the lines fixed in this round, the same three ways (adjudication text, published text, rendered PDF via pdftotext), append a dated round section to verify3-O.md, and give the verdict SEND or FIX-FIRST.`, { label: `verify3-r${rounds + 1}`, phase: 'Fix', schema: OUT, model: 'opus', effort: 'max' })
  log(`verify3 round ${rounds + 1} → ${ver ? ver.verdict : 'null'}`)
}
return { repair: rep && rep.verdict, verify: ver && ver.verdict, rounds, summary: ver && ver.summary }