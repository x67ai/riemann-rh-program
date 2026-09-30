"""e_controls.py -- task (e): where exactly does stability (the Lee-Yang property of the
Bohr lift) fail for the RH-false controls, and what do the RH-true controls do?

(A) Davenport-Heilbronn.  chi = character mod 5 with chi(2) = i; kappa from results/ccm-dh-test/dh.py.
    a(n) = Re chi(n) + kappa Im chi(n) = c chi(n) + conj(c) conj(chi(n)),  c = (1 - i kappa)/2.
    So f_DH = c L(s,chi) + conj(c) L(s,conj chi), and its S-part (n with all prime factors in S) is
        D_S(s) = c L_S(s,chi) + conj(c) L_S(s,conj chi),  L_S = prod_{p in S}(1 - chi(p)p^{-s})^{-1}.
    For p = +-1 mod 5, chi(p) = +-1 is real: the factor is common.  For p = +-2 mod 5, chi(p) = +-i and
    (1 - chi(p)w)(1 - conj chi(p) w) = 1 + w^2.  Hence, with z_p = p^{1/2-s}, c_p = p^{-1/2}:
        D_S = [common Euler factors] * N_S(z) / prod_{p in S2}(1 + c_p^2 z_p^2),
        N_S(z) = c prod_{p in S2}(1 - conj(chi(p)) c_p z_p) + conj(c) prod_{p in S2}(1 - chi(p) c_p z_p).
    (A1) identity check of the decomposition against dh.py at s = 2 + 3i (S = primes < 2e5).
    (A2) stability of N_S on the closed polydisc: minimal polyradius of a zero (< 1 = unstable).
    (A3) zeros of D_S(s) with sigma > 1/2 on the actual Kronecker line (no twist), S = primes <= X,
         near DH's off-line zero rho = 0.808517 + 85.699348 i: do they converge to rho as X grows?
(B) F_{a,q}(s) = zeta(s)(1 + a q^{-s} + q^{1-2s}): local factor in z = q^{1/2-s} is 1 + (a/sqrt q) z + z^2.
    Lee-Yang (roots on |z| = 1) iff a <= 2 sqrt q (Ramanujan at q).  Off-line zeros computed exactly.
(C) RH-true: curves over finite fields are rank-1 Lee-Yang restrictions exactly (checked on examples);
    L(s, chi_4) partial products are products of one-variable stable factors (Lee-Yang construction
    applies verbatim).  Also: zeta's own S-part never vanishes in sigma > 0 (product of nonzero factors).
"""
import numpy as np, mpmath as mp, sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'ccm-dh-test'))
import dh

mp.mp.dps = 30


def primes_upto(n):
    s = np.ones(n + 1, bool); s[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(x) for x in np.nonzero(s)[0]]


def chi5(n):
    r = n % 5
    return {0: 0, 1: 1, 2: 1j, 3: -1j, 4: -1}[r]


KAP = dh.kappa()
C = (1 - 1j * KAP) / 2


def D_S(s, S):
    L1 = mp.mpf(1); L2 = mp.mpf(1)
    for p in S:
        x = chi5(p)
        if x == 0:
            continue
        L1 /= (1 - x * mp.power(p, -s)); L2 /= (1 - mp.conj(x) * mp.power(p, -s))
    return C * L1 + mp.conj(C) * L2


def N_S_z(z, S2):
    """N_S as a polynomial in the lifted variables z_p (p in S2 = primes = +-2 mod 5)"""
    a = C; b = mp.conj(C)
    for p, zp in zip(S2, z):
        cp = mp.power(p, -0.5)
        a *= (1 - mp.conj(chi5(p)) * cp * zp)
        b *= (1 - chi5(p) * cp * zp)
    return a + b


def min_polyradius(S2, ngrid=400):
    """smallest r such that N_S has a zero with max|z_p| <= r (r < 1 means unstable).
    N_S = 0 <=> prod_p M_p(z_p) = -conj(C)/C, M_p(z) = (1 - chi(p) c z)/(1 - conj(chi(p)) c z).
    Search: all z_p on the circle |z_p| = r (a zero with max|z| <= r exists iff one exists with
    all |z_p| <= r; by the maximum principle in each variable separately the extremal zeros can be
    taken on the distinguished boundary is NOT automatic, so we scan radii and phases directly)."""
    target = -np.conj(complex(C)) / complex(C)
    cps = np.array([p ** -0.5 for p in S2]); ch = np.array([complex(chi5(p)) for p in S2])
    best = None
    for r in np.linspace(0.05, 1.2, 116):
        # image of the polydisc of radius r under log prod M_p: each M_p maps |z|<=r onto a closed disc;
        # the product hits target iff target is in the product set. Sample boundary phases.
        th = np.linspace(0, 2 * np.pi, ngrid, endpoint=False)
        logs = []
        for cp, x in zip(cps, ch):
            z = r * np.exp(1j * th)
            M = (1 - x * cp * z) / (1 - np.conj(x) * cp * z)
            logs.append(np.log(M))
        # Minkowski sum of the boundary curves (convex images of discs under log M are close to convex);
        # test: distance from log(target) to the sum set, sampled
        lt = np.log(target)
        acc = logs[0][:, None] if len(logs) == 1 else None
        if len(logs) == 1:
            dmin = np.min(np.abs(np.exp(logs[0]) - target))
            inside = None
        else:
            # two-variable reduction: for each sampled z_1..z_{k-1} on the circle, solve the last variable
            import itertools
            k = len(logs)
            sub = th[::max(1, ngrid // 60)]
            dmin = np.inf; inside = False
            for idx in itertools.product(range(len(sub)), repeat=k - 1):
                prod = 1.0 + 0j
                for j, ii in enumerate(idx):
                    z = r * np.exp(1j * sub[ii])
                    prod *= (1 - ch[j] * cps[j] * z) / (1 - np.conj(ch[j]) * cps[j] * z)
                w = target / prod   # need M_last(z_last) = w
                x = ch[-1]; cp = cps[-1]
                # (1 - x cp z)/(1 - conj(x) cp z) = w  =>  z = (1 - w)/(cp (x - w conj(x)))
                zl = (1 - w) / (cp * (x - w * np.conj(x)))
                if abs(zl) <= r:
                    inside = True
                dmin = min(dmin, abs(abs(zl) - r))
                if inside:
                    break
        if len(logs) >= 2 and inside:
            return r
    return None


def dh_zero_track(Xs, rho, radius=0.6):
    out = []
    for X in Xs:
        S = primes_upto(X)
        f = lambda s: D_S(s, S)
        try:
            z = mp.findroot(f, rho)
            out.append((X, complex(z), float(abs(f(z))), float(abs(z - rho))))
        except Exception as e:
            out.append((X, None, None, None))
    return out


def main():
    t0 = time.time()
    print('== (A1) decomposition f_DH = c L(chi) + conj(c) L(conj chi): check at s = 2 + 3i ==')
    s = mp.mpc(2, 3)
    S = primes_upto(200000)
    v1 = D_S(s, S); v2 = dh.f_dh(s)
    print('D_S(2+3i), S = primes < 2e5 :', mp.nstr(v1, 15))
    print('dh.f_dh(2+3i)               :', mp.nstr(v2, 15), '  |diff| =', mp.nstr(abs(v1 - v2), 3))
    print('kappa =', mp.nstr(KAP, 20), ' c = (1 - i kappa)/2 =', mp.nstr(C, 15))

    print('\n== (A2) stability of the lifted numerator N_S on the polydisc (primes = +-2 mod 5 only) ==')
    target = -np.conj(complex(C)) / complex(C)
    print('zero condition: prod_{p in S2} M_p(z_p) = -conj(c)/c = exp(i*%.6f)' % np.angle(target))
    for S2 in ([2], [3], [2, 3], [2, 7], [3, 7], [2, 3, 7], [7, 13], [2, 13]):
        r = min_polyradius(S2)
        reach = sum(2 * np.arcsin(p ** -0.5) for p in S2)
        print(f'S2={S2}: angular reach sum 2 arcsin(p^-1/2) = {reach:.4f} vs needed |arg| = {abs(np.angle(target)):.4f}'
              f' -> minimal polyradius of a zero ~ {r}  ({"UNSTABLE (zero inside the unit polydisc)" if (r is not None and r < 1) else "stable up to r=1.2 scan" if r is None else "stable"})')

    print('\n== (A3) zeros of the S-truncated DH series D_S(s) near DH\'s off-line zero ==')
    rho = mp.mpc('0.808517182456637', '85.699348485377592')
    print('DH off-line zero (dh.find_zero):', mp.nstr(dh.find_zero(rho), 18), ' |f_DH| =', mp.nstr(abs(dh.f_dh(rho)), 3))
    for X, z, fz, dist in dh_zero_track([7, 13, 30, 100, 300, 1000, 3000, 10000], rho):
        if z is None:
            print(f'X={X:6d}: Newton from rho did not converge')
        else:
            print(f'X={X:6d}: zero of D_S at {z.real:.6f} + {z.imag:.6f} i   |D_S|={fz:.1e}  |zero - rho| = {dist:.4f}'
                  f'  sigma - 1/2 = {z.real - 0.5:+.4f}')
        sys.stdout.flush()

    print('\n== (A3b) off-line zeros of D_S in 1/2 < sigma < 1.6, 0 < t < 100 for small S (grid + Newton) ==')
    for S in ([2, 3], [2, 3, 7], primes_upto(13), primes_upto(30)):
        found = []
        for sg in np.linspace(0.55, 1.55, 11):
            for tt in np.linspace(1, 100, 199):
                try:
                    z = mp.findroot(lambda s: D_S(s, S), mp.mpc(sg, tt))
                except Exception:
                    continue
                if 0.5 < z.real < 1.8 and 0 < z.imag < 100 and abs(D_S(z, S)) < 1e-20:
                    if not any(abs(z - w) < 1e-6 for w in found):
                        found.append(z)
        found.sort(key=lambda z: z.imag)
        print(f'S={S}: {len(found)} zeros with 1/2 < sigma, 0 < t < 100; first few:',
              [f'{complex(z).real:.4f}+{complex(z).imag:.3f}i' for z in found[:8]])
        sys.stdout.flush()

    print('\n== (B) F_{a,q} local factor 1 + (a/sqrt q) z + z^2, z = q^{1/2-s} ==')
    for q, a in ((2, 3), (5, 5), (3, 4), (5, 4), (7, 6)):
        rts = np.roots([1, a / np.sqrt(q), 1])
        sig = [0.5 - np.log(abs(r)) / np.log(q) for r in rts]
        print(f'q={q} a={a} (2 sqrt q = {2*np.sqrt(q):.4f}): |roots| = {[round(abs(r), 6) for r in rts]} '
              f'-> zeros at sigma = {[round(x, 6) for x in sig]}  '
              f'{"OFF the line (local factor not Lee-Yang: Ramanujan fails at q)" if a > 2*np.sqrt(q) else "on the line (Lee-Yang)"}')

    print('\n== (C) RH-true controls ==')
    # elliptic curves over F_5: P(u) = 1 - a u + 5 u^2; z = sqrt5 u
    for a in range(-4, 5):
        rts = np.roots([1, -a / np.sqrt(5), 1])
        print(f'E/F_5 with a_5 = {a:+d}: |roots of 1 - (a/sqrt5) z + z^2| = {[round(abs(r), 12) for r in rts]} (Lee-Yang: all = 1)')
    # genus-2 example from zoo III.15 rider: b = (1,0,-2/3,0,1)
    rts = np.roots([1, 0, -2 / 3, 0, 1])
    print('genus 2, p=3, a1=0, a2=-2: |roots| =', [round(abs(r), 12) for r in rts])
    # non-curve datum (13, 8): Hasse fails
    rts = np.roots([1, -8 / np.sqrt(13), 1])
    print('non-curve datum q=13, a=8 (|a| > 2 sqrt 13 = 7.21): |roots| =', [round(abs(r), 6) for r in rts], '(not Lee-Yang)')
    print(f'\nelapsed {time.time() - t0:.1f} s')


if __name__ == '__main__':
    main()
