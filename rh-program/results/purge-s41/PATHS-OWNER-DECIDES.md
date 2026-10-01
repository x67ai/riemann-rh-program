# PATHS-OWNER-DECIDES — third-party but not literature, or not settled

Written 17:47 IST 2026-10-01 by the read-only purge inventory. None of these paths is in PATHS-THIRD-PARTY.txt. To purge a group, append its paths to that file before running the purge (and uncomment the matching block of GITIGNORE-PROPOSED.txt). Sizes are the largest version in history, in bytes; H = tracked at HEAD, h = history only.

## 1. ABSTRACT-LISTINGS — 345 paths, 3769056 bytes, 340 at HEAD

Bibliographic listings fetched from the arXiv API (Atom XML: titles, authors, abstracts), saved as .xml, as .txt, or parsed into JSON; plus a few empty query outputs. Short, but not the program's. The program's own query scripts and query logs are KEEP. By folder:

- `rh-program/results/beta-shapes-s35/verify/` — 2 files, 44252 bytes, 2 at HEAD
- `rh-program/results/beta-shapes-s35/verify-O/` — 2 files, 53912 bytes, 2 at HEAD
- `rh-program/results/conj-O-s38/sources/` — 5 files, 56390 bytes, 5 at HEAD
- `rh-program/results/conj-O-s38/verify-O/arxiv/` — 10 files, 54278 bytes, 10 at HEAD
- `rh-program/results/d4-infty-s36/verify/` — 2 files, 97730 bytes, 2 at HEAD
- `rh-program/results/dz-half-s39/sources/` — 9 files, 952704 bytes, 9 at HEAD
- `rh-program/results/dz-half-s39/verify-O/sources/` — 7 files, 212781 bytes, 7 at HEAD
- `rh-program/results/e3-borger-rung1/sources/` — 2 files, 16045 bytes, 1 at HEAD
- `rh-program/results/e3-borger-rung1/sources-O/` — 1 files, 62346 bytes, 1 at HEAD
- `rh-program/results/fejer-form-s39/sources/` — 1 files, 1916 bytes, 0 at HEAD
- `rh-program/results/fejer-form-s39/verify-O/sources/` — 2 files, 9713 bytes, 2 at HEAD
- `rh-program/results/free-greedy-s40/compute/verify-O/sources/` — 2 files, 23184 bytes, 2 at HEAD
- `rh-program/results/free-greedy-s40/theory/sources/` — 12 files, 169283 bytes, 11 at HEAD
- `rh-program/results/free-greedy-s40/theory/verify-O/sources/` — 7 files, 37436 bytes, 6 at HEAD
- `rh-program/results/lemmaG-s39/sources/` — 7 files, 18705 bytes, 7 at HEAD
- `rh-program/results/lemmaG-s39/verify-O/sources/` — 6 files, 83828 bytes, 6 at HEAD
- `rh-program/results/local-greedy-s40/sources/` — 2 files, 23584 bytes, 2 at HEAD
- `rh-program/results/local-greedy-s40/verify-O/sources/` — 3 files, 96784 bytes, 3 at HEAD
- `rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/` — 32 files, 140022 bytes, 32 at HEAD
- `rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/` — 16 files, 68958 bytes, 16 at HEAD
- `rh-program/results/novel-wave-s36/staircase/lit/api/` — 50 files, 326463 bytes, 50 at HEAD
- `rh-program/results/novel-wave-s36/tournament/verify/` — 1 files, 32829 bytes, 1 at HEAD
- `rh-program/results/novel-wave-s37/beurling-fe/sources/arxiv-queries/` — 2 files, 0 bytes, 2 at HEAD
- `rh-program/results/novel-wave-s37/beurling-frontier/sources/` — 6 files, 437731 bytes, 6 at HEAD
- `rh-program/results/novel-wave-s37/proof-mine/verify/` — 1 files, 2101 bytes, 1 at HEAD
- `rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/` — 14 files, 130617 bytes, 14 at HEAD
- `rh-program/results/qcond-s38/sources/arxiv-queries/` — 6 files, 78615 bytes, 6 at HEAD
- `rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/` — 8 files, 34823 bytes, 8 at HEAD
- `rh-program/results/qtwin-s39/sources/arxiv-queries/` — 8 files, 61865 bytes, 7 at HEAD
- `rh-program/results/qtwin-s39/verify-O/sources/` — 5 files, 63198 bytes, 5 at HEAD
- `rh-program/results/s5-multiplicity-s40/verify-O/sources/` — 6 files, 68782 bytes, 6 at HEAD
- `rh-program/results/u-offsurgery-s39/sources/` — 1 files, 5522 bytes, 1 at HEAD
- `rh-program/results/u-offsurgery-s39/verify-O/sources/` — 22 files, 145749 bytes, 22 at HEAD
- `rh-program/results/watch-poll-s34/` — 1 files, 8038 bytes, 1 at HEAD
- `rh-program/results/watch-poll-s34/raw/` — 21 files, 62427 bytes, 21 at HEAD
- `rh-program/results/watch-poll-s35/raw/` — 21 files, 28815 bytes, 21 at HEAD
- `rh-program/results/watch-poll-s35/raw-wide/` — 21 files, 28815 bytes, 21 at HEAD
- `rh-program/results/watch-poll-s37/raw/` — 21 files, 28815 bytes, 21 at HEAD

Full list (size, flag, path):

```
    29742 H rh-program/results/beta-shapes-s35/verify-O/arxiv-O-2.xml
    24170 H rh-program/results/beta-shapes-s35/verify-O/arxiv-O.xml
    32938 H rh-program/results/beta-shapes-s35/verify/arxiv-searches-2.xml
    11314 H rh-program/results/beta-shapes-s35/verify/arxiv-searches.xml
    17393 H rh-program/results/conj-O-s38/sources/arxiv-O-q1.xml
     7069 H rh-program/results/conj-O-s38/sources/arxiv-O-q2.xml
      758 H rh-program/results/conj-O-s38/sources/arxiv-O-q3.xml
     6628 H rh-program/results/conj-O-s38/sources/arxiv-O-q4.xml
    24542 H rh-program/results/conj-O-s38/sources/arxiv-O-q5.xml
     2626 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-1.xml
      798 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-10.xml
      744 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-2.xml
     3140 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-3.xml
      782 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-4.xml
      800 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-5.xml
    36308 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-6.xml
     7578 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-7.xml
      762 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-8.xml
      740 H rh-program/results/conj-O-s38/verify-O/arxiv/qO-9.xml
    11037 H rh-program/results/d4-infty-s36/verify/arxiv-searches-2.xml
    86693 H rh-program/results/d4-infty-s36/verify/arxiv-searches.xml
   380193 H rh-program/results/dz-half-s39/sources/arxiv-beurling-generalized-sorted.xml
     5381 H rh-program/results/dz-half-s39/sources/arxiv-beurling-recent-titles.txt
     1773 H rh-program/results/dz-half-s39/sources/arxiv-generalized-numbers-2023-09-to-2026-10.txt
     9417 H rh-program/results/dz-half-s39/sources/arxiv-q-Beurlingintegers.xml
    10344 H rh-program/results/dz-half-s39/sources/arxiv-q-Beurlingnumber.xml
    17395 H rh-program/results/dz-half-s39/sources/arxiv-q-Beurlingprimes.xml
   214235 H rh-program/results/dz-half-s39/sources/arxiv-q-g-primes.xml
   198281 H rh-program/results/dz-half-s39/sources/arxiv-q-generalizedintegers.xml
   115685 H rh-program/results/dz-half-s39/sources/arxiv-q-generalizedprimes.xml
     6954 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-BE-shevtsova.xml
     6546 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-BE-tyurin.xml
    63829 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-O-beurling-integers.xml
    28254 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-O-beurling-random.xml
     4410 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-O-diamond-zhang.xml
    95308 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-O-genprimes.xml
     7480 H rh-program/results/dz-half-s39/verify-O/sources/arxiv-O-wellbehaved.xml
    62346 H rh-program/results/e3-borger-rung1/sources-O/arxiv-api-O.xml
    16045 H rh-program/results/e3-borger-rung1/sources/arxiv-api-searches.xml
        0 h rh-program/results/e3-borger-rung1/sources/q.xml
     1916 h rh-program/results/fejer-form-s39/sources/q1.xml
      774 H rh-program/results/fejer-form-s39/verify-O/sources/arxiv_q_fejer_ff.xml
     8939 H rh-program/results/fejer-form-s39/verify-O/sources/arxiv_q_hp19.xml
    12657 H rh-program/results/free-greedy-s40/compute/verify-O/sources/arxiv-q1-beurling-numerical-zeros.xml
    10527 H rh-program/results/free-greedy-s40/compute/verify-O/sources/arxiv-q2-beurling-RH-discrete.xml
      728 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-beurling-greedy.txt
     2233 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-beurling-prescribed.txt
     2385 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-beurling-real-zero.txt
    33356 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-beurling-recent-2025-2026.txt
    93350 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-beurling-zeta-or-primes-recent.txt
     2793 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-delone-beurling.txt
        0 h rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-delone-beurling.txt.tmp
      886 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-genprimes-feedback-prescribed-inverse.txt
    17209 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-hilberdink.txt
      730 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-lagarias-beurling.txt
    14827 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-revesz-beurling.txt
      786 H rh-program/results/free-greedy-s40/theory/sources/pa-arxiv-q-zhang-beurling.txt
        0 h rh-program/results/free-greedy-s40/theory/verify-O/sources/arxiv-q1-epstein-real-zeros.xml
      760 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q1-epstein-real-zeros.xml
    13255 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q2-epstein-zeros-real.xml
     8121 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q3-beurling-siegel.xml
      844 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q4-counting-real-zero.xml
     1036 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q5-dirichlet-poscoef-realzero.xml
    13420 H rh-program/results/free-greedy-s40/theory/verify-O/sources/q6-genprimes-onesided.xml
     3069 H rh-program/results/lemmaG-s39/sources/arxiv-2606.24536-abs.xml
     1785 H rh-program/results/lemmaG-s39/sources/arxiv-q1-breuer-simon.xml
     8379 H rh-program/results/lemmaG-s39/sources/arxiv-q2-np-euler.xml
     3140 H rh-program/results/lemmaG-s39/sources/arxiv-q3-np-primezeta.xml
      788 H rh-program/results/lemmaG-s39/sources/arxiv-q4-beurling-ff.xml
      757 H rh-program/results/lemmaG-s39/sources/arxiv-q5-genprimes-necklace.xml
      787 H rh-program/results/lemmaG-s39/sources/arxiv-q6-euler-thin.xml
     6378 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r1-additive-semigroup.xml
    23610 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r2-arith-semigroup.xml
      752 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r3-beurling-ff.xml
    22206 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r4-necklace-zeta.xml
     4231 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r5-natbound-primes.xml
    26651 H rh-program/results/lemmaG-s39/verify-O/sources/arxiv-r6-primezeta.xml
    17209 H rh-program/results/local-greedy-s40/sources/api_hilberdink.xml
     6375 H rh-program/results/local-greedy-s40/sources/api_ids_1.xml
     8577 H rh-program/results/local-greedy-s40/verify-O/sources/arxiv-q1-beurling-ramanujan-condition.xml
    79779 H rh-program/results/local-greedy-s40/verify-O/sources/arxiv-q2-beurling-multiplicative.xml
     8428 H rh-program/results/local-greedy-s40/verify-O/sources/arxiv-q3-genprimes-primepowers.xml
     3270 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/caratheodory_rh.xml
      772 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/cf_xi.xml
      722 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/grommer.xml
      798 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/hankel_powersums_entire.xml
      790 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/hankel_rh.xml
      756 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/hilbert_polya_tridiagonal.xml
      774 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/inverse_spectral_riemann.xml
      782 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/jacobi_operator_rh.xml
      768 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/jacobi_zeros.xml
      798 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/jacobi_zeta.xml
     9895 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/keiper_li.xml
     4128 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/lagarias_li.xml
     3198 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/lagarias_positivity.xml
      764 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/li_dh.xml
      780 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/li_positive_definite.xml
    12345 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/li_positivity.xml
      864 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/li_toeplitz.xml
      770 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/lp_euler.xml
     8016 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/op_zeros_zeta.xml
      828 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/power_sums_zeros.xml
     2955 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/romik.xml
      748 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/schur_zeta.xml
    13741 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/secondary_zeta.xml
      768 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/spectral_transformation_euler.xml
      802 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/stieltjes_cf_zeros.xml
      772 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/stieltjes_cf_zeta.xml
    31996 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/summary.json
    13492 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/summary2.json
     3730 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/tridiagonal_zeta_zeros.xml
    13881 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/turan_jensen.xml
     4591 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/uvarov_geronimus_zeta.xml
      728 H rh-program/results/novel-wave-s36/fingerprint/verify/arxiv/verblunsky_zeta.xml
     2462 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/abs_Hamburger_AND_abs_Riemann_zeta_.xml
     3415 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Dirichlet_series_AND_all_only_real_zeros_.xml
      772 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Euler_product_AND_all_Hermite_Biehler_.xml
    14244 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Fourier_quasicrystal_AND_all_almost_periodic_.xml
      790 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Fourier_quasicrystal_AND_all_zeta_OR_all_Riemann_.xml
     2928 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Fourier_quasicrystals_AND_all_infinite.xml
     7942 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Hamburger_AND_all_functional_equation_AND_all_zeta_OR_all_Dirichlet_.xml
     6899 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Lee_Yang_AND_all_zeta.xml
    12424 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Lee_Yang_polynomial_.xml
      788 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_Riemann_hypothesis_AND_all_stable_polynomials_.xml
      754 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_crystalline_measure_AND_all_zeta.xml
     4372 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_partial_Euler_product_AND_all_zeros_AND_all_critical_line_.xml
     5241 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_quantum_graph_AND_all_Riemann_zeta_AND_all_zeros.xml
      842 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_real_zeros_AND_all_Dirichlet_polynomial_AND_all_functional_equation_.xml
      782 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/all_stable_polynomial_AND_all_Dirichlet_series_.xml
     4303 H rh-program/results/novel-wave-s36/ly-infinity/sources/arxiv-queries/ti_finite_Euler_products_.xml
     2018 H rh-program/results/novel-wave-s36/staircase/lit/api/q01_au_haglund_riemann.xml
     5212 H rh-program/results/novel-wave-s36/staircase/lit/api/q02_incgamma_riemannxi.xml
     5214 H rh-program/results/novel-wave-s36/staircase/lit/api/q03_incgamma_xifunction.xml
    65222 H rh-program/results/novel-wave-s36/staircase/lit/api/q04_approximates_riemann.xml
    10281 H rh-program/results/novel-wave-s36/staircase/lit/api/q05_monotonic_zeros.xml
    28321 H rh-program/results/novel-wave-s36/staircase/lit/api/q06_hyperbolic_gamma.xml
     2090 H rh-program/results/novel-wave-s36/staircase/lit/api/q07_all_haglund_conj.xml
     2962 H rh-program/results/novel-wave-s36/staircase/lit/api/q08_incgamma_zeta_zeros.xml
     3285 H rh-program/results/novel-wave-s36/staircase/lit/api/q09_incgamma_RH.xml
      746 H rh-program/results/novel-wave-s36/staircase/lit/api/q10_truncat_riemannxi.xml
      780 H rh-program/results/novel-wave-s36/staircase/lit/api/q11_truncation_xi_zeros.xml
    27368 H rh-program/results/novel-wave-s36/staircase/lit/api/q12_zeros_of_approximations.xml
      742 H rh-program/results/novel-wave-s36/staircase/lit/api/q13_partial_theta_zeta.xml
      824 H rh-program/results/novel-wave-s36/staircase/lit/api/q14_theta_truncat_xi.xml
     8331 H rh-program/results/novel-wave-s36/staircase/lit/api/q15_polya_xi_approx.xml
      780 H rh-program/results/novel-wave-s36/staircase/lit/api/q16_debruijn_newman_incgamma.xml
     6697 H rh-program/results/novel-wave-s36/staircase/lit/api/q17_riemann_integral_rep_truncat.xml
    27420 H rh-program/results/novel-wave-s36/staircase/lit/api/q18_ids_known.xml
      788 H rh-program/results/novel-wave-s36/staircase/lit/api/q19_lagarias_hilbert.xml
     2379 H rh-program/results/novel-wave-s36/staircase/lit/api/q20_hermite_biehler_zeta.xml
      800 H rh-program/results/novel-wave-s36/staircase/lit/api/q21_chowla_selberg_critical.xml
     6190 H rh-program/results/novel-wave-s36/staircase/lit/api/q22_au_ki_haseo.xml
      748 H rh-program/results/novel-wave-s36/staircase/lit/api/q23_deformations_xi.xml
     4882 H rh-program/results/novel-wave-s36/staircase/lit/api/q24_debranges_riemann_xi.xml
      782 H rh-program/results/novel-wave-s36/staircase/lit/api/q25_polya_only_real_zeros.xml
     2551 H rh-program/results/novel-wave-s36/staircase/lit/api/q26_eisenstein_constant_term_RH.xml
      776 H rh-program/results/novel-wave-s36/staircase/lit/api/q27_smooth_incgamma.xml
      772 H rh-program/results/novel-wave-s36/staircase/lit/api/q28_smooth_theta.xml
      764 H rh-program/results/novel-wave-s36/staircase/lit/api/q29_smooth_riemannxi.xml
      812 H rh-program/results/novel-wave-s36/staircase/lit/api/q30_smooth_zeta_zeros_functional.xml
      758 H rh-program/results/novel-wave-s36/staircase/lit/api/q31_Sunits_theta.xml
      762 H rh-program/results/novel-wave-s36/staircase/lit/api/q32_Sunits_incgamma.xml
      778 H rh-program/results/novel-wave-s36/staircase/lit/api/q33_partialEuler_riemannxi.xml
      790 H rh-program/results/novel-wave-s36/staircase/lit/api/q34_partialEuler_incgamma.xml
      760 H rh-program/results/novel-wave-s36/staircase/lit/api/q35_partialEuler_theta.xml
     4372 H rh-program/results/novel-wave-s36/staircase/lit/api/q36_partialEuler_zeros_critline.xml
      824 H rh-program/results/novel-wave-s36/staircase/lit/api/q37_finiteEuler_functional_zeros.xml
     2802 H rh-program/results/novel-wave-s36/staircase/lit/api/q38_EulerProduct_incgamma.xml
      808 H rh-program/results/novel-wave-s36/staircase/lit/api/q39_truncatedEuler_approx_zeta.xml
    33242 H rh-program/results/novel-wave-s36/staircase/lit/api/q40_au_matiyasevich.xml
    31647 H rh-program/results/novel-wave-s36/staircase/lit/api/q41_au_nastasescu.xml
     1860 H rh-program/results/novel-wave-s36/staircase/lit/api/q42_au_alzergani.xml
     2687 H rh-program/results/novel-wave-s36/staircase/lit/api/q43_lagarias_debranges_dirichlet.xml
      854 H rh-program/results/novel-wave-s36/staircase/lit/api/q44_EulerProduct_theta_zeros.xml
     4283 H rh-program/results/novel-wave-s36/staircase/lit/api/q45_hamburgers_theorem.xml
     4789 H rh-program/results/novel-wave-s36/staircase/lit/api/q46_hamburger_theorem_zeta.xml
     4313 H rh-program/results/novel-wave-s36/staircase/lit/api/q47_hamburger_dirichlet_series.xml
     2609 H rh-program/results/novel-wave-s36/staircase/lit/api/q48_ti_hamburger.xml
     4975 H rh-program/results/novel-wave-s36/staircase/lit/api/q49_riemann_functional_eq_dirichlet_series.xml
     2013 H rh-program/results/novel-wave-s36/staircase/lit/api/q50_ids_iurato.xml
    32829 H rh-program/results/novel-wave-s36/tournament/verify/prior_art_arxiv.xml
        0 H rh-program/results/novel-wave-s37/beurling-fe/sources/arxiv-queries/hamburger-thm.html
        0 H rh-program/results/novel-wave-s37/beurling-fe/sources/arxiv-queries/reader-lagarias-delone.xml
    28345 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-O-beurling-random.xml
    39435 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-O-genprimes-random.xml
    17228 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-O-random-sieve.xml
   215315 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-beurling-recent.xml
   129928 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-genprimes.xml
     7480 H rh-program/results/novel-wave-s37/beurling-frontier/sources/arxiv-search-wellbehaved.xml
     5976 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_ids.xml
     2089 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q0.xml
     2097 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q1.xml
      752 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q2.xml
     6372 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q3.xml
     2117 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q4.xml
     2113 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q5.xml
      798 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q6.xml
      824 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_q7.xml
     8171 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_r0.xml
    82924 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_r1.xml
     8893 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_r2.xml
     5511 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_r3.xml
     1980 H rh-program/results/novel-wave-s37/proof-mine/verify-O/sources/arxiv_r4.xml
     2101 H rh-program/results/novel-wave-s37/proof-mine/verify/arxiv_gelfond.xml
        0 H rh-program/results/qcond-s38/sources/arxiv-queries/q1-saias-weingartner.xml
    62722 H rh-program/results/qcond-s38/sources/arxiv-queries/q1-weingartner.xml
     5666 H rh-program/results/qcond-s38/sources/arxiv-queries/q2-lev-olevskii.xml
      734 H rh-program/results/qcond-s38/sources/arxiv-queries/q3-generalized-dirac-comb.xml
     8745 H rh-program/results/qcond-s38/sources/arxiv-queries/q4-crystalline-meyer.xml
      748 H rh-program/results/qcond-s38/sources/arxiv-queries/q5-dirac-comb-idempotent.xml
     9448 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q1.xml
      790 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q2.xml
      774 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q3.xml
      850 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q4.xml
    17209 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q5.xml
     4194 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q6.xml
      740 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q7.xml
      818 H rh-program/results/qcond-s38/verify-O/sources/arxiv-queries/reader-O-q8.xml
        0 h rh-program/results/qtwin-s39/sources/arxiv-queries/q1-kns.xml
      764 H rh-program/results/qtwin-s39/sources/arxiv-queries/q1b-kns.xml
     2026 H rh-program/results/qtwin-s39/sources/arxiv-queries/q1c-kns.xml
     9448 H rh-program/results/qtwin-s39/sources/arxiv-queries/q2-beurling-fe.xml
     5554 H rh-program/results/qtwin-s39/sources/arxiv-queries/q3-crystalline-positive.xml
    38556 H rh-program/results/qtwin-s39/sources/arxiv-queries/q4-fourier-quasicrystal.xml
      790 H rh-program/results/qtwin-s39/sources/arxiv-queries/q5-genprimes-fe.xml
     4727 H rh-program/results/qtwin-s39/sources/arxiv-queries/q6-abstracts.xml
      770 H rh-program/results/qtwin-s39/verify-O/sources/q10-kolountzakis-lagarias.xml
     6110 H rh-program/results/qtwin-s39/verify-O/sources/q11-abstracts.xml
     4321 H rh-program/results/qtwin-s39/verify-O/sources/q7-hamburger-general-dirichlet.xml
     4128 H rh-program/results/qtwin-s39/verify-O/sources/q8-gendir-fe-euler.xml
    47869 H rh-program/results/qtwin-s39/verify-O/sources/q9-positive-eigenmeasure.xml
      764 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q1-beurling-unique-factorization.xml
      822 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q2-beurling-integers-natural.xml
    64922 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q3-beurling-multiplicatively.xml
      758 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q4-beurling-rational-integers.xml
      774 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q5-olofsson.xml
      742 H rh-program/results/s5-multiplicity-s40/verify-O/sources/arxiv-O-q6-olofsson-au.xml
     5522 H rh-program/results/u-offsurgery-s39/sources/abstracts-related.txt
      700 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-almaamori.xml
    11388 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-bdv.xml
      750 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-beurl-intvalued.xml
     3886 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-beurl-multiplicity.xml
    56553 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-beurl-recent.xml
     3807 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-dmv.xml
      766 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-feedback.xml
      786 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-gint-integers.xml
    10070 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-gprimes-constr.xml
     3862 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-gprimes-regular.xml
      728 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-greedy.xml
    17209 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-hilberdink.xml
      762 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-inverse.xml
      730 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-lagarias-beurling.xml
     7017 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-lagarias-delone.xml
     5580 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-maamori.xml
     6889 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-neamah.xml
      730 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-olofsson.xml
      772 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-prescribed.xml
      822 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-subsemigroup.xml
      748 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-zhang.xml
    11194 H rh-program/results/u-offsurgery-s39/verify-O/sources/arxiv-zhang2.xml
     8038 H rh-program/results/watch-poll-s34/abstracts.txt
    12305 H rh-program/results/watch-poll-s34/raw/abstracts.xml
     1500 H rh-program/results/watch-poll-s34/raw/id_2204_03107.xml
     2782 H rh-program/results/watch-poll-s34/raw/id_2501_14545.xml
     1965 H rh-program/results/watch-poll-s34/raw/id_2509_09771.xml
     2767 H rh-program/results/watch-poll-s34/raw/id_2606_09096.xml
     3402 H rh-program/results/watch-poll-s34/raw/id_2609_02882.xml
     7720 H rh-program/results/watch-poll-s34/raw/q_absolute_point.xml
      796 H rh-program/results/watch-poll-s34/raw/q_borger.xml
      828 H rh-program/results/watch-poll-s34/raw/q_cc7.xml
      830 H rh-program/results/watch-poll-s34/raw/q_eisenberg.xml
      875 H rh-program/results/watch-poll-s34/raw/q_exactwkb.xml
      834 H rh-program/results/watch-poll-s34/raw/q_goldston_suriajaya.xml
      796 H rh-program/results/watch-poll-s34/raw/q_gomila.xml
      844 H rh-program/results/watch-poll-s34/raw/q_krein_debranges.xml
     3511 H rh-program/results/watch-poll-s34/raw/q_lamzouri.xml
      866 H rh-program/results/watch-poll-s34/raw/q_lehmer.xml
     4976 H rh-program/results/watch-poll-s34/raw/q_mitkovski_poltoratski.xml
      905 H rh-program/results/watch-poll-s34/raw/q_prismatic.xml
     7185 H rh-program/results/watch-poll-s34/raw/q_rh_claims.xml
      863 H rh-program/results/watch-poll-s34/raw/q_suzuki.xml
     5877 H rh-program/results/watch-poll-s34/raw/q_weil_positivity.xml
     1500 H rh-program/results/watch-poll-s35/raw-wide/id_2204_03107.xml
     2782 H rh-program/results/watch-poll-s35/raw-wide/id_2501_14545.xml
     1965 H rh-program/results/watch-poll-s35/raw-wide/id_2509_09771.xml
     2767 H rh-program/results/watch-poll-s35/raw-wide/id_2606_09096.xml
     3402 H rh-program/results/watch-poll-s35/raw-wide/id_2609_02882.xml
     3453 H rh-program/results/watch-poll-s35/raw-wide/id_2609_20367.xml
      942 H rh-program/results/watch-poll-s35/raw-wide/q_absolute_point.xml
      796 H rh-program/results/watch-poll-s35/raw-wide/q_borger.xml
      828 H rh-program/results/watch-poll-s35/raw-wide/q_cc7.xml
      830 H rh-program/results/watch-poll-s35/raw-wide/q_eisenberg.xml
      875 H rh-program/results/watch-poll-s35/raw-wide/q_exactwkb.xml
      834 H rh-program/results/watch-poll-s35/raw-wide/q_goldston_suriajaya.xml
      796 H rh-program/results/watch-poll-s35/raw-wide/q_gomila.xml
      844 H rh-program/results/watch-poll-s35/raw-wide/q_krein_debranges.xml
      800 H rh-program/results/watch-poll-s35/raw-wide/q_lamzouri.xml
      866 H rh-program/results/watch-poll-s35/raw-wide/q_lehmer.xml
      840 H rh-program/results/watch-poll-s35/raw-wide/q_mitkovski_poltoratski.xml
      905 H rh-program/results/watch-poll-s35/raw-wide/q_prismatic.xml
      995 H rh-program/results/watch-poll-s35/raw-wide/q_rh_claims.xml
      863 H rh-program/results/watch-poll-s35/raw-wide/q_suzuki.xml
      932 H rh-program/results/watch-poll-s35/raw-wide/q_weil_positivity.xml
     1500 H rh-program/results/watch-poll-s35/raw/id_2204_03107.xml
     2782 H rh-program/results/watch-poll-s35/raw/id_2501_14545.xml
     1965 H rh-program/results/watch-poll-s35/raw/id_2509_09771.xml
     2767 H rh-program/results/watch-poll-s35/raw/id_2606_09096.xml
     3402 H rh-program/results/watch-poll-s35/raw/id_2609_02882.xml
     3453 H rh-program/results/watch-poll-s35/raw/id_2609_20367.xml
      942 H rh-program/results/watch-poll-s35/raw/q_absolute_point.xml
      796 H rh-program/results/watch-poll-s35/raw/q_borger.xml
      828 H rh-program/results/watch-poll-s35/raw/q_cc7.xml
      830 H rh-program/results/watch-poll-s35/raw/q_eisenberg.xml
      875 H rh-program/results/watch-poll-s35/raw/q_exactwkb.xml
      834 H rh-program/results/watch-poll-s35/raw/q_goldston_suriajaya.xml
      796 H rh-program/results/watch-poll-s35/raw/q_gomila.xml
      844 H rh-program/results/watch-poll-s35/raw/q_krein_debranges.xml
      800 H rh-program/results/watch-poll-s35/raw/q_lamzouri.xml
      866 H rh-program/results/watch-poll-s35/raw/q_lehmer.xml
      840 H rh-program/results/watch-poll-s35/raw/q_mitkovski_poltoratski.xml
      905 H rh-program/results/watch-poll-s35/raw/q_prismatic.xml
      995 H rh-program/results/watch-poll-s35/raw/q_rh_claims.xml
      863 H rh-program/results/watch-poll-s35/raw/q_suzuki.xml
      932 H rh-program/results/watch-poll-s35/raw/q_weil_positivity.xml
     1500 H rh-program/results/watch-poll-s37/raw/id_2204_03107.xml
     2782 H rh-program/results/watch-poll-s37/raw/id_2501_14545.xml
     1965 H rh-program/results/watch-poll-s37/raw/id_2509_09771.xml
     2767 H rh-program/results/watch-poll-s37/raw/id_2606_09096.xml
     3402 H rh-program/results/watch-poll-s37/raw/id_2609_02882.xml
     3453 H rh-program/results/watch-poll-s37/raw/id_2609_20367.xml
      942 H rh-program/results/watch-poll-s37/raw/q_absolute_point.xml
      796 H rh-program/results/watch-poll-s37/raw/q_borger.xml
      828 H rh-program/results/watch-poll-s37/raw/q_cc7.xml
      830 H rh-program/results/watch-poll-s37/raw/q_eisenberg.xml
      875 H rh-program/results/watch-poll-s37/raw/q_exactwkb.xml
      834 H rh-program/results/watch-poll-s37/raw/q_goldston_suriajaya.xml
      796 H rh-program/results/watch-poll-s37/raw/q_gomila.xml
      844 H rh-program/results/watch-poll-s37/raw/q_krein_debranges.xml
      800 H rh-program/results/watch-poll-s37/raw/q_lamzouri.xml
      866 H rh-program/results/watch-poll-s37/raw/q_lehmer.xml
      840 H rh-program/results/watch-poll-s37/raw/q_mitkovski_poltoratski.xml
      905 H rh-program/results/watch-poll-s37/raw/q_prismatic.xml
      995 H rh-program/results/watch-poll-s37/raw/q_rh_claims.xml
      863 H rh-program/results/watch-poll-s37/raw/q_suzuki.xml
      932 H rh-program/results/watch-poll-s37/raw/q_weil_positivity.xml
```

## 2. PUBLIC-DATA — 8 paths

Numeric data published by someone else (a zero table, LMFDB records, a conversion of a published certificate log). Facts rather than literature; the owner decides.

- `rh-program/results/d1-m2a/gomila/gomila-chain-manifest.json` — 156090 bytes, H — exact-rational conversion of Gomila's published 883-prism barrier log (third-party computational output)
- `rh-program/results/d1-m2a/gomila/gomila-scalars.json` — 1734782 bytes, H — exact-rational conversion of Gomila's published 883-prism barrier log (third-party computational output)
- `rh-program/results/e1-m5u/sources-O/lmfdb-nf-3.3.7063225849.1.html` — 91564 bytes, H — LMFDB number-field page (public database, CC BY-SA), saved as HTML
- `rh-program/results/e1-m5u/sources-O/lmfdb-nf-3.3.7063225849.2.html` — 94153 bytes, H — LMFDB number-field page (public database, CC BY-SA), saved as HTML
- `rh-program/results/e1-m5u/sources/lmfdb-frobenius-extract.txt` — 823 bytes, H — LMFDB data extract (Frobenius types for two cubic fields)
- `rh-program/results/e1-m5u/sources/lmfdb-nf-3.3.7063225849.1.html` — 91564 bytes, H — LMFDB number-field page (public database, CC BY-SA), saved as HTML
- `rh-program/results/e1-m5u/sources/lmfdb-nf-3.3.7063225849.2.html` — 94153 bytes, H — LMFDB number-field page (public database, CC BY-SA), saved as HTML
- `rh-program/results/fejer-form-s39/sources/odlyzko-zeros1.txt` — 1800000 bytes, H — Odlyzko's published table of zeta zeros

Related, classified KEEP (program code and computations that embed the same Gomila numbers): `rh-program/results/d1-m2a/gomila/gomila-scratch-{arb,mp}.lean`, `gomila-log-replay.txt`, `rh-program/results/d1-m2a/moments/gomila-{plus,minus}.json`.

## 3. NOT SETTLED — 7 paths

- `rh-program/lean/Zeta23.lean` — 1388 bytes, H — root import file copied from Anthropic's Zeta23 (Anthropic header kept) and extended with the program's imports
- `rh-program/lean/Zeta23/W1/ArgPrinciple/General.lean` — 12909 bytes, H — Lean code ported statement-for-statement from Jude Gomila's MIT-licensed repo (attributed in the header); load-bearing for the W1 checker
- `rh-program/lean/Zeta23/W1/ArgPrinciple/Rect.lean` — 26335 bytes, H — Lean code ported statement-for-statement from Jude Gomila's MIT-licensed repo (attributed in the header); load-bearing for the W1 checker
- `rh-program/results/arxiv/haglund-counterexample/haglund-counterexample-certificate.zip` — 531515 bytes, H — program certificate archive (also deposited on Zenodo) that bundles 10 NIST DLMF page dumps (certificate/producer-B/lit/dlmf-*.html|txt)
- `rh-program/results/c3-r/s14/correspondence/2026-09-18-alvarez-lopez-reply.md` — 4621 bytes, H — quotes a private email from a third party verbatim (privacy, not literature)
- `rh-program/results/d1-m1/v11/audit/audit-source-to-port.diff` — 7231 bytes, H — audit artifact quoting the Gomila source Lean (diff and elaborated statements of the ported files)
- `rh-program/results/d1-m1/v11/audit/elaborated-statements-source.txt` — 10847 bytes, H — audit artifact quoting the Gomila source Lean (diff and elaborated statements of the ported files)

Notes on group 3:

- The certificate zip (5 versions in history) bundles `certificate/producer-B/lit/`, ten NIST DLMF pages (five HTML, five text). The same pages are in PATHS-THIRD-PARTY.txt as loose files. Purging the zip removes the program's deposited certificate archive from history; keeping it keeps the DLMF pages inside it. A clean rebuild without `lit/` would change the archive hash that the paper and the Zenodo record cite.
- The two ArgPrinciple Lean files and the two audit files carry code from github.com/judegomila/dbn-lambda-01787854-candidate-audit (MIT License, attributed in each file header). MIT permits redistribution with the notice; the files are load-bearing for the W1 checker.
- `rh-program/lean/Zeta23.lean` is Anthropic's root import file (Apache-2.0 header kept) extended with the program's imports; 44 lines of import statements.
- The correspondence record quotes a private email verbatim. Not literature; a privacy question.

