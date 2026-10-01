/* s7dp.c -- independent check of s7gen: S7(num/den) by the ADDITIVE dynamic program over multiples (as S5's generator,
   u-offsurgery-s39/verify-F/s5gen_F.c), with the rule allowed to act only at prime powers.  No multiplicativity is used:
   A(n) = a[n] is accumulated by "a[k*q] += a[k], k increasing" for every copy of every g-prime q chosen so far.
   Variant 0 = standard, 1 = act only at primes.  Output: a_n as uint32 to argv[5]; stdout: N(X), sup/inf E, max a_n.
   Build: cc -O2 -o s7dp s7dp.c      Usage: s7dp num den X variant a.out */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv){
  if(argc < 6){ fprintf(stderr, "usage: s7dp num den X variant a.out\n"); return 1; }
  int64_t num = atoll(argv[1]), den = atoll(argv[2]); uint64_t X = strtoull(argv[3], 0, 10); int var = atoi(argv[4]);
  uint32_t *a = calloc(X + 1, 4), *spf = calloc(X + 1, 4);
  for(uint64_t i = 2; i <= X; i++) if(!spf[i]) for(uint64_t j = i; j <= X; j += i) if(!spf[j]) spf[j] = (uint32_t)i;
  a[1] = 1; int64_t N = 1; double supE = -1e300, infE = 1e300; uint64_t maxa = 1;
  for(uint64_t n = 2; n <= X; n++){
    uint64_t p = spf[n], r = n; int e = 0; while(r % p == 0){ r /= p; e++; }
    if(r == 1 && !(var == 1 && e >= 2)){                 /* n = p^e: the rule may act */
      int64_t A = a[n];
      __int128 t = (__int128)2*num*(int64_t)(n - 1) + (__int128)2*den*(1 - N - A) + den, d2 = 2*den;
      int64_t m = (int64_t)(t >= 0 ? t/d2 : -((-t + d2 - 1)/d2)); if(m < 0) m = 0;
      for(int64_t c = 0; c < m; c++) for(uint64_t k = 1; k*n <= X; k++) a[k*n] += a[k];
    }
    N += a[n]; if(a[n] > maxa) maxa = a[n];
    double E = (double)((__int128)den*N - (__int128)num*(int64_t)(n - 1) - den)/(double)den;
    if(E > supE) supE = E; if(E - (double)num/den < infE) infE = E - (double)num/den;
  }
  FILE *f = fopen(argv[5], "wb"); fwrite(a, 4, X + 1, f); fclose(f);
  printf("s7dp num=%lld den=%lld X=%llu var=%d N(X)=%lld supE=%.4f infE=%.4f maxa=%llu\n", (long long)num, (long long)den,
         (unsigned long long)X, var, (long long)N, supE, infE, (unsigned long long)maxa);
  return 0;
}
