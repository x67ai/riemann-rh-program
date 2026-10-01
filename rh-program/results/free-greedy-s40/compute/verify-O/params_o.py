# params_o.py -- t = 1/rho to 80 digits, TFX = round(t * 2^92); my own (Opus reader).
import sys
from mpmath import mp, mpf, pi, nint
mp.dps = 80
name = sys.argv[1]
rho = {'pi4': pi/4, 'pi16': pi/16, 'pi32': pi/32, 'r08': mpf(4)/5}[name]
t = 1/rho
tfx = int(nint(t * mpf(2)**92))
err = abs(mpf(tfx) - t*mpf(2)**92)
assert err <= 0.5
print(tfx, mp.nstr(t, 25), mp.nstr(rho, 25))
