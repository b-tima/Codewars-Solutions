#include <math.h>

int bouncingBall(double h, double bounce, double window) {
    if( bounce <= 0
        || bounce >= 1
        || window >= h
        || h <= 0) return -1;
    return 2 * floor(log(window/h)/log(bounce)) + 1;
}