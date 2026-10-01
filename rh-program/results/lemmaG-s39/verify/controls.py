#!/usr/bin/env python3
"""controls.py — the random-surgery control (Theorem B: Bernoulli thinning T_0.75, seeds 1-4, X = 1e10, frontier data, read-only) and
the regular-deletion control (greedy c = 1, alpha = 0.75, X = 1e10) through THIS unit's pipeline (dyadic.py), with the truncated
Franel diagonal from cO's rnums outputs (converted to this unit's 'rn' rows). No count is recomputed; files are read in place."""
import subprocess, os
FR = "../../novel-wave-s37/beurling-frontier/verify/data_big/"; CO = "../../conj-O-s38/verify/rn/"
os.makedirs("data/controls", exist_ok=True)
def conv(src, run, dst):
    with open(dst, "w") as f:
        for line in open(src):
            if line.startswith("#"): continue
            hi, piR, Q, W = line.strip().split(","); f.write("rn,%s,%s,%s,%s\n" % (run, hi, Q, W))
args = []
for s in (1, 2, 3, 4):
    conv(CO + "bern_a0.75_s%d.csv" % s, "bern_a0.750_s%d" % s, "data/controls/bern_s%d.rn" % s)
os.system("cat data/controls/bern_s1.rn data/controls/bern_s2.rn data/controls/bern_s3.rn data/controls/bern_s4.rn > data/controls/bern_all.rn")
args.append(FR + "bern_a0.75.csv:data/controls/bern_all.rn")
head = open(FR + "greedy_a0.75.csv").readline().strip(); run = head.split("run=")[1].split()[0]
conv(CO + "greedy_a0.75_c1.csv", run, "data/controls/greedy075.rn"); args.append(FR + "greedy_a0.75.csv:data/controls/greedy075.rn")
print(subprocess.run(["python3", "dyadic.py"] + args, capture_output=True, text=True).stdout)
