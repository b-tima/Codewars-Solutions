#include <string.h>

typedef unsigned long long ull;

unsigned long long* productFib(ull prod) {
  ull *fib_buffer = malloc(3*sizeof(ull));
  *fib_buffer = 1;
  *(fib_buffer + 1) = 1;
  *(fib_buffer + 2) = 0;
  
  while((*fib_buffer)*(*(fib_buffer + 1)) <= prod){
  
    if ((*fib_buffer)*(*(fib_buffer + 1)) == prod){
      *(fib_buffer + 2) = 1;
      break;
    }
    
    ull temp = *(fib_buffer + 1);
    *(fib_buffer + 1) = *(fib_buffer + 1) + *fib_buffer;
    *fib_buffer = temp;
  }  

  return fib_buffer;
}