# Tools register — the programs later work may start from

**Opened 02:42 IST 2026-10-03 (side-session; source: `results/external/claude-shaped-science-2026/process-lessons.md` P2, dual-read). No rows yet: the first are entered when a charter of Session 42 first needs them.**

**What this file is.** The register required by KICKSTART Part 2 item 10(y). `THEOREM-LEDGER.md` records statements; the Instruments tables of the direction files record quantities; this file records PROGRAMS: what each computes, how far it has been checked, and who has used it. A charter's "Read first" names the rows a writer unit should start from.

**Rules (binding).**
1. WHO AND WHEN. Every unit's NOTE §0 ends with its TOOL ROWS in the row shape below, after its LEDGER ROWS: every program of the unit that another unit could run for the same purpose. A unit that closes as a kill or a gap enters its rows all the same. The reads check the rows with the rest of the NOTE; the orchestrator copies them here at the unit's reconciliation.
2. WRITERS START FROM A ROW. A writer unit that needs a registered tool uses it (by import, or by a copy that says in its first line where it came from). A writer that builds its own version says in one line of its NOTE why — a different algorithm wanted as a cross-check, a limit of the registered tool, a different object.
3. READERS ARE UNTOUCHED. A reader shares no code with the unit it reads (`READ-BRIEF-O.md` step 3). A reader's own program gets a row when it is the better-checked one; the row says "reader's program" so that the next read of the same unit does not use it.
4. VALIDATED AGAINST. The row names what the tool was checked against — a brute force, a second producer, a reader's own program, a known answer on a ladder rung — and by whom. "Not validated" is a legal entry and is written, not left blank.
5. KNOWN LIMITS AND BUGS. Range, precision, memory, and every recorded bug with the commit or line that fixed it. A bug found later is a new dated line under the row, never an edit.
6. NO BACKFILL CAMPAIGN. A tool older than this file gets its row when a charter first needs it.

## Index

| ID | what it computes | file | validated against | used by |
|---|---|---|---|---|

## Rows

Row block (copy this shape):

    ### K-000 — <what it computes, in one line>
    - File. `<path>` (language; SHA-256 <first 16 hex> at entry)
    - Does. <inputs, outputs, range, precision; speed on this machine with the instance it was measured on>
    - Validated against. <what, to what agreement, by whom, where the log is> | not validated
    - Limits and bugs. <range, precision, memory; each recorded bug and its fix>
    - Role. writer's program | reader's program (not to be used by a later read of the same unit)
    - Used by. <units>
    - Entered. <stamp from scripts/stamp.py>, Session N.
