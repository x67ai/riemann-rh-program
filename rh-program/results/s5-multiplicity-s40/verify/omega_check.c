/* omega_check.c -- unit s5-multiplicity-s40, §2.5 and task 3.  INDEPENDENT certification of the S5(4/5) dump by a different
   identity, and its extension to 2X.  For every 2 <= n <= X (X = 10^9) it checks
     (I)  Omega(n) a(n) = sum_{q g-prime, k>=1, q^k | n} m_q Omega(q) a(n/q^k)      (NOTE §2.1 with h = Omega; q = n included)
     (II) m_n = max(0, floor(rho(n-1) + 1 - N(n-1) - A(n) + 1/2)),  A(n) = a(n) - m_n,  rho = 4/5, exact integers;
   by induction (I)+(II) at every n <=> the dump IS S5(4/5) on [1, X] (NOTE §2.5).  For X < n <= 2X it GENERATES: every
   g-prime q dividing such n with q < n is <= X, and n/q^k <= X, so A(n) = acc(n)/Omega(n) from the dump alone (the
   division must be exact -- checked), m_n by the rule.  Segmented (S = 5e7); Omega by a segmented sieve.
   Build: cc -O3 -o omega_check omega_check.c -lm      Usage: omega_check a.u16 gp.u32 X gp_ext.out  */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <sys/stat.h>
int main(int argc,char**argv){
  int fd=open(argv[1],O_RDONLY); struct stat st; fstat(fd,&st); const uint16_t *a=mmap(0,st.st_size,PROT_READ,MAP_SHARED,fd,0);
  uint64_t X=strtoull(argv[3],0,10), X2=2*X, S=50000000ULL; if((uint64_t)st.st_size!=2*(X+1)){fprintf(stderr,"size\n");return 1;}
  FILE *fg=fopen(argv[2],"rb"); fseek(fg,0,SEEK_END); uint64_t ng=ftell(fg)/8; fseek(fg,0,SEEK_SET);
  uint32_t *gq=malloc(ng*4), pr[2]; uint8_t *gom=calloc(ng,1); for(uint64_t i=0;i<ng;i++){ if(fread(pr,4,2,fg)!=2) return 1; if(pr[1]!=1){fprintf(stderr,"m!=1\n");return 1;} gq[i]=pr[0]; }
  fclose(fg); FILE *fe=fopen(argv[4],"wb");
  uint32_t sq=(uint32_t)sqrt((double)X2)+2; uint8_t *cmp=calloc(sq+1,1); uint32_t *sp=malloc(sq*4); int nsp=0;
  for(uint32_t i=2;i<=sq;i++) if(!cmp[i]){ sp[nsp++]=i; for(uint64_t j=(uint64_t)i*i;j<=sq;j+=i) cmp[j]=1; }
  uint32_t *acc=malloc(S*4), *rem=malloc(S*4); uint8_t *om=malloc(S);
  int64_t N=1; uint64_t badI=0, badII=0, badDiv=0, gi=0, next_g=0; /* gi: g-primes with q < L+S processed for omega */
  uint64_t maxa=0,maxan=0; int64_t supE5=-1000000000; uint64_t supEn=0; uint64_t ext_g=0; uint16_t *aext=NULL;
  for(uint64_t L=2; L<=X2; L+=S){
    uint64_t R=L+S; if(R>X2+1) R=X2+1; uint64_t len=R-L;
    for(uint64_t i=0;i<len;i++){ rem[i]=(uint32_t)(L+i); om[i]=0; }
    for(int t=0;t<nsp;t++){ uint64_t p=sp[t]; if(p*p>=R) break; uint64_t s0=((L+p-1)/p)*p;
      for(uint64_t n=s0;n<R;n+=p){ uint64_t i=n-L; while(rem[i]%p==0){ rem[i]/=(uint32_t)p; om[i]++; } } }
    for(uint64_t i=0;i<len;i++) if(rem[i]>1) om[i]++;
    while(next_g<ng && gq[next_g]<R){ gom[next_g]=om[gq[next_g]-L]; next_g++; }   /* Omega(q) for g-primes in this segment */
    memset(acc,0,len*4);
    for(uint64_t t=0;t<next_g;t++){ uint64_t q=gq[t]; uint32_t w=gom[t];
      for(uint64_t qk=q; qk<R; ){ uint64_t j0=(L+qk-1)/qk; if(j0<1) j0=1;
        for(uint64_t j=j0; j*qk<R; j++){ uint64_t n=j*qk; if(j>X) { fprintf(stderr,"read beyond dump\n"); return 1; } acc[n-L]+=w*(uint32_t)a[j]; }
        if(qk>(R-1)/q) break; qk*=q; } }
    for(uint64_t i=0;i<len;i++){ uint64_t n=L+i; int64_t an, mn, A;
      if(n<=X){ an=a[n];
        /* m_n from the list: is n a g-prime? */
        mn=(gi<ng && gq[gi]==n)?1:0; if(mn) gi++;
        if((uint64_t)acc[i]!=(uint64_t)an*om[i]) badI++;
        A=an-mn;
      } else { if(acc[i]%om[i]) { badDiv++; } A=acc[i]/om[i]; an=-1; mn=0; }
      int64_t t2=2*4*(int64_t)(n-1)+2*5*(1-N-A)+5, m=t2>=0? t2/10 : -((-t2+9)/10); if(m<0) m=0;
      if(n<=X){ if(m!=mn) badII++; }
      else { mn=m; an=A+mn; if(mn){ uint32_t o[2]={(uint32_t)n,(uint32_t)mn}; fwrite(o,4,2,fe); ext_g++; }
        if((uint64_t)an>maxa){maxa=an;maxan=n;} int64_t E5=5*(N+an)-4*(int64_t)(n-1)-5; if(E5>supE5){supE5=E5;supEn=n;} }
      N+=an;
      if(n==X) printf("n=X=%llu: N=%lld  checks so far: (I) failures %llu, (II) failures %llu\n",(unsigned long long)n,(long long)N,(unsigned long long)badI,(unsigned long long)badII);
    }
    fprintf(stderr,"segment up to %llu done\n",(unsigned long long)(R-1));
  }
  fclose(fe);
  printf("[X, 2X]: N(2X)=%lld  C(2X)=%lld/5  g-primes in (X,2X]: %llu  max a_n=%llu at %llu  sup E=%lld/5 at %llu  inexact divisions %llu\n",(long long)N,(long long)(5*N-4*(int64_t)X2),(unsigned long long)ext_g,(unsigned long long)maxa,(unsigned long long)maxan,(long long)supE5,(unsigned long long)supEn,(unsigned long long)badDiv);
  return 0;
}
