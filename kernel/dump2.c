#include "kernel/defs.h"
#include "kernel/proc.h"
#include "kernel/riscv.h"
#include "kernel/spinlock.h"
#include <stdbool.h>

extern struct proc proc[NPROC];

static bool isProcessViewable(int viewer_pid, struct proc *target_proc) {
  const int target_pid = target_proc->pid;

  const int target_parent_pid =
      target_proc->parent == 0 ? -1 : target_proc->parent->pid;

  return target_pid == viewer_pid || target_parent_pid == viewer_pid;
}

uint64 sys_dump2(void) {
  static const uint64 access_denied_code = -1;
  static const uint64 invalid_process_code = -2;
  static const uint64 invalid_register_code = -3;
  static const uint64 invalid_memory_code = -4;

  struct proc *viewer = myproc();

  int target_pid;
  int target_register;
  uint64 return_value;

  argint(0, &target_pid);
  argint(1, &target_register);
  argaddr(2, &return_value);

  if (target_register < 2 || target_register > 11) {
    return invalid_register_code;
  }

  struct proc *target;

  for (target = proc; target < &proc[NPROC]; target++) {
    acquire(&target->lock);

    if (target->pid == target_pid) {
      goto process_found;
    }

    release(&target->lock);
  }

  return invalid_process_code;

process_found:
  uint64 register_value;
  uint64 return_code = 0;

  if (viewer != target) {
    acquire(&viewer->lock);
  }

  if (!isProcessViewable(viewer->pid, target)) {
    return_code = access_denied_code;
    goto release_and_return;
  }

  register_value = (&target->context.s2)[target_register - 2];

  if (copyout(viewer->pagetable, return_value, (char *)&register_value,
              sizeof(register_value)) < 0) {
    return_code = invalid_memory_code;
  }

release_and_return:
  if (viewer != target) {
    release(&viewer->lock);
  }

  release(&target->lock);
  return return_code;
}