# SHARED — stream `free-greedy-s40` (S8, the free greedy system)

Dated blocks, appended as the work lands, by the orchestrator and by the two units (`compute/`, `theory/`). Read at start and before every close. Machine-clock stamps.

## 2026-10-01 11:45 IST — orchestrator: stream opened

- Charter `CHARTER.md`; prototype `proto/s8_proto.py` with logs `proto/s8_pi4_2e7.log` (rho = pi/4 to 2e7), `s8_r08_2e6.log`, `s8_eoverpi_2e6.log`, `s8_r0995_2e6.log`.
- Prototype numbers (rho = pi/4): sup E = 8.22, 13.33, 26.63, 39.53, 47.86 at 1e3 … 1e7; sup|psi - x| = 108.6, 758.6, 4792.7, 29823.2, 260184.9; N(1e7) = 7853984, pi_P(1e7) = 650561.
- Reflection identity (boundary convention checked by hand): pi_P(x) = max(0, floor(sup_{y<=x} V(y) + 1/2)), E = pi_P - V, V(x) = rho(x - 1) - C(x).
