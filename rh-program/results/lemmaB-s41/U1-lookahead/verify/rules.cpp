// U1-lookahead (Session 41): block generator for S8-type placement rules.
// Blocks [B, p1*B): every factor of a composite in the block is < B, so the block's composites are known before its
// primes are placed (charter §2(d)).  Each composite n = q*m is emitted once, q = the factor of LARGEST INDEX.
// Bookkeeping: a prime is counted at its deficit time x* (first x with T(x) - Nbook(x) = tau); its ACTUAL position
// a in [max(B, x* - W), x*] is chosen by the rule.  Actual N >= bookkeeping N, so E(x-) >= -tau for every rule.
// Usage: rules RHO X RULE TAU [W K J H]   RULE = greedy | early (a = x* - W) | look (anti-clustering, see pick())
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;
static double rho, X, tau, W = 0, H = 2.0; static int K = 1, J = 0; static char rule[16];
static vector<double> G; static vector<int> Lx;          // sorted g-integers < B, largest prime index
static vector<double> P;                                   // prime positions by index
static vector<double> fut;                                 // known g-integers in [Bh, Bh*p_J) (for look-ahead)
static long cnt(const vector<double>& v, double a, double b) {
  return lower_bound(v.begin(), v.end(), b) - lower_bound(v.begin(), v.end(), a); }
static double pick(double xs, double B) {                  // the placement rule
  double lo = max(B, xs - W);
  if (!strcmp(rule, "greedy") || W <= 0) return xs;
  if (!strcmp(rule, "early")) return lo;
  double best = xs, bc = 1e300;                            // "look": minimise known load at the dilates p_j * a
  for (int k = 0; k < K; k++) {
    double a = (K == 1) ? xs : lo + (xs - lo) * k / (K - 1);
    double c = 0;
    for (int j = 0; j < J && j < (int)P.size(); j++) {
      double y = P[j] * a; c += cnt(fut, y - H, y + H) - rho * 2 * H; }
    c += 1e-9 * (xs - a);                                  // tie-break toward the deficit time
    if (c < bc) { bc = c; best = a; }
  }
  return best;
}
int main(int argc, char** argv) {
  rho = atof(argv[1]); X = atof(argv[2]); strncpy(rule, argv[3], 15); tau = atof(argv[4]);
  if (argc > 5) W = atof(argv[5]); if (argc > 6) K = atoi(argv[6]); if (argc > 7) J = atoi(argv[7]);
  if (argc > 8) H = atof(argv[8]);
  double t = 1.0 / rho; double Nbook = 1;                  // N counts the unit 1
  double p1 = 1.0 + tau * t;                               // first deficit time (no early placement for p1)
  G = {1.0}; Lx = {-1}; P = {p1}; Nbook = 2;
  G.push_back(p1); Lx.push_back(0);
  double B = p1, supE = 0, infEm = 1e9, maxgap = 0, lastp = p1; long ncomp = 0;
  double dec = 10; double supdec = 0;
  printf("# rule=%s rho=%.10f X=%g tau=%g W=%g K=%d J=%d H=%g p1=%.6f\n", rule, rho, X, tau, W, K, J, H, p1);
  while (B < X) {
    double Bh = min(B * p1, X);
    vector<pair<double,int>> cv;
    for (int i = 0; i < (int)P.size(); i++) {
      double q = P[i]; if (q * p1 >= Bh) continue;
      size_t lo = lower_bound(G.begin(), G.end(), B / q * (1 - 1e-12)) - G.begin(), hi = lower_bound(G.begin(), G.end(), Bh / q * (1 + 1e-12)) - G.begin();   // widened: B/q may round past a g-integer on the boundary
      for (size_t k = lo; k < hi; k++) if (Lx[k] <= i) { double v = q * G[k]; if (v >= B && v < Bh) cv.push_back({v, i}); }
    }
    sort(cv.begin(), cv.end()); ncomp += cv.size();
    if (!strcmp(rule, "look") && W > 0) {                  // known future g-integers: products of known ones, in [Bh, Bh*pJ)
      fut.clear(); double top = Bh * P[min((size_t)J, P.size()) - 1] + H + 1;
      vector<double> kn(G.begin(), G.end()); for (auto& c : cv) kn.push_back(c.first); sort(kn.begin(), kn.end());
      for (int i = 0; i < (int)P.size() && P[i] < B; i++) {
        size_t lo = lower_bound(kn.begin(), kn.end(), Bh / P[i]) - kn.begin(), hi = lower_bound(kn.begin(), kn.end(), top / P[i]) - kn.begin();
        for (size_t k = lo; k < hi; k++) if (kn[k] > 1) fut.push_back(P[i] * kn[k]);   // with multiplicity: a load proxy
      }
      sort(fut.begin(), fut.end());
    }
    vector<pair<double,int>> np; size_t j = 0;
    while (true) {
      double xs = 1.0 + (Nbook - 1.0 + tau) / rho;         // T(xs) - Nbook = tau
      if (j < cv.size() && cv[j].first <= xs) { Nbook += 1; j++; continue; }
      if (xs >= Bh) break;
      double a = pick(xs, B); P.push_back(a); np.push_back({a, (int)P.size() - 1}); Nbook += 1;
    }
    vector<pair<double,int>> ev(cv); ev.insert(ev.end(), np.begin(), np.end()); sort(ev.begin(), ev.end());
    double N = cnt(G, 0, B + 0.0) ; N = G.size();           // actual N just below B
    for (auto& e : ev) {
      double T = rho * (e.first - 1.0) + 1.0;
      infEm = min(infEm, N - T); N += 1; double E = N - T; supE = max(supE, E);
      while (e.first > dec) { printf("x=%.3g supE=%.4f supE/log2=%.5f\n", dec, supdec, supdec / pow(log(dec), 2)); dec *= 10; }
      supdec = max(supdec, E);
    }
    for (auto& p : np) { if (p.first - lastp > maxgap) maxgap = p.first - lastp; lastp = max(lastp, p.first); }
    vector<double> G2; vector<int> L2; G2.reserve(G.size() + ev.size()); L2.reserve(G.size() + ev.size());
    size_t a = 0, b = 0;
    while (a < G.size() || b < ev.size()) {
      if (b >= ev.size() || (a < G.size() && G[a] <= ev[b].first)) { G2.push_back(G[a]); L2.push_back(Lx[a]); a++; }
      else { G2.push_back(ev[b].first); L2.push_back(ev[b].second); b++; }
    }
    G.swap(G2); Lx.swap(L2); B = Bh;
  }
  printf("x=%.3g supE=%.4f supE/log2=%.5f\n", X, supdec, supdec / pow(log(X), 2));
  printf("RESULT rule=%s tau=%g W=%g K=%d J=%d N=%zu pi=%zu comp=%ld supE=%.4f supE/log2X=%.5f infE(x-)=%.6f maxgap=%.2f\n",
         rule, tau, W, K, J, G.size(), P.size(), ncomp, supE, supE / pow(log(X), 2), infEm, maxgap);
}
