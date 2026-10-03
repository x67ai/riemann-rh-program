# resum.py -- recompute the summary block of finished census files with the current census.summarize (no new evaluation).
import sys, json
from census import summarize
for fn in sys.argv[1:]:
    R = json.load(open(fn))
    s = summarize(R)
    json.dump(R, open(fn, "w"), separators=(",", ":"))
    print(fn.split("/")[-1], "landings", s["landings"], "nonreal_ends", s["nonreal_ends"], "exits", s["exits"])
