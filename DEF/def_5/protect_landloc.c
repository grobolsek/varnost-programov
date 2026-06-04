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

  struct landlock_ruleset_attr ruleset_attr = {
    .handled_access_fs =
        LANDLOCK_ACCESS_FS_EXECUTE |
        LANDLOCK_ACCESS_FS_WRITE_FILE |
        LANDLOCK_ACCESS_FS_READ_FILE |
        LANDLOCK_ACCESS_FS_READ_DIR |
        LANDLOCK_ACCESS_FS_REMOVE_DIR |
        LANDLOCK_ACCESS_FS_REMOVE_FILE |
        LANDLOCK_ACCESS_FS_MAKE_CHAR |
        LANDLOCK_ACCESS_FS_MAKE_DIR |
        LANDLOCK_ACCESS_FS_MAKE_REG |
        LANDLOCK_ACCESS_FS_MAKE_SOCK |
        LANDLOCK_ACCESS_FS_MAKE_FIFO |
        LANDLOCK_ACCESS_FS_MAKE_BLOCK |
        LANDLOCK_ACCESS_FS_MAKE_SYM |
        LANDLOCK_ACCESS_FS_REFER |
        LANDLOCK_ACCESS_FS_TRUNCATE |
        LANDLOCK_ACCESS_FS_IOCTL_DEV |
        LANDLOCK_ACCESS_FS_RESOLVE_UNIX,
    .handled_access_net =
        LANDLOCK_ACCESS_NET_BIND_TCP |
        LANDLOCK_ACCESS_NET_CONNECT_TCP,
    .scoped =
        LANDLOCK_SCOPE_ABSTRACT_UNIX_SOCKET |
        LANDLOCK_SCOPE_SIGNAL,
};

	// TODO: Protect program from opening files outside of the current directory
	

	// TODO: Apply protections
	

	// Run the program
	execv(argv[1], &argv[1]);
	perror("execv");
	return 0;
}
