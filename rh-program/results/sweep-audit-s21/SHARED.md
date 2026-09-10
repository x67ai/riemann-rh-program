# sweep-audit-s21 — SHARED

Dated blocks from the standing-order-6 REFINEMENT AUDIT of the closed Grossmann sweep (Session 21, rank 4).

---

## 2026-09-10 — AUDIT.md COMPLETE (38/38 reports classified)

- **Deliverable:** `results/sweep-audit-s21/AUDIT.md` — §1 method, §2 table (38 rows), §3 findings, §4 refutation-shaped close + proposed Group-V zoo text, §5 honesty note.
- **SHA-256 (AUDIT.md):** `13dd2abfb49a4c6953b07916d9ec4da685759354c16c13668ea00d32d872e4dc`
- **Size:** 86317 bytes, 483 lines.

**The close, in one line.** No sweep verdict rests on the absence of literature alone — class (D) is empty, 0 of 38 — and 35 of 38 stand on internal S1–S5 grounds, but three do not: lorentzian-log-concavity (dead-end 0.82), condensed-analytic-stacks (instrument 0.60) and lee-yang-stat-mech (instrument 0.72) each kill what the branch has built on internal grounds and close what it has not built with a sentence saying nobody has written it.

**Count per class.**

| class | meaning | count | reports |
|---|---|---|---|
| **(A)** | internal S1–S5 grounds alone; absence clause absent or decorative | **9** | W1-04, W1-10, W1-15, W1-20, W1-21, W1-22, W2-01, W2-07, WP-00 |
| **(B)** | MIXED, internal grounds sufficient on their own | **26** | W1-00, W1-01, W1-02, W1-03, W1-05, W1-06, W1-07, W1-08, W1-09, W1-11, W1-12, W1-13, W1-16, W1-17, W1-18, W1-19, W1-23, W1-24, W2-00, W2-02, W2-03, W2-04, W2-05, W2-06, W2-08, WP-01 |
| **(C)** | MIXED, internal grounds INSUFFICIENT without the absence clause | **3** | W1-14 lorentzian-log-concavity (dead-end 0.82), W1-25 condensed-analytic-stacks (instrument 0.60), W1-26 lee-yang-stat-mech (instrument 0.72) |
| **(D)** | rests on absence alone | **0** | — |

**Report-id key.** W1-nn = `results/grossmann-sweep.json` reports[nn] (27); W2-nn = `results/grossmann-sweep2.json` reports[nn] (9); WP-nn = `results/grossmann-sweep2-partial.json` reports[nn] (2). Verdict rationale = the `fit.S1`–`fit.S5` block plus `first_interface`; there is no free-text rationale field.

**Consequences recorded, for the orchestrator (not executed here).**

1. The (C) list is non-empty, so per the brief's completion clause the three named branches go to a scout pair under the refinement as the next Grossmann-style stream, judging fit against S1–S5 on internal properties only. AUDIT §3 names the fit question per branch and the zoo entries that would bind each at brief time; it does not answer them.
2. Proposed **Group-V zoo text** is in AUDIT §4 — a new **V.5 "The Grossmann-condition rule"**, with a one-line pointer for V.2 and a dated rider for **III.16**, whose STATEMENT currently carries the sweep's absence sentence ("arXiv contains literally zero papers coupling Lorentzian polynomials to RH") into the executable suite. **Proposed, not inserted: `BARRIER-ZOO.md` is untouched by this audit.**
3. **Wording defect, closure-level only.** `grossmann-sweep2.json` `closure.wave2_summary` welds an absence clause to an internal clause in one sentence for beyond-endoscopy ("verified-negative — zero papers ever couple beyond endoscopy to RH, and the branch's target outputs … are exactly the DH/Epstein-shared properties"); the same shape appears for riemann-hilbert-painleve and lapidus. The scouts' own reports carry the internal grounds and all three rows are (B). The risk is a summary quoted onward without the report behind it.

**Rules observed.** Literature-and-record only: no scouting, no construction, no re-run of the sweep. Every quoted sentence carries its report id and field. U.S. English. Files edited: `AUDIT.md` and this file only. Not committed — the autocommit watchdog and the next session's orchestrator commit.
