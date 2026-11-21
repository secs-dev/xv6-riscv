#include "kernel/types.h"
#include "user/user.h"


int sendMessage(int fd[], int nfd, char message[], int cntByte) {
	int n = write(fd[nfd], message, cntByte);
	return n;
}

void readMessage(int nfd, char *buf) {
	int total = 0;
	while (total < 4) {
		int n = read(nfd, buf + total, 4 - total);
		if (n <= 0) {
			exit(1);
		}
		total += n;
	}

	buf[4] = '\0';

}
	
int main() {
	int proc0[2];
	int proc1[2];

	if (pipe(proc0) < 0 || pipe(proc1) < 0) {
		exit(1);
	}

	int pid = fork();

	if (pid > 0) {

		char buf[5];

		close(proc0[0]);
		close(proc1[1]);

        	

		if (sendMessage(proc0, 1, "ping", 4) != 4) {
			exit(1);
		}
		
		close(proc0[1]);

		readMessage(proc1[0], buf);
		printf("%d: %s\n", getpid(), buf);	

		close(proc1[0]);
		wait(0);
		

	} else if(pid == 0) {
		char buf[5];
		

		close(proc0[1]);
		close(proc1[0]);
		
		readMessage(proc0[0], buf);
		printf("%d: %s\n", getpid(), buf);

   		 close(proc0[0]);
		
		if (sendMessage(proc1, 1, "pong", 4) != 4) {
			exit(1);
		}
		
		close(proc1[1]);


	
	
	} else {
		exit(1);
	}
	exit(0);
}
