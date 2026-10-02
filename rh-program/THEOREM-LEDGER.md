# Theorem ledger — the statements later work may cite, the statements known to be false, and what has been tried on a shared target

**What this file is.** The one register required by KICKSTART Part 2 item 10(q). `BARRIER-ZOO.md` records what whole proof CLASSES cannot do; the Instruments tables of the direction files (10(k)) record comparable QUANTITIES; this file records single STATEMENTS: what is proved and how far it has been checked, what is false and by which witness, and — where three or more units have worked on one target — the routes tried and where each broke. A charter cites rows by ID. Once a unit's rows are here, the row is the record of a statement's status, not the label inside the NOTE. In-house model: `results/d1-m3/LEDGER.md`.

**Opened 2026-10-03 (side-session; source: `results/external/cogentic-2026/process-lessons.md` P4, P5, dual-read). No rows yet: the first are entered at the first reconciliation of Session 42.**

**Rules (binding).**
1. APPEND-ONLY. A row block is never edited after entry. A correction, an upgrade, a withdrawal or a new check is a new dated line under the row ("L-012/c1 …") that says what changed and why, or a new row that names the row it corrects. Only the Index table is kept current by hand; where Index and blocks disagree, the blocks win.
2. WHO AND WHEN. Every unit's NOTE §0 ends with its LEDGER ROWS in the row shape below — the statements of its close, the proved parts of a unit that closes as a gap or a kill, and every statement it shows false. The reads check the rows with the rest of the NOTE. The orchestrator enters them here in the same step in which it writes the unit's reconciliation, copying the reconciled text; a row is never restated after the reads.
3. SELF-CONTAINED. The statement names every hypothesis and uses only notation defined in "Definitions" below or in the row itself. A statement that cannot be made self-contained in about twenty lines gets a row that points to its charter and says so.
4. KINDS. PROVED · CONDITIONAL (on named rows or named open statements) · NUMERICAL (the range and the producers, pointing to its Instruments row, which holds the value; never an exponent — `BRIEF-WARNINGS.md` W2) · EXCLUDED (false; the witness and where it is checked) · WITHDRAWN (with the row or read that withdrew it).
5. CHECKS, recorded per row as they happen: writer · read-F (with the sections it covered) · read-O · Lean. "Dual-read" is never written without the sections.
6. NO BACKFILL CAMPAIGN. A result older than this file gets its row when a charter first cites it; the orchestrator writes that row from the reconciled NOTE and marks it "backfilled" — an index entry: the charter cites the source through it, and the row's wording is checked by the next read that uses it.
7. STATUS keeps its one-line results and adds the row IDs; charters cite row IDs.
8. TARGETS. Where three or more units share one target, the target has a table below: one row per unit, entered at the unit's reconciliation. A target that is restated opens a new table that names its predecessor.

## Index

| ID | short name | kind | checks | source |
|---|---|---|---|---|

## Definitions

(Entered with the first rows that need them: D-01, D-02, … — one definition each, with the file and section it is taken from.)

## Rows

Row block (copy this shape):

    ### L-000 — <short name> [KIND]
    - Statement. <self-contained; hypotheses explicit; definitions by D-number>
    - Checks. writer (<model>, Session N) · read-F <sections, Session N> · read-O <✓ / pairs applied, Session N> · Lean <— / file>
    - Novelty. <label, with the printed core and page where there is one; single- or dual-checked>
    - Source. `<file>` §<section>, SHA-256 <first 16 hex> at entry
    - Depends on. <row IDs; printed theorems with page>
    - Entered. <HH:MM IST YYYY-MM-DD>, Session N.

## Targets

Target table (copy this shape):

    ### T-00 — <the target in one line> (full statement: <row ID or charter §>; predecessor: <T-id or none>)
    | unit | route, in one line | broke at, in one line | outcome: row ID, zoo entry, or 10(m) label (i)/(ii)/(iii) | file |
    |---|---|---|---|---|
