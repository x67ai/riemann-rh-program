export const meta = {
  name: 'd1-audit-m2a-s14',
  description: 'D1: the M1 v1 adversarial audit that Session 8 never ran (two independent auditors, one Opus 5), reconcile, then build M2a (barrier certificate format + Lean checker + two f_t producers + Instance02 at the Platt–Trudgian row) and run Gomila screen steps 3–4',
  phases: [
    { title: 'Audit', detail: 'two independent standing-order-5 audits of results/d1-m1 (Fable + Opus 5)' },
    { title: 'Reconcile', detail: 'merge to AUDIT.md + RUN-REPORT.md; apply small repairs; gate' },
    { title: 'Spec', detail: 'M2a barrier-certificate contract (SPEC.md + schema)' },
    { title: 'Build', detail: 'BarrierCert.lean checker+soundness; Arb and mpmath-ball f_t producers' },
    { title: 'Instance', detail: 'Instance02 at the Polymath15 row 2 / PT pairing; Gomila steps 3–4' },
    { title: 'Final audit', detail: 'adversarial re-verification of everything built' },
  ],
}

const RH = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const LEAN = '/Users/jaytyagi/rh-lean-work/zeta-23-lean-main'

const COMMON = `You are an implementation/verification agent in the RH research program (Session 14, 2026-09-02), direction D1 — the certified refutation arm.
Program root (the path contains SPACES; always quote it in shell): ${RH}
Lean working tree (space-free, toolchain hot, full library built 2026-09-02): ${LEAN}  — Lean 4 v4.33.0-rc2, lake on PATH via 'export PATH="$HOME/.elan/bin:$PATH"'. Build ONLY targeted modules ('lake build Zeta23.DBN.Defs' etc.), never the whole library; ONE lake process at a time (lake does not lock its build directory). This program's own Lean files are the eight under '${RH}/lean/Zeta23/' (README there); the working tree carries the same files plus upstream Zeta23. Any new or changed program file is copied back to '${RH}/lean/Zeta23/<same path>' with the program's header (Copyright 2026 Kunal Tyagi, Apache-2.0 — copy an existing header) and the lean/README.md table updated.
BINDING RULES (STATUS.md standing orders + KICKSTART.md):
- Standing order 5: nothing load-bearing from memory. Every mathematical bound you implement (approximation error terms, tail bounds, mesh criteria) is DERIVED in your deliverable with the derivation checkable, or quoted from an on-disk source with exact page. On disk: Polymath15, 'Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn–Newman constant' = 'fetched/p3-22a4-polymath15-2019-upper-bound-debruijn-newman.pdf' (arXiv version) and 'fetched/p3-22a5-polymath15-2019-upper-bound-published-forum-pi.pdf' (published, Forum Math. Pi); Platt–Trudgian, RH true to height 3 000 175 332 800 = 'fetched/p3-22a1-platt-trudgian-2020-rh-true-up-to-3e12.pdf'; Rodgers–Tao = 'fetched/p3-22a3-...pdf'. Read 'results/corpus-routing.md' caveat 9 (the Λ bracket of record is 0 ≤ Λ ≤ 0.2 by Platt–Trudgian Cor. 2; never write 'Λ < 0.2').
- THERMAL POLICY (binding): at most 2 concurrent heavy local processes for YOU (other agents share the machine; the machine-wide cap is 4). Heavy = anything pegging a core for minutes: mpmath/flint sweeps, lake builds. Batch, don't shrink. python3 has mpmath 1.3.0 and python-flint 0.6.0 (see 'results/d1-m1/arb-leg-notes.md' for what worked).
- Trust vocabulary (D-R3/D-R8): producers are UNTRUSTED by design; the Lean side is 'kernel-checked modulo displayed hypotheses'; never 'fully machine-checked'. No 'native_decide'; 'decide +kernel' over integer data, the NumericCert/RowCert/W1 discipline.
- U.S. English. Honest reporting: a failure is reported as a failure; a partial build is labeled partial with the cut line stated.
- Read first: 'directions/D1-certified-refutation-arm.md' (FIRST DELIVERABLE, milestone ladder, D-R2/D-R3/D-R8, Current frontier), 'results/d1-m0/m2a-m2b-design.md' (all of it — §1.3 statement skeleton, §1.6 work breakdown, §4 enclosure conventions, §7 the Defs.lean deviation record), 'results/d1-m1/FORMAT.md', 'results/d1-m1/acceptance-report.md', '${LEAN}/Zeta23/DBN/Defs.lean', '${LEAN}/Zeta23/W1/{Format,Checker,Soundness}.lean', 'results/d1-m0/gomila-screen.md'.
- Your final text return is data for the orchestrator, not prose. Write deliverables to disk as you go.`

const AUDIT_SCHEMA = {
  type: 'object', required: ['verdict', 'fatals', 'majors', 'summary', 'file'],
  properties: { verdict: { enum: ['clean', 'repairs-proposed', 'defects', 'fatal'] }, fatals: { type: 'integer' }, majors: { type: 'integer' },
    summary: { type: 'string', maxLength: 5000 }, file: { type: 'string' }, gomila_unblock: { type: 'string', maxLength: 1500 } },
}

function auditBrief(tag) {
  return `${COMMON}

TASK — the standing-order-5 ADVERSARIAL AUDIT of everything Session 8 built in 'results/d1-m1/' (M1 v1: W1 transcript contract, mpmath-ball leg, Arb leg, acceptance suite, and the Lean W1 layer). This audit was scheduled in Session 8 and never ran (usage-limit death); it is the gate on everything D1 builds next. You are auditor ${tag} of two independent auditors (the other is a different model; assume nothing about their findings). Assume the implementers made errors and hunt them.
1. RE-DERIVE the Euler–Maclaurin remainder bound in 'zeta_encl.py' independently (write the derivation in your report); check the implementation matches the derivation (signs, first-omitted-term index, the σ-condition, the handling of |t| large); same for 'hurwitz_encl.py' and the DH tan θ enclosure in the acceptance code. Any bound that is not rigorous as implemented is FATAL.
2. Enclosure honesty: ≥ 50 fresh random points per evaluator (your own random seeds) vs dps-100 mpmath reference values; any reference value outside its enclosure = FATAL. Test edge regimes: σ near 1/2 and near 1, |t| near the largest heights used, and the DH function at its off-line zero.
3. Winding scheme: re-derive the geometry — does the mesh-admissibility criterion in FORMAT.md actually imply the claimed argument-increment bound (the half-plane / disc-excluding-zero argument)? Corrupt ≥ 3 accepted transcripts by hand in ways a buggy producer might (shift one enclosure so 0 enters a cell; break the sum-width < 1/2 condition; change the integer m; break the contour ordering) and confirm 'checker_ref.py' REJECTS each; a checker that accepts corrupted data is FATAL. Then run the LEAN checker on the same corrupted data if the Examples/Checker architecture permits (find out how Session 8 ran the Lean checker on transcripts — the acceptance report claims '8/8 null transcripts × 2 checkers' — and REPRODUCE that claim; if it cannot be reproduced, say so).
4. Rounding directions in both ball→integer conversions (outward!), scale-K handling, exact-rational rectangle data; and that 'checker_ref.py' shares no evaluation code with the producers.
5. Independence of the two producer legs (Arb vs mpmath-ball): confirm no shared evaluation code; re-run the two-producer cross-check on at least two acceptance transcripts yourself.
6. Check every numerical claim in 'acceptance-report.md' and 'cost-curve.json' against the artifacts on disk; recompute at least the DH live-fire transcript's winding enclosure from scratch with your own script.
7. The Lean layer: confirm 'lake build Zeta23.W1.Soundness' passes (it did at 01:52 today; do not rebuild the whole library), run '#print axioms' on the soundness theorem(s) in a scratch file and record the output; check that the Lean checker's check is the SAME predicate as FORMAT.md/checker_ref.py (compare clause by clause; a divergence is MAJOR at least).
Write '${RH}/results/d1-m1/AUDIT-${tag}.md' (findings with severities and exact locations; the derivations; the scripts you used saved alongside as 'audit_${tag}_*.py'; repairs PROPOSED as replacement code/text — do NOT modify the Session-8 files; the reconciler applies repairs). In the 'gomila_unblock' field state exactly which of Gomila screen steps 3–4 ('results/d1-m0/gomila-screen.md' §4) M1 v1 as built now clears, and what M2a must add. Return the schema.`
}

const AUDIT_SCHEMA_O = {
  type: 'object', required: ['verdict', 'fatals', 'majors', 'summary', 'file'],
  properties: { verdict: { enum: ['clean', 'repairs-proposed', 'defects', 'fatal'] }, fatals: { type: 'integer' }, majors: { type: 'integer' },
    summary: { type: 'string', maxLength: 9000 }, file: { type: 'string' }, gomila_unblock: { type: 'string', maxLength: 3000 } },
}
function auditBriefO() {
  return `RESUMED RUN. A previous run of this exact audit (brief below) was cut off by a usage limit AFTER writing '${RH}/results/d1-m1/AUDIT-O.md' (49 KB, 02:25 IST) and the 'audit_O_*' scripts/logs alongside, but BEFORE returning its structured summary (the structured-output call failed five times — most likely the summary was too long). Do NOT redo the audit from scratch: read AUDIT-O.md first, re-run the audit_O_* scripts and confirm their outputs match their logs, complete any of steps 1–7 below that the report does not cover, fix the report where the re-run disagrees, and then RETURN the schema with a summary UNDER 3000 CHARACTERS (verdict, counts, the majors in one line each, and the gomila_unblock statement under 1500 characters).

` + auditBrief('O')
}

phase('Audit')
const audits = await parallel([
  () => agent(auditBrief('F'), { label: 'audit-F', phase: 'Audit', effort: 'xhigh', schema: AUDIT_SCHEMA }),
  () => agent(auditBriefO(), { label: 'audit-O', phase: 'Audit', effort: 'xhigh', model: 'opus', schema: AUDIT_SCHEMA_O }),
])
const auditsOk = audits.filter(Boolean)
log(`audits: ${auditsOk.map(a => a.verdict + ' (fatals ' + a.fatals + ')').join(' / ')}`)

phase('Reconcile')
const rec = await agent(`${COMMON}

TASK — RECONCILE the two independent audits of M1 v1: 'results/d1-m1/AUDIT-F.md' (Fable 5.1) and 'results/d1-m1/AUDIT-O.md' (Opus 5). Returned summaries: ${JSON.stringify(auditsOk.map(a => ({ verdict: a.verdict, fatals: a.fatals, majors: a.majors, summary: a.summary.slice(0, 3000), gomila: a.gomila_unblock })))}.
Protocol: every FATAL/MAJOR finding from either auditor is RE-VERIFIED by you (rerun their script, or your own) before it is accepted; disagreements are settled by computation, not by vote. Then: (1) APPLY the repairs that are small and verified (fix the code, re-run the affected validation, record before/after), and list large defects as demanded repairs with a cost; (2) re-run the full acceptance suite's checker pass on all transcripts after repairs; (3) write 'results/d1-m1/AUDIT.md' (the merged, binding audit: per-finding table with auditor, severity, your verification, status APPLIED/DEMANDED/OVERRULED) and 'results/d1-m1/RUN-REPORT.md' (the honest statement of what M1 v1 now IS, with trust vocabulary; what remains for v1.1 per D-R3 — the argument principle in Lean; the f_t evaluator status; and 'Gomila steps 3–4: what is cleared, what M2a must add'). (4) Verdict for the gate: 'clean' or 'repaired-clean' lets M2a proceed; 'defects-remain' lets it proceed with the defects listed as constraints; 'fatal' stops the build. Return the schema; keep 'summary' under 4000 characters.`,
  { label: 'reconcile', phase: 'Reconcile', effort: 'xhigh', schema: {
    type: 'object', required: ['verdict', 'summary', 'constraints'],
    properties: { verdict: { enum: ['clean', 'repaired-clean', 'defects-remain', 'fatal'] }, summary: { type: 'string', maxLength: 6000 },
      constraints: { type: 'string', maxLength: 3000 } } } })
log(`reconcile: ${rec?.verdict}`)
if (!rec || rec.verdict === 'fatal') {
  log('M1 v1 audit FATAL — M2a build not started')
  return { audits, reconcile: rec, m2a: 'not-started' }
}

phase('Spec')
const spec = await agent(`${COMMON}

M1 v1 audit verdict: ${rec.verdict}. Constraints carried forward: ${rec.constraints}.

TASK — write the M2a BARRIER-CERTIFICATE CONTRACT that the Lean checker and the two producers consume (design note §1.3/§1.6 items b–e; the Session-8 Format-architect pattern). Deliverables in 'results/d1-m2a/' (create):
1. 'SPEC.md' — referee-grade. Fix precisely, from the on-disk Polymath15 paper (Theorem 1.2 and its proof; Theorem 1.3 / the effective approximation A + B (+C) with its explicit error bound; the barrier region; the asymptotic-region hypothesis and how Polymath15 discharge it — cite pages of p3-22a4/p3-22a5): (a) the exact mathematical statement the barrier transcript certifies (which function — H_t via the effective approximation with error E — on which box in (x,y,t), what 'nonvanishing on every prism' means, the per-slice winding/argument scheme, the t-interpolation bound between slices, all in a form matching what 'Polymath15Bridge' in Defs.lean expects as hypotheses — read Defs.lean and make the contract fit the ELABORATED shapes, not the pseudocode); (b) what stays a DISPLAYED hypothesis (BarrierEnclOK: true values lie in enclosures; ZeroVerification: cited to PT Thm 1) versus what the checker verifies in integer arithmetic; (c) the asymptotic-region component: either a second checked lane (rows of a finite computation + a citable analytic tail from Polymath15 with exact location) or a displayed hypothesis — DECIDE, state the reason, and make sure the decision is honest about what is and is not kernel-checked; (d) the integer transcript format (scale K, exact-rational box data, prism list, enclosures as integer pairs, winding rows), 'barrier-schema.json', and a tiny worked micro-example with all integers; (e) the compatibility map to Gomila's artifact format (883 prisms, printed-enclosure logs; 'results/d1-m0/gomila-screen.md' §3) so that M2a′ is a conversion, not a redesign.
2. The instance parameters: Polymath15 Table 1 row 2 as the design note fixes it (X = 5·10^12 + 194858, t0 = 0.186, y0 = 0.16733; recompute t0 + y0²/2 exactly and confirm it is the row that pairs with Platt–Trudgian's height for Λ ≤ 0.2 — design note §0) — write them as exact rationals in SPEC.md with the PT pairing arithmetic redone.
Return the schema.`,
  { label: 'spec', phase: 'Spec', effort: 'xhigh', schema: {
    type: 'object', required: ['summary', 'files', 'asymptotic_decision'],
    properties: { summary: { type: 'string', maxLength: 5000 }, files: { type: 'array', items: { type: 'string' } },
      asymptotic_decision: { type: 'string', maxLength: 1500 }, open_points: { type: 'string', maxLength: 2000 } } } })
log(`spec: ${spec?.files?.join(', ')}`)

phase('Build')
const BUILD_SCHEMA = { type: 'object', required: ['status', 'summary', 'files'],
  properties: { status: { enum: ['complete', 'partial', 'blocked'] }, summary: { type: 'string', maxLength: 5000 }, files: { type: 'array', items: { type: 'string' } }, validation: { type: 'string', maxLength: 2500 } } }
const specSummary = JSON.stringify((spec && spec.summary) || 'SPEC.md missing — derive from the design note').slice(0, 2500)

const [lean, arb, mp] = await parallel([
  () => agent(`${COMMON}

The contract is on disk: read 'results/d1-m2a/SPEC.md' + 'barrier-schema.json' first. Spec summary: ${specSummary}. Asymptotic-region decision: ${JSON.stringify(spec?.asymptotic_decision || '')}.

TASK — M2a item (b): 'Zeta23/DBN/BarrierCert.lean' in the Lean working tree: the barrier transcript structure (integer data exactly per SPEC.md), 'checkBarrier' as a decidable Bool-valued check in the RowCert/W1 architecture (integer comparisons only; 'decide +kernel'-friendly), and the soundness theorem 'cert_of_checkBarrier': if checkBarrier data = true and the displayed hypothesis BarrierEnclOK data holds (true values in enclosures), then the barrier hypothesis in the form Polymath15Bridge (Defs.lean) consumes. Follow 'Zeta23/W1/Soundness.lean' as the pattern (it proved the analogous cert_of_checkW1 with H-ENCL/H-AP displayed). The analytic content (what nonvanishing on prisms + the t-interpolation bound imply) is stated as a displayed hypothesis wherever it is not proved — say so in the module docstring with the D-R3 vocabulary; never leave a 'sorry'. Build with 'lake build Zeta23.DBN.BarrierCert' (one lake process at a time; targeted module only). Then: '#print axioms' on every theorem (must be propext/Classical.choice/Quot.sound only), a scratch example transcript that checks by 'decide +kernel' (small), copy the file to '${RH}/lean/Zeta23/DBN/BarrierCert.lean' with the program header, update '${RH}/lean/README.md' table, and add the module to '${LEAN}/Zeta23.lean' imports if the root file lists program modules (it lists DBN.Defs and W1.* — follow that). Write 'results/d1-m2a/lean-notes.md' (build log excerpt, axioms output, the exact statement of every displayed hypothesis). Return the schema.`,
    { label: 'lean-barriercert', phase: 'Build', effort: 'xhigh', schema: BUILD_SCHEMA }),
  () => agent(`${COMMON}

The contract is on disk: read 'results/d1-m2a/SPEC.md' + 'barrier-schema.json' first. Spec summary: ${specSummary}.

TASK — M2a item (c): the ARB-side f_t / H_t PRODUCER in 'results/d1-m2a/producer_arb.py' (python-flint 0.6.0 balls; see 'results/d1-m1/arb-leg-notes.md' and 'producer_arb.py' for the ball→integer outward-rounding pattern). Implement the effective approximation of H_t from Polymath15 (Theorem 1.3 / the A + B (+C) approximants with the EXPLICIT error bound E — transcribe every formula from the on-disk PDF with page numbers into the module docstring; derive any intermediate inequality you need in full), in ball arithmetic end to end, so that each prism's enclosure is a rigorous enclosure of H_t (approximant ball + rigorous error radius). VALIDATE against direct high-precision numerical evaluation of H_t (mpmath quad of the defining integral, or the ξ-based identity at t = 0) at moderate x (say x ≤ 10^4, several t in [0, 0.2], several y) — at least 30 points — enclosure must CONTAIN the reference; report widths. Then produce the Instance02 barrier transcript per SPEC.md at the row-2 parameters (X ≈ 5·10^12 — measure the per-prism cost first, extrapolate, and if the full mesh is beyond a few hours at ≤ 2 processes, produce the FULL transcript for as large a sub-box/coarser-but-rigorous mesh as the spec's admissibility criterion allows and state the cut line honestly — never a non-rigorous shortcut). Emit the integer transcript file(s) under 'results/d1-m2a/transcripts/'. Independence discipline: share the SPEC with the mpmath leg but NO evaluation code. Write 'results/d1-m2a/arb-leg-notes.md'. Return the schema.`,
    { label: 'arb-ft-producer', phase: 'Build', effort: 'xhigh', schema: BUILD_SCHEMA }),
  () => agent(`${COMMON}

The contract is on disk: read 'results/d1-m2a/SPEC.md' + 'barrier-schema.json' first. Spec summary: ${specSummary}.

TASK — M2a item (d): the independent MPMATH-BALL f_t / H_t PRODUCER in 'results/d1-m2a/producer_mp.py', on top of the M1 ball core 'results/d1-m1/ball.py' (reuse the ball layer; NO code shared with the Arb leg's evaluation). Implement Polymath15's effective approximation of H_t (Theorem 1.3 / A + B (+C) with the explicit error term — transcribe from the on-disk PDF with page numbers into the docstring; derive intermediate inequalities in full) in interval arithmetic end to end. VALIDATE: ≥ 30 points at moderate x against direct high-precision evaluation (mpmath quad of the defining integral at dps ≥ 60), enclosure must CONTAIN the reference; report widths. Then produce the Instance02 barrier transcript per SPEC.md at the row-2 parameters (measure per-prism cost, extrapolate, batch ≤ 2 processes; if the full mesh is infeasible in a few hours, deliver the largest fully rigorous sub-box and state the cut line honestly). Emit integer transcripts under 'results/d1-m2a/transcripts/'. Write 'results/d1-m2a/mp-leg-notes.md'. Return the schema.`,
    { label: 'mp-ft-producer', phase: 'Build', effort: 'xhigh', schema: BUILD_SCHEMA }),
])
log(`build: lean=${lean?.status} arb=${arb?.status} mp=${mp?.status}`)

phase('Instance')
const inst = await agent(`${COMMON}

Build status — Lean: ${JSON.stringify(lean?.status)} (${JSON.stringify(lean?.summary || '').slice(0, 1500)}); Arb leg: ${JSON.stringify(arb?.status)} (${JSON.stringify(arb?.summary || '').slice(0, 1500)}); mpmath leg: ${JSON.stringify(mp?.status)} (${JSON.stringify(mp?.summary || '').slice(0, 1500)}). Contract: 'results/d1-m2a/SPEC.md'.

TASK — M2a item (e) + the Gomila M2a′ conversion (screen steps 3–4). (1) TWO-PRODUCER CROSS-CHECK of the Instance02 transcripts: cell-wise nonempty intersection of the two legs' enclosures; any disagreement beyond radii is stop-the-line and is reported as such. (2) Run the reference checker (write 'results/d1-m2a/checker_ref.py' in exact Fraction arithmetic implementing SPEC.md, sharing no code with producers — mirror the Lean predicate clause by clause) on every transcript; then the LEAN checker: write 'Zeta23/DBN/Instance02.lean' embedding the transcript data (or the largest fully rigorous sub-box transcript, honestly labeled) and closing 'checkBarrier data = true' by 'decide +kernel' — measure kernel time; if the literal is too large for the kernel, split it per the W1/Examples pattern or record the exact size limit hit. Build with 'lake build Zeta23.DBN.Instance02' (one lake process). '#print axioms'. Copy to '${RH}/lean/Zeta23/DBN/' with program header; update lean/README.md. (3) GOMILA steps 3–4 ('results/d1-m0/gomila-screen.md' §4): fetch the claimant's sealed artifacts (repo judegomila/dbn-lambda-01787854-candidate-audit @ a74738d — network with a retry loop, once a minute up to 30 attempts), convert the 883-prism barrier logs to the SPEC.md transcript format (exact conversion with outward rounding; record the mapping), run checker_ref + the Lean checker on the converted data, and run BOTH of D1's producers on a spot sample of ≥ 20 of Gomila's prisms (same box, same t) for the two-producer spot check — report agreement/disagreement per prism. State clearly what this does and does not establish (the claim stays 'screen-open'/'not a record' vocabulary per the screen note §7 unless every step passes, and even then it is 'M2a′ candidate', never a record). (4) Write 'results/d1-m2a/INSTANCE-REPORT.md' and update 'results/d1-m0/gomila-screen.md' with a dated addendum for steps 3–4 (append-only). Return the schema.`,
  { label: 'instance02+gomila', phase: 'Instance', effort: 'xhigh', schema: {
    type: 'object', required: ['instance_status', 'gomila_status', 'summary'],
    properties: { instance_status: { enum: ['kernel-checked', 'partial', 'blocked'] }, gomila_status: { enum: ['steps-3-4-pass', 'partial', 'fail', 'blocked'] },
      summary: { type: 'string', maxLength: 6000 }, files: { type: 'array', items: { type: 'string' } } } } })
log(`instance: ${inst?.instance_status}; gomila: ${inst?.gomila_status}`)

phase('Final audit')
const fin = await agent(`${COMMON}

TASK — the standing-order-5 FINAL AUDIT of everything built this session under 'results/d1-m2a/' and 'lean/Zeta23/DBN/'. Inputs: spec = ${JSON.stringify(spec?.summary || '').slice(0, 1200)}; lean = ${JSON.stringify(lean?.summary || '').slice(0, 1200)}; arb = ${JSON.stringify(arb?.summary || '').slice(0, 1200)}; mp = ${JSON.stringify(mp?.summary || '').slice(0, 1200)}; instance = ${JSON.stringify(inst?.summary || '').slice(0, 2000)}. You are adversarial. (1) Re-derive the effective-approximation error bound from the on-disk Polymath15 paper yourself and check both producers implement it (constants, the range conditions on x, y, t under which the bound is valid — Polymath15 state explicit ranges; a producer used outside them is FATAL). (2) Enclosure honesty spot-check for both legs at fresh points vs direct evaluation. (3) Corrupt ≥ 3 transcripts and confirm checker_ref AND the Lean checker reject. (4) Compare the Lean predicate, checker_ref, and SPEC.md clause by clause. (5) Check every claim in INSTANCE-REPORT.md and the Gomila addendum against artifacts; recompute the PT pairing arithmetic exactly. (6) Confirm '#print axioms' outputs and that no 'sorry'/'admit'/'native_decide' exists in the program's Lean files ('grep -rn' over '${RH}/lean'). (7) Write 'results/d1-m2a/AUDIT.md' with findings, severities, repairs applied (small) or demanded (large), and 'results/d1-m2a/RUN-REPORT.md': the honest statement of what M2a now IS in trust vocabulary — which hypotheses are displayed, what is kernel-checked, what the Λ ≤ 0.2 instance establishes and does not, the Gomila status, the cost curve, and the exact next steps (v1.1 argument principle; M2b bridge; any cut line). Return the schema.`,
  { label: 'final-audit', phase: 'Final audit', effort: 'xhigh', schema: {
    type: 'object', required: ['verdict', 'fatals', 'summary'],
    properties: { verdict: { enum: ['clean', 'repaired-clean', 'defects-remain', 'fatal'] }, fatals: { type: 'integer' }, summary: { type: 'string', maxLength: 6000 } } } })
log(`final audit: ${fin?.verdict}`)
return { audits, reconcile: rec, spec, lean, arb, mp, instance: inst, final: fin }