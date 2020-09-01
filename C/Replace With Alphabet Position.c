#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

char *alphabet_position(char *text) {
    size_t len = strlen(text);
    char *result = malloc((len * 3 + 1) * sizeof(char));
    *result = '\0';
    for(int i = 0; i < len; i++){
        if(isalpha(*(text + i))){
            char a = isupper(*(text + i)) ? 'A' : 'a';
            char buffer[3];
            sprintf(buffer, "%i ", *(text + i) - a + 1);
            strcat(result, buffer);
        }
    }
    *(result + strlen(result) - 1) = '\0';
    return result;
}