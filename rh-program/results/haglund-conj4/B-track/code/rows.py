"""per-branch markdown rows for pencil k: python3 rows.py track.json X > rows.md"""
import sys, json
T = json.load(open(sys.argv[1])); X = float(sys.argv[2])
print('| # | start z (t=0) | end | x* | tau* | worst dIm | #grid Im(dz/dt)>0 | grid pts |')
print('|---|---|---|---|---|---|---|---|')
for i, b in enumerate(T['branches']):
    s = '%.6f + %.6fi' % (float(b['start'][0]), float(b['start'][1]))
    out = '' if float(b['start'][0]) <= X else ' (start outside W)'
    xs = ts = ''
    if b['status'] == 'axis-approach' and b.get('landing') and b['landing'].get('found'):
        L = b['landing']; e = 'landed'; xs = '%.6f' % float(L['x_star']); ts = '%.5f' % L['tau_star']
        if float(L['x_star']) > X: e += ' (outside W)'
    elif b['status'] == 'end-t1':
        e = 'Xi_k+1 zero %.6f + %.6fi' % (float(b['end_t1'][0]), float(b['end_t1'][1]))
        if float(b['end_t1'][0]) > X: e += ' (outside W)'
    else:
        e = b['status'] + ' at tau=%s' % b['last']['tau']
    w = b['worst_increase_Im']
    print('| %d | %s%s | %s | %s | %s | %s | %d | %d |' % (i, s, out, e, xs, ts, ('%.3e' % w) if w is not None else '-',
          len(b['grid_pos_imdzdt']), b['n_grid']))
