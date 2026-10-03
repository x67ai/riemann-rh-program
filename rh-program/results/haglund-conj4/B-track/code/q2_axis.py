"""Q2 real axis: S_k on [x0, x1] for k = 26, 27 -> ../data/q2-axis-k{k}.json"""
import sys, json
sys.path.insert(0, '.')
import mpmath as mp, realaxis
mp.mp.dps = 30
k = int(sys.argv[1]); x0 = float(sys.argv[2]); x1 = float(sys.argv[3])
r = realaxis.run(k, x1, 0.05, 0.01, x_start=x0)
json.dump(r, open('../data/q2-axis-k%d.json' % k, 'w'), indent=1)
print(json.dumps({kk: r[kk] for kk in r if kk not in ('extrema_near',)}, indent=1))
