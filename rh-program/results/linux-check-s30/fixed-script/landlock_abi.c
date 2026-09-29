#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/landlock.h>
int main(void){ long v = syscall(SYS_landlock_create_ruleset, NULL, 0, LANDLOCK_CREATE_RULESET_VERSION);
  if (v < 0) { perror("landlock_create_ruleset"); return 1; } printf("Landlock ABI version supported by this kernel: %ld\n", v); return 0; }
