#!/usr/bin/env python3
"""UNTRUSTED reference checker for the M2a barrier-certificate contract (results/d1-m2a/SPEC.md).

Implements, on the JSON documents of barrier-schema.json, exactly the integer checks of SPEC.md
section 7.3 (barrier lane: C-B0 ... C-B12 per prism, C-B13 chain) and section 7.4 (asymptotic
lane: C-A1 ... C-A6).  Every comparison is on Python ints (arbitrary precision); rationals are
compared by cross-multiplication; no float is ever formed.  It is a producer-side pre-validation
tool and the executable spec of the Lean checker `checkBarrier` / `checkAsym` -- NOT the trusted
checker (the trusted one is the Lean kernel on the emitted literals).

usage:  barrier_ref_checker.py <manifest.json>        (barrier lane; prism files resolved next to it)
        barrier_ref_checker.py <asymptotic.json>      (asymptotic lane)
exit 0 = ACCEPT, 1 = REJECT (first failing check named), 2 = shape error.
"""
import json, os, re, sys

INT = re.compile(r"^-?(0|[1-9][0-9]*)$")
POS = re.compile(r"^[1-9][0-9]*$")
NAT = re.compile(r"^(0|[1-9][0-9]*)$")

class Reject(Exception): pass
class Shape(Exception): pass

def I(s, pat=INT, what="integer"):
    if not isinstance(s, str) or not pat.match(s):
        raise Shape(f"{what} string expected, got {s!r}")
    return int(s)

def rat(o, what="rational"):
    if not isinstance(o, dict) or set(o) != {"n", "d"}:
        raise Shape(f"{what}: object {{n,d}} expected")
    return (I(o["n"]), I(o["d"], POS, "positive integer"))

def ratlist(l, what):
    if not isinstance(l, list) or len(l) < 2:
        raise Shape(f"{what}: list of >= 2 rationals expected")
    return [rat(r, what) for r in l]

def req(c, name):
    if not c: raise Reject(name)

# ---- rational comparisons by cross-multiplication (denominators checked >= 1 by C-B0 first)
def lt(r, s): return r[0]*s[1] < s[0]*r[1]
def le(r, s): return r[0]*s[1] <= s[0]*r[1]
def eq(r, s): return r[0]*s[1] == s[0]*r[1]

def edge_ok(start, stop, inc, l, name):
    req(len(l) >= 2, f"{name}: C-B3 fewer than two breakpoints")
    req(eq(l[0], start), f"{name}: C-B3 first breakpoint != edge start")
    req(eq(l[-1], stop), f"{name}: C-B3 last breakpoint != edge stop")
    for a, b in zip(l, l[1:]):
        req(lt(a, b) if inc else lt(b, a), f"{name}: C-B3 not strictly monotone")

def check_prism(rect, p, name):
    x1, x2, y1, y2 = rect
    K = I(p["scales"]["K"], POS); A = I(p["scales"]["A"], POS)
    mesh = {e: ratlist(p["mesh"][e], f"{name}.mesh.{e}") for e in ("bottom", "right", "top", "left")}
    rows = p["segments"]
    if not isinstance(rows, list): raise Shape("segments: list expected")
    rows = [{k: I(r[k]) for k in ("reLo", "reHi", "imLo", "imHi", "argLo", "argHi")} for r in rows]
    Fn = I(p["modulus_floor"]["Fn"], NAT); Fd = I(p["modulus_floor"]["Fd"], POS)
    E = I(p["approx_defect"], NAT); D = I(p["displacement"], NAT)
    tn, td = rat(p["seam"], "seam")
    # C-B0 denominators / scales (positivity is syntactic in the schema; re-verified here)
    req(K >= 1 and A >= 1 and td >= 1 and Fd >= 1, f"{name}: C-B0 scale/denominator")
    req(tn >= 0, f"{name}: C-B0 seam >= 0")
    for e in mesh:
        for r in mesh[e]: req(r[1] >= 1, f"{name}: C-B0 mesh denominator")
    # C-B3 mesh walks on the common rectangle (bottom/right increasing, top/left decreasing)
    edge_ok(x1, x2, True, mesh["bottom"], name)
    edge_ok(y1, y2, True, mesh["right"], name)
    edge_ok(x2, x1, False, mesh["top"], name)
    edge_ok(y2, y1, False, mesh["left"], name)
    # C-B4 row count
    M = sum(len(mesh[e]) - 1 for e in mesh)
    req(len(rows) == M, f"{name}: C-B4 |segments| = {len(rows)} != M = {M}")
    # C-B5, C-B6, C-B7 per row
    Slo = Shi = 0
    for k, r in enumerate(rows):
        req(r["reLo"] <= r["reHi"] and r["imLo"] <= r["imHi"], f"{name}: C-B5 empty box, row {k}")
        req(r["reLo"] > 0 or r["reHi"] < 0 or r["imLo"] > 0 or r["imHi"] < 0, f"{name}: C-B6 box contains 0, row {k}")
        req(r["argLo"] <= r["argHi"] and -A <= 2*r["argLo"] and 2*r["argHi"] <= A, f"{name}: C-B7 argument row, row {k}")
        Slo += r["argLo"]; Shi += r["argHi"]
    # C-B8 width, C-B9 containment of m = 0
    req(2*(Shi - Slo) < A, f"{name}: C-B8 winding width 2*({Shi}-{Slo}) >= A={A}")
    req(Slo <= 0 <= Shi, f"{name}: C-B9 0 not in [{Slo},{Shi}]")
    # C-B11 floor
    def mdist(lo, hi): return 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
    for k, r in enumerate(rows):
        req((mdist(r["reLo"], r["reHi"])**2 + mdist(r["imLo"], r["imHi"])**2) * Fd*Fd >= Fn*Fn*K*K,
            f"{name}: C-B11 floor fails, row {k}")
    # C-B12 prism gate: (E + D)/K < Fn/Fd
    req((E + D)*Fd < Fn*K, f"{name}: C-B12 (E+D)*Fd={ (E+D)*Fd } >= Fn*K={Fn*K}")
    return (tn, td), M, Slo, Shi, K, A

def check_barrier(manifest, base):
    if manifest.get("kind") != "manifest": raise Shape("kind != manifest")
    rect = tuple(rat(manifest["rect"][k], k) for k in ("x1", "x2", "y1", "y2"))
    t0 = rat(manifest["t0"], "t0")
    for r in rect + (t0,): req(r[1] >= 1, "C-B0 rectangle/t0 denominator")
    x1, x2, y1, y2 = rect
    # C-B2' rectangle nondegenerate, y1 > 0, t0 > 0
    req(lt(x1, x2), "C-B2' x1 < x2"); req(lt(y1, y2), "C-B2' y1 < y2")
    req(y1[0] > 0, "C-B2' y1 > 0"); req(t0[0] > 0, "C-B2' t0 > 0")
    seams = []
    report = []
    for entry in manifest["prisms"]:
        with open(os.path.join(base, entry["file"])) as fh: p = json.load(fh)
        if p.get("kind") != "prism": raise Shape(f"{entry['file']}: kind != prism")
        req(eq(rat(p["seam"]), rat(entry["seam"])), f"{entry['file']}: manifest/prism seam mismatch")
        seam, M, Slo, Shi, K, A = check_prism(rect, p, entry["file"])
        seams.append(seam); report.append((entry["file"], M, Slo, Shi, K, A))
    # C-B13 chain: first seam = 0, strictly increasing, last seam < t0
    req(len(seams) >= 1, "C-B13 no prisms")
    req(seams[0][0] == 0, "C-B13 first seam != 0")
    for a, b in zip(seams, seams[1:]): req(lt(a, b), "C-B13 seams not strictly increasing")
    req(lt(seams[-1], t0), "C-B13 last seam not < t0")
    return report

def check_asym(a):
    if a.get("kind") != "asymptotic": raise Shape("kind != asymptotic")
    K = I(a["scales"]["K"], POS)
    t0 = rat(a["t0"]); y0 = rat(a["y0"]); yA = rat(a["yA"])
    req(t0[0] > 0 and y0[0] > 0 and yA[0] >= 0, "C-A1 t0 > 0, y0 > 0, yA >= 0")
    # C-A1: yA^2 >= 1 - 2 t0  <=>  (t0d - 2 t0n) * yAd^2 <= yAn^2 * t0d
    req((t0[1] - 2*t0[0]) * yA[1]**2 <= yA[0]**2 * t0[1], "C-A1 yA^2 >= 1 - 2*t0 fails")
    rows = [{k: I(r[k]) for k in ("Nlo", "Nhi", "T", "E")} for r in a["rows"]]
    req(len(rows) >= 1, "C-A2 no rows")
    for k, r in enumerate(rows):
        req(r["Nlo"] <= r["Nhi"], f"C-A3 window empty, row {k}")
        req(0 <= r["E"] < r["T"], f"C-A3 E < T fails, row {k} (T={r['T']}, E={r['E']})")
    for k, (r, s) in enumerate(zip(rows, rows[1:])):
        req(s["Nlo"] == r["Nhi"] + 1, f"C-A4 rows not consecutive at row {k+1}")
    t = {k: I(a["tail"][k], NAT) for k in ("N1", "Q1", "Q2", "Q3", "Q4", "E1")}
    req(t["N1"] == rows[-1]["Nhi"] + 1, "C-A5 tail N1 != last Nhi + 1")
    S = t["Q1"] + t["Q2"] + t["Q3"] + t["Q4"] + t["E1"]
    req(S < 2*K, f"C-A6 tail sum {S} >= 2K = {2*K}")
    return rows, t, S, K

def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    path = sys.argv[1]
    with open(path) as fh: doc = json.load(fh)
    try:
        if doc.get("format") != "M2a-barrier-transcript" or doc.get("version") != "1.0":
            raise Shape("format/version")
        if doc.get("kind") == "manifest":
            rep = check_barrier(doc, os.path.dirname(os.path.abspath(path)))
            for f, M, Slo, Shi, K, A in rep:
                print(f"  prism {f}: M={M} S_lo={Slo} S_hi={Shi} K={K} A={A}")
            print(f"ACCEPT (barrier lane, {len(rep)} prisms): checks C-B0..C-B13 pass -- integer facts only; "
                  f"the certified statement holds modulo the displayed hypotheses H2-B and the holomorphy input (SPEC.md section 6)")
        elif doc.get("kind") == "asymptotic":
            rows, t, S, K = check_asym(doc)
            print(f"  rows={len(rows)} first Nlo={rows[0]['Nlo']} last Nhi={rows[-1]['Nhi']} tail N1={t['N1']} tail sum={S} 2K={2*K}")
            print("ACCEPT (asymptotic lane): checks C-A1..C-A6 pass -- integer facts only; modulo H2-A and H-TAIL (SPEC.md section 6)")
        else:
            raise Shape("kind must be manifest or asymptotic")
    except Reject as e:
        print(f"REJECT at {e}"); sys.exit(1)
    except (Shape, KeyError, TypeError) as e:
        print(f"SHAPE ERROR: {e}"); sys.exit(2)

if __name__ == "__main__":
    main()
