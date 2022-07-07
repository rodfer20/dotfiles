#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int dup2(int fildes, int fildes2);

struct subprocess {
  pid_t pid;
  int stdin;
  int stdout;
  int stderr;
};

void close_c(int fd) {
  if (close(fd) == -1) { perror("Could not close pipe end" ); exit(1); }
}

void mk_pipe(int fds[2]) {
  if (pipe(fds) == -1) { perror("Could not create pipe"); exit(1); }
}

void mv_fd(int fd1, int fd2) {
  if (dup2(fd1,  fd2) == -1) { perror("Could not duplicate pipe end"); exit(1); }
  close(fd1);
}

// Start program at argv[0] with arguments argv.
// Set up new stdin, stdout and stderr.
// Puts references to new process and pipes into `p`.
void call(char* argv[], struct subprocess * p) {
  int child_in[2]; int child_out[2]; int child_err[2];
  pipe(child_in); pipe(child_out); pipe(child_err);
  pid_t pid = fork();
  if (pid == 0) {
    close_c(0); close_c(1); close_c(2);                                 // close parent pipes
    close_c(child_in[1]); close_c(child_out[0]); close_c(child_err[0]); // unused child pipe ends
    mv_fd(child_in[0], 0); mv_fd(child_out[1], 1); mv_fd(child_err[1], 2);
    char* envp[] = { NULL };
    execve(argv[0], argv, envp);
  } else {
    close_c(child_in[0]); close_c(child_out[1]); close_c(child_err[1]); // unused child pipe ends
    p->pid = pid;
    p->stdin = child_in[1];   // parent wants to write to subprocess child_in
    p->stdout = child_out[0]; // parent wants to read from subprocess child_out
    p->stderr = child_err[0]; // parent wants to read from subprocess child_err
  }
}
