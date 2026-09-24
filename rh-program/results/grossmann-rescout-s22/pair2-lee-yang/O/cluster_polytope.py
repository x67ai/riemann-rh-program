#!/usr/bin/env python3
"""Scout O, PAIR 2 (W1-26 Lee-Yang) -- exact infeasibility certificates + realizations.

LEMMA (multiaffine vertex lemma; proved in scout-O.md section 5.2).  For an n-site +-1
ferromagnet with x_ij = exp(-2 J_ij) in [0, 1], the normalized coefficients
Q_k(x) = sum_{|S|=k} prod_{i in S, j not in S} x_ij are multiaffine in x (each x_ij occurs
at most once in each cut product).  Hence the vector (Q_1, ..., Q_{n//2}) lies in the convex
hull of its values at the vertices x in {0,1}^E.  At a vertex, edges with x = 0 lock their
ends (J = infinity) and edges with x = 1 are free (J = 0), so Z/Z(0) = prod_C (1 + z^{|C|})
over the connected clusters C of locked edges: the vertex values depend only on the integer
partition of n.  CLUSTER POLYTOPE K_n := conv{ coeffs of prod_{c in lambda} (1 + z^c) :
lambda a partition of n }.  Necessary condition: T in K_n.

Per class and orientation s, for m = m_pos .. while n = 2g + m <= NLP:
  LP (scipy HiGHS): min lambda0 + lambda.T s.t. lambda0 + lambda.V_pi >= 0 for all partitions,
  |lambda| <= 1.  Negative optimum -> separating functional; it is rationalized and
  RE-CHECKED EXACTLY (Fractions on the integer vertices; exact sign of X + Y/sqrt q on T).
  m_poly = first m with T in K_n (no exact separator).
Then realization search (feasibility.solve) at m = m_poly .. m_poly + EXTRA while n <= NMAX.
Controls (zoo V.4): a non-RH datum must fail the realization search; a planted
ferromagnet's own polynomial must be realized.
"""
import itertools, json, math, os, sys, time
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import feasibility as F  # target_parts, sign_xy, weil_poly, solve, mp_check

NLP = int(os.environ.get("NLP", "40"))
NMAX = int(os.environ.get("NMAX", "13"))
EXTRA = int(os.environ.get("EXTRA", "3"))
t0 = time.time()


def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


_V = {}


def vertices(n):
    if n in _V:
        return _V[n]
    rows, labels = [], []
    for lam in partitions(n):
        poly = [1]
        for c in lam:
            new = [0] * (len(poly) + c)
            for i, a in enumerate(poly):
                new[i] += a
                new[i + c] += a
            poly = new
        rows.append(poly[1:n // 2 + 1])
        labels.append(lam)
    _V[n] = (rows, labels)
    return _V[n]


def lp_separate(n, parts, q):
    """returns (inside: bool, certificate or None). parts: exact (X, Y) coefficient pairs."""
    rows, labels = vertices(n)
    K = n // 2
    scale = [math.comb(n, k) for k in range(1, K + 1)]
    V = np.array([[r[k] / scale[k] for k in range(K)] for r in rows], dtype=float)
    T = np.array([float(parts[k + 1][0] + parts[k + 1][1] / math.sqrt(q)) / scale[k]
                  for k in range(K)])
    # variables: lambda0, lambda_1..K ; minimize lambda0 + lambda.T
    c = np.concatenate([[1.0], T])
    A = -np.hstack([np.ones((len(V), 1)), V])     # -(lambda0 + lambda.V) <= 0
    b = np.zeros(len(V))
    res = linprog(c, A_ub=A, b_ub=b, bounds=[(-1, 1)] * (K + 1), method="highs")
    if res.status != 0 or res.fun > -1e-9:
        return True, None
    # rationalize and re-check exactly
    lam = [Fraction(v).limit_denominator(10 ** 6) for v in res.x]
    # exact: lambda0 + sum_k lambda_k * V_k / scale_k >= 0 for every vertex
    lam_true = [lam[0]] + [lam[k + 1] / scale[k] for k in range(K)]
    minv = min(lam_true[0] + sum(lam_true[k + 1] * r[k] for k in range(K)) for r in rows)
    if minv < 0:  # shift lambda0 up to restore validity exactly
        lam_true[0] -= minv
    # value at T:  lambda0 + sum lambda_k (X_k + Y_k / sqrt q)
    X = lam_true[0] + sum(lam_true[k + 1] * parts[k + 1][0] for k in range(K))
    Y = sum(lam_true[k + 1] * parts[k + 1][1] for k in range(K))
    sgn = F.sign_xy(X, Y, q)
    if sgn < 0:
        # tight vertices of the certificate (for the record)
        vals = [lam_true[0] + sum(lam_true[k + 1] * r[k] for k in range(K)) for r in rows]
        tight = [labels[i] for i, v in enumerate(vals) if v == 0][:6]
        return False, {"lambda": [str(v) for v in lam_true], "value_at_T_float":
                       float(X + Y / math.sqrt(q)), "tight_partitions": tight}
    return True, None  # LP said outside but exact check failed: treat as not certified


def run(r, orient_list=(1, -1)):
    q, a, g = F.weil_poly(r)
    rec = {"p": q, "g": g, "a1": r["a1"]}
    if g == 2:
        rec["a2"] = r["a2"]
    for s in orient_list:
        key = "noflip" if s == 1 else "flip"
        out = {}
        v1 = F.target_parts(q, a, s, 0)
        if F.sign_xy(sum(x for x, _ in v1), sum(y for _, y in v1), q) == 0:
            out.update(status="unrealizable-all-m", reason="root at z = 1")
            rec[key] = out
            continue
        m = 0
        while not all(F.sign_xy(X, Y, q) > 0 for X, Y in F.target_parts(q, a, s, m)):
            m += 1
        out["m_pos"] = m
        cert = []
        m_poly = None
        mm = m
        while 2 * g + mm <= NLP:
            inside, c = lp_separate(2 * g + mm, F.target_parts(q, a, s, mm), q)
            if inside:
                m_poly = mm
                break
            cert.append({"m": mm, "n": 2 * g + mm, **c})
            mm += 1
        out["certified_outside_polytope_for_m"] = [c["m"] for c in cert]
        out["certificates"] = cert[:2] + (cert[-1:] if len(cert) > 2 else [])
        out["m_poly"] = m_poly
        out["search"] = []
        found = None
        if m_poly is not None:
            for mm in range(m_poly, m_poly + EXTRA + 1):
                n = 2 * g + mm
                if n > NMAX:
                    out["search"].append({"m": mm, "n": n, "skipped": "n > NMAX"})
                    break
                parts = F.target_parts(q, a, s, mm)
                mp.mp.dps = 40
                T = [mp.mpf(X.numerator) / X.denominator +
                     (mp.mpf(Y.numerator) / Y.denominator) / mp.sqrt(q) for X, Y in parts]
                best = F.solve(n, T, F.NSTART)
                att = {"m": mm, "n": n, "best": best[0] if best else None}
                if best and best[0] < 1e-11:
                    rel, circ = F.mp_check(n, best[1], T)
                    att.update(realized=True, Jmin=float(best[1].min()),
                               Jmax=float(best[1].max()), mp_rel_coef_err=rel,
                               max_root_modulus_dev=circ,
                               J=[round(float(x), 10) for x in best[1]])
                    out["search"].append(att)
                    found = mm
                    break
                att["realized"] = False
                out["search"].append(att)
        if found is not None:
            out["status"] = "realized"
        elif m_poly is None:
            out["status"] = "certified-unrealizable-all-m<=%d" % (NLP - 2 * g)
        else:
            out["status"] = "undecided"
        out["m_real"] = found
        rec[key] = out
    return rec


def fmt(rec):
    tag = "g=%d p=%d a1=%d%s" % (rec["g"], rec["p"], rec["a1"],
                                (" a2=%d" % rec["a2"]) if rec["g"] == 2 else "")
    parts = []
    for key in ("noflip", "flip"):
        if key not in rec:
            continue
        o = rec[key]
        if o["status"] == "unrealizable-all-m":
            parts.append("%s: UNREALIZABLE-ALL-m (root z=1)" % key)
            continue
        s = "%s: %s m_pos=%d m_poly=%s m_real=%s" % (key, o["status"], o["m_pos"], o["m_poly"],
                                                   o["m_real"])
        if o["search"] and o["search"][-1].get("realized"):
            a = o["search"][-1]
            s += " n=%d Jmax=%.3f mpErr=%.1e rootDev=%.1e" % (a["n"], a["Jmax"],
                                                           a["mp_rel_coef_err"],
                                                           a["max_root_modulus_dev"])
        elif o["search"]:
            a = o["search"][-1]
            s += " lastSearch(m=%d,best=%s)" % (a["m"], a.get("best", a.get("skipped")))
        parts.append(s)
    return tag + " | " + " | ".join(parts)


def main():
    which = os.environ.get("WHICH", "all")
    out = os.environ.get("OUT", "cluster_polytope.json")
    g1 = json.load(open(os.path.join(HERE, "classes_g1.json")))
    g2 = json.load(open(os.path.join(HERE, "classes_g2.json")))
    if which == "controls":
        # V.4 controls. (i) non-RH datum (g=1, p=13, a1=8: |a1| > 2 sqrt 13): must NOT be realized.
        # (ii) non-RH g=2 datum (p=5, a1=0, a2=12: w^2 + 12/5 - 2 has no real root): must not.
        # (iii) planted ferromagnet: 4 sites, J = (0.3,0.1,0.7,0.2,0.5,0.4); its own coefficients
        #       must be realized.
        recs = []
        for r in ({"p": 13, "a1": 8}, {"p": 5, "a1": 0, "a2": 12}):
            recs.append(run(r, (1,)))
        for rr in recs:
            print("CONTROL non-RH:", fmt(rr))
        edges, cut, levels = F.system(4)
        J = np.array([0.3, 0.1, 0.7, 0.2, 0.5, 0.4])
        w = np.exp(-2 * cut @ J)
        sizes = np.array(list(itertools.product((0, 1), repeat=4))).sum(1)
        T = [mp.mpf(float(w[sizes == k].sum())) for k in range(5)]
        best = F.solve(4, T, 12)
        print("CONTROL planted 4-site ferromagnet: best residual %.2e (realized: %s)"
              % (best[0], best[0] < 1e-11))
        return
    classes = g1 if which == "g1" else g2 if which == "g2" else g1 + g2
    res = []
    for r in classes:
        rec = run(r)
        res.append(rec)
        print(fmt(rec), flush=True)
    json.dump(res, open(os.path.join(HERE, out), "w"), indent=0)
    print("elapsed s: %.1f" % (time.time() - t0))


if __name__ == "__main__":
    main()
