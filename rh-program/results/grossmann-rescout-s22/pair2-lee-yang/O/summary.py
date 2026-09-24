#!/usr/bin/env python3
"""Scout O, PAIR 2 -- tallies of the (R-b) computation + the zeros-as-input realizations.

Reads cluster_polytope_g1.json and cluster_polytope_g2p{3,5,7}.json (+ satellite.json if
present, which upgrades 'undecided' records that the satellite search realized).
Also checks, for every class, the two ZEROS-AS-INPUT realizations:
  (Z0) untwisted product of two-spin factors (1 + 2 x_j z + z^2), x_j = -cos(theta_j) in (0,1]:
       exists iff every cos(theta_j) < 0 (after dividing out nothing; m = 0);
  (Z1) Newman 1974 Example 2.3 twisted pairs (n_1 = n_2 = 1): factor cosh(2z/a) - exp(-2J),
       i.e. (1 - 2 e^{-2J} z + z^2) up to normalization -> realizes cos(theta_j) = e^{-2J_j} > 0;
       together with (Z0) for cos < 0 and Example 2.1 (single spin, cosh) for cos = 0 this
       realizes every RH-true class with J_j = -1/2 log|cos theta_j| >= 0.
"""
import json, math, os
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
mp.mp.dps = 50


def load(name):
    p = os.path.join(HERE, name)
    return json.load(open(p)) if os.path.exists(p) else []


g1 = load("cluster_polytope_g1.json")
g2 = sum((load("cluster_polytope_g2p%d.json" % p) for p in (3, 5, 7)), [])
sat = {(r["p"], r["a1"], r.get("a2"), r["orient"]): r for r in load("satellite.json")}


def status(rec, key):
    o = rec[key]
    st = o["status"]
    if st == "undecided":
        s = sat.get((rec["p"], rec["a1"], rec.get("a2"), key))
        if s and s.get("realized"):
            return "realized", s["m"]
    if st == "realized":
        return "realized", o["m_real"]
    if st.startswith("certified") or st == "unrealizable-all-m":
        return "certified", None
    return "undecided", None


def tally(recs, label):
    out = {}
    for key in ("noflip",):
        c = {"realized": 0, "certified": 0, "undecided": 0}
        ms = []
        for r in recs:
            s, m = status(r, key)
            c[s] += 1
            if m is not None:
                ms.append(m)
        out[key] = c
        out["max_m_real_noflip"] = max(ms) if ms else None
    # class-or-twist (flip allowed)
    c = {"realized": 0, "certified": 0, "undecided": 0}
    for r in recs:
        s1, _ = status(r, "noflip")
        s2, _ = status(r, "flip") if "flip" in r else (s1, None)
        if "realized" in (s1, s2):
            c["realized"] += 1
        elif s1 == "certified" and s2 == "certified":
            c["certified"] += 1
        else:
            c["undecided"] += 1
    out["class_or_twist"] = c
    print(label, json.dumps(out))
    return out


print("== counts ==")
T1 = tally(g1, "g=1 (60 classes, p<=13):")
T2 = tally(g2, "g=2 (357 classes, p in {3,5,7}):")
for p in (3, 5, 7):
    tally([r for r in g2 if r["p"] == p], "  g=2 p=%d:" % p)

# certified-by-what breakdown at g=2 (noflip)
pos_only = face = 0
for r in g2:
    o = r["noflip"]
    if o["status"].startswith("certified"):
        if o["m_pos"] > 36:
            pos_only += 1
        else:
            face += 1
print("g=2 noflip certified: by coefficient sign alone for all m<=36 (m_pos>36): %d; "
      "by an exact cluster-polytope / face certificate for some m in [m_pos, 36]: %d"
      % (pos_only, face))
wmax = [r for r in g2 if r["noflip"]["status"].startswith("certified")]
print("g=2 noflip certified classes (p,a1,a2):", [(r["p"], r["a1"], r["a2"]) for r in wmax])
und = [(r["p"], r["a1"], r["a2"], k) for r in g2 for k in ("noflip", "flip")
       if status(r, k)[0] == "undecided"]
print("g=2 undecided (p,a1,a2,orientation):", und)

# g=1 threshold statement
ok = all((status(r, "noflip")[0] == "realized") == (r["a1"] > -math.sqrt(r["p"])) for r in g1)
print("g=1: noflip realized  <=>  a1 > -sqrt(p)  on all 60 classes:", ok)

# ---------------------------------------------------------------- zeros as input
print("== zeros-as-input realizations ==")
classes = json.load(open(os.path.join(HERE, "classes_g2.json")))
n_untw = 0
nzero = 0
worst = 0
Jmin, Jmax = 1e9, -1
for r in classes:
    q = r["p"]; c1 = mp.mpf(r["a1"]) / mp.sqrt(q); c2 = mp.mpf(r["a2"]) / q
    D = mp.mpf(r["a1"] ** 2 - 4 * r["a2"] + 8 * q) / q   # exact integer numerator, >= 0 by RH
    w = [(-c1 + mp.sqrt(D)) / 2, (-c1 - mp.sqrt(D)) / 2]     # w_j = 2 cos(theta_j)
    cos = [x / 2 for x in w]
    if all(cj < 0 for cj in cos):
        n_untw += 1
    # Z1: product over j of (1 - 2 cos_j z + z^2); J_j = -1/2 log|cos_j| (inf if cos_j = 0)
    poly = [mp.mpf(1)]
    for cj in cos:
        f = [1, -2 * cj, 1]
        new = [mp.mpf(0)] * (len(poly) + 2)
        for i, a in enumerate(poly):
            for k, b in enumerate(f):
                new[i + k] += a * b
        poly = new
        if abs(cj) < mp.mpf(10) ** -40:
            nzero += 1
        else:
            J = -mp.log(abs(cj)) / 2
            Jmin = min(Jmin, float(J)); Jmax = max(Jmax, float(J))
    target = [1, c1, c2, c1, 1]
    worst = max(worst, float(max(abs(a - b) for a, b in zip(poly, target))))
print("g=2 classes with BOTH cos(theta_j) < 0 (untwisted two-pair product realization at m=0,"
      " couplings J_j = -1/2 log(-cos theta_j)): %d of %d" % (n_untw, len(classes)))
print("Newman-1974 twisted product (Examples 2.1/2.3) reproduces P(z/sqrt q) for all %d classes;"
      " max coefficient error %.1e; J_j range [%.4f, %.4f] (all >= 0)"
      % (len(classes), worst, Jmin, Jmax))
print("factors with cos(theta_j) = 0 (a2 = 2q; Example 2.1 single spin / J = +inf pair):", nzero)
