"""Q3 table from ../data/q3-k{k}.json"""
import json, sys, os
import mpmath as mp
print('| k | range | points | B>0 | real Xi_k / Xi_k+1 | extrema | max in (0,1) (x*, tau*) | min in (0,1) |')
print('|---|---|---|---|---|---|---|---|')
for k in range(1, 13):
    f = '../data/q3-k%d.json' % k
    if not os.path.exists(f): continue
    r = json.load(open(f))
    mx = [e for e in r['extrema_in01'] if e['type'] == 'max']
    lst = '; '.join('%.4f, %.3f' % (float(e['x']), float(-mp.log(mp.mpf(e['S'])))) for e in mx)
    print('| %d | [0, %.1f] | %d | %s | %d / %d | %d | %d: %s | %d |' % (k, r['x_end'], r['n_points'], r['B_positive'],
          r['real_zeros_t0'], r['real_zeros_t1'], r['extrema_total'], len(mx), lst, len(r['min_in01'])))
