// dp7o.c -- read-O (Session 41) second independent generator of S7(rho): additive DP over multiples,
// written from NOTE.md §1 Definition only; NO multiplicativity used. a[] holds, for every j > n, the number of
// representations of j by the g-primes chosen before step j; choosing g-prime q (one copy) does a[kq] += a[k], k = 1,2,...
// usage: dp7o num den cap X dump|-   (dump: uint16 a_n, n = 0..X)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
typedef __int128 i128;
int main(int argc, char **argv){
  int64_t num = atoll(argv[1]), den = atoll(argv[2]); int cap = atoi(argv[3]); uint64_t X = strtoull(argv[4], 0, 10);
  uint32_t *a = calloc(X+1, 4); uint8_t *pp = calloc(X+1, 1); // pp: 0 = not a prime power, 1 = prime power
  uint8_t *comp = calloc(X+1, 1);
  for (uint64_t i = 2; i <= X; i++) if (!comp[i]) { for (uint64_t j = i*i; j <= X; j += i) comp[j] = 1;
    for (uint64_t q = i; ; q *= i) { pp[q] = 1; if (q > X / i) break; } }
  free(comp);
  a[1] = 1; int64_t N = 1, dEmax = INT64_MIN, dEmin = INT64_MAX; uint64_t maxa = 0;
  for (uint64_t n = 2; n <= X; n++) {
    if (pp[n]) { uint64_t A = a[n];
      i128 Y = (i128)2*num*(i128)(n-1) + (i128)2*den*((i128)1 - N - (i128)A) + den; int64_t m = 0;
      if (Y >= 0) m = (int64_t)(Y / (2*den)); if (cap > 0 && m > cap) m = cap;
      for (int64_t t = 0; t < m; t++) for (uint64_t k = 1; k <= X / n; k++) a[k*n] += a[k];
      if (a[n] != A + (uint64_t)m) { fprintf(stderr, "dp inconsistency at %llu\n", (unsigned long long)n); return 2; } }
    N += a[n]; if (a[n] > maxa) maxa = a[n];
    int64_t dE = den*N - num*(int64_t)(n-1) - den; if (dE > dEmax) dEmax = dE; if (dE < dEmin) dEmin = dE;
  }
  printf("DP rho=%lld/%lld cap=%d X=%llu N=%lld supE=%lld/%lld infE_int=%lld/%lld maxa=%llu\n", (long long)num, (long long)den, cap,
    (unsigned long long)X, (long long)N, (long long)dEmax, (long long)den, (long long)dEmin, (long long)den, (unsigned long long)maxa);
  if (strcmp(argv[5], "-")) { FILE *f = fopen(argv[5], "wb"); for (uint64_t n = 0; n <= X; n++) { uint16_t v = (uint16_t)a[n];
      if (a[n] > 65535) { fprintf(stderr, "overflow\n"); return 3; } fwrite(&v, 2, 1, f); } fclose(f); }
  return 0;
}
