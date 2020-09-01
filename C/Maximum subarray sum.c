#include <stddef.h>

int maxSequence(const int* array, size_t n) {
    if (n == 0) return 0;
    int sum = 0;
    int maxSum = 0;
    int maxSumi = 0;

    // Find max
    for(int i = 0; i < n; i++){
        sum += *(array + i);
        if(sum > maxSum){
            maxSum = sum;
            maxSumi = i;
        }
    }

    // Find max again.
    sum = 0;
    maxSum = 0;
    for(int i = maxSumi; i >= 0; i--){
        sum += *(array + i);
        if(sum > maxSum){
            maxSum = sum;
            maxSumi = i;
        }
    }

    return maxSum;
}