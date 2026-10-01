/* mkbits.c -- bitset of the g-primes <= 10^9 of S5(4/5) from gpF_r08_1e9.u32 (pairs (q, m_q)); bit q set iff q is a g-prime. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(int c,char**v){ FILE*f=fopen(v[1],"rb"); uint64_t L=1000000000ULL; uint8_t*b=calloc(L/8+1,1); uint32_t pr[2]; uint64_t n=0;
 while(fread(pr,4,2,f)==2){ if(pr[1]!=1){fprintf(stderr,"m!=1 at %u\n",pr[0]);return 1;} b[pr[0]>>3]|=1<<(pr[0]&7); n++; }
 FILE*o=fopen(v[2],"wb"); fwrite(b,1,L/8+1,o); fclose(o); printf("bits set: %llu\n",(unsigned long long)n); return 0; }
