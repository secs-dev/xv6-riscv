#include "kernel/types.h"
#include "user/user.h"

void test0();
void test1();
void test2();
void test3();
void periodic();
void work(int ticks);

volatile static int count;
static int failed = 0;

int
main(int argc, char *argv[])
{
  test0();
  test1();
  test2();
  test3();

  if(failed == 0)
    printf("\nall alarm checks passed\n");
  else
    printf("\n%d alarm checks failed\n", failed);

  exit(failed != 0);
}

void
periodic()
{
  count++;
  sigreturn();
}

void
work(int ticks)
{
  int start = uptime();

  while(uptime() - start < ticks){
    for(volatile int i = 0; i < 100000; i++){
      asm volatile("nop");
    }
  }
}

void
test0()
{
  int before;

  printf("test0 start\n");

  count = 0;
  sigalarm(1, periodic);
  work(10);

  sigalarm(0, 0);
  before = count;

  work(10);

  if(before == 0){
    printf("test0 failed: alarm was never called\n");
    failed++;
  } else if(count != before){
    printf("test0 failed: alarm called after disable\n");
    failed++;
  } else {
    printf("test0 passed\n");
  }
}

void
test1()
{
  int result;

  printf("test1 start\n");

  sigalarm(0, 0);
  result = sigreturn();

  if(result == -1){
    printf("test1 passed\n");
  } else {
    printf("test1 failed: expected -1, got %d\n", result);
    failed++;
  }
}

void
test2()
{
  int pid;
  int status;

  printf("test2 start\n");

  for(int i = 0; i < 5; i++){
    pid = fork();

    if(pid < 0){
      printf("test2 failed: fork failed\n");
      failed++;
      return;
    }

    if(pid == 0){
      sigalarm(1, periodic);
      exit(0);
    }

    status = -1;
    if(wait(&status) != pid || status != 0){
      printf("test2 failed: first child failed\n");
      failed++;
      return;
    }

    pid = fork();

    if(pid < 0){
      printf("test2 failed: second fork failed\n");
      failed++;
      return;
    }

    if(pid == 0){
      count = 0;

      work(10);

      if(count != 0){
        printf("test2 failed: old alarm was called\n");
        exit(1);
      }

      exit(0);
    }

    status = -1;
    if(wait(&status) != pid || status != 0){
      printf("test2 failed: alarm state was reused\n");
      failed++;
      return;
    }
  }

  printf("test2 passed\n");
}

void
test3()
{
  int before;
  int after;

  printf("test3 start\n");

  count = 0;
  sigalarm(100, periodic);

  work(6);
  before = count;

  sigalarm(2, periodic);

  work(24);
  after = count;

  sigalarm(0, 0);

  if(before != 0){
    printf("test3 failed: alarm called too early\n");
    failed++;
  } else if(after < 2){
    printf("test3 failed: new interval not applied\n");
    failed++;
  } else {
    printf("test3 passed\n");
  }
}
