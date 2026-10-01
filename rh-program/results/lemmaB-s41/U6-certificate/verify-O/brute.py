#!/usr/bin/env python3
"""brute.py — definition-level brute force for S8(pi/D) (read-O, U6): sweep the lattice points x_m = 1 + (m - 1/2) t
in order; at each, pop from a min-heap every g-integer < x_m (mpmath, 60 digits); place a g-prime iff N(x_m-) = m,
then push p^k g for every known g-integer g (all of them exceed x_m). No cell form, no symmetric functions, no
fixed point: an independent check of s8gen at small X.
Usage: brute.py D X  -> prints N, pi at integer checkpoints, lattice data, and writes brute_D_X.txt (cell of every
composite) for comparison."""
import sys, heapq, bisect
import mpmath as mp
mp.mp.dps = 60
D = int(sys.argv[1]); X = mp.mpf(sys.argv[2])
t = mp.mpf(D) / mp.pi
K = int(mp.floor(mp.pi * (X - 1) / D + mp.mpf(1) / 2))
heap = [(mp.mpf(1), ())]                  # (value, sorted tuple of prime lattice indices)
known = [(mp.mpf(1), ())]                 # all g-integers <= X found so far
primes = []; N = 0; pic = 0
cps = [V for V in (1000, 3162, 10000, 31622, 100000, 316227, 1000000) if V < 1 + (K - mp.mpf(1) / 2) * t]
cpres = {}; cellof = {}
minmarg = mp.mpf(10)
for m in range(1, K + 1):
    xm = 1 + (m - mp.mpf(1) / 2) * t
    while heap and heap[0][0] < xm:
        v, fac = heapq.heappop(heap)
        for V in cps:
            if V not in cpres and v > V:
                cpres[V] = (N, pic)
        N += 1
        if len(fac) >= 2:
            cellof[fac] = m
            w = mp.pi * (v - 1) / D + mp.mpf(1) / 2
            minmarg = min(minmarg, w - mp.floor(w), mp.ceil(w) - w)
    for V in cps:
        if V not in cpres and xm > V:
            cpres[V] = (N, pic)
    if heap and abs(heap[0][0] - xm) < mp.mpf(10) ** -40:
        raise SystemExit("tie within 1e-40")
    if N == m:                            # D(x_m) reaches 1/2: place a g-prime at x_m
        pic += 1; N += 1; primes.append(m)
        p = xm; new = []
        lim = X / p
        for (g, fac) in known:
            if g > lim: break
            v = g * p; e = 1
            while v <= X:
                nf = tuple(sorted(fac + (m,) * e))
                new.append((v, nf))
                if len(nf) >= 2: heapq.heappush(heap, (v, nf))   # the prime itself is counted at placement
                v *= p; e += 1
        for it in new: bisect.insort(known, it)
    elif N < m:
        raise SystemExit("violation N(x_m-) < m")
print("brute D=%d X=%s K=%d N(x_K)=%d pi(x_K)=%d e_K=%d composites=%d min margin in W %.3e"
      % (D, mp.nstr(X, 12), K, N, pic, N - K - 1, len(cellof), float(minmarg)))
for V in cps:
    print("CHECK V=%d N(V)=%d pi(V)=%d" % (V, cpres[V][0], cpres[V][1]))
with open("brute_%d_%s.txt" % (D, sys.argv[2]), "w") as f:
    for fac in sorted(cellof, key=lambda q: (cellof[q], q)):
        f.write("%d %s\n" % (cellof[fac], " ".join(map(str, fac))))
    f.write("PRIMES %s\n" % " ".join(map(str, primes)))
