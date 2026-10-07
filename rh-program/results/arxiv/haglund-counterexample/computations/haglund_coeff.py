"""haglund_coeff.py -- sign of the 1/t^2 coefficient of Haglund's Xi_N = xi_N - c_N on the critical line.
Exact: coefficient_N = -sum_{n>N} kappa_n with kappa_n proportional to (8X^3 - 30X^2 + 15X) e^{-X}, X = pi n^2
(negative only for n = 1), and sum over all n = 0 (Riemann's kernel is even).  Checked numerically by
t^2 * Xi_N(1/2+it) at t = 2000, 4000, 8000 (Gamma-parts are e^{-pi t/4}-small there)."""
import sys
import mpmath as mp
sys.path.insert(0, '.')
import stair as st
mp.mp.dps = 40
Z = st.Chain('zeta')
for N in (1, 2, 3, 4, 5):
    cN = st.c_N(N)
    vals = []
    for t in (2000, 4000, 8000):
        v = Z.E_tail(mp.mpc(mp.mpf(1)/2, t), st.w_trunc(N)).real - cN
        vals.append(v*t*t)
    # predicted leading coefficient from the tail kernel derivative, in the same normalization:
    # xi_N(1/2+it) - c_N = -Q_N(t),  Q_N(t) ~ -2 sum_{n>N} phitilde_n'(0)/t^2 ... print the tail sum for comparison
    pred = mp.fsum((8*(mp.pi*n*n)**3 - 30*(mp.pi*n*n)**2 + 15*mp.pi*n*n)*mp.exp(-mp.pi*n*n) for n in range(N + 1, N + 40))
    print(f'N={N}: t^2*Xi_N(1/2+it) at t=2000,4000,8000: {[mp.nstr(v, 10) for v in vals]} ; '
          f'sum_(n>N)(8X^3-30X^2+15X)e^-X = {mp.nstr(pred, 10)} ; ratio = {mp.nstr(vals[-1]/pred, 8)}')
