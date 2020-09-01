#include <string.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define M_PI 3.14159265358979323846

char* iterPi(double epsilon) {
    uint32_t times = 0;
    double pi_approx = 0.0;
    while(fabs((pi_approx * 4) - M_PI) > epsilon){
        pi_approx += pow(-1, times) * ((double) 1 / (2 * times + 1));
        times++;
    }
    char *result = malloc(20);
    *result = '\0';
    char *times_str = malloc(5);
    char *pi_str = malloc(11);
    sprintf(times_str, "%i", times);
    sprintf(pi_str, "%.10f", pi_approx * 4);
    strcat(result, "[");
    strcat(result, times_str);
    strcat(result, ", ");
    strcat(result, pi_str);
    strcat(result, "]");
    return result;
}