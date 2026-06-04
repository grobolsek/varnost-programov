#include <stdio.h>
#include <unistd.h>

int main()
{
  setvbuf(stdin, NULL, _IONBF, 0);
  setvbuf(stdout, NULL, _IONBF, 0);
  setvbuf(stderr, NULL, _IONBF, 0);
	
	char flag[64];
	char *flagptr = flag;
	FILE *fp = fopen("flag.txt", "r");
	fgets(flag, 64, fp);
	fclose(fp);

	char buffer[32];
	printf("Yell: ");
	fgets(buffer, 32, stdin);
	printf("An echo is heard in the distance: ...\n");
	printf(buffer);

  return 0;
}
