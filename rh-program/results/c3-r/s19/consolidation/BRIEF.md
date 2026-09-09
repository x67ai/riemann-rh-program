# Consolidation step (KICKSTART Part 2 item 10(a)) — C3-r, streams of Sessions 14–18, feeding the Q-S4⁗ brief

**Written:** 2026-09-09 20:44 IST, Session 19 (orchestrator). **Agent:** one consolidation agent. **Output:** `results/c3-r/s19/insights-digest.md` — write it in chunks AS YOU GO (a section per stream, appended the moment it is drafted), never at the end; the orchestrator harvests whatever is on disk if you die.

## Why
The next stream is Session 17 queue item 3, the **Q-S4⁗ literature decision**: can a compact lamination by Riemann surfaces contain a finite-type χ = +1 leaf (≅ D) inside a measure-null saturated set of hyperbolic preserved leaves that is the non-transverse set of a foliated flow; manifold case with rank_Q H₁(M ∖ N; Q) = ∞. Instruments now ON DISK: Duminy's theorem (Cantwell–Conlon 2002, `results/fetch-r4/a01-12-warsaw.md`), Hurder Problem 5.4 (r3s-29 §5), Ghys 1995 (silent — `a02-ghys1995.md`), Ghys 1999 (r3s-35, cite by section), Epstein 1976 (r3s-34), Candel 1993 (r3s-31), the textbooks (`a08-textbooks-closed-leaf.md`). Item 10(a) says: before that brief is written, one agent digests every stream's on-disk results so the brief quotes the digest instead of re-deriving or, worse, forgetting.

## Inputs (read in this order; quote with file + section/line; nothing from memory)
1. `results/c3-r/m2c-feasibility-ledger.md` from `## §16.` (line 317) to the end — §16, §16-bis, §16-ter (esp. §8.2–§8.4), §16-quater, §16-quinquies.
2. `directions/C3-geometric-substrate.md` §"Current frontier" (line ~202 onward) and the work log from 2026-09-05.
3. Session-16 Q-S4′ stream: `results/c3-r/s16/qs4prime/scout-F.md`, `scout-O.md`, `adjudication.md` (§5 "next decidable question" and §7 novelty ledger, §8 honesty), `refute-F.md`, `refute-O.md`, `refute-adjudication.md` (§1.5–§1.6, §8), `f1-check-O.md` (§0 verdict table, §4.4 hypotheses, §9), `f1-check-C0-seminorm-s17.md`.
4. Session-16 novelty stream: `results/c3-r/s16/novelty/sweep-F.md`, `sweep-O.md`, `adjudication.md` (§0 table, §1 N-A…N-G with the 2026-09-09 dated blocks, §3 required wording, §6 honesty).
5. Zoo: `BARRIER-ZOO.md` IV.11–IV.15 (with their dated blocks); `results/c3-r/s16/zoo-entries-read-O.md`.
6. Session-18 ingest reports bearing on the gate: `results/fetch-r4/a01-12-warsaw.md`, `a02-ghys1995.md`, `a03-kopei.md`, `a04-leichtnam-cm387.md`, `a08-textbooks-closed-leaf.md`, `a11-deninger-singhof.md`, `a12-calegari-kmnt.md`, `a09-identity-p3-bonus.md` (Ghys 1999 / Leichtnam 2008 identity); and `results/fetch-r4/RECORD-CORRECTIONS-s19.md` (what was corrected on 2026-09-09 — the digest must not reintroduce a corrected wording).
7. Session 14 (only where the s16 files point back): `results/c3-r/s14/qstar-adjudication.md` §4, §9; `s14/novelty/adjudication.md` §0–§2.

## Output format — `results/c3-r/s19/insights-digest.md`
Header: what this is, the date, the input list actually read (with what you did NOT read, per standing order 5 honesty).
**One section per stream** — (A) Q-S4′ scouts + adjudication; (B) the adversarial refute pass; (C) the Opus check f1-check-O + the C⁰ seminorm note; (D) the novelty sweep + adjudication; (E) the zoo entries IV.11–IV.15; (F) the Round-4 ingest as it bears on the gate — each section EXACTLY:
- **Three most useful findings** (each: one sentence, the exact statement or number, file + section; mark PROVED / ADJUDICATED / RECALLED / AGENT'S INFERENCE as the source marks it).
- **The most useful failure** (what was tried and died, why, the file + section).
- **What the next stream should borrow** (a device, a definition, a citation, a table — concrete).
**Closing sections:**
- **G. The state of the Q-S4⁗ gate in one page**: the exact question as re-posed in ledger §16-ter §8.4 + the 2026-09-09 block; the instruments on disk with their exact hypotheses (Duminy Thm 1.1 with the standing hypotheses of Cantwell–Conlon p. 225, Hurder 5.4 as printed p. 226, Ghys 1995 Thms A/A′/B, Epstein 1976 §2, Candel 1993 Thm 4.1/Cor. 4.2, Candel–Conlon I Lemma 11.2.10 / Def. 4.3.3); what each can and cannot decide; the "next decidable step" (semiproperness of the archimedean leaf — quote A-IV's structure from the refute adjudication).
- **H. Refutation-shaped statements already on the record** (KICKSTART 10(c)): list every statement of the form "proof class X cannot yield Y because Z" or "Y holds" that Sessions 14–18 established for C3-r, verbatim or tightly paraphrased with its source and its dual-model status. These are the zoo's raw material and the brief's premises.
- **I. A proposed contract theorem for the gate (KICKSTART 10(g))**: write the Q-S4⁗ question as a contract theorem with numbered clauses (hypotheses = the S4′ + clause (0) axioms as printed; conclusion candidates = the two faces of the gate), each clause tagged with what discharges it (a printed theorem, a program theorem, or OPEN), a dependency chain, and the exact clause the next brief should aim to discharge. Lint your own text for "clearly / obviously / easy to see / well known" — none allowed.
- **J. What the Q-S4⁗ brief must quote** — a numbered list of ≤ 12 sentences the brief must carry verbatim (with sources), including every Round-4 correction that bears (Ghys 1995's actual subject; Duminy's hypotheses; Kopei without fixed points; Moore–Schochet Ch. III p. 57; Ghys 1999 by section).

## Rules
- Nothing from memory; every claim carries a file + section/line. Where the sources disagree, say so and which is binding (ledger and adjudications outrank scouts and sweeps; dated blocks outrank the text they follow).
- Do NOT re-derive mathematics and do NOT propose constructions (standing order 6 — literature decision first). Digest only.
- U.S. English. Stamp the file with the machine clock (`date`). Write in chunks; append a section as soon as it is drafted.
- Append a two-line progress note to `results/c3-r/s19/SHARED.md` when you start and when you finish (KICKSTART 10(e)).
- Return: a ≤ 3000-character summary and the path. The digest lives on disk.
