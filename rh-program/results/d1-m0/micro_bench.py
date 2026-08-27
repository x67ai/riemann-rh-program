"""micro_bench.py -- per-operation mpmath cost vs precision (pure-python backend)
+ interval-arithmetic (mpmath.iv) overhead factors.  Feeds the D-R5 cost-curve
fit: build_matrix cost ~ (#transcendental evals) * t_sin(dps) etc.
"""
import json
import sys
import time

import mpmath as mp
from mpmath import iv


def bench(f, args_list, reps=3):
    best = None
    for _ in range(reps):
        t = time.perf_counter()
        for a in args_list:
            f(a)
        dt = (time.perf_counter() - t)/len(args_list)
        best = dt if best is None else min(best, dt)
    return best


def bench2(f, pairs, reps=3):
    best = None
    for _ in range(reps):
        t = time.perf_counter()
        for a, b in pairs:
            f(a, b)
        dt = (time.perf_counter() - t)/len(pairs)
        best = dt if best is None else min(best, dt)
    return best


def main():
    out = {'backend': mp.libmp.BACKEND, 'mpmath_version': mp.__version__,
           'float_ops_us': {}, 'iv_ops_us': {}, 'iv_over_float': {}}
    n = 400
    for dps in (30, 60, 100, 150, 200, 300):
        mp.mp.dps = dps
        xs = [mp.mpf('1.234567') + mp.mpf(i)/997 for i in range(n)]
        ys = [mp.mpf('0.987654') + mp.mpf(i)/1009 for i in range(n)]
        pairs = list(zip(xs, ys))
        row = {
            'sin': bench(mp.sin, xs)*1e6,
            'exp': bench(mp.exp, xs)*1e6,
            'mul': bench2(lambda a, b: a*b, pairs)*1e6,
            'add': bench2(lambda a, b: a + b, pairs)*1e6,
        }
        out['float_ops_us'][dps] = {k: round(v, 2) for k, v in row.items()}
        print(dps, out['float_ops_us'][dps], flush=True)

    for dps in (30, 60, 100, 150):
        iv.dps = dps
        mp.mp.dps = dps
        xs = [iv.mpf(mp.mpf('1.234567') + mp.mpf(i)/997) for i in range(n)]
        ys = [iv.mpf(mp.mpf('0.987654') + mp.mpf(i)/1009) for i in range(n)]
        pairs = list(zip(xs, ys))
        row = {}
        try:
            row['sin'] = bench(iv.sin, xs)*1e6
            row['exp'] = bench(iv.exp, xs)*1e6
        except Exception as e:
            row['transcendental_error'] = repr(e)
        row['mul'] = bench2(lambda a, b: a*b, pairs)*1e6
        row['add'] = bench2(lambda a, b: a + b, pairs)*1e6
        out['iv_ops_us'][dps] = {k: (round(v, 2) if isinstance(v, float) else v)
                                 for k, v in row.items()}
        fl = out['float_ops_us'][dps]
        out['iv_over_float'][dps] = {
            k: round(row[k]/fl[k], 2) for k in row
            if k in fl and isinstance(row[k], float)}
        print('iv', dps, out['iv_ops_us'][dps], '->', out['iv_over_float'][dps],
              flush=True)

    with open(sys.argv[1], 'w') as fh:
        json.dump(out, fh, indent=1)
    print('done', sys.argv[1])


if __name__ == '__main__':
    main()
