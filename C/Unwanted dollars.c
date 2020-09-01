#include <math.h>

double money_value(char s[]) {
    double result = 0;
    int point = 0, decimal = 0, negative = 0;
    for (s; *s != '\0'; s++) {
        if (*s >= '0' && *s <= '9')
            result = result*(decimal ? 1 : 10) + (*s - '0')*pow(10, point -= decimal);
        else if (*s == '-')
            negative = 1;
        else if (*s == '.')
            decimal = 1;
    }
    return negative ? -result : result;
}