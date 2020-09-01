#include <stdlib.h>
#include <string.h>

void strxchg(char *s1, char *s2) {
    char *temp = malloc(sizeof(char)*(strlen(s1) + 1));
    for(int i = strlen(s1) - 1; i >= 0; i--){
        temp[strlen(s1) - i - 1] = s1[i];
    }
    temp[strlen(s1)] = '\0';
    for(int i = strlen(s2)-1; i >= 0; i--){
        s1[strlen(s2) - i - 1] = s2[i];
    }
    s1[strlen(s2)] = '\0';
    strcpy(s2, temp);
    free(temp);
}