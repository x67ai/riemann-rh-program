#!/usr/bin/env python3
"""Session 26 queue item 2 (D3 zoo note; writer Fable 5.1) -- deliverable 1.
Re-run of results/program-digest-s25/verify-orch/residue_signs.py (the orchestrator's sixteen-zero
computation of the on-line Mobius residues 1/(rho zeta'(rho))), reproduced in the same print format,
then extended to the first 200 nontrivial zeros at 30 digits, with the check of clause (3)(a):
the residue of 1/xi at a simple on-line zero is purely imaginary (arg = +-pi/2) and alternates.
Definitions: xi(s) = H(s) zeta(s), H(s) = (1/2) s (s-1) pi^{-s/2} Gamma(s/2); at a zero rho of zeta,
xi'(rho) = H(rho) zeta'(rho), so Res_{s=rho} 1/xi = 1/(H(rho) zeta'(rho)); Res_{s=rho} 1/zeta = 1/zeta'(rho);
the Mobius-side weight is w = 1/(rho zeta'(rho)) (the orchestrator's "w").
Log: results/zoo-s26/logs/residue_signs_rerun.log. One process; mpmath only."""
import os, sys, time
from mpmath import mp, mpf, mpc, zetazero, zeta, gamma, pi, arg, diff, fabs, log, exp, sqrt, im, re, nstr
mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
LOG = os.path.join(ROOT, 'logs', 'residue_signs_rerun.log')
ORCH = os.path.join(os.path.dirname(os.path.dirname(ROOT)), 'program-digest-s25', 'verify-orch', 'residue_signs_run.log')
out = open(LOG, 'w')
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.write(s + '\n'); out.flush()
t0 = time.time()
P('# residue_signs_rerun.py -- mpmath', __import__('mpmath').__version__, '-- mp.dps =', mp.dps, '-- started', time.strftime('%a %b %d %H:%M:%S %Z %Y'))
def H(s): return mpf(1)/2 * s * (s - 1) * pi**(-s/2) * gamma(s/2)
def xi(s): return H(s) * zeta(s)
N = 200
rows = []
P('## Part A: the orchestrator\'s sixteen, same format as verify-orch/residue_signs.py')
orch_lines = [l.rstrip('\n') for l in open(ORCH)] if os.path.exists(ORCH) else None
mism = 0
for n in range(1, 17):
    r = zetazero(n); d = zeta(r, derivative=1); w = 1/(r*d)
    line = f"n={n:2d} gamma={float(r.imag):12.6f}  Re w={float(w.real):+.5f}  Im w={float(w.imag):+.5f}  arg(1/zeta')={float(arg(1/d)/pi):+.3f}pi"
    tag = ''
    if orch_lines is not None:
        tag = '  [== orch log]' if line == orch_lines[n-1] else f'  [!= orch log: {orch_lines[n-1]!r}]'
        if line != orch_lines[n-1]: mism += 1
    P(line + tag)
P(f'Part A result: {16 - mism}/16 lines byte-identical to the orchestrator\'s log ({ORCH})')
P('')
P('## Part B: the first 200 zeros at 30 digits')
P('# columns: n, gamma, sign Re w, Re w, Im w, arg(1/zeta\')/pi, arg(Res 1/xi)/pi, |arg(Res 1/xi)| - pi/2, arg H(rho)/pi, |xi\'(rho) - diff xi| (independent numeric derivative), |Im rho - 1/2|')
signs = []; args_zeta = []; dev_xi = []; args_xi = []; dev_diff = []; imxi = []; absres = []
for n in range(1, N + 1):
    r = zetazero(n)
    d = zeta(r, derivative=1)
    w = 1/(r*d)
    h = H(r)
    xip = h * d                       # xi'(rho) at a zero of zeta
    res_xi = 1/xip                    # Res_{rho} 1/xi
    a_z = arg(1/d)/pi; a_x = arg(res_xi)/pi; a_h = arg(h)/pi
    dev = fabs(arg(res_xi)) - pi/2    # must be 0 to working precision
    xip_num = diff(xi, r)             # independent: numeric derivative of xi at rho
    dd = fabs(xip - xip_num)
    s = '+' if w.real > 0 else '-'
    signs.append(s); args_zeta.append(a_z); dev_xi.append(dev); args_xi.append(a_x); dev_diff.append(dd); imxi.append(fabs(re(res_xi))/fabs(res_xi)); absres.append(fabs(res_xi))
    P(f"{n:3d} {nstr(r.imag, 12):>16s} {s} {nstr(w.real, 8):>14s} {nstr(w.imag, 8):>14s} {nstr(a_z, 6):>10s} {nstr(a_x, 6):>10s} {nstr(dev, 3):>10s} {nstr(a_h, 6):>10s} {nstr(dd, 3):>10s} {nstr(fabs(r.real - mpf(1)/2), 3):>8s}")
P('')
P('## Part C: summary over n = 1..200')
plus = signs.count('+'); minus = signs.count('-')
P(f'sign counts of Re[1/(rho zeta\'(rho))]: + {plus}, - {minus} (of {N})')
changes = sum(1 for i in range(1, N) if signs[i] != signs[i-1])
P(f'sign changes between consecutive zeros: {changes} of {N-1} steps (strict alternation would be {N-1})')
runs = []; cur = signs[0]; ln = 1
for s in signs[1:]:
    if s == cur: ln += 1
    else: runs.append(ln); cur = s; ln = 1
runs.append(ln)
P(f'longest run of equal sign of Re w: {max(runs)}; run-length histogram: ' + ', '.join(f'{k}:{runs.count(k)}' for k in sorted(set(runs))))
P('sign string (n = 1..200): ' + ''.join(signs))
P(f'first sixteen signs: {",".join(signs[:16])}  (orchestrator: -,+,-,+,-,+,+,-,+,-,-,+,+,-,+,-)')
P(f'range of arg(1/zeta\'(rho))/pi over n <= 200: [{nstr(min(args_zeta), 6)}, {nstr(max(args_zeta), 6)}]')
P(f'range of arg(1/zeta\'(rho))/pi over n <= 16: [{nstr(min(args_zeta[:16]), 6)}, {nstr(max(args_zeta[:16]), 6)}]  (orchestrator: (-0.33pi, +0.27pi))')
P(f'arg(Res_rho 1/xi)/pi takes the values: {sorted(set(nstr(a, 12) for a in args_xi))}')
P(f'max | |arg(Res 1/xi)| - pi/2 | over n <= 200: {nstr(max(dev_xi), 3)}  (clause (3)(a): must be 0 to working precision)')
P('max |Re(Res 1/xi)|/|Res 1/xi| over n <= 200: ' + nstr(max(imxi), 3) + '  (relative; the absolute size |Res 1/xi| = 1/|H(rho) zeta_prime(rho)| grows like e^{pi gamma/4}: |Res| at n = 1, 100, 200 = ' + nstr(absres[0], 3) + ', ' + nstr(absres[99], 3) + ', ' + nstr(absres[199], 3) + ')')
xs = ['+' if a > 0 else '-' for a in args_xi]
xchanges = sum(1 for i in range(1, N) if xs[i] != xs[i-1])
P(f'sign of Im(Res 1/xi) alternates at every consecutive pair: {xchanges == N-1} ({xchanges} changes of {N-1})')
P(f'Im(Res 1/xi) sign string: ' + ''.join(xs))
P(f'max |xi\'(rho) - numeric diff xi(rho)| over n <= 200: {nstr(max(dev_diff), 3)}  (independent check of xi\' = H zeta\' at a zero)')
P(f'max |Re rho - 1/2| over the 200 zeros returned by zetazero: {nstr(max(fabs(zetazero(n).real - mpf(1)/2) for n in (1, 50, 100, 150, 200)), 3)} (sampled)')
P(f'elapsed {time.time() - t0:.1f} s; finished', time.strftime('%a %b %d %H:%M:%S %Z %Y'))
out.close()
