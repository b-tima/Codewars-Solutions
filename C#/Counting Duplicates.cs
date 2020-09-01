using System;
using System.Linq;

public class Kata
{
  public static int DuplicateCount(string str)
    => str.GroupBy(x => x.ToString().ToLower()).Where(x => x.Count() > 1).Count();
}