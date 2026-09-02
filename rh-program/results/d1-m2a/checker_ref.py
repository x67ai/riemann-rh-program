#!/usr/bin/env python3
"""checker_ref.py -- UNTRUSTED reference checker for the M2a barrier lane (SPEC.md v1.0 section 7.3), written for
M2a item (e) as an INDEPENDENT second implementation: exact `fractions.Fraction` arithmetic, mirroring the Lean
predicate `Zeta23.DBN.checkBarrier` (Zeta23/DBN/BarrierCert.lean, 2026-09-02) CLAUSE BY CLAUSE and in the same
order, so that a disagreement between this program and the kernel would localize to one clause.  It shares no
code with either producer (producer_mp.py / ft_mp.py, producer_arb.py) nor with barrier_ref_checker.py (the
contract agent's cross-multiplication implementation); the only common object is SPEC.md.

Mirror map (Lean name -> function here):
  W1.densPos / chainLt / chainGt / firstOK / lastOK / edgeOK   -> dens_pos, chain_lt, chain_gt, first_ok, last_ok, edge_ok
  W1.rowOK / rowsOK / sumArgLo / sumArgHi                        -> row_ok, rows_ok, sum_arg_lo, sum_arg_hi
  W1.mdist / floorRowOK / floorRowsOK                            -> mdist, floor_row_ok, floor_rows_ok
  DBN.checkPrismW1 (toW1 r p)                                    -> check_prism_w1(rect, prism)
  DBN.checkPrism r p                                             -> check_prism(rect, prism)
  DBN.checkBarrierChain d                                        -> check_barrier_chain(barrier)
  DBN.checkBarrier d                                             -> check_barrier(barrier)
Rationals n/d are compared as Fractions (a Fraction equality/order is the cross-multiplied one when d >= 1; the
Lean checker verifies d >= 1 first, C-B0, and so does this program before forming any Fraction).

Trust: this is a producer-side pre-validation and cross-validation tool.  The TRUSTED checker is the Lean kernel on
the emitted literals (`decide +kernel`, Zeta23/DBN/Instance02*.lean).  Acceptance here means exactly that the
integer/rational relations C-B0..C-B13 hold -- nothing analytic (H2-B, hHol stay displayed).

usage: checker_ref.py <manifest.json> [--quiet]        exit 0 ACCEPT, 1 REJECT (first failing clause named), 2 shape
       checker_ref.py --prism <prism.json> --rect x1n/x1d x2n/x2d y1n/y1d y2n/y2d     (one prism, checkPrism only)
"""
import json, os, re, sys
from fractions import Fraction

INT = re.compile(r"^-?(0|[1-9][0-9]*)$")

class Shape(Exception): pass

def as_int(s, what="integer"):
    if not isinstance(s, str) or not INT.match(s):
        raise Shape(f"{what}: decimal integer string expected, got {s!r}")
    return int(s)

def as_pair(o, what="rational"):
    if not isinstance(o, dict) or set(o.keys()) != {"n", "d"}:
        raise Shape(f"{what}: {{n,d}} object expected")
    return (as_int(o["n"], what + ".n"), as_int(o["d"], what + ".d"))

def fr(pair):
    # only called after the denominator has been checked >= 1 (C-B0); Fraction order = cross-multiplied order
    return Fraction(pair[0], pair[1])

# ---- W1 helpers (Zeta23/W1/Checker.lean), on lists of (n, d) pairs -------------------------------------------
def dens_pos(l):                       # every denominator >= 1
    return all(r[1] >= 1 for r in l)

def chain_lt(l):                       # adjacent strict increase
    return all(fr(a) < fr(b) for a, b in zip(l, l[1:]))

def chain_gt(l):                       # adjacent strict decrease
    return all(fr(b) < fr(a) for a, b in zip(l, l[1:]))

def first_ok(t, l):
    return len(l) >= 1 and fr(l[0]) == fr(t)

def last_ok(t, l):
    return len(l) >= 1 and fr(l[-1]) == fr(t)

def edge_ok(start, stop, inc, l):
    return len(l) >= 2 and first_ok(start, l) and last_ok(stop, l) and (chain_lt(l) if inc else chain_gt(l))

def row_ok(A, r):
    reLo, reHi, imLo, imHi, argLo, argHi = r
    c5 = reLo <= reHi and imLo <= imHi
    c6 = (0 < reLo) or (reHi < 0) or (0 < imLo) or (imHi < 0)
    c7 = argLo <= argHi and -A <= 2 * argLo and 2 * argHi <= A
    return c5 and c6 and c7

def rows_ok(A, rows):
    return all(row_ok(A, r) for r in rows)

def sum_arg_lo(rows): return sum(r[4] for r in rows)
def sum_arg_hi(rows): return sum(r[5] for r in rows)

def mdist(lo, hi):
    return 0 if (lo <= 0 and 0 <= hi) else min(abs(lo), abs(hi))

def floor_row_ok(K, Fn, Fd, r):
    return Fn ** 2 * K ** 2 <= (mdist(r[0], r[1]) ** 2 + mdist(r[2], r[3]) ** 2) * Fd ** 2

def floor_rows_ok(K, Fn, Fd, rows):
    return all(floor_row_ok(K, Fn, Fd, r) for r in rows)

# ---- DBN.checkPrismW1 (toW1 r p) --------------------------------------------------------------------------------
def check_prism_w1(rect, p, fail):
    (xn1, xd1), (xn2, xd2), (yn1, yd1), (yn2, yd2) = rect
    K, A = p["K"], p["A"]
    m = p["mesh"]; rows = p["rows"]
    if not (1 <= K): return fail("C-B0 K >= 1")
    if not (1 <= A): return fail("C-B0 A >= 1")
    for v, nm in ((xd1, "xd1"), (xd2, "xd2"), (yd1, "yd1"), (yd2, "yd2")):
        if not (1 <= v): return fail(f"C-B0 rectangle denominator {nm} >= 1")
    for e in ("bottom", "right", "top", "left"):
        if not dens_pos(m[e]): return fail(f"C-B0 mesh denominator ({e})")
    if not (fr((xn1, xd1)) < fr((xn2, xd2))): return fail("C-B2' x1 < x2")
    if not (fr((yn1, yd1)) < fr((yn2, yd2))): return fail("C-B2' y1 < y2")
    if not edge_ok((xn1, xd1), (xn2, xd2), True, m["bottom"]): return fail("C-B3 bottom edge walk")
    if not edge_ok((yn1, yd1), (yn2, yd2), True, m["right"]): return fail("C-B3 right edge walk")
    if not edge_ok((xn2, xd2), (xn1, xd1), False, m["top"]): return fail("C-B3 top edge walk")
    if not edge_ok((yn2, yd2), (yn1, yd1), False, m["left"]): return fail("C-B3 left edge walk")
    if not (len(rows) + 4 == len(m["bottom"]) + len(m["right"]) + len(m["top"]) + len(m["left"])):
        return fail(f"C-B4 row count {len(rows)} + 4 != {len(m['bottom']) + len(m['right']) + len(m['top']) + len(m['left'])}")
    for k, r in enumerate(rows):
        if not row_ok(A, r):
            which = "C-B5" if not (r[0] <= r[1] and r[2] <= r[3]) else ("C-B6" if not ((0 < r[0]) or (r[1] < 0) or (0 < r[2]) or (r[3] < 0)) else "C-B7")
            return fail(f"{which} row {k} = {r}")
    Slo, Shi = sum_arg_lo(rows), sum_arg_hi(rows)
    if not (2 * (Shi - Slo) < A): return fail(f"C-B8 2*({Shi} - {Slo}) >= A = {A}")
    if not (Slo <= 0): return fail(f"C-B9 S_lo = {Slo} > 0")
    if not (0 <= Shi): return fail(f"C-B9 S_hi = {Shi} < 0")
    # m = 0 is built in (toW1 sets m := 0; `decide (w.m = 0)` is trivially true)
    return True

# ---- DBN.checkPrism r p ------------------------------------------------------------------------------------------
def check_prism(rect, p, fail=None):
    msgs = []
    def f(msg):
        msgs.append(msg); return False
    fail = fail or f
    ok = check_prism_w1(rect, p, fail)
    if not ok: return False, msgs
    if not (1 <= p["td"]): return False, [fail("C-B0 seam denominator >= 1")] and msgs
    if not (0 <= p["tn"]): fail("C-B0 seam numerator >= 0"); return False, msgs
    if not (0 <= p["Fn"]): fail("C-B0 Fn >= 0"); return False, msgs
    if not (1 <= p["Fd"]): fail("C-B0 Fd >= 1"); return False, msgs
    for k, r in enumerate(p["rows"]):
        if not floor_row_ok(p["K"], p["Fn"], p["Fd"], r):
            fail(f"C-B11 floor row {k}: (mre^2+mim^2)*Fd^2 < Fn^2*K^2"); return False, msgs
    if not (0 <= p["E"]): fail("C-B0 E >= 0"); return False, msgs
    if not (0 <= p["D"]): fail("C-B0 D >= 0"); return False, msgs
    if not ((p["E"] + p["D"]) * p["Fd"] < p["Fn"] * p["K"]):
        fail(f"C-B12 (E + D)*Fd = {(p['E'] + p['D']) * p['Fd']} >= Fn*K = {p['Fn'] * p['K']}"); return False, msgs
    return True, msgs

# ---- DBN.checkBarrierChain d --------------------------------------------------------------------------------------
def check_barrier_chain(b):
    (xn1, xd1), (xn2, xd2), (yn1, yd1), (yn2, yd2) = b["rect"]
    t0n, t0d = b["t0"]
    seams = [(p["tn"], p["td"]) for p in b["prisms"]]
    if not (1 <= xd1 and 1 <= xd2 and 1 <= yd1 and 1 <= yd2): return "C-B0 rectangle denominators"
    if not (1 <= t0d): return "C-B0 t0 denominator"
    if not (0 < yn1): return "C-B2' y1 > 0"
    if not (0 < t0n): return "C-B2' t0 > 0"
    if not (fr((xn1, xd1)) < fr((xn2, xd2))): return "C-B2' x1 < x2"
    if not (fr((yn1, yd1)) < fr((yn2, yd2))): return "C-B2' y1 < y2"
    if not dens_pos(seams): return "C-B0 seam denominators (chain)"
    if not first_ok((0, 1), seams): return "C-B13 first seam != 0 (or no prisms)"
    if not chain_lt(seams + [(t0n, t0d)]): return "C-B13 seams not strictly increasing / last seam not < t0"
    return None

def check_barrier(b):
    """mirror of `checkBarrierChain d && d.prisms.all (checkPrism d.rect)`; returns (ok, message)."""
    msg = check_barrier_chain(b)
    if msg: return False, msg
    for j, p in enumerate(b["prisms"]):
        ok, msgs = check_prism(b["rect"], p)
        if not ok: return False, f"prism {j} ({p.get('_file', '?')}): " + (msgs[0] if msgs else "checkPrism false")
    return True, "ACCEPT"

# ---- JSON (barrier-schema.json) -> the Lean literal shape -------------------------------------------------------
def load_prism(path):
    p = json.load(open(path))
    if p.get("format") != "M2a-barrier-transcript" or p.get("version") != "1.0" or p.get("kind") != "prism":
        raise Shape(f"{path}: format/version/kind")
    seam = as_pair(p["seam"], "seam")
    if not isinstance(p["segments"], list): raise Shape("segments")
    rows = []
    for r in p["segments"]:
        if set(r.keys()) != {"reLo", "reHi", "imLo", "imHi", "argLo", "argHi"}: raise Shape("row keys")
        rows.append(tuple(as_int(r[k], k) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")))
    mesh = {}
    for e in ("bottom", "right", "top", "left"):
        l = p["mesh"][e]
        if not isinstance(l, list): raise Shape(f"mesh.{e}")
        mesh[e] = [as_pair(r, f"mesh.{e}") for r in l]
    return {"tn": seam[0], "td": seam[1], "K": as_int(p["scales"]["K"], "K"), "A": as_int(p["scales"]["A"], "A"),
            "mesh": mesh, "rows": rows, "Fn": as_int(p["modulus_floor"]["Fn"], "Fn"), "Fd": as_int(p["modulus_floor"]["Fd"], "Fd"),
            "E": as_int(p["approx_defect"], "E"), "D": as_int(p["displacement"], "D"), "_file": os.path.basename(path),
            "_index": p.get("index")}

def load_barrier(manifest_path):
    m = json.load(open(manifest_path))
    if m.get("format") != "M2a-barrier-transcript" or m.get("version") != "1.0" or m.get("kind") != "manifest":
        raise Shape("manifest format/version/kind")
    rect = tuple(as_pair(m["rect"][k], k) for k in ("x1", "x2", "y1", "y2"))
    t0 = as_pair(m["t0"], "t0")
    base = os.path.dirname(os.path.abspath(manifest_path))
    prisms = []
    for e in m["prisms"]:
        p = load_prism(os.path.join(base, e["file"]))
        ms = as_pair(e["seam"], "manifest seam")
        # manifest/prism consistency (a JSON-level check; the Lean data has one copy of the seam)
        if not (ms[1] >= 1 and p["td"] >= 1 and fr(ms) == fr((p["tn"], p["td"]))):
            raise Shape(f"{e['file']}: manifest seam {ms} != prism seam {(p['tn'], p['td'])}")
        prisms.append(p)
    return {"rect": rect, "t0": t0, "prisms": prisms}

def main(argv):
    quiet = "--quiet" in argv; argv = [a for a in argv if a != "--quiet"]
    try:
        if argv and argv[0] == "--prism":
            p = load_prism(argv[1]); assert argv[2] == "--rect"
            rect = tuple((int(s.split("/")[0]), int(s.split("/")[1])) for s in argv[3:7])
            ok, msgs = check_prism(rect, p)
            print(("ACCEPT checkPrism" if ok else "REJECT at " + msgs[0]) + f"  [{argv[1]}: {len(p['rows'])} rows, K={p['K']}, A={p['A']}]")
            return 0 if ok else 1
        b = load_barrier(argv[0])
        ok, msg = check_barrier(b)
        if not quiet:
            for j, p in enumerate(b["prisms"]):
                print(f"  prism {j:4d} {p['_file']}: seam {p['tn']}/{p['td']} rows {len(p['rows'])} K={p['K']} A={p['A']} "
                      f"S=[{sum_arg_lo(p['rows'])},{sum_arg_hi(p['rows'])}] Fn/Fd={Fraction(p['Fn'], p['Fd'])!s:.24} E={p['E']} D={p['D']}")
        nrows = sum(len(p["rows"]) for p in b["prisms"])
        if ok:
            print(f"ACCEPT checkBarrier ({len(b['prisms'])} prisms, {nrows} rows): C-B0..C-B13 hold -- integer/rational facts only; "
                  "the certified statement holds modulo H2-B and hHol (SPEC.md section 6)")
            return 0
        print(f"REJECT at {msg}")
        return 1
    except (Shape, KeyError, TypeError, AssertionError, IndexError) as e:
        print(f"SHAPE ERROR: {e!r}"); return 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
