/* s8g_mom.h — integer block moments of Delta = W - W0 for every g-integer (read-O, U6).
 * Cells m < 2^16: every g-integer stored individually as its enclosure (Hlo, Hhi) of 2^F W.
 * Cells m >= 2^16, m in [2^j, 2^(j+1)): blocks of L = 2^(j-14) consecutive cells; block i covers cells
 * [2^j + iL, 2^j + (i+1)L), i.e. W in (2^j + iL - 1, 2^j + (i+1)L - 1]; centre W0 = 2^j + iL - 1 + L/2 (integer),
 * so |Delta| <= L/2 for every g-integer of the block.
 * Stored per block (all exact integer sums; per-term truncations bounded in read-O §2):
 *   cnt; s1lo <= 2^64 sum Delta <= s1hi;  s2 = sum D2^2 with D2 = floor(2^32 Delta_lo), a2 = sum |D2|;
 *   s3 = sum D3^3 with D3 = floor(2^16 Delta_lo), q3 = sum D3^2, a3 = sum |D3|; wmax = max width (2^-F units). */
typedef struct {
  u64 cnt; i128 s1lo, s1hi; i128 s2; u128 a2; i128 s3; u128 q3; u128 a3; u64 wmax; u64 pad;
} Mom;

#define NOCT 17                 /* octaves j = 16 .. 32 */
#define NBLK (NOCT << 14)
static Mom *mom;
static u128 *ind_lo, *ind_hi; static u64 *ind_cell; static size_t nind, capind;

static inline void add_point(u64 m, u128 Hlo, u128 Hhi) {
  if (m < 65536) {
    if (nind == capind) {
      capind = capind ? 2 * capind : 1 << 16;
      ind_lo = realloc(ind_lo, capind * 16); ind_hi = realloc(ind_hi, capind * 16); ind_cell = realloc(ind_cell, capind * 8);
      if (!ind_lo || !ind_hi || !ind_cell) die("alloc ind");
    }
    ind_lo[nind] = Hlo; ind_hi[nind] = Hhi; ind_cell[nind] = m; nind++;
    return;
  }
  int j = 63 - __builtin_clzll(m);
  if (j - 16 >= NOCT) die("cell beyond block table");
  u64 L = 1ULL << (j - 14);
  u64 i = (m - (1ULL << j)) >> (j - 14);
  Mom *b = &mom[((u64)(j - 16) << 14) | i];
  u64 W0 = (1ULL << j) + i * L - 1 + L / 2;
  u128 W0F = (u128)W0 << F;
  i128 dlo = (i128)Hlo - (i128)W0F, dhi = (i128)Hhi - (i128)W0F;
  u64 width = (u64)(Hhi - Hlo);
  if ((Hhi - Hlo) >> 40) die("enclosure wider than 2^-50");
  b->cnt++;
  b->s1lo += dlo >> 26;                 /* floor(2^64 Delta_lo) */
  b->s1hi += (dhi >> 26) + 1;           /* > 2^64 Delta_hi */
  i64 D2 = (i64)(dlo >> (F - 32));
  b->s2 += (i128)D2 * D2; b->a2 += (u128)(D2 < 0 ? -D2 : D2);
  i64 D3 = (i64)(dlo >> (F - 16));
  b->s3 += (i128)D3 * D3 * D3; b->q3 += (u128)((i128)D3 * D3); b->a3 += (u128)(D3 < 0 ? -D3 : D3);
  if (width > b->wmax) b->wmax = width;
}

typedef struct { u64 cell; u128 lo, hi; } Ind;
static int ind_cmp(const void *a, const void *b) {
  const Ind *x = a, *y = b;
  if (x->cell != y->cell) return x->cell < y->cell ? -1 : 1;
  if (x->lo != y->lo) return x->lo < y->lo ? -1 : 1;
  return 0;
}
static void write_moments(const char *base) {
  char fn[1024];
  Ind *tmp = malloc(nind * sizeof(Ind)); if (!tmp) die("alloc tmp");
  for (size_t k = 0; k < nind; k++) { tmp[k].cell = ind_cell[k]; tmp[k].lo = ind_lo[k]; tmp[k].hi = ind_hi[k]; }
  qsort(tmp, nind, sizeof(Ind), ind_cmp);              /* canonical order, independent of the enumeration order */
  for (size_t k = 0; k < nind; k++) { ind_cell[k] = tmp[k].cell; ind_lo[k] = tmp[k].lo; ind_hi[k] = tmp[k].hi; }
  free(tmp);
  snprintf(fn, sizeof fn, "%s.blk", base);
  FILE *f = fopen(fn, "wb"); if (!f) die("open blk");
  u64 nb = NBLK; fwrite(&nb, 8, 1, f); fwrite(mom, sizeof(Mom), NBLK, f); fclose(f);
  snprintf(fn, sizeof fn, "%s.ind", base);
  f = fopen(fn, "wb"); if (!f) die("open ind");
  u64 ni = nind; fwrite(&ni, 8, 1, f);
  for (size_t k = 0; k < nind; k++) { fwrite(&ind_cell[k], 8, 1, f); fwrite(&ind_lo[k], 16, 1, f); fwrite(&ind_hi[k], 16, 1, f); }
  fclose(f);
}
