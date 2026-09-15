# Watch item — luckyseoul/perry-beurling-spectral-sieve (PBSS) (FYI only, 2026-09-15)

**Sponsor's ask (2026-09-15, chat, FYI only; the RH program NOT resumed):** "and this is one another
attempt: https://github.com/luckyseoul/perry-beurling-spectral-sieve".

**Pin.** GitHub `luckyseoul/perry-beurling-spectral-sieve`, author Nicholas Perry, MIT, Python; created
2026-07-26, last push 2026-09-14, 0 stars. Read this session: README, docs/STATUS.md (dated 2026-09-05),
docs/THEOREMS_AB.md, docs/WEIL_TRANSFER_OBSTRUCTION.md, docs/ZERO_PROPORTION_FEASIBILITY.md,
docs/related/anthropic-riemann-zeta/README.md, the status-note TeX abstract (copies in the session
scratchpad only; nothing fetched into the corpus). Not run, not audited line by line.

## 1. What it is, in the program's language

A **diagnostic**, by its own repeated statement ("Not a proof of RH... yet"; "Converse (low energy ⇒ RH)
is essentially as hard as RH"). Object: the prime-counting residual q_T(u) = (θ(x) − x)/√x on a log
window x = e^{uT}, u ∈ [0, 1], projected onto shifted Legendre polynomials of degree ≤ d; the statistic
is the energy ratio R_d = ‖P_d q‖²/‖q‖². Mechanism, via the explicit formula: an on-line zero ½ + iγ
contributes a bounded oscillation sin(γTu), whose low-degree projection is O(T⁻²) by integration by parts
(their Lemmas M3/M5 — elementary and correct as model statements); an off-line zero σ + it contributes
e^{T(σ−½)u} sin(tTu), an exponentially growing envelope, which is what the diagnostic is meant to see.

The repository's own audit trail (September 2026) is honest and has already reached the classical wall:

- "Theorem A" (RH ⇒ R_d = O(T⁻²) for the exact continuous residual) — proved conditionally; fine.
- "B-ABS": subexponential growth of one absolute Legendre moment ⇔ RH — an RH-equivalence. In plain
  terms it is von Koch's ψ(x) − x = O(x^{½+ε}) ⇔ RH re-parametrized on a log window with a polynomial
  weight. No leverage: the "unconditional growth bound remains unproved" line is RH itself.
- "B-RES" (the normalized converse, R_d decay ⇒ RH) — OPEN, and their own
  `BEURLING_NORMALIZED_COUNTEREXAMPLE.md` shows it is **false for positive discrete Beurling systems**
  (zeros at 11/20 ± iγ with every fixed-degree detrended ratio O(e^{−T/10}/T)). That is the program's
  **zoo entry I.2 (the Beurling counterexample factory)** hitting them from the inside: a criterion
  that consumes only the prime-density residual holds for Beurling worlds where RH fails, so it cannot
  decide RH for ζ without an input that Beurling systems lack. They found the barrier themselves; they
  have not named the consequence (that the diagnostic is structurally blind, not merely incomplete).
- `WEIL_TRANSFER_OBSTRUCTION.md` reads the Alpöge–Furman/Claude paper's Lemma 3.1 (n₊(A*JA) ≤ n₊(J))
  and Proposition 4.1 correctly as an UPPER inertia bound that supplies no lower singular-value bound
  for their projection, retracts their earlier "Weil-visible channel" dictionary, and gives a 2×2
  vanishing-compression example. Consistent with the program's own account of what the two-moment
  certificate consumes (a trace, a Hilbert–Schmidt norm, integrality) and discards (off-diagonals).
- `ZERO_PROPORTION_FEASIBILITY.md`: STOP — no inequality mapping Weil/BGST rank methods onto R_d.

## 2. Relevance to the program

**None as a route; none as an input; a small confirmatory datum for the zoo.**

- Route: it is a reformulation-class object (RH-equivalent statements plus a heuristic whose converse
  fails in Beurling worlds). The program's Group-I battery (I.1 DH/Epstein at the axiom, I.2 Beurling)
  is exactly the test it fails, and it fails it on its own record. Nothing here reaches any live
  direction (C2 is the only ACTIVE direction; PBSS has no contact with the strip-positive cone or the
  confinement theorem).
- Input: no theorem the program could consume; the model lemmas are elementary; the numerics (R_4 ≈
  0.15–0.19 "soft plateau" through x ≈ 5·10¹⁰) are what RH plus the explicit formula predict at finite
  T and carry no information about zeros beyond the heights already rigorously verified.
- Datum: a third-party, AI-assisted (the repo carries an AGENTS.md) attempt that independently rebuilt
  the I.2 kill for its own criterion. If the zoo ever wants an "external confirmations" rider on I.2,
  this is a citable instance; not worth a zoo stream on its own.
- Courtesy: not owed. Their reading of the Alpöge–Furman/Claude linear algebra is accurate and makes no
  claim against the 2/3 theorem.

## 3. Label

[external, read-only, FYI; no verification workflow run; no corpus fetch; nothing load-bearing].
