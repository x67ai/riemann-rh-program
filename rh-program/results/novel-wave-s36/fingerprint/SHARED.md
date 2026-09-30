# SHARED — seed N3 `fingerprint` (Jacobi / Schur / Verblunsky parameters of ζ)

Append-only, dated blocks, one per unit of work. Agent: Opus 5.5 (default effort), wave S36, 2026-09-30.

---

## 2026-09-30 17:58 — Unit 0: setup, objects, plan

**Read:** WAVE-CHARTER.md (all), STATUS.md 72–103, BARRIER-ZOO §0, I.1, IV.1, IV.9, V.4, V.5 (heads).

**Tooling found:** python-flint 0.6.0 (Arb ball arithmetic) is installed; `arb_series.zeta` (Hurwitz, with
`deflate=True`), `lgamma`, `log` on power series. Timing: Taylor series of ζ at s = 1/2, length 1300,
12 000 bits, 13.5 s. This makes the moment route *rigorous* (every number is a ball with a proved radius), so
"verified digits" = digits certified by the ball radius, not printed digits. mpmath 1.3.0 (pure-Python
backend) for the independent zeros route (`mpmath.zetazero`).

**Objects as I will use them (derivations go in NOTE §1; each is checked on toys in Unit 1):**

- E(w) := Ξ(√w) = ξ(1/2 + i√w), genus 0 in w, zeros w_k = γ_k² (γ_k > 0 or Re γ_k > 0, one per ± pair).
- Power sums s_m := Σ_{γ>0} γ^{−2m} = (−1)^{m+1} m c_{2m}, where log ξ(1/2 + x) = Σ c_k x^k.
- Stieltjes function F(w) := −E′(w)/E(w) = Σ_{γ>0} 1/(γ² − w) = Σ_{m≥0} s_{m+1} w^m
  = ∫ dν(y)/(1 − wy),  ν := Σ_{γ>0} γ^{−2} δ_{γ^{−2}} (weight = location × multiplicity).
- S-fraction F = c_0/(1 − α_1 w/(1 − α_2 w/(1 − …))), c_m = s_{m+1}; J-fraction by even contraction:
  a_0 = α_1, a_n = α_{2n} + α_{2n+1}, b_n² = α_{2n−1}α_{2n}.
- Circle side: z_ρ := 1 − 1/ρ; C(z) := 2 ξ′/ξ(1/(1 − z)) (Carathéodory under RH);
  σ := Σ_ρ |ρ|^{−2} δ_{z_ρ} (finite; NOT Σ_ρ δ_{z_ρ}, which is infinite);
  moments m_n = λ_{n+1} − 2λ_n + λ_{n−1} (λ_0 = 0, λ_{−n} = λ_n), m_0 = 2λ_1; Verblunsky α_n^V of σ/m_0.

**Plan:** U1 toys (real-rooted polynomial; complex pair; sin√w/√w with exact S-fraction 1/((2n+1)(2n+3)); circle
toys) → U2 ζ tables by Arb (moments at 1/2; Li at 1) → U3 zeros cross-check (mpmath.zetazero + smooth tail)
→ U4 mining → U5 controls (curve over F_q exact; L(χ₄); DH; F_{a,q}) → U6 task (d) → U7 prior art → NOTE.
