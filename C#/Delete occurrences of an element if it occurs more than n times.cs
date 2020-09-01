using System;
using System.Collections.Generic;
using System.Linq;

public class Kata {
    public static int[] DeleteNth(int[] arr, int x)
    {
      List<int> returnValues = new List<int>();
      foreach (int i in arr)
        if (returnValues.Count(y => y == i) < x)
          returnValues.Add(i);
      return returnValues.ToArray();
    }
}