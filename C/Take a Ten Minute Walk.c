#include <stdbool.h>
#include <string.h>
#include <stdio.h>

bool isValidWalk(const char *walk) {
    if(strlen(walk) != 10) return false;
    int grid[2] = {0, 0};
    for(int i = 0; i < 10; i++){
        switch (*(walk + i))
        {
            case 'n':
                grid[0]++;
                break;
            case 's':
                grid[0]--;
                break;
            case 'e':
                grid[1]++;
                break;
            case 'w':
                grid[1]--;
                break;
        }
    }
    return grid[0] == 0 && grid[1] == 0;
}