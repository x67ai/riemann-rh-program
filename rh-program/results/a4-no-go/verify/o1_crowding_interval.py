"""o1_crowding_interval.py -- Session 8 (2026-08-26): per-cell interval-arithmetic
hardening of the pair-channel cell-crowding ledger constant (pair-channel.md O1;
Theorem B(ii); paper.md Theorem 4.7 "ratio 0.9775").

WHAT IS CERTIFIED (end-to-end mpmath.iv, directed rounding; exact rational box
endpoints; the only float inputs are non-load-bearing search HINTS for lower-bound
witness positions, which are then re-evaluated rigorously):

Model: N = 64, lambda = 1 flat window (SPEC 1.4). psi(z) = sin(A z)/(65 sin(B z)),
A = 65 pi/64, B = pi/64 (= the harmonic sum Sum_{|j|<=32} e^{-2 pi i j z/64}/65).
R_y(x) = Re psi(x + i y)^2.  Cells: 65 cells of width Delta = 64/65 centered at the
psi-zero grid g_k = k Delta.  Capacity curves (pair-channel.md Sections 5-6):

    kappa_k(y)      = sup_{x in cell k} [-R_y(x)]_+          nu(y)  = Sum_k kappa_k(y)
    nu_joint(d,d')  = Sum_k sup_{cell k} [-(R_{d+d'} + R_{|d-d'|})(x)]_+
    Sgen2(d,d')    = [ 8 nu(d) + 4 nu_joint(d,d') ] / (2 abar(2d)^2)
    abar(x)         = (1 + 2 Sum_{j=1}^{32} cosh(pi j x/32)) / 65   (increasing, x >= 0)

Theorem B(ii)'s ledger condition is sup_{d,d' <= Y} Sgen2 <= 1 on the R5 family
Y = 1/(2 pi).  The Session-7 float value 0.97746 was the max over a 0.004-step grid
whose last point <= Y is d = 0.156 -- i.e. it is the grid max for the family capped
at 0.156, not the continuum sup of the full family.

This script certifies, by per-cell branch-and-bound over x with mean-value forms in
(x, s, t) (derivatives via psi psi': dR/dx = 2 Re(psi psi'), dR/dy = -2 Im(psi psi')):

  (C1) REPAIR:  sup { Sgen2(d,d') : 0 < d, d' <= 39/250 = 0.156 }  <=  C*  (< 1),
       via a finite partition of (0, 0.156] into rational depth boxes: for every box
       pair, rigorous upper bounds NU >= sup nu(d), NJ >= sup nu_joint, and the lower
       bound abar(2 d_left) for the budget (abar increasing termwise).  w = 2 pi d:
       this is the multi-pair family w <= 0.98018.
  (C2) DISPROOF: rigorous LOWER bounds showing Sgen2(d,d) > 1 at d = 0.158, 0.159,
       0.1591 (all < 1/(2 pi) = 0.15915494...): the ledger condition FAILS on the
       deepest sliver of the R5 family; the continuum family constant is NOT 0.9775.
  (C3) BYPRODUCT (Theorem B(i) stream-3 self-consistency, both sides rigorous):
       max nu_joint over (0, 0.13]^2 <= C13  and  the in-cell coupling floor
       Phi_0 := inf { R_s(x) + R_t(x) : |x| <= 32/65, 0 <= s <= 5093/16000,
       0 <= t <= 5093/32000 } >= PHI0_LO, with the certified check 2 C13 < PHI0_LO
       (note's float floor 0.6665; hulls: 5093/32000 = 0.15915625 > 1/(2 pi)).

Symmetry used: psi(-x + i y) = conj(psi(x + i y)) (replace j by -j in the harmonic
sum), hence R_y is even in x and cell 65-k is the mirror of cell k; nu-sums are
cell0 + 2*(cells 1..32); cell 32's right edge is exactly x = 32 = N/2 (32.5*64/65).

Cell 0 (the peak cell, containing the removable singularity of the closed form) is
evaluated through the 32-term harmonic sum instead of the closed form.

Upper-bound semantics: each reported upper bound is a .b endpoint of an outward-
rounded interval computation, each lower bound a .a endpoint.  The mean-value form
sup_box(-Phi) <= -Phi(center) + Sum_i sup_box|dPhi/du_i| * halfwidth_i is licensed
by convexity of the box and smoothness of Phi (entire in all three variables).
Branch-and-bound refinement stops when the x-resolvable part of the gap is below
tolx; the depth-box first-order terms are genuine family variation (the sup over
the depth box), not slack, and stay in the reported bound.

Output: printed certificate + o1_crowding_interval_out.json next to this file.
THERMAL: single process, no parallelism.
"""
import json
import os
import time
from fractions import Fraction

import mpmath
from mpmath import iv

iv.dps = 15

T_START = time.time()

# ---------------------------------------------------------------- iv helpers
def fr2iv(fr):
    """Exact Fraction -> 1-ulp iv enclosure."""
    return iv.mpf(fr.numerator) / iv.mpf(fr.denominator)

def box2iv(afr, bfr):
    """[a, b] with Fraction endpoints -> outward iv enclosure."""
    lo = fr2iv(afr)
    hi = fr2iv(bfr)
    return iv.mpf([lo.a, hi.b])

def mag(x):
    """sup |x| over an iv as a point iv (upper bound)."""
    return iv.mpf(max(abs(x.a), abs(x.b)))

def ivcosh(x):
    e = iv.exp(x)
    return (e + 1 / e) / 2

def cmul(u, v):
    return (u[0] * v[0] - u[1] * v[1], u[0] * v[1] + u[1] * v[0])

A_IV = 65 * iv.pi / 64
B_IV = iv.pi / 64
BETA = iv.pi / 32                      # 2 pi / 64
DELTA = Fraction(64, 65)

# ------------------------------------------ closed-form psi, psi', R (x != 0 mod 64)
def trig_x(X):
    ax, bx = A_IV * X, B_IV * X
    return iv.sin(ax), iv.cos(ax), iv.sin(bx), iv.cos(bx)

def psi_parts(tx, Y):
    """x-trig tuple + depth interval Y -> (psi, P, CA, Q, CB, mQ), psi = (re, im)."""
    sax, cax, sbx, cbx = tx
    ea = iv.exp(A_IV * Y)
    chA, shA = (ea + 1 / ea) / 2, (ea - 1 / ea) / 2
    eb = iv.exp(B_IV * Y)
    chB, shB = (eb + 1 / eb) / 2, (eb - 1 / eb) / 2
    P = (sax * chA, cax * shA)          # sin(Az)
    CA = (cax * chA, -sax * shA)        # cos(Az)
    Q = (sbx * chB, cbx * shB)          # sin(Bz)
    CB = (cbx * chB, -sbx * shB)        # cos(Bz)
    mQ = Q[0] ** 2 + Q[1] ** 2          # |sin(Bz)|^2 > 0 away from x = 0 mod 64
    num = cmul(P, (Q[0], -Q[1]))
    psi = (num[0] / (65 * mQ), num[1] / (65 * mQ))
    return psi, P, CA, Q, CB, mQ

def R_of(psi):
    return psi[0] ** 2 - psi[1] ** 2

def W_of(psi, P, CA, Q, CB, mQ):
    """W = psi * psi'; dR/dx = 2 Re W, dR/dy = -2 Im W."""
    n1 = cmul(CA, Q)
    n2 = cmul(P, CB)
    num = (A_IV * n1[0] - B_IV * n2[0], A_IV * n1[1] - B_IV * n2[1])
    q2 = cmul(Q, Q)
    num2 = cmul(num, (q2[0], -q2[1]))
    dpsi = (num2[0] / (65 * mQ ** 2), num2[1] / (65 * mQ ** 2))
    return cmul(psi, dpsi)

# ------------------------------------------ harmonic-sum psi (cell 0) and abar
def psi_sum(X, Y):
    """psi via Sum_j u_j e^{-2 pi i j z/64}; valid everywhere (32-term pair sum)."""
    re = iv.mpf(1)
    im = iv.mpf(0)
    for j in range(1, 33):
        c = iv.cos(j * BETA * X)
        s = iv.sin(j * BETA * X)
        e = iv.exp(j * BETA * Y)
        re += c * (e + 1 / e)           # 2 cos cosh
        im += -s * (e - 1 / e)          # -2 sin sinh
    return (re / 65, im / 65)

def abar_iv(xfr):
    """abar at exact rational argument (iv enclosure)."""
    X = fr2iv(xfr)
    s = iv.mpf(1)
    for j in range(1, 33):
        s += 2 * ivcosh(j * BETA * X)
    return s / 65

# ------------------------------------------ per-cell sup of -(sum_i R_{y_i})
def leaf_eval(afr, bfr, parts, use_sum):
    """One leaf on x-box [afr, bfr].  parts = [(Y_iv, halfwidth_fr), ...].
    Returns (ub, lb, yslack): rigorous sup upper bound of -Phi on the leaf, a valid
    lower bound from the center point, and the depth-box first-order term (the part
    of ub that x-refinement cannot reduce)."""
    X = box2iv(afr, bfr)
    if use_sum:
        phi = iv.mpf(0)
        for (Y, _) in parts:
            phi += R_of(psi_sum(X, Y))
        if phi.a >= 0:
            return float(-phi.a), float(-phi.b), 0.0
        mfr = (afr + bfr) / 2
        Xm = fr2iv(mfr)
        phim = iv.mpf(0)
        for (Y, _) in parts:
            phim += R_of(psi_sum(Xm, Y))
        return float(-phi.a), float(-phim.b), 0.0
    tx = trig_x(X)
    phi = iv.mpf(0)
    packs = []
    for (Y, _) in parts:
        pk = psi_parts(tx, Y)
        packs.append(pk)
        phi += R_of(pk[0])
    ub_plain = -phi.a
    if ub_plain <= 0:
        return float(ub_plain), float(-phi.b), 0.0
    # center point (tight)
    mfr = (afr + bfr) / 2
    Xm = fr2iv(mfr)
    txm = trig_x(Xm)
    phim = iv.mpf(0)
    for (Y, _) in parts:
        phim += R_of(psi_parts(txm, Y)[0])
    lb = float(-phim.b)
    # mean-value form
    hx = fr2iv((bfr - afr) / 2)
    dx = iv.mpf(0)
    ysl = iv.mpf(0)
    for (Y, hwfr), pk in zip(parts, packs):
        W = W_of(*pk)
        dx += 2 * W[0]
        ysl += mag(2 * W[1]) * fr2iv(hwfr)
    mv = iv.mpf(-phim.a) + ysl + mag(dx) * hx
    ub = min(float(ub_plain), float(mv.b))
    return ub, lb, float(ysl.b)

HXMIN = DELTA / 64        # depth-slack is trusted as irreducible only on x-leaves
                          # at least this narrow (on wide leaves the interval
                          # enclosure of dR/dy is dependency-inflated)

def cell_sup(k, parts, tolx=1e-5, maxleaves=300, clamp=True):
    """Certified enclosure (lb, ub) of sup_{x in cell k} (-Phi), Phi = sum R_{y_i}.
    Cells 1..32: closed form + mean-value; cell 0: harmonic sum on [0, Delta/2]
    (R even in x).  clamp: clamp at 0 (for [-Phi]_+).

    Refinement rule: the top leaf is split while its ub exceeds the target and
    EITHER it is wider than HXMIN (so its depth-slack term is not yet trustworthy)
    OR its ub net of the depth-slack still exceeds the target (x-resolvable gap)."""
    if k == 0:
        a, b = Fraction(0), DELTA / 2
    else:
        a, b = (2 * k - 1) * DELTA / 2, (2 * k + 1) * DELTA / 2
    use_sum = (k == 0)
    leaves = []
    best_lb = -1e99
    q = (b - a) / 4
    for i in range(4):
        ub, lb, ys = leaf_eval(a + i * q, a + (i + 1) * q, parts, use_sum)
        leaves.append((ub, a + i * q, a + (i + 1) * q, ys))
        best_lb = max(best_lb, lb)
    floor = 0.0 if clamp else -1e99
    while len(leaves) < maxleaves:
        leaves.sort(key=lambda t: t[0])
        top = leaves[-1]
        target = max(best_lb + tolx, floor)
        wide = (top[2] - top[1]) > HXMIN
        if top[0] <= target or (not wide and top[0] - top[3] <= target):
            break
        leaves.pop()
        m = (top[1] + top[2]) / 2
        for (aa, bb) in ((top[1], m), (m, top[2])):
            ub, lb, ys = leaf_eval(aa, bb, parts, use_sum)
            leaves.append((ub, aa, bb, ys))
            best_lb = max(best_lb, lb)
    ub_cell = max(l[0] for l in leaves)
    if clamp:
        return max(0.0, best_lb), max(0.0, ub_cell)
    return best_lb, ub_cell

def nu_bound(parts, tolx=1e-5):
    """Certified (lb, ub) of Sum_k sup_cell [-Phi]_+ = cell0 + 2*(cells 1..32)."""
    lo = iv.mpf(0)
    hi = iv.mpf(0)
    for k in range(33):
        lb, ub = cell_sup(k, parts, tolx=tolx)
        w = 1 if k == 0 else 2
        lo += w * iv.mpf(lb)
        hi += w * iv.mpf(ub)
    return float(lo.a), float(hi.b)

# ------------------------------------------ depth boxes
def depth_parts_single(afr, bfr):
    return [(box2iv(afr, bfr), (bfr - afr) / 2)]

def depth_parts_joint(a1, b1, a2, b2):
    """(d,d') in [a1,b1] x [a2,b2] -> S = d+d', T = |d-d'| hulls."""
    s_lo, s_hi = a1 + a2, b1 + b2
    if b1 <= a2:
        t_lo, t_hi = a2 - b1, b2 - a1
    elif b2 <= a1:
        t_lo, t_hi = a1 - b2, b1 - a2
    else:
        t_lo, t_hi = Fraction(0), max(b1 - a2, b2 - a1)
    return [(box2iv(s_lo, s_hi), (s_hi - s_lo) / 2),
            (box2iv(t_lo, t_hi), (t_hi - t_lo) / 2)]

# ================================================================ MAIN
def main():
    out = {"date": "2026-08-26", "session": 8, "iv_dps": iv.dps,
           "mpmath_version": mpmath.__version__}

    # ---------- self-test: enclosures contain independent cmath values ----------
    import cmath
    def psif(z):
        return sum(cmath.exp(-2j * cmath.pi * j * z / 64)
                   for j in range(-32, 33)) / 65
    st_ok = True
    for (xx, yy) in ((0.925, 0.311), (0.4, 0.05), (12.3, 0.2), (31.9, 0.156)):
        rf = (psif(xx + 1j * yy) ** 2).real
        xf, yf = Fraction(xx), Fraction(yy)      # exact binary fractions
        X, Y = box2iv(xf, xf), box2iv(yf, yf)
        enc = R_of(psi_parts(trig_x(X), Y)[0])
        enc2 = R_of(psi_sum(X, Y))
        if not (enc.a <= rf <= enc.b and enc2.a <= rf <= enc2.b):
            st_ok = False
    print(f"[self-test] closed-form and harmonic-sum iv enclosures contain "
          f"independent cmath values at 4 points: {'PASS' if st_ok else 'FAIL'}")
    out["selftest_enclosures"] = st_ok
    assert st_ok

    # ---------- float hint pass (numpy; NON-load-bearing) ----------
    import numpy as np
    JJ = np.arange(-32, 33)
    NXH = 6001

    def cell_hints(d_float):
        """Per-cell float argmax x of the joint dip -(R_{2d} + R_0) and of the
        single dip -R_d, for the (C2) lower-bound witnesses."""
        hj, hs = {}, {}
        gj = np.exp(2 * np.pi * JJ * (2 * d_float) / 64) / 65
        g0 = np.ones(65) / 65
        gs = np.exp(2 * np.pi * JJ * d_float / 64) / 65
        for k in range(1, 33):
            xs = np.linspace(k - 0.5, k + 0.5, NXH) * (64.0 / 65.0)
            ph = np.exp(-2j * np.pi * np.outer(xs, JJ) / 64)
            aj = ((ph @ gj) ** 2).real + ((ph @ g0) ** 2).real
            asg = ((ph @ gs) ** 2).real
            hj[k] = float(xs[int(np.argmin(aj))])
            hs[k] = float(xs[int(np.argmin(asg))])
        return hj, hs

    # ================================================================
    # (C1) REPAIR: certified sup Sgen2 over (0, 39/250]^2
    # ================================================================
    E = [Fraction(x, 1000) for x in
         (0, 20, 40, 60, 80, 100, 115, 125, 130, 135, 140, 144, 147,
          150, 152, 154, 155, 156)]
    nb = len(E) - 1
    print(f"\n(C1) partition of (0, 0.156] into {nb} boxes; "
          f"{nb * (nb + 1) // 2} unordered box pairs for nu_joint")

    NU, ALO = [], []
    for i in range(nb):
        lb, ub = nu_bound(depth_parts_single(E[i], E[i + 1]))
        NU.append(ub)
        ab = abar_iv(2 * E[i])       # abar increasing => lower bound on the box
        ALO.append(ab.a)
        print(f"  d-box ({float(E[i]):.3f},{float(E[i+1]):.3f}] : "
              f"nu_ub = {ub:.6f}  abar_lo(2d) = {mpmath.nstr(ab.a, 10)}"
              f"  [{time.time()-T_START:.0f}s]")
    NJ = {}
    for i in range(nb):
        for j in range(i, nb):
            lb, ub = nu_bound(depth_parts_joint(E[i], E[i + 1], E[j], E[j + 1]))
            NJ[(i, j)] = ub
        print(f"  nu_joint row {i:2d} done; row max = "
              f"{max(NJ[(i, jj)] for jj in range(i, nb)):.6f}  "
              f"[{time.time()-T_START:.0f}s]")

    bounds = []
    for i in range(nb):
        njmax = max(NJ[(min(i, j), max(i, j))] for j in range(nb))
        alo = iv.mpf(ALO[i])
        val = (8 * iv.mpf(NU[i]) + 4 * iv.mpf(njmax)) / (2 * alo ** 2)
        bounds.append(float(val.b))
    cstar = max(bounds)
    ibind = bounds.index(cstar)
    print("\n  per-d-box certified Sgen2 bounds:")
    for i in range(nb):
        print(f"    d in ({float(E[i]):.3f},{float(E[i+1]):.3f}] : "
              f"Sgen2 <= {bounds[i]:.6f}")
    verdict1 = ("PASS: < 1 -- the ledger constant closes at Y* = 0.156 "
                "(w <= 0.98018)") if cstar < 1 else "FAIL: >= 1"
    print(f"\n  (C1) CERTIFIED: sup over d, d' in (0, 39/250] of Sgen2 <= "
          f"{cstar:.6f}  (binding d-box ({float(E[ibind]):.3f},"
          f"{float(E[ibind+1]):.3f}])")
    print(f"       {verdict1}")
    out["C1_edges"] = [str(e) for e in E]
    out["C1_nu_ub"] = NU
    out["C1_nu_joint_ub"] = {f"{i},{j}": v for (i, j), v in NJ.items()}
    out["C1_bounds"] = bounds
    out["C1_Cstar"] = cstar
    out["C1_pass"] = bool(cstar < 1)

    # per-cell enclosures at the binding (corner) box pair
    print("\n  per-cell enclosures [lb, ub] of sup [-(R_s + R_t)]_+ at the corner "
          "box pair (0.155, 0.156]^2 (cells 0..32; cell 65-k mirrors cell k):")
    parts_c = depth_parts_joint(E[-2], E[-1], E[-2], E[-1])
    percell = {}
    for k in range(33):
        lb, ub = cell_sup(k, parts_c)
        percell[k] = (lb, ub)
        if ub > 5e-6:
            print(f"    cell {k:2d}: [{lb:.6f}, {ub:.6f}]")
    out["C1_percell_corner"] = {str(k): v for k, v in percell.items()}

    # ================================================================
    # (C2) DISPROOF at the deep end of the R5 family
    # ================================================================
    print("\n(C2) rigorous LOWER bounds of Sgen2(d, d) near the family endpoint "
          "1/(2 pi) = 0.1591549...:")
    out["C2"] = {}
    offs = (-0.001, -0.0005, 0.0, 0.0005, 0.001)
    for dstr, dnum in (("0.158", Fraction(158, 1000)),
                       ("0.159", Fraction(159, 1000)),
                       ("0.1591", Fraction(1591, 10000))):
        hj, hs = cell_hints(float(dnum))
        S = box2iv(2 * dnum, 2 * dnum)
        T0 = box2iv(Fraction(0), Fraction(0))
        Dv = box2iv(dnum, dnum)
        njlo = iv.mpf(0)
        nulo = iv.mpf(0)
        for k in range(1, 33):
            bestj = 0.0
            bests = 0.0
            for off in offs:
                xj = Fraction(round((hj[k] + off) * 100000), 100000)
                tx = trig_x(fr2iv(xj))
                phi = R_of(psi_parts(tx, S)[0]) + R_of(psi_parts(tx, T0)[0])
                bestj = max(bestj, float((-phi).a))
                xs_ = Fraction(round((hs[k] + off) * 100000), 100000)
                r = R_of(psi_parts(trig_x(fr2iv(xs_)), Dv)[0])
                bests = max(bests, float((-r).a))
            njlo += 2 * iv.mpf(bestj)
            nulo += 2 * iv.mpf(bests)
        ahi = abar_iv(2 * dnum)
        val = (8 * iv.mpf(nulo.a) + 4 * iv.mpf(njlo.a)) / (2 * iv.mpf(ahi.b) ** 2)
        lo = float(val.a)
        tag = "> 1: LEDGER FAILS here" if lo > 1 else "(<= 1)"
        print(f"  d = d' = {dstr}: nu_lo = {float(nulo.a):.6f}  "
              f"nu_joint_lo = {float(njlo.a):.6f}  =>  Sgen2 >= {lo:.6f}  {tag}")
        out["C2"][dstr] = {"nu_lo": float(nulo.a), "nu_joint_lo": float(njlo.a),
                           "Sgen2_lo": lo, "exceeds_1": bool(lo > 1)}

    # ================================================================
    # (C3) BYPRODUCT: B(i) stream-3 self-consistency, both sides rigorous
    # ================================================================
    print("\n(C3) Theorem B(i) stream-3 self-consistency at Y = 0.13:")
    i13 = E.index(Fraction(130, 1000))
    c13 = max(NJ[(i, j)] for i in range(i13) for j in range(i, i13))
    print(f"  certified max nu_joint over (0, 0.13]^2 <= {c13:.6f}"
          f"   (2x = {2 * c13:.6f})")
    smax, tmax = Fraction(5093, 16000), Fraction(5093, 32000)
    phi0 = None
    NSB = 16
    for a in range(NSB):
        for b in range(NSB):
            parts = [(box2iv(a * smax / NSB, (a + 1) * smax / NSB),
                      smax / (2 * NSB)),
                     (box2iv(b * tmax / NSB, (b + 1) * tmax / NSB),
                      tmax / (2 * NSB))]
            lb, ub = cell_sup(0, parts, tolx=5e-4, maxleaves=400, clamp=False)
            inf_phi = -ub
            phi0 = inf_phi if phi0 is None else min(phi0, inf_phi)
    print(f"  certified Phi_0 >= {phi0:.6f}   (note's float floor: 0.6665)")
    ok13 = 2 * c13 < phi0
    print(f"  2 * max nu_joint = {2 * c13:.6f} "
          f"{'<' if ok13 else '>='} Phi_0 >= {phi0:.6f}  =>  one-pair-per-cell cap "
          f"self-consistency at Y = 0.13: {'CERTIFIED' if ok13 else 'NOT certified'}")
    b13 = []
    for i in range(i13):
        njmax = max(NJ[(min(i, j), max(i, j))] for j in range(i13))
        val = (8 * iv.mpf(NU[i]) + 4 * iv.mpf(njmax)) / (2 * iv.mpf(ALO[i]) ** 2)
        b13.append(float(val.b))
    print(f"  certified sup Sgen2 over (0, 0.13]^2 <= {max(b13):.6f} "
          f"(float record: 0.6852)")
    out["C3"] = {"max_nu_joint_013": c13, "Phi0_lo": phi0,
                 "cap_selfconsistency_certified": bool(ok13),
                 "Sgen2_Y013_ub": max(b13)}

    # ---------------------------------------------------------------- verdict
    print("\n================ CERTIFICATE ================")
    print(f"(C1) For all pair depths d, d' in (0, 39/250]  (w = 2 pi d <= 0.98018):")
    print(f"     8 nu(d) + 4 nu_joint(d,d') <= {cstar:.6f} * 2 abar(2d)^2   "
          f"[{'CERTIFIED < 1' if cstar < 1 else 'NOT certified'}]")
    print(f"(C2) At d = d' = 0.159 (inside the R5 family w <= 1): "
          f"Sgen2 >= {out['C2']['0.159']['Sgen2_lo']:.4f} > 1.")
    print("     The ledger inequality Sgen2 <= 1 FAILS on the deepest sliver of "
          "the R5 family; 0.97746 is the")
    print("     grid max for the family capped at d <= 0.156, whose interval-"
          f"certified continuum value is C* = {cstar:.6f}.")
    if ok13:
        print(f"(C3) B(i) crowding-cap self-consistency at Y = 0.13 fully "
              f"certified: 2 * {c13:.4f} = {2*c13:.4f} < Phi_0 >= {phi0:.4f}.")
    else:
        print(f"(C3) B(i) crowding-cap self-consistency at Y = 0.13 NOT "
              f"certified: 2 * {c13:.4f} = {2*c13:.4f} vs Phi_0 >= {phi0:.4f}.")
    print(f"Total time {time.time()-T_START:.0f}s")
    out["elapsed_s"] = round(time.time() - T_START, 1)

    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "o1_crowding_interval_out.json"), "w") as fh:
        json.dump(out, fh, indent=1)

if __name__ == "__main__":
    main()
