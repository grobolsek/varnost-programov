#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/landlock.h>
#include <fcntl.h>
#include <sys/prctl.h>
#include <seccomp.h>

#ifndef O_PATH
#define O_PATH 010000000
#endif

int main(int argc, char *argv[])
{
	if (argc < 2) {
		fprintf(stderr, "Usage: %s <program> <args...>\n", argv[0]);
		return 1;
	}

	// TODO: Protect program from running external programs
  scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_KILL);
  if (ctx == NULL) {
    perror("seccomp_init");
    return 1;
  }
  seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(arch_prctl), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(brk), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(execve), 0, SCMP_A0(SCMP_CMP_EQ, (scmp_datum_t)argv[1]));
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(fstat), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(getrandom), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(mprotect), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(openat), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(prlimit64), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(readlinkat), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(rseq), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(set_robust_list), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(set_tid_address), 0);
seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);  seccomp_load(ctx);

	// TODO: Protect program from opening files outside of the current directory
	

	// TODO: Apply protections
	

	// Run the program
	execv(argv[1], &argv[1]);
	perror("execv");
	return 0;
}
