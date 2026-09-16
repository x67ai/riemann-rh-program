#!/usr/bin/env python3
"""dh_zero_precision_check.py -- diagnostic: are the DH on-line zeros located at dps 20 accurate?  Refine at dps 40 and compare;
also compare f_DH(1/2 + iu) at dps 20 vs dps 40 at a few points, and compare Z_DH computed via xi_dh with the FE-symmetrized value."""
import sys, os, json
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..', 'ccm-dh-test')); import dh
zd = json.load(open(os.path.join(HERE, 'out', 'zero_side_dh.json')))
onl = [mp.mpf(z) for z in zd['online']]
t = 85.69934848537759
near = sorted(onl, key=lambda z: abs(z - t))[:6] + [onl[0], onl[-1]]
for z20 in near:
    mp.mp.dps = 40
    z40 = mp.findroot(lambda u: dh.z_dh(u)[0], z20)
    mp.mp.dps = 20; f20 = dh.f_dh(mp.mpc(0.5, z20)); zz20 = dh.z_dh(z20)
    mp.mp.dps = 40; f40 = dh.f_dh(mp.mpc(0.5, z20)); zz40 = dh.z_dh(z20)
    print(f"zero {mp.nstr(z20, 15)}: refined at dps 40 -> {mp.nstr(z40, 25)}; shift = {mp.nstr(z40 - z20, 3)};  f_DH(1/2+iu) at dps20 = {mp.nstr(f20, 8)}, dps40 = {mp.nstr(f40, 8)};  Z_DH (re, im) dps20 = {mp.nstr(zz20[0], 4)}, {mp.nstr(zz20[1], 2)}; dps40 = {mp.nstr(zz40[0], 4)}, {mp.nstr(zz40[1], 2)}")
# accuracy of mp.zeta(s, a) itself at dps 20 vs 40 at s = 1/2 + 120i and 0.8 + 85.7i
for s in (mp.mpc(0.5, 120), mp.mpc(0.8, 85.7), mp.mpc(0.5, 60)):
    mp.mp.dps = 20; v20 = dh.f_dh(s)
    mp.mp.dps = 40; v40 = dh.f_dh(s)
    print(f"f_DH({mp.nstr(s, 6)}): dps20 {mp.nstr(v20, 12)}  dps40 {mp.nstr(v40, 12)}  |diff| = {mp.nstr(abs(v20 - v40), 3)}")
