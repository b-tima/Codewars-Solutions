#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

bool comp(const int *a, const int *b, size_t n){
    bool found;
    int *bcpy = malloc((n + 1) * sizeof(int));
    memcpy(bcpy, b, n * sizeof(int));
    for(int i = 0; i < n; i++){
        found = false;
        for(int j = 0; j < n; j++){
            if(*(a + i) * *(a + i) == *(bcpy + j)){
                *(bcpy + j) = -1;
                found = true;
                break;
            }
        }
        if(!found){
            free(bcpy);
            return false;  
        }
    }
    free(bcpy);
    return true;
}