# Tools register — the programs later work may start from

**Opened 02:42 IST 2026-10-03 (side-session; source: `results/external/claude-shaped-science-2026/process-lessons.md` P2, dual-read). First rows K-001–K-003 entered 17:34 IST 2026-10-03 (the stream `haglund-conj4`).**

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
| K-001 | Haglund's Φ_n, Ξ_N (two routes), Ξ, a proved tail bound, a rigorous winding number — Arb | `results/arxiv/haglund-counterexample/certificate/producer-A/hag_core.py` | a ladder of Haglund's printed zeros; certificate B (mpmath intervals); a third evaluation | haglund-cert-s37; haglund-conj4 (orchestrator, A-track) |
| K-002 | S_k = Ξ_{k+1}/Φ_{k+1} and a level-curve tracer for the pencil Ξ_k + tΦ_{k+1} — Arb midpoints with radii watched | `results/haglund-conj4/orch-probe/c4probe.py`, `trace.py` | Haglund's zero of Ξ_1; route L against route T; A-track, B-track and the reader on 15 landings | haglund-conj4 (orchestrator; A-track started from it) |
| K-003 | symbolic check of Haglund's (47) and the 1/x² coefficients (51) at 120 digits | `results/haglund-conj4/L-lit/check_task3.py` | the two printed versions of (47)/(52); the paper's Proposition tail | haglund-conj4 (L-lit) |

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

    ### K-001 — Haglund's Φ_n, Ξ_N by two routes, Ξ, a proved tail bound, a rigorous winding number (Arb)
    - File. `rh-program/results/arxiv/haglund-counterexample/certificate/producer-A/hag_core.py` (Python, python-flint 0.6.0; SHA-256 938427c9589f4faf at entry)
    - Does. `Phi(n, z)`, `XiN_L(N, z)` (literal sum; needs about 0.4·x bits near the real axis at height x), `Xi(z)`, `XiN_T(N, z)` (Ξ minus the tail terms plus a proved error ball; 256 bits suffice at height 3143), `tail_bound`, `winding` (argument principle on a square with bisection). Every function returns an Arb enclosure valid on the input box. About 1 ms per point value by route T.
    - Validated against. The ladder of the certificate (Haglund's table zeros and appendix zero); certificate B (mpmath intervals, independent code); the third evaluation at 4800 bits; B-track's mpmath evaluator in the stream haglund-conj4 (the certified zeros of Ξ_27 reproduced).
    - Limits and bugs. At moderate precision Arb's incomplete gamma function can return a ball with a large radius where about 110 digits cancel (Φ_9 at small real x: relative radius 1e−9 at 400 bits) — the radius must be read, never the midpoint alone (found 2026-10-03, ORCH-NOTES N8 of haglund-conj4). No derivative routine.
    - Role. writer's program (certificate A).
    - Used by. haglund-cert-s37; the paper's archive; haglund-conj4 (orchestrator's probe, A-track).
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03 (backfilled: the tool is of Session 37).

    ### K-002 — S_k = Ξ_{k+1}/Φ_{k+1} and a level-curve tracer for the pencil Ξ_k + tΦ_{k+1}
    - File. `rh-program/results/haglund-conj4/orch-probe/c4probe.py`, `trace.py`, `control.py`, `far2.py`, `rcrit.py`, `compare_AB.py` (Python; import K-001; SHA-256 of c4probe.py 17bafb9d1f81dd19 at entry)
    - Does. S_k by route T or L with the precision raised until the Arb radius is below 2^−40 relative; follows Im S_k = 0 from a zero of Ξ_k (predictor along −1/S′, corrector along the normal); real-axis scans of S_k and of the control (Ξ_{k+1} + λ)/Φ_{k+1}; the far-field law; the margin of the real-axis criterion. A branch in seconds.
    - Validated against. Haglund's printed zero of Ξ_1 (S_1 = 1 to 1e−22); route L against route T; the k = 1 landings against a real-axis scan, A-track, B-track and the reader's code (agreement to the printed digits).
    - Limits and bugs. `newton_zero` (plain Newton) runs away far from the axis — use Newton on log S (`far2.py`); `rcrit.py` gave two wrong rows before it summed the tail directly and checked radii (both fixed the same day). Midpoint arithmetic: not a certificate.
    - Role. writer's program (the orchestrator's probe).
    - Used by. haglund-conj4.
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03.

    ### K-003 — symbolic check of Haglund's (47) and the 1/x² coefficients of Φ_n (51)
    - File. `rh-program/results/haglund-conj4/L-lit/check_task3.py` (Python, sympy + mpmath; SHA-256 7f5b39e4949c40d5 at entry)
    - Does. The series of the algebraic part of G(z; a, b) to O(z⁻⁶); the coefficients (51) for n = 1…7 at 120 digits with partial sums. Under 5 s.
    - Validated against. The two printed versions of Haglund's (47) and (52) (it decides between them: the author's web copy of 2011 is the correct one); the limits of the paper's Proposition tail (4× Haglund's convention).
    - Limits and bugs. None recorded.
    - Role. writer's program.
    - Used by. haglund-conj4 (L-lit).
    - Entered. 17:34 IST 2026-10-03, side-session of 2026-10-03.
