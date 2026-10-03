# p3table.py -- NOTE rows for the P3 files p3_k<k>.json (k given on the command line).
import sys, os, json
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
for k in [int(a) for a in sys.argv[1:]]:
    o = json.load(open(os.path.join(D, "p3_k%d.json" % k)))
    ok = (o["n_min"] == 0 and o["n_unresolved"] == 0 and o["all_consistent"] and o["frontier_rescan_agrees"]
          and o["S_at_0"] > 1 and o["S_at_X"] < 0 and o["landings_eq_half_real_diff"])
    umin = min([u for x, u in o["maxima"]] + [1.0])
    print("| %d | %.0f | %d / %d | %d | %d | %s | %s | %s | %.1e | %.4f | %s |" % (
        k, o["X"], o["R_k"], o["R_k1"], o["n_max"], o["n_min"], "yes" if o["landings_eq_half_real_diff"] else "NO",
        "yes" if o["all_consistent"] else "NO", "yes" if o["frontier_rescan_agrees"] else "NO", umin,
        o["largest_real_zero_Xik1"] or 0, "PASS" if ok else "CHECK"))
