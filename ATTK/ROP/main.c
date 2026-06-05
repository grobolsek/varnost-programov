#include <stdio.h>
#include <unistd.h>

void win(long a, long b)
{
	char secret[64];

	if (a == 0xdeadbeef)
	{
		FILE *f = fopen("/flag.txt", "r");
		fgets(secret, 64, f);
	}

	if (b == 0xbadc0de)
	{
		puts(secret);
	}
}

int main()
{
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);

	char buffer[32];
	gets(buffer);

  return 0;
}
