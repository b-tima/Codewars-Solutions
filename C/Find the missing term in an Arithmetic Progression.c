#include <stddef.h>
#include <stdlib.h>

int find_missing(const int *nums, size_t n){
    int k = *(nums + 1) - *(nums), lastK;
    for(int i = 1; i < n - 1; i++){
        lastK = k;
        k = *(nums + i + 1) - *(nums + i);
        if(abs(k) < abs(lastK)) return *(nums + i - 1) + k;
        if(i + 2 == n) return *(nums + i) + lastK;

    }
    return *nums;
}