# zeros_track.py REF.zeros OTHER1.zeros [OTHER2.zeros ...] -- stability of the zeros of F_X under X:
# for every zero of the reference file (largest X), the nearest zero in each other file and the displacement.
import sys
def read(fn):
    Z, X = [], None
    for ln in open(fn):
        if ln.startswith("# X ="): X = float(ln.split()[3])
        p = ln.split()
        if p and not p[0].startswith("#"): Z.append(complex(float(p[0]), float(p[1])))
    return X, Z
XR, R = read(sys.argv[1])
others = [read(f) for f in sys.argv[2:]]
print(f"# zeros_track: reference X = {XR:.3e} ({len(R)} zeros); others: " + ", ".join(f"X = {X:.3e} ({len(Z)})" for X, Z in others))
print("#  sigma(ref)     t(ref)     " + "  ".join(f"|dz| at X={X:.1e}  dsigma" for X, _ in others))
for z in sorted(R, key=lambda q: -q.real):
    row = f"  {z.real:.8f}  {z.imag:12.6f}"
    for X, Z in others:
        if not Z: row += "      -        -   "; continue
        n = min(Z, key=lambda q: abs(q - z))
        row += f"   {abs(n - z):.2e}  {n.real - z.real:+.2e}"
    print(row)
