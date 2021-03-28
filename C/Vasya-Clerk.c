#include <stdlib.h>

#include <stdio.h>

int tickets(size_t length, const int people[]) {
    int buffer = 0;
    for(int i = length - 1; i >= 0; i--){
        printf("buffer = %i\n", buffer);
        if(buffer > 0 && people[i] != 100){
            buffer -= people[i];
            printf("n = %i, people[i] = %i, buffer = %i\n", i, people[i], buffer);
            /*if(buffer < 0){
                return 0;
            }*/
        }
        buffer += people[i] - 25;
    }
    return buffer == 0 ? 1 : 0;
}

int main(){
    size_t length = 5;
    int queue[10] = {25, 25, 50, 50, 100};

    printf("succes == %i\n", tickets(length, queue));

    return 0;
}
