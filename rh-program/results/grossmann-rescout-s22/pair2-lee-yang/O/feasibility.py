#!/usr/bin/env python3
"""Scout O, PAIR 2 (W1-26 Lee-Yang), Session 24 item 2 -- the (R-b) feasibility step.

Question (PRICING.md 2(c), line 128): is T_m(z) := P(z/sqrt q) (1+z)^m, up to a positive
constant, the partition function Z(z) = sum_{S subset [n]} z^{|S|} exp(sum_{i<j} J_ij s_i s_j)
of an n = 2g + m site +-1 ferromagnet (J_ij >= 0 finite, uniform fugacity z per up spin)?

Normalizing by exp(sum J), Z(z)/Z(0) = sum_S z^{|S|} prod_{i in S, j not in S} x_ij with
x_ij = exp(-2 J_ij) in (0, 1].  Unknowns: C(n,2) couplings; equations: coefficients
k = 1 .. floor(n/2) (the polynomial is palindromic on both sides).

Per class and per orientation s (s = +1: the literal target; s = -1: the flip z -> -z,
which is the quadratic twist, P_twist(T) = P(-T)):
  (1) m_pos(s) = least m with every coefficient of T_m strictly positive -- decided EXACTLY
      (each coefficient is X + Y/sqrt(q) with X, Y rational; its sign is decided in integers).
      For m < m_pos no ferromagnet exists (every coefficient of Z is a positive sum).
      If P(s/sqrt q) = 0 (a root at z = 1), T_m(1) = 0 for every m while Z(1) > 0: no m works.
  (2) for m = m_pos, m_pos+1, ... up to n <= NMAX: bounded least squares (J in [0, JMAX])
      on r_k = log Q_k(J) - log T_k, several random starts; success = max |r_k| < 1e-11,
      then an independent mpmath (40 digits) recomputation of Z from the found J and a
      root check |z| = 1.
Outputs: feasibility.json (per class records) and stdout log.
"""
import itertools, json, math, os, sys, time
from fractions import Fraction
import numpy as np
from scipy.optimize import least_squares
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
NMAX = int(os.environ.get("NMAX", "13"))
JMAX = float(os.environ.get("JMAX", "12"))
NSTART = int(os.environ.get("NSTART", "12"))
EXTRA_M = int(os.environ.get("EXTRA_M", "4"))
rng = np.random.default_rng(20260924)
t0 = time.time()


def target_parts(q, a, s, m):
    """Coefficients of P(s z/sqrt q)(1+z)^m as pairs (X, Y): value = X + Y/sqrt(q).
    a = [a0=1, a1, ..., a_{2g}] with P(T) = sum a_k T^k; b_k = a_k s^k q^{-k/2}.
    For k even, q^{-k/2} rational; for k odd, q^{-k/2} = q^{-(k-1)/2} / sqrt q."""
    d = len(a) - 1
    b = []
    for k in range(d + 1):
        sk = s ** k
        if k % 2 == 0:
            b.append((Fraction(a[k] * sk, q ** (k // 2)), Fraction(0)))
        else:
            b.append((Fraction(0), Fraction(a[k] * sk, q ** ((k - 1) // 2))))
    out = []
    for k in range(d + m + 1):
        X = Fraction(0); Y = Fraction(0)
        for j in range(max(0, k - m), min(d, k) + 1):
            c = math.comb(m, k - j)
            X += c * b[j][0]; Y += c * b[j][1]
        out.append((X, Y))
    return out


def sign_xy(X, Y, q):
    """exact sign of X + Y/sqrt(q)  (= sign of X sqrt(q) + Y)."""
    if X == 0 and Y == 0:
        return 0
    if X >= 0 and Y >= 0:
        return 1
    if X <= 0 and Y <= 0:
        return -1
    # opposite signs: compare X^2 q with Y^2
    lhs, rhs = X * X * q, Y * Y
    if lhs == rhs:
        return 0
    return (1 if X > 0 else -1) if lhs > rhs else (1 if Y > 0 else -1)


def weil_poly(r):
    q = r["p"]
    if "a2" in r:
        return q, [1, r["a1"], r["a2"], q * r["a1"], q * q], 2
    return q, [1, r["a1"], q], 1


_cache = {}


def system(n):
    if n in _cache:
        return _cache[n]
    edges = list(itertools.combinations(range(n), 2))
    subsets = np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int8)
    size = subsets.sum(axis=1)
    cut = np.array([[s[i] != s[j] for (i, j) in edges] for s in subsets], dtype=np.float64)
    half = n // 2
    levels = [np.where(size == k)[0] for k in range(1, half + 1)]
    _cache[n] = (edges, cut, levels)
    return _cache[n]


def solve(n, T, tries):
    edges, cut, levels = system(n)
    logT = np.log(np.array([float(T[k]) for k in range(1, n // 2 + 1)]))
    E = len(edges)

    def fun(J):
        w = np.exp(-2.0 * cut @ J)
        return np.array([math.log(w[L].sum()) for L in levels]) - logT

    def jac(J):
        w = np.exp(-2.0 * cut @ J)
        rows = []
        for L in levels:
            Qk = w[L].sum()
            rows.append(-2.0 * (cut[L].T @ w[L]) / Qk)
        return np.array(rows)

    best = None
    for t in range(tries):
        J0 = rng.uniform(0.0, 1.5 if t % 2 == 0 else 4.0, E)
        try:
            res = least_squares(fun, J0, jac=jac, bounds=(0.0, JMAX), xtol=1e-15,
                                ftol=1e-15, gtol=1e-15, max_nfev=3000)
        except Exception as e:  # pragma: no cover
            continue
        err = float(np.max(np.abs(res.fun)))
        if best is None or err < best[0]:
            best = (err, res.x.copy())
        if err < 1e-11:
            break
    return best


def mp_check(n, J, T):
    """recomputation of Z(z)/Z(0) coefficients: cut sums in float64 (exact for the
    rounded J), exponentials and level sums at 40 digits; roots of the result."""
    mp.mp.dps = 40
    edges, cut, levels = system(n)
    subsets = np.array(list(itertools.product((0, 1), repeat=n)), dtype=np.int8)
    size = subsets.sum(axis=1)
    ex = 2.0 * (cut @ np.asarray(J, dtype=np.float64))
    coef = [mp.mpf(0)] * (n + 1)
    for e, k in zip(ex, size):
        coef[int(k)] += mp.exp(-mp.mpf(float(e)))
    rel = max(abs(coef[k] / T[k] - 1) for k in range(n + 1))
    roots = np.roots([float(c) for c in coef[::-1]])
    circ = float(np.max(np.abs(np.abs(roots) - 1.0)))
    return float(rel), circ


def run_class(r):
    q, a, g = weil_poly(r)
    rec = {"p": q, "g": g, "a1": r["a1"]}
    if g == 2:
        rec["a2"] = r["a2"]
    for s in (+1, -1):
        key = "noflip" if s == 1 else "flip"
        out = {}
        # root at z = 1?
        v1 = target_parts(q, a, s, 0)
        tot = (sum(x for x, _ in v1), sum(y for _, y in v1))
        if sign_xy(tot[0], tot[1], q) == 0:
            out.update(status="unrealizable-all-m", reason="P(s/sqrt q) = 0: root at z = 1")
            rec[key] = out
            continue
        m = 0
        while True:
            parts = target_parts(q, a, s, m)
            if all(sign_xy(X, Y, q) > 0 for X, Y in parts):
                break
            m += 1
            if m > 200:
                raise RuntimeError("m_pos > 200")
        out["m_pos"] = m
        out["attempts"] = []
        mp.mp.dps = 40
        found = None
        for mm in range(m, m + EXTRA_M + 1):
            n = 2 * g + mm
            if n > NMAX:
                out["attempts"].append({"m": mm, "n": n, "skipped": "n > NMAX"})
                break
            parts = target_parts(q, a, s, mm)
            T = [X + Y / mp.sqrt(q) for X, Y in [(mp.mpf(X.numerator) / X.denominator,
                                                   mp.mpf(Y.numerator) / Y.denominator)
                                                  for X, Y in parts]]
            best = solve(n, T, NSTART)
            att = {"m": mm, "n": n, "best_max_abs_log_residual": best[0] if best else None}
            if best and best[0] < 1e-11:
                J = best[1]
                rel, circ = mp_check(n, J, T)
                att.update(realized=True, Jmin=float(J.min()), Jmax=float(J.max()),
                           J_at_bound=bool(J.max() > JMAX - 1e-6),
                           mp_rel_coef_err=rel, max_root_modulus_dev=circ,
                           J=[round(float(x), 12) for x in J])
                out["attempts"].append(att)
                found = mm
                break
            att["realized"] = False
            out["attempts"].append(att)
        out["status"] = "realized" if found is not None else "not-found"
        out["m_real"] = found
        rec[key] = out
    return rec


def main():
    g1 = json.load(open(os.path.join(HERE, "classes_g1.json")))
    g2 = json.load(open(os.path.join(HERE, "classes_g2.json")))
    only = os.environ.get("ONLY")
    classes = [r for r in g1 + g2 if (only is None or (only == "g1") == ("a2" not in r))]
    results = []
    for i, r in enumerate(classes):
        rec = run_class(r)
        results.append(rec)
        tag = "g=%d p=%d a1=%d%s" % (rec["g"], rec["p"], rec["a1"],
                                    (" a2=%d" % rec["a2"]) if rec["g"] == 2 else "")
        line = []
        for key in ("noflip", "flip"):
            o = rec[key]
            if o["status"] == "unrealizable-all-m":
                line.append("%s: UNREALIZABLE all m (root at z=1)" % key)
            else:
                a = o["attempts"][-1]
                line.append("%s: m_pos=%d m_real=%s best=%.1e%s" % (
                    key, o["m_pos"], o["m_real"], a.get("best_max_abs_log_residual") or float("nan"),
                    (" Jmax=%.3f mpErr=%.1e rootDev=%.1e" % (a["Jmax"], a["mp_rel_coef_err"],
                                                             a["max_root_modulus_dev"]))
                    if a.get("realized") else ""))
        print(tag, "|", " | ".join(line), flush=True)
    json.dump(results, open(os.path.join(HERE, os.environ.get("OUT", "feasibility.json")), "w"),
              indent=0)
    print("elapsed s: %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
