"""Table row for pencil k from ../data/k{k}-zeros.json, ../data/q3-k{k}.json, ../data/k{k}-track.json."""
import sys, json
import mpmath as mp
mp.mp.dps = 30
k = int(sys.argv[1]); tr = sys.argv[2] if len(sys.argv) > 2 else '../data/k%d-track.json' % k
Z = json.load(open('../data/k%d-zeros.json' % k)); Q = json.load(open('../data/q3-k%d.json' % k)); T = json.load(open(tr))
X = Z['X']
row = dict(k=k, X=round(X, 3), Y=Z['Y_k'])
row['AP_total_Xik'] = Z['total_%d' % k]; row['AP_total_Xik1'] = Z['total_%d' % (k + 1)]
row['nonreal_in_W_Xik'] = Z['nonreal_in_W_%d' % k]; row['nonreal_in_W_Xik1'] = Z['nonreal_in_W_%d' % (k + 1)]
row['real_in_W_Xik_AP'] = Z['real_in_W_%d' % k]; row['real_in_W_Xik1_AP'] = Z['real_in_W_%d' % (k + 1)]
row['q3_real_t0_to_Xplus12'] = Q['real_zeros_t0']; row['q3_real_t1_to_Xplus12'] = Q['real_zeros_t1']
row['q3_min_in01'] = Q['min_in01']
q3max = [e for e in Q['extrema_in01'] if e['type'] == 'max']
lands, ends_in, ends_out, other, entered = [], [], [], [], []
worst = None; pos = []
nr1 = [mp.mpc(a, b) for a, b in Z['nonreal_%d' % (k + 1)]]
for br in T['branches']:
    s = mp.mpc(*br['start']); inside = mp.re(s) <= X
    w = br['worst_increase_Im']
    if inside and w is not None and (worst is None or w > worst[0]): worst = (w, br['start'])
    if inside: pos += [(t, br['start']) for t in br['grid_pos_imdzdt']]
    if br['status'] == 'axis-approach' and br['landing'] and br['landing']['found']:
        L = br['landing']; xs = float(L['x_star'])
        (lands if xs <= X else ends_out).append(dict(start=br['start'], x_star=L['x_star'], tau_star=L['tau_star'],
              tau_c=L['tau_c'], z_c=L['z_c'], model_im=L['im_model_at_c'], ok=L['uc_gt_ustar']))
        if not inside and xs <= X: entered.append(br['start'])
    elif br['status'] == 'end-t1':
        e = mp.mpc(*br['end_t1'])
        d = min(abs(e - z) for z in nr1) if nr1 else 1e9
        rec = dict(start=br['start'], end=br['end_t1'], match_dist=float(d))
        if mp.re(e) <= X:
            ends_in.append(rec)
            if not inside: entered.append(br['start'])
        else:
            if inside: ends_out.append(rec)
    else:
        other.append(dict(start=br['start'], status=br['status'], last=br['last']))
row['landings'] = sorted(lands, key=lambda d: float(d['x_star']))
row['n_landings'] = len(lands); row['n_nonreal_ends_in_W'] = len(ends_in)
row['exits'] = ends_out; row['entered'] = entered; row['other'] = other
row['worst_increase_Im'] = worst; row['grid_pos_imdzdt'] = pos
row['q3_max_in01_to_X'] = [(e['x'], e['S']) for e in q3max if float(e['x']) <= X]
row['max_match_dist'] = max([r['match_dist'] for r in ends_in] or [0])
json.dump(row, open('../data/k%d-row.json' % k, 'w'), indent=1)
print(json.dumps(row, indent=1)[:5000])
