# read-O — second reader of `cogentic-2026/process-lessons.md`

PLAN (written before any reading; replaced by the header once the work starts)
1. Read the paper (2609.40324v1.pdf, all 17 pages) into scratch text; list every practice.
2. Read KICKSTART.md whole; STATUS.md lines 26-46 and 122-127 (cut); the wave files named in the brief.
3. Step 1 blind pass: §1 table, five rows per append — paper words / on record? / failure on record? / verdict.
4. Step 2: open process-lessons.md only now; record SHA-256 and line count.
5. A: check every paper quotation character by character against pdftotext output (scripted).
6. B: check every record citation (paths, line numbers, counts, sizes) with wc/grep/awk.
7. C: P1-P10 "already adopted?" checks; §B "already ours" checks.
8. D: missed practices (Step-1 rows the study does not treat).
9. E: rules (p)-(t): conflicts with orders 0-14 and KICKSTART items, cost, evidence, verdict.
10. F: refusals (§C) and staged items (§E); E.1 against lemmaB-s41 CHARTER and U7-patterns NOTE §0.
11. G: tone (U.S. English; no RH-status sentences; banned words).
12. Write §4 FIX-FIRST and §5 minor pairs (OLD/NEW, OLD quoted exactly), §6-§9, verdict line.

## §1 Blind pass — the paper's practices against the record (written before `process-lessons.md` was opened)

Sources: the PDF via `pdftotext` (raw and `-layout`), all 17 pages; `KICKSTART.md` whole; `STATUS.md` l. 26–46 and 122–127; the wave files named in the brief. "K:n" = `KICKSTART.md` line n; "S:n" = `STATUS.md` line n; "dig:n" = `results/novel-wave-s39/insights-digest.md` line n; "CH:n" = `results/lemmaB-s41/CHARTER.md` line n; "RBO:n" = `results/novel-wave-s41/READ-BRIEF-O.md` line n. Quotes are exact; "𝑂" (math italic in the PDF) is written O.

| # | Practice — the paper's words (§) | On the record? | Failure on the record it would have prevented? | Verdict |
|---|---|---|---|---|
| 1 | Shared disk workspace, scheduling by the orchestrator — "They share a workspace on disk and are coordinated by an orchestrator that decides which of them runs, when, and on what." (§2) | YES — `SHARED.md` per stream, K:72 (10(e)); CH:3 | — | already ours |
| 2 | The orchestrator does no mathematics — "The orchestrator does not perform mathematical derivations itself." (§2); "neither the advisor nor the orchestrator is permitted a mathematical opinion: they cannot speculate on what the answer is likely to be, recommend a technique, or declare a direction promising or dead." (§2.4) | NO — the opposite is binding: S:41 order 11(c) (the orchestrator's own read is the second model), S:42 order 12(d) (a proof is a GAP until the orchestrator reads it at the line); CH:16–20 "What the orchestrator worked out today (use it; check it)"; `lemmaB-s41/ORCH-NOTES.md` (itself dual-read: `orch-notes-read-O.md`) | PARTLY — K:91 (Session 41's orchestrator did Lemma B_ρ mathematics in long silent responses and hit the output ceiling repeatedly); dig:523–531 (E.12: five errors in the orchestrator's briefs/charters, all caught by the units). Counter-evidence: the orchestrator's O9 relation was used by U3 (`U3-firstbound/read-F.md`:6) | DECLINE the ban (conflicts with orders 11(c), 12(d)); the lean form already exists (orchestrator mathematics in a notes file that is itself read, briefs say "use it; check it") |
| 3 | Directions include counterexamples and repair — "A direction here is a specific claim (e.g., a bound, a constant, a construction), finding counterexamples, or as the run goes on, repairing and finalizing promising proofs." (§2.1) | YES — CH:22–29 (seven units on one target, U5 "the adversary"); K:70 (10(c)); S:39 order 10(f); repair = read pairs applied by the orchestrator (RBO:9, 16; `scripts/apply-read-pairs.py`) | — | already ours |
| 4 | Direction, not method — "A prover is assigned to a direction to work on, but not how to work on it." (§2.1) | NO — charters prescribe methods: CH:25 (U3: "Chebyshev-type identities, the Lindley form"), CH:27 (U5: "Hilberdink's and Neamah–Hilberdink's methods at the page") | WEAK — dig:524–526: a brief's gap lemma "is false (η(2s))" (conjO) and a brief's dichotomy "is not one" (lemG); both caught by the units, no unit lost | DECLINE as a rule; the "use it; check it" label (CH:16) is the lean form already in use |
| 5 | Per-prover briefing by a summarizer — "each prover sees only a briefing, written for it by a summarizer, which is spawned by the orchestrator. The summarizer reads all prior attempts and their verdicts, selects the most informative ones as context, and gives suggestions for possible next steps, based on what has worked and what has not." (§2.1). NB Fig. 1's caption says instead "an advisor writes each prover an individual briefing" — the paper is inconsistent on who writes it | PARTLY — one consolidation agent per wave, "The next briefs must quote it" (K:68, 10(a)); briefs written by the orchestrator (CH, RBO) | no evidence on the record that a per-unit summary would have changed a unit | already ours in lean form (the digest); per-prover summarizers DECLINED (one agent per unit per wave) |
| 6 | Independent briefings, different readings — "Each summarizer produces its briefing independently, so provers in the same round receive different readings of the same history." (§2.1) | NO | no evidence on the record (the program's diversity comes from distinct units, CH:22–29) | DECLINE |
| 7 | Paths, not quotes — "Longer documents are given as paths rather than quoted in full, so a prover … can open what it wants to read selectively." (§2.1) | YES — CH:5–8 ("Read first (in this order)", paths and sections); RBO:6 | — | already ours |
| 8 | Literature reviewers, re-dispatched on a stall — "Literature reviewers search for related work and retrieve information such as definitions and theorems that a prover is likely to need. They can also be sent out again mid-run to do a more targeted search and find results that can help overcome ongoing technical barriers." (§2); "Literature reviewers supply background at the start and can be dispatched again mid-run when attempts stall at the same step." (Fig. 1) | PARTLY — prior-art gate S:28 (order 1), Grossmann sweep S:35 (order 6), prior art at the page in every read RBO:15. No agent that fetches what a WRITER needs before writing; no stall trigger | YES, repeatedly — prior art ON DISK missed by writers, caught only by a reader: dig:454 (qcond F2, Hilberdink 2012), dig:488 (lemG F5, Hilberdink 2012 Thm A), dig:494 (qtw F2, Hilberdink 2012), dig:516 (s5m F2, Olofsson 2010); `U3-firstbound/read-F.md`:17 (Diamond–Zhang Thm 6.13, on disk in `dz-half-s39/sources/`); off disk: `U5-obstruction/read-O.md`:24–25 (Hilberdink JTNB 2011, F7). One paper (Hilberdink 2012) was missed by three units of one wave | ADOPT in a lean form: one literature agent per wave before the units start, on-disk corpus first, writing a sources file every unit reads; re-dispatch only on a recorded stall |
| 9 | Independent parallel provers — "Provers generate candidate proofs independently and in parallel based on assigned briefings that selectively summarize findings obtained so far." (§2) | YES — S:42 order 12(c) (up to ten); CH:3 | — | already ours |
| 10 | Complementary verifiers; the orchestrator "evaluates verifier consensus" (§2) — "Verifiers critique candidate solutions from complementary angles and scopes." (§2) | YES — read-F (orchestrator) + read-O (Opus), RBO:3; scopes split on purpose (`U3-firstbound/read-F.md`:3 "left to the Opus reader"); reconciliation by the orchestrator (`lemmaG-s39/read-F.md`:22–29) | — | already ours |
| 11 | Cross-draft verifier; acceptance needs both — "A separate verifier reads all of the round’s drafts side by side, which allows it to spot shared blind spots and compare the strengths of individual proofs. A draft is accepted only when it passes both verifiers." (§2.2; the PDF has a curly ’) | PARTLY — per-draft: YES (two reads per unit). Cross-draft: only the consolidation digest, AFTER the reads and with no acceptance role (dig:328 §B cross-unit propositions; dig:386 §C "Controls — what each unit used, and flags on their use") | YES — shared blind spots across one wave's units: Hilberdink 2012 missed by qcond, lemG, qtw (dig:454, 488, 494); fits read as laws in conjO, uoff, fgC (dig:470, 472, 513) and a scan read as a statement on ζ_P in lg (dig:520); qtw re-proved and claimed qcond's Lemma M (dig:493) | ADOPT in a lean form: a cross-unit blind-spot pass inside the digest agent's brief (already funded by 10(a)); no new acceptance gate |
| 12 | Adversarial default — "Both are adversarial: they start from the assumption that every step is wrong until justified, and that every citation is incorrect until checked." (§2.2; also §1 "begin with the assumption that the proofs are incorrect or incomplete") | YES — RBO:13 ("Labels in the NOTE … are claims to test, not facts"; "A statement checked only by reading it is not re-derived"); RBO:15 ("A citation from memory is a defect"); S:34 order 5 | — | already ours |
| 13 | Record pooled by target, with method and objection — "The record pools attempts by what they were trying to establish, storing with each one the method used and the objection it failed on." (§2.3) | YES, under other names — unit closes "proof class X cannot yield Y because Z" (CH:32; K:70, 10(c)); the zoo (`BARRIER-ZOO.md`:1–3); "CLOSED ROUTES, with reasons on the record" (S:124); 10(m) abandonment labels (K:81); the waste line (K:83; dig:684 §H) | — | already ours |
| 14 | Salvage ledger — "Verifiers often confirm individual lemmas inside proofs they otherwise reject. At the end of a round, an auditor extracts those fragments, rewrites each as a self-contained lemma, and sends it to be verified again in isolation. What survives becomes available to every later prover as something that may be reused without being proved again." (§2.3) | PARTLY — salvage lists from adjudications in the early phase (`directions/A2-richer-functionals.md`:75 "Salvage (from adjudication, mandatory for any successor)"; LOG:104); dual-read status per NOTE ("CLOSED DUAL-READ", `U3-firstbound/read-F.md`:18); the target theorem restated in the charter (CH:11). No single register of dual-read statements; no isolated re-check of fragments of a failed NOTE | YES, one case — qtw re-proved and claimed Lemma M, Cor. M1 and Theorem D, proved first in qcond's dual read and entered qcond's NOTE at 05:24, forty minutes before qtw's NOTE was final (06:04); qtw cited the sibling at an older hash (`qtwin-s39/read-O.md`:174–175; dig:493) | ADOPT in a lean form: one append-only register of dual-read statements (statement, hypotheses, file:line, hash, both reads), written by the applier; isolation re-checks only when a NOTE's close fails |
| 15 | Dead ends in the ledger — "The ledger also records dead ends, for example, a bound excluded by a verified counterexample is written down as excluded, so that later rounds do not revisit them." (§2.3) | YES — the zoo; Untried entries leave "only into a result file or a zoo entry" (K:81); CH:8 ("F1 is binding here … Do not build on it") | — | already ours |
| 16 | The record steers the next round — "The orchestrator and advisor read the record and decide what the next round should do." (§2.3) | YES — 10(a) digest quoted by the next briefs (K:68); 10(d) reallocation (K:71); dig:533 §F survivor filter | — | already ours |
| 17 | Process advisor over the whole run's verification logs — "At the end of each round, a process advisor reviews verification logs, not only from the current round but from the run as a whole, to adjust how subsequent rounds are conducted. It surfaces patterns that become visible over time: repeated mistakes, common gaps in arguments, recurring verification blind spots where one verifier missed but was caught by some other verifier, etc." and recommends "a warning about a mistake several provers keep making, or a stricter justification standard for the kind of step where earlier drafts cut corners." (§2.4) | PARTLY — the digest lists every FIX-FIRST and which read found it (dig:447–531) and the orchestrator's own brief errors (dig:523–531, E.12); the waste line feeds KICKSTART amendments (K:83). Nothing turns the errata into a warning in the next charter or read brief, and nothing tallies error classes across waves | YES — the orchestrator's read-F found no FIX-FIRST in six units where read-O found 2–6 each: qcond (dig:452), conjO (:465), lemG (:482), dzh (:489), qtw (:492), fej (:500); `lemmaG-s39/read-F.md`:23 "F1 and F2 are real and were MISSED here"; the s41 orchestrator reads are partial by design (`U3-firstbound/read-F.md`:3). Recurring class "fit read as a law" (dig:470, 472, 513) with no warning in the next charter (CH:32 carries labels, not that warning) | ADOPT in a lean form: one added section in the existing digest — error classes with counts across waves, each with a one-line warning copied into the next charter and read brief; no new agent |
| 18 | The advisor is separate because the orchestrator lacks context — "This is a separate agent because the orchestrator, which must juggle concurrent duties across many agents, rarely has the context window to review and synthesize log trends itself." (§2.4) | YES in substance — the digest is "ONE consolidation agent" (K:68); the orchestrator's budget is binding (K:91, amendment of 17:00 IST 2026-10-01) | — | already ours |
| 19 | The advisor steers allocation and per-prover instructions — "It also advises the orchestrator on how to allocate prover attempts and how to adjust the instructions given to each prover and verifier for the next round." (§2.4) | YES for allocation (dig:533 §F, survivor filter and ranking; K:71 10(d)); the program's digest DOES judge merit, which Cogentic forbids its advisor (row 2) | — | already ours; Cogentic's "no opinion" limit DECLINED (the digest's merit judgment is read and quoted, K:68) |
| 20 | Termination — "Rounds continue until a draft clears verification or until the budget runs out." (§2); "When a candidate clears all verification, the orchestrator may continue to explore some remaining promising that may yield a better result, terminating once those avenues are exhausted." (§2.5; "remaining promising" is the paper's own wording) | PARTLY — unit stop lines (K:81 10(m); CH:34); a graded result pulls the next session's budget into follow-ups (K:71 10(d)). A budget stop for the TARGET is excluded by K:67 ("never paces itself to a horizon") and S:39 (order 10) | — | already ours (10(d)); budget-based termination DECLINED |
| 21 | Comparator — "Upon termination, a comparator selects the strongest verified proof" (§2.5) | PARTLY — dig:533 §F ranks candidate next units; no case on the record of several verified proofs of one claim | no evidence on the record | DECLINE (no use case) |
| 22 | Formal writer and a final audit against the accepted proof — "a formal writer expands it into a complete manuscript, and a final verification audit checks the compiled document against the accepted proof to ensure no errors were introduced during exposition." (§2.5) | YES — `results/arxiv/DE-INTERNALIZATION.md`:91–100 (an integrity lens "diffed every numeric literal, every inline and display math span and all 35 theorem-family blocks … no mathematics changed"); `check-submittable.sh` (:281) | — | already ours |
| 23 | Output readable without the run — "so that it can be read and checked by domain experts who knows nothing about the run that produced it." (§2.5; "knows" is the paper's) | YES — S:44 order 13; K:92 item 17; `DE-INTERNALIZATION.md`:280 ("Nothing in them refers to a document the reader cannot open.") | — | already ours |
| 24 | Small call budgets, reported — "used O(100) calls to Gemini for most problems, and O(1000) for the hardest" (§1) | PARTLY — lean-budget rules (K:67); the waste line (K:83). No per-target count of agents spent | no evidence on the record that the missing count cost anything | DECLINE as a rule (at most: the waste line may state the wave's agent count) |
| 25 | Statement only, no hints — "A key feature of the system is that it only needs a problem statement, without any expert hints, and can work autonomously until it produces a result in the form of a paper." (§1); "did not provide any hints to the system" (§3.5). The appendix qualifies this: A.4 prescribes a fallback target, A.5 says "if the lower bound PoA is of the form 2 − Ω(1/n) then an idea upper bound should be of the form 2 − O(1/n)" | n/a — the program writes its own charters | — | DECLINE (nothing transfers; the claim is weaker than stated) |
| 26 | Problems inside the authors' expertise; human experts verify — "That was possible because of how the problems were chosen: they come from areas the authors work in." (§4); "domain experts subsequently verified every proof." (§3) | NO — no human domain referee; the dual-model rule substitutes (S:36 order 7; S:41 order 11(c)) | — | DECLINE (no expert available; a limit to state, not a rule) |
| 27 | A faithful machine score — "What each of these approaches requires is a cheap, faithful, and machine-computable score." … "However, not every problem is amenable to such an approach." (§1) | PARTLY — exact-data pattern units and certificates (CH:28–29; S:42 order 12(b) "computation at scale, pattern discovery in exact data") | — | adopt only where a score is faithful to the target (checked in §8 against the study's staged item) |
| 28 | Generation outruns reading — "A system like this can produce candidate results faster than they can be read, and the gap widens as the compute budget grows." (§4) | PARTLY — the backlog is on the record: S:123 ("Owed at the open of Session 42: the orchestrator's `read-F.md` for U1, U5, U2, U4 and the reconciliation of the two waiting reads (U1: 17 pairs; U5: 21 pairs)"); of lemmaB-s41's seven units only U3 and U6 hold both reads (folder listing); "HARVEST FIRST" puts reads before new work (S:123) | YES — the backlog itself; U4 and U2 reported after the close with no read (S:123 updates of 18:29 and 18:34 IST) | ADOPT in a lean form: size a wave to the reads the orchestrator can do in the same session, or launch the readers with the writers |
| 29 | Formalize to settle correctness — "One possibility is to formalize in a proof assistant such as Lean (Moura and Ullrich, 2021), so that correctness is settled mechanically. However, human understanding of the solution might lag behind." (§4) | YES — K:73 (10(f)), K:76 (10(j)); S:124 item 1(v) | — | already ours |
| 30 | Weaker target first (prompt A.4) — "If you cannot prove the factor 3 approximation, you should first try to prove that this is a factor 4 approximation, then try to strengthen it." (App. A.4; the run landed at 3.52, between the two rungs, Thm 4) | YES — CH:25 (U3: "first E = o(x), then E = O(x^{θ₀}) for some θ₀ < 1"); the ladder rule K:69 (10(b)) | — | already ours |
| 31 | Prove or disprove (prompt A.5) — "Prove or disprove that this mechanism has a PoA of 1.5." (App. A.5) | YES — CH:32 ("Close with a theorem-shaped statement: 'Y holds' or 'proof class X cannot yield Y because Z'"); K:70 (10(c)) | — | already ours |
| 32 | Name the source to read first (prompts A.2, A.3, A.5) — "Read this paper: https://arxiv.org/abs/2307.03844." (App. A.2) | YES — CH:5–8 | — | already ours |
| 33 | Agent-launched literature search (prompt A.3) — "Please also have the lit reviewers do a deep search so you understand the landscape. Feel free to launch as many lit reviewers as you feel you need." (App. A.3) | NO — agent-spawned children are refused on the record (K:84, from the Cognition study's §C) | — | DECLINE the open-ended spawn; row 8's lean form covers the need |
| 34 | Simplifying assumption, removed afterward (A.5) — "Note that the prompts asked the system to make some mild assumption. We removed the assumption by asking Gemini to look at the output proof and modify it accordingly." (App. A.5) | PARTLY — the ladder (K:69); hypotheses tested for necessity in reads (RBO:26 item (b): "is discreteness used anywhere") | — | already ours in substance |
| 35 | Public, updated results list — "We maintain an up-to-date list of results obtained with Cogentic, with links to their companion papers, at https://sites.google.com/view/cogentic." (§3) | PARTLY — the landing page (S:126 item 3(iii), `results/x67-landing-s41/`); deposited archives with hashes (S:44 order 13) | — | already ours (wording is the sponsor's call, S:126) |
| 36 | Report being superseded — "Subsequent to the companion paper, Sakaue (2026b) obtained a tight O(√d) bound." (§3.1) | YES — zoo riders and novelty relabels (dig:509–510, R4; `BARRIER-ZOO.md` riders) | — | already ours |
| 37 | Humans finish the exposition — "We checked the argument, wrote the exposition around it, and in some cases carried it further than the harness had." (§4) | n/a — the orchestrator's read and reconciliation play this part (`lemmaG-s39/read-F.md`:22–29) | — | no transfer |

**Blind-pass summary.** 37 rows. Already ours: 1, 3, 7, 9, 10, 12, 13, 15, 16, 18, 22, 23, 29, 30, 31, 32, 35, 36 (and 19, 20, 34 in substance). Adopt in a lean form, each with a recorded failure behind it: **8** (a literature agent per wave, on-disk corpus first), **11** (a cross-unit blind-spot pass inside the digest), **14** (a register of dual-read statements), **17** (error classes across waves, turned into one-line warnings in the next charter and read brief), **28** (wave size matched to the reads). Decline: 2 (conflicts with orders 11(c), 12(d)), 4, 5 (per-prover form), 6, 21, 24, 25, 26, 33. Two cautions on the paper itself: Fig. 1 and §2.1 disagree on who writes the briefings (advisor vs. summarizer), and the "no expert hints" claim of §1 and §3.5 sits beside prompts that carry hints (A.4, A.5).

## §2 Quotes from the paper — checked character by character

Method: every double-quoted string in the study (102 of them) was searched in the `pdftotext` text of the PDF, whitespace and line breaks joined, "…" treated as an elision (each part must occur, in order), math-italic letters (𝑂, 𝑑) read as plain letters. 48 match exactly and one more after typography (l. 33); of the 53 that do not match, 49 are quotations of the program's own files (checked in §3) or fragments between two quotations, and four are paper quotations, listed below with l. 33. Every other paper quotation, including all quotations in P1–P10, §A, §B, §C, §D and E.1, matches the PDF exactly.

| Line | Study's text | PDF's text | Kind |
|---|---|---|---|
| 33 | "A separate verifier reads all of the round's drafts side by side" | "round’s" (right single quotation mark, U+2019) | typography only; the study's straight apostrophe is acceptable, listed for completeness (no pair) |
| 54 | "… rarely has the context window to review and synthesize log trends itself" | the same words; the sentence crosses the page break after "across" (p. 4 → p. 5) | none — an artifact of the page break |
| 136 | "Proofcouncil: An LLM agent for solving open mathematical problems" | "Proofcouncil: An llm agent for solving open mathematical problems" | case changed (minor m1) |
| 136 | "AI co-mathematician: Accelerating mathematicians with agentic AI" | "Ai co-mathematician: Accelerating mathematicians with agentic ai" | case changed (minor m2) |
| 136 | "Advancing mathematics research with AI-driven formal proof search" | "Advancing mathematics research with ai-driven formal proof search" | case changed (minor m3) |

Arxiv numbers in E.2 (2609.15983, 2607.09474, 2602.10177, 2605.06651, 2605.22763) all match the reference list. The local PDF's SHA-256 prefix `f19883ba88420612` matches the study's header.

**Quotations that are exact but used for a claim the paper does not make** (the content check, not the character check):
- §D (l. 130): "rarely has the context window" (§2.4) is the paper's reason why the ADVISOR is a separate agent. The paper does not take its orchestrator "out of verification altogether": the orchestrator "evaluates verifier consensus" (§2, Components), and the paper gives no reason tied to the context window for its rule that the orchestrator "does not perform mathematical derivations itself". → F9.
- §0 (l. 9): "it only needs a problem statement, without any expert hints" is quoted without the appendix that qualifies it: A.4's prompt names two reference papers and a fallback ("If you cannot prove the factor 3 approximation, you should first try to prove that this is a factor 4 approximation"), and A.5's second prompt names the expected form ("if the lower bound PoA is of the form 2 − Ω(1/n) then an idea upper bound should be of the form 2 − O(1/n)"). → m5.
- P1 (l. 19–20): the paper's provers DO receive method suggestions — from the summarizer, which "gives suggestions for possible next steps, based on what has worked and what has not" (§2.1) — and from the problem-setter's prompt (A.4 names the duality paper that the proof of Thm 4 builds on). Only the orchestrator and the advisor are barred. The one-sentence gloss on l. 20 is right about the allocator; rule (r)'s free unit ("no method … no expected answer") is stricter than anything in the paper. → §7 (r).

## §3 Citations of the program's record — recounted

**Confirmed** (recounted or read at the line): K:67 and K:78 as the sources of 10(a)–(j) and 10(k)–(o); S:41 "the orchestrator does that check in person" and S:42 "is a GAP until read at the line by the orchestrator"; S:24 contains "the orchestrator's construction" and "the reads of U1, U5, U2, U4 by the orchestrator are owed", and S:24 is 25,069 bytes ("a 25 kB header line" ✓); E.12 lists exactly five brief/charter errors caught by units plus the uoff stop trigger "caught by the reads, not by the unit" (dig:524–531; "five … and a sixth" ✓); K:85 "invest in steering artifacts … not in fan-out" ✓, and it is the NS study's refusal (`openai-ns-2026/process-lessons.md`:48) ✓; RBO steps 2–4 quotes ✓; `lemmaG-s39/read-F.md`:3 and `U3-firstbound/read-F.md`:3 and :18 quotes ✓; sixteen units hold both `read-F.md` and `read-O.md` since Session 37 ✓ (folder count: three of novel-wave-s37, conj-O-s38, qcond-s38, dz-half-s39, fejer-form-s39, lemmaG-s39, qtwin-s39, u-offsurgery-s39, four of Session 40, U3 and U6 of lemmaB-s41); §E.1–E.7 read-O FIX-FIRST items 3 + 4 + 14 + 5 + 2 + 6 + 2 = 36 ✓, read-F's only ones uoff F1–F2, both in read-O ✓ ("one unit (2 items …)" ✓); "were not checked" (`lemmaG-s39/read-F.md`:23) ✓; `BARRIER-ZOO.md` has 64 entry headings (I 11, II 5, III 21, IV 22, V 5) ✓; S:124 "CLOSED ROUTES, with reasons on the record:" ✓; "ATTEMPT k — breaks at: …" (K:91) ✓; "implicit and lossy" is the NS study's §3 (`openai-ns-2026/process-lessons.md`:20) ✓; `d1-m3/LEDGER.md` shape ✓; CH:8 quote ✓; R2, R3, R4, R5, R6 as described (dig:461, 479, 509, 518, 522) ✓; "G with proved T-parts" occurs (S:24, S:424) ✓; S:127 "over 560 kB" ✓; the three digests' errata sections (s36 §E "Errata of the orchestrator's Session-36 seeds", s37 §E, s39 §E) ✓; kind (1)–(5) items E.1 F2, E.4 F5, E.6 F2, E.10 F2, R4, U5 F7, E.3, E.2 F4, E.9 F2, E.11 F1, E.12, E.9 F1, E.4 F1, E.8 F2, E.10 F1, E.11 F2, U5 F5–F6, E.6 F5, R1, R2–R6 all say what the study says they say ✓; the Session-39 numerical counterexample withdrawn in Session 40 (LOG:2208, 12:17 IST 2026-10-01) ✓; DE-INTERNALIZATION l. 91–100, 276–281, 288 quotes ✓; the Haglund paper refereed in Session 38 with 41 pairs applied (LOG, Session 38, 01:57 IST), de-internalized in Session 39 (S:44 order 13(e)) and checked after that only by `check-submittable.sh` ✓; Theorem D "conditional only on Meyer's theorem (Q4)" in qcond's pre-reader NOTE (l. 304) and unconditional after the Session-39 read ✓; U7 NOTE §0: "to 10¹⁰ in 2 and 1 minutes, plus twelve variants", and §5.6's class "linear combination of E at the scales x/p_q, q ≤ 4" ✓; `U3-firstbound` CH:25 quote ✓; S:123 "Theorem 4.1 (the power bump) and Cor. 4.2 FIRST, …" ✓.

**Mismatches** (each becomes a pair in §4 or §5):

| # | Study | Record | Pair |
|---|---|---|---|
| a | l. 14: the one-target loop is "the shape the program has itself run since Session 36" | Sessions 36–39 ran multi-TARGET waves: s36 four seeds (Lee–Yang, staircase, fingerprint, tournament; `novel-wave-s36/WAVE-CHARTER.md`:19–37), s37 three seeds on three questions, wave 3 eleven units on at least eight different questions (dig:21–300; fgT and fgC share S8, qcond and qtw share Q_cond). One object with two units first in Session 40 (`free-greedy-s40/CHARTER.md`:3); seven units on ONE target first and only in Session 41 (`lemmaB-s41`) | F1 |
| b | l. 28: the charter "by 10(a) must quote ONE consolidation digest" — presented as how history reaches units | `lemmaB-s41/CHARTER.md` (16:45 IST) contains no digest (grep "digest": 0); the wave-3 digest was LAUNCHED at 16:57 and DONE at 17:28 (LOG, Session 41), while the seven units ran | F2 |
| c | l. 49: a salvage ledger exists "For one direction only" | adjudication salvage lists, "mandatory for any successor", for A1, A2, B1, C1, A4, C3 (`directions/A2-richer-functionals.md`:75; `results/adjudication-{A1,B1,C1}.json`; LOG:82, 104; `BARRIER-ZOO.md`:465) | F3 |
| d | l. 56: "nothing carries them into the next charter or reader brief … neither has a line that came from an errata section" | CH:8 carries fgT read-O F1 into the charter as binding (dig:505–506: "binding on lemmaB-s41 (CHARTER §0 item 3)"); RBO:28 target (d) makes the reader refit a sup-E table — a kind-(2) check, for one unit | F4 |
| e | l. 56: on disk "in four cases", in print "in three more (… Diamond–Zhang Thm 6.13: U3)" | Diamond–Zhang 2016 was on disk since Session 39: `results/dz-half-s39/sources/t-50-diamond-zhang-2016-book.txt`, the file the orchestrator cites at the page (`U3-firstbound/read-F.md`:17). Five on disk, two in print (Bateman–Grosswald was fetched by the reader, `free-greedy-s40/theory/read-O.md`:210–211) | F5 |
| f | l. 63: "Session 41's seven units converged on one stuck object" | S:124: "THE OBJECT BOTH SIDES REDUCED TO … (U7 Cor. 5.4) … (ORCH-NOTES O4; U5's gap)" — two units and the orchestrator's notes | F6 |
| g | l. 37, l. 130: standing order 11 is "for the sponsor's reasons of usage" / "a question of usage" | S:41 and LOG:2059 record the order with no reason given | F7, F8 |
| h | l. 35: "the dual read is one full read plus one partial read" | `free-greedy-s40/theory/read-F.md`:18: "NOTE read whole … (440 lines)"; partial reads are real (`lemmaG-s39`, `U3-firstbound`) but not the rule | F12 |
| i | l. 35: read-O "runs 30–50 kB", read-F "runs 2–10 kB" | over the sixteen units: read-O 31,459–51,605 bytes (qtwin-s39 51.6 kB), read-F 2,130–11,120 bytes (novel-wave-s37/beurling-frontier 11.1 kB) | m8, m9 |
| j | l. 49: "NOTE files of 28–54 kB" | the theorem NOTEs named run 28,172 (U3) to 57,386 bytes (`free-greedy-s40/theory/NOTE.md`, which holds Theorem 1.6) | m10 |
| k | l. 57: BRIEF-WARNINGS "Seeded in this side-session" | no `rh-program/BRIEF-WARNINGS.md` exists (nor `THEOREM-LEDGER.md`) | m11 |
| l | l. 22: the charter reader "launched WITH the units … (Session 41 did this once for ORCH-NOTES.md …)" | the reader checked ORCH-NOTES O1, O2, O8 only — the notes, not the charter's §2 claims — launched 17:05 IST, after the units (`orch-notes-read-O.md`:1–3; LOG 17:05) | m12 |
| m | l. 9: "The five prompts … each is a few lines" | six prompts (A.5 prints two); A.4's runs about 25 lines | m4 |

## §4 FIX-FIRST pairs (OLD quoted exactly from `process-lessons.md` at af9f27d0…; line numbers at that hash)

**F1** (l. 14) — the one-target shape is one stream old, not six sessions (§3 a); rule (r) and the target tables of (q) have one instance behind them.
OLD: which is the shape the program has itself run since Session 36 (waves of up to ten units on one charter, dual reads, a consolidation digest; `results/lemmaB-s41/CHARTER.md` is the latest instance).
NEW: which is the shape of the program's stream `lemmaB-s41` (Session 41: seven units on one target, dual reads, the orchestrator's reconciliation; `results/lemmaB-s41/CHARTER.md`), the only stream of that shape on the record — the waves of Sessions 36–40 put up to eleven units on one charter, but on different targets.

**F2** (l. 28) — the latest charter quoted no digest; the wave-3 digest ran after it (§3 b). This also bears on (p), whose warnings travel through the digest.
OLD: The history, though, reaches every unit through ONE reading: the orchestrator's charter, which by 10(a) must quote ONE consolidation digest (`KICKSTART.md` l. 68).
NEW: The history, though, reaches every unit through ONE reading: the orchestrator's charter, which by 10(a) must quote ONE consolidation digest (`KICKSTART.md` l. 68) — and in Session 41 it quoted none: `lemmaB-s41/CHARTER.md` was written at 16:45 IST, the wave-3 digest was launched at 16:57 and done at 17:28, while the seven units ran.

**F3** (l. 49) — a salvage step is on the record under another name (§3 c).
OLD: For one direction only. `results/d1-m3/LEDGER.md` is exactly this shape for D1's zero-free boxes
NEW: In two places. The adjudications of Sessions 4–6 extracted "Salvage (from adjudication, mandatory for any successor)" from the directions they killed (A1, A2, B1, C1, A4, C3: `directions/A2-richer-functionals.md` l. 75, `results/adjudication-*.json`) — the paper's salvage step at the level of a direction, not continued in the waves; and `results/d1-m3/LEDGER.md` is exactly this shape for D1's zero-free boxes

**F4** (l. 56) — the premise of rule (p) was stated as an absolute and is false as stated (§3 d); (p) survives on the narrower premise.
OLD: Nothing sorts them by kind, and nothing carries them into the next charter or reader brief: the reader brief is redrafted each session with per-unit targets (`READ-BRIEF-O.md`), the charter's "Rules for every unit" carries labels and operating rules, and neither has a line that came from an errata section.
NEW: Nothing sorts them by kind. Single errata reach the next charter by hand (`lemmaB-s41/CHARTER.md` §0 item 3 carries fgT's read-O F1 as binding), and a reader brief may carry one kind's check for one unit (`READ-BRIEF-O.md`, target (d) for `free-greedy-s40/compute`: refit the sup-E table and "state what the data can and cannot exclude"); but no kind is carried forward as a standing line for every writer and every reader.

**F5** (l. 56) — Diamond–Zhang was on disk (§3 e); the count that motivates naming on-disk core papers is five, not four.
OLD: ALREADY ON DISK in four cases (Hilberdink 2012 in three units: E.1 F2, E.4 F5, E.6 F2; Olofsson 2010: E.10 F2), in print in three more (Bateman–Grosswald 1964: R4; Hilberdink 2011, fetched by the reader: `lemmaB-s41/U5-obstruction/read-O.md` F7; Diamond–Zhang Thm 6.13: U3)
NEW: ALREADY ON DISK in five cases (Hilberdink 2012 in three units: E.1 F2, E.4 F5, E.6 F2; Olofsson 2010: E.10 F2; Diamond–Zhang 2016 Thm 6.13 for U3, on disk since Session 39 at `results/dz-half-s39/sources/t-50-diamond-zhang-2016-book.txt`), in print in two more (Bateman–Grosswald 1964: R4; Hilberdink 2011, fetched by the reader: `lemmaB-s41/U5-obstruction/read-O.md` F7)

**F6** (l. 63) — the evidence for rule (s) overstated (§3 f); the rule's trigger ("two or more units") is still met.
OLD: Session 41's seven units converged on one stuck object
NEW: Two of Session 41's units and the orchestrator's notes converged on one stuck object (U7 Cor. 5.4, U5's gap, ORCH-NOTES O4)

**F7** (l. 37) — a reason attributed to the sponsor that the record does not give (§3 g).
OLD: standing order 11(a), (c) fixes it, for the sponsor's reasons of usage.
NEW: standing order 11(a), (c) fixes it; the record gives no reason for the order (`STATUS.md` l. 41; `LOG.md`, 14:09 IST 2026-09-30).

**F8** (l. 130) — the same attribution, second place.
OLD: because it is a question of usage;
NEW: because the order is the sponsor's and the record gives no reason for it;

**F9** (l. 130) — a quotation used for a claim the paper does not make (§2).
OLD: (3) The paper takes its coordinator out of verification altogether because it "rarely has the context window" (§2.4);
NEW: (3) The paper keeps its coordinator out of mathematical derivation ("The orchestrator does not perform mathematical derivations itself", §2) while it "evaluates verifier consensus" (§2); its context-window sentence (§2.4) is the reason for a separate advisor, not for that rule;

**F10** (l. 134) — E.1 misstates the reduction it stages (CH:12–13): it drops r₀ > ρ and turns (B), an asymptotic exponent bound, into a threshold.
OLD: Theorem 1.6 reduces the refutation of Conjecture U to exhibiting a discrete never-undershooting system whose integer error stays under a threshold
NEW: Theorem 1.6 reduces the refutation of Conjecture U to exhibiting a discrete system with (A) N(u) − ρu ≥ r₀ > ρ for all u ≥ 1 and (B) N(u) − ρu = O(u^θ) for some θ < ½·r₀/(r₀ + ρ) — an asymptotic bound on an exponent, which no finite run certifies

**F11** (l. 134) — no evaluator checks a statement for all u ≥ 1; (A) has to hold by construction.
OLD: checks (A) exactly and returns a score
NEW: checks (A) exactly up to X (for all u, (A) must hold by construction, as `lemmaB-s41/CHARTER.md` §3 U1 requires) and returns a score

**F12** (l. 35) — overgeneralized (§3 h); P3's "Two FULL reads: no" and the isolated check of (q) lean on it.
OLD: The record shows the dual read is one full read plus one partial read.
NEW: The record shows the dual read is often one full read plus one partial read: the orchestrator's read was partial in `lemmaG-s39` and `U3-firstbound`, whole in `free-greedy-s40/theory` (`read-F.md` l. 18).

**FIX-FIRST total: 12 pairs (F1–F12).** Claims on which the study rests a rule and which are false on the record as written: F4 (rule (p)'s premise), F6 (rule (s)'s evidence), F1 (rule (r)'s scope), F12 (rule (q)'s isolated check); F2 bears on the route by which (p)'s warnings would travel.

## §5 Minor pairs (OLD quoted exactly at af9f27d0…)

**m1** (l. 136) — title as printed in the paper's reference list.
OLD: Proofcouncil: An LLM agent for solving open mathematical problems
NEW: Proofcouncil: An llm agent for solving open mathematical problems

**m2** (l. 136) — the same.
OLD: AI co-mathematician: Accelerating mathematicians with agentic AI
NEW: Ai co-mathematician: Accelerating mathematicians with agentic ai

**m3** (l. 136) — the same.
OLD: Advancing mathematics research with AI-driven formal proof search
NEW: Advancing mathematics research with ai-driven formal proof search

**m4** (l. 9) — six prompts, not five; A.4 is not a few lines.
OLD: The five prompts are printed in Appendix A; each is a few lines.
NEW: The prompts are printed in Appendix A — six for the five problems (A.5 has two); the longest (A.4) runs about twenty-five lines.

**m5** (l. 9) — the paper's own appendix qualifies the quoted claim (§2 of this read).
OLD: "it only needs a problem statement, without any expert hints";
NEW: "it only needs a problem statement, without any expert hints" — a claim Appendix A qualifies (A.4 names two reference papers and a fallback target; A.5's second prompt names the expected form of the bound);

**m6** (l. 14) — the paper says O(1000) for the hardest.
OLD: closed in hundreds of model calls and checked by experts.
NEW: closed in O(100) model calls for most problems and O(1000) for the hardest, and checked by experts.

**m7** (l. 23) — the paper has no ablation (the study's own §0); "costs nothing" is not on the page.
OLD: taking mathematics away from it costs nothing.
NEW: the paper reports no cost of taking mathematics away from it (it has no ablation, §0).

**m8** (l. 35) — recount over the sixteen units (§3 i).
OLD: runs 30–50 kB with re-derivations
NEW: runs 31–52 kB with re-derivations

**m9** (l. 35) — the same.
OLD: runs 2–10 kB (the sixteen units read both ways since Session 37)
NEW: runs 2–11 kB (the sixteen units read both ways since Session 37)

**m10** (l. 49) — recount (§3 j).
OLD: NOTE files of 28–54 kB
NEW: NOTE files of 28–57 kB

**m11** (l. 57) — no `BRIEF-WARNINGS.md` exists (§3 k).
OLD: Seeded in this side-session with the five kinds above, each with its evidence.
NEW: To be seeded, when the rule is adopted, with the five kinds above, each with its evidence (no such file exists yet).

**m12** (l. 22) — what Session 41 actually did (§3 l).
OLD: (Session 41 did this once for `ORCH-NOTES.md`: `results/lemmaB-s41/orch-notes-read-O.md`).
NEW: (Session 41 did this once, for three of the orchestrator's notes — O1, O2, O8, not the charter's §2 — launched at 17:05 IST, after the seven units: `results/lemmaB-s41/orch-notes-read-O.md`).

**m13** (l. 65) — no zoo entry says this.
OLD: by the zoo's own account, mostly places where no printed tool reaches;
NEW: on the record so far, often places where no printed tool was found;

**m14** (l. 111) — Theorem D's condition was a citation removed by reading the source, not an assumption removed by a new proof (qcond pre-reader NOTE l. 304; read-O F1).
OLD: Conditional first, hypothesis removed later** (Theorem D; the K-conditional theorems) is A.5's "mild assumption", removed in a follow-up.
NEW: Conditional first, hypothesis removed later** (the K-conditional theorems) is A.5's "mild assumption", removed in a follow-up; Theorem D is a different case — its condition was a quoted theorem, removed in Session 39 by reading Meyer at the page.

**m15** (l. 112) — the zoo is not all program proofs.
OLD: the program proves the obstruction for a proof CLASS.
NEW: the zoo records the obstruction for a proof CLASS (59 of its 64 entries; Group V's five are process barriers, and Group III's are literature-certified rather than proved here).

**m16** (l. 125) — stop conditions were adopted from the Cognition study's failures, not the program's.
OLD: were each bought with a failure;
NEW: were each bought with a failure, the program's own or (for stop conditions, 10(m)) one the Cognition study records;

**m17** (l. 21) — of the five, three are mathematical, one numerical, one a wrong expectation (dig:524–529).
OLD: the wave-3 digest lists five mathematical errors in the orchestrator's briefs and charters that units had to catch
NEW: the wave-3 digest lists five errors in the orchestrator's briefs and charters (three mathematical, one numerical, one a wrong expectation) that units had to catch

**m18** (l. 42) — "from memory" is the NS study's pre-10(a) description; the current charter points to files (CH:5–8).
OLD: It is rewritten by the orchestrator, from memory of the harvest, each time a charter is drafted
NEW: It is rewritten by the orchestrator each time a charter is drafted

**m19** (l. 14) — tone, borderline (standing order 14's spirit: a clause whose job is to disclaim, not to inform). Optional.
OLD: The program's target is not of that kind, and nothing below assumes that the loop that closes such a question closes anything here.
NEW: The program's target is not of that kind.

**Minor total: 19 pairs (m1–m19).** Tone check (G): no British spelling outside quotations ("Towards" at l. 136 is a title); none of "clearly / obviously / easy to see / well known"; no sentence about whether the Riemann hypothesis is proved, open or untouched (m19 is the nearest).
