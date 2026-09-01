"""audit_O_lean_vs_py.py -- AUDITOR O: DIFFERENTIAL TEST of the Lean kernel checker
`Zeta23.W1.checkW1` against the Python reference checker `checker_ref.run_checks`
(task item 7: "check that the Lean checker's check is the SAME predicate").

Method: generate N random W1Data (small integers, adversarially biased to the
boundary of every clause), emit them as Lean literals, kernel-evaluate `checkW1`
on each with `decide +kernel`, and compare to the Python verdict.

The ONLY intended difference is FORMAT.md's C10: the JSON checker ties the `mode`
field to m (refutation => m >= 1, exclusion => m = 0), while the Lean structure has
no mode field and instead requires 0 <= m (FORMAT.md sec.12.5).  The Python
verdict is therefore taken MODE-FREE: accept iff the transcript would be accepted
under SOME mode, i.e. C1-C9 (+C11) hold and m >= 0.  Under that reading the two
predicates must agree on every case.

Usage:
  python3 audit_O_lean_vs_py.py N SEED OUT.lean   # write cases + Python expectations,
  then: lake build Zeta23.W1.AuditOFuzz   (a Lean error names any disagreeing case)
"""
import json, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import checker_ref

HERE = os.path.dirname(os.path.abspath(__file__))


def py_accept(d):
    """Mode-free Python verdict (see the module docstring)."""
    for mode in ("refutation", "exclusion"):
        dd = dict(d, mode=mode)
        try:
            checker_ref.run_checks(dd)
            return True
        except checker_ref.Reject:
            continue
    return False


def _valid_case(rng):
    """A VALID W1Data (all of C1-C9, and C11 if a floor is present)."""
    q1 = rng.choice([3, 4, 5, 8, 10, 20])
    p1 = rng.randint(q1 // 2 + 1, q1 - 1)
    q2 = rng.choice([3, 4, 5, 8, 10, 20])
    p2 = rng.randint(q2 // 2 + 1, q2 - 1)
    if p1 * q2 > p2 * q1:                       # enforce sigma1 <= sigma2
        p1, q1, p2, q2 = p2, q2, p1, q1
        if 2 * p1 <= q1:                        # keep sigma1 > 1/2
            p1, q1 = 3, 5
            if p1 * q2 > p2 * q1:
                p2, q2 = 9, 10
    b1 = rng.choice([1, 2]); b2 = rng.choice([1, 2])
    T = rng.randint(-5, 40)
    a1, a2 = T * b1, (T + 1) * b2
    A = rng.choice([8, 20, 100, 1000, 10 ** 6])
    K = rng.choice([1, 2, 100, 10 ** 6])

    def chain(a, b, inc):
        """a, b as (n, d); build 1..3 interior breakpoints strictly between."""
        n = rng.randint(1, 3)
        pts = [a]
        for i in range(1, n):
            pts.append((a[0] * b[1] * (n - i) + b[0] * a[1] * i, a[1] * b[1] * n))
        pts.append(b)
        # drop duplicates / non-strict steps (happens when a == b)
        keep = [pts[0]]
        for q in pts[1:]:
            r = keep[-1]
            ok = (r[0] * q[1] < q[0] * r[1]) if inc else (q[0] * r[1] < r[0] * q[1])
            if ok:
                keep.append(q)
        if len(keep) < 2 or not (keep[-1][0] * b[1] == b[0] * keep[-1][1]):
            keep = [a, b]
        return keep

    bottom = chain((p1, q1), (p2, q2), True)
    right = chain((a1, b1), (a2, b2), True)
    top = chain((p2, q2), (p1, q1), False)
    left = chain((a2, b2), (a1, b1), False)
    if len(bottom) < 2 or len(top) < 2:
        bottom, top = [(p1, q1), (p2, q2)], [(p2, q2), (p1, q1)]
    M = sum(len(x) - 1 for x in (bottom, right, top, left))
    m = rng.choice([0, 0, 1, 1, 2])
    # argument rows: split A*m into M integer pieces, each within the clamp,
    # total width < A/2
    base = (A * m) // M
    rem = A * m - base * M
    los, his = [], []
    wtot = 0
    for i in range(M):
        v = base + (1 if i < rem else 0)
        v = max(-(A // 2), min(A // 2, v))
        w = rng.choice([0, 0, 1]) if wtot * 2 < A // 4 else 0
        lo, hi = v, v + w
        if 2 * hi > A:
            hi = A // 2
        if 2 * lo < -A:
            lo = -(A // 2)
        los.append(lo); his.append(hi); wtot += hi - lo
    # fix the containment: nudge the last row so S_lo <= A*m <= S_hi
    Slo, Shi = sum(los), sum(his)
    d = A * m - Slo
    if d > 0:
        los[-1] += d; his[-1] += d
    elif d < 0:
        los[-1] += d; his[-1] += d
    rows = []
    for i in range(M):
        sgn = rng.randrange(4)
        lo1, hi1 = rng.randint(1, 9), rng.randint(1, 9)
        lo1, hi1 = min(lo1, hi1), max(lo1, hi1)
        lo2, hi2 = sorted((rng.randint(-9, 9), rng.randint(-9, 9)))
        if sgn == 0:   box = (lo1, hi1, lo2, hi2)          # reLo > 0
        elif sgn == 1: box = (-hi1, -lo1, lo2, hi2)        # reHi < 0
        elif sgn == 2: box = (lo2, hi2, lo1, hi1)          # imLo > 0
        else:          box = (lo2, hi2, -hi1, -lo1)        # imHi < 0
        rows.append((box[0], box[1], box[2], box[3], los[i], his[i]))
    floor = None
    if rng.random() < 0.45:
        mins = []
        for (rl, rh, il, ih, _a, _b) in rows:
            mre = 0 if rl <= 0 <= rh else min(abs(rl), abs(rh))
            mim = 0 if il <= 0 <= ih else min(abs(il), abs(ih))
            mins.append(mre * mre + mim * mim)
        import math as _m
        Fn = _m.isqrt(min(mins)) if mins else 0
        floor = (max(0, Fn - rng.choice([0, 0, 1])), K)
    return {"mode": "exclusion", "function": "zeta", "m": m, "K": K, "A": A,
            "rect": {"sigma1": (p1, q1), "sigma2": (p2, q2), "T1": (a1, b1), "T2": (a2, b2)},
            "mesh": {"bottom": bottom, "right": right, "top": top, "left": left},
            "rows": rows, "floor": floor}


def _perturb(rng, d):
    """One targeted single-clause perturbation of a valid case."""
    import copy as _c
    d = _c.deepcopy(d)
    what = rng.randrange(14)
    R = d["rows"]
    if what == 0 and R:                       # C6: a box containing 0
        i = rng.randrange(len(R)); r = list(R[i])
        r[0], r[1], r[2], r[3] = -3, 4, -2, 5
        R[i] = tuple(r)
    elif what == 1 and R:                     # C5: empty box
        i = rng.randrange(len(R)); r = list(R[i]); r[0], r[1] = r[1] + 1, r[1]
        R[i] = tuple(r)
    elif what == 2 and R:                     # C7: clamp violation
        i = rng.randrange(len(R)); r = list(R[i]); r[5] = d["A"] // 2 + 1
        R[i] = tuple(r)
    elif what == 3 and R:                     # C8: widen
        i = rng.randrange(len(R)); r = list(R[i]); r[5] = r[4] + d["A"] // 2
        R[i] = tuple(r)
    elif what == 4:                           # C9: shift m
        d["m"] += rng.choice([-1, 1])
    elif what == 5:                           # C10 (Lean): negative m
        d["m"] = -rng.randint(1, 3)
    elif what == 6:                           # C2: sigma1 on/below the line
        d["rect"]["sigma1"] = (1, 2)
        d["mesh"]["bottom"][0] = (1, 2); d["mesh"]["top"][-1] = (1, 2)
    elif what == 7:                           # C2: sigma2 >= 1
        d["rect"]["sigma2"] = (1, 1)
        d["mesh"]["bottom"][-1] = (1, 1); d["mesh"]["top"][0] = (1, 1)
    elif what == 8:                           # C3: break monotonicity
        e = rng.choice(["bottom", "right", "top", "left"])
        L = d["mesh"][e]
        if len(L) > 2:
            i = rng.randrange(len(L) - 1); L[i], L[i + 1] = L[i + 1], L[i]
        else:
            L.reverse()
    elif what == 9:                           # C4: drop a row
        if R: R.pop()
    elif what == 10:                          # C4: add a mesh point
        d["mesh"]["right"].insert(1, d["mesh"]["right"][0])
    elif what == 11:                          # C1: bad denominator
        e = rng.choice(["bottom", "right", "top", "left"])
        i = rng.randrange(len(d["mesh"][e]))
        d["mesh"][e][i] = (d["mesh"][e][i][0], rng.choice([0, -1]))
    elif what == 12:                          # C1: K or A < 1
        if rng.random() < 0.5: d["K"] = rng.choice([0, -5])
        else: d["A"] = rng.choice([0, -3])
    elif what == 13 and d["floor"] is not None:   # C11: inflate the floor
        d["floor"] = (d["floor"][0] + rng.randint(1, 3), d["floor"][1])
    return d


def rnd_case(rng):
    d = _valid_case(rng)
    if rng.random() < 0.55:
        d = _perturb(rng, d)
    return d


def lean_int(n):
    return "(%d)" % n if n < 0 else "%d" % n


def emit(name, d):
    r = d["rect"]
    rows = ", ".join("⟨%s, %s, %s, %s, %s, %s⟩" % tuple(lean_int(x) for x in row) for row in d["rows"])
    def lst(l):
        return "[" + ", ".join("(%s, %s)" % (lean_int(a), lean_int(b)) for a, b in l) + "]"
    s = ["def %s : W1Data where" % name,
         "  p1 := %s;  q1 := %s" % (lean_int(r["sigma1"][0]), lean_int(r["sigma1"][1])),
         "  p2 := %s;  q2 := %s" % (lean_int(r["sigma2"][0]), lean_int(r["sigma2"][1])),
         "  a1 := %s;  b1 := %s" % (lean_int(r["T1"][0]), lean_int(r["T1"][1])),
         "  a2 := %s;  b2 := %s" % (lean_int(r["T2"][0]), lean_int(r["T2"][1])),
         "  K := %s" % lean_int(d["K"]),
         "  A := %s" % lean_int(d["A"]),
         "  m := %s" % lean_int(d["m"]),
         "  bottom := %s" % lst(d["mesh"]["bottom"]),
         "  right  := %s" % lst(d["mesh"]["right"]),
         "  top    := %s" % lst(d["mesh"]["top"]),
         "  left   := %s" % lst(d["mesh"]["left"]),
         "  rows := [%s]" % rows]
    if d["floor"] is not None:
        s += ["", "def %s_fl : W1Floor where" % name,
              "  Fn := %s" % lean_int(d["floor"][0]),
              "  Fd := %s" % lean_int(d["floor"][1])]
    return "\n".join(s)


def main(argv):
    if argv[1] == "gen":
        argv = [argv[0]] + argv[2:]
    n = int(argv[1]); seed = int(argv[2]); out = argv[3]
    rng = random.Random(seed)
    blocks = ["""/- auditor-O differential-test cases (Session 14): random W1Data, kernel-checked. -/
import Zeta23.W1.Checker
namespace Zeta23
namespace W1
set_option maxRecDepth 100000
"""]
    thms, expects = [], []
    for i in range(n):
        d = rnd_case(rng)
        name = "fz%03d" % i
        blocks.append(emit(name, d))
        # checkW1 in Lean is C1-C10 ONLY (C11 lives in checkW1Floor), so the
        # Python comparand for `%s_c` must be run with the floor removed.
        pv = py_accept(dict(d, floor=None))
        thms.append("theorem %s_c : checkW1 %s = %s := by decide +kernel" % (name, name, str(pv).lower()))
        rec = {"name": name, "py": pv}
        if d["floor"] is not None:
            pf = pv and d["floor"][0] >= 0 and d["floor"][1] >= 1 and all(
                (0 if lo <= 0 <= hi else min(abs(lo), abs(hi))) ** 2 * 1 * 0 == 0 for lo, hi in [])
            # recompute C11 exactly (mode-free)
            Fn, Fd = d["floor"]
            ok = pv and Fn >= 0 and Fd >= 1
            if ok:
                for (rl, rh, il, ih, _a, _b) in d["rows"]:
                    mre = 0 if rl <= 0 <= rh else min(abs(rl), abs(rh))
                    mim = 0 if il <= 0 <= ih else min(abs(il), abs(ih))
                    if not (mre * mre + mim * mim) * Fd * Fd >= Fn * Fn * d["K"] * d["K"]:
                        ok = False
                        break
            thms.append("theorem %s_f : checkW1Floor %s %s_fl = %s := by decide +kernel"
                        % (name, name, name, str(ok).lower()))
            rec["pyfloor"] = ok
        expects.append(rec)
    blocks.append("\n".join(thms))
    blocks.append("end W1\nend Zeta23")
    with open(out, "w") as fh:
        fh.write("\n\n".join(blocks) + "\n")
    with open(os.path.join(HERE, "audit_O_lean_vs_py.expect.json"), "w") as fh:
        json.dump(expects, fh, indent=1)
    acc = sum(1 for e in expects if e["py"])
    print("wrote %s : %d cases (%d python-ACCEPT, %d python-REJECT)"
          % (out, n, acc, n - acc))
    print("Lean must AGREE on every one; a build failure names the disagreeing case.")


if __name__ == "__main__":
    main(sys.argv)
