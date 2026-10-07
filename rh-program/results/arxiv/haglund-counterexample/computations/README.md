# Floating-point computations for Sections 3 and 5

The floating-point computations behind Sections 3 and 5 of *A counterexample to Haglund's
monotonic-zeros conjecture for the Riemann Ξ approximants*: the zero census, the tail
coefficients, the lobe scan and the 50-digit zeros. The stored outputs are the ones the
paper's numbers were read from.

Python 3 with [mpmath](https://mpmath.org). Run every script from this folder; each writes its
output here. `stair.py` holds the evaluators that the other scripts import.

| Computation | Command | Stored output |
|---|---|---|
| Zero census of Ξ_4 for 0 < Im s ≤ 200 | `python3 census.py haglund 4 200` | `census_haglund_N4_T200.json`, `run_census_haglund_4_200.log` |
| Zero census of ξ_N, N = 1, …, 5, for 0 < Im s ≤ 200 | `python3 census.py zeta <N> 200` | `census_zeta_N<N>_T200.json`, `census_zeta_N<N>_T200.log` |
| Second check of the non-real zeros of that census | `python3 reverify.py census_zeta_N<N>_T200.json` | `reverify_zeta_N<N>_T200.json`, `reverify_zeta_N<N>_T200.log` |
| The lobes of Ξ up to height 320 and the real zeros they carry, N = 1, …, 8 | `python3 lobes.py 320 8` | `lobes_T320.json`, `lobes_T320.log` |
| Tail coefficients: the limit of t²Ξ_N(t) | `python3 haglund_coeff.py` | `haglund_coeff.log` |
| Lobe scan in the windows [4(N+1)² − 40, 4(N+1)² + 90], N = 6, …, 30 | `python3 lobe_scan.py <Nmin> <Nmax>` | `lobe_scan_<Nmin>_<Nmax>.json`, `run_lobe_scan_<Nmin>_<Nmax>.log` |
| Margins read from the lobe scans | `python3 lobe_margins.py` | `lobe_margins_N6-17.log`, `lobe_margins_N6-29.log`, `lobe_margins_N6-30.log` |
| The zeros at N = 27 (Ξ_27), to 50 digits | `python3 verify_violation.py haglund 27 3142.95 3144.0 3144.45 3146.32 1.0` | `violation_haglund_N27_3142.json`, `run_verify_violation_haglund_27_3142.95_3144.0_3144.45_3146.32_1.0.log` |
| The zeros at N = 24 (ξ_24), to 50 digits | `python3 verify_violation.py zeta 24 2507.5 2509.2 2509.6 2511.7 1.0` | `violation_zeta_N24_2507.json`, `run_verify_violation_zeta_24_2507.5_2509.2_2509.6_2511.7_1.0.log` |
| Riemann's identity and the constants c_N | `python3 c1_identity.py` | `c1_identity.log` |

None of these computations is interval-rigorous; the two certificates of Section 6 are in
`../certificate/`.
