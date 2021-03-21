#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

typedef struct State
{
    int if_zero;
    int if_one;
    int output;
} State;

typedef struct Fsm
{
    // States are 'numbered' in the order they are placed in list
    // that is, S1 is in index 0, S2 is in index 0 etc.
    State *states;
} Fsm;

int getNum(const char *instr){
    // Returns one less then found integer value
    int state = 0;
    for(int n = 0; isnum(instr[n]); n++){
        state = state*10 + (instr[n] - '0');
    }
    return state - 1;
}

Fsm *compile(const char *instructions)
{
    // FIX!
    Fsm *const fsm = NULL;

    // Initialize states
    int numStates = 0;
    for (int i = 0; instructions[i]; i++)
        if (instructions[i] == '\n')
            numStates++;
    fsm->states = malloc((numStates + 1) * sizeof(State));

    char *buffer = malloc(2 * sizeof(char));

    bool state_def = true;
    bool next_output = false;
    bool zero_def = false;
    bool one_def = false;
    bool output_def = false;

    int numOfStates = 0;

    for (int i = 0; instructions[i] != '\0'; i++)
    {
        // Check stuff
        switch (instructions[i])
        {
        case ' ':
            continue;
        case '\n':
            state_def = true;
            continue;
        case ';':
            if (next_output)
                output_def = true;
            else
                zero_def = true;
            continue;
        case ',':
            one_def = true;
            continue;
        }

        // Do stuff
        if(state_def){
            numOfStates++;
            state_def = false;
        }
        else if(zero_def){
            next_output = true;

            fsm->states[numOfStates].if_zero = getNum(instructions + i + 1);
            zero_def = false;
        }
        else if(one_def){
            fsm->states[numOfStates].if_one = getNum(instructions + i + 1);
            one_def = false;
        }
        else if(output_def){
            fsm->states[numOfStates].output = getNum(instructions) + 1;
        }
    }
    return fsm;
}

int run_fsm(const Fsm *fsm, const char *start, const _Bool *input, const size_t len_input,
            const char **final_state, const char **path)
{
    // Return: final_state_value
    // Return by reference: final_state, path (memory is preallocated)
    // State name `const char *`s should be somewhere in your `Fsm`
    // TODO: run_fsm

    int start_state = getNum(start + 1);

    State currentState = fsm->states[start_state];

    for(int i = 0; i < len_input; i++){
        currentState = input[i] ? fsm->states[currentState.if_one] : fsm->states[currentState.if_zero];
    }

    return -1;
}

void free_fsm(Fsm *fsm)
{
    // TODO: free other things in free_fsm
    free(fsm);
}
