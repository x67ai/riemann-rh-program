"""Joint-kernel multi-pair ledger:
  coupling(p,q) = 4 m_p m_q Phi(d_p,d_q; x),  Phi = R_{d+d'} + R_{|d-d'|}
  nu_joint(d,d') = sum_cells sup_cell [-(Phi)]_+
  Sgen2(d;Y) = [8 nu(d) + 4 sup_{d'<=Y} nu_joint(d,d')] / (2 abar(2d)^2)
Search the largest Y with sup_{d<=Y} Sgen2 <= 1.
Also deep-tail crossing for abar(2y) >= sqrt(260) abar(y).
"""
import numpy as np
from pairchan_core import N, abar, psiN

Delta = N / 65.0
xs = np.linspace(0, N, 12001, endpoint=False)
cell_idx = np.floor((xs / Delta) + 0.5).astype(int) % 65

def Rfun(y):
    if y < 1e-9:
        return np.array([abs(psiN(x)) ** 2 * np.sign(1) for x in xs])  # R_0 = psi^2
    return np.array([(psiN(x + 1j * y) ** 2).real for x in xs])

Rcache = {}
def R(y):
    key = round(y, 4)
    if key not in Rcache:
        Rcache[key] = Rfun(key)
    return Rcache[key]

def nu_of(arr):
    return sum(max(0.0, float(np.max(-arr[cell_idx == k]))) for k in range(65))

dgrid = np.round(np.arange(0.004, 0.1641, 0.004), 4)

def check_Y(Y):
    worst, wd, wdp = 0.0, None, None
    ds = [d for d in dgrid if d <= Y + 1e-12]
    for d in ds:
        nu_d = nu_of(R(d))
        sup_j = 0.0
        sup_dp = None
        for dp in ds:
            arr = R(round(d + dp, 4)) + R(round(abs(d - dp), 4))
            nj = nu_of(arr)
            if nj > sup_j:
                sup_j, sup_dp = nj, dp
        val = (8 * nu_d + 4 * sup_j) / (2 * abar(2 * d) ** 2)
        if val > worst:
            worst, wd, wdp = val, d, sup_dp
    return worst, wd, wdp

for Y in (0.150, 0.156, 0.1592, 0.162):
    w, d, dp = check_Y(Y)
    print(f"Y = {Y:6.4f}: sup Sgen2 = {w:.4f} at d = {d}, worst d' = {dp}  "
          f"{'OK' if w <= 1 else 'FAIL'}")

# deep-tail crossing: smallest y with abar(2y)/abar(y) >= sqrt(260)
import numpy as np
target = np.sqrt(260)
for y in np.arange(1.0, 1.35, 0.05):
    print(f"y={y:.2f}: abar(2y)/abar(y) = {abar(2*y)/abar(y):.3f} (target {target:.3f})")
