# zeta100.py -- read-O: are all zeros of zeta with 0 < t <= 100 on the critical line? (NOTE l. 139 has this as [recalled, unverified])
# Count A: mpmath.nzeros(100) (Backlund/Turing-type count of zeros in the critical strip up to height 100).
# Count B: sign changes of Hardy's Z(t) on (0, 100] on a grid of step 0.005, refined by bisection (each is a zero ON the line).
import mpmath as mp
mp.mp.dps = 20
A = mp.nzeros(100)
ts = [0.005*k for k in range(1, 20001)]; zs = [mp.siegelz(t) for t in ts]
B = sum(1 for i in range(len(ts)-1) if zs[i]*zs[i+1] < 0)
print('nzeros(100) =', A, ' sign changes of Z on (0,100] =', B, ' first/last zero on line:', mp.zetazero(1).imag, mp.zetazero(A).imag)
print('ALL ON LINE' if A == B else 'MISMATCH')
