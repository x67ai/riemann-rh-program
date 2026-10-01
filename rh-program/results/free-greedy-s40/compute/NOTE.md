# UNIT `free-greedy-s40/compute` — S8 at scale: NOTE

Opened 2026-10-01 11:26 IST (machine clock), Opus 5.5 agent. Charter `../CHARTER.md`, brief `BRIEF.md`. Code and logs in `verify/`; scratch over 50 MB in `/private/tmp/rh-s40-free-greedy/`. Machine: Apple M4 (arm64, 10 cores), 24 GB RAM (unit cap 4 GB); on arm64 `long double` is the same 64-bit type as `double`, so extended precision here means double-double.

## 0. Close

(written last)

## 1. Log of work (appended as it lands)

- 11:26 — unit opened; read CHARTER, BRIEF, `proto/s8_proto.py` and the four prototype logs.
- 11:30 — **dress rehearsal passed [computed].** `verify/s8_port.c` (a line-by-line C port of the prototype: IEEE double, same incremental deficit, same heap order, compiled with `-ffp-contract=off`) reproduces all four prototype logs row for row (`diff` empty): `verify/port_pi4_2e7.log` vs `proto/s8_pi4_2e7.log`, and the ρ = 0.8, e/π, 0.95π/3 logs at 2e6. The Python prototype itself rerun at X = 1e7 (`verify/proto_run_pi4_1e7.log`) and the port at 1e7 (`verify/port_pi4_1e7.log`) agree: final count 7,853,983 g-integers ≤ 10⁷, 650,561 g-primes, sup E = 47.8635405622, sup|ψ − x| = 260184.909. Note on the charter's "N = 7,853,984": the prototype's table row records N at the first event ≥ 10⁷, one event past 10⁷; the exact N(10⁷) is 7,853,983.
