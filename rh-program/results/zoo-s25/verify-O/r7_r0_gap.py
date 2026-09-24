# Reader check (Opus 5): arithmetic of the IV.9 close-2 and close-4 riders; the decomposition of the 73L / 1.1L gap.
import math
cB = 2/math.sqrt(72*math.e)
print('c_B = 2/sqrt(72e) =', round(cB, 8))
print('(7/(8 cB))^2 =', round((7/(8*cB))**2, 4), ' (13/(16 cB))^2 =', round((13/(16*cB))**2, 4))
print('(0.7071/cB)^2 =', round((1/math.sqrt(2)/cB)**2, 2), ' (0.85/cB)^2 =', round((0.85/cB)**2, 2))
print('(7/(8*0.85))^2 =', round((7/(8*0.85))**2, 4), ' (7/(8/sqrt2))^2 =', round((7/(8/math.sqrt(2)))**2, 4))
print('73 / 1.1 =', round(73/1.1, 1), '; 73 / 1.086 =', round(73/1.086, 1))
print('uniformity part 73 / 32.30 =', round(73/(13/(16*cB))**2, 2), '; c_B part (rate 1/sqrt2) =', round((1/math.sqrt(2)/cB)**2, 2),
      '; asymptote at rate 1/sqrt2 with exponent 13/8: (13/(16/sqrt2))^2 =', round((13/(16/math.sqrt(2)))**2, 3))
t, d = 1e6, 0.1
a, b = math.log(math.log(3 + t)), 2*math.log(1/d)
c = math.log(2*8.70)
L = 4/d*(a + b + c)
print('L*(0.1,1e6) at b1 = 8.70, C1 = 1:', round(L, 2), ' shares %.1f/%.1f/%.1f %%' % (100*a/(a+b+c), 100*b/(a+b+c), 100*c/(a+b+c)),
      ' floor', round(4/d*(b + c), 2))
