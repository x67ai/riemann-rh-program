# read-O — Opus reader, theory note of stream `haglund-conj4`

Status: IN PROGRESS (built incrementally; plan first, attempts appended as made).

## Plan (at most 20 lines)

1. Read READ-BRIEF-O.md (this stream), then BRIEF-WARNINGS.md, the two named sections of
   novel-wave-s41/READ-BRIEF-O.md, CHARTER.md, SOURCES.md, ORCH-NOTES.md, NOTE.md.
2. Do not open orch-probe/, A-track/code/, B-track/code/, any correspondence/ folder.
3. §1: re-derive pencil = Xi - L_t, positivity of L_t on the real axis, from Haglund's (10), (14).
4. §2: re-derive the theorem on real zeros and the stay-real criterion, step by step.
5. §3: re-derive the conditional description of solutions of Xi = c (RH + simple zeros).
6. §4: re-derive the unconditional off-axis proposition (Im Xi'(beta) > 0 => monotone Im).
7. §5: check that heuristic material is labeled as such and nothing heuristic is used as proved.
8. Re-run decisive numbers with own mpmath code in verify-O/ (two routes for Phi_n).
9. Check every citation at the page (Haglund arXiv:0910.5228v1 p. 11 and others in SOURCES.md).
10. Targets (a)-(i) from the brief, each marked ✓ / GAP / FALSE.
11. Deliver VERDICT LINE with OLD/NEW correction pairs (FIX-FIRST vs minor); append SHARED.md blocks.

## Header

- Reader: Opus (claude-opus-5-5), second model of the dual-model check; read opened 16:27 IST 2026-10-03.
- NOTE: `NOTE.md`, SHA-256 `57ea9099818ff9ad4de4da2b8b6b6f4f505511ed4e859918411cb88f0641913d`, 87 lines (all line numbers below refer to this hash).
- Read: `READ-BRIEF-O.md`; `rh-program/BRIEF-WARNINGS.md` (W1–W7); `novel-wave-s41/READ-BRIEF-O.md` sections "What a read at the line is" and "Shape of read-O.md" only; `CHARTER.md`, `SOURCES.md`, `ORCH-NOTES.md`, `NOTE.md` whole. Sources at the page: listed in §3.
- Not opened (by the brief): `orch-probe/`, `A-track/code/`, `B-track/code/`, any `correspondence/` folder.
- Re-run: `verify-O/` (own mpmath code, system Python 3.9, mpmath 1.3.0).
