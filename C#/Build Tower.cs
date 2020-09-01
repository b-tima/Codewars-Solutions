using System;

public class Kata
{
    public static string[] TowerBuilder(int nFloors)
    {
      string[] returnValue = new string[nFloors];
      for (int i = 0; i < nFloors; i++)
        returnValue[i] = new string(' ', (nFloors - 1) * 2).Insert((nFloors - i) - 1, new string('*', i * 2 + 1)).Remove((nFloors - 1) * 2 + 1, 2 * i);
      return returnValue;
    }
}