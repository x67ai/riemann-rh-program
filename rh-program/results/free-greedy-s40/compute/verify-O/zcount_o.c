// zcount_o.c -- argument principle for F_X (direct sums over a dump of g-integers), boxes of height H
// over [s1, s2] x [t1, t2], adaptive steps (|d arg| <= pi/8 between consecutive points). Opus reader.
// usage: zcount_o DUMP X rho s1 s2 t1 t2 H h0
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
static double *LG; static size_t NN; static double X, RHO, EX; static long NEV = 0;
static double complex F(double complex s) {
  double sr = 0, si = 0, cr = 0, ci = 0, r = creal(s), t = cimag(s);
  for (size_t i = 0; i < NN; ++i) {
    double L = LG[i], a = exp(-r * L), tr = a * cos(t * L), ti = -a * sin(t * L), y;
    y = sr + tr; cr += (fabs(sr) >= fabs(tr)) ? (sr - y) + tr : (tr - y) + sr; sr = y;
    y = si + ti; ci += (fabs(si) >= fabs(ti)) ? (si - y) + ti : (ti - y) + si; si = y;
  }
  NEV++;
  double complex Xs = cexp(-s * log(X));
  return (sr + cr) + I * (si + ci) + RHO * X * Xs / (s - 1) - EX * Xs;
}
static double minabs = 1e300;
// accumulate arg change from a to b (values fa, fb known), refining while |d arg| > pi/8
static double seg(double complex a, double complex b, double complex fa, double complex fb, int depth) {
  double d = carg(fb / fa);
  if (fabs(d) <= M_PI / 8 || depth > 30) { if (depth > 30) fprintf(stderr, "depth limit at %g%+gi\n", creal(a), cimag(a)); return d; }
  double complex m = 0.5 * (a + b), fm = F(m); if (cabs(fm) < minabs) minabs = cabs(fm);
  return seg(a, m, fa, fm, depth + 1) + seg(m, b, fm, fb, depth + 1);
}
static double edge(double complex a, double complex b, double h0) {
  int n = (int)ceil(cabs(b - a) / h0); double tot = 0;
  double complex p = a, fp = F(p); if (cabs(fp) < minabs) minabs = cabs(fp);
  for (int i = 1; i <= n; ++i) {
    double complex q = a + (b - a) * ((double)i / n), fq = F(q); if (cabs(fq) < minabs) minabs = cabs(fq);
    tot += seg(p, q, fp, fq, 0); p = q; fp = fq;
  }
  return tot;
}
int main(int argc, char** argv) {
  if (argc < 10) return 1;
  X = strtod(argv[2], 0); RHO = strtod(argv[3], 0);
  double s1 = atof(argv[4]), s2 = atof(argv[5]), t1 = atof(argv[6]), t2 = atof(argv[7]), H = atof(argv[8]), h0 = atof(argv[9]);
  FILE* f = fopen(argv[1], "rb"); fseek(f, 0, SEEK_END); size_t tot = ftell(f) / 8; fseek(f, 0, SEEK_SET);
  size_t want = tot; double* v = malloc(want * 8); fread(v, 8, want, f); fclose(f);
  NN = 0; while (NN < tot && v[NN] <= X) NN++;
  LG = malloc(NN * 8); for (size_t i = 0; i < NN; ++i) LG[i] = log(v[i]); free(v);
  EX = (double)NN - RHO * (X - 1.0) - 1.0;
  printf("# zcount X=%.6g N=%zu E(X)=%.8f rect [%g,%g]x[%g,%g] boxes of height %g, base step %g\n", X, NN, EX, s1, s2, t1, t2, H, h0);
  double total = 0;
  for (double ta = t1; ta < t2 - 1e-12; ta += H) {
    double tb = fmin(ta + H, t2); minabs = 1e300;
    double w = edge(s1 + I * ta, s2 + I * ta, h0) + edge(s2 + I * ta, s2 + I * tb, h0)
             + edge(s2 + I * tb, s1 + I * tb, h0) + edge(s1 + I * tb, s1 + I * ta, h0);
    w /= 2 * M_PI; total += w;
    printf("box t in [%7.2f, %7.2f]: winding %+.4f  min|F| on boundary %.3e  (evals so far %ld)\n", ta, tb, w, minabs, NEV);
    fflush(stdout);
  }
  printf("# total winding %.4f\n", total);
  return 0;
}
