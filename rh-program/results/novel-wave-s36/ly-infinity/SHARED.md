# SHARED — seed N1 `ly-infinity` (novel-approach wave, Session 36)

Agent: Opus 5.5 (default effort). Folder: `results/novel-wave-s36/ly-infinity/`. Nothing here is committed by this agent.

---

## 2026-09-30 17:45 IST — unit 0: bootstrap

Read: WAVE-CHARTER.md (whole); STATUS.md 72–103; BARRIER-ZOO.md §0, I.1, III.15 (with riders), IV.1, IV.9, V.4, V.5; KICKSTART Part 2 items 10, 12; `results/ccm-dh-test/dh.py`.

First-pass derivation notes (to be checked by computation and at the page):
- Seed (1) re-derived: with z_p = p^{1/2-s}, Q(z) = prod(1 - p^{-1/2} z_p) restricts to E_S(s) = prod_{p in S}(1 - p^{-s}); Qtilde = prod(z_p - p^{-1/2}) restricts to P^{1/2-s} E_S(1-s). So f_pm(s) = E_S(s) pm P^{1/2-s} E_S(1-s) = E_S(s)(1 pm B(s)), B = prod of Blaschke factors b_p. Zeros on Re s = 1/2: yes. But the Lee-Yang lift adds nothing for product type: a product of one-variable Hermite-Biehler factors is Hermite-Biehler.
- Suspected ERRATUM (sign): E_S is the partial product of 1/zeta; the phase of B carries +2 pi S_X(t) while zeta's zeros sit at 2 theta(t) + 2 pi S(t) = pi mod 2 pi; the prime fluctuation enters with the OPPOSITE sign (anti-aligned). The zeta-aligned Lee-Yang product is prod(1 + p^{-s}) (Blaschke zero at -p^{-1/2}) or truncated geometric series per prime.
- Suspected no-go (to prove carefully): for ANY Lee-Yang polynomial p of multidegree m in prime variables, the restriction t -> p(p^{-it}) has |N(a,b) - W (b-a)/2pi| < |m|, W = sum m_p log p >= |m| log 2. So every nonconstant restriction has a zero in every interval of length > 2 pi / log 2 = 9.0647; Xi has none in (-14.13, 14.13). Hurwitz then forbids locally uniform convergence to Xi.
