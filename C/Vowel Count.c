#include <stddef.h>

size_t get_count(const char *s){
    char vowels[5] = "aeiou";
    int count = 0;
    while(1){
        for(int i = 0; i < 5; i++)
            if(*s == vowels[i])
                count++;
        if(*s == '\0')
            break;
        *s++;
    }
    return count;
}