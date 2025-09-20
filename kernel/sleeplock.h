#ifndef KERNEL_SLEEPLOCK_H
#define KERNEL_SLEEPLOCK_H

#include "kernel/types.h"
#include "kernel/spinlock.h"

// Long-term locks for processes
struct sleeplock {
  uint locked;       // Is the lock held?
  struct spinlock lk; // spinlock protecting this sleep lock
  
  // For debugging:
  char *name;        // Name of lock.
  int pid;           // Process holding lock
};

#endif /* KERNEL_SLEEPLOCK_H */