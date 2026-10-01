/* gen2.c -- second, structurally different generator for S5(P/Q) (read-O, Session 40).
   A(n) by PULL: Omega is completely additive, so D(f) = sum Omega(n) f_n n^-s is a derivation and
   Omega(n) a_n = sum_{d|n, d>1} L(d) a_{n/d},  L(d) = sum_{q^k = d} m_q Omega(q)  (exact integers).
   At step n the d = n term with k = 1 is unknown (it is m_n Omega(n)), so A(n) = [sum_{d|n,1<d<n} L(d)a_{n/d} + L_pow(n)] / Omega(n),
   where L_pow(n) holds the k >= 2 contributions already planted. Checks divisibility by Omega(n) at every n.
   usage: gen2 X P Q   (prints decade lines with the same hashes as gen.c) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc,char**argv){
  uint64_t X=strtoull(argv[1],0,10); int64_t P=atoll(argv[2]),Q=atoll(argv[3]);
  uint32_t *spf=calloc(X+1,4); uint16_t *a=calloc(X+1,2); uint16_t *L=calloc(X+1,2); uint8_t *Om=calloc(X+1,1);
  if(!spf||!a||!L||!Om){fprintf(stderr,"alloc\n");return 1;}
  for(uint64_t i=2;i<=X;i++) if(!spf[i]) for(uint64_t j=i;j<=X;j+=i) if(!spf[j]) spf[j]=(uint32_t)i;
  Om[1]=0; for(uint64_t i=2;i<=X;i++) Om[i]=Om[i/spf[i]]+1;
  a[1]=1; int64_t N=1; uint64_t sites=0,bad=0; uint16_t amax=0; uint64_t argamax=0; int64_t supQE=-(1LL<<62); uint64_t argsup=0, dec=10;
  uint64_t fnv=1469598103934665603ULL, fnvg=1469598103934665603ULL;
  uint64_t pr[16]; int ex[16]; uint64_t divs[200000];
  for(uint64_t n=2;n<=X;n++){
    int k=0; uint64_t t=n; while(t>1){ uint64_t p=spf[t]; int e=0; while(t%p==0){t/=p;e++;} pr[k]=p; ex[k]=e; k++; }
    int nd=1; divs[0]=1;
    for(int i=0;i<k;i++){ int cur=nd; uint64_t pp=1; for(int e=1;e<=ex[i];e++){ pp*=pr[i]; for(int j=0;j<cur;j++) divs[nd++]=divs[j]*pp; } }
    int64_t S=0; for(int j=0;j<nd;j++){ uint64_t d=divs[j]; if(d>1 && d<n && L[d]) S+=(int64_t)L[d]*a[n/d]; }
    S+=L[n]; /* only k>=2 contributions are planted at n before step n */
    if(S % Om[n]){ bad++; } int64_t A=S/Om[n];
    int64_t num=2*P*(int64_t)(n-1)+3*Q-2*Q*(N+A); int64_t m = num>=0 ? num/(2*Q) : 0;
    int64_t an=A+m; a[n]=(uint16_t)an; if(an>65535) bad++;
    if(m>0){ sites++; L[n]+=(uint16_t)(m*Om[n]); unsigned __int128 pw=(unsigned __int128)n*n; while(pw<=X){ L[(uint64_t)pw]+=(uint16_t)(m*Om[n]); pw*=n; }
      fnvg^=n; fnvg*=1099511628211ULL; fnvg^=(uint64_t)m; fnvg*=1099511628211ULL; }
    if(a[n]>amax){amax=a[n];argamax=n;}
    N+=an; int64_t QE=Q*N-P*(int64_t)n-(Q-P); if(QE>supQE){supQE=QE;argsup=n;}
    fnv^=a[n]; fnv*=1099511628211ULL;
    if(n==dec||n==X){ printf("D2 x=%llu N=%lld supE=%.4f@%llu maxa=%u@%llu sites=%llu hashA=%016llx hashG=%016llx nonint=%llu\n",(unsigned long long)n,(long long)N,(double)supQE/Q,(unsigned long long)argsup,amax,(unsigned long long)argamax,(unsigned long long)sites,(unsigned long long)fnv,(unsigned long long)fnvg,(unsigned long long)bad); fflush(stdout); if(n==dec)dec*=10; }
  }
  return 0;
}
