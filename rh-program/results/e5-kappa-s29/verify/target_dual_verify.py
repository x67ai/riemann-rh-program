#!/usr/bin/env python3
"""target_dual_verify.py -- re-verify a saved plain-dual certificate (target_dual_s_config{ci}.npy) with an escalating repair eta.
Usage: python3 target_dual_verify.py <ci> <hu> <d> [T_v]"""
import numpy as np, sys, json
from scipy.special import digamma
from kappa_pipeline import *
LOGPI = np.log(np.pi)
def a_fn(tau):
    tau = np.asarray(tau, float); z = 0.5j*tau
    return (np.real((1 - 1j*tau)*digamma(0.5 + z) + 1j*tau*digamma(1.0 + z)) - 1.0 - LOGPI)/(2*np.pi)
ci = int(sys.argv[1]); hu = float(sys.argv[2]); d = float(sys.argv[3]); T_v = float(sys.argv[4]) if len(sys.argv) > 4 else 1000.0
s = np.load(f"target_dual_s_config{ci}.npy")
for eta in (2e-5, 5e-5, 2e-4, 8e-4, 3.2e-3):
    v = verify_dual(a_fn, lambda T: 0.377896*1.05, lambda T: float(a_fn(T)), s, d, hu, eta=eta, c_rep=1.0, T_v=T_v, h0=0.01)
    print(f"config {ci}: eta = {eta}: ok = {v['ok']}, kappa_cert = {v['kappa_cert']}")
    if v["ok"]:
        json.dump(dict(ci=ci, hu=hu, d=d, eta=eta, kappa_cert=v["kappa_cert"], verify=v), open(f"target_dual_verify_config{ci}.json", "w"), indent=1); break
