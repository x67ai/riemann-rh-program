# stripo.py -- read-O: argument principle for F_X = rho*zeta + D_X on the rectangle [s0, s1] x [t0, t1] (direct sums via fxo,
# exact ratio recurrence along each side; zeta by mpmath). Reports the winding number, the largest phase step and min|F| per side.
# usage: stripo.py dump X s0 s1 t0 t1 Ks Kt
import subprocess, sys, os, math, cmath, mpmath as mp
mp.mp.dps = 15
FXO = '/private/tmp/rh-s41-read-localgreedy/fxo'; TMP = '/private/tmp/rh-s41-read-localgreedy'
dump, X = sys.argv[1], int(float(sys.argv[2])); s0, s1, t0, t1 = map(float, sys.argv[3:7]); Ks, Kt = int(sys.argv[7]), int(sys.argv[8])
hs, ht = (s1 - s0)/Ks, (t1 - t0)/Kt
seg = os.path.join(TMP, 'strip_%d.txt' % os.getpid())
with open(seg, 'w') as f:
    f.write('%.15f %.15f %.15f 0 %d\n' % (s0, t0, hs, Ks)); f.write('%.15f %.15f 0 %.15f %d\n' % (s1, t0, ht, Kt))
    f.write('%.15f %.15f %.15f 0 %d\n' % (s1, t1, -hs, Ks)); f.write('%.15f %.15f 0 %.15f %d\n' % (s0, t1, -ht, Kt))
RN, RD = os.environ.get('RHO_NUM', '3'), os.environ.get('RHO_DEN', '5'); rho = mp.mpf(RN)/int(RD)
out = subprocess.run([FXO, dump, str(X), RN, RD, seg], capture_output=True, text=True, check=True).stdout.split('\n')
pts = []
for l in out:
    v = l.split()
    if len(v) == 7: pts.append((int(v[0]), complex(float(v[1]), float(v[2])), complex(float(v[3]), float(v[4]))))
cyc = []
for q in range(4):
    side = [p for p in pts if p[0] == q]; cyc += side[:-1]
vals = [(q, s, complex(rho*mp.zeta(mp.mpc(s.real, s.imag))) + d) for q, s, d in cyc]
wind = 0.0; maxstep = [0.0]*4; minF = [1e9]*4
for i in range(len(vals)):
    q, s, F = vals[i]; G = vals[(i+1) % len(vals)][2]; st = cmath.phase(G/F); wind += st
    maxstep[q] = max(maxstep[q], abs(st)); minF[q] = min(minF[q], abs(F))
print('RECT X=%d [%.3f,%.3f]x[%.3f,%.3f] steps hs=%.4f ht=%.4f points=%d' % (X, s0, s1, t0, t1, hs, ht, len(vals)))
print('  winding = %.6f' % (wind/(2*math.pi)))
for q, name in enumerate(('bottom', 'right', 'top', 'left')): print('  %-6s max phase step %.4f rad, min|F| %.5f' % (name, maxstep[q], minF[q]))
