#include <stdio.h>
#include <stdlib.h>

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
  printf("What's your name? ");
  gets(name);
  printf("Hello, %s!\n", name);
  return 0;
}
