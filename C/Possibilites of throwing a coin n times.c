#include <stdlib.h>
#include <math.h>

char *coin(int n) {
    char *result = malloc(n * pow(2, n) * (n - 1) * sizeof(char));
    int i;
    for (i = 0; i < pow(2, n); i++) {
        for (int j = 0; j < n; j++) {
            if ((i & (int)pow(2, n - j - 1)) == (int)pow(2, n - j - 1)) {
                result[i*(n + 1) + j] = 'T';
            }
            else {
                result[i*(n + 1) + j] = 'H';
            }
        }
        result[i*(n + 1) + n] = ',';
    }
    result[--i*(n + 1) + n] = '\0';
    return result;
}