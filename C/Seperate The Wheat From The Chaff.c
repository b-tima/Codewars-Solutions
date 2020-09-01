#include <stdlib.h>
#include <stdbool.h>

long long *wheat_from_chaff(const long long *values, unsigned count) {
    long long *result = malloc(sizeof(long long) * count);
    unsigned left = 0, right = count - 1;
    bool foundLeft = false, foundRight = false;
    while (left <= right && right != -1 && left < count) {
        if (values[left] > 0) {
            foundLeft = true;
        }
        else {
            result[left] = values[left];
            left++;
        }
        if (values[right] < 0) {
            foundRight = true;
        }
        else {
            result[right] = values[right];
            right--;
        }
        if (foundLeft && foundRight) {
            foundLeft = false;
            foundRight = false;
            result[left] = values[right];
            result[right] = values[left];
            left++;
            right--;
        }
    }
    return result;
}