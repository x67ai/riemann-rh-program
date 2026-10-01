/* gen.c -- independent generator for the integer-greedy system S5(rho), rho = P/Q (read-O, Session 40).
   Rule (NOTE l.54-56): m_n = max(0, floor(rho(n-1) + 1 - N(n-1) - A(n) + 1/2)), a_n = A(n) + m_n, N(n) = N(n-1) + a_n.
   Exact: num = 2P(n-1) + 3Q - 2Q(N(n-1)+A(n)); m = num>=0 ? num/(2Q) : 0.  QE(n) = Q N(n) - P n - (Q-P).
   A(n) by a multiplicative push sieve: each copy of g-prime q multiplies the series by 1/(1-q^-s) over the whole array.
   usage: gen X P Q outprefix   (writes outprefix.a16 = a_1..a_X as uint16, outprefix.gp = (uint32 n, uint8 m) records) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
typedef struct { uint64_t v; double w; } HE;
static HE *hp; static size_t hn = 0, hcap = 0;
static void hpush(uint64_t v, double w){ if(hn==hcap){hcap=hcap?2*hcap:1024; hp=realloc(hp,hcap*sizeof(HE));}
  size_t i=hn++; while(i){size_t p=(i-1)/2; if(hp[p].v<=v)break; hp[i]=hp[p]; i=p;} hp[i].v=v; hp[i].w=w; }
static HE hpop(void){ HE top=hp[0], x=hp[--hn]; size_t i=0; for(;;){size_t l=2*i+1,r=l+1,s=i; uint64_t sv=x.v;
  if(l<hn&&hp[l].v<sv){s=l;sv=hp[l].v;} if(r<hn&&hp[r].v<sv){s=r;} if(s==i)break; hp[i]=hp[s]; i=s;} if(hn) hp[i]=x; return top; }
int main(int argc, char **argv){
  if(argc<5){fprintf(stderr,"usage: gen X P Q outprefix\n");return 1;}
  uint64_t X=strtoull(argv[1],0,10); int64_t P=atoll(argv[2]), Q=atoll(argv[3]); const char *pre=argv[4];
  uint16_t *a=calloc(X+1,sizeof(uint16_t)); if(!a){fprintf(stderr,"alloc\n");return 1;}
  /* odd-only composite bit sieve: bit (n>>1)&7 of byte n>>4 set iff odd n is composite */
  uint8_t *cs=calloc((X>>4)+2,1); if(!cs){fprintf(stderr,"alloc cs\n");return 1;}
  for(uint64_t p=3;p*p<=X;p+=2) if(!((cs[p>>4]>>((p>>1)&7))&1)) for(uint64_t j=p*p;j<=X;j+=2*p) cs[j>>4]|=(uint8_t)(1u<<((j>>1)&7));
  char fn[1024]; snprintf(fn,sizeof fn,"%s.gp",pre); FILE *fg=fopen(fn,"wb");
  a[1]=1; int64_t N=1; uint64_t sites=0,mult=0,ncomp=0,mhist[8]={0},pi=0,primeg=0; int overflow=0;
  uint64_t fnv=1469598103934665603ULL, fnvg=1469598103934665603ULL;
  int64_t supQE=-(1LL<<62), infQE=(1LL<<62); uint64_t argsup=0; uint16_t amax=0; uint64_t argamax=0;
  double psi=0, psic=0, dmax=-1e300, dmin=1e300; uint64_t dec=10; int64_t recQE=-(1LL<<62);
  int64_t QEprev=Q*1-P*1-(Q-P); /* QE(1) */
  printf("# gen X=%llu rho=%lld/%lld\n",(unsigned long long)X,(long long)P,(long long)Q);
  printf("# records of E for n>=1e5: n a_n E(n-1) E(n) m_n\n");
  for(uint64_t n=2;n<=X;n++){
    int isp = (n==2) || (n%2==1 && !((cs[n>>4]>>((n>>1)&7))&1)); pi+=isp;
    int64_t A=a[n]; int64_t num=2*P*(int64_t)(n-1)+3*Q-2*Q*(N+A); int64_t m = num>=0 ? num/(2*Q) : 0;
    if(m>0){ sites++; mult+=m; mhist[m<7?m:7]++; primeg+=isp;
      /* composite? trial division is cheap enough only for small n; flag by smallest factor */
      { int comp = (n>2 && (n%2==0 || ((cs[n>>4]>>((n>>1)&7))&1))); if(comp){ncomp++; if(ncomp<=30) printf("# composite g-prime #%llu: %llu (m=%lld)\n",(unsigned long long)ncomp,(unsigned long long)n,(long long)m);} }
      uint32_t n32=(uint32_t)n; uint8_t m8=(uint8_t)m; fwrite(&n32,4,1,fg); fwrite(&m8,1,1,fg);
      for(int64_t c=0;c<m;c++) for(uint64_t j=n;j<=X;j+=n){ uint32_t s=(uint32_t)a[j]+a[j/n]; if(s>65535) overflow=1; a[j]=(uint16_t)s; }
      double lq=log((double)n); unsigned __int128 pw=(unsigned __int128)n*n; while(pw<=X){ hpush((uint64_t)pw, m*lq); pw*=n; }
      { double y=m*lq - psic; double t=psi+y; psic=(t-psi)-y; psi=t; }
    }
    while(hn && hp[0].v==n){ HE e=hpop(); double y=e.w-psic; double t=psi+y; psic=(t-psi)-y; psi=t; }
    uint16_t an=a[n]; if(an>amax){amax=an;argamax=n; if(n>=100000) printf("# a-record n=%llu a_n=%u\n",(unsigned long long)n,an);}
    N+=an; int64_t QE=Q*N-P*(int64_t)n-(Q-P);
    if(QE>supQE){supQE=QE;argsup=n;} if(QE<infQE) infQE=QE;
    if(n>=100000 && QE>recQE){ recQE=QE; printf("R %llu %u %.4f %.4f %lld\n",(unsigned long long)n,an,(double)QEprev/Q,(double)QE/Q,(long long)m); }
    double D=psi-(double)n; if(D>dmax)dmax=D; if(D-1.0<dmin)dmin=D-1.0;
    QEprev=QE;
    fnv^=an; fnv*=1099511628211ULL; if(m>0){ fnvg^=n; fnvg*=1099511628211ULL; fnvg^=(uint64_t)m; fnvg*=1099511628211ULL; }
    if(n==dec || n==X){
      printf("D x=%llu N=%lld supE=%.4f@%llu infE(real)=%.4f maxa=%u@%llu sites=%llu mult=%llu comp=%llu supDpsi=%.6g infDpsi=%.6g hashA=%016llx hashG=%016llx ovf=%d pi=%llu primeg=%llu\n",
        (unsigned long long)n,(long long)N,(double)supQE/Q,(unsigned long long)argsup,(double)infQE/Q-(double)P/Q,amax,(unsigned long long)argamax,
        (unsigned long long)sites,(unsigned long long)mult,(unsigned long long)ncomp,dmax,dmin,(unsigned long long)fnv,(unsigned long long)fnvg,overflow,(unsigned long long)pi,(unsigned long long)primeg);
      fflush(stdout); if(n==dec) dec*=10;
    }
  }
  printf("# multiplicity histogram m=1..6,7+:"); for(int i=1;i<8;i++) printf(" %llu",(unsigned long long)mhist[i]); printf("\n");
  fclose(fg); snprintf(fn,sizeof fn,"%s.a16",pre); FILE *fa=fopen(fn,"wb"); fwrite(a,sizeof(uint16_t),X+1,fa); fclose(fa);
  printf("# done overflow=%d\n",overflow); return 0;
}
