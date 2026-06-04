#include <stdio.h>
#include <stdlib.h>

int main()
{
    long len = 0;
    printf("Number of measurements:\n");
    scanf("%ld", &len);
    int* mems = malloc(4 * len);
    for (int i = 0; i < len; i++)
        scanf("%d", &mems[i]);
    int min = mems[0], max = mems[0];
    for (int i = 1; i < len; i++) {
        if (mems[i] < min)
            min = mems[i];
        if (mems[i] > max)
            max = mems[i];
    }
    printf("Min: %d, Max: %d\n", min, max);
    free(mems);
    return 0;
}
