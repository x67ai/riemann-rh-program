// zt.c -- direct-sum evaluation of F_X(s) = sum_{n<=X} n^{-s} + rho X^{1-s}/(s-1) - E(X) X^{-s}
// over a dump of the g-integers (doubles, sorted) written by s8o. Opus reader, Session 41.
// E(X) = N(X) - rho (X - 1) - 1 with N(X) counted from the dump. Neumaier-compensated sums.
// usage: zt DUMP X rho eval  s r t ...      (prints F, F')
//        zt DUMP X rho newton r t [r t ...] (Newton from each start)
//        zt DUMP X rho real a b             (bisection for a real zero in [a, b])
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <complex.h>
static double *LG; static size_t NN; static double X, RHO, EX;
typedef struct { double s, c; } acc;
static inline void add(acc* a, double v) { double t = a->s + v; if (fabs(a->s) >= fabs(v)) a->c += (a->s - t) + v; else a->c += (v - t) + a->s; a->s = t; }
static void evalF(double r, double t, double complex* F, double complex* Fp) {
  acc fr = {0, 0}, fi = {0, 0}, dr = {0, 0}, di = {0, 0};
  for (size_t i = 0; i < NN; ++i) {
    double L = LG[i], a = exp(-r * L), c = cos(t * L), s = sin(t * L);
    double tr = a * c, ti = -a * s;
    add(&fr, tr); add(&fi, ti); add(&dr, -L * tr); add(&di, -L * ti);
  }
  double complex S = (fr.s + fr.c) + I * (fi.s + fi.c), D = (dr.s + dr.c) + I * (di.s + di.c);
  double complex s = r + I * t, lX = log(X), Xs = cexp(-s * lX);
  double complex main = RHO * X * Xs / (s - 1), tail = -EX * Xs;
  *F = S + main + tail;
  *Fp = D + main * (-lX - 1.0 / (s - 1)) + EX * lX * Xs;
}
int main(int argc, char** argv) {
  if (argc < 5) return 1;
  X = strtod(argv[2], 0); RHO = strtod(argv[3], 0);
  FILE* f = fopen(argv[1], "rb"); fseek(f, 0, SEEK_END); size_t tot = ftell(f) / 8; fseek(f, 0, SEEK_SET);
  double* v = malloc(tot * 8); fread(v, 8, tot, f); fclose(f);
  NN = 0; while (NN < tot && v[NN] <= X) NN++;
  LG = malloc(NN * 8); for (size_t i = 0; i < NN; ++i) LG[i] = log(v[i]); free(v);
  EX = (double)NN - RHO * (X - 1.0) - 1.0;
  printf("# zt X=%.6g N(X)=%zu E(X)=%.10f rho=%.17g\n", X, NN, EX, RHO);
  double complex F, Fp;
  if (!strcmp(argv[4], "eval")) {
    for (int k = 5; k + 1 < argc; k += 2) {
      double r = strtod(argv[k], 0), t = strtod(argv[k + 1], 0); evalF(r, t, &F, &Fp);
      printf("s=%.12f%+.12fi F=%.15e%+.15ei |F|=%.12e F'=%.12e%+.12ei\n", r, t, creal(F), cimag(F), cabs(F), creal(Fp), cimag(Fp));
    }
  } else if (!strcmp(argv[4], "newton")) {
    for (int k = 5; k + 1 < argc; k += 2) {
      double complex s = strtod(argv[k], 0) + I * strtod(argv[k + 1], 0);
      for (int it = 0; it < 12; ++it) {
        evalF(creal(s), cimag(s), &F, &Fp);
        double complex ds = F / Fp; s -= ds;
        if (cabs(ds) < 1e-14) break;
      }
      evalF(creal(s), cimag(s), &F, &Fp);
      printf("zero %.12f %+.12f |F|=%.3e |F'|=%.6f\n", creal(s), cimag(s), cabs(F), cabs(Fp));
      fflush(stdout);
    }
  } else if (!strcmp(argv[4], "real")) {
    double a = strtod(argv[5], 0), b = strtod(argv[6], 0), fa, fb;
    evalF(a, 0, &F, &Fp); fa = creal(F); evalF(b, 0, &F, &Fp); fb = creal(F);
    printf("F(%.6f)=%.12e F(%.6f)=%.12e\n", a, fa, b, fb);
    if (fa * fb > 0) { printf("no sign change\n"); return 0; }
    for (int it = 0; it < 60 && b - a > 1e-15; ++it) {
      double m = 0.5 * (a + b); evalF(m, 0, &F, &Fp);
      if (creal(F) * fa > 0) { a = m; fa = creal(F); } else b = m;
    }
    printf("real zero %.13f (bracket width %.1e)\n", 0.5 * (a + b), b - a);
  }
  return 0;
}
