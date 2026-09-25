# Multiple Zeta Functions: An Example

Nobushige Kurokawa

We try to construct multiple zeta functions as follows. Let $Z_i(s)$ be usual zeta functions for $i = 1, \ldots, r$: we assume that they are defined by Euler products and meromorphic on $\mathbf{C}$ of finite order with functional equations. Let $m_i : \mathbf{C} \longrightarrow \mathbf{Z}$ denote the multiplicity of zeros and poles of $Z_i(s)$ so that we have the Hadamard expression

$$Z_i(s) = \prod_{\rho \in \mathbf{C}} (s - \rho)^{m_i(\rho)}$$

up to a factor $\exp(P(s))$ for a polynomial $P(s)$. Here we simplify the notation by omitting the usual exponential factor making the convergence, since at the first level we are mainly interested in zeros and poles of (multiple) zeta functions. For more precise studies, it is better to consider such a product via zeta regularized determinant (cf. [2a]). Now we define a "multiple zeta function" by

$$Z_1(s) \otimes \cdots \otimes Z_r(s) = \prod_{\rho_i \in \mathbf{C}} (s - (\rho_1 + \cdots + \rho_r))^{m(\rho_1, \ldots, \rho_r)}$$

where

$$m(\rho_1, \ldots, \rho_r) = m_1(\rho_1) \cdots m_r(\rho_r) \times \left\{ \begin{array}{ll}
1 & \text{if all } \Im(\rho_i) \geq 0, \\
(-1)^{r-1} & \text{if all } \Im(\rho_i) < 0, \\
0 & \text{otherwise.}
\end{array} \right.$$

It is not difficult to see that $Z_1(s) \otimes \cdots \otimes Z_r(s)$ has an Euler product expression at least formally, but we must remark that the above "parity condition" is crucial to have a neat Euler product (cf. [2b, p.336]). As noted in [2b] and [2c] these multiple zeta functions would be considered to be associated to multiple categories of Ehresmann (or higher stacks

Received October 20, 1990.

---

of Grothendieck). Instead of treating the general case, in this paper we examine the following simple example

$$\left(1 - M^{-s}\right)^{\otimes r} = \left(1 - M^{-s}\right) \otimes \cdots \otimes \left(1 - M^{-s}\right) \quad (r \text{ copies})$$

for a positive real number $M > 1$ and $r = 2,3,\ldots$, which may be called a multiple hyperbolic sine function. This case is directly related to the multiple gamma function $\Gamma_r(z)$ of Barnes [1] revivaled by Shintani [4] and Vignéras [5]. We see that in this particular case the above mentioned Euler product expression is given by polylogarithm $\operatorname{Li}_r(z) = \sum_{m=1}^{\infty} z^m m^{-r}$ (cf. Lewin [3]). Symbolically speaking the following equalities hold:

$$\left(1 - M^{-s}\right)^{\otimes r} = \exp \left(-\frac{1}{(2\pi i)^{r-1}} \operatorname{Li}_r(M^{-s})\right)$$

$$= \Gamma_r \left(-\frac{s \log M}{2\pi i}\right)^{-1} \Gamma_r \left(r + \frac{s \log M}{2\pi i}\right)^{(-1)^r},$$

which indicate functional equations under $s \to -s$ corresponding to the functional equation of $\operatorname{Li}_r(z)$ under $z \to z^{-1}$.

To fix the notation we define $(1-M_1^{-s}) \otimes \cdots \otimes (1-M_r^{-s})$ for $M_i > 1$ by the following Hadamard expression:

$$\left(1 - M_1^{-s}\right) \otimes \cdots \otimes \left(1 - M_r^{-s}\right)$$

$$= s \prod_{n_i \geq 0} P_r \left(\frac{s}{\omega(n_1,\ldots,n_r)}\right)$$

$$\times \prod_{n_i > 0} P_r \left(-\frac{s}{\omega(n_1,\ldots,n_r)}\right)^{(-1)^{r-1}}$$

where

$$P_r(z) = (1-z) \exp \left(z + \frac{z^2}{2} + \cdots + \frac{z^r}{r}\right)$$

and

$$\omega(n_1,\ldots,n_r) = 2\pi i \left(\frac{n_1}{\log M_1} + \cdots + \frac{n_r}{\log M_r}\right).$$

---

This definition is equivalent to the previous one up to the precise exponential factor making the convergence. We show

Theorem 1. For $M > 1$ and $r = 2,3,\ldots$, we have

$$
\left(1 - M^{-s}\right)^{\otimes r} = \exp\left(-\frac{1}{(2\pi i)^{r-1}}\text{Li}_r(M^{-s})\right.
-\sum_{k=1}^{r-1}\frac{1}{(2\pi i)^{k-1}}h_r^{(k-1)} \left(\frac{s \log M}{2\pi i}\right)\text{Li}_k(M^{-s}) + Q(s))
$$

in $\Re(s) > 0$, where $h_r(T) = (T+r-1)\cdots(T+1)/(r-1)$! is a polynomial belonging to $\mathbf{Q}[T]$ and $Q(T)$ is a polynomial belonging to $\mathbf{C}[T]$ of degree $r$.

We reduce $(1-M^{-s})^{\otimes r}$ to simpler functions. Let

$$h(n,r) = \#\left\{\left(n_1,\ldots,n_r\right); n_i \geq 0 \text{ and } n_1+\cdots+n_r=n\right\}.$$

Then

$$\left(1 - M^{-s}\right)^{\otimes r}$$
$$= s \prod_{n=1}^{\infty} P_r \left(\frac{s \log M}{2\pi in}\right)^h(n,r) P_r \left(-\frac{s \log M}{2\pi in}\right)^{(-1)^{r-1} h(n-r,r)}$$

since

$$\#\left\{\left(n_1,\ldots,n_r\right); n_i > 0 \text{ and } n_1+\cdots+n_r=n\right\} = h(n-r,r).$$

We have

$$h(n,r) = \binom{n+r-1}{n} = \binom{n+r-1}{r-1} = h_r(n)$$

and $h(n-r,r) = h_r(n-r) = (-1)^{r-1} h_r(-n)$. Define

$$F_r(z) = \exp\left(\frac{z^{r-1}}{r-1}\right) \prod_{n=1}^{\infty} \left(P_r\left(\frac{z}{n}\right)P_r\left(-\frac{z}{n}\right)^{(-1)^{r-1}}\right)^{n^{r-1}}$$

for $r = 2,3,\ldots$ and put

---

$$
F_1(z) = \prod_{n=1}^{\infty} P_1\left(\frac{z}{n}\right) P_1\left(-\frac{z}{n}\right) = \frac{\sin(\pi z)}{\pi z}.
$$

Then expanding $h_r(T)$ as $\sum_{k=1}^{r} c(r,k) T^{k-1}$ we have

$$
(1-M^{-s})^{\otimes r} = s \prod_{k=1}^{r} \left(P_r\left(\frac{s \log M}{2\pi in}\right) P_r\left(-\frac{s \log M}{2\pi in}\right)^{(-1)^{k-1}}\right)^{c(r,k) n^{k-1}}
$$

$$
= s \prod_{k=1}^{r} F_k\left(\frac{s \log M}{2\pi i}\right)^{c(r,k)} \cdot \exp(R(s))
$$

for a polynomial $R(s)$ of degree at most $r-1$. Thus, Theorem 1 is reduced to the following

**Theorem 2.** For $r=2,3,\ldots$, we have

$$F_r(z) = \exp\left(-\frac{(r-1)!}{(2\pi i)^{r-1}}\sum_{k=0}^{r-1} \frac{(2\pi i)^k}{k!} z^k \text{Li}_{r-k}(e^{-2\pi iz})$$

$$
+\frac{\pi i}{r} z^r + \frac{(r-1)!}{(2\pi i)^{r-1}} \zeta(r))
$$

in $\Im(z)<0$.

**Proof.** By definition

$$\log F_r(z) = \frac{z^{r-1}}{r-1} + \sum_{n=1}^{\infty} n^{r-1}(\log\left(1-\frac{z}{n}\right)+(-1)^{r-1} \log\left(1+\frac{z}{n}\right)$$

$$
+ \sum_{k=1}^{r} \frac{1}{k}\left(\frac{z}{n}\right)^k (1+(-1)^{k+r-1}).
$$

(Notice that the term $k=r$ vanishes, so $P_r(z)$ can be replaced by

---

$P_{r-1}(z)$ in the definition of $F_r(z)$. Hence

$$\frac{F'_r(z)}{F_r(z)} = z^{r-2}$$

$$+ \sum_{n=1}^{\infty} n^{r-1} \left( \frac{1}{z-n} + \frac{(-1)^{r-1}}{z+n} \right)$$

$$+ \frac{1}{n} \sum_{k=1}^{r} \left( \frac{z}{n} \right)^{k-1} (1 + (-1)^{k+r-1})$$

$$= z^{r-1} \left( \frac{1}{z} + \sum_{n=1}^{\infty} \frac{2z}{z^2 - n^2} \right)$$

$$= z^{r-1} \pi \cot(\pi z).$$

This function is holomorphic in $\Im(z) < 0$ and finite at $z = 0$, so noting $F_r(0) = 1$ we have

$$F_r(z) = \exp \left( \int_0^z u^{r-1} \pi \cot(\pi u) du \right)$$

where we take the integral on the line $u = tz$ for $0 \leq t \leq 1$. We denote the integral by $I(z)$, and we calculate it. Since $\Im(z) < 0$, for $t > 0$ we have

$$\cot(\pi tz) = i \left( 1 + 2 \sum_{m=1}^{\infty} e^{-2\pi imzt} \right).$$

By repeated integration by parts, for $\alpha \in \mathbf{C} - \{0\}$

$$\int_0^1 t^{r-1} e^{\alpha t} dt = (-1)^{r-1}(r-1)! \frac{e^\alpha}{\alpha^r} \left( \sum_{k=0}^{r-1} \frac{(-1)^k}{k!} \alpha^k - e^{-\alpha} \right).$$

Hence

$$I(z) = i\pi z^r \int_0^1 t^{r-1} \left( 1 + 2 \sum_{m=1}^{\infty} e^{-2\pi imzt} \right) dt$$

$$= -\frac{(r-1)!}{(2\pi i)^{r-1}} \sum_{k=0}^{r-1} \frac{(2\pi i)^k}{k!} z^k \mathrm{Li}_{r-k}\left(e^{-2\pi iz}\right) + \frac{\pi i}{r} z^r + \frac{(r-1)!}{(2\pi i)^{r-1}} \zeta(r).$$

Q.E.D.

---

Remarks.

(1) According to Lewin [3, p.30] the above expression for $F_2(z)$ was essentially obtained by Hölder (1928): our $F_2(z)$ is same to $F(z)$ noted there, and using the double gamma function $\Gamma_2(z)$ of Barnes [1] (see Shintani [4] or Vignéras[5]) we have

$$F_2(z) = \frac{\Gamma_2(z)}{\Gamma_2(2-z)} 2\sin(\pi z).$$

Similarly the essential part of $F_r(z)$ is given by

$$(\Gamma_r(z)^{(-1)^r} \Gamma_r(r-z)^{-1})^{(r-1)!}$$

using the multiple gamma function $\Gamma_r(z)$.

(2) In [4], Shintani studied an analogue of $F_2(z)$ associated to a real quadratic number field. He conjectured the algebraicity of its values at $z$ belonging to that field, and proved it in some cases. In our case it may be interesting to investigate whether $F_2(z)$ is algebraic for each rational number $z$. (Here the "real quadratic field" is $\mathbf{Q} \oplus \mathbf{Q}$.) For example $F_2(1/4) \in \bar{\mathbf{Q}}$ is equivalent to $\sum_{m:\text{odd}} (-1)^{(m-1)/2} m^{-2} = \pi \log \alpha$ for an $\alpha \in \bar{\mathbf{Q}}$. In fact, as in the proof of Theorem 2, we see that for $0 < z < 1$

$$F_2(z) = (2\sin(\pi z))^z \exp\left(\frac{1}{2\pi} \sum_{m=1}^{\infty} \frac{\sin(2\pi mz)}{m^2}\right),$$

hence

$$F_2\left(\frac{1}{4}\right) = 2^{1/8} \exp\left(\frac{1}{2\pi} \sum_{m:\text{odd}} (-1)^{(m-1)/2} m^{-2}\right).$$

It is also written as

$$F_2\left(\frac{1}{4}\right) = 2^{1/8} \exp\left(\frac{3}{\pi^3} \zeta_{\mathbf{Q}(i)}(2)\right) = 2^{1/8} \exp\left(-3\zeta_{\mathbf{Q}(i)}'(-1)\right).$$

In particular, the previous property is equivalent to $\zeta_{\mathbf{Q}(i)}(2) = \frac{\pi^3}{6} \log \alpha$ or $\zeta_{\mathbf{Q}(i)}'(-1) = -\frac{1}{6} \log \alpha$.

(3) We notice that the case of $(1-M_1^{-s}) \otimes \cdots \otimes (1-M_r^{-s})$ is not so simple. For example, let $M,N > 1$ and assume that $\log M/\log N$ is irrational and $\liminf_{m \to \infty} \| m \log M/\log N \|^{1/m} \geq 1$, where $\| x \|= min $n \in \mathbf{Z}$ |x-n|. Then

$$
(1-M^{-s}) \otimes (1-N^{-s}) = \exp\left(\frac{1}{2i} \sum_{m=1}^{\infty} \frac{1}{m} \cot\left(\pi \frac{m \log M}{\log N}\right) M^{-ms}\right.
+\frac{1}{2i} \sum_{n=1}^{\infty} \frac{1}{n} \cot\left(\pi \frac{n \log N}{\log M}\right) N^{-ns}
$$

$$
+\frac{1}{2} \log(1-M^{-s}) +\frac{1}{2} \log(1-N^{-s})
$$

+ $Q(s)$)

in $\Re(s) > 0$ with a certain quadratic polynomial $Q(s)$. The above diophantine condition is satisfied if $M$ (resp. log $M$) and $N$ (resp. log $N$) are algebraic. Unfortunately, this result is beyond the scope of this paper, and it is properly treated from a viewpoint generally accessible to $Z_1(s) \otimes \cdots \otimes Z_r(s)$.

(4) Infinite products of zeta functions such as $\prod_{m=0}^{\infty} \zeta(s+m)^{a(m)}$ for a polynomial $a(T) \in \mathbf{Z}[T]$ are expressed by using $\zeta(s) \otimes \Gamma_r(s)$. This example is meromorphic on $\mathbf{C}$, and it is investigated also from the viewpoint of [2d].

(5) Above calculations for Theorems 1 and 2 imply that the "gamma factor" of each Selberg zeta function is expressed as a product of multiple gamma functions generalizing the result of Vignéras [5].

(6) The "multiple sine function" $F_r(z)$ ($r \geq 2$) satisfies the following algebraic differential equation:

$$F''_r(z) F_r(z) - (1-z^{1-r}) F'_r(z)^2 - (r-1)z^{-1} F'_r(z) F_r(z)$$

$$
=-\pi^2 z^{r-1} F_r(z)^2.
$$

This fact seems to be remarkable when we recall that multiple gamma functions do not satisfy any algebraic differential equation according to Barnes.

## References

[1] E.W. Barnes, On the theory of the multiple gamma function, Trans. Cambridge Philos. Soc., 19 (1904), 374-425.

[2a] N. Kurokawa, Parabolic components of zeta functions, Proc. Japan Acad., 64A (1988), 21-24.

[2b] _____, On some Euler products (I), Proc. Japan Acad., 60A (1984), 335-338.

---

[2c] ____, Special values of Selberg zeta functions, Contemporary Mathematics, 83 (1989), 133-150.

[2d] ____, Analyticity of Dirichlet series over prime powers, Springer Lecture Notes in Mathematics, 1434 (1990), 168-177.

[3] L. Lewin, “Polylogarithms and Associated Functions”, North-Holland, 1981.

[4] T. Shintani, On a Kronecker limit formula for real quadratic fields, J. Fac. Sci. Univ. Tokyo, 24 (1977), 167-199.

[5] M.-F. Vignéras, L'équation fonctionnelle de la fonction zêta de Selberg du groupe modulaire PSL(2,Z), Astérisque, 61 (1979), 235-249.

Department of Mathematics
Tokyo Institute of Technology
Oh-okayama, Meguro, Tokyo 152
Japan

Current Address:
Department of Mathematics
Faculty of Science
University of Tokyo
Hongo, Tokyo 113
Japan