#include "user/new.hpp"

void *operator new(size_t n) { return malloc(n); }

void operator delete(void *p) { free(p); }

void *operator new[](size_t n){
    return malloc(n);
}

void operator delete[](void *p)
{
    return free(p);
}