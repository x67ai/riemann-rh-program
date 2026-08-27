"""
run_fuchs.py -- prolate eigenvalue leakage vs the CCM-quoted Fuchs 1964 law.

Operators (CCM 2511.22755 Lemma 7.2(ii) context, gamma = 2 pi lambda^2 = c):
  (A) compressed cosine transform  (P_lambda F P_lambda on evens):
      kernel  2*lambda*cos(c u v)  on [0,1]^2, eigenvalues chi_n, n=0,4,8,... -> +1
  (B) folded sinc (time-and-band-limiting on evens):
      kernel  sin(c(u-v))/(pi(u-v)) + sin(c(u+v))/(pi(u+v)) on [0,1]^2,
      eigenvalues lambda_n (n even); consistency: chi_n^2 = lambda_n.

CCM-quoted Fuchs law (n=4):  1 - chi(lambda) ~ (2^14/3) sqrt2 pi^5 e^{-4 pi lambda^2 + 9 log lambda}
i.e. ratio  R := (1-chi_4) / (lambda^9 e^{-4 pi lambda^2})  ->  (2^14/3) sqrt2 pi^5 ~ 2.3634e6.

Usage: python3 run_fuchs.py
"""
import json
import time
import mpmath as mp
import weilform as wf

mp.mp.dps = 70

MUS = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
OUT = []


def nystrom_eigs(kernel, n):
    """Global n-point GL Nystrom on [0,1]; symmetrized; all eigenvalues desc."""
    xs, ws = wf.gl_nodes(n)
    Y = [(x + 1)/2 for x in xs]
    W = [w/2 for w in ws]
    A = mp.matrix(n, n)
    for i in range(n):
        for j in range(i, n):
            v = mp.sqrt(W[i]*W[j])*kernel(Y[i], Y[j])
            A[i, j] = v
            A[j, i] = v
    E = mp.eigsy(A, eigvals_only=True)
    return sorted([E[i] for i in range(n)], reverse=True)


for mu_s in MUS:
    mu = mp.mpf(mu_s)
    c = 2*mp.pi*mu
    lam = mp.sqrt(mu)
    M = int(1.3*float(c)) + 30       # global GL points
    t0 = time.time()

    kcos = lambda u, v: 2*lam*mp.cos(c*u*v)
    chis = nystrom_eigs(kcos, M)
    # convergence check on the key quantity
    chis_lo = nystrom_eigs(kcos, M - 12)
    conv = mp.nstr(abs((1 - chis[1]) - (1 - chis_lo[1])), 4)

    def ksinc(u, v):
        d, s = u - v, u + v
        t1 = c/mp.pi if d == 0 else mp.sin(c*d)/(mp.pi*d)
        t2 = c/mp.pi if s == 0 else mp.sin(c*s)/(mp.pi*s)
        return t1 + t2
    lams = nystrom_eigs(ksinc, M)

    one_minus_chi = [mp.mpf(1) - x for x in chis[:4]]
    one_minus_lam = [mp.mpf(1) - x for x in lams[:4]]
    # CCM/Fuchs ratio for the n=4 mode = 2nd largest cosine eigenvalue
    R4 = one_minus_chi[1]/(lam**9*mp.e**(-4*mp.pi*lam**2))
    R0 = one_minus_chi[0]/(lam*mp.e**(-4*mp.pi*lam**2))
    # consistency chi^2 vs sinc-even eigenvalue: chi_0^2 =? lam_0, chi_4^2 =? lam_4(3rd)
    cons = [mp.nstr(chis[0]**2 - lams[0], 4), mp.nstr(chis[1]**2 - lams[2], 4)]
    rec = {
        'mu': mu_s, 'c': mp.nstr(c, 10), 'M_points': M, 'conv_check_1mchi4': conv,
        'chi_top4': [mp.nstr(x, 20) for x in chis[:4]],
        'one_minus_chi_top4': [mp.nstr(x, 15) for x in one_minus_chi],
        'sinc_top4': [mp.nstr(x, 20) for x in lams[:4]],
        'one_minus_sinc_top4': [mp.nstr(x, 15) for x in one_minus_lam],
        'ln_one_minus_chi0': mp.nstr(mp.log(one_minus_chi[0]), 12),
        'ln_one_minus_chi4': mp.nstr(mp.log(one_minus_chi[1]), 12),
        'R4_vs_CCM_2.3634e6': mp.nstr(R4, 10),
        'R0': mp.nstr(R0, 10),
        'chi_sq_vs_sinc_consistency': cons,
        'time_s': round(time.time() - t0, 1),
    }
    OUT.append(rec)
    print(f"mu={mu_s}: 1-chi0={rec['one_minus_chi_top4'][0]} 1-chi4={rec['one_minus_chi_top4'][1]} "
          f"R4={rec['R4_vs_CCM_2.3634e6']} ({rec['time_s']}s)", flush=True)
    with open('outputs/fuchs.json', 'w') as fh:
        json.dump(OUT, fh, indent=1)

print('done')
