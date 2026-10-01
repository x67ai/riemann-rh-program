/* s8g_core.h — types, parameters, 320-bit exact fallback for s8gen.c (read-O, U6, second producer).
 * Decision rule (proved in read-O §2): for a composite c = x_{n_1} ... x_{n_j} (j >= 2), with b_i = 2 n_i - 1 and
 * E_r = e_r(b_1..b_j), W(c) := rho (c - 1) + 1/2 = (E_1 + 1)/2 + sum_{r=2}^{j} E_r kappa_r, kappa_r = t^(r-1)/2^r.
 * With K_r = floor(kappa_r 2^F) (certified, kappa_r irrational): 2^F W(c) lies in the OPEN interval
 * (Hlo, Hlo + sum_{r>=2} E_r), Hlo = (E_1+1) 2^(F-1) + sum E_r K_r. The cell of c is m = floor(W) + 1. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <time.h>
typedef unsigned __int128 u128;
typedef __int128 i128;
typedef uint64_t u64;
typedef int64_t i64;
typedef uint32_t u32;
typedef uint16_t u16;

#define F 90
#define NL 6            /* 6 x 64 = 384-bit limbs; fixed point 2^-320 */
#define MAXR 40
#define MAXCP 64

static int D, R;
static double tdbl;
static u64 KFIN, NCAP;
static u128 Kr[MAXR + 2];
static u64 KH[MAXR + 2][NL];
static int ncp;
static u64 cpV[MAXCP], cpCell[MAXCP];
static u128 cpW[MAXCP];
static u64 cpWH[MAXCP][NL];

static void die(const char *m) { fprintf(stderr, "FATAL: %s\n", m); printf("FATAL: %s\n", m); exit(2); }

static u128 parse_u128(const char *s) {
  u128 v = 0;
  for (; *s >= '0' && *s <= '9'; s++) v = v * 10 + (u128)(*s - '0');
  return v;
}
static void print_u128(FILE *f, u128 v) {
  char b[64]; int k = 63; b[k] = 0;
  if (v == 0) { fputs("0", f); return; }
  while (v) { b[--k] = '0' + (int)(v % 10); v /= 10; }
  fputs(b + k, f);
}
static void parse_limbs(char *s, u64 *a) {
  for (int i = 0; i < NL; i++) {
    while (*s == ' ') s++;
    a[i] = strtoull(s, &s, 16);
  }
}

static void read_params(const char *fn) {
  FILE *f = fopen(fn, "r"); if (!f) die("params file");
  char line[4096], key[16];
  while (fgets(line, sizeof line, f)) {
    if (sscanf(line, "%15s", key) != 1) continue;
    char *p = line + strlen(key);
    if (!strcmp(key, "D")) D = atoi(p);
    else if (!strcmp(key, "F")) { if (atoi(p) != F) die("F mismatch"); }
    else if (!strcmp(key, "F2")) { if (atoi(p) != 64 * (NL - 1)) die("F2 mismatch"); }
    else if (!strcmp(key, "R")) { R = atoi(p); if (R > MAXR - 1) die("R too large"); }
    else if (!strcmp(key, "TDBL")) tdbl = strtod(p, NULL);
    else if (!strcmp(key, "KFIN")) KFIN = strtoull(p, NULL, 10);
    else if (!strcmp(key, "NCAP")) NCAP = strtoull(p, NULL, 10);
    else if (!strcmp(key, "K")) {
      char *q; int r = (int)strtol(p, &q, 10);
      while (*q == ' ') q++;
      Kr[r] = parse_u128(q);
      while (*q && *q != ' ') q++;
      parse_limbs(q, KH[r]);
    } else if (!strcmp(key, "CP")) {
      if (ncp >= MAXCP) die("too many checkpoints");
      char *q; cpV[ncp] = strtoull(p, &q, 10);
      while (*q == ' ') q++;
      cpW[ncp] = parse_u128(q);
      while (*q && *q != ' ') q++;
      parse_limbs(q, cpWH[ncp]);
      cpCell[ncp] = (u64)(cpW[ncp] >> F) + 1;   /* x_{cell-1} < V < x_cell */
      ncp++;
    }
  }
  fclose(f);
  if (!D || !R || !KFIN || !NCAP || tdbl <= 2.0) die("incomplete params");
}

/* ---- 384-bit unsigned arithmetic, little-endian limbs ---- */
static void ml_add_u128(u64 *a, u128 v, int at) {   /* a += v * 2^(64 at) */
  u128 c = v;
  for (int i = at; i < NL && c; i++) { u128 s = (u128)a[i] + (u64)c; a[i] = (u64)s; c = (c >> 64) + (s >> 64); }
  if (c) die("ml overflow");
}
static void ml_muladd(u64 *a, const u64 *k, u128 e) { /* a += k * e, e < 2^64 required */
  if (e >> 64) die("ml_muladd: E_r too large");
  u64 ee = (u64)e; u128 carry = 0;
  for (int i = 0; i < NL; i++) {
    u128 s = (u128)k[i] * ee + a[i] + carry; a[i] = (u64)s; carry = s >> 64;
  }
  if (carry) die("ml overflow");
}
static int ml_cmp(const u64 *a, const u64 *b) {
  for (int i = NL - 1; i >= 0; i--) { if (a[i] != b[i]) return a[i] < b[i] ? -1 : 1; }
  return 0;
}
/* Exact enclosure at 2^-320 of W(c) for the factor list bb[0..j-1]: 2^320 W in (HL, HH). */
static void exact_W(const u64 *bb, int j, u64 *HL, u64 *HH) {
  u128 E[MAXR + 2]; memset(E, 0, sizeof E); E[0] = 1;
  for (int i = 0; i < j; i++) for (int r = i + 1; r >= 1; r--) E[r] += (u128)bb[i] * E[r - 1];
  memset(HL, 0, NL * 8);
  u128 e1p1 = E[1] + 1;            /* (E1+1) 2^319 = ((E1+1)>>1) 2^320 + ((E1+1)&1) 2^319 */
  ml_add_u128(HL, (u128)(u64)(e1p1 & 1) << 63, NL - 2);
  ml_add_u128(HL, e1p1 >> 1, NL - 1);
  u128 wsum = 0;
  for (int r = 2; r <= j; r++) { ml_muladd(HL, KH[r], E[r]); wsum += E[r]; }
  memcpy(HH, HL, NL * 8);
  ml_add_u128(HH, wsum, 0);
}
