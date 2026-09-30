# SHARED — producer B, unit `haglund-cert-s37` (independent of producer A; no Arb, no python-flint)

## 2026-09-30 22:50 — setup
- Read: `../BRIEF.md` (binding), staircase NOTE §4/§6/§7, Haglund arXiv:0910.5228 text pp. 1–4 and the Appendix
  (zeros of Ξ₁, p. 15 of the text file, line ~730). Did NOT open `../producer-A/`.
- Environment: Python 3.9.6, mpmath 1.3.0 (`mp.iv`, outward-rounded interval arithmetic). No Arb/flint imported anywhere.
- Sources saved to disk for every cited identity/bound (`lit/`, fetched 2026-09-30 from dlmf.nist.gov, text via `lit/html2txt.py`):
  DLMF 2.10.1 (Euler–Maclaurin with remainder ∫(B_{2m} − B̃_{2m}(x))/(2m)! f^{(2m)}), 24.9.2 (|B_{2n}(x) − B_{2n}| ≤ (2 − 2^{1−2n})|B_{2n}|),
  5.11.1 + 5.11(ii) (Stirling series; complex remainder ≤ sec^{2n}(½ ph z) × first neglected term), 25.2.9 (ζ by E–M, cross-reference).
- Plan: tail route Ξ_N = Ξ − Σ_{n>N} Φ_n (Haglund (12)); Ξ = ξ(½+iz) by Stirling + Euler–Maclaurin; Φ_n by its literal form (14) with
  h(w) = X^{−w}Γ(w,X) = ∫₁^∞ e^{−Xu}u^{w−1}du enclosed by repeated integration by parts (large X) or Γ(w) − lower series (small X),
  each with a remainder proved in CERT.md; explicit tail bound for n > M. Winding numbers by a Taylor model
  (DFT of tight point enclosures on a circle + Cauchy bound from a crude box enclosure on a larger circle), piecewise along ∂S.
