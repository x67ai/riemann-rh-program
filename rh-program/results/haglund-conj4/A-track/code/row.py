# row.py -- print the NOTE §0 row and a short SHARED line for a finished census file (P1 or P2).
import sys, os, json
HAG = {1: 1, 2: 7, 3: 15, 4: 32, 5: 53, 6: 79, 7: 113, 8: 155, 9: 207, 10: 263}
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def row(fn, wind=None):
    R = json.load(open(fn))
    s = R["summary"]; k = R["k"]; c = s["checks"]; H = R["hygiene"]
    names = [("count_k", "A"), ("Y_stable_k", "A4")]
    ok = []
    if c["count_k"] and c["count_k1"]: ok.append("A")
    if c["Y_stable_k"] and c["Y_stable_k1"]: ok.append("A4")
    if wind: ok.append("W")
    if c["all_Xik1_nonreal_are_ends"]: ok.append("C1")
    if c["landings_eq_half_real_diff"]: ok.append("C2")
    if c["landings_match_maxima"]: ok.append("C3")
    if c["axis_no_min"] and c["axis_intervals_consistent"] and c.get("axis_ends_outside_01", True): ok.append("D")
    rt = H["retrace"]
    rt_ok = all(r["end"] == r["end2"] and ((r.get("dx_land", 0) or 0) < 1e-8) and ((r.get("dz_end", 0) or 0) < 1e-8) for r in rt)
    lt = H.get("LT")
    hyg = "re-trace %d/%d" % (sum(1 for r in rt if r["end"] == r["end2"]), len(rt))
    mx = max([r.get("dx_land", 0) or 0 for r in rt] + [r.get("dz_end", 0) or 0 for r in rt] + [0])
    hyg += " (ends to %.1e)" % mx
    if lt: hyg += "; L/T %d pts max rel %.1e" % (lt["points"], lt["max_rel_diff"])
    hyg += "; Arb rel radius <= %.1e" % s["arb_maxrel"]
    if rt_ok and (lt is None or lt["max_rel_diff"] < 1e-11) and s["arb_maxrel"] <= 2.0 ** -40: ok.append("H")
    failed = [kk for kk, v in c.items() if not v]
    xa, xb = R["window"]
    hag = HAG.get(k), HAG.get(k + 1)
    hs = " [%s / %s]" % (hag[0] if hag[0] else "-", hag[1] if hag[1] else "-") if R["tag"] == "P1" else ""
    other = s.get("other_ends") or []
    line = "| %d | %s | %.0f | %d / %d%s | %d / %d | %d | %d | %d | %d | %.1e | %.3f | %s%s; %s |" % (
        k, ("%.2f" % xb) if R["tag"] == "P1" else ("[%.0f, %.0f]" % (xa, xb)), s["Y"], s["R_k"], s["R_k1"], hs,
        s["nonreal_k"], s["nonreal_k1"], s["branches"], s["landings"], s["nonreal_ends"], s["exits"], s["worst_dy"],
        s["min_margin"], ", ".join(ok), (" FAILED: " + ", ".join(failed)) if failed else "", hyg)
    if other: line += " other ends: %s" % other
    return line

if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(row(a))
