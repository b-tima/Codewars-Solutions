using System;
using System.Collections.Generic;

public class Kata
{
    public static string ToCamelCase(string str)
    {
      List<string> result = new List<string>();
      var splitted = str.Split(new char[2] { '_', '-' });
      for (int i = 0; i < splitted.Length; i++)
      {
        if (i == 0)
        {
          result.Add(splitted[0]);
          continue;
        }
        result.Add(Capitalize(splitted[i]));
      }
      return string.Join(string.Empty, result);
    }

    public static string Capitalize(string str) => str[0].ToString().ToUpper() + str.Substring(1).ToLower();
}