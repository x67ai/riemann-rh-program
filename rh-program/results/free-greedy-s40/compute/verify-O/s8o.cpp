// s8o.cpp -- independent generator of S8(rho), Opus reader (Session 41).
// Written from CHARTER section 1 only (no code of the unit consulted).
// g-prime with count k so far sits at the lattice point L_k = 1 + (k - 1/2) t, t = 1/rho;
// the next g-integer is min(next composite, L_k) (composite first on a tie).
// Arithmetic: positions as 128-bit unsigned fixed point with F fractional bits,
// rigorous error bounds (in ulps); every composite-vs-lattice decision is certified
// (|diff| > errC + errL) or counted as a FLAG. Composites m = n * p, p = P(m) largest
// g-prime factor, n a "prefix" (g-integer with n * P(n) <= X); every prefix walks the
// g-prime list from P(n) on. Windows [a, b) with b <= a * (1 + 0.9 (q0 - 1)), so all
// factors of a window's composites are already known; window composites std::sort-ed.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <ctime>
typedef unsigned __int128 u128;
typedef __int128 i128;
static const int F = 92;
static u128 ONE, TFX;              // 2^F, round(t 2^F) (|err| <= 1/2 ulp)
static double TD, RHO, ULP, XD;
static u128 XFX;

static inline u128 mulshift(u128 a, u128 b) {          // floor(a b / 2^F)
  uint64_t a0 = (uint64_t)a, a1 = (uint64_t)(a >> 64), b0 = (uint64_t)b, b1 = (uint64_t)(b >> 64);
  u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1, p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
  u128 mid = p01 + p10; u128 midc = (mid < p01) ? ((u128)1 << 64) : 0;
  u128 lo = p00 + (mid << 64); u128 c1 = (lo < p00) ? 1 : 0;
  u128 hi = p11 + (mid >> 64) + midc + c1;
  return (hi << (128 - F)) | (lo >> F);
}
static inline double toD(u128 v) { return (double)(v >> 40) * ldexp(1.0, 40 - F); }
static inline u128 lattice(uint64_t k) { return ONE + (((u128)(2 * k - 1) * TFX) >> 1); }
static inline double lattice_err(uint64_t k) { return (2.0 * k - 1.0) * 0.25 + 1.0; }
static u128 parse_u128(const char* s) { u128 v = 0; for (; *s; ++s) v = v * 10 + (u128)(*s - '0'); return v; }

struct Prefix { u128 N, C; double eN, eC; uint32_t cur; };
static std::vector<uint32_t> PK;   // lattice index of each stored g-prime (p <= X/q0), in order
static std::vector<Prefix> PRE;

// running state
static uint64_t cnt = 1, npr = 0;  // g-integers placed so far (1 included), g-primes so far
static double supE = 0.0, supEx = 1.0;
static double thS = 0.0, thC = 0.0; // theta_P, Neumaier-compensated
static long long flags = 0, ncmp = 0;
static double minratio = 1e300, minabs = 1e300, minrel = 1e300;
static FILE* dumpf = nullptr; static double dumpX = 0;
static std::vector<double> dumpbuf;
// checkpoints
static std::vector<double> CPX; static std::vector<u128> CPF; static size_t cp = 0;
struct Row { double x; uint64_t N, pi; double supE, supEx, theta; };
static std::vector<Row> rows;

static inline void addtheta(double v) {
  double t = thS + v;
  if (fabs(thS) >= fabs(v)) thC += (thS - t) + v; else thC += (v - t) + thS;
  thS = t;
}
static void flushdump() { if (dumpf && !dumpbuf.empty()) { fwrite(dumpbuf.data(), 8, dumpbuf.size(), dumpf); dumpbuf.clear(); } }

static inline void emit(u128 v, bool isprime) {
  while (cp < CPF.size() && v >= CPF[cp]) {
    rows.push_back({CPX[cp], cnt, npr, supE, supEx, thS + thC}); cp++;
  }
  uint64_t j = cnt;                                   // 0-based index of this g-integer
  i128 diff = (i128)(ONE + (u128)j * TFX) - (i128)v;  // (1 + j t - n) 2^F
  double E = RHO * ((double)diff * ULP);              // E(n_j) = j - rho (n_j - 1)
  double vd = toD(v);
  if (E > supE) { supE = E; supEx = vd; }
  cnt++;
  if (dumpf && vd <= dumpX) { dumpbuf.push_back(vd); if (dumpbuf.size() >= (1u << 20)) flushdump(); }
  if (isprime) {
    npr++; addtheta(log(vd));
    uint64_t k = j;
    if (vd <= XD / (1.0 + 0.5 * TD) * 1.000001) PK.push_back((uint32_t)k);
    if (vd * vd <= XD * (1 + 1e-9)) {
      Prefix P; P.N = v; P.eN = lattice_err(k); P.C = mulshift(v, TFX);
      P.eC = (0.5 * vd + TD * P.eN + 2.0) * (1 + 1e-9); P.cur = (uint32_t)(PK.size() - 1);
      PRE.push_back(P);
    }
  }
}
