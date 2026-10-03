# regen.py -- regenerate the rows of the §0-P1 / §0-P2 tables of NOTE.md from the data files (keeps notes lines).
import os, sys, glob, json
from row import row
H = os.path.dirname(os.path.abspath(__file__))
fn = os.path.join(H, "..", "NOTE.md")
L = open(fn).read().split("\n")
def regen(marker, files):
    i = L.index(marker)
    j = i
    while not L[j - 1].startswith("|---"):
        j -= 1
    old = L[j:i]
    notes = [l for l in old if not l.startswith("| ")]
    new = [row(f) for f in files]
    L[j:i] = new + notes
D = os.path.join(H, "..", "data")
p1 = sorted(glob.glob(os.path.join(D, "census_k*.json")), key=lambda f: int(f.split("census_k")[1].split(".")[0]))
p2 = sorted(glob.glob(os.path.join(D, "frontier_k*.json")), key=lambda f: int(f.split("frontier_k")[1].split(".")[0]))
regen("<!-- P1 rows -->", p1)
regen("<!-- P2 rows -->", p2)
open(fn, "w").write("\n".join(L))
print("P1 rows", len(p1), "P2 rows", len(p2))
