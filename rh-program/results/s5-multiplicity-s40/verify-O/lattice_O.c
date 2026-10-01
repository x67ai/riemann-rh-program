/* lattice_O.c -- Opus reader (Session 41). Exact f_G(n) = number of multisets of elements of G (each m_q = 1) with
 * product n, over the FULL divisor lattice of n (no top-prime reduction, no identity): f = coefficient of
 * prod_{g in G} (1 - x^{v(g)})^{-1}, computed by one in-place unbounded-knapsack pass per g over the sub-box
 * {e : v(g) <= e <= E}, in increasing linear index, uint64 cells, EVERY addition overflow-checked.
 * Input: file from gdiv_O.py (header '# NAME n=.. primes=[..] exps=[..]', then lines 'q v_1 ... v_d').
 * Prints f(n) and f at the divisor n0 = n / (product of the last three primes) when they have exponent 1.
 * Build: clang -O2 -o lattice_O lattice_O.c */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#define MAXD 32
static int d, E[MAXD], ord[MAXD];      /* ord: dimension order, ord[d-1] innermost */
static uint64_t stride[MAXD], T;
static uint64_t *f;
static int overflow = 0;
static int lo_[MAXD];                  /* current g's exponent vector (in original order) */

static void sweep(int lev, uint64_t base, uint64_t off) {
  int k = ord[lev];
  if (lev == d - 2) {
    int k2 = ord[d - 1]; uint64_t s1 = stride[k];
    for (int e1 = lo_[k]; e1 <= E[k]; e1++) {
      uint64_t b1 = base + (uint64_t)e1 * s1;
      for (int e = lo_[k2]; e <= E[k2]; e++) {
        uint64_t i = b1 + (uint64_t)e, x = f[i], y = f[i - off], z = x + y;
        if (z < x) overflow = 1;
        f[i] = z;
      }
    }
    return;
  }
  if (lev == d - 1) {
    uint64_t s = stride[k];
    for (int e = lo_[k]; e <= E[k]; e++) {
      uint64_t i = base + (uint64_t)e * s, x = f[i], y = f[i - off], z = x + y;
      if (z < x) overflow = 1;
      f[i] = z;
    }
    return;
  }
  for (int e = lo_[k]; e <= E[k]; e++) sweep(lev + 1, base + (uint64_t)e * stride[k], off);
}

int main(int argc, char **argv) {
  if (argc < 2) { fprintf(stderr, "usage: lattice_O FILE\n"); return 1; }
  FILE *fp = fopen(argv[1], "r"); if (!fp) { perror("open"); return 1; }
  char line[4096]; long long P[MAXD];
  if (!fgets(line, sizeof line, fp)) return 1;
  char *pp = strstr(line, "primes=["), *pe = strstr(line, "exps=[");
  d = 0; pp += 8; while (*pp && *pp != ']') { P[d++] = strtoll(pp, &pp, 10); while (*pp == ',' || *pp == ' ') pp++; }
  int dd = 0; pe += 6; while (*pe && *pe != ']') { E[dd++] = (int)strtol(pe, &pe, 10); while (*pe == ',' || *pe == ' ') pe++; }
  if (dd != d) { fprintf(stderr, "header mismatch\n"); return 1; }
  /* order: innermost = largest exponent range (ties: earlier prime); outer ones by decreasing size too */
  int used[MAXD] = {0};
  for (int lev = d - 1; lev >= 0; lev--) { int b = -1; for (int k = 0; k < d; k++) if (!used[k] && (b < 0 || E[k] > E[b])) b = k; ord[lev] = b; used[b] = 1; }
  T = 1; for (int lev = d - 1; lev >= 0; lev--) { stride[ord[lev]] = T; T *= (uint64_t)(E[ord[lev]] + 1); }
  f = calloc(T, sizeof(uint64_t)); if (!f) { fprintf(stderr, "alloc %llu cells failed\n", (unsigned long long)T); return 1; }
  f[0] = 1;
  long ng = 0; uint64_t cells = 0; clock_t t0 = clock();
  while (fgets(line, sizeof line, fp)) {
    if (line[0] == '#') continue;
    char *s = line; long long q = strtoll(s, &s, 10); (void)q;
    uint64_t off = 0, c = 1;
    for (int k = 0; k < d; k++) { lo_[k] = (int)strtol(s, &s, 10); off += (uint64_t)lo_[k] * stride[k]; c *= (uint64_t)(E[k] + 1 - lo_[k]); }
    if (off == 0) { fprintf(stderr, "zero vector\n"); return 1; }
    sweep(0, 0, off); ng++; cells += c;
    if (ng % 500 == 0) fprintf(stderr, "g=%ld cells=%llu t=%.0fs\n", ng, (unsigned long long)cells, (double)(clock() - t0) / CLOCKS_PER_SEC);
  }
  printf("file=%s d=%d T=%llu g=%ld cells=%llu overflow=%d t=%.1fs\n", argv[1], d, (unsigned long long)T, ng,
         (unsigned long long)cells, overflow, (double)(clock() - t0) / CLOCKS_PER_SEC);
  printf("f(n) = %llu\n", (unsigned long long)f[T - 1]);
  if (d >= 4 && E[d - 1] == 1 && E[d - 2] == 1 && E[d - 3] == 1) {
    uint64_t i0 = T - 1 - stride[d - 1] - stride[d - 2] - stride[d - 3];
    printf("f(n/(p_{d-2} p_{d-1} p_d)) = %llu  [divisor n0 = n/(%lld*%lld*%lld)]\n", (unsigned long long)f[i0], P[d - 3], P[d - 2], P[d - 1]);
  }
  return overflow ? 3 : 0;
}
