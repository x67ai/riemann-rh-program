"""Unit fejer-form-s39: which Fejer kernel sees V (t = 5) and which sees t = -5 over F_5 (NOTE §3, one-sidedness).
K_M = 1 + 2 sum_{n<=M} (1 - n/(M+1)) cos(n theta) (untwisted, all coefficients >= 0); twisted = K_M(theta + pi)."""
import json
Z = json.load(open('r1_zeta_data.json'))
for r in Z['5']:
    if r['g'] == 1 and r['t'] in (5, -5):
        p = [r['s'][n] / 5**(n / 2) for n in range(1, 9)]
        un = [round(1 + sum((1 - n / (M + 1)) * p[n - 1] for n in range(1, M + 1)), 4) for M in range(1, 9)]
        tw = [round(1 + sum((1 - n / (M + 1)) * (-1)**n * p[n - 1] for n in range(1, M + 1)), 4) for M in range(1, 9)]
        print('t=', r['t'], 'untwisted K_M, M=1..8:', un); print('     twisted  K_M(.+pi):', tw)
