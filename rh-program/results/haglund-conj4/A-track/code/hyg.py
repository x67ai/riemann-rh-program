# hyg.py -- aggregate the numerical hygiene of all finished census / frontier files.
import os, json, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
tot = {"files": 0, "branches": 0, "retraced": 0, "retrace_same_end": 0, "retrace_max_dx_land": 0.0, "retrace_max_dz_end": 0.0,
       "LT_points": 0, "LT_max_rel": 0.0, "arb_maxrel": 0.0, "arb_maxprec": 0, "count_flags": 0, "count_maxdev": 0.0,
       "max_turn": 0.0, "max_rejections": 0}
for fn in sorted(glob.glob(os.path.join(D, "census_k*.json")) + glob.glob(os.path.join(D, "frontier_k*.json"))):
    R = json.load(open(fn))
    s = R["summary"]; H = R["hygiene"]
    tot["files"] += 1; tot["branches"] += len(R["branches"])
    for r in H["retrace"]:
        tot["retraced"] += 1
        tot["retrace_same_end"] += int(r["end"] == r["end2"])
        tot["retrace_max_dx_land"] = max(tot["retrace_max_dx_land"], r.get("dx_land") or 0.0)
        tot["retrace_max_dz_end"] = max(tot["retrace_max_dz_end"], r.get("dz_end") or 0.0)
    if H.get("LT"):
        tot["LT_points"] += H["LT"]["points"]; tot["LT_max_rel"] = max(tot["LT_max_rel"], H["LT"]["max_rel_diff"])
    tot["arb_maxrel"] = max(tot["arb_maxrel"], s["arb_maxrel"]); tot["arb_maxprec"] = max(tot["arb_maxprec"], s["arb_maxprec"])
    for c in R["counts"].values():
        tot["count_flags"] += c["flags"]; tot["count_maxdev"] = max(tot["count_maxdev"], c["dev"])
    for r in R["branches"]:
        tot["max_turn"] = max(tot["max_turn"], r["max_turn"]); tot["max_rejections"] = max(tot["max_rejections"], r["rejections"])
print(json.dumps(tot, indent=0))
