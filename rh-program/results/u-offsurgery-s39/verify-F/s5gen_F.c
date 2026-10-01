/* s5gen_F.c -- orchestrator's own generator of the integer-greedy system S5(num/den) (u-offsurgery-s39 NOTE sec. 2),
   written from the NOTE's definition alone, exact integer arithmetic for the rule (no floating point):
     m_n = max(0, floor(rho*(n-1) + 1 - N(n-1) - A(n) + 1/2)),  a_n = A(n) + m_n,  rho = num/den.
   Output: binary list of g-primes as (uint32 n, uint32 m) pairs to argv[4]; optional uint16 a_n dump to argv[5];
   stdout: counts, max a_n with its n, running records of E in units of 1/den, N(10^k).
   Build: cc -O2 -o s5gen_F s5gen_F.c      Usage: s5gen_F num den X gp.out [a.out] */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int argc, char **argv){
  if(argc<5){fprintf(stderr,"usage: s5gen_F num den X gp.out [a.out]\n");return 1;}
  int64_t num=atoll(argv[1]), den=atoll(argv[2]); uint64_t X=strtoull(argv[3],0,10);
  uint16_t *a=calloc(X+1,sizeof(uint16_t)); if(!a){fprintf(stderr,"oom\n");return 1;}
  FILE *fg=fopen(argv[4],"wb"); FILE *fa=argc>5?fopen(argv[5],"wb"):NULL;
  a[1]=1; int64_t N=1; uint64_t ngp=0, nmult=0, maxa=0, maxan=0; int sat=0;
  int64_t recE=-1000000; uint64_t pw=10;
  for(uint64_t n=2;n<=X;n++){
    int64_t A=a[n];
    /* floor((2*num*(n-1) + 2*den*(1 - N - A) + den) / (2*den)) with floor division */
    int64_t t = 2*num*(int64_t)(n-1) + 2*den*(1 - N - A) + den, d2 = 2*den;
    int64_t m = t>=0 ? t/d2 : -((-t + d2 - 1)/d2);
    if(m>0){
      ngp++; nmult+=m;
      for(int64_t c=0;c<m;c++) for(uint64_t k=1;k*n<=X;k++){ uint32_t v=(uint32_t)a[k*n]+a[k]; if(v>0xFFFFu){sat=1;v=0xFFFFu;} a[k*n]=(uint16_t)v; }
      uint32_t pr[2]={(uint32_t)n,(uint32_t)m}; fwrite(pr,4,2,fg);
    }
    uint64_t an=a[n]; N+=an;
    if(an>maxa){maxa=an;maxan=n;}
    int64_t E=den*N - num*(int64_t)(n-1) - den;      /* den*(N(n) - rho(n-1) - 1) */
    if(E>recE){ recE=E; if(n>=1000 && (double)E/den > 30.0) printf("recE n=%llu E=%.1f a_n=%llu\n",(unsigned long long)n,(double)E/den,(unsigned long long)an); }
    if(n==pw){ printf("N(%llu)=%lld  g-prime sites=%llu  max a_n=%llu at n=%llu  sup E=%.1f\n",(unsigned long long)n,(long long)N,(unsigned long long)ngp,(unsigned long long)maxa,(unsigned long long)maxan,(double)recE/den); pw*=10; }
  }
  if(fa){ fwrite(a,2,X+1,fa); fclose(fa); }
  fclose(fg);
  printf("done X=%llu sites=%llu totalmult=%llu maxa=%llu at %llu sat=%d\n",(unsigned long long)X,(unsigned long long)ngp,(unsigned long long)nmult,(unsigned long long)maxa,(unsigned long long)maxan,sat);
  return 0;
}
