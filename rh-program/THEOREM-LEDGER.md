# Theorem ledger — the statements later work may cite, the statements known to be false, and what has been tried on a shared target

**What this file is.** The one register required by KICKSTART Part 2 item 10(q). `BARRIER-ZOO.md` records what whole proof CLASSES cannot do; the Instruments tables of the direction files (10(k)) record comparable QUANTITIES; this file records single STATEMENTS: what is proved and how far it has been checked, what is false and by which witness, and — where three or more units have worked on one target — the routes tried and where each broke. A charter cites rows by ID. Once a unit's rows are here, the row is the record of a statement's status, not the label inside the NOTE. In-house model: `results/d1-m3/LEDGER.md`.

**Opened 2026-10-03 (side-session; source: `results/external/cogentic-2026/process-lessons.md` P4, P5, dual-read). First rows L-001–L-007 entered 17:34 IST 2026-10-03 (the stream `haglund-conj4`, a side-session); the rows Session 42 owes for the stream `lemmaB-s41` are still to come.**

**Rules (binding).**
1. APPEND-ONLY. A row block is never edited after entry. A correction, an upgrade, a withdrawal or a new check is a new dated line under the row ("L-012/c1 …") that says what changed and why, or a new row that names the row it corrects. Only the Index table is kept current by hand; where Index and blocks disagree, the blocks win.
2. WHO AND WHEN. Every unit's NOTE §0 ends with its LEDGER ROWS in the row shape below — the statements of its close, the proved parts of a unit that closes as a gap or a kill, and every statement it shows false. The reads check the rows with the rest of the NOTE. The orchestrator enters them here in the same step in which it writes the unit's reconciliation, copying the reconciled text; a row is never restated after the reads. Since 02:42 IST 2026-10-03 (KICKSTART 10(y)) the LEDGER ROWS are the first part of one close block at the end of NOTE §0: LEDGER ROWS, then TOOL ROWS (`TOOLS.md`), then one line ASKED / DELIVERED — what the brief asked, what was delivered, and every restriction the unit put on the problem that the brief did not, with its reason.
3. SELF-CONTAINED. The statement names every hypothesis and uses only notation defined in "Definitions" below or in the row itself. A statement that cannot be made self-contained in about twenty lines gets a row that points to its charter and says so.
4. KINDS. PROVED · CONDITIONAL (on named rows or named open statements; the row LEADS with the open hypothesis and says in one clause how it stands to the target — equivalent, stronger, weaker with the reason, or not known: `BRIEF-WARNINGS.md` W3) · NUMERICAL (the range and the producers, pointing to its Instruments row, which holds the value; never an exponent — `BRIEF-WARNINGS.md` W2) · EXCLUDED (false; the witness and where it is checked) · WITHDRAWN (with the row or read that withdrew it).
5. CHECKS, recorded per row as they happen: writer · read-F (with the sections it covered) · read-O · Lean. "Dual-read" is never written without the sections.
6. NO BACKFILL CAMPAIGN. A result older than this file gets its row when a charter first cites it; the orchestrator writes that row from the reconciled NOTE and marks it "backfilled" — an index entry: the charter cites the source through it, and the row's wording is checked by the next read that uses it.
7. STATUS keeps its one-line results and adds the row IDs; charters cite row IDs.
8. TARGETS. Where three or more units share one target, the target has a table below: one row per unit, entered at the unit's reconciliation. A target that is restated opens a new table that names its predecessor.

## Index

| ID | short name | kind | checks | source |
|---|---|---|---|---|
| L-001 | the pencil Ξ_k + tΦ_{k+1} is Ξ minus a positive level | PROVED | writer; read-O ✓ | `results/haglund-conj4/NOTE.md` §1 |
| L-002 | real zeros of the pencil: lobes, parity, and the criterion for staying real | PROVED | writer; read-O ✓ after F1 | `results/haglund-conj4/NOTE.md` §2 |
| L-003 | a lift-off forces −(log L_t)″ ≥ Σ_γ[…] | CONDITIONAL (zeros of Ξ real) | writer; read-O ✓ | `results/haglund-conj4/NOTE.md` §2 |
| L-004 | frozen level: zeros of Ξ − c descend and land at the top of their lobe | CONDITIONAL (zeros of Ξ real and simple); in print in substance | writer; read-O ✓ after F2 | `results/haglund-conj4/NOTE.md` §3 |
| L-005 | Φ_n is nearly constant on a fixed disc | PROVED | writer; read-O ✓ | `results/haglund-conj4/NOTE.md` §4 |
| L-006 | an off-axis zero of Ξ with Im Ξ′ > 0 forces an ascending zero of the pencil for all large k | PROVED | writer; read-O ✓ | `results/haglund-conj4/NOTE.md` §4 |
| L-007 | census of Haglund's Conjecture 4: 535 branches, k ≤ 6 and k = 26, 27; real axis k ≤ 20 | NUMERICAL | A-track; B-track (k ≤ 3); orchestrator's comparison | `results/haglund-conj4/NOTE.md` §6 |

## Definitions

(Entered with the first rows that need them: D-01, D-02, … — one definition each, with the file and section it is taken from.)

- **D-01 (Haglund's objects; arXiv:0910.5228v1 (1)–(14); `results/haglund-conj4/NOTE.md` §1).** Ξ(z) = ξ(½ + iz). For n ≥ 1, φ̃_n(v) = 2y(2y − 3)e^{v/2 − y} with y = πn²e^{2v}, and Φ_n(z) = 2∫_0^∞ φ̃_n(v) cos(zv) dv (entire; equal to Haglund's (14)). Ξ_N = Σ_{n≤N} Φ_n; Q_N = Ξ − Ξ_N = Σ_{n>N} Φ_n. A positive lobe of Ξ is an interval between consecutive real zeros on which Ξ > 0; the central lobe is (0, γ_1).
- **D-02 (the pencil; Haglund p. 11; `results/haglund-conj4/NOTE.md`).** For k ≥ 1 and 0 ≤ t ≤ 1: F_t = Ξ_k + tΦ_{k+1}, u = 1 − t, L_t = uΦ_{k+1} + Q_{k+1}, S_k = Ξ_{k+1}/Φ_{k+1}. (D): along every branch of zeros of F_t in the open upper half-plane the imaginary part does not increase with t. (R): a real zero stays real as t increases. Haglund's Conjecture 4 is (D); (R) is in its lead-in.

## Rows

Row block (copy this shape):

    ### L-000 — <short name> [KIND]
    - Statement. <self-contained; hypotheses explicit; definitions by D-number>
    - Checks. writer (<model>, Session N) · read-F <sections, Session N> · read-O <✓ / pairs applied, Session N> · Lean <— / file>
    - Novelty. <label, with the printed core and page where there is one; single- or dual-checked>
    - Source. `<file>` §<section>, SHA-256 <first 16 hex> at entry
    - Depends on. <row IDs; printed theorems with page>
    - Entered. <HH:MM IST YYYY-MM-DD>, Session N.

    ### L-001 — the pencil is Ξ minus a positive level [PROVED]
    - Statement. (D-01, D-02.) For n ≥ 2, φ̃_n is positive, strictly decreasing and strictly convex on [0, ∞), and Φ_n(x) > 0 for every real x. For k ≥ 1, 0 ≤ t ≤ 1 and all complex z: F_t(z) = Ξ(z) − L_t(z); L_t(x) > 0 for real x; ∂F_t/∂t = Φ_{k+1}, positive on the real axis. At z with Φ_{k+1}(z) ≠ 0: F_t(z) = 0 ⟺ S_k(z) = u, and along a branch of simple zeros dz/dt = −1/S_k′(z).
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ (§1.0–1.3, side-session 2026-10-03) · Lean —
    - Novelty. On a printed core: the kernel properties are the program's paper (Zenodo 10.5281/zenodo.23071930, Theorem sandwich, proof termwise); Φ_2 > 0 on ℝ is Baccaro 2026 p. 3, and Φ_{k+1} > 0 for every k is in his repository record. The form "Ξ minus a positive level" was not found there (L-lit, one reader).
    - Source. `results/haglund-conj4/NOTE.md` §1, SHA-256 f308961ab85988c7 at entry
    - Depends on. the paper's Theorem sandwich; Haglund (6), (14).
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-002 — real zeros of the pencil [PROVED]
    - Statement. (D-01, D-02; k ≥ 1, 0 ≤ t ≤ 1.) (a) t ↦ F_t(x) is strictly increasing for every real x. (b) Every real zero of F_t lies in a positive lobe of Ξ; counted with multiplicity each positive lobe (γ_j, γ_{j+1}) holds an even number and the central lobe an odd number; the number of zeros in (0, ∞) is finite and odd. (c) {x : F_t(x) > 0} increases with t. (d) At a real zero of multiplicity 2 where F_{t_0} ≤ 0 locally, a conjugate pair arrives on the axis; where F_{t_0} ≥ 0 locally, a pair leaves it; at a real zero of multiplicity ≥ 3 at least one pair leaves just after t_0. (e) (R) holds for k if and only if every critical point of x ↦ S_k(x) on the real axis with value in (0, 1] is a non-degenerate local maximum.
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ after F1 (the first form of (e) was false for degenerate critical points; 3 pairs applied) · Lean —
    - Novelty. New as a statement on a printed core (the paper's Corollary odd and Proposition tail; Baccaro 2026 Lemma 4.3 for k = 1) — reader's label, with L-lit's search.
    - Source. `results/haglund-conj4/NOTE.md` §2, SHA-256 f308961ab85988c7 at entry
    - Depends on. L-001; the paper's Proposition tail and Corollary odd.
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-003 — a lift-off forces an inequality between Ξ and the level [CONDITIONAL]
    - Statement. OPEN HYPOTHESIS: every zero of Ξ is real (the Riemann hypothesis; nothing weaker is shown to suffice). Then, if a pair of real zeros of F_{t_0} leaves the axis at x_0 (L-002(d)): −(log L_{t_0})″(x_0) ≥ Σ_{γ>0}[(x_0 − γ)^{−2} + (x_0 + γ)^{−2}]. Without the hypothesis the same argument gives (log Ξ)″(x_0) ≥ (log L_{t_0})″(x_0).
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ (§1.5) · Lean —
    - Novelty. Not searched beyond the stream's sources; an elementary consequence of L-002 and the Hadamard product.
    - Source. `results/haglund-conj4/NOTE.md` §2 (Proposition 2.3), SHA-256 f308961ab85988c7 at entry
    - Depends on. L-002.
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-004 — the frozen-level model [CONDITIONAL; in print in substance]
    - Statement. OPEN HYPOTHESIS: every zero of Ξ is real and simple (the Riemann hypothesis with simplicity). Then for a constant c > 0 the zeros of Ξ − c in the open first quadrant are one on each curve C_m (the points with arg Ξ = −2πm; a graph over the y-axis) for which the maximum M_m of Ξ on the m-th positive lobe is < c; as c decreases each moves down C_m with strictly decreasing imaginary part and reaches the real axis at the critical point of its lobe exactly when c = M_m. This is a statement about Ξ − c, NOT about the pencil, whose level L_t is not constant.
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ after F2 (two gaps filled; 2 pairs) · Lean —
    - Novelty. In print in substance: Titchmarsh, The Theory of Functions, §8.52 p. 266; Csordas–Smith, Michigan Math. J. 47 (2000), (2.5) p. 604 and (3.3)–(3.4) p. 609 (L-lit, checked at the page; above height ½ no hypothesis is needed).
    - Source. `results/haglund-conj4/NOTE.md` §3 (Lemma 3.1, Proposition 3.2), SHA-256 f308961ab85988c7 at entry
    - Depends on. the Hadamard product of Ξ.
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-005 — Φ_n is nearly constant on a fixed disc [PROVED]
    - Statement. (D-01.) For R > 0 and n ≥ 2 with πn² ≥ R + ½: |Φ_n(z)/Φ_n(0) − 1| ≤ 3.1R²/(π²n⁴) for |z| ≤ R; and (2X − 1)e^{−X} ≤ ½Φ_n(0) ≤ (2X + 3)e^{−X} for X = πn² ≥ 4π.
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ (§1.9; every constant recomputed; 25 numerical tests) · Lean —
    - Novelty. Not searched; an elementary kernel estimate.
    - Source. `results/haglund-conj4/NOTE.md` §4 (Lemma 4.1), SHA-256 f308961ab85988c7 at entry
    - Depends on. —
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-006 — an off-axis zero of Ξ forces an ascending zero of the pencil [PROVED]
    - Statement. (D-01, D-02.) Let β be a simple zero of Ξ with Im β > 0 and Im Ξ′(β) ≠ 0. Then there are a disc D about β and k_0 such that for every k ≥ k_0 and every t ∈ [0, 1], F_t has exactly one zero z_k(t) in D, it is simple, t ↦ z_k(t) is continuously differentiable, and sign d(Im z_k)/dt = sign Im Ξ′(β) on [0, 1]. In particular a simple zero β above the real axis with Im Ξ′(β) > 0 would make (D) fail for every k ≥ k_0. For the mirror pencil Ξ + L_t the sign is reversed. Nothing is claimed for a fixed k, for Im Ξ′(β) = 0, or for multiple zeros.
    - Checks. writer (Fable 5.1, side-session 2026-10-03) · read-F — (the writer is the orchestrator) · read-O ✓ (§1.10: no gap); the sign confirmed on the control Ξ + 5e−5 by three codes · Lean —
    - Novelty. New in the sources reached [novelty: dual-model check, 2026-10-03] (the orchestrator's search; L-lit's 16 citing works; the reader's search).
    - Source. `results/haglund-conj4/NOTE.md` §4 (Proposition 4.2), SHA-256 f308961ab85988c7 at entry
    - Depends on. L-001, L-005.
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

    ### L-007 — a census of Haglund's Conjecture 4 [NUMERICAL]
    - Statement. (D-02.) In the windows of `results/haglund-conj4/NOTE.md` §6 — every zero of Ξ_k with 0 ≤ Re z ≤ 2π(k+2)² + 30 for k = 1, …, 6, and frontier windows for k = 26, 27; 535 branches — the imaginary part decreases at every step of every followed branch and every landing is at a local maximum of S_k; for k = 1, …, 20, on [0, 4(k+2)² + 40], S_k has no local minimum with value in (0, 1). Floating point with Arb radii watched (A-track) and mpmath (B-track, k = 1, 2, 3); not interval-rigorous; a statement about these windows only.
    - Checks. A-track (Opus) · B-track (Opus; independent code and method; k ≤ 3) · the orchestrator's comparison of 15 landings (|Δx*| ≤ 3.9e−7) · controls that fire.
    - Novelty. No computation on Conjecture 4 for k ≥ 2 found in print [novelty: dual-model check, 2026-10-03].
    - Source. `results/haglund-conj4/NOTE.md` §6, SHA-256 f308961ab85988c7 at entry; Instruments: the table of that section.
    - Depends on. —
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (the second).

## Targets

Target table (copy this shape):

    ### T-00 — <the target in one line> (full statement: <row ID or charter §>; predecessor: <T-id or none>)
    | unit | route, in one line | broke at, in one line | outcome: row ID, zoo entry, or 10(m) label (i)/(ii)/(iii) | file |
    |---|---|---|---|---|
