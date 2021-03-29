using System.Collections;
using System.Collections.Generic;
public class Primes
{
   public static IEnumerable<int> Stream()
   {
       yield return 2;
       List<int> primes = new List<int>();
       int current_number = 3;
       while(true){
           bool is_prime = true;
           foreach(int prime in primes){
               if(prime * prime > current_number){
                   break;
               }
               if(current_number % prime == 0){
                   is_prime = false;
                   break;
               }
           }
           if(is_prime){
               primes.Add(current_number);
               yield return current_number;
           }
           current_number += 2;
       }
   }
}