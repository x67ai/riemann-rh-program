// twsumO.go — Job 2 part A (Opus 5) independent evaluator of the D4 sign-channel datum
//
//   W_zeta(f_{t,L}) = ghat(i/2) + ghat(-i/2) + ARCH_zeta(t, L) - P_X(g_t)
//   P_X(g_t) = sum_{n <= X} w_n cos(t log n),  w_n = 2 Lambda(n) n^{-1/2} a(log n),
//   a(x) = L^{-3} A(x/L),  A(v) = int B'(w) B'(w - v) dw,  B(v) = Z^{-1} exp(-1/(1 - 4v^2)) on |v| < 1/2,
//   X = floor(e^L),  ARCH = (1/(2 pi L^3)) int eta^2 Bhat(eta)^2 [Re psi(1/4 + i r/2) - log pi] d eta, r = t + eta/L
//
// written from the definitions of results/c2-m6/m6-rung1-note.md section 1 (identity (1.1), (1.2)) and
// results/c2-m2/separation-note.md section 0.1; NOT derived from d4_twisted_sum.rs or twisted_sum.rs.
//
// Independent design choices (against Job 1's harness):
//   * phase in TURNS (units of 2 pi), not radians: t log n / (2 pi) = k * frac(t ln2 / 2pi) + frac(t log m0 / 2pi) + t u / 2pi
//     with m0 = 1 + i/4096 and u = log(m/m0) = 2 atanh(z); the two "large" pieces are computed ONCE PER HEIGHT
//     with math/big at 320 bits (own pi by Machin, own log by the atanh series), so the per-term work in
//     double-double is only t * u / 2pi with |u| <= 1.23e-4 — no dd representation of log n (<= 28.35) is ever formed.
//   * 4097-entry table (not 257), built from big.Float, not from a hard-coded constant list.
//   * A(v) by tanh-sinh quadrature with A, A', A'' tabulated and QUINTIC Hermite interpolation.
//   * odd-only segmented byte sieve, dynamic segment scheduling; dd (two-sum) accumulation, not Neumaier.
//   * Bhat by composite Gauss-Legendre; eta-integral by composite Gauss-Legendre; own complex digamma
//     (recurrence + asymptotic series), no mpmath.
//   * DH coefficients by the divisor recursion on a(n) = (1, kappa, -kappa, -1, 0) by n mod 5, own code.
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"math"
	"math/big"
	"math/cmplx"
	"os"
	"runtime"
	"sort"
	"sync"
	"sync/atomic"
	"time"
)

// ---------------------------------------------------------------- double-double
type dd struct{ h, l float64 }

func twoSum(a, b float64) (float64, float64) {
	s := a + b
	bb := s - a
	e := (a - (s - bb)) + (b - bb)
	return s, e
}
func quickTwoSum(a, b float64) (float64, float64) {
	s := a + b
	e := b - (s - a)
	return s, e
}
func twoProd(a, b float64) (float64, float64) {
	// float64(...) forces rounding: the Go compiler on arm64 otherwise fuses a*b with a later add/sub into
	// an FMA across statements (Go spec, "Arithmetic operators"), which silently breaks error-free transforms
	// (found in this program's first build: p1 - round(p1) was fused with t*v.h, a 1.7e-20*t phase error).
	p := float64(a * b)
	e := math.FMA(a, b, -p)
	return p, e
}
func ddAdd(x, y dd) dd {
	s, e := twoSum(x.h, y.h)
	t, f := twoSum(x.l, y.l)
	e += t
	s, e = quickTwoSum(s, e)
	e += f
	s, e = quickTwoSum(s, e)
	return dd{s, e}
}
func ddMul(x, y dd) dd {
	p, e := twoProd(x.h, y.h)
	e += x.h*y.l + x.l*y.h
	p, e = quickTwoSum(p, e)
	return dd{p, e}
}

// ---------------------------------------------------------------- big-float constants
const prec = 320

func bf(x float64) *big.Float { return new(big.Float).SetPrec(prec).SetFloat64(x) }

// atanh(y) = sum y^(2j+1)/(2j+1), |y| <= 1/3
func bigAtanh(y *big.Float) *big.Float {
	sum := new(big.Float).SetPrec(prec)
	y2 := new(big.Float).SetPrec(prec).Mul(y, y)
	term := new(big.Float).SetPrec(prec).Set(y)
	eps := new(big.Float).SetPrec(prec).SetMantExp(bf(1), -prec-8)
	for j := 0; j < 10000; j++ {
		q := new(big.Float).SetPrec(prec).Quo(term, bf(float64(2*j+1)))
		sum.Add(sum, q)
		term.Mul(term, y2)
		if new(big.Float).Abs(q).Cmp(eps) < 0 && j > 3 {
			break
		}
	}
	return sum
}

// log(1 + x) = 2 atanh(x / (2 + x)), x in [0, 1]
func bigLog1p(x *big.Float) *big.Float {
	den := new(big.Float).SetPrec(prec).Add(bf(2), x)
	y := new(big.Float).SetPrec(prec).Quo(x, den)
	r := bigAtanh(y)
	return r.Mul(r, bf(2))
}

// atan(1/k) = sum (-1)^j / ((2j+1) k^(2j+1))
func bigAtanInv(k float64) *big.Float {
	sum := new(big.Float).SetPrec(prec)
	x := new(big.Float).SetPrec(prec).Quo(bf(1), bf(k))
	x2 := new(big.Float).SetPrec(prec).Mul(x, x)
	term := new(big.Float).SetPrec(prec).Set(x)
	for j := 0; j < 400; j++ {
		q := new(big.Float).SetPrec(prec).Quo(term, bf(float64(2*j+1)))
		if j%2 == 0 {
			sum.Add(sum, q)
		} else {
			sum.Sub(sum, q)
		}
		term.Mul(term, x2)
	}
	return sum
}

var bigPi, bigTwoPi, bigLn2 *big.Float

func initBig() {
	a := bigAtanInv(5)
	a.Mul(a, bf(16))
	b := bigAtanInv(239)
	b.Mul(b, bf(4))
	bigPi = new(big.Float).SetPrec(prec).Sub(a, b)
	bigTwoPi = new(big.Float).SetPrec(prec).Mul(bigPi, bf(2))
	bigLn2 = bigLog1p(bf(1))
}

// split a big.Float into a double-double (h = RN(x), l = RN(x - h))
func toDD(x *big.Float) dd {
	h, _ := x.Float64()
	r := new(big.Float).SetPrec(prec).Sub(x, bf(h))
	l, _ := r.Float64()
	return dd{h, l}
}

// frac(x) in [-1/2, 1/2)
func bigFracSym(x *big.Float) *big.Float {
	// floor(x + 1/2)
	y := new(big.Float).SetPrec(prec).Add(x, bf(0.5))
	iv, _ := y.Int(nil) // truncates toward zero
	fl := new(big.Float).SetPrec(prec).SetInt(iv)
	if fl.Cmp(y) > 0 { // negative non-integer: trunc > floor
		fl.Sub(fl, bf(1))
	}
	return new(big.Float).SetPrec(prec).Sub(x, fl)
}

// ---------------------------------------------------------------- per-height phase tables (turns)
const TB = 4096 // table resolution

type phaseTab struct {
	t      float64
	aTurn  dd           // frac(t ln2 / 2pi)
	tTurn  [TB + 1]dd   // frac(t log(1 + i/TB) / 2pi)
	logTab [TB + 1]float64 // log(1 + i/TB) as double (for the weight only)
	inv2pi dd
	ln2    float64
}

func newPhaseTab(t float64) *phaseTab {
	pt := &phaseTab{t: t}
	bt := bf(t)
	x := new(big.Float).SetPrec(prec).Mul(bt, bigLn2)
	x.Quo(x, bigTwoPi)
	pt.aTurn = toDD(bigFracSym(x))
	for i := 0; i <= TB; i++ {
		lg := bigLog1p(new(big.Float).SetPrec(prec).Quo(bf(float64(i)), bf(TB)))
		pt.logTab[i], _ = lg.Float64()
		y := new(big.Float).SetPrec(prec).Mul(bt, lg)
		y.Quo(y, bigTwoPi)
		pt.tTurn[i] = toDD(bigFracSym(y))
	}
	pt.inv2pi = toDD(new(big.Float).SetPrec(prec).Quo(bf(1), bigTwoPi))
	pt.ln2, _ = bigLn2.Float64()
	return pt
}

var c23 dd // 2/3 as dd

// phaseTurns returns (frac(t log n / 2pi) as hi + lo in [-1/2, 1/2]) and log n (double, for the weight)
func (pt *phaseTab) phaseTurns(n float64) (float64, float64, float64) {
	fr, ex := math.Frexp(n) // n = fr 2^ex, fr in [0.5, 1)
	m := 2 * fr
	k := ex - 1
	i := int((m-1)*TB + 0.5)
	m0 := 1 + float64(i)/TB
	s := m - m0 // exact (Sterbenz)
	dh, dl := twoSum(m, m0)
	q1 := s / dh
	r := math.FMA(-q1, dh, s) // exact remainder
	r -= q1 * dl
	q2 := r / dh
	zh, zl := quickTwoSum(q1, q2)
	z := dd{zh, zl}
	// u = 2 atanh z = 2z + (2/3) z^3 + (2/5) z^5 + (2/7) z^7
	z2 := ddMul(z, z)
	z3 := ddMul(z2, z)
	t3 := ddMul(z3, c23)
	zz := zh * zh
	z5 := zz * zz * zh
	small := 0.4*z5 + (2.0/7.0)*z5*zz
	u := ddAdd(dd{2 * zh, 2 * zl}, t3)
	u = ddAdd(u, dd{small, 0})
	v := ddMul(u, pt.inv2pi) // turns per unit t
	p1, e1 := twoProd(pt.t, v.h)
	p2, e2 := twoProd(pt.t, v.l)
	j := math.Round(p1)
	f1 := p1 - j // exact
	kf := float64(k)
	ka, kae := twoProd(kf, pt.aTurn.h)
	j2 := math.Round(ka)
	g := ka - j2 // exact
	kal := kf * pt.aTurn.l
	tt := pt.tTurn[i]
	s1, se1 := twoSum(f1, g)
	s2, se2 := twoSum(s1, tt.h)
	j3 := math.Round(s2)
	s2 -= j3 // exact
	tail := ((se1 + se2) + (e1 + p2)) + ((e2 + kae) + (kal + tt.l))
	hi, lo := twoSum(s2, tail)
	if hi > 0.5 {
		hi -= 1
	} else if hi < -0.5 {
		hi += 1
	}
	logn := kf*pt.ln2 + pt.logTab[i] + u.h
	return hi, lo, logn
}

func cosTurns(hi, lo float64) float64 {
	// cos(2 pi (hi + lo))
	ph := 2 * math.Pi * hi
	pl := 2*math.Pi*lo + 2.4492935982947064e-16*hi
	return math.Cos(ph) - pl*math.Sin(ph)
}

// ---------------------------------------------------------------- the test function
var Zb float64 // normalization, computed

func phiDerivs(w float64) (b, p1, p2, p3 float64) {
	s := 1 - 4*w*w
	if s <= 0 {
		return 0, 0, 0, 0
	}
	b = math.Exp(-1/s) / Zb
	if b == 0 {
		return 0, 0, 0, 0
	}
	is := 1 / s
	p1 = -8 * w * is * is
	p2 = -8*is*is - 128*w*w*is*is*is
	p3 = -384*w*is*is*is - 3072*w*w*w*is*is*is*is
	return
}
func Bp(w float64) float64 { b, p1, _, _ := phiDerivs(w); return b * p1 }
func Bpp(w float64) float64 {
	b, p1, p2, _ := phiDerivs(w)
	return b * (p1*p1 + p2)
}
func Bppp(w float64) float64 {
	b, p1, p2, p3 := phiDerivs(w)
	return b * (p1*p1*p1 + 3*p1*p2 + p3)
}

// tanh-sinh on [a, b]
type tsNode struct{ x, w float64 } // x in (-1,1), weight
var tsNodes []tsNode

func initTS(h float64) {
	tsNodes = tsNodes[:0]
	for k := -int(3.3 / h); k <= int(3.3/h); k++ {
		tau := float64(k) * h
		sh := math.Pi / 2 * math.Sinh(tau)
		x := math.Tanh(sh)
		c := math.Cosh(sh)
		w := h * math.Pi / 2 * math.Cosh(tau) / (c * c)
		if w < 1e-300 {
			continue
		}
		tsNodes = append(tsNodes, tsNode{x, w})
	}
}
func tsInt(f func(float64) float64, a, b float64) float64 {
	c, r := (a+b)/2, (b-a)/2
	s := 0.0
	for _, nd := range tsNodes {
		s += nd.w * f(c+r*nd.x)
	}
	return s * r
}

// A-table: A, A', A'' on v_j = j/NA, quintic Hermite
const NA = 8192

var Atab, A1tab, A2tab [NA + 1]float64

func Adirect(v float64) (float64, float64, float64) {
	if v >= 1 {
		return 0, 0, 0
	}
	a, b := v-0.5, 0.5
	A := tsInt(func(w float64) float64 { return Bp(w) * Bp(w-v) }, a, b)
	A1 := -tsInt(func(w float64) float64 { return Bp(w) * Bpp(w-v) }, a, b)
	A2 := tsInt(func(w float64) float64 { return Bp(w) * Bppp(w-v) }, a, b)
	return A, A1, A2
}

func buildAtab() {
	var wg sync.WaitGroup
	nth := runtime.GOMAXPROCS(0)
	for th := 0; th < nth; th++ {
		wg.Add(1)
		go func(th int) {
			defer wg.Done()
			for j := th; j <= NA; j += nth {
				Atab[j], A1tab[j], A2tab[j] = Adirect(float64(j) / NA)
			}
		}(th)
	}
	wg.Wait()
}

func Ainterp(v float64) float64 {
	if v >= 1 || v <= -1 {
		return 0
	}
	if v < 0 {
		v = -v
	}
	x := v * NA
	j := int(x)
	if j >= NA {
		return 0
	}
	s := x - float64(j)
	h := 1.0 / NA
	y0, y1 := Atab[j], Atab[j+1]
	d0, d1 := A1tab[j]*h, A1tab[j+1]*h
	c0, c1 := A2tab[j]*h*h, A2tab[j+1]*h*h
	// quintic Hermite basis
	s2 := s * s
	s3 := s2 * s
	s4 := s3 * s
	s5 := s4 * s
	h0 := 1 - 10*s3 + 15*s4 - 6*s5
	h1 := s - 6*s3 + 8*s4 - 3*s5
	h2 := 0.5*s2 - 1.5*s3 + 1.5*s4 - 0.5*s5
	h3 := 0.5*s3 - s4 + 0.5*s5
	h4 := -4*s3 + 7*s4 - 3*s5
	h5 := 10*s3 - 15*s4 + 6*s5
	return y0*h0 + d0*h1 + c0*h2 + c1*h3 + d1*h4 + y1*h5
}

// ---------------------------------------------------------------- sieve + sum (zeta)
type acc struct {
	s, l1        dd
	nprimes, npp int64
}

func (a *acc) add(w, c float64) {
	wc := float64(w * c)
	a.s = ddAdd(a.s, dd{wc, math.FMA(w, c, -wc)})
	a.l1 = ddAdd(a.l1, dd{math.Abs(w), 0})
}

func simpleSieve(n int) []int {
	comp := make([]bool, n+1)
	var ps []int
	for i := 2; i <= n; i++ {
		if !comp[i] {
			ps = append(ps, i)
			for j := i * i; j <= n; j += i {
				comp[j] = true
			}
		}
	}
	return ps
}

func sumZeta(pt *phaseTab, L float64, X int64, nth int) (acc, float64) {
	sq := int64(math.Sqrt(float64(X)))
	for (sq+1)*(sq+1) <= X {
		sq++
	}
	for sq*sq > X {
		sq--
	}
	base := simpleSieve(int(sq) + 1)
	invL := 1 / L
	norm := 2 / (L * L * L)
	// prime powers p^k, k >= 2
	var tot acc
	for _, p := range base {
		if int64(p) > sq {
			break
		}
		lp := math.Log(float64(p))
		for q := int64(p) * int64(p); q <= X; q *= int64(p) {
			hi, lo, lgn := pt.phaseTurns(float64(q))
			w := norm * lp / math.Sqrt(float64(q)) * Ainterp(lgn*invL)
			tot.add(w, cosTurns(hi, lo))
			tot.npp++
			if q > X/int64(p) {
				break
			}
		}
	}
	// the prime 2
	{
		hi, lo, lgn := pt.phaseTurns(2)
		w := norm * lgn / math.Sqrt(2) * Ainterp(lgn*invL)
		tot.add(w, cosTurns(hi, lo))
		tot.nprimes++
	}
	// odd primes by segments of S odds: segment g covers odd values 1 + 2(gS + j), j in [0, S)
	const S = 1 << 20
	nOdd := (X + 1) / 2 // odds 1..X
	nseg := (nOdd + S - 1) / S
	var next int64
	res := make([]acc, nth)
	var wg sync.WaitGroup
	oddBase := base[1:] // skip 2
	for th := 0; th < nth; th++ {
		wg.Add(1)
		go func(th int) {
			defer wg.Done()
			buf := make([]byte, S)
			var a acc
			for {
				g := atomic.AddInt64(&next, 1) - 1
				if g >= nseg {
					break
				}
				lo := 1 + 2*g*S // first odd value
				cnt := int64(S)
				if g*S+cnt > nOdd {
					cnt = nOdd - g*S
				}
				hiV := lo + 2*(cnt-1)
				for j := range buf[:cnt] {
					buf[j] = 0
				}
				for _, p := range oddBase {
					pp := int64(p)
					if pp*pp > hiV {
						break
					}
					st := pp * pp
					if st < lo {
						st = ((lo + pp - 1) / pp) * pp
						if st%2 == 0 {
							st += pp
						}
					}
					b := buf[:cnt]
					for idx := (st - lo) / 2; idx < cnt; idx += pp {
						b[idx] = 1
					}
				}
				for j := int64(0); j < cnt; j++ {
					if buf[j] != 0 {
						continue
					}
					n := lo + 2*j
					if n < 3 {
						continue
					}
					nf := float64(n)
					hi, lo2, lgn := pt.phaseTurns(nf)
					w := norm * lgn / math.Sqrt(nf) * Ainterp(lgn*invL)
					a.add(w, cosTurns(hi, lo2))
					a.nprimes++
				}
			}
			res[th] = a
		}(th)
	}
	wg.Wait()
	for _, a := range res {
		tot.s = ddAdd(tot.s, a.s)
		tot.l1 = ddAdd(tot.l1, a.l1)
		tot.nprimes += a.nprimes
		tot.npp += a.npp
	}
	return tot, 0
}

// ---------------------------------------------------------------- DH coefficients
func dhKappa() float64 {
	s5 := math.Sqrt(5)
	return (math.Sqrt(10-2*s5) - 2) / (s5 - 1)
}
func dhA(n int64, kap float64) float64 {
	switch n % 5 {
	case 1:
		return 1
	case 2:
		return kap
	case 3:
		return -kap
	case 4:
		return -1
	}
	return 0
}

func dhLambda(X int64) []float64 {
	kap := dhKappa()
	lam := make([]float64, X+1)
	for n := int64(2); n <= X; n++ {
		lam[n] = dhA(n, kap) * math.Log(float64(n))
	}
	// Lambda(n) = a(n) log n - sum_{d | n, 1 < d < n} Lambda(d) a(n/d)
	amod := [5]float64{0, 1, kap, -kap, -1}
	for d := int64(2); d <= X/2; d++ {
		ld := lam[d]
		if ld == 0 {
			continue
		}
		for m := int64(2); d*m <= X; m++ {
			am := amod[m%5]
			if am != 0 {
				lam[d*m] -= ld * am
			}
		}
	}
	return lam
}

func sumDH(pt *phaseTab, L float64, X int64, lam []float64) acc {
	invL := 1 / L
	norm := 2 / (L * L * L)
	var a acc
	for n := int64(2); n <= X; n++ {
		if lam[n] == 0 {
			continue
		}
		nf := float64(n)
		hi, lo, lgn := pt.phaseTurns(nf)
		w := norm * lam[n] / math.Sqrt(nf) * Ainterp(lgn*invL)
		a.add(w, cosTurns(hi, lo))
		a.nprimes++
	}
	return a
}

// ---------------------------------------------------------------- Gauss-Legendre
func gaussLegendre(n int) ([]float64, []float64) {
	x := make([]float64, n)
	w := make([]float64, n)
	for i := 0; i < n; i++ {
		z := math.Cos(math.Pi * (float64(i) + 0.75) / (float64(n) + 0.5))
		for it := 0; it < 100; it++ {
			p1, p2 := 1.0, 0.0
			for j := 1; j <= n; j++ {
				p3 := p2
				p2 = p1
				p1 = ((2*float64(j)-1)*z*p2 - (float64(j)-1)*p3) / float64(j)
			}
			pp := float64(n) * (z*p1 - p2) / (z*z - 1)
			z1 := z
			z = z1 - p1/pp
			if math.Abs(z-z1) < 1e-16 {
				p1, p2 = 1.0, 0.0
				for j := 1; j <= n; j++ {
					p3 := p2
					p2 = p1
					p1 = ((2*float64(j)-1)*z*p2 - (float64(j)-1)*p3) / float64(j)
				}
				pp = float64(n) * (z*p1 - p2) / (z*z - 1)
				x[i] = z
				w[i] = 2 / ((1 - z*z) * pp * pp)
				break
			}
		}
	}
	return x, w
}

// Bhat(eta) = int B(v) e^{i eta v} dv for complex eta, composite GL on [-1/2, 1/2]
type glRule struct{ x, w []float64 }

func compositeGL(a, b float64, panels, order int) glRule {
	gx, gw := gaussLegendre(order)
	var r glRule
	h := (b - a) / float64(panels)
	for p := 0; p < panels; p++ {
		c := a + (float64(p)+0.5)*h
		for i := range gx {
			r.x = append(r.x, c+gx[i]*h/2)
			r.w = append(r.w, gw[i]*h/2)
		}
	}
	return r
}

var bRule glRule
var bVals []float64

func initBhat() {
	bRule = compositeGL(-0.5, 0.5, 2000, 20)
	bVals = make([]float64, len(bRule.x))
	for i, v := range bRule.x {
		s := 1 - 4*v*v
		if s > 0 {
			bVals[i] = math.Exp(-1/s) / Zb
		}
	}
}
func BhatReal(eta float64) float64 {
	s := 0.0
	for i, v := range bRule.x {
		if bVals[i] != 0 {
			s += bRule.w[i] * bVals[i] * math.Cos(eta*v)
		}
	}
	return s
}
func BhatC(xi complex128) complex128 {
	var s complex128
	for i, v := range bRule.x {
		if bVals[i] != 0 {
			s += complex(bRule.w[i]*bVals[i], 0) * cmplx.Exp(complex(0, 1)*xi*complex(v, 0))
		}
	}
	return s
}

// complex digamma
func digamma(z complex128) complex128 {
	var shift complex128
	for cmplx.Abs(z) < 20 || real(z) < 10 {
		shift -= 1 / z
		z += 1
	}
	b := []float64{1.0 / 6, -1.0 / 30, 1.0 / 42, -1.0 / 30, 5.0 / 66, -691.0 / 2730, 7.0 / 6, -3617.0 / 510}
	iz2 := 1 / (z * z)
	pw := iz2
	s := cmplx.Log(z) - 1/(2*z)
	for k := 1; k <= 8; k++ {
		s -= complex(b[k-1]/float64(2*k), 0) * pw
		pw *= iz2
	}
	return s + shift
}

func bracket(r float64, mode string) float64 {
	if mode == "dh" {
		return real(digamma(complex(0.75, r/2))) + math.Log(5/math.Pi)
	}
	return real(digamma(complex(0.25, r/2))) - math.Log(math.Pi)
}

func arch(t, L float64, mode string, H float64, panelW float64) float64 {
	rule := compositeGL(0, H, int(H/panelW), 20)
	var wg sync.WaitGroup
	nth := runtime.GOMAXPROCS(0)
	part := make([]float64, nth)
	for th := 0; th < nth; th++ {
		wg.Add(1)
		go func(th int) {
			defer wg.Done()
			s := 0.0
			for i := th; i < len(rule.x); i += nth {
				eta := rule.x[i]
				bh := BhatReal(eta)
				f := eta * eta * bh * bh
				s += rule.w[i] * f * (bracket(t+eta/L, mode) + bracket(t-eta/L, mode))
			}
			part[th] = s
		}(th)
	}
	wg.Wait()
	s := 0.0
	for _, p := range part {
		s += p
	}
	return s / (2 * math.Pi * L * L * L)
}

// pole terms 2 Re[h(i/2) conj(h(-i/2))], h(r) = (r - t) Bhat(L (r - t))
func pole(t, L float64) float64 {
	hp := complex(-t, 0.5) * BhatC(complex(L, 0)*complex(-t, 0.5))
	hm := complex(-t, -0.5) * BhatC(complex(L, 0)*complex(-t, -0.5))
	return 2 * real(hp*cmplx.Conj(hm))
}

// ---------------------------------------------------------------- main
func exactDecimal(x float64) string {
	s := new(big.Float).SetFloat64(x).Text('f', 80)
	for len(s) > 1 && s[len(s)-1] == '0' {
		s = s[:len(s)-1]
	}
	if s[len(s)-1] == '.' {
		s = s[:len(s)-1]
	}
	return s
}

func main() {
	mode := flag.String("mode", "zeta", "zeta | dh | selftest | archonly | atest")
	tstr := flag.String("t", "1e6", "height (parsed as a double)")
	L := flag.Float64("L", 10, "bandwidth")
	nth := flag.Int("threads", 8, "threads")
	out := flag.String("out", "", "output JSON")
	nself := flag.Int("n", 5000, "selftest count")
	seed := flag.Uint64("seed", 424242, "selftest seed")
	noArch := flag.Bool("noarch", false, "skip ARCH")
	flag.Parse()
	runtime.GOMAXPROCS(*nth)
	var t float64
	fmt.Sscan(*tstr, &t)
	t0 := time.Now()
	initBig()
	c23 = toDD(new(big.Float).SetPrec(prec).Quo(bf(2), bf(3)))
	initTS(1.0 / 128)
	Zb = 1
	Zb = tsInt(func(v float64) float64 { s := 1 - 4*v*v; if s <= 0 { return 0 }; return math.Exp(-1 / s) }, -0.5, 0.5)
	buildAtab()
	initBhat()
	X := int64(math.Floor(math.Exp(*L)))
	res := map[string]interface{}{
		"program": "checker-O/twsumO.go (Job 2 part A, Opus 5)", "mode": *mode,
		"t_exact": exactDecimal(t), "t_bits": fmt.Sprintf("0x%016x", math.Float64bits(t)),
		"L": *L, "X": X, "threads": *nth, "Z": Zb, "A0": Atab[0],
		"date": time.Now().Format(time.UnixDate),
	}
	pt := newPhaseTab(t)
	res["setup_s"] = time.Since(t0).Seconds()
	switch *mode {
	case "atest":
		// interpolation vs direct quadrature at pseudo-random v; A(0) at two tanh-sinh steps
		st := *seed
		maxe := 0.0
		for i := 0; i < 2000; i++ {
			st ^= st << 13
			st ^= st >> 7
			st ^= st << 17
			v := float64(st>>11) / (1 << 53)
			a, _, _ := Adirect(v)
			e := math.Abs(a - Ainterp(v))
			if e > maxe {
				maxe = e
			}
		}
		res["A_interp_max_abs_err_2000v"] = maxe
		a0h, _, _ := Adirect(0)
		initTS(1.0 / 256)
		a0hh, _, _ := Adirect(0)
		zz := tsInt(func(v float64) float64 { s := 1 - 4*v*v; if s <= 0 { return 0 }; return math.Exp(-1 / s) }, -0.5, 0.5)
		res["A0_h128"] = a0h
		res["A0_h256"] = a0hh
		res["Z_h256"] = zz
		// Parseval: int eta^2 Bhat^2 = 2 pi A(0)
		rule := compositeGL(0, 3000, 1500, 20)
		s := 0.0
		for i, eta := range rule.x {
			b := BhatReal(eta)
			s += rule.w[i] * eta * eta * b * b
		}
		res["parseval_int_eta2_Bhat2"] = 2 * s
		res["parseval_2piA0"] = 2 * math.Pi * Atab[0]
		res["Bhat0"] = BhatReal(0)
	case "nlist":
		var rows [][]interface{}
		for _, a := range flag.Args() {
			var n int64
			fmt.Sscan(a, &n)
			hi, lo, _ := pt.phaseTurns(float64(n))
			rows = append(rows, []interface{}{n, fmt.Sprintf("%.17e", hi), fmt.Sprintf("%.17e", lo)})
		}
		res["selftest_rows"] = rows
	case "selftest":
		// output (n, frac hi, frac lo) for pseudo-random n <= X; checked in mpmath at 50 digits by selftest_check.py
		st := *seed
		var rows [][]interface{}
		for i := 0; i < *nself; i++ {
			st ^= st << 13
			st ^= st >> 7
			st ^= st << 17
			n := int64(2 + st%uint64(X-1))
			hi, lo, _ := pt.phaseTurns(float64(n))
			rows = append(rows, []interface{}{n, fmt.Sprintf("%.17e", hi), fmt.Sprintf("%.17e", lo)})
		}
		res["selftest_rows"] = rows
		res["seed"] = *seed
	case "zeta", "dh":
		ts := time.Now()
		var a acc
		if *mode == "zeta" {
			a, _ = sumZeta(pt, *L, X, *nth)
		} else {
			lam := dhLambda(X)
			kap := dhKappa()
			res["kappa"] = kap
			res["witness_L3"] = lam[3]
			res["witness_L4"] = lam[4]
			res["witness_L6"] = lam[6]
			res["witness_L12"] = lam[12]
			a = sumDH(pt, *L, X, lam)
		}
		res["sum_s"] = time.Since(ts).Seconds()
		res["P"] = a.s.h + a.s.l
		res["P_hi"] = a.s.h
		res["P_lo"] = a.s.l
		res["l1"] = a.l1.h + a.l1.l
		res["n_primes_or_nonzero"] = a.nprimes
		res["n_prime_powers"] = a.npp
		res["n_terms"] = a.nprimes + a.npp
		if !*noArch {
			ta := time.Now()
			ar := arch(t, *L, *mode, 3000, 2)
			ar2 := arch(t, *L, *mode, 2000, 1)
			res["ARCH"] = ar
			res["ARCH_H2000_panel1"] = ar2
			pl := 0.0
			if *mode == "zeta" && t < 1000 {
				pl = pole(t, *L)
				res["pole_note"] = "computed: 2 Re[h(i/2) conj h(-i/2)] by composite GL"
			} else if *mode == "zeta" {
				res["pole_note"] = "not computed (t >= 1000): Lemma-G bound of the record, below 1e-300"
			}
			res["pole"] = pl
			res["W"] = pl + ar - (a.s.h + a.s.l)
			res["arch_s"] = time.Since(ta).Seconds()
		}
	case "archonly":
		for _, m := range []string{"zeta"} {
			res["ARCH_"+m] = arch(t, *L, m, 3000, 2)
		}
	}
	res["wall_s"] = time.Since(t0).Seconds()
	keys := make([]string, 0, len(res))
	for k := range res {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	b, _ := json.MarshalIndent(res, "", " ")
	if *out != "" {
		os.WriteFile(*out, b, 0644)
	}
	if *mode != "selftest" {
		fmt.Println(string(b))
	} else {
		fmt.Printf("selftest: %d rows written to %s\n", *nself, *out)
	}
}
