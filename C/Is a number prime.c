#include <stdbool.h>
#include <math.h>

bool is_prime(int num){
    if(num <= 3) return num > 1;
    if(num % 2 == 0) return false;
    if(num % 3 == 0) return false;
    int i = 5;
    while(pow(i, 2) <= num){
        if(num % i == 0) return false;
        i += 2;
    }
    return true;
}