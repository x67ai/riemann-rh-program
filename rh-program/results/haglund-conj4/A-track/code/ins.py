# ins.py -- insert the lines read from stdin into NOTE.md just before the marker line "<!-- <name> -->".
import sys, os
name = sys.argv[1]
fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "NOTE.md")
L = open(fn).read().split("\n")
new = [l for l in sys.stdin.read().split("\n") if l.strip() != ""] if len(sys.argv) < 3 else sys.stdin.read().rstrip("\n").split("\n")
m = "<!-- %s -->" % name
i = L.index(m)
L[i:i] = new
open(fn, "w").write("\n".join(L))
print("inserted %d lines before %s" % (len(new), m))
