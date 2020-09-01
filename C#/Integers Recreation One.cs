using System;
using System.Collections.Generic;

public class SumSquaredDivisors 
{
    public static string listSquared(long n, long m)
    {
      List<string> returnList = new List<string>();
      for(long i = n; i <= m; i++)
      {
        long value = 0;
        List<long> preList = new List<long>() { i };
        for (long j = 1; j < i; j++)
          if (i % j == 0)
            preList.Add(j);
        foreach (long j in preList)
          value += (long)Math.Pow(j, 2);
        if (Math.Sqrt(value) % 1 == 0)
          returnList.Add($"[{i}, {value}]");
      }
      if (returnList.Count < 1)
        return "[]";
      string returnValue = "";
      for(int i = 0; i < returnList.Count; i++)
      {
        if (i == 0)
          returnValue += "[";
        returnValue += returnList[i];
        if(i == returnList.Count - 1)
        {
          returnValue += "]";
          break;
        }
        returnValue += ", ";
      }
      return returnValue;
    }
}