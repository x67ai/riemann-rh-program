"""
fp_core.py -- core algorithms for seed N3 `fingerprint` (ball arithmetic, python-flint / Arb).

Conventions (derived in NOTE.md section 1):
  E(w) = Xi(sqrt w);  F(w) = -E'(w)/E(w) = sum_{m>=0} c_m w^m,  c_m = s_{m+1} = sum_{gamma>0} gamma^{-2(m+1)}.
  S-fraction  F = c_0/(1 - al_1 w/(1 - al_2 w/(1 - ...)))  (Stieltjes; al_n > 0 all n  <=>  nu >= 0 on (0,inf)).
  J-fraction  (even contraction)  a_0 = al_1, a_n = al_{2n} + al_{2n+1}, b_n^2 = al_{2n-1} al_{2n}.
  Circle: moments m_k of a real symmetric measure on T; Verblunsky alpha_n in Simon's convention
          Phi_{n+1} = z Phi_n - alpha_n Phi_n^*, alpha_n = -Phi_{n+1}(0).

Every routine works on python-flint `arb` balls, so every output carries a proved error radius.
"""
from flint import arb, arb_series, ctx, fmpq, arb_mat


def sfrac_from_series(c, nmax=None, stop_on_zero=True):
    """Viskovatov/Stieltjes algorithm: given power-series coefficients c[0..L-1] of F with c[0] != 0,
    return al[1..] with F = c0/(1 - al1 w/(1 - al2 w/ ...)).
    Each step: F_{n} = (1 - 1/F_{n-1}) / (al_n w), with F_{n-1}(0) = 1.  Uses len(c)-1 steps at most.
    Stops early if al_n contains 0 (precision exhausted or degenerate) when stop_on_zero."""
    L = len(c)
    if nmax is None:
        nmax = L - 1
    oldcap = ctx.cap
    ctx.cap = L
    try:
        c0 = c[0]
        F = arb_series([x / c0 for x in c])
        al = []
        cur_len = L
        for n in range(1, nmax + 1):
            if cur_len < 2:
                break
            ctx.cap = cur_len
            G = 1 - 1 / F
            g = G.coeffs()
            # g[0] should be exactly 0 (contains 0); drop it
            if len(g) < 2:
                break
            a = g[1]
            al.append(a)
            if stop_on_zero and a.contains(0):
                break
            # F_n = (G / w) / a, length cur_len - 1
            newc = [x / a for x in g[1:cur_len]]
            cur_len = cur_len - 1
            ctx.cap = cur_len
            F = arb_series(newc)
        return al
    finally:
        ctx.cap = oldcap


def jfrac_from_sfrac(al):
    """al = [al_1, al_2, ...] -> (a[0..], b2[1..]) by even contraction."""
    a = []
    b2 = []
    # al index: al[k-1] = al_k
    if len(al) >= 1:
        a.append(al[0])
    n = 1
    while 2 * n <= len(al):
        b2.append(al[2 * n - 2] * al[2 * n - 1])      # al_{2n-1} al_{2n}
        if 2 * n + 1 <= len(al):
            a.append(al[2 * n - 1] + al[2 * n])       # al_{2n} + al_{2n+1}
        n += 1
    return a, b2


def hankel_dets(c, nmax, shift=0):
    """det(c_{i+j+shift})_{i,j<n} for n = 1..nmax (direct, for small cross-checks)."""
    out = []
    for n in range(1, nmax + 1):
        M = arb_mat(n, n, [c[i + j + shift] for i in range(n) for j in range(n)])
        out.append(M.det())
    return out


def sfrac_from_hankel(c, nmax):
    """Independent route: al_{2k} = D0_{k+1} D1_{k-1} / (D0_k D1_k), al_{2k+1} = D0_k D1_{k+1} / (D0_{k+1} D1_k),
    D0_k = det(c_{i+j})_{k x k}, D1_k = det(c_{i+j+1})_{k x k}, D_0 := 1."""
    kmax = nmax // 2 + 2
    D0 = [arb(1)] + hankel_dets(c, kmax, 0)
    D1 = [arb(1)] + hankel_dets(c, kmax, 1)
    al = []
    for n in range(1, nmax + 1):
        if n % 2 == 1:
            k = (n - 1) // 2
            al.append(D0[k] * D1[k + 1] / (D0[k + 1] * D1[k]))
        else:
            k = n // 2
            al.append(D0[k + 1] * D1[k - 1] / (D0[k] * D1[k]))
    return al


def verblunsky_levinson(m, nmax=None):
    """Real symmetric measure on T with moments m[k] = int z^k dmu (= int z^{-k} dmu), k = 0..K.
    Returns (alpha[0..], h[0..]) with h_n = ||Phi_n||^2.  Simon's convention."""
    K = len(m) - 1
    if nmax is None:
        nmax = K
    phi = [arb(1)]
    h = [m[0]]
    alpha = []
    for n in range(0, min(nmax, K)):
        r = sum((phi[k] * m[k + 1] for k in range(n + 1)), arb(0))
        a = r / h[-1]
        alpha.append(a)
        # Phi_{n+1} = z Phi_n - a Phi_n^*,  Phi_n^* = reversed coefficients (real case)
        zphi = [arb(0)] + phi
        star = list(reversed(phi)) + [arb(0)]
        phi = [zphi[k] - a * star[k] for k in range(n + 2)]
        h.append(h[-1] * (1 - a * a))
    return alpha, h


def schur_parameters(Fcoef, nmax):
    """Independent route: Schur algorithm on the Caratheodory function F(z) = sum Fcoef[k] z^k, F(0) = 1.
    f = (F - 1)/(z (F + 1)); gamma_k = f_k(0); f_{k+1} = (f_k - gamma_k)/(z (1 - gamma_k f_k)) (real case)."""
    L = len(Fcoef)
    oldcap = ctx.cap
    try:
        ctx.cap = L
        F = arb_series(Fcoef)
        num = (F - 1).coeffs()          # starts with 0
        ctx.cap = L - 1
        f = arb_series(num[1:]) / arb_series((F + 1).coeffs()[:L - 1])
        gam = []
        cur = L - 1
        for k in range(nmax):
            if cur < 1:
                break
            fc = f.coeffs()
            g0 = fc[0] if len(fc) > 0 else arb(0)
            gam.append(g0)
            if cur < 2:
                break
            ctx.cap = cur
            numer = (f - g0).coeffs()
            if len(numer) < 2:
                break
            denom = (1 - g0 * f).coeffs()
            cur = cur - 1
            ctx.cap = cur
            f = arb_series(numer[1:cur + 1]) / arb_series(denom[:cur])
        return gam
    finally:
        ctx.cap = oldcap


def digits(x):
    """Certified decimal digits of a ball (relative accuracy)."""
    b = x.rel_accuracy_bits()
    return max(0, int(b * 0.30103))


def fmt(x, n=20):
    return x.str(n, radius=False)
