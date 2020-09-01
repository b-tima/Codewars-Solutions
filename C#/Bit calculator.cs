using System;
using System.Linq;

public class Kata
{
    public static int Calculate(string num1, string num2)
    {
      int x = 0;
      int y = 0;
      for (int i = 0; i < num1.Length; i++)
        x += string.Join("", num1.Reverse())[i] == '1' ? (int)Math.Round(Math.Pow(2, i)) : 0;
      for (int i = 0; i < num2.Length; i++)
        y += string.Join("", num2.Reverse())[i] == '1' ? (int)Math.Round(Math.Pow(2, i)) : 0;
      return x + y;
    }
}