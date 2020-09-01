using System;
using System.Numerics;

public class SumFct
{
    public static BigInteger perimeter(BigInteger n)
    {
      BigInteger x = 1;
      BigInteger y = 1;
      BigInteger z = 0;
      for(int i = 0; i < n + 1; i++)
      {
        z = x + y;
        x = y;
        y = z;
      }
      return z * 4 - 4;
    }
}