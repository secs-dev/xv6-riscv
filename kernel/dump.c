#include "kernel/proc.h"
#include "kernel/defs.h"

uint64 sys_dump(void) {
  struct proc *p = myproc();
  struct trapframe *trap_frame = p->trapframe;

  for (uint i = 0; i < 10; ++i) {
    printf("s%u = %d\n", i + 2, (int)(&trap_frame->s2)[i]);
  }

  return 0;
}