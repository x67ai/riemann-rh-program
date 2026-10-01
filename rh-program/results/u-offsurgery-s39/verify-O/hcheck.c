/* hcheck.c -- max of (|E(n)|+1)/n^th and |C(n)|/n^th over windows, from the a16 array (rho = 4/5) (read-O, S40) */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
int main(int argc,char**argv){
  int fd=open(argv[1],O_RDONLY); off_t sz=lseek(fd,0,SEEK_END); const uint16_t *a=mmap(0,sz,PROT_READ,MAP_SHARED,fd,0); uint64_t X=sz/2-1;
  double th[3]={0.30,0.32,0.35}; double mE[3]={0},mEtop[3]={0},mC[3]={0}; uint64_t amE[3]={0}; int64_t N=1; uint64_t low=0;
  for(uint64_t n=2;n<=X;n++){ int64_t Nprev=N; N+=a[n];
    double Eprev=(double)Nprev-0.8*(n-1)-0.2; if(Eprev<=0.3+1e-12) low++;
    if(n<1000) continue; double E=(double)N-0.8*n-0.2, C=(double)N-0.8*n;
    for(int i=0;i<3;i++){ double d=pow((double)n,th[i]); double v=(fabs(E)+1)/d; if(v>mE[i]){mE[i]=v;amE[i]=n;} if(n>=100000000 && v>mEtop[i]) mEtop[i]=v; double c=fabs(C)/d; if(c>mC[i]) mC[i]=c; } }
  for(int i=0;i<3;i++) printf("theta %.2f: max_{1e3..1e9}(|E|+1)/n^th = %.4f at n=%llu; top decade %.4f; max |C(n)|/n^th = %.4f\n",th[i],mE[i],(unsigned long long)amE[i],mEtop[i],mC[i]);
  printf("fraction of n<=1e9 with E(n-1) <= 0.3: %.5f\n",(double)low/(X-1)); return 0; }
