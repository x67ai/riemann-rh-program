# census.py -- A-track P1/P2 driver: for pencil k on the window [xa, xb] x [0, Y]: (a) real counts and non-real zeros of
# Xi_k and Xi_{k+1} with argument-principle checks, (b) every branch from a non-real zero of Xi_k, (c) completeness,
# (d) the real-axis test; hygiene (half-step re-trace of one branch in ten; routes L and T at sample points for k <= 6).
import sys, os, json, math, time
from a_core import *
from axis import scan, Sx
from tracer import trace, newton_S
from zeros import count_sym, count_rect, newton_XiN, march, dedup

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
APPENDIX = [(20.62534600592171760132974, 2.697151842339519632505712), (26.05616693357829946749575, 7.125359707612690330897455),
 (31.50143137824977099308422, 10.72915037105496782822450), (36.72702276874255239918647, 13.75961410603683555833019),
 (41.73703479849622101486046, 16.44012737324329251859479), (46.56622866997881255099908, 18.88186965378958902053812),
 (51.24456582311629453468990, 21.14750420601374895347492), (55.79525368022472028456165, 23.27625685820891335493023),
 (60.23621426525993802296865, 25.29458549895993860216014), (64.58150497097301796850798, 27.22133555778112035831075),
 (68.84235653395121330563843, 29.07049609150585601287785), (73.02789933182939276748060, 30.85279227139366634464017),
 (77.14567324003250763696303, 32.57666324204392832752644), (81.20199121212953110713480, 34.24889253114939152723783),
 (85.20220345212231662722890, 35.87503096670553315342957), (89.15089297349449318064800, 37.45968995259880236581690),
 (93.05202292717284600209187, 39.00675061925213970478000), (96.90904939663401491219210, 40.51951660155401879741380)]

def Xk(k):
    return 2 * math.pi * (k + 2) ** 2 + 30

def log(msg, fh=None):
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)

def zlist(js):
    return [complex(a, b) for a, b in js]

def jl(zs):
    return [[z.real, z.imag] for z in zs]

def subsample(path, nmax=120):
    if len(path) <= nmax:
        return path
    st = len(path) / float(nmax)
    out = [path[int(i * st)] for i in range(nmax)]
    out.append(path[-1])
    return out

def load_seeds(N):
    """non-real zeros of Xi_N known so far (file written by the run for pencil N-1), else Haglund's appendix for N = 1."""
    if N == 1:
        return [complex(a, b) for a, b in APPENDIX]
    p = os.path.join(DATA, "zeros_Xi%d.json" % N)
    if os.path.exists(p):
        return zlist(json.load(open(p))["zeros"])
    return []

def locate(N, xa, xb, route="T"):
    """non-real zeros of Xi_N with real part in [xa, xb] (upper half plane): refine seeds by Newton, march to xb."""
    seeds = load_seeds(N)
    zs = []
    for z in seeds:
        if xa - 20 <= z.real <= xb + 20:
            w, ok = newton_XiN(N, z, route, maxmove=0.5)
            if ok and w.imag > 1e-9:
                zs.append(w)
    zs = dedup(zs)
    zs = march(N, zs, xb + 5, route)
    return zs
