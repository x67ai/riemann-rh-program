export const meta = {
  name: 'c3r-referee-debts-s14',
  description: 'Pay the Session-8 referee debts on the C3-r probe notes with duplicated independent referees (one Opus 5), run the dual-model novelty sweep on the Session-8 claims, adjudicate everything by re-derivation',
  phases: [
    { title: 'Referee', detail: '3 debts x 2 independent referees (Fable + Opus 5), line-by-line re-derivation' },
    { title: 'Novelty', detail: 'dual-model prior-art sweep on the five Session-8 novelty claims' },
    { title: 'Adjudicate', detail: 'binding re-derivation of every contested point; dated repair blocks in the notes' },
  ],
}

const RH = '/Users/jaytyagi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Work/2026/Math/riemann/rh-program'
const OUT = 'results/c3-r/referee-s14'

const COMMON = `You are a mathematics referee/verification agent in the RH research program (Session 14, 2026-09-02), direction C3-r (geometric substrate, reduced recommission).
Program root (the path contains SPACES; always quote it in shell): ${RH}
All deliverables go under '${RH}/${OUT}/' (create it). Write deliverables to disk in chunks as you go; your final text return is data for the orchestrator, not prose.
BINDING RULES (sponsor standing orders, STATUS.md):
- Standing order 5: nothing load-bearing from memory. Every claim you make about a source must be read from the on-disk PDF at a stated page, or from a fetched primary text at a stated location. Recalled theorems are labeled [RU] and carry no weight.
- Standing order 7 (new, 2026-09-02): novelty/priority claims are verified twice, by two different models; you are ONE of the two. Never soften a finding because you expect the other check to catch it.
- This is one of the hardest problems in mathematics; no corner is cut. A referee pass is a LINE-BY-LINE re-derivation of the proof under review, not an audit around it. If a step cannot be re-derived, say so: 'not re-derived' is an honest verdict; 'plausible' is not a verdict.
- U.S. English. Honest labels: PASS / PASS-WITH-REPAIRS (list them, each with the replacement text) / FAIL (state the false claim and a counterexample or the exact gap). Severity per finding: FATAL (a stated theorem is false or its proof has an unfillable gap) / MAJOR (gap fillable, but the note must change) / MINOR (wording, citation, typo).
- Primary sources ON DISK (read them; page numbers are the printed ones unless you say PDF-page): [x-03] Deninger, Dynamical systems for arithmetic schemes, arXiv:1807.06400v4 = 'fetched/x-03-deninger-dynamical-systems-for-arithmetic-schemes-arxiv-v4.pdf'; [x-06] Deninger, Primes, knots and periodic orbits, arXiv:2301.11643 = 'fetched/x-06-deninger-2024-primes-knots-and-periodic-orbits.pdf'; [r3s-08] Morishita, arXiv:2508.15971v5 = 'fetched-r3/r3s-08-morishita-deninger-cc-bridge-2508.15971.pdf'; [D25] Deninger, Rational Witt vectors and associated sheaves, arXiv:2508.05329v1 = 'fetched-r3/r3s-22-deninger-rational-witt-vectors-associated-sheaves-arxiv-2508.05329v1-SESSION8-FETCH.pdf'. Read 'results/corpus-routing.md' header caveats before citing any corpus file.
- Program context you must read first: 'results/c3-r/probe-9.3-adjudication.md' (the binding Session-8 adjudication; its §2 lists the verified source anchors), then the note under review in full.
- Do NOT edit the probe notes or any direction file; the adjudicator applies repairs. Your report is a separate file.`

const DEBTS = [
  {
    key: 'A-thmB',
    title: "probe A's Theorem B(b): the n-cell construction and the infinite-dimensionality conclusion",
    note: 'results/c3-r/probe-9.3-a.md',
    scope: `The debt (adjudication §4 item 6): Theorem B(b) of probe A was checked at proof-sketch level only. Re-derive it line by line: the splitting of the multiplicative group of the algebraic closure of Q as (roots of unity) x V with V uniquely divisible; the Q-linear independence of the V-components of distinct rational primes modulo torsion; the definition of the unitary characters Psi_t for t in [0,1/2]^n and that each satisfies (Tors) and lies in the E_max locus (check [x-03]'s definitions of the classes E_f, E_max, E_tors and the (Tors)/(Image) conditions at the pages the note cites, p. 27 in particular); that [Psi_t, 1] lies in the closure of the periodic set by [x-03] Thm 8.2 (verify the hypotheses of Thm 8.2 as printed, including its unconditional status for Spec Z and the [Per11] citation); continuity of t -> Theta(t) in X_0's topology (this needs the actual topology on X_0 — the colimit/suspension topology of [x-03] §§3–5 — state it and check continuity against it, not against an assumed product topology); injectivity of Theta (the note argues via Galois-fixedness of rational primes and injectivity of the colimit strata, [x-03] Prop. 4.2 p. 27 — verify exactly what Prop. 4.2 says); the compact-to-Hausdorff homeomorphism step and the dimension-monotonicity step (Hurewicz–Wallman: state the exact theorem used and its hypotheses — separable metric? normal + closed subspace?); and the scope notes (i)–(iii) (for E strictly between E_f and E_max, do the cells fall outside E, and does part (a) really hold on the whole window?). Also check the interaction with the adjudication's finding that X_0 is NON-HAUSDORFF along packets: Theorem B(b) hypothesizes Hausdorffness of the SUBSYSTEM S in its subspace topology — confirm the proof never uses Hausdorffness of X_0 itself.`,
  },
  {
    key: 'B-corA1',
    title: "probe B's Corollary A.1: the converse inclusion cl(gamma) ⊆ Gamma_p (packets are exactly the orbit closures)",
    note: 'results/c3-r/probe-9.3-b.md',
    scope: `The debt (adjudication §4 item 6; probe B's own Q-c): Corollary A.1's converse inclusion was argued at proposition grade only — 'every limit of {F_n(P_0)} along any subnet is P_0^b for some b in the prime-to-p profinite completion, by compactness and the same pointwise evaluation; limits with some component of b equal to 0 kill a mu_{l^infty} and violate (Tors), so they leave the space — one gets cl(gamma) ∩ (char-p part) = Gamma_p exactly'. Re-derive: (1) the exact topology on X_0 in which closures are taken ([x-03] §§3–5: the topology on the character spaces, the colimit over finite-level strata, the suspension); (2) whether 'pointwise convergence of characters' is the right description of that topology on the char-p stratum, and on the whole space (it may differ: check whether X_0's topology is a colimit topology which is FINER than pointwise convergence — this is exactly where a subnet limit could exist pointwise but not in X_0, or conversely); (3) the claim that a limit with a zero component 'leaves the space' — is it excluded by (Tors), by the class E, or by the topology, and does it matter for the closure computed IN X_0; (4) whether cl(gamma) could meet OTHER strata (the generic point stratum, other primes' packets) — Theorem A's ⊇ direction is about the char-p packet; the equality claim needs that nothing else is in the closure, which is a statement about the whole colimit topology, not just the packet; (5) restate what is actually proved at referee grade: equality in every chart of the colimit, or only within the char-p part. Note the adjudication says nothing load-bearing rests on this converse; your job is to settle it honestly either way and to state its exact scope.`,
  },
  {
    key: '94-lemmas',
    title: "the 9.4 note's Lemmas A–D and Proposition 1 (the transplant trichotomy D1–D3)",
    note: 'results/c3-r/probe-9.4-note.md',
    scope: `The debt (9.4 note §8 item 1): Lemmas A, B, C, D and Proposition 1 (§§4–6) are derived in the note and owe a referee pass. Press exactly where the note itself says a referee should press, and everywhere else: (Lemma A) the identification of mod-p-additive multiplicative maps with the Teichmüller class in packet coordinates, INCLUDING its converse (the note flags 'Lemma A's converse (the V F = p Witt identity)'); (Lemma B) the archimedean defect bound selects the empty set on the periodic locus — check the test r = s = 1 and the claim |P(2-bar) - 2| >= 1 at every packet point, for every class E ⊆ E_tors, and whether 'the periodic locus' is the right locus; (Lemma C) surjectivity of Aut(C) -> Aut(mu(C)) = the profinite units, via Steinitz — check each extension step (cyclotomic, to the algebraic closure, along a transcendence basis, then to C) and the exact use of choice; (Lemma D) the Aut(C)-action on the character space commutes with the G-action, with every F_nu, with the Q_{>0}-action and the flow, and PRESERVES each named class E_tors, E_max, E_f, E_fg, E_fd, E_fd0 — the note's press point: 'Lemma D(ii)'s class-stability claims for E_max's (Image) condition' — read [x-03] Def. 4.1 and the definitions of every named class and verify stability one class at a time, especially (Image) for E_max, and the ⊗Q-dimension conditions; (Lemma D(iii)) the coordinate formula (a, nu) -> (u_sigma a, nu) on the packet, via the divisible-image argument; (Proposition 1) the consumption of '[x-03] p. 33: the fibers of the (38)-fibration are the Q_{>0}-orbits' — read (38)–(39) verbatim and verify the fibers statement; verify that distinct base classes lie on distinct orbits; verify the uncountability input. Also check §3's freshman's-dream N-invariance argument and §7's Haar formal count (all orbits in Gamma_p have length log p — [x-06] Thm 4.2 — read it). Report each lemma separately with its own verdict.`,
  },
]

const REF_SCHEMA = {
  type: 'object', required: ['verdict', 'fatals', 'majors', 'minors', 'summary', 'file'],
  properties: {
    verdict: { enum: ['PASS', 'PASS-WITH-REPAIRS', 'FAIL', 'NOT-RE-DERIVED'] },
    fatals: { type: 'integer' }, majors: { type: 'integer' }, minors: { type: 'integer' },
    summary: { type: 'string', maxLength: 5000 },
    file: { type: 'string' },
  },
}

function refereeBrief(d, tag) {
  return `${COMMON}

YOUR ITEM: ${d.title}. Note under review: '${d.note}'. You are referee ${tag} of two independent referees on this item; the other referee is a different model and you must not assume anything about their findings.

${d.scope}

METHOD. (1) Read the adjudication, then the whole note (not just the section), so you know what the note claims elsewhere and what the adjudication already re-derived. (2) Open the primary sources at every cited location and quote the relevant sentence(s) verbatim into your report with the page. If a cited location does not say what the note says it says, that is a finding. (3) Re-derive every step in your own words, in full, in the report — a reader must be able to check your derivation without the note. (4) Where you find a gap, try to FILL it (state the repair as replacement text) and try to BREAK it (construct a counterexample); report both attempts. (5) End with a verdict block: verdict, severity-tagged findings with locations, the exact replacement text for each repair, and a one-paragraph 'what is now established at referee grade and what its precise scope is'.
Write the report to '${OUT}/${d.key}-${tag}.md' (referee-grade markdown, dated 2026-09-02, with a sources section listing every page you read). Return the schema fields; 'file' is the report path relative to the program root.`
}

phase('Referee')

const NOV_SCHEMA = {
  type: 'object', required: ['summary', 'file', 'verdicts'],
  properties: {
    summary: { type: 'string', maxLength: 5000 }, file: { type: 'string' },
    verdicts: { type: 'array', items: { type: 'object', required: ['claim', 'verdict'], properties: {
      claim: { type: 'string', maxLength: 200 }, verdict: { enum: ['NOVEL', 'ANTICIPATED', 'PARTIAL', 'UNDETERMINED'] },
      source: { type: 'string', maxLength: 600 } } } },
  },
}

function noveltyBrief(tag) {
  return `${COMMON}

YOUR TASK: the standing-order-7 NOVELTY / PRIOR-ART sweep, check ${tag} of two (the other check is a different model; do not assume anything about it). The five Session-8 claims below are each asserted somewhere in 'results/c3-r/probe-9.3-a.md', 'probe-9.3-b.md', 'probe-9.3-adjudication.md' or 'probe-9.4-note.md' to be new — 'by an argument not present in [x-03], [x-06], or [r3s-08]', 'new in this note', etc. Your job is to find out whether each is in the literature, and to record HOW you searched so a later session can see what was and was not covered. The program's earlier sweeps missed Winkelmann 2002 because they searched in prime-indexed language while the source used eigenvalue/geodesic-length language; vary the vocabulary deliberately (dynamical-systems, foliation, profinite/solenoid, class-field-theory, Witt-vector and knot-theoretic phrasings).

CLAIMS.
N1. The packet-closure law (Theorem A): in Deninger's dynamical system X_0 = X(Spec Z) (arXiv:1807.06400), the closure of any single periodic orbit contains its entire packet Gamma_p; the forcing group is the cokernel of the prime-to-p linking homomorphism (Morishita's lk_p); mechanism = profinite accumulation of Frobenius return exponents (CRT). Also: packets are minimal sets; any closed flow-invariant subset containing one periodic orbit of length log p contains uncountably many.
N2. X_0 is non-Hausdorff along its packets (no periodic orbit is closed as a subset); and every closed flow-invariant subset of X_0 meeting every packet is infinite-dimensional (contains n-cells for every n) — so the first alternative of Deninger's own question ([x-03] §6 p. 40, a closed sub-dynamical system Y_0 ⊂ X_0 with one closed orbit of length log p per prime) has answer NO.
N3. The identity B_p = coker(Aut_ring(F_p-bar) -> Aut_group(F_p-bar^x)) = coker(lk_p) for the packet base, and the Aut(C)-equivariance no-go: no Aut(C)-stable selection of one orbit per packet exists (Proposition 1 of the 9.4 note); the transport of Deninger's local mod-p-additivity principle to C selects nothing canonical (the trichotomy D1–D3).
N4. The Haar-average road: replace the 'one orbit per prime' demand by Haar measure on the packet base B_p (canonical, Aut(C)-equivariant, flow-invariant), and the corresponding question DQ-M — a trace formula for foliated flows admitting a CONTINUUM of periodic orbits with a transverse measure on the continuum (the existing Alvarez Lopez–Kordyukov–Leichtnam formulas assume simple/isolated closed orbits). Has anyone formulated or proved such a measured trace formula, or proposed Haar-averaging Deninger's packets?
N5. Theorem C: one-orbit-per-prime 'admissible cuts' of X_0 exist (reachability a_0 · p^Z-hat in the base) but are non-canonical and forfeit every certified theorem of [x-03].

WHERE TO LOOK (all of it; record each search with its phrasing and result). (a) The full citing literature of arXiv:1807.06400 and of Deninger's related papers (arXiv:2301.11643, 2508.05329, his 2024 'Dynamical systems for arithmetic schemes' follow-ups, Kucharczyk–Scholze 'Topological realisations of absolute Galois groups', Morishita 2508.15971 and his knot-theoretic papers, Alvarez Lopez–Kordyukov–Leichtnam 2402.06671 and sequels, Leichtnam's papers, Deninger–Singhof, Kim–Morishita, Lutz's Münster thesis if findable). Use WebSearch, WebFetch on arXiv listing/abs pages (if arxiv.org is unreachable use export.arxiv.org or a mirror), Google Scholar 'cited by' pages, Semantic Scholar, zbMATH Open (zbmath.org — free), and the Consensus paper-search MCP tool if reachable via ToolSearch. (b) Search the on-disk corpus: grep -il across 'sources-extracted/' and any text you can extract from 'fetched/', 'fetched-r2/', 'fetched-r3/' for 'packet', 'orbit closure', 'non-Hausdorff', 'linking number', 'Haar', 'continuum of periodic orbits', 'transverse measure'. (c) For each claim: verdict NOVEL (nothing found, with the search log), ANTICIPATED (state the source, exact location, and quote the sentence), PARTIAL (a special case or a closely related statement exists — quote it and state the difference precisely), or UNDETERMINED (a source that might contain it was unreachable — name it, so the sponsor can fetch it per standing order 1).
Write the report to '${OUT}/novelty-${tag}.md' with: per-claim verdict + evidence, the complete search log (phrasing, engine, date, hit or no hit), and a list of every document you opened. Return the schema fields.`
}

const REF_TAGS = [{ tag: 'F', model: undefined }, { tag: 'O', model: 'opus' }]

const [debtResults, novResults] = await parallel([
  () => pipeline(DEBTS,
    d => parallel(REF_TAGS.map(r => () => agent(refereeBrief(d, r.tag),
      { label: `ref-${r.tag}:${d.key}`, phase: 'Referee', effort: 'xhigh', schema: REF_SCHEMA, ...(r.model ? { model: r.model } : {}) }))),
    (refs, d) => agent(`${COMMON}

YOUR TASK: BINDING ADJUDICATION of the two independent referee reports on: ${d.title}. Note under review: '${d.note}'. Referee reports: '${OUT}/${d.key}-F.md' (Fable 5.1) and '${OUT}/${d.key}-O.md' (Opus 5). Their returned summaries: ${JSON.stringify((refs || []).filter(Boolean).map(r => ({ verdict: r.verdict, fatals: r.fatals, majors: r.majors, summary: r.summary.slice(0, 2500) })))}.

Protocol (STATUS.md standing order 5 + the Session-4 process learning): (1) Read both reports and the note. (2) Every finding either referee raised is RE-DERIVED by you against the primary source — you do not weigh testimony; where the referees disagree, the source decides, and where both agree you still check the mathematics yourself. (3) For every FATAL or MAJOR finding: decide UPHELD / OVERRULED with your own derivation written out. (4) Produce the binding verdict for the item: PASS / PASS-WITH-REPAIRS / FAIL, and the exact scope of what is established at referee grade. (5) APPLY the repairs to the note as dated blocks, following the program's convention: never silently rewrite earlier text; add a dated block '**[REFEREE PASS 2026-09-02 — Session 14]**' at the head of the relevant section (or of the note, for a FATAL) that states the finding, the replacement text, and where the original wording stood; if a statement is false, say 'WITHDRAWN' in the block. Keep the note's existing dated blocks intact. (6) Write '${OUT}/${d.key}-adjudication.md': the per-finding table (referee, finding, severity, your re-derivation, UPHELD/OVERRULED), the binding verdict, the scope statement, the list of edits you made to the note (file + section), and a 'novelty ledger' listing every result in this item that is claimed new (for the separate dual-model novelty sweep). Return the schema.`,
      { label: `adjudicate:${d.key}`, phase: 'Adjudicate', effort: 'xhigh', schema: {
        type: 'object', required: ['verdict', 'upheld_fatals', 'upheld_majors', 'summary', 'edits'],
        properties: { verdict: { enum: ['PASS', 'PASS-WITH-REPAIRS', 'FAIL'] }, upheld_fatals: { type: 'integer' }, upheld_majors: { type: 'integer' },
          summary: { type: 'string', maxLength: 6000 }, edits: { type: 'array', items: { type: 'string' } } } } })),
  () => parallel(REF_TAGS.map(r => () => agent(noveltyBrief(r.tag),
      { label: `novelty-${r.tag}`, phase: 'Novelty', effort: 'xhigh', schema: NOV_SCHEMA, ...(r.model ? { model: r.model } : {}) })))
    .then(novs => agent(`${COMMON}

YOUR TASK: BINDING ADJUDICATION of the two independent novelty sweeps (standing order 7). Reports: '${OUT}/novelty-F.md' (Fable 5.1) and '${OUT}/novelty-O.md' (Opus 5). Their returned verdict tables: ${JSON.stringify((novs || []).filter(Boolean).map(n => n.verdicts))}.
Protocol: (1) Where the two sweeps agree NOVEL, confirm that the UNION of their search logs covers the vocabulary variants listed in the brief (dynamical, foliation, profinite/solenoid, class-field, Witt, knot-theoretic) and the citing literature of arXiv:1807.06400; if a corner is uncovered, search it yourself now and record it. (2) Where either sweep says ANTICIPATED or PARTIAL: open the source yourself, quote the passage, and decide by comparing statements — never by counting votes. (3) Where either says UNDETERMINED: try once more to reach the source; if still unreachable, list it in a 'SPONSOR FETCH' block with exact bibliographic data. (4) Write '${OUT}/novelty-adjudication.md' with the per-claim binding verdict (NOVEL-DUAL-CHECKED / ANTICIPATED / PARTIAL / UNDETERMINED), the evidence, and the merged search log. (5) Then insert, as dated blocks '**[NOVELTY — dual-model check 2026-09-02]**' in each probe note (probe-9.3-a.md, probe-9.3-b.md, probe-9.3-adjudication.md, probe-9.4-note.md) at the point where the claim is made, a one-to-three-sentence statement of the verdict and the source if any. Do not delete or rewrite anything else. Return the schema.`,
      { label: 'novelty-adjudicate', phase: 'Adjudicate', effort: 'xhigh', schema: {
        type: 'object', required: ['summary', 'verdicts', 'sponsor_fetch'],
        properties: { summary: { type: 'string', maxLength: 6000 },
          verdicts: { type: 'array', items: { type: 'object', required: ['claim', 'verdict'], properties: { claim: { type: 'string', maxLength: 200 }, verdict: { type: 'string', maxLength: 60 }, source: { type: 'string', maxLength: 600 } } } },
          sponsor_fetch: { type: 'array', items: { type: 'string' } } } } })),
])

const debts = (debtResults || []).filter(Boolean)
log(`referee debts adjudicated: ${debts.map(x => x.verdict).join(', ')}; novelty: ${novResults ? 'done' : 'missing'}`)
return { debts: debtResults, novelty: novResults }