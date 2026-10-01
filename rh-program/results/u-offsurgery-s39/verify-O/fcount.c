/* fcount.c -- exact count of factorizations of n into the g-primes of a .gp list (read-O, Session 40, claim C3).
   f(n) = #{multisets of listed g-primes (with multiplicity m_q as distinct copies) with product n}, by an unbounded-knapsack
   DP over the mixed-radix divisor lattice of n. Since S5's rule never removes a g-prime, f(n) <= a_n for every n, and for
   n <= max(list) with every g-prime < n listed, f(n) = a_n exactly.  usage: fcount file.gp "2^5*3^3*5^4*7*..." */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#define MAXK 40
int K; uint64_t pr[MAXK]; int E[MAXK]; uint64_t stride[MAXK+1];
int main(int argc,char**argv){
  if(argc<3){fprintf(stderr,"usage\n");return 1;}
  /* parse spec */
  char *s=strdup(argv[2]); K=0; for(char *tok=strtok(s,"*"); tok; tok=strtok(0,"*")){ char *c=strchr(tok,'^'); pr[K]=strtoull(tok,0,10); E[K]=c?atoi(c+1):1; K++; }
  double l10=0; for(int i=0;i<K;i++) l10+=E[i]*log10((double)pr[i]);
  stride[0]=1; for(int i=0;i<K;i++) stride[i+1]=stride[i]*(uint64_t)(E[i]+1);
  uint64_t Lsz=stride[K]; fprintf(stderr,"lattice %llu entries, log10 n = %.4f\n",(unsigned long long)Lsz,l10);
  uint64_t *f=calloc(Lsz,8); if(!f){fprintf(stderr,"alloc\n");return 1;} f[0]=1;
  FILE *fp=fopen(argv[1],"rb"); uint32_t q; uint8_t m; uint64_t nq=0, nmult=0; int ovf=0;
  int v[MAXK], e[MAXK];
  while(fread(&q,4,1,fp)==1 && fread(&m,1,1,fp)==1){
    uint64_t t=q; int ok=1; for(int i=0;i<K;i++){ v[i]=0; while(t%pr[i]==0){ t/=pr[i]; v[i]++; } if(v[i]>E[i]){ok=0;break;} }
    if(!ok || t!=1) continue;
    nq++; nmult+=m; uint64_t off=0; for(int i=0;i<K;i++) off+=v[i]*stride[i];
    for(int c=0;c<m;c++){
      /* odometer over the sub-box e_i in [v_i, E_i], coordinate 0 fastest => increasing index order */
      for(int i=0;i<K;i++) e[i]=v[i];
      for(;;){
        uint64_t base=0; for(int i=1;i<K;i++) base+=e[i]*stride[i];
        for(int x=v[0]; x<=E[0]; x++){ uint64_t d=base+x; uint64_t a=f[d], b=f[d-off]; uint64_t sum=a+b; if(sum<a) ovf=1; f[d]=sum; }
        int i=1; while(i<K){ if(++e[i]<=E[i]) break; e[i]=v[i]; i++; } if(i>=K) break;
      }
    }
  }
  fclose(fp);
  uint64_t top=f[Lsz-1];
  printf("n = %s  log10 n = %.4f  dividing g-primes = %llu (copies %llu)  f(n) = %llu  log f/log n = %.5f  overflow = %d\n",
    argv[2], l10, (unsigned long long)nq, (unsigned long long)nmult, (unsigned long long)top, log10((double)top)/l10, ovf);
  return 0;
}
