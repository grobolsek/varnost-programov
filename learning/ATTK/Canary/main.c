#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void win()
{
  system("/bin/sh");
}

int main()
{
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);

  char name[64];
  char correct = 'n';
  while (correct != 'y') {
    printf("Please enter your name:\n");
    read(0, name, 0x64);
    printf("Hello, %s", name);
    printf("Is this name correct [y/n]?\n");
		correct = getchar();
		getchar(); // newline
  }

  printf("Welcome, %s! Enjoy the challenge.\n", name);
  return 0;
}
