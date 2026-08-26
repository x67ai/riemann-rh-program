"""m0i_certify.py -- D1 M0(i): CERTIFIED DH Weil-form negativity witnesses.

Per rung (lambda = pnum/pden exact rational, N, dps_find, dps_cert):

  1. FINDER (float mpmath, dps_find): T = weilform.build_matrix(lam, N, 'dh'),
     parity split, mp.eigsy on both sectors; ground eigenvectors extracted.
  2. WITNESS FREEZE: unit-2-norm ground eigenvector rounded to 40 significant
     decimal digits.  The frozen decimal vector is the EXACT witness the
     certificate covers (any test vector bounds the minimum from above, so
     rounding costs nothing but a ~1e-39 shift of the certified value).
  3. CERTIFIER (mpmath.iv at dps_cert, directed rounding end-to-end):
     re-evaluate Q_DH(v) = v^T tau v from scratch in interval arithmetic --
     lambda as exact rational, L = 2 log lambda, composite Gauss-Legendre
     archimedean quadrature, Lambda_DH divisor recursion (kappa from surds),
     prime sums, tail and constant terms, the O(N^2) quadratic form, and the
     norm^2 -- all in iv.  Output: enclosures [lo, hi] for Q_DH(v) and for the
     Rayleigh quotient Q/(v,v).  hi < 0 certifies Q_DH(v) < 0 for the exact
     frozen v, hence: the truncated DH Weil form is NOT PSD at support lambda
     (bandwidth N).  Certificate semantics: the enclosure is rigorous for the
     STATED quadrature rule (M panels x K Gauss-Legendre nodes; float-Newton
     nodes treated as exact numbers); the quadrature-DISCRETIZATION error is
     controlled separately by the --grid-double rider, which repeats the whole
     iv evaluation on an independent, much finer rule (M2 = M + 62, K2 = 64)
     and reports the shift between the two certified enclosures.
  4. ANALYSIS (float, dps_find): the off-line-quadruple matrix S_off from the
     closed-form continuation fhat(tau) at tau = +-gamma -+ i*delta
     (gamma = 85.699..., delta = beta - 1/2 = 0.3085...); decomposition
     Q = S_on(v) + S_off(v) with S_on := Te - S_off (exact matrix identity on
     the zero side of the Weil explicit formula; DH has no pole term -- the
     completed function is entire); witness localization at the packet index
     n0 = gamma*L/(2*pi); rank-<=4 eigenstructure of S_off; the crash
     criterion K_inv = max eig of (-So_)^(1/2) Son'^(-1) (-So_)^(1/2) over the
     negative eigendirections of S_off (Son' = S_on + positive part of S_off):
     the form is indefinite iff K_inv > 1, so the K_inv(lambda) curve crossing
     1 is the derived onset estimate for the reconciliation write-up.

Usage:
  python3 m0i_certify.py OUT.json pnum pden N dps_find dps_cert [flags]
Flags: --grid-double  --son-eig  --selftest  --skip-analysis
Conventions: results/ccm-dh-test/weilform.py (triple-validated Sessions 4-6);
zero-side/vhat convention: results/ccm-dh-test/test_conventions.py (T2).
"""
import json
import os
import resource
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STACK = os.path.abspath(os.path.join(HERE, '..', 'ccm-dh-test'))
sys.path.insert(0, STACK)

import mpmath as mp
from mpmath import iv

import weilform as wf

GAMMA_S = '85.699348485377592'   # Im rho_DH (re-verified Session 5, residual 7.6e-41)
BETA_S = '0.808517182456637'     # Re rho_DH
# Archived DH conductor-Fuchs fit (results/d1-m0/chi3-conductor-point.json,
# five_point_table row 'dh'):  ln eps = a - c*mu + b*ln mu
LAW_A, LAW_C, LAW_B = '3.5069', '2.6043', '2.7101'


# ------------------------------------------------------------------ finder
def finder(lam, N, dps_find):
    mp.mp.dps = dps_find
    t0 = time.perf_counter()
    T = wf.build_matrix(lam, N, 'dh')
    t_build = time.perf_counter() - t0
    Te, To = wf.parity_blocks(T, N)
    t0 = time.perf_counter()
    ee, Ve, oe = wf.eig_sym(Te)
    eo, Vo, oo = wf.eig_sym(To)
    t_eig = time.perf_counter() - t0
    out = {'t_build_s': round(t_build, 1), 't_eig_s': round(t_eig, 1),
           'min_even': mp.nstr(ee[0], 15), 'min_odd': mp.nstr(eo[0], 15),
           'even_low4': [mp.nstr(x, 10) for x in ee[:4]],
           'odd_low4': [mp.nstr(x, 10) for x in eo[:4]]}
    vecs = {}
    for parity, (ev, V, order) in (('even', (ee, Ve, oe)), ('odd', (eo, Vo, oo))):
        dim = N + 1 if parity == 'even' else N
        col = order[0]
        v = [V[i, col] for i in range(dim)]
        nrm = mp.sqrt(mp.fsum(x*x for x in v))
        v = [x/nrm for x in v]
        if mp.fsum(v) < 0:            # sign convention: sum > 0
            v = [-x for x in v]
        vecs[parity] = (ev[0], v)
    return out, vecs, Te, To


# ---------------------------------------------------------------- certifier
def lambda_dh_iv(nmax):
    s5 = iv.sqrt(iv.mpf(5))
    kap = (iv.sqrt(iv.mpf(10) - 2*s5) - 2)/(s5 - 1)
    pat = {1: iv.mpf(1), 2: kap, 3: -kap, 4: iv.mpf(-1), 0: iv.mpf(0)}
    a = [None] + [pat[n % 5] for n in range(1, nmax + 1)]
    lamv = [iv.mpf(0)]*(nmax + 1)
    for n in range(2, nmax + 1):
        s = a[n]*iv.log(iv.mpf(n))
        for d in range(2, n):
            if n % d == 0:
                s -= lamv[d]*a[n//d]
        lamv[n] = s
    return {n: lamv[n] for n in range(2, nmax + 1)}


def iv_phi_diag(pnum, pden, N, dps_cert, M, K):
    """All (2N+1) distinct entries of tau (phi_n, diag_j) enclosed in iv."""
    iv.dps = dps_cert
    mp.mp.dps = dps_cert
    lam_iv = iv.mpf(pnum)/iv.mpf(pden)
    L = 2*iv.log(lam_iv)
    lam_f = mp.mpf(pnum)/mp.mpf(pden)
    nmax = int(mp.floor(lam_f**2 + mp.mpf('1e-9')))

    xs, ws = wf.gl_nodes(K)                    # float mpf, treated exact
    h = L/M
    half = iv.mpf(1)/iv.mpf(2)
    Y, W = [], []
    for m in range(M):
        c_ = h*(iv.mpf(2*m + 1))*half
        r_ = h*half
        for x, w in zip(xs, ws):
            Y.append(c_ + r_*iv.mpf(x))
            W.append(r_*iv.mpf(w))
    npts = len(Y)

    a2 = iv.mpf(3)/iv.mpf(2)                   # 2a, a = 3/4
    q0 = iv.mpf(2)
    g, s1, yl = [], [], []
    for y in Y:
        den = -iv.expm1(-2*y)
        e2ay = iv.exp(-a2*y)
        g.append(-2*e2ay/den)
        s1.append(2*q0*e2ay*iv.expm1(-half*y)/den)   # -(2-2a) = -1/2
        yl.append(y/L)

    lamdict = lambda_dh_iv(nmax)
    ms = sorted(lamdict)
    logm = {m: iv.log(iv.mpf(m)) for m in ms}
    coefm = {m: lamdict[m]/iv.sqrt(iv.mpf(m)) for m in ms}
    onem = {m: (1 - logm[m]/L) for m in ms}

    twopiL = 2*iv.pi/L
    phi = {0: iv.mpf(0)}
    for n in range(1, N + 1):
        w_ = twopiL*n
        arch = iv.mpf(0)
        for i in range(npts):
            arch += W[i]*g[i]*iv.sin(w_*Y[i])
        pr = iv.mpf(0)
        for m in ms:
            pr += coefm[m]*iv.sin(w_*logm[m])
        phi[n] = half*arch - pr

    tail = -q0*iv.log(-iv.expm1(-2*L))
    cst = (iv.log(iv.mpf(5)/iv.pi) - iv.euler)*q0
    diag = {}
    for j in range(0, N + 1):
        w_ = twopiL*j
        acc = iv.mpf(0)
        for i in range(npts):
            sn = iv.sin(w_*Y[i]*half)
            dq = 2*(-2*sn*sn - yl[i]*iv.cos(w_*Y[i]))
            acc += W[i]*(s1[i] + g[i]*dq)
        pr = iv.mpf(0)
        for m in ms:
            pr += coefm[m]*2*onem[m]*iv.cos(w_*logm[m])
        diag[j] = half*(acc + tail + cst) - pr
    return phi, diag, L


def cfull_iv(wit_strs, parity, N):
    s2i = 1/iv.sqrt(iv.mpf(2))
    c = {}
    if parity == 'even':
        c[0] = iv.mpf(wit_strs[0])
        for n in range(1, N + 1):
            c[n] = iv.mpf(wit_strs[n])*s2i
            c[-n] = c[n]
    else:
        for n in range(1, N + 1):
            c[n] = iv.mpf(wit_strs[n - 1])*s2i
            c[-n] = -c[n]
        c[0] = iv.mpf(0)
    return c


def q_iv(c, phi, diag, N, parity):
    invpd = {d: 1/(iv.pi*iv.mpf(d)) for d in range(1, 2*N + 1)}
    phif = {}
    for n in range(0, N + 1):
        phif[n] = phi[n] if n else iv.mpf(0)
        phif[-n] = -phif[n]
    idxs = [j for j in range(-N, N + 1) if not (parity == 'odd' and j == 0)]
    tot = iv.mpf(0)
    for j in idxs:
        tot += c[j]*c[j]*diag[abs(j)]
    for ai in range(len(idxs)):
        j = idxs[ai]
        for bi in range(ai + 1, len(idxs)):
            k = idxs[bi]
            tot += 2*c[j]*c[k]*(phif[j] - phif[k])*invpd[k - j]
    n2 = iv.mpf(0)
    for j in idxs:
        n2 += c[j]*c[j]
    return tot, n2


def certify(pnum, pden, N, dps_cert, witnesses, M, K):
    """witnesses: {parity: [40-digit strings]} -> enclosures."""
    t0 = time.perf_counter()
    phi, diag, L = iv_phi_diag(pnum, pden, N, dps_cert, M, K)
    t_build = time.perf_counter() - t0
    out = {'dps_cert': dps_cert, 'M_panels': M, 'K_gl': K,
           't_iv_build_s': round(t_build, 1)}
    mp.mp.dps = dps_cert + 10
    for parity, strs in witnesses.items():
        t0 = time.perf_counter()
        c = cfull_iv(strs, parity, N)
        Q, n2 = q_iv(c, phi, diag, N, parity)
        R = Q/n2
        lo, hi = mp.mpf(R.a), mp.mpf(R.b)
        out[parity] = {
            'Q_interval': [mp.nstr(mp.mpf(Q.a), 30), mp.nstr(mp.mpf(Q.b), 30)],
            'rayleigh_interval': [mp.nstr(lo, 30), mp.nstr(hi, 30)],
            'rayleigh_width': mp.nstr(mp.mpf(R.delta.a), 3),
            'certified_negative': bool(hi < 0),
            't_qf_s': round(time.perf_counter() - t0, 2)}
    return out


# ----------------------------------------------------------------- analysis
def vhat(n, L, t):
    num = -2j*mp.sin(t*L/2)
    den = 2j*mp.pi*n/L - 1j*t
    if abs(den) < mp.mpf('1e-25'):
        return mp.sqrt(L)*mp.e**(1j*t*L/2)
    return num/(mp.sqrt(L)*den)


def sector_hat(N, L, t, parity):
    s2 = mp.sqrt(2)
    if parity == 'even':
        return [vhat(0, L, t)] + [(vhat(n, L, t) + vhat(-n, L, t))/s2
                                  for n in range(1, N + 1)]
    return [(vhat(n, L, t) - vhat(-n, L, t))/s2 for n in range(1, N + 1)]


PAIRS = [(0, 1), (1, 0), (2, 3), (3, 2)]


def soff_vectors(N, L, parity):
    gam = mp.mpf(GAMMA_S)
    delta = mp.mpf(BETA_S) - mp.mpf('0.5')
    taus = [gam - 1j*delta, gam + 1j*delta, -gam - 1j*delta, -gam + 1j*delta]
    return [sector_hat(N, L, t, parity) for t in taus]


def soff_apply(U, x):
    dots = {(a, b): mp.fsum(mp.conj(U[b][i])*x[i] for i in range(len(x)))
            for a, b in PAIRS}
    return [mp.fsum(U[a][m]*dots[(a, b)] for a, b in PAIRS).real
            for m in range(len(x))]


def soff_qf(U, x):
    return mp.fsum(soff_apply(U, x)[m]*x[m] for m in range(len(x)))


def soff_dense(U):
    dim = len(U[0])
    S = mp.matrix(dim, dim)
    cu = [[mp.conj(z) for z in u] for u in U]
    for m in range(dim):
        for n in range(dim):
            S[m, n] = mp.fsum(U[a][m]*cu[b][n] for a, b in PAIRS).real
    for m in range(dim):
        for n in range(m + 1, dim):
            v = (S[m, n] + S[n, m])/2
            S[m, n] = v
            S[n, m] = v
    return S


def soff_eig(U):
    """Nonzero eigenpairs of the rank-<=8 S_off via Re/Im span reduction."""
    dim = len(U[0])
    raw = []
    for u in U:
        raw.append([z.real for z in u])
        raw.append([z.imag for z in u])
    basis = []
    for r in raw:
        v = list(r)
        n0 = mp.sqrt(mp.fsum(x*x for x in v))
        if n0 == 0:
            continue
        for b in basis:
            d = mp.fsum(b[i]*v[i] for i in range(dim))
            v = [v[i] - d*b[i] for i in range(dim)]
        # second orthogonalization pass for numerical hygiene
        for b in basis:
            d = mp.fsum(b[i]*v[i] for i in range(dim))
            v = [v[i] - d*b[i] for i in range(dim)]
        nn = mp.sqrt(mp.fsum(x*x for x in v))
        if nn > mp.mpf('1e-30')*n0:
            basis.append([x/nn for x in v])
    r = len(basis)
    Sb = [soff_apply(U, b) for b in basis]
    Sr = mp.matrix(r, r)
    for i in range(r):
        for j in range(r):
            Sr[i, j] = mp.fsum(basis[i][k]*Sb[j][k] for k in range(dim))
    for i in range(r):
        for j in range(i + 1, r):
            v = (Sr[i, j] + Sr[j, i])/2
            Sr[i, j] = v
            Sr[j, i] = v
    E, V = mp.eigsy(Sr)
    pairs = []
    for k in range(r):
        p = [mp.fsum(V[i, k]*basis[i][m] for i in range(r)) for m in range(dim)]
        pn = mp.sqrt(mp.fsum(x*x for x in p))
        pairs.append((E[k], [x/pn for x in p]))
    pairs.sort(key=lambda t: t[0])
    return pairs


def analysis(lam, N, Te, vecs, son_eig=False):
    """Off-line quadruple decomposition + crash criterion (float, analysis-grade)."""
    L = 2*mp.log(lam)
    gam = mp.mpf(GAMMA_S)
    n0 = gam*L/(2*mp.pi)
    out = {'packet_n0': float(mp.nstr(n0, 8))}

    for parity in ('even', 'odd'):
        ev0, v = vecs[parity]
        mags = [abs(x) for x in v]
        offset = 0 if parity == 'even' else 1
        imax = max(range(len(v)), key=lambda i: mags[i]) + offset
        wnd = mp.fsum(mags[i]**2 for i in range(len(v))
                      if abs(i + offset - n0) <= 12)
        out[parity + '_localization'] = {
            'argmax_index': imax,
            'mass_within_12_of_n0': float(mp.nstr(wnd, 4)),
            'top4': sorted([[i + offset, float(mp.nstr(mags[i], 4))]
                            for i in range(len(v))], key=lambda p: -p[1])[:4]}

    Ue = soff_vectors(N, L, 'even')
    Uo = soff_vectors(N, L, 'odd')
    for parity, U in (('even', Ue), ('odd', Uo)):
        ev0, v = vecs[parity]
        so = soff_qf(U, v)
        out[parity + '_decomp'] = {
            'Q_float': mp.nstr(ev0, 12),
            'S_off(v)': mp.nstr(so, 12),
            'S_on(v)': mp.nstr(ev0 - so, 12)}

    eigp = soff_eig(Ue)
    out['soff_even_eigs'] = [mp.nstr(e, 8) for e, _ in eigp]
    negs = [(e, p) for e, p in eigp if e < -mp.mpf('1e-40')]
    poss = [(e, p) for e, p in eigp if e > mp.mpf('1e-40')]
    if negs:
        e1, p1 = negs[0]
        _, vg = vecs['even']
        out['coupling_nu1'] = mp.nstr(e1, 10)
        out['witness_overlap_p1'] = mp.nstr(
            abs(mp.fsum(p1[i]*vg[i] for i in range(len(vg)))), 6)
        Sd = soff_dense(Ue)
        Son = Te - Sd
        dim = Son.rows
        for e, p in poss:
            for m in range(dim):
                for n in range(dim):
                    Son[m, n] += e*p[m]*p[n]
        out['R_ray_p1'] = mp.nstr(
            -e1/mp.fsum(p1[m]*mp.fsum(Son[m, n]*p1[n] for n in range(dim))
                        for m in range(dim)), 8)
        try:
            xs = []
            for e, p in negs:
                b = mp.matrix(p)
                xs.append(mp.lu_solve(Son, b))
            r = len(negs)
            C = mp.matrix(r, r)
            for i in range(r):
                for j in range(r):
                    C[i, j] = (mp.sqrt(-negs[i][0])*mp.sqrt(-negs[j][0]) *
                               mp.fsum(negs[i][1][k]*xs[j][k]
                                       for k in range(dim)))
            for i in range(r):
                for j in range(i + 1, r):
                    v_ = (C[i, j] + C[j, i])/2
                    C[i, j] = v_
                    C[j, i] = v_
            EC, _ = mp.eigsy(C)
            out['K_inv'] = mp.nstr(max(EC), 8)
            out['K_inv_note'] = ('exact indefiniteness criterion: K_inv > 1 '
                                 'iff min eig(Te) < 0; analysis-grade float')
        except Exception as ex:
            out['K_inv'] = 'FAILED: ' + str(ex)
        if son_eig:
            ES, _ = mp.eigsy(Son)
            evs = sorted(ES[i] for i in range(dim))
            out['son_prime_low4'] = [mp.nstr(x, 8) for x in evs[:4]]
    return out


# --------------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = {a for a in sys.argv[1:] if a.startswith('--')}
    out_path, pnum, pden, N, dps_find, dps_cert = (
        args[0], int(args[1]), int(args[2]), int(args[3]),
        int(args[4]), int(args[5]))

    mp.mp.dps = dps_find
    lam = mp.mpf(pnum)/mp.mpf(pden)
    lam_str = mp.nstr(lam, 12)
    mu = float(mp.nstr(lam**2, 10))
    rec = {'lambda': lam_str, 'lambda_rational': [pnum, pden], 'mu': mu,
           'N': N, 'dps_find': dps_find, 'dps_cert': dps_cert,
           'kind': 'dh', 'date': '2026-08-26'}

    # conductor-Fuchs baseline at this mu (archived DH fit)
    a_, c_, b_ = mp.mpf(LAW_A), mp.mpf(LAW_C), mp.mpf(LAW_B)
    lneps = a_ - c_*mp.mpf(mu) + b_*mp.log(mp.mpf(mu))
    rec['baseline_ln_eps'] = float(mp.nstr(lneps, 8))
    rec['baseline_eps'] = mp.nstr(mp.e**lneps, 4)

    t_all = time.perf_counter()
    frec, vecs, Te, To = finder(lam, N, dps_find)
    rec['finder'] = frec
    print(f"[{lam_str}] finder: min_even={frec['min_even']} "
          f"min_odd={frec['min_odd']}", flush=True)

    # freeze witnesses (only sectors with negative float minimum get certified)
    witnesses = {}
    mp.mp.dps = dps_find
    for parity in ('even', 'odd'):
        ev0, v = vecs[parity]
        if ev0 < -mp.mpf('1e-45') or '--selftest' in flags:
            witnesses[parity] = [mp.nstr(x, 40) for x in v]
    rec['witness_frozen_digits'] = 40
    rec['witness'] = witnesses
    rec['certification_attempted'] = sorted(witnesses)

    if witnesses:
        M = N + 10
        K = max(30, int(0.8*dps_cert))
        cert = certify(pnum, pden, N, dps_cert, witnesses, M, K)
        rec['certificate'] = cert
        for p in sorted(witnesses):
            print(f"[{lam_str}] certified {p}: R in "
                  f"{cert[p]['rayleigh_interval']} "
                  f"neg={cert[p]['certified_negative']}", flush=True)
        if '--grid-double' in flags:
            cert2 = certify(pnum, pden, N, dps_cert, witnesses, M + 62, 64)
            rec['certificate_grid_double'] = cert2
            for p in sorted(witnesses):
                mp.mp.dps = dps_cert + 10
                c1 = (mp.mpf(cert[p]['rayleigh_interval'][0])
                      + mp.mpf(cert[p]['rayleigh_interval'][1]))/2
                c2 = (mp.mpf(cert2[p]['rayleigh_interval'][0])
                      + mp.mpf(cert2[p]['rayleigh_interval'][1]))/2
                rec.setdefault('grid_double_center_shift', {})[p] = \
                    mp.nstr(abs(c1 - c2), 3)
            print(f"[{lam_str}] grid-double shifts: "
                  f"{rec['grid_double_center_shift']}", flush=True)

    if '--skip-analysis' not in flags:
        mp.mp.dps = dps_find
        rec['analysis'] = analysis(lam, N, Te, vecs,
                                   son_eig='--son-eig' in flags)
        print(f"[{lam_str}] analysis: K_inv={rec['analysis'].get('K_inv')} "
              f"decomp_even={rec['analysis']['even_decomp']}", flush=True)

    rec['t_wall_s'] = round(time.perf_counter() - t_all, 1)
    rec['peak_rss_mb'] = round(
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576, 1)
    with open(out_path, 'w') as fh:
        json.dump(rec, fh, indent=1)
    print(f"[{lam_str}] done in {rec['t_wall_s']}s -> {out_path}", flush=True)


if __name__ == '__main__':
    main()
