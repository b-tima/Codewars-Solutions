using System;

public class Persist 
{
    public static int Persistence(long n)
    {
      int steps = 0;
      string currentStr = n.ToString();
      while (true)
      {
        if (currentStr.Length < 2)
          return steps;
        int currentValue = 1;
        foreach (char c in currentStr)
          currentValue *= int.Parse(c.ToString());
        currentStr = currentValue.ToString();
        steps++;
      }
    }
}