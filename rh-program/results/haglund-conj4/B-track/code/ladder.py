"""B-track ladder (BRIEF-B-track 'Ladder first'). Writes ../data/ladder.json and prints a log."""
import sys, json, time
sys.path.insert(0, '.')
import mpmath as mp, hb
out = {}
def log(*a):
    print(*a); sys.stdout.flush()

# L0: mpmath.gammainc against own continued fraction / series at large complex first argument
mp.mp.dps = 40
pts = [(mp.mpc(2.25,10.3), mp.pi), (mp.mpc(1.25,-50), 4*mp.pi), (mp.mpc(-17.75,170), 36*mp.pi),
       (mp.mpc(1.55,1572), 729*mp.pi), (mp.mpc(2.25,1572), 784*mp.pi), (mp.mpc(-30,400), 25*mp.pi),
       (mp.mpc(0.25+30,-169), 49*mp.pi), (mp.mpc(-49.75,412), 196*mp.pi)]
L0 = []
for w, a in pts:
    m = mp.gammainc(w, a); c, j = hb.gup_cf(w, a); s, k, canc = hb.gup_ser(w, a)
    r = dict(w=str(w), a=str(a), rel_mp_cf=float(abs(m-c)/abs(c)), rel_ser_cf=float(abs(s-c)/abs(c)), ser_canc_bits=canc, cf_terms=j)
    L0.append(r); log('L0', r)
out['L0'] = L0

# L1: Haglund's appendix zeros of Xi_1 (25 digits) -- Newton at dps 40 on Phi_1 by (14) and by the relation form
H = [('14.04543957882981756479858','0'),('20.62534600592171760132974','2.697151842339519632505712'),
 ('26.05616693357829946749575','7.125359707612690330897455'),('31.50143137824977099308422','10.72915037105496782822450'),
 ('36.72702276874255239918647','13.75961410603683555833019'),('41.73703479849622101486046','16.44012737324329251859479'),
 ('46.56622866997881255099908','18.88186965378958902053812'),('51.24456582311629453468990','21.14750420601374895347492'),
 ('55.79525368022472028456165','23.27625685820891335493023'),('60.23621426525993802296865','25.29458549895993860216014'),
 ('64.58150497097301796850798','27.22133555778112035831075'),('68.84235653395121330563843','29.07049609150585601287785'),
 ('73.02789933182939276748060','30.85279227139366634464017'),('77.14567324003250763696303','32.57666324204392832752644'),
 ('81.20199121212953110713480','34.24889253114939152723783'),('85.20220345212231662722890','35.87503096670553315342957'),
 ('89.15089297349449318064800','37.45968995259880236581690'),('93.05202292717284600209187','39.00675061925213970478000'),
 ('96.90904939663401491219210','40.51951660155401879741380')]
mp.mp.dps = 40
L1 = []
for re_, im_ in H:
    zH = mp.mpc(re_, im_)
    z1, st, it, d = hb.newton(lambda z: hb.Phi(1, z), zH)
    z2, st2, it2, d2 = hb.newton(lambda z: hb.XiN(1, z), zH)
    r = dict(zH=re_+'+'+im_+'i', dist_eq14=float(abs(z1-zH)), dist_routeT=float(abs(z2-zH)), eq14_vs_T=float(abs(z1-z2)))
    L1.append(r); log('L1', r)
out['L1'] = L1

# L2: largest real zeros of Xi_1..Xi_4 (Haglund p. 4 table), literal sum at dps 60 and route T at dps 30
tab = {1:'14.0454395788', 2:'39.5324810798', 3:'65.0320737720', 4:'103.3679880094'}
L2 = []
for N, v in tab.items():
    x0 = mp.mpf(v)
    mp.mp.dps = 30
    xT = hb.bisect_real(lambda x: hb.XiN(N, x), x0 - mp.mpf('1e-6'), x0 + mp.mpf('1e-6'))
    mp.mp.dps = 60
    xL = hb.bisect_real(lambda x: mp.re(hb.XiN_lit(N, x)), x0 - mp.mpf('1e-6'), x0 + mp.mpf('1e-6'))
    r = dict(N=N, table=v, routeT=mp.nstr(xT, 16), literal60=mp.nstr(xL, 16), diff_table=float(abs(xL - x0)), T_vs_lit=float(abs(xT - xL)))
    L2.append(r); log('L2', r)
out['L2'] = L2
json.dump(out, open('../data/ladder.json', 'w'), indent=1)
log('saved L0-L2')
