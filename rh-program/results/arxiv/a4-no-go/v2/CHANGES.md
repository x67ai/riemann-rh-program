# Version 2 — 18 October 2026

Previous version: Zenodo 10.5281/zenodo.22171689, concept DOI 10.5281/zenodo.22171688; Hexagon 2610.00252v1.
Previous title: The two-moment certificate is robust under Rudnick–Sarnak-range cubic augmentation with capacity control.
Revised title: Cubic augmentation of a two-moment model: an exact finite absorption theorem and its limits.

This revision replaces broad claims with a proved finite theorem and corrects the main certificate.

- Full-class and pinned-class exact absorption claims are withdrawn. Equality on a searched dictionary, even with heuristic pricing, does not prove the infimum over every admissible pair-containing configuration. The uniform 20/27 spectral bound is retained at its weaker scope.
- A new theorem proves exact absorption over all atom-only configurations at arbitrary positions for one fully specified N=64 model, for both the distinct-count and simple-fraction objectives. It combines the analytic integer-mark lower bound with a certified three-column law.
- The old printed clean-grid witness is not feasible: its cubic deficit is approximately 1.3486057e-5 in the implemented relative band. The replacement uses exact integer site vectors and algebraically defined weights, with the cubic expectation exactly at its center.
- The displayed cubic tolerance and code differed: epsilon*N versus epsilon*B3. Version 2 explicitly chooses epsilon*N; the new center-target law satisfies both conventions.
- The new certificate establishes the spectral count ladder at EVERY positive threshold, by rigorous inertia counts at 2,3,4 and strict monotonicity bucket bounds, at C_led=10 and hence every larger constant. This is a finite witness property, not a ladder theorem about zeta.
- Selected half-band row values are irrational algebraic numbers. Claims that all rows are rational and that decimal Fraction rationalizations establish their exact geometric feasibility are removed. The new certificate uses Arb outward balls, no optimizer and no feasibility grace. Exact cyclotomic polynomial checks are included.
- Shallow-pair formulas are corrected to spectrum (2m,0), Frobenius 4m^2 and cubic 8m^3. The isolated-block identity is retained at its proper conditional-on-Frobenius meaning.
- A common translation does not change traces. The erroneous sentence that the half-band row detects the vacancy location is replaced by a genuine relative-separation example.
- Structural grid, pair-block, sine-process and conditional sharp-capacity results are retained with self-contained proofs. Divergent-cutoff garnish is explicitly an isolated-spectrum observation with its stated hypotheses.
- The open zeta cubic-budget identification and all-threshold analytic ladder bridge are stated consistently. Historical optimization records are evidence about their dictionaries and implemented relative tolerance, not proofs of the stronger claims.
- No new Lean build or formalization of the revised witness is claimed. Portable source, exact inputs, code, results, build instructions and licenses accompany this revision; the AI disclosure records the Codex work.
