"""
u3a_zeros_chunk.py -- resumable, chunked computation of zeta zeros with Arb (acb.zeta_zeros, Platt-type,
certified on the critical line).  Each call appends up to CHUNK zeros (in sub-chunks of 5000) to
tables/zeta_zeros_arb.txt and stops before ~8 minutes.  Usage: python3 u3a_zeros_chunk.py TARGET
"""
import sys, os, time
from flint import acb, ctx
here = os.path.dirname(os.path.abspath(__file__))
tabdir = os.path.join(os.path.dirname(here), 'tables')
zfile = os.path.join(tabdir, 'zeta_zeros_arb.txt')
TARGET = int(sys.argv[1])
n_have = 0
if os.path.exists(zfile):
    with open(zfile) as fh:
        for line in fh:
            n_have += 1
ctx.prec = 140
t0 = time.time()
with open(zfile, 'a') as fh:
    n = n_have + 1
    while n <= TARGET and time.time() - t0 < 480:
        k = min(5000, TARGET - n + 1)
        zz = acb.zeta_zeros(n, k)
        for i, z in enumerate(zz):
            fh.write('%d %s %d\n' % (n + i, z.imag.str(34, radius=False), int(z.imag.rel_accuracy_bits())))
        fh.flush()
        n += k
        print('zeros to', n - 1, '%.1fs' % (time.time() - t0), flush=True)
print('have', n - 1)
