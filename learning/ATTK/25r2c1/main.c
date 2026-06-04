#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setup() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
}

char *envget(const char *name, char *envp[]) {
  for (int i = 0; envp[i] != NULL; i++) {
    if (strncmp(envp[i], name, strlen(name)) == 0 && envp[i][strlen(name)] == '=') {
      return envp[i] + strlen(name) + 1;
    }
  }
  return NULL;
}

void cat() {
  char line[256];
  while (fgets(line, sizeof(line), stdin)) {
    printf(line);
  }
}

int main(int argc, char *argv[], char *envp[])
{
	setup();
  char *flag = envget("FLAG", envp);
  cat();
  return 0;
}
