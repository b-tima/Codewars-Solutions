#include <stdbool.h>
#include <ctype.h>

#define alpha_len 26

bool is_pangram(const char *str_in) {
    const char *alphabet = "abcdefghijklmnopqrstuvwxyz";
    bool found[alpha_len] = {false};
    int index = 0;
    while (str_in[index] != '\0'){
        bool foundAll = true;
        for (int i = 0; i < alpha_len; i++){
            if(str_in[index] == alphabet[i] || tolower(str_in[index]) == alphabet[i]){
                found[i] = true;
            }
            if(!found[i]){
                foundAll = false;
            }
        }
        if(foundAll){
            return true;
        }
        index++;
    }
    return false;
}