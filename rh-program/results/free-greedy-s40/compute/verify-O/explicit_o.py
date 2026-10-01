# explicit_o.py -- zero sum -sum 2Re(x^r/r) over the unit's 44 zeros of F_{1e11} (sigma > 1/2, t <= 200) and
# -x^b/b for the real zero, against MY measured psi_P(x) - x (verify-O/logs/o_pi4_1e9.log, o_pi4_1e10.log). Opus reader.
import sys
zs = set()
for line in open('../verify/logs/zeros_pi4_X1.000000e+11.txt'):
    if line.startswith('#'): continue
    f = line.split()
    try: s, t = float(f[0]), float(f[1])
    except: continue
    if 0.5 < s < 1.05 and 0.01 < t <= 200: zs.add((round(s, 10), round(t, 10)))
zs = sorted(zs, key=lambda z: z[1]); beta = 0.5147419
print(f"# {len(zs)} complex zeros (unit's list at X = 1e11) + real zero {beta}")
meas = {}
for fn in ('logs/o_pi4_1e9.log', 'logs/o_pi4_1e10.log'):
    try:
        for line in open(fn):
            if line[0].isdigit(): f = line.split(); meas[float(f[0])] = float(f[5])
    except FileNotFoundError: pass
for x in sorted(meas):
    if x < 1e4: continue
    P = -sum(2 * (x ** complex(s, t) / complex(s, t)).real for s, t in zs) - x ** beta / beta
    print(f"x={x:.4e} measured psi-x={meas[x]:+.6e} zero-sum={P:+.6e} diff={meas[x]-P:+.3e} ({(meas[x]-P)/abs(meas[x])*100:+.2f} %)")
