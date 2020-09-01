#include <stdlib.h>
#include <ctype.h>

char *camel_case(const char *s)
{
    char *result = malloc(100);
    char word = 1;
    int i = 0, offset = 0;
    while(*(s + i)){
        if(isspace(*(s + i))){
            word = 1;
            offset++;
        }else if(word){
            *(result + i - offset) = toupper(*(s + i));
            word = 0;
        }else
            *(result + i - offset) = *(s + i);
        i++;
    }
    *(result + i - offset) = '\0';
    return result;
}