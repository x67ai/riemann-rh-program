// fxo.c -- read-O (Session 41): DIRECT sums D_X(s) = sum_{n<=X} (a_n - rho) n^{-s} and D_X'(s) = -sum (a_n - rho) log n n^{-s}
// at points along segments s_a + j*delta, j = 0..K (per n: n^{-s_a} once, then the exact ratio n^{-delta}; no Taylor moments).
// F_X = rho*zeta + D_X is assembled in Python (mpmath zeta). Written from NOTE §3.0's definition only.
// usage: fxo dump.u16 X num den segfile > out   (segfile lines: sa_re sa_im d_re d_im K)
// Summation: per-block (2^14 n) double partial sums flushed into Neumaier-compensated global sums.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
typedef struct { double s, c; } nm;
static void nadd(nm *a, double v){ double t = a->s + v; if (fabs(a->s) >= fabs(v)) a->c += (a->s - t) + v; else a->c += (v - t) + a->s; a->s = t; }
int main(int argc, char **argv){
  if (argc < 6) { fprintf(stderr, "usage\n"); return 1; }
  int fd = open(argv[1], O_RDONLY); struct stat st; fstat(fd, &st);
  uint16_t *a = mmap(0, st.st_size, PROT_READ, MAP_PRIVATE, fd, 0);
  uint64_t X = strtoull(argv[2], 0, 10); double rho = atof(argv[3]) / atof(argv[4]);
  if ((uint64_t)st.st_size / 2 < X + 1) { fprintf(stderr, "dump too short\n"); return 1; }
  FILE *sf = fopen(argv[5], "r"); int ns = 0; double sar[64], sai[64], dr[64], di[64]; int K[64], off[64], P = 0;
  while (ns < 64 && fscanf(sf, "%lf %lf %lf %lf %d", &sar[ns], &sai[ns], &dr[ns], &di[ns], &K[ns]) == 5) { off[ns] = P; P += K[ns] + 1; ns++; }
  double *lr = calloc(P, 8), *li = calloc(P, 8), *ldr = calloc(P, 8), *ldi = calloc(P, 8);
  nm *gr = calloc(P, sizeof(nm)), *gi = calloc(P, sizeof(nm)), *gdr = calloc(P, sizeof(nm)), *gdi = calloc(P, sizeof(nm));
  for (uint64_t n = 1; n <= X; n++) {
    double b = (double)a[n] - rho; double L = log((double)n);
    for (int q = 0; q < ns; q++) {
      double m0 = exp(-sar[q]*L), ph = sai[q]*L; double wr = m0*cos(ph), wi = -m0*sin(ph);
      int o = off[q], k = K[q]; double rr = 1, ri = 0;
      if (k > 0) { double rm = exp(-dr[q]*L), rp = di[q]*L; rr = rm*cos(rp); ri = -rm*sin(rp); }
      for (int j = 0; j <= k; j++) {
        lr[o+j] += b*wr; li[o+j] += b*wi; ldr[o+j] -= b*L*wr; ldi[o+j] -= b*L*wi;
        double tr = wr*rr - wi*ri; wi = wr*ri + wi*rr; wr = tr;
      }
    }
    if ((n & 16383) == 0 || n == X) for (int j = 0; j < P; j++) {
      nadd(&gr[j], lr[j]); nadd(&gi[j], li[j]); nadd(&gdr[j], ldr[j]); nadd(&gdi[j], ldi[j]); lr[j] = li[j] = ldr[j] = ldi[j] = 0; }
  }
  for (int q = 0; q < ns; q++) for (int j = 0; j <= K[q]; j++) { int p = off[q] + j;
    printf("%d %.12f %.12f %.15e %.15e %.15e %.15e\n", q, sar[q] + j*dr[q], sai[q] + j*di[q],
      gr[p].s + gr[p].c, gi[p].s + gi[p].c, gdr[p].s + gdr[p].c, gdi[p].s + gdi[p].c); }
  return 0;
}
