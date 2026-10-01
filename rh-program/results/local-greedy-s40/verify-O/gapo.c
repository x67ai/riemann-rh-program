// gapo.c -- read-O: largest gap between consecutive primes and between consecutive prime powers up to X (segmented sieve).
// Checks NOTE l. 70 ("max prime gap below 10^9 [recalled, unverified] 282") and gives G(X) of Lemma 1.2 exactly.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
static int cmp(const void *a, const void *b){ uint64_t x = *(const uint64_t*)a, y = *(const uint64_t*)b; return x < y ? -1 : x > y; }
int main(int argc, char **argv){
  uint64_t X = strtoull(argv[1], 0, 10), SQ = (uint64_t)sqrt((double)X) + 1, S = 1 << 22;
  uint8_t *c = calloc(SQ + 1, 1); uint32_t *pr = malloc(sizeof(uint32_t)*(SQ + 1)); int np = 0;
  for (uint64_t i = 2; i <= SQ; i++) if (!c[i]) { pr[np++] = (uint32_t)i; for (uint64_t j = i*i; j <= SQ; j += i) c[j] = 1; }
  // higher prime powers p^k (k >= 2) <= X, sorted
  uint64_t *hp = malloc(sizeof(uint64_t)*200000); int nh = 0;
  for (int i = 0; i < np; i++) for (uint64_t q = (uint64_t)pr[i]*pr[i]; q <= X; q *= pr[i]) { hp[nh++] = q; if (q > X / pr[i]) break; }
  qsort(hp, nh, sizeof(uint64_t), cmp);
  uint8_t *seg = malloc(S); uint64_t lastp = 2, lastq = 2, gp = 0, gq = 0, gpa = 0, gqa = 0; int hi = 0;
  for (uint64_t L = 3; L <= X; L += S) { uint64_t R = L + S; if (R > X + 1) R = X + 1; memset(seg, 1, R - L);
    for (int i = 0; i < np && (uint64_t)pr[i]*pr[i] < R; i++) { uint64_t p = pr[i], j = ((L + p - 1)/p)*p; if (j < p*p) j = p*p; for (; j < R; j += p) seg[j - L] = 0; }
    for (uint64_t n = L; n < R; n++) { int isp = seg[n - L]; int ishp = 0; while (hi < nh && hp[hi] < n) hi++; if (hi < nh && hp[hi] == n) ishp = 1;
      if (isp) { if (n - lastp > gp) { gp = n - lastp; gpa = lastp; } lastp = n; }
      if (isp || ishp) { if (n - lastq > gq) { gq = n - lastq; gqa = lastq; } lastq = n; } } }
  printf("X=%llu max prime gap %llu after %llu ; max prime-power gap %llu after %llu\n", (unsigned long long)X,
    (unsigned long long)gp, (unsigned long long)gpa, (unsigned long long)gq, (unsigned long long)gqa);
  return 0;
}
