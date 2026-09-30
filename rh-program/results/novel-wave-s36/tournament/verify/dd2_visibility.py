"""DD2 visibility law: |min eigenvalue| / max eigenvalue of the Pick kernel for DH versus the height
offset D between the sampling circle (center 1.5 + i(gamma - D), radius r, n = 24) and DH's off-line zero."""
import mpmath as mp
from dd2_pick_kernel import F_dh, eig_range
mp.mp.dps = 90
gam = mp.mpf('85.699348')
for r in (mp.mpf('0.3'), mp.mpf('0.45')):
    for D in (0, 1, 2.5, 5, 7.5, 10):
        E = eig_range(F_dh, mp.mpf('1.5') + 1j * (gam - D), r, 24)
        ratio = -E[0] / E[-1]
        print(f"r={mp.nstr(r,3)} D={D:5}: min={mp.nstr(E[0], 5)}  max={mp.nstr(E[-1], 5)}  "
              f"-min/max={mp.nstr(ratio, 5)}  log10={mp.nstr(mp.log10(abs(ratio)), 5)}", flush=True)
