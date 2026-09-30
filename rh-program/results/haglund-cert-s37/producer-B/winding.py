"""winding.py -- rigorous zero count of an entire f in a closed square S = c + [-r, r]^2 (Producer B).  CERT.md section W.
 (W1) Cauchy: f(z) = sum a_k (z-c)^k with |a_k| <= M_R / R^k, M_R >= max_{|z-c|=R} |f|; M_R from box enclosures of f on
      nbox boxes covering the circle (each box = bounding box of an arc's chord widened by the sagitta).
 (W2) DFT on m points c + rho w^j (w = e^{2 pi i/m}):  D_k = (1/m) sum_j f(c + rho w^j) w^{-jk} rho^{-k} = sum_{l>=0} a_{k+lm} rho^{lm}.
 (W3) For |z-c| <= r' < R:  |f(z) - sum_{k<K} D_k (z-c)^k| <= E := M_R [ q^m/(1-q^m) sum_{k<K} x^k + x^K/(1-x) ],  q = rho/R, x = r'/R.
 (W4) Boundary walk: each piece's enclosure  P(piece box) + disk(E)  must exclude 0 (convex set, so the continuous argument
      change along the piece is the principal arg of F(end)/F(start)); pieces are bisected until every enclosure excludes 0
      and every ratio box lies in Re > 0.  Winding k = (sum of increments)/2pi = number of zeros in the open square.
"""
from fractions import Fraction
from ivc import *


def circle_pt(c, rad, frac):
    ang = 2 * iv.pi * R(frac)
    return c + C(R(rad) * iv.cos(ang), R(rad) * iv.sin(ang))


def crude_bound(f, c, Rad, nbox):
    sag = R(Rad) * (1 - iv.cos(iv.pi / nbox))
    M = mp.mpf(0)
    for j in range(nbox):
        p0 = circle_pt(c, Rad, Fraction(j, nbox))
        p1 = circle_pt(c, Rad, Fraction(j + 1, nbox))
        B = C(hull(p0.re, p1.re), hull(p0.im, p1.im)).widen(sag)
        M = max(M, f(B).absup())
    return M


def taylor_model(f, c, Rad, rho, m, K, nbox, log=print):
    MR = crude_bound(f, c, Rad, nbox)
    log('  crude bound M_R = %s on |z-c| = %s (%d boxes)' % (mp.nstr(MR, 6), Rad, nbox))
    vals = [f(circle_pt(c, rho, Fraction(j, m))) for j in range(m)]
    D = []
    for k in range(K):
        acc = C(0)
        for j in range(m):
            ang = -2 * iv.pi * R(Fraction(j * k % m, m))
            acc = acc + vals[j] * C(iv.cos(ang), iv.sin(ang))
        D.append(acc / m / R(rho) ** k)
    return D, MR, vals


def model_error(MR, Rad, rho, m, K, rp):
    q = R(rho) / R(Rad)
    x = R(rp) / R(Rad)
    if not hi(x) < 1:
        raise ValueError('r\' must be < R')
    geo = sum((x ** k for k in range(K)), R(0))
    E = R(MR) * (q ** m / (1 - q ** m) * geo + x ** K / (1 - x))
    return hi(E)


def horner(D, zc):
    acc = C(0)
    for a in reversed(D):
        acc = acc * zc + a
    return acc


def winding(D, E, c, r, pieces_per_side=8, maxdepth=14, log=print):
    """argument-principle count on the square c + [-r, r]^2 (counterclockwise) with the model (D, E)."""
    rr = R(r)
    V = [c + C(-rr, -rr), c + C(rr, -rr), c + C(rr, rr), c + C(-rr, rr)]
    stats = {'pieces': 0, 'minabs': None, 'maxwidth': mp.mpf(0)}

    def F(zbox):
        return horner(D, zbox - c).widen(E)

    def pt(a, b, t):
        return V[a] + (V[b] - V[a]) * R(t)

    def piece(a, b, t0, t1, depth):
        p0, p1 = pt(a, b, t0), pt(a, b, t1)
        Bx = C(hull(p0.re, p1.re), hull(p0.im, p1.im))
        FB = F(Bx)
        F0, F1 = F(p0), F(p1)
        ok = not FB.contains0()
        if ok:
            try:
                qq = F1 / F0
                ok = lo(qq.re) > 0
            except ZeroDivisionError:
                ok = False
        if not ok:
            if depth >= maxdepth:
                raise RuntimeError('boundary piece cannot exclude 0 (side %d, t in [%s, %s])' % (a, t0, t1))
            tm = (t0 + t1) / 2
            return piece(a, b, t0, tm, depth + 1) + piece(a, b, tm, t1, depth + 1)
        stats['pieces'] += 1
        ab = FB.abslo()
        stats['minabs'] = ab if stats['minabs'] is None else min(stats['minabs'], ab)
        d = arg_right(qq)
        stats['maxwidth'] = max(stats['maxwidth'], hi(d) - lo(d))
        return d

    total = R(0)
    for a in range(4):
        b = (a + 1) % 4
        for j in range(pieces_per_side):
            total = total + piece(a, b, Fraction(j, pieces_per_side), Fraction(j + 1, pieces_per_side), 0)
    k = total / (2 * iv.pi)
    kint = int(mp.nint((lo(k) + hi(k)) / 2))
    certified = (lo(k) > kint - mp.mpf('0.5')) and (hi(k) < kint + mp.mpf('0.5'))
    log('  winding: %d pieces, all enclosures exclude 0 (min |F| over pieces >= %s, E = %s); sum/2pi in [%s, %s] -> k = %d%s'
        % (stats['pieces'], mp.nstr(stats['minabs'], 4), mp.nstr(E, 4), mp.nstr(lo(k), 12), mp.nstr(hi(k), 12), kint,
           '' if certified else '  (NOT CERTIFIED)'))
    return kint if certified else None, stats


def newton_on_model(D, c, steps=6):
    """non-rigorous location estimate of the model's zero near c (midpoint arithmetic)."""
    a = [d.mid() for d in D]
    e = mp.mpc(0)
    for _ in range(steps):
        p = sum(a[k] * e ** k for k in range(len(a)))
        dp = sum(k * a[k] * e ** (k - 1) for k in range(1, len(a)))
        e = e - p / dp
    return c.mid() + e
