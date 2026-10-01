# boxo.py -- read-O: winding number and min|F_X| on a box boundary from DIRECT sums (fxo, exact ratio recurrence along
# each side; no Taylor moments) + mpmath zeta; sampled Lipschitz margin; tail bound under H_theta (NOTE §3.0 formula).
# usage: boxo.py dump X s0 s1 t0 t1 K CX   (CX = C(X) = N(X) - 0.6X, from the generator log)
import subprocess, sys, os, math, cmath, mpmath as mp
mp.mp.dps = 25
FXO = '/private/tmp/rh-s41-read-localgreedy/fxo'; TMP = '/private/tmp/rh-s41-read-localgreedy'
dump, X = sys.argv[1], int(float(sys.argv[2])); s0, s1, t0, t1 = map(float, sys.argv[3:7]); K = int(sys.argv[7]); CX = float(sys.argv[8])
hs, ht = (s1 - s0)/K, (t1 - t0)/K
seg = os.path.join(TMP, 'box_%d.txt' % os.getpid())
with open(seg, 'w') as f:
    f.write('%.15f %.15f %.15f 0 %d\n' % (s0, t0, hs, K)); f.write('%.15f %.15f 0 %.15f %d\n' % (s1, t0, ht, K))
    f.write('%.15f %.15f %.15f 0 %d\n' % (s1, t1, -hs, K)); f.write('%.15f %.15f 0 %.15f %d\n' % (s0, t1, -ht, K))
out = subprocess.run([FXO, dump, str(X), os.environ.get('RHO_NUM', '3'), os.environ.get('RHO_DEN', '5'), seg], capture_output=True, text=True, check=True).stdout.split('\n')
pts = []
for l in out:
    v = l.split()
    if len(v) == 7: pts.append((int(v[0]), complex(float(v[1]), float(v[2])), complex(float(v[3]), float(v[4])), complex(float(v[5]), float(v[6]))))
cyc = []
for q in range(4):
    side = [p for p in pts if p[0] == q]; cyc += side[:-1]          # drop each side's end point (= next side's start)
RN, RD = os.environ.get('RHO_NUM', '3'), os.environ.get('RHO_DEN', '5'); rho = mp.mpf(RN)/int(RD); vals = []
for q, s, d, dd in cyc:
    z = mp.mpc(s.real, s.imag); F = complex(rho*mp.zeta(z)) + d; Fp = complex(rho*mp.zeta(z, derivative=1)) + dd; vals.append((s, F, Fp))
wind = 0.0; maxstep = 0.0
for i in range(len(vals)):
    a, b = vals[i][1], vals[(i+1) % len(vals)][1]; st = cmath.phase(b/a); wind += st; maxstep = max(maxstep, abs(st))
mins = min(vals, key=lambda v: abs(v[1])); maxd = max(abs(v[2]) for v in vals); h = max(hs, ht)
print('BOX X=%d [%.4f,%.4f]x[%.4f,%.4f] K=%d points=%d' % (X, s0, s1, t0, t1, K, len(vals)))
print('  winding = %.6f   max phase step = %.4f rad' % (wind/(2*math.pi), maxstep))
print('  min|F_X| on samples = %.5f at s = %.5f + %.5fi ; max|F_X\'| on samples = %.4f ; spacing h = %.5f' % (abs(mins[1]), mins[0].real, mins[0].imag, maxd, h))
print('  sampled Lipschitz lower bound  min|F| - max|F\'| h/2 = %.5f' % (abs(mins[1]) - maxd*h/2))
for th in (0.30, 0.35, 0.40, 0.45):
    tb = max(abs(CX)*X**(-v[0].real) + abs(v[0])*X**(th - v[0].real)/(v[0].real - th) for v in vals)
    corner = abs(CX)*X**(-s0) + abs(complex(s0, t1))*X**(th - s0)/(s0 - th)
    print('  tail bound H_%.2f: max over samples %.5f ; at corner (s0, t1) %.5f ; ratio min|F|/tail = %.2f' % (th, tb, corner, abs(mins[1])/corner))
