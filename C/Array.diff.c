#include <stdlib.h>
#include <stdint.h>

int *array_diff(const int *arr1, size_t n1, const int *arr2, size_t n2, size_t *z) {
    int *result = malloc(n1*sizeof(int));
    for(uint8_t i = 0; i < n1; i++){
        uint8_t found = 0;
        int currentValue = *(arr1 + i);
        for(uint8_t j = 0; j < n2; j++){
            if(currentValue == *(arr2 + j)){
                found = 1;
            }
        }
        if(!found){
            *(result + *z) = currentValue;
            *z += 1;
        }
    }
    return result;
}