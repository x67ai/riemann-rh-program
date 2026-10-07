"""
stair.py -- evaluators for the "staircase" chains of seed N2, and zero-census tools.

GENERAL THETA CHAIN.  A completed function G with theta series
    Theta(x) = sum_k b_k e^{-pi k^2 x / Q},   b_k = c_k k^kap   (kap = 0 even type, kap = 1 odd type),
    G(s) = int_0^inf Theta(x) x^{(s+kap)/2} dx/x ,
and the modular relation Theta(1/x) = x^{1/2+kap} Theta(x) + C (sqrt(x) - 1) [C = 0 for kap = 1],
split at x = 1 (Riemann's second proof) gives, for ALL s,
    G(s) = -2C (1/s + 1/(1-s)) + sum_k b_k T_k(s),
    T_k(s) = X^{-(s+kap)/2} Gamma((s+kap)/2, X) + X^{-(1-s+kap)/2} Gamma((1-s+kap)/2, X),  X = pi k^2 / Q.
A CHAIN MEMBER keeps weights w_k in [0, 1] (w_k = 1 for k in an index set, else 0; or a smooth cutoff):
    G_w(s) = -2C (1/s + 1/(1-s)) + sum_k w_k b_k T_k(s).
Entire normalizations used for zero counting:
    kap = 0:  E_w(s) = (1/2) s (s-1) G_w(s)  = C + (1/2) s (s-1) sum_k w_k b_k T_k(s)     [xi_N for zeta]
    kap = 1:  E_w(s) = G_w(s).
Both satisfy E(1-s) = E(s) and E(conj s) = conj E(s) (real coefficients), so E is real on Re s = 1/2.

EVALUATION.  Two independent routes:
  'tail'  : E_w = E_full - (s(s-1)/2)^{[kap=0]} sum_k (1 - w_k) b_k T_k(s), with E_full from zeta / Hurwitz zeta /
            Dirichlet L (no cancellation near the critical line, where E_full is exponentially small);
  'direct': E_w from the truncated sum itself (cancellation of ~log10(1/|E|) digits; run at raised precision).
The census uses 'tail'; 'direct' is the cross-check for reported zeros.
"""
import mpmath as mp

# ----------------------------------------------------------------------------------------------
# chain definitions
# ----------------------------------------------------------------------------------------------


class Chain:
    """kind: 'zeta', 'Faq', 'DH', 'chi4'.  coeff(k) -> c_k ; kap ; Q ; C (polar constant, kap=0 only)."""

    def __init__(self, kind, a=None, q=None):
        self.kind = kind
        if kind == 'zeta':
            self.kap, self.Q, self.C = 0, mp.mpf(1), mp.mpf(1)/2
            self.coeff = lambda k: 1
        elif kind == 'Faq':
            self.a, self.q = mp.mpf(a), int(q)
            self.kap, self.Q, self.C = 0, mp.mpf(q)**2, (1 + self.a + self.q)/2
            qq = self.q
            self.coeff = lambda k: 1 + (self.a if k % qq == 0 else 0) + (qq if k % (qq*qq) == 0 else 0)
        elif kind == 'DH':
            self.kap, self.Q, self.C = 1, mp.mpf(5), mp.mpf(0)
            self.coeff = self._dh_coeff
        elif kind == 'chi4':
            self.kap, self.Q, self.C = 1, mp.mpf(4), mp.mpf(0)
            self.coeff = lambda k: (0, 1, 0, -1)[k % 4]
        else:
            raise ValueError(kind)

    @staticmethod
    def kappa_dh():
        s5 = mp.sqrt(5)
        return (mp.sqrt(10 - 2*s5) - 2)/(s5 - 1)

    def _dh_coeff(self, k):
        r = k % 5
        if r == 0:
            return 0
        kap = self.kappa_dh()
        return {1: mp.mpf(1), 2: kap, 3: -kap, 4: mp.mpf(-1)}[r]

    # ---- full completed function (entire normalization E) ----
    def E_full(self, s):
        k = self.kind
        if k == 'zeta':
            return s*(s - 1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
        if k == 'Faq':
            q, a = self.q, self.a
            xi = s*(s - 1)/2 * mp.pi**(-s/2) * mp.gamma(s/2) * mp.zeta(s)
            return xi * (mp.mpf(q)**s + a + mp.mpf(q)**(1 - s))
        if k == 'DH':
            kap = self.kappa_dh()
            f = 5**(-s)*(mp.zeta(s, mp.mpf(1)/5) + kap*mp.zeta(s, mp.mpf(2)/5)
                         - kap*mp.zeta(s, mp.mpf(3)/5) - mp.zeta(s, mp.mpf(4)/5))
            return (5/mp.pi)**((s + 1)/2) * mp.gamma((s + 1)/2) * f
        if k == 'chi4':
            L = mp.dirichlet(s, [0, 1, 0, -1])
            return (4/mp.pi)**((s + 1)/2) * mp.gamma((s + 1)/2) * L
        raise ValueError

    def T(self, s, k):
        X = mp.pi * k * k / self.Q
        kap = self.kap
        a1 = (s + kap)/2
        a2 = (1 - s + kap)/2
        return X**(-a1) * mp.gammainc(a1, X) + X**(-a2) * mp.gammainc(a2, X)

    def pref(self, s):
        return s*(s - 1)/2 if self.kap == 0 else mp.mpf(1)

    # ---- chain members ----
    def E_direct(self, s, w, kmax):
        """w: function k -> weight in [0,1]; sums k = 1..kmax."""
        acc = mp.fsum(w(k) * self.coeff(k) * k**self.kap * self.T(s, k)
                      for k in range(1, kmax + 1) if w(k) != 0 and self.coeff(k) != 0)
        return self.C + self.pref(s) * acc if self.kap == 0 else acc

    def E_tail(self, s, w, kextra=None):
        """E_w = E_full - pref * sum_k (1-w_k) b_k T_k, k up to where terms are negligible."""
        full = self.E_full(s)
        pref = self.pref(s)
        # terms negligible when e^{-X} X^{|Re s|/2} tiny relative to working precision
        eps = mp.mpf(10)**(-mp.mp.dps - 8)
        scale = max(abs(full), mp.mpf(10)**(-10**6))
        acc = mp.mpc(0)
        k = 1
        kmin_needed = int(mp.sqrt(max(abs(s), 1) * self.Q / mp.pi)) + 3
        small_run = 0
        while True:
            wk = w(k)
            ck = self.coeff(k)
            if wk != 1 and ck != 0:
                term = (1 - wk) * ck * k**self.kap * self.T(s, k)
                acc += term
                mag = abs(pref * term)
                if k > kmin_needed and mag < eps * max(scale, abs(pref*acc)):
                    small_run += 1
                else:
                    small_run = 0
            else:
                if k > kmin_needed:
                    small_run += 1
            if k > kmin_needed and small_run >= 3:
                # verify a crude bound for the rest: terms decay faster than geometric here
                break
            k += 1
            if kextra is not None and k > kextra:
                break
            if k > 5000:
                raise RuntimeError('tail did not converge')
        return full - pref * acc


def w_trunc(N):
    return lambda k: 1 if k <= N else 0


def smooth_numbers_weight(S):
    S = list(S)

    def w(k):
        m = k
        for p in S:
            while m % p == 0:
                m //= p
        return 1 if m == 1 else 0
    return w


def c_N(N):
    """limit of xi_N(1/2+it) as |t| -> inf, computed as the positive tail sum."""
    return mp.fsum((4*mp.pi*n*n - 1) * mp.exp(-mp.pi*n*n) for n in range(N + 1, N + 60))


# ----------------------------------------------------------------------------------------------
# argument principle along a polyline (adaptive), zero census in rectangles
# ----------------------------------------------------------------------------------------------


def arg_change_segment(f, z0, z1, n0=16, maxdepth=30, cache=None, dmax=0.6):
    """Total change of arg f along the straight segment z0 -> z1, adaptively refined so that
    each step changes arg by at most dmax (radians) AND the step is consistent at half-step
    (arg(f(mid)) splits the step into two pieces each < dmax). Returns (delta, samples, minabs)."""
    def F(z):
        if cache is not None:
            key = (mp.nstr(z.real, 25), mp.nstr(z.imag, 25))
            if key in cache:
                return cache[key]
            v = f(z)
            cache[key] = v
            return v
        return f(z)

    pts = [z0 + (z1 - z0) * mp.mpf(j)/n0 for j in range(n0 + 1)]
    vals = [F(z) for z in pts]
    total = mp.mpf(0)
    minabs = min(abs(v) for v in vals)
    stack = [(pts[j], vals[j], pts[j + 1], vals[j + 1], 0) for j in range(n0)][::-1]
    while stack:
        za, va, zb, vb, d = stack.pop()
        if va == 0 or vb == 0:
            raise ZeroDivisionError('zero on contour at %s' % mp.nstr(za if va == 0 else zb, 15))
        dab = mp.arg(vb / va)
        if d >= maxdepth:
            raise RuntimeError('max depth reached near %s' % mp.nstr(za, 15))
        zm = (za + zb)/2
        vm = F(zm)
        minabs = min(minabs, abs(vm))
        d1 = mp.arg(vm / va)
        d2 = mp.arg(vb / vm)
        if abs(dab) <= dmax and abs(d1) <= dmax and abs(d2) <= dmax and abs(d1 + d2 - dab) < 1e-8:
            total += d1 + d2
        else:
            stack.append((zm, vm, zb, vb, d + 1))
            stack.append((za, va, zm, vm, d + 1))
    return total, minabs


def count_zeros_rect(f, s1, s2, t1, t2, n0=16, cache=None, dmax=0.6):
    """Number of zeros of f in the open rectangle [s1,s2] x [t1,t2] (argument principle)."""
    c = [mp.mpc(s1, t1), mp.mpc(s2, t1), mp.mpc(s2, t2), mp.mpc(s1, t2)]
    tot = mp.mpf(0)
    mins = []
    for j in range(4):
        d, m = arg_change_segment(f, c[j], c[(j + 1) % 4], n0=n0, cache=cache, dmax=dmax)
        tot += d
        mins.append(m)
    n = tot / (2*mp.pi)
    return n, min(mins)


def sign_change_zeros(fr, t1, t2, h):
    """Zeros of the real function fr on [t1,t2] by sign changes on a grid of step h, refined
    by bisection+secant. Returns list of zeros and list of 'suspicious' local minima of |fr|
    (no sign change but small value relative to neighbors), for close-pair detection."""
    n = int(mp.ceil((t2 - t1)/h))
    ts = [t1 + (t2 - t1)*mp.mpf(j)/n for j in range(n + 1)]
    vs = [fr(t) for t in ts]
    zs = []
    susp = []
    for j in range(n):
        if vs[j] == 0:
            zs.append(ts[j])
            continue
        if mp.sign(vs[j]) != mp.sign(vs[j + 1]) and vs[j + 1] != 0:
            z = mp.findroot(fr, (ts[j], ts[j + 1]), solver='anderson')
            zs.append(z)
    for j in range(1, n):
        a, b, c = abs(vs[j - 1]), abs(vs[j]), abs(vs[j + 1])
        if b < a and b < c and mp.sign(vs[j - 1]) == mp.sign(vs[j]) == mp.sign(vs[j + 1]):
            susp.append((ts[j], vs[j], max(a, c)))
    return zs, susp


# ----------------------------------------------------------------------------------------------
# root refinement with RELATIVE tolerances (the functions are ~1e-70 in size near the line)
# ----------------------------------------------------------------------------------------------


def refine_real_root(fr, a, b, fa=None, fb=None, tol=None, maxit=200):
    """Illinois-bracketed root of a real function on [a,b] with a sign change; tolerance on |b-a|."""
    a, b = mp.mpf(a), mp.mpf(b)
    fa = fr(a) if fa is None else fa
    fb = fr(b) if fb is None else fb
    tol = tol or mp.mpf(10)**(-(mp.mp.dps - 6)) * max(1, abs(a))
    side = 0
    for _ in range(maxit):
        if abs(b - a) < tol:
            break
        c = (a*fb - b*fa)/(fb - fa)
        if not (min(a, b) < c < max(a, b)):
            c = (a + b)/2
        fc = fr(c)
        if fc == 0:
            return c
        if mp.sign(fc) == mp.sign(fb):
            b, fb = c, fc
            if side == -1:
                fa /= 2
            side = -1
        else:
            a, fa = c, fc
            if side == 1:
                fb /= 2
            side = 1
        # occasional bisection to guarantee shrinkage
        if _ % 7 == 6:
            m = (a + b)/2
            fm = fr(m)
            if mp.sign(fm) == mp.sign(fa):
                a, fa = m, fm
            else:
                b, fb = m, fm
    return (a + b)/2


def secant_complex(f, s0, s1=None, tol=None, maxit=100):
    """Secant iteration for an analytic f; stops when |ds| < tol (relative-to-1 scale)."""
    tol = tol or mp.mpf(10)**(-(mp.mp.dps - 8))
    s0 = mp.mpc(s0)
    s1 = mp.mpc(s1) if s1 is not None else s0 + mp.mpc('1e-6', '1e-6')
    f0, f1 = f(s0), f(s1)
    for it in range(maxit):
        if f1 == f0:
            break
        s2 = s1 - f1*(s1 - s0)/(f1 - f0)
        if abs(s2 - s1) < tol * max(1, abs(s2)):
            return s2, it, True
        s0, f0 = s1, f1
        s1, f1 = s2, f(s2)
    return s1, maxit, False


def E_auto(chain, s, w, N, loss_margin=25):
    """Direct formula when it does not cancel (far from the line), tail formula otherwise."""
    s = mp.mpc(s)
    if s.real < mp.mpf(1)/2:
        s = 1 - s  # symmetry E(1-s) = E(s)
    if s.real > 6:
        with mp.workdps(mp.mp.dps + 10):
            v = chain.E_direct(s, w, N)
            # magnitude of the largest summand, for a cancellation check
            big = abs(chain.C) if chain.kap == 0 else mp.mpf(0)
            big = max(big, abs(chain.pref(s) * chain.T(s, 1)))
        if big == 0 or abs(v) > big * mp.mpf(10)**(-(mp.mp.dps - loss_margin)):
            return +v
    return chain.E_tail(s, w)
