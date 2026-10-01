/* primes_O.c -- Opus reader (Session 41). From MY g-prime lists (s5gen_O.c output) and my own odd-only Eratosthenes
 * sieve to 2e9: per-decade accepted primes / refused primes / composite g-primes; pi(1e9), pi(2e9); the refused primes
 * <= 400; and c_l(1e9) = #{composite g-primes <= 1e9 divisible by l} for the first 30 refused primes l.
 * Build: clang -O2 -o primes_O primes_O.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#define XM 2000000000ULL
static uint8_t *comp; /* bit i <-> odd number 2i+1 composite */
static inline int isprime(uint64_t n) { if (n < 2) return 0; if (n == 2) return 1; if (!(n & 1)) return 0; uint64_t i = n >> 1; return !((comp[i >> 3] >> (i & 7)) & 1); }
int main(int argc, char **argv) {
  const char *dir = argc > 1 ? argv[1] : "/private/tmp/rh-s41-read-s5mult";
  comp = calloc(XM / 16 + 2, 1);
  comp[0] |= 1; /* 1 is not prime */
  for (uint64_t p = 3; p * p <= XM; p += 2) if (isprime(p)) for (uint64_t m = p * p; m <= XM; m += 2 * p) { uint64_t i = m >> 1; comp[i >> 3] |= (uint8_t)(1u << (i & 7)); }
  uint64_t pi_dec[11] = {0}, acc_dec[11] = {0}, cmp_dec[11] = {0}, pi1 = 0, pi2 = 0;
  for (uint64_t n = 2, nd = 10, d = 0; n <= XM; n++) { if (n == nd) { d++; nd *= 10; } if (isprime(n)) { pi_dec[d]++; if (n <= 1000000000ULL) pi1++; pi2++; } }
  /* read g-prime lists */
  char path[512]; int isacc_small[401] = {0};
  uint64_t refused[64]; int nref = 0; uint64_t cl[64] = {0};
  for (int f = 0; f < 2; f++) {
    snprintf(path, sizeof path, "%s/%s", dir, f ? "gp_O_ext.u32" : "gp_O_1e9.u32");
    FILE *fp = fopen(path, "rb"); if (!fp) { perror(path); return 1; }
    uint32_t pr[2];
    while (fread(pr, 4, 2, fp) == 2) {
      uint64_t q = pr[0], d = 0, t = q; while (t >= 10) { t /= 10; d++; }
      if (isprime(q)) { acc_dec[d]++; if (q <= 400) isacc_small[q] = 1; } else cmp_dec[d]++;
    }
    fclose(fp);
  }
  printf("pi(1e9)=%llu pi(2e9)=%llu diff=%llu\n", (unsigned long long)pi1, (unsigned long long)pi2, (unsigned long long)(pi2 - pi1));
  for (int d = 0; d < 10; d++) printf("decade %d: primes=%llu accepted=%llu refused=%llu composite_gp=%llu\n", d,
    (unsigned long long)pi_dec[d], (unsigned long long)acc_dec[d], (unsigned long long)(pi_dec[d] - acc_dec[d]), (unsigned long long)cmp_dec[d]);
  printf("refused primes <= 400:");
  for (int p = 2; p <= 400; p++) if (isprime(p) && !isacc_small[p]) { printf(" %d", p); if (nref < 30) refused[nref++] = p; }
  printf("\naccepted primes <= 150:");
  for (int p = 2; p <= 150; p++) if (isprime(p) && isacc_small[p]) printf(" %d", p);
  printf("\n");
  snprintf(path, sizeof path, "%s/gp_O_1e9.u32", dir);
  FILE *fp = fopen(path, "rb"); uint32_t pr[2];
  while (fread(pr, 4, 2, fp) == 2) { uint64_t q = pr[0]; if (isprime(q)) continue; for (int i = 0; i < nref; i++) if (q % refused[i] == 0) cl[i]++; }
  fclose(fp);
  double mn = 1e9, mx = 0;
  for (int i = 0; i < nref; i++) { double r = (double)cl[i] * refused[i] / 1e9; if (r < mn) mn = r; if (r > mx) mx = r;
    printf("c_l(1e9) l=%llu: %llu  (c_l*l/1e9 = %.4f)\n", (unsigned long long)refused[i], (unsigned long long)cl[i], r); }
  printf("range of c_l*l/1e9 over first %d refused l: %.4f .. %.4f ; 0.9/ln(1e9) = %.4f\n", nref, mn, mx, 0.9 / log(1e9));
  return 0;
}
