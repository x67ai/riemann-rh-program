#!/usr/bin/env python3
"""
A4 M2 gate -- kernels.py (implementer, per SPEC.md sections 1, 4).

Single code path for null and dictionary columns (SPEC 1.4): every trace row and
every spectrum is computed from the same finite-circle Fourier objects.

Geometry: period N zeros on the circle of circumference N (mean gap = 1).
Harmonics j with |j| <= J = floor(lambda*N/2); u_j >= 0, sum u_j = 1, so the
sampling kernel psi(x) = sum_j u_j e^{2 pi i j x / N} has psi(0) = 1.

Configurations: on-line atoms (position theta in [0,N), integer mark m) and
off-line pairs {theta + i*d, theta - i*d} (circle-unit depth d, pair mult m).
Depth conversion (SPEC 1.2): dimensionless depth w at bandwidth lambda' is
w = 2*pi*lambda'*d, i.e. d = w/(2*pi*lambda').

Fourier data: c_s = sum_z m_z e^{-2 pi i s g_z / N} over the zero multiset
(complex g for off-line zeros). Conjugate-pair symmetry gives c_{-s} = conj(c_s).
  atoms:  c_s += m e^{-2 pi i s theta / N}
  pairs:  c_s += 2 m e^{-2 pi i s theta / N} cosh(2 pi s d / N)

Trace rows (master formula, SPEC 1.1/1.4):
  tr      = c_0 = N (mass constraint)
  tr^2    = sum_s (u*u)(s) |c_s|^2
  tr^3    = sum_{a,b} W3(a,b) c_a c_b conj(c_{a+b}),  W3(a,b) = sum_j u_{j+a} u_j u_{j-b}
Spectrum: B[j,j'] = sqrt(u_j u_{j'}) c_{j-j'} (Hermitian, (2J+1)x(2J+1)) has
exactly the nonzero spectrum of the alias-free normalized Weil-Gabor compression
G-hat (tight-frame window assembly with d'' = 2J+1 windows; derivation recorded
in RUN-REPORT.md section "Discretization"). eig moments == Fourier traces is
asserted per column (consistency gate).
"""
import math
from dataclasses import dataclass, field

import numpy as np


# ---------------------------------------------------------------- windows / kernels
def u_vec(N: int, lam: float, window=("flat",)):
    """Normalized harmonic weights u_j, j = -J..J, J = floor(lam*N/2). sum u = 1.
    window: ("flat",) or ("cos", vartheta) meaning v(sigma) = cos(2*vartheta*sigma)."""
    J = int(math.floor(lam * N / 2))
    j = np.arange(-J, J + 1)
    if window[0] == "flat":
        u = np.ones(2 * J + 1)
    elif window[0] == "cos":
        vt = float(window[1])
        sigma = j / (lam * N)          # in [-1/2, 1/2]
        u = np.cos(2 * vt * sigma)
        if np.any(u <= 0):
            raise ValueError("cos window not positive on band")
    else:
        raise ValueError(window)
    u = u / u.sum()
    return J, u


def autocorr(u):
    """(u*u)(s) for s = -(2J)..(2J), returned as full array; a[s] via index s+2J."""
    return np.convolve(u, u)


def w3_tensor(u, J):
    """W3[a,b] = sum_j u_{j+a} u_j u_{j-b}, a,b in [-2J, 2J]. Dense (4J+1)^2 array.
    Index [a+2J, b+2J]."""
    n = 2 * J + 1
    # brute but vectorized over j: fine for J <= 64
    A = np.zeros((4 * J + 1, 4 * J + 1))
    # u indexed by j in [-J, J] -> array index j+J
    for a in range(-2 * J, 2 * J + 1):
        # v_a[j] = u_{j+a} u_j, support j in [max(-J,-J-a), min(J,J-a)]
        lo = max(-J, -J - a)
        hi = min(J, J - a)
        if lo > hi:
            continue
        jj = np.arange(lo, hi + 1)
        va = u[jj + a + J] * u[jj + J]
        # W3[a,b] = sum_j va[j] * u_{j-b}; j-b in [-J,J] -> b in [j-J, j+J]
        for b in range(-2 * J, 2 * J + 1):
            jb = jj[(jj - b >= -J) & (jj - b <= J)]
            if len(jb) == 0:
                continue
            A[a + 2 * J, b + 2 * J] = np.dot(
                u[jb + a + J] * u[jb + J], u[jb - b + J])
    return A


def w3_flat_closed(J):
    """Flat window: W3[a,b] = u0^3 * #{j: j, j+a, j-b in [-J,J]}, u0 = 1/(2J+1).
    Vectorized closed form (used for large-n null runs)."""
    a = np.arange(-2 * J, 2 * J + 1)[:, None]
    b = np.arange(-2 * J, 2 * J + 1)[None, :]
    hi = np.minimum(np.minimum(J, J - a), J + b)
    lo = np.maximum(np.maximum(-J, -J - a), -J + b)
    cnt = np.clip(hi - lo + 1, 0, None).astype(float)
    return cnt / (2 * J + 1) ** 3


# ---------------------------------------------------------------- configurations
@dataclass
class Config:
    """Explicit N-periodic marked configuration (SPEC 3.1)."""
    N: int
    atom_pos: np.ndarray      # float positions in [0, N)
    atom_mrk: np.ndarray      # integer marks >= 1
    pair_pos: np.ndarray      # float positions
    pair_mrk: np.ndarray      # integer pair multiplicities >= 1
    pair_d: np.ndarray        # circle-unit depths d > 0
    tag: str = ""

    def mass(self):
        return int(round(self.atom_mrk.sum() + 2 * self.pair_mrk.sum()))

    def n_distinct(self):
        return len(self.atom_pos) + 2 * len(self.pair_pos)

    def npairs(self):
        return len(self.pair_pos)

    def max_mark(self):
        mm = 0
        if len(self.atom_mrk):
            mm = int(self.atom_mrk.max())
        if len(self.pair_mrk):
            mm = max(mm, int(self.pair_mrk.max()))
        return mm

    def key(self):
        return (tuple(np.round(self.atom_pos, 9)), tuple(self.atom_mrk),
                tuple(np.round(self.pair_pos, 9)), tuple(self.pair_mrk),
                tuple(np.round(self.pair_d, 9)))


def make_config(N, atoms=(), pairs=(), tag=""):
    """atoms: list of (pos, mark); pairs: list of (pos, mult, d_circle)."""
    ap = np.array([a[0] for a in atoms], dtype=float) % N
    am = np.array([a[1] for a in atoms], dtype=int)
    pp = np.array([p[0] for p in pairs], dtype=float) % N
    pm = np.array([p[1] for p in pairs], dtype=int)
    pd = np.array([p[2] for p in pairs], dtype=float)
    return Config(N, ap, am, pp, pm, pd, tag)


def c_coeffs(cfg: Config, smax: int):
    """c_s for s = 0..smax (c_{-s} = conj(c_s)).

    Note: Apple Accelerate's complex GEMV raises spurious FP flags (verified
    correct to 3e-14 against a pure reduction); flags suppressed locally and
    replaced by an explicit finiteness assertion."""
    s = np.arange(0, smax + 1)
    c = np.zeros(smax + 1, dtype=complex)
    with np.errstate(all="ignore"):
        if len(cfg.atom_pos):
            ph = np.exp(-2j * np.pi * np.outer(s, cfg.atom_pos) / cfg.N)
            c += ph @ cfg.atom_mrk.astype(float)
        if len(cfg.pair_pos):
            ph = np.exp(-2j * np.pi * np.outer(s, cfg.pair_pos) / cfg.N)
            ch = np.cosh(2 * np.pi * np.outer(s, cfg.pair_d) / cfg.N)
            c += (ph * ch) @ (2 * cfg.pair_mrk.astype(float))
    assert np.isfinite(c).all(), "non-finite Fourier coefficients"
    return c


def c_full(c):
    """Extend c_s (s = 0..smax) to s = -smax..smax by conjugate symmetry."""
    return np.concatenate([np.conj(c[:0:-1]), c])


# ---------------------------------------------------------------- geometry bundle
@dataclass
class Geometry:
    """Precomputed kernel data for one (N, lambda1, lambda', windows) choice."""
    N: int
    lam1: float
    lamp: float
    win1: tuple
    winp: tuple
    J1: int = 0
    Jp: int = 0
    u1: np.ndarray = None
    up: np.ndarray = None
    a1: np.ndarray = None      # autocorr of u1
    ap: np.ndarray = None      # autocorr of up
    W3p: np.ndarray = None     # cubic tensor at lambda'
    Vgrid: tuple = (2, 3, 4, 6, 8, 12, 16)

    def __post_init__(self):
        self.J1, self.u1 = u_vec(self.N, self.lam1, self.win1)
        self.Jp, self.up = u_vec(self.N, self.lamp, self.winp)
        self.a1 = autocorr(self.u1)
        self.ap = autocorr(self.up)
        if self.winp[0] == "flat":
            self.W3p = w3_flat_closed(self.Jp)
        else:
            self.W3p = w3_tensor(self.up, self.Jp)
        self.smax = max(2 * self.J1, 2 * self.Jp)

    def depth_from_w(self, w):
        """circle depth d from dimensionless depth w at bandwidth lambda'."""
        return w / (2 * np.pi * self.lamp)


def frob(c, acorr, J):
    """sum_s (u*u)(s)|c_s|^2, s in [-2J, 2J]; c indexed 0..smax."""
    s2 = np.abs(c[: 2 * J + 1]) ** 2
    # acorr index s+2J for s in [-2J, 2J]; symmetric
    w = acorr[2 * J:]          # s = 0..2J
    return float(w[0] * s2[0] + 2.0 * np.dot(w[1:], s2[1:]))


def cubic(c, W3, J):
    """sum_{a,b in [-2J,2J]} W3[a,b] c_a c_b conj(c_{a+b}); c indexed 0..smax>=2J."""
    cf = c_full(c[: 2 * J + 1])          # index s+2J for s in [-2J, 2J]
    n = 4 * J + 1
    ca = cf[:, None]
    cb = cf[None, :]
    idx = np.arange(n)[:, None] + np.arange(n)[None, :] - 2 * J   # (a+b) + 2J
    valid = (idx >= 0) & (idx < n)
    cab = np.zeros((n, n), dtype=complex)
    cab[valid] = cf[idx[valid]]
    val = np.sum(W3 * (ca * cb * np.conj(cab)))
    assert abs(val.imag) < 1e-6 * (1 + abs(val.real)), f"cubic not real: {val}"
    return float(val.real)


def b_matrix(c, u, J):
    """B[j,j'] = sqrt(u_j u_{j'}) c_{j-j'}, j in [-J, J]. Hermitian."""
    cf = c_full(c[: 2 * J + 1])
    d = np.arange(-J, J + 1)[:, None] - np.arange(-J, J + 1)[None, :]  # j-j'
    B = cf[d + 2 * J]
    ru = np.sqrt(u)
    return B * np.outer(ru, ru)


# ---------------------------------------------------------------- row evaluation
@dataclass
class Rows:
    F1: float
    Fp: float
    Cp: float
    nV: np.ndarray            # counts per Vgrid
    nneg: int
    Nd: int
    mass: int
    eig_consistency: float    # max relative deviation eig-moments vs Fourier rows
    S1: np.ndarray = None     # |c_j|^2 for j=1..N-1 (Tier-2), filled on demand


def rows_for(cfg: Config, geom: Geometry, tier2=False, neg_tol=1e-8):
    c = c_coeffs(cfg, geom.smax)
    F1 = frob(c, geom.a1, geom.J1)
    Fp = frob(c, geom.ap, geom.Jp)
    Cp = cubic(c, geom.W3p, geom.Jp)
    B = b_matrix(c, geom.up, geom.Jp)
    ev = np.linalg.eigvalsh(B)
    aev = np.abs(ev)
    nV = np.array([int(np.sum(aev >= V)) for V in geom.Vgrid])
    scale = max(1.0, aev.max())
    nneg = int(np.sum(ev < -neg_tol * scale))
    # consistency: eig moments vs Fourier traces
    t1 = ev.sum()
    t2 = float(np.sum(ev ** 2))
    t3 = float(np.sum(ev ** 3))
    dev = max(abs(t1 - cfg.mass()) / cfg.N,
              abs(t2 - Fp) / max(1.0, abs(Fp)),
              abs(t3 - Cp) / max(1.0, abs(Cp)))
    S1 = None
    if tier2:
        S1 = np.abs(c[1: cfg.N]) ** 2
    return Rows(F1, Fp, Cp, nV, nneg, cfg.n_distinct(), cfg.mass(), dev, S1), ev


# ---------------------------------------------------------------- self-test
if __name__ == "__main__":
    N = 64
    g = Geometry(N, 1.0, 0.5, ("flat",), ("flat",))
    print(f"N={N}: J1={g.J1} (harmonics {2*g.J1+1}), Jp={g.Jp} ({2*g.Jp+1})")

    # (1) single atoms: eigenvalue m, F per zero m, cubic per zero m^2
    for m in (1, 2, 3, 8):
        cfg = make_config(N, atoms=[(17.3, m)])
        # single atom alone (mass != N: fine for block checks)
        r, ev = rows_for(cfg, g)
        print(f"atom m={m}: max eig={ev[-1]:.6f} (want {m}); "
              f"Fp={r.Fp:.6f} (want {m*m}); Cp={r.Cp:.6f} (want {m**3}); "
              f"consist={r.eig_consistency:.2e}")

    # (2) pair block law: eigenvalues m(1 +/- A'), cubic 2 m^3 (1 + 3 A'^2)
    print("\npair block law at lambda'=1/2 (A' = sum_j u_j cosh(4 pi j d / N)):")
    for w in (1 / 64, 1 / 8, 1 / 4, 1 / 2, 3 / 4, 1.0, 2.0):
        d = g.depth_from_w(w)
        cfg = make_config(N, pairs=[(11.7, 1, d)])
        r, ev = rows_for(cfg, g)
        j = np.arange(-g.Jp, g.Jp + 1)
        Ap = float(np.dot(g.up, np.cosh(4 * np.pi * j * d / N)))
        pred = np.array([1 - Ap, 1 + Ap])
        got = np.array([ev[0], ev[-1]])
        cub_pred = 2 * (1 + 3 * Ap * Ap)
        print(f"w={w:5.3f}: eigs=({got[0]:+.6f},{got[1]:+.6f}) "
              f"pred=({pred[0]:+.6f},{pred[1]:+.6f}) "
              f"Cp={r.Cp:+.6f} (pred {cub_pred:+.6f}) "
              f"A'={Ap:.6f} (sinh(w)/w={math.sinh(w)/w:.6f}) "
              f"nneg={r.nneg}")

    # (3) shallow-pair continuity: w -> 0+ cubic -> +8 (doubles mimicry)
    d = g.depth_from_w(1 / 64)
    cfg = make_config(N, pairs=[(11.7, 1, d)])
    r, ev = rows_for(cfg, g)
    print(f"\nshallow pair w=1/64: cubic={r.Cp:.6f} (double: 8), eigs edge "
          f"({ev[0]:.2e}, {ev[-1]:.6f})")

    # (4) position-independence of isolated blocks
    devs = []
    for pos in (0.0, 0.37, 11.113, 40.5):
        cfg = make_config(N, pairs=[(pos, 1, g.depth_from_w(0.5))])
        r, _ = rows_for(cfg, g)
        devs.append((r.Fp, r.Cp))
    devs = np.array(devs)
    print(f"position-independence: Fp spread={np.ptp(devs[:,0]):.2e}, "
          f"Cp spread={np.ptp(devs[:,1]):.2e}")

    # (5) full-mass lattice configs: doubles corner iso values
    ndbl = 10
    nsim = N - 2 * ndbl
    sites = np.linspace(0, N, nsim + ndbl, endpoint=False)
    atoms = [(sites[i], 2 if i % 5 == 0 else 1) for i in range(nsim + ndbl)]
    # exactly ndbl doubles: every 5th of 54 sites -> 11; adjust
    marks = np.ones(nsim + ndbl, dtype=int)
    marks[:ndbl] = 2
    cfg = make_config(N, atoms=[(sites[i], marks[i]) for i in range(len(sites))])
    r, ev = rows_for(cfg, g)
    print(f"\nlattice 44 simple + 10 doubles: mass={r.mass}, Nd={r.Nd}, "
          f"F1={r.F1:.3f} (iso N+2k={N+2*ndbl}), Fp={r.Fp:.3f}, Cp={r.Cp:.3f} "
          f"(iso {nsim + 8*ndbl}), consist={r.eig_consistency:.2e}")
