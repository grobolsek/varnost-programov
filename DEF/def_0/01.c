#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
  if (argc != 2) {
    printf("There must be 2 argumnets");
    return 1;
  }

	// Get name
	char* name = malloc(128);
	printf("Enter your name: ");
	fgets(name, 128, stdin);
	printf("Hello, %s!\n", name);

	// Open file
	FILE *input = fopen(argv[1], "r");
  if (input == NULL) {
    perror("Error opening file");
    return 1;
  }

	// Get file size
	if (fseek(input, 0, SEEK_END) < 0) {
    perror("Error seeking file");
    return 1;
  }
	long size = ftell(input);
  if (size < 0) {
    perror("Error getting file size");
    return 1;
  }
	if (fseek(input, 0, SEEK_SET)) {
    perror("Error seeking file");
    return 1;
  }
	if (size > (long)10*1024*1024*1024) // size > 10GB
	{
		printf("File too large!\n");
		return 1;
	}

	// Read file
	long len = 0;
	if (fscanf(input, "%ld", &len) != 1) {
    printf("Error reading file!\n");
    return 1;
  }
  if (len < 0 || len > 100000) {
    printf("File must be between 0 and 100000\n");
    return 1;
  }

	// Read data and calculate statistics
	int sum = 0;
	int* entries = malloc(len * sizeof(int));
	for (int i = 0; i < len; i++)
	{
		if (fscanf(input, "%d", &entries[i])) {
      printf("Error reading file\n");
      return 1;
    }
		sum += entries[i];
	}
	int avg = sum / len;
	printf("Average: %d\n", avg);

	// Do stuff!
	int entry = 0;
	for (int i = 0; i < 10; i++)
	{
		printf("Select entry: ");
		if (scanf(" %d", &entry) != 1) {
      printf("Error reading input\n");
      return 1;
    }
    if ( entry < 0 || entry > len) {
      return 1;
    }
		printf("Entry %d: %d\n", entry, entries[entry]);
		printf("Modify entry: ");
		if (scanf(" %d", &entries[entry]) != 1) {
      printf("Error reading entries\n");
      return 1;
    }
	}

	// Greet and exit
	printf("Goodbye, %s!\n", name);
	return 0;
}
