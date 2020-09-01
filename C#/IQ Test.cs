using System;
using System.Linq;
using System.Collections.Generic;

public class IQ
    {
    public static int Test(string numbers)
    {
      var splitted = numbers.Split(' ');
      List<int> values = new List<int>();
      foreach (string i in splitted)
        values.Add(Convert.ToInt32(i));
      List<Tuple<int, bool>> dicValues = new List<Tuple<int, bool>>();
      foreach(int i in values)
      {
        if (i % 2 == 0)
          dicValues.Add(new Tuple<int, bool>(values.IndexOf(i), true));
        else
          dicValues.Add(new Tuple<int, bool>(values.IndexOf(i), false));
      }
      if (dicValues.Count(x => !x.Item2) > dicValues.Count(x => x.Item2))
        return dicValues.Single(x => x.Item2 == true).Item1+1;
      else
        return dicValues.Single(x => x.Item2 == false).Item1+1;
    }
    }