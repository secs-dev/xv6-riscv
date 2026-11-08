#include "kernel/types.h"
#include "user/user.h"

static void
readn(int fd, char *buf, int n)
{
  int got = 0;
  while (got < n) {
    int r = read(fd, buf + got, n - got);
    if (r <= 0) {
      fprintf(2, "pingpong: read error\n");
      exit(1);
    }
    got += r;
  }
}

static void
writen(int fd, char *buf, int n)
{
  if (write(fd, buf, n) != n) {
    fprintf(2, "pingpong: write error\n");
    exit(1);
  }
}

int
main(void)
{
  int p2c[2]; 
  int c2p[2]; 
  char buf[5];

  if (pipe(p2c) < 0 || pipe(c2p) < 0) {
    fprintf(2, "pingpong: pipe failed\n");
    exit(1);
  }

  int pid = fork();
  if (pid < 0) {
    fprintf(2, "pingpong: fork failed\n");
    exit(1);
  }

  if (pid == 0) {

    close(p2c[1]);
    close(c2p[0]);

    readn(p2c[0], buf, 4);
    buf[4] = 0;
    printf("%d: got %s\n", getpid(), buf);

    writen(c2p[1], "pong", 4);

    close(p2c[0]);
    close(c2p[1]);
    exit(0);
  } else {

    close(p2c[0]);
    close(c2p[1]);

    writen(p2c[1], "ping", 4);

    readn(c2p[0], buf, 4);
    buf[4] = 0;
    printf("%d: got %s\n", getpid(), buf);

    close(p2c[1]);
    close(c2p[0]);
    wait(0);
    exit(0);
  }
}