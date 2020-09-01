#include <stdbool.h>

int getSize(char *str){
    int size = 0;
    while(*str != '\0'){
        size++;
        str++;
    }
    return size;
}

bool solution(const char *string, const char *ending){
    if(getSize(string) < getSize(ending)) return false;
    string += getSize(string) - getSize(ending);

    while(*string != '\0'){
        if(*string != *ending){
            return false;
        }
        string++;
        ending++;
    }
    return true;
}