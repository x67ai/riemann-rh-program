# census.py -- A-track P1/P2 driver: for pencil k on the window [xa, xb] x [0, Y]: (a) real counts and non-real zeros of
# Xi_k and Xi_{k+1} with argument-principle checks, (b) every branch from a non-real zero of Xi_k, (c) completeness,
# (d) the real-axis test; hygiene (half-step re-trace of one branch in ten; routes L and T at sample points for k <= 6).
import sys, os, json, math, time
from a_core import *
from axis import scan, Sx
from tracer import trace, newton_S
from zeros import count_sym, count_rect, newton_XiN, march, dedup

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
APPENDIX = [(20.62534600592171760132974, 2.697151842339519632505712), (26.05616693357829946749575, 7.125359707612690330897455),
 (31.50143137824977099308422, 10.72915037105496782822450), (36.72702276874255239918647, 13.75961410603683555833019),
 (41.73703479849622101486046, 16.44012737324329251859479), (46.56622866997881255099908, 18.88186965378958902053812),
 (51.24456582311629453468990, 21.14750420601374895347492), (55.79525368022472028456165, 23.27625685820891335493023),
 (60.23621426525993802296865, 25.29458549895993860216014), (64.58150497097301796850798, 27.22133555778112035831075),
 (68.84235653395121330563843, 29.07049609150585601287785), (73.02789933182939276748060, 30.85279227139366634464017),
 (77.14567324003250763696303, 32.57666324204392832752644), (81.20199121212953110713480, 34.24889253114939152723783),
 (85.20220345212231662722890, 35.87503096670553315342957), (89.15089297349449318064800, 37.45968995259880236581690),
 (93.05202292717284600209187, 39.00675061925213970478000), (96.90904939663401491219210, 40.51951660155401879741380)]

def Xk(k):
    return 2 * math.pi * (k + 2) ** 2 + 30

def log(msg, fh=None):
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)

def zlist(js):
    return [complex(a, b) for a, b in js]

def jl(zs):
    return [[z.real, z.imag] for z in zs]

def subsample(path, nmax=120):
    if len(path) <= nmax:
        return path
    st = len(path) / float(nmax)
    out = [path[int(i * st)] for i in range(nmax)]
    out.append(path[-1])
    return out

def load_seeds(N):
    """non-real zeros of Xi_N known so far (file written by the run for pencil N-1), else Haglund's appendix for N = 1."""
    if N == 1:
        return [complex(a, b) for a, b in APPENDIX]
    p = os.path.join(DATA, "zeros_Xi%d.json" % N)
    if os.path.exists(p):
        return zlist(json.load(open(p))["zeros"])
    return []

def locate(N, xa, xb, route="T"):
    """non-real zeros of Xi_N with real part in [xa, xb] (upper half plane): refine seeds by Newton, march to xb."""
    seeds = load_seeds(N)
    zs = []
    for z in seeds:
        if xa - 20 <= z.real <= xb + 20:
            w, ok = newton_XiN(N, z, route, maxmove=0.5)
            if ok and w.imag > 1e-9:
                zs.append(w)
    zs = dedup(zs)
    zs = march(N, zs, xb + 5, route)
    return zs

def count_win(N, xa, xb, Y, ds=0.25, route="T"):
    """zeros of Xi_N in [xa,xb] x [-Y,Y]: (arg change along (xb,0)->(xb,Y)->(xa,Y)->(xa,0))/pi (floating point)."""
    from zeros import argpath
    t0 = time.time()
    tot, ns, nf = 0.0, 0, 0
    # with xa = 0 the left edge is the imaginary axis, where Xi_N > 0 (NOTE C3): its arg change is 0 and it is not
    # sampled (Arb's gamma_upper also degenerates there at the real points b - y/2 = 0, -1, ...).
    edges = [(lambda s: complex(xb, s), 0.0, Y), (lambda s: complex(xb - s, Y), 0.0, xb - xa)]
    if xa > 0:
        edges.append((lambda s: complex(xa, Y - s), 0.0, Y))
    for (fn, a, b) in edges:
        t, n, f = argpath(N, fn, a, b, ds, route)
        tot += t; ns += n; nf += f
    val = tot / math.pi
    return {"N": N, "xa": xa, "xb": xb, "Y": Y, "count": int(round(val)), "dev": abs(val - round(val)),
            "samples": ns, "flags": nf, "secs": round(time.time() - t0, 2)}

def seed_scan(N, xa, xb, ytop, route="T", dx=None, dy=0.8):
    """Newton from a grid of seeds in [xa,xb] x (0, ytop]; returns the distinct non-real zeros found in the strip."""
    out = []
    x = xa + 0.01
    while x <= xb:
        sp = 2 * math.pi / math.log(max(x, 40.0) / (2 * math.pi))
        y = 0.15
        while y <= ytop:
            z, ok = newton_XiN(N, complex(x, y), route, it=40, maxmove=2.0)
            if ok and z.imag > 1e-6 and xa - 1 <= z.real <= xb + 1 and all(abs(z - w) > 1e-7 for w in out):
                out.append(z)
            y += dy
        x += (dx or sp / 2)
    return dedup(out)

def fill(N, xa, xb, Y, zs, Rreal, route="T", width=12.0, logf=print):
    """make the located list of non-real zeros of Xi_N in [xa,xb] x (0,Y] complete strip by strip (argument principle
    per strip [a,b] x [-Y,Y] minus the real zeros in [a,b]); seeds a grid where a strip is short."""
    from axis import Sx
    zs = list(zs)
    a = xa
    report = []
    while a < xb - 1e-9:
        b = min(xb, a + width)
        # strip edges must avoid real zeros: nudge b off any real zero
        for r in Rreal:
            if abs(r - b) < 1e-3:
                b += 2e-3
        c = count_win(N, a, b, Y, route=route)
        nreal = sum(1 for r in Rreal if a < r < b)
        want = (c["count"] - nreal)
        have = 2 * sum(1 for z in zs if a < z.real < b and 0 < z.imag <= Y)
        if want != have:
            logf("  strip [%.3f, %.3f]: count %d, real %d, located non-real %d (x2) -> seed scan" % (a, b, c["count"], nreal, have // 2))
            for w in seed_scan(N, a, b, Y, route):
                if a < w.real < b and all(abs(w - v) > 1e-7 for v in zs):
                    zs.append(w)
            have = 2 * sum(1 for z in zs if a < z.real < b and 0 < z.imag <= Y)
        report.append({"a": a, "b": b, "count": c["count"], "real": nreal, "nonreal_located": have // 2,
                       "ok": c["count"] - nreal == have, "dev": c["dev"]})
        a = b
    return dedup(zs), report

def run(k, xa, xb, tag, Y=None, route="T", next_xb=None, h0=0.25, turnmax=0.12, seeds_k=None):
    T0 = time.time()
    R = {"k": k, "tag": tag, "window": [xa, xb], "route": route}
    log("k=%d %s window [%.3f, %.3f]" % (k, tag, xa, xb))
    # (d) and real counts: one scan of S_k
    ax = scan(k, xa, xb, route)
    R["axis"] = {kk: ax[kk] for kk in ("R_k", "R_k1", "n_max", "n_min", "n_unresolved", "all_consistent", "ngrid",
                                        "nrefined", "zeros_Xik", "zeros_Xik1", "extrema01", "secs")}
    R["axis"]["bad_intervals"] = [I for I in ax["intervals01"] if not I["consistent"]]
    sa, sb = Sx(k, xa, route)[0], Sx(k, xb, route)[0]
    R["axis"]["S_at_ends"] = [sa, sb]
    R["axis"]["ends_outside_01"] = not (0 <= sa <= 1) and not (0 <= sb <= 1)
    log("  axis: R_k=%d R_k+1=%d max=%d min=%d unresolved=%d consistent=%s (%.0fs)" % (ax["R_k"], ax["R_k1"], ax["n_max"],
        ax["n_min"], ax["n_unresolved"], ax["all_consistent"], ax["secs"]))
    # (a) non-real zeros of Xi_k in the window
    zk = [z for z in (seeds_k if seeds_k is not None else locate(k, xa, xb, route)) if xa < z.real < xb]
    log("  located %d non-real zeros of Xi_%d" % (len(zk), k))
    # (b) branches
    br = []
    for i, z in enumerate(zk):
        r = trace(k, z, -1, h0, turnmax, route, xedge=xb)
        r["path"] = subsample(r["path"])
        br.append(r)
    log("  traced %d branches (%.0fs)" % (len(br), time.time() - T0))
    # zeros of Xi_{k+1}: branch ends + march (+ to next_xb for the next pencil)
    ends = [complex(*r["z_end"]) for r in br if r["end"] == "u0"]
    zk1_all = march(k + 1, dedup(ends), max(xb, next_xb or xb) + 5, route) if ends else []
    zk1 = [z for z in zk1_all if xa < z.real < xb]
    # Y and counts (fill strips that are short)
    ymax = max([z.imag for z in zk + zk1] + [1.0])
    Y = Y or float(math.ceil(ymax + 5))
    R["Y"] = Y
    # window counts first; the strip-by-strip completion (fill) runs only for a function whose count does not match
    ck = count_win(k, xa, xb, Y, route=route); ck1 = count_win(k + 1, xa, xb, Y, route=route)
    repk = repk1 = []
    if ck["count"] != ax["R_k"] + 2 * len([z for z in zk if z.imag <= Y]):
        log("  count mismatch for Xi_%d: %d vs %d + 2*%d -> strips" % (k, ck["count"], ax["R_k"], len(zk)))
        zk, repk = fill(k, xa, xb, Y, zk, ax["zeros_Xik"], route, logf=log)
    if ck1["count"] != ax["R_k1"] + 2 * len([z for z in zk1 if z.imag <= Y]):
        log("  count mismatch for Xi_%d: %d vs %d + 2*%d -> strips" % (k + 1, ck1["count"], ax["R_k1"], len(zk1)))
        zk1, repk1 = fill(k + 1, xa, xb, Y, zk1, ax["zeros_Xik1"], route, logf=log)
    R["strips_k"], R["strips_k1"] = repk, repk1
    ck4 = count_win(k, xa, xb, 4 * Y, route=route); ck14 = count_win(k + 1, xa, xb, 4 * Y, route=route)
    R["counts"] = {"Xi_k@Y": ck, "Xi_k1@Y": ck1, "Xi_k@4Y": ck4, "Xi_k1@4Y": ck14}
    nk = [z for z in zk if z.imag <= Y]; nk1 = [z for z in zk1 if z.imag <= Y]
    R["zeros_Xik_nonreal"], R["zeros_Xik1_nonreal"] = jl(nk), jl(nk1)
    chk = {"count_k": ck["count"] == ax["R_k"] + 2 * len(nk), "count_k1": ck1["count"] == ax["R_k1"] + 2 * len(nk1),
           "Y_stable_k": ck["count"] == ck4["count"], "Y_stable_k1": ck1["count"] == ck14["count"]}
    # trace branches from zeros of Xi_k found by the fill (not traced yet)
    done = [complex(*r["start"]) for r in br]
    for z in nk:
        if all(abs(z - w) > 1e-8 for w in done):
            r = trace(k, z, -1, h0, turnmax, route, xedge=xb); r["path"] = subsample(r["path"]); br.append(r)
    R["branches"] = br
    # (c) completeness
    endsU0 = [complex(*r["z_end"]) for r in br if r["end"] == "u0"]
    unmatched = [z for z in nk1 if all(abs(z - w) > 1e-8 * max(1, abs(z)) for w in endsU0)]
    back = []
    for z in unmatched:
        rb = trace(k, z, +1, h0, turnmax, route, xedge=None); rb["path"] = subsample(rb["path"]); back.append(rb)
    R["backward_from_unmatched_Xik1"] = back
    lands = sorted([r["x_land"] for r in br if r["end"] == "landed" and "x_land" in r])
    maxima = sorted([e["x"] for e in ax["extrema01"] if e["type"] == "max"])
    lm = [x for x in maxima if all(abs(x - y) > 1e-7 for y in lands)]
    back2 = []
    for x in lm:
        z0 = complex(x, 1e-3)
        rb = trace(k, z0, +1, h0, turnmax, route); rb["path"] = subsample(rb["path"]); back2.append(rb)
    R["backward_from_unmatched_maxima"] = back2
    chk["landings_eq_half_real_diff"] = len(lands) == (ax["R_k1"] - ax["R_k"]) / 2.0
    chk["landings_match_maxima"] = len(lm) == 0 and len(lands) == len(maxima)
    chk["all_Xik1_nonreal_are_ends"] = len(unmatched) == 0
    chk["axis_no_min"] = ax["n_min"] == 0 and ax["n_unresolved"] == 0
    chk["axis_intervals_consistent"] = ax["all_consistent"]
    chk["axis_ends_outside_01"] = R["axis"]["ends_outside_01"]
    R["checks"] = chk
    R["zk1_all_for_next"] = jl(zk1_all)
    R["secs"] = round(time.time() - T0, 1)
    return R

def hygiene(R, route="T", every=10, lt=True):
    k = R["k"]
    br = R["branches"]
    H = {"retrace": [], "LT": None}
    for i in range(0, len(br), every):
        r = br[i]
        r2 = trace(k, complex(*r["start"]), -1, r["h0"] / 2, r["turnmax"] / 2, route, xedge=R["window"][1], keep_path=False)
        if r["end"] == "landed" and "x_land" in r and "x_land" in r2:
            diff = max(abs(r["x_land"] - r2["x_land"]), abs(r["u_land"] - r2["u_land"]) / max(abs(r["u_land"]), 1e-300) * 1e-8)
            d = {"i": i, "end": r["end"], "end2": r2["end"], "dx_land": abs(r["x_land"] - r2["x_land"]),
                 "du_land_rel": abs(r["u_land"] - r2["u_land"]) / max(abs(r["u_land"]), 1e-300)}
        else:
            d = {"i": i, "end": r["end"], "end2": r2["end"],
                 "dz_end": abs(complex(*r["z_end"]) - complex(*r2["z_end"])) if r["end"] == "u0" else None}
        H["retrace"].append(d)
    if lt and k <= 6:
        worst = 0.0
        npts = 0
        for r in br:
            P = r["path"]
            for j in sorted(set([0, len(P) // 4, len(P) // 2, (3 * len(P)) // 4, len(P) - 1])):
                u, x, y = P[j]
                z = complex(x, y)
                a = S(k, az(z), "T", 40); b = S(k, az(z), "L", 40)
                ctx.prec = 128
                rel = float((abs(a - b) / abs(a)).mid()) if abs(a).mid() != 0 else 0.0
                worst = max(worst, rel); npts += 1
        H["LT"] = {"points": npts, "max_rel_diff": worst}
    R["hygiene"] = H
    return H

def summarize(R):
    br = R["branches"]
    xb = R["window"][1]
    land = [r for r in br if r["end"] == "landed"]
    # a branch that reaches u = 0 at a zero of Xi_{k+1} beyond Re z = xb crossed the right edge first: an exit
    u0 = [r for r in br if r["end"] == "u0" and r["z_end"][0] <= xb]
    ex = [r for r in br if r["end"] == "exit-right" or (r["end"] == "u0" and r["z_end"][0] > xb)]
    other = [r for r in br if r["end"] not in ("landed", "u0", "exit-right")]
    wdy = max([r["worst_dy"] for r in br] + [-float("inf")])
    mm = min([r["min_margin"] for r in br] + [float("inf")])
    S_ = {"R_k": R["axis"]["R_k"], "R_k1": R["axis"]["R_k1"], "nonreal_k": len(R["zeros_Xik_nonreal"]),
          "nonreal_k1": len(R["zeros_Xik1_nonreal"]), "branches": len(br), "landings": len(land), "nonreal_ends": len(u0),
          "exits": len(ex), "other_ends": [(r["start"], r["end"]) for r in other], "worst_dy": wdy, "min_margin": mm,
          "checks": R["checks"], "Y": R["Y"], "arb_maxrel": max(STATS["maxrel"], R.get("summary", {}).get("arb_maxrel", 0)),
          "arb_maxprec": max(STATS["maxprec"], R.get("summary", {}).get("arb_maxprec", 0)), "secs": R["secs"]}
    R["summary"] = S_
    return S_

if __name__ == "__main__":
    k = int(sys.argv[1]); tag = sys.argv[2] if len(sys.argv) > 2 else "P1"
    if tag == "P1":
        xa, xb, nxt = 0.0, Xk(k), Xk(k + 1)
    else:
        xa, xb, nxt = 4.0 * (k + 1) ** 2 - 40, 4.0 * (k + 2) ** 2 + 40, None
    ctx.prec = 96
    R = run(k, xa, xb, tag, next_xb=nxt)
    hygiene(R)
    s = summarize(R)
    log("SUMMARY k=%d %s: %s" % (k, tag, json.dumps({kk: v for kk, v in s.items() if kk != "other_ends"})))
    log("hygiene: %s" % json.dumps(R["hygiene"]))
    os.makedirs(DATA, exist_ok=True)
    fn = os.path.join(DATA, ("census_k%d.json" if tag == "P1" else "frontier_k%d.json") % k)
    json.dump(R, open(fn, "w"), separators=(",", ":"))
    if tag == "P1":
        json.dump({"N": k + 1, "zeros": R["zk1_all_for_next"], "from": "census k=%d (branch ends + march)" % k},
                  open(os.path.join(DATA, "zeros_Xi%d.json" % (k + 1)), "w"))
    log("wrote %s (%.0f kB)" % (fn, os.path.getsize(fn) / 1024.0))
