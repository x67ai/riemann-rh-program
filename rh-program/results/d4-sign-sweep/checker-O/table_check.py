#!/usr/bin/env python3
"""D4 Job 2 part C.1 (Opus 5): (i) every SHA-256 in hashes.txt against the file on disk; (ii) every row of the note's section 6
against out/zeta_*.json, out/control1_*.json, the replay JSONs, out/planted_*, out/dhreg_*; (iii) the counts and the ladder.
Independent of harness/d4_note_table.py: printed numbers are parsed and compared to the JSON value within half a unit of the last
printed digit; derived columns (|W1-W2|, tol, W, delta_vis, band, X) are recomputed. Log: logs/table_check_run.log; out/table_check.json."""
import json, os, re, glob, hashlib, math
from decimal import Decimal, getcontext
import mpmath as mp
getcontext().prec = 60; mp.mp.dps = 40
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O = os.path.join(ROOT, 'out')
EPS = 1.0266395604864687e-30; PT = 3000175332800
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
res = dict(hash_mismatch=[], hash_superseded=[], hash_missing=[], row_issues=[], counts={})
# (i)
print('== (i) hashes.txt ==')
ent = []
for n, l in enumerate(open(os.path.join(ROOT, 'hashes.txt')).read().splitlines(), 1):
    if not l.strip() or l.startswith('#'): continue
    h, rest = l.split(None, 1); path = rest.split(' (')[0].strip()
    ent.append((n, h, path, rest))
last = {}
for n, h, p, r in ent: last[p] = (n, h)
ok = 0
for n, h, p, r in ent:
    fp = os.path.join(ROOT, p)
    if not os.path.exists(fp): res['hash_missing'].append((n, p)); continue
    d = sha(fp)
    if d == h: ok += 1
    elif last[p][0] != n: res['hash_superseded'].append((n, p, h[:16], 'later entry line %d' % last[p][0], 'later entry matches' if last[p][1] == d else 'LATER ENTRY ALSO DIFFERS'))
    else: res['hash_mismatch'].append((n, p, h[:16], d[:16]))
print(f'entries {len(ent)}, distinct paths {len(last)}; match {ok}; MISMATCH (latest entry for its path) {len(res["hash_mismatch"])}: {res["hash_mismatch"]}')
print(f'missing files: {res["hash_missing"]}')
print(f'superseded earlier entries (the same path re-hashed later in the file): {len(res["hash_superseded"])}')
for s in res['hash_superseded']: print('   ', s)
note_sha = sha(os.path.join(ROOT, 'd4-sweep-note.md')); print('the note on disk', note_sha, '| listed in hashes.txt:', any(p == 'd4-sweep-note.md' and h == note_sha for n, h, p, r in ent))
# (ii)
print('== (ii) section 6 rows ==')
note = open(os.path.join(ROOT, 'd4-sweep-note.md')).read()
tab = note[note.index('<!-- S6-TABLE-BEGIN -->'):note.index('<!-- S6-TABLE-END -->')]
rows = [l for l in tab.splitlines() if l.startswith('| ') and not l.startswith('| #') and not l.startswith('|---')]
plan = json.load(open(os.path.join(ROOT, 'harness', 'sweep_plan.json'))); kof = {p['t_exact']: p['k'] for p in plan['tier1']}
cmpA = json.load(open(os.path.join(HERE, 'out', 'compare.json')))
def agrees(s, v, slack=0.5000001):
    s = s.strip().replace('**', '')
    m = re.fullmatch(r'([+-]?)(\d+)(?:\.(\d+))?(?:e([+-]?\d+))?', s)
    if not m: return None
    x = float(s); nd = len(m.group(3) or ''); ex = int(m.group(4) or 0)
    return abs(x - v) <= slack * 10.0 ** (ex - nd) + 1e-300
def lsign(t): return 22.4 * (math.log(t) / math.log(1e6)) ** (1 / 3)
issues = []; seen = set(); wmax = (0, None)
for line in rows:
    c = [x.strip() for x in line.strip().strip('|').split(' | ')]
    if len(c) != 20: issues.append(('column count', len(c), line[:60])); continue
    lab, t, L = c[0], c[1], float(c[2]); Lg = f'{L:g}'
    pj = os.path.join(O, f'zeta_t{t}_L{Lg}.json'); J = json.load(open(pj)); seen.add((t, Lg))
    c1p = os.path.join(O, f'control1_t{t}_L{Lg}.json')
    if os.path.exists(c1p):
        C = json.load(open(c1p)); rp = os.path.join(ROOT, C['replay_json']); RJ = json.load(open(rp))
        P2, W2, wall2 = RJ['P'], RJ['W'], C['replay_wall_s']
        if C['P_replay'] != P2 or C['W_replay'] != W2: issues.append((t, Lg, 'control1 JSON P/W differ from the replay JSON it names'))
        if C['replay_json_sha256'] != sha(rp): issues.append((t, Lg, 'control1 replay_json_sha256 != replay file on disk'))
        if C['job1_json_sha256'] != sha(pj): issues.append((t, Lg, 'control1 job1_json_sha256 != zeta JSON on disk'))
        if C['twsumO_sha256'] != 'd57080a8eeee7da8e59322df2446c976a3b8ee64a18cf6064975dced489d0f45': issues.append((t, Lg, 'twsumO hash in control1'))
        if RJ['n_terms'] != J['n_terms']: issues.append((t, Lg, 'term counts differ', RJ['n_terms'], J['n_terms']))
    else:
        r = [r for r in cmpA if r['job1_source'].endswith(os.path.basename(pj))]
        if len(r) != 1: issues.append((t, Lg, 'no control1 and no compare.json row')); continue
        r = r[0]; rp = os.path.join(HERE, r['checkerO_json']); RJ = json.load(open(rp)); P2, W2, wall2 = RJ['P'], RJ['W'], None
    tf = int(t)
    # label
    explab = ('PT edge' if tf == 3000175332900 else 'rehearsal') if J.get('tier') == 'rehearsal' else (f'k={kof[t]}' if t in kof else ('control' if 'control' in (J.get('label') or '') else str(J.get('tier'))))
    chk = []
    chk.append(('label', lab == explab or (lab == 'rehearsal' and explab in ('rehearsal', 'PT edge')), lab, explab))
    chk.append(('t', J['t_exact'] == t, t, J['t_exact']))
    chk.append(('X', int(c[3]) == J['X'] == int(mp.floor(mp.exp(mp.mpf(c[2])))), c[3], J['X']))
    chk.append(('terms', int(c[4]) == J['n_terms'] == RJ['n_terms'], c[4], J['n_terms']))
    chk.append(('P1', agrees(c[5], J['P_dd']), c[5], J['P_dd']))
    chk.append(('P2', agrees(c[6], P2), c[6], P2))
    chk.append(('ARCH', agrees(c[7], J['ARCH']), c[7], J['ARCH']))
    chk.append(('W1', agrees(c[8], J['W']), c[8], J['W']))
    chk.append(('W1 = pole + ARCH - P1', abs(J['pole'] + J['ARCH'] - J['P_dd'] - J['W']) <= 1e-17, J['pole'] + J['ARCH'] - J['P_dd'], J['W']))
    chk.append(('W2', agrees(c[9], W2), c[9], W2))
    dW = abs(J['W'] - W2); wmax = max(wmax, (dW, (t, Lg)))
    chk.append(('|W1-W2| recomputed', agrees(c[10], dW), c[10], dW))
    tol = 1e-10 + EPS * tf * J['l1_norm']
    chk.append(('tol = 1e-10 + eps_proven t l1', agrees(c[11], tol) or (J.get('tier') == 'rehearsal' and agrees(c[11], 1e-10)), c[11], tol))
    chk.append(('Control 1 PASS', dW <= tol, dW, tol))
    chk.append(('phase line', agrees(c[12], J['phase_line']), c[12], J['phase_line']))
    b = J['budget']
    chk.append(('budget', agrees(c[13], b['total']), c[13], b['total']))
    chk.append(('budget total = sum of lines', abs(sum(v for k, v in b.items() if k != 'total') - b['total']) <= 1e-12 * b['total'], sum(v for k, v in b.items() if k != 'total'), b['total']))
    m = re.fullmatch(r'([\d.]+) \[([\d.]+), ([\d.]+)\]', c[14])
    dv = 0.1 * (lsign(tf) / L) ** 1.5
    chk.append(('delta_vis printed = JSON', m and agrees(m.group(1), J['delta_vis']), c[14], J['delta_vis']))
    chk.append(('delta_vis recomputed from the law', abs(dv - J['delta_vis']) <= 1e-12, dv, J['delta_vis']))
    chk.append(('band = delta/1.837, delta*1.837', m and agrees(m.group(2), J['delta_vis_band_factor_1p5'][0]) and agrees(m.group(3), J['delta_vis_band_factor_1p5'][1]) and abs(J['delta_vis_band_factor_1p5'][1] / J['delta_vis'] - 1.5 ** 1.5) < 1e-12 and abs(J['delta_vis'] / J['delta_vis_band_factor_1p5'][0] - 1.5 ** 1.5) < 1e-12, c[14], J['delta_vis_band_factor_1p5']))
    c2 = J['control2_zero_side']; pf = os.path.join(O, c2['json']) if c2.get('json') else None
    m2 = re.fullmatch(r'(\S+) / (\S+) \((\S+), (PASS|FAIL)\)', c[15])
    chk.append(('Control 2 printed = JSON', bool(m2) and agrees(m2.group(1), c2['kernel_value']) and agrees(m2.group(2), c2['expected']) and agrees(m2.group(3), c2['rel_diff']) and (m2.group(4) == 'PASS') == bool(c2['pass_']), c[15], (c2['kernel_value'], c2['expected'], c2['rel_diff'])))
    if pf and os.path.exists(pf):
        PF = json.load(open(pf))
        chk.append(('Control 2 = planted_* file', PF['pair_kernel_re'] == c2['kernel_value'] and PF['expected'] == c2['expected'] and PF['pass_'] and abs(PF['delta'] - J['delta_vis']) < 1e-15, pf[-50:], (PF['pair_kernel_re'], PF['expected'])))
    else: chk.append(('Control 2 planted_* file exists', False, c2.get('json'), None))
    dh = J['control2_coefficient_side_DH']; df = os.path.join(O, dh['json']) if dh.get('json') else None
    if df and os.path.exists(df):
        DF = json.load(open(df))
        chk.append(('DH = dhreg_* file, P within 1e-12, W < 0', DF['P_dd'] == dh['P'] and abs(DF['P_dd'] - 0.339995468928925) <= 1e-12 and dh['W'] < 0 and abs(dh['arch'] - DF['P_dd'] - dh['W']) < 1e-16 and c[16] == 'FIRES, PASS', c[16], (DF['P_dd'], dh['W'])))
    else: chk.append(('DH dhreg_* file exists', False, dh.get('json'), None))
    m3 = re.fullmatch(r'(\S+) / (\S+)', c[17])
    chk.append(('wall sum', bool(m3) and agrees(m3.group(1), J['time_sum_s']), c[17], J['time_sum_s']))
    chk.append(('wall replay', bool(m3) and ((m3.group(2) == '—' and wall2 is None) or (wall2 is not None and agrees(m3.group(2), wall2))), c[17], wall2))
    h1, h2 = [x.strip() for x in c[18].split('/')]
    chk.append(('hash JSON1', h1 == sha(pj)[:8], h1, sha(pj)[:8]))
    chk.append(('hash JSON2', h2 == sha(rp)[:8], h2, sha(rp)[:8]))
    chk.append(('verdict', c[19] == J['verdict'] == ('silent (W > 0)' if J['W'] > 0 else 'x'), c[19], J['verdict']))
    for name, good, a, bb in chk:
        if not good: issues.append((lab, t, Lg, name, str(a)[:80], str(bb)[:80]))
print(f'rows parsed {len(rows)}; checks per row {len(chk)}; issues {len(issues)}')
for i in issues: print('  ISSUE', i)
print(f'max |W1 - W2| over the 133 rows (recomputed from the replay JSONs): {wmax[0]:.3e} at {wmax[1]}')
res['row_issues'] = issues
# (iii)
print('== (iii) counts ==')
Z = [p for p in glob.glob(os.path.join(O, 'zeta_t*_L*.json')) if not p.endswith('.sidecar.json')]
Js = [json.load(open(p)) for p in Z]
reh = [J for J in Js if J.get('tier') == 'rehearsal' and int(J['t_exact']) != 3000175332900]
sw = [J for J in Js if J not in reh]
n22 = sum(J['L'] == 22 for J in sw); n28 = sum(J['L'] == 28.35 for J in sw)
above = sum(int(J['t_exact']) > PT for J in sw); at = sum(int(J['t_exact']) == PT for J in sw); below = sum(int(J['t_exact']) < PT for J in sw)
norow = [(J['t_exact'], J['L']) for J in Js if (J['t_exact'], '%g' % J['L']) not in seen]
print(f'zeta JSONs {len(Js)} = rehearsal {len(reh)} + sweep {len(sw)}; sweep at L = 22: {n22}, at L = 28.35: {n28}; strictly above PT {above}, at PT {at}, below {below}; rows in section 6 {len(rows)}; JSONs without a row: {norow}')
print('control1 JSONs', len(glob.glob(os.path.join(O, 'control1_*.json'))), '| replayO JSONs', len(glob.glob(os.path.join(O, 'replayO_*.json'))), '| planted', len(glob.glob(os.path.join(O, 'planted_*.json'))), '| dhreg', len(glob.glob(os.path.join(O, 'dhreg_*.json'))))
print('all sweep W > 0:', all(J['W'] > 0 for J in sw), '| all verdict silent:', all(J['verdict'] == 'silent (W > 0)' for J in sw), '| all controls_pass:', all(J['controls_pass'] for J in sw), '| any stop_line:', [J['stop_line'] for J in sw if J.get('stop_line')])
bad = []; maxrel = 0; maxulp = 0
for k in range(121):
    ex = round(Decimal(PT) * (Decimal(10) ** (Decimal(k) / 16))); dbl = int(float(ex)); pl = int(plan['tier1'][k]['t_exact'])
    if dbl != pl:
        bad.append(k); maxrel = max(maxrel, abs(pl - int(ex)) / int(ex))
        maxulp = max(maxulp, abs(pl - dbl) / max(1, math.ulp(float(dbl))))
    fl = int(float(round(PT * 10 ** (k / 16))))
    assert fl == pl, (k, fl, pl)
print(f'ladder: the plan heights equal float(round(PT * 10**(k/16))) evaluated in double arithmetic (d4_plan.py line 64) for all 121; they equal the double nearest round(PT*10^(k/16)) computed exactly for {121 - len(bad)}/121; differ at k = {bad}; max relative difference {maxrel:.2e}, max {maxulp:.0f} ulp (below 2^53: units)')
res['counts'] = dict(zeta=len(Js), rehearsal=len(reh), sweep=len(sw), L22=n22, L2835=n28, above_PT=above, at_PT=at, rows=len(rows), ladder_exact_mismatch=bad)
json.dump(res, open(os.path.join(HERE, 'out', 'table_check.json'), 'w'), indent=1, default=str)
