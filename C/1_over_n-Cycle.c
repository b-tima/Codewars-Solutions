#include <stdio.h>
#include <stdlib.h>

#define atoi my_own_function

int my_own_function(char *str){
    int result = 0;
    while(*str != '\0'){
        result = 10 * result + (*(str++) - '0');
    }
    return result;
}

int cycle(int n){
    if(n % 2 == 0 || n % 5 == 0){
        return -1;
    }
    int numDigits = 1;
    for(int mod = 10 % n; mod != 1; numDigits++){
        mod = 10 * mod % n;
    }
    return numDigits;
}

int main(int argc, char **argv){
    if(argc != 2){
        printf("Invalid argument\n");
        return 0;
    }

    int n = atoi(argv[1]);

    int result = cycle(n);

    printf("n = %i, count = %i\n", n, result);

    return 0;
}
