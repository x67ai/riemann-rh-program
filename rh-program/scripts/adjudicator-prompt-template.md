# Adjudicator prompt template (used for A1, B1 in Session 3 — reuse verbatim for future killer-vs-referee conflicts)

Spawn as a single `general-purpose` background agent. Substitute `{ID}` (e.g. `C1`), `{PROPOSAL}` (e.g. `C1:requirements-first-field`), `{DIRECTION_FILE}`, `{KILLER_SCORE}`, `{REFEREE_SCORE}`. For Track-B/C proposals include the S1–S5 paragraph (as in the B1 run); for Track-A proposals include the proportion-scope paragraph (as in the A1 run). Save the agent's JSON to `results/adjudication-{ID}.json`, then write the verdict section into the direction file and flip its status.

---

You are an adjudicator in a Riemann Hypothesis research program. Two independent critics reviewed research direction {PROPOSAL} and reached OPPOSITE verdicts: the "killer" critic says REFUTED (score {KILLER_SCORE}), the "referee" critic says survives-with-repairs (score {REFEREE_SCORE}). Your job: read both verdicts and the direction file, weigh the specific technical arguments (not the scores), and issue a final binding verdict.

Read these files fully:
1. /Users/jaytyagi/Documents/Work/2026/Math/riemann/rh-program/results/adjudication-input-{ID}.json — both verdicts with full findings (killer lens + referee lens)
2. /Users/jaytyagi/Documents/Work/2026/Math/riemann/rh-program/directions/{DIRECTION_FILE} — the direction file (the proposal being judged)
3. /Users/jaytyagi/Documents/Work/2026/Math/riemann/rh-program/results/map-hooks.txt — condensed formalized obstructions of the base machinery (context)

Adjudication standards:
- A "refuted" verdict must rest on a specific, checkable technical argument (an obstruction the proposal cannot evade, a false claimed input, a first theorem that is a known-hard problem in disguise). If the killer's fatal finding is of that kind and the referee did not rebut it, refuted stands.
- If the killer's fatal finding is actually a repairable gap (the referee's repairs address it), survives-with-repairs stands — but state which repairs are MANDATORY.
- Judge argument by argument. Cross-examine: does the referee's read actually answer the killer's strongest point, or do they talk past each other?

[TRACK B/C VARIANT — include for B/C proposals:] {PROPOSAL} is a Track-B/C direction (new machinery aimed at full RH), so it MUST satisfy the S1-S5 specification — in particular S1 (consume Euler-product input that Davenport-Heilbronn/Epstein violate) and S4 (a new positivity GENERATOR, not a bigger Weil-positivity cone). A killer finding that the proposal is "Weil positivity in disguise" (the known trap: the campaign post-mortem found every refuted route's first substantive step was Weil positivity in disguise) is fatal IF technically substantiated and unrebutted.

[TRACK A VARIANT — include for A proposals:] Note that Track A directions are scoped as supporting infrastructure (instruments, proportion progress), NOT full-RH routes — a killer finding of the form "this cannot prove RH" does not refute a direction whose stated scope is proportion improvement; but a finding of "the claimed proportion gain is impossible/already known impossible" does.

Your final message must be EXACTLY a JSON object (no prose around it):
{
  "proposal": "{PROPOSAL}",
  "final_verdict": "survives" | "survives-with-repairs" | "refuted",
  "final_score": <0-10>,
  "adjudication": "<the decisive reasoning: which findings stand, which fall, and why — 200-400 words>",
  "mandatory_repairs": ["<repair>", ...],
  "killer_findings_upheld": ["<claim>", ...],
  "killer_findings_overruled": ["<claim + why overruled>", ...]
}
