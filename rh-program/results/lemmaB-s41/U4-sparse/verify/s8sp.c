/* s8sp.c -- unit U4-sparse (stream lemmaB-s41), written 2026-10-01.
   S8(rho) [mode 0] and the feedback-free lattice monoid [mode 1] (every lattice point a generator), rho = pi/D.
   Block sweep: composites in [B,B') are q*m, q a generator with q*q < B', m a stored element with spf(m) >= q,
   B' <= p1*B, so every cofactor is known when the block is processed. Lindley queue per lattice step:
   c_k = composites in (x_{k-1}, x_k], e_k = max(e_{k-1} + c_k - 1, 0), generator at x_k iff e_{k-1} + c_k = 0.
   Exact ordering: every composite within 1e-5 steps of a lattice point is re-decided in double-double
   (t = D/pi and every lattice factor in double-double, factorization read from the stored spf/cofactor chain).
   Usage: s8sp D X mode out.tsv [edump_write|-] [edump_compare]   (e dumps: uint16 per lattice step, saturating) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

typedef struct { double hi, lo; } dd;
static dd dd_qs(double s, double e){ double r = s + e; dd z = { r, e - (r - s) }; return z; }
static dd dd_add(dd a, dd b){ double s = a.hi + b.hi, v = s - a.hi;
  double e = (a.hi - (s - v)) + (b.hi - v) + a.lo + b.lo; return dd_qs(s, e); }
static dd dd_mul(dd a, dd b){ double p = a.hi * b.hi; double e = fma(a.hi, b.hi, -p) + a.hi * b.lo + a.lo * b.hi;
  return dd_qs(p, e); }
static dd dd_muld(dd a, double b){ double p = a.hi * b; double e = fma(a.hi, b, -p) + a.lo * b; return dd_qs(p, e); }
static dd dd_div(dd a, dd b){ double q1 = a.hi / b.hi; dd r = dd_add(a, dd_muld(b, -q1)); double q2 = r.hi / b.hi;
  r = dd_add(r, dd_muld(b, -q2)); double q3 = r.hi / b.hi; dd q = dd_qs(q1, q2); dd z = { q3, 0 }; return dd_add(q, z); }

static double t, rho, p1;
static dd tdd;
static double *val; static uint32_t *spf, *cof; static uint8_t *om; static size_t Gn = 0, Gcap = 0;
static uint32_t *gen; static size_t ngen = 0, gencap = 0;
static double Xstore;

static void gpush(double v, uint32_t s, uint32_t c, uint8_t o){
  if (Gn == Gcap){ Gcap = Gcap ? Gcap * 3 / 2 : (1u << 20);
    val = realloc(val, Gcap * sizeof *val); spf = realloc(spf, Gcap * sizeof *spf);
    cof = realloc(cof, Gcap * sizeof *cof); om = realloc(om, Gcap);
    if (!val || !spf || !cof || !om){ fprintf(stderr, "oom G\n"); exit(1); } }
  val[Gn] = v; spf[Gn] = s; cof[Gn] = c; om[Gn] = o; Gn++;
}
static void genpush(uint32_t gi){
  if (ngen == gencap){ gencap = gencap ? gencap * 2 : 4096; gen = realloc(gen, gencap * sizeof *gen); }
  gen[ngen++] = gi;
}
static inline double xlat(int64_t k){ return 1.0 + ((double)k - 0.5) * t; }
static dd xlatdd(int64_t k){ dd one = { 1.0, 0.0 }; return dd_add(one, dd_muld(tdd, (double)k - 0.5)); }
static int64_t latidx(double v){ return (int64_t)llround((v - 1.0) / t + 0.5); }
/* double-double value of stored element i (product of its lattice factors) */
static dd elemdd(uint32_t i){ dd acc = { 1.0, 0.0 };
  while (i != 0){ uint32_t p = spf[i]; acc = dd_mul(acc, xlatdd(latidx(val[p]))); i = cof[i]; }
  return acc; }

typedef struct { double n; uint32_t q, m; int64_t k; } comp_t;

/* audit counters */
static long long n_audit = 0, n_flip = 0, n_unres = 0; static double min_dd_margin = 1.0;

/* step index k with x_{k-1} < n <= x_k, re-decided in double-double when within 1e-5 steps of a lattice point */
static int64_t step_of(double n, uint32_t qi, uint32_t mi){
  double s = (n - 1.0) / t + 0.5; double fl = floor(s); double fr = s - fl;
  int64_t k = (int64_t)fl + 1;
  if (fr < 1e-5 || fr > 1.0 - 1e-5){
    n_audit++;
    dd ndd = dd_mul(elemdd(qi), elemdd(mi));
    dd m1 = { -1.0, 0.0 }, half = { 0.5, 0.0 };
    dd sdd = dd_add(dd_div(dd_add(ndd, m1), tdd), half);
    double f2 = floor(sdd.hi); double frac = (sdd.hi - f2) + sdd.lo;
    if (frac < 0){ f2 -= 1.0; frac += 1.0; } if (frac >= 1.0){ f2 += 1.0; frac -= 1.0; }
    double mg = frac < 1.0 - frac ? frac : 1.0 - frac;
    if (mg < min_dd_margin) min_dd_margin = mg;
    if (mg < 1e-22) n_unres++;
    int64_t k2 = (int64_t)f2 + 1;
    if (k2 != k){ n_flip++; k = k2; }
  }
  return k;
}

static int kcmp(const void *a, const void *b){ const comp_t *x = a, *y = b;
  if (x->k != y->k) return (x->k > y->k) - (x->k < y->k); return (x->n > y->n) - (x->n < y->n); }

/* per-bin statistics; bin b covers x_k in [10^{b/4}, 10^{(b+1)/4}) */
#define NB 64
#define HC 16
#define HE 48
#define NWIN 13
typedef struct { long long nsteps, nprime, ncomp, sc2, scc1, cmax, se, se2, emax, kemax, om[4], hc[HC], he[HE];
  double Emax; long long nw[NWIN]; double w1[NWIN], w2[NWIN]; long long viol, cmpd; } bin_t;
static bin_t bins[NB];

int main(int argc, char **argv){
  if (argc < 5){ fprintf(stderr, "usage: s8sp D X mode out.tsv [edump_write|-] [edump_compare]\n"); return 1; }
  double D = atof(argv[1]), X = atof(argv[2]); int mode = atoi(argv[3]);
  FILE *fo = fopen(argv[4], "w"); if (!fo){ perror("out"); return 1; }
  FILE *fdw = (argc > 5 && strcmp(argv[5], "-")) ? fopen(argv[5], "wb") : NULL;
  FILE *fdc = (argc > 6) ? fopen(argv[6], "rb") : NULL;
  dd pidd = { 3.141592653589793116, 1.224646799147353207e-16 }, Ddd = { D, 0.0 };
  tdd = dd_div(Ddd, pidd); t = tdd.hi; rho = 1.0 / t; p1 = 1.0 + t / 2.0;
  Xstore = (X + 2.0 * t) / p1 * (1.0 + 1e-9);
  int64_t kmax = (int64_t)floor((X - 1.0) / t + 0.5);
  const int64_t SEG = (int64_t)1 << 22;
  gpush(1.0, UINT32_MAX, 0, 0);
  int64_t kB = 0, e = 0, prevc = 0; long long nseg = 0;
  double carryn[256]; uint8_t carryo[256]; int ncarry = 0;
  comp_t *cb = NULL; size_t cbcap = 0;
  int64_t *newp = malloc((size_t)(SEG + 2) * sizeof *newp);
  uint16_t *ebuf = malloc((size_t)(SEG + 2) * sizeof *ebuf), *lbuf = malloc((size_t)(SEG + 2) * sizeof *lbuf);
  long long wacc[NWIN]; for (int j = 0; j < NWIN; j++) wacc[j] = 0;
  int b = 0; double bnext = pow(10.0, 0.25);
  for (int i = 0; i < NB; i++) bins[i].Emax = -1e300;
  while (kB < kmax){
    double B = 1.0 + (double)kB * t;
    double Bmax = p1 * (B > p1 ? B : p1);
    int64_t kB2 = (int64_t)floor((Bmax - 1.0) / t);
    if (kB2 > kB + SEG) kB2 = kB + SEG;
    if (kB2 > kmax + 1) kB2 = kmax + 1;
    if (kB2 <= kB){ fprintf(stderr, "segment stall at kB=%lld\n", (long long)kB); return 1; }
    double B2 = 1.0 + (double)kB2 * t;
    if (B > p1 && B2 / p1 > Xstore){ fprintf(stderr, "store too small\n"); return 1; }
    size_t nc = 0;
    for (size_t g = 0; g < ngen; g++){
      uint32_t qi = gen[g]; double q = val[qi];
      if (q * q >= B2) break;
      double lo = B / q * (1.0 - 1e-12), hi = B2 / q * (1.0 + 1e-12);
      size_t a = qi, bb = Gn;
      while (a < bb){ size_t mid = (a + bb) / 2; if (val[mid] < lo) a = mid + 1; else bb = mid; }
      for (size_t i = a; i < Gn && val[i] < hi; i++){
        if (spf[i] < qi) continue;
        double n = q * val[i];
        if (n < B || n >= B2) continue;
        if (nc == cbcap){ cbcap = cbcap ? cbcap * 3 / 2 : (1u << 20); cb = realloc(cb, cbcap * sizeof *cb);
          if (!cb){ fprintf(stderr, "oom cb\n"); return 1; } }
        cb[nc].n = n; cb[nc].q = qi; cb[nc].m = (uint32_t)i;
        cb[nc].k = step_of(n, qi, (uint32_t)i);
        if (cb[nc].k < kB + 1 || cb[nc].k > kB2 + 1){ fprintf(stderr, "step out of segment\n"); return 1; }
        nc++;
      }
    }
    qsort(cb, nc, sizeof *cb, kcmp);
    /* sweep the lattice points of the segment */
    int64_t klo = kB + 1, khi = kB2 < kmax ? kB2 : kmax, np = 0; size_t p = 0;
    for (int64_t k = klo; k <= khi; k++){
      double xk = xlat(k), xk1 = xlat(k - 1);
      while (xk >= bnext){ b++; bnext = pow(10.0, (b + 1) / 4.0); }
      bin_t *bp = &bins[b];
      long long c = 0; double Emx = -1e300;
      for (int i = 0; i < ncarry; i++){ c++; double E = e + 0.5 + c - (carryn[i] - xk1) / t; if (E > Emx) Emx = E;
        int o = carryo[i] >= 5 ? 3 : carryo[i] - 2; bp->om[o]++; }
      ncarry = 0;
      while (p < nc && cb[p].k == k){ c++; double E = e + 0.5 + c - (cb[p].n - xk1) / t; if (E > Emx) Emx = E;
        int oo = om[cb[p].m] + 1; int o = oo >= 5 ? 3 : oo - 2; bp->om[o]++; p++; }
      int idle = (e == 0 && c == 0);
      int64_t en = e + c - 1; if (en < 0) en = 0;
      if (en + 0.5 > Emx) Emx = en + 0.5;
      bp->nsteps++; bp->nprime += idle; bp->ncomp += c; bp->sc2 += c * c; bp->scc1 += c * prevc;
      if (c > bp->cmax) bp->cmax = c; bp->hc[c < HC ? c : HC - 1]++;
      bp->se += en; bp->se2 += en * en; if (en > bp->emax){ bp->emax = en; bp->kemax = k; }
      bp->he[en < HE ? en : HE - 1]++; if (Emx > bp->Emax) bp->Emax = Emx;
      for (int j = 0; j < NWIN; j++){ wacc[j] += c;
        if ((k & (((int64_t)1 << j) - 1)) == 0){ bp->nw[j]++; bp->w1[j] += (double)wacc[j];
          bp->w2[j] += (double)wacc[j] * (double)wacc[j]; wacc[j] = 0; } }
      ebuf[k - klo] = en > 65535 ? 65535 : (uint16_t)en;
      if (mode == 1 || idle) newp[np++] = k;
      e = en; prevc = c;
    }
    int64_t nst = khi - klo + 1;
    if (nst > 0 && fdw) fwrite(ebuf, sizeof *ebuf, (size_t)nst, fdw);
    if (nst > 0 && fdc){ size_t got = fread(lbuf, sizeof *lbuf, (size_t)nst, fdc);
      int bb2 = 0; double bn2 = pow(10.0, 0.25);
      for (int64_t i = 0; i < (int64_t)got; i++){ double xk = xlat(klo + i); while (xk >= bn2){ bb2++; bn2 = pow(10.0, (bb2 + 1) / 4.0); }
        if (lbuf[i] < 65535){ bins[bb2].cmpd++; if (ebuf[i] > lbuf[i]) bins[bb2].viol++; } } }
    while (p < nc){ if (khi < kB2 && cb[p].k > khi){ p++; continue; }  /* final segment: steps beyond X */
      if (cb[p].k != kB2 + 1){ fprintf(stderr, "leftover composite k=%lld\n", (long long)cb[p].k); return 1; }
      if (ncarry >= 256){ fprintf(stderr, "carry overflow\n"); return 1; }
      carryn[ncarry] = cb[p].n; carryo[ncarry] = om[cb[p].m] + 1; ncarry++; p++; }
    /* append the segment's elements to the store, in exact order (composite of step k before the generator at x_k) */
    size_t ic = 0; int64_t ip = 0;
    while (ic < nc || ip < np){
      int takec = (ip >= np) || (ic < nc && cb[ic].k <= newp[ip]);
      double v = takec ? cb[ic].n : xlat(newp[ip]);
      if (v > Xstore) break;
      if (Gn >= UINT32_MAX - 2){ fprintf(stderr, "index overflow\n"); return 1; }
      if (takec){ gpush(v, cb[ic].q, cb[ic].m, (uint8_t)(om[cb[ic].m] + 1)); ic++; }
      else { gpush(v, (uint32_t)Gn, 0, 1); genpush((uint32_t)(Gn - 1)); ip++; }
    }
    kB = kB2; nseg++;
    if (nseg % 20 == 0) fprintf(stderr, "seg %lld  x=%.3e  Gn=%zu  ngen=%zu  e=%lld\n", nseg, B2, Gn, ngen, (long long)e);
  }
  fprintf(fo, "# s8sp D=%g X=%g mode=%d t=%.17g rho=%.17g p1=%.17g audits=%lld flips=%lld unresolved=%lld min_dd_margin=%.3e Gn=%zu\n",
    D, X, mode, t, rho, p1, n_audit, n_flip, n_unres, min_dd_margin, Gn);
  fprintf(fo, "# cols: b x_lo x_hi nsteps nidle ncomp sc2 scc1 cmax se se2 emax kemax Emax om2 om3 om4 om5p viol cmpd | hc[%d] | he[%d] | (nw w1 w2)x%d\n", HC, HE, NWIN);
  for (int i = 0; i < NB; i++){ bin_t *bp = &bins[i]; if (!bp->nsteps) continue;
    fprintf(fo, "%d %.6e %.6e %lld %lld %lld %lld %lld %lld %lld %lld %lld %lld %.4f %lld %lld %lld %lld %lld %lld |",
      i, pow(10.0, i / 4.0), pow(10.0, (i + 1) / 4.0), bp->nsteps, bp->nprime, bp->ncomp, bp->sc2, bp->scc1, bp->cmax,
      bp->se, bp->se2, bp->emax, bp->kemax, bp->Emax, bp->om[0], bp->om[1], bp->om[2], bp->om[3], bp->viol, bp->cmpd);
    for (int j = 0; j < HC; j++) fprintf(fo, " %lld", bp->hc[j]); fprintf(fo, " |");
    for (int j = 0; j < HE; j++) fprintf(fo, " %lld", bp->he[j]); fprintf(fo, " |");
    for (int j = 0; j < NWIN; j++) fprintf(fo, " %lld %.0f %.0f", bp->nw[j], bp->w1[j], bp->w2[j]); fprintf(fo, "\n"); }
  fclose(fo); if (fdw) fclose(fdw); if (fdc) fclose(fdc);
  fprintf(stderr, "done: audits=%lld flips=%lld unresolved=%lld min_dd_margin=%.3e Gn=%zu ngen=%zu\n",
    n_audit, n_flip, n_unres, min_dd_margin, Gn, ngen);
  return 0;
}
