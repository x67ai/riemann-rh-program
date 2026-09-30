# NOTE — unit `haglund-cert-s37`: Haglund's Conjecture 1 fails at N = 27 (a dual-producer interval-rigorous certificate)

Orchestrator: Fable 5.1, Session 37, 2026-09-30. Producers: A (Opus; Arb via python-flint 0.6.0; `producer-A/`) and B (Opus; mpmath 1.3.0 intervals with
outward rounding and exact rational Bernoulli numbers, no Arb; `producer-B/`), independent (neither read the other's folder). Brief: `BRIEF.md`.
Read at the line by the orchestrator: Producer A's CERT §1, §3 (Lemmas B, Γ, T, the half-plane lemma, identity (12), the argument principle) and
Producer B's CERT §B (B1–B8: Stirling and Euler–Maclaurin remainders from DLMF pages saved on disk, the integration-by-parts and lower-series remainders,
the tail bound, the Taylor-model and boundary-walk lemmas) — every bound re-derived by the orchestrator and found correct. Re-run by the orchestrator:
`producer-A/h1.py` (`rerun-F/A-h1-rerun.log`: byte-identical values, timings apart), `producer-B/ladder.py` (`rerun-F/B-ladder-rerun.log`).

## Theorem H (certified twice; the objects are Haglund's, arXiv:0910.5228 pp. 1–4: Ξ_N = Σ_{n≤N} Φ_n, (13)–(14))

 (H1) Ξ₂₇ has a real zero in (3144.8946, 3144.8947): Ξ₂₇(3144.8946) = −1.760194631277…e−1070, Ξ₂₇(3144.8947) = +1.068716492261…e−1070, rigorous enclosures
      excluding 0 (A: literal sum at 4800 and 6400 bits AND tail route at 256, 1024 bits; B: tail route with proved remainders AND the literal sum at 4400 bits).
 (H2) Ξ₂₇ has a zero z₀ in the square of half-width 4·10⁻¹¹ (A) / 3.7·10⁻¹¹ (B) about c = 3143.2206824215 + 0.3152587994 i — winding number 1 along the
      boundary in every run of both producers (A: r = 1e−3, 1e−6, 1e−10, 4e−11; B: r = 1e−3 down to 3.7e−11, and after re-centering r = 1e−48:
      z₀ = 3143.220682421536585287281295989417800119… + 0.315258799378214845382286373009271765… i); zero-free control squares return 0 for both.
 (H3) Hence z₀ ∈ Q is non-real (Im z₀ > 0.3152) with Re z₀ < 3143.2207 < 3144.8946 < the real zero of (H1): listed by increasing real part, the imaginary parts
      of the zeros of Ξ₂₇ in the closed first quadrant are not nondecreasing — Conjecture 1 (p. 3) is FALSE for N = 27, and so is the weak form of Remark 1 (p. 4)
      (a non-real zero in Q with real part below a real zero, hence below the largest real zero). The pair (z₀, x₁) violates the conjecture under every
      enumeration by increasing real part, so Haglund's side assumption (one zero per vertical line) plays no role.
 (H4) a second real zero in (3145.5998, 3145.5999) (both producers). (H5) The seed's sibling chain ξ₂₄ = Ξ₂₄ + c₂₄: an off-line zero at 0.8159896243 + 2508.2839748053 i
      (in s) below real zeros at t ∈ (2510.2026, 2510.2027), (2510.7086, 2510.7087) — winding 1, both producers (B's route uses Jacobi's theta relation, cited).

Trust base: Producer A — Arb's ball arithmetic (gamma_upper, zeta, gamma) and Haglund's identity (12) for the tail route (the literal route uses only gamma_upper);
Producer B — mpmath's primitive interval operations and DLMF remainders read on disk. Ladder run first by both (Haglund's p. 4 table zeros at N = 1, 2;
his appendix zero of Ξ₁ at 20.6253…+2.6972…i with winding 1; zero-free controls). Cross-checks between the two routes inside each producer agree to
≤ 10⁻¹¹³⁷; the two producers' values agree to every printed digit. Hashes (10(i)): A CERT b1ecfe0a604c8b05e3439ad9ecae1c2a86c2fcdda55930cecbd1defea499513f;
B CERT c4a8ca6bc2d02b6f2e428d91b7cd05044272fd2d7546d37976dd1cd1648d87a3; per-log hashes in each producer's CERT/SHARED.

## Scope and status

 What it is: a rigorous counterexample to a published sufficient condition for RH (Haglund's Conjecture 1 implies RH by his Proposition 1); open since 2009,
 tested by its author to N ≤ 10 (weak form). What it is NOT: a statement about RH or about the zeros of ζ (RH is verified far above height 3143; the off-line
 zero belongs to the approximant Ξ₂₇, at a height where its window departs from Ξ — N2 NOTE §4, Proposition F). Novelty: `[dual-model check, 2026-09-30]`
 (N2's Opus literature sub-agent; the orchestrator's own search `NOVELTY-F.md`: Ahn's 2012 Penn thesis and the 2026 result on Conjecture 4 do not touch it).
 Mechanism of failure (N2 NOTE §4, Theorem D′): Haglund's real zeros are the pairs in the positive lobes of Ξ deeper than a smooth level Q_N; a shallow lobe
 followed by a deeper one at the departure height ≈ 4(N+1)² leaves an off-line pair below real zeros; the scan found this first at N = 27 for Ξ_N and
 N = 24 for ξ_N (the scan is not a proof of minimality). External use: allowed after the sponsor's decision (standing order 8 forbids prospectus artifacts,
 not results); a Lean-side acceptance of the certificate is priced as a separate unit (interval evaluation of incomplete gamma functions at 4000+ bits
 is not on the Comparator's record; not funded in Session 37).
