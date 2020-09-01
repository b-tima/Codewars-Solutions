using System;
using System.Numerics;

public static class Kata
{
    public static string sumStrings(string a, string b)
    {
      BigInteger x, y;
      BigInteger.TryParse(a, out x);
      BigInteger.TryParse(b, out y);
      return (x + y).ToString();
    }
}