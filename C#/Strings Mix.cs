using System.Collections.Generic;
using System.Linq;

public class Mixing 
{
    public static string Mix(string s1, string s2)
    {
      Dictionary<char, string> results = new Dictionary<char, string>();
      string str1 = string.Join("", s1.Replace(" ", ""));
      string str2 = string.Join("", s2.Replace(" ", ""));
      foreach(char c in str1 + str2)
      {
        if (!char.IsLetter(c) || char.IsUpper(c)) continue;
        int valueStr1 = str1.Count(x => x == c);
        int valueStr2 = str2.Count(x => x == c);
        if (valueStr1 <= 1 && valueStr2 <= 1) continue;
        if (valueStr1 == valueStr2 && !results.ContainsKey(c)) results.Add(c, $"=:{new string(c, valueStr1)}");
        else if (valueStr1 > valueStr2 && !results.ContainsKey(c)) results.Add(c, $"1:{new string(c, valueStr1)}");
        else if (!results.ContainsKey(c)) results.Add(c, $"2:{new string(c, valueStr2)}");
      }
      return string.Join("/", results.Values.OrderBy(x => -x.Length).ThenBy(x => x[0]).ThenBy(x => x[2]));
    }
}