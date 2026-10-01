# tailcheck070.py -- read-O: along sigma = 0.70, t in [0.1, 100], compare |F_X| (X = 1e7, direct sums via fxo) with the H_0.40
# tail bound at X = 1e9, |C(X)|X^-sigma + |s|X^(theta-sigma)/(sigma-theta), |C(1e9)| = 2. Log: logs/strip_left_sigma070_tailcheck.log
# run: printf "0.70 0.1 0 0.025 3996\n" > leftline.txt; fxo g_c0_1e9.u16 10000000 3 5 leftline.txt > leftline.out; python3 tailcheck070.py
import mpmath as mp
mp.mp.dps = 15; rho = mp.mpf(3)/5; X = 1e9
rows = [l.split() for l in open('/private/tmp/rh-s41-read-localgreedy/leftline.out') if l.strip()]
best = (1e9, None); minF = (1e9, None)
for v in rows:
    s = complex(float(v[1]), float(v[2])); D = complex(float(v[3]), float(v[4]))
    F = abs(complex(rho*mp.zeta(mp.mpc(s.real, s.imag))) + D); tail = 2*X**(-0.70) + abs(s)*X**(0.40 - 0.70)/0.30
    if F/tail < best[0]: best = (F/tail, s, F, tail)
    if F < minF[0]: minF = (F, s)
print('sigma=0.70, t in [0.1,100], X=1e7 values: min|F_X| = %.4f at t = %.3f' % (minF[0], minF[1].imag))
print('min over the line of |F_X| / (H_0.40 tail at X=1e9) = %.3f at t = %.3f (|F|=%.4f, tail=%.4f)' % (best[0], best[1].imag, best[2], best[3]))
