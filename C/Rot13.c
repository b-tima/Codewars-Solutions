#include <stdlib.h>
#include <string.h>
#include <stddef.h>
#include <ctype.h>

char *rot13(const char *src){
    size_t len = strlen(src);
    char *result = malloc((len + 1) * sizeof(char));
    for(int i = 0; i < len; i++){
        char workingChar = *(src + i);
        if(isalpha(workingChar)){
            char z = isupper(workingChar) ? 'Z' : 'z';
            char a = isupper(workingChar) ? 'A' : 'a';
            *(result + i) = workingChar + 13 <= z ? workingChar + 13 : a + ((workingChar + 13) % z) - 1;
        }else{
            *(result + i) = workingChar;
        }
    }
    *(result + len) = '\0';
    return result;
}