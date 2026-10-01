#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
int main(){ uint64_t X=2000000000ULL; uint8_t *c=calloc(X/16+1,1); /* bit for odd i: index i/2 */
 for(uint64_t i=3;i*i<=X;i+=2) if(!(c[i>>4]&(1<<((i>>1)&7)))) for(uint64_t j=i*i;j<=X;j+=2*i) c[j>>4]|=1<<((j>>1)&7);
 uint64_t cnt=1, at1e9=0, at5e8=0; for(uint64_t i=3;i<=X;i+=2){ if(!(c[i>>4]&(1<<((i>>1)&7)))) cnt++; if(i==499999999) at5e8=cnt; if(i==999999999) at1e9=cnt; }
 printf("pi(5e8)=%llu pi(1e9)=%llu pi(2e9)=%llu diff(2e9-1e9)=%llu\n",(unsigned long long)at5e8,(unsigned long long)at1e9,(unsigned long long)cnt,(unsigned long long)(cnt-at1e9)); return 0; }
