#include <stdbool.h>
#include <stdint.h>

bool alphanumeric(const char* strin) {
    const char allowedChars[37] = "abcdefghijklmnopqrstuvwxyz0123456789";
    // if the string is empty
    if(*strin == '\0') return false;
    bool valid = false;
    while(*strin != '\0'){
        for(uint8_t i = 0; i < 37; i++){
            if( *strin == allowedChars[i]
                || (i < 27 && *strin == allowedChars[i] - 32)){
                    valid = true;
                    break;
            }
        }
        if(valid){
            strin++;
            valid = false;
        }else{
            return false;
        }
    }

    return true;
}