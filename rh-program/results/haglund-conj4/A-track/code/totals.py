# totals.py -- totals over the finished P1 / P2 files for the close block.
import os, json, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
def tot(pattern):
    fs = sorted(glob.glob(os.path.join(D, pattern)), key=lambda f: int(f.rsplit("_k", 1)[1].split(".")[0]))
    T = {"ks": [], "branches": 0, "landings": 0, "ends": 0, "exits": 0, "worst_dy": -1e300, "min_margin": 1e300,
         "all_checks": True, "failed": []}
    for f in fs:
        R = json.load(open(f)); s = R["summary"]
        T["ks"].append(R["k"]); T["branches"] += s["branches"]; T["landings"] += s["landings"]
        T["ends"] += s["nonreal_ends"]; T["exits"] += s["exits"]
        T["worst_dy"] = max(T["worst_dy"], s["worst_dy"]); T["min_margin"] = min(T["min_margin"], s["min_margin"])
        bad = [c for c, v in s["checks"].items() if not v]
        if bad: T["all_checks"] = False; T["failed"].append((R["k"], bad))
    return T
print("P1", json.dumps(tot("census_k*.json")))
print("P2", json.dumps(tot("frontier_k*.json")))
