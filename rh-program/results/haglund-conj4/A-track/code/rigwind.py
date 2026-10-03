# rigwind.py -- A-track: the rigorous winding number of hag_core (producer-A, Session 37) for Xi_N on the rectangle
# [-X, X] x [-Y, Y] (counterclockwise corners as exact decimals). Xi_N is even, so the count there is twice the count in
# [0, X] x [-Y, Y] (no zero on the imaginary axis, NOTE C3). Route L (literal sum) on boxes, at working precision prec.
import sys, os, time
from a_core import *
from hag_core import winding

def main(N, X, Y, K0=400, prec=128, maxdepth=14, route="L"):
    ctx.prec = prec
    Xa, Ya = arb(X), arb(Y)
    verts = [acb(-Xa, -Ya), acb(Xa, -Ya), acb(Xa, Ya), acb(-Xa, Ya)]
    if route == "L":
        f = lambda B: XiN_L(N, B)
    else:
        from hag_core import XiN_T
        f = lambda B: XiN_T(N, B, M=N + 8)
    keep = []
    def out(line):
        if ("piece " not in line) or ("FAIL" in line):
            keep.append(line)
            print(line, flush=True)
    t0 = time.time()
    w = winding(f, verts, K0, maxdepth=maxdepth, out=out, tag="N=%d X=%s Y=%s" % (N, X, Y))
    print("RESULT N=%d X=%s Y=%s winding=%s half=%s secs=%.1f" % (N, X, Y, w, (w // 2 if w is not None else None),
          time.time() - t0), flush=True)

if __name__ == "__main__":
    N = int(sys.argv[1]); X = sys.argv[2]; Y = sys.argv[3]
    K0 = int(sys.argv[4]) if len(sys.argv) > 4 else 400
    prec = int(sys.argv[5]) if len(sys.argv) > 5 else 128
    route = sys.argv[6] if len(sys.argv) > 6 else "L"
    main(N, X, Y, K0, prec, route=route)
