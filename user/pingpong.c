#include "../kernel/types.h"
#include "user.h"

int main() {
    int p[2];
    char buf[5];

    if (pipe(p) < 0) {
        printf("pingpong: ошибка создания pipe\n");
        exit(1);
    }

    if (fork() == 0) {
        // Дочерний процесс
        int n = read(p[0], buf, 4);
        if (n == 0) {
            printf("%d: pipe закрыт, данных нет\n", getpid());
        } else {
            buf[4] = '\0';
            printf("%d: получил %s\n", getpid(), buf);
            write(p[1], "pong", 4);
        }
        close(p[0]);
        close(p[1]);
        exit(0);
    } else {
        // Родительский процесс
        if (write(p[1], "ping", 4) < 0) {
            printf("%d: ошибка записи в закрытый pipe\n", getpid());
        }
        wait(0);
        close(p[1]);
        int n = read(p[0], buf, 4);
        if (n == 0) {
            printf("%d: pipe закрыт, данных нет\n", getpid());
        } else {
            buf[4] = '\0';
            printf("%d: получил %s\n", getpid(), buf);
        }        
        close(p[0]);
        exit(0);
    }
}