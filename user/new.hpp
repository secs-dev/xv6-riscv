#ifndef NEW_HPP
#define NEW_HPP

extern "C" {
#include "kernel/types.h"

//

#include "user/user.h"
}

using size_t = unsigned long;

void *operator new(size_t n);
void operator delete(void *p);

void *operator new[](size_t n);
void operator delete[](void *p);

inline void *operator new(size_t, void *p) noexcept { return p; }
inline void operator delete(void *, void *) noexcept {}

#endif /* NEW_HPP */